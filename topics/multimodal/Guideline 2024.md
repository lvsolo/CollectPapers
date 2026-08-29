# Multimodal — 2024 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 69 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web.
- **链接**: [arXiv:2402.17553](https://arxiv.org/abs/2402.17553) · 📚 被引 10
- **作者**: Raghav Kapoor, Yash Parag Butala, Melisa Russak, Jing Yu Koh, Kiran Kamble, Waseem AlShikh et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> For decades, human-computer interaction has fundamentally been manual. Even today, almost all productive work done on the computer necessitates human input at every step. Autonomous virtual agents represent an exciting step in automating many of these menial tasks. Virtual agents would empower users with limited technical proficiency to harness the full possibilities of computer systems. They could also enable the efficient streamlining of numerous computer tasks, ranging from calendar management to complex travel bookings, with minimal human intervention. In this paper, we introduce OmniACT, the first-of-a-kind dataset and benchmark for assessing an agent's capability to generate executable programs to accomplish computer tasks. Our scope extends beyond traditional web automation, covering a diverse range of desktop applications. The dataset consists of fundamental tasks such as "Play the next song", as well as longer horizon tasks such as "Send an email to John Doe mentioning the time and place to meet". Specifically, given a pair of screen image and a visually-grounded natural language task, the goal is to generate a script capable of fully executing the task. We run several strong baseline language model agents on our benchmark. The strongest baseline, GPT-4, performs the best on our benchmark However, its performance level still reaches only 15% of the human proficiency in generating executable scripts capable of completing the task, demonstrating the challenge of our task for conventional web agents. Our benchmark provides a platform to measure and evaluate the progress of language model agents in automating computer tasks and motivates future work towards building multimodal models that bridge large language models and the visual grounding of computer screens.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

</details>

### SyncMask: Synchronized Attentional Masking for Fashion-centric Vision-Language Pretraining.
- **链接**: [arXiv:2404.01156](https://arxiv.org/abs/2404.01156) · 📚 被引 14
- **作者**: Chull Hwan Song, Taebaek Hwang, Jooyoung Yoon, Shunghyun Choi, Yeong Hyeon Gu
- **🏷️ 机构**: Dealicious Inc., Sejong University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have made significant strides in cross-modal understanding through large-scale paired datasets. However, in fashion domain, datasets often exhibit a disparity between the information conveyed in image and text. This issue stems from datasets containing multiple images of a single fashion item all paired with one text, leading to cases where some textual details are not visible in individual images. This mismatch, particularly when non-co-occurring elements are masked, undermines the training of conventional VLM objectives like Masked Language Modeling and Masked Image Modeling, thereby hindering the model's ability to accurately align fine-grained visual and textual features. Addressing this problem, we propose Synchronized attentional Masking (SyncMask), which generate masks that pinpoint the image patches and word tokens where the information co-occur in both image and text. This synchronization is accomplished by harnessing cross-attentional features obtained from a momentum model, ensuring a precise alignment between the two modalities. Additionally, we enhance grouped batch sampling with semi-hard negatives, effectively mitigating false negative issues in Image-Text Matching and Image-Text Contrastive learning objectives within fashion datasets. Our experiments demonstrate the effectiveness of the proposed approach, outperforming existing methods in three downstream tasks.

</details>

### PartDistill: 3D Shape Part Segmentation by Vision-Language Model Distillation.
- **链接**: [arXiv:2312.04016](https://arxiv.org/abs/2312.04016) · 📚 被引 17
- **作者**: Ardian Umam, Cheng-Kun Yang, Min-Hung Chen, Jen-Hui Chuang, Yen-Yu Lin
- **🏷️ 机构**: National Yang Ming Chiao Tung University, MediaTek, NVIDIA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a cross-modal distillation framework, PartDistill, which transfers 2D knowledge from vision-language models (VLMs) to facilitate 3D shape part segmentation. PartDistill addresses three major challenges in this task: the lack of 3D segmentation in invisible or undetected regions in the 2D projections, inconsistent 2D predictions by VLMs, and the lack of knowledge accumulation across different 3D shapes. PartDistill consists of a teacher network that uses a VLM to make 2D predictions and a student network that learns from the 2D predictions while extracting geometrical features from multiple 3D shapes to carry out 3D part segmentation. A bi-directional distillation, including forward and backward distillations, is carried out within the framework, where the former forward distills the 2D predictions to the student network, and the latter improves the quality of the 2D predictions, which subsequently enhances the final 3D segmentation. Moreover, PartDistill can exploit generative models that facilitate effortless 3D shape creation for generating knowledge sources to be distilled. Through extensive experiments, PartDistill boosts the existing methods with substantial margins on widely used ShapeNetPart and PartNetE datasets, by more than 15% and 12% higher mIoU scores, respectively. The code for this work is available at https://github.com/ardianumam/PartDistill.

</details>

### MMA: Multi-Modal Adapter for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02249) · 📚 被引 83
- **作者**: Lingxiao Yang, Ru-Yuan Zhang, Yanchen Wang, Xiaohua Xie
- **🏷️ 机构**: Sun Yat-sen University, Shanghai Jiao Tong University, Stanford University
- **会议**: CVPR 2024

### Source-Free Domain Adaptation with Frozen Multimodal Foundation Model.
- **链接**: [arXiv:2311.16510](https://arxiv.org/abs/2311.16510) · 📚 被引 55
- **作者**: Song Tang, Wenxin Su, Mao Ye, Xiatian Zhu
- **🏷️ 机构**: University of Shanghai for Science and Technology, University of Electronic Science and Technology of China, University of Surrey
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Source-Free Domain Adaptation (SFDA) aims to adapt a source model for a target domain, with only access to unlabeled target training data and the source model pre-trained on a supervised source domain. Relying on pseudo labeling and/or auxiliary supervision, conventional methods are inevitably error-prone. To mitigate this limitation, in this work we for the first time explore the potentials of off-the-shelf vision-language (ViL) multimodal models (e.g.,CLIP) with rich whilst heterogeneous knowledge. We find that directly applying the ViL model to the target domain in a zero-shot fashion is unsatisfactory, as it is not specialized for this particular task but largely generic. To make it task specific, we propose a novel Distilling multimodal Foundation model(DIFO)approach. Specifically, DIFO alternates between two steps during adaptation: (i) Customizing the ViL model by maximizing the mutual information with the target model in a prompt learning manner, (ii) Distilling the knowledge of this customized ViL model to the target model. For more fine-grained and reliable distillation, we further introduce two effective regularization terms, namely most-likely category encouragement and predictive consistency. Extensive experiments show that DIFO significantly outperforms the state-of-the-art alternatives. Code is here

</details>

### Sieve: Multimodal Dataset Pruning Using Image Captioning Models.
- **链接**: [arXiv:2310.02110](https://arxiv.org/abs/2310.02110) · 📚 被引 16
- **作者**: Anas Mahmoud, Mostafa Elhoushi, Amro Abbas, Yu Yang, Newsha Ardalani, Hugh Leather et al.
- **🏷️ 机构**: FAIR at Meta, UC Los Angeles, DatologyAI
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) are pretrained on large, diverse, and noisy web-crawled datasets. This underscores the critical need for dataset pruning, as the quality of these datasets is strongly correlated with the performance of VLMs on downstream tasks. Using CLIPScore from a pretrained model to only train models using highly-aligned samples is one of the most successful methods for pruning. We argue that this approach suffers from multiple limitations including: false positives and negatives due to CLIP's pretraining on noisy labels. We propose a pruning signal, Sieve, that employs synthetic captions generated by image-captioning models pretrained on small, diverse, and well-aligned image-text pairs to evaluate the alignment of noisy image-text pairs. To bridge the gap between the limited diversity of generated captions and the high diversity of alternative text (alt-text), we estimate the semantic textual similarity in the embedding space of a language model pretrained on unlabeled text corpus. Using DataComp, a multimodal dataset filtering benchmark, when evaluating on 38 downstream tasks, our pruning approach, surpasses CLIPScore by 2.6\% and 1.7\% on medium and large scale respectively. In addition, on retrieval tasks, Sieve leads to a significant improvement of 2.7% and 4.5% on medium and large scale respectively.

</details>

### MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding.
- **链接**: [arXiv:2404.05726](https://arxiv.org/abs/2404.05726) · 📚 被引 98
- **作者**: Bo He, Hengduo Li, Young Kyun Jang, Menglin Jia, Xuefei Cao, Ashish Shah et al.
- **🏷️ 机构**: University of Maryland, Meta, University of Central Florida
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the success of large language models (LLMs), integrating the vision model into LLMs to build vision-language foundation models has gained much more interest recently. However, existing LLM-based large multimodal models (e.g., Video-LLaMA, VideoChat) can only take in a limited number of frames for short video understanding. In this study, we mainly focus on designing an efficient and effective model for long-term video understanding. Instead of trying to process more frames simultaneously like most existing work, we propose to process videos in an online manner and store past video information in a memory bank. This allows our model to reference historical video content for long-term analysis without exceeding LLMs' context length constraints or GPU memory limits. Our memory bank can be seamlessly integrated into current multimodal LLMs in an off-the-shelf manner. We conduct extensive experiments on various video understanding tasks, such as long-video understanding, video question answering, and video captioning, and our model can achieve state-of-the-art performances across multiple datasets. Code available at https://boheumd.github.io/MA-LMM/.

</details>

### Multimodal Representation Learning by Alternating Unimodal Adaptation.
- **链接**: [arXiv:2311.10707](https://arxiv.org/abs/2311.10707) · 📚 被引 56
- **作者**: Xiaohui Zhang, Jaehong Yoon, Mohit Bansal, Huaxiu Yao
- **🏷️ 机构**: UNC-Chapel Hill
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning, which integrates data from diverse sensory modes, plays a pivotal role in artificial intelligence. However, existing multimodal learning methods often struggle with challenges where some modalities appear more dominant than others during multimodal learning, resulting in suboptimal performance. To address this challenge, we propose MLA (Multimodal Learning with Alternating Unimodal Adaptation). MLA reframes the conventional joint multimodal learning process by transforming it into an alternating unimodal learning process, thereby minimizing interference between modalities. Simultaneously, it captures cross-modal interactions through a shared head, which undergoes continuous optimization across different modalities. This optimization process is controlled by a gradient modification mechanism to prevent the shared head from losing previously acquired information. During the inference phase, MLA utilizes a test-time uncertainty-based model fusion mechanism to integrate multimodal information. Extensive experiments are conducted on five diverse datasets, encompassing scenarios with complete modalities and scenarios with missing modalities. These experiments demonstrate the superiority of MLA over competing prior approaches. Our code is available at https://github.com/Cecile-hi/Multimodal-Learning-with-Alternating-Unimodal-Adaptation.

</details>

### ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation.
- **链接**: [arXiv:2312.16217](https://arxiv.org/abs/2312.16217) · 📚 被引 81
- **作者**: Xiaoqi Li, Mingxu Zhang, Yiran Geng, Haoran Geng, Yuxing Long, Yan Shen et al.
- **🏷️ 机构**: School of Computer Science, Peking University, Beijing University of Posts and Telecommunications, CUHK,MMLab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robot manipulation relies on accurately predicting contact points and end-effector directions to ensure successful operation. However, learning-based robot manipulation, trained on a limited category within a simulator, often struggles to achieve generalizability, especially when confronted with extensive categories. Therefore, we introduce an innovative approach for robot manipulation that leverages the robust reasoning capabilities of Multimodal Large Language Models (MLLMs) to enhance the stability and generalization of manipulation. By fine-tuning the injected adapters, we preserve the inherent common sense and reasoning ability of the MLLMs while equipping them with the ability for manipulation. The fundamental insight lies in the introduced fine-tuning paradigm, encompassing object category understanding, affordance prior reasoning, and object-centric pose prediction to stimulate the reasoning ability of MLLM in manipulation. During inference, our approach utilizes an RGB image and text prompt to predict the end effector's pose in chain of thoughts. After the initial contact is established, an active impedance adaptation policy is introduced to plan the upcoming waypoints in a closed-loop manner. Moreover, in real world, we design a test-time adaptation (TTA) strategy for manipulation to enable the model better adapt to the current real-world scene configuration. Experiments in simulator and real-world show the promising performance of ManipLLM. More details and demonstrations can be found at https://sites.google.com/view/manipllm.

</details>

### Multimodal Prompt Perceiver: Empower Adaptiveness, Generalizability and Fidelity for All-in-One Image Restoration.
- **链接**: [arXiv:2312.02918](https://arxiv.org/abs/2312.02918) · 📚 被引 73
- **作者**: Yuang Ai, Huaibo Huang, Xiaoqiang Zhou, Jiexiang Wang, Ran He
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,MAIS &#x0026; CRIPAC,Beijing,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite substantial progress, all-in-one image restoration (IR) grapples with persistent challenges in handling intricate real-world degradations. This paper introduces MPerceiver: a novel multimodal prompt learning approach that harnesses Stable Diffusion (SD) priors to enhance adaptiveness, generalizability and fidelity for all-in-one image restoration. Specifically, we develop a dual-branch module to master two types of SD prompts: textual for holistic representation and visual for multiscale detail representation. Both prompts are dynamically adjusted by degradation predictions from the CLIP image encoder, enabling adaptive responses to diverse unknown degradations. Moreover, a plug-in detail refinement module improves restoration fidelity via direct encoder-to-decoder information transformation. To assess our method, MPerceiver is trained on 9 tasks for all-in-one IR and outperforms state-of-the-art task-specific methods across most tasks. Post multitask pre-training, MPerceiver attains a generalized representation in low-level vision, exhibiting remarkable zero-shot and few-shot capabilities in unseen tasks. Extensive experiments on 16 IR tasks underscore the superiority of MPerceiver in terms of adaptiveness, generalizability and fidelity.

</details>

### Can Language Beat Numerical Regression? Language-Based Multimodal Trajectory Prediction.
- **链接**: [arXiv:2403.18447](https://arxiv.org/abs/2403.18447) · 📚 被引 49
- **作者**: Inhwan Bae, Junoh Lee, Hae-Gon Jeon
- **🏷️ 机构**: AI Graduate School, School of Electrical Engineering and Computer Science Gwangju Institute of Science and Technology,Gwangju,South Korea
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Language models have demonstrated impressive ability in context understanding and generative performance. Inspired by the recent success of language foundation models, in this paper, we propose LMTraj (Language-based Multimodal Trajectory predictor), which recasts the trajectory prediction task into a sort of question-answering problem. Departing from traditional numerical regression models, which treat the trajectory coordinate sequence as continuous signals, we consider them as discrete signals like text prompts. Specially, we first transform an input space for the trajectory coordinate into the natural language space. Here, the entire time-series trajectories of pedestrians are converted into a text prompt, and scene images are described as text information through image captioning. The transformed numerical and image data are then wrapped into the question-answering template for use in a language model. Next, to guide the language model in understanding and reasoning high-level knowledge, such as scene context and social relationships between pedestrians, we introduce an auxiliary multi-task question and answering. We then train a numerical tokenizer with the prompt data. We encourage the tokenizer to separate the integer and decimal parts well, and leverage it to capture correlations between the consecutive numbers in the language model. Lastly, we train the language model using the numerical tokenizer and all of the question-answer prompts. Here, we propose a beam-search-based most-likely prediction and a temperature-based multimodal prediction to implement both deterministic and stochastic inferences. Applying our LMTraj, we show that the language-based model can be a powerful pedestrian trajectory predictor, and outperforms existing numerical-based predictor methods. Code is publicly available at https://github.com/inhwanbae/LMTrajectory .

</details>

### ViP-LLaVA: Making Large Multimodal Models Understand Arbitrary Visual Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01227) · 📚 被引 82
- **作者**: Mu Cai, Haotian Liu, Siva Karthik Mustikovela, Gregory P. Meyer, Yuning Chai, Dennis Park et al.
- **🏷️ 机构**: University of Wisconsin-Madison, Cruise LLC
- **会议**: CVPR 2024

### Honeybee: Locality-Enhanced Projector for Multimodal LLM.
- **链接**: [arXiv:2312.06742](https://arxiv.org/abs/2312.06742) · 📚 被引 84
- **作者**: Junbum Cha, Wooyoung Kang, Jonghwan Mun, Byungseok Roh
- **🏷️ 机构**: Kakao Brain
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Multimodal Large Language Models (MLLMs), a visual projector plays a crucial role in bridging pre-trained vision encoders with LLMs, enabling profound visual understanding while harnessing the LLMs' robust capabilities. Despite the importance of the visual projector, it has been relatively less explored. In this study, we first identify two essential projector properties: (i) flexibility in managing the number of visual tokens, crucial for MLLMs' overall efficiency, and (ii) preservation of local context from visual features, vital for spatial understanding. Based on these findings, we propose a novel projector design that is both flexible and locality-enhanced, effectively satisfying the two desirable properties. Additionally, we present comprehensive strategies to effectively utilize multiple and multifaceted instruction datasets. Through extensive experiments, we examine the impact of individual design choices. Finally, our proposed MLLM, Honeybee, remarkably outperforms previous state-of-the-art methods across various benchmarks, including MME, MMBench, SEED-Bench, and LLaVA-Bench, achieving significantly higher efficiency. Code and models are available at https://github.com/kakaobrain/honeybee.

</details>

### LION : Empowering Multimodal Large Language Model with Dual-Level Visual Knowledge.
- **链接**: [arXiv:2311.11860](https://arxiv.org/abs/2311.11860) · 📚 被引 45
- **作者**: Gongwei Chen, Leyang Shen, Rui Shao, Xiang Deng, Liqiang Nie
- **🏷️ 机构**: School of Computer Science and Technology, Harbin Institute of Technology,Shenzhen
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have endowed LLMs with the ability to perceive and understand multi-modal signals. However, most of the existing MLLMs mainly adopt vision encoders pretrained on coarsely aligned image-text pairs, leading to insufficient extraction and reasoning of visual knowledge. To address this issue, we devise a dual-Level vIsual knOwledge eNhanced Multimodal Large Language Model (LION), which empowers the MLLM by injecting visual knowledge in two levels. 1) Progressive incorporation of fine-grained spatial-aware visual knowledge. We design a vision aggregator cooperated with region-level vision-language (VL) tasks to incorporate fine-grained spatial-aware visual knowledge into the MLLM. To alleviate the conflict between image-level and region-level VL tasks during incorporation, we devise a dedicated stage-wise instruction-tuning strategy with mixture-of-adapters. This progressive incorporation scheme contributes to the mutual promotion between these two kinds of VL tasks. 2) Soft prompting of high-level semantic visual evidence. We facilitate the MLLM with high-level semantic visual evidence by leveraging diverse image tags. To mitigate the potential influence caused by imperfect predicted tags, we propose a soft prompting method by embedding a learnable token into the tailored text instruction. Comprehensive experiments on several multi-modal benchmarks demonstrate the superiority of our model (e.g., improvement of 5% accuracy on VSR and 3% CIDEr on TextCaps over InstructBLIP, 5% accuracy on RefCOCOg over Kosmos-2).

</details>

### Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping.
- **链接**: [arXiv:2312.04521](https://arxiv.org/abs/2312.04521) · 📚 被引 73
- **作者**: Alex Costanzino, Pierluigi Zama Ramirez, Giuseppe Lisanti, Luigi Di Stefano
- **🏷️ 机构**: University of Bologna,CVLAB,Department of Computer Science and Engineering (DISI),Italy
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The paper explores the industrial multimodal Anomaly Detection (AD) task, which exploits point clouds and RGB images to localize anomalies. We introduce a novel light and fast framework that learns to map features from one modality to the other on nominal samples. At test time, anomalies are detected by pinpointing inconsistencies between observed and mapped features. Extensive experiments show that our approach achieves state-of-the-art detection and segmentation performance in both the standard and few-shot settings on the MVTec 3D-AD dataset while achieving faster inference and occupying less memory than previous multimodal AD methods. Moreover, we propose a layer-pruning technique to improve memory and time efficiency with a marginal sacrifice in performance.

</details>

### On the Robustness of Large Multimodal Models Against Image Adversarial Attacks.
- **链接**: [arXiv:2312.03777](https://arxiv.org/abs/2312.03777) · 📚 被引 51
- **作者**: Xuanming Cui, Alejandro Aparcedo, Young Kyun Jang, Ser-Nam Lim
- **🏷️ 机构**: University of Central Florida
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in instruction tuning have led to the development of State-of-the-Art Large Multimodal Models (LMMs). Given the novelty of these models, the impact of visual adversarial attacks on LMMs has not been thoroughly examined. We conduct a comprehensive study of the robustness of various LMMs against different adversarial attacks, evaluated across tasks including image classification, image captioning, and Visual Question Answer (VQA). We find that in general LMMs are not robust to visual adversarial inputs. However, our findings suggest that context provided to the model via prompts, such as questions in a QA pair helps to mitigate the effects of visual adversarial inputs. Notably, the LMMs evaluated demonstrated remarkable resilience to such attacks on the ScienceQA task with only an 8.10% drop in performance compared to their visual counterparts which dropped 99.73%. We also propose a new approach to real-world image classification which we term query decomposition. By incorporating existence queries into our input prompt we observe diminished attack effectiveness and improvements in image classification accuracy. This research highlights a previously under-explored facet of LMM robustness and sets the stage for future work aimed at strengthening the resilience of multimodal systems in adversarial environments.

</details>

### Question Aware Vision Transformer for Multimodal Reasoning.
- **链接**: [arXiv:2402.05472](https://arxiv.org/abs/2402.05472) · 📚 被引 23
- **作者**: Roy Ganz, Yair Kittenplon, Aviad Aberdam, Elad Ben-Avraham, Oren Nuriel, Shai Mazor et al.
- **🏷️ 机构**: Technion,Israel, AWS AI Labs
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language (VL) models have gained significant research focus, enabling remarkable advances in multimodal reasoning. These architectures typically comprise a vision encoder, a Large Language Model (LLM), and a projection module that aligns visual features with the LLM's representation space. Despite their success, a critical limitation persists: the vision encoding process remains decoupled from user queries, often in the form of image-related questions. Consequently, the resulting visual features may not be optimally attuned to the query-specific elements of the image. To address this, we introduce QA-ViT, a Question Aware Vision Transformer approach for multimodal reasoning, which embeds question awareness directly within the vision encoder. This integration results in dynamic visual features focusing on relevant image aspects to the posed question. QA-ViT is model-agnostic and can be incorporated efficiently into any VL architecture. Extensive experiments demonstrate the effectiveness of applying our method to various multimodal architectures, leading to consistent improvement across diverse tasks and showcasing its potential for enhancing visual and scene-text understanding.

</details>

### Embracing Unimodal Aleatoric Uncertainty for Robust Multimodal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02538) · 📚 被引 52
- **作者**: Zixian Gao, Xun Jiang, Xing Xu, Fumin Shen, Yujie Li, Heng Tao Shen
- **🏷️ 机构**: Center for Future Media &#x0026; School of Computer Science and Engineering, University of Electronic Science and Technology of China,China, Kyushu Institute of Technology,Japan
- **会议**: CVPR 2024

### PAIR Diffusion: A Comprehensive Multimodal Object-Level Image Editor.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00822) · 📚 被引 13
- **作者**: Vidit Goel, Elia Peruzzo, Yifan Jiang, Dejia Xu, Xingqian Xu, Nicu Sebe et al.
- **🏷️ 机构**: Picsart AI Research (PAIR), University of Trento, UT Austin
- **会议**: CVPR 2024

### SmartEdit: Exploring Complex Instruction-Based Image Editing with Multimodal Large Language Models.
- **链接**: [arXiv:2312.06739](https://arxiv.org/abs/2312.06739) · 📚 被引 83
- **作者**: Yuzhou Huang, Liangbin Xie, Xintao Wang, Ziyang Yuan, Xiaodong Cun, Yixiao Ge et al.
- **🏷️ 机构**: The Chinese University of Hong Kong,Shenzhen,CUHK-SZ, ARC Lab, Tencent PCG, Tencent AI Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current instruction-based editing methods, such as InstructPix2Pix, often fail to produce satisfactory results in complex scenarios due to their dependence on the simple CLIP text encoder in diffusion models. To rectify this, this paper introduces SmartEdit, a novel approach to instruction-based image editing that leverages Multimodal Large Language Models (MLLMs) to enhance their understanding and reasoning capabilities. However, direct integration of these elements still faces challenges in situations requiring complex reasoning. To mitigate this, we propose a Bidirectional Interaction Module that enables comprehensive bidirectional information interactions between the input image and the MLLM output. During training, we initially incorporate perception data to boost the perception and understanding capabilities of diffusion models. Subsequently, we demonstrate that a small amount of complex instruction editing data can effectively stimulate SmartEdit's editing capabilities for more complex instructions. We further construct a new evaluation dataset, Reason-Edit, specifically tailored for complex instruction-based image editing. Both quantitative and qualitative results on this evaluation dataset indicate that our SmartEdit surpasses previous methods, paving the way for the practical application of complex instruction-based image editing.

</details>

### Modeling Dense Multimodal Interactions Between Biological Pathways and Histology for Survival Prediction.
- **链接**: [arXiv:2304.06819](https://arxiv.org/abs/2304.06819) · 📚 被引 130
- **作者**: Guillaume Jaume, Anurag Vaidya, Richard J. Chen, Drew F. K. Williamson, Paul Pu Liang, Faisal Mahmood
- **🏷️ 机构**: Mass General Brigham, CMU
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integrating whole-slide images (WSIs) and bulk transcriptomics for predicting patient survival can improve our understanding of patient prognosis. However, this multimodal task is particularly challenging due to the different nature of these data: WSIs represent a very high-dimensional spatial description of a tumor, while bulk transcriptomics represent a global description of gene expression levels within that tumor. In this context, our work aims to address two key challenges: (1) how can we tokenize transcriptomics in a semantically meaningful and interpretable way?, and (2) how can we capture dense multimodal interactions between these two modalities? Specifically, we propose to learn biological pathway tokens from transcriptomics that can encode specific cellular functions. Together with histology patch tokens that encode the different morphological patterns in the WSI, we argue that they form appropriate reasoning units for downstream interpretability analyses. We propose fusing both modalities using a memory-efficient multimodal Transformer that can model interactions between pathway and histology patch tokens. Our proposed model, SURVPATH, achieves state-of-the-art performance when evaluated against both unimodal and multimodal baselines on five datasets from The Cancer Genome Atlas. Our interpretability framework identifies key multimodal prognostic factors, and, as such, can provide valuable insights into the interaction between genotype and phenotype, enabling a deeper understanding of the underlying biological mechanisms at play. We make our code public at: https://github.com/ajv012/SurvPath.

</details>

### DIEM: Decomposition-Integration Enhancing Multimodal Insights.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02578) · 📚 被引 1
- **作者**: Xinyi Jiang, Guoming Wang, Junhao Guo, Juncheng Li, Wenqiao Zhang, Rongxing Lu et al.
- **🏷️ 机构**: Zhejiang University, University of New Brunswick
- **会议**: CVPR 2024

### Hallucination Augmented Contrastive Learning for Multimodal Large Language Model.
- **链接**: [arXiv:2312.06968](https://arxiv.org/abs/2312.06968) · 📚 被引 91
- **作者**: Chaoya Jiang, Haiyang Xu, Mengfan Dong, Jiaxing Chen, Wei Ye, Ming Yan et al.
- **🏷️ 机构**: National Engineering Research Center for Software Engineering, Peking University, Alibaba Group
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal large language models (MLLMs) have been shown to efficiently integrate natural language with visual information to handle multi-modal tasks. However, MLLMs still face a fundamental limitation of hallucinations, where they tend to generate erroneous or fabricated information. In this paper, we address hallucinations in MLLMs from a novel perspective of representation learning. We first analyzed the representation distribution of textual and visual tokens in MLLM, revealing two important findings: 1) there is a significant gap between textual and visual representations, indicating unsatisfactory cross-modal representation alignment; 2) representations of texts that contain and do not contain hallucinations are entangled, making it challenging to distinguish them. These two observations inspire us with a simple yet effective method to mitigate hallucinations. Specifically, we introduce contrastive learning into MLLMs and use text with hallucination as hard negative examples, naturally bringing representations of non-hallucinative text and visual samples closer while pushing way representations of non-hallucinating and hallucinative text. We evaluate our method quantitatively and qualitatively, showing its effectiveness in reducing hallucination occurrences and improving performance across multiple benchmarks. On the MMhal-Bench benchmark, our method obtains a 34.66% /29.5% improvement over the baseline MiniGPT-4/LLaVA. Our code is available on https://github.com/X-PLUG/mPLUG-HalOwl/tree/main/hacl.

</details>

### MV-Adapter: Multimodal Video Transfer Learning for Video Text Retrieval.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02563) · 📚 被引 26
- **作者**: Xiaojie Jin, Bowen Zhang, Weibo Gong, Kai Xu, Xueqing Deng, Peng Wang et al.
- **🏷️ 机构**: Bytedance Inc., Hefei University of Technology
- **会议**: CVPR 2024

### Modeling Multimodal Social Interactions: New Challenges and Baselines with Densely Aligned Representations.
- **链接**: [arXiv:2403.02090](https://arxiv.org/abs/2403.02090) · 📚 被引 8
- **作者**: Sangmin Lee, Bolin Lai, Fiona Ryan, Bikram Boote, James M. Rehg
- **🏷️ 机构**: University of Illinois Urbana-Champaign, Georgia Institute of Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding social interactions involving both verbal and non-verbal cues is essential for effectively interpreting social situations. However, most prior works on multimodal social cues focus predominantly on single-person behaviors or rely on holistic visual representations that are not aligned to utterances in multi-party environments. Consequently, they are limited in modeling the intricate dynamics of multi-party interactions. In this paper, we introduce three new challenging tasks to model the fine-grained dynamics between multiple people: speaking target identification, pronoun coreference resolution, and mentioned player prediction. We contribute extensive data annotations to curate these new challenges in social deduction game settings. Furthermore, we propose a novel multimodal baseline that leverages densely aligned language-visual representations by synchronizing visual features with their corresponding utterances. This facilitates concurrently capturing verbal and non-verbal cues pertinent to social reasoning. Experiments demonstrate the effectiveness of the proposed approach with densely aligned multimodal representations in modeling fine-grained social interactions. Project website: https://sangmin-git.github.io/projects/MMSI.

</details>

### HHMR: Holistic Hand Mesh Recovery by Enhancing the Multimodal Controllability of Graph Diffusion Models.
- **链接**: [arXiv:2406.01334](https://arxiv.org/abs/2406.01334) · 📚 被引 12
- **作者**: Mengcheng Li, Hongwen Zhang, Yuxiang Zhang, Ruizhi Shao, Tao Yu, Yebin Liu
- **🏷️ 机构**: Tsinghua University,Department of Automation, School of Artificial Intelligence, Beijing Normal University, Beijing National Research Center for Information Science and Technology, Tsinghua University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a trend of the deep integration of the generation and reconstruction paradigms. In this paper, we extend the ability of controllable generative models for a more comprehensive hand mesh recovery task: direct hand mesh generation, inpainting, reconstruction, and fitting in a single framework, which we name as Holistic Hand Mesh Recovery (HHMR). Our key observation is that different kinds of hand mesh recovery tasks can be achieved by a single generative model with strong multimodal controllability, and in such a framework, realizing different tasks only requires giving different signals as conditions. To achieve this goal, we propose an all-in-one diffusion framework based on graph convolution and attention mechanisms for holistic hand mesh recovery. In order to achieve strong control generation capability while ensuring the decoupling of multimodal control signals, we map different modalities to a shared feature space and apply cross-scale random masking in both modality and feature levels. In this way, the correlation between different modalities can be fully exploited during the learning of hand priors. Furthermore, we propose Condition-aligned Gradient Guidance to enhance the alignment of the generated model with the control signals, which significantly improves the accuracy of the hand mesh reconstruction and fitting. Experiments show that our novel framework can realize multiple hand mesh recovery tasks simultaneously and outperform the existing methods in different tasks, which provides more possibilities for subsequent downstream applications including gesture recognition, pose generation, mesh editing, and so on.

</details>

### SEED-Bench: Benchmarking Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01263) · 📚 被引 174
- **作者**: Bohao Li, Yuying Ge, Yixiao Ge, Guangzhi Wang, Rui Wang, Ruimao Zhang et al.
- **🏷️ 机构**: School of Data Science, The Chinese University of HongKong,Shenzhen, Tencent AI Lab, ARC Lab, Tencent PCG
- **会议**: CVPR 2024

### All in One Framework for Multimodal Re-Identification in the Wild.
- **链接**: [arXiv:2405.04741](https://arxiv.org/abs/2405.04741) · 📚 被引 28
- **作者**: He Li, Mang Ye, Ming Zhang, Bo Du
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Wuhan University,National Engineering Research Center for Multimedia Software, Hubei Luojia Laboratory,Wuhan,China, Guangzhou Urban Planning Design Survey Research Institute,Guangzhou,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Re-identification (ReID), recent advancements yield noteworthy progress in both unimodal and cross-modal retrieval tasks. However, the challenge persists in developing a unified framework that could effectively handle varying multimodal data, including RGB, infrared, sketches, and textual information. Additionally, the emergence of large-scale models shows promising performance in various vision tasks but the foundation model in ReID is still blank. In response to these challenges, a novel multimodal learning paradigm for ReID is introduced, referred to as All-in-One (AIO), which harnesses a frozen pre-trained big model as an encoder, enabling effective multimodal retrieval without additional fine-tuning. The diverse multimodal data in AIO are seamlessly tokenized into a unified space, allowing the modality-shared frozen encoder to extract identity-consistent features comprehensively across all modalities. Furthermore, a meticulously crafted ensemble of cross-modality heads is designed to guide the learning trajectory. AIO is the \textbf{first} framework to perform all-in-one ReID, encompassing four commonly used modalities. Experiments on cross-modal and multimodal ReID reveal that AIO not only adeptly handles various modal data but also excels in challenging contexts, showcasing exceptional performance in zero-shot and domain generalization scenarios.

</details>

### Correlation-Decoupled Knowledge Distillation for Multimodal Sentiment Analysis with Incomplete Modalities.
- **链接**: [arXiv:2404.16456](https://arxiv.org/abs/2404.16456) · 📚 被引 57
- **作者**: Mingcheng Li, Dingkang Yang, Xiao Zhao, Shuaibing Wang, Yan Wang, Kun Yang et al.
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal sentiment analysis (MSA) aims to understand human sentiment through multimodal data. Most MSA efforts are based on the assumption of modality completeness. However, in real-world applications, some practical factors cause uncertain modality missingness, which drastically degrades the model's performance. To this end, we propose a Correlation-decoupled Knowledge Distillation (CorrKD) framework for the MSA task under uncertain missing modalities. Specifically, we present a sample-level contrastive distillation mechanism that transfers comprehensive knowledge containing cross-sample correlations to reconstruct missing semantics. Moreover, a category-guided prototype distillation mechanism is introduced to capture cross-category correlations using category prototypes to align feature distributions and generate favorable joint representations. Eventually, we design a response-disentangled consistency distillation strategy to optimize the sentiment decision boundaries of the student network through response disentanglement and mutual information maximization. Comprehensive experiments on three datasets indicate that our framework can achieve favorable improvements compared with several baselines.

</details>

### Querying as Prompt: Parameter-Efficient Learning for Multimodal Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02536) · 📚 被引 5
- **作者**: Tian Liang, Jing Huang, Ming Kong, Luyuan Chen, Qiang Zhu
- **🏷️ 机构**: Zhejiang University, Beijing Information Science and Technology University
- **会议**: CVPR 2024

### BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02327) · 📚 被引 33
- **作者**: Siyuan Liang, Mingli Zhu, Aishan Liu, Baoyuan Wu, Xiaochun Cao, Ee-Chien Chang
- **🏷️ 机构**: National University of Singapore, The Chinese University of Hong Kong,Shenzhen, Beihang University
- **会议**: CVPR 2024

### Multimodal Sense-Informed Forecasting of 3D Human Motions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00209) · 📚 被引 11
- **作者**: Zhenyu Lou, Qiongjie Cui, Haofan Wang, Xu Tang, Hong Zhou
- **🏷️ 机构**: Zhejiang University, Nanjing University of Science and Technology, Xiaohongshu Inc
- **会议**: CVPR 2024

### Compositional Chain-of-Thought Prompting for Large Multimodal Models.
- **链接**: [arXiv:2311.17076](https://arxiv.org/abs/2311.17076) · 📚 被引 96
- **作者**: Chancharik Mitra, Brandon Huang, Trevor Darrell, Roei Herzig
- **🏷️ 机构**: University of California,Berkeley
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The combination of strong visual backbones and Large Language Model (LLM) reasoning has led to Large Multimodal Models (LMMs) becoming the current standard for a wide range of vision and language (VL) tasks. However, recent research has shown that even the most advanced LMMs still struggle to capture aspects of compositional visual reasoning, such as attributes and relationships between objects. One solution is to utilize scene graphs (SGs)--a formalization of objects and their relations and attributes that has been extensively used as a bridge between the visual and textual domains. Yet, scene graph data requires scene graph annotations, which are expensive to collect and thus not easily scalable. Moreover, finetuning an LMM based on SG data can lead to catastrophic forgetting of the pretraining objective. To overcome this, inspired by chain-of-thought methods, we propose Compositional Chain-of-Thought (CCoT), a novel zero-shot Chain-of-Thought prompting method that utilizes SG representations in order to extract compositional knowledge from an LMM. Specifically, we first generate an SG using the LMM, and then use that SG in the prompt to produce a response. Through extensive experiments, we find that the proposed CCoT approach not only improves LMM performance on several vision and language VL compositional benchmarks but also improves the performance of several popular LMMs on general multimodal benchmarks, without the need for fine-tuning or annotated ground-truth SGs. Code: https://github.com/chancharikmitra/CCoT

</details>

### Generate Subgoal Images Before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01327) · 📚 被引 9
- **作者**: Fei Ni, Jianye Hao, Shiguang Wu, Longxin Kou, Jiashun Liu, Yan Zheng et al.
- **🏷️ 机构**: Tianjin University,China, Huawei Noah&#x0027;s Ark Lab,China
- **会议**: CVPR 2024

### Summarize the Past to Predict the Future: Natural Language Descriptions of Context Boost Multimodal Object Interaction Anticipation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01731) · 📚 被引 15
- **作者**: Razvan-George Pasca, Alexey Gavryushin, Muhammad Hamza, Yen-Ling Kuo, Kaichun Mo, Luc Van Gool et al.
- **🏷️ 机构**: ETH Zurich, Univ. of Zurich, Univ. of Virginia
- **会议**: CVPR 2024

### Mirasol3B: A Multimodal Autoregressive Model for Time-Aligned and Contextual Modalities.
- **链接**: [arXiv:2311.05698](https://arxiv.org/abs/2311.05698) · 📚 被引 16
- **作者**: A. J. Piergiovanni, Isaac Noble, Dahun Kim, Michael S. Ryoo, Victor Gomes, Anelia Angelova
- **🏷️ 机构**: Google DeepMind, Google Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One of the main challenges of multimodal learning is the need to combine heterogeneous modalities (e.g., video, audio, text). For example, video and audio are obtained at much higher rates than text and are roughly aligned in time. They are often not synchronized with text, which comes as a global context, e.g., a title, or a description. Furthermore, video and audio inputs are of much larger volumes, and grow as the video length increases, which naturally requires more compute dedicated to these modalities and makes modeling of long-range dependencies harder. We here decouple the multimodal modeling, dividing it into separate, focused autoregressive models, processing the inputs according to the characteristics of the modalities. We propose a multimodal model, called Mirasol3B, consisting of an autoregressive component for the time-synchronized modalities (audio and video), and an autoregressive component for the context modalities which are not necessarily aligned in time but are still sequential. To address the long-sequences of the video-audio inputs, we propose to further partition the video and audio sequences in consecutive snippets and autoregressively process their representations. To that end, we propose a Combiner mechanism, which models the audio-video information jointly within a timeframe. The Combiner learns to extract audio and video features from raw spatio-temporal signals, and then learns to fuse these features producing compact but expressive representations per snippet. Our approach achieves the state-of-the-art on well established multimodal benchmarks, outperforming much larger models. It effectively addresses the high computational demand of media inputs by both learning compact representations, controlling the sequence length of the audio-video feature representations, and modeling their dependencies in time.

</details>

### Sniffer: Multimodal Large Language Model for Explainable Out-of-Context Misinformation Detection.
- **链接**: [arXiv:2403.03170](https://arxiv.org/abs/2403.03170) · 📚 被引 80
- **作者**: Peng Qi, Zehong Yan, Wynne Hsu, Mong-Li Lee
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Misinformation is a prevalent societal issue due to its potential high risks. Out-of-context (OOC) misinformation, where authentic images are repurposed with false text, is one of the easiest and most effective ways to mislead audiences. Current methods focus on assessing image-text consistency but lack convincing explanations for their judgments, which is essential for debunking misinformation. While Multimodal Large Language Models (MLLMs) have rich knowledge and innate capability for visual reasoning and explanation generation, they still lack sophistication in understanding and discovering the subtle crossmodal differences. In this paper, we introduce SNIFFER, a novel multimodal large language model specifically engineered for OOC misinformation detection and explanation. SNIFFER employs two-stage instruction tuning on InstructBLIP. The first stage refines the model's concept alignment of generic objects with news-domain entities and the second stage leverages language-only GPT-4 generated OOC-specific instruction data to fine-tune the model's discriminatory powers. Enhanced by external tools and retrieval, SNIFFER not only detects inconsistencies between text and image but also utilizes external knowledge for contextual verification. Our experiments show that SNIFFER surpasses the original MLLM by over 40% and outperforms state-of-the-art methods in detection accuracy. SNIFFER also provides accurate and persuasive explanations as validated by quantitative and human evaluations.

</details>

### MMSum: A Dataset for Multimodal Summarization and Thumbnail Generation of Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02069) · 📚 被引 9
- **作者**: Jielin Qiu, Jiacheng Zhu, William Han, Aditesh Kumar, Karthik Mittal, Claire Jin et al.
- **🏷️ 机构**: Carnegie Mellon University, MIT CSAIL, Microsoft Azure AI
- **会议**: CVPR 2024

### GLaMM: Pixel Grounding Large Multimodal Model.
- **链接**: [arXiv:2311.03356](https://arxiv.org/abs/2311.03356) · 📚 被引 203
- **作者**: Hanoona Abdul Rasheed, Muhammad Maaz, Sahal Shaji Mullappilly, Abdelrahman M. Shaker, Salman H. Khan, Hisham Cholakkal et al.
- **🏷️ 机构**: Mohamed bin Zayed University of AI
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) extend Large Language Models to the vision domain. Initial LMMs used holistic images and text prompts to generate ungrounded textual responses. Recently, region-level LMMs have been used to generate visually grounded responses. However, they are limited to only referring to a single object category at a time, require users to specify the regions, or cannot offer dense pixel-wise object grounding. In this work, we present Grounding LMM (GLaMM), the first model that can generate natural language responses seamlessly intertwined with corresponding object segmentation masks. GLaMM not only grounds objects appearing in the conversations but is flexible enough to accept both textual and optional visual prompts (region of interest) as input. This empowers users to interact with the model at various levels of granularity, both in textual and visual domains. Due to the lack of standard benchmarks for the novel setting of visually Grounded Conversation Generation (GCG), we introduce a comprehensive evaluation protocol with our curated grounded conversations. Our proposed GCG task requires densely grounded concepts in natural scenes at a large-scale. To this end, we propose a densely annotated Grounding-anything Dataset (GranD) using our proposed automated annotation pipeline that encompasses 7.5M unique concepts grounded in a total of 810M regions available with segmentation masks. Besides GCG, GLaMM also performs effectively on several downstream tasks, e.g., referring expression segmentation, image and region-level captioning and vision-language conversations.

</details>

### PixelLM: Pixel Reasoning with Large Multimodal Model.
- **链接**: [arXiv:2312.02228](https://arxiv.org/abs/2312.02228) · 📚 被引 81
- **作者**: Zhongwei Ren, Zhicheng Huang, Yunchao Wei, Yao Zhao, Dongmei Fu, Jiashi Feng et al.
- **🏷️ 机构**: Beijing Jiaotong University, University of Science and Technology Beijing, ByteDance Inc.
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While large multimodal models (LMMs) have achieved remarkable progress, generating pixel-level masks for image reasoning tasks involving multiple open-world targets remains a challenge. To bridge this gap, we introduce PixelLM, an effective and efficient LMM for pixel-level reasoning and understanding. Central to PixelLM is a novel, lightweight pixel decoder and a comprehensive segmentation codebook. The decoder efficiently produces masks from the hidden embeddings of the codebook tokens, which encode detailed target-relevant information. With this design, PixelLM harmonizes with the structure of popular LMMs and avoids the need for additional costly segmentation models. Furthermore, we propose a target refinement loss to enhance the model's ability to differentiate between multiple targets, leading to substantially improved mask quality. To advance research in this area, we construct MUSE, a high-quality multi-target reasoning segmentation benchmark. PixelLM excels across various pixel-level image reasoning and understanding tasks, outperforming well-established methods in multiple benchmarks, including MUSE, single- and multi-referring segmentation. Comprehensive ablations confirm the efficacy of each proposed component. All code, models, and datasets will be publicly available.

</details>

### TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding.
- **链接**: [arXiv:2312.02051](https://arxiv.org/abs/2312.02051) · 📚 被引 170
- **作者**: Shuhuai Ren, Linli Yao, Shicheng Li, Xu Sun, Lu Hou
- **🏷️ 机构**: National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes TimeChat, a time-sensitive multimodal large language model specifically designed for long video understanding. Our model incorporates two key architectural contributions: (1) a timestamp-aware frame encoder that binds visual content with the timestamp of each frame, and (2) a sliding video Q-Former that produces a video token sequence of varying lengths to accommodate videos of various durations. Additionally, we construct an instruction-tuning dataset, encompassing 6 tasks and a total of 125K instances, to further enhance TimeChat's instruction-following performance. Experiment results across various video understanding tasks, such as dense captioning, temporal grounding, and highlight detection, demonstrate TimeChat's strong zero-shot temporal localization and reasoning capabilities. For example, it achieves +9.2 F1 score and +2.8 CIDEr on YouCook2, +5.8 HIT@1 on QVHighlights, and +27.5 R@1 (IoU=0.5) on Charades-STA, compared to state-of-the-art video large language models, holding the potential to serve as a versatile video assistant for long-form video comprehension tasks and satisfy realistic user requirements.

</details>

### OmniVec2 - A Novel Transformer Based Network for Large Scale Multimodal and Multitask Learning.
- **链接**: [arXiv:2507.13364](https://arxiv.org/abs/2507.13364) · 📚 被引 36
- **作者**: Siddharth Srivastava, Gaurav Sharma
- **🏷️ 机构**: Typeface
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel multimodal multitask network and associated training algorithm. The method is capable of ingesting data from approximately 12 different modalities namely image, video, audio, text, depth, point cloud, time series, tabular, graph, X-ray, infrared, IMU, and hyperspectral. The proposed approach utilizes modality specialized tokenizers, a shared transformer architecture, and cross-attention mechanisms to project the data from different modalities into a unified embedding space. It addresses multimodal and multitask scenarios by incorporating modality-specific task heads for different tasks in respective modalities. We propose a novel pretraining strategy with iterative modality switching to initialize the network, and a training algorithm which trades off fully joint training over all modalities, with training on pairs of modalities at a time. We provide comprehensive evaluation across 25 datasets from 12 modalities and show state of the art performances, demonstrating the effectiveness of the proposed architecture, pretraining strategy and adapted multitask training.

</details>

### Generative Multimodal Models are In-Context Learners.
- **链接**: [arXiv:2312.13286](https://arxiv.org/abs/2312.13286) · 📚 被引 126
- **作者**: Quan Sun, Yufeng Cui, Xiaosong Zhang, Fan Zhang, Qiying Yu, Yueze Wang et al.
- **🏷️ 机构**: Beijing Academy of Artificial Intelligence, Tsinghua University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The human ability to easily solve multimodal tasks in context (i.e., with only a few demonstrations or simple instructions), is what current multimodal systems have largely struggled to imitate. In this work, we demonstrate that the task-agnostic in-context learning capabilities of large multimodal models can be significantly enhanced by effective scaling-up. We introduce Emu2, a generative multimodal model with 37 billion parameters, trained on large-scale multimodal sequences with a unified autoregressive objective. Emu2 exhibits strong multimodal in-context learning abilities, even emerging to solve tasks that require on-the-fly reasoning, such as visual prompting and object-grounded generation. The model sets a new record on multiple multimodal understanding tasks in few-shot settings. When instruction-tuned to follow specific instructions, Emu2 further achieves new state-of-the-art on challenging tasks such as question answering benchmarks for large multimodal models and open-ended subject-driven generation. These achievements demonstrate that Emu2 can serve as a base model and general-purpose interface for a wide range of multimodal tasks. Code and models are publicly available to facilitate future research.

</details>

### Contextual Augmented Global Contrast for Multimodal Intent Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02546) · 📚 被引 32
- **作者**: Kaili Sun, Zhiwen Xie, Mang Ye, Huyin Zhang
- **🏷️ 机构**: School of Computer Science, Wuhan University,Wuhan,China, School of Computer Science, Central China Normal University,Wuhan,China
- **会议**: CVPR 2024

### GlitchBench: Can Large Multimodal Models Detect Video Game Glitches?
- **链接**: [arXiv:2312.05291](https://arxiv.org/abs/2312.05291) · 📚 被引 14
- **作者**: Mohammad Reza Taesiri, Tianjun Feng, Cor-Paul Bezemer, Anh Nguyen
- **🏷️ 机构**: University of Alberta, Auburn University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal models (LMMs) have evolved from large language models (LLMs) to integrate multiple input modalities, such as visual inputs. This integration augments the capacity of LLMs for tasks requiring visual comprehension and reasoning. However, the extent and limitations of their enhanced abilities are not fully understood, especially when it comes to real-world tasks. To address this gap, we introduce GlitchBench, a novel benchmark derived from video game quality assurance tasks, to test and evaluate the reasoning capabilities of LMMs. Our benchmark is curated from a variety of unusual and glitched scenarios from video games and aims to challenge both the visual and linguistic reasoning powers of LMMs in detecting and interpreting out-of-the-ordinary events. We evaluate multiple state-of-the-art LMMs, and we show that GlitchBench presents a new challenge for these models. Code and data are available at: https://glitchbench.github.io/

</details>

### Link-Context Learning for Multimodal LLMs.
- **链接**: [arXiv:2308.07891](https://arxiv.org/abs/2308.07891) · 📚 被引 6
- **作者**: Yan Tai, Weichen Fan, Zhao Zhang, Ziwei Liu
- **🏷️ 机构**: Ningbo Institute of Digital Twin, Eastern Institute of Technology,Ningbo,China, SenseTime Research, Nanyang Technological University,S-Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to learn from context with novel concepts, and deliver appropriate responses are essential in human conversations. Despite current Multimodal Large Language Models (MLLMs) and Large Language Models (LLMs) being trained on mega-scale datasets, recognizing unseen images or understanding novel concepts in a training-free manner remains a challenge. In-Context Learning (ICL) explores training-free few-shot learning, where models are encouraged to ``learn to learn" from limited tasks and generalize to unseen tasks. In this work, we propose link-context learning (LCL), which emphasizes "reasoning from cause and effect" to augment the learning capabilities of MLLMs. LCL goes beyond traditional ICL by explicitly strengthening the causal relationship between the support set and the query set. By providing demonstrations with causal links, LCL guides the model to discern not only the analogy but also the underlying causal associations between data points, which empowers MLLMs to recognize unseen images and understand novel concepts more effectively. To facilitate the evaluation of this novel approach, we introduce the ISEKAI dataset, comprising exclusively of unseen generated image-label pairs designed for link-context learning. Extensive experiments show that our LCL-MLLM exhibits strong link-context learning capabilities to novel concepts over vanilla MLLMs. Code and data will be released at https://github.com/isekai-portal/Link-Context-Learning.

</details>

### Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs.
- **链接**: [arXiv:2401.06209](https://arxiv.org/abs/2401.06209) · 📚 被引 192
- **作者**: Shengbang Tong, Zhuang Liu, Yuexiang Zhai, Yi Ma, Yann LeCun, Saining Xie
- **🏷️ 机构**: New York University, FAIR, Meta, UC Berkeley
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Is vision good enough for language? Recent advancements in multimodal models primarily stem from the powerful reasoning abilities of large language models (LLMs). However, the visual component typically depends only on the instance-level contrastive language-image pre-training (CLIP). Our research reveals that the visual capabilities in recent multimodal LLMs (MLLMs) still exhibit systematic shortcomings. To understand the roots of these errors, we explore the gap between the visual embedding space of CLIP and vision-only self-supervised learning. We identify ''CLIP-blind pairs'' - images that CLIP perceives as similar despite their clear visual differences. With these pairs, we construct the Multimodal Visual Patterns (MMVP) benchmark. MMVP exposes areas where state-of-the-art systems, including GPT-4V, struggle with straightforward questions across nine basic visual patterns, often providing incorrect answers and hallucinated explanations. We further evaluate various CLIP-based vision-and-language models and found a notable correlation between visual patterns that challenge CLIP models and those problematic for multimodal LLMs. As an initial effort to address these issues, we propose a Mixture of Features (MoF) approach, demonstrating that integrating vision self-supervised learning features with MLLMs can significantly enhance their visual grounding capabilities. Together, our research suggests visual representation learning remains an open challenge, and accurate visual grounding is crucial for future successful multimodal systems.

</details>

### Data-Efficient Multimodal Fusion on a Single GPU.
- **链接**: [arXiv:2312.10144](https://arxiv.org/abs/2312.10144) · 📚 被引 8
- **作者**: Noël Vouitsis, Zhaoyan Liu, Satya Krishna Gorti, Valentin Villecroze, Jesse C. Cresswell, Guangwei Yu et al.
- **🏷️ 机构**: Layer 6 AI
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of multimodal alignment is to learn a single latent space that is shared between multimodal inputs. The most powerful models in this space have been trained using massive datasets of paired inputs and large-scale computational resources, making them prohibitively expensive to train in many practical scenarios. We surmise that existing unimodal encoders pre-trained on large amounts of unimodal data should provide an effective bootstrap to create multimodal models from unimodal ones at much lower costs. We therefore propose FuseMix, a multimodal augmentation scheme that operates on the latent spaces of arbitrary pre-trained unimodal encoders. Using FuseMix for multimodal alignment, we achieve competitive performance -- and in certain cases outperform state-of-the art methods -- in both image-text and audio-text retrieval, with orders of magnitude less compute and data: for example, we outperform CLIP on the Flickr30K text-to-image retrieval task with $\sim \! 600\times$ fewer GPU days and $\sim \! 80\times$ fewer image-text pairs. Additionally, we show how our method can be applied to convert pre-trained text-to-image generative models into audio-to-image ones. Code is available at: https://github.com/layer6ai-labs/fusemix.

</details>

### Polos: Multimodal Metric Learning from Human Feedback for Image Captioning.
- **链接**: [arXiv:2402.18091](https://arxiv.org/abs/2402.18091) · 📚 被引 19
- **作者**: Yuiga Wada, Kanta Kaneda, Daichi Saito, Komei Sugiura
- **🏷️ 机构**: Keio University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Establishing an automatic evaluation metric that closely aligns with human judgments is essential for effectively developing image captioning models. Recent data-driven metrics have demonstrated a stronger correlation with human judgments than classic metrics such as CIDEr; however they lack sufficient capabilities to handle hallucinations and generalize across diverse images and texts partially because they compute scalar similarities merely using embeddings learned from tasks unrelated to image captioning evaluation. In this study, we propose Polos, a supervised automatic evaluation metric for image captioning models. Polos computes scores from multimodal inputs, using a parallel feature extraction mechanism that leverages embeddings trained through large-scale contrastive learning. To train Polos, we introduce Multimodal Metric Learning from Human Feedback (M$^2$LHF), a framework for developing metrics based on human feedback. We constructed the Polaris dataset, which comprises 131K human judgments from 550 evaluators, which is approximately ten times larger than standard datasets. Our approach achieved state-of-the-art performance on Composite, Flickr8K-Expert, Flickr8K-CF, PASCAL-50S, FOIL, and the Polaris dataset, thereby demonstrating its effectiveness and robustness.

</details>

### Cloud-Device Collaborative Learning for Multimodal Large Language Models.
- **链接**: [arXiv:2312.16279](https://arxiv.org/abs/2312.16279) · 📚 被引 24
- **作者**: Guanqun Wang, Jiaming Liu, Chenxuan Li, Yuan Zhang, Junpeng Ma, Xinyu Wei et al.
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The burgeoning field of Multimodal Large Language Models (MLLMs) has exhibited remarkable performance in diverse tasks such as captioning, commonsense reasoning, and visual scene understanding. However, the deployment of these large-scale MLLMs on client devices is hindered by their extensive model parameters, leading to a notable decline in generalization capabilities when these models are compressed for device deployment. Addressing this challenge, we introduce a Cloud-Device Collaborative Continual Adaptation framework, designed to enhance the performance of compressed, device-deployed MLLMs by leveraging the robust capabilities of cloud-based, larger-scale MLLMs. Our framework is structured into three key components: a device-to-cloud uplink for efficient data transmission, cloud-based knowledge adaptation, and an optimized cloud-to-device downlink for model deployment. In the uplink phase, we employ an Uncertainty-guided Token Sampling (UTS) strategy to effectively filter out-of-distribution tokens, thereby reducing transmission costs and improving training efficiency. On the cloud side, we propose Adapter-based Knowledge Distillation (AKD) method to transfer refined knowledge from large-scale to compressed, pocket-size MLLMs. Furthermore, we propose a Dynamic Weight update Compression (DWC) strategy for the downlink, which adaptively selects and quantizes updated weight parameters, enhancing transmission efficiency and reducing the representational disparity between cloud and device models. Extensive experiments on several multimodal benchmarks demonstrate the superiority of our proposed framework over prior Knowledge Distillation and device-cloud collaboration methods. Notably, we also validate the feasibility of our approach to real-world experiments.

</details>

### Enhancing Multimodal Cooperation via Sample-Level Modality Valuation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02581) · 📚 被引 36
- **作者**: Yake Wei, Ruoxuan Feng, Zihe Wang, Di Hu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing
- **会议**: CVPR 2024

### Omni-SMoLA: Boosting Generalist Multimodal Models with Soft Mixture of Low-Rank Experts.
- **链接**: [arXiv:2312.00968](https://arxiv.org/abs/2312.00968) · 📚 被引 16
- **作者**: Jialin Wu, Xia Hu, Yaqing Wang, Bo Pang, Radu Soricut
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multi-modal models (LMMs) exhibit remarkable performance across numerous tasks. However, generalist LMMs often suffer from performance degradation when tuned over a large collection of tasks. Recent research suggests that Mixture of Experts (MoE) architectures are useful for instruction tuning, but for LMMs of parameter size around O(50-100B), the prohibitive cost of replicating and storing the expert models severely limits the number of experts we can use. We propose Omni-SMoLA, an architecture that uses the Soft MoE approach to (softly) mix many multimodal low rank experts, and avoids introducing a significant number of new parameters compared to conventional MoE models. The core intuition here is that the large model provides a foundational backbone, while different lightweight experts residually learn specialized knowledge, either per-modality or multimodally. Extensive experiments demonstrate that the SMoLA approach helps improve the generalist performance across a broad range of generative vision-and-language tasks, achieving new SoTA generalist performance that often matches or outperforms single specialized LMM baselines, as well as new SoTA specialist performance.

</details>

### Towards Language-Driven Video Inpainting via Multimodal Large Language Models.
- **链接**: [arXiv:2401.10226](https://arxiv.org/abs/2401.10226) · 📚 被引 27
- **作者**: Jianzong Wu, Xiangtai Li, Chenyang Si, Shangchen Zhou, Jingkang Yang, Jiangning Zhang et al.
- **🏷️ 机构**: National Key Laboratory of General Artificial Intelligence, Peking University, S-Lab, Nanyang Technological University, Zhejiang University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a new task -- language-driven video inpainting, which uses natural language instructions to guide the inpainting process. This approach overcomes the limitations of traditional video inpainting methods that depend on manually labeled binary masks, a process often tedious and labor-intensive. We present the Remove Objects from Videos by Instructions (ROVI) dataset, containing 5,650 videos and 9,091 inpainting results, to support training and evaluation for this task. We also propose a novel diffusion-based language-driven video inpainting framework, the first end-to-end baseline for this task, integrating Multimodal Large Language Models to understand and execute complex language-based inpainting requests effectively. Our comprehensive results showcase the dataset's versatility and the model's effectiveness in various language-instructed inpainting scenarios. We will make datasets, code, and models publicly available.

</details>

### V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01243) · 📚 被引 56
- **作者**: Penghao Wu, Saining Xie
- **🏷️ 机构**: UC,San Diego, New York University
- **会议**: CVPR 2024

### GSVA: Generalized Segmentation via Multimodal Large Language Models.
- **链接**: [arXiv:2312.10103](https://arxiv.org/abs/2312.10103) · 📚 被引 83
- **作者**: Zhuofan Xia, Dongchen Han, Yizeng Han, Xuran Pan, Shiji Song, Gao Huang
- **🏷️ 机构**: Department of Automation, BNRist, Tsinghua University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized Referring Expression Segmentation (GRES) extends the scope of classic RES to refer to multiple objects in one expression or identify the empty targets absent in the image. GRES poses challenges in modeling the complex spatial relationships of the instances in the image and identifying non-existing referents. Multimodal Large Language Models (MLLMs) have recently shown tremendous progress in these complicated vision-language tasks. Connecting Large Language Models (LLMs) and vision models, MLLMs are proficient in understanding contexts with visual inputs. Among them, LISA, as a representative, adopts a special [SEG] token to prompt a segmentation mask decoder, e.g., SAM, to enable MLLMs in the RES task. However, existing solutions to GRES remain unsatisfactory since current segmentation MLLMs cannot correctly handle the cases where users might reference multiple subjects in a singular prompt or provide descriptions incongruent with any image target. In this paper, we propose Generalized Segmentation Vision Assistant (GSVA) to address this gap. Specifically, GSVA reuses the [SEG] token to prompt the segmentation model towards supporting multiple mask references simultaneously and innovatively learns to generate a [REJ] token to reject the null targets explicitly. Experiments validate GSVA's efficacy in resolving the GRES issue, marking a notable enhancement and setting a new record on the GRES benchmark gRefCOCO dataset. GSVA also proves effective across various classic referring segmentation and comprehension tasks.

</details>

### ULIP-2: Towards Scalable Multimodal Pre-Training for 3D Understanding.
- **链接**: [arXiv:2305.08275](https://arxiv.org/abs/2305.08275) · 📚 被引 110
- **作者**: Le Xue, Ning Yu, Shu Zhang, Artemis Panagopoulou, Junnan Li, Roberto Martín-Martín et al.
- **🏷️ 机构**: Salesforce AI Research, University of Texas at Austin, Stanford University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in multimodal pre-training have shown promising efficacy in 3D representation learning by aligning multimodal features across 3D shapes, their 2D counterparts, and language descriptions. However, the methods used by existing frameworks to curate such multimodal data, in particular language descriptions for 3D shapes, are not scalable, and the collected language descriptions are not diverse. To address this, we introduce ULIP-2, a simple yet effective tri-modal pre-training framework that leverages large multimodal models to automatically generate holistic language descriptions for 3D shapes. It only needs 3D data as input, eliminating the need for any manual 3D annotations, and is therefore scalable to large datasets. ULIP-2 is also equipped with scaled-up backbones for better multimodal representation learning. We conduct experiments on two large-scale 3D datasets, Objaverse and ShapeNet, and augment them with tri-modal datasets of 3D point clouds, images, and language for training ULIP-2. Experiments show that ULIP-2 demonstrates substantial benefits in three downstream tasks: zero-shot 3D classification, standard 3D classification with fine-tuning, and 3D captioning (3D-to-language generation). It achieves a new SOTA of 50.6% (top-1) on Objaverse-LVIS and 84.7% (top-1) on ModelNet40 in zero-shot classification. In the ScanObjectNN benchmark for standard fine-tuning, ULIP-2 reaches an overall accuracy of 91.5% with a compact model of only 1.4 million parameters. ULIP-2 sheds light on a new paradigm for scalable multimodal 3D representation learning without human annotations and shows significant improvements over existing baselines. The code and datasets are released at https://github.com/salesforce/ULIP.

</details>

### RELI11D: A Comprehensive Multimodal Human Motion Dataset and Method.
- **链接**: [arXiv:2403.19501](https://arxiv.org/abs/2403.19501) · 📚 被引 10
- **作者**: Ming Yan, Yan Zhang, Shuqiang Cai, Shuqi Fan, Xincheng Lin, Yudi Dai et al.
- **🏷️ 机构**: Fujian Key Laboratory of Sensing and Computing for Smart Cities, Xiamen University, Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China, School of Informatics, Xiamen University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Comprehensive capturing of human motions requires both accurate captures of complex poses and precise localization of the human within scenes. Most of the HPE datasets and methods primarily rely on RGB, LiDAR, or IMU data. However, solely using these modalities or a combination of them may not be adequate for HPE, particularly for complex and fast movements. For holistic human motion understanding, we present RELI11D, a high-quality multimodal human motion dataset involves LiDAR, IMU system, RGB camera, and Event camera. It records the motions of 10 actors performing 5 sports in 7 scenes, including 3.32 hours of synchronized LiDAR point clouds, IMU measurement data, RGB videos and Event steams. Through extensive experiments, we demonstrate that the RELI11D presents considerable challenges and opportunities as it contains many rapid and complex motions that require precise location. To address the challenge of integrating different modalities, we propose LEIR, a multimodal baseline that effectively utilizes LiDAR Point Cloud, Event stream, and RGB through our cross-attention fusion strategy. We show that LEIR exhibits promising results for rapid motions and daily motions and that utilizing the characteristics of multiple modalities can indeed improve HPE performance. Both the dataset and source code will be released publicly to the research community, fostering collaboration and enabling further exploration in this field.

</details>

### MMA-Diffusion: MultiModal Attack on Diffusion Models.
- **链接**: [arXiv:2311.17516](https://arxiv.org/abs/2311.17516) · 📚 被引 59
- **作者**: Yijun Yang, Ruiyuan Gao, Xiaosen Wang, Tsung-Yi Ho, Nan Xu, Qiang Xu
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Singular Security Lab, Institute of Automation, Chinese Academy of Sciences
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, Text-to-Image (T2I) models have seen remarkable advancements, gaining widespread adoption. However, this progress has inadvertently opened avenues for potential misuse, particularly in generating inappropriate or Not-Safe-For-Work (NSFW) content. Our work introduces MMA-Diffusion, a framework that presents a significant and realistic threat to the security of T2I models by effectively circumventing current defensive measures in both open-source models and commercial online services. Unlike previous approaches, MMA-Diffusion leverages both textual and visual modalities to bypass safeguards like prompt filters and post-hoc safety checkers, thus exposing and highlighting the vulnerabilities in existing defense mechanisms.

</details>

### Binding Touch to Everything: Learning Unified Multimodal Tactile Representations.
- **链接**: [arXiv:2401.18084](https://arxiv.org/abs/2401.18084) · 📚 被引 59
- **作者**: Fengyu Yang, Chao Feng, Ziyang Chen, Hyoungseob Park, Daniel Wang, Yiming Dou et al.
- **🏷️ 机构**: Yale University, University of Michigan
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to associate touch with other modalities has huge implications for humans and computational systems. However, multimodal learning with touch remains challenging due to the expensive data collection process and non-standardized sensor outputs. We introduce UniTouch, a unified tactile model for vision-based touch sensors connected to multiple modalities, including vision, language, and sound. We achieve this by aligning our UniTouch embeddings to pretrained image embeddings already associated with a variety of other modalities. We further propose learnable sensor-specific tokens, allowing the model to learn from a set of heterogeneous tactile sensors, all at the same time. UniTouch is capable of conducting various touch sensing tasks in the zero-shot setting, from robot grasping prediction to touch image question answering. To the best of our knowledge, UniTouch is the first to demonstrate such capabilities. Project page: https://cfeng16.github.io/UniTouch/

</details>

### Narrative Action Evaluation with Prompt-Guided Multimodal Interaction.
- **链接**: [arXiv:2404.14471](https://arxiv.org/abs/2404.14471) · 📚 被引 17
- **作者**: Shiyi Zhang, Sule Bai, Guangyi Chen, Lei Chen, Jiwen Lu, Junle Wang et al.
- **🏷️ 机构**: Shenzhen International Graduate School, Tsinghua University, Carnegie Mellon University,Pittsburgh,PA,USA, Tsinghua University,Department of Automation
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate a new problem called narrative action evaluation (NAE). NAE aims to generate professional commentary that evaluates the execution of an action. Unlike traditional tasks such as score-based action quality assessment and video captioning involving superficial sentences, NAE focuses on creating detailed narratives in natural language. These narratives provide intricate descriptions of actions along with objective evaluations. NAE is a more challenging task because it requires both narrative flexibility and evaluation rigor. One existing possible solution is to use multi-task learning, where narrative language and evaluative information are predicted separately. However, this approach results in reduced performance for individual tasks because of variations between tasks and differences in modality between language information and evaluation information. To address this, we propose a prompt-guided multimodal interaction framework. This framework utilizes a pair of transformers to facilitate the interaction between different modalities of information. It also uses prompts to transform the score regression task into a video-text matching task, thus enabling task interactivity. To support further research in this field, we re-annotate the MTL-AQA and FineGym datasets with high-quality and comprehensive action narration. Additionally, we establish benchmarks for NAE. Extensive experiment results prove that our method outperforms separate learning methods and naive multi-task learning methods. Data and code are released at https://github.com/shiyi-zh0408/NAE_CVPR2024.

</details>

### Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities.
- **链接**: [arXiv:2401.14405](https://arxiv.org/abs/2401.14405) · 📚 被引 8
- **作者**: Yiyuan Zhang, Xiaohan Ding, Kaixiong Gong, Yixiao Ge, Ying Shan, Xiangyu Yue
- **🏷️ 机构**: The Chinese University of Hong Kong,MMLab, Tencent AI Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to improve transformers of a specific modality with irrelevant data from other modalities, e.g., improve an ImageNet model with audio or point cloud datasets. We would like to highlight that the data samples of the target modality are irrelevant to the other modalities, which distinguishes our method from other works utilizing paired (e.g., CLIP) or interleaved data of different modalities. We propose a methodology named Multimodal Pathway - given a target modality and a transformer designed for it, we use an auxiliary transformer trained with data of another modality and construct pathways to connect components of the two models so that data of the target modality can be processed by both models. In this way, we utilize the universal sequence-to-sequence modeling abilities of transformers obtained from two modalities. As a concrete implementation, we use a modality-specific tokenizer and task-specific head as usual but utilize the transformer blocks of the auxiliary model via a proposed method named Cross-Modal Re-parameterization, which exploits the auxiliary weights without any inference costs. On the image, point cloud, video, and audio recognition tasks, we observe significant and consistent performance improvements with irrelevant data from other modalities. The code and models are available at https://github.com/AILab-CVC/M2PT.

</details>

### Exploring the Transferability of Visual Prompting for Multimodal Large Language Models.
- **链接**: [arXiv:2404.11207](https://arxiv.org/abs/2404.11207) · 📚 被引 14
- **作者**: Yichi Zhang, Yinpeng Dong, Siyuan Zhang, Tianzan Min, Hang Su, Jun Zhu
- **🏷️ 机构**: Institute for AI, Tsinghua-Bosch Joint ML Center, BNRist Center, Tsinghua University,THBI Lab,Dept. of Comp. Sci. and Tech.,Beijing,China,100084
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although Multimodal Large Language Models (MLLMs) have demonstrated promising versatile capabilities, their performance is still inferior to specialized models on downstream tasks, which makes adaptation necessary to enhance their utility. However, fine-tuning methods require independent training for every model, leading to huge computation and memory overheads. In this paper, we propose a novel setting where we aim to improve the performance of diverse MLLMs with a group of shared parameters optimized for a downstream task. To achieve this, we propose Transferable Visual Prompting (TVP), a simple and effective approach to generate visual prompts that can transfer to different models and improve their performance on downstream tasks after trained on only one model. We introduce two strategies to address the issue of cross-model feature corruption of existing visual prompting methods and enhance the transferability of the learned prompts, including 1) Feature Consistency Alignment: which imposes constraints to the prompted feature changes to maintain task-agnostic knowledge; 2) Task Semantics Enrichment: which encourages the prompted images to contain richer task-specific semantics with language guidance. We validate the effectiveness of TVP through extensive experiments with 6 modern MLLMs on a wide variety of tasks ranging from object recognition and counting to multimodal reasoning and hallucination correction.

</details>

### C3Net: Compound Conditioned ControlNet for Multimodal Content Generation.
- **链接**: [arXiv:2311.17951](https://arxiv.org/abs/2311.17951) · 📚 被引 6
- **作者**: Juntao Zhang, Yuehuai Liu, Yu-Wing Tai, Chi-Keung Tang
- **🏷️ 机构**: HKUST, Dartmouth College
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Compound Conditioned ControlNet, C3Net, a novel generative neural architecture taking conditions from multiple modalities and synthesizing multimodal contents simultaneously (e.g., image, text, audio). C3Net adapts the ControlNet architecture to jointly train and make inferences on a production-ready diffusion model and its trainable copies. Specifically, C3Net first aligns the conditions from multi-modalities to the same semantic latent space using modality-specific encoders based on contrastive training. Then, it generates multimodal outputs based on the aligned latent space, whose semantic information is combined using a ControlNet-like architecture called Control C3-UNet. Correspondingly, with this system design, our model offers an improved solution for joint-modality generation through learning and explaining multimodal conditions instead of simply taking linear interpolations on the latent space. Meanwhile, as we align conditions to a unified latent space, C3Net only requires one trainable Control C3-UNet to work on multimodal semantic information. Furthermore, our model employs unimodal pretraining on the condition alignment stage, outperforming the non-pretrained alignment even on relatively scarce training data and thus demonstrating high-quality compound condition generation. We contribute the first high-quality tri-modal validation set to validate quantitatively that C3Net outperforms or is on par with first and contemporary state-of-the-art multimodal generation. Our codes and tri-modal dataset will be released.

</details>

### MM-Narrator: Narrating Long-form Videos with Multimodal In-Context Learning.
- **链接**: [arXiv:2311.17435](https://arxiv.org/abs/2311.17435) · 📚 被引 26
- **作者**: Chaoyi Zhang, Kevin Lin, Zhengyuan Yang, Jianfeng Wang, Linjie Li, Chung-Ching Lin et al.
- **🏷️ 机构**: University of Sydney, Microsoft, Advanced Micro Devices
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MM-Narrator, a novel system leveraging GPT-4 with multimodal in-context learning for the generation of audio descriptions (AD). Unlike previous methods that primarily focused on downstream fine-tuning with short video clips, MM-Narrator excels in generating precise audio descriptions for videos of extensive lengths, even beyond hours, in an autoregressive manner. This capability is made possible by the proposed memory-augmented generation process, which effectively utilizes both the short-term textual context and long-term visual memory through an efficient register-and-recall mechanism. These contextual memories compile pertinent past information, including storylines and character identities, ensuring an accurate tracking and depicting of story-coherent and character-centric audio descriptions. Maintaining the training-free design of MM-Narrator, we further propose a complexity-based demonstration selection strategy to largely enhance its multi-step reasoning capability via few-shot multimodal in-context learning (MM-ICL). Experimental results on MAD-eval dataset demonstrate that MM-Narrator consistently outperforms both the existing fine-tuning-based approaches and LLM-based approaches in most scenarios, as measured by standard evaluation metrics. Additionally, we introduce the first segment-based evaluator for recurrent text generation. Empowered by GPT-4, this evaluator comprehensively reasons and marks AD generation performance in various extendable dimensions.

</details>

### MMVP: A Multimodal MoCap Dataset with Vision and Pressure Sensors.
- **链接**: [arXiv:2403.17610](https://arxiv.org/abs/2403.17610) · 📚 被引 12
- **作者**: He Zhang, Shenghao Ren, Haolei Yuan, Jianhui Zhao, Fan Li, Shuangpeng Sun et al.
- **🏷️ 机构**: Beihang University, Nanjing University, Tsinghua University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Foot contact is an important cue for human motion capture, understanding, and generation. Existing datasets tend to annotate dense foot contact using visual matching with thresholding or incorporating pressure signals. However, these approaches either suffer from low accuracy or are only designed for small-range and slow motion. There is still a lack of a vision-pressure multimodal dataset with large-range and fast human motion, as well as accurate and dense foot-contact annotation. To fill this gap, we propose a Multimodal MoCap Dataset with Vision and Pressure sensors, named MMVP. MMVP provides accurate and dense plantar pressure signals synchronized with RGBD observations, which is especially useful for both plausible shape estimation, robust pose fitting without foot drifting, and accurate global translation tracking. To validate the dataset, we propose an RGBD-P SMPL fitting method and also a monocular-video-based baseline framework, VP-MoCap, for human motion capture. Experiments demonstrate that our RGBD-P SMPL Fitting results significantly outperform pure visual motion capture. Moreover, VP-MoCap outperforms SOTA methods in foot-contact and global translation estimation accuracy. We believe the configuration of the dataset and the baseline frameworks will stimulate the research in this direction and also provide a good reference for MoCap applications in various domains. Project page: https://metaverse-ai-lab-thu.github.io/MMVP-Dataset/.

</details>

### TRINS: Towards Multimodal Language Models that Can Read.
- **链接**: [arXiv:2406.06730](https://arxiv.org/abs/2406.06730) · 📚 被引 1
- **作者**: Ruiyi Zhang, Yanzhe Zhang, Jian Chen, Yufan Zhou, Jiuxiang Gu, Changyou Chen et al.
- **🏷️ 机构**: Adobe Research, Georgia Institute of Technology, State University of New York at Buffalo
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal language models have shown remarkable proficiency in understanding and editing images. However, a majority of these visually-tuned models struggle to comprehend the textual content embedded in images, primarily due to the limitation of training data. In this work, we introduce TRINS: a Text-Rich image INStruction dataset, with the objective of enhancing the reading ability of the multimodal large language model. TRINS is built upon LAION using hybrid data annotation strategies that include machine-assisted and human-assisted annotation processes. It contains 39,153 text-rich images, captions, and 102,437 questions. Specifically, we show that the number of words per annotation in TRINS is significantly longer than that of related datasets, providing new challenges. Furthermore, we introduce a simple and effective architecture, called a Language-vision Reading Assistant (LaRA), which is good at understanding textual content within images. LaRA outperforms existing state-of-the-art multimodal large language models on the TRINS dataset, as well as other classical benchmarks. Lastly, we conducted a comprehensive evaluation with TRINS on various text-rich image understanding and generation tasks, demonstrating its effectiveness.

</details>

### Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language.
- **链接**: [arXiv:2406.05629](https://arxiv.org/abs/2406.05629) · 📚 被引 9
- **作者**: Mark Hamilton, Andrew Zisserman, John R. Hershey, William T. Freeman
- **🏷️ 机构**: MIT, Microsoft, Oxford, Google, Google
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present DenseAV, a novel dual encoder grounding architecture that learns high-resolution, semantically meaningful, and audio-visually aligned features solely through watching videos. We show that DenseAV can discover the ``meaning'' of words and the ``location'' of sounds without explicit localization supervision. Furthermore, it automatically discovers and distinguishes between these two types of associations without supervision. We show that DenseAV's localization abilities arise from a new multi-head feature aggregation operator that directly compares dense image and audio representations for contrastive learning. In contrast, many other systems that learn ``global'' audio and video representations cannot localize words and sound. Finally, we contribute two new datasets to improve the evaluation of AV representations through speech and sound prompted semantic segmentation. On these and other datasets we show DenseAV dramatically outperforms the prior art on speech and sound prompted semantic segmentation. DenseAV outperforms the previous state-of-the-art, ImageBind, on cross-modal retrieval using fewer than half of the parameters. Project Page: \href{https://aka.ms/denseav}{https://aka.ms/denseav}

</details>

### ES3: Evolving Self-Supervised Learning of Robust Audio-Visual Speech Representations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02556) · 📚 被引 8
- **作者**: Yuanhang Zhang, Shuang Yang, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology, CAS,Key Laboratory of Intelligent Information Processing of Chinese Academy of Sciences (CAS),Beijing,China,100190
- **会议**: CVPR 2024

### Enhancing Visual Document Understanding with Contrastive Learning in Large Visual-Language Models.
- **链接**: [arXiv:2402.19014](https://arxiv.org/abs/2402.19014) · 📚 被引 28
- **作者**: Xin Li, Yunfei Wu, Xinghua Jiang, Zhihao Guo, Mingming Gong, Haoyu Cao et al.
- **🏷️ 机构**: Tencent YouTu Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the advent of Large Visual-Language Models (LVLMs) has received increasing attention across various domains, particularly in the field of visual document understanding (VDU). Different from conventional vision-language tasks, VDU is specifically concerned with text-rich scenarios containing abundant document elements. Nevertheless, the importance of fine-grained features remains largely unexplored within the community of LVLMs, leading to suboptimal performance in text-rich scenarios. In this paper, we abbreviate it as the fine-grained feature collapse issue. With the aim of filling this gap, we propose a contrastive learning framework, termed Document Object COntrastive learning (DoCo), specifically tailored for the downstream tasks of VDU. DoCo leverages an auxiliary multimodal encoder to obtain the features of document objects and align them to the visual features generated by the vision encoder of LVLM, which enhances visual representation in text-rich scenarios. It can represent that the contrastive learning between the visual holistic representations and the multimodal fine-grained features of document objects can assist the vision encoder in acquiring more effective visual cues, thereby enhancing the comprehension of text-rich documents in LVLMs. We also demonstrate that the proposed DoCo serves as a plug-and-play pre-training method, which can be employed in the pre-training of various LVLMs without inducing any increase in computational complexity during the inference process. Extensive experimental results on multiple benchmarks of VDU reveal that LVLMs equipped with our proposed DoCo can achieve superior performance and mitigate the gap between VDU and generic vision-language tasks.

</details>

### MLIP: Enhancing Medical Visual Representation with Divergence Encoder and Knowledge-guided Contrastive Learning.
- **链接**: [arXiv:2402.02045](https://arxiv.org/abs/2402.02045) · 📚 被引 31
- **作者**: Zhe Li, Laurence T. Yang, Bocheng Ren, Xin Nie, Zhangyang Gao, Cheng Tan et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, AI Lab, Research Center for Industries of the Future, Westlake University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The scarcity of annotated data has sparked significant interest in unsupervised pre-training methods that leverage medical reports as auxiliary signals for medical visual representation learning. However, existing research overlooks the multi-granularity nature of medical visual representation and lacks suitable contrastive learning techniques to improve the models' generalizability across different granularities, leading to the underutilization of image-text information. To address this, we propose MLIP, a novel framework leveraging domain-specific medical knowledge as guiding signals to integrate language information into the visual domain through image-text contrastive learning. Our model includes global contrastive learning with our designed divergence encoder, local token-knowledge-patch alignment contrastive learning, and knowledge-guided category-level contrastive learning with expert knowledge. Experimental evaluations reveal the efficacy of our model in enhancing transfer performance for tasks such as image classification, object detection, and semantic segmentation. Notably, MLIP surpasses state-of-the-art methods even with limited annotated data, highlighting the potential of multimodal pre-training in advancing medical representation learning.

</details>

### Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding.
- **链接**: [arXiv:2311.08046](https://arxiv.org/abs/2311.08046) · 📚 被引 156
- **作者**: Peng Jin, Ryuichi Takanobu, Wancai Zhang, Xiaochun Cao, Li Yuan
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University,Shenzhen,China, Peng Cheng Laboratory,Shenzhen,China, Nari Technology Co.,Ltd.,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models have demonstrated impressive universal capabilities across a wide range of open-ended tasks and have extended their utility to encompass multimodal conversations. However, existing methods encounter challenges in effectively handling both image and video understanding, particularly with limited visual tokens. In this work, we introduce Chat-UniVi, a Unified Vision-language model capable of comprehending and engaging in conversations involving images and videos through a unified visual representation. Specifically, we employ a set of dynamic visual tokens to uniformly represent images and videos. This representation framework empowers the model to efficiently utilize a limited number of visual tokens to simultaneously capture the spatial details necessary for images and the comprehensive temporal relationship required for videos. Moreover, we leverage a multi-scale representation, enabling the model to perceive both high-level semantic concepts and low-level visual details. Notably, Chat-UniVi is trained on a mixed dataset containing both images and videos, allowing direct application to tasks involving both mediums without requiring any modifications. Extensive experimental results demonstrate that Chat-UniVi consistently outperforms even existing methods exclusively designed for either images or videos. Code is available at https://github.com/PKU-YuanGroup/Chat-UniVi.

</details>

### TIM: A Time Interval Machine for Audio-Visual Action Recognition.
- **链接**: [arXiv:2404.05559](https://arxiv.org/abs/2404.05559) · 📚 被引 29
- **作者**: Jacob Chalk, Jaesung Huh, Evangelos Kazakos, Andrew Zisserman, Dima Damen
- **🏷️ 机构**: University of Bristol, University of Oxford,VGG, Czech Technical University in Prague
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diverse actions give rise to rich audio-visual signals in long videos. Recent works showcase that the two modalities of audio and video exhibit different temporal extents of events and distinct labels. We address the interplay between the two modalities in long videos by explicitly modelling the temporal extents of audio and visual events. We propose the Time Interval Machine (TIM) where a modality-specific time interval poses as a query to a transformer encoder that ingests a long video input. The encoder then attends to the specified interval, as well as the surrounding context in both modalities, in order to recognise the ongoing action. We test TIM on three long audio-visual video datasets: EPIC-KITCHENS, Perception Test, and AVE, reporting state-of-the-art (SOTA) for recognition. On EPIC-KITCHENS, we beat previous SOTA that utilises LLMs and significantly larger pre-training by 2.9% top-1 action recognition accuracy. Additionally, we show that TIM can be adapted for action detection, using dense multi-scale interval queries, outperforming SOTA on EPIC-KITCHENS-100 for most metrics, and showing strong performance on the Perception Test. Our ablations show the critical role of integrating the two modalities and modelling their time intervals in achieving this performance. Code and models at: https://github.com/JacobChalk/TIM

</details>

### C2KD: Bridging the Modality Gap for Cross-Modal Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01515)
- **作者**: Fushuo Huo, Wenchao Xu, Jingcai Guo, Haozhao Wang, Song Guo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While conversational generative AI has shown considerable potential in enhancing decision-making for agricultural professionals, its exploration has predominantly been anchored in text-based interactions. The evolution of multimodal conversational AI, leveraging vast amounts of image-text data from diverse sources, marks a significant stride forward. However, the application of such advanced vision-language models in the agricultural domain, particularly for crop disease diagnosis, remains underexplored. In this work, we present the crop disease domain multimodal (CDDM) dataset, a pioneering resource designed to advance the field of agricultural research through the application of multimodal learning techniques. The dataset comprises 137,000 images of various crop diseases, accompanied by 1 million question-answer pairs that span a broad spectrum of agricultural knowledge, from disease identification to management practices. By integrating visual and textual data, CDDM facilitates the development of sophisticated question-answering systems capable of providing precise, useful advice to farmers and agricultural professionals. We demonstrate the utility of the dataset by finetuning state-of-the-art multimodal models, showcasing significant improvements in crop disease diagnosis. Specifically, we employed a novel finetuning strategy that utilizes low-rank adaptation (LoRA) to finetune the visual encoder, adapter and language model simultaneously. Our contributions include not only the dataset but also a finetuning strategy and a benchmark to stimulate further research in agricultural technology, aiming to bridge the gap between advanced AI techniques and practical agricultural applications. The dataset is available at https: //github.com/UnicomAI/UnicomBenchmark/tree/main/CDDMBench.

</details>

### MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_22) · 📚 被引 50
- **作者**: Xin Liu, Yichen Zhu, Jindong Gu, Yunshi Lan, Chao Yang, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2024

### PathMMU: A Massive Multimodal Expert-Level Benchmark for Understanding and Reasoning in Pathology.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73033-7_4) · 📚 被引 12
- **作者**: Yuxuan Sun, Hao Wu, Chenglu Zhu, Sunyi Zheng, Qizi Chen, Kai Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### TrafficNight: An Aerial Multimodal Benchmark for Nighttime Vehicle Surveillance.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73650-6_3) · 📚 被引 3
- **作者**: Guoxing Zhang, Yiming Liu, Xiaoyu Yang, Hailong Huang, Chao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Explicitly Guided Information Interaction Network for Cross-Modal Point Cloud Completion.
- **链接**: [arXiv:2407.02887](https://arxiv.org/abs/2407.02887) · [代码](https://github.com/WHU-USI3DV/EGIInet) · 📚 被引 14
- **作者**: Hang Xu, Chen Long, Wenxiao Zhang, Yuan Liu, Zhen Cao, Zhen Dong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we explore a novel framework, EGIInet (Explicitly Guided Information Interaction Network), a model for View-guided Point cloud Completion (ViPC) task, which aims to restore a complete point cloud from a partial one with a single view image. In comparison with previous methods that relied on the global semantics of input images, EGIInet efficiently combines the information from two modalities by leveraging the geometric nature of the completion task. Specifically, we propose an explicitly guided information interaction strategy supported by modal alignment for point cloud completion. First, in contrast to previous methods which simply use 2D and 3D backbones to encode features respectively, we unified the encoding process to promote modal alignment. Second, we propose a novel explicitly guided information interaction strategy that could help the network identify critical information within images, thus achieving better guidance for completion. Extensive experiments demonstrate the effectiveness of our framework, and we achieved a new state-of-the-art (+16% CD over XMFnet) in benchmark datasets despite using fewer parameters than the previous methods. The pre-trained model and code and are available at https://github.com/WHU-USI3DV/EGIInet.

</details>

### Exploring Conditional Multi-modal Prompts for Zero-Shot HOI Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73007-8_1) · 📚 被引 18
- **作者**: Ting Lei, Shaofeng Yin, Yuxin Peng, Yang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### E3M: Zero-Shot Spatio-Temporal Video Grounding with Expectation-Maximization Multimodal Modulation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73010-8_14)
- **作者**: Peijun Bao, Zihao Shao, Wenhan Yang, Boon Poh Ng, Alex C. Kot
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### BenchLMM: Benchmarking Cross-Style Visual Capability of Large Multimodal Models.
- **链接**: [arXiv:2312.02896](https://arxiv.org/abs/2312.02896) · 📚 被引 10
- **作者**: Rizhao Cai, Zirui Song, Dayan Guan, Zhenhao Chen, Yaohang Li, Xing Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) such as GPT-4V and LLaVA have shown remarkable capabilities in visual reasoning with common image styles. However, their robustness against diverse style shifts, crucial for practical applications, remains largely unexplored. In this paper, we propose a new benchmark, BenchLMM, to assess the robustness of LMMs against three different styles: artistic image style, imaging sensor style, and application style, where each style has five sub-styles. Utilizing BenchLMM, we comprehensively evaluate state-of-the-art LMMs and reveal: 1) LMMs generally suffer performance degradation when working with other styles; 2) An LMM performs better than another model in common style does not guarantee its superior performance in other styles; 3) LMMs' reasoning capability can be enhanced by prompting LMMs to predict the style first, based on which we propose a versatile and training-free method for improving LMMs; 4) An intelligent LMM is expected to interpret the causes of its errors when facing stylistic variations. We hope that our benchmark and analysis can shed new light on developing more intelligent and versatile LMMs.

</details>

### MultiDelete for Multimodal Machine Unlearning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72940-9_10) · 📚 被引 4
- **作者**: Jiali Cheng, Hadi Amiri
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Towards Multimodal Open-Set Domain Generalization and Adaptation Through Self-supervision.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73202-7_16) · 📚 被引 10
- **作者**: Hao Dong, Eleni N. Chatzi, Olga Fink
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data.
- **链接**: [arXiv:2407.07582](https://arxiv.org/abs/2407.07582) · [代码](https://github.com/siyi-wind/TIP) · 📚 被引 16
- **作者**: Siyi Du, Shaoming Zheng, Yinsong Wang, Wenjia Bai, Declan P. O'Regan, Chen Qin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Images and structured tables are essential parts of real-world databases. Though tabular-image representation learning is promising to create new insights, it remains a challenging task, as tabular data is typically heterogeneous and incomplete, presenting significant modality disparities with images. Earlier works have mainly focused on simple modality fusion strategies in complete data scenarios, without considering the missing data issue, and thus are limited in practice. In this paper, we propose TIP, a novel tabular-image pre-training framework for learning multimodal representations robust to incomplete tabular data. Specifically, TIP investigates a novel self-supervised learning (SSL) strategy, including a masked tabular reconstruction task for tackling data missingness, and image-tabular matching and contrastive learning objectives to capture multimodal information. Moreover, TIP proposes a versatile tabular encoder tailored for incomplete, heterogeneous tabular data and a multimodal interaction module for inter-modality representation learning. Experiments are performed on downstream multimodal classification tasks using both natural and medical image datasets. The results show that TIP outperforms state-of-the-art supervised/SSL image/multimodal algorithms in both complete and incomplete data scenarios. Our code is available at https://github.com/siyi-wind/TIP.

</details>

### 🤖 VideoAgent: A Memory-Augmented Multimodal Agent for Video Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72670-5_5)
- **作者**: Yue Fan, Xiaojian Ma, Rujie Wu, Yuntao Du, Jiaqi Li, Zhi Gao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### BLINK: Multimodal Large Language Models Can See but Not Perceive.
- **链接**: [arXiv:2404.12390](https://arxiv.org/abs/2404.12390) · 📚 被引 60
- **作者**: Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Blink, a new benchmark for multimodal language models (LLMs) that focuses on core visual perception abilities not found in other evaluations. Most of the Blink tasks can be solved by humans "within a blink" (e.g., relative depth estimation, visual correspondence, forensics detection, and multi-view reasoning). However, we find these perception-demanding tasks cast significant challenges for current multimodal LLMs because they resist mediation through natural language. Blink reformats 14 classic computer vision tasks into 3,807 multiple-choice questions, paired with single or multiple images and visual prompting. While humans get 95.70% accuracy on average, Blink is surprisingly challenging for existing multimodal LLMs: even the best-performing GPT-4V and Gemini achieve accuracies of 51.26% and 45.72%, only 13.17% and 7.63% higher than random guessing, indicating that such perception abilities have not "emerged" yet in recent multimodal LLMs. Our analysis also highlights that specialist CV models could solve these problems much better, suggesting potential pathways for future improvements. We believe Blink will stimulate the community to help multimodal LLMs catch up with human-level visual perception.

</details>

### Dissecting Dissonance: Benchmarking Large Multimodal Models Against Self-Contradictory Instructions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72998-0_23) · 📚 被引 0
- **作者**: Jin Gao, Lei Gan, Yuankai Li, Yixin Ye, Dequan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Eyes Closed, Safety on: Protecting Multimodal LLMs via Image-to-Text Transformation.
- **链接**: [arXiv:2403.09572](https://arxiv.org/abs/2403.09572) · 📚 被引 12
- **作者**: Yunhao Gou, Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have shown impressive reasoning abilities. However, they are also more vulnerable to jailbreak attacks than their LLM predecessors. Although still capable of detecting the unsafe responses, we observe that safety mechanisms of the pre-aligned LLMs in MLLMs can be easily bypassed with the introduction of image features. To construct robust MLLMs, we propose ECSO (Eyes Closed, Safety On), a novel training-free protecting approach that exploits the inherent safety awareness of MLLMs, and generates safer responses via adaptively transforming unsafe images into texts to activate the intrinsic safety mechanism of pre-aligned LLMs in MLLMs. Experiments on five state-of-the-art (SoTA) MLLMs demonstrate that ECSO enhances model safety significantly (e.g.,, 37.6% improvement on the MM-SafetyBench (SD+OCR) and 71.3% on VLSafe with LLaVA-1.5-7B), while consistently maintaining utility results on common MLLM benchmarks. Furthermore, we show that ECSO can be used as a data engine to generate supervised-finetuning (SFT) data for MLLM alignment without extra human intervention.

</details>

### Multimodal Label Relevance Ranking via Reinforcement Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72848-8_23) · 📚 被引 1
- **作者**: Taian Guo, Taolin Zhang, Haoqian Wu, Hanjun Li, Ruizhi Qiao, Xing Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Multimodal Cross-Domain Few-Shot Learning for Egocentric Action Recognition.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73414-4_11)
- **作者**: Masashi Hatano, Ryo Hachiuma, Ryo Fujii, Hideo Saito
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MotionChain: Conversational Motion Controllers via Multimodal Prompts.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73347-5_4) · 📚 被引 12
- **作者**: Biao Jiang, Xin Chen, Chi Zhang, Fukun Yin, Zhuoyuan Li, Gang Yu et al.
- **🏷️ 机构**: Tencent
- **会议**: ECCV 2024

### PARIS3D: Reasoning-Based 3D Part Segmentation Using Large Multimodal Model.
- **链接**: [arXiv:2404.03836](https://arxiv.org/abs/2404.03836) · [代码](https://github.com/AmrinKareem/PARIS3D) · 📚 被引 3
- **作者**: Amrin Kareem, Jean Lahoud, Hisham Cholakkal
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in 3D perception systems have significantly improved their ability to perform visual recognition tasks such as segmentation. However, these systems still heavily rely on explicit human instruction to identify target objects or categories, lacking the capability to actively reason and comprehend implicit user intentions. We introduce a novel segmentation task known as reasoning part segmentation for 3D objects, aiming to output a segmentation mask based on complex and implicit textual queries about specific parts of a 3D object. To facilitate evaluation and benchmarking, we present a large 3D dataset comprising over 60k instructions paired with corresponding ground-truth part segmentation annotations specifically curated for reasoning-based 3D part segmentation. We propose a model that is capable of segmenting parts of 3D objects based on implicit textual queries and generating natural language explanations corresponding to 3D object segmentation requests. Experiments show that our method achieves competitive performance to models that use explicit queries, with the additional abilities to identify part concepts, reason about them, and complement them with world knowledge. Our source code, dataset, and trained models are available at https://github.com/AmrinKareem/PARIS3D.

</details>

### Missing Modality Prediction for Unpaired Multimodal Learning via Joint Embedding of Unimodal Models.
- **链接**: [arXiv:2407.12616](https://arxiv.org/abs/2407.12616) · 📚 被引 9
- **作者**: Donggeun Kim, Taesup Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning typically relies on the assumption that all modalities are fully available during both the training and inference phases. However, in real-world scenarios, consistently acquiring complete multimodal data presents significant challenges due to various factors. This often leads to the issue of missing modalities, where data for certain modalities are absent, posing considerable obstacles not only for the availability of multimodal pretrained models but also for their fine-tuning and the preservation of robustness in downstream tasks. To address these challenges, we propose a novel framework integrating parameter-efficient fine-tuning of unimodal pretrained models with a self-supervised joint-embedding learning method. This framework enables the model to predict the embedding of a missing modality in the representation space during inference. Our method effectively predicts the missing embedding through prompt tuning, leveraging information from available modalities. We evaluate our approach on several multimodal benchmark datasets and demonstrate its effectiveness and robustness across various scenarios of missing modalities.

</details>

### Improving Vision and Language Concepts Understanding with Multimodal Counterfactual Samples.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72890-7_11) · 📚 被引 4
- **作者**: Chengen Lai, Shengli Song, Sitong Yan, Guangneng Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models.
- **链接**: [arXiv:2403.09792](https://arxiv.org/abs/2403.09792) · [代码](https://github.com/RUCAIBox/HADES) · 📚 被引 30
- **作者**: Yifan Li, Hangyu Guo, Kun Zhou, Wayne Xin Zhao, Ji-Rong Wen
- **🏷️ 机构**: Renmin University
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study the harmlessness alignment problem of multimodal large language models (MLLMs). We conduct a systematic empirical analysis of the harmlessness performance of representative MLLMs and reveal that the image input poses the alignment vulnerability of MLLMs. Inspired by this, we propose a novel jailbreak method named HADES, which hides and amplifies the harmfulness of the malicious intent within the text input, using meticulously crafted images. Experimental results show that HADES can effectively jailbreak existing MLLMs, which achieves an average Attack Success Rate (ASR) of 90.26% for LLaVA-1.5 and 71.60% for Gemini Pro Vision. Our code and data are available at https://github.com/RUCAIBox/HADES.

</details>

### Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding.
- **链接**: [arXiv:2407.09781](https://arxiv.org/abs/2407.09781) · 📚 被引 5
- **作者**: Ruihuang Li, Zhengqiang Zhang, Chenhang He, Zhiyuan Ma, Vishal M. Patel, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent vision-language pre-training models have exhibited remarkable generalization ability in zero-shot recognition tasks. Previous open-vocabulary 3D scene understanding methods mostly focus on training 3D models using either image or text supervision while neglecting the collective strength of all modalities. In this work, we propose a Dense Multimodal Alignment (DMA) framework to densely co-embed different modalities into a common space for maximizing their synergistic benefits. Instead of extracting coarse view- or region-level text prompts, we leverage large vision-language models to extract complete category information and scalable scene descriptions to build the text modality, and take image modality as the bridge to build dense point-pixel-text associations. Besides, in order to enhance the generalization ability of the 2D model for downstream 3D tasks without compromising the open-vocabulary capability, we employ a dual-path integration approach to combine frozen CLIP visual features and learnable mask features. Extensive experiments show that our DMA method produces highly competitive open-vocabulary segmentation performance on various indoor and outdoor tasks.

</details>

### Learning Video Context as Interleaved Multimodal Sequences.
- **链接**: [arXiv:2407.21757](https://arxiv.org/abs/2407.21757) · [代码](https://github.com/showlab/MovieSeq) · 📚 被引 4
- **作者**: Kevin Qinghong Lin, Pengchuan Zhang, Difei Gao, Xide Xia, Joya Chen, Ziteng Gao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Narrative videos, such as movies, pose significant challenges in video understanding due to their rich contexts (characters, dialogues, storylines) and diverse demands (identify who, relationship, and reason). In this paper, we introduce MovieSeq, a multimodal language model developed to address the wide range of challenges in understanding video contexts. Our core idea is to represent videos as interleaved multimodal sequences (including images, plots, videos, and subtitles), either by linking external knowledge databases or using offline models (such as whisper for subtitles). Through instruction-tuning, this approach empowers the language model to interact with videos using interleaved multimodal instructions. For example, instead of solely relying on video as input, we jointly provide character photos alongside their names and dialogues, allowing the model to associate these elements and generate more comprehensive responses. To demonstrate its effectiveness, we validate MovieSeq's performance on six datasets (LVU, MAD, Movienet, CMD, TVC, MovieQA) across five settings (video classification, audio description, video-text retrieval, video captioning, and video question-answering). The code will be public at https://github.com/showlab/MovieSeq.

</details>

### LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents.
- **链接**: [arXiv:2311.05437](https://arxiv.org/abs/2311.05437) · 📚 被引 44
- **作者**: Shilong Liu, Hao Cheng, Haotian Liu, Hao Zhang, Feng Li, Tianhe Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LLaVA-Plus is a general-purpose multimodal assistant that expands the capabilities of large multimodal models. It maintains a skill repository of pre-trained vision and vision-language models and can activate relevant tools based on users' inputs to fulfill real-world tasks. LLaVA-Plus is trained on multimodal instruction-following data to acquire the ability to use tools, covering visual understanding, generation, external knowledge retrieval, and compositions. Empirical results show that LLaVA-Plus outperforms LLaVA in existing capabilities and exhibits new ones. It is distinct in that the image query is directly grounded and actively engaged throughout the entire human-AI interaction sessions, significantly improving tool use performance and enabling new scenarios.

</details>

### Dolphins: Multimodal Language Model for Driving.
- **链接**: [arXiv:2312.00438](https://arxiv.org/abs/2312.00438) · 📚 被引 46
- **作者**: Yingzi Ma, Yulong Cao, Jiachen Sun, Marco Pavone, Chaowei Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The quest for fully autonomous vehicles (AVs) capable of navigating complex real-world scenarios with human-like understanding and responsiveness. In this paper, we introduce Dolphins, a novel vision-language model architected to imbibe human-like abilities as a conversational driving assistant. Dolphins is adept at processing multimodal inputs comprising video (or image) data, text instructions, and historical control signals to generate informed outputs corresponding to the provided instructions. Building upon the open-sourced pretrained Vision-Language Model, OpenFlamingo, we first enhance Dolphins's reasoning capabilities through an innovative Grounded Chain of Thought (GCoT) process. Then we tailored Dolphins to the driving domain by constructing driving-specific instruction data and conducting instruction tuning. Through the utilization of the BDD-X dataset, we designed and consolidated four distinct AV tasks into Dolphins to foster a holistic understanding of intricate driving scenarios. As a result, the distinctive features of Dolphins are characterized into two dimensions: (1) the ability to provide a comprehensive understanding of complex and long-tailed open-world driving scenarios and solve a spectrum of AV tasks, and (2) the emergence of human-like capabilities including gradient-free instant adaptation via in-context learning and error recovery via reflection.

</details>

### Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models.
- **链接**: [arXiv:2404.13013](https://arxiv.org/abs/2404.13013) · 📚 被引 46
- **作者**: Chuofan Ma, Yi Jiang, Jiannan Wu, Zehuan Yuan, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Groma, a Multimodal Large Language Model (MLLM) with grounded and fine-grained visual perception ability. Beyond holistic image understanding, Groma is adept at region-level tasks such as region captioning and visual grounding. Such capabilities are built upon a localized visual tokenization mechanism, where an image input is decomposed into regions of interest and subsequently encoded into region tokens. By integrating region tokens into user instructions and model responses, we seamlessly enable Groma to understand user-specified region inputs and ground its textual output to images. Besides, to enhance the grounded chat ability of Groma, we curate a visually grounded instruction dataset by leveraging the powerful GPT-4V and visual prompting techniques. Compared with MLLMs that rely on the language model or external module for localization, Groma consistently demonstrates superior performances in standard referring and grounding benchmarks, highlighting the advantages of embedding localization into image tokenization. Project page: https://groma-mllm.github.io/.

</details>

### Nymeria: A Massive Collection of Multimodal Egocentric Daily Motion in the Wild.
- **链接**: [arXiv:2406.09905](https://arxiv.org/abs/2406.09905) · 📚 被引 29
- **作者**: Lingni Ma, Yuting Ye, Fangzhou Hong, Vladimir Guzov, Yifeng Jiang, Rowan Postyeni et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Nymeria - a large-scale, diverse, richly annotated human motion dataset collected in the wild with multiple multimodal egocentric devices. The dataset comes with a) full-body ground-truth motion; b) multiple multimodal egocentric data from Project Aria devices with videos, eye tracking, IMUs and etc; and c) a third-person perspective by an additional observer. All devices are precisely synchronized and localized in on metric 3D world. We derive hierarchical protocol to add in-context language descriptions of human motion, from fine-grain motion narration, to simplified atomic action and high-level activity summarization. To the best of our knowledge, Nymeria dataset is the world's largest collection of human motion in the wild; first of its kind to provide synchronized and localized multi-device multimodal egocentric data; and the world's largest motion-language dataset. It provides 300 hours of daily activities from 264 participants across 50 locations, total travelling distance over 399Km. The language descriptions contain 301.5K sentences in 8.64M words from a vocabulary size of 6545. To demonstrate the potential of the dataset, we evaluate several SOTA algorithms for egocentric body tracking, motion synthesis, and action recognition. Data and code are open-sourced for research (c.f. https://www.projectaria.com/datasets/nymeria).

</details>

### MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73397-0_18) · 📚 被引 80
- **作者**: Brandon McKinzie, Zhe Gan, Jean-Philippe Fauconnier, Sam Dodge, Bowen Zhang, Philipp Dufter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Object-Oriented Anchoring and Modal Alignment in Multimodal Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72973-7_11) · 📚 被引 0
- **作者**: Shibin Mei, Bingbing Ni, Hang Wang, Chenglong Zhao, Fengfa Hu, Zhiming Pi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### LHRS-Bot: Empowering Remote Sensing with VGI-Enhanced Large Multimodal Language Model.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72904-1_26) · 📚 被引 75
- **作者**: Dilxat Muhtar, Zhenshi Li, Feng Gu, Xueliang Zhang, Pengfeng Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Strengthening Multimodal Large Language Model with Bootstrapped Preference Optimization.
- **链接**: [arXiv:2403.08730](https://arxiv.org/abs/2403.08730) · 📚 被引 14
- **作者**: Renjie Pi, Tianyang Han, Wei Xiong, Jipeng Zhang, Runtao Liu, Rui Pan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) excel in generating responses based on visual inputs. However, they often suffer from a bias towards generating responses similar to their pretraining corpus, overshadowing the importance of visual information. We treat this bias as a "preference" for pretraining statistics, which hinders the model's grounding in visual input. To mitigate this issue, we propose Bootstrapped Preference Optimization (BPO), which conducts preference learning with datasets containing negative responses bootstrapped from the model itself. Specifically, we propose the following two strategies: 1) using distorted image inputs to the MLLM for eliciting responses that contain signified pretraining bias; 2) leveraging text-based LLM to explicitly inject erroneous but common elements into the original response. Those undesirable responses are paired with original annotated responses from the datasets to construct the preference dataset, which is subsequently utilized to perform preference learning. Our approach effectively suppresses pretrained LLM bias, enabling enhanced grounding in visual inputs. Extensive experimentation demonstrates significant performance improvements across multiple benchmarks, advancing the state-of-the-art in multimodal conversational systems.

</details>

### Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning.
- **链接**: [arXiv:2407.04207](https://arxiv.org/abs/2407.04207)
- **作者**: Mainak Singha, Ankit Jha, Divyam Gupta, Pranav Singla, Biplab Banerjee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the challenges inherent in sketch-based image retrieval (SBIR) across various settings, including zero-shot SBIR, generalized zero-shot SBIR, and fine-grained zero-shot SBIR, by leveraging the vision-language foundation model CLIP. While recent endeavors have employed CLIP to enhance SBIR, these approaches predominantly follow uni-modal prompt processing and overlook to exploit CLIP's integrated visual and textual capabilities fully. To bridge this gap, we introduce SpLIP, a novel multi-modal prompt learning scheme designed to operate effectively with frozen CLIP backbones. We diverge from existing multi-modal prompting methods that treat visual and textual prompts independently or integrate them in a limited fashion, leading to suboptimal generalization. SpLIP implements a bi-directional prompt-sharing strategy that enables mutual knowledge exchange between CLIP's visual and textual encoders, fostering a more cohesive and synergistic prompt processing mechanism that significantly reduces the semantic gap between the sketch and photo embeddings. In addition to pioneering multi-modal prompt learning, we propose two innovative strategies for further refining the embedding space. The first is an adaptive margin generation for the sketch-photo triplet loss, regulated by CLIP's class textual embeddings. The second introduces a novel task, termed conditional cross-modal jigsaw, aimed at enhancing fine-grained sketch-photo alignment by implicitly modeling sketches' viable patch arrangement using knowledge of unshuffled photos. Our comprehensive experimental evaluations across multiple benchmarks demonstrate the superior performance of SpLIP in all three SBIR scenarios. Project page: https://mainaksingha01.github.io/SpLIP/ .

</details>

### MoMA: Multimodal LLM Adapter for Fast Personalized Image Generation.
- **链接**: [arXiv:2404.05674](https://arxiv.org/abs/2404.05674) · 📚 被引 20
- **作者**: Kunpeng Song, Yizhe Zhu, Bingchen Liu, Qing Yan, Ahmed Elgammal, Xiao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present MoMA: an open-vocabulary, training-free personalized image model that boasts flexible zero-shot capabilities. As foundational text-to-image models rapidly evolve, the demand for robust image-to-image translation grows. Addressing this need, MoMA specializes in subject-driven personalized image generation. Utilizing an open-source, Multimodal Large Language Model (MLLM), we train MoMA to serve a dual role as both a feature extractor and a generator. This approach effectively synergizes reference image and text prompt information to produce valuable image features, facilitating an image diffusion model. To better leverage the generated features, we further introduce a novel self-attention shortcut method that efficiently transfers image features to an image diffusion model, improving the resemblance of the target object in generated images. Remarkably, as a tuning-free plug-and-play module, our model requires only a single reference image and outperforms existing methods in generating images with high detail fidelity, enhanced identity-preservation and prompt faithfulness. Our work is open-source, thereby providing universal access to these advancements.

</details>

### Boosting the Power of Small Multimodal Reasoning Models to Match Larger Models with Self-consistency Training.
- **链接**: [arXiv:2311.14109](https://arxiv.org/abs/2311.14109) · [代码](https://github.com/chengtan9907/mc-cot) · 📚 被引 14
- **作者**: Cheng Tan, Jingxuan Wei, Zhangyang Gao, Linzhuang Sun, Siyuan Li, Ruifeng Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal reasoning is a challenging task that requires models to reason across multiple modalities to answer questions. Existing approaches have made progress by incorporating language and visual modalities into a two-stage reasoning framework, separating rationale generation from answer inference. However, these approaches often fall short due to the inadequate quality of the generated rationales. In this work, we delve into the importance of rationales in model reasoning. We observe that when rationales are completely accurate, the model's accuracy significantly improves, highlighting the need for high-quality rationale generation. Motivated by this, we propose MC-CoT, a self-consistency training strategy that generates multiple rationales and answers, subsequently selecting the most accurate through a voting process. This approach not only enhances the quality of generated rationales but also leads to more accurate and robust answers. Through extensive experiments, we demonstrate that our approach significantly improves model performance across various benchmarks. Remarkably, we show that even smaller base models, when equipped with our proposed approach, can achieve results comparable to those of larger models, illustrating the potential of our approach in harnessing the power of rationales for improved multimodal reasoning. The code is available at https://github.com/chengtan9907/mc-cot.

</details>

### Decoupling Common and Unique Representations for Multimodal Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73397-0_17) · 📚 被引 46
- **作者**: Yi Wang, Conrad M. Albrecht, Nassim Ait Ali Braham, Chenying Liu, Zhitong Xiong, Xiao Xiang Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning.
- **链接**: [arXiv:2407.15680](https://arxiv.org/abs/2407.15680) · 📚 被引 11
- **作者**: Zhecan Wang, Garrett Bingham, Adams Wei Yu, Quoc V. Le, Thang Luong, Golnaz Ghiasi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucination has been a major problem for large language models and remains a critical challenge when it comes to multimodality in which vision-language models (VLMs) have to deal with not just textual but also visual inputs. Despite rapid progress in VLMs, resources for evaluating and addressing multimodal hallucination are limited and mostly focused on evaluation. This work introduces HaloQuest, a novel visual question answering dataset that captures various aspects of multimodal hallucination such as false premises, insufficient contexts, and visual challenges. A novel idea from HaloQuest is to leverage synthetic images, apart from real ones, to enable dataset creation at scale. With over 7.7K examples spanning across a wide variety of categories, HaloQuest was designed to be both a challenging benchmark for VLMs and a fine-tuning dataset for advancing multimodal reasoning. Our experiments reveal that current models struggle with HaloQuest, with all open-source VLMs achieving below 36% accuracy. On the other hand, fine-tuning on HaloQuest significantly reduces hallucination rates while preserving performance on standard reasoning tasks. Our results discover that benchmarking with generated images is highly correlated (r=0.97) with real images. Last but not least, we propose a novel Auto-Eval mechanism that is highly correlated with human raters (r=0.99) for evaluating VLMs. In sum, this work makes concrete strides towards understanding, evaluating, and mitigating hallucination in VLMs, serving as an important step towards more reliable multimodal AI systems in the future.

</details>

### Instruction Tuning-Free Visual Token Complement for Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73004-7_26) · 📚 被引 3
- **作者**: Dongsheng Wang, Jiequan Cui, Miaoge Li, Wang Lin, Bo Chen, Hanwang Zhang
- **🏷️ 机构**: NUS
- **会议**: ECCV 2024

### AdaShield : Safeguarding Multimodal Large Language Models from Structure-Based Attack via Adaptive Shield Prompting.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72661-3_5) · 📚 被引 15
- **作者**: Yu Wang, Xiaogeng Liu, Yu Li, Muhao Chen, Chaowei Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### InternVideo2: Scaling Foundation Models for Multimodal Video Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73013-9_23)
- **作者**: Yi Wang, Kunchang Li, Xinhao Li, Jiashuo Yu, Yinan He, Guo Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### UniIR: Training and Benchmarking Universal Multimodal Information Retrievers.
- **链接**: [arXiv:2311.17136](https://arxiv.org/abs/2311.17136) · 📚 被引 26
- **作者**: Cong Wei, Yang Chen, Haonan Chen, Hexiang Hu, Ge Zhang, Jie Fu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing information retrieval (IR) models often assume a homogeneous format, limiting their applicability to diverse user needs, such as searching for images with text descriptions, searching for a news article with a headline image, or finding a similar photo with a query image. To approach such different information-seeking demands, we introduce UniIR, a unified instruction-guided multimodal retriever capable of handling eight distinct retrieval tasks across modalities. UniIR, a single retrieval system jointly trained on ten diverse multimodal-IR datasets, interprets user instructions to execute various retrieval tasks, demonstrating robust performance across existing datasets and zero-shot generalization to new tasks. Our experiments highlight that multi-task training and instruction tuning are keys to UniIR's generalization ability. Additionally, we construct the M-BEIR, a multimodal retrieval benchmark with comprehensive results, to standardize the evaluation of universal multimodal information retrieval.

</details>

### Diagnosing and Re-learning for Balanced Multimodal Learning.
- **链接**: [arXiv:2407.09705](https://arxiv.org/abs/2407.09705) · [代码](https://github.com/GeWu-Lab/Diagnosing_Relearning_ECCV2024) · 📚 被引 24
- **作者**: Yake Wei, Siwei Li, Ruoxuan Feng, Di Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To overcome the imbalanced multimodal learning problem, where models prefer the training of specific modalities, existing methods propose to control the training of uni-modal encoders from different perspectives, taking the inter-modal performance discrepancy as the basis. However, the intrinsic limitation of modality capacity is ignored. The scarcely informative modalities can be recognized as ``worse-learnt'' ones, which could force the model to memorize more noise, counterproductively affecting the multimodal model ability. Moreover, the current modality modulation methods narrowly concentrate on selected worse-learnt modalities, even suppressing the training of others. Hence, it is essential to consider the intrinsic limitation of modality capacity and take all modalities into account during balancing. To this end, we propose the Diagnosing \& Re-learning method. The learning state of each modality is firstly estimated based on the separability of its uni-modal representation space, and then used to softly re-initialize the corresponding uni-modal encoder. In this way, the over-emphasizing of scarcely informative modalities is avoided. In addition, encoders of worse-learnt modalities are enhanced, simultaneously avoiding the over-training of other modalities. Accordingly, multimodal learning is effectively balanced and enhanced. Experiments covering multiple types of modalities and multimodal frameworks demonstrate the superior performance of our simple-yet-effective method for balanced multimodal learning. The source code and dataset are available at \url{https://github.com/GeWu-Lab/Diagnosing_Relearning_ECCV2024}.

</details>

### Robust Multimodal Learning via Representation Decoupling.
- **链接**: [arXiv:2407.04458](https://arxiv.org/abs/2407.04458)
- **作者**: Shicai Wei, Yang Luo, Yuji Wang, Chunbo Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning robust to missing modality has attracted increasing attention due to its practicality. Existing methods tend to address it by learning a common subspace representation for different modality combinations. However, we reveal that they are sub-optimal due to their implicit constraint on intra-class representation. Specifically, the sample with different modalities within the same class will be forced to learn representations in the same direction. This hinders the model from capturing modality-specific information, resulting in insufficient learning. To this end, we propose a novel Decoupled Multimodal Representation Network (DMRNet) to assist robust multimodal learning. Specifically, DMRNet models the input from different modality combinations as a probabilistic distribution instead of a fixed point in the latent space, and samples embeddings from the distribution for the prediction module to calculate the task loss. As a result, the direction constraint from the loss minimization is blocked by the sampled representation. This relaxes the constraint on the inference representation and enables the model to capture the specific information for different modality combinations. Furthermore, we introduce a hard combination regularizer to prevent DMRNet from unbalanced training by guiding it to pay more attention to hard modality combinations. Finally, extensive experiments on multimodal classification and segmentation tasks demonstrate that the proposed DMRNet outperforms the state-of-the-art significantly.

</details>

### A Comprehensive Study of Multimodal Large Language Models for Image Quality Assessment.
- **链接**: [arXiv:2403.10854](https://arxiv.org/abs/2403.10854)
- **作者**: Tianhe Wu, Kede Ma, Jie Liang, Yujiu Yang, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Multimodal Large Language Models (MLLMs) have experienced significant advancement in visual understanding and reasoning, their potential to serve as powerful, flexible, interpretable, and text-driven models for Image Quality Assessment (IQA) remains largely unexplored. In this paper, we conduct a comprehensive and systematic study of prompting MLLMs for IQA. We first investigate nine prompting systems for MLLMs as the combinations of three standardized testing procedures in psychophysics (i.e., the single-stimulus, double-stimulus, and multiple-stimulus methods) and three popular prompting strategies in natural language processing (i.e., the standard, in-context, and chain-of-thought prompting). We then present a difficult sample selection procedure, taking into account sample diversity and uncertainty, to further challenge MLLMs equipped with the respective optimal prompting systems. We assess three open-source and one closed-source MLLMs on several visual attributes of image quality (e.g., structural and textural distortions, geometric transformations, and color differences) in both full-reference and no-reference scenarios. Experimental results show that only the closed-source GPT-4V provides a reasonable account for human perception of image quality, but is weak at discriminating fine-grained quality variations (e.g., color differences) and at comparing visual quality of multiple images, tasks humans can perform effortlessly.

</details>

### UMBRAE: Unified Multimodal Brain Decoding.
- **链接**: [arXiv:2404.07202](https://arxiv.org/abs/2404.07202) · 📚 被引 17
- **作者**: Weihao Xia, Raoul de Charette, A. Cengiz Öztireli, Jing-Hao Xue
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address prevailing challenges of the brain-powered research, departing from the observation that the literature hardly recover accurate spatial information and require subject-specific models. To address these challenges, we propose UMBRAE, a unified multimodal decoding of brain signals. First, to extract instance-level conceptual and spatial details from neural signals, we introduce an efficient universal brain encoder for multimodal-brain alignment and recover object descriptions at multiple levels of granularity from subsequent multimodal large language model (MLLM). Second, we introduce a cross-subject training strategy mapping subject-specific features to a common feature space. This allows a model to be trained on multiple subjects without extra resources, even yielding superior results compared to subject-specific models. Further, we demonstrate this supports weakly-supervised adaptation to new subjects, with only a fraction of the total training data. Experiments demonstrate that UMBRAE not only achieves superior results in the newly introduced tasks but also outperforms methods in well established tasks. To assess our method, we construct and share with the community a comprehensive brain understanding benchmark BrainHub. Our code and benchmark are available at https://weihaox.github.io/UMBRAE.

</details>

### LLMGA: Multimodal Large Language Model Based Generation Assistant.
- **链接**: [arXiv:2311.16500](https://arxiv.org/abs/2311.16500) · 📚 被引 10
- **作者**: Bin Xia, Shiyin Wang, Yingfan Tao, Yitong Wang, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce a Multimodal Large Language Model-based Generation Assistant (LLMGA), leveraging the vast reservoir of knowledge and proficiency in reasoning, comprehension, and response inherent in Large Language Models (LLMs) to assist users in image generation and editing. Diverging from existing approaches where Multimodal Large Language Models (MLLMs) generate fixed-size embeddings to control Stable Diffusion (SD), our LLMGA provides a detailed language generation prompt for precise control over SD. This not only augments LLM context understanding but also reduces noise in generation prompts, yields images with more intricate and precise content, and elevates the interpretability of the network. To this end, we curate a comprehensive dataset comprising prompt refinement, similar image generation, inpainting \& outpainting, and instruction-based editing. Moreover, we propose a two-stage training scheme. In the first stage, we train the MLLM to grasp the properties of image generation and editing, enabling it to generate detailed prompts. In the second stage, we optimize SD to align with the MLLM's generation prompts. Additionally, we propose a reference-based restoration network to alleviate texture, brightness, and contrast disparities between generated and preserved regions during inpainting and outpainting. Extensive results show that LLMGA has promising generation and editing capabilities and can enable more flexible and expansive applications in an interactive manner.

</details>

### Towards Multimodal Sentiment Analysis Debiasing via Bias Purification.
- **链接**: [arXiv:2403.05023](https://arxiv.org/abs/2403.05023) · 📚 被引 20
- **作者**: Dingkang Yang, Mingcheng Li, Dongling Xiao, Yang Liu, Kun Yang, Zhaoyu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Sentiment Analysis (MSA) aims to understand human intentions by integrating emotion-related clues from diverse modalities, such as visual, language, and audio. Unfortunately, the current MSA task invariably suffers from unplanned dataset biases, particularly multimodal utterance-level label bias and word-level context bias. These harmful biases potentially mislead models to focus on statistical shortcuts and spurious correlations, causing severe performance bottlenecks. To alleviate these issues, we present a Multimodal Counterfactual Inference Sentiment (MCIS) analysis framework based on causality rather than conventional likelihood. Concretely, we first formulate a causal graph to discover harmful biases from already-trained vanilla models. In the inference phase, given a factual multimodal input, MCIS imagines two counterfactual scenarios to purify and mitigate these biases. Then, MCIS can make unbiased decisions from biased observations by comparing factual and counterfactual outcomes. We conduct extensive experiments on several standard MSA benchmarks. Qualitative and quantitative results show the effectiveness of the proposed framework.

</details>

### CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios.
- **链接**: [arXiv:2403.04640](https://arxiv.org/abs/2403.04640) · [代码](https://github.com/rikeilong/Bay-CAT) · 📚 被引 20
- **作者**: Qilang Ye, Zitong Yu, Rui Shao, Xinyu Xie, Philip Torr, Xiaochun Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on the challenge of answering questions in scenarios that are composed of rich and complex dynamic audio-visual components. Although existing Multimodal Large Language Models (MLLMs) can respond to audio-visual content, these responses are sometimes ambiguous and fail to describe specific audio-visual events. To overcome this limitation, we introduce the CAT, which enhances MLLM in three ways: 1) besides straightforwardly bridging audio and video, we design a clue aggregator that aggregates question-related clues in dynamic audio-visual scenarios to enrich the detailed knowledge required for large language models. 2) CAT is trained on a mixed multimodal dataset, allowing direct application in audio-visual scenarios. Notably, we collect an audio-visual joint instruction dataset named AVinstruct, to further enhance the capacity of CAT to model cross-semantic correlations. 3) we propose AI-assisted ambiguity-aware direct preference optimization, a strategy specialized in retraining the model to favor the non-ambiguity response and improve the ability to localize specific audio-visual objects. Extensive experimental results demonstrate that CAT outperforms existing methods on multimodal tasks, especially in Audio-Visual Question Answering (AVQA) tasks. The codes and the collected instructions are released at https://github.com/rikeilong/Bay-CAT.

</details>

### BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation.
- **链接**: [arXiv:2408.05926](https://arxiv.org/abs/2408.05926) · 📚 被引 0
- **作者**: Hee Suk Yoon, Eunseop Yoon, Joshua Tian Jin Tee, Kang Zhang, Yu-Jung Heo, Du-Seong Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Dialogue Response Generation (MDRG) is a recently proposed task where the model needs to generate responses in texts, images, or a blend of both based on the dialogue context. Due to the lack of a large-scale dataset specifically for this task and the benefits of leveraging powerful pre-trained models, previous work relies on the text modality as an intermediary step for both the image input and output of the model rather than adopting an end-to-end approach. However, this approach can overlook crucial information about the image, hindering 1) image-grounded text response and 2) consistency of objects in the image response. In this paper, we propose BI-MDRG that bridges the response generation path such that the image history information is utilized for enhanced relevance of text responses to the image content and the consistency of objects in sequential image responses. Through extensive experiments on the multimodal dialogue benchmark dataset, we show that BI-MDRG can effectively increase the quality of multimodal dialogue. Additionally, recognizing the gap in benchmark datasets for evaluating the image consistency in multimodal dialogue, we have created a curated set of 300 dialogues annotated to track object consistency across conversations.

</details>

### Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73039-9_14) · 📚 被引 38
- **作者**: Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeffrey Nichols et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer.
- **链接**: [arXiv:2212.09877](https://arxiv.org/abs/2212.09877) · [代码](https://github.com/salesforce/LayoutDETR) · 📚 被引 8
- **作者**: Ning Yu, Chia-Chih Chen, Zeyuan Chen, Rui Meng, Gang Wu, Paul Josel et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graphic layout designs play an essential role in visual communication. Yet handcrafting layout designs is skill-demanding, time-consuming, and non-scalable to batch production. Generative models emerge to make design automation scalable but it remains non-trivial to produce designs that comply with designers' multimodal desires, i.e., constrained by background images and driven by foreground content. We propose LayoutDETR that inherits the high quality and realism from generative modeling, while reformulating content-aware requirements as a detection problem: we learn to detect in a background image the reasonable locations, scales, and spatial relations for multimodal foreground elements in a layout. Our solution sets a new state-of-the-art performance for layout generation on public benchmarks and on our newly-curated ad banner dataset. We integrate our solution into a graphical system that facilitates user studies, and show that users prefer our designs over baselines by significant margins. Code, models, dataset, and demos are available at https://github.com/salesforce/LayoutDETR.

</details>

### Merlin: Empowering Multimodal LLMs with Foresight Minds.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73235-5_24) · 📚 被引 14
- **作者**: En Yu, Liang Zhao, Yana Wei, Jinrong Yang, Dongming Wu, Lingyu Kong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning Multimodal Latent Generative Models with Energy-Based Prior.
- **链接**: [arXiv:2409.19862](https://arxiv.org/abs/2409.19862) · 📚 被引 0
- **作者**: Shiyu Yuan, Jiali Cui, Hanao Li, Tian Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal generative models have recently gained significant attention for their ability to learn representations across various modalities, enhancing joint and cross-generation coherence. However, most existing works use standard Gaussian or Laplacian distributions as priors, which may struggle to capture the diverse information inherent in multiple data types due to their unimodal and less informative nature. Energy-based models (EBMs), known for their expressiveness and flexibility across various tasks, have yet to be thoroughly explored in the context of multimodal generative models. In this paper, we propose a novel framework that integrates the multimodal latent generative model with the EBM. Both models can be trained jointly through a variational scheme. This approach results in a more expressive and informative prior, better-capturing of information across multiple modalities. Our experiments validate the proposed model, demonstrating its superior generation coherence.

</details>

### FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models.
- **链接**: [arXiv:2406.10740](https://arxiv.org/abs/2406.10740) · 📚 被引 4
- **作者**: Zhikai Zhang, Yitang Li, Haofeng Huang, Mingxian Lin, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human motion synthesis is a fundamental task in computer animation. Despite recent progress in this field utilizing deep learning and motion capture data, existing methods are always limited to specific motion categories, environments, and styles. This poor generalizability can be partially attributed to the difficulty and expense of collecting large-scale and high-quality motion data. At the same time, foundation models trained with internet-scale image and text data have demonstrated surprising world knowledge and reasoning ability for various downstream tasks. Utilizing these foundation models may help with human motion synthesis, which some recent works have superficially explored. However, these methods didn't fully unveil the foundation models' potential for this task and only support several simple actions and environments. In this paper, we for the first time, without any motion data, explore open-set human motion synthesis using natural language instructions as user control signals based on MLLMs across any motion task and environment. Our framework can be split into two stages: 1) sequential keyframe generation by utilizing MLLMs as a keyframe designer and animator; 2) motion filling between keyframes through interpolation and motion tracking. Our method can achieve general human motion synthesis for many downstream tasks. The promising results demonstrate the worth of mocap-free human motion synthesis aided by MLLMs and pave the way for future research.

</details>

### LLaVA-Grounding: Grounded Visual Chat with Large Multimodal Models.
- **链接**: [arXiv:2312.02949](https://arxiv.org/abs/2312.02949) · [代码](https://github.com/UX-Decoder/LLaVA-Grounding) · 📚 被引 54
- **作者**: Hao Zhang, Hongyang Li, Feng Li, Tianhe Ren, Xueyan Zou, Shilong Liu et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the recent significant advancements in large multi-modal models (LMMs), the importance of their grounding capability in visual chat is increasingly recognized. Despite recent efforts to enable LMMs to support grounding, their capabilities for grounding and chat are usually separate, and their chat performance drops dramatically when asked to ground. The problem is the lack of a dataset for grounded visual chat (GVC). Existing grounding datasets only contain short captions. To address this issue, we have created GVC data that allows for the combination of grounding and chat capabilities. To better evaluate the GVC capabilities, we have introduced a benchmark called Grounding-Bench. Additionally, we have proposed a model design that can support GVC and various types of visual prompts by connecting segmentation models with language models. Experimental results demonstrate that our model outperforms other LMMs on Grounding-Bench. Furthermore, our model achieves competitive performance on classic grounding benchmarks like RefCOCO/+/g and Flickr30K Entities. Our code will be released at https://github.com/UX-Decoder/LLaVA-Grounding .

</details>

### GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73337-6_8) · 📚 被引 3
- **作者**: Henry Hengyuan Zhao, Pan Zhou, Mike Zheng Shou
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### UniCode: Learning a Unified Codebook for Multimodal Large Language Models.
- **链接**: [arXiv:2403.09072](https://arxiv.org/abs/2403.09072) · 📚 被引 5
- **作者**: Sipeng Zheng, Bohan Zhou, Yicheng Feng, Ye Wang, Zongqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose \textbf{UniCode}, a novel approach within the domain of multimodal large language models (MLLMs) that learns a unified codebook to efficiently tokenize visual, text, and potentially other types of signals. This innovation addresses a critical limitation in existing MLLMs: their reliance on a text-only codebook, which restricts MLLM's ability to generate images and texts in a multimodal context. Towards this end, we propose a language-driven iterative training paradigm, coupled with an in-context pre-training task we term ``image decompression'', enabling our model to interpret compressed visual data and generate high-quality images.The unified codebook empowers our model to extend visual instruction tuning to non-linguistic generation tasks. Moreover, UniCode is adaptable to diverse stacked quantization approaches in order to compress visual signals into a more compact token representation. Despite using significantly fewer parameters and less data during training, Unicode demonstrates promising capabilities in visual reconstruction and generation. It also achieves performances comparable to leading MLLMs across a spectrum of VQA benchmarks.

</details>

### OpenPSG: Open-Set Panoptic Scene Graph Generation via Large Multimodal Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72684-2_12) · 📚 被引 11
- **作者**: Zijian Zhou, Zheng Zhu, Holger Caesar, Miaojing Shi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Siamese Vision Transformers are Scalable Audio-Visual Learners.
- **链接**: [arXiv:2403.19638](https://arxiv.org/abs/2403.19638) · [代码](https://github.com/GenjiB/AVSiam) · 📚 被引 4
- **作者**: Yan-Bo Lin, Gedas Bertasius
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional audio-visual methods rely on independent audio and visual backbones, which is costly and not scalable. In this work, we investigate using an audio-visual siamese network (AVSiam) for efficient and scalable audio-visual pretraining. Our framework uses a single shared vision transformer backbone to process audio and visual inputs, improving its parameter efficiency, reducing the GPU memory footprint, and allowing us to scale our method to larger datasets and model sizes. We pretrain our model using a contrastive audio-visual matching objective with a multi-ratio random masking scheme, which enables our model to process larger audio-visual instance batches, helpful for contrastive learning. Unlike prior audio-visual methods, our method can robustly handle audio, visual, and audio-visual inputs with a single shared ViT backbone. Furthermore, despite using the shared backbone for both modalities, AVSiam achieves competitive or even better results than prior methods on AudioSet and VGGSound for audio-visual classification and retrieval. Our code is available at https://github.com/GenjiB/AVSiam

</details>

### Self-Supervised Audio-Visual Soundscape Stylization.
- **链接**: [arXiv:2409.14340](https://arxiv.org/abs/2409.14340) · 📚 被引 4
- **作者**: Tingle Li, Renhao Wang, Po-Yao Huang, Andrew Owens, Gopala Anumanchipalli
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Speech sounds convey a great deal of information about the scenes, resulting in a variety of effects ranging from reverberation to additional ambient sounds. In this paper, we manipulate input speech to sound as though it was recorded within a different scene, given an audio-visual conditional example recorded from that scene. Our model learns through self-supervision, taking advantage of the fact that natural video contains recurring sound events and textures. We extract an audio clip from a video and apply speech enhancement. We then train a latent diffusion model to recover the original speech, using another audio-visual clip taken from elsewhere in the video as a conditional hint. Through this process, the model learns to transfer the conditional example's sound properties to the input speech. We show that our model can be successfully trained using unlabeled, in-the-wild videos, and that an additional visual signal can improve its sound prediction abilities. Please see our project webpage for video results: https://tinglok.netlify.app/files/avsoundscape/

</details>

### SCPNet: Unsupervised Cross-Modal Homography Estimation via Intra-modal Self-supervised Learning.
- **链接**: [arXiv:2407.08148](https://arxiv.org/abs/2407.08148) · [代码](https://github.com/RM-Zhang/SCPNet) · 📚 被引 5
- **作者**: Runmin Zhang, Jun Ma, Si-Yuan Cao, Lun Luo, Beinan Yu, Shu-Jie Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel unsupervised cross-modal homography estimation framework based on intra-modal Self-supervised learning, Correlation, and consistent feature map Projection, namely SCPNet. The concept of intra-modal self-supervised learning is first presented to facilitate the unsupervised cross-modal homography estimation. The correlation-based homography estimation network and the consistent feature map projection are combined to form the learnable architecture of SCPNet, boosting the unsupervised learning framework. SCPNet is the first to achieve effective unsupervised homography estimation on the satellite-map image pair cross-modal dataset, GoogleMap, under [-32,+32] offset on a 128x128 image, leading the supervised approach MHN by 14.0% of mean average corner error (MACE). We further conduct extensive experiments on several cross-modal/spectral and manually-made inconsistent datasets, on which SCPNet achieves the state-of-the-art (SOTA) performance among unsupervised approaches, and owns 49.0%, 25.2%, 36.4%, and 10.7% lower MACEs than the supervised approach MHN. Source code is available at https://github.com/RM-Zhang/SCPNet.

</details>

### Improving Medical Multi-modal Contrastive Learning with Expert Annotations.
- **链接**: [arXiv:2403.10153](https://arxiv.org/abs/2403.10153) · 📚 被引 16
- **作者**: Yogesh Kumar, Pekka Marttinen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce eCLIP, an enhanced version of the CLIP model that integrates expert annotations in the form of radiologist eye-gaze heatmaps. It tackles key challenges in contrastive multi-modal medical imaging analysis, notably data scarcity and the "modality gap" -- a significant disparity between image and text embeddings that diminishes the quality of representations and hampers cross-modal interoperability. eCLIP integrates a heatmap processor and leverages mixup augmentation to efficiently utilize the scarce expert annotations, thus boosting the model's learning effectiveness. eCLIP is designed to be generally applicable to any variant of CLIP without requiring any modifications of the core architecture. Through detailed evaluations across several tasks, including zero-shot inference, linear probing, cross-modal retrieval, and Retrieval Augmented Generation (RAG) of radiology reports using a frozen Large Language Model, eCLIP showcases consistent improvements in embedding quality. The outcomes reveal enhanced alignment and uniformity, affirming eCLIP's capability to harness high-quality annotations for enriched multi-modal analysis in the medical imaging domain.

</details>

### CoLeaF: A Contrastive-Collaborative Learning Framework for Weakly Supervised Audio-Visual Video Parsing.
- **链接**: [arXiv:2405.10690](https://arxiv.org/abs/2405.10690) · 📚 被引 6
- **作者**: Faegheh Sardari, Armin Mustafa, Philip J. B. Jackson, Adrian Hilton
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised audio-visual video parsing (AVVP) methods aim to detect audible-only, visible-only, and audible-visible events using only video-level labels. Existing approaches tackle this by leveraging unimodal and cross-modal contexts. However, we argue that while cross-modal learning is beneficial for detecting audible-visible events, in the weakly supervised scenario, it negatively impacts unaligned audible or visible events by introducing irrelevant modality information. In this paper, we propose CoLeaF, a novel learning framework that optimizes the integration of cross-modal context in the embedding space such that the network explicitly learns to combine cross-modal information for audible-visible events while filtering them out for unaligned events. Additionally, as videos often involve complex class relationships, modelling them improves performance. However, this introduces extra computational costs into the network. Our framework is designed to leverage cross-class relationships during training without incurring additional computations at inference. Furthermore, we propose new metrics to better evaluate a method's capabilities in performing AVVP. Our extensive experiments demonstrate that CoLeaF significantly improves the state-of-the-art results by an average of 1.9% and 2.4% F-score on the LLP and UnAV-100 datasets, respectively.

</details>

### Distractors-Immune Representation Learning with Cross-Modal Contrastive Regularization for Change Captioning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72775-7_18) · 📚 被引 14
- **作者**: Yunbin Tu, Liang Li, Li Su, Chenggang Yan, Qingming Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Multi-modal Relation Distillation for Unified 3D Representation Learning.
- **链接**: [arXiv:2407.14007](https://arxiv.org/abs/2407.14007)
- **作者**: Huiqun Wang, Yiping Bao, Panwang Pan, Zeming Li, Xiao Liu, Ruijie Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in multi-modal pre-training for 3D point clouds have demonstrated promising results by aligning heterogeneous features across 3D shapes and their corresponding 2D images and language descriptions. However, current straightforward solutions often overlook intricate structural relations among samples, potentially limiting the full capabilities of multi-modal learning. To address this issue, we introduce Multi-modal Relation Distillation (MRD), a tri-modal pre-training framework, which is designed to effectively distill reputable large Vision-Language Models (VLM) into 3D backbones. MRD aims to capture both intra-relations within each modality as well as cross-relations between different modalities and produce more discriminative 3D shape representations. Notably, MRD achieves significant improvements in downstream zero-shot classification tasks and cross-modality retrieval tasks, delivering new state-of-the-art performance.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

- LabelDistill: Label-Guided Cross-Modal Knowledge Distillation for Camera-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather. → [3d-detection](../3d-detection/Guideline%202024.md)
- GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)

## 🆕 增量新增

### MTMMC: A Large-Scale Real-World Multi-Modal Camera Tracking Benchmark. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2403.20225](https://arxiv.org/abs/2403.20225) · 📚 被引 6
- **作者**: Sanghyun Woo, Kwanyong Park, Inkyu Shin, Myungchul Kim, In So Kweon
- **🏷️ 机构**: New York University, ETRI, KAIST
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有跨摄像头多目标跟踪数据集多为合成或受控环境、难以模拟真实动态的问题，该论文提出了MTMMC，一个大规模真实世界多模态数据集，包含16个多模态相机在校园和工厂两种环境、不同时间天气季节下捕获的长视频序列。该数据集提供RGB和热成像两种模态，增强了跟踪精度，并作为现有数据集的超集，为研究复杂真实场景下的多摄像头跟踪提供了挑战性测试平台。
- **摘要（英）**: This paper tackles the limitation of existing multi-target multi-camera tracking datasets being synthetic or controlled, by introducing MTMMC, a large-scale real-world dataset with long videos from 16 multi-modal cameras in campus and factory environments across various conditions. It includes RGB and thermal modalities to improve tracking accuracy and serves as a superset of existing datasets, providing a challenging benchmark for real-world complexities.
- **核心贡献**: 构建了大规模真实世界多模态多摄像头跟踪数据集。
- **创新点**: 引入RGB和热成像双模态，覆盖多样环境条件。
- **结果**: 提供了更具挑战性的基准，促进真实场景跟踪研究。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-target multi-camera tracking is a crucial task that involves identifying and tracking individuals over time using video streams from multiple cameras. This task has practical applications in various fields, such as visual surveillance, crowd behavior analysis, and anomaly detection. However, due to the difficulty and cost of collecting and labeling data, existing datasets for this task are either synthetically generated or artificially constructed within a controlled camera network setting, which limits their ability to model real-world dynamics and generalize to diverse camera configurations. To address this issue, we present MTMMC, a real-world, large-scale dataset that includes long video sequences captured by 16 multi-modal cameras in two different environments - campus and factory - across various time, weather, and season conditions. This dataset provides a challenging test-bed for studying multi-camera tracking under diverse real-world complexities and includes an additional input modality of spatially aligned and temporally synchronized RGB and thermal cameras, which enhances the accuracy of multi-camera tracking. MTMMC is a super-set of existing datasets, benefiting independent fields such as person detection, re-identification, and multiple object tracking. We provide baselines and new learning setups on this dataset and set the reference scores for future studies. The datasets, models, and test server will be made publicly available.

</details>

### MMMU: A Massive Multi-Discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2311.16502](https://arxiv.org/abs/2311.16502) · 📚 被引 399
- **作者**: Xiang Yue, Yuansheng Ni, Tianyu Zheng, Kai Zhang, Ruoqi Liu, Ge Zhang et al.
- **🏷️ 机构**: IN. AI Research, University of Waterloo, Independent
- **会议**: CVPR 2024
- **摘要（中）**: ①针对现有多模态基准测试主要评估静态图像理解，缺乏对需要大学水平学科知识和深度推理的专家级任务评估的问题。②提出了MMMU基准，包含11.5K个来自大学考试、测验和教科书的跨学科多模态问题，覆盖6大学科、30个主题、183个子领域和30种异构图像类型。③相比现有基准，MMMU强调高级感知与领域特定知识推理，模拟专家任务。④评估14个开源LMM和GPT-4V、Gemini，GPT-4V和Gemini Ultra仅分别达到56%和59%的准确率，表明该基准极具挑战性。
- **摘要（英）**: This paper introduces MMMU, a massive multi-discipline multimodal benchmark with 11.5K college-level questions across 30 subjects and 183 subfields, targeting expert-level perception and reasoning. Unlike existing benchmarks, it emphasizes domain-specific knowledge and deliberate reasoning. Evaluation shows GPT-4V and Gemini Ultra achieve only 56% and 59% accuracy, highlighting significant room for improvement.
- **核心贡献**: 构建了首个大规模多学科、专家级多模态理解与推理基准MMMU。
- **创新点**: 通过覆盖30种异构图像类型和大学水平学科知识，实现从基础感知到专家推理的全面评估。
- **结果**: GPT-4V和Gemini Ultra准确率仅56%和59%，证明现有模型在专家级任务上仍有巨大提升空间。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MMMU: a new benchmark designed to evaluate multimodal models on massive multi-discipline tasks demanding college-level subject knowledge and deliberate reasoning. MMMU includes 11.5K meticulously collected multimodal questions from college exams, quizzes, and textbooks, covering six core disciplines: Art & Design, Business, Science, Health & Medicine, Humanities & Social Science, and Tech & Engineering. These questions span 30 subjects and 183 subfields, comprising 30 highly heterogeneous image types, such as charts, diagrams, maps, tables, music sheets, and chemical structures. Unlike existing benchmarks, MMMU focuses on advanced perception and reasoning with domain-specific knowledge, challenging models to perform tasks akin to those faced by experts. The evaluation of 14 open-source LMMs as well as the proprietary GPT-4V(ision) and Gemini highlights the substantial challenges posed by MMMU. Even the advanced GPT-4V and Gemini Ultra only achieve accuracies of 56% and 59% respectively, indicating significant room for improvement. We believe MMMU will stimulate the community to build next-generation multimodal foundation models towards expert artificial general intelligence.

</details>

### MVBench: A Comprehensive Multi-modal Video Understanding Benchmark. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2311.17005](https://arxiv.org/abs/2311.17005) · 📚 被引 308
- **作者**: Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Yi Liu et al.
- **🏷️ 机构**: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, Shanghai AI Laboratory, Pudan University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对现有多模态大模型基准主要评估静态图像空间理解，忽视视频时间动态理解的问题。②提出了MVBench基准，包含20个无法通过单帧解决的挑战性视频任务，并引入静态到动态的方法定义时间相关任务。③通过将静态任务转换为动态任务，系统生成需要从感知到认知的广泛时间技能的视频任务，并自动将公开视频注释转换为多项选择问答。④该范式高效构建基准且保证评估公平性，为视频理解评估提供了新标准。
- **摘要（英）**: MVBench addresses the lack of temporal understanding evaluation in video tasks for MLLMs by introducing 20 challenging video tasks that cannot be solved with a single frame. It uses a static-to-dynamic method to define tasks and automatically converts public annotations into multiple-choice QA, ensuring efficiency and fairness. This benchmark systematically evaluates temporal skills from perception to cognition.
- **核心贡献**: 提出了首个覆盖20个时间相关视频任务的综合多模态视频理解基准MVBench。
- **创新点**: 通过静态到动态的任务转换方法，系统生成需要广泛时间技能的视频任务。
- **结果**: 高效构建基准并保证评估公平性，为视频理解研究提供了新标准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rapid development of Multi-modal Large Language Models (MLLMs), a number of diagnostic benchmarks have recently emerged to evaluate the comprehension capabilities of these models. However, most benchmarks predominantly assess spatial understanding in the static image tasks, while overlooking temporal understanding in the dynamic video tasks. To alleviate this issue, we introduce a comprehensive Multi-modal Video understanding Benchmark, namely MVBench, which covers 20 challenging video tasks that cannot be effectively solved with a single frame. Specifically, we first introduce a novel static-to-dynamic method to define these temporal-related tasks. By transforming various static tasks into dynamic ones, we enable the systematic generation of video tasks that require a broad spectrum of temporal skills, ranging from perception to cognition. Then, guided by the task definition, we automatically convert public video annotations into multiple-choice QA to evaluate each task. On one hand, such a distinct paradigm allows us to build MVBench efficiently, without much manual intervention. On the other hand, it guarantees evaluation fairness with ground-truth video annotations, avoiding the biased scoring of LLMs. Moreover, we further develop a robust video MLLM baseline, i.e., VideoChat2, by progressive multi-modal training with diverse instruction-tuning data. The extensive results on our MVBench reveal that, the existing MLLMs are far from satisfactory in temporal understanding, while our VideoChat2 largely surpasses these leading models by over 15% on MVBench. All models and data are available at https://github.com/OpenGVLab/Ask-Anything.

</details>

### MIntRec2.0: A Large-scale Benchmark Dataset for Multimodal Intent Recognition and Out-of-scope Detection in Conversations. **⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2403.10943](https://arxiv.org/abs/2403.10943)
- **作者**: Hanlei Zhang, Xin Wang, Hua Xu, Qianrui Zhou, Kai Gao, Jianhua Su et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①针对多模态意图识别中数据集规模有限和难以处理对话中越界样本的问题。②提出了MIntRec2.0，一个大规模多模态意图识别基准，包含1245个对话和15040个样本，标注30个细粒度意图类别，并包含5736个越界样本。③相比现有工作，数据集规模更大，并专门处理多轮对话中的越界样本。④提供了通用框架支持单轮和多轮对话数据组织、特征提取、融合和分类检测。
- **摘要（英）**: This paper addresses limited dataset scale and out-of-scope sample handling in multimodal intent recognition. It introduces MIntRec2.0, a large-scale benchmark with 1,245 dialogues and 15,040 samples, annotated with 30 intent classes and 5,736 out-of-scope samples. It provides a general framework for data organization, feature extraction, fusion, and classification.
- **核心贡献**: 提出了大规模多模态意图识别基准，包含越界样本处理。
- **创新点**: 专门处理多轮对话中的越界样本，并扩展意图类别。
- **结果**: 数据集和框架支持多模态意图识别研究。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal intent recognition poses significant challenges, requiring the incorporation of non-verbal modalities from real-world contexts to enhance the comprehension of human intentions. Existing benchmark datasets are limited in scale and suffer from difficulties in handling out-of-scope samples that arise in multi-turn conversational interactions. We introduce MIntRec2.0, a large-scale benchmark dataset for multimodal intent recognition in multi-party conversations. It contains 1,245 dialogues with 15,040 samples, each annotated within a new intent taxonomy of 30 fine-grained classes. Besides 9,304 in-scope samples, it also includes 5,736 out-of-scope samples appearing in multi-turn contexts, which naturally occur in real-world scenarios. Furthermore, we provide comprehensive information on the speakers in each utterance, enriching its utility for multi-party conversational research. We establish a general framework supporting the organization of single-turn and multi-turn dialogue data, modality feature extraction, multimodal fusion, as well as in-scope classification and out-of-scope detection. Evaluation benchmarks are built using classic multimodal fusion methods, ChatGPT, and human evaluators. While existing methods incorporating nonverbal information yield improvements, effectively leveraging context information and detecting out-of-scope samples remains a substantial challenge. Notably, large language models exhibit a significant performance gap compared to humans, highlighting the limitations of machine learning methods in the cognitive intent understanding task. We believe that MIntRec2.0 will serve as a valuable resource, providing a pioneering foundation for research in human-machine conversational interactions, and significantly facilitating related applications. The full dataset and codes are available at https://github.com/thuiar/MIntRec2.0.

</details>

### Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/f2b9e8e7a36d43ddfd3d55113d56b1e0-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 5
- **作者**: Kehan Guo, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对大语言模型（LLM）在分子结构解析任务中的能力评估问题。②提出了一个多模态基准，用于测试LLM解决分子谜题的能力。③相比现有工作，该基准结合了分子结构和多模态数据。④摘要未提供具体结果数据。
- **摘要（英）**: This paper addresses the evaluation of LLMs on molecular structure elucidation tasks. It proposes a multimodal benchmark for testing LLMs on molecule puzzles. Compared to existing work, it integrates molecular structures with multimodal data. Specific results are not provided in the abstract.
- **核心贡献**: 提出了分子结构解析的多模态基准。
- **创新点**: 将LLM评估扩展到分子科学领域。
- **结果**: 未报告具体实验结果。

### MLLM-CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs. **⭐⭐** (相关度: 25%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/32923dff09f75cf1974c145764a523e2-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 5
- **作者**: Jihyung Kil, Zheda Mai, Justin Lee, Arpita Chowdhury, Zihe Wang, Kerrie Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对多模态大语言模型（MLLM）在比较推理任务上的评估不足问题。②提出了MLLM-CompBench基准，专门测试模型的比较推理能力。③相比现有基准，更聚焦于比较推理这一特定认知能力。④摘要未提供具体数据。
- **摘要（英）**: This paper addresses the insufficient evaluation of MLLMs on comparative reasoning tasks. It introduces MLLM-CompBench, a benchmark specifically for testing comparative reasoning. Compared to existing benchmarks, it focuses on this specific cognitive ability. Specific results are not detailed in the abstract.
- **核心贡献**: 提出了比较推理基准MLLM-CompBench。
- **创新点**: 聚焦于比较推理能力的评估。
- **结果**: 未报告具体性能数据。

### II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2406.05862](https://arxiv.org/abs/2406.05862)
- **作者**: Ziqiang Liu, Feiteng Fang, Xi Feng, Xeron Du, Chenhao Zhang, Noah Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对多模态大语言模型（MLLM）在图像高阶感知（如隐含意义理解）能力评估的缺失问题。②提出了II-Bench基准，专门评估模型对图像隐含意义的理解能力。③相比现有基准，更关注高阶感知和抽象图像理解。④实验发现MLLM最高准确率仅74.8%，而人类平均90%、最高98%，且模型在抽象复杂图像上表现更差，加入情感极性提示可提升准确率。
- **摘要（英）**: This paper addresses the lack of evaluation for MLLMs' higher-order perception, such as image implication understanding. It proposes II-Bench, a benchmark for this purpose. Compared to existing benchmarks, it focuses on abstract and complex image semantics. Experiments show MLLMs achieve at most 74.8% accuracy versus 90% human average, with worse performance on abstract images and improvements when sentiment hints are added.
- **核心贡献**: 提出了II-Bench基准，系统评估MLLM的图像隐含意义理解能力。
- **创新点**: 首次聚焦于图像高阶感知的基准设计。
- **结果**: MLLM最高准确率74.8%，远低于人类90%平均水平。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancements in the development of multimodal large language models (MLLMs) have consistently led to new breakthroughs on various benchmarks. In response, numerous challenging and comprehensive benchmarks have been proposed to more accurately assess the capabilities of MLLMs. However, there is a dearth of exploration of the higher-order perceptual capabilities of MLLMs. To fill this gap, we propose the Image Implication understanding Benchmark, II-Bench, which aims to evaluate the model's higher-order perception of images. Through extensive experiments on II-Bench across multiple MLLMs, we have made significant findings. Initially, a substantial gap is observed between the performance of MLLMs and humans on II-Bench. The pinnacle accuracy of MLLMs attains 74.8%, whereas human accuracy averages 90%, peaking at an impressive 98%. Subsequently, MLLMs perform worse on abstract and complex images, suggesting limitations in their ability to understand high-level semantics and capture image details. Finally, it is observed that most models exhibit enhanced accuracy when image sentiment polarity hints are incorporated into the prompts. This observation underscores a notable deficiency in their inherent understanding of image sentiment. We believe that II-Bench will inspire the community to develop the next generation of MLLMs, advancing the journey towards expert artificial general intelligence (AGI). II-Bench is publicly available at https://huggingface.co/datasets/m-a-p/II-Bench.

</details>

### WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d1fa821312040303b089ae529dbf81a6-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Michael Wornow, Avanika Narayan, Ben Viggiano, Ishan S. Khare, Tathagat Verma, Tibor Thompson et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对多模态基础模型在业务流程管理（BPM）任务中的评估缺失问题。②提出了WONDERBREAD基准，用于评估模型在BPM任务上的表现。③相比现有基准，专注于业务流程管理这一特定领域。④摘要未提供具体数据。
- **摘要（英）**: This paper addresses the lack of evaluation for multimodal foundation models on business process management tasks. It introduces WONDERBREAD, a benchmark for this purpose. Compared to existing benchmarks, it focuses on the BPM domain. Specific results are not provided in the abstract.
- **核心贡献**: 提出了WONDERBREAD基准，评估多模态模型在BPM任务上的能力。
- **创新点**: 将多模态评估扩展到业务流程管理领域。
- **结果**: 未报告具体实验结果。

### MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/586640cda3db2dc77349013dcefee456-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 8
- **作者**: Yichi Zhang, Yao Huang, Yitong Sun, Chang Liu, Zhe Zhao, Zhengwei Fang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对多模态大语言模型（MLLM）在可信度方面缺乏系统评估的问题。②提出了MultiTrust，一个全面的基准测试，涵盖真实性、安全性、鲁棒性等维度，并设计了多层次的评估任务。③相比现有基准，更全面地覆盖了可信度的多个方面，并引入了细粒度的评估协议。④通过大规模实验揭示了当前MLLM在可信度上的显著缺陷，为后续改进提供了方向。
- **摘要（英）**: This paper addresses the lack of systematic evaluation of trustworthiness in multimodal large language models (MLLMs). It introduces MultiTrust, a comprehensive benchmark covering dimensions such as truthfulness, safety, and robustness, with multi-level evaluation tasks. Compared to existing benchmarks, it provides broader coverage and finer-grained protocols, revealing significant deficiencies in current MLLMs through extensive experiments.
- **核心贡献**: 提出了首个全面覆盖多模态大语言模型可信度的基准测试MultiTrust。
- **创新点**: 设计了多维度、多粒度的可信度评估框架，并引入细粒度协议。
- **结果**: 实验揭示了当前MLLM在可信度上的显著缺陷，为改进提供了依据。

### Weakly Misalignment-Free Adaptive Feature Alignment for UAVs-Based Multimodal Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02534) · 📚 被引 83
- **作者**: Chen Chen, Jiahao Qi, Xingyue Liu, Kangcheng Bin, Ruigang Fu, Xikun Hu et al.
- **🏷️ 机构**: National University of Defense Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对无人机多模态目标检测中特征对齐易受弱对齐影响的问题，提出弱对齐无关的自适应特征对齐方法，通过设计对齐机制减少模态间错位。该方法在无人机多模态检测任务上提升鲁棒性，但摘要信息不完整，具体效果未给出。
- **摘要（英）**: This work tackles weak misalignment in multimodal object detection for UAVs, proposing an adaptive feature alignment method that is robust to misalignment. It improves robustness in UAV-based detection, though specific results are not provided in the abstract.
- **核心贡献**: 提出弱对齐无关的自适应特征对齐方法用于无人机多模态检测。
- **创新点**: 设计对弱对齐鲁棒的特征对齐机制。
- **结果**: 提升无人机多模态检测的鲁棒性。

### Open-World Human-Object Interaction Detection via Multi-Modal Prompts. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01604) · 📚 被引 28
- **作者**: Jie Yang, Bingliang Li, Ailing Zeng, Lei Zhang, Ruimao Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong,Shenzhen, International Digital Economy Academy
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放世界场景下人类-物体交互检测中，现有方法难以处理未见过的交互类别和多样化的提示信息的问题。②提出了利用多模态提示（如文本和视觉）进行开放世界HOI检测的方法，通过融合多模态信息增强模型对未知交互的泛化能力。③相比传统闭集检测方法，该方法能适应开放世界中的新类别和动态场景。④摘要未提供具体数据，但方法设计旨在提升开放世界检测的鲁棒性和灵活性。
- **摘要（英）**: This work addresses open-world human-object interaction detection by leveraging multi-modal prompts to handle unseen interaction categories. It integrates text and visual cues to improve generalization to novel interactions. The approach aims to enhance robustness and flexibility in dynamic open-world scenarios.
- **核心贡献**: 提出基于多模态提示的开放世界HOI检测方法。
- **创新点**: 利用多模态信息融合提升对未知交互类别的泛化能力。
- **结果**: 摘要未提供具体数据，但方法旨在提升开放世界检测性能。

### IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.15241](https://arxiv.org/abs/2403.15241) · 📚 被引 110
- **作者**: Junbo Yin, Jianbing Shen, Runnan Chen, Wei Li, Ruigang Yang, Pascal Frossard et al.
- **🏷️ 机构**: School of Computer Science and Technology, Beijing Institute of Technology, SKL-IOTSC, CIS, University of Macau, The University of Hong Kong
- **会议**: CVPR 2024
- **摘要（中）**: 针对BEV表示中物体尺寸小、点云稀疏导致3D感知可靠性差的问题，提出IS-Fusion多模态融合框架，联合捕获实例级和场景级上下文信息。通过层级场景融合模块（HSF）和实例引导融合模块（IGF），在不同粒度上融合多模态场景上下文，并利用实例候选增强场景特征。相比仅关注BEV场景级融合的现有方法，显式引入实例级多模态信息，提升实例中心任务性能。在挑战性数据集上验证了有效性。
- **摘要（英）**: To address the challenges of small object sizes and sparse point clouds in BEV representation for reliable 3D perception, this paper proposes IS-Fusion, a multimodal fusion framework that jointly captures instance- and scene-level contextual information. It introduces Hierarchical Scene Fusion (HSF) and Instance-Guided Fusion (IGF) modules to fuse multimodal context at different granularities and enhance scene features with instance guidance. Unlike existing BEV-only fusion methods, it explicitly incorporates instance-level information, improving instance-centric tasks like 3D detection. Experiments on challenging datasets demonstrate its effectiveness.
- **核心贡献**: 提出IS-Fusion框架，首次在BEV融合中显式结合实例级与场景级多模态上下文。
- **创新点**: 设计HSF和IGF模块，实现多粒度场景融合与实例引导的BEV特征增强。
- **结果**: 在挑战性数据集上验证了实例级融合对3D检测性能的提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bird's eye view (BEV) representation has emerged as a dominant solution for describing 3D space in autonomous driving scenarios. However, objects in the BEV representation typically exhibit small sizes, and the associated point cloud context is inherently sparse, which leads to great challenges for reliable 3D perception. In this paper, we propose IS-Fusion, an innovative multimodal fusion framework that jointly captures the Instance- and Scene-level contextual information. IS-Fusion essentially differs from existing approaches that only focus on the BEV scene-level fusion by explicitly incorporating instance-level multimodal information, thus facilitating the instance-centric tasks like 3D object detection. It comprises a Hierarchical Scene Fusion (HSF) module and an Instance-Guided Fusion (IGF) module. HSF applies Point-to-Grid and Grid-to-Region transformers to capture the multimodal scene context at different granularities. IGF mines instance candidates, explores their relationships, and aggregates the local multimodal context for each instance. These instances then serve as guidance to enhance the scene feature and yield an instance-aware BEV representation. On the challenging nuScenes benchmark, IS-Fusion outperforms all the published multimodal works to date. Code is available at: https://github.com/yinjunbo/IS-Fusion.

</details>

### Scene-adaptive and Region-aware Multi-modal Prompt for Open Vocabulary Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01584) · 📚 被引 14
- **作者**: Xiaowei Zhao, Xianglong Liu, Duorui Wang, Yajun Gao, Zhide Liu
- **🏷️ 机构**: Beihang University,State Key Laboratory of Complex &#x0026; Critical Software Environment
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇目标检测中多模态提示（prompt）设计不足的问题，该论文提出场景自适应和区域感知的多模态提示方法。方法通过引入场景级和区域级上下文信息，动态调整提示特征，以提升模型对未知类别的泛化能力。相比固定提示或单一模态提示，该方法能更好地适应不同场景和区域分布。实验表明在多个开放词汇检测基准上取得了性能提升。
- **摘要（英）**: This paper addresses the limitations of multimodal prompts in open-vocabulary object detection by proposing scene-adaptive and region-aware prompt learning. It dynamically adjusts prompt features using scene-level and region-level context, improving generalization to unseen categories. Compared to fixed or single-modal prompts, the method adapts better to diverse scenes and regions, achieving performance gains on multiple benchmarks.
- **核心贡献**: 提出场景自适应与区域感知的多模态提示机制，提升开放词汇检测的泛化性。
- **创新点**: 将场景和区域上下文动态融入提示生成过程。
- **结果**: 在多个基准上取得性能提升。

### AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis.
- **链接**: [arXiv:2402.17483](https://arxiv.org/abs/2402.17483) · 📚 被引 13
- **作者**: Tang Tao, Guangrun Wang, Yixing Lao, Peng Chen, Jie Liu, Liang Lin et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, University of Oxford, HKU
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural implicit fields have been a de facto standard in novel view synthesis. Recently, there exist some methods exploring fusing multiple modalities within a single field, aiming to share implicit features from different modalities to enhance reconstruction performance. However, these modalities often exhibit misaligned behaviors: optimizing for one modality, such as LiDAR, can adversely affect another, like camera performance, and vice versa. In this work, we conduct comprehensive analyses on the multimodal implicit field of LiDAR-camera joint synthesis, revealing the underlying issue lies in the misalignment of different sensors. Furthermore, we introduce AlignMiF, a geometrically aligned multimodal implicit field with two proposed modules: Geometry-Aware Alignment (GAA) and Shared Geometry Initialization (SGI). These modules effectively align the coarse geometry across different modalities, significantly enhancing the fusion process between LiDAR and camera data. Through extensive experiments across various datasets and scenes, we demonstrate the effectiveness of our approach in facilitating better interaction between LiDAR and camera modalities within a unified neural field. Specifically, our proposed AlignMiF, achieves remarkable improvement over recent implicit fusion methods (+2.01 and +3.11 image PSNR on the KITTI-360 and Waymo datasets) and consistently surpasses single modality performance (13.8% and 14.2% reduction in LiDAR Chamfer Distance on the respective datasets).

</details>

### Draw Step by Step: Reconstructing CAD Construction Sequences from Point Clouds via Multimodal Diffusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02564) · 📚 被引 23
- **作者**: Weijian Ma, Shuaiqi Chen, Yunzhong Lou, Xueyang Li, Xiangdong Zhou
- **🏷️ 机构**: School of Computer Science and Technology, Fudan University
- **会议**: CVPR 2024

### StreamingFlow: Streaming Occupancy Forecasting with Asynchronous Multi-modal Data Streams via Neural Ordinary Differential Equation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01405) · 📚 被引 3
- **作者**: Yining Shi, Kun Jiang, Ke Wang, Jiusi Li, Yunlong Wang, Mengmeng Yang et al.
- **🏷️ 机构**: School of Vehicle and Mobility, Tsinghua University, KargoBot, Inc
- **会议**: CVPR 2024

### SDSTrack: Self-Distillation Symmetric Adapter Learning for Multi-Modal Visual Object Tracking.
- **链接**: [arXiv:2403.16002](https://arxiv.org/abs/2403.16002) · 📚 被引 113
- **作者**: Xiaojun Hou, Jiazheng Xing, Yijie Qian, Yaowei Guo, Shuo Xin, Junhao Chen et al.
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Visual Object Tracking (VOT) has recently gained significant attention due to its robustness. Early research focused on fully fine-tuning RGB-based trackers, which was inefficient and lacked generalized representation due to the scarcity of multimodal data. Therefore, recent studies have utilized prompt tuning to transfer pre-trained RGB-based trackers to multimodal data. However, the modality gap limits pre-trained knowledge recall, and the dominance of the RGB modality persists, preventing the full utilization of information from other modalities. To address these issues, we propose a novel symmetric multimodal tracking framework called SDSTrack. We introduce lightweight adaptation for efficient fine-tuning, which directly transfers the feature extraction ability from RGB to other domains with a small number of trainable parameters and integrates multimodal features in a balanced, symmetric manner. Furthermore, we design a complementary masked patch distillation strategy to enhance the robustness of trackers in complex environments, such as extreme weather, poor imaging, and sensor failure. Extensive experiments demonstrate that SDSTrack outperforms state-of-the-art methods in various multimodal tracking scenarios, including RGB+Depth, RGB+Thermal, and RGB+Event tracking, and exhibits impressive results in extreme conditions. Our source code is available at https://github.com/hoqolo/SDSTrack.

</details>

### OVMR: Open-Vocabulary Recognition with Multi-Modal References.
- **链接**: [arXiv:2406.04675](https://arxiv.org/abs/2406.04675) · 📚 被引 8
- **作者**: Zehong Ma, Shiliang Zhang, Longhui Wei, Qi Tian
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing, Huawei Inc.
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The challenge of open-vocabulary recognition lies in the model has no clue of new categories it is applied to. Existing works have proposed different methods to embed category cues into the model, \eg, through few-shot fine-tuning, providing category names or textual descriptions to Vision-Language Models. Fine-tuning is time-consuming and degrades the generalization capability. Textual descriptions could be ambiguous and fail to depict visual details. This paper tackles open-vocabulary recognition from a different perspective by referring to multi-modal clues composed of textual descriptions and exemplar images. Our method, named OVMR, adopts two innovative components to pursue a more robust category cues embedding. A multi-modal classifier is first generated by dynamically complementing textual descriptions with image exemplars. A preference-based refinement module is hence applied to fuse uni-modal and multi-modal classifiers, with the aim to alleviate issues of low-quality exemplar images or textual descriptions. The proposed OVMR is a plug-and-play module, and works well with exemplar images randomly crawled from the Internet. Extensive experiments have demonstrated the promising performance of OVMR, \eg, it outperforms existing methods across various scenarios and setups. Codes are publicly available at \href{https://github.com/Zehong-Ma/OVMR}{https://github.com/Zehong-Ma/OVMR}.

</details>

### Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset.
- **链接**: [arXiv:2406.09383](https://arxiv.org/abs/2406.09383) · 📚 被引 16
- **作者**: Yiming Li, Zhiheng Li, Nuo Chen, Moonjun Gong, Zonglin Lyu, Zehong Wang et al.
- **🏷️ 机构**: New York University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale datasets have fueled recent advancements in AI-based autonomous vehicle research. However, these datasets are usually collected from a single vehicle's one-time pass of a certain location, lacking multiagent interactions or repeated traversals of the same place. Such information could lead to transformative enhancements in autonomous vehicles' perception, prediction, and planning capabilities. To bridge this gap, in collaboration with the self-driving company May Mobility, we present the MARS dataset which unifies scenarios that enable MultiAgent, multitraveRSal, and multimodal autonomous vehicle research. More specifically, MARS is collected with a fleet of autonomous vehicles driving within a certain geographical area. Each vehicle has its own route and different vehicles may appear at nearby locations. Each vehicle is equipped with a LiDAR and surround-view RGB cameras. We curate two subsets in MARS: one facilitates collaborative driving with multiple vehicles simultaneously present at the same location, and the other enables memory retrospection through asynchronous traversals of the same location by multiple vehicles. We conduct experiments in place recognition and neural reconstruction. More importantly, MARS introduces new research opportunities and challenges such as multitraversal 3D reconstruction, multiagent perception, and unsupervised object discovery. Our data and codes can be found at https://ai4ce.github.io/MARS/.

</details>

### VCoder: Versatile Vision Encoders for Multimodal Large Language Models.
- **链接**: [arXiv:2312.14233](https://arxiv.org/abs/2312.14233) · 📚 被引 37
- **作者**: Jitesh Jain, Jianwei Yang, Humphrey Shi
- **🏷️ 机构**: SHI Labs@Georgia Tech, Microsoft Research, Redmond
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans possess the remarkable skill of Visual Perception, the ability to see and understand the seen, helping them make sense of the visual world and, in turn, reason. Multimodal Large Language Models (MLLM) have recently achieved impressive performance on vision-language tasks ranging from visual question-answering and image captioning to visual reasoning and image generation. However, when prompted to identify or count (perceive) the entities in a given image, existing MLLM systems fail. Working towards developing an accurate MLLM system for perception and reasoning, we propose using Versatile vision enCoders (VCoder) as perception eyes for Multimodal LLMs. We feed the VCoder with perception modalities such as segmentation or depth maps, improving the MLLM's perception abilities. Secondly, we leverage the images from COCO and outputs from off-the-shelf vision perception models to create our COCO Segmentation Text (COST) dataset for training and evaluating MLLMs on the object perception task. Thirdly, we introduce metrics to assess the object perception abilities in MLLMs on our COST dataset. Lastly, we provide extensive experimental evidence proving the VCoder's improved object-level perception skills over existing Multimodal LLMs, including GPT-4V. We open-source our dataset, code, and models to promote research. We open-source our code at https://github.com/SHI-Labs/VCoder

</details>

### Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action.
- **链接**: [arXiv:2312.17172](https://arxiv.org/abs/2312.17172) · 📚 被引 95
- **作者**: Jiasen Lu, Christopher Clark, Sangho Lee, Zichen Zhang, Savya Khosla, Ryan Marten et al.
- **🏷️ 机构**: Allen Institute for AI, University of Illinois Urbana-Champaign
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

</details>

### EMOPortraits: Emotion-Enhanced Multimodal One-Shot Head Avatars.
- **链接**: [arXiv:2404.19110](https://arxiv.org/abs/2404.19110) · 📚 被引 41
- **作者**: Nikita Drobyshev, Antoni Bigata Casademunt, Konstantinos Vougioukas, Zoe Landgraf, Stavros Petridis, Maja Pantic
- **🏷️ 机构**: Imperial College London
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Head avatars animated by visual signals have gained popularity, particularly in cross-driving synthesis where the driver differs from the animated character, a challenging but highly practical approach. The recently presented MegaPortraits model has demonstrated state-of-the-art results in this domain. We conduct a deep examination and evaluation of this model, with a particular focus on its latent space for facial expression descriptors, and uncover several limitations with its ability to express intense face motions. To address these limitations, we propose substantial changes in both training pipeline and model architecture, to introduce our EMOPortraits model, where we: Enhance the model's capability to faithfully support intense, asymmetric face expressions, setting a new state-of-the-art result in the emotion transfer task, surpassing previous methods in both metrics and quality. Incorporate speech-driven mode to our model, achieving top-tier performance in audio-driven facial animation, making it possible to drive source identity through diverse modalities, including visual signal, audio, or a blend of both. We propose a novel multi-view video dataset featuring a wide range of intense and asymmetric facial expressions, filling the gap with absence of such data in existing datasets.

</details>

### SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather.
- **链接**: [arXiv:2508.16408](https://arxiv.org/abs/2508.16408) · 📚 被引 23
- **作者**: Edoardo Palladin, Roland Dietze, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal sensor fusion is an essential capability for autonomous robots, enabling object detection and decision-making in the presence of failing or uncertain inputs. While recent fusion methods excel in normal environmental conditions, these approaches fail in adverse weather, e.g., heavy fog, snow, or obstructions due to soiling. We introduce a novel multi-sensor fusion approach tailored to adverse weather conditions. In addition to fusing RGB and LiDAR sensors, which are employed in recent autonomous driving literature, our sensor fusion stack is also capable of learning from NIR gated camera and radar modalities to tackle low light and inclement weather. We fuse multimodal sensor data through attentive, depth-based blending schemes, with learned refinement on the Bird's Eye View (BEV) plane to combine image and range features effectively. Our detections are predicted by a transformer decoder that weighs modalities based on distance and visibility. We demonstrate that our method improves the reliability of multimodal sensor fusion in autonomous vehicles under challenging weather conditions, bridging the gap between ideal conditions and real-world edge cases. Our approach improves average precision by 17.2 AP compared to the next best method for vulnerable pedestrians in long distances and challenging foggy scenes. Our project page is available at https://light.princeton.edu/samfusion/

</details>

## 跨领域论文（完整笔记在其他领域）

- MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark. → [vlm](../vlm/Guideline%202024.md)
- MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI. → [vlm](../vlm/Guideline%202024.md)
- WikiDO: A New Benchmark Evaluating Cross-Modal Retrieval for Vision-Language Models. → [vlm](../vlm/Guideline%202024.md)
- DevBench: A multimodal developmental benchmark for language learning. → [vlm](../vlm/Guideline%202024.md)
- VERIFIED: A Video Corpus Moment Retrieval Benchmark for Fine-Grained Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding. → [vlm](../vlm/Guideline%202024.md)
- LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- UniMODE: Unified Monocular 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Holistic Autonomous Driving Understanding by Bird'View Injected Multi-Modal Large Models. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Training-Free Open-Vocabulary Segmentation with Offline Diffusion-Augmented Prototype Generation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Image-to-Image Matching via Foundation Models: A New Perspective for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and StructurEd Representation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Abductive Ego-View Accident Video Understanding for Safe Driving Perception. → [video-understanding](../video-understanding/Guideline%202024.md)
- Consistency and Uncertainty: Identifying Unreliable Responses From Black-Box Vision-Language Models for Selective Visual Question Answering. → [vlm](../vlm/Guideline%202024.md)
- MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. → [network-pruning](../network-pruning/Guideline%202024.md)
- MULTIFLOW: Shifting Towards Task-Agnostic Vision-Language Pruning. → [network-pruning](../network-pruning/Guideline%202024.md)
- SyncMask: Synchronized Attentional Masking for Fashion-centric Vision-Language Pretraining. → [vlm](../vlm/Guideline%202024.md)
- PartDistill: 3D Shape Part Segmentation by Vision-Language Model Distillation. → [vlm](../vlm/Guideline%202024.md)
- MMA: Multi-Modal Adapter for Vision-Language Models. → [vlm](../vlm/Guideline%202024.md)
- MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- Honeybee: Locality-Enhanced Projector for Multimodal LLM. → [vlm](../vlm/Guideline%202024.md)
- LION : Empowering Multimodal Large Language Model with Dual-Level Visual Knowledge. → [vlm](../vlm/Guideline%202024.md)
- Question Aware Vision Transformer for Multimodal Reasoning. → [vision-transformer](../vision-transformer/Guideline%202024.md)
- SmartEdit: Exploring Complex Instruction-Based Image Editing with Multimodal Large Language Models. → [vlm](../vlm/Guideline%202024.md)
- Sniffer: Multimodal Large Language Model for Explainable Out-of-Context Misinformation Detection. → [vlm](../vlm/Guideline%202024.md)
- TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- Link-Context Learning for Multimodal LLMs. → [vlm](../vlm/Guideline%202024.md)
- Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs. → [vlm](../vlm/Guideline%202024.md)
- GSVA: Generalized Segmentation via Multimodal Large Language Models. → [vlm](../vlm/Guideline%202024.md)
- Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Self-Supervised Class-Agnostic Motion Prediction with Spatial and Temporal Consistency Regularizations. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- ES3: Evolving Self-Supervised Learning of Robust Audio-Visual Speech Representations. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Enhancing Visual Document Understanding with Contrastive Learning in Large Visual-Language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- DeTra: A Unified Model for Object Detection and Trajectory Forecasting. → [object-detection](../object-detection/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- LabelDistill: Label-Guided Cross-Modal Knowledge Distillation for Camera-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- LEROjD: Lidar Extended Radar-Only Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. → [bev](../bev/Guideline%202024.md)
<!-- COMPLETE v1 papers=160 -->
