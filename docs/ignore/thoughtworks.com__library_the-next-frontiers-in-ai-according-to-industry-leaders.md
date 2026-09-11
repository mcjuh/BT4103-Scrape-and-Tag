<!-- Source: https://research.thoughtworks.com/library/the-next-frontiers-in-ai-according-to-industry-leaders | Title: The next frontiers in AI according to industry leaders | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# The next frontiers in AI according to industry leaders
By 
Published: June 04, 2025 
Trying to follow changes in the world of AI — and generative AI in particular — is challenging. However, AI events and keynote speeches in particular are exceptionally useful for understanding the key narrative threads and emerging trends. 
Based on watching a number of keynotes from the last nine months or so, the key trends we think are particularly important are: 
  * The possibility that LLMs are an ‘off-ramp’ on the path to artificial general intelligence (AGI). 
  * Alternatives to transformer-based architectures.
  * Hardware innovation and AI evolution.
  * The mainstreaming of agentic AI.
  * Open-source AI.
  * Physical AI and world models.


Let’s take a look at each of these in more detail.
### Are LLMs an off ramp on the path to AGI?
While LLMs have been the main focus of attention when it comes to AI today, researcher Francois Chollet has suggested that they’re [something of a distraction](https://www.freethink.com/robots-ai/arc-prize-agi) when it comes to the bid to create artificial general intelligence (AGI). Speaking on the Dwarkesh podcast, he argued that “OpenAI… set back progress to AGI by five to 10 years.”
While Chollet’s claim might sound combative, Meta’s Yann LeCun defended his argument. Speaking at [NVIDIA GTC 2025](https://www.nvidia.com/en-us/on-demand/session/gtc25-s73208/) alongside NVIDIA’s Chief Scientist Bill Dally, he said:
“Today’s LLMs are typically trained by 30 trillion tokens. Each token is typically three bytes long. So in total there are 10¹⁴ bytes. This will take any average human nearly 400,000 years to complete the reading - the content of the entire internet. A psychologist believes that a four year old is awake for nearly 16,000 hours in its life. It transfers ~ two Mbps of data to the visual cortex through the optic nerve. If we multiply this by 16,000 hours times 3600 (seconds of an hour), then it is roughly 10¹⁴ bytes in four years through the vision. So we “see” as much data as text that would take us 400,000 hours to “read”! It means that we will never reach AGI by training LLMs from text-only data.”
**_Yann LeCun_**
**_Chief Scientist, Meta_**
In other words, LLMs are insufficient in the pursuit of AGI. Of course, whether AGI is desirable or, indeed, if it’s possible at all, are other debates to be had, but what matters is that current interest in LLMs certainly won’t be the start of a path towards anything resembling AGI.
### Alternatives to transformer-based architectures 
Transformer-based architectures dominate the AI landscape. This is because of their attention mechanism, which has several strengths, including scalability, parallel processing tokens, fine-tuning for domain-specific data and handling multimodality. 
However, they nevertheless have some significant limitations:
  * They’re quadratic in context length, which is compute-intensive and slow.
  * Interactions between tokens are restricted to pairwise attention via dot products, which limits the model’s ability to represent higher-order relationships.
  * They lack any mechanism for combining multiple tokens into higher-level abstractions or complex interactions. 


These limitations are leading to a resurgence in alternative paradigms, most notably Long Short-Term Memory. More specifically, we’re seeing something called Matrix Long Short-Term Memory (mLSTM). These are versions of LSTMs that apply matrix-based memory representations, which makes them not only faster but also more energy-efficient than transformer models. They address several scalability and latency challenges that AI developers and researchers are trying to overcome.
Speaking at [NeurIPS at the end of 2024](https://neurips.cc/virtual/2024/invited-talk/101129), Sepp Hochreiter — the inventor of LSTM — highlighted the urgency of rethinking how AI systems think. He called for models that actually deliberate before producing an output. He spoke, for instance, of “a new series of AI models designed to spend more time thinking before responding is the need of the hour. The high speed of inference will matter in the future.” 
xLSTM-7B, a state-of-the-art open-source model, exemplifies this shift. As one of the most promising transformer alternatives, it may shape the next phase of generative AI design.
### The foundational AI hardware of the future 
Generative AI's progress is deeply rooted in hardware innovation. In the last ten years, computational power has increased dramatically — by factors ranging from 5x to 10,000x. This has enabled breakthroughs in both model training and inference. Advanced reasoning approaches like Chain of Thought, Best-of-n sampling, path planning, and consistency validation have succeeded largely due to this exponential leap in computation.
The shift in architectural strategy — from scaling out to scaling up — has delivered transformative gains in performance. Today, the computational load required for agentic AI and complex reasoning is estimated to be 100x more than previously anticipated. Meeting this surge in demand, leading cloud providers — AWS, Azure, GCP and OCI — have already deployed a combined total of 1.3 million Hopper GPUs and 3.6 million Blackwell GPUs, with rapid expansion still underway.
On the other hand, we are witnessing the peak of what digital CMOS (Complementary Metal Oxide Semiconductor) technology can offer. After decades of refinement, it now delivers extraordinary compute power with massive capital efficiency. Google’s next-generation TPUs exemplify this evolution — offering a 3,600x increase in compute compared to their 2018 predecessors. The latest TPU pods pack over 9,000 chips, driving 42.5 exaflops per pod while using 29% less power built specifically to meet the rising demands of generative and agentic AI. To contextualize, that’s 24 times more performance than today’s leading supercomputer.
Yet, as we look beyond CMOS, the next frontier could be neuromorphic computing — hardware modeled on the architecture of the brain. Spiking nets, the biological blueprint of our cognitive systems, communicate through binary spikes, offering the potential for energy-efficient, event-driven AI. 
But the promise comes with significant technical challenges. Unlike digital systems, analog neuromorphic chips cannot multiplex, requiring one physical neuron for every virtual neuron. Given the scale of modern AI models, building such systems on a single chip is impractical. Scaling across chips introduces even more complexity, reducing system efficiency and reliability. In short, while CMOS remains dominant today, the seeds of post-silicon computing are being sown. 
In pursuit of scalable, AI-first infrastructure, Google has announced a $75 billion capital expenditure aimed at strengthening its AI server fleet and cloud backbone. The initiative accelerates an open, interoperable multi-cloud platform, where AI agents can integrate directly into enterprise environments — interfacing with legacy databases, business applications and external AI models. Notably, by the end of 2025, cloud infrastructure will lead the market by adopting NVIDIA’s cutting-edge Vera Rubin GPUs, offering 50 petaflops of FP4 inference performance, setting a new standard for real-time AI performance at scale.
### The open-source AI revolution
Turning innovation in AI into truly impactful technology requires robust compute- infrastructure. In turn, that requires substantial capital investment. 
The future of foundational AI lies in open-source consensus models, collaboratively trained across distributed global data centers, each with access to distinct datasets. This approach allows for decentralized, transparent, and inclusive development of AI models, enabling richer capabilities and reducing monopolistic control over foundational AI technologies. These models will enable flexible adaptation across vertical industries. 
A case in point is Isaac Groot N1 — a recent open-source humanoid intelligence model developed jointly by NVIDIA, Google DeepMind and Disney Research. With built-in reasoning and a next-generation Newtonian physics engine, it is a benchmark for AI-human embodiment. As open-source platforms scale, they may outlast proprietary stacks, especially in the development of multilingual LLMs that cater to culturally and linguistically diverse populations in real time—ushering in a new paradigm of globally accessible AI. 
Extending this open-source momentum, frameworks like the Agent Development Kit (ADK) are central to the rise of agentic AI. ADK enables the creation of multi-agent systems with modular ease and supports the [Model Context Protocol (MCP)](https://www.thoughtworks.com/insights/blog/generative-ai/model-context-protocol-beneath-hype) — a standardized approach allowing AI models to access and operate across diverse tools and data sources efficiently. 
Today there are a few prominent open-source Generative AI models across different domains:
  * Text generation: Mixtral 7B by Mistral, LLaMA-2 by Meta, and Phi-2 by Microsoft
  * Image generation: Stable Diffusion by Stability AI, and Kandinsky 2.2 by Sberbank
  * Video and animation: ModelScope by Alibaba DAMO


### Agents everywhere
The trajectory of computing has evolved — from retrieval-based paradigms to generative models and now toward agentic computing, a domain centered on autonomous reasoning. This transition marks the rise of agentic AI, where decision-making and contextual understanding take precedence.
Speaking at [an AI conference in February 2025](https://underline.io/lecture/115522-ai-agents-and-applications), Andrew Ng, DeepLearning founder, talked about this at length.
Specifically, he highlighted that software agents are at the core of this model. They exhibit sophisticated behaviors: strategic planning, causal reasoning, persistent memory and adaptive tool use. They are capable of multi-step execution and collaborative task completion. Currently, five agent types are already proving transformative in enterprise and operational settings.
  1. Customer agents are multimodal systems that understand and reason across text, audio, images and video. They engage in natural conversations, integrate with enterprise systems and act on users’ behalf — appearing in contact centers, devices, websites and vehicles. For example, Google's Contact Center 
  2. Creative agents assist in artistic tasks by generating ideas, supporting prototyping and speeding up content creation—helping reduce production time and accelerate time-to-market. For instance, Runway’s Gen-2 enables video creators to generate scenes from text or still images, cutting down visual effects production time.
  3. Data agents identify relevant data, frame the right questions and activate insights. Tools like BigQuery unify structured and unstructured data using open formats such as Apache Iceberg. These agents support roles from data engineers to analysts across storage systems and cloud platforms. Example: Google Cloud's Looker Studio uses AI agents to suggest visualizations and explore data automatically.
  4. Coding agents help write, debug and maintain code. AI tools like Gemini, Aider, Cursor and GitHub Copilot streamline software development — from prototyping to production and maintenance. GitHub Copilot, for example, auto-suggests code snippets as developers type, speeding up implementation and reducing errors.
  5. Security agents handle malware detection and threat analysis, as well as real-time alert triage to strengthen cybersecurity operations. Microsoft Security Copilot helps analysts identify, prioritize, and respond to cyber threats faster using threat intelligence and language models.


Today’s agentic AI is still in its early stages but already exhibits four emerging design patterns: reflection, tool use, strategic planning and multi-agent collaboration. Looking ahead, self-improving AI agents are no longer science fiction — they are an imminent and plausible reality.
### Physical AI
The logical successor to agentic AI is physical AI — intelligent robotic systems capable of perceiving, reasoning and acting in the real world. Unlike software agents confined to digital domains, robots bring cognition into physical form. 
Speaking at [NVIDIA’s AI Summit in India in October 2024](https://www.youtube.com/live/_waPvOwL9Z8), Jensen Huang forecast that by 2030, a global labor shortfall of at least 15 million will be offset by general-purpose robots, marking the arrival of physical AI at industrial scale.
Training these systems poses significant challenges. Unlike LLMs, robots require control and action data, which is costly and time-consuming to acquire. To overcome this, developers must collect real-world sensor datasets and expand them through synthetic data generation. These synthetic environments are then used to train robot policies through imitation learning or reinforcement learning. However, synthetic success must translate to the real world. This demands rigorous validation via digital twins, simulating dynamics, sensors, and environmental variability using software/hardware-in-the-loop testbeds before deployment.
Collaboration among multiple robots is becoming central to robotics, powered by shared post-training policies. The field is advancing toward generalist humanoid foundation models trained on synthetic data and simulations. Meanwhile, robots themselves are generating synthetic data to pre-train AI models — flipping the traditional pipeline.
Inspired by human cognition, slow thinking lets robots understand and plan, while fast thinking enables fluid, real-time action.
AI architecture is changing due to falling compute costs. GenAI's processing ($40/GB) used to dominate over data transfer (~$0.10/GB), but hardware advances now enable distributed small language models (SLMs), fostering modular, decentralized software architectures. This amplifies the role of data engineering, particularly for large-scale unstructured content.
In the near future, professionals like recruiters, marketers and financial analysts will use GenAI to amplify productivity by an order of magnitude — coding, analyzing and deploying smarter tools.
However, AI misuse remains a concern—deep fakes and disinformation can cause real harm. The solution lies in reasoning-capable AI that can evaluate the trustworthiness of its own outputs. 
### AI factories
In the same talk at AI Summit in India, Huang also argued that we’ve entered a new era in computing. This future, he went on to claim, requires radical rethinking as we move away from hand-crafted software on general-purpose machines toward machine learning-driven software executed on GPUs and dedicated accelerators. 
Future systems, he said, will not rely on traditional programming. Instead, they will generate tokens. These AI-driven systems, or “AI factories,” will operate on the next-generation of open-source operating systems which will have been purpose-built for autonomous software generation.
An AI factory, according to Huang, is a data center optimized for AI. It ingests data, trains AI models to output new models, decisions, services or products. Jensen Huang claims data is the new raw material, and AI models are the new products.
Key components of AI factories:
  1. Data as the raw material. Just as factories use raw materials, AI factories consume large-scale data to produce intelligence.
  2. Massive computing power. AI factories will be powered by GPUs (like H100s), optimized for large-scale model training and inference.
  3. AI infrastructure software. An AI software stack (e.g., NVIDIA AI Enterprise, DGX Cloud, CUDA) will be used to manage and accelerate workloads.
  4. Model training and deployment. AI factories will take a key role in creating foundation models and deploy them across various domains. 
  5. Automation and orchestration. AI workflows will be highly automated, with software managing data pipelines, training cycles and deployment.
  6. Scalable outputs. The end product will be either generalist or specialist AI that can power apps, robots, digital twins and enterprise solutions.


However, sceptics point the following pitfalls on the concept and operation of AI factories:
  * Over-reliance on GPU-centric architectures.
  * “Tokens as atomic software units” are not fully defined.
  * Autonomous software may lack accountability and robust safety measures .


Simultaneously, the world is witnessing a profound shift in data center strategy. It’s no longer about how many data centers are built, but instead how they are powered. In a world where every facility is constrained by power, energy becomes the currency of compute. Revenue is now tightly coupled with available electrical capacity, positioning computing squarely as a power-limited industry.
### Joint Embedding Predictive Architecture (JEPA): An innovative new approach
In biological systems, ‘world models’ represent mental simulations of the physical world. They’re used to anticipate outcomes, plan actions and reason about environments. Joint Embedding Predictive Architecture (JEPA) is a self-supervised learning framework that distinguishes itself by predicting abstract representations rather than predicting the next token. In AI, world models are gaining traction as a potential successor to LLMs, offering a more generalized and grounded approach. 
LeCun points out that many real-world phenomena are unpredictable at fine-grained levels. Models that attempt pixel-level prediction often fail by generating implausible detail. Thus, using self-supervised learning to predict video frames directly is not viable—unless the system learns at the level of abstract representations.
JEPA utilizes self-supervised learning and energy-based models to predict abstract representations of future states, focusing on the underlying dynamics and structure of the world. This approach contrasts with large language models (LLMs), which primarily rely on statistical patterns in text data to generate tokens.
“Within three to five years,” LeCun said, “we’ll have a much better paradigm for systems that can reason and plan”.
### Keeping your eyes on the AI horizon
There’s lots happening across the AI industry; trying to summarize it effectively would be immensely difficult — even with an exceptionally effective LLM! However, there are clearly some key throughlines: from model architecture and hardware to the industrial application of AI, innovation and experimentation is happening on a number of different fronts. 
Anyone that’s been trying to stay on top of this exciting field will know all too well just how challenging it is; it’s probably only going to get harder in the years to come. However, at their best, industry events provide a valuable glimpse into what leaders think is important and where they think our attention should be focused. While there’s undoubtedly always commercial imperatives somewhere in their pronouncements, it’s still worth listening with both critical distance and an open mind.