# VLM — 2024 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2405.05256](https://arxiv.org/abs/2405.05256) · 📚 被引 19
- **作者**: Prannay Kaul, Zhizhong Li, Hao Yang, Yonatan Dukler, Ashwin Swaminathan, C. J. Taylor et al.
- **🏷️ 机构**: University of Oxford,VGG, AWS AI Labs
- **会议**: CVPR 2024
- **摘要（中）**: ①针对大型视觉语言模型（LVLM）在自由形式生成中的幻觉问题，现有基准主要评估特定问题格式（如多项选择）的幻觉（Type II），而忽略了开放式回答中的幻觉（Type I），且两者往往负相关。②提出了THRONE，一个基于对象的自动评估框架，利用公开语言模型识别LVLM自由输出中的幻觉，并计算信息量丰富的指标。③改进点在于无需外部API调用，且专门针对Type I幻觉进行量化评估。④通过在多个最新LVLM上的评估，表明现有指标的改进并不减少Type I幻觉，揭示了现有基准的局限性。
- **摘要（英）**: This paper addresses the hallucination issue in large vision-language models (LVLMs) during free-form generation, which is often overlooked by existing benchmarks focusing on specific question formats. It proposes THRONE, an object-based automatic framework that uses public language models to detect hallucinations and compute informative metrics. The evaluation shows that improvements in existing metrics do not reduce Type I hallucinations, highlighting the limitations of current benchmarks.
- **核心贡献**: 提出了首个针对LVLM自由形式生成中Type I幻觉的自动评估框架THRONE。
- **创新点**: 利用公开语言模型自动识别幻觉，无需外部API，并区分Type I和Type II幻觉。
- **结果**: 实验表明现有指标改进与Type I幻觉减少不相关，揭示了基准的不足。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mitigating hallucinations in large vision-language models (LVLMs) remains an open problem. Recent benchmarks do not address hallucinations in open-ended free-form responses, which we term "Type I hallucinations". Instead, they focus on hallucinations responding to very specific question formats -- typically a multiple-choice response regarding a particular object or attribute -- which we term "Type II hallucinations". Additionally, such benchmarks often require external API calls to models which are subject to change. In practice, we observe that a reduction in Type II hallucinations does not lead to a reduction in Type I hallucinations but rather that the two forms of hallucinations are often anti-correlated. To address this, we propose THRONE, a novel object-based automatic framework for quantitatively evaluating Type I hallucinations in LVLM free-form outputs. We use public language models (LMs) to identify hallucinations in LVLM responses and compute informative metrics. By evaluating a large selection of recent LVLMs using public datasets, we show that an improvement in existing metrics do not lead to a reduction in Type I hallucinations, and that established benchmarks for measuring Type I hallucinations are incomplete. Finally, we provide a simple and effective data augmentation method to reduce Type I and Type II hallucinations as a strong baseline. Code is now available at https://github.com/amazon-science/THRONE .

</details>

### DeIL: Direct-and-Inverse CLIP for Open-World Few-Shot Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02693) · 📚 被引 15
- **作者**: Shuai Shao, Yu Bai, Yan Wang, Baodi Liu, Yicong Zhou
- **🏷️ 机构**: Zhejiang Lab, China University of Petroleum (East China), Beihang University
- **会议**: CVPR 2024

### Towards Better Vision-Inspired Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01285) · 📚 被引 6
- **作者**: Yun-Hao Cao, Kaixiang Ji, Ziyuan Huang, Chuanyang Zheng, Jiajia Liu, Jian Wang et al.
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology, Ant Group
- **会议**: CVPR 2024

### DRESS : Instructing Large Vision-Language Models to Align and Interact with Humans via Natural Language Feedback.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01350) · 📚 被引 21
- **作者**: Yangyi Chen, Karan Sikka, Michael Cogswell, Heng Ji, Ajay Divakaran
- **🏷️ 机构**: SRI International, University of Illinois Urbana-Champaign
- **会议**: CVPR 2024

### Hallusionbench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01363) · 📚 被引 144
- **作者**: Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia Li, Xiaoyu Liu et al.
- **🏷️ 机构**: University of Maryland,College Park
- **会议**: CVPR 2024

### Language Models as Black-Box Optimizers for Vision-Language Models.
- **链接**: [arXiv:2309.05950](https://arxiv.org/abs/2309.05950) · 📚 被引 22
- **作者**: Shihong Liu, Samuel Yu, Zhiqiu Lin, Deepak Pathak, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) pre-trained on web-scale datasets have demonstrated remarkable capabilities on downstream tasks when fine-tuned with minimal data. However, many VLMs rely on proprietary data and are not open-source, which restricts the use of white-box approaches for fine-tuning. As such, we aim to develop a black-box approach to optimize VLMs through natural language prompts, thereby avoiding the need to access model parameters, feature embeddings, or even output logits. We propose employing chat-based LLMs to search for the best text prompt for VLMs. Specifically, we adopt an automatic hill-climbing procedure that converges to an effective prompt by evaluating the performance of current prompts and asking LLMs to refine them based on textual feedback, all within a conversational process without human-in-the-loop. In a challenging 1-shot image classification setup, our simple approach surpasses the white-box continuous prompting method (CoOp) by an average of 1.5% across 11 datasets including ImageNet. Our approach also outperforms both human-engineered and LLM-generated prompts. We highlight the advantage of conversational feedback that incorporates both positive and negative prompts, suggesting that LLMs can utilize the implicit gradient direction in textual feedback for a more efficient search. In addition, we find that the text prompts generated through our strategy are not only more interpretable but also transfer well across different VLM architectures in a black-box manner. Lastly, we apply our framework to optimize the state-of-the-art black-box VLM (DALL-E 3) for text-to-image generation, prompt inversion, and personalization.

</details>

### Sonic VisionLM: Playing Sound with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02537) · 📚 被引 16
- **作者**: Zhifeng Xie, Shengye Yu, Qile He, Mengtian Li
- **🏷️ 机构**: Shanghai University
- **会议**: CVPR 2024

### PeVL: Pose-Enhanced Vision-Language Model for Fine-Grained Human Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01784) · 📚 被引 12
- **作者**: Haosong Zhang, Mei Chee Leong, Liyuan Li, Weisi Lin
- **🏷️ 机构**: Institute for Infocomm Research (I2R), A *STAR,Singapore, Nanyang Technological University,Singapore
- **会议**: CVPR 2024

### Dual Memory Networks: A Versatile Adaptation Approach for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02713) · 📚 被引 43
- **作者**: Yabin Zhang, Wenjie Zhu, Hui Tang, Zhiyuan Ma, Kaiyang Zhou, Lei Zhang
- **🏷️ 机构**: HKPolyU, HKUST, HKBU
- **会议**: CVPR 2024

### SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01370) · 📚 被引 225
- **作者**: Boyuan Chen, Zhuo Xu, Sean Kirmani, Brian Ichter, Dorsa Sadigh, Leonidas J. Guibas et al.
- **🏷️ 机构**: Google DeepMind, Google Research
- **会议**: CVPR 2024

### Leveraging Vision-Language Models for Improving Domain Generalization in Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02258) · 📚 被引 32
- **作者**: Sravanti Addepalli, Ashish Ramayee Asokan, Lakshay Sharma, R. Venkatesh Babu
- **🏷️ 机构**: Indian Institute of Science,Vision and AI Lab,Bangalore
- **会议**: CVPR 2024

### Active Prompt Learning in Vision Language Models.
- **链接**: [arXiv:2311.11178](https://arxiv.org/abs/2311.11178) · 📚 被引 9
- **作者**: Jihwan Bang, Sumyeong Ahn, Jae-Gil Lee
- **🏷️ 机构**: KAIST Michigan, State University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained Vision Language Models (VLMs) have demonstrated notable progress in various zero-shot tasks, such as classification and retrieval. Despite their performance, because improving performance on new tasks requires task-specific knowledge, their adaptation is essential. While labels are needed for the adaptation, acquiring them is typically expensive. To overcome this challenge, active learning, a method of achieving a high performance by obtaining labels for a small number of samples from experts, has been studied. Active learning primarily focuses on selecting unlabeled samples for labeling and leveraging them to train models. In this study, we pose the question, "how can the pre-trained VLMs be adapted under the active learning framework?" In response to this inquiry, we observe that (1) simply applying a conventional active learning framework to pre-trained VLMs even may degrade performance compared to random selection because of the class imbalance in labeling candidates, and (2) the knowledge of VLMs can provide hints for achieving the balance before labeling. Based on these observations, we devise a novel active learning framework for VLMs, denoted as PCB. To assess the effectiveness of our approach, we conduct experiments on seven different real-world datasets, and the results demonstrate that PCB surpasses conventional active learning and random sampling methods. Code will be available in https://github.com/kaist-dmlab/pcb .

</details>

### FFF: Fixing Flawed Foundations in contrastive pre-training results in very strong Vision-Language models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01344) · 📚 被引 8
- **作者**: Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
- **🏷️ 机构**: Samsung AI Center Cambridge,UK
- **会议**: CVPR 2024

### PracticalDG: Perturbation Distillation on Vision-Language Models for Hybrid Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02218) · 📚 被引 19
- **作者**: Zining Chen, Weiqiu Wang, Zhicheng Zhao, Fei Su, Aidong Men, Hongying Meng
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,The school of Artificial Intelligence, Brunel University Uxbridge
- **会议**: CVPR 2024

### EgoThink: Evaluating First-Person Perspective Thinking Capability of Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01355) · 📚 被引 26
- **作者**: Sijie Cheng, Zhicheng Guo, Jingwen Wu, Kechen Fang, Peng Li, Huaping Liu et al.
- **🏷️ 机构**: Tsinghua University,Department of Computer Science and Technology, University of Toronto,Department of Electrical and Computer Engineering, Tsinghua University,Zhili College
- **会议**: CVPR 2024

### JoAPR: Cleaning the Lens of Prompt Learning for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02711) · 📚 被引 6
- **作者**: Yuncheng Guo, Xiaodong Gu
- **🏷️ 机构**: Fudan University,Department of Electronic Engineering,Shanghai,China,200438
- **会议**: CVPR 2024

### RegionGPT: Towards Region Understanding Vision Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01309) · 📚 被引 54
- **作者**: Qiushan Guo, Shalini De Mello, Hongxu Yin, Wonmin Byeon, Ka Chun Cheung, Yizhou Yu et al.
- **🏷️ 机构**: The University of Hong Kong, NVIDIA
- **会议**: CVPR 2024

### Anchor-based Robust Finetuning of Vision-Language Models.
- **链接**: [arXiv:2404.06244](https://arxiv.org/abs/2404.06244) · 📚 被引 6
- **作者**: Jinwei Han, Zhiwen Lin, Zhongyisun Sun, Yingguo Gao, Ke Yan, Shouhong Ding et al.
- **🏷️ 机构**: School of Computer Science, Wuhan University, YouTu Lab, Tencent, Electronic Information School, Wuhan University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We aim at finetuning a vision-language model without hurting its out-of-distribution (OOD) generalization. We address two types of OOD generalization, i.e., i) domain shift such as natural to sketch images, and ii) zero-shot capability to recognize the category that was not contained in the finetune data. Arguably, the diminished OOD generalization after finetuning stems from the excessively simplified finetuning target, which only provides the class information, such as ``a photo of a [CLASS]''. This is distinct from the process in that CLIP was pretrained, where there is abundant text supervision with rich semantic information. Therefore, we propose to compensate for the finetune process using auxiliary supervision with rich semantic information, which acts as anchors to preserve the OOD generalization. Specifically, two types of anchors are elaborated in our method, including i) text-compensated anchor which uses the images from the finetune set but enriches the text supervision from a pretrained captioner, ii) image-text-pair anchor which is retrieved from the dataset similar to pretraining data of CLIP according to the downstream task, associating with the original CLIP text with rich semantics. Those anchors are utilized as auxiliary semantic information to maintain the original feature space of CLIP, thereby preserving the OOD generalization capabilities. Comprehensive experiments demonstrate that our method achieves in-distribution performance akin to conventional finetuning while attaining new state-of-the-art results on domain shift and zero-shot learning benchmarks.

</details>

### SocialCounterfactuals: Probing and Mitigating Intersectional Social Biases in Vision-Language Models with Counterfactual Examples.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01138) · 📚 被引 15
- **作者**: Phillip Howard, Avinash Madasu, Tiep Le, Gustavo A. Lujan-Moreno, Anahita Bhiwandiwalla, Vasudev Lal
- **🏷️ 机构**: Intel Labs
- **会议**: CVPR 2024

### Visual Program Distillation: Distilling Tools and Programmatic Reasoning into Vision-Language Models.
- **链接**: [arXiv:2312.03052](https://arxiv.org/abs/2312.03052) · 📚 被引 38
- **作者**: Yushi Hu, Otilia Stretcu, Chun-Ta Lu, Krishnamurthy Viswanathan, Kenji Hata, Enming Luo et al.
- **🏷️ 机构**: Google Research, University of Washington
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Solving complex visual tasks such as "Who invented the musical instrument on the right?" involves a composition of skills: understanding space, recognizing instruments, and also retrieving prior knowledge. Recent work shows promise by decomposing such tasks using a large language model (LLM) into an executable program that invokes specialized vision models. However, generated programs are error-prone: they omit necessary steps, include spurious ones, and are unable to recover when the specialized models give incorrect outputs. Moreover, they require loading multiple models, incurring high latency and computation costs. We propose Visual Program Distillation (VPD), an instruction tuning framework that produces a vision-language model (VLM) capable of solving complex visual tasks with a single forward pass. VPD distills the reasoning ability of LLMs by using them to sample multiple candidate programs, which are then executed and verified to identify a correct one. It translates each correct program into a language description of the reasoning steps, which are then distilled into a VLM. Extensive experiments show that VPD improves the VLM's ability to count, understand spatial relations, and reason compositionally. Our VPD-trained PaLI-X outperforms all prior VLMs, achieving state-of-the-art performance across complex vision tasks, including MMBench, OK-VQA, A-OKVQA, TallyQA, POPE, and Hateful Memes. An evaluation with human annotators also confirms that VPD improves model response factuality and consistency. Finally, experiments on content moderation demonstrate that VPD is also helpful for adaptation to real-world applications with limited data.

</details>

### Semantic Shield: Defending Vision-Language Models Against Backdooring and Poisoning via Fine-Grained Knowledge Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02344) · 📚 被引 3
- **作者**: Alvi Md. Ishmam, Christopher Thomas
- **🏷️ 机构**: Virginia Tech
- **会议**: CVPR 2024

### Efficient Test-Time Adaptation of Vision-Language Models.
- **链接**: [arXiv:2403.18293](https://arxiv.org/abs/2403.18293)
- **作者**: Adilbek Karmanov, Dayan Guan, Shijian Lu, Abdulmotaleb El Saddik, Eric P. Xing
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation with pre-trained vision-language models has attracted increasing attention for tackling distribution shifts during the test time. Though prior studies have achieved very promising performance, they involve intensive computation which is severely unaligned with test-time adaptation. We design TDA, a training-free dynamic adapter that enables effective and efficient test-time adaptation with vision-language models. TDA works with a lightweight key-value cache that maintains a dynamic queue with few-shot pseudo labels as values and the corresponding test-sample features as keys. Leveraging the key-value cache, TDA allows adapting to test data gradually via progressive pseudo label refinement which is super-efficient without incurring any backpropagation. In addition, we introduce negative pseudo labeling that alleviates the adverse impact of pseudo label noises by assigning pseudo labels to certain negative classes when the model is uncertain about its pseudo label predictions. Extensive experiments over two benchmarks demonstrate TDA's superior effectiveness and efficiency as compared with the state-of-the-art. The code has been released in \url{https://kdiaaa.github.io/tda/}.

</details>

### Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding.
- **链接**: [arXiv:2311.16922](https://arxiv.org/abs/2311.16922) · 📚 被引 184
- **作者**: Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Li, Shijian Lu, Chunyan Miao et al.
- **🏷️ 机构**: DAMO Academy, Alibaba Group, Nanyang Technological University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have advanced considerably, intertwining visual recognition and language understanding to generate content that is not only coherent but also contextually attuned. Despite their success, LVLMs still suffer from the issue of object hallucinations, where models generate plausible yet incorrect outputs that include objects that do not exist in the images. To mitigate this issue, we introduce Visual Contrastive Decoding (VCD), a simple and training-free method that contrasts output distributions derived from original and distorted visual inputs. The proposed VCD effectively reduces the over-reliance on statistical bias and unimodal priors, two essential causes of object hallucinations. This adjustment ensures the generated content is closely grounded to visual inputs, resulting in contextually accurate outputs. Our experiments show that VCD, without either additional training or the usage of external tools, significantly mitigates the object hallucination issue across different LVLM families. Beyond mitigating object hallucinations, VCD also excels in general LVLM benchmarks, highlighting its wide-ranging applicability.

</details>

### PromptKD: Unsupervised Prompt Distillation for Vision-Language Models.
- **链接**: [arXiv:2403.02781](https://arxiv.org/abs/2403.02781) · 📚 被引 110
- **作者**: Zheng Li, Xiang Li, Xinyi Fu, Xin Zhang, Weiqiang Wang, Shuo Chen et al.
- **🏷️ 机构**: College of Computer Science, Nankai University,PCA Lab, VCIP, NKIARI,Shenzhen Futian, Ant Group,Tiansuan Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has emerged as a valuable technique in enhancing vision-language models (VLMs) such as CLIP for downstream tasks in specific domains. Existing work mainly focuses on designing various learning forms of prompts, neglecting the potential of prompts as effective distillers for learning from larger teacher models. In this paper, we introduce an unsupervised domain prompt distillation framework, which aims to transfer the knowledge of a larger teacher model to a lightweight target model through prompt-driven imitation using unlabeled domain images. Specifically, our framework consists of two distinct stages. In the initial stage, we pre-train a large CLIP teacher model using domain (few-shot) labels. After pre-training, we leverage the unique decoupled-modality characteristics of CLIP by pre-computing and storing the text features as class vectors only once through the teacher text encoder. In the subsequent stage, the stored class vectors are shared across teacher and student image encoders for calculating the predicted logits. Further, we align the logits of both the teacher and student models via KL divergence, encouraging the student image encoder to generate similar probability distributions to the teacher through the learnable prompts. The proposed prompt distillation process eliminates the reliance on labeled data, enabling the algorithm to leverage a vast amount of unlabeled images within the domain. Finally, the well-trained student image encoders and pre-stored text features (class vectors) are utilized for inference. To our best knowledge, we are the first to (1) perform unsupervised domain-specific prompt-driven knowledge distillation for CLIP, and (2) establish a practical pre-storing mechanism of text features as shared class vectors between teacher and student. Extensive experiments on 11 datasets demonstrate the effectiveness of our method.

</details>

### FairCLIP: Harnessing Fairness in Vision-Language Learning.
- **链接**: [arXiv:2403.19949](https://arxiv.org/abs/2403.19949) · 📚 被引 53
- **作者**: Yan Luo, Min Shi, Muhammad Osama Khan, Muhammad Muneeb Afzal, Hao Huang, Shuaihang Yuan et al.
- **🏷️ 机构**: Harvard University,Harvard Ophthalmology AI Lab, Tandon School of Engineering, New York University, New York University Abu Dhabi,Multimedia and Visual Computing Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fairness is a critical concern in deep learning, especially in healthcare, where these models influence diagnoses and treatment decisions. Although fairness has been investigated in the vision-only domain, the fairness of medical vision-language (VL) models remains unexplored due to the scarcity of medical VL datasets for studying fairness. To bridge this research gap, we introduce the first fair vision-language medical dataset Harvard-FairVLMed that provides detailed demographic attributes, ground-truth labels, and clinical notes to facilitate an in-depth examination of fairness within VL foundation models. Using Harvard-FairVLMed, we conduct a comprehensive fairness analysis of two widely-used VL models (CLIP and BLIP2), pre-trained on both natural and medical domains, across four different protected attributes. Our results highlight significant biases in all VL models, with Asian, Male, Non-Hispanic, and Spanish being the preferred subgroups across the protected attributes of race, gender, ethnicity, and language, respectively. In order to alleviate these biases, we propose FairCLIP, an optimal-transport-based approach that achieves a favorable trade-off between performance and fairness by reducing the Sinkhorn distance between the overall sample distribution and the distributions corresponding to each demographic group. As the first VL dataset of its kind, Harvard-FairVLMed holds the potential to catalyze advancements in the development of machine learning models that are both ethically aware and clinically effective. Our dataset and code are available at https://ophai.hms.harvard.edu/datasets/harvard-fairvlmed10k.

</details>

### The Neglected Tails in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01234) · 📚 被引 31
- **作者**: Shubham Parashar, Zhiqiu Lin, Tian Liu, Xiangjue Dong, Yanan Li, Deva Ramanan et al.
- **🏷️ 机构**: Texas A&#x0026;M University, Carnegie Mellon University, Zhejiang Lab
- **会议**: CVPR 2024

### Jack of All Tasks, Master of Many: Designing General-purpose Coarse-to-Fine Vision-Language Model.
- **链接**: [arXiv:2312.12423](https://arxiv.org/abs/2312.12423) · 📚 被引 25
- **作者**: Shraman Pramanick, Guangxing Han, Rui Hou, Sayan Nag, Ser-Nam Lim, Nicolas Ballas et al.
- **🏷️ 机构**: Johns Hopkins University, Meta, University of Toronto
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability of large language models (LLMs) to process visual inputs has given rise to general-purpose vision systems, unifying various vision-language (VL) tasks by instruction tuning. However, due to the enormous diversity in input-output formats in the vision domain, existing general-purpose models fail to successfully integrate segmentation and multi-image inputs with coarse-level tasks into a single framework. In this work, we introduce VistaLLM, a powerful visual system that addresses coarse- and fine-grained VL tasks over single and multiple input images using a unified framework. VistaLLM utilizes an instruction-guided image tokenizer that filters global embeddings using task descriptions to extract compressed and refined features from numerous images. Moreover, VistaLLM employs a gradient-aware adaptive sampling technique to represent binary segmentation masks as sequences, significantly improving over previously used uniform sampling. To bolster the desired capability of VistaLLM, we curate CoinIt, a comprehensive coarse-to-fine instruction tuning dataset with 6.8M samples. We also address the lack of multi-image grounding datasets by introducing a novel task, AttCoSeg (Attribute-level Co-Segmentation), which boosts the model's reasoning and grounding capability over multiple input images. Extensive experiments on a wide range of V- and VL tasks demonstrate the effectiveness of VistaLLM by achieving consistent state-of-the-art performance over strong baselines across all downstream tasks. Our project page can be found at https://shramanpramanick.github.io/VistaLLM/.

</details>

### Building Vision-Language Models on Solid Foundations with Masked Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01348) · 📚 被引 8
- **作者**: Sepehr Sameni, Kushal Kafle, Hao Tan, Simon Jenni
- **🏷️ 机构**: University of Bern, Adobe Research
- **会议**: CVPR 2024

### Non-autoregressive Sequence-to-Sequence Vision-Language Models.
- **链接**: [arXiv:2403.02249](https://arxiv.org/abs/2403.02249) · 📚 被引 2
- **作者**: Kunyu Shi, Qi Dong, Luis Goncalves, Zhuowen Tu, Stefano Soatto
- **🏷️ 机构**: AWS AI Labs
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sequence-to-sequence vision-language models are showing promise, but their applicability is limited by their inference latency due to their autoregressive way of generating predictions. We propose a parallel decoding sequence-to-sequence vision-language model, trained with a Query-CTC loss, that marginalizes over multiple inference paths in the decoder. This allows us to model the joint distribution of tokens, rather than restricting to conditional distribution as in an autoregressive model. The resulting model, NARVL, achieves performance on-par with its state-of-the-art autoregressive counterpart, but is faster at inference time, reducing from the linear complexity associated with the sequential generation of tokens to a paradigm of constant time joint inference.

</details>

### A Closer Look at the Few-Shot Adaptation of Large Vision-Language Models.
- **链接**: [arXiv:2312.12730](https://arxiv.org/abs/2312.12730) · 📚 被引 50
- **作者**: Julio Silva-Rodríguez, Sina Hajimiri, Ismail Ben Ayed, Jose Dolz
- **🏷️ 机构**: &#x00E9;TS Montreal
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient transfer learning (ETL) is receiving increasing attention to adapt large pre-trained language-vision models on downstream tasks with a few labeled samples. While significant progress has been made, we reveal that state-of-the-art ETL approaches exhibit strong performance only in narrowly-defined experimental setups, and with a careful adjustment of hyperparameters based on a large corpus of labeled samples. In particular, we make two interesting, and surprising empirical observations. First, to outperform a simple Linear Probing baseline, these methods require to optimize their hyper-parameters on each target task. And second, they typically underperform -- sometimes dramatically -- standard zero-shot predictions in the presence of distributional drifts. Motivated by the unrealistic assumptions made in the existing literature, i.e., access to a large validation set and case-specific grid-search for optimal hyperparameters, we propose a novel approach that meets the requirements of real-world scenarios. More concretely, we introduce a CLass-Adaptive linear Probe (CLAP) objective, whose balancing term is optimized via an adaptation of the general Augmented Lagrangian method tailored to this context. We comprehensively evaluate CLAP on a broad span of datasets and scenarios, demonstrating that it consistently outperforms SoTA approaches, while yet being a much more efficient alternative.

</details>

### Label Propagation for Zero-shot Classification with Vision-Language Models.
- **链接**: [arXiv:2404.04072](https://arxiv.org/abs/2404.04072) · 📚 被引 15
- **作者**: Vladan Stojnic, Yannis Kalantidis, Giorgos Tolias
- **🏷️ 机构**: Czech Technical University in Prague,VRG, FEE, NAVER LABS Europe
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have demonstrated impressive performance on zero-shot classification, i.e. classification when provided merely with a list of class names. In this paper, we tackle the case of zero-shot classification in the presence of unlabeled data. We leverage the graph structure of the unlabeled data and introduce ZLaP, a method based on label propagation (LP) that utilizes geodesic distances for classification. We tailor LP to graphs containing both text and image features and further propose an efficient method for performing inductive inference based on a dual solution and a sparsification step. We perform extensive experiments to evaluate the effectiveness of our method on 14 common datasets and show that ZLaP outperforms the latest related works. Code: https://github.com/vladan-stojnic/ZLaP

</details>

### Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation.
- **链接**: [arXiv:2404.01943](https://arxiv.org/abs/2404.01943) · 📚 被引 31
- **作者**: Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, Junjie Hu, Ming Jiang et al.
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences,Beijing,China,100190, University of Wisconsin,Department of Computer Science,Madison,WI,USA, Indiana University,Department of Human-centered Computing,Indianapolis,IN,USA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-language navigation (VLN) enables the agent to navigate to a remote location following the natural language instruction in 3D environments. At each navigation step, the agent selects from possible candidate locations and then makes the move. For better navigation planning, the lookahead exploration strategy aims to effectively evaluate the agent's next action by accurately anticipating the future environment of candidate locations. To this end, some existing works predict RGB images for future environments, while this strategy suffers from image distortion and high computational cost. To address these issues, we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments, which are more robust and efficient than pixel-wise RGB reconstruction. Furthermore, with the predicted future environmental representations, our lookahead VLN model is able to construct the navigable future path tree and select the optimal path via efficient parallel evaluation. Extensive experiments on the VLN-CE datasets confirm the effectiveness of our method.

</details>

### SC- Tune: Unleashing Self-Consistent Referential Comprehension in Large Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01242) · 📚 被引 6
- **作者**: Tongtian Yue, Jie Cheng, Longteng Guo, Xingyuan Dai, Zijia Zhao, Xingjian He et al.
- **🏷️ 机构**: Laboratory of Cognition and Decision Intelligence for Complex Systems, CASIA, State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA
- **会议**: CVPR 2024

### On the Test-Time Zero-Shot Generalization of Vision-Language Models: Do we Really need Prompt Learning?
- **链接**: [arXiv:2405.02266](https://arxiv.org/abs/2405.02266) · 📚 被引 34
- **作者**: Maxime Zanella, Ismail Ben Ayed
- **🏷️ 机构**: UCLouvain UMons, &#x00C9;ts Montr&#x00E9;al
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The development of large vision-language models, notably CLIP, has catalyzed research into effective adaptation techniques, with a particular focus on soft prompt tuning. Conjointly, test-time augmentation, which utilizes multiple augmented views of a single image to enhance zero-shot generalization, is emerging as a significant area of interest. This has predominantly directed research efforts toward test-time prompt tuning. In contrast, we introduce a robust MeanShift for Test-time Augmentation (MTA), which surpasses prompt-based methods without requiring this intensive training procedure. This positions MTA as an ideal solution for both standalone and API-based applications. Additionally, our method does not rely on ad hoc rules (e.g., confidence threshold) used in some previous test-time augmentation techniques to filter the augmented views. Instead, MTA incorporates a quality assessment variable for each view directly into its optimization process, termed as the inlierness score. This score is jointly optimized with a density mode seeking process, leading to an efficient training- and hyperparameter-free approach. We extensively benchmark our method on 15 datasets and demonstrate MTA's superiority and computational efficiency. Deployed easily as plug-and-play module on top of zero-shot models and state-of-the-art few-shot methods, MTA shows systematic and consistent improvements.

</details>

### Investigating Compositional Challenges in Vision-Language Models for Visual Grounding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01341) · 📚 被引 12
- **作者**: Yunan Zeng, Yan Huang, Jinjin Zhang, Zequn Jie, Zhenhua Chai, Liang Wang
- **🏷️ 机构**: Center for Research on Intelligent Perception and Computing (CRIPAC), Meituan
- **会议**: CVPR 2024

### Semantics-Aware Motion Retargeting with Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00210) · 📚 被引 11
- **作者**: Haodong Zhang, Zhike Chen, Haocheng Xu, Lei Hao, Xiaofei Wu, Songcen Xu et al.
- **🏷️ 机构**: Zhejiang University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024

### CLIP-KD: An Empirical Study of CLIP Model Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01510) · 📚 被引 67
- **作者**: Chuanguang Yang, Zhulin An, Libo Huang, Junyu Bi, Xinqiang Yu, Han Yang et al.
- **🏷️ 机构**: Institute of Computing Technology,Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [object-detection](../object-detection/Guideline%202024.md)
- BLINK: Multimodal Large Language Models Can See but Not Perceive. → [multimodal](../multimodal/Guideline%202024.md)
- Eyes Closed, Safety on: Protecting Multimodal LLMs via Image-to-Text Transformation. → [multimodal](../multimodal/Guideline%202024.md)
- Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents. → [multimodal](../multimodal/Guideline%202024.md)
- Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training. → [multimodal](../multimodal/Guideline%202024.md)
- Strengthening Multimodal Large Language Model with Bootstrapped Preference Optimization. → [multimodal](../multimodal/Guideline%202024.md)
- MoMA: Multimodal LLM Adapter for Fast Personalized Image Generation. → [multimodal](../multimodal/Guideline%202024.md)
- Instruction Tuning-Free Visual Token Complement for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- AdaShield : Safeguarding Multimodal Large Language Models from Structure-Based Attack via Adaptive Shield Prompting. → [multimodal](../multimodal/Guideline%202024.md)
- A Comprehensive Study of Multimodal Large Language Models for Image Quality Assessment. → [multimodal](../multimodal/Guideline%202024.md)
- LLMGA: Multimodal Large Language Model Based Generation Assistant. → [multimodal](../multimodal/Guideline%202024.md)
- CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios. → [multimodal](../multimodal/Guideline%202024.md)
- Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Merlin: Empowering Multimodal LLMs with Foresight Minds. → [multimodal](../multimodal/Guideline%202024.md)
- FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- LLaVA-Grounding: Grounded Visual Chat with Large Multimodal Models. → [multimodal](../multimodal/Guideline%202024.md)
- GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator. → [multimodal](../multimodal/Guideline%202024.md)
- UniCode: Learning a Unified Codebook for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Mind the Interference: Retaining Pre-trained Knowledge in Parameter Efficient Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion. → [continual-learning](../continual-learning/Guideline%202024.md)
- IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202024.md)
