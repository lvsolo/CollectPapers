# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Arch-Graph: Acyclic Architecture Relation Predictor for Task-Transferable Neural Architecture Search.
- **链接**: [arXiv:2204.05941](https://arxiv.org/abs/2204.05941) · 📚 被引 21
- **作者**: Minbin Huang, Zhijian Huang, Changlin Li, Xin Chen, Hang Xu, Zhenguo Li et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, ReLER AAII, UTS, The University of Hong Kong
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) aims to find efficient models for multiple tasks. Beyond seeking solutions for a single task, there are surging interests in transferring network design knowledge across multiple tasks. In this line of research, effectively modeling task correlations is vital yet highly neglected. Therefore, we propose \textbf{Arch-Graph}, a transferable NAS method that predicts task-specific optimal architectures with respect to given task embeddings. It leverages correlations across multiple tasks by using their embeddings as a part of the predictor's input for fast adaptation. We also formulate NAS as an architecture relation graph prediction problem, with the relational graph constructed by treating candidate architectures as nodes and their pairwise relations as edges. To enforce some basic properties such as acyclicity in the relational graph, we add additional constraints to the optimization process, converting NAS into the problem of finding a Maximal Weighted Acyclic Subgraph (MWAS). Our algorithm then strives to eliminate cycles and only establish edges in the graph if the rank results can be trusted. Through MWAS, Arch-Graph can effectively rank candidate models for each task with only a small budget to finetune the predictor. With extensive experiments on TransNAS-Bench-101, we show Arch-Graph's transferability and high sample efficiency across numerous tasks, beating many NAS methods designed for both single-task and multi-task search. It is able to find top 0.16\% and 0.29\% architectures on average on two search spaces under the budget of only 50 models.

</details>

### ISNAS-DIP: Image-Specific Neural Architecture Search for Deep Image Prior.
- **链接**: [arXiv:2111.15362](https://arxiv.org/abs/2111.15362) · [代码](https://github.com/ozgurkara99/ISNAS-DIP) · 📚 被引 18
- **作者**: Metin Ersin Arican, Ozgur Kara, Gustav Bredell, Ender Konukoglu
- **🏷️ 机构**: Bogazici University,Department of Electrical and Electronics Engineering,Istanbul,Turkey, ETH-Zurich,Department of Information Technology and Electrical Engineering,Zurich,Switzerland
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works show that convolutional neural network (CNN) architectures have a spectral bias towards lower frequencies, which has been leveraged for various image restoration tasks in the Deep Image Prior (DIP) framework. The benefit of the inductive bias the network imposes in the DIP framework depends on the architecture. Therefore, researchers have studied how to automate the search to determine the best-performing model. However, common neural architecture search (NAS) techniques are resource and time-intensive. Moreover, best-performing models are determined for a whole dataset of images instead of for each image independently, which would be prohibitively expensive. In this work, we first show that optimal neural architectures in the DIP framework are image-dependent. Leveraging this insight, we then propose an image-specific NAS strategy for the DIP framework that requires substantially less training than typical NAS approaches, effectively enabling image-specific NAS. We justify the proposed strategy's effectiveness by (1) demonstrating its performance on a NAS Dataset for DIP that includes 522 models from a particular search space (2) conducting extensive experiments on image denoising, inpainting, and super-resolution tasks. Our experiments show that image-specific metrics can reduce the search space to a small cohort of models, of which the best model outperforms current NAS approaches for image restoration. Codes and datasets are available at https://github.com/ozgurkara99/ISNAS-DIP.

</details>

### Demystifying the Neural Tangent Kernel from a Practical Perspective: Can it be trusted for Neural Architecture Search without training?
- **链接**: [arXiv:2203.14577](https://arxiv.org/abs/2203.14577) · [代码](https://github.com/nutellamok/DemystifyingNTK) · 📚 被引 17
- **作者**: Jisoo Mok, Byunggook Na, Ji-Hoon Kim, Dongyoon Han, Sungroh Yoon
- **🏷️ 机构**: Seoul National University,Department of ECE, NAVER AI Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Neural Architecture Search (NAS), reducing the cost of architecture evaluation remains one of the most crucial challenges. Among a plethora of efforts to bypass training of each candidate architecture to convergence for evaluation, the Neural Tangent Kernel (NTK) is emerging as a promising theoretical framework that can be utilized to estimate the performance of a neural architecture at initialization. In this work, we revisit several at-initialization metrics that can be derived from the NTK and reveal their key shortcomings. Then, through the empirical analysis of the time evolution of NTK, we deduce that modern neural architectures exhibit highly non-linear characteristics, making the NTK-based metrics incapable of reliably estimating the performance of an architecture without some amount of training. To take such non-linear characteristics into account, we introduce Label-Gradient Alignment (LGA), a novel NTK-based metric whose inherent formulation allows it to capture the large amount of non-linear advantage present in modern neural architectures. With minimal amount of training, LGA obtains a meaningful level of rank correlation with the post-training test accuracy of an architecture. Lastly, we demonstrate that LGA, complemented with few epochs of training, successfully guides existing search algorithms to achieve competitive search performances with significantly less search cost. The code is available at: https://github.com/nutellamok/DemystifyingNTK.

</details>

### Distribution Consistent Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01061) · 📚 被引 7
- **作者**: Junyi Pan, Chong Sun, Yizhou Zhou, Ying Zhang, Chen Li
- **🏷️ 机构**: WeChat, Tencent Inc
- **会议**: CVPR 2022

### HyperSegNAS: Bridging One-Shot Neural Architecture Search with 3D Medical Image Segmentation using HyperNet.
- **链接**: [arXiv:2112.10652](https://arxiv.org/abs/2112.10652) · 📚 被引 32
- **作者**: Cheng Peng, Andriy Myronenko, Ali Hatamizadeh, Vishwesh Nath, Md Mahfuzur Rahman Siddiquee, Yufan He et al.
- **🏷️ 机构**: Johns Hopkins University, NVIDIA, Arizona State University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic segmentation of 3D medical images is a challenging task due to the high variability of the shape and pattern of objects (such as organs or tumors). Given the recent success of deep learning in medical image segmentation, Neural Architecture Search (NAS) has been introduced to find high-performance 3D segmentation network architectures. However, because of the massive computational requirements of 3D data and the discrete optimization nature of architecture search, previous NAS methods require a long search time or necessary continuous relaxation, and commonly lead to sub-optimal network architectures. While one-shot NAS can potentially address these disadvantages, its application in the segmentation domain has not been well studied in the expansive multi-scale multi-path search space. To enable one-shot NAS for medical image segmentation, our method, named HyperSegNAS, introduces a HyperNet to assist super-net training by incorporating architecture topology information. Such a HyperNet can be removed once the super-net is trained and introduces no overhead during architecture search. We show that HyperSegNAS yields better performing and more intuitive architectures compared to the previous state-of-the-art (SOTA) segmentation networks; furthermore, it can quickly and accurately find good architecture candidates under different computing constraints. Our method is evaluated on public datasets from the Medical Segmentation Decathlon (MSD) challenge, and achieves SOTA performances.

</details>

### Global Convergence of MAML and Theory-Inspired Neural Architecture Search for Few-Shot Learning.
- **链接**: [arXiv:2203.09137](https://arxiv.org/abs/2203.09137) · 📚 被引 34
- **作者**: Haoxiang Wang, Yite Wang, Ruoyu Sun, Bo Li
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model-agnostic meta-learning (MAML) and its variants have become popular approaches for few-shot learning. However, due to the non-convexity of deep neural nets (DNNs) and the bi-level formulation of MAML, the theoretical properties of MAML with DNNs remain largely unknown. In this paper, we first prove that MAML with over-parameterized DNNs is guaranteed to converge to global optima at a linear rate. Our convergence analysis indicates that MAML with over-parameterized DNNs is equivalent to kernel regression with a novel class of kernels, which we name as Meta Neural Tangent Kernels (MetaNTK). Then, we propose MetaNTK-NAS, a new training-free neural architecture search (NAS) method for few-shot learning that uses MetaNTK to rank and select architectures. Empirically, we compare our MetaNTK-NAS with previous NAS methods on two popular few-shot learning benchmarks, miniImageNet, and tieredImageNet. We show that the performance of MetaNTK-NAS is comparable or better than the state-of-the-art NAS method designed for few-shot learning while enjoying more than 100x speedup. We believe the efficiency of MetaNTK-NAS makes itself more practical for many real-world tasks.

</details>

### Shapley-NAS: Discovering Operation Contribution for Neural Architecture Search.
- **链接**: [arXiv:2206.09811](https://arxiv.org/abs/2206.09811) · [代码](https://github.com/Euphoria16/Shapley-NAS.git) · 📚 被引 55
- **作者**: Han Xiao, Ziwei Wang, Zheng Zhu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a Shapley value based method to evaluate operation contribution (Shapley-NAS) for neural architecture search. Differentiable architecture search (DARTS) acquires the optimal architectures by optimizing the architecture parameters with gradient descent, which significantly reduces the search cost. However, the magnitude of architecture parameters updated by gradient descent fails to reveal the actual operation importance to the task performance and therefore harms the effectiveness of obtained architectures. By contrast, we propose to evaluate the direct influence of operations on validation accuracy. To deal with the complex relationships between supernet components, we leverage Shapley value to quantify their marginal contributions by considering all possible combinations. Specifically, we iteratively optimize the supernet weights and update the architecture parameters by evaluating operation contributions via Shapley value, so that the optimal architectures are derived by selecting the operations that contribute significantly to the tasks. Since the exact computation of Shapley value is NP-hard, the Monte-Carlo sampling based algorithm with early truncation is employed for efficient approximation, and the momentum update mechanism is adopted to alleviate fluctuation of the sampling process. Extensive experiments on various datasets and various search spaces show that our Shapley-NAS outperforms the state-of-the-art methods by a considerable margin with light search cost. The code is available at https://github.com/Euphoria16/Shapley-NAS.git

</details>

### Performance-Aware Mutual Knowledge Distillation for Improving Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01162) · 📚 被引 13
- **作者**: Pengtao Xie, Xuefeng Du
- **🏷️ 机构**: University of California, San Diego,La Jolla,CA,United States, University of Wisconsin-Madison,Madison,WI,United States
- **会议**: CVPR 2022

### β-DARTS: Beta-Decay Regularization for Differentiable Architecture Search.
- **链接**: [arXiv:2203.01665](https://arxiv.org/abs/2203.01665) · 📚 被引 111
- **作者**: Peng Ye, Baopu Li, Yikang Li, Tao Chen, Jiayuan Fan, Wanli Ouyang
- **🏷️ 机构**: Fudan University, BAIDU USA LLC, Shanghai AI Laboratory
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search~(NAS) has attracted increasingly more attention in recent years because of its capability to design deep neural networks automatically. Among them, differential NAS approaches such as DARTS, have gained popularity for the search efficiency. However, they suffer from two main issues, the weak robustness to the performance collapse and the poor generalization ability of the searched architectures. To solve these two problems, a simple-but-efficient regularization method, termed as Beta-Decay, is proposed to regularize the DARTS-based NAS searching process. Specifically, Beta-Decay regularization can impose constraints to keep the value and variance of activated architecture parameters from too large. Furthermore, we provide in-depth theoretical analysis on how it works and why it works. Experimental results on NAS-Bench-201 show that our proposed method can help to stabilize the searching process and makes the searched network more transferable across different datasets. In addition, our search scheme shows an outstanding property of being less dependent on training time and data. Comprehensive experiments on a variety of search spaces and datasets validate the effectiveness of the proposed method.

</details>

### BaLeNAS: Differentiable Architecture Search via the Bayesian Learning Rule.
- **链接**: [arXiv:2111.13204](https://arxiv.org/abs/2111.13204) · 📚 被引 15
- **作者**: Miao Zhang, Shirui Pan, Xiaojun Chang, Steven Su, Jilin Hu, Gholamreza Haffari et al.
- **🏷️ 机构**: Aalborg University, Monash University, ReLER, AAII, UTS
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable Architecture Search (DARTS) has received massive attention in recent years, mainly because it significantly reduces the computational cost through weight sharing and continuous relaxation. However, more recent works find that existing differentiable NAS techniques struggle to outperform naive baselines, yielding deteriorative architectures as the search proceeds. Rather than directly optimizing the architecture parameters, this paper formulates the neural architecture search as a distribution learning problem through relaxing the architecture weights into Gaussian distributions. By leveraging the natural-gradient variational inference (NGVI), the architecture distribution can be easily optimized based on existing codebases without incurring more memory and computational consumption. We demonstrate how the differentiable NAS benefits from Bayesian principles, enhancing exploration and improving stability. The experimental results on NAS-Bench-201 and NAS-Bench-1shot1 benchmark datasets confirm the significant improvements the proposed framework can make. In addition, instead of simply applying the argmax on the learned parameters, we further leverage the recently-proposed training-free proxies in NAS to select the optimal architecture from a group architectures drawn from the optimized distribution, where we achieve state-of-the-art results on the NAS-Bench-201 and NAS-Bench-1shot1 benchmarks. Our best architecture in the DARTS search space also obtains competitive test errors with 2.37\%, 15.72\%, and 24.2\% on CIFAR-10, CIFAR-100, and ImageNet datasets, respectively.

</details>

### Neural Architecture Search with Representation Mutual Information.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01161)
- **作者**: Xiawu Zheng, Xiang Fei, Lei Zhang, Chenglin Wu, Fei Chao, Jianzhuang Liu et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2022

### Training-free Transformer Architecture Search.
- **链接**: [arXiv:2203.12217](https://arxiv.org/abs/2203.12217) · 📚 被引 56
- **作者**: Qinqin Zhou, Kekai Sheng, Xiawu Zheng, Ke Li, Xing Sun, Yonghong Tian et al.
- **🏷️ 机构**: School of Informatics, Xiamen University,Media Analytics and Computing Lab, Tencent Youtu Lab, Peng Cheng Laboratory
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, Vision Transformer (ViT) has achieved remarkable success in several computer vision tasks. The progresses are highly relevant to the architecture design, then it is worthwhile to propose Transformer Architecture Search (TAS) to search for better ViTs automatically. However, current TAS methods are time-consuming and existing zero-cost proxies in CNN do not generalize well to the ViT search space according to our experimental observations. In this paper, for the first time, we investigate how to conduct TAS in a training-free manner and devise an effective training-free TAS (TF-TAS) scheme. Firstly, we observe that the properties of multi-head self-attention (MSA) and multi-layer perceptron (MLP) in ViTs are quite different and that the synaptic diversity of MSA affects the performance notably. Secondly, based on the observation, we devise a modular strategy in TF-TAS that evaluates and ranks ViT architectures from two theoretical perspectives: synaptic diversity and synaptic saliency, termed as DSS-indicator. With DSS-indicator, evaluation results are strongly correlated with the test accuracies of ViT models. Experimental results demonstrate that our TF-TAS achieves a competitive performance against the state-of-the-art manually or automatically design ViT architectures, and it promotes the searching efficiency in ViT search space greatly: from about $24$ GPU days to less than $0.5$ GPU days. Moreover, the proposed DSS-indicator outperforms the existing cutting-edge zero-cost approaches (e.g., TE-score and NASWOT).

</details>
