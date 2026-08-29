# Multimodal — 2020 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Cross-Modal Weighting Network for RGB-D Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58520-4_39)
- **作者**: Gongyang Li, Zhi Liu, Linwei Ye, Yang Wang, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### 6D Camera Relocalization in Ambiguous Scenes via Continuous Multimodal Inference.
- **链接**: [arXiv:2004.04807](https://arxiv.org/abs/2004.04807) · 📚 被引 17
- **作者**: Mai Bui, Tolga Birdal, Haowen Deng, Shadi Albarqouni, Leonidas J. Guibas, Slobodan Ilic et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a multimodal camera relocalization framework that captures ambiguities and uncertainties with continuous mixture models defined on the manifold of camera poses. In highly ambiguous environments, which can easily arise due to symmetries and repetitive structures in the scene, computing one plausible solution (what most state-of-the-art methods currently regress) may not be sufficient. Instead we predict multiple camera pose hypotheses as well as the respective uncertainty for each prediction. Towards this aim, we use Bingham distributions, to model the orientation of the camera pose, and a multivariate Gaussian to model the position, with an end-to-end deep neural network. By incorporating a Winner-Takes-All training scheme, we finally obtain a mixture model that is well suited for explaining ambiguities in the scene, yet does not suffer from mode collapse, a common problem with mixture density networks. We introduce a new dataset specifically designed to foster camera localization research in ambiguous environments and exhaustively evaluate our method on synthetic as well as real data on both ambiguous scenes and on non-ambiguous benchmark datasets. We plan to release our code and dataset under $\href{https://multimodal3dvision.github.io}{multimodal3dvision.github.io}$.

</details>
