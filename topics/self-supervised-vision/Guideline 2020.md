# Self-supervised Vision — 2020 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### InfoGAN-CR and ModelCentrality: Self-supervised Model Training and Selection for Disentangling GANs.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lin20e.html)
- **作者**: Zinan Lin, Kiran Koshy Thekumparampil, Giulia Fanti, Sewoong Oh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Self-supervised Label Augmentation via Input Transformations.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lee20c.html)
- **作者**: Hankook Lee, Sung Ju Hwang, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Learning Compound Tasks without Task-specific Knowledge via Imitation and Self-supervised Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lee20f.html)
- **作者**: Sang-Hyun Lee, Seung-Woo Seo
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Automatic Shortcut Removal for Self-Supervised Representation Learning.
- **链接**: [arXiv:2002.08822](https://arxiv.org/abs/2002.08822)
- **作者**: Matthias Minderer, Olivier Bachem, Neil Houlsby, Michael Tschannen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In self-supervised visual representation learning, a feature extractor is trained on a "pretext task" for which labels can be generated cheaply, without human annotation. A central challenge in this approach is that the feature extractor quickly learns to exploit low-level visual features such as color aberrations or watermarks and then fails to learn useful semantic representations. Much work has gone into identifying such "shortcut" features and hand-designing schemes to reduce their effect. Here, we propose a general framework for mitigating the effect shortcut features. Our key assumption is that those features which are the first to be exploited for solving the pretext task may also be the most vulnerable to an adversary trained to make the task harder. We show that this assumption holds across common pretext tasks and datasets by training a "lens" network to make small image changes that maximally reduce performance in the pretext task. Representations learned with the modified images outperform those learned without in all tested cases. Additionally, the modifications made by the lens reveal how the choice of pretext task and dataset affects the features learned by self-supervision.

</details>

### Skew-Fit: State-Covering Self-Supervised Reinforcement Learning.
- **链接**: [arXiv:1903.03698](https://arxiv.org/abs/1903.03698)
- **作者**: Vitchyr Pong, Murtaza Dalal, Steven Lin, Ashvin Nair, Shikhar Bahl, Sergey Levine
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous agents that must exhibit flexible and broad capabilities will need to be equipped with large repertoires of skills. Defining each skill with a manually-designed reward function limits this repertoire and imposes a manual engineering burden. Self-supervised agents that set their own goals can automate this process, but designing appropriate goal setting objectives can be difficult, and often involves heuristic design decisions. In this paper, we propose a formal exploration objective for goal-reaching policies that maximizes state coverage. We show that this objective is equivalent to maximizing goal reaching performance together with the entropy of the goal distribution, where goals correspond to full state observations. To instantiate this principle, we present an algorithm called Skew-Fit for learning a maximum-entropy goal distributions. We prove that, under regularity conditions, Skew-Fit converges to a uniform distribution over the set of valid states, even when we do not know this set beforehand. Our experiments show that combining Skew-Fit for learning goal distributions with existing goal-reaching methods outperforms a variety of prior methods on open-sourced visual goal-reaching tasks. Moreover, we demonstrate that Skew-Fit enables a real-world robot to learn to open a door, entirely from scratch, from pixels, and without any manually-designed reward function.

</details>

### Planning to Explore via Self-Supervised World Models.
- **链接**: [arXiv:2005.05960](https://arxiv.org/abs/2005.05960)
- **作者**: Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, Deepak Pathak
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reinforcement learning allows solving complex tasks, however, the learning tends to be task-specific and the sample efficiency remains a challenge. We present Plan2Explore, a self-supervised reinforcement learning agent that tackles both these challenges through a new approach to self-supervised exploration and fast adaptation to new tasks, which need not be known during exploration. During exploration, unlike prior methods which retrospectively compute the novelty of observations after the agent has already reached them, our agent acts efficiently by leveraging planning to seek out expected future novelty. After exploration, the agent quickly adapts to multiple downstream tasks in a zero or a few-shot manner. We evaluate on challenging control tasks from high-dimensional image inputs. Without any training supervision or task-specific interaction, Plan2Explore outperforms prior self-supervised exploration methods, and in fact, almost matches the performances oracle which has access to rewards. Videos and code at https://ramanans1.github.io/plan2explore/

</details>

### Graph-based, Self-Supervised Program Repair from Diagnostic Feedback.
- **链接**: [arXiv:2005.10636](https://arxiv.org/abs/2005.10636)
- **作者**: Michihiro Yasunaga, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of learning to repair programs from diagnostic feedback (e.g., compiler error messages). Program repair is challenging for two reasons: First, it requires reasoning and tracking symbols across source code and diagnostic feedback. Second, labeled datasets available for program repair are relatively small. In this work, we propose novel solutions to these two challenges. First, we introduce a program-feedback graph, which connects symbols relevant to program repair in source code and diagnostic feedback, and then apply a graph neural network on top to model the reasoning process. Second, we present a self-supervised learning paradigm for program repair that leverages unlabeled programs available online to create a large amount of extra program repair examples, which we use to pre-train our models. We evaluate our proposed approach on two applications: correcting introductory programming assignments (DeepFix dataset) and correcting the outputs of program synthesis (SPoC dataset). Our final system, DrRepair, significantly outperforms prior work, achieving 68.2% full repair rate on DeepFix (+22.9% over the prior best), and 48.4% synthesis success rate on SPoC (+3.7% over the prior best).

</details>

### A Simple Framework for Contrastive Learning of Visual Representations.
- **链接**: [arXiv:2002.05709](https://arxiv.org/abs/2002.05709)
- **作者**: Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey E. Hinton
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents SimCLR: a simple framework for contrastive learning of visual representations. We simplify recently proposed contrastive self-supervised learning algorithms without requiring specialized architectures or a memory bank. In order to understand what enables the contrastive prediction tasks to learn useful representations, we systematically study the major components of our framework. We show that (1) composition of data augmentations plays a critical role in defining effective predictive tasks, (2) introducing a learnable nonlinear transformation between the representation and the contrastive loss substantially improves the quality of the learned representations, and (3) contrastive learning benefits from larger batch sizes and more training steps compared to supervised learning. By combining these findings, we are able to considerably outperform previous methods for self-supervised and semi-supervised learning on ImageNet. A linear classifier trained on self-supervised representations learned by SimCLR achieves 76.5% top-1 accuracy, which is a 7% relative improvement over previous state-of-the-art, matching the performance of a supervised ResNet-50. When fine-tuned on only 1% of the labels, we achieve 85.8% top-5 accuracy, outperforming AlexNet with 100X fewer labels.

</details>

### On Contrastive Learning for Likelihood-free Inference.
- **链接**: [arXiv:2002.03712](https://arxiv.org/abs/2002.03712)
- **作者**: Conor Durkan, Iain Murray, George Papamakarios
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Likelihood-free methods perform parameter inference in stochastic simulator models where evaluating the likelihood is intractable but sampling synthetic data is possible. One class of methods for this likelihood-free problem uses a classifier to distinguish between pairs of parameter-observation samples generated using the simulator and pairs sampled from some reference distribution, which implicitly learns a density ratio proportional to the likelihood. Another popular class of methods fits a conditional distribution to the parameter posterior directly, and a particular recent variant allows for the use of flexible neural density estimators for this task. In this work, we show that both of these approaches can be unified under a general contrastive learning scheme, and clarify how they should be run and compared.

</details>
