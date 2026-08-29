# Autonomous Driving — 2021 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Exploring Simple 3D Multi-Object Tracking for Autonomous Driving.
- **链接**: [arXiv:2108.10312](https://arxiv.org/abs/2108.10312) · 📚 被引 112
- **作者**: Chenxu Luo, Xiaodong Yang, Alan L. Yuille
- **🏷️ 机构**: QCraft, Johns Hopkins University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D multi-object tracking in LiDAR point clouds is a key ingredient for self-driving vehicles. Existing methods are predominantly based on the tracking-by-detection pipeline and inevitably require a heuristic matching step for the detection association. In this paper, we present SimTrack to simplify the hand-crafted tracking paradigm by proposing an end-to-end trainable model for joint detection and tracking from raw point clouds. Our key design is to predict the first-appear location of each object in a given snippet to get the tracking identity and then update the location based on motion estimation. In the inference, the heuristic matching step can be completely waived by a simple read-off operation. SimTrack integrates the tracked object association, newborn object detection, and dead track killing in a single unified model. We conduct extensive evaluations on two large-scale datasets: nuScenes and Waymo Open Dataset. Experimental results reveal that our simple approach compares favorably with the state-of-the-art methods while ruling out the heuristic matching rules.

</details>

### MultiSiam: Self-supervised Multi-instance Siamese Representation Learning for Autonomous Driving.
- **链接**: [arXiv:2108.12178](https://arxiv.org/abs/2108.12178) · [代码](https://github.com/KaiChen1998/MultiSiam) · 📚 被引 35
- **作者**: Kai Chen, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving has attracted much attention over the years but turns out to be harder than expected, probably due to the difficulty of labeled data collection for model training. Self-supervised learning (SSL), which leverages unlabeled data only for representation learning, might be a promising way to improve model performance. Existing SSL methods, however, usually rely on the single-centric-object guarantee, which may not be applicable for multi-instance datasets such as street scenes. To alleviate this limitation, we raise two issues to solve: (1) how to define positive samples for cross-view consistency and (2) how to measure similarity in multi-instance circumstances. We first adopt an IoU threshold during random cropping to transfer global-inconsistency to local-consistency. Then, we propose two feature alignment methods to enable 2D feature maps for multi-instance similarity measurement. Additionally, we adopt intra-image clustering with self-attention for further mining intra-image similarity and translation-invariance. Experiments show that, when pre-trained on Waymo dataset, our method called Multi-instance Siamese Network (MultiSiam) remarkably improves generalization ability and achieves state-of-the-art transfer performance on autonomous driving benchmarks, including Cityscapes and BDD100K, while existing SSL counterparts like MoCo, MoCo-v2, and BYOL show significant performance drop. By pre-training on SODA10M, a large-scale autonomous driving dataset, MultiSiam exceeds the ImageNet pre-trained MoCo-v2, demonstrating the potential of domain-specific pre-training. Code will be available at https://github.com/KaiChen1998/MultiSiam.

</details>

### NEAT: Neural Attention Fields for End-to-End Autonomous Driving.
- **链接**: [arXiv:2109.04456](https://arxiv.org/abs/2109.04456) · 📚 被引 212
- **作者**: Kashyap Chitta, Aditya Prakash, Andreas Geiger
- **🏷️ 机构**: Max Planck Institute for Intelligent Systems,T&#x00FC;bingen
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient reasoning about the semantic, spatial, and temporal structure of a scene is a crucial prerequisite for autonomous driving. We present NEural ATtention fields (NEAT), a novel representation that enables such reasoning for end-to-end imitation learning models. NEAT is a continuous function which maps locations in Bird's Eye View (BEV) scene coordinates to waypoints and semantics, using intermediate attention maps to iteratively compress high-dimensional 2D image features into a compact representation. This allows our model to selectively attend to relevant regions in the input while ignoring information irrelevant to the driving task, effectively associating the images with the BEV representation. In a new evaluation setting involving adverse environmental conditions and challenging scenarios, NEAT outperforms several strong baselines and achieves driving scores on par with the privileged CARLA expert used to generate its training data. Furthermore, visualizing the attention maps for models with NEAT intermediate representations provides improved interpretability.

</details>

### TMCOSS: Thresholded Multi-Criteria Online Subset Selection for Data-Efficient Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00628) · 📚 被引 4
- **作者**: Soumi Das, Harikrishna Patibandla, Suparna Bhattacharya, Kshounis Bera, Niloy Ganguly, Sourangshu Bhattacharya
- **🏷️ 机构**: IIT Kharagpur, HPE Enterprise,Hewlett Packard Labs, HPE Enterprise
- **会议**: ICCV 2021

### Large Scale Interactive Motion Forecasting for Autonomous Driving : The Waymo Open Motion Dataset.
- **链接**: [arXiv:2104.10133](https://arxiv.org/abs/2104.10133) · 📚 被引 513
- **作者**: Scott Ettinger, Shuyang Cheng, Benjamin Caine, Chenxi Liu, Hang Zhao, Sabeek Pradhan et al.
- **🏷️ 机构**: Waymo LLC, Google Brain
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As autonomous driving systems mature, motion forecasting has received increasing attention as a critical requirement for planning. Of particular importance are interactive situations such as merges, unprotected turns, etc., where predicting individual object motion is not sufficient. Joint predictions of multiple objects are required for effective route planning. There has been a critical need for high-quality motion data that is rich in both interactions and annotation to develop motion planning models. In this work, we introduce the most diverse interactive motion dataset to our knowledge, and provide specific labels for interacting objects suitable for developing joint prediction models. With over 100,000 scenes, each 20 seconds long at 10 Hz, our new dataset contains more than 570 hours of unique data over 1750 km of roadways. It was collected by mining for interesting interactions between vehicles, pedestrians, and cyclists across six cities within the United States. We use a high-accuracy 3D auto-labeling system to generate high quality 3D bounding boxes for each road agent, and provide corresponding high definition 3D maps for each scene. Furthermore, we introduce a new set of metrics that provides a comprehensive evaluation of both single agent and joint agent interaction motion forecasting models. Finally, we provide strong baseline models for individual-agent prediction and joint-prediction. We hope that this new large-scale interactive motion dataset will provide new opportunities for advancing motion forecasting models.

</details>

### Safety-aware Motion Prediction with Unseen Vehicles for Autonomous Driving.
- **链接**: [arXiv:2109.01510](https://arxiv.org/abs/2109.01510) · [代码](https://github.com/xrenaa/Safety-Aware-Motion-Prediction) · 📚 被引 24
- **作者**: Xuanchi Ren, Tao Yang, Li Erran Li, Alexandre Alahi, Qifeng Chen
- **🏷️ 机构**: HKUST, Xi&#x2019;an Jiaotong University, Alexa AI, Amazon
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion prediction of vehicles is critical but challenging due to the uncertainties in complex environments and the limited visibility caused by occlusions and limited sensor ranges. In this paper, we study a new task, safety-aware motion prediction with unseen vehicles for autonomous driving. Unlike the existing trajectory prediction task for seen vehicles, we aim at predicting an occupancy map that indicates the earliest time when each location can be occupied by either seen and unseen vehicles. The ability to predict unseen vehicles is critical for safety in autonomous driving. To tackle this challenging task, we propose a safety-aware deep learning model with three new loss functions to predict the earliest occupancy map. Experiments on the large-scale autonomous driving nuScenes dataset show that our proposed model significantly outperforms the state-of-the-art baselines on the safety-aware motion prediction task. To the best of our knowledge, our approach is the first one that can predict the existence of unseen vehicles in most cases. Project page at {\url{https://github.com/xrenaa/Safety-Aware-Motion-Prediction}}.

</details>

### MGNet: Monocular Geometric Scene Understanding for Autonomous Driving.
- **链接**: [arXiv:2206.13199](https://arxiv.org/abs/2206.13199) · [代码](https://github.com/markusschoen/MGNet) · 📚 被引 49
- **作者**: Markus Schön, Michael Buchholz, Klaus Dietmayer
- **🏷️ 机构**: Ulm University,Institute of Measurement, Control and Microtechnology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MGNet, a multi-task framework for monocular geometric scene understanding. We define monocular geometric scene understanding as the combination of two known tasks: Panoptic segmentation and self-supervised monocular depth estimation. Panoptic segmentation captures the full scene not only semantically, but also on an instance basis. Self-supervised monocular depth estimation uses geometric constraints derived from the camera measurement model in order to measure depth from monocular video sequences only. To the best of our knowledge, we are the first to propose the combination of these two tasks in one single model. Our model is designed with focus on low latency to provide fast inference in real-time on a single consumer-grade GPU. During deployment, our model produces dense 3D point clouds with instance aware semantic labels from single high-resolution camera images. We evaluate our model on two popular autonomous driving benchmarks, i.e., Cityscapes and KITTI, and show competitive performance among other real-time capable methods. Source code is available at https://github.com/markusschoen/MGNet.

</details>

### LookOut: Diverse Multi-Future Prediction and Planning for Self-Driving.
- **链接**: [arXiv:2101.06547](https://arxiv.org/abs/2101.06547) · 📚 被引 113
- **作者**: Alexander Cui, Sergio Casas, Abbas Sadat, Renjie Liao, Raquel Urtasun
- **🏷️ 机构**: Waabi, Google Brain
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present LookOut, a novel autonomy system that perceives the environment, predicts a diverse set of futures of how the scene might unroll and estimates the trajectory of the SDV by optimizing a set of contingency plans over these future realizations. In particular, we learn a diverse joint distribution over multi-agent future trajectories in a traffic scene that covers a wide range of future modes with high sample efficiency while leveraging the expressive power of generative models. Unlike previous work in diverse motion forecasting, our diversity objective explicitly rewards sampling future scenarios that require distinct reactions from the self-driving vehicle for improved safety. Our contingency planner then finds comfortable and non-conservative trajectories that ensure safe reactions to a wide range of future scenarios. Through extensive evaluations, we show that our model demonstrates significantly more diverse and sample-efficient motion forecasting in a large-scale self-driving dataset as well as safer and less-conservative motion plans in long-term closed-loop simulations when compared to current state-of-the-art models.

</details>

### ACDC: The Adverse Conditions Dataset with Correspondences for Semantic Driving Scene Understanding.
- **链接**: [arXiv:2104.13395](https://arxiv.org/abs/2104.13395) · 📚 被引 0
- **作者**: Christos Sakaridis, Dengxin Dai, Luc Van Gool
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Level-5 driving automation requires a robust visual perception system that can parse input images under any condition. However, existing driving datasets for dense semantic perception are either dominated by images captured under normal conditions or are small in scale. To address this, we introduce ACDC, the Adverse Conditions Dataset with Correspondences for training and testing methods for diverse semantic perception tasks on adverse visual conditions. ACDC consists of a large set of 8012 images, half of which (4006) are equally distributed between four common adverse conditions: fog, nighttime, rain, and snow. Each adverse-condition image comes with a high-quality pixel-level panoptic annotation, a corresponding image of the same scene under normal conditions, and a binary mask that distinguishes between intra-image regions of clear and uncertain semantic content. 1503 of the corresponding normal-condition images feature panoptic annotations, raising the total annotated images to 5509. ACDC supports the standard tasks of semantic segmentation, object detection, instance segmentation, and panoptic segmentation, as well as the newly introduced uncertainty-aware semantic segmentation. A detailed empirical study demonstrates the challenges that the adverse domains of ACDC pose to state-of-the-art supervised and unsupervised approaches and indicates the value of our dataset in steering future progress in the field. Our dataset and benchmark are publicly available at https://acdc.vision.ee.ethz.ch

</details>
