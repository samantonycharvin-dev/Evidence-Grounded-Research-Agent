# Sources and Provenance

This project uses a small controlled corpus of public research sources related to Retrieval-Augmented Generation (RAG), RAG evaluation, citations, adaptive retrieval, and corrective retrieval.

The prototype corpus contains curated summaries of the sources rather than complete paper text.

## Source Register

| ID | Source | Year | Topic | Original / Public URL |
|---|---|---:|---|---|
| S01 | Evaluation of Retrieval-Augmented Generation: A Survey | 2024 | RAG evaluation | https://arxiv.org/abs/2405.07437 |
| S02 | ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | 2024 | RAG evaluation | https://aclanthology.org/2024.naacl-long.20/ |
| S03 | RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation | 2024 | RAG diagnostics | https://arxiv.org/abs/2408.08067 |
| S04 | Enabling Large Language Models to Generate Text with Citations | 2023 | Citation generation | https://aclanthology.org/2023.emnlp-main.398/ |
| S05 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | 2024 | Adaptive retrieval | https://arxiv.org/abs/2310.11511 |
| S06 | Corrective Retrieval Augmented Generation | 2024 | Corrective retrieval | https://arxiv.org/abs/2401.15884 |

## How the Sources Were Used

### S01 — RAG Evaluation Survey

Used to provide background on evaluating both retrieved context and generated answers, including relevance and support by retrieved evidence.

### S02 — ARES

Used for the prototype's understanding of context relevance, answer faithfulness, and answer relevance as RAG evaluation dimensions.

### S03 — RAGChecker

Used to support the distinction between retrieval-side and generation-side weaknesses and claim-level diagnostic evaluation.

### S04 — Citation Generation

Included as part of the broader research corpus concerning evidence traceability and citation-supported generation.

### S05 — Self-RAG

Included as evidence concerning adaptive retrieval and reflection/critique mechanisms.

### S06 — Corrective RAG

Included as evidence concerning evaluating retrieved documents and taking corrective action when initial retrieval is inadequate.

## Provenance Rules

The benchmark was designed as an independent technical experiment.

- Public research sources were used as the evidence basis.
- No employer or client data was used.
- Source summaries in `data/corpus.json` were curated for this controlled prototype.
- The project does not reproduce benchmark questions from external datasets.
- External research was used to inform methodology and evidence selection.
- The prototype does not claim to reproduce the original results of the cited papers.
- Results reported in this repository are results produced by this project.

## Important Corpus Limitation

The corpus is intentionally small and consists of curated source summaries rather than complete papers.

Therefore, an agent claim being supported by the prototype corpus means:

> The claim is supported by the evidence representation available to the agent.

It does not necessarily mean that the claim exhaustively represents everything stated in the original paper.

## AI-Assisted Development

AI tools were used for coding assistance, debugging, explanations, and implementation support.

The project architecture, research question, evaluation design, benchmark structure, experimental decisions, execution, interpretation, and final validation were reviewed by the author.

No employer or client information was used as training or evaluation data.