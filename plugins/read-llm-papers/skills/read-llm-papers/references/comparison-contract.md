# Paper comparison contract

Use this structure for comparison mode. Compare papers against the user's decision, not against a generic leaderboard.

## 1. Decision summary

Start with:

- the question the comparison answers
- a one-sentence conclusion
- the best paper for each distinct reader goal
- confidence in the comparison

Name an overall winner only when the decisive evidence is directly comparable.

## 2. Identity and status

Use a compact table with one column per paper. Include title, inspected version, public date, venue status, and withdrawal, retraction, or errata status. Add official paper and artifact links.

## 3. Alignment matrix

Align these items before comparing results:

| Dimension | Paper A | Paper B | Comparable? |
| --- | --- | --- | --- |
| Task and claim |  |  |  |
| Base model and scale |  |  |  |
| Training data |  |  |  |
| Benchmark and split |  |  |  |
| Metric and evaluator |  |  |  |
| Inference budget |  |  |  |
| Hardware or compute |  |  |  |
| Released artifacts |  |  |  |

Use **Not reported** for missing facts and **Not comparable** for a real mismatch. Do not fill gaps with likely values.

## 4. Dimension-by-dimension comparison

Compare along the dimensions that matter to the request. Usually include:

1. problem framing and assumptions
2. core mechanism
3. genuine novelty relative to the closest prior work
4. evidence quality and diagnostic value
5. efficiency and deployment cost
6. reproducibility and practical usefulness

For each dimension, state the evidence first and then the judgment. Avoid giving every dimension equal space when one is decisive.

## 5. Comparable results

Show headline numbers only after alignment. Use one row per matched setting:

| Setting and metric | Paper A | Paper B | Interpretation |
| --- | ---: | ---: | --- |

Do not place unmatched headline scores in adjacent cells as if they form a contest. Explain differences in datasets, judges, prompts, tool access, sampling, or test-time compute beside the result.

## 6. Verdict and reader action

Use one of these forms:

- **Directly comparable:** “For [goal] under [matched setting], Paper A is the stronger choice because [evidence].”
- **Partly comparable:** “Paper A has stronger evidence for [claim], while Paper B is more useful for [different goal].”
- **Not directly comparable:** “There is no defensible overall winner because [specific mismatch]. Compare the methods and tradeoffs, not the headline scores.”

End with which paper to read first, the figure or table to inspect in each paper, and one experiment that would make the comparison fairer.

## Scale the format

For two or three papers, use the full matrix. For a larger set, first cluster papers by task or evaluation regime, then compare within clusters. Do not create an unreadable table with many sparse columns.
