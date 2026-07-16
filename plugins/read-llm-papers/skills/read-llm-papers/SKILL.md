---
name: read-llm-papers
description: Read, triage, explain, compare, and critically assess large-language-model and generative-AI research papers from Hugging Face Daily Papers, arXiv, OpenReview, conference sites, DOI pages, uploaded PDFs, or paper titles. Use for daily paper selection, five-minute paper reports, method and experiment explanations, novelty checks, reproducibility reviews, paper comparisons, or deciding whether a paper deserves close reading. Ground conclusions in the full paper and official artifacts, inspect figures and tables, distinguish evidence from author claims and inference, and produce concise reports in the user's language.
---

# Read LLM Papers

Turn a paper or a daily paper list into a decision-oriented, evidence-grounded reading report. Optimize for understanding and research judgment, not for replacing the abstract with a longer abstract.

## Choose the mode

- Use **single-paper mode** by default for one paper, PDF, link, DOI, or title. Produce the five-minute report.
- Use **daily-triage mode** when the user gives a Hugging Face Daily Papers page, a date, or several papers and asks what to read. Rank the list first. Deep-read only the requested papers or the best one to three.
- Use **comparison mode** when the user asks how papers differ. Normalize problem setting, data, model scale, baselines, metrics, and compute before comparing results.
- Use **deep-dive mode** only when the user explicitly asks for derivations, implementation details, appendix analysis, or a reproduction plan. Do not force the five-minute length limit in this mode.

If the user states interests, current projects, hardware, or reading goals, use them when judging relevance. Otherwise assume a technically literate graduate student who wants current LLM research.

## Acquire reliable sources

1. Resolve the exact paper identity. Record title, authors, date, version, venue status, and arXiv or DOI identifier. Do not merge similarly titled papers.
2. Open the Hugging Face paper page when it is the entry point, then obtain the full paper from arXiv, OpenReview, the publisher, or the uploaded PDF.
3. Prefer sources in this order:
   - user-provided full paper
   - official paper HTML or PDF
   - official code, model, dataset, and project pages
   - author or institution pages
   - reputable secondary discussion
4. Search for the official repository, released checkpoints, datasets, licenses, and later versions when these affect reproducibility or current relevance.
5. Treat the full paper as the source of truth for technical claims. Treat repository documentation as the source of truth for current artifact availability.

If only an abstract or summary is accessible, produce an **abstract-level preview**. State the limitation near the top and omit unsupported experimental or implementation detail.

Read [evidence-rules.md](references/evidence-rules.md) before analyzing a paper when sources conflict, the PDF is difficult to parse, or the answer will make strong novelty or performance claims.

## Read in passes

### Pass 1: Map the paper

Read the title, abstract, introduction, conclusion, section headings, limitations, the main method figure, and the main results table. Identify:

- the problem and why it matters
- the specific gap in prior work
- the proposed mechanism
- the strongest claimed result
- the intended scope and assumptions

### Pass 2: Reconstruct the argument

Read the related work, method, training objective, data construction, evaluation setup, ablations, and relevant appendix sections. Reconstruct the paper as:

`input and data → core components → training signal → inference procedure → measured outcome`

Explain the mechanism causally. Define each new term at first use. Use equations only when they change the reader's understanding. Explain symbols in plain language.

### Pass 3: Audit the evidence

For each major contribution, locate the exact experiment, ablation, figure, or analysis that supports it. Check whether the evidence establishes the claimed cause or only a correlation. Apply the domain checklist in [llm-paper-checklist.md](references/llm-paper-checklist.md).

Inspect the actual page image when figure, table, or equation extraction appears incomplete. Do not infer a chart's values from a caption alone.

## Run daily triage

Use the Hugging Face list only for first-pass selection. Do not treat upvotes as scientific quality.

Score each paper out of 100:

| Dimension | Points | Question |
| --- | ---: | --- |
| Relevance | 30 | Does it match the user's research, methods, or near-term work? |
| Novelty | 25 | Is the central idea meaningfully different from close prior work? |
| Evidence | 25 | Do the experiments appear broad, fair, and diagnostic? |
| Usability | 20 | Are code, models, data, or actionable ideas available? |

During triage, use title, abstract, metadata, and official artifacts. Mark the score as preliminary. Return a compact ranked table with one-line reasons and one of these actions:

- **Deep read** for the most valuable papers
- **Scan** for useful but nonessential papers
- **Skip for now** for weak relevance or weak evidence

Then perform full-text analysis only for the selected papers. Avoid spending deep-reading time on every item.

## Write the report

Read [report-contract.md](references/report-contract.md) and follow it for single-paper mode. Keep the default Chinese report around 1,200 to 1,800 Chinese characters, excluding the source list. Prefer a few dense sections over many shallow headings.

Use a compact table only when exact comparisons are easier to understand in rows. Explain the core method as a short sequence or a small diagram only when the structure truly benefits from it.

Write in the user's language. Keep established English names after their first Chinese explanation when this helps later searching.

## Compare papers fairly

Before comparing scores, align:

- benchmark version and split
- metric definition and evaluation protocol
- base model, parameter count, context length, and tool access
- training data and possible contamination
- inference budget, sampling count, search depth, and test-time compute
- baseline implementation and prompt quality

If these are not aligned, compare methods and tradeoffs rather than declaring a winner. State when a result is not directly comparable.

## Quality gate

Before answering, verify that:

- the report names the paper's real contribution rather than restating its topic
- every important number has a section, table, figure, or official artifact source
- the method explanation covers training and inference when both matter
- the strongest result includes the baseline and evaluation setting
- limitations include at least one issue inferred from the evidence, not only the authors' limitations section
- author claims, verified findings, and your own judgment are distinguishable
- missing information is labeled unknown instead of guessed
- the final verdict tells the reader whether and where to spend more time

If any check fails, revise the report before returning it.

## Handle follow-up questions

Reuse the resolved paper and evidence already gathered. For a follow-up about one equation, table, figure, or experiment, answer that item directly and cite its location. Expand only the relevant part rather than regenerating the entire report.
