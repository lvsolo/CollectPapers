# 3D Detection — 2023 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### RangePerception: Taming LiDAR Range View for Efficient and Accurate 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fb8e52adcd9b59bad73f109c53afc43a-Abstract-Conference.html) · 📚 11 citations
- **作者**: Yeqi Bai, Ben Fei, Youquan Liu, Tao Ma, Yuenan Hou, Botian Shi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e352b765e625934ce86919995e2371aa-Abstract-Conference.html)
- **作者**: Yang Cao, Yihan Zeng, Hang Xu, Dan Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Depth-discriminative Metric Learning for Monocular 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fda257e65f46e21dbc117b20fd0aba3c-Abstract-Conference.html) · 📚 12 citations
- **作者**: Wonhyeok Choi, Mingyu Shin, Sunghoon Im
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### 3D Copy-Paste: Physically Plausible Object Insertion for Monocular 3D Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/370fa2e691f57eb319bc263a07dad4a5-Abstract-Conference.html) · 📚 20 citations
- **作者**: Yunhao Ge, Hong-Xing Yu, Cheng Zhao, Yuliang Guo, Xinyu Huang, Liu Ren et al.
- **🏷️ 机构**: Stanford University
- **会议**: NeurIPS 2023

### Diffusion-SS3D: Diffusion Model for Semi-supervised 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/99786eed5e16920f908572fb00e151c3-Abstract-Conference.html)
- **作者**: Cheng-Ju Ho, Chen-Hsuan Tai, Yen-Yu Lin, Ming-Hsuan Yang, Yi-Hsuan Tsai
- **🏷️ 机构**: UC Merced
- **会议**: NeurIPS 2023

### Query-based Temporal Fusion with Explicit Motion for 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ef0dcb44a47185f5bacac62571f6e920-Abstract-Conference.html) · 📚 27 citations
- **作者**: Jinghua Hou, Zhe Liu, Dingkang Liang, Zhikang Zou, Xiaoqing Ye, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: NeurIPS 2023

### Leveraging Vision-Centric Multi-Modal Expertise for 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/79206ac5b7e88eeeed74997f3b6f4c7f-Abstract-Conference.html)
- **作者**: Linyan Huang, Zhiqi Li, Chonghao Sima, Wenhai Wang, Jingdong Wang, Yu Qiao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2023

### STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5d8c01de2dc698c54201c1c7d0b86974-Abstract-Conference.html)
- **作者**: Sujin Jang, Dae Ung Jo, Sung Ju Hwang, Dongwook Lee, Daehyun Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### MonoUNI: A Unified Vehicle and Infrastructure-side Monocular 3D Object Detection Network with Sufficient Depth Clues.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2703a0e3c2b33506295a77762338cf24-Abstract-Conference.html) · 📚 68 citations
- **作者**: Jinrang Jia, Zhenjia Li, Yifeng Shi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CluB: Cluster Meets BEV for LiDAR-Based 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7f2fc4053a66edfa430bcdf9a6ff3b17-Abstract-Conference.html)
- **作者**: Yingjie Wang, Jiajun Deng, Yuenan Hou, Yao Li, Yu Zhang, Jianmin Ji et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Flow-Based Feature Fusion for Vehicle-Infrastructure Cooperative 3D Object Detection.
- **链接**: [arXiv:2311.01682](https://arxiv.org/abs/2311.01682) · [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6ca5d2665de83394f437dad0c3746907-Abstract-Conference.html) · [代码](https://github.com/haibao-yu/FFNet-VIC3D) · 📚 71 citations
- **作者**: Haibao Yu, Yingjuan Tang, Enze Xie, Jilei Mao, Ping Luo, Zaiqing Nie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

- **摘要（英，原文）**:

  > Cooperatively utilizing both ego-vehicle and infrastructure sensor data can significantly enhance autonomous driving perception abilities. However, the uncertain temporal asynchrony and limited communication conditions can lead to fusion misalignment and constrain the exploitation of infrastructure data. To address these issues in vehicle-infrastructure cooperative 3D (VIC3D) object detection, we propose the Feature Flow Net (FFNet), a novel cooperative detection framework. FFNet is a flow-based feature fusion framework that uses a feature flow prediction module to predict future features and compensate for asynchrony. Instead of transmitting feature maps extracted from still-images, FFNet transmits feature flow, leveraging the temporal coherence of sequential infrastructure frames. Furthermore, we introduce a self-supervised training approach that enables FFNet to generate feature flow with feature prediction ability from raw infrastructure sequences. Experimental results demonstrate that our proposed method outperforms existing cooperative detection methods while only requiring about 1/100 of the transmission cost of raw data and covers all latency in one model on the DAIR-V2X dataset. The code is available at \href{https://github.com/haibao-yu/FFNet-VIC3D}{https://github.com/haibao-yu/FFNet-VIC3D}.

### HEDNet: A Hierarchical Encoder-Decoder Network for 3D Object Detection in Point Clouds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a64e641fa00a7eb9500cb7e1835d0495-Abstract-Conference.html) · 📚 88 citations
- **作者**: Gang Zhang, Junnan Chen, Guohuan Gao, Jianmin Li, Xiaolin Hu
- **🏷️ 机构**: Tsinghua
- **会议**: NeurIPS 2023

### Unleash the Potential of Image Branch for Cross-modal 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a1f0c0cd6caaa4863af5f12608edf63e-Abstract-Conference.html) · 📚 35 citations
- **作者**: Yifan Zhang, Qijian Zhang, Junhui Hou, Yixuan Yuan, Guoliang Xing
- **🏷️ 机构**: City University of Hong Kong
- **会议**: NeurIPS 2023

### Differentiable Registration of Images and LiDAR Point Clouds with VoxelPoint-to-Pixel Matching.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a0a53fefef4c2ad72d5ab79703ba70cb-Abstract-Conference.html) · 📚 58 citations
- **作者**: Junsheng Zhou, Baorui Ma, Wenyuan Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
