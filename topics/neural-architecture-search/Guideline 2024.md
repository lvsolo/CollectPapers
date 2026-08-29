# Neural Architecture Search — 2024 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Vision Transformer Neural Architecture Search for Out-of-Distribution Generalization: Benchmark and Insights.
- **链接**: [arXiv:2501.03782](https://arxiv.org/abs/2501.03782) · 📚 被引 2
- **作者**: Sy-Tuyen Ho, Tuan Van Vo, Somayeh Ebrahimkhani, Ngai-Man Cheung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While ViTs have achieved across machine learning tasks, deploying them in real-world scenarios faces a critical challenge: generalizing under OoD shifts. A crucial research gap exists in understanding how to design ViT architectures, both manually and automatically, for better OoD generalization. To this end, we introduce OoD-ViT-NAS, the first systematic benchmark for ViTs NAS focused on OoD generalization. This benchmark includes 3000 ViT architectures of varying computational budgets evaluated on 8 common OoD datasets. Using this benchmark, we analyze factors contributing to OoD generalization. Our findings reveal key insights. First, ViT architecture designs significantly affect OoD generalization. Second, ID accuracy is often a poor indicator of OoD accuracy, highlighting the risk of optimizing ViT architectures solely for ID performance. Third, we perform the first study of NAS for ViTs OoD robustness, analyzing 9 Training-free NAS methods. We find that existing Training-free NAS methods are largely ineffective in predicting OoD accuracy despite excelling at ID accuracy. Simple proxies like Param or Flop surprisingly outperform complex Training-free NAS methods in predicting OoD accuracy. Finally, we study how ViT architectural attributes impact OoD generalization and discover that increasing embedding dimensions generally enhances performance. Our benchmark shows that ViT architectures exhibit a wide range of OoD accuracy, with up to 11.85% improvement for some OoD shifts. This underscores the importance of studying ViT architecture design for OoD. We believe OoD-ViT-NAS can catalyze further research into how ViT designs influence OoD generalization.

</details>

### MOTE-NAS: Multi-Objective Training-based Estimate for Efficient Neural Architecture Search.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b6e118c759c16f2424997bbb6a1ffd61-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yuming Zhang, Jun-Wei Hsieh, Xin Li, Ming-Ching Chang, Chun-Chieh Lee, Kuo-Chin Fan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### CE-NAS: An End-to-End Carbon-Efficient Neural Architecture Search Framework.
- **链接**: [arXiv:2406.01414](https://arxiv.org/abs/2406.01414) · 📚 被引 2
- **作者**: Yiyang Zhao, Yunzhuo Liu, Bo Jiang, Tian Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work presents a novel approach to neural architecture search (NAS) that aims to increase carbon efficiency for the model design process. The proposed framework CE-NAS addresses the key challenge of high carbon cost associated with NAS by exploring the carbon emission variations of energy and energy differences of different NAS algorithms. At the high level, CE-NAS leverages a reinforcement-learning agent to dynamically adjust GPU resources based on carbon intensity, predicted by a time-series transformer, to balance energy-efficient sampling and energy-intensive evaluation tasks. Furthermore, CE-NAS leverages a recently proposed multi-objective optimizer to effectively reduce the NAS search space. We demonstrate the efficacy of CE-NAS in lowering carbon emissions while achieving SOTA results for both NAS datasets and open-domain NAS tasks. For example, on the HW-NasBench dataset, CE-NAS reduces carbon emissions by up to 7.22X while maintaining a search efficiency comparable to vanilla NAS. For open-domain NAS tasks, CE-NAS achieves SOTA results with 97.35% top-1 accuracy on CIFAR-10 with only 1.68M parameters and a carbon consumption of 38.53 lbs of CO2. On ImageNet, our searched model achieves 80.6% top-1 accuracy with a 0.78 ms TensorRT latency using FP16 on NVIDIA V100, consuming only 909.86 lbs of CO2, making it comparable to other one-shot-based NAS baselines.

</details>
