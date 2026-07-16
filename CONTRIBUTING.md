# Contributing

Contributions that improve reading accuracy, evidence quality, report clarity, or coverage of new LLM research areas are welcome.

## Before opening a pull request

1. Keep the core `SKILL.md` workflow concise.
2. Put detailed domain checks or report rules in `references/`.
3. Do not add claims that require one specific model or tool unless the workflow degrades safely without it.
4. Mark unavailable information as unknown instead of adding plausible defaults.
5. Run `python3 scripts/validate.py`.

When changing report behavior, include one realistic input paper and a short explanation of how the resulting report improved.
