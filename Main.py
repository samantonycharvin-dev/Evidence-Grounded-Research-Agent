from typing import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field

from retriever_logic import retrieve_evidence


# --------------------------------------------------
# 1. Shared state
# --------------------------------------------------

class ResearchState(TypedDict):
    question: str
    evidence: list
    answer: str
    verification: dict
    retry_count: int


# --------------------------------------------------
# 2. Structured verification schemas
# --------------------------------------------------

class ClaimCheck(BaseModel):
    claim: str = Field(description="A factual claim made in the answer")
    supported: bool = Field(
        description="Whether the retrieved evidence directly supports the claim"
    )
    reason: str = Field(
        description="Why the evidence supports or does not support the claim"
    )
    source_ids: list[str] = Field(
        description="Source IDs supporting the claim"
    )


class VerificationResult(BaseModel):
    claims: list[ClaimCheck]


# --------------------------------------------------
# 3. Gemini
# --------------------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

verifier_model = model.with_structured_output(VerificationResult)


# --------------------------------------------------
# 4. Retrieve evidence
# --------------------------------------------------

def retrieve(state: ResearchState):

    evidence = retrieve_evidence(
        state["question"]
    )

    return {
        "evidence": evidence
    }


# --------------------------------------------------
# 5. Generate answer
# --------------------------------------------------

def answer_question(state: ResearchState):

    evidence_text = "\n\n".join(
        f"[{source['source_id']}] {source['text']}"
        for source in state["evidence"]
    )

    prompt = f"""
You are a research assistant.

Answer the research question using ONLY the evidence provided.

Research question:
{state["question"]}

Evidence:
{evidence_text}

Rules:
1. Do not use outside knowledge.
2. Every factual claim should have a source citation such as [S01].
3. If evidence is insufficient, explicitly say so.
4. Do not invent information.
"""

    response = model.invoke(prompt)

    return {
        "answer": response.text
    }


# --------------------------------------------------
# 6. Verify claims
# --------------------------------------------------

def verify_claims(state: ResearchState):

    evidence_text = "\n\n".join(
        f"[{source['source_id']}] {source['text']}"
        for source in state["evidence"]
    )

    prompt = f"""
You are an evidence verification system.

Research question:
{state["question"]}

Generated answer:
{state["answer"]}

Retrieved evidence:
{evidence_text}

Extract the important factual claims.

For each claim:
1. Determine whether the retrieved evidence directly supports it.
2. Use supported=true only when evidence supports it.
3. Use supported=false when evidence does not support it.
4. Explain your reasoning.
5. Identify supporting source IDs.
6. Do not use outside knowledge.
"""

    verification = verifier_model.invoke(prompt)

    return {
        "verification": verification.model_dump()
    }


# --------------------------------------------------
# 7. Conditional routing
# --------------------------------------------------

def route_after_verification(state: ResearchState):

    claims = state["verification"]["claims"]

    # If there are no claims, treat the result as insufficient.
    if not claims:
        return "refine"

    all_supported = all(
        claim["supported"]
        for claim in claims
    )

    # Allow one refinement attempt.
    if all_supported:
        return "final"

    if state["retry_count"] < 1:
        return "refine"

    return "final"


# --------------------------------------------------
# 8. Refinement node
# --------------------------------------------------

def refine_research(state: ResearchState):

    return {
        "retry_count": state["retry_count"] + 1
    }


# --------------------------------------------------
# 9. Build graph
# --------------------------------------------------

builder = StateGraph(ResearchState)

builder.add_node("retrieve", retrieve)
builder.add_node("answer_question", answer_question)
builder.add_node("verify_claims", verify_claims)
builder.add_node("refine", refine_research)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "answer_question")
builder.add_edge("answer_question", "verify_claims")

builder.add_conditional_edges(
    "verify_claims",
    route_after_verification,
    {
        "final": END,
        "refine": "refine"
    }
)

builder.add_edge("refine", "retrieve")

graph = builder.compile()


# --------------------------------------------------
# 10. Run
# --------------------------------------------------

def run_agent(question: str):
    return graph.invoke({
        "question": question,
        "evidence": [],
        "answer": "",
        "verification": {},
        "retry_count": 0
    })


if __name__ == "__main__":
    result = run_agent("How is RAG evaluated?")

    print("\nRetrieved sources:")
    for source in result["evidence"]:
        print(
            f"- {source['source_id']}: "
            f"{source['title']}"
        )

    print("\nAnswer:")
    print(result["answer"])

    print("\nClaim verification:")
    for claim in result["verification"]["claims"]:
        print(f"\nClaim: {claim['claim']}")
        print(f"Supported: {claim['supported']}")
        print(f"Reason: {claim['reason']}")
        print(f"Sources: {claim['source_ids']}")

    print(f"\nRefinement attempts: {result['retry_count']}")