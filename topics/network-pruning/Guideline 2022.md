# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Sparse DETR: Efficient End-to-End Object Detection with Learnable Sparsity.
- **链接**: [arXiv:2111.14330](https://arxiv.org/abs/2111.14330) · [代码](https://github.com/kakaobrain/sparse-detr) · 📚 被引 0
- **作者**: Byungseok Roh, Jaewoong Shin, Wuhyun Shin, Saehoon Kim
- **🏷️ 机构**: Yanan University, Chongqing University of Science and Technology
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DETR is the first end-to-end object detector using a transformer encoder-decoder architecture and demonstrates competitive performance but low computational efficiency on high resolution feature maps. The subsequent work, Deformable DETR, enhances the efficiency of DETR by replacing dense attention with deformable attention, which achieves 10x faster convergence and improved performance. Deformable DETR uses the multiscale feature to ameliorate performance, however, the number of encoder tokens increases by 20x compared to DETR, and the computation cost of the encoder attention remains a bottleneck. In our preliminary experiment, we observe that the detection performance hardly deteriorates even if only a part of the encoder token is updated. Inspired by this observation, we propose Sparse DETR that selectively updates only the tokens expected to be referenced by the decoder, thus help the model effectively detect objects. In addition, we show that applying an auxiliary detection loss on the selected tokens in the encoder improves the performance while minimizing computational overhead. We validate that Sparse DETR achieves better performance than Deformable DETR even with only 10% encoder tokens on the COCO dataset. Albeit only the encoder tokens are sparsified, the total computation cost decreases by 38% and the frames per second (FPS) increases by 42% compared to Deformable DETR. Code is available at https://github.com/kakaobrain/sparse-detr

</details>

## 跨领域论文（完整笔记在其他领域）

- Memory Replay with Data Compression for Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
