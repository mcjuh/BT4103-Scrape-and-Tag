<!-- Source: https://www.thoughtworks.com/insights/blog/generative-ai/putting-nvidia-nemotron-3-5-lightning-test | Title: Putting NVIDIA Nemotron 3.5 Lightning to the test | Thoughtworks | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Putting NVIDIA Nemotron 3.5 Lightning to the test 
Control, customization and speed
[ Engineering Stack Back ](https://www.thoughtworks.com/engineering)
Close


By 
Published: August 11, 2026 
TL;DR:
  * We post-trained NVIDIA Nemotron 3.5 Lightning for legal and healthcare in a few hours on a single node. The legal adapter was preferred over the base model in 75% of blind comparisons and more than doubled accuracy on a public legal benchmark; the healthcare adapter was preferred in 60%.
  * We fine-tuned away two thirds of the model's recognizable 'AI writing' tells with no measurable loss in writing quality, vocabulary or reasoning benchmarks.
  * The model ships with speculative decoding enabled by default, worth 1.5–2x faster generation out of the box.


Always-on agents complete complex, multi-step tasks autonomously and not every step needs the same model. Complex reasoning demands frontier-level capability while high-volume, domain-specific tasks are better handled by specialized models. Agentic AI is becoming a system of models, and the specialized models in that system need three things: accuracy on your domain, output behavior you control and economics that survive always-on operation.
NVIDIA Nemotron 3.5 Lightning, a fully customizable open model, a 30B mixture-of-experts with 3B active parameters distilled from NVIDIA's frontier Nemotron 3 Ultra, is built around exactly those three promises: model control, customizability for highest accuracy and fastest task completion. As an early access partner, we tested all three; this post summarizes what we found. Each section links to a full technical report.
## Domain adaptation: Teaching the model your business
The knowledge that makes your organization different, like contracts, clinical protocols, institutional judgment, sits in a corpus no public model has seen. For most enterprises, that corpus can never leave the building; post-training is how it reaches the model.
We used low-rank adapters: small, trainable 'correction layers' that sit alongside the frozen model and nudge it toward a domain. We trained both adapters concurrently on a single node with eight NVIDIA H100 80GB GPUs, in a few hours, with no data or output leaving our environment.
The deciding test was blind comparison: hundreds of held-out questions answered by both the base and adapted models, scored by an independent AI judge from a different model family that never knew which answer came from which model.
  * **Legal:** the adapted model was preferred in 112 of 163 blind comparisons; a 75% win rate (p < 0.001). On CaseHOLD, a benchmark that asks a model to identify the holding a court actually reached, accuracy more than doubled from 35% to 77%.
  * **Healthcare:** the adapted model was preferred in 82 of 167 blind comparisons; a 60% win rate (p = 0.002). On held-out clinical questions the model never saw in training, its prediction error fell 24% and answer-token accuracy rose from 64% to 69%.
  * **General ability preserved:** the legal adapter held every general-capability check, including reasoning, mathematics and broad legal knowledge, to within 1.5 points of the base model.


Building a specialized model took an afternoon; this wasn't a months-long project. That cost profile is what makes a system of models realistic: a specialized model per domain, each one trained on data that defines your advantage and cannot go to a third-party API. 
**Read the[post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains technical report](https://research.thoughtworks.com/library/post-training-nvidia-nemotron-3-5-lightning-enterprise-domains). **
## Behavioral tuning: Teaching the model to stop writing like a model
Customization isn't only about what a model knows; it's also about how it writes. Readers have developed a reliable instinct for machine-made text, built on phrases models overuse. Some appear more than a thousand times more often in model output than in human writing. For any agent whose output reaches customers, such as support responses, product copy or reports, that synthetic signature is a quality problem benchmarks don't capture.
Using our published, MIT-licensed [antislop framework](https://arxiv.org/pdf/2510.15061), we profiled the model's own verbal tics (4,267 overused patterns), generated ~13,000 targeted training examples and trained the preferences directly into the weights. This took about thirteen hours on two NVIDIA H100 80GB GPUs.
When evaluated on 400 held-out prompts with all inference-time assistance switched off:
  * **66.4% of the identified overused patterns were eliminated.**
  * **Writing quality was statistically unchanged** , scored by an independent judge on a six-part rubric.
  * **Vocabulary richness held at 98.4% of baseline.** Where conventional preference-training methods collapsed it to as low as 74%, the model found different phrasings rather than retreating to fewer words.
  * **Reasoning remained intact.** General knowledge and math benchmarks both came out marginally higher.


The same open weights that accept a domain adapter also accept this kind of fine-grained behavioral tuning. That's what 'fully customizable' means in practice.
**Read the[teaching a model to stop writing like a model technical report](https://research.thoughtworks.com/library/teaching-model-stop-writing-like-model).**
### Antislopped model agentic benchmarks
MMLU and GSM8K are both several years old, and neither is agentic. Neither one tests whether a model can carry out multi-step work using tools, which is how most people actually deploy these models now. So we ran a second round on harder and more current evaluations.
The most relevant of these is τ-bench. It places the model in a customer service role, hands it a set of tools that read and write to a mock company database and has a separate language model play the customer. Scoring a point means completing the customer’s actual request correctly, which typically takes ten or more conversational turns and several chained tool calls, with the model needing to look up the right records before acting on them. We ran both the retail and airline domains, three trials each, for a total of 495 task attempts per model.  
Table showing antislopping benchmarks  
|  What we measured  |  Original  |  Antislop  |  Change  |  
| --- | --- | --- | --- |  
|  τ-bench, customer service agent  |  0.640  |  0.624  |  No significant change  |  
|  MMLU-Pro, harder knowledge and reasoning  |  0.703  |  0.713  |  No significant change  |  
|  HumanEval+, code that has to actually run  |  0.750  |  0.707  |  No significant change  |  
|  IFEval, following explicit instructions  |  0.387  |  0.387  |  Identical  |  
Table showing antislopping benchmarks  
|  What we measured  |  
| --- |  
|  τ-bench, customer service agent  |  
|  MMLU-Pro, harder knowledge and reasoning  |  
|  HumanEval+, code that has to actually run  |  
|  IFEval, following explicit instructions  |  
|  Original  |  
| --- |  
|  0.640  |  
|  0.703  |  
|  0.750  |  
|  0.387  |  
|  Antislop  |  
| --- |  
|  0.624  |  
|  0.713  |  
|  0.707  |  
|  0.387  |  
|  Change  |  
| --- |  
|  No significant change  |  
|  No significant change  |  
|  No significant change  |  
|  Identical  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Every one of these differences sits inside the measurement noise (statistically not significant). The confidence interval on the τ-bench comparison runs from roughly seven points down to four points up, so the two models are indistinguishable on it. MMLU-Pro came out marginally ahead for the tuned model. IFEval came out identical to three decimal places, because IFEval measures whether a model obeys explicit output constraints such as word counts, required keywords and formatting rules. If a style-focused fine-tune were going to break something, that ability is exactly where the damage would show, and it's untouched.
Taken together with the creative writing results above, this is the outcome we hoped for. The model writes noticeably less like a machine and performs the same on knowledge, reasoning, code, instruction following and multi-step tool use. Running the identical IFEval prompts twice through the identical model at temperature zero gave 0.4025 and 0.3870, because the serving stack batches requests in ways that make even greedy decoding slightly non-deterministic. Anything under roughly two points here is unmeasurable, whatever the point estimates happen to say. For the same reason we ran τ-bench across three trials rather than one, since a single pass over a fifty-task domain carries more than ten points of sampling noise on its own.
## Inference speed: An accelerator you don't have to build
Speed is the third leg, because always-on agents generate tokens continuously and every token is GPU time. Speculative decoding is the standard acceleration: a small, fast drafter guesses the next few tokens and the full model verifies them in one pass, producing identical output faster. Normally, this means training and maintaining a separate draft model.
Nemotron 3.5 Lightning ships with an outstanding speculative decoder built in and enabled by default, via its native multi-token prediction head. Across 2,091 measurements — two inference engines, two GPU generations (H200 and B200), three workloads, concurrency from 1 to 128 — the native head delivered 1.46–1.96× the throughput of unaccelerated decoding, with task accuracy shown equivalent.
There is particularly strong evidence for how good that default is. We trained a state-of-the-art EAGLE-3 draft head specifically for this model, which required engineering work to extend open tooling to support its hybrid Mamba-2 architecture, and it could only match the built-in head overall. A native head this strong is rare; usually a purpose-trained drafter wins comfortably.
The economics follow directly. On self-hosted hardware, cost per token is the reciprocal of throughput, so the built-in acceleration roughly halves GPU cost per generated token under load. In our worked example, there was a decrease from $0.477 to $0.250 per million output tokens. You get that on day one, on stock vLLM, with nothing to train and no second artifact to maintain.
**Read the[speculative decoding for NVIDIA Nemotron 3.5 Lightning technical report](https://research.thoughtworks.com/library/eagle-3-speculative-decoding-nvidia-nemotron-3-5-lightning).**
## Three findings, one story
The three findings are all part of one story. Model control means the entire specialization loop, training, evaluation and deployment, runs inside your environment. Customizability means you can shape both what the model knows and how it writes, cheaply enough to do it per domain. And because an always-on agent is never done generating, speed determines how many agents a given hardware footprint can support.
**An organization starting with NVIDIA Nemotron 3.5 Lightning can pick one domain whose data cannot leave its environment, train a domain-adapted model in hours rather than weeks and deploy it confident it can sustain the pace of always-on agents on modest hardware.**
  * [ Data strategy Semantic drift and semantic integrity: Stewarding meaning in the age of AI  Learn more ](https://www.thoughtworks.com/insights/blog/data-strategy/semantic-drift-stewarding-meaning-ai)
  * [ Generative AI Navigating today’s AI token crisis  Learn more ](https://www.thoughtworks.com/insights/blog/generative-ai/navigating-ai-token-crisis)
  * [ Programming languages Is a codeless future an illusion?  Learn more ](https://www.thoughtworks.com/insights/blog/programming-languages/codeless-future-illusion)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Explore a snapshot of today's tech landscape
[ Read Technology Radar ](https://www.thoughtworks.com/radar)