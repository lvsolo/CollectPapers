# Vision Transformer — 2023 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### HiViT: A Simpler and More Efficient Design of Hierarchical Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=3F6I-0-57SC)
- **作者**: Xiaosong Zhang, Yunjie Tian, Lingxi Xie, Wei Huang, Qi Dai, Qixiang Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Vision Transformer Adapter for Dense Predictions.
- **链接**: [arXiv:2205.08534](https://arxiv.org/abs/2205.08534) · [代码](https://github.com/czczup/ViT-Adapter)
- **作者**: Zhe Chen, Yuchen Duan, Wenhai Wang, Junjun He, Tong Lu, Jifeng Dai et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work investigates a simple yet powerful dense prediction task adapter for Vision Transformer (ViT). Unlike recently advanced variants that incorporate vision-specific inductive biases into their architectures, the plain ViT suffers inferior performance on dense predictions due to weak prior assumptions. To address this issue, we propose the ViT-Adapter, which allows plain ViT to achieve comparable performance to vision-specific transformers. Specifically, the backbone in our framework is a plain ViT that can learn powerful representations from large-scale multi-modal data. When transferring to downstream tasks, a pre-training-free adapter is used to introduce the image-related inductive biases into the model, making it suitable for these tasks. We verify ViT-Adapter on multiple dense prediction tasks, including object detection, instance segmentation, and semantic segmentation. Notably, without using extra detection data, our ViT-Adapter-L yields state-of-the-art 60.9 box AP and 53.0 mask AP on COCO test-dev. We hope that the ViT-Adapter could serve as an alternative for vision-specific transformers and facilitate future research. The code and models will be released at https://github.com/czczup/ViT-Adapter.

</details>

### Budgeted Training for Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=sVzBN-DlJRi)
- **作者**: Zhuofan Xia, Xuran Pan, Xuan Jin, Yuan He, Hui Xue, Shiji Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### GPViT: A High Resolution Non-Hierarchical Vision Transformer with Group Propagation.
- **链接**: [arXiv:2212.06795](https://arxiv.org/abs/2212.06795)
- **作者**: Chenhongyi Yang, Jiarui Xu, Shalini De Mello, Elliot J. Crowley, Xiaolong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present the Group Propagation Vision Transformer (GPViT): a novel nonhierarchical (i.e. non-pyramidal) transformer model designed for general visual recognition with high-resolution features. High-resolution features (or tokens) are a natural fit for tasks that involve perceiving fine-grained details such as detection and segmentation, but exchanging global information between these features is expensive in memory and computation because of the way self-attention scales. We provide a highly efficient alternative Group Propagation Block (GP Block) to exchange global information. In each GP Block, features are first grouped together by a fixed number of learnable group tokens; we then perform Group Propagation where global information is exchanged between the grouped features; finally, global information in the updated grouped features is returned back to the image features through a transformer decoder. We evaluate GPViT on a variety of visual recognition tasks including image classification, semantic segmentation, object detection, and instance segmentation. Our method achieves significant performance gains over previous works across all tasks, especially on tasks that require highresolution outputs, for example, our GPViT-L3 outperforms Swin Transformer-B by 2.0 mIoU on ADE20K semantic segmentation with only half as many parameters. Project page: chenhongyiyang.com/projects/GPViT/GPViT

</details>

### MixPro: Data Augmentation with MaskMix and Progressive Attention Labeling for Vision Transformer.
- **链接**: [arXiv:2304.12043](https://arxiv.org/abs/2304.12043) · [代码](https://github.com/fistyee/MixPro)
- **作者**: Qihao Zhao, Yangyu Huang, Wei Hu, Fan Zhang, Jun Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recently proposed data augmentation TransMix employs attention labels to help visual transformers (ViT) achieve better robustness and performance. However, TransMix is deficient in two aspects: 1) The image cropping method of TransMix may not be suitable for ViTs. 2) At the early stage of training, the model produces unreliable attention maps. TransMix uses unreliable attention maps to compute mixed attention labels that can affect the model. To address the aforementioned issues, we propose MaskMix and Progressive Attention Labeling (PAL) in image and label space, respectively. In detail, from the perspective of image space, we design MaskMix, which mixes two images based on a patch-like grid mask. In particular, the size of each mask patch is adjustable and is a multiple of the image patch size, which ensures each image patch comes from only one image and contains more global contents. From the perspective of label space, we design PAL, which utilizes a progressive factor to dynamically re-weight the attention weights of the mixed attention label. Finally, we combine MaskMix and Progressive Attention Labeling as our new data augmentation method, named MixPro. The experimental results show that our method can improve various ViT-based models at scales on ImageNet classification (73.8\% top-1 accuracy based on DeiT-T for 300 epochs). After being pre-trained with MixPro on ImageNet, the ViT-based models also demonstrate better transferability to semantic segmentation, object detection, and instance segmentation. Furthermore, compared to TransMix, MixPro also shows stronger robustness on several benchmarks. The code is available at https://github.com/fistyee/MixPro.

</details>
