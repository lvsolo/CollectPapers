# Multi-camera Perception — 2022 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MVP-N: A Dataset and Benchmark for Real-World Multi-View Object Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/819b8452be7d6af1351d4c4f9cbdbd9b-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 5
- **作者**: Ren Wang, Jiayue Wang, Tae Sung Kim, Jinsung Kim, Hyuk-Jae Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### MBW: Multi-view Bootstrapping in the Wild.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/144258c36a5559a6cf9f7d53a527eb57-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 0
- **作者**: Mosam Dabhi, Chaoyang Wang, Tim Clifford, László A. Jeni, Ian R. Fasel, Simon Lucey
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Geo-Neus: Geometry-Consistent Neural Implicit Surfaces Learning for Multi-view Reconstruction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/16415eed5a0a121bfce79924db05d3fe-Abstract-Conference.html) · 📚 被引 39
- **作者**: Qiancheng Fu, Qingshan Xu, Yew Soon Ong, Wenbing Tao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Multi-view Subspace Clustering on Topological Manifold.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/a6610efd6c767f63343a4ab28505212e-Abstract-Conference.html) · 📚 被引 5
- **作者**: Shudong Huang, Hongjie Wu, Yazhou Ren, Ivor W. Tsang, Zenglin Xu, Wentao Feng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Uncertainty Estimation for Multi-view Data: The Power of Seeing the Whole Picture.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/2ab3163ee384cd46baa7f1abb2b1bf19-Abstract-Conference.html) · 📚 被引 2
- **作者**: Myong Chol Jung, He Zhao, Joanna Dipnall, Belinda Gabbe, Lan Du
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### WT-MVSNet: Window-based Transformers for Multi-view Stereo.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/38e511a690709603d4cc3a1c52b4a9fd-Abstract-Conference.html) · 📚 被引 6
- **作者**: Jinli Liao, Yikang Ding, Yoli Shavit, Dihe Huang, Shihao Ren, Jia Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Unsupervised Multi-View Object Segmentation Using Radiance Field Propagation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/70de9e3948645a1be2de657f14d85c6d-Abstract-Conference.html) · 📚 被引 1
- **作者**: Xinhang Liu, Jiaben Chen, Huai Yu, Yu-Wing Tai, Chi-Keung Tang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### 360-MLC: Multi-view Layout Consistency for Self-training and Hyper-parameter Tuning.
- **链接**: [arXiv:2210.12935](https://arxiv.org/abs/2210.12935) · 📚 被引 0
- **作者**: Bolivar Solarte, Chin-Hsuan Wu, Yueh-Cheng Liu, Yi-Hsuan Tsai, Min Sun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present 360-MLC, a self-training method based on multi-view layout consistency for finetuning monocular room-layout models using unlabeled 360-images only. This can be valuable in practical scenarios where a pre-trained model needs to be adapted to a new data domain without using any ground truth annotations. Our simple yet effective assumption is that multiple layout estimations in the same scene must define a consistent geometry regardless of their camera positions. Based on this idea, we leverage a pre-trained model to project estimated layout boundaries from several camera views into the 3D world coordinate. Then, we re-project them back to the spherical coordinate and build a probability function, from which we sample the pseudo-labels for self-training. To handle unconfident pseudo-labels, we evaluate the variance in the re-projected boundaries as an uncertainty value to weight each pseudo-label in our loss function during training. In addition, since ground truth annotations are not available during training nor in testing, we leverage the entropy information in multiple layout estimations as a quantitative metric to measure the geometry consistency of the scene, allowing us to evaluate any layout estimator for hyper-parameter tuning, including model selection without ground truth annotations. Experimental results show that our solution achieves favorable performance against state-of-the-art methods when self-training from three publicly available source datasets to a unique, newly labeled dataset consisting of multi-view of the same scenes.

</details>

### Align then Fusion: Generalized Large-scale Multi-view Clustering with Anchor Matching Correspondences.
- **链接**: [arXiv:2205.15075](https://arxiv.org/abs/2205.15075) · [代码](https://github.com/wangsiwei2010/NeurIPS22-FMVACC) · 📚 被引 16
- **作者**: Siwei Wang, Xinwang Liu, Suyuan Liu, Jiaqi Jin, Wenxuan Tu, Xinzhong Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view anchor graph clustering selects representative anchors to avoid full pair-wise similarities and therefore reduce the complexity of graph methods. Although widely applied in large-scale applications, existing approaches do not pay sufficient attention to establishing correct correspondences between the anchor sets across views. To be specific, anchor graphs obtained from different views are not aligned column-wisely. Such an \textbf{A}nchor-\textbf{U}naligned \textbf{P}roblem (AUP) would cause inaccurate graph fusion and degrade the clustering performance. Under multi-view scenarios, generating correct correspondences could be extremely difficult since anchors are not consistent in feature dimensions. To solve this challenging issue, we propose the first study of the generalized and flexible anchor graph fusion framework termed \textbf{F}ast \textbf{M}ulti-\textbf{V}iew \textbf{A}nchor-\textbf{C}orrespondence \textbf{C}lustering (FMVACC). Specifically, we show how to find anchor correspondence with both feature and structure information, after which anchor graph fusion is performed column-wisely. Moreover, we theoretically show the connection between FMVACC and existing multi-view late fusion \cite{liu2018late} and partial view-aligned clustering \cite{huang2020partially}, which further demonstrates our generality. Extensive experiments on seven benchmark datasets demonstrate the effectiveness and efficiency of our proposed method. Moreover, the proposed alignment module also shows significant performance improvement applying to existing multi-view anchor graph competitors indicating the importance of anchor alignment. Our code is available at \url{https://github.com/wangsiwei2010/NeurIPS22-FMVACC}.

</details>

### ElasticMVS: Learning elastic part representation for self-supervised multi-view stereopsis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/94ef721705ea95d6981632be62bb66e2-Abstract-Conference.html) · 📚 被引 2
- **作者**: Jinzhi Zhang, Ruofan Tang, Zheng Cao, Jing Xiao, Ruqi Huang, Lu Fang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Multiview Human Body Reconstruction from Uncalibrated Cameras.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/33610fba262d7b6fed0810b89f55e147-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhixuan Yu, Linguang Zhang, Yuanlu Xu, Chengcheng Tang, Luan Tran, Cem Keskin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Hierarchical Normalization for Robust Monocular Depth Estimation.
- **链接**: [arXiv:2210.09670](https://arxiv.org/abs/2210.09670) · 📚 被引 8
- **作者**: Chi Zhang, Wei Yin, Billzb Wang, Gang Yu, Bin Fu, Chunhua Shen
- **🏷️ 机构**: Tencent, ZJU
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we address monocular depth estimation with deep neural networks. To enable training of deep monocular estimation models with various sources of datasets, state-of-the-art methods adopt image-level normalization strategies to generate affine-invariant depth representations. However, learning with image-level normalization mainly emphasizes the relations of pixel representations with the global statistic in the images, such as the structure of the scene, while the fine-grained depth difference may be overlooked. In this paper, we propose a novel multi-scale depth normalization method that hierarchically normalizes the depth representations based on spatial information and depth distributions. Compared with previous normalization strategies applied only at the holistic image level, the proposed hierarchical normalization can effectively preserve the fine-grained details and improve accuracy. We present two strategies that define the hierarchical normalization contexts in the depth domain and the spatial domain, respectively. Our extensive experiments show that the proposed normalization strategy remarkably outperforms previous normalization methods, and we set new state-of-the-art on five zero-shot transfer benchmark datasets.

</details>
