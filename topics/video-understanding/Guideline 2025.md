# Video Understanding — 2025 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LVBench: An Extreme Long Video Understanding Benchmark.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02131) · 📚 被引 14
- **作者**: Weihan Wang, Zehai He, Wenyi Hong, Yean Cheng, Xiaohan Zhang, Ji Qi et al.
- **🏷️ 机构**: Zhipu AI, Tsinghua University
- **会议**: ICCV 2025

### Streaming Videollms for Real-Time Procedural Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02097) · 📚 被引 1
- **作者**: Dibyadip Chatterjee, Edoardo Remelli, Yale Song, Bugra Tekin, Abhay Mittal, Bharat Bhatnagar et al.
- **🏷️ 机构**: Meta Reality Labs, FAIR, Meta
- **会议**: ICCV 2025

### VideoLLaMB: Long Streaming Video Understanding with Recurrent Memory Bridges.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02240) · 📚 被引 4
- **作者**: Yuxuan Wang, Yiqi Song, Cihang Xie, Yang Liu, Zilong Zheng
- **🏷️ 机构**: State Key Laboratory of General Artificial Intelligence, BIGAI,NLCo Lab, University of California,Computer Science and Engineering, Wangxuan Institute of Computer Technology, Peking University
- **会议**: ICCV 2025

### Apollo: An Exploration of Video Understanding in Large Multimodal Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zohar_Apollo__An_Exploration_of_Video_Understanding_in_Large_Multimodal_CVPR_2025_paper.html)
- **作者**: Orr Zohar, Xiaohan Wang, Yann Dubois, Nikhil Mehta, Tong Xiao, Philippe Hansen-Estruch et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### VideoAds for Fast-Paced Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02025) · 📚 被引 2
- **作者**: Zheyuan Zhang, Wanying Dou, Linkai Peng, Hongyi Pan, Ulas Bagci, Boqing Gong
- **🏷️ 机构**: Northwestern University, Boston University
- **会议**: ICCV 2025

### DynImg: Key Frames with Visual Prompts are Good Representation for Multi-Modal Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02198) · 📚 被引 0
- **作者**: Xiaoyi Bao, Chenwei Xie, Hao Tang, Tingyu Weng, Xiaofeng Wang, Yun Zheng et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Alibaba Group
- **会议**: ICCV 2025

### VideoICL: Confidence-based Iterative In-context Learning for Out-of-Distribution Video Understanding.
- **链接**: [arXiv:2412.02186](https://arxiv.org/abs/2412.02186) · [代码](https://github.com/KangsanKim07/VideoICL) · 📚 被引 2
- **作者**: Kangsan Kim, Geon Park, Youngwan Lee, Woongyeong Yeo, Sung Ju Hwang
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in video large multimodal models (LMMs) have significantly improved their video understanding and reasoning capabilities. However, their performance drops on out-of-distribution (OOD) tasks that are underrepresented in training data. Traditional methods like fine-tuning on OOD datasets are impractical due to high computational costs. While In-context learning (ICL) with demonstration examples has shown promising generalization performance in language tasks and image-language tasks without fine-tuning, applying ICL to video-language tasks faces challenges due to the limited context length in Video LMMs, as videos require longer token lengths. To address these issues, we propose VideoICL, a novel video in-context learning framework for OOD tasks that introduces a similarity-based relevant example selection strategy and a confidence-based iterative inference approach. This allows to select the most relevant examples and rank them based on similarity, to be used for inference. If the generated response has low confidence, our framework selects new examples and performs inference again, iteratively refining the results until a high-confidence response is obtained. This approach improves OOD video understanding performance by extending effective context length without incurring high costs. The experimental results on multiple benchmarks demonstrate significant performance gains, especially in domain-specific scenarios, laying the groundwork for broader video comprehension applications. Code will be released at https://github.com/KangsanKim07/VideoICL

</details>

### DIV-FF: Dynamic Image-Video Feature Fields For Environment Understanding in Egocentric Videos.
- **链接**: [arXiv:2503.08344](https://arxiv.org/abs/2503.08344) · 📚 被引 0
- **作者**: Lorenzo Mur-Labadia, Josechu Guerrero, Ruben Martinez-Cantin
- **🏷️ 机构**: I3A - Universidad de Zaragoza
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Environment understanding in egocentric videos is an important step for applications like robotics, augmented reality and assistive technologies. These videos are characterized by dynamic interactions and a strong dependence on the wearer engagement with the environment. Traditional approaches often focus on isolated clips or fail to integrate rich semantic and geometric information, limiting scene comprehension. We introduce Dynamic Image-Video Feature Fields (DIV FF), a framework that decomposes the egocentric scene into persistent, dynamic, and actor based components while integrating both image and video language features. Our model enables detailed segmentation, captures affordances, understands the surroundings and maintains consistent understanding over time. DIV-FF outperforms state-of-the-art methods, particularly in dynamically evolving scenarios, demonstrating its potential to advance long term, spatio temporal scene understanding.

</details>

### OVO-Bench: How Far is Your Video-LLMs from Real-World Online Video Understanding?
- **链接**: [arXiv:2501.05510](https://arxiv.org/abs/2501.05510) · [代码](https://github.com/JoeLeelyf/OVO-Bench) · 📚 被引 5
- **作者**: Junbo Niu, Yifei Li, Ziyang Miao, Chunjiang Ge, Yuanhang Zhou, Qihao He et al.
- **🏷️ 机构**: Shanghai Artificial Intelligence Laboratory, Beihang University, Tsinghua University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Temporal Awareness, the ability to reason dynamically based on the timestamp when a question is raised, is the key distinction between offline and online video LLMs. Unlike offline models, which rely on complete videos for static, post hoc analysis, online models process video streams incrementally and dynamically adapt their responses based on the timestamp at which the question is posed. Despite its significance, temporal awareness has not been adequately evaluated in existing benchmarks. To fill this gap, we present OVO-Bench (Online-VideO-Benchmark), a novel video benchmark that emphasizes the importance of timestamps for advanced online video understanding capability benchmarking. OVO-Bench evaluates the ability of video LLMs to reason and respond to events occurring at specific timestamps under three distinct scenarios: (1) Backward tracing: trace back to past events to answer the question. (2) Real-time understanding: understand and respond to events as they unfold at the current timestamp. (3) Forward active responding: delay the response until sufficient future information becomes available to answer the question accurately. OVO-Bench comprises 12 tasks, featuring 644 unique videos and approximately human-curated 2,800 fine-grained meta-annotations with precise timestamps. We combine automated generation pipelines with human curation. With these high-quality samples, we further developed an evaluation pipeline to systematically query video LLMs along the video timeline. Evaluations of nine Video-LLMs reveal that, despite advancements on traditional benchmarks, current models struggle with online video understanding, showing a significant gap compared to human agents. We hope OVO-Bench will drive progress in video LLMs and inspire future research in online video reasoning. Our benchmark and code can be accessed at https://github.com/JoeLeelyf/OVO-Bench.

</details>

### VISTA: Enhancing Long-Duration and High-Resolution Video Understanding by Video Spatiotemporal Augmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ren_VISTA_Enhancing_Long-Duration_and_High-Resolution_Video_Understanding_by_Video_Spatiotemporal_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Weiming Ren, Huan Yang, Jie Min, Cong Wei, Wenhu Chen
- **🏷️ 机构**: University of Waterloo, 01.AI
- **会议**: CVPR 2025

### Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shu_Video-XL_Extra-Long_Vision_Language_Model_for_Hour-Scale_Video_Understanding_CVPR_2025_paper.html)
- **作者**: Yan Shu, Zheng Liu, Peitian Zhang, Minghao Qin, Junjie Zhou, Zhengyang Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding.
- **链接**: [arXiv:2412.00493](https://arxiv.org/abs/2412.00493) · 📚 被引 18
- **作者**: Duo Zheng, Shijia Huang, Liwei Wang
- **🏷️ 机构**: The Chinese University of Hong Kong
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancement of Multimodal Large Language Models (MLLMs) has significantly impacted various multimodal tasks. However, these models face challenges in tasks that require spatial understanding within 3D environments. Efforts to enhance MLLMs, such as incorporating point cloud features, have been made, yet a considerable gap remains between the models' learned representations and the inherent complexity of 3D scenes. This discrepancy largely stems from the training of MLLMs on predominantly 2D data, which restricts their effectiveness in comprehending 3D spaces. To address this issue, in this paper, we propose a novel generalist model, i.e., Video-3D LLM, for 3D scene understanding. By treating 3D scenes as dynamic videos and incorporating 3D position encoding into these representations, our Video-3D LLM aligns video representations with real-world spatial contexts more accurately. In addition, we have implemented a maximum coverage sampling technique to optimize the trade-off between computational cost and performance. Extensive experiments demonstrate that our model achieves state-of-the-art performance on several 3D scene understanding benchmarks, including ScanRefer, Multi3DRefer, Scan2Cap, ScanQA, and SQA3D.

</details>

### BOLT: Boost Large Vision-Language Model Without Training for Long-form Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_BOLT_Boost_Large_Vision-Language_Model_Without_Training_for_Long-form_Video_CVPR_2025_paper.html)
- **作者**: Shuming Liu, Chen Zhao, Tianqi Xu, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MMVU, a comprehensive expert-level, multi-discipline benchmark for evaluating foundation models in video understanding. MMVU includes 3,000 expert-annotated questions spanning 27 subjects across four core disciplines: Science, Healthcare, Humanities & Social Sciences, and Engineering. Compared to prior benchmarks, MMVU features three key advancements. First, it challenges models to apply domain-specific knowledge and perform expert-level reasoning to analyze specialized-domain videos, moving beyond the basic visual perception typically assessed in current video benchmarks. Second, each example is annotated by human experts from scratch. We implement strict data quality controls to ensure the high quality of the dataset. Finally, each example is enriched with expert-annotated reasoning rationals and relevant domain knowledge, facilitating in-depth analysis. We conduct an extensive evaluation of 32 frontier multimodal foundation models on MMVU. The latest System-2-capable models, o1 and Gemini 2.0 Flash Thinking, achieve the highest performance among the tested models. However, they still fall short of matching human expertise. Through in-depth error analyses and case studies, we offer actionable insights for future advancements in expert-level, knowledge-intensive video understanding for specialized domains.

</details>

### Flow4Agent: Long-form Video Understanding via Motion Prior from Optical Flow.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02211) · 📚 被引 0
- **作者**: Ruyang Liu, Shangkun Sun, Haoran Tang, Wei Gao, Ge Li
- **🏷️ 机构**: School of Electronic and Computer Engineering, Shenzhen Graduate School, Peking University
- **会议**: ICCV 2025

### AdsQA: Towards Advertisement Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02172) · 📚 被引 2
- **作者**: Xinwei Long, Kai Tian, Peng Xu, Guoli Jia, Jingxuan Li, Sa Yang et al.
- **🏷️ 机构**: Tsinghua University, Independent Researcher, Peking University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in multimodal large language models (MLLMs) have expanded research in video understanding, primarily focusing on high-level tasks such as video captioning and question-answering. Meanwhile, a smaller body of work addresses dense, pixel-precise segmentation tasks, which typically involve category-guided or referral-based object segmentation. Although both directions are essential for developing models with human-level video comprehension, they have largely evolved separately, with distinct benchmarks and architectures. This paper aims to unify these efforts by introducing ViCaS, a new dataset containing thousands of challenging videos, each annotated with detailed, human-written captions and temporally consistent, pixel-accurate masks for multiple objects with phrase grounding. Our benchmark evaluates models on both holistic/high-level understanding and language-guided, pixel-precise segmentation. We also present carefully validated evaluation measures and propose an effective model architecture that can tackle our benchmark. Project page: https://ali2500.github.io/vicas-project/

</details>

### Bringing RNNs Back to Efficient Open-Ended Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02177) · 📚 被引 0
- **作者**: Weili Xu, Enxin Song, Wenhao Chai, Xuexiang Wen, Tian Ye, Gaoang Wang
- **🏷️ 机构**: Zhejiang University, University of Washington, HKUST (GZ)
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite advancements in multimodal large language models (MLLMs), current approaches struggle in medium-to-long video understanding due to frame and context length limitations. As a result, these models often depend on frame sampling, which risks missing key information over time and lacks task-specific relevance. To address these challenges, we introduce HierarQ, a task-aware hierarchical Q-Former based framework that sequentially processes frames to bypass the need for frame sampling, while avoiding LLM's context length limitations. We introduce a lightweight two-stream language-guided feature modulator to incorporate task awareness in video understanding, with the entity stream capturing frame-level object information within a short context and the scene stream identifying their broader interactions over longer period of time. Each stream is supported by dedicated memory banks which enables our proposed Hierachical Querying transformer (HierarQ) to effectively capture short and long-term context. Extensive evaluations on 10 video benchmarks across video understanding, question answering, and captioning tasks demonstrate HierarQ's state-of-the-art performance across most datasets, proving its robustness and efficiency for comprehensive video analysis.

</details>

### DynFocus: Dynamic Cooperative Network Empowers LLMs with Video Understanding.
- **链接**: [arXiv:2411.12355](https://arxiv.org/abs/2411.12355) · 📚 被引 0
- **作者**: Yudong Han, Qingpei Guo, Liyuan Pan, Liu Liu, Yu Guan, Ming Yang
- **🏷️ 机构**: Beijing Institute of Technology, Ant Group, Huawei,KooMap Dept.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The challenge in LLM-based video understanding lies in preserving visual and semantic information in long videos while maintaining a memory-affordable token count. However, redundancy and correspondence in videos have hindered the performance potential of existing methods. Through statistical learning on current datasets, we observe that redundancy occurs in both repeated and answer-irrelevant frames, and the corresponding frames vary with different questions. This suggests the possibility of adopting dynamic encoding to balance detailed video information preservation with token budget reduction. To this end, we propose a dynamic cooperative network, DynFocus, for memory-efficient video encoding in this paper. Specifically, i) a Dynamic Event Prototype Estimation (DPE) module to dynamically select meaningful frames for question answering; (ii) a Compact Cooperative Encoding (CCE) module that encodes meaningful frames with detailed visual appearance and the remaining frames with sketchy perception separately. We evaluate our method on five publicly available benchmarks, and experimental results consistently demonstrate that our method achieves competitive performance.

</details>

### STOP: Integrated Spatial-Temporal Dynamic Prompting for Video Understanding.
- **链接**: [arXiv:2503.15973](https://arxiv.org/abs/2503.15973) · [代码](https://github.com/zhoujiahuan1991/CVPR2025-STOP) · 📚 被引 6
- **作者**: Zichen Liu, Kunlun Xu, Bing Su, Xu Zou, Yuxin Peng, Jiahuan Zhou
- **🏷️ 机构**: Peking University,Wangxuan Institute of Computer Technology,Beijing,China, Renmin University of China,Gaoling School of Artificial Intelligence,Beijing,China, Huazhong University of Science and Technology,School of Artificial Intelligence and Automation,Wuhan,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained on tremendous image-text pairs, vision-language models like CLIP have demonstrated promising zero-shot generalization across numerous image-based tasks. However, extending these capabilities to video tasks remains challenging due to limited labeled video data and high training costs. Recent video prompting methods attempt to adapt CLIP for video tasks by introducing learnable prompts, but they typically rely on a single static prompt for all video sequences, overlooking the diverse temporal dynamics and spatial variations that exist across frames. This limitation significantly hinders the model's ability to capture essential temporal information for effective video understanding. To address this, we propose an integrated Spatial-TempOral dynamic Prompting (STOP) model which consists of two complementary modules, the intra-frame spatial prompting and inter-frame temporal prompting. Our intra-frame spatial prompts are designed to adaptively highlight discriminative regions within each frame by leveraging intra-frame attention and temporal variation, allowing the model to focus on areas with substantial temporal dynamics and capture fine-grained spatial details. Additionally, to highlight the varying importance of frames for video understanding, we further introduce inter-frame temporal prompts, dynamically inserting prompts between frames with high temporal variance as measured by frame similarity. This enables the model to prioritize key frames and enhances its capacity to understand temporal dependencies across sequences. Extensive experiments on various video benchmarks demonstrate that STOP consistently achieves superior performance against state-of-the-art methods. The code is available at https://github.com/zhoujiahuan1991/CVPR2025-STOP.

</details>

### DrVideo: Document Retrieval Based Long Video Understanding.
- **链接**: [arXiv:2406.12846](https://arxiv.org/abs/2406.12846) · 📚 被引 15
- **作者**: Ziyu Ma, Chenhui Gou, Hengcan Shi, Bin Sun, Shutao Li, Hamid Rezatofighi et al.
- **🏷️ 机构**: Hunan University,College of Electrical and Information Engineering, Monash University,Faculty of IT,Data Science &#x0026; AI Department
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of the existing methods for video understanding primarily focus on videos only lasting tens of seconds, with limited exploration of techniques for handling long videos. The increased number of frames in long videos poses two main challenges: difficulty in locating key information and performing long-range reasoning. Thus, we propose DrVideo, a document-retrieval-based system designed for long video understanding. Our key idea is to convert the long-video understanding problem into a long-document understanding task so as to effectively leverage the power of large language models. Specifically, DrVideo first transforms a long video into a coarse text-based long document to initially retrieve key frames and then updates the documents with the augmented key frame information. It then employs an agent-based iterative loop to continuously search for missing information and augment the document until sufficient question-related information is gathered for making the final predictions in a chain-of-thought manner. Extensive experiments on long video benchmarks confirm the effectiveness of our method. DrVideo significantly outperforms existing LLM-based state-of-the-art methods on EgoSchema benchmark (3 minutes), MovieChat-1K benchmark (10 minutes), and the long split of Video-MME benchmark (average of 44 minutes).

</details>

### Towards Universal Soccer Video Understanding.
- **链接**: [arXiv:2412.01820](https://arxiv.org/abs/2412.01820) · 📚 被引 18
- **作者**: Jiayuan Rao, Haoning Wu, Hao Jiang, Ya Zhang, Yanfeng Wang, Weidi Xie
- **🏷️ 机构**: Shanghai Jiao Tong University,School of Artificial Intelligence,China, Alibaba Group,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a globally celebrated sport, soccer has attracted widespread interest from fans all over the world. This paper aims to develop a comprehensive multi-modal framework for soccer video understanding. Specifically, we make the following contributions in this paper: (i) we introduce SoccerReplay-1988, the largest multi-modal soccer dataset to date, featuring videos and detailed annotations from 1,988 complete matches, with an automated annotation pipeline; (ii) we present an advanced soccer-specific visual encoder, MatchVision, which leverages spatiotemporal information across soccer videos and excels in various downstream tasks; (iii) we conduct extensive experiments and ablation studies on event classification, commentary generation, and multi-view foul recognition. MatchVision demonstrates state-of-the-art performance on all of them, substantially outperforming existing models, which highlights the superiority of our proposed data and model. We believe that this work will offer a standard paradigm for sports understanding research.

</details>

### Adaptive Keyframe Sampling for Long Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_Adaptive_Keyframe_Sampling_for_Long_Video_Understanding_CVPR_2025_paper.html) · 📚 被引 30
- **作者**: Xi Tang, Jihao Qiu, Lingxi Xie, Yunjie Tian, Jianbin Jiao, Qixiang Ye
- **🏷️ 机构**: University of Chinese Academy of Sciences, University at Buffalo, SUNY
- **会议**: CVPR 2025

### Re-thinking Temporal Search for Long-Form Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_Re-thinking_Temporal_Search_for_Long-Form_Video_Understanding_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Jinhui Ye, Zihan Wang, Haosen Sun, Keshigeyan Chandrasegaran, Zane Durante, Cristóbal Eyzaguirre et al.
- **🏷️ 机构**: Stanford University, Northwestern University, Carnegie Mellon University
- **会议**: CVPR 2025

### Holmes-VAU: Towards Long-term Video Anomaly Understanding at Any Granularity.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Holmes-VAU_Towards_Long-term_Video_Anomaly_Understanding_at_Any_Granularity_CVPR_2025_paper.html) · 📚 被引 22
- **作者**: Huaxin Zhang, Xiaohao Xu, Xiang Wang, Jialong Zuo, Xiaonan Huang, Changxin Gao et al.
- **🏷️ 机构**: Huazhong University of Science and Technology,Key Laboratory of Image Processing and Intelligent Control, School of Artificial Intelligence and Automation, University of Michigan,Ann Arbor, Kanagawa University
- **会议**: CVPR 2025

### Action Detail Matters: Refining Video Recognition with Local Action Queries.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Action_Detail_Matters_Refining_Video_Recognition_with_Local_Action_Queries_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Mengmeng Wang, Zeyi Huang, Xiangjie Kong, Guojiang Shen, Guang Dai, Jingdong Wang et al.
- **🏷️ 机构**: Zhejiang University of Technology, Huawei, State Grid Corporation of China,SGIT AI Lab
- **会议**: CVPR 2025

### Temporal Alignment-Free Video Matching for Few-shot Action Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Temporal_Alignment-Free_Video_Matching_for_Few-shot_Action_Recognition_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: SuBeen Lee, WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- When the Future Becomes the Past: Taming Temporal Correspondence for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
