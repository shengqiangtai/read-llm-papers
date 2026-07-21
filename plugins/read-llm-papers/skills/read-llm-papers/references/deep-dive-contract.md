# Deep-dive report contract

Use this structure when the user asks for derivations, implementation details, appendix analysis, or a reproduction plan. Spend depth on the requested issue instead of expanding every section equally.

## 1. Scope and answer

State the exact question being answered, the inspected paper version, and a short answer. List any missing source or artifact that limits confidence.

## 2. Required background

Define only the concepts needed for the requested detail. Separate paper-specific terminology from standard terminology. State the paper's assumptions before using them.

## 3. Mechanism or derivation

For a method explanation:

1. define inputs, outputs, and state
2. trace data through the components
3. explain the objective or feedback signal
4. separate training-time and inference-time behavior
5. identify the claimed source of improvement

For a derivation, define every symbol, show the important intermediate steps, and state where an equality depends on an assumption. Add a small sanity check or limiting case when useful.

## 4. Paper-to-implementation map

Use a compact mapping when code is requested:

| Paper concept | Code object | Shape or type | Role |
| --- | --- | --- | --- |

Then give the smallest useful pseudocode or code skeleton. Mark each implementation choice as one of:

- specified by the paper
- verified in official code
- analyst recommendation
- unknown

Do not invent omitted hyperparameters or silently replace an unavailable component.

## 5. Focused evidence audit

Trace each important claim to its exact experiment, ablation, figure, table, or appendix. Check whether the evidence isolates the proposed mechanism. Include alternative explanations, variance, evaluator bias, data leakage, and unmatched compute only when they affect the requested question.

## 6. Reproduction plan

Provide:

1. required data, models, code, licenses, and external services
2. preprocessing and environment assumptions
3. a minimal smoke test
4. the full training or evaluation sequence
5. checkpoints and expected intermediate signals
6. success criteria and failure diagnostics
7. known and unknown compute requirements

Keep estimates labeled and show their basis.

## 7. Remaining uncertainty

End with the strongest supported conclusion, the most important unresolved detail, and the next source, experiment, or code path to inspect. Do not repeat the whole five-minute report unless the user asks for both.
