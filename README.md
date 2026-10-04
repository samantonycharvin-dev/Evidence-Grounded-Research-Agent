# Evidence-Grounded Research Agent

A LangGraph-based research agent designed to test whether generated claims are actually supported by the evidence retrieved during research.

## Research Question

> Can an AI research agent produce an answer whose individual claims are actually supported by the evidence it retrieved?

The project focuses on **evidence grounding and claim-level verification**, rather than treating a fluent answer as automatically reliable.

---

## Architecture

```text
QUESTION
   ↓
RETRIEVE
   ↓
GENERATE ANSWER
   ↓
EXTRACT CLAIMS
   ↓
VERIFY CLAIMS
   ↓
SUPPORTED?
  ↙     ↘
YES      NO
 ↓        ↓
FINAL   REFINE
          ↓
       RETRIEVE