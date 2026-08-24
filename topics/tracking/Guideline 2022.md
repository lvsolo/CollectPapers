# Tracking — 2022 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Quo Vadis: Is Trajectory Forecasting the Key Towards Long-Term Multi-Object Tracking?
- **链接**: [arXiv:2210.07681](https://arxiv.org/abs/2210.07681) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/647dc4a76b3efdd676f50f32949299a8-Abstract-Conference.html) · [代码](https://github.com/dendorferpatrick/QuoVadis) · 📚 75 citations
- **作者**: Patrick Dendorfer, Vladimir Yugay, Aljosa Osep, Laura Leal-Taixé
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > Recent developments in monocular multi-object tracking have been very successful in tracking visible objects and bridging short occlusion gaps, mainly relying on data-driven appearance models. While we have significantly advanced short-term tracking performance, bridging longer occlusion gaps remains elusive: state-of-the-art object trackers only bridge less than 10% of occlusions longer than three seconds. We suggest that the missing key is reasoning about future trajectories over a longer time horizon. Intuitively, the longer the occlusion gap, the larger the search space for possible associations. In this paper, we show that even a small yet diverse set of trajectory predictions for moving agents will significantly reduce this search space and thus improve long-term tracking robustness. Our experiments suggest that the crucial components of our approach are reasoning in a bird's-eye view space and generating a small yet diverse set of forecasts while accounting for their localization uncertainty. This way, we can advance state-of-the-art trackers on the MOTChallenge dataset and significantly improve their long-term tracking performance. This paper's source code and experimental data are available at https://github.com/dendorferpatrick/QuoVadis.
