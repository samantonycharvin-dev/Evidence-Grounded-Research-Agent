# Final Prototype Results

## Experiment

Evidence-Grounded Research Agent

The prototype evaluated whether a LangGraph-based research agent could generate claims that were supported by the evidence retrieved from a controlled RAG corpus.

## Prototype Benchmark Results

| Task | Category | Execution | Automated Verification | Human Audit |
|---|---|---|---|---|
| Q01 | Direct factual | Successful | 4/4 supported | 4/4 supported |
| Q03 | Multi-source synthesis | Successful | 4/4 supported | 4/4 supported |
| Q07 | Conflicting evidence | Successful in an earlier run | 4/4 supported | Detailed output unavailable for retrospective audit |
| Q09 | Insufficient evidence | Not completed | N/A | N/A |

### Summary

Three of the four prototype tasks were successfully executed.

Across those successful executions:

- 12 claims were generated.
- 12 claims were marked as supported by the automated verifier.
- Q01 and Q03 were independently human-audited: 8/8 claims were confirmed as supported by the retrieved evidence.
- Q07 also produced 4/4 supported claims according to the automated verifier, but its detailed successful output was overwritten by a later failed benchmark run and therefore was not independently audited.
- Q09 could not be completed because the Gemini API returned a temporary 503 model-availability error.

## Important Interpretation

The 12/12 automated support result should not be interpreted as 100% factual accuracy.

The primary metric demonstrated here is **evidence support / faithfulness**: whether generated claims were supported by the retrieved corpus evidence.

The experiment does not establish universal factual correctness, and the prototype corpus and benchmark are intentionally limited.

## External Execution Limitations

The benchmark experienced intermittent Gemini API availability and quota limitations during execution.

Q09 was therefore not completed.

No result was fabricated or inferred for the failed task.

## Scope

This was a controlled prototype experiment using a small curated corpus of public RAG research summaries. It is not a full-paper benchmark or a production-grade RAG evaluation.