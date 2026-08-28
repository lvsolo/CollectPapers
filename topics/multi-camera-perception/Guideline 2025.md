# Multi-camera Perception — 2025 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 72 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### HiPoNet: A Multi-View Simplicial Complex Network for High Dimensional Point-Cloud and Single-Cell data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b284aad9fb5c6d74b9535a30ece69e1c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Siddharth Viswanath, Hiren Madhu, Dhananjay Bhaskar, Jake Kovalic, Dave Johnson, Christopher J. Tape et al.
- **🏷️ 机构**: Yale University, Boise State University, University College London, University of London
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MANTA, a visual-text anomaly detection dataset for tiny objects. The visual component comprises over 137.3K images across 38 object categories spanning five typical domains, of which 8.6K images are labeled as anomalous with pixel-level annotations. Each image is captured from five distinct viewpoints to ensure comprehensive object coverage. The text component consists of two subsets: Declarative Knowledge, including 875 words that describe common anomalies across various domains and specific categories, with detailed explanations for < what, why, how>, including causes and visual characteristics; and Constructivist Learning, providing 2K multiple-choice questions with varying levels of difficulty, each paired with images and corresponded answer explanations. We also propose a baseline for visual-text tasks and conduct extensive benchmarking experiments to evaluate advanced methods across different settings, highlighting the challenges and efficacy of our dataset.

</details>

### SparseMVC: Probing Cross-view Sparsity Variations for Multi-view Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e366fff693ee7cdbca8ed2764bc18a71-Abstract-Conference.html)
- **作者**: Ruimeng Liu, Xin Zou, Chang Tang, Xiao Zheng, Xingchen Hu, Kun Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### PCDreamer: Point Cloud Completion Through Multi-view Diffusion Priors.
- **链接**: [arXiv:2411.19036](https://arxiv.org/abs/2411.19036) · 📚 被引 8
- **作者**: Guangshun Wei, Yuan Feng, Long Ma, Chen Wang, Yuanfeng Zhou, Changjian Li
- **🏷️ 机构**: Shandong University, University of Edinburgh
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents PCDreamer, a novel method for point cloud completion. Traditional methods typically extract features from partial point clouds to predict missing regions, but the large solution space often leads to unsatisfactory results. More recent approaches have started to use images as extra guidance, effectively improving performance, but obtaining paired data of images and partial point clouds is challenging in practice. To overcome these limitations, we harness the relatively view-consistent multi-view diffusion priors within large models, to generate novel views of the desired shape. The resulting image set encodes both global and local shape cues, which are especially beneficial for shape completion. To fully exploit the priors, we have designed a shape fusion module for producing an initial complete shape from multi-modality input (i.e.,, images and point clouds), and a follow-up shape consolidation module to obtain the final complete shape by discarding unreliable points introduced by the inconsistency from diffusion priors. Extensive experimental results demonstrate our superior performance, especially in recovering fine details.

</details>

### Sharp-It: A Multi-view to Multi-view Diffusion Model for 3D Synthesis and Manipulation.
- **链接**: [arXiv:2412.02631](https://arxiv.org/abs/2412.02631) · 📚 被引 4
- **作者**: Yiftach Edelstein, Or Patashnik, Dana Cohen-Bar, Lihi Zelnik-Manor
- **🏷️ 机构**: Technion - Israel Institute of Technology, Tel Aviv University
- **会议**: CVPR 2025

> We introduce ForeSight, a novel joint detection and forecasting framework for vision-based 3D perception in autonomous vehicles. Traditional approaches treat detection and forecasting as separate sequential tasks, limiting their ability to leverage temporal cues. ForeSight addresses this limitation with a multi-task streaming and bidirectional learning approach, allowing detection and forecasting to share query memory and propagate information seamlessly. The forecast-aware detection transformer enhances spatial reasoning by integrating trajectory predictions from a multiple hypothesis forecast memory queue, while the streaming forecast transformer improves temporal consistency using past forecasts and refined detections. Unlike tracking-based methods, ForeSight eliminates the need for explicit object association, reducing error propagation with a tracking-free model that efficiently scales across multi-frame sequences. Experiments on the nuScenes dataset show that ForeSight achieves state-of-the-art performance, achieving an EPA of 54.9%, surpassing previous methods by 9.3%, while also attaining the best mAP and minADE among multi-view detection and forecasting models.

</details>

### Multi-View 3D Point Tracking.
- **链接**: [arXiv:2508.21060](https://arxiv.org/abs/2508.21060)
- **作者**: Frano Rajic, Haofei Xu, Marko Mihajlovic, Siyuan Li, Irem Demir, Emircan Gündogdu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the first data-driven multi-view 3D point tracker, designed to track arbitrary points in dynamic scenes using multiple camera views. Unlike existing monocular trackers, which struggle with depth ambiguities and occlusion, or prior multi-camera methods that require over 20 cameras and tedious per-sequence optimization, our feed-forward model directly predicts 3D correspondences using a practical number of cameras (e.g., four), enabling robust and accurate online tracking. Given known camera poses and either sensor-based or estimated multi-view depth, our tracker fuses multi-view features into a unified point cloud and applies k-nearest-neighbors correlation alongside a transformer-based update to reliably estimate long-range 3D correspondences, even under occlusion. We train on 5K synthetic multi-view Kubric sequences and evaluate on two real-world benchmarks: Panoptic Studio and DexYCB, achieving median trajectory errors of 3.1 cm and 2.0 cm, respectively. Our method generalizes well to diverse camera setups of 1-8 views with varying vantage points and video lengths of 24-150 frames. By releasing our tracker alongside training and evaluation datasets, we aim to set a new standard for multi-view 3D tracking research and provide a practical tool for real-world applications. Project page available at https://ethz-vlg.github.io/mvtracker.

</details>

### MVTrajecter: Multi-View Pedestrian Tracking With Trajectory Motion Cost and Trajectory Appearance Cost.
- **链接**: [arXiv:2509.01157](https://arxiv.org/abs/2509.01157) · 📚 被引 1
- **作者**: Taiga Yamane, Ryo Masumura, Satoshi Suzuki, Shota Orihashi
- **🏷️ 机构**: NTT Corporation,NTT Human Informatics Laboratries
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-View Pedestrian Tracking (MVPT) aims to track pedestrians in the form of a bird's eye view occupancy map from multi-view videos. End-to-end methods that detect and associate pedestrians within one model have shown great progress in MVPT. The motion and appearance information of pedestrians is important for the association, but previous end-to-end MVPT methods rely only on the current and its single adjacent past timestamp, discarding the past trajectories before that. This paper proposes a novel end-to-end MVPT method called Multi-View Trajectory Tracker (MVTrajecter) that utilizes information from multiple timestamps in past trajectories for robust association. MVTrajecter introduces trajectory motion cost and trajectory appearance cost to effectively incorporate motion and appearance information, respectively. These costs calculate which pedestrians at the current and each past timestamp are likely identical based on the information between those timestamps. Even if a current pedestrian could be associated with a false pedestrian at some past timestamp, these costs enable the model to associate that current pedestrian with the correct past trajectory based on other past timestamps. In addition, MVTrajecter effectively captures the relationships between multiple timestamps leveraging the attention mechanism. Extensive experiments demonstrate the effectiveness of each component in MVTrajecter and show that it outperforms the previous state-of-the-art methods.

</details>

### Point Cloud Self-Supervised Learning via 3D to Multi-View Masked Learner.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02564)
- **作者**: Zhimin Chen, Xuewei Chen, Xiao Guo, Yingwei Li, Longlong Jing, Liang Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### AF-UMC: An Alignment-Free Fusion Framework for Unaligned Multi-View Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/965484d5b2b2624ba17295612a3ba7e8-Abstract-Conference.html) · 📚 被引 0
- **作者**: Bohang Sun, Yuena Lin, Tao Yang, Zhen Zhu, Zhen Yang, Gengyu Lyu
- **🏷️ 机构**: Beijing University of Technology, Idealism Beijing Technology Co., Ltd, Zhejiang Sci-Tech University
- **会议**: NeurIPS 2025

### MIX: A Multi-view Time-Frequency Interactive Explanation Framework for Time Series Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/46559eba5b7b86236675d7ea34f52f5c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Viet-Hung Tran, Ngoc Phu Doan, Zichi Zhang, Tuan Dung Pham, Phi Hung Nguyen, Xuan Hoang Nguyen et al.
- **🏷️ 机构**: The Queen's University Belfast, Queen's University Belfast, Aarhus University
- **会议**: NeurIPS 2025

### A Data-Driven Prism: Multi-View Source Separation with Diffusion Model Priors.
- **链接**: [arXiv:2510.05205](https://arxiv.org/abs/2510.05205) · 📚 被引 0
- **作者**: Sebastian Wagner-Carena, Aizhan Akhmetzhanova, Sydney Erickson
- **🏷️ 机构**: New York University / Simons Foundation, Harvard University, Stanford University
- **会议**: NeurIPS 2025

### Where Graph Meets Heterogeneity: Multi-View Collaborative Graph Experts.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7315c16422558ae81d65a812723d2cec-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhihao Wu, Jinyu Cai, Yunhe Zhang, Jielong Lu, Zhaoliang Chen, Shuman Zhuang et al.
- **🏷️ 机构**: Zhejiang University, National University of Singapore, University of Macau
- **会议**: NeurIPS 2025

### LLM-DAMVC: A Large Language Model Assisted Dynamic Agent for Multi-View Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ad48f017e6c3d474caf511208e600459-Abstract-Conference.html) · 📚 被引 0
- **作者**: Haiming Xu, Qianqian Wang
- **🏷️ 机构**: ByteDance Inc., Xidian University
- **会议**: NeurIPS 2025

### Multi-View Oriented GPLVM: Expressiveness and Efficiency.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5e50b663324972bb8cc7b5c06a059438-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zi Yang, Ying Li, Zhidi Lin, Michael Minyi Zhang, Pablo M. Olmos
- **🏷️ 机构**: Jiangnan University, University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have demonstrated remarkable capabilities in various tasks. However, effectively evaluating these MLLMs on face perception remains largely unexplored. To address this gap, we introduce FaceBench, a dataset featuring hierarchical multi-view and multi-level attributes specifically designed to assess the comprehensive face perception abilities of MLLMs. Initially, we construct a hierarchical facial attribute structure, which encompasses five views with up to three levels of attributes, totaling over 210 attributes and 700 attribute values. Based on the structure, the proposed FaceBench consists of 49,919 visual question-answering (VQA) pairs for evaluation and 23,841 pairs for fine-tuning. Moreover, we further develop a robust face perception MLLM baseline, Face-LLaVA, by training with our proposed face VQA data. Extensive experiments on various mainstream MLLMs and Face-LLaVA are conducted to test their face perception ability, with results also compared against human performance. The results reveal that, the existing MLLMs are far from satisfactory in understanding the fine-grained facial attributes, while our Face-LLaVA significantly outperforms existing open-source models with a small amount of training data and is comparable to commercial ones like GPT-4o and Gemini. The dataset will be released at https://github.com/CVI-SZU/FaceBench.

</details>

### MIHC: Multi-View Interpretable Hypergraph Neural Networks with Information Bottleneck for Chip Congestion Prediction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7fc54f90195097ed0ee6200f1dc274d3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zeyue Zhang, Heng Ping, Peiyu Zhang, Nikos Kanakaris, Xiaoling Lu, Paul Bogdan et al.
- **🏷️ 机构**: Renmin University of China, University of Southern California, Amazon
- **会议**: NeurIPS 2025

### MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/819aaee144cb40e887a4aa9e781b1547-Abstract-Conference.html) · 📚 被引 0
- **作者**: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han
- **🏷️ 机构**: Software Engineering, Tsinghua University, Tsinghua University, Tsinghua University, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

### Stable Part Diffusion 4D: Multi-View RGB and Kinematic Parts Video Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a61023ce36d21010f1423304f8ec49af-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hao Zhang, Chun-Han Yao, Simon Donné, Narendra Ahuja, Varun Jampani
- **🏷️ 机构**: Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Stability AI, University of Illinois at Urbana-Champaign
- **会议**: NeurIPS 2025

### Gaussian Regression-Driven Tensorized Incomplete Multi-View Clustering with Dual Manifold Regularization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/684c59d614fe6ae74a3be8c3ef07e061-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhenhao Zhong, Zhibin Gu, Pengpeng Yang, Yaqian Zhou, Ruiqiang Guo
- **🏷️ 机构**: Xi'an Jiaotong University, Hebei Normal University, University of Florence; China Three Gorges University
- **会议**: NeurIPS 2025

### MET3R: Measuring Multi-View Consistency in Generated Images.
- **链接**: [arXiv:2501.06336](https://arxiv.org/abs/2501.06336) · 📚 被引 17
- **作者**: Mohammad Asim, Christopher Wewer, Thomas Wimmer, Bernt Schiele, Jan Eric Lenssen
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2025

### SAINT: Sequence-Aware Integration for Spatial Transcriptomics Multi-View Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a86441358d4b88afe485f160dc6a982f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zeyu Zhu, Ke Liang, Lingyuan Meng, Meng Liu, Suyuan Liu, Renxiang Guan et al.
- **🏷️ 机构**: National University of Defense Technology, Shandong Jianzhu University, Changsha University
- **会议**: NeurIPS 2025

### SynCL: A Synergistic Training Strategy with Instance-Aware Contrastive Learning for End-to-End Multi-Camera 3D Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/056932270665ac01253e5ef7c5dc32aa-Abstract-Conference.html)
- **作者**: Shubo Lin, Yutong Kou, Zirui Wu, Shaoru Wang, Bing Li, Weiming Hu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### MuTri: Multi-view Tri-alignment for OCT to OCTA 3D Image Translation.
- **链接**: [arXiv:2504.01428](https://arxiv.org/abs/2504.01428) · 📚 被引 5
- **作者**: Zhuangzhuang Chen, Hualiang Wang, Chubin Ou, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Department of Electronic and Computer Engineering, Southern Medical University,Department of Radiology, Guangdong Provincial People&#x2019;s Hospital
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Optical coherence tomography angiography (OCTA) shows its great importance in imaging microvascular networks by providing accurate 3D imaging of blood vessels, but it relies upon specialized sensors and expensive devices. For this reason, previous works show the potential to translate the readily available 3D Optical Coherence Tomography (OCT) images into 3D OCTA images. However, existing OCTA translation methods directly learn the mapping from the OCT domain to the OCTA domain in continuous and infinite space with guidance from only a single view, i.e., the OCTA project map, resulting in suboptimal results. To this end, we propose the multi-view Tri-alignment framework for OCT to OCTA 3D image translation in discrete and finite space, named MuTri. In the first stage, we pre-train two vector-quantized variational auto-encoder (VQ- VAE) by reconstructing 3D OCT and 3D OCTA data, providing semantic prior for subsequent multi-view guidances. In the second stage, our multi-view tri-alignment facilitates another VQVAE model to learn the mapping from the OCT domain to the OCTA domain in discrete and finite space. Specifically, a contrastive-inspired semantic alignment is proposed to maximize the mutual information with the pre-trained models from OCT and OCTA views, to facilitate codebook learning. Meanwhile, a vessel structure alignment is proposed to minimize the structure discrepancy with the pre-trained models from the OCTA project map view, benefiting from learning the detailed vessel structure information. We also collect the first large-scale dataset, namely, OCTA2024, which contains a pair of OCT and OCTA volumes from 846 subjects.

</details>

### MVPaint: Synchronized Multi-View Diffusion for Painting Anything 3D.
- **链接**: [arXiv:2411.02336](https://arxiv.org/abs/2411.02336) · 📚 被引 10
- **作者**: Wei Cheng, Juncheng Mu, Xianfang Zeng, Xin Chen, Anqi Pang, Chi Zhang et al.
- **🏷️ 机构**: StepFun, Shanghai AI Laboratory, ByteDance
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Texturing is a crucial step in the 3D asset production workflow, which enhances the visual appeal and diversity of 3D assets. Despite recent advancements in Text-to-Texture (T2T) generation, existing methods often yield subpar results, primarily due to local discontinuities, inconsistencies across multiple views, and their heavy dependence on UV unwrapping outcomes. To tackle these challenges, we propose a novel generation-refinement 3D texturing framework called MVPaint, which can generate high-resolution, seamless textures while emphasizing multi-view consistency. MVPaint mainly consists of three key modules. 1) Synchronized Multi-view Generation (SMG). Given a 3D mesh model, MVPaint first simultaneously generates multi-view images by employing an SMG model, which leads to coarse texturing results with unpainted parts due to missing observations. 2) Spatial-aware 3D Inpainting (S3I). To ensure complete 3D texturing, we introduce the S3I method, specifically designed to effectively texture previously unobserved areas. 3) UV Refinement (UVR). Furthermore, MVPaint employs a UVR module to improve the texture quality in the UV space, which first performs a UV-space Super-Resolution, followed by a Spatial-aware Seam-Smoothing algorithm for revising spatial texturing discontinuities caused by UV unwrapping. Moreover, we establish two T2T evaluation benchmarks: the Objaverse T2T benchmark and the GSO T2T benchmark, based on selected high-quality 3D meshes from the Objaverse dataset and the entire GSO dataset, respectively. Extensive experimental results demonstrate that MVPaint surpasses existing state-of-the-art methods. Notably, MVPaint could generate high-fidelity textures with minimal Janus issues and highly enhanced cross-view consistency.

</details>

### MV-SSM: Multi-View State Space Modeling for 3D Human Pose Estimation.
- **链接**: [arXiv:2509.00649](https://arxiv.org/abs/2509.00649) · 📚 被引 2
- **作者**: Aviral Chharia, Wenbo Gou, Haoye Dong
- **🏷️ 机构**: Carnegie Mellon University, National University of Singapore
- **会议**: CVPR 2025

### QSCA: Quantization with Self-Compensating Auxiliary for Monocular Depth Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2d13e0a4097e44b9f167f2e67aa0214a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jincheol Yang, Jaemin Choi, Matti Zinke, Suk-Ju Kang
- **🏷️ 机构**: Sogang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incomplete multi-view clustering (IMVC), missing data induce prototype shifts within views and semantic inconsistencies across views. A feasible solution is to explore cross-view consistency in paired complete observations, further imputing and aligning the similarity relationships inherently shared across views. Nevertheless, existing methods are constrained by two-tiered limitations: (1) Neither instance- nor cluster-level consistency learning construct a semantic space shared across views to learn consensus semantics. The former enforces cross-view instances alignment, and wrongly regards unpaired observations with semantic consistency as negative pairs; the latter focuses on cross-view cluster counterparts while coarsely handling fine-grained intra-cluster relationships within views. (2) Excessive reliance on consistency results in unreliable imputation and alignment without incorporating view-specific cluster information. Thus, we propose an IMVC framework, imputation- and alignment-free for consensus semantics learning (FreeCSL). To bridge semantic gaps across all observations, we learn consensus prototypes from available data to discover a shared space, where semantically similar observations are pulled closer for consensus semantics learning. To capture semantic relationships within specific views, we design a heuristic graph clustering based on modularity to recover cluster structure with intra-cluster compactness and inter-cluster separation for cluster semantics enhancement. Extensive experiments demonstrate, compared to state-of-the-art competitors, FreeCSL achieves more confident and robust assignments on IMVC task.

</details>

### CaMuViD: Calibration-Free Multi-View Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Daryani_CaMuViD_Calibration-Free_Multi-View_Detection_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Amir Etefaghi Daryani, M. Usman Maqbool Bhutta, Byron Hernandez, Henry Medeiros
- **🏷️ 机构**: University of Florida
- **会议**: CVPR 2025

### MammAlps: A Multi-view Video Behavior Monitoring Dataset of Wild Mammals in the Swiss Alps.
- **链接**: [arXiv:2503.18223](https://arxiv.org/abs/2503.18223) · [代码](https://github.com/eceo-epfl/MammAlps) · 📚 被引 1
- **作者**: Valentin Gabeff, Haozhe Qi, Brendan Flaherty, Gencer Sumbul, Alexander Mathis, Devis Tuia
- **🏷️ 机构**: Ecole Polytechnique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL),Switzerland
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monitoring wildlife is essential for ecology and ethology, especially in light of the increasing human impact on ecosystems. Camera traps have emerged as habitat-centric sensors enabling the study of wildlife populations at scale with minimal disturbance. However, the lack of annotated video datasets limits the development of powerful video understanding models needed to process the vast amount of fieldwork data collected. To advance research in wild animal behavior monitoring we present MammAlps, a multimodal and multi-view dataset of wildlife behavior monitoring from 9 camera-traps in the Swiss National Park. MammAlps contains over 14 hours of video with audio, 2D segmentation maps and 8.5 hours of individual tracks densely labeled for species and behavior. Based on 6135 single animal clips, we propose the first hierarchical and multimodal animal behavior recognition benchmark using audio, video and reference scene segmentation maps as inputs. Furthermore, we also propose a second ecology-oriented benchmark aiming at identifying activities, species, number of individuals and meteorological conditions from 397 multi-view and long-term ecological events, including false positive triggers. We advocate that both tasks are complementary and contribute to bridging the gap between machine learning and ecology. Code and data are available at: https://github.com/eceo-epfl/MammAlps

</details>

### Multi-View Pose-Agnostic Change Localization with Zero Labels.
- **链接**: [arXiv:2412.03911](https://arxiv.org/abs/2412.03911) · 📚 被引 1
- **作者**: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald G. Dansereau, Niko Sünderhauf, Dimity Miller
- **🏷️ 机构**: Queensland University of Technology, University of Sydney,ACFR, ARIAM
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous agents often require accurate methods for detecting and localizing changes in their environment, particularly when observations are captured from unconstrained and inconsistent viewpoints. We propose a novel label-free, pose-agnostic change detection method that integrates information from multiple viewpoints to construct a change-aware 3D Gaussian Splatting (3DGS) representation of the scene. With as few as 5 images of the post-change scene, our approach can learn an additional change channel in a 3DGS and produce change masks that outperform single-view techniques. Our change-aware 3D scene representation additionally enables the generation of accurate change masks for unseen viewpoints. Experimental results demonstrate state-of-the-art performance in complex multi-object scenes, achieving a 1.7x and 1.5x improvement in Mean Intersection Over Union and F1 score respectively over other baselines. We also contribute a new real-world dataset to benchmark change detection in diverse challenging scenes in the presence of lighting variations.

</details>

### SplatFlow: Multi-View Rectified Flow Model for 3D Gaussian Splatting Synthesis.
- **链接**: [arXiv:2411.16443](https://arxiv.org/abs/2411.16443) · 📚 被引 5
- **作者**: Hyojun Go, Byeongjun Park, Jiho Jang, Jin-Young Kim, Soonwoo Kwon, Changick Kim
- **🏷️ 机构**: EverEx, KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-based generation and editing of 3D scenes hold significant potential for streamlining content creation through intuitive user interactions. While recent advances leverage 3D Gaussian Splatting (3DGS) for high-fidelity and real-time rendering, existing methods are often specialized and task-focused, lacking a unified framework for both generation and editing. In this paper, we introduce SplatFlow, a comprehensive framework that addresses this gap by enabling direct 3DGS generation and editing. SplatFlow comprises two main components: a multi-view rectified flow (RF) model and a Gaussian Splatting Decoder (GSDecoder). The multi-view RF model operates in latent space, generating multi-view images, depths, and camera poses simultaneously, conditioned on text prompts, thus addressing challenges like diverse scene scales and complex camera trajectories in real-world settings. Then, the GSDecoder efficiently translates these latent outputs into 3DGS representations through a feed-forward 3DGS method. Leveraging training-free inversion and inpainting techniques, SplatFlow enables seamless 3DGS editing and supports a broad range of 3D tasks-including object editing, novel view synthesis, and camera pose estimation-within a unified framework without requiring additional complex pipelines. We validate SplatFlow's capabilities on the MVImgNet and DL3DV-7K datasets, demonstrating its versatility and effectiveness in various 3D generation, editing, and inpainting-based tasks.

</details>

### Multi-view Reconstruction via SfM-guided Monocular Depth Estimation.
- **链接**: [arXiv:2503.14483](https://arxiv.org/abs/2503.14483) · 📚 被引 10
- **作者**: Haoyu Guo, He Zhu, Sida Peng, Haotong Lin, Yunzhi Yan, Tao Xie et al.
- **🏷️ 机构**: Zhejiang University, Beijing Normal Univeristy
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a new method for multi-view geometric reconstruction. In recent years, large vision models have rapidly developed, performing excellently across various tasks and demonstrating remarkable generalization capabilities. Some works use large vision models for monocular depth estimation, which have been applied to facilitate multi-view reconstruction tasks in an indirect manner. Due to the ambiguity of the monocular depth estimation task, the estimated depth values are usually not accurate enough, limiting their utility in aiding multi-view reconstruction. We propose to incorporate SfM information, a strong multi-view prior, into the depth estimation process, thus enhancing the quality of depth prediction and enabling their direct application in multi-view geometric reconstruction. Experimental results on public real-world datasets show that our method significantly improves the quality of depth estimation compared to previous monocular depth estimation works. Additionally, we evaluate the reconstruction quality of our approach in various types of scenes including indoor, streetscape, and aerial views, surpassing state-of-the-art MVS methods. The code and supplementary materials are available at https://zju3dv.github.io/murre/ .

</details>

### Geometry-guided Online 3D Video Synthesis with Multi-View Temporal Consistency.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ha_Geometry-guided_Online_3D_Video_Synthesis_with_Multi-View_Temporal_Consistency_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Hyunho Ha, Lei Xiao, Christian Richardt, Thu Nguyen-Phuoc, Changil Kim, Min H. Kim et al.
- **🏷️ 机构**: KAIST, Meta
- **会议**: CVPR 2025

### MVSAnywhere: Zero-Shot Multi-View Stereo.
- **链接**: [arXiv:2503.22430](https://arxiv.org/abs/2503.22430) · 📚 被引 13
- **作者**: Sergio Izquierdo, Mohamed Sayed, Michael Firman, Guillermo Garcia-Hernando, Daniyar Turmukhambetov, Javier Civera et al.
- **🏷️ 机构**: Universidad de Zaragoza,I3A, Niantic, University of Edinburgh
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Computing accurate depth from multiple views is a fundamental and longstanding challenge in computer vision. However, most existing approaches do not generalize well across different domains and scene types (e.g. indoor vs. outdoor). Training a general-purpose multi-view stereo model is challenging and raises several questions, e.g. how to best make use of transformer-based architectures, how to incorporate additional metadata when there is a variable number of input views, and how to estimate the range of valid depths which can vary considerably across different scenes and is typically not known a priori? To address these issues, we introduce MVSA, a novel and versatile Multi-View Stereo architecture that aims to work Anywhere by generalizing across diverse domains and depth ranges. MVSA combines monocular and multi-view cues with an adaptive cost volume to deal with scale-related issues. We demonstrate state-of-the-art zero-shot depth estimation on the Robust Multi-View Depth Benchmark, surpassing existing multi-view stereo and monocular baselines.

</details>

### Pippo: High-Resolution Multi-View Humans from a Single Image.
- **链接**: [arXiv:2502.07785](https://arxiv.org/abs/2502.07785) · 📚 被引 10
- **作者**: Yash Kant, Ethan Weber, Jin Kyu Kim, Rawal Khirodkar, Su Zhaoen, Julieta Martinez et al.
- **🏷️ 机构**: Meta Reality Labs, University of Toronto
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Pippo, a generative model capable of producing 1K resolution dense turnaround videos of a person from a single casually clicked photo. Pippo is a multi-view diffusion transformer and does not require any additional inputs - e.g., a fitted parametric model or camera parameters of the input image. We pre-train Pippo on 3B human images without captions, and conduct multi-view mid-training and post-training on studio captured humans. During mid-training, to quickly absorb the studio dataset, we denoise several (up to 48) views at low-resolution, and encode target cameras coarsely using a shallow MLP. During post-training, we denoise fewer views at high-resolution and use pixel-aligned controls (e.g., Spatial anchor and Plucker rays) to enable 3D consistent generations. At inference, we propose an attention biasing technique that allows Pippo to simultaneously generate greater than 5 times as many views as seen during training. Finally, we also introduce an improved metric to evaluate 3D consistency of multi-view generations, and show that Pippo outperforms existing works on multi-view human generation from a single image.

</details>

### MVPortrait: Text-Guided Motion and Emotion Control for Multi-view Vivid Portrait Animation.
- **链接**: [arXiv:2503.19383](https://arxiv.org/abs/2503.19383) · 📚 被引 7
- **作者**: Yukang Lin, Hokit Fung, Jianjin Xu, Zeping Ren, Adela S. M. Lau, Guosheng Yin et al.
- **🏷️ 机构**: Tsinghua University, The University of Hong Kong, Carnegie Mellon University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent portrait animation methods have made significant strides in generating realistic lip synchronization. However, they often lack explicit control over head movements and facial expressions, and cannot produce videos from multiple viewpoints, resulting in less controllable and expressive animations. Moreover, text-guided portrait animation remains underexplored, despite its user-friendly nature. We present a novel two-stage text-guided framework, MVPortrait (Multi-view Vivid Portrait), to generate expressive multi-view portrait animations that faithfully capture the described motion and emotion. MVPortrait is the first to introduce FLAME as an intermediate representation, effectively embedding facial movements, expressions, and view transformations within its parameter space. In the first stage, we separately train the FLAME motion and emotion diffusion models based on text input. In the second stage, we train a multi-view video generation model conditioned on a reference portrait image and multi-view FLAME rendering sequences from the first stage. Experimental results exhibit that MVPortrait outperforms existing methods in terms of motion and emotion control, as well as view consistency. Furthermore, by leveraging FLAME as a bridge, MVPortrait becomes the first controllable portrait animation framework that is compatible with text, speech, and video as driving signals.

</details>

### Enhanced Contrastive Learning with Multi-view Longitudinal Data for Chest X-ray Report Generation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Enhanced_Contrastive_Learning_with_Multi-view_Longitudinal_Data_for_Chest_X-ray_CVPR_2025_paper.html)
- **作者**: Kang Liu, Zhuoqi Ma, Xiaolu Kang, Yunan Li, Kun Xie, Zhicheng Jiao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### MVBoost: Boost 3D Reconstruction with Multi-View Refinement.
- **链接**: [arXiv:2411.17772](https://arxiv.org/abs/2411.17772) · 📚 被引 1
- **作者**: Xiangyu Liu, Xiaomei Zhang, Zhiyuan Ma, Xiangyu Zhu, Zhen Lei
- **🏷️ 机构**: Chinese Academy of Sciences,MAIS, Institute of Automation,Beijing,China, The Hong Kong Polytechnic University,Hong Kong,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in 3D object reconstruction have been remarkable, yet most current 3D models rely heavily on existing 3D datasets. The scarcity of diverse 3D datasets results in limited generalization capabilities of 3D reconstruction models. In this paper, we propose a novel framework for boosting 3D reconstruction with multi-view refinement (MVBoost) by generating pseudo-GT data. The key of MVBoost is combining the advantages of the high accuracy of the multi-view generation model and the consistency of the 3D reconstruction model to create a reliable data source. Specifically, given a single-view input image, we employ a multi-view diffusion model to generate multiple views, followed by a large 3D reconstruction model to produce consistent 3D data. MVBoost then adaptively refines these multi-view images, rendered from the consistent 3D data, to build a large-scale multi-view dataset for training a feed-forward 3D reconstruction model. Additionally, the input view optimization is designed to optimize the corresponding viewpoints based on the user's input image, ensuring that the most important viewpoint is accurately tailored to the user's needs. Extensive evaluations demonstrate that our method achieves superior reconstruction results and robust generalization compared to prior works.

</details>

### 3DEnhancer: Consistent Multi-View Diffusion for 3D Enhancement.
- **链接**: [arXiv:2412.18565](https://arxiv.org/abs/2412.18565) · 📚 被引 4
- **作者**: Yihang Luo, Shangchen Zhou, Yushi Lan, Xingang Pan, Chen Change Loy
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite advances in neural rendering, due to the scarcity of high-quality 3D datasets and the inherent limitations of multi-view diffusion models, view synthesis and 3D model generation are restricted to low resolutions with suboptimal multi-view consistency. In this study, we present a novel 3D enhancement pipeline, dubbed 3DEnhancer, which employs a multi-view latent diffusion model to enhance coarse 3D inputs while preserving multi-view consistency. Our method includes a pose-aware encoder and a diffusion-based denoiser to refine low-quality multi-view images, along with data augmentation and a multi-view attention module with epipolar aggregation to maintain consistent, high-quality 3D outputs across views. Unlike existing video-based approaches, our model supports seamless multi-view enhancement with improved coherence across diverse viewing angles. Extensive evaluations show that 3DEnhancer significantly outperforms existing methods, boosting both multi-view enhancement and per-instance 3D optimization tasks.

</details>

### SIR-DIFF: Sparse Image Sets Restoration with Multi-View Diffusion Model.
- **链接**: [arXiv:2503.14463](https://arxiv.org/abs/2503.14463) · 📚 被引 1
- **作者**: Yucheng Mao, Boyang Wang, Nilesh Kulkarni, Jeong Joon Park
- **🏷️ 机构**: University of Michigan,Ann Arbor
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The computer vision community has developed numerous techniques for digitally restoring true scene information from single-view degraded photographs, an important yet extremely ill-posed task. In this work, we tackle image restoration from a different perspective by jointly denoising multiple photographs of the same scene. Our core hypothesis is that degraded images capturing a shared scene contain complementary information that, when combined, better constrains the restoration problem. To this end, we implement a powerful multi-view diffusion model that jointly generates uncorrupted views by extracting rich information from multi-view relationships. Our experiments show that our multi-view approach outperforms existing single-view image and even video-based methods on image deblurring and super-resolution tasks. Critically, our model is trained to output 3D consistent images, making it a promising tool for applications requiring robust multi-view integration, such as 3D reconstruction or pose estimation.

</details>

### PMNI: Pose-free Multi-view Normal Integration for Reflective and Textureless Surface Reconstruction.
- **链接**: [arXiv:2504.08410](https://arxiv.org/abs/2504.08410) · 📚 被引 1
- **作者**: Mingzhi Pei, Xu Cao, Xiangyi Wang, Heng Guo, Zhanyu Ma
- **🏷️ 机构**: Beijing University of Posts and Telecommunications, Independent Researcher
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reflective and textureless surfaces remain a challenge in multi-view 3D reconstruction. Both camera pose calibration and shape reconstruction often fail due to insufficient or unreliable cross-view visual features. To address these issues, we present PMNI (Pose-free Multi-view Normal Integration), a neural surface reconstruction method that incorporates rich geometric information by leveraging surface normal maps instead of RGB images. By enforcing geometric constraints from surface normals and multi-view shape consistency within a neural signed distance function (SDF) optimization framework, PMNI simultaneously recovers accurate camera poses and high-fidelity surface geometry. Experimental results on synthetic and real-world datasets show that our method achieves state-of-the-art performance in the reconstruction of reflective surfaces, even without reliable initial camera poses.

</details>

### IMFine: 3D Inpainting via Geometry-guided Multi-view Refinement.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shi_IMFine_3D_Inpainting_via_Geometry-guided_Multi-view_Refinement_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Zhihao Shi, Dong Huo, Yuhongze Zhou, Yan Min, Juwei Lu, Xinxin Zuo
- **🏷️ 机构**: Huawei Canada Research Institute, University of Alberta, McMaster University
- **会议**: CVPR 2025

### ROLL: Robust Noisy Pseudo-label Learning for Multi-View Clustering with Noisy Correspondence.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_ROLL_Robust_Noisy_Pseudo-label_Learning_for_Multi-View_Clustering_with_Noisy_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Yuan Sun, Yongxiang Li, Zhenwen Ren, Guiduo Duan, Dezhong Peng, Peng Hu
- **🏷️ 机构**: Sichuan University,College of Computer Science, Southwest University of Science and Technology,School of Computer Science and Technology, University of Electronic Science and Technology of China,School of Computer Science and Engineering
- **会议**: CVPR 2025

### GAF: Gaussian Avatar Reconstruction from Monocular Videos via Multi-view Diffusion.
- **链接**: [arXiv:2412.10209](https://arxiv.org/abs/2412.10209) · 📚 被引 14
- **作者**: Jiapeng Tang, Davide Davoli, Tobias Kirschstein, Liam Schoneveld, Matthias Nießner
- **🏷️ 机构**: Technical University of Munich, Toyota Motor Europe NV/SA, Woven by Toyota
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel approach for reconstructing animatable 3D Gaussian avatars from monocular videos captured by commodity devices like smartphones. Photorealistic 3D head avatar reconstruction from such recordings is challenging due to limited observations, which leaves unobserved regions under-constrained and can lead to artifacts in novel views. To address this problem, we introduce a multi-view head diffusion model, leveraging its priors to fill in missing regions and ensure view consistency in Gaussian splatting renderings. To enable precise viewpoint control, we use normal maps rendered from FLAME-based head reconstruction, which provides pixel-aligned inductive biases. We also condition the diffusion model on VAE features extracted from the input image to preserve facial identity and appearance details. For Gaussian avatar reconstruction, we distill multi-view diffusion priors by using iteratively denoised images as pseudo-ground truths, effectively mitigating over-saturation issues. To further improve photorealism, we apply latent upsampling priors to refine the denoised latent before decoding it into an image. We evaluate our method on the NeRSemble dataset, showing that GAF outperforms previous state-of-the-art methods in novel view synthesis. Furthermore, we demonstrate higher-fidelity avatar reconstructions from monocular videos captured on commodity devices.

</details>

### CAP4D: Creating Animatable 4D Portrait Avatars with Morphable Multi-View Diffusion Models.
- **链接**: [arXiv:2412.12093](https://arxiv.org/abs/2412.12093) · 📚 被引 15
- **作者**: Felix Taubner, Ruihang Zhang, Mathieu Tuli, David B. Lindell
- **🏷️ 机构**: University of Toronto, LG Electronics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing photorealistic and dynamic portrait avatars from images is essential to many applications including advertising, visual effects, and virtual reality. Depending on the application, avatar reconstruction involves different capture setups and constraints $-$ for example, visual effects studios use camera arrays to capture hundreds of reference images, while content creators may seek to animate a single portrait image downloaded from the internet. As such, there is a large and heterogeneous ecosystem of methods for avatar reconstruction. Techniques based on multi-view stereo or neural rendering achieve the highest quality results, but require hundreds of reference images. Recent generative models produce convincing avatars from a single reference image, but visual fidelity yet lags behind multi-view techniques. Here, we present CAP4D: an approach that uses a morphable multi-view diffusion model to reconstruct photoreal 4D (dynamic 3D) portrait avatars from any number of reference images (i.e., one to 100) and animate and render them in real time. Our approach demonstrates state-of-the-art performance for single-, few-, and multi-image 4D portrait avatar reconstruction, and takes steps to bridge the gap in visual fidelity between single-image and multi-view reconstruction techniques.

</details>

### MAGE : Single Image to Material-Aware 3D via the Multi-View G-Buffer Estimation Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_MAGE__Single_Image_to_Material-Aware_3D_via_the_Multi-View_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Haoyuan Wang, Zhenwei Wang, Xiaoxiao Long, Cheng Lin, Gerhard P. Hancke, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong, Nanjing University, The University of Hong Kong
- **会议**: CVPR 2025

### CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models.
- **链接**: [arXiv:2411.18613](https://arxiv.org/abs/2411.18613) · 📚 被引 34
- **作者**: Rundi Wu, Ruiqi Gao, Ben Poole, Alex Trevithick, Changxi Zheng, Jonathan T. Barron et al.
- **🏷️ 机构**: Google DeepMind, Columbia University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present CAT4D, a method for creating 4D (dynamic 3D) scenes from monocular video. CAT4D leverages a multi-view video diffusion model trained on a diverse combination of datasets to enable novel view synthesis at any specified camera poses and timestamps. Combined with a novel sampling approach, this model can transform a single monocular video into a multi-view video, enabling robust 4D reconstruction via optimization of a deformable 3D Gaussian representation. We demonstrate competitive performance on novel view synthesis and dynamic scene reconstruction benchmarks, and highlight the creative capabilities for 4D scene generation from real or generated videos. See our project page for results and interactive demos: https://cat-4d.github.io/.

</details>

### DriveScape: High-Resolution Driving Video Generation by Multi-View Feature Fusion.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DriveScape_High-Resolution_Driving_Video_Generation_by_Multi-View_Feature_Fusion_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Wei Wu, Xi Guo, Weixuan Tang, Tingxuan Huang, Chiyu Wang, Chenjing Ding
- **🏷️ 机构**: Tsinghua University, Sensetime Research, Northeastern University
- **会议**: CVPR 2025

### RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images.
- **链接**: [arXiv:2503.14198](https://arxiv.org/abs/2503.14198) · [代码](https://github.com/iSEE-Laboratory/RoGSplat) · 📚 被引 3
- **作者**: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China, South China University of Technology, Hong Kong University of Science and Technology (Guangzhou)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents RoGSplat, a novel approach for synthesizing high-fidelity novel views of unseen human from sparse multi-view images, while requiring no cumbersome per-subject optimization. Unlike previous methods that typically struggle with sparse views with few overlappings and are less effective in reconstructing complex human geometry, the proposed method enables robust reconstruction in such challenging conditions. Our key idea is to lift SMPL vertices to dense and reliable 3D prior points representing accurate human body geometry, and then regress human Gaussian parameters based on the points. To account for possible misalignment between SMPL model and images, we propose to predict image-aligned 3D prior points by leveraging both pixel-level features and voxel-level features, from which we regress the coarse Gaussians. To enhance the ability to capture high-frequency details, we further render depth maps from the coarse 3D Gaussians to help regress fine-grained pixel-wise Gaussians. Experiments on several benchmark datasets demonstrate that our method outperforms state-of-the-art methods in novel view synthesis and cross-dataset generalization. Our code is available at https://github.com/iSEE-Laboratory/RoGSplat.

</details>

### EASEMVC: Efficient Dual Selection Mechanism for Deep Multi-View Clustering.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xiao_EASEMVCEfficient_Dual_Selection_Mechanism_for_Deep_Multi-View_Clustering_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Baili Xiao, Zhibin Dong, Ke Liang, Suyuan Liu, Siwei Wang, Tianrui Liu et al.
- **🏷️ 机构**: National University of Defense Technology,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: CVPR 2025

### Deep Fair Multi-View Clustering with Attention KAN.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Deep_Fair_Multi-View_Clustering_with_Attention_KAN_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Haiming Xu, Qianqian Wang, Boyue Wang, Quanxue Gao
- **🏷️ 机构**: Xidian University, Beijing University of Technology
- **会议**: CVPR 2025

### A Hubness Perspective on Representation Learning for Graph-Based Multi-View Clustering.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_A_Hubness_Perspective_on_Representation_Learning_for_Graph-Based_Multi-View_Clustering_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Zheming Xu, He Liu, Congyan Lang, Tao Wang, Yidong Li, Michael C. Kampffmeyer
- **🏷️ 机构**: Beijing Jiaotong University,School of Computer Science &amp; Technology, UiT The Arctic University of Norway,Department of Physics and Technology
- **会议**: CVPR 2025

### SKDream: Controllable Multi-view and 3D Generation with Arbitrary Skeletons.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_SKDream_Controllable_Multi-view_and_3D_Generation_with_Arbitrary_Skeletons_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Yuanyou Xu, Zongxin Yang, Yi Yang
- **🏷️ 机构**: ReLER, CCAI, Zhejiang University, DBMI, HMS, Harvard University
- **会议**: CVPR 2025

### MITracker: Multi-View Integration for Visual Object Tracking.
- **链接**: [arXiv:2502.20111](https://arxiv.org/abs/2502.20111) · 📚 被引 7
- **作者**: Mengjie Xu, Yitao Zhu, Haotian Jiang, Jiaming Li, Zhenrong Shen, Sheng Wang et al.
- **🏷️ 机构**: ShanghaiTech University,School of Biomedical Engineering &#x0026; State Key Laboratory of Advanced Medical Materials and Devices, Shanghai Jiao Tong University,School of Biomedical Engineering
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view object tracking (MVOT) offers promising solutions to challenges such as occlusion and target loss, which are common in traditional single-view tracking. However, progress has been limited by the lack of comprehensive multi-view datasets and effective cross-view integration methods. To overcome these limitations, we compiled a Multi-View object Tracking (MVTrack) dataset of 234K high-quality annotated frames featuring 27 distinct objects across various scenes. In conjunction with this dataset, we introduce a novel MVOT method, Multi-View Integration Tracker (MITracker), to efficiently integrate multi-view object features and provide stable tracking outcomes. MITracker can track any object in video frames of arbitrary length from arbitrary viewpoints. The key advancements of our method over traditional single-view approaches come from two aspects: (1) MITracker transforms 2D image features into a 3D feature volume and compresses it into a bird's eye view (BEV) plane, facilitating inter-view information fusion; (2) we propose an attention mechanism that leverages geometric information from fused 3D feature volume to refine the tracking results at each view. MITracker outperforms existing methods on the MVTrack and GMTD datasets, achieving state-of-the-art performance. The code and the new dataset will be available at https://mii-laboratory.github.io/MITracker/.

</details>

### Robust-MVTON: Learning Cross-Pose Feature Alignment and Fusion for Robust Multi-View Virtual Try-On.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Robust-MVTON_Learning_Cross-Pose_Feature_Alignment_and_Fusion_for_Robust_Multi-View_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Nannan Zhang, Yijiang Li, Dong Du, Zheng Chong, Zhengwentai Sun, Jianhao Zeng et al.
- **🏷️ 机构**: CUHKSZ, UCSD, NJUST
- **会议**: CVPR 2025

### CoMatcher: Multi-View Collaborative Feature Matching.
- **链接**: [arXiv:2504.01872](https://arxiv.org/abs/2504.01872) · 📚 被引 5
- **作者**: Jintao Zhang, Zimin Xia, Mingyue Dong, Shuhan Shen, Linwei Yue, Xianwei Zheng
- **🏷️ 机构**: Wuhan University,The State Key Lab. LIESMARS, &#x00C9;cole Polytechnique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL), Chinese Academy of Sciences
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a multi-view collaborative matching strategy for reliable track construction in complex scenarios. We observe that the pairwise matching paradigms applied to image set matching often result in ambiguous estimation when the selected independent pairs exhibit significant occlusions or extreme viewpoint changes. This challenge primarily stems from the inherent uncertainty in interpreting intricate 3D structures based on limited two-view observations, as the 3D-to-2D projection leads to significant information loss. To address this, we introduce CoMatcher, a deep multi-view matcher to (i) leverage complementary context cues from different views to form a holistic 3D scene understanding and (ii) utilize cross-view projection consistency to infer a reliable global solution. Building on CoMatcher, we develop a groupwise framework that fully exploits cross-view relationships for large-scale matching tasks. Extensive experiments on various complex scenarios demonstrate the superiority of our method over the mainstream two-view matching paradigm.

</details>

### MonoInstance: Enhancing Monocular Priors via Multi-view Instance Alignment for Neural Rendering and Reconstruction.
- **链接**: [arXiv:2503.18363](https://arxiv.org/abs/2503.18363) · 📚 被引 10
- **作者**: Wenyuan Zhang, Yixiao Yang, Han Huang, Liang Han, Kanle Shi, Yu-Shen Liu et al.
- **🏷️ 机构**: Tsinghua University,School of Software,Beijing,China, Kuaishou Technology,Beijing,China, Wayne State University,Department of Computer Science,Detroit,USA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth priors have been widely adopted by neural rendering in multi-view based tasks such as 3D reconstruction and novel view synthesis. However, due to the inconsistent prediction on each view, how to more effectively leverage monocular cues in a multi-view context remains a challenge. Current methods treat the entire estimated depth map indiscriminately, and use it as ground truth supervision, while ignoring the inherent inaccuracy and cross-view inconsistency in monocular priors. To resolve these issues, we propose MonoInstance, a general approach that explores the uncertainty of monocular depths to provide enhanced geometric priors for neural rendering and reconstruction. Our key insight lies in aligning each segmented instance depths from multiple views within a common 3D space, thereby casting the uncertainty estimation of monocular depths into a density measure within noisy point clouds. For high-uncertainty areas where depth priors are unreliable, we further introduce a constraint term that encourages the projected instances to align with corresponding instance masks on nearby views. MonoInstance is a versatile strategy which can be seamlessly integrated into various multi-view neural rendering frameworks. Our experimental results demonstrate that MonoInstance significantly improves the performance in both reconstruction and novel view synthesis under various benchmarks.

</details>

### Attribute-Missing Multi-view Graph Clustering.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Attribute-Missing_Multi-view_Graph_Clustering_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Bowen Zhao, Qianqian Wang, Zhengming Ding, Quanxue Gao
- **🏷️ 机构**: Xidian University, Tulane University
- **会议**: CVPR 2025

### SceneCrafter: Controllable Multi-View Driving Scene Editing.
- **链接**: [arXiv:2506.19488](https://arxiv.org/abs/2506.19488) · 📚 被引 1
- **作者**: Zehao Zhu, Yuliang Zou, Chiyu Max Jiang, Bo Sun, Vincent Casser, Xiukun Huang et al.
- **🏷️ 机构**: Waymo, Johns Hopkins University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Simulation is crucial for developing and evaluating autonomous vehicle (AV) systems. Recent literature builds on a new generation of generative models to synthesize highly realistic images for full-stack simulation. However, purely synthetically generated scenes are not grounded in reality and have difficulty in inspiring confidence in the relevance of its outcomes. Editing models, on the other hand, leverage source scenes from real driving logs, and enable the simulation of different traffic layouts, behaviors, and operating conditions such as weather and time of day. While image editing is an established topic in computer vision, it presents fresh sets of challenges in driving simulation: (1) the need for cross-camera 3D consistency, (2) learning ``empty street" priors from driving data with foreground occlusions, and (3) obtaining paired image tuples of varied editing conditions while preserving consistent layout and geometry. To address these challenges, we propose SceneCrafter, a versatile editor for realistic 3D-consistent manipulation of driving scenes captured from multiple cameras. We build on recent advancements in multi-view diffusion models, using a fully controllable framework that scales seamlessly to multi-modality conditions like weather, time of day, agent boxes and high-definition maps. To generate paired data for supervising the editing model, we propose a novel framework on top of Prompt-to-Prompt to generate geometrically consistent synthetic paired data with global edits. We also introduce an alpha-blending framework to synthesize data with local edits, leveraging a model trained on empty street priors through novel masked training and multi-view repaint paradigm. SceneCrafter demonstrates powerful editing capabilities and achieves state-of-the-art realism, controllability, 3D consistency, and scene editing quality compared to existing baselines.

</details>

### All-Day Multi-Camera Multi-Target Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html)
- **作者**: Huijie Fan, Yu Qiao, Yihao Zhen, Tinghui Zhao, Baojie Fan, Qiang Wang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2025

### OmniStereo: Real-time Omnidireactional Depth Estimation with Multiview Fisheye Cameras.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_OmniStereo_Real-time_Omnidireactional_Depth_Estimation_with_Multiview_Fisheye_Cameras_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Jiaxi Deng, Yushen Wang, Haitao Meng, Zuoxun Hou, Yi Chang, Gang Chen
- **🏷️ 机构**: Sun Yat-Sen University,Guangzhou,China, Technical University of Munich,Munich,Germany, Beijing Institute of Space Mechanics and Electricity,Beijing,China
- **会议**: CVPR 2025

### GeoDepth: From Point-to-Depth to Plane-to-Depth Modeling for Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_GeoDepth_From_Point-to-Depth_to_Plane-to-Depth_Modeling_for_Self-Supervised_Monocular_Depth_CVPR_2025_paper.html)
- **作者**: Haifeng Wu, Shuhang Gu, Lixin Duan, Wen Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Align3R: Aligned Monocular Depth Estimation for Dynamic Videos.
- **链接**: [arXiv:2412.03079](https://arxiv.org/abs/2412.03079) · 📚 被引 27
- **作者**: Jiahao Lu, Tianyu Huang, Peng Li, Zhiyang Dou, Cheng Lin, Zhiming Cui et al.
- **🏷️ 机构**: HKUST, CUHK, HKU
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent developments in monocular depth estimation methods enable high-quality depth estimation of single-view images but fail to estimate consistent video depth across different frames. Recent works address this problem by applying a video diffusion model to generate video depth conditioned on the input video, which is training-expensive and can only produce scale-invariant depth values without camera poses. In this paper, we propose a novel video-depth estimation method called Align3R to estimate temporal consistent depth maps for a dynamic video. Our key idea is to utilize the recent DUSt3R model to align estimated monocular depth maps of different timesteps. First, we fine-tune the DUSt3R model with additional estimated monocular depth as inputs for the dynamic scenes. Then, we apply optimization to reconstruct both depth maps and camera poses. Extensive experiments demonstrate that Align3R estimates consistent video depth and camera poses for a monocular video with superior performance than baseline methods.

</details>

### Scalable Autoregressive Monocular Depth Estimation.
- **链接**: [arXiv:2411.11361](https://arxiv.org/abs/2411.11361)
- **作者**: Jinhong Wang, Jian Liu, Dongqi Tang, Weiqiang Wang, Wentong Li, Danny Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper shows that the autoregressive model is an effective and scalable monocular depth estimator. Our idea is simple: We tackle the monocular depth estimation (MDE) task with an autoregressive prediction paradigm, based on two core designs. First, our depth autoregressive model (DAR) treats the depth map of different resolutions as a set of tokens, and conducts the low-to-high resolution autoregressive objective with a patch-wise casual mask. Second, our DAR recursively discretizes the entire depth range into more compact intervals, and attains the coarse-to-fine granularity autoregressive objective in an ordinal-regression manner. By coupling these two autoregressive objectives, our DAR establishes new state-of-the-art (SOTA) on KITTI and NYU Depth v2 by clear margins. Further, our scalable approach allows us to scale the model up to 2.0B and achieve the best RMSE of 1.799 on the KITTI dataset (5% improvement) compared to 1.896 by the current SOTA (Depth Anything). DAR further showcases zero-shot generalization ability on unseen datasets. These results suggest that DAR yields superior performance with an autoregressive prediction paradigm, providing a promising approach to equip modern autoregressive large models (e.g., GPT-4o) with depth estimation capabilities.

</details>

### Vision-Language Embodiment for Monocular Depth Estimation.
- **链接**: [arXiv:2503.16535](https://arxiv.org/abs/2503.16535) · 📚 被引 4
- **作者**: Jinchang Zhang, Guoyu Lu
- **🏷️ 机构**: University of Georgia Binghamton University,Intelligent Vision and Sensing Lab, Binghamton University,Intelligent Vision and Sensing Lab
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Depth estimation is a core problem in robotic perception and vision tasks, but 3D reconstruction from a single image presents inherent uncertainties. Current depth estimation models primarily rely on inter-image relationships for supervised training, often overlooking the intrinsic information provided by the camera itself. We propose a method that embodies the camera model and its physical characteristics into a deep learning model, computing embodied scene depth through real-time interactions with road environments. The model can calculate embodied scene depth in real-time based on immediate environmental changes using only the intrinsic properties of the camera, without any additional equipment. By combining embodied scene depth with RGB image features, the model gains a comprehensive perspective on both geometric and visual details. Additionally, we incorporate text descriptions containing environmental content and depth information as priors for scene understanding, enriching the model's perception of objects. This integration of image and language - two inherently ambiguous modalities - leverages their complementary strengths for monocular depth estimation. The real-time nature of the embodied language and depth prior model ensures that the model can continuously adjust its perception and behavior in dynamic environments. Experimental results show that the embodied depth estimation method enhances model performance across different scenes.

</details>

### SkySense-O: Towards Open-World Remote Sensing Interpretation with Vision-Centric Visual-Language Modeling.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SkySense-O_Towards_Open-World_Remote_Sensing_Interpretation_with_Vision-Centric_Visual-Language_Modeling_CVPR_2025_paper.html) · 📚 被引 24
- **作者**: Qi Zhu, Jiangwei Lao, Deyi Ji, Junwei Luo, Kang Wu, Yingying Zhang et al.
- **🏷️ 机构**: USTC,MoE Key Laboratory of Brain-inspired Intelligent Perception and Cognition, Shanghai Jiaotong University, Wuhan University
- **会议**: CVPR 2025

### Revisiting Audio-Visual Segmentation with Vision-Centric Transformer.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Revisiting_Audio-Visual_Segmentation_with_Vision-Centric_Transformer_CVPR_2025_paper.html)
- **作者**: Shaofei Huang, Rui Ling, Tianrui Hui, Hongyu Li, Xu Zhou, Shifeng Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202025.md)
- OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations. → [3d-detection](../3d-detection/Guideline%202025.md)
- MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers. → [3d-detection](../3d-detection/Guideline%202025.md)
- Boosting Multi-View Indoor 3D Object Detection Via Adaptive 3D Volume Construction. → [3d-detection](../3d-detection/Guideline%202025.md)
