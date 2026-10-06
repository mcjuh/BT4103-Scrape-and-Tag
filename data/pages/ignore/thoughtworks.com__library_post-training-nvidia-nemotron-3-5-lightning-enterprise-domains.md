<!-- Source: https://research.thoughtworks.com/library/post-training-nvidia-nemotron-3-5-lightning-enterprise-domains | Title: Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains
By 
Published: August 11, 2026 
## 1. Summary
Open models give an enterprise control over its AI stack, and the knowledge that distinguishes one organization from another sits in a corpus no public model has been trained on. Applying a model to that corpus without the corpus leaving a trusted environment is the reason to self-host it.
Post-training is how that corpus reaches the model. NVIDIA describes Nemotron 3.5 Lightning as a model that can be post-trained for specialized workflows to improve accuracy on specialized tasks. This work measures how far that goes on real domain data, and what it costs. Two adapters were trained, one on legal text and one on clinical text, on a single self-hosted node from which no corpus and no generation left.
Legal and healthcare are the two domains enterprises most often want a private model for, and they are difficult in different ways. Legal work turns on the exact wording of a clause or a holding, and its public benchmarks reflect that: CaseHOLD asks a model to pick which holding a court actually reached from several plausible alternatives, and LegalBench collects more than a hundred tasks written by practicing lawyers. Healthcare asks instead for recall under constraint, and its benchmarks are mostly examinations: PubMedQA poses yes-or-no questions over biomedical abstracts, MedQA is drawn from the US medical licensing exams, MedMCQA from Indian medical entrance exams. A useful adapter has to move the domain without disturbing the general ability the model already has, and both kinds of movement are measured here.
Both adapters end up ahead of the base model, and healthcare took two attempts to get there. The result worth carrying away is why the first attempt failed: across four training configurations, the cheapest signal a training run reports for free ranked them in exactly the opposite order to answer quality, and selecting on it would have shipped the worst of the three healthcare adapters.
Every comparison in this document is this model against itself, on data held out from training. That keeps the question to what post-training adds, which is the question an organization deciding whether to do this actually has.
### 1.1 Headline
We trained two adapters, one on legal text and one on clinical text, in a few hours on a single node, and both finished ahead of the base model on blind comparison. Choosing between candidates turned out to be harder than training them. A training run reports two numbers for free, held-out loss and token accuracy on data the model never saw, and both appear below; neither says whether an answer is any good. So we added the measurement that decided what shipped: a few hundred answers from the base model and from each adapter on the same held-out questions, handed to an independent judge in both orders, which picks the better answer without being told which model produced it. 
The judge is Claude Opus 5, chosen from a different model family than the one under test, and a base-against-base control establishes what it scores when both answers come from the same model, so any departure from that reference measures the adapter rather than the judge's habits. Throughout this piece, bold marks a statistically significant improvement over the base model.  
Table showing headline findings  
|  Quantity  |  Legal  |  Healthcare, shipped  |  Healthcare, first attempt  |  
| --- | --- | --- | --- |  
|  Training budget  |  500 steps at 1e-4  |  100 steps at 3e-5  |  500 steps at 1e-4  |  
|  Judged win rate  |  **0.7546**  |  **0.6048**  |  0.3413  |  
|  <0.001  |  0.002  |  <0.001  |  
|  Control reference  |  0.4908  |  0.4581  |  0.4581  |  
|  Held-out domain loss  |  1.5777 to 0.9700  |  1.5034 to 1.1407  |  1.5034 to 0.9734  |  
|  Held-out domain accuracy  |  0.6472 to 0.7342  |  0.6437 to 0.6883  |  0.6437 to 0.7212  |  
|  Public domain task  |  CaseHOLD **+42.4 pts** , n=3,600  |  not measured  |  PubMedQA −0.6 pts, n=500  |  
|  Held-out generalization  |  LegalBench +2.69 pts  |  not measured  |  not measured  |  
|  Arithmetic guardrail, n=400  |  −1.0 pts  |  −5.25 pts  |  −4.25 pts  |  
|  Repetition loops  |  36.8% to 3.1%  |  not measured  |  13.8% to 0.6%  |  
Table showing headline findings  
|  Quantity  |  
| --- |  
|  Training budget  |  
|  Judged win rate  |  
|  Control reference  |  
|  Held-out domain loss  |  
|  Held-out domain accuracy  |  
|  Public domain task  |  
|  Held-out generalization  |  
|  Arithmetic guardrail, n=400  |  
|  Repetition loops  |  
|  Legal  |  
| --- |  
|  500 steps at 1e-4  |  
|  **0.7546**  |  
|  <0.001  |  
|  0.4908  |  
|  1.5777 to 0.9700  |  
|  0.6472 to 0.7342  |  
|  CaseHOLD **+42.4 pts** , n=3,600  |  
|  LegalBench +2.69 pts  |  
|  −1.0 pts  |  
|  36.8% to 3.1%  |  
|  Healthcare, shipped  |  
| --- |  
|  100 steps at 3e-5  |  
|  **0.6048**  |  
|  0.002  |  
|  0.4581  |  
|  1.5034 to 1.1407  |  
|  0.6437 to 0.6883  |  
|  not measured  |  
|  not measured  |  
|  −5.25 pts  |  
|  not measured  |  
|  Healthcare, first attempt  |  
| --- |  
|  500 steps at 1e-4  |  
|  0.3413  |  
|  <0.001  |  
|  0.4581  |  
|  1.5034 to 0.9734  |  
|  0.6437 to 0.7212  |  
|  PubMedQA −0.6 pts, n=500  |  
|  not measured  |  
|  −4.25 pts  |  
|  13.8% to 0.6%  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
  * **Legal.** The adapter is preferred in 112 of 163 judged domain comparisons against 29 losses. It more than doubles CaseHOLD accuracy, gains on two of nineteen held-out LegalBench tasks it never trained on without moving the benchmark as a whole, and holds every regression guardrail to a movement of 1.5 points or less, against an equivalence margin that 400 items support only at about five to seven points.


  * **Healthcare.** The shipped adapter is preferred in 82 of 167 comparisons against 47 losses. The first configuration, trained on the identical corpus with the identical target modules for five times as many steps at three times the learning rate, was preferred in 46 against 99.


### 1.2 An inversion between loss and answer quality
The most useful thing we learned was not about either domain. It was about how to tell a good adapter from a bad one, and it runs opposite to the signal that is cheapest to read. Across the three adapters, which span a seventeen-fold range of total optimizer travel, held-out domain loss and judged answer quality move in opposite directions. The state with the lowest held-out loss and the highest token accuracy of any state measured is the one the judge ranks last. The state with the highest loss of the three adapters is the only healthcare adapter that beats the base model.
Selecting a configuration on held-out loss, which is the cheapest signal available and the one a training run reports for free, would have shipped the worst of the three healthcare adapters. _Section 7_ gives the ladder.
One cost does not respond to configuration. Arithmetic accuracy falls at least 4.25 points, and at most 6.00, on every healthcare adapter measured, at every training budget tested. That is a property of the corpus rather than of the schedule;  _Section 9_ records it as unresolved.
## 2. The system under test
Two things bound what a domain adapter can achieve here: the model it attaches to, and the rules we set for measuring it.
### 2.1 Target model
NVIDIA describes Nemotron 3.5 Lightning as a customizable open model that gives control over always-on agents, trained for popular agent harnesses, delivering leading out-of-the-box accuracy for agentic tasks, and able to be post-trained for specialized workflows to improve accuracy on specialized tasks. It is a 30B mixture-of-experts model with 3B active parameters, multi-token prediction and 1M context, built for long-running multi-turn work.
The architecture matters here because it determines what an adapter can reach. Of its 52 layers, 23 are Mamba-2 state-space layers, 23 are mixture-of-experts, and 6 are full attention, at indices 5, 12, 19, 26, 33 and 42. Each mixture-of-experts layer holds 128 routed experts plus one shared expert that every token passes through. Hidden size is 2688 and the vocabulary is 131,072. The checkpoint measured here is an early-access build in bf16, and it is the same artifact the companion speculative-decoding write-up measures; both documents identify it by the per-file SHA256 manifest digest 64624ed9…c746a0.
### 2.2 Scope of this work
This document measures domain-knowledge post-training. No agentic benchmark, tool-use benchmark or multi-turn harness was run, so nothing here speaks to the model's performance as an agent. Of the capability areas this model is positioned for, this work touches reasoning only, through GSM8K and ARC-Challenge used as regression guardrails.
All measurements are bf16 at sequence length 4096, single-turn. The model advertises context up to 1M; no long-context claim is made. Adapters were trained and evaluated on one node, and no corpus or generation left it.
### 2.3 Hardware and software
One node did everything, training and evaluation alike, and every version below is pinned because two of them turned out to matter:  
Hardware and software used in the experiment  
|  Component  |  Value  |  
| --- | --- |  
|  Node  |  p5.48xlarge, 8 × H100 80 GB, us-east-2a  |  
|  Driver  |  580.126.09  |  
|  Training  |  torch 2.9.1+cu128, transformers 4.57.6, peft 0.20.0, accelerate 1.14.0, FSDP2 full-shard  |  
|  Serving and scoring  |  vLLM 0.25.1, lm-eval 0.4.12  |  
|  Judge  |  Claude Opus 5, accessed by API  |  
Hardware and software used in the experiment  
|  Component  |  
| --- |  
|  Node  |  
|  Driver  |  
|  Training  |  
|  Serving and scoring  |  
|  Judge  |  
|  Value  |  
| --- |  
|  p5.48xlarge, 8 × H100 80 GB, us-east-2a  |  
|  580.126.09  |  
|  torch 2.9.1+cu128, transformers 4.57.6, peft 0.20.0, accelerate 1.14.0, FSDP2 full-shard  |  
|  vLLM 0.25.1, lm-eval 0.4.12  |  
|  Claude Opus 5, accessed by API  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
## 3. Method
How this was measured mattered more than how it was trained, because the cheapest signal turned out to be misleading and the design is what caught it.
### 3.1 Measurement design
Published evidence indicates that public multiple-choice benchmarks respond weakly to modest domain adaptation. A legal model gained 3 to 4 points on MMLU law subsets from 30B legal tokens, and across seven medical models domain adaptation beat the base model in about one third of comparisons. NVIDIA's own guidance states that standard academic datasets often fail to meet the distinctive requirements of enterprises. The measurement was therefore tiered, with Tier 1 as the deciding tier and Tier 3 as a parity check.  
Table showing research questions  
|  Tier  |  Question  |  Instruments  |  
| --- | --- | --- |  
|  Does the model improve on the organization's own held-out data?  |  Held-out loss and assistant-token accuracy; pairwise judged win rate  |  
|  Do public tasks in the domain respond?  |  CaseHOLD for legal, PubMedQA for healthcare  |  
|  Was general capability preserved?  |  MMLU professional law, MedQA, MedMCQA, ARC-Challenge, GSM8K  |  
Table showing research questions  
|  Tier  |  
| --- |  
|  Question  |  
| --- |  
|  Does the model improve on the organization's own held-out data?  |  
|  Do public tasks in the domain respond?  |  
|  Was general capability preserved?  |  
|  Instruments  |  
| --- |  
|  Held-out loss and assistant-token accuracy; pairwise judged win rate  |  
|  CaseHOLD for legal, PubMedQA for healthcare  |  
|  MMLU professional law, MedQA, MedMCQA, ARC-Challenge, GSM8K  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Tier 3 expects parity. Improvement there is neither predicted nor claimed.
### 3.2 Adapters
A low-rank adapter learns a small correction alongside the frozen model rather than rewriting it, which is what makes this affordable and reversible. These are rank 32, alpha 64, dropout 0.05. Target modules are the attention projections on the six attention layers and the shared expert on the 23 mixture-of-experts layers. The pattern anchors on shared_experts, so the 128 routed experts per layer receive no adapter, and each run asserts this and reports the count. 
The router receives no adapter, because perturbing routing destabilizes mixture-of-experts training. All Mamba-2 parameters, the embeddings and the language modelling head are frozen.  
Table showing adapters  
|  Run  |  Trainable tensors  |  Trainable parameters  |  Share of total  |  
| --- | --- | --- | --- |  
|  Legal 500, healthcare 500  |  152  |  14,188,544  |  0.043%  |  
|  Healthcare 100-step arms  |  140  |  13,156,352  |  0.040%  |  
Table showing adapters  
|  Legal 500, healthcare 500  |  
| --- |  
|  Healthcare 100-step arms  |  
|  Trainable tensors  |  
| --- |  
|  152  |  
|  140  |  
|  Trainable parameters  |  
| --- |  
|  14,188,544  |  
|  13,156,352  |  
|  Share of total  |  
| --- |  
|  0.043%  |  
|  0.040%  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The 12-tensor difference is a correction applied between the two sets of runs. The original pattern was anchored only at its end, so it also matched the model's multi-token-prediction head. Those 12 tensors are inert: lora_B initializes to zero, the head is absent from the training forward pass, so it received no gradient and the product B @ A is exactly zero, verified by reading the tensors. The corrected pattern anchors on the backbone prefix and excludes them.
### 3.3 Corpora
Both corpora are built from public datasets, so the recipe can be reproduced without proprietary data. Each also carries a fraction of general-instruction data, called replay, whose purpose is to keep the model's everyday conversational ability intact while it learns the domain. Training only on domain text is what makes a model forget how to do anything else.  
Table showing the corpora used for each domain  
|  Corpus  |  Train rows  |  Validation rows  |  Domain sources  |  
| --- | --- | --- | --- |  
|  Legal  |  103,190  |  1,042  |  CaseHOLD, eCFR-QA, ToSDR-QA, ToS clause understanding, definition classification, diversity jurisdiction, function of decision  |  
|  Healthcare  |  69,538  |  702  |  PubMedQA, MedReason, medical-o1  |  
Table showing the corpora used for each domain  
|  Corpus  |  
| --- |  
|  Legal  |  
|  Healthcare  |  
|  Train rows  |  
| --- |  
|  103,190  |  
|  69,538  |  
|  Validation rows  |  
| --- |  
|  1,042  |  
|  702  |  
|  Domain sources  |  
| --- |  
|  CaseHOLD, eCFR-QA, ToSDR-QA, ToS clause understanding, definition classification, diversity jurisdiction, function of decision  |  
|  PubMedQA, MedReason, medical-o1  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Replay is 15% of rows in both, drawn from NVIDIA post-training and instruction-following sets, and carries 54.5% of healthcare supervised tokens because replay answers are longer than domain answers. Results are therefore reported per stratum, since an aggregate over both describes neither.
Each training row is a user turn and an assistant turn. Where the source dataset supplies a reasoning trace it is carried in a separate field and the chat template renders it inside the model's thinking block, so the supervised target is the reasoning and the answer together.
### 3.4 Separation of training and evaluation data
A domain adapter can appear to learn a great deal simply by having seen the test questions, so the two sets are kept apart mechanically rather than by assumption. Every evaluation split used in this document was hashed against the training corpus. Training rows whose normalized question hash collides with an evaluation item are dropped at corpus-build time, and the manifest records the count. For Tier 1 the held-out slice was verified after the fact by hashing full message lists: zero of 256 rows appear in the corresponding training set. The win-rate prompt set is drawn from a further offset in the validation file so that it is disjoint from the rows the loss curve reflects; one legal row that collided with training was dropped, and the generator reports the drop.
CaseHOLD and PubMedQA training splits were deliberately sampled into the corpora, which is the standard supervised protocol for those datasets. Their scores in _Section 5_ are on the disjoint test splits and are not zero-shot generalization claims.
### 3.5 Training configuration
Neither run was long, and that is the point: both stop well short of one pass over their corpus. Effective batch is one per device by eight gradient accumulation steps by four ranks, so 32 sequences per step at sequence length 4096. Cosine decay with two percent warmup, tied to the step budget. Two runs ran concurrently on disjoint 4-GPU sets.  
Table showing training configuration  
|  Run  |  Steps  |  Learning rate  |  Rows consumed  |  Fraction of one epoch  |  
| --- | --- | --- | --- | --- |  
|  Legal  |  500  |  1e-4  |  16,000  |  0.155  |  
|  Healthcare, first  |  500  |  1e-4  |  16,000  |  0.230  |  
|  Healthcare arms  |  100  |  1e-4 and 3e-5  |  3,200  |  0.046  |  
Table showing training configuration  
|  Legal  |  
| --- |  
|  Healthcare, first  |  
|  Healthcare arms  |  
|  Steps  |  
| --- |  
|  500  |  
|  500  |  
|  100  |  
|  Learning rate  |  
| --- |  
|  1e-4  |  
|  1e-4  |  
|  1e-4 and 3e-5  |  
|  Rows consumed  |  
| --- |  
|  16,000  |  
|  16,000  |  
|  3,200  |  
|  Fraction of one epoch  |  
| --- |  
|  0.155  |  
|  0.230  |  
|  0.046  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
No run completed one pass over its corpus.
### 3.6 Serving for evaluation
Fine-tuned states are scored from weights with the adapter merged in, because serving the adapter at runtime raises an illegal memory access on this architecture. The merge is verified arithmetically against the adapter tensors, and independently against the runtime path on the same rows:  
Table   
|  Path  |  Held-out loss  |  Held-out accuracy  |  
| --- | --- | --- |  
|  Adapter applied at load  |  0.745235  |  0.787193  |  
|  Merged weights, no adapter  |  0.745122  |  0.787393  |  
Table   
|  Path  |  
| --- |  
|  Adapter applied at load  |  
|  Merged weights, no adapter  |  
|  Held-out loss  |  
| --- |  
|  0.745235  |  
|  0.745122  |  
|  Held-out accuracy  |  
| --- |  
|  0.787193  |  
|  0.787393  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The two agree to 1.13 × 10⁻⁴ in loss and 2.00 × 10⁻⁴ in accuracy, so the merged artifact and the runtime artifact are the same model for measurement purposes.
## 4. Domain results
These are the measurements that decided what to ship.
### 4.1 Held-out loss and accuracy
The cheapest measurement of a domain adapter is the one every training run already produces: how well the model predicts held-out answers it never trained on. It comes first here because it is the number most teams have, and _Section 7_ shows how badly it can mislead. The same 256 validation rows per domain, none of them in training, scored token by token over the answer positions.  
Held out loss and accuracy  
|  Domain  |  State  |  Stratum  |  Rows  |  Supervised tokens  |  Loss  |  Accuracy  |  
| --- | --- | --- | --- | --- | --- | --- |  
|  Legal  |  base  |  domain  |  221  |  17,703  |  1.5777  |  0.6472  |  
|  Legal  |  500 steps  |  domain  |  221  |  17,703  |  0.9700  |  0.7342  |  
|  Legal  |  base  |  replay  |  35  |  42,262  |  0.7625  |  0.7950  |  
|  Legal  |  500 steps  |  replay  |  35  |  42,262  |  0.6511  |  0.8094  |  
|  Healthcare  |  base  |  domain  |  215  |  78,189  |  1.5034  |  0.6437  |  
|  Healthcare  |  100 steps at 3e-5  |  domain  |  215  |  78,189  |  1.1407  |  0.6883  |  
|  Healthcare  |  base  |  replay  |  41  |  48,633  |  0.9290  |  0.7517  |  
|  Healthcare  |  100 steps at 3e-5  |  replay  |  41  |  48,633  |  0.8371  |  0.7571  |  
Held out loss and accuracy  
|  Domain  |  
| --- |  
|  Legal  |  
|  Legal  |  
|  Legal  |  
|  Legal  |  
|  Healthcare  |  
|  Healthcare  |  
|  Healthcare  |  
|  Healthcare  |  
|  State  |  
| --- |  
|  base  |  
|  500 steps  |  
|  base  |  
|  500 steps  |  
|  base  |  
|  100 steps at 3e-5  |  
|  base  |  
|  100 steps at 3e-5  |  
|  Stratum  |  
| --- |  
|  domain  |  
|  domain  |  
|  replay  |  
|  replay  |  
|  domain  |  
|  domain  |  
|  replay  |  
|  replay  |  
|  Rows  |  
| --- |  
|  221  |  
|  221  |  
|  215  |  
|  215  |  
|  Supervised tokens  |  
| --- |  
|  17,703  |  
|  17,703  |  
|  42,262  |  
|  42,262  |  
|  78,189  |  
|  78,189  |  
|  48,633  |  
|  48,633  |  
|  Loss  |  
| --- |  
|  1.5777  |  
|  0.9700  |  
|  0.7625  |  
|  0.6511  |  
|  1.5034  |  
|  1.1407  |  
|  0.9290  |  
|  0.8371  |  
|  Accuracy  |  
| --- |  
|  0.6472  |  
|  0.7342  |  
|  0.7950  |  
|  0.8094  |  
|  0.6437  |  
|  0.6883  |  
|  0.7517  |  
|  0.7571  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Legal domain loss falls 38.5% and accuracy rises 8.70 points. Healthcare domain loss falls 24.1% and accuracy rises 4.46 points. Replay loss falls and replay accuracy rises in both, so general instruction-following was not traded for the domain gain.
The aggregate over both strata is the weaker quantity and is omitted from this table. Token weighting makes it largely a replay measurement for legal: domain answers there average 80 supervised tokens against 1,207 for replay, so 35 replay rows of 256 carry 70% of that domain's tokens.
### 4.2 Pairwise judged win rate
Loss says how well a model reproduces a corpus. It does not say whether an answer is any good, and for a domain adapter that is the question that matters, so the deciding measurement here is a blind comparison of answers. Each pair is one question, the base model's answer and the adapter's, handed to an independent judge that does not know which is which. The prompt set is 200 questions per domain, drawn from the validation file after the slice _Section 4.1_ measures. Both states generate greedily from the same prompt at a 2048-token budget. Each pair is judged twice with the responses swapped, and a win requires agreement in both orderings; disagreements are reported as ties rather than resolved. The judge is Claude Opus 5, a different model family from the system under test, which removes same-family self-preference.
Each control compares the base model against itself, from two samples of one distribution at temperature 0.7 differing only in seed. No adapter output enters a control, so one control per domain serves every state of that domain. The true rate of a control is 50% by construction, and its departure measures judge bias plus sampling noise.
A win rate needs a convention for ties, and the choice changes the number without changing the conclusion. Counting ties as half gives legal (112 + 22/2) / 163. Excluding ties entirely gives 0.7943, and counting outright wins alone gives 0.687; the committed results carry the first two. z is a sign test on decided pairs only. The controls shown are the domain stratum's; the replay-stratum controls are omitted, and one of them matters, because on legal replay the adapter's 0.5541 sits below its own control of 0.5811. Two judge refusals occurred on each healthcare run and are counted as undecided.  
Table showing win rate  
|  Domain  |  State  |  Stratum  |  Win  |  Loss  |  Tie  |  Win rate  |  
| --- | --- | --- | --- | --- | --- | --- |  
|  Legal  |  500 steps  |  domain  |  163  |  112  |  29  |  22  |  **0.7546**  |  6.99  |  <0.001  |  
|  Legal  |  control  |  domain  |  163  |  35  |  38  |  90  |  0.4908  |  −0.35  |  0.73  |  
|  Legal  |  500 steps  |  replay  |  37  |  14  |  10  |  13  |  0.5541  |  0.82  |  0.41  |  
|  Healthcare  |  100 steps at 3e-5  |  domain  |  167  |  82  |  47  |  38  |  **0.6048**  |  3.08  |  0.002  |  
|  Healthcare  |  control  |  domain  |  167  |  36  |  50  |  81  |  0.4581  |  −1.51  |  0.13  |  
|  Healthcare  |  100 steps at 3e-5  |  replay  |  33  |  12  |  11  |  10  |  0.5152  |  0.21  |  0.83  |  
Table showing win rate  
|  Domain  |  
| --- |  
|  Legal  |  
|  Legal  |  
|  Legal  |  
|  Healthcare  |  
|  Healthcare  |  
|  Healthcare  |  
|  State  |  
| --- |  
|  500 steps  |  
|  control  |  
|  500 steps  |  
|  100 steps at 3e-5  |  
|  control  |  
|  100 steps at 3e-5  |  
|  Stratum  |  
| --- |  
|  domain  |  
|  domain  |  
|  replay  |  
|  domain  |  
|  domain  |  
|  replay  |  
|  163  |  
| --- |  
|  163  |  
|  167  |  
|  167  |  
|  112  |  
| --- |  
|  Loss  |  
| --- |  
|  Win rate  |  
| --- |  
|  **0.7546**  |  
|  0.4908  |  
|  0.5541  |  
|  **0.6048**  |  
|  0.4581  |  
|  0.5152  |  
|  6.99  |  
| --- |  
|  −0.35  |  
|  0.82  |  
|  3.08  |  
|  −1.51  |  
|  0.21  |  
|  <0.001  |  
| --- |  
|  0.73  |  
|  0.41  |  
|  0.002  |  
|  0.13  |  
|  0.83  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The legal control sits at 0.4908, close enough to neutral that no adjustment is material. The healthcare control sits at 0.4581, a bias of 4.2 points running against the fine-tuned model rather than for it, so the shipped healthcare margin over its own control is 14.7 points.
Neither replay stratum moves significantly, which under free generation is consistent with _Section 4.1's_ finding that general instruction-following was not traded for the domain gain.
### 4.3 Generation budget as a measurement variable
The win rate was first measured at a 512-token budget and the healthcare result inverted when the budget was raised. The cause is truncation of the base model rather than any property of the adapters.  
Generation budget as a measurable variable  
|  Healthcare domain stratum  |  At the budget  |  No closing thinking tag  |  Median tokens  |  
| --- | --- | --- | --- |  
|  Base, 512 budget  |  125 of 167  |  112  |  512  |  
|  Base, 2048 budget  |  32 of 167  |  26  |  826  |  
|  Shipped adapter, 2048 budget  |  1 of 167  |  464  |  
Generation budget as a measurable variable  
|  Healthcare domain stratum  |  
| --- |  
|  Base, 512 budget  |  
|  Base, 2048 budget  |  
|  Shipped adapter, 2048 budget  |  
|  At the budget  |  
| --- |  
|  125 of 167  |  
|  32 of 167  |  
|  1 of 167  |  
|  No closing thinking tag  |  
| --- |  
|  112  |  
|  Median tokens  |  
| --- |  
|  512  |  
|  826  |  
|  464  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
At 512 tokens three quarters of base generations stopped mid-reasoning without producing an answer, so the judge compared a truncated output against a complete one. At 2048 both sides finish. The reported figures throughout this document are at 2048.  
Table showing budget and domains  
|  Domain  |  State  |  512 budget  |  2048 budget  |  
| --- | --- | --- | --- |  
|  Legal  |  500 steps  |  0.7515  |  0.7546  |  
|  Healthcare  |  500 steps  |  0.5449  |  0.3413  |  
Table showing budget and domains  
|  Domain  |  
| --- |  
|  Legal  |  
|  Healthcare  |  
|  State  |  
| --- |  
|  500 steps  |  
|  500 steps  |  
|  512 budget  |  
| --- |  
|  0.7515  |  
|  0.5449  |  
|  2048 budget  |  
| --- |  
|  0.7546  |  
|  0.3413  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Legal is insensitive to the budget. Healthcare appeared to win slightly at 512 and loses decisively at 2048. A generation budget is therefore a measurement parameter for judged comparisons on this model, and reporting one without it is not interpretable.
## 5. Public benchmark results
Public benchmarks answer a different question from the one in _Section 4_. They are standardized, so a score can be compared with what others report, and they are also blunt: a multiple-choice test over a few hundred items registers only fairly large movements. They are used here in two roles. Tier 2 is the domain test, run over the full split so the before-and-after comparison has as much statistical power as the dataset allows. Tier 3 is the safety check, asking whether teaching the model law or medicine cost it any general ability, and run over the first 400 items because the expected and desired answer is no change. All fine-tuned states are scored from weights with the adapter merged in.  
Public benchmark results  
|  Tier  |  Domain  |  Task  |  Base  |  Fine-tuned  |  Change  |  
| --- | --- | --- | --- | --- | --- |  
|  Legal  |  CaseHOLD  |  3,600  |  0.3472  |  **0.7714**  |  **+42.4 pts**  |  <0.001  |  
|  Healthcare  |  PubMedQA  |  500  |  0.7820  |  0.7760  |  −0.6 pts  |  0.82  |  
|  Legal  |  MMLU professional law  |  400  |  0.5750  |  0.5900  |  +1.5 pts  |  0.67  |  
|  Legal  |  ARC-Challenge  |  400  |  0.6150  |  0.6300  |  +1.5 pts  |  0.66  |  
|  Legal  |  GSM8K  |  400  |  0.8975  |  0.8875  |  −1.0 pts  |  0.65  |  
|  Healthcare  |  MedQA 4-options  |  400  |  0.7350  |  0.7375  |  +0.3 pts  |  0.94  |  
|  Healthcare  |  MedMCQA  |  400  |  0.6275  |  0.6250  |  −0.3 pts  |  0.94  |  
|  Healthcare  |  ARC-Challenge  |  400  |  0.6125  |  0.6250  |  +1.25 pts  |  0.71  |  
|  Healthcare  |  GSM8K  |  400  |  0.8975  |  0.8450  |  −5.25 pts  |  0.03  |  
Public benchmark results  
|  Tier  |  
| --- |  
|  Domain  |  
| --- |  
|  Legal  |  
|  Healthcare  |  
|  Legal  |  
|  Legal  |  
|  Legal  |  
|  Healthcare  |  
|  Healthcare  |  
|  Healthcare  |  
|  Healthcare  |  
|  Task  |  
| --- |  
|  CaseHOLD  |  
|  PubMedQA  |  
|  MMLU professional law  |  
|  ARC-Challenge  |  
|  GSM8K  |  
|  MedQA 4-options  |  
|  MedMCQA  |  
|  ARC-Challenge  |  
|  GSM8K  |  
|  3,600  |  
| --- |  
|  500  |  
|  400  |  
|  400  |  
|  400  |  
|  400  |  
|  400  |  
|  400  |  
|  400  |  
|  Base  |  
| --- |  
|  0.3472  |  
|  0.7820  |  
|  0.5750  |  
|  0.6150  |  
|  0.8975  |  
|  0.7350  |  
|  0.6275  |  
|  0.6125  |  
|  0.8975  |  
|  Fine-tuned  |  
| --- |  
|  **0.7714**  |  
|  0.7760  |  
|  0.5900  |  
|  0.6300  |  
|  0.8875  |  
|  0.7375  |  
|  0.6250  |  
|  0.6250  |  
|  0.8450  |  
|  Change  |  
| --- |  
|  **+42.4 pts**  |  
|  −0.6 pts  |  
|  +1.5 pts  |  
|  +1.5 pts  |  
|  −1.0 pts  |  
|  +0.3 pts  |  
|  −0.3 pts  |  
|  +1.25 pts  |  
|  −5.25 pts  |  
|  <0.001  |  
| --- |  
|  0.82  |  
|  0.67  |  
|  0.66  |  
|  0.65  |  
|  0.94  |  
|  0.94  |  
|  0.71  |  
|  0.03  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Of the nine comparisons, one is a significant improvement and one a significant regression. CaseHOLD gains 42.4 points at p < 0.001, and it is the only gain in the table that a significance test supports. Healthcare GSM8K falls 5.25 points at p = 0.03 on the shipped 100-step state. The 500-step first attempt falls 4.25 points at 400 items and 4.02 points on the full 1,319-item split, where the paired test gives p = 2.0 × 10⁻⁵ (Section 5.2). The remaining seven comparisons are at parity, on the bound Section 5.1 derives from the 400-item cap.
Every score above is plain accuracy, the fraction of items answered correctly, and GSM8K runs with five worked examples in the prompt. One row is sensitive to that choice. ARC-Challenge can also be scored with answers normalized by length, and on that measure the base model and the shipped healthcare adapter are identical rather than 1.25 points apart. The regression check is unaffected either way, since both readings show no loss.
The healthcare rows come from two states. PubMedQA was scored on the 500-step first attempt; the MedQA, MedMCQA, ARC-Challenge and GSM8K rows were scored on the shipped 100-step state. No PubMedQA measurement of the shipped state exists, which _Section 9_ records as an open item.
GSM8K can be graded strictly, requiring the answer in an exact format, or leniently, accepting a correct number wherever it appears. The two agree on every state in this table, so the reading here does not depend on the choice. They disagree on one state, which _Section 7.2_ reports on both.
CaseHOLD more than doubles. Its training split was sampled into the legal corpus by design, so this is a supervised in-domain result on a disjoint test split.
PubMedQA does not move. The base score of 0.7820 already sits at the level published reasoning-required results occupy, so the task offers little room on this corpus. Its training split was also sampled, and PubMedQA did not move despite that, which bounds what a 500-item multiple-choice task can register on this corpus.
### 5.1 Run-to-run variation
ARC-Challenge is scored in both suites, which makes the base model's score on it a cross-run reproducibility check. Three measurements of the same weights at the same item cap and the same seed returned 0.6175, 0.6150 and 0.6125, a two-item spread in 400 caused by automatic batch sizing changing batch composition under bf16. Every Tier 3 movement above except healthcare GSM8K is at most six items. None is resolvable by the unpaired test used here: at n = 400 per arm the smallest difference detectable at 80% power runs from about six points at GSM8K's base rate to about 10 points at MMLU professional law's, and the tightest equivalence margin the sample supports is about five to seven points. A paired analysis over per-item outcomes, as in _Section 5.2_ , resolves smaller differences at the same cap. Parity here is unrefuted rather than demonstrated.
### 5.2 Arithmetic on the full split
Healthcare GSM8K was repeated on the complete 1,319-item split with per-item logging, which makes the paired test available.  
Arithmetic on the full split  
|  Quantity  |  Value  |  
| --- | --- |  
|  Base accuracy, flexible-extract  |  0.8901 ± 0.0086  |  
|  Fine-tuned accuracy, 500 steps  |  0.8499 ± 0.0098  |  
|  Same pair on strict-match  |  0.8878 and 0.8491  |  
|  Items base solved and fine-tuned failed  |  101  |  
|  Items base failed and fine-tuned solved  |  48  |  
|  McNemar χ², continuity-corrected  |  18.15  |  
|  2.0 × 10⁻⁵  |  
Arithmetic on the full split  
|  Quantity  |  
| --- |  
|  Base accuracy, flexible-extract  |  
|  Fine-tuned accuracy, 500 steps  |  
|  Same pair on strict-match  |  
|  Items base solved and fine-tuned failed  |  
|  Items base failed and fine-tuned solved  |  
|  McNemar χ², continuity-corrected  |  
|  Value  |  
| --- |  
|  0.8901 ± 0.0086  |  
|  0.8499 ± 0.0098  |  
|  0.8878 and 0.8491  |  
|  101  |  
|  18.15  |  
|  2.0 × 10⁻⁵  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
This measurement is of the 500-step first attempt, which is the state _Section 7.2_ tabulates; the shipped 100-step state was not repeated on the full split. The adapter breaks 101 problems the base model solves and repairs 48, a net loss of 53. 
The full-split figure of −4.02 points reproduces the −4.25 points that state gives at 400 items, where the unpaired test gave only p = 0.068 and could not be separated from the half-point movements around it.
## 6. Held-out generalization
CaseHOLD cannot answer whether the legal gain generalizes, because its training split was used. This section asks that question against legal tasks the adapter never saw.
Nineteen LegalBench tasks, grouped into six reasoning types. Eleven LegalBench families that overlap the training corpus were excluded when the task set was generated, and the exclusion is asserted against the corpus builder's own list by an existing test. Group scores macro-average without size weighting. An item cap of 900 leaves 16 of the 19 tasks at their full split and caps the three that would otherwise dominate. Scored from merged weights against LegalBench's published few-shot completion prompts.
Figure 1. Exact-match accuracy on six held-out LegalBench reasoning groups, base model against the legal adapter, ordered by change. None of these tasks appears in the training corpus and eleven contaminated task families were excluded when the set was generated. Issue spotting and interpretation gain; rhetorical understanding and rule application are level; rule recall and rule conclusion sit below the base model. Two of the nineteen tasks account for the movement, which the group macro-average conceals.  Figure 1. Exact-match accuracy on six held-out LegalBench reasoning groups, base model against the legal adapter, ordered by change. None of these tasks appears in the training corpus and eleven contaminated task families were excluded when the set was generated. Issue spotting and interpretation gain; rhetorical understanding and rule application are level; rule recall and rule conclusion sit below the base model. Two of the nineteen tasks account for the movement, which the group macro-average conceals.   
Table  
|  Group  |  Base  |  Legal adapter  |  Change  |  
| --- | --- | --- | --- |  
|  issue_spotting  |  0.4284 ± 0.0107  |  **0.5669**  |  **+13.85 pts**  |  7.82  |  
|  interpretation  |  0.6604 ± 0.0076  |  **0.7220**  |  **+6.16 pts**  |  6.00  |  
|  rhetorical_understanding  |  0.6864 ± 0.0112  |  0.6932  |  +0.68 pts  |  0.43  |  
|  rule_application  |  0.7129 ± 0.0329  |  0.7111  |  −0.18 pts  |  −0.04  |  
|  rule_recall  |  0.4430 ± 0.0070  |  0.4240  |  −1.90 pts  |  −1.83  |  
|  rule_conclusion  |  0.7918 ± 0.0250  |  0.7669  |  −2.49 pts  |  −0.69  |  
|  Mean of six groups  |  +2.69 pts  |  
Table  
|  Group  |  
| --- |  
|  issue_spotting  |  
|  interpretation  |  
|  rhetorical_understanding  |  
|  rule_application  |  
|  rule_recall  |  
|  rule_conclusion  |  
|  Mean of six groups  |  
|  Base  |  
| --- |  
|  0.4284 ± 0.0107  |  
|  0.6604 ± 0.0076  |  
|  0.6864 ± 0.0112  |  
|  0.7129 ± 0.0329  |  
|  0.4430 ± 0.0070  |  
|  0.7918 ± 0.0250  |  
|  Legal adapter  |  
| --- |  
|  **0.5669**  |  
|  **0.7220**  |  
|  0.6932  |  
|  0.7111  |  
|  0.4240  |  
|  0.7669  |  
|  Change  |  
| --- |  
|  **+13.85 pts**  |  
|  **+6.16 pts**  |  
|  +0.68 pts  |  
|  −0.18 pts  |  
|  −1.90 pts  |  
|  −2.49 pts  |  
|  +2.69 pts  |  
|  7.82  |  
| --- |  
|  6.00  |  
|  0.43  |  
|  −0.04  |  
|  −1.83  |  
|  −0.69  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Two of the six groups improve, by margins far outside their standard errors, and both are tasks of reading legal text and classifying it, which is the shape of the training corpus. Rule recall does not improve: that task is retrieval of specific legal facts, and a 14-million-parameter adapter over 16,000 rows has no mechanism to add knowledge the base model lacks. Rule application and rule conclusion, which reason over a rule supplied in the prompt, are unchanged.
The group averages flatter the result, and the task-level numbers carry it. Two of the nineteen tasks account for almost all of the movement: contract_qa gains 45.00 points over 80 items, and corporate_lobbying rises from a base score of exactly 0.000 to 0.3633 over 490 items. A base score of zero is a prompt-format failure rather than absent knowledge, since the base model emits the literal option list instead of a verdict. The other is international_citizenship_questions, at 0.0000 against 0.0233. Excluding both moves the macro-average from +2.69 points to +0.46. Ten of the nineteen tasks regress, the largest being citation_prediction_classification at −11.11 points.
The claim this supports is narrow: the adapter transfers to two held-out tasks that resemble its training data, and not across LegalBench as a whole.
## 7. Configuration sensitivity
The first healthcare adapter regressed. Its learning curve indicated why it might be recoverable: most of the accuracy gain existed by step 100, and the final 400 steps bought 0.0068 of token accuracy and 0.112 of loss.  
Configuration sensitivity  
|  Step  |  Held-out loss  |  Token accuracy  |  
| --- | --- | --- |  
|  25  |  4.7088  |  0.7131  |  
|  100  |  4.2714  |  0.7332  |  
|  250  |  4.1828  |  0.7392  |  
|  500  |  4.1590  |  0.7400  |  
Configuration sensitivity  
|  Step  |  
| --- |  
|  100  |  
|  250  |  
|  500  |  
|  Held-out loss  |  
| --- |  
|  4.7088  |  
|  4.2714  |  
|  4.1828  |  
|  4.1590  |  
|  Token accuracy  |  
| --- |  
|  0.7131  |  
|  0.7332  |  
|  0.7392  |  
|  0.7400  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Two further arms tested that, each 100 steps, differing from each other only in learning rate, run concurrently on disjoint 4-GPU sets. Both consumed the same corpus, verified by reading the row count out of each run's own log, and both reported the intended learning rate in their first logged step.
### 7.1 Divergence between held-out loss and judged quality
The two figures below plot the same four healthcare states on the same axis, one measured by loss and one by judged quality. They slope in opposite directions.
Figure 2. Held-out domain loss for four healthcare states, ordered by integrated learning rate, which is the total optimizer travel of each run. Loss falls monotonically as training continues, so this quantity alone ranks the largest adapter best. Figure 3 plots judged quality over the same four states and the same axis.  Figure 2. Held-out domain loss for four healthcare states, ordered by integrated learning rate, which is the total optimizer travel of each run. Loss falls monotonically as training continues, so this quantity alone ranks the largest adapter best. Figure 3 plots judged quality over the same four states and the same axis. 
Figure 3. Judged win rate against the base model over the states and the axis of Figure 2. The dashed line is the control, the base model against itself, at 0.4581. The base state is the control rather than a point on the series, so it carries no marker. Quality peaks at the smallest adapter and falls below the control at the largest, which is the state Figure 2 ranks best. The two figures slope in opposite directions over one range.  Figure 3. Judged win rate against the base model over the states and the axis of Figure 2. The dashed line is the control, the base model against itself, at 0.4581. The base state is the control rather than a point on the series, so it carries no marker. Quality peaks at the smallest adapter and falls below the control at the largest, which is the state Figure 2 ranks best. The two figures slope in opposite directions over one range.   
Divergence between held-out loss and judged quality table  
|  State  |  Integrated LR  |  Domain loss  |  Domain accuracy  |  Judged win rate  |  
| --- | --- | --- | --- | --- |  
|  Base  |  1.5034  |  0.6437  |  0.4581 (control)  |  
|  Arm B  |  1.5 × 10⁻³  |  1.1407  |  0.6883  |  **0.6048**  |  0.0021  |  
|  Arm A  |  5.0 × 10⁻³  |  1.0440  |  0.7053  |  0.5000  |  1.00  |  
|  Original  |  2.5 × 10⁻²  |  0.9734  |  0.7212  |  0.3413  |  <0.001  |  
Divergence between held-out loss and judged quality table  
|  State  |  
| --- |  
|  Base  |  
|  Arm B  |  
|  Arm A  |  
|  Original  |  
|  Integrated LR  |  
| --- |  
|  1.5 × 10⁻³  |  
|  5.0 × 10⁻³  |  
|  2.5 × 10⁻²  |  
|  Domain loss  |  
| --- |  
|  1.5034  |  
|  1.1407  |  
|  1.0440  |  
|  0.9734  |  
|  Domain accuracy  |  
| --- |  
|  0.6437  |  
|  0.6883  |  
|  0.7053  |  
|  0.7212  |  
|  Judged win rate  |  
| --- |  
|  0.4581 (control)  |  
|  **0.6048**  |  
|  0.5000  |  
|  0.3413  |  
|  0.0021  |  
| --- |  
|  1.00  |  
|  <0.001  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Loss and accuracy improve monotonically with total optimizer travel. Judged quality moves monotonically in the opposite direction. Over the range measured, held-out loss on this corpus is inversely related to judged answer quality, so optimizing it further degrades the model.
The judge's recorded reasons on the 99 pairs the base model won against the 500-step state concern precision of claims: the disease mechanism named where the adapter is vague, a supplied odds ratio and hazard ratio cited from the evidence in the prompt, the required yes-no-maybe verdict absent. On the representative exhibit pair the two answers run 2,214 and 2,158 characters, so length is not the discriminator.
Configuration selection for the shipped healthcare adapter was therefore on judged win rate. The three states are reported separately and are never averaged.
### 7.2 Arithmetic cost across the ladder
One cost did not respond to any of these configurations, which is what marks it as a property of the corpus rather than of the schedule:  
Arithmetic cost across the ladder table  
|  Guardrail, 400 items  |  Base  |  500 at 1e-4  |  100 at 1e-4  |  100 at 3e-5  |  
| --- | --- | --- | --- | --- |  
|  GSM8K, flexible-extract  |  0.8975  |  0.8550  |  0.8400  |  0.8450  |  
|  GSM8K, strict-match  |  0.8975  |  0.8550  |  0.8375  |  0.8450  |  
|  MedQA 4-options  |  0.7350  |  0.7275  |  0.7125  |  0.7375  |  
|  MedMCQA  |  0.6275  |  0.6475  |  0.6325  |  0.6250  |  
|  ARC-Challenge  |  0.6125  |  0.6175  |  0.6100  |  0.6250  |  
Arithmetic cost across the ladder table  
|  Guardrail, 400 items  |  
| --- |  
|  GSM8K, flexible-extract  |  
|  GSM8K, strict-match  |  
|  MedQA 4-options  |  
|  MedMCQA  |  
|  ARC-Challenge  |  
|  Base  |  
| --- |  
|  0.8975  |  
|  0.8975  |  
|  0.7350  |  
|  0.6275  |  
|  0.6125  |  
|  500 at 1e-4  |  
| --- |  
|  0.8550  |  
|  0.8550  |  
|  0.7275  |  
|  0.6475  |  
|  0.6175  |  
|  100 at 1e-4  |  
| --- |  
|  0.8400  |  
|  0.8375  |  
|  0.7125  |  
|  0.6325  |  
|  0.6100  |  
|  100 at 3e-5  |  
| --- |  
|  0.8450  |  
|  0.8450  |  
|  0.7375  |  
|  0.6250  |  
|  0.6250  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The three adapters span a seventeen-fold range of optimizer travel and their GSM8K scores fall within 1.5 points of each other, which is three times the two-item run-to-run spread of _section 5.1_. All three sit 4.25 to 5.75 points below the base model on flexible-extract, and 4.25 to 6.00 points below it on strict-match. The 100-step 1e-4 arm is the only state measured on which the two filters disagree, by one item in 400. Training less does not recover arithmetic.
Healthcare therefore has two independent axes. Judged quality is dose-dependent and recoverable. Arithmetic cost appears at the smallest dose tested and does not diminish with it, so it belongs to the corpus. The healthcare corpus carries 3.75% mathematics replay, which did not preserve the capability.
### 7.3 Recommended configuration
The settings that produced the shipped adapters, for a team reproducing this on its own corpus:  
Recommended configuration table  
|  Domain  |  Steps  |  Learning rate  |  Fraction of one epoch  |  
| --- | --- | --- | --- |  
|  Legal  |  500  |  1e-4  |  0.155  |  
|  Healthcare  |  100  |  3e-5  |  0.046  |  
Recommended configuration table  
|  Domain  |  
| --- |  
|  Legal  |  
|  Healthcare  |  
|  Steps  |  
| --- |  
|  500  |  
|  100  |  
|  Learning rate  |  
| --- |  
|  1e-4  |  
|  3e-5  |  
|  Fraction of one epoch  |  
| --- |  
|  0.155  |  
|  0.046  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The two domains take different budgets on the same recipe, the same rank and the same target modules. A single budget applied to both would have produced one success and one regression.
## 8. Reproduction
Every measurement records its own configuration: the model served, the item cap, the seed, the tensor-parallel size, the GPU model, the driver and engine versions and the process exit code.
The pipeline is five steps on public tooling, at the settings in _Section 3_. The wrapper scripts that ran them are supplied on request.
  1. Build the domain corpus and the replay mixture, holding out 256 validation rows per domain and dropping any training row whose normalized question hash collides with an evaluation item.
  2. Train a rank-32 adapter over the attention projections of the six attention layers and the shared expert of the 23 mixture-of-experts layers, with peft 0.20.0 under FSDP2 full-shard on 8 × H100: 500 steps at 1e-4 for legal, 100 steps at 3e-5 for healthcare, sequence length 4096, bf16.
  3. Recover a loadable adapter from the sharded FSDP2 checkpoint and merge it into the base weights. Serving the adapter at runtime is unusable on this architecture, and _Section 3.6_ gives the check that the merged and runtime artifacts agree.
  4. Score Tier 1 held-out loss and token accuracy through the training encoder. Score Tier 2 and Tier 3 with lm-eval 0.4.12 against a vLLM 0.25.1 server, and the held-out LegalBench subset with the benchmark's own completion prompts.
  5. Generate a few hundred completions per state on held-out prompts, then judge each pair blind in both orderings against the base generations, with a base-against-base control per domain.


### 8.1 Configuration requirements
Four requirements are mandatory on this model, and each produced a failure before it was identified:
  * **Merged weights for serving.** A runtime adapter path raises an illegal memory access on this architecture, which replaces the fused mixture-of-experts path with an adapter-capable one. The merge precedes serving.
  * **Adapter recovery from the sharded checkpoint.** Saving an adapter directly raises under FSDP2, after the routine has already written its metadata file, so the output directory exists and contains no weights. A directory-existence check passes on it.
  * **An explicit corpus path.** The Tier 1 measurement script previously defaulted its corpus path. A launch that omitted the argument scored models trained on one corpus against another corpus's validation split, which a corpus rebuild had reshuffled into training data. The argument is now mandatory and has no default.
  * **A stated generation budget.**(_Section 4.3)_. A judged comparison without its budget is not interpretable.


## 9. Limitations
**Composition with the EAGLE-3 draft head.** Whether a merged domain adapter preserves the acceptance of the companion write-up's draft head is not measured. The domain adapters measured here are merged into the target weights and that head was trained and measured against the unadapted target, so the two workstreams are not known to compose.
**Arithmetic regression in the healthcare adapter.** 4.25 to 6.00 points of GSM8K at every training budget tested, established at p = 2.0 × 10⁻⁵ on the full 1,319-item split for the 500-step state. Not recovered by reducing the budget. Multi-step arithmetic is relevant to agentic deployment, and this cost is unresolved. Raising the mathematics fraction of the replay mixture above 3.75% is the untested next step.
**No agentic or tool-use measurement.**(_Section 2.2_.)
**One judge.** The win rate rests on a single judge model, scored in both orderings with a base-against-base control per domain. A second judge from a third family would strengthen it and was not run.
**Controls are sampled while comparisons are greedy.** Each control draws two samples at temperature 0.7 so that its two sides differ; the comparison arms are greedy. The control therefore measures judge bias in a nearby but not identical decoding regime. The alternative, two greedy passes, yields byte-identical text and a figure of exactly 0.500 whatever the bias.
**PubMedQA registers nothing.** Its training split was sampled into the corpus and the test score moved −0.6 points. Whether the shipped healthcare adapter would move it is not measured; the PubMedQA figure in _Section 5_ is the 500-step state.
**LegalBench was measured for legal only.** The equivalent held-out generalization test for healthcare, MedXpertQA, was not run.
**Single measurements.** Tier 1 and the win rate were each measured once per state. No repeat-run variance is available for them. _Section 5.1_ gives the reproducibility spread for the lm-eval tasks.
**One item cap in Tier 3.** 400 items, so the smallest difference the unpaired test resolves there is 6 to 10 points depending on the base rate, on the bound _Section 5.1_ derives, and a smaller movement is not resolvable there.
**Sequence length and turn count.** 4096 tokens, single-turn, against an advertised 1M context and a model positioned for multi-turn workflows.
## 10. Conclusions
This work answers a question a company can reasonably ask before committing to any of this: can an open 30B model be taught a specialized domain, on data that never leaves the building, cheaply enough to be worth doing? For legal and for healthcare, on this model, it can.
We adapted Nemotron 3.5 Lightning with low-rank adapters, which learn a small correction alongside the frozen model rather than rewriting it. That is what made it inexpensive: each adapter touches about 0.04% of the model's parameters, neither run completed a single pass over its corpus, and the two together took a few hours on one eight-GPU node. The legal adapter is preferred over the base model in 112 of 163 blind comparisons, more than doubles CaseHOLD accuracy, and carries two held-out LegalBench tasks it never trained on. The shipped healthcare adapter is preferred in 82 of 167. Nothing in the general-ability checks moves by more than 1.5 points, apart from arithmetic on healthcare, which falls between 4.25 and 6.00 points.
Getting there in healthcare took two attempts, and why the first one failed is the result we would pass on before any other. Held-out loss, which every training run reports for free, ranked four healthcare configurations in exactly the reverse of their judged quality: the state with the lowest loss and the highest token accuracy is the one the judge places last, and the state with the highest loss of the three adapters is the only one that beats the base model. A team selecting on loss would have shipped the worst of the three and had a falling curve to justify it.
What worked instead is cheap enough to run on every candidate. A few hundred generations from the base model and from the adapter on held-out questions, shown to a judge from a different model family in both orders, with a base-against-base control to expose the judge's own bias, took under twenty minutes per configuration and was the only measurement that ordered the four states correctly.
Two further findings transfer. Training budget is domain-specific rather than a property of the recipe: legal wanted 500 steps at 1e-4 and healthcare 100 steps at a third of that learning rate, on identical rank and identical target modules, and one budget applied to both would have produced one success and one regression. And one cost did not respond to any configuration tried: arithmetic accuracy falls between 4.25 and 6.00 points on every healthcare adapter measured, at every budget, which points at the corpus rather than the schedule. _Section 9_ records it as unresolved and names the untested lever.
An organization starting from here would take one domain whose data cannot leave its environment, build the corpus from what it already owns with a replay fraction to protect general ability, train for hours rather than weeks, and decide what to ship on judged answers rather than on the loss curve.
_**This write-up covers post-training for enterprise domains.[EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning](https://research.thoughtworks.com/library/eagle-3-speculative-decoding-nvidia-nemotron-3-5-lightning) is its companion, and the two are submitted together. The adapters were trained and evaluated on Thoughtworks-operated AWS instances, and no corpus or generation left the node.**_
##  Keep reading 
  * [ Insights EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning By  **Gustavo Lujan** Experimenting with speculative decoding using the EAGLE-3 draft head.  ](https://research.thoughtworks.com/library/eagle-3-speculative-decoding-nvidia-nemotron-3-5-lightning)
  * [ Insights Teaching a model to stop writing like a model By  **Allen Roush** How can we make an AI model write less like a model and more like a human?  ](https://research.thoughtworks.com/library/teaching-model-stop-writing-like-model)
  * [ Insights Cultural counterfactuals By  **Phillip Howard** , **Xin Su** , **Parag Mahajani** Discover the 'Cultural Counterfactuals' dataset. We help you uncover hidden bias in AI vision models related to religion, nationality, and socioeconomic status.  ](https://research.thoughtworks.com/library/cultural-counterfactuals)


Thoughtworks respects your privacy and only uses cookies that are essential for this site to function. If you enjoy our content and would like a personalized experience please ‘’accept optional cookies’’. See our [Privacy policy](https://www.thoughtworks.com/about-us/privacy-policy) for more.
Manage preferences Decline cookies Accept optional cookies
## Privacy Preference Center
## Privacy Preference Center
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Functional Cookies
  * ### Targeting Cookies


#### Your Privacy
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://research.thoughtworks.com/about-us/privacy-policy)
#### Strictly Necessary Cookies
Always Active
These cookies are essential in enabling you to move around our site and use our features. Without them, services you ask for can't be provided. Registered Visitor Cookie: a unique identifier given to each registered user that recognizes you anonymously during site access.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies collect information so we can analyze how our visitors use our site but they don't collect information that identifies you. All information is anonymous and is only used to improve how our site works.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies allow websites and applications to remember choices you make and provide more enhanced, personal features. We may use information collected from functional cookies to identify user behavior and to serve content based on the user profile. These cookies can't track your browsing activity on other websites and don't gather any information about you for advertising usage or to record where you’ve been on the internet, outside our site.
Cookies Details
#### Targeting Cookies
Targeting Cookies
In order to keep our website services relevant, easy to use and up-to-date, we use web analytics services to help us understand how people use the site. Cookies allow us to recognize your browser or device and identify whether you've visited our website before, what you've previously viewed or clicked on and how you found us. The information is anonymous and only used for statistical purposes.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All