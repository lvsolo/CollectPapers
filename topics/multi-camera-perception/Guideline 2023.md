# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UniFusion: Unified Multi-view Fusion Transformer for Spatial-Temporal Representation in Bird's-Eye-View.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00798) · 📚 被引 50
- **作者**: Zequn Qin, Jingyu Chen, Chao Chen, Xiaozhi Chen, Xi Li
- **🏷️ 机构**: Zhejiang University,College of Computer Science &amp; Technology, DJI
- **会议**: ICCV 2023

### AIDE: A Vision-Driven Multi-View, Multi-Modal, Multi-Tasking Dataset for Assistive Driving Perception.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01871) · 📚 被引 67
- **作者**: Dingkang Yang, Shuai Huang, Zhi Xu, Zhenpeng Li, Shunli Wang, Mingcheng Li et al.
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain shift degrades the performance of object detection models in practical applications. To alleviate the influence of domain shift, plenty of previous work try to decouple and learn the domain-invariant (common) features from source domains via domain adversarial learning (DAL). However, inspired by causal mechanisms, we find that previous methods ignore the implicit insignificant non-causal factors hidden in the common features. This is mainly due to the single-view nature of DAL. In this work, we present an idea to remove non-causal factors from common features by multi-view adversarial training on source domains, because we observe that such insignificant non-causal factors may still be significant in other latent spaces (views) due to the multi-mode structure of data. To summarize, we propose a Multi-view Adversarial Discriminator (MAD) based domain generalization model, consisting of a Spurious Correlations Generator (SCG) that increases the diversity of source domain by random augmentation and a Multi-View Domain Classifier (MVDC) that maps features to multiple latent spaces, such that the non-causal factors are removed and the domain-invariant features are purified. Extensive experiments on six benchmarks show our MAD obtains state-of-the-art performance.

</details>

### Robust Multiview Point Cloud Registration with Reliable Pose Graph Initialization and History Reweighting.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00917) · 📚 被引 45
- **作者**: Haiping Wang, Yuan Liu, Zhen Dong, Yulan Guo, Yu-Shen Liu, Wenping Wang et al.
- **🏷️ 机构**: Wuhan University, The University of Hong Kong, Sun Yat-sen University
- **会议**: CVPR 2023

### Neural Pixel Composition for 3D-4D View Synthesis from Multi-Views.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00036) · 📚 被引 8
- **作者**: Aayush Bansal, Michael Zollhöfer
- **🏷️ 机构**: Reality Labs Research,Pittsburgh,USA
- **会议**: CVPR 2023

### Deep Incomplete Multi-View Clustering with Cross-View Partial Sample and Prototype Alignment.
- **链接**: [arXiv:2303.15689](https://arxiv.org/abs/2303.15689) · 📚 被引 102
- **作者**: Jiaqi Jin, Siwei Wang, Zhibin Dong, Xinwang Liu, En Zhu
- **🏷️ 机构**: School of Computer, National University of Defense Technology,Changsha,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of existing multi-view clustering relies on the assumption of sample integrity across multiple views. However, in real-world scenarios, samples of multi-view are partially available due to data corruption or sensor failure, which leads to incomplete multi-view clustering study (IMVC). Although several attempts have been proposed to address IMVC, they suffer from the following drawbacks: i) Existing methods mainly adopt cross-view contrastive learning forcing the representations of each sample across views to be exactly the same, which might ignore view discrepancy and flexibility in representations; ii) Due to the absence of non-observed samples across multiple views, the obtained prototypes of clusters might be unaligned and biased, leading to incorrect fusion. To address the above issues, we propose a Cross-view Partial Sample and Prototype Alignment Network (CPSPAN) for Deep Incomplete Multi-view Clustering. Firstly, unlike existing contrastive-based methods, we adopt pair-observed data alignment as 'proxy supervised signals' to guide instance-to-instance correspondence construction among views. Then, regarding of the shifted prototypes in IMVC, we further propose a prototype alignment module to achieve incomplete distribution calibration across views. Extensive experimental results showcase the effectiveness of our proposed modules, attaining noteworthy performance improvements when compared to existing IMVC competitors on benchmark datasets.

</details>

### Learning to Fuse Monocular and Multi-view Cues for Multi-frame Depth Estimation in Dynamic Scenes.
- **链接**: [arXiv:2304.08993](https://arxiv.org/abs/2304.08993) · 📚 被引 41
- **作者**: Rui Li, Dong Gong, Wei Yin, Hao Chen, Yu Zhu, Kaixuan Wang et al.
- **🏷️ 机构**: Northwestern Polytechnical University, The University of New South Wales, DJI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-frame depth estimation generally achieves high accuracy relying on the multi-view geometric consistency. When applied in dynamic scenes, e.g., autonomous driving, this consistency is usually violated in the dynamic areas, leading to corrupted estimations. Many multi-frame methods handle dynamic areas by identifying them with explicit masks and compensating the multi-view cues with monocular cues represented as local monocular depth or features. The improvements are limited due to the uncontrolled quality of the masks and the underutilized benefits of the fusion of the two types of cues. In this paper, we propose a novel method to learn to fuse the multi-view and monocular cues encoded as volumes without needing the heuristically crafted masks. As unveiled in our analyses, the multi-view cues capture more accurate geometric information in static areas, and the monocular cues capture more useful contexts in dynamic areas. To let the geometric perception learned from multi-view cues in static areas propagate to the monocular representation in dynamic areas and let monocular cues enhance the representation of multi-view cost volume, we propose a cross-cue fusion (CCF) module, which includes the cross-cue attention (CCA) to encode the spatially non-local relative intra-relations from each source to enhance the representation of the other. Experiments on real-world datasets prove the significant effectiveness and generalization ability of the proposed method.

</details>

### OmniCity: Omnipotent City Understanding with Multi-Level and Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01669) · 📚 被引 30
- **作者**: Weijia Li, Yawen Lai, Linning Xu, Yuanbo Xiangli, Jinhua Yu, Conghui He et al.
- **🏷️ 机构**: Sun Yat-Sen University, SenseTime Research, The Chinese University of Hong Kong
- **会议**: CVPR 2023

### Multi-Sensor Large-Scale Dataset for Multi-View 3D Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02049) · 📚 被引 14
- **作者**: Oleg Voynov, Gleb Bobrovskikh, Pavel A. Karpyshev, Saveliy Galochkin, Andrei-Timotei Ardelean, Arseniy Bozhenko et al.
- **🏷️ 机构**: Skolkovo Institute of Science and Technology
- **会议**: CVPR 2023

### GCFAgg: Global and Cross-View Feature Aggregation for Multi-View Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01902) · 📚 被引 186
- **作者**: Weiqing Yan, Yuanyang Zhang, Chenlei Lv, Chang Tang, Guanghui Yue, Liang Liao et al.
- **🏷️ 机构**: School of Computer and Control Engineering, Yantai University,Yantai,China,264005, College of Computer Science and Software Engineering, Shenzhen University,Shenzhen,China,518060, School of Computer, China University of Geosciences,Wuhan,China,430074
- **会议**: CVPR 2023

### Cross-Guided Optimization of Radiance Fields with Multi-View Image Super-Resolution for High-Resolution Novel View Synthesis.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01196) · 📚 被引 14
- **作者**: Youngho Yoon, Kuk-Jin Yoon
- **🏷️ 机构**: Visual Intelligence Lab., KAIST,Korea
- **会议**: CVPR 2023

### POEM: Reconstructing Hand in a Point Embedded Multi-view Stereo.
- **链接**: [arXiv:2304.04038](https://arxiv.org/abs/2304.04038) · 📚 被引 14
- **作者**: Lixin Yang, Jian Xu, Licheng Zhong, Xinyu Zhan, Zhicheng Wang, Kejian Wu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Nreal
- **会议**: CVPR 2023

### Adaptive Patch Deformation for Textureless-Resilient Multi-View Stereo.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00162) · 📚 被引 35
- **作者**: Yuesong Wang, Zhaojie Zeng, Tao Guan, Wei Yang, Zhuo Chen, Wenkai Liu et al.
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Huazhong University of Science &#x0026; Technology, School of Computer Science &#x0026; Technology, Zhejiang University
- **会议**: CVPR 2023

### MetaViewer: Towards A Unified Multi-View Representation.
- **链接**: [arXiv:2303.06329](https://arxiv.org/abs/2303.06329) · 📚 被引 14
- **作者**: Ren Wang, Haoliang Sun, Yuling Ma, Xiaoming Xi, Yilong Yin
- **🏷️ 机构**: Shandong University, Shandong Jianzhu University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing multi-view representation learning methods typically follow a specific-to-uniform pipeline, extracting latent features from each view and then fusing or aligning them to obtain the unified object representation. However, the manually pre-specify fusion functions and view-private redundant information mixed in features potentially degrade the quality of the derived representation. To overcome them, we propose a novel bi-level-optimization-based multi-view learning framework, where the representation is learned in a uniform-to-specific manner. Specifically, we train a meta-learner, namely MetaViewer, to learn fusion and model the view-shared meta representation in outer-level optimization. Start with this meta representation, view-specific base-learners are then required to rapidly reconstruct the corresponding view in inner-level. MetaViewer eventually updates by observing reconstruction processes from uniform to specific over all views, and learns an optimal fusion scheme that separates and filters out view-private information. Extensive experimental results in downstream tasks such as classification and clustering demonstrate the effectiveness of our method.

</details>

### A Light Touch Approach to Teaching Transformers Multi-view Geometry.
- **链接**: [arXiv:2211.15107](https://arxiv.org/abs/2211.15107) · 📚 被引 10
- **作者**: Yash Bhalgat, João F. Henriques, Andrew Zisserman
- **🏷️ 机构**: University of Oxford,Visual Geometry Group
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers are powerful visual learners, in large part due to their conspicuous lack of manually-specified priors. This flexibility can be problematic in tasks that involve multiple-view geometry, due to the near-infinite possible variations in 3D shapes and viewpoints (requiring flexibility), and the precise nature of projective geometry (obeying rigid laws). To resolve this conundrum, we propose a "light touch" approach, guiding visual Transformers to learn multiple-view geometry but allowing them to break free when needed. We achieve this by using epipolar lines to guide the Transformer's cross-attention maps, penalizing attention values outside the epipolar lines and encouraging higher attention along these lines since they contain geometrically plausible matches. Unlike previous methods, our proposal does not require any camera pose information at test-time. We focus on pose-invariant object instance retrieval, where standard Transformer networks struggle, due to the large differences in viewpoint between query and retrieved images. Experimentally, our method outperforms state-of-the-art approaches at object retrieval, without needing pose information at test-time.

</details>

### Instant Multi-View Head Capture through Learnable Registration.
- **链接**: [arXiv:2306.07437](https://arxiv.org/abs/2306.07437) · 📚 被引 25
- **作者**: Timo Bolkart, Tianye Li, Michael J. Black
- **🏷️ 机构**: MPI for Intelligent Systems,T&#x00FC;bingen, University of Southern California
- **会议**: CVPR 2023

### RIAV-MVS: Recurrent-Indexing an Asymmetric Volume for Multi-View Stereo.
- **链接**: [arXiv:2205.14320](https://arxiv.org/abs/2205.14320) · 📚 被引 12
- **作者**: Changjiang Cai, Pan Ji, Qingan Yan, Yi Xu
- **🏷️ 机构**: OPPO US Research Center, InnoPeak Technology, Inc.
- **会议**: CVPR 2023

### Multi-View Azimuth Stereo via Tangent Space Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00086) · 📚 被引 14
- **作者**: Xu Cao, Hiroaki Santo, Fumio Okura, Yasuyuki Matsushita
- **🏷️ 机构**: Osaka University
- **会议**: CVPR 2023

### GM-NeRF: Learning Generalizable Model-Based Neural Radiance Fields from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01978) · 📚 被引 33
- **作者**: Jianchuan Chen, Wentao Yi, Liqian Ma, Xu Jia, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, ZMO AI Inc.
- **会议**: CVPR 2023

### MAIR: Multi-View Attention Inverse Rendering with 3D Spatially-Varying Lighting Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00811) · 📚 被引 12
- **作者**: Junyong Choi, SeokYeong Lee, Haesol Park, Seung-Won Jung, Ig-Jae Kim, Junghyun Cho
- **🏷️ 机构**: Korea Institute of Science and Technology(KIST), Korea University
- **会议**: CVPR 2023

### 3D Concept Learning and Reasoning from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00888) · 📚 被引 42
- **作者**: Yining Hong, Chunru Lin, Yilun Du, Zhenfang Chen, Joshua B. Tenenbaum, Chuang Gan
- **🏷️ 机构**: UCLA, Shanghai Jiaotong University, MIT CSAIL
- **会议**: CVPR 2023

### StyleGAN Salon: Multi-View Latent Optimization for Pose-Invariant Hairstyle Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00832) · 📚 被引 10
- **作者**: Sasikarn Khwanmuang, Pakkapon Phongthawee, Patsorn Sangkloy, Supasorn Suwajanakorn
- **🏷️ 机构**: VISTEC,Thailand, Phranakhon Rajabhat University,Thailand
- **会议**: CVPR 2023

### Multi-view Inverse Rendering for Large-scale Real-world Indoor Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01203) · 📚 被引 25
- **作者**: Zhen Li, Lingli Wang, Mofang Cheng, Cihui Pan, Jiaqi Yang
- **🏷️ 机构**: Realsee, Northwestern Polytechnical University
- **会议**: CVPR 2023

### NeuralUDF: Learning Unsigned Distance Fields for Multi-View Reconstruction of Surfaces with Arbitrary Topologies.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01996) · 📚 被引 67
- **作者**: Xiaoxiao Long, Cheng Lin, Lingjie Liu, Yuan Liu, Peng Wang, Christian Theobalt et al.
- **🏷️ 机构**: The University of Hong Kong, Tencent Games, Max Planck Institute for Informatics
- **会议**: CVPR 2023

### NeAT: Learning Neural Implicit Surfaces with Arbitrary Topologies from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00032) · 📚 被引 42
- **作者**: Xiaoxu Meng, Weikai Chen, Bo Yang
- **🏷️ 机构**: Digital Content Technology Center, Tencent Games
- **会议**: CVPR 2023

### I2MVFormer: Large Language Model Generated Multi-View Document Supervision for Zero-Shot Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01456) · 📚 被引 77
- **作者**: Muhammad Ferjad Naeem, Muhammad Gul Zain Ali Khan, Yongqin Xian, Muhammad Zeshan Afzal, Didier Stricker, Luc Van Gool et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, TUKL, Google
- **会议**: CVPR 2023

### VolRecon: Volume Rendering of Signed Ray Distance Functions for Generalizable Multi-View Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01601) · 📚 被引 52
- **作者**: Yufan Ren, Fangjinhua Wang, Tong Zhang, Marc Pollefeys, Sabine Süsstrunk
- **🏷️ 机构**: IVRL IC EPFL, ETH Zurich,Department of Computer Science
- **会议**: CVPR 2023

### PermutoSDF: Fast Multi-View Reconstruction with Implicit Surfaces Using Permutohedral Lattices.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00818) · 📚 被引 72
- **作者**: Radu Alexandru Rosu, Sven Behnke
- **🏷️ 机构**: University of Bonn,Germany
- **会议**: CVPR 2023

### BKinD-3D: Self-Supervised 3D Keypoint Discovery from Multi-View Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00869)
- **作者**: Jennifer J. Sun, Lili Karashchuk, Amil Dravid, Serim Ryou, Sonia Fereidooni, John C. Tuthill et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Sample-level Multi-view Graph Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02295) · 📚 被引 48
- **作者**: Yuze Tan, Yixi Liu, Shudong Huang, Wentao Feng, Jiancheng Lv
- **🏷️ 机构**: Sichuan University
- **会议**: CVPR 2023

> The mechanisms behind the success of multi-view self-supervised learning (MVSSL) are not yet fully understood. Contrastive MVSSL methods have been studied through the lens of InfoNCE, a lower bound of the Mutual Information (MI). However, the relation between other MVSSL methods and MI remains unclear. We consider a different lower bound on the MI consisting of an entropy and a reconstruction term (ER), and analyze the main MVSSL families through its lens. Through this ER bound, we show that clustering-based methods such as DeepCluster and SwAV maximize the MI. We also re-interpret the mechanisms of distillation-based approaches such as BYOL and DINO, showing that they explicitly maximize the reconstruction term and implicitly encourage a stable entropy, and we confirm this empirically. We show that replacing the objectives of common MVSSL methods with this ER bound achieves competitive performance, while making them stable when training with smaller batch sizes or smaller exponential moving average (EMA) coefficients. Github repo: https://github.com/apple/ml-entropy-reconstruction.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning is a central component in recent approaches to deep multi-view clustering (MVC). However, we find large variations in the development of self-supervision-based methods for deep MVC, potentially slowing the progress of the field. To address this, we present DeepMVC, a unified framework for deep MVC that includes many recent methods as instances. We leverage our framework to make key observations about the effect of self-supervision, and in particular, drawbacks of aligning representations with contrastive learning. Further, we prove that contrastive alignment can negatively influence cluster separability, and that this effect becomes worse when the number of views increases. Motivated by our findings, we develop several new DeepMVC instances with new forms of self-supervision. We conduct extensive experiments and find that (i) in line with our theoretical findings, contrastive alignments decreases performance on datasets with many views; (ii) all methods benefit from some form of self-supervision; and (iii) our new instances outperform previous methods on several datasets. Based on our results, we suggest several promising directions for future research. To enhance the openness of the field, we provide an open-source implementation of DeepMVC, including recent models and our new instances. Our implementation includes a consistent evaluation protocol, facilitating fair and accurate evaluation of methods and components.

</details>

### Highly Confident Local Structure Based Consensus Graph Learning for Incomplete Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01508) · 📚 被引 51
- **作者**: Jie Wen, Chengliang Liu, Gehui Xu, Zhihao Wu, Chao Huang, Lunke Fei et al.
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen Key Laboratory of Visual Object Detection and Recognition,Shenzhen,China, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University,Shenzhen,China, School of Computer Science and Technology, Guangdong University of Technology,Guangzhou,China
- **会议**: CVPR 2023

### CutMIB: Boosting Light Field Super-Resolution via Multi-View Image Blending.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00167) · 📚 被引 51
- **作者**: Zeyu Xiao, Yutong Liu, Ruisheng Gao, Zhiwei Xiong
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2023

### Exploring and Exploiting Uncertainty for Incomplete Multi-View Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01903) · 📚 被引 44
- **作者**: Mengyao Xie, Zongbo Han, Changqing Zhang, Yichen Bai, Qinghua Hu
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University
- **会议**: CVPR 2023

### High-fidelity 3D GAN Inversion by Pseudo-multi-view Optimization.
- **链接**: [arXiv:2211.15662](https://arxiv.org/abs/2211.15662) · 📚 被引 51
- **作者**: Jiaxin Xie, Hao Ouyang, Jingtan Piao, Chenyang Lei, Qifeng Chen
- **🏷️ 机构**: HKUST, CUHK,MMLab, CAIR, HKISI-CAS
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a high-fidelity 3D generative adversarial network (GAN) inversion framework that can synthesize photo-realistic novel views while preserving specific details of the input image. High-fidelity 3D GAN inversion is inherently challenging due to the geometry-texture trade-off in 3D inversion, where overfitting to a single view input image often damages the estimated geometry during the latent optimization. To solve this challenge, we propose a novel pipeline that builds on the pseudo-multi-view estimation with visibility analysis. We keep the original textures for the visible parts and utilize generative priors for the occluded parts. Extensive experiments show that our approach achieves advantageous reconstruction and novel view synthesis quality over state-of-the-art methods, even for images with out-of-distribution textures. The proposed pipeline also enables image attribute editing with the inverted latent code and 3D-aware texture modification. Our approach enables high-fidelity 3D rendering from a single image, which is promising for various applications of AI-generated 3D content.

</details>

### NEF: Neural Edge Fields for 3D Parametric Curve Reconstruction from Multi-View Images.
- **链接**: [arXiv:2303.07653](https://arxiv.org/abs/2303.07653) · 📚 被引 35
- **作者**: Yunfan Ye, Renjiao Yi, Zhirui Gao, Chenyang Zhu, Zhiping Cai, Kai Xu
- **🏷️ 机构**: National University of Defense Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the problem of reconstructing 3D feature curves of an object from a set of calibrated multi-view images. To do so, we learn a neural implicit field representing the density distribution of 3D edges which we refer to as Neural Edge Field (NEF). Inspired by NeRF, NEF is optimized with a view-based rendering loss where a 2D edge map is rendered at a given view and is compared to the ground-truth edge map extracted from the image of that view. The rendering-based differentiable optimization of NEF fully exploits 2D edge detection, without needing a supervision of 3D edges, a 3D geometric operator or cross-view edge correspondence. Several technical designs are devised to ensure learning a range-limited and view-independent NEF for robust edge extraction. The final parametric 3D curves are extracted from NEF with an iterative optimization method. On our benchmark with synthetic data, we demonstrate that NEF outperforms existing state-of-the-art methods on all metrics. Project page: https://yunfan1202.github.io/NEF/.

</details>

### MVImgNet: A Large-scale Dataset of Multi-view Images.
- **链接**: [arXiv:2303.06042](https://arxiv.org/abs/2303.06042) · 📚 被引 131
- **作者**: Xianggang Yu, Mutian Xu, Yidan Zhang, Haolin Liu, Chongjie Ye, Yushuang Wu et al.
- **🏷️ 机构**: FNii, CUHKSZ, SSE, CUHKSZ
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Being data-driven is one of the most iconic properties of deep learning algorithms. The birth of ImageNet drives a remarkable trend of "learning from large-scale data" in computer vision. Pretraining on ImageNet to obtain rich universal representations has been manifested to benefit various 2D visual tasks, and becomes a standard in 2D vision. However, due to the laborious collection of real-world 3D data, there is yet no generic dataset serving as a counterpart of ImageNet in 3D vision, thus how such a dataset can impact the 3D community is unraveled. To remedy this defect, we introduce MVImgNet, a large-scale dataset of multi-view images, which is highly convenient to gain by shooting videos of real-world objects in human daily life. It contains 6.5 million frames from 219,188 videos crossing objects from 238 classes, with rich annotations of object masks, camera parameters, and point clouds. The multi-view attribute endows our dataset with 3D-aware signals, making it a soft bridge between 2D and 3D vision. We conduct pilot studies for probing the potential of MVImgNet on a variety of 3D and 2D visual tasks, including radiance field reconstruction, multi-view stereo, and view-consistent image understanding, where MVImgNet demonstrates promising performance, remaining lots of possibilities for future explorations. Besides, via dense reconstruction on MVImgNet, a 3D object point cloud dataset is derived, called MVPNet, covering 87,200 samples from 150 categories, with the class label on each point cloud. Experiments show that MVPNet can benefit the real-world 3D object classification while posing new challenges to point cloud understanding. MVImgNet and MVPNet will be publicly available, hoping to inspire the broader vision community.

</details>

### 3D-aware Facial Landmark Detection via Multi-view Consistent Training on Synthetic Data.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01226) · 📚 被引 17
- **作者**: Libing Zeng, Lele Chen, Wentao Bao, Zhong Li, Yi Xu, Junsong Yuan et al.
- **🏷️ 机构**: Texas A&#x0026;M University, InnoPeak Technology, Inc,OPPO US Research Center, Michigan State University
- **会议**: CVPR 2023

### NeuralDome: A Neural Modeling Pipeline on Multi-View Human-Object Interactions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00853) · 📚 被引 33
- **作者**: Juze Zhang, Haimin Luo, Hongdi Yang, Xinru Xu, Qianyang Wu, Ye Shi et al.
- **🏷️ 机构**: ShanghaiTech University
- **会议**: CVPR 2023

### GeoMVSNet: Learning Multi-View Stereo with Geometry Perception.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02060) · 📚 被引 119
- **作者**: Zhe Zhang, Rui Peng, Yuxi Hu, Ronggang Wang
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University,China, School of Science and Engineering, The Chinese University of Hong Kong,Shenzhen,China
- **会议**: CVPR 2023

### Multi-View Stereo Representation Revist: Region-Aware MVSNet.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01667) · 📚 被引 28
- **作者**: Yisu Zhang, Jianke Zhu, Lixiang Lin
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2023

### NeuFace: Realistic 3D Neural Face Rendering from Multi-View Images.
- **链接**: [arXiv:2303.14092](https://arxiv.org/abs/2303.14092) · 📚 被引 18
- **作者**: Mingwu Zheng, Haiyu Zhang, Hongyu Yang, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, Institute of Artificial Intelligence, Beihang University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Realistic face rendering from multi-view images is beneficial to various computer vision and graphics applications. Due to the complex spatially-varying reflectance properties and geometry characteristics of faces, however, it remains challenging to recover 3D facial representations both faithfully and efficiently in the current studies. This paper presents a novel 3D face rendering model, namely NeuFace, to learn accurate and physically-meaningful underlying 3D representations by neural rendering techniques. It naturally incorporates the neural BRDFs into physically based rendering, capturing sophisticated facial geometry and appearance clues in a collaborative manner. Specifically, we introduce an approximated BRDF integration and a simple yet new low-rank prior, which effectively lower the ambiguities and boost the performance of the facial BRDFs. Extensive experiments demonstrate the superiority of NeuFace in human face rendering, along with a decent generalization ability to common objects.

</details>

### Relightable Neural Human Assets from Multi-view Gradient Illuminations.
- **链接**: [arXiv:2212.07648](https://arxiv.org/abs/2212.07648) · 📚 被引 24
- **作者**: Taotao Zhou, Kai He, Di Wu, Teng Xu, Qixuan Zhang, Kuixiang Shao et al.
- **🏷️ 机构**: ShanghaiTech University, University of Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human modeling and relighting are two fundamental problems in computer vision and graphics, where high-quality datasets can largely facilitate related research. However, most existing human datasets only provide multi-view human images captured under the same illumination. Although valuable for modeling tasks, they are not readily used in relighting problems. To promote research in both fields, in this paper, we present UltraStage, a new 3D human dataset that contains more than 2,000 high-quality human assets captured under both multi-view and multi-illumination settings. Specifically, for each example, we provide 32 surrounding views illuminated with one white light and two gradient illuminations. In addition to regular multi-view images, gradient illuminations help recover detailed surface normal and spatially-varying material maps, enabling various relighting applications. Inspired by recent advances in neural representation, we further interpret each example into a neural human asset which allows novel view synthesis under arbitrary lighting conditions. We show our neural human assets can achieve extremely high capture performance and are capable of representing fine details such as facial wrinkles and cloth folds. We also validate UltraStage in single image relighting tasks, training neural networks with virtual relighted data from neural assets and demonstrating realistic rendering improvements over prior arts. UltraStage will be publicly available to the community to stimulate significant future developments in various human modeling and rendering tasks. The dataset is available at https://miaoing.github.io/RNHA.

</details>

### Multi-View Reconstruction Using Signed Ray Distance Functions (SRDF).
- **链接**: [arXiv:2209.00082](https://arxiv.org/abs/2209.00082) · 📚 被引 11
- **作者**: Pierre Zins, Yuanlu Xu, Edmond Boyer, Stefanie Wuhrer, Tony Tung
- **🏷️ 机构**: Inria centre at the University Grenoble Alpes, Meta Reality Labs,Sausalito,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate a new optimization framework for multi-view 3D shape reconstructions. Recent differentiable rendering approaches have provided breakthrough performances with implicit shape representations though they can still lack precision in the estimated geometries. On the other hand multi-view stereo methods can yield pixel wise geometric accuracy with local depth predictions along viewing rays. Our approach bridges the gap between the two strategies with a novel volumetric shape representation that is implicit but parameterized with pixel depths to better materialize the shape surface with consistent signed distances along viewing rays. The approach retains pixel-accuracy while benefiting from volumetric integration in the optimization. To this aim, depths are optimized by evaluating, at each 3D location within the volumetric discretization, the agreement between the depth prediction consistency and the photometric consistency for the corresponding pixels. The optimization is agnostic to the associated photo-consistency term which can vary from a median-based baseline to more elaborate criteria learned functions. Our experiments demonstrate the benefit of the volumetric integration with depth predictions. They also show that our approach outperforms existing approaches over standard 3D benchmarks with better geometry estimations.

</details>

### Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01719)
- **作者**: Ziqi Pang, Jie Li, Pavel Tokmakov, Dian Chen, Sergey Zagoruyko, Yu-Xiong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative Convolution Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00791)
- **作者**: Wencheng Han, Junbo Yin, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Self-supervised Monocular Depth Estimation: Let's Talk About The Weather.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00818)
- **作者**: Kieran Saunders, George Vogiatzis, Luis J. Manso
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00838)
- **作者**: Xuepeng Shi, Georgi Dikov, Gerhard Reitmayr, Tae-Kyun Kim, Mohsen Ghafoorian
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01485)
- **作者**: Chaoqiang Zhao, Matteo Poggi, Fabio Tosi, Lei Zhou, Qiyu Sun, Yang Tang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### HaMuCo: Hand Pose Estimation via Multiview Collaborative Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01898)
- **作者**: Xiaozheng Zheng, Chao Wen, Zhou Xue, Pengfei Ren, Jingyu Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Two-in-One Depth: Bridging the Gap Between Monocular and Binocular Self-supervised Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00863)
- **作者**: Zhengming Zhou, Qiulei Dong
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### CL-MVSNet: Unsupervised Multi-view Stereo with Dual-level Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00349)
- **作者**: Kaiqiang Xiong, Rui Peng, Zhe Zhang, Tianxing Feng, Jianbo Jiao, Feng Gao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### GeoMIM: Towards Better 3D Knowledge Transfer via Masked Image Modeling for Multi-view 3D Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01635)
- **作者**: Jihao Liu, Tai Wang, Boxiao Liu, Qihang Zhang, Yu Liu, Hongsheng Li
- **🏷️ 机构**: SenseTime, CUHK
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [3d-detection](../3d-detection/Guideline%202023.md)
- 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- ImGeoNet: Image-induced Geometry-aware Voxel Representation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
