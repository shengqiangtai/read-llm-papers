# LLM paper audit checklist

Load the relevant parts of this checklist during Pass 3. Do not turn every item into prose. Report only issues that affect the paper's claims.

## Model and training papers

- Are data sources, filtering, deduplication, and licenses disclosed?
- Could benchmark data or near-duplicates enter pretraining, continued training, or synthetic data?
- Are token count, model size, architecture, optimizer, schedule, and compute sufficiently specified?
- Are comparisons matched for data, parameters, training tokens, and inference budget?
- Does an ablation isolate each proposed component?
- Are gains stable across model sizes, seeds, and task families?

## Post-training and reasoning

- Is the base model identical across comparisons?
- Are teacher models, reward models, verifiers, and sampling budgets disclosed?
- Could gains come from more generated tokens, retries, tools, or test-time compute?
- Are reward hacking, format compliance, and benchmark-specific tuning separated from real reasoning gains?
- Does the evaluation assume that generated chain-of-thought is faithful? If so, is that assumption tested?

## Agents and tool use

- Are tools, environment, memory, prompts, failure recovery, and maximum steps specified?
- Are baselines given the same tools, observations, and action budget?
- Are success rates averaged over enough independent runs?
- Are latency, token use, API cost, and failure modes reported?
- Could benchmark leakage occur through web search, repository access, or memorized solutions?

## Retrieval and long context

- Are corpus, chunking, retriever, reranker, and indexing choices controlled?
- Does the comparison match total context and retrieved-token budgets?
- Are retrieval quality and answer quality measured separately?
- Are citation correctness and source entailment checked, not merely citation presence?
- Is the long-context task resistant to position bias and answer-string matching?

## Evaluation and LLM judges

- Is the metric aligned with the claimed capability?
- Are prompts, decoding settings, and exact model versions reported?
- If an LLM judge is used, is order bias, self-preference, verbosity bias, and judge agreement examined?
- Is human evaluation large enough, blinded where possible, and accompanied by agreement measures?
- Are confidence intervals, variance, or significance tests shown when differences are small?
- Are failed cases and subgroup results available, or only an aggregate mean?

## Benchmarks and datasets

- Is the target construct defined clearly enough to know what the benchmark measures?
- Are annotation procedure, quality control, demographics, and exclusions described?
- Are train, validation, and test items independent?
- Can superficial cues or answer-format artifacts solve the task?
- Are contamination checks appropriate for public LLMs?
- Does the benchmark distinguish capability from prompt following and memorization?

## Multimodal work

- Are image, video, and audio resolutions or sampling rates matched across baselines?
- Can text-only shortcuts solve the task?
- Are perception errors separated from reasoning errors?
- Do qualitative examples represent typical performance rather than selected successes?
- Are generated-media metrics complemented by human or task-based evaluation?

## Efficiency and systems

- Is accuracy measured at matched hardware, batch size, precision, and serving conditions?
- Are preprocessing, communication, memory, and compilation costs included?
- Is throughput reported together with latency and quality?
- Does the method remain useful outside the authors' hardware scale?

## Reproducibility status

Record whether each item is available, promised, partial, or absent:

- source code
- training code
- evaluation code
- prompts and configurations
- checkpoints
- datasets
- environment or dependency lock
- license
- compute description

Judge reproduction difficulty from the missing critical item, not from repository appearance.
