# Tracking — 2024 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DeconfuseTrack: Dealing with Confusion for Multi-Object Tracking.
- **链接**: [arXiv:2403.02767](https://arxiv.org/abs/2403.02767) · 📚 被引 25
- **作者**: Cheng Huang, Shoudong Han, Mengyu He, Wenbo Zheng, Yuhao Wei
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,National Key Laboratory of Multispectral Information Intelligent Processing Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Accurate data association is crucial in reducing confusion, such as ID switches and assignment errors, in multi-object tracking (MOT). However, existing advanced methods often overlook the diversity among trajectories and the ambiguity and conflicts present in motion and appearance cues, leading to confusion among detections, trajectories, and associations when performing simple global data association. To address this issue, we propose a simple, versatile, and highly interpretable data association approach called Decomposed Data Association (DDA). DDA decomposes the traditional association problem into multiple sub-problems using a series of non-learning-based modules and selectively addresses the confusion in each sub-problem by incorporating targeted exploitation of new cues. Additionally, we introduce Occlusion-aware Non-Maximum Suppression (ONMS) to retain more occluded detections, thereby increasing opportunities for association with trajectories and indirectly reducing the confusion caused by missed detections. Finally, based on DDA and ONMS, we design a powerful multi-object tracker named DeconfuseTrack, specifically focused on resolving confusion in MOT. Extensive experiments conducted on the MOT17 and MOT20 datasets demonstrate that our proposed DDA and ONMS significantly enhance the performance of several popular trackers. Moreover, DeconfuseTrack achieves state-of-the-art performance on the MOT17 and MOT20 test sets, significantly outperforms the baseline tracker ByteTrack in metrics such as HOTA, IDF1, AssA. This validates that our tracking design effectively reduces confusion caused by simple global association.

### Towards Generalizable Multi-Object Tracking.
- **链接**: [arXiv:2406.00429](https://arxiv.org/abs/2406.00429) · [代码](https://github.com/qinzheng2000/GeneralTrack.git) · 📚 被引 37
- **作者**: Zheng Qin, Le Wang, Sanping Zhou, Panpan Fu, Gang Hua, Wei Tang
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, School of Software Engineering, Xi&#x0027;an Jiaotong University, Wormpex AI Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multi-Object Tracking MOT encompasses various tracking scenarios, each characterized by unique traits. Effective trackers should demonstrate a high degree of generalizability across diverse scenarios. However, existing trackers struggle to accommodate all aspects or necessitate hypothesis and experimentation to customize the association information motion and or appearance for a given scenario, leading to narrowly tailored solutions with limited generalizability. In this paper, we investigate the factors that influence trackers generalization to different scenarios and concretize them into a set of tracking scenario attributes to guide the design of more generalizable trackers. Furthermore, we propose a point-wise to instance-wise relation framework for MOT, i.e., GeneralTrack, which can generalize across diverse scenarios while eliminating the need to balance motion and appearance. Thanks to its superior generalizability, our proposed GeneralTrack achieves state-of-the-art performance on multiple benchmarks and demonstrates the potential for domain generalization. https://github.com/qinzheng2000/GeneralTrack.git

### Multi-Object Tracking in the Dark.
- **链接**: [arXiv:2405.06600](https://arxiv.org/abs/2405.06600) · [代码](https://github.com/ying-fu/LMOT)
- **作者**: Xinzhe Wang, Kang Ma, Qiankun Liu, Yunhao Zou, Ying Fu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Low-light scenes are prevalent in real-world applications (e.g. autonomous driving and surveillance at night). Recently, multi-object tracking in various practical use cases have received much attention, but multi-object tracking in dark scenes is rarely considered. In this paper, we focus on multi-object tracking in dark scenes. To address the lack of datasets, we first build a Low-light Multi-Object Tracking (LMOT) dataset. LMOT provides well-aligned low-light video pairs captured by our dual-camera system, and high-quality multi-object tracking annotations for all videos. Then, we propose a low-light multi-object tracking method, termed as LTrack. We introduce the adaptive low-pass downsample module to enhance low-frequency components of images outside the sensor noises. The degradation suppression learning strategy enables the model to learn invariant information under noise disturbance and image quality degradation. These components improve the robustness of multi-object tracking in dark scenes. We conducted a comprehensive analysis of our LMOT dataset and proposed LTrack. Experimental results demonstrate the superiority of the proposed method and its competitiveness in real night low-light scenes. Dataset and Code: https: //github.com/ying-fu/LMOT

### HIPTrack: Visual Tracking with Historical Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01822) · 📚 被引 107
- **作者**: Wenrui Cai, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: State Key Laboratory of Virtual Reality Technology and Systems, Beihang University,Beijing,China
- **会议**: CVPR 2024

### MS-MANO: Enabling Hand Pose Tracking with Biomechanical Constraints.
- **链接**: [arXiv:2404.10227](https://arxiv.org/abs/2404.10227) · 📚 被引 9
- **作者**: Pengfei Xie, Wenqiang Xu, Tutian Tang, Zhenjun Yu, Cewu Lu
- **🏷️ 机构**: Southeast University, Shanghai Jiao Tong University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This work proposes a novel learning framework for visual hand dynamics analysis that takes into account the physiological aspects of hand motion. The existing models, which are simplified joint-actuated systems, often produce unnatural motions. To address this, we integrate a musculoskeletal system with a learnable parametric hand model, MANO, to create a new model, MS-MANO. This model emulates the dynamics of muscles and tendons to drive the skeletal system, imposing physiologically realistic constraints on the resulting torque trajectories. We further propose a simulation-in-the-loop pose refinement framework, BioPR, that refines the initial estimated pose through a multi-layer perceptron (MLP) network. Our evaluation of the accuracy of MS-MANO and the efficacy of the BioPR is conducted in two separate parts. The accuracy of MS-MANO is compared with MyoSuite, while the efficacy of BioPR is benchmarked against two large-scale public datasets and two recent state-of-the-art methods. The results demonstrate that our approach consistently improves the baseline methods both quantitatively and qualitatively.

## 跨领域论文（完整笔记在其他领域）

- ADA-Track: End-to-End Multi-Camera 3D Multi-Object Tracking with Alternating Detection and Association. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Self-Supervised Multi-Object Tracking with Path Consistency. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
