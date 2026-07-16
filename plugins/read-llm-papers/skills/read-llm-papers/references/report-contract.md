# Five-minute report contract

Use this structure for single-paper mode. Combine adjacent sections when that improves flow, but preserve the information.

## 1. Thirty-second verdict

Start with:

- one sentence stating what the paper actually changes
- **Read recommendation:** deep read, scan, or skip for now
- **Best for:** the reader who benefits most
- **Confidence:** high, medium, or low, based on source access and evidence quality

Do not begin with a generic field overview.

## 2. Paper card

Include title, authors or organization, first public date, latest inspected version, venue status, paper link, and official code/model/data links. Say unavailable when an artifact cannot be verified.

## 3. Problem and gap

Answer in plain language:

1. What exact task or scientific question is studied?
2. Why do existing methods fail or cost too much?
3. What assumption does this paper change?

Keep background to what is needed to understand the new idea.

## 4. Core method

Give one mental model, then explain three to five steps. Cover:

- inputs and outputs
- new modules or data
- objective or feedback signal
- training stages
- inference-time behavior and cost

For a mathematical contribution, explain the key equation's purpose and variables. For a systems contribution, explain data movement, bottlenecks, and resource tradeoffs. For a benchmark, explain construction, contamination controls, metrics, and what capability is actually measured.

## 5. What is genuinely new

Separate:

- new scientific or algorithmic idea
- new engineering combination
- new dataset or evaluation
- scale-up of an existing approach

Give at most three contributions. Compare each to the closest prior approach when the paper supplies enough evidence.

## 6. Key evidence

Use a table with no more than four rows:

| Claim | Evidence | Compared with | Caveat |
| --- | --- | --- | --- |

Include exact values only when verified. Cite the table, figure, section, or appendix beside each value. Explain the most informative ablation, not every benchmark score.

## 7. Critical assessment

Give two or three strengths and two or three limitations. At least one limitation must come from inspecting the setup or results. Consider alternative explanations, baseline fairness, data leakage, judge bias, variance, compute, missing ablations, and generalization.

Never write vague limitations such as more experiments are needed without naming the missing experiment and why it matters.

## 8. Reproduction reality

State:

- code, weights, data, and license availability
- stated or inferable hardware and compute
- hidden dependencies such as proprietary data, APIs, or judge models
- likely reproduction difficulty as low, medium, or high, with one reason

Do not invent compute estimates. Mark an estimate clearly and show its basis.

## 9. Reader takeaway

End with:

- three facts or ideas worth remembering
- the one figure, table, or section to inspect during a ten-minute follow-up
- one research question the paper leaves open

## Source list

List only sources actually used. Put the paper first, followed by official artifacts and then any secondary material. Use direct links.
