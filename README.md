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

## Data Safety & Compliance

- This project uses only synthetic and curated public research data.
- No client or company data is included.
- All sources are publicly available (arXiv, ACL Anthology, EMNLP).
- No personal identifiers, secrets, or credentials are stored in this repository.
- Dependencies are audited regularly for security vulnerabilities.
- GitHub Secret Protection and Push Protection are enabled to prevent accidental leaks.
