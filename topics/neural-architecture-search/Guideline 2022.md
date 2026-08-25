# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Arch-Graph: Acyclic Architecture Relation Predictor for Task-Transferable Neural Architecture Search.
- **链接**: [arXiv:2204.05941](https://arxiv.org/abs/2204.05941)
- **作者**: Minbin Huang, Zhijian Huang, Changlin Li, Xin Chen, Hang Xu, Zhenguo Li et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, ReLER AAII, UTS, The University of Hong Kong
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Neural Architecture Search (NAS) aims to find efficient models for multiple tasks. Beyond seeking solutions for a single task, there are surging interests in transferring network design knowledge across multiple tasks. In this line of research, effectively modeling task correlations is vital yet highly neglected. Therefore, we propose \textbf{Arch-Graph}, a transferable NAS method that predicts task-specific optimal architectures with respect to given task embeddings. It leverages correlations across multiple tasks by using their embeddings as a part of the predictor's input for fast adaptation. We also formulate NAS as an architecture relation graph prediction problem, with the relational graph constructed by treating candidate architectures as nodes and their pairwise relations as edges. To enforce some basic properties such as acyclicity in the relational graph, we add additional constraints to the optimization process, converting NAS into the problem of finding a Maximal Weighted Acyclic Subgraph (MWAS). Our algorithm then strives to eliminate cycles and only establish edges in the graph if the rank results can be trusted. Through MWAS, Arch-Graph can effectively rank candidate models for each task with only a small budget to finetune the predictor. With extensive experiments on TransNAS-Bench-101, we show Arch-Graph's transferability and high sample efficiency across numerous tasks, beating many NAS methods designed for both single-task and multi-task search. It is able to find top 0.16\% and 0.29\% architectures on average on two search spaces under the budget of only 50 models.

### ISNAS-DIP: Image-Specific Neural Architecture Search for Deep Image Prior.
- **链接**: [arXiv:2111.15362](https://arxiv.org/abs/2111.15362) · [代码](https://github.com/ozgurkara99/ISNAS-DIP)
- **作者**: Metin Ersin Arican, Ozgur Kara, Gustav Bredell, Ender Konukoglu
- **🏷️ 机构**: Bogazici University,Department of Electrical and Electronics Engineering,Istanbul,Turkey, ETH-Zurich,Department of Information Technology and Electrical Engineering,Zurich,Switzerland
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Recent works show that convolutional neural network (CNN) architectures have a spectral bias towards lower frequencies, which has been leveraged for various image restoration tasks in the Deep Image Prior (DIP) framework. The benefit of the inductive bias the network imposes in the DIP framework depends on the architecture. Therefore, researchers have studied how to automate the search to determine the best-performing model. However, common neural architecture search (NAS) techniques are resource and time-intensive. Moreover, best-performing models are determined for a whole dataset of images instead of for each image independently, which would be prohibitively expensive. In this work, we first show that optimal neural architectures in the DIP framework are image-dependent. Leveraging this insight, we then propose an image-specific NAS strategy for the DIP framework that requires substantially less training than typical NAS approaches, effectively enabling image-specific NAS. We justify the proposed strategy's effectiveness by (1) demonstrating its performance on a NAS Dataset for DIP that includes 522 models from a particular search space (2) conducting extensive experiments on image denoising, inpainting, and super-resolution tasks. Our experiments show that image-specific metrics can reduce the search space to a small cohort of models, of which the best model outperforms current NAS approaches for image restoration. Codes and datasets are available at https://github.com/ozgurkara99/ISNAS-DIP.

### Demystifying the Neural Tangent Kernel from a Practical Perspective: Can it be trusted for Neural Architecture Search without training?
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01156)
- **作者**: Jisoo Mok, Byunggook Na, Ji-Hoon Kim, Dongyoon Han, Sungroh Yoon
- **🏷️ 机构**: Seoul National University,Department of ECE, NAVER AI Lab
- **会议**: CVPR 2022

### Distribution Consistent Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01061)
- **作者**: Junyi Pan, Chong Sun, Yizhou Zhou, Ying Zhang, Chen Li
- **🏷️ 机构**: WeChat, Tencent Inc
- **会议**: CVPR 2022

### HyperSegNAS: Bridging One-Shot Neural Architecture Search with 3D Medical Image Segmentation using HyperNet.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02008)
- **作者**: Cheng Peng, Andriy Myronenko, Ali Hatamizadeh, Vishwesh Nath, Md Mahfuzur Rahman Siddiquee, Yufan He et al.
- **🏷️ 机构**: Johns Hopkins University, NVIDIA, Arizona State University
- **会议**: CVPR 2022

### Global Convergence of MAML and Theory-Inspired Neural Architecture Search for Few-Shot Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00957)
- **作者**: Haoxiang Wang, Yite Wang, Ruoyu Sun, Bo Li
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2022

### Shapley-NAS: Discovering Operation Contribution for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01159)
- **作者**: Han Xiao, Ziwei Wang, Zheng Zhu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2022

### Performance-Aware Mutual Knowledge Distillation for Improving Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01162)
- **作者**: Pengtao Xie, Xuefeng Du
- **🏷️ 机构**: University of California, San Diego,La Jolla,CA,United States, University of Wisconsin-Madison,Madison,WI,United States
- **会议**: CVPR 2022

### β-DARTS: Beta-Decay Regularization for Differentiable Architecture Search.
- **链接**: [arXiv:2203.01665](https://arxiv.org/abs/2203.01665)
- **作者**: Peng Ye, Baopu Li, Yikang Li, Tao Chen, Jiayuan Fan, Wanli Ouyang
- **🏷️ 机构**: Fudan University, BAIDU USA LLC, Shanghai AI Laboratory
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Neural Architecture Search~(NAS) has attracted increasingly more attention in recent years because of its capability to design deep neural networks automatically. Among them, differential NAS approaches such as DARTS, have gained popularity for the search efficiency. However, they suffer from two main issues, the weak robustness to the performance collapse and the poor generalization ability of the searched architectures. To solve these two problems, a simple-but-efficient regularization method, termed as Beta-Decay, is proposed to regularize the DARTS-based NAS searching process. Specifically, Beta-Decay regularization can impose constraints to keep the value and variance of activated architecture parameters from too large. Furthermore, we provide in-depth theoretical analysis on how it works and why it works. Experimental results on NAS-Bench-201 show that our proposed method can help to stabilize the searching process and makes the searched network more transferable across different datasets. In addition, our search scheme shows an outstanding property of being less dependent on training time and data. Comprehensive experiments on a variety of search spaces and datasets validate the effectiveness of the proposed method.

### BaLeNAS: Differentiable Architecture Search via the Bayesian Learning Rule.
- **链接**: [arXiv:2111.13204](https://arxiv.org/abs/2111.13204)
- **作者**: Miao Zhang, Shirui Pan, Xiaojun Chang, Steven Su, Jilin Hu, Gholamreza Haffari et al.
- **🏷️ 机构**: Aalborg University, Monash University, ReLER, AAII, UTS
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Differentiable Architecture Search (DARTS) has received massive attention in recent years, mainly because it significantly reduces the computational cost through weight sharing and continuous relaxation. However, more recent works find that existing differentiable NAS techniques struggle to outperform naive baselines, yielding deteriorative architectures as the search proceeds. Rather than directly optimizing the architecture parameters, this paper formulates the neural architecture search as a distribution learning problem through relaxing the architecture weights into Gaussian distributions. By leveraging the natural-gradient variational inference (NGVI), the architecture distribution can be easily optimized based on existing codebases without incurring more memory and computational consumption. We demonstrate how the differentiable NAS benefits from Bayesian principles, enhancing exploration and improving stability. The experimental results on NAS-Bench-201 and NAS-Bench-1shot1 benchmark datasets confirm the significant improvements the proposed framework can make. In addition, instead of simply applying the argmax on the learned parameters, we further leverage the recently-proposed training-free proxies in NAS to select the optimal architecture from a group architectures drawn from the optimized distribution, where we achieve state-of-the-art results on the NAS-Bench-201 and NAS-Bench-1shot1 benchmarks. Our best architecture in the DARTS search space also obtains competitive test errors with 2.37\%, 15.72\%, and 24.2\% on CIFAR-10, CIFAR-100, and ImageNet datasets, respectively.

### Neural Architecture Search with Representation Mutual Information.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01161)
- **作者**: Xiawu Zheng, Xiang Fei, Lei Zhang, Chenglin Wu, Fei Chao, Jianzhuang Liu et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2022

### Training-free Transformer Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01062)
- **作者**: Qinqin Zhou, Kekai Sheng, Xiawu Zheng, Ke Li, Xing Sun, Yonghong Tian et al.
- **🏷️ 机构**: School of Informatics, Xiamen University,Media Analytics and Computing Lab, Tencent Youtu Lab, Peng Cheng Laboratory
- **会议**: CVPR 2022
