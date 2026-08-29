# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### ILLUME: Rationalizing Vision-Language Models through Human Interactions.
- **链接**: [出版页](https://proceedings.mlr.press/v202/brack23a.html)
- **作者**: Manuel Brack, Patrick Schramowski, Björn Deiseroth, Kristian Kersting
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Distilling Internet-Scale Vision-Language Models into Embodied Agents.
- **链接**: [arXiv:2301.12507](https://arxiv.org/abs/2301.12507)
- **作者**: Theodore R. Sumers, Kenneth Marino, Arun Ahuja, Rob Fergus, Ishita Dasgupta
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instruction-following agents must ground language into their observation and action spaces. Learning to ground language is challenging, typically requiring domain-specific engineering or large quantities of human interaction data. To address this challenge, we propose using pretrained vision-language models (VLMs) to supervise embodied agents. We combine ideas from model distillation and hindsight experience replay (HER), using a VLM to retroactively generate language describing the agent's behavior. Simple prompting allows us to control the supervision signal, teaching an agent to interact with novel objects based on their names (e.g., planes) or their features (e.g., colors) in a 3D rendered environment. Fewshot prompting lets us teach abstract category membership, including pre-existing categories (food vs toys) and ad-hoc ones (arbitrary preferences over objects). Our work outlines a new and effective way to use internet-scale VLMs, repurposing the generic language grounding acquired by such models to teach task-relevant groundings to embodied agents.

</details>

## 跨领域论文（完整笔记在其他领域）

- Open-VCLIP: Transforming CLIP to an Open-vocabulary Video Model via Interpolated Weight Optimization. → [open-set-detection](../open-set-detection/Guideline%202023.md)
