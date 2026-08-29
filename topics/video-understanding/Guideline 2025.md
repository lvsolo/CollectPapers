# Video Understanding — 2025 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### EgoExoBench: A Benchmark for First- and Third-person View Video Understanding in MLLMs.
- **链接**: [arXiv:2507.18342](https://arxiv.org/abs/2507.18342) · 📚 被引 0
- **作者**: Yuping He, Yifei Huang, Guo Chen, Baoqi Pei, Jilan Xu, Tong Lu et al.
- **🏷️ 机构**: Nanjing University, The University of Tokyo, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transferring and integrating knowledge across first-person (egocentric) and third-person (exocentric) viewpoints is intrinsic to human intelligence, enabling humans to learn from others and convey insights from their own experiences. Despite rapid progress in multimodal large language models (MLLMs), their ability to perform such cross-view reasoning remains unexplored. To address this, we introduce EgoExoBench, the first benchmark for egocentric-exocentric video understanding and reasoning. Built from publicly available datasets, EgoExoBench comprises over 7,300 question-answer pairs spanning eleven sub-tasks organized into three core challenges: semantic alignment, viewpoint association, and temporal reasoning. We evaluate 13 state-of-the-art MLLMs and find that while these models excel on single-view tasks, they struggle to align semantics across perspectives, accurately associate views, and infer temporal dynamics in the ego-exo context. We hope EgoExoBench can serve as a valuable resource for research on embodied agents and intelligent assistants seeking human-like cross-view intelligence.

</details>

### MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs.
- **链接**: [arXiv:2511.07250](https://arxiv.org/abs/2511.07250) · 📚 被引 0
- **作者**: Tianhao Peng, Haochen Wang, Yuanxing Zhang, Noah Wang, Zili Wang, Ge Zhang et al.
- **🏷️ 机构**: Beijing University of Aeronautics and Astronautics, Institute of automation, Chinese Academy of Sciences; University of Chinese Academy of Sciences, Kuaishou- 快手科技
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of Multimodal Large Language Models (MLLMs) has expanded AI capabilities to visual modalities, yet existing evaluation benchmarks remain limited to single-video understanding, overlooking the critical need for multi-video understanding in real-world scenarios (e.g., sports analytics and autonomous driving). To address this significant gap, we introduce MVU-Eval, the first comprehensive benchmark for evaluating Multi-Video Understanding for MLLMs. Specifically, our MVU-Eval mainly assesses eight core competencies through 1,824 meticulously curated question-answer pairs spanning 4,959 videos from diverse domains, addressing both fundamental perception tasks and high-order reasoning tasks. These capabilities are rigorously aligned with real-world applications such as multi-sensor synthesis in autonomous systems and cross-angle sports analytics. Through extensive evaluation of state-of-the-art open-source and closed-source models, we reveal significant performance discrepancies and limitations in current MLLMs' ability to perform understanding across multiple videos. The benchmark will be made publicly available to foster future research.

</details>

### Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding.
- **链接**: [arXiv:2509.15178](https://arxiv.org/abs/2509.15178) · [代码](https://github.com/zaiquanyang/LLaVA_Next_STVG) · 📚 被引 0
- **作者**: Zaiquan Yang, Yuhao Liu, Gerhard P. Hancke, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatio-temporal video grounding (STVG) aims at localizing the spatio-temporal tube of a video, as specified by the input text query. In this paper, we utilize multimodal large language models (MLLMs) to explore a zero-shot solution in STVG. We reveal two key insights about MLLMs: (1) MLLMs tend to dynamically assign special tokens, referred to as \textit{grounding tokens}, for grounding the text query; and (2) MLLMs often suffer from suboptimal grounding due to the inability to fully integrate the cues in the text query (\textit{e.g.}, attributes, actions) for inference. Based on these insights, we propose a MLLM-based zero-shot framework for STVG, which includes novel decomposed spatio-temporal highlighting (DSTH) and temporal-augmented assembling (TAS) strategies to unleash the reasoning ability of MLLMs. The DSTH strategy first decouples the original query into attribute and action sub-queries for inquiring the existence of the target both spatially and temporally. It then uses a novel logit-guided re-attention (LRA) module to learn latent variables as spatial and temporal prompts, by regularizing token predictions for each sub-query. These prompts highlight attribute and action cues, respectively, directing the model's attention to reliable spatial and temporal related visual regions. In addition, as the spatial grounding by the attribute sub-query should be temporally consistent, we introduce the TAS strategy to assemble the predictions using the original video frames and the temporal-augmented frames as inputs to help improve temporal consistency. We evaluate our method on various MLLMs, and show that it outperforms SOTA methods on three common STVG benchmarks. The code will be available at https://github.com/zaiquanyang/LLaVA_Next_STVG.

</details>

### VideoHallu: Evaluating and Mitigating Multi-modal Hallucinations on Synthetic Video Understanding.
- **链接**: [arXiv:2505.01481](https://arxiv.org/abs/2505.01481) · [代码](https://github.com/zli12321/VideoHallu.git) · 📚 被引 0
- **作者**: Zongxia Li, Xiyang Wu, Guangyao Shi, Yubin Qin, Hongyang Du, Tianyi Zhou et al.
- **🏷️ 机构**: University of Maryland, College Park, University of Maryland, University of Southern California
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have achieved strong results in video understanding, yet a key question remains: do they truly comprehend visual content or only learn shallow correlations between vision and language? Real visual understanding, especially of physics and common sense, is essential for AI systems that interact with the physical world. Current evaluations mostly use real-world videos similar to training data, so high benchmark scores may not reflect real reasoning ability. To address this, we propose negative-control tests using videos that depict physically impossible or logically inconsistent events. We introduce VideoHallu, a synthetic dataset of physics- and commonsense-violating scenes generated with Veo2, Sora, and Kling. It includes expert-annotated question-answer pairs across four categories of violations. Tests of leading VLMs (Qwen-2.5-VL, Video-R1, VideoChat-R1) show that, despite strong results on benchmarks such as MVBench and MMVU, they often miss these violations, exposing gaps in visual reasoning. Reinforcement learning fine-tuning on VideoHallu improves recognition of such violations without reducing standard benchmark performance. Our data is available at https://github.com/zli12321/VideoHallu.git.

</details>

### Unleashing Hour-Scale Video Training for Long Video-Language Understanding.
- **链接**: [arXiv:2506.05332](https://arxiv.org/abs/2506.05332) · 📚 被引 1
- **作者**: Jingyang Lin, Jialian Wu, Ximeng Sun, Ze Wang, Jiang Liu, Yusheng Su et al.
- **🏷️ 机构**: University of Rochester, AMD, Boston University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent long-form video-language understanding benchmarks have driven progress in video large multimodal models (Video-LMMs). However, the scarcity of well-annotated long videos has left the training of hour-long Video-LMMs underexplored. To close this gap, we present VideoMarathon, a large-scale hour-long video instruction-following dataset. This dataset includes around 9,700 hours of long videos sourced from diverse domains, ranging from 3 to 60 minutes per video. Specifically, it contains 3.3M high-quality QA pairs, spanning six fundamental topics: temporality, spatiality, object, action, scene, and event. Compared to existing video instruction datasets, VideoMarathon significantly extends training video durations up to 1 hour, and supports 22 diverse tasks requiring both short- and long-term video comprehension. Building on VideoMarathon, we propose Hour-LLaVA, a powerful and efficient Video-LMM for hour-scale video-language modeling. It enables hour-long video training and inference at 1-FPS sampling by leveraging a memory augmentation module, which adaptively integrates question-relevant and spatiotemporally informative semantics from the cached full video context. In our experiments, Hour-LLaVA achieves the best performance on multiple representative long video-language benchmarks, demonstrating the high quality of the VideoMarathon dataset and the superiority of the Hour-LLaVA model.

</details>

### MR. Video: MapReduce as an Effective Principle for Long Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/0a02c2bc2e2148b803c4ade1d71e1d25-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ziqi Pang, Yu-Xiong Wang
- **🏷️ 机构**: UIUC, University of Illinois Urbana-Champaign
- **会议**: NeurIPS 2025

### Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding.
- **链接**: [arXiv:2505.18079](https://arxiv.org/abs/2505.18079) · 📚 被引 0
- **作者**: Xiaoyi Zhang, Zhaoyang Jia, Zongyu Guo, Jiahao Li, Bin Li, Houqiang Li et al.
- **🏷️ 机构**: Microsoft, University of Science and Technology of China, Microsoft Research
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-form video understanding presents significant challenges due to extensive temporal-spatial complexity and the difficulty of question answering under such extended contexts. While Large Language Models (LLMs) have demonstrated considerable advancements in video analysis capabilities and long context handling, they continue to exhibit limitations when processing information-dense hour-long videos. To overcome such limitations, we propose the Deep Video Discovery (DVD) agent to leverage an agentic search strategy over segmented video clips. Unlike previous video agents that rely on predefined workflows applied uniformly across different queries, our approach emphasizes the autonomous and adaptive nature of agents. By providing a set of search-centric tools on multi-granular video database, our DVD agent leverages the advanced reasoning capability of LLM to plan on its current observation state, strategically selects tools to orchestrate adaptive workflow for different queries in light of the gathered information. We perform comprehensive evaluation on multiple long video understanding benchmarks that demonstrates our advantage. Our DVD agent achieves state-of-the-art performance on the challenging LVBench dataset, reaching an accuracy of 74.2%, which substantially surpasses all prior works, and further improves to 76.0% with transcripts. The code has been released at https://github.com/microsoft/DeepVideoDiscovery.

</details>

### VideoLucy: Deep Memory Backtracking for Long Video Understanding.
- **链接**: [arXiv:2510.12422](https://arxiv.org/abs/2510.12422) · 📚 被引 0
- **作者**: Jialong Zuo, Yongtai Deng, Lingdong Kong, Jingkang Yang, Rui Jin, Yiwei Zhang et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, National University of Singapore, MMLab@NTU
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that agent-based systems leveraging large language models (LLMs) for key information retrieval and integration have emerged as a promising approach for long video understanding. However, these systems face two major challenges. First, they typically perform modeling and reasoning on individual frames, struggling to capture the temporal context of consecutive frames. Second, to reduce the cost of dense frame-level captioning, they adopt sparse frame sampling, which risks discarding crucial information. To overcome these limitations, we propose VideoLucy, a deep memory backtracking framework for long video understanding. Inspired by the human recollection process from coarse to fine, VideoLucy employs a hierarchical memory structure with progressive granularity. This structure explicitly defines the detail level and temporal scope of memory at different hierarchical depths. Through an agent-based iterative backtracking mechanism, VideoLucy systematically mines video-wide, question-relevant deep memories until sufficient information is gathered to provide a confident answer. This design enables effective temporal understanding of consecutive frames while preserving critical details. In addition, we introduce EgoMem, a new benchmark for long video understanding. EgoMem is designed to comprehensively evaluate a model's ability to understand complex events that unfold over time and capture fine-grained details in extremely long videos. Extensive experiments demonstrate the superiority of VideoLucy. Built on open-source models, VideoLucy significantly outperforms state-of-the-art methods on multiple long video understanding benchmarks, achieving performance even surpassing the latest proprietary models such as GPT-4o. Our code and dataset will be made publicly at https://videolucy.github.io

</details>

### Temporal Chain of Thought: Long-Video Understanding by Thinking in Frames.
- **链接**: [arXiv:2507.02001](https://arxiv.org/abs/2507.02001) · 📚 被引 0
- **作者**: Anurag Arnab, Ahmet Iscen, Mathilde Caron, Alireza Fathi, Cordelia Schmid
- **🏷️ 机构**: Google DeepMind, Google, INRIA
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite recent advances in Vision-Language Models (VLMs), long-video understanding remains a challenging problem. Although state-of-the-art long-context VLMs can process around 1000 input frames, they still struggle to effectively leverage this sequence length, and succumb to irrelevant distractors within the context window. We present Temporal Chain of Thought, an inference strategy for video question-answering that curates the model's input context. We use the VLM itself to iteratively identify and extract the most relevant frames from the video, which are then used for answering. We demonstrate how leveraging more computation at inference-time to select the most relevant context leads to improvements in accuracy, in agreement with recent work on inference-time scaling of LLMs. Moreover, we achieve state-of-the-art results on 4 diverse video question-answering datasets, showing consistent improvements with 3 different VLMs. In particular, our method shines on longer videos which would not otherwise fit within the model's context window: On longer videos of more than 1 hour on LVBench, our approach using a context window of 32K outperforms the same VLM using standard inference with a 700K context window by 2.8 points.

</details>

### EPFL-Smart-Kitchen: An Ego-Exo Multi-Modal Dataset for Challenging Action and Motion Understanding in Video-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/80644c59e7ea4bc6267a8b62808e8486-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Andy Bonnetto, Haozhe Qi, Franklin Leong, Matea Tashkovska, Mahdi Rad, Solaiman Shokur et al.
- **🏷️ 机构**: EPFL - EPF Lausanne, EPFL - Switzerland, EPFL
- **会议**: NeurIPS 2025

### Generalizing Single-Frame Supervision to Event-Level Understanding for Video Anomaly Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/092a75a70fb3e822ee9f2efb6eefca7f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Junxi Chen, Liang Li, Yunbin Tu, Li Su, Zhe Xue, Qingming Huang
- **🏷️ 机构**: University of the Chinese Academy of Sciences, Alibaba Group, University of Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding.
- **链接**: [arXiv:2503.13139](https://arxiv.org/abs/2503.13139) · 📚 被引 2
- **作者**: Weiyu Guo, Ziyang Chen, Shaoguang Wang, JianXiang He, Yijie Xu, Jinhui Ye et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, Tsinghua University, Tsinghua University, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding long video content is a complex endeavor that often relies on densely sampled frame captions or end-to-end feature selectors, yet these techniques commonly overlook the logical relationships between textual queries and visual elements. In practice, computational constraints necessitate coarse frame subsampling, a challenge analogous to "finding a needle in a haystack." To address this issue, we introduce a semantics-driven search framework that reformulates keyframe selection under the paradigm of Visual Semantic-Logical Search. Specifically, we systematically define four fundamental logical dependencies: 1) spatial co-occurrence, 2) temporal proximity, 3) attribute dependency, and 4) causal order. These relations dynamically update frame sampling distributions through an iterative refinement process, enabling context-aware identification of semantically critical frames tailored to specific query requirements. Our method establishes new SOTA performance on the manually annotated benchmark in key-frame selection metrics. Furthermore, when applied to downstream video question-answering tasks, the proposed approach demonstrates the best performance gains over existing methods on LongVideoBench and Video-MME, validating its effectiveness in bridging the logical gap between textual queries and visual-temporal reasoning. The code will be publicly available.

</details>

### Vid-SME: Membership Inference Attacks against Large Video Understanding Models.
- **链接**: [arXiv:2506.03179](https://arxiv.org/abs/2506.03179) · 📚 被引 0
- **作者**: Qi Li, Runpeng Yu, Xinchao Wang
- **🏷️ 机构**: National University of Singapore
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) demonstrate remarkable capabilities in handling complex multimodal tasks and are increasingly adopted in video understanding applications. However, their rapid advancement raises serious data privacy concerns, particularly given the potential inclusion of sensitive video content, such as personal recordings and surveillance footage, in their training datasets. Determining improperly used videos during training remains a critical and unresolved challenge. Despite considerable progress on membership inference attacks (MIAs) for text and image data in MLLMs, existing methods fail to generalize effectively to the video domain. These methods suffer from poor scalability as more frames are sampled and generally achieve negligible true positive rates at low false positive rates (TPR@Low FPR), mainly due to their failure to capture the inherent temporal variations of video frames and to account for model behavior differences as the number of frames varies. To address these challenges, we introduce Vid-SME, the first membership inference method tailored for video data used in video understanding LLMs (VULLMs). Vid-SME leverages the confidence of model output and integrates adaptive parameterization to compute Sharma-Mittal entropy (SME) for video inputs. By leveraging the SME difference between natural and temporally-reversed video frames, Vid-SME derives robust membership scores to determine whether a given video is part of the model's training set. Experiments on various self-trained and open-sourced VULLMs demonstrate the strong effectiveness of Vid-SME.

</details>

### In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting.
- **链接**: [arXiv:2509.07447](https://arxiv.org/abs/2509.07447) · 📚 被引 0
- **作者**: Taiying Peng, Jiacheng Hua, Miao Liu, Feng Lu
- **🏷️ 机构**: Beihang University, Shanghai Artificial Intelligence Laboratory, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of advanced multimodal large language models (MLLMs) has significantly enhanced AI assistants' ability to process complex information across modalities. Recently, egocentric videos, by directly capturing user focus, actions, and context in an unified coordinate, offer an exciting opportunity to enable proactive and personalized AI user experiences with MLLMs. However, existing benchmarks overlook the crucial role of gaze as an indicator of user intent. To address this gap, we introduce EgoGazeVQA, an egocentric gaze-guided video question answering benchmark that leverages gaze information to improve the understanding of longer daily-life videos. EgoGazeVQA consists of gaze-based QA pairs generated by MLLMs and refined by human annotators. Our experiments reveal that existing MLLMs struggle to accurately interpret user intentions. In contrast, our gaze-guided intent prompting methods significantly enhance performance by integrating spatial, temporal, and intent-related cues. We further conduct experiments on gaze-related fine-tuning and analyze how gaze estimation accuracy impacts prompting effectiveness. These results underscore the value of gaze for more personalized and effective AI assistants in egocentric settings. Project page: https://taiyi98.github.io/projects/EgoGazeVQA

</details>

### Vgent: Graph-based Retrieval-Reasoning-Augmented Generation For Long Video Understanding.
- **链接**: [arXiv:2510.14032](https://arxiv.org/abs/2510.14032) · 📚 被引 0
- **作者**: Xiaoqian Shen, Wenxuan Zhang, Jun Chen, Mohamed Elhoseiny
- **🏷️ 机构**: KAUST, DAMO Academy, Alibaba Group, Facebook
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding and reasoning over long videos pose significant challenges for large video language models (LVLMs) due to the difficulty in processing intensive video tokens beyond context window and retaining long-term sequential information. Retrieval-Augmented Generation (RAG) has demonstrated effectiveness in processing long context for Large Language Models (LLMs); however, applying RAG to long video faces challenges such as disrupted temporal dependencies and inclusion of irrelevant information that can hinder accurate reasoning. To address these limitations, we propose Vgent, a novel graph-based retrieval-reasoning-augmented generation framework to enhance LVLMs for long video understanding. Our approach introduces two key innovations: (i) It represents videos by structured graphs with semantic relationships across video clips preserved to improve retrieval effectiveness. (ii) It introduces an intermediate reasoning step to mitigate the reasoning limitation of LVLMs, which leverages structured verification to reduce retrieval noise and facilitate the explicit aggregation of relevant information across clips, resulting in more accurate and context-aware responses. We comprehensively evaluate our framework with various open-source LVLMs on three long-video understanding benchmarks. Our approach yielded an overall performance improvement of $3.0\%\sim 5.4\%$ over base models on MLVU, and outperformed state-of-the-art video RAG methods by $8.6\%$. Our code is publicly available at https://xiaoqian-shen.github.io/Vgent.

</details>

### UniViT: Unifying Image and Video Understanding in One Vision Encoder.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/69b6de0de842bfedbc40ed6e162b4233-Abstract-Conference.html) · 📚 被引 0
- **作者**: Feilong Tang, Xiang An, Haolin Yang, Yin Xie, Kaicheng Yang, Ming Hu et al.
- **🏷️ 机构**: Monash University, University of Chicago, DEEP GLINT
- **会议**: NeurIPS 2025

### Universal Visuo-Tactile Video Understanding for Embodied Interaction.
- **链接**: [arXiv:2505.22566](https://arxiv.org/abs/2505.22566) · 📚 被引 0
- **作者**: Yifan Xie, Mingyang Li, Shoujie Li, Xingting Li, Guangyu Chen, Fei Ma et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, University of Science and Technology Beijing
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tactile perception is essential for embodied agents to understand physical attributes of objects that cannot be determined through visual inspection alone. While existing approaches have made progress in visual and language modalities for physical understanding, they fail to effectively incorporate tactile information that provides crucial haptic feedback for real-world interaction. In this paper, we present VTV-LLM, the first multi-modal large language model for universal Visuo-Tactile Video (VTV) understanding that bridges the gap between tactile perception and natural language. To address the challenges of cross-sensor and cross-modal integration, we contribute VTV150K, a comprehensive dataset comprising 150,000 video frames from 100 diverse objects captured across three different tactile sensors (GelSight Mini, DIGIT, and Tac3D), annotated with four fundamental tactile attributes (hardness, protrusion, elasticity, and friction). We develop a novel three-stage training paradigm that includes VTV enhancement for robust visuo-tactile representation, VTV-text alignment for cross-modal correspondence, and text prompt finetuning for natural language generation. Our framework enables sophisticated tactile reasoning capabilities including feature assessment, comparative analysis, scenario-based decision making and so on. Experimental evaluations demonstrate that VTV-LLM achieves superior performance in tactile video understanding tasks, establishing a foundation for more intuitive human-machine interaction in tactile domains.

</details>

### AdaVideoRAG: Omni-Contextual Adaptive Retrieval-Augmented Efficient Long Video Understanding.
- **链接**: [arXiv:2506.13589](https://arxiv.org/abs/2506.13589) · 📚 被引 0
- **作者**: Zhucun Xue, Jiangning Zhang, Xurong Xie, Yuxuan Cai, Yong Liu, Xiangtai Li et al.
- **🏷️ 机构**: Zhejiang University (ZJU), Youtu Lab, Tencent, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) perform well in video understanding but degrade on long videos due to fixed-length context and weak long-term dependency modeling. Retrieval-Augmented Generation (RAG) can expand knowledge dynamically, yet existing video RAG schemes adopt fixed retrieval paradigms that ignore query difficulty. This uniform design causes redundant computation and latency for simple queries, while coarse retrieval for complex, multi-hop reasoning can miss key information. Such single-step retrieval severely limits the trade-off between efficiency and cognitive depth. We propose AdaVideoRAG, an adaptive RAG framework for long-video understanding. A lightweight intent classifier dynamically selects suitable retrieval schemes according to query complexity from the simplest to the most sophisticated. We design an Omni-Knowledge Indexing module that extracts and organizes multi-modal information into three databases: (1) a text base built from clip captions, ASR, and OCR; (2) a visual base; and (3) a knowledge graph for deep semantic understanding. This supports hierarchical knowledge access, from naive retrieval to graph-based retrieval, balancing resource cost and reasoning ability. To evaluate deep understanding, we further construct the HiVU benchmark. Experiments show that AdaVideoRAG significantly improves both efficiency and accuracy on long-video QA tasks and can be seamlessly plugged into existing MLLMs through lightweight APIs, establishing a new paradigm for adaptive retrieval-augmented video analysis.

</details>

### LiveStar: Live Streaming Assistant for Real-World Online Video Understanding.
- **链接**: [arXiv:2511.05299](https://arxiv.org/abs/2511.05299) · 📚 被引 0
- **作者**: Zhenyu Yang, Kairui Zhang, Yuhang Hu, Bing Wang, Shengsheng Qian, Bin Wen et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, ShanghaiTech University, Zhengzhou University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite significant progress in Video Large Language Models (Video-LLMs) for offline video understanding, existing online Video-LLMs typically struggle to simultaneously process continuous frame-by-frame inputs and determine optimal response timing, often compromising real-time responsiveness and narrative coherence. To address these limitations, we introduce LiveStar, a pioneering live streaming assistant that achieves always-on proactive responses through adaptive streaming decoding. Specifically, LiveStar incorporates: (1) a training strategy enabling incremental video-language alignment for variable-length video streams, preserving temporal consistency across dynamically evolving frame sequences; (2) a response-silence decoding framework that determines optimal proactive response timing via a single forward pass verification; (3) memory-aware acceleration via peak-end memory compression for online inference on 10+ minute videos, combined with streaming key-value cache to achieve 1.53x faster inference. We also construct an OmniStar dataset, a comprehensive dataset for training and benchmarking that encompasses 15 diverse real-world scenarios and 5 evaluation tasks for online video understanding. Extensive experiments across three benchmarks demonstrate LiveStar's state-of-the-art performance, achieving an average 19.5% improvement in semantic correctness with 18.1% reduced timing difference compared to existing online Video-LLMs, while improving FPS by 12.0% across all five OmniStar tasks. Our model and dataset can be accessed at https://github.com/yzy-bupt/LiveStar.

</details>

### StreamForest: Efficient Online Video Understanding with Persistent Event Memory.
- **链接**: [arXiv:2509.24871](https://arxiv.org/abs/2509.24871) · 📚 被引 0
- **作者**: Xiangyu Zeng, Kefan Qiu, Qingyu Zhang, Xinhao Li, Jing Wang, Jiaxin Li et al.
- **🏷️ 机构**: Nanjing University; Shanghai AI Lab, nanjing university, Nanjing University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have recently achieved remarkable progress in video understanding. However, their effectiveness in real-time streaming scenarios remains limited due to storage constraints of historical visual features and insufficient real-time spatiotemporal reasoning. To address these challenges, we propose StreamForest, a novel architecture specifically designed for streaming video understanding. Central to StreamForest is the Persistent Event Memory Forest, a memory mechanism that adaptively organizes video frames into multiple event-level tree structures. This process is guided by penalty functions based on temporal distance, content similarity, and merge frequency, enabling efficient long-term memory retention under limited computational resources. To enhance real-time perception, we introduce a Fine-grained Spatiotemporal Window, which captures detailed short-term visual cues to improve current scene perception. Additionally, we present OnlineIT, an instruction-tuning dataset tailored for streaming video tasks. OnlineIT significantly boosts MLLM performance in both real-time perception and future prediction. To evaluate generalization in practical applications, we introduce ODV-Bench, a new benchmark focused on real-time streaming video understanding in autonomous driving scenarios. Experimental results demonstrate that StreamForest achieves the state-of-the-art performance, with accuracies of 77.3% on StreamingBench, 60.5% on OVBench, and 55.6% on OVO-Bench. In particular, even under extreme visual token compression (limited to 1024 tokens), the model retains 96.8% of its average accuracy in eight benchmarks relative to the default setting. These results underscore the robustness, efficiency, and generalizability of StreamForest for streaming video understanding.

</details>

### FlexSelect: Flexible Token Selection for Efficient Long Video Understanding.
- **链接**: [arXiv:2506.00993](https://arxiv.org/abs/2506.00993) · 📚 被引 0
- **作者**: Yunzhu Zhang, Yu Lu, Tianyi Wang, Fengyun Rao, Yi Yang, Linchao Zhu
- **🏷️ 机构**: Zhejiang University, National University of Singapore, WeChat, Tencent Inc.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-form video understanding poses a significant challenge for video large language models (VideoLLMs) due to prohibitively high computational and memory demands. In this paper, we propose FlexSelect, a flexible and efficient token selection strategy for processing long videos. FlexSelect identifies and retains the most semantically relevant content by leveraging cross-modal attention patterns from a reference transformer layer. It comprises two key components: (1) a training-free token ranking pipeline that leverages faithful cross-modal attention weights to estimate each video token's importance, and (2) a rank-supervised lightweight selector that is trained to replicate these rankings and filter redundant tokens. This generic approach can be seamlessly integrated into various VideoLLM architectures, such as LLaVA-Video, InternVL and Qwen-VL, serving as a plug-and-play module to extend their temporal context length. Empirically, FlexSelect delivers strong gains across multiple long-video benchmarks including VideoMME, MLVU, LongVB, and LVBench. Moreover, it achieves significant speed-ups (for example, up to 9 times on a LLaVA-Video-7B model), highlighting FlexSelect's promise for efficient long-form video understanding. Project page available at: https://yunzhuzhang0918.github.io/flex_select

</details>

### ReAgent-V: A Reward-Driven Multi-Agent Framework for Video Understanding.
- **链接**: [arXiv:2506.01300](https://arxiv.org/abs/2506.01300) · 📚 被引 1
- **作者**: Yiyang Zhou, Yangfan He, Yaofeng Su, Siwei Han, Joel Jang, Gedas Bertasius et al.
- **🏷️ 机构**: The University of North Carolina at Chapel Hill, JD.com, Fudan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video understanding is fundamental to tasks such as action recognition, video reasoning, and robotic control. Early video understanding methods based on large vision-language models (LVLMs) typically adopt a single-pass reasoning paradigm without dynamic feedback, limiting the model's capacity to self-correct and adapt in complex scenarios. Recent efforts have attempted to address this limitation by incorporating reward models and reinforcement learning to enhance reasoning, or by employing tool-agent frameworks. However, these approaches face several challenges, including high annotation costs, reward signals that fail to capture real-time reasoning states, and low inference efficiency. To overcome these issues, we propose ReAgent-V, a novel agentic video understanding framework that integrates efficient frame selection with real-time reward generation during inference. These reward signals not only guide iterative answer refinement through a multi-perspective reflection mechanism-adjusting predictions from conservative, neutral, and aggressive viewpoints-but also enable automatic filtering of high-quality data for supervised fine-tuning (SFT), direct preference optimization (DPO), and group relative policy optimization (GRPO). ReAgent-V is lightweight, modular, and extensible, supporting flexible tool integration tailored to diverse tasks. Extensive experiments on 12 datasets across three core applications-video understanding, video reasoning enhancement, and vision-language-action model alignment-demonstrate significant gains in generalization and reasoning, with improvements of up to 6.9%, 2.1%, and 9.8%, respectively, highlighting the effectiveness and versatility of the proposed framework.

</details>

### State Space Prompting via Gathering and Spreading Spatio-Temporal Information for Video Understanding.
- **链接**: [arXiv:2510.12160](https://arxiv.org/abs/2510.12160) · 📚 被引 0
- **作者**: Jiahuan Zhou, Kai Zhu, Zhenyu Cui, Zichen Liu, Xu Zou, Gang Hua
- **🏷️ 机构**: Peking University, Renmin University of China, The Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, pre-trained state space models have shown great potential for video classification, which sequentially compresses visual tokens in videos with linear complexity, thereby improving the processing efficiency of video data while maintaining high performance. To apply powerful pre-trained models to downstream tasks, prompt learning is proposed to achieve efficient downstream task adaptation with only a small number of fine-tuned parameters. However, the sequentially compressed visual prompt tokens fail to capture the spatial and temporal contextual information in the video, thus limiting the effective propagation of spatial information within a video frame and temporal information between frames in the state compression model and the extraction of discriminative information. To tackle the above issue, we proposed a State Space Prompting (SSP) method for video understanding, which combines intra-frame and inter-frame prompts to aggregate and propagate key spatiotemporal information in the video. Specifically, an Intra-Frame Gathering (IFG) module is designed to aggregate spatial key information within each frame. Besides, an Inter-Frame Spreading (IFS) module is designed to spread discriminative spatio-temporal information across different frames. By adaptively balancing and compressing key spatio-temporal information within and between frames, our SSP effectively propagates discriminative information in videos in a complementary manner. Extensive experiments on four video benchmark datasets verify that our SSP significantly outperforms existing SOTA methods by 2.76% on average while reducing the overhead of fine-tuning parameters.

</details>

### Disentangled Concepts Speak Louder Than Words: Explainable Video Action Recognition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a5e146ca55a2b18be41942cfa677123d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jongseo Lee, Wooil Lee, Gyeong-Moon Park, Seong Tae Kim, Jinwoo Choi
- **🏷️ 机构**: Kyung Hee University, Korea University
- **会议**: NeurIPS 2025

### Storyboard-guided Alignment for Fine-grained Video Action Recognition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/528388f1ad3a481249a97cbb698d2fe6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Enqi Liu, Liyuan Pan, Yan Yang, Yiran Zhong, Zhijing Wu, Xinxiao Wu et al.
- **🏷️ 机构**: Beijing Institute of Technology, Australian National University, Shanghai AI Lab
- **会议**: NeurIPS 2025

## 跨领域论文（完整笔记在其他领域）

- Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- InfiniPot-V: Memory-Constrained KV Cache Compression for Streaming Video Understanding. → [network-pruning](../network-pruning/Guideline%202025.md)
- One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding. → [network-pruning](../network-pruning/Guideline%202025.md)
- FastVID: Dynamic Density Pruning for Fast Video Large Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
