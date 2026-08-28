# Neural Architecture Search — 2020 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Stabilizing Differentiable Architecture Search via Perturbation-based Regularization.
- **链接**: [arXiv:2002.05283](https://arxiv.org/abs/2002.05283)
- **作者**: Xiangning Chen, Cho-Jui Hsieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable architecture search (DARTS) is a prevailing NAS solution to identify architectures. Based on the continuous relaxation of the architecture space, DARTS learns a differentiable architecture weight and largely reduces the search cost. However, its stability has been challenged for yielding deteriorating architectures as the search proceeds. We find that the precipitous validation loss landscape, which leads to a dramatic performance drop when distilling the final architecture, is an essential factor that causes instability. Based on this observation, we propose a perturbation-based regularization - SmoothDARTS (SDARTS), to smooth the loss landscape and improve the generalizability of DARTS-based methods. In particular, our new formulations stabilize DARTS-based methods by either random smoothing or adversarial attack. The search trajectory on NAS-Bench-1Shot1 demonstrates the effectiveness of our approach and due to the improved stability, we achieve performance gain across various search spaces on 4 datasets. Furthermore, we mathematically show that SDARTS implicitly regularizes the Hessian norm of the validation loss, which accounts for a smoother loss landscape and improved performance.

</details>

### Neural Architecture Search in A Proxy Validation Loss Landscape.
- **链接**: [出版页](http://proceedings.mlr.press/v119/li20c.html)
- **作者**: Yanxi Li, Minjing Dong, Yunhe Wang, Chang Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data.
- **链接**: [arXiv:1912.07768](https://arxiv.org/abs/1912.07768)
- **作者**: Felipe Petroski Such, Aditya Rawal, Joel Lehman, Kenneth O. Stanley, Jeffrey Clune
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper investigates the intriguing question of whether we can create learning algorithms that automatically generate training data, learning environments, and curricula in order to help AI agents rapidly learn. We show that such algorithms are possible via Generative Teaching Networks (GTNs), a general approach that is, in theory, applicable to supervised, unsupervised, and reinforcement learning, although our experiments only focus on the supervised case. GTNs are deep neural networks that generate data and/or training environments that a learner (e.g. a freshly initialized neural network) trains on for a few SGD steps before being tested on a target task. We then differentiate through the entire learning process via meta-gradients to update the GTN parameters to improve performance on the target task. GTNs have the beneficial property that they can theoretically generate any type of data or training environment, making their potential impact large. This paper introduces GTNs, discusses their potential, and showcases that they can substantially accelerate learning. We also demonstrate a practical and exciting application of GTNs: accelerating the evaluation of candidate architectures for neural architecture search (NAS), which is rate-limited by such evaluations, enabling massive speed-ups in NAS. GTN-NAS improves the NAS state of the art, finding higher performing architectures when controlling for the search proposal mechanism. GTN-NAS also is competitive with the overall state of the art approaches, which achieve top performance while using orders of magnitude less computation than typical NAS methods. Speculating forward, GTNs may represent a first step toward the ambitious goal of algorithms that generate their own training data and, in doing so, open a variety of interesting new research questions and directions.

</details>
