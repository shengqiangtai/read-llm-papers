# Read LLM Papers Skill

[English](README.md)

这是一个面向 Codex 和 ChatGPT 的开源论文阅读 Skill。它会把大模型前沿论文整理成有证据、可判断、约五分钟读完的精读报告，适合每天关注 Hugging Face Daily Papers，但阅读时间有限的研究者。

## 主要能力

- 先筛选一整天的 Hugging Face Daily Papers，再决定精读哪些论文
- 阅读论文全文，而不是把摘要改写得更长
- 检查核心方法图、主结果表、消融实验、局限和附录
- 区分实验事实、作者主张、分析判断和未知信息
- 检查数据污染、基线公平性、LLM 裁判偏差、测试时计算量和复现条件
- 默认生成五分钟精读报告，也支持多论文比较和技术深挖
- 支持 Hugging Face、arXiv、OpenReview、DOI、论文标题和上传的 PDF

## 作为 Plugin 安装

先添加这个 GitHub 仓库：

```bash
codex plugin marketplace add shengqiangtai/read-llm-papers-skill
```

然后在 ChatGPT 桌面端打开插件目录，选择 **Read LLM Papers**，完成安装。

## 只安装 Skill

安装到个人 Codex 环境：

```bash
git clone https://github.com/shengqiangtai/read-llm-papers-skill.git
mkdir -p "$HOME/.agents/skills"
cp -R read-llm-papers-skill/plugins/read-llm-papers/skills/read-llm-papers "$HOME/.agents/skills/"
```

如果只想在某个项目中使用，可以把同一文件夹复制到该项目的 `.agents/skills/read-llm-papers`。

## 使用示例

精读单篇论文：

```text
$read-llm-papers 分析这篇论文，生成一份五分钟中文精读报告：
https://huggingface.co/papers/2607.13124
```

筛选每日论文：

```text
$read-llm-papers 帮我筛选今天的 Hugging Face Daily Papers。
我主要关注大模型后训练、推理、社会智能和评测，请精读最值得看的两篇。
```

比较两篇论文：

```text
$read-llm-papers 比较这两篇论文。先统一模型规模、训练数据、测试集、推理预算和代码开放情况，再判断结果。
```

在 ChatGPT 中，可以从输入框选择这个 Skill。如果当前界面支持 Skill 提及，也可以使用 `@` 选择它。

## 默认报告内容

1. 三十秒结论和阅读建议
2. 论文版本及官方代码、模型和数据
3. 研究问题、已有缺口和核心方法
4. 真正的新意和已有方法组合
5. 主要结论与证据表
6. 优点、局限和其他可能解释
7. 复现难度
8. 三个要点，以及最值得打开的一张图或一张表

当来源允许时，关键结论会标注对应的章节、图、表、附录或官方仓库链接。

## 验证修改

```bash
python3 scripts/validate.py
```

## 许可证

MIT
