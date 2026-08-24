# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UP-DETR: Unsupervised Pre-Training for Object Detection With Transformers.
- **链接**: [arXiv:2011.09094](https://arxiv.org/abs/2011.09094) · [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Dai_UP-DETR_Unsupervised_Pre-Training_for_Object_Detection_With_Transformers_CVPR_2021_paper.html) · [代码](https://github.com/dddzg/up-detr) · 📚 被引 447
- **作者**: Zhigang Dai, Bolun Cai, Yugeng Lin, Junying Chen
- **🏷️ 机构**: South China University of Technology,School of Software Engineering, Tencent Wechat AI
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > DEtection TRansformer (DETR) for object detection reaches competitive performance compared with Faster R-CNN via a transformer encoder-decoder architecture. However, trained with scratch transformers, DETR needs large-scale training data and an extreme long training schedule even on COCO dataset. Inspired by the great success of pre-training transformers in natural language processing, we propose a novel pretext task named random query patch detection in Unsupervised Pre-training DETR (UP-DETR). Specifically, we randomly crop patches from the given image and then feed them as queries to the decoder. The model is pre-trained to detect these query patches from the input image. During the pre-training, we address two critical issues: multi-task learning and multi-query localization. (1) To trade off classification and localization preferences in the pretext task, we find that freezing the CNN backbone is the prerequisite for the success of pre-training transformers. (2) To perform multi-query localization, we develop UP-DETR with multi-query patch detection with attention mask. Besides, UP-DETR also provides a unified perspective for fine-tuning object detection and one-shot detection tasks. In our experiments, UP-DETR significantly boosts the performance of DETR with faster convergence and higher average precision on object detection, one-shot detection and panoptic segmentation. Code and pre-training models: https://github.com/dddzg/up-detr.

### Uncertainty-Aware Joint Salient Object and Camouflaged Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Uncertainty-Aware_Joint_Salient_Object_and_Camouflaged_Object_Detection_CVPR_2021_paper.html) · 📚 被引 270
- **作者**: Aixuan Li, Jing Zhang, Yunqiu Lv, Bowen Liu, Tong Zhang, Yuchao Dai
- **🏷️ 机构**: Northwestern Polytechnical University,China, Australian National University,Australia, EPFL,Switzerland
- **会议**: CVPR 2021

### Instant-Teaching: An End-to-End Semi-Supervised Object Detection Framework.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Instant-Teaching_An_End-to-End_Semi-Supervised_Object_Detection_Framework_CVPR_2021_paper.html) · 📚 被引 194
- **作者**: Qiang Zhou, Chaohui Yu, Zhibin Wang, Qi Qian, Hao Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Points As Queries: Weakly Semi-Supervised Object Detection by Points.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Points_As_Queries_Weakly_Semi-Supervised_Object_Detection_by_Points_CVPR_2021_paper.html) · 📚 被引 87
- **作者**: Liangyu Chen, Tong Yang, Xiangyu Zhang, Wei Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### GAIA: A Transfer Learning System of Object Detection That Fits Your Needs.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Bu_GAIA_A_Transfer_Learning_System_of_Object_Detection_That_Fits_CVPR_2021_paper.html) · 📚 被引 35
- **作者**: Xingyuan Bu, Junran Peng, Junjie Yan, Tieniu Tan, Zhaoxiang Zhang
- **🏷️ 机构**: ia.ac.cn
- **会议**: CVPR 2021

### Adaptive Image Transformer for One-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Adaptive_Image_Transformer_for_One-Shot_Object_Detection_CVPR_2021_paper.html) · 📚 被引 57
- **作者**: Ding-Jie Chen, He-Yen Hsieh, Tyng-Luh Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Class-Aware Robust Adversarial Training for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Class-Aware_Robust_Adversarial_Training_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 52
- **作者**: Pin-Chun Chen, Bo-Han Kung, Jun-Cheng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Scale-Aware Automatic Augmentation for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Scale-Aware_Automatic_Augmentation_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 49
- **作者**: Yukang Chen, Yanwei Li, Tao Kong, Lu Qi, Ruihang Chu, Lei Li et al.
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2021

### AQD: Towards Accurate Quantized Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_AQD_Towards_Accurate_Quantized_Object_Detection_CVPR_2021_paper.html) · 📚 被引 27
- **作者**: Peng Chen, Jing Liu, Bohan Zhuang, Mingkui Tan, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2021

### Robust and Accurate Object Detection via Adversarial Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Robust_and_Accurate_Object_Detection_via_Adversarial_Learning_CVPR_2021_paper.html) · 📚 被引 60
- **作者**: Xiangning Chen, Cihang Xie, Mingxing Tan, Li Zhang, Cho-Jui Hsieh, Boqing Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Dynamic Head: Unifying Object Detection Heads With Attentions.
- **链接**: [arXiv:2106.08322](https://arxiv.org/abs/2106.08322) · [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Dai_Dynamic_Head_Unifying_Object_Detection_Heads_With_Attentions_CVPR_2021_paper.html) · [代码](https://github.com/microsoft/DynamicHead) · 📚 被引 940
- **作者**: Xiyang Dai, Yinpeng Chen, Bin Xiao, Dongdong Chen, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > The complex nature of combining localization and classification in object detection has resulted in the flourished development of methods. Previous works tried to improve the performance in various object detection heads but failed to present a unified view. In this paper, we present a novel dynamic head framework to unify object detection heads with attentions. By coherently combining multiple self-attention mechanisms between feature levels for scale-awareness, among spatial locations for spatial-awareness, and within output channels for task-awareness, the proposed approach significantly improves the representation ability of object detection heads without any computational overhead. Further experiments demonstrate that the effectiveness and efficiency of the proposed dynamic head on the COCO benchmark. With a standard ResNeXt-101-DCN backbone, we largely improve the performance over popular object detectors and achieve a new state-of-the-art at 54.0 AP. Furthermore, with latest transformer backbone and extra data, we can push current best COCO result to a new record at 60.6 AP. The code will be released at https://github.com/microsoft/DynamicHead.

### General Instance Distillation for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Dai_General_Instance_Distillation_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 234
- **作者**: Xing Dai, Zeren Jiang, Zhao Wu, Yiping Bao, Zhicheng Wang, Si Liu et al.
- **🏷️ 机构**: MEGVII Technology, BeiHang University
- **会议**: CVPR 2021

### Unbiased Mean Teacher for Cross-Domain Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Deng_Unbiased_Mean_Teacher_for_Cross-Domain_Object_Detection_CVPR_2021_paper.html) · 📚 被引 336
- **作者**: Jinhong Deng, Wen Li, Yuhua Chen, Lixin Duan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Group Collaborative Learning for Co-Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Fan_Group_Collaborative_Learning_for_Co-Salient_Object_Detection_CVPR_2021_paper.html) · 📚 被引 101
- **作者**: Qi Fan, Deng-Ping Fan, Huazhu Fu, Chi-Keung Tang, Ling Shao, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Generalized Few-Shot Object Detection Without Forgetting.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Fan_Generalized_Few-Shot_Object_Detection_Without_Forgetting_CVPR_2021_paper.html) · 📚 被引 165
- **作者**: Zhibo Fan, Yuchen Ma, Zeming Li, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### OTA: Optimal Transport Assignment for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ge_OTA_Optimal_Transport_Assignment_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 482
- **作者**: Zheng Ge, Songtao Liu, Zeming Li, Osamu Yoshie, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### Depth From Camera Motion and Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Griffin_Depth_From_Camera_Motion_and_Object_Detection_CVPR_2021_paper.html) · 📚 被引 33
- **作者**: Brent A. Griffin, Jason J. Corso
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Positive-Unlabeled Data Purification in the Wild for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Positive-Unlabeled_Data_Purification_in_the_Wild_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 7
- **作者**: Jianyuan Guo, Kai Han, Han Wu, Chao Zhang, Xinghao Chen, Chunjing Xu et al.
- **🏷️ 机构**: Huawei Technologies,Noah&#x2019;s Ark Lab, University of Sydney,School of Computer Science, Faculty of Engineering, Peking University,Key Lab of Machine Perception (MOE),Dept. of Machine Intelligence
- **会议**: CVPR 2021

### Beyond Bounding-Box: Convex-Hull Feature Adaptation for Oriented and Densely Packed Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Beyond_Bounding-Box_Convex-Hull_Feature_Adaptation_for_Oriented_and_Densely_Packed_CVPR_2021_paper.html) · 📚 被引 244
- **作者**: Zonghao Guo, Chang Liu, Xiaosong Zhang, Jianbin Jiao, Xiangyang Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### ReDet: A Rotation-Equivariant Detector for Aerial Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Han_ReDet_A_Rotation-Equivariant_Detector_for_Aerial_Object_Detection_CVPR_2021_paper.html) · 📚 被引 886
- **作者**: Jiaming Han, Jian Ding, Nan Xue, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Informative and Consistent Correspondence Mining for Cross-Domain Weakly Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hou_Informative_and_Consistent_Correspondence_Mining_for_Cross-Domain_Weakly_Supervised_Object_CVPR_2021_paper.html) · 📚 被引 16
- **作者**: Luwei Hou, Yu Zhang, Kui Fu, Jia Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Dense Relation Distillation With Context-Aware Aggregation for Few-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Dense_Relation_Distillation_With_Context-Aware_Aggregation_for_Few-Shot_Object_Detection_CVPR_2021_paper.html) · 📚 被引 192
- **作者**: Hanzhe Hu, Shuai Bai, Aoxue Li, Jinshi Cui, Liwei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### SAIL-VOS 3D: A Synthetic Dataset and Baselines for Object Detection and 3D Mesh Reconstruction From Video Data.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_SAIL-VOS_3D_A_Synthetic_Dataset_and_Baselines_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 15
- **作者**: Yuan-Ting Hu, Jiahong Wang, Raymond A. Yeh, Alexander G. Schwing
- **🏷️ 机构**: University of Illinois at Urbana-Champaign
- **会议**: CVPR 2021

### Interpolation-Based Semi-Supervised Learning for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Jeong_Interpolation-Based_Semi-Supervised_Learning_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 45
- **作者**: Jisoo Jeong, Vikas Verma, Minsung Hyun, Juho Kannala, Nojun Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Calibrated RGB-D Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ji_Calibrated_RGB-D_Salient_Object_Detection_CVPR_2021_paper.html) · 📚 被引 262
- **作者**: Wei Ji, Jingjing Li, Shuang Yu, Miao Zhang, Yongri Piao, Shunyu Yao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Towards Open World Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Joseph_Towards_Open_World_Object_Detection_CVPR_2021_paper.html)
- **作者**: K. J. Joseph, Salman H. Khan, Fahad Shahbaz Khan, Vineeth N. Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### UniT: Unified Knowledge Transfer for Any-Shot Object Detection and Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Khandelwal_UniT_Unified_Knowledge_Transfer_for_Any-Shot_Object_Detection_and_Segmentation_CVPR_2021_paper.html) · 📚 被引 24
- **作者**: Siddhesh Khandelwal, Raghav Goyal, Leonid Sigal
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Transformation Invariant Few-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.html) · 📚 被引 88
- **作者**: Aoxue Li, Zhenguo Li
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab,China
- **会议**: CVPR 2021

### Generalized Focal Loss V2: Learning Reliable Localization Quality Estimation for Dense Object Detection.
- **链接**: [arXiv:2011.12885](https://arxiv.org/abs/2011.12885) · [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Generalized_Focal_Loss_V2_Learning_Reliable_Localization_Quality_Estimation_for_CVPR_2021_paper.html) · [代码](https://github.com/implus/GFocalV2) · 📚 被引 396
- **作者**: Xiang Li, Wenhai Wang, Xiaolin Hu, Jun Li, Jinhui Tang, Jian Yang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Localization Quality Estimation (LQE) is crucial and popular in the recent advancement of dense object detectors since it can provide accurate ranking scores that benefit the Non-Maximum Suppression processing and improve detection performance. As a common practice, most existing methods predict LQE scores through vanilla convolutional features shared with object classification or bounding box regression. In this paper, we explore a completely novel and different perspective to perform LQE -- based on the learned distributions of the four parameters of the bounding box. The bounding box distributions are inspired and introduced as "General Distribution" in GFLV1, which describes the uncertainty of the predicted bounding boxes well. Such a property makes the distribution statistics of a bounding box highly correlated to its real localization quality. Specifically, a bounding box distribution with a sharp peak usually corresponds to high localization quality, and vice versa. By leveraging the close correlation between distribution statistics and the real localization quality, we develop a considerably lightweight Distribution-Guided Quality Predictor (DGQP) for reliable LQE based on GFLV1, thus producing GFLV2. To our best knowledge, it is the first attempt in object detection to use a highly relevant, statistical representation to facilitate LQE. Extensive experiments demonstrate the effectiveness of our method. Notably, GFLV2 (ResNet-101) achieves 46.2 AP at 14.6 FPS, surpassing the previous state-of-the-art ATSS baseline (43.6 AP at 14.6 FPS) by absolute 2.6 AP on COCO {\tt test-dev}, without sacrificing the efficiency both in training and inference. Code will be available at https://github.com/implus/GFocalV2.

### Beyond Max-Margin: Class Margin Equilibrium for Few-Shot Object Detection.
- **链接**: [arXiv:2103.04612](https://arxiv.org/abs/2103.04612) · [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Beyond_Max-Margin_Class_Margin_Equilibrium_for_Few-Shot_Object_Detection_CVPR_2021_paper.html) · [代码](https://github.com/Bohao-Lee/CME) · 📚 被引 180
- **作者**: Bohao Li, Boyu Yang, Chang Liu, Feng Liu, Rongrong Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Few-shot object detection has made substantial progressby representing novel class objects using the feature representation learned upon a set of base class objects. However,an implicit contradiction between novel class classification and representation is unfortunately ignored. On the one hand, to achieve accurate novel class classification, the distributions of either two base classes must be far away fromeach other (max-margin). On the other hand, to precisely represent novel classes, the distributions of base classes should be close to each other to reduce the intra-class distance of novel classes (min-margin). In this paper, we propose a class margin equilibrium (CME) approach, with the aim to optimize both feature space partition and novel class reconstruction in a systematic way. CME first converts the few-shot detection problem to the few-shot classification problem by using a fully connected layer to decouple localization features. CME then reserves adequate margin space for novel classes by introducing simple-yet-effective class margin loss during feature learning. Finally, CME pursues margin equilibrium by disturbing the features of novel class instances in an adversarial min-max fashion. Experiments on Pascal VOC and MS-COCO datasets show that CME significantly improves upon two baseline detectors (up to $3\sim 5\%$ in average), achieving state-of-the-art performance. Code is available at https://github.com/Bohao-Lee/CME .

### Few-Shot Object Detection via Classification Refinement and Distractor Retreatment.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Few-Shot_Object_Detection_via_Classification_Refinement_and_Distractor_Retreatment_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Yiting Li, Haiyue Zhu, Yu Cheng, Wenxin Wang, Chek Sing Teo, Cheng Xiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### RankDetNet: Delving Into Ranking Constraints for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_RankDetNet_Delving_Into_Ranking_Constraints_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 15
- **作者**: Ji Liu, Dong Li, Rongzhang Zheng, Lu Tian, Yi Shan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### IQDet: Instance-Wise Quality Distribution Sampling for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ma_IQDet_Instance-Wise_Quality_Distribution_Sampling_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 62
- **作者**: Yuchen Ma, Songtao Liu, Zeming Li, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### Neural Auto-Exposure for High-Dynamic Range Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Onzon_Neural_Auto-Exposure_for_High-Dynamic_Range_Object_Detection_CVPR_2021_paper.html) · 📚 被引 50
- **作者**: Emmanuel Onzon, Fahim Mannan, Felix Heide
- **🏷️ 机构**: Algolux, Princeton University,Algolux
- **会议**: CVPR 2021

### Improved Handling of Motion Blur in Online Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sayed_Improved_Handling_of_Motion_Blur_in_Online_Object_Detection_CVPR_2021_paper.html) · 📚 被引 42
- **作者**: Mohamed Sayed, Gabriel J. Brostow
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### FSCE: Few-Shot Object Detection via Contrastive Proposal Encoding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.html) · 📚 被引 505
- **作者**: Bo Sun, Banghuai Li, Shengcai Cai, Ye Yuan, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Sparse R-CNN: End-to-End Object Detection With Learnable Proposals.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_Sparse_R-CNN_End-to-End_Object_Detection_With_Learnable_Proposals_CVPR_2021_paper.html) · 📚 被引 1308
- **作者**: Peize Sun, Rufeng Zhang, Yi Jiang, Tao Kong, Chenfeng Xu, Wei Zhan et al.
- **🏷️ 机构**: ByteDance Inc., Carnegie Mellon University
- **会议**: CVPR 2021

### Equalization Loss v2: A New Gradient Balance Approach for Long-Tailed Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Tan_Equalization_Loss_v2_A_New_Gradient_Balance_Approach_for_Long-Tailed_CVPR_2021_paper.html) · 📚 被引 179
- **作者**: Jingru Tan, Xin Lu, Gang Zhang, Changqing Yin, Quanquan Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Humble Teachers Teach Better Students for Semi-Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Tang_Humble_Teachers_Teach_Better_Students_for_Semi-Supervised_Object_Detection_CVPR_2021_paper.html) · 📚 被引 179
- **作者**: Yihe Tang, Weifeng Chen, Yijun Luo, Yuting Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Unsupervised Object Detection With LIDAR Clues.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Tian_Unsupervised_Object_Detection_With_LIDAR_Clues_CVPR_2021_paper.html) · 📚 被引 26
- **作者**: Hao Tian, Yuntao Chen, Jifeng Dai, Zhaoxiang Zhang, Xizhou Zhu
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: CVPR 2021

### MeGA-CDA: Memory Guided Attention for Category-Aware Unsupervised Domain Adaptive Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/VS_MeGA-CDA_Memory_Guided_Attention_for_Category-Aware_Unsupervised_Domain_Adaptive_Object_CVPR_2021_paper.html) · 📚 被引 160
- **作者**: Vibashan VS, Vikram Gupta, Poojan Oza, Vishwanath A. Sindagi, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Data-Uncertainty Guided Multi-Phase Learning for Semi-Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Data-Uncertainty_Guided_Multi-Phase_Learning_for_Semi-Supervised_Object_Detection_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Zhenyu Wang, Yali Li, Ye Guo, Lu Fang, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### End-to-End Object Detection With Fully Convolutional Network.
- **链接**: [arXiv:2012.03544](https://arxiv.org/abs/2012.03544) · [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_End-to-End_Object_Detection_With_Fully_Convolutional_Network_CVPR_2021_paper.html) · [代码](https://github.com/Megvii-BaseDetection/DeFCN) · 📚 被引 247
- **作者**: Jianfeng Wang, Lin Song, Zeming Li, Hongbin Sun, Jian Sun, Nanning Zheng
- **🏷️ 机构**: MEGVII, XJTU
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Mainstream object detectors based on the fully convolutional network has achieved impressive performance. While most of them still need a hand-designed non-maximum suppression (NMS) post-processing, which impedes fully end-to-end training. In this paper, we give the analysis of discarding NMS, where the results reveal that a proper label assignment plays a crucial role. To this end, for fully convolutional detectors, we introduce a Prediction-aware One-To-One (POTO) label assignment for classification to enable end-to-end detection, which obtains comparable performance with NMS. Besides, a simple 3D Max Filtering (3DMF) is proposed to utilize the multi-scale features and improve the discriminability of convolutions in the local region. With these techniques, our end-to-end framework achieves competitive performance against many state-of-the-art detectors with NMS on COCO and CrowdHuman datasets. The code is available at https://github.com/Megvii-BaseDetection/DeFCN .

## 跨领域论文（完整笔记在其他领域）

- Objects Are Different: Flexible Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- GrooMeD-NMS: Grouped Mathematically Differentiable NMS for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- To the Point: Efficient 3D Object Detection in the Range Image With Graph Convolution Kernels. → [3d-detection](../3d-detection/Guideline%202021.md)
- MonoRUn: Monocular 3D Object Detection by Reconstruction and Uncertainty Propagation. → [3d-detection](../3d-detection/Guideline%202021.md)
- Back-Tracing Representative Points for Voting-Based 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202021.md)
- LiDAR-Aug: A General Rendering-Based Augmentation Framework for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- OPANAS: One-Shot Path Aggregation Network Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202021.md)
- Delving Into Localization Errors for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- HVPR: Hybrid Voxel-Point Representation for Single-Stage 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- 3D Object Detection With Pointformer. → [3d-detection](../3d-detection/Guideline%202021.md)
- Offboard 3D Object Detection From Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202021.md)
- Categorical Depth Distribution Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- RSN: Range Sparse Net for Efficient, Accurate LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- There Is More Than Meets the Eye: Self-Supervised Multi-Object Detection and Tracking With Sound by Distilling Multimodal Knowledge. → [multimodal](../multimodal/Guideline%202021.md)
- PointAugmenting: Cross-Modal Augmentation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Depth-Conditioned Dynamic Message Propagation for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
