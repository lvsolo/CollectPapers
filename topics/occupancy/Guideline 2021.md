# Occupancy — 2021 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SA-ConvONet: Sign-Agnostic Optimization of Convolutional Occupancy Networks.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00644) · 📚 被引 73
- **作者**: Jiapeng Tang, Jiabao Lei, Dan Xu, Feiying Ma, Kui Jia, Lei Zhang
- **🏷️ 机构**: South China University of Technology,School of Electronic and Information Engineering, HKUST,Department of Computer Science and Engineering,HK, Alibaba Group,DAMO Academy
- **会议**: ICCV 2021

## 🆕 增量新增

### Generative Occupancy Fields for 3D Surface-Aware Image Synthesis. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/acab0116c354964a558e65bdd07ff047-Abstract.html)
- **作者**: Xudong Xu, Xingang Pan, Dahua Lin, Bo Dai
- **🏷️ 机构**: CUHK, Shanghai AI Lab
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对现有生成模型在图像合成中缺乏3D表面感知能力，导致生成图像与几何结构不一致的问题。②提出了生成占用场（Generative Occupancy Fields），将3D占用场与生成对抗网络结合，在潜在空间中建模表面感知的辐射场，实现从任意视角合成与3D结构一致的图像。③相比NeRF-based生成模型，该方法显式利用占用场约束表面几何，提升多视角一致性，并支持显式控制。④实验在多个数据集上展示了高质量、多视角一致的图像合成，但摘要未给出具体量化指标。
- **摘要（英）**: This paper tackles the lack of 3D surface awareness in generative image synthesis, which causes geometric inconsistencies across views. It introduces Generative Occupancy Fields, integrating occupancy fields with GANs to model surface-aware radiance in latent space, enabling view-consistent synthesis. Compared to NeRF-based generators, it explicitly enforces surface geometry, improving multi-view coherence and controllability, with qualitative results on multiple datasets.
- **核心贡献**: 提出生成占用场框架，实现表面感知的多视角一致图像合成。
- **创新点**: 将占用场与GAN结合，在潜在空间中显式建模表面几何。
- **结果**: 在多个数据集上实现高质量、多视角一致的图像生成。
<!-- COMPLETE v1 papers=2 -->
