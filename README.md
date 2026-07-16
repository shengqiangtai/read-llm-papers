# Read LLM Papers Skill

[中文说明](README.zh-CN.md)

An open-source Codex and ChatGPT skill that turns frontier LLM papers into concise, evidence-grounded reading reports. It is designed for researchers who follow Hugging Face Daily Papers but have only a few minutes for each paper.

## What it does

- Triages a full Hugging Face Daily Papers list before spending time on full texts.
- Reads the full paper instead of expanding the abstract.
- Inspects the main method figure, results table, ablations, limitations, and appendix.
- Separates verified findings, author claims, analyst assessments, and unknowns.
- Audits data contamination, baseline fairness, LLM-judge bias, test-time compute, and reproducibility.
- Produces a default five-minute report, with optional comparison and deep-dive modes.
- Works with Hugging Face, arXiv, OpenReview, DOI pages, paper titles, and uploaded PDFs.

## Install as a plugin

Add this repository as a marketplace source:

```bash
codex plugin marketplace add shengqiangtai/read-llm-papers-skill
```

Then open the plugin directory in the ChatGPT desktop app, choose the **Read LLM Papers** marketplace, and install the plugin.

## Install only the skill

For a user-wide Codex installation:

```bash
git clone https://github.com/shengqiangtai/read-llm-papers-skill.git
mkdir -p "$HOME/.agents/skills"
cp -R read-llm-papers-skill/plugins/read-llm-papers/skills/read-llm-papers "$HOME/.agents/skills/"
```

For one repository, copy the same skill folder to `.agents/skills/read-llm-papers` inside that repository.

## Use it

Explicit invocation in Codex:

```text
$read-llm-papers Analyze https://huggingface.co/papers/2607.13124 as a five-minute reading report.
```

Daily triage:

```text
$read-llm-papers Triage today's Hugging Face Daily Papers. I care about post-training, model reasoning, social intelligence, and evaluation. Deep-read the best two papers.
```

Paper comparison:

```text
$read-llm-papers Compare these two papers. Normalize the model scale, data, benchmarks, inference budget, and artifact availability before judging the results.
```

In ChatGPT, select the bundled skill from the composer or mention it with `@` when that surface exposes skill mentions.

## Default report

The five-minute report includes:

1. A thirty-second verdict and reading recommendation
2. Paper identity and official artifacts
3. Problem, gap, and core method
4. Genuine novelty versus engineering combination
5. A compact claim-to-evidence table
6. Strengths, limitations, and alternative explanations
7. Reproduction difficulty
8. Three takeaways and the one figure or table worth opening

Reports are grounded in exact sections, figures, tables, appendices, and official repository pages whenever those sources are available.

## Repository structure

```text
.agents/plugins/marketplace.json
plugins/read-llm-papers/
├── .codex-plugin/plugin.json
└── skills/read-llm-papers/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
```

The plugin is only a distribution wrapper. The complete reading workflow lives in `SKILL.md`, while detailed report and audit rules are loaded only when needed.

## Validate changes

```bash
python3 scripts/validate.py
```

## Design influences

The workflow draws inspiration from [GPT Academic](https://github.com/binary-husky/gpt_academic), [ChatPaper](https://github.com/kaixindelele/ChatPaper), [PaperQA2](https://github.com/future-house/paper-qa), [STORM](https://github.com/stanford-oval/storm), [MinerU](https://github.com/opendatalab/MinerU), [Docling](https://github.com/docling-project/docling), and [Marker](https://github.com/datalab-to/marker). The implementation is original and does not include code from those projects.

## License

MIT
