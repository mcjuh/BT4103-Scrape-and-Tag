<!-- Source: https://research.thoughtworks.com/library/eagle-3-speculative-decoding-nvidia-nemotron-3-5-lightning | Title: EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning
By 
Published: August 11, 2026 
## 1. Summary
Open models give an enterprise control over its AI stack, which is what makes it possible to apply a language model to proprietary data without that data leaving a trusted environment. Self-hosting moves the economics of inference onto the organization's own hardware. From that point the cost of a generated token is a function of how many tokens a GPU can produce per second, which is an engineering quantity rather than a line on a price list.
Speculative decoding raises that quantity without altering which tokens the target would have produced. Nemotron 3.5 Lightning arrives with a speculative decoder already fitted: the model ships a native multi-token prediction head and serves it on stock vLLM. This work measures that head, and compares it against an EAGLE-3 head trained for the same target: 2,091 individual measurements across two inference engines, two GPU generations, three workloads and concurrency from one to 128 requests.
### 1.1 Native multi-token prediction against unaccelerated decoding
The first question is what the model already does on its own, with no external draft head anywhere in the picture. Turning its multi-token prediction off and on is the whole measurement, and the ratio below is how much faster it generates with the feature enabled. Each figure divides the MTP column by the no-spec column of the measurements in s _ection 4.1_ and s _ection 4.2_ , one measurement each.  
Table showing performance across different hardware architectures.  
|  Domain  |  H200, 1 request  |  H200, 32 concurrent  |  B200, 1 request  |  B200, 32 concurrent  |  
| --- | --- | --- | --- | --- |  
|  Mathematics  |  1.64×  |  1.96×  |  1.74×  |  1.91×  |  
|  Code  |  1.52×  |  1.81×  |  1.56×  |  1.82×  |  
|  Chat  |  1.46×  |  1.76×  |  1.49×  |  1.75×  |  
Table showing performance across different hardware architectures.  
|  Domain  |  
| --- |  
|  Mathematics  |  
|  Code  |  
|  Chat  |  
|  H200, 1 request  |  
| --- |  
|  1.64×  |  
|  1.52×  |  
|  1.46×  |  
|  H200, 32 concurrent  |  
| --- |  
|  1.96×  |  
|  1.81×  |  
|  1.76×  |  
|  B200, 1 request  |  
| --- |  
|  1.74×  |  
|  1.56×  |  
|  1.49×  |  
|  B200, 32 concurrent  |  
| --- |  
|  1.91×  |  
|  1.82×  |  
|  1.75×  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
That is most of the benefit speculative decoding has to offer on this model, and it requires no training and no second artifact. A default this strong makes the comparison in s _ection 1.2_ a demanding one. Multi-token prediction is increasingly common among recent open mixture-of-experts models. DeepSeek-V3 publishes a multi-token prediction module in its open weights, and Qwen3-Next trains an MTP path reachable through a serving engine rather than through Transformers. This work measured no other model's head, so nothing here ranks them against this one.
Reaching the head still takes engine-side work: a serving stack that implements the target side. Three of the four configuration requirements mentioned below apply to the native head as they do to ours, and each produces a wrong measurement rather than an error.
### 1.2 The EAGLE-3 drafter against native multi-token prediction
The second question is whether a draft head trained for this target can beat the one already fitted. This is the study's most carefully controlled comparison, and the one part of it that is repeated enough to carry a confidence interval: vLLM on H200, one request at a time, temperature 0, natural stopping, an equal three-token draft budget for both arms so neither is given more to work with, and twenty repeated measurements per arm within one server session per arm. Both arms were measured in the same twenty windows on the same node. The interval is a two-sample delta-method interval at n = 20 per arm and does not cover boot-to-boot variation.  
Table showing comparing draft model with native MTP capabilities  
|  Domain  |  Ours ÷ native MTP  |  Change  |  95% CI on the ratio  |  Sample  |  
| --- | --- | --- | --- | --- |  
|  Mathematics  |  1.0003  |  +0.03%  |  [0.9935, 1.0070]  |  20 repeats, cap 4096  |  
|  Code  |  1.0111  |  +1.11%  |  [1.0053, 1.0169]  |  20 repeats, cap 4096  |  
|  Chat  |  0.8921  |  −10.79%  |  [0.8850, 0.8993]  |  20 repeats, cap 4096  |  
Table showing comparing draft model with native MTP capabilities  
|  Domain  |  
| --- |  
|  Mathematics  |  
|  Code  |  
|  Chat  |  
|  Ours ÷ native MTP  |  
| --- |  
|  1.0003  |  
|  1.0111  |  
|  0.8921  |  
|  Change  |  
| --- |  
|  +0.03%  |  
|  +1.11%  |  
|  −10.79%  |  
|  95% CI on the ratio  |  
| --- |  
|  [0.9935, 1.0070]  |  
|  [1.0053, 1.0169]  |  
|  [0.8850, 0.8993]  |  
|  Sample  |  
| --- |  
|  20 repeats, cap 4096  |  
|  20 repeats, cap 4096  |  
|  20 repeats, cap 4096  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Mathematics is at parity, its interval spanning 1.0. Code is above parity and chat below it, both outside their intervals.
### 1.3 A stronger baseline than expected
A native multi-token prediction head is commonly a training-time device that serving stacks discard at deployment, with lower acceptance than a draft head trained for the purpose. NVIDIA's head overturns that expectation, and four measurements establish how far:
  * At an equal draft budget, this head's acceptance is 0.85 to 0.95 times native multi-token prediction's, in all six single-stream cases (s _ection 4.4_).
  * At a single stream on B200, this head's throughput is 0.77 to 0.86 times native multi-token prediction's, across all three domains (s _ection 4.2_).
  * Native multi-token prediction leads every domain on both node types at 128 concurrent requests (s _ection 4.2_).
  * The highest absolute throughput measured anywhere in this study is native multi-token prediction's.


Each head leads in a different regime. On H200 at a single stream the EAGLE-3 head leads on code and matches native multi-token prediction on mathematics, and between four and 32 concurrent requests it leads on mathematics and code on both node types; native multi-token prediction leads on B200 at a single stream and above 64 concurrent requests on both node types. Either path is worth 1.2 to 2.0 times unaccelerated decoding across everything measured on vLLM, s _ection 5_ reports the single-stream output residual against unaccelerated decoding together with task accuracy shown equivalent under concurrency at a ±0.05 margin. The choice is a per-workload one.
The engineering that produced the comparison is the transferable part: s _ection 3_ records the SpecForge backend, the auxiliary hidden-state capture and the draft geometry correction that no EAGLE-3 tooling supplied for a hybrid Mamba-2 target when this work began.
## 2. The system being tested
Nemotron 3.5 Lightning is a hybrid of three different layer types, and reaching its internal activations is what made this work an engineering project as much as a training run. Of its 52 layers, 23 are Mamba-2 state-space layers, 23 are mixture-of-experts with 128 routed experts and one shared expert, and only six are full attention. The vocabulary is 131,072 tokens. Generation uses multi-token prediction, so the model already speculates before any external draft head is added. No long-context measurement was taken; s _ection 8_ states that scope.
On a target that already predicts several tokens per forward pass, a comparison against unaccelerated decoding sizes the whole speculative gain rather than a draft head's contribution to it. Both figures appear here, and every comparison between draft heads is against the model's own native multi-token prediction head, running on the same node, the same engine, the same dataset and the same draft budget.
All measurements are on a bf16 early access checkpoint, identified by a per-file SHA256 manifest digest of 64624ed9…c746a0. Every figure in this document is bf16. Throughput and acceptance are properties of a numeric format as much as of a model, so none of them transfer to a checkpoint published in another format.
## 3. Speculative decoding on a hybrid Mamba-2 target
Generating text one token at a time leaves a modern GPU mostly idle, because each step waits on the one before it. Speculative decoding fills that idle capacity: a small, fast draft model guesses the next few tokens, and the large model checks all of them in a single forward pass. Guesses it would have made itself are kept, the first wrong guess and everything after it is thrown away, and the output is the same text the large model would have produced alone. The saving comes from doing one expensive pass where several would otherwise have been needed.
EAGLE-3 is one way of training that draft model, and it works by feeding on the target's own internal activations, which it takes from attention layers. That assumption is where this target became interesting: only 6 of this target's 52 layers are attention layers.
SpecForge, the training framework, had no nemotron_h backend; we added one, including auxiliary hidden-state capture for a hybrid stack. The head is trained on three intermediate layer outputs, [2, 26, 48].
Earlier heads carried seven key-value heads against the target's two, and vLLM could not reconcile the resulting KV-cache page size against a Mamba-2 target, failing inside unify_kv_cache_spec_page_size. A sweep over 13 configurations of dtype, attention backend and block size established that no runtime flag resolves a mismatched head, and the head was retrained at num_key_value_heads=2. The result is a one-layer, 400 MB draft head with a 32,000 token draft vocabulary against the target's 131,072.
The head serves on stock upstream vllm==0.25.1 installed from PyPI, with no fork, no weight conversion and no patch, because vLLM already implements the target side through SupportsEagle3 on NemotronHForCausalLM. SGLang requires one commit that adds the equivalent auxiliary capture to nemotron_h, one file and 57 added lines against four removed. That commit is the natural upstream contribution from this work and is offered to the SGLang project.
## 4. Throughput
Throughput was measured in the two regimes that matter to a deployment, because speculative decoding behaves very differently in each. A single request at a time is what a developer with a local agent experiences, and there the GPU has idle capacity to spare, which is exactly what speculation spends. A server handling many requests at once has no idle capacity, because the concurrent requests already fill it, and speculation has to earn its place against them. _Section 4.1_ covers the first, s _ection 4.2_ the second, and the crossover between them turned out to be the most useful result in this study.
### 4.1 Single stream
This is the regime the EAGLE-3 paper reports and the one a developer running a local coding agent occupies: one request in flight, temperature 0, generation ending at the model's own end-of-sequence token, one GPU per server. Tokens per second are output tokens. no-spec is the target served with speculative decoding disabled, MTP is the model's native multi-token prediction head, and ours is the EAGLE-3 head. Each arm runs at the draft budget that suits it best, which is two to five proposed tokens depending on the domain and the arm.  
Single stream comparison table  
|  Domain  |  node  |  no-spec  |  MTP (τ)  |  ours (τ)  |  ÷ no-spec  |  ÷ MTP  |  
| --- | --- | --- | --- | --- | --- | --- |  
|  Math  |  H200  |  327  |  537 (3.38)  |  **575 (3.63)**  |  1.76×  |  **1.07**  |  
|  Code  |  H200  |  311  |  474 (2.99)  |  **488 (2.76)**  |  1.57×  |  **1.03**  |  
|  Chat  |  H200  |  315  |  461 (2.82)  |  442 (2.15)  |  1.41×  |  0.96  |  
|  Math  |  B200  |  372  |  649 (4.18)  |  559 (3.63)  |  1.50×  |  0.86  |  
|  Code  |  B200  |  375  |  585 (2.98)  |  496 (2.75)  |  1.32×  |  0.85  |  
|  Chat  |  B200  |  376  |  562 (2.83)  |  450 (2.14)  |  1.20×  |  0.80  |  
Single stream comparison table  
|  Domain  |  
| --- |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  node  |  
| --- |  
|  H200  |  
|  H200  |  
|  H200  |  
|  B200  |  
|  B200  |  
|  B200  |  
|  no-spec  |  
| --- |  
|  327  |  
|  311  |  
|  315  |  
|  372  |  
|  375  |  
|  376  |  
|  MTP (τ)  |  
| --- |  
|  537 (3.38)  |  
|  474 (2.99)  |  
|  461 (2.82)  |  
|  649 (4.18)  |  
|  585 (2.98)  |  
|  562 (2.83)  |  
|  ours (τ)  |  
| --- |  
|  **575 (3.63)**  |  
|  **488 (2.76)**  |  
|  442 (2.15)  |  
|  559 (3.63)  |  
|  496 (2.75)  |  
|  450 (2.14)  |  
|  ÷ no-spec  |  
| --- |  
|  1.76×  |  
|  1.57×  |  
|  1.41×  |  
|  1.50×  |  
|  1.32×  |  
|  1.20×  |  
|  ÷ MTP  |  
| --- |  
|  **1.07**  |  
|  **1.03**  |  
|  0.96  |  
|  0.86  |  
|  0.85  |  
|  0.80  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
τ is acceptance, the mean number of tokens accepted per verification step. An acceptance of 3.0 means each target forward pass yields three tokens. Mathematics is GSM8K, code is HumanEval source fragments, chat is MT-Bench flattened to single turns. The ÷ no-spec and ÷ MTP columns describe the EAGLE-3 arm. Bold marks a value where the EAGLE-3 head leads native multi-token prediction, and carries that meaning in every table of this section. The B200 rows come from a separate set of runs, and every value in this table is a single measurement.
Figure 1. Throughput against unaccelerated decoding on H200 with vLLM, by domain, at one request and at 32 concurrent requests. Temperature 0, generation ending at the model's own end-of-sequence token, one GPU per server. The single-request values are the H200 rows of the ÷ no-spec column above, with each arm at its own best draft budget; the 32-request values come from the concurrency measurements reported below, at an equal three-token budget for both arms. Each value is a single measurement.  Figure 1. Throughput against unaccelerated decoding on H200 with vLLM, by domain, at one request and at 32 concurrent requests. Temperature 0, generation ending at the model's own end-of-sequence token, one GPU per server. The single-request values are the H200 rows of the ÷ no-spec column above, with each arm at its own best draft budget; the 32-request values come from the concurrency measurements reported below, at an equal three-token budget for both arms. Each value is a single measurement. 
On H200 the EAGLE-3 head is worth 1.41 to 1.76 times unaccelerated decoding and sits within a few percent of the model's own multi-token prediction head. On B200 it reaches 1.20 to 1.50 times, and native multi-token prediction leads it in all three domains. A few percent is inside the range a single measurement can produce by chance, which is why the three H200 cases were repeated twenty times per arm; s _ection 1.2_ carries that result. The repeat also holds the draft budget equal across the two arms, which is the stricter comparison and moves the code and mathematics ratios toward parity. In that repeat the EAGLE-3 head is 10.79% slower than native multi-token prediction on chat.
Figure 2. Throughput against the model's own native multi-token prediction head, H200 with vLLM at one request, over twenty repeated measurements per arm at an equal three-token draft budget, within one server session per arm and in the same twenty windows for both arms. Bars give a two-sample delta-method 95% interval on the ratio, which does not cover boot-to-boot variation. Mathematics spans parity; code sits above it and chat below it, both outside their intervals.  Figure 2. Throughput against the model's own native multi-token prediction head, H200 with vLLM at one request, over twenty repeated measurements per arm at an equal three-token draft budget, within one server session per arm and in the same twenty windows for both arms. Bars give a two-sample delta-method 95% interval on the ratio, which does not cover boot-to-boot variation. Mathematics spans parity; code sits above it and chat below it, both outside their intervals. 
### 4.2 Under concurrency
A served deployment runs many requests at once, and speculation behaves differently when the GPU is already busy. At 32 concurrent requests, aggregate throughput:  
Under concurrency table  
|  Domain  |  node  |  no-spec  |  MTP  |  ours  |  ÷ no-spec  |  ÷ MTP  |  
| --- | --- | --- | --- | --- | --- | --- |  
|  Math  |  H200  |  2197  |  4310  |  **4417**  |  2.01×  |  **1.02**  |  
|  Code  |  H200  |  2087  |  3768  |  **3789**  |  1.82×  |  **1.01**  |  
|  Chat  |  H200  |  2109  |  3716  |  3326  |  1.58×  |  0.89  |  
|  Math  |  B200  |  2912  |  5562  |  **5872**  |  2.02×  |  **1.06**  |  
|  Code  |  B200  |  2673  |  4861  |  4804  |  1.80×  |  0.99  |  
|  Chat  |  B200  |  2802  |  4907  |  4477  |  1.60×  |  0.91  |  
Under concurrency table  
|  Domain  |  
| --- |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  node  |  
| --- |  
|  H200  |  
|  H200  |  
|  H200  |  
|  B200  |  
|  B200  |  
|  B200  |  
|  no-spec  |  
| --- |  
|  2197  |  
|  2087  |  
|  2109  |  
|  2912  |  
|  2673  |  
|  2802  |  
|  4310  |  
| --- |  
|  3768  |  
|  3716  |  
|  5562  |  
|  4861  |  
|  4907  |  
|  ours  |  
| --- |  
|  **4417**  |  
|  **3789**  |  
|  3326  |  
|  **5872**  |  
|  4804  |  
|  4477  |  
|  ÷ no-spec  |  
| --- |  
|  2.01×  |  
|  1.82×  |  
|  1.58×  |  
|  2.02×  |  
|  1.80×  |  
|  1.60×  |  
|  ÷ MTP  |  
| --- |  
|  **1.02**  |  
|  **1.01**  |  
|  0.89  |  
|  **1.06**  |  
|  0.99  |  
|  0.91  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
At a single stream on B200, native multi-token prediction leads all three domains under this protocol: the EAGLE-3 head reaches 0.77 to 0.86 times its throughput, depending on whether each arm runs at its own best draft budget or both run at an equal one. That deficit closes under load: at 32 concurrent requests the head reaches parity on code and exceeds native multi-token prediction on mathematics on both node types.
The concurrency ladder below covers 1 to 128 concurrent requests. Each value is the best EAGLE-3 arm divided by native multi-token prediction at a three-token budget.  
Concurrency ladder  
|  Domain  |  node  |  B=1  |  B=4  |  B=16  |  B=32  |  B=64  |  B=128  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
|  Math  |  H200  |  **1.09**  |  **1.08**  |  **1.11**  |  **1.14**  |  **1.01**  |  0.87  |  
|  Code  |  H200  |  **1.03**  |  1.00  |  **1.07**  |  **1.08**  |  **1.03**  |  0.89  |  
|  Chat  |  H200  |  0.91  |  0.92  |  0.94  |  0.95  |  0.93  |  0.80  |  
|  Math  |  B200  |  0.97  |  **1.07**  |  **1.11**  |  **1.10**  |  0.93  |  0.71  |  
|  Code  |  B200  |  0.88  |  **1.02**  |  **1.08**  |  **1.06**  |  **1.01**  |  0.80  |  
|  Chat  |  B200  |  0.77  |  0.91  |  0.94  |  0.94  |  0.91  |  0.64  |  
Concurrency ladder  
|  Domain  |  
| --- |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  node  |  
| --- |  
|  H200  |  
|  H200  |  
|  H200  |  
|  B200  |  
|  B200  |  
|  B200  |  
|  **1.09**  |  
| --- |  
|  **1.03**  |  
|  0.91  |  
|  0.97  |  
|  0.88  |  
|  0.77  |  
|  **1.08**  |  
| --- |  
|  1.00  |  
|  0.92  |  
|  **1.07**  |  
|  **1.02**  |  
|  0.91  |  
|  B=16  |  
| --- |  
|  **1.11**  |  
|  **1.07**  |  
|  0.94  |  
|  **1.11**  |  
|  **1.08**  |  
|  0.94  |  
|  B=32  |  
| --- |  
|  **1.14**  |  
|  **1.08**  |  
|  0.95  |  
|  **1.10**  |  
|  **1.06**  |  
|  0.94  |  
|  B=64  |  
| --- |  
|  **1.01**  |  
|  **1.03**  |  
|  0.93  |  
|  0.93  |  
|  **1.01**  |  
|  0.91  |  
|  B=128  |  
| --- |  
|  0.87  |  
|  0.89  |  
|  0.80  |  
|  0.71  |  
|  0.80  |  
|  0.64  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The head leads from four to 32 concurrent requests on mathematics on both node types, and on code at every step in that range except four concurrent requests on H200, where the two arms are level. At 128 concurrent requests native multi-token prediction leads every domain, because a three-token draft continues to scale where a five-token budget saturates the verification step. A deployment serving at high concurrency should either reduce the draft budget or stop speculating. The crossover is domain- and node-dependent: on B200 mathematics it falls between 32 and 64 concurrent requests, and on H200 mathematics, H200 code and B200 code between 64 and 128.
Figure 3. Throughput against native multi-token prediction on H200 across the concurrency ladder. Each point is the best EAGLE-3 arm divided by native multi-token prediction at a three-token budget. The shaded span, four to 32 concurrent requests, is where the head leads on mathematics and, except at four concurrent requests, on code. Output length is forced to 512 tokens. Each point is a single measurement.  Figure 3. Throughput against native multi-token prediction on H200 across the concurrency ladder. Each point is the best EAGLE-3 arm divided by native multi-token prediction at a three-token budget. The shaded span, four to 32 concurrent requests, is where the head leads on mathematics and, except at four concurrent requests, on code. Output length is forced to 512 tokens. Each point is a single measurement. 
Figure 4. The same measurement on B200, on the vertical scale of Figure 3 so the two are read against one axis. The head starts below parity at one request, crosses above it from four to 32 concurrent requests, and falls further at 128 than it does on H200. Each point is a single measurement.  Figure 4. The same measurement on B200, on the vertical scale of Figure 3 so the two are read against one axis. The head starts below parity at one request, crosses above it from four to 32 concurrent requests, and falls further at 128 than it does on H200. Each point is a single measurement. 
This ladder forces 512 output tokens per request, where the canonical form of the protocol forces 1024. Both arms of every comparison ran at 512, so the ratios are controlled, and the absolute throughputs behind them are not comparable to a figure measured at 1024, ours or anyone else's.
### 4.3 Tree drafting and the choice of engine
vLLM proposes one linear continuation per verification step. SGLang can propose a branching set and verify every branch in the same pass, which raises the chance that some path through the tree matches what the target would have produced.  
Tree drafting table  
|  Domain  |  node  |  no-spec  |  MTP (τ)  |  ours (τ)  |  ÷ no-spec  |  ÷ MTP  |  
| --- | --- | --- | --- | --- | --- | --- |  
|  Math  |  B200  |  269  |  349 (3.37)  |  **415**(4.95)  |  1.54×  |  **1.19**  |  
|  Code  |  B200  |  269  |  306 (3.20)  |  **358**(4.66)  |  1.33×  |  **1.17**  |  
|  Chat  |  B200  |  270  |  298 (3.00)  |  **304**(4.12)  |  1.13×  |  **1.02**  |  
|  Math  |  H200  |  234  |  361 (3.36)  |  **394**(4.08)  |  1.68×  |  **1.09**  |  
|  Code  |  H200  |  234  |  321 (3.22)  |  314 (3.74)  |  1.34×  |  0.98  |  
|  Chat  |  H200  |  235  |  311 (3.01)  |  269 (3.22)  |  1.15×  |  0.87  |  
Tree drafting table  
|  Domain  |  
| --- |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  Math  |  
|  Code  |  
|  Chat  |  
|  node  |  
| --- |  
|  B200  |  
|  B200  |  
|  B200  |  
|  H200  |  
|  H200  |  
|  H200  |  
|  no-spec  |  
| --- |  
|  269  |  
|  269  |  
|  270  |  
|  234  |  
|  234  |  
|  235  |  
|  MTP (τ)  |  
| --- |  
|  349 (3.37)  |  
|  306 (3.20)  |  
|  298 (3.00)  |  
|  361 (3.36)  |  
|  321 (3.22)  |  
|  311 (3.01)  |  
|  ours (τ)  |  
| --- |  
|  **415**(4.95)  |  
|  **358**(4.66)  |  
|  **304**(4.12)  |  
|  **394**(4.08)  |  
|  314 (3.74)  |  
|  269 (3.22)  |  
|  ÷ no-spec  |  
| --- |  
|  1.54×  |  
|  1.33×  |  
|  1.13×  |  
|  1.68×  |  
|  1.34×  |  
|  1.15×  |  
|  ÷ MTP  |  
| --- |  
|  **1.19**  |  
|  **1.17**  |  
|  **1.02**  |  
|  **1.09**  |  
|  0.98  |  
|  0.87  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
B200 rows use a tree five steps deep with eight branches and sixteen draft tokens; H200 rows use a chain five steps deep. On B200 the head leads native multi-token prediction on all three domains, and the tree reaches an acceptance of 4.95 on mathematics, the highest figure measured anywhere in this study.
The highest acceptance does not identify the fastest deployment, because SGLang is the slower engine on this model by a factor of 1.35 on this head: measured at a single stream on B200 it reaches 559 tokens per second on vLLM against 415 on SGLang. Native multi-token prediction's own gap between the engines is wider still, at 649 against 349. Matching the draft width at three tokens on both engines and comparing 63 matched measurements on one H200 node isolates the engine from the speculation depth:  
Comparison table  
|  Arm  |  SGLang ÷ vLLM, mean  |  vLLM faster by  |  
| --- | --- | --- |  
|  No speculation  |  0.756  |  1.32×  |  
|  Native MTP, three tokens  |  0.675  |  1.48×  |  
|  Ours, three tokens  |  0.664  |  1.51×  |  
Comparison table  
|  No speculation  |  
| --- |  
|  Native MTP, three tokens  |  
|  Ours, three tokens  |  
|  SGLang ÷ vLLM, mean  |  
| --- |  
|  0.756  |  
|  0.675  |  
|  0.664  |  
|  vLLM faster by  |  
| --- |  
|  1.32×  |  
|  1.48×  |  
|  1.51×  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Acceptance agrees across the two engines to within two percent, at a mean ratio of 1.019 for this head over 21 paired measurements, so the difference is engine implementation rather than drafting. The gap also widens with load: from one to 64 concurrent requests on mathematics the unaccelerated deficit narrows from 0.71 to 0.79 while both speculative arms widen from about 0.65 to 0.51, so SGLang's speculative path scales worse with batch size than vLLM's on top of a baseline disadvantage. On this model, vLLM with a chain is the configuration to deploy, and the tree is the configuration that produces the best acceptance number.
### 4.4 Acceptance, throughput and batch size
Acceptance moves by less than two percent from one to 64 concurrent requests on mathematics and code, for every arm; chat rises 4.6 to 9.7%. Over the same range the EAGLE-3 head's speedup against unaccelerated decoding decays from 1.67 to 1.42 times on mathematics, while its acceptance holds. The cause sits in the hardware rather than in the head: the GPU is running out of spare compute to spend on verification. A serving stack should therefore decide whether to speculate from batch size, because acceptance gives no signal that the transition has happened.
Figure 5. Accepted tokens per verification step against concurrency on mathematics, SGLang, for native multi-token prediction and for two draft budgets of this head, with acceptance scoped measurement each. Two measured points per arm, at one and at 64 concurrent requests. Acceptance moves by less than two percent across that range for every arm.  Figure 5. Accepted tokens per verification step against concurrency on mathematics, SGLang, for native multi-token prediction and for two draft budgets of this head, with acceptance scoped measurement each. Two measured points per arm, at one and at 64 concurrent requests. Acceptance moves by less than two percent across that range for every arm. 
Figure 6. Throughput against unaccelerated decoding on the runs of Figure 5, at the same two concurrency points. The speedup falls 15% while acceptance is flat, which is the divergence this section describes.  Figure 6. Throughput against unaccelerated decoding on the runs of Figure 5, at the same two concurrency points. The speedup falls 15% while acceptance is flat, which is the divergence this section describes. 
Higher acceptance can produce lower throughput. On chat a five-token chain reaches an acceptance of 2.488 against a three-token chain's 2.281, and 244.7 tokens per second against 259.7, because speedup follows approximately τ / (N·c + 1), where N is the draft budget and c the cost of a draft forward pass relative to a target one. A deeper chain can buy more cost than acceptance. Across ten draft geometries the fastest configuration on chat carries the lowest acceptance of the set.
At equal draft budget this head's acceptance is below native multi-token prediction's in all six single-stream cases, at 0.85 to 0.95 times, so where the head wins throughput it does so on a draft forward pass that costs less per verification step rather than on more accepted tokens per step. That is a hardware-cost effect, and improved draft kernels would reduce it.
## 5. Output and task equivalence
Speed is only worth having if the answers do not change, and speculative decoding is designed so they cannot: a drafted token is kept only when the target model would have chosen it anyway. That is a guarantee about the mathematics, and this section asks whether it survives contact with a real serving stack. It does, and establishing it turned up two properties of the stack that any team measuring this model will meet.
The first is that the throughput-optimal configuration is not reproducible run to run. With --moe-backend flashinfer_cutlass, the same server given the same prompt twice at temperature zero returns identical text about 20% of the time. The likely mechanism is a non-associative reduction in the fused mixture-of-experts router, which selects six experts of 128. An exact-match test on those flags is therefore measuring the engine, not the draft head, so equivalence was measured on the deterministic default backends.
The second is that two servers started from the same flag set either agree almost completely or disagree almost completely, and which of the two is fixed when the process starts. Three successive launches of an unaccelerated pair agreed on two of 140, then 164 of 164, then four of 164, with no draft head anywhere in the comparison. Byte-exact agreement is therefore an instrument only between two servers first shown to be in the same state, which an unaccelerated pair establishes; without that check a single figure mixes the launch state with the effect being measured, and the launch state is the larger by an order of magnitude.
Between two servers in the same state, at a 4096-token cap on whole problems, this head agrees with unaccelerated decoding on 153 of 164 code prompts and 163 of 164 on mathematics. The model's own native multi-token prediction head differs on the same prompts, in the same counts. An earlier measurement at a 512-token cap returned 150 of 150 byte-identical completions; its own re-run on a later node returned one of 50 on code, which the launch-state effect accounts for, so the July figure describes one pair of servers rather than the stack.
Byte-exact agreement holds at batch 1 only. Outputs are not batch-invariant on any backend: a server that agrees with itself completely at batch 1 does so 31% of the time at 32 concurrent requests on mathematics, over 32 prompts. That property belongs to the serving stack rather than to a drafter, so task accuracy carries the equivalence claim under load.
GSM8K exact match at temperature 0 and concurrency 32, 1319 problems per arm, graded strictly:  
Comparison table  
|  Arm  |  Exact match  |  Difference against no-spec  |  
| --- | --- | --- |  
|  Unaccelerated  |  0.6823  |  
|  Native MTP  |  0.6808  |  −0.0015  |  
|  EAGLE-3 head  |  0.6869  |  +0.0045  |  
Comparison table  
|  Unaccelerated  |  
| --- |  
|  Native MTP  |  
|  EAGLE-3 head  |  
|  Exact match  |  
| --- |  
|  0.6823  |  
|  0.6808  |  
|  0.6869  |  
|  Difference against no-spec  |  
| --- |  
|  −0.0015  |  
|  +0.0045  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Equivalence is established by two one-sided tests at a ±0.05 margin rather than by a single hypothesis test, which could show only a failure to reject equality. All arms reject both nulls at p < 0.01. The margin is limited by the sample rather than by the difference: at n=1319 the standard error of the difference is 0.018, so no margin below ±0.030 is demonstrable however small the true gap, and this arm's observed difference supports ±0.035.
## 6. Cost per output token
On self-hosted hardware the cost of a token is time on a GPU, so a throughput gain converts directly into a cost saving with no billing model in between. The figures below are derived that way, from measured throughput rather than read off an invoice, and no billed cost measurement was taken for this model.
At fixed hardware and fixed parallelism, GPU time per output token is the reciprocal of throughput per GPU, so a throughput ratio converts directly into a cost ratio. Against unaccelerated decoding on H200, the 1.76 times single-stream figure on mathematics is a 43% reduction in GPU-seconds per output token and the 2.01 times figure at 32 concurrent requests is a 50% reduction. Against native multi-token prediction the repeated equal-budget measurement on mathematics is at parity, 1.0003 with a 95% interval of [0.9935, 1.0070], so no cost reduction against that baseline is demonstrated at a single stream; at 32 concurrent requests the single measurement gives 2.4%. The larger figure against unaccelerated decoding is mostly delivered by the model's own multi-token prediction head rather than by this one.
One worked absolute example, using the B200 concurrency-32 mathematics row above. The rate basis is 5.00 US dollars per B200 GPU-hour, taken from a survey of 26 rental providers in mid-2026 whose median was about 4.49 dollars per GPU-hour, and whose spot and budget marketplaces quoted 2.10 to 2.80 dollars for the same device. The basis therefore sits above the surveyed median, so it does not flatter these figures against open-market procurement:  
Comparison table  
|  Arm  |  Throughput  |  Derived cost per 1M output tokens  |  
| --- | --- | --- |  
|  Unaccelerated  |  2912 tok/s  |  $0.477  |  
|  Native MTP  |  5562 tok/s  |  $0.250  |  
|  EAGLE-3 head  |  5872 tok/s  |  $0.237  |  
Comparison table  
|  Unaccelerated  |  
| --- |  
|  Native MTP  |  
|  EAGLE-3 head  |  
|  Throughput  |  
| --- |  
|  2912 tok/s  |  
|  5562 tok/s  |  
|  5872 tok/s  |  
|  Derived cost per 1M output tokens  |  
| --- |  
|  $0.477  |  
|  $0.250  |  
|  $0.237  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
These throughputs were measured on a reserved hyperscaler capacity block at 10.37 dollars per GPU-hour, about 2.1 times the basis, and the same survey puts that vendor's on-demand rate for this device at about 2.8 times it. 
Cost per token is exactly linear in the rate, so a deployment procuring through a hyperscaler pays proportionally more than the table shows and one procuring on the open market pays less, while the ratios between the three arms are untouched.
## 7. Relation to NVIDIA's own measurements
NVIDIA's own performance figures for this model were taken on a different device, at a different concurrency, on a different workload, and are described in NVIDIA's launch material. Absolute tokens per second from the two sources describe different conditions and are not compared here.
This write-up measured H200 and B200 with one GPU per server, on single-turn corpora whose median prompt is 231 characters on mathematics, closed-loop with natural stopping and on a fixed-length ladder, comparing this model against itself under a different decoding configuration. No comparison against another vendor's model appears, because none was measured. Nothing here speaks to accuracy: the tasks measured are GSM8K, HumanEval fragments and MT-Bench, none of which is an agentic benchmark.
## 8. Limitations
  1. Native multi-token prediction leads this head in three regimes: on chat at a single stream on H200, by 10.79% over twenty repeated measurements per arm; at a single stream on B200 across all three domains, where the head reaches 0.77 to 0.86 times its throughput; and at 128 concurrent requests on every domain and both node types. Its acceptance at equal draft budget is also higher in all six single-stream cases.
  2. Open-loop measurement was not run, so no goodput figure at a latency target exists. The time to first token is not comparable between separately launched servers. One such comparison showed a 43.6% difference that proved to come from the --mamba-backend setting rather than from the drafter.
  3. No multi-turn or long-context measurement exists. Servers ran at a maximum model length of 8192 tokens and the heads trained at sequence lengths of 4,096 and 12,288, so nothing here speaks to the model's 1M context or to multi-turn agentic workloads.
  4. Outside the twenty-repeat measurements of s _ection 1.2_ , the code corpus continues HumanEval source fragments rather than completing HumanEval problems, because the prompt file was split on newlines rather than on problem boundaries. _Section 1.2_ and the 4096-token re-run in s _ection 5_ use the corrected 164-problem corpus. Both arms received identical prompts in the same session throughout, so the ratios are controlled measurements of a narrower workload than the label suggests.
  5. The tables draw on three draft heads of one architecture. Head A produced every H200 vLLM figure and is the proposed release artifact; head B produced only the three H200 rows of the SGLang table; head C produced every B200 figure. A and C were both trained on B200 and differ in training corpus and in training sequence length, 4,096 against 12,288; B and C differ in training node. Measured on one H200 machine at a single stream over twenty repeats per arm at a 4096-token cap, head C exceeds head A by 1.5% on mathematics, 2.2% on code and 1.2% on chat, each outside its interval, and B and C separate by 4.9% on mathematics. Both separations are larger than the mathematics and code effects in s _ection 1.2_ and smaller than the chat effect, and no head has been measured against another across the full matrix. Every measurement records which of the three served it, and each head is identified by a SHA256 of its weights.
  6. Every repeated measurement is on H200 with vLLM. The B200 runs, the SGLang concurrency runs and the tree results are single measurements.
  7. Whether this head retains its acceptance against a target carrying a merged domain adapter is not measured. Every figure here is against the unadapted target, and the companion write-up's adapters are merged into the target weights.
  8. The throughput-optimal serving configuration is not reproducible run to run, which constrains deployments needing byte-identical transcripts, cached evaluations or reproducible bug reports. A deterministic fused mixture-of-experts router would resolve it.


## 9. Reproduction
The head serves on stock upstream vLLM:

```
  



| pip install vllm==0.25.1

 |  
| --- |  




| VLLM_ATTENTION_BACKEND=FLASHINFER \
 |  



| CUDA_VISIBLE_DEVICES=0 vllm serve /path/to/nemotron-3-5-lightning \
 |  



|   --trust-remote-code --tensor-parallel-size 1 \
 |  



|   --gpu-memory-utilization 0.85 --max-model-len 8192 \
 |  



|   --mamba-backend flashinfer --moe-backend flashinfer_cutlass --no-enable-prefix-caching \
 |  



|   --speculative-config '{"model":"/path/to/eagle3-head","method":"eagle3","num_speculative_tokens":3}' \
 |  



|   --port 30032

 |  


```
Copy
The native multi-token prediction arm replaces the speculative configuration with {"method":"mtp","num_speculative_tokens":3}; the unaccelerated arm omits it. The draft path is a local directory holding config.json and model.safetensors, and no conversion step exists because none is required. Equivalence measurements leave --mamba-backend and --moe-backend at their defaults, for the reason given above.
Four configuration requirements each produced a wrong measurement rather than an error.
  1. ~/.cache/vllm/torch_compile_cache/ must be cleared when swapping draft heads. The compile cache key does not encode the draft's attention geometry, so a stale graph is reused and fails at generation time, after the server has reported healthy.
  2. Achieved concurrency must be verified for every measurement. A request for 64 concurrent streams against a server capped at 8 measures 8 with a queue, and reports normally.
  3. Each concurrent vLLM instance needs its own VLLM_CACHE_ROOT and TRITON_CACHE_DIR. Mamba-2 Triton warmup takes about five minutes per instance and instances sharing a cache serialize on it.
  4. On SGLang, --cuda-graph-max-bs must equal --max-running-requests, and --disable-radix-cache is required for nemotron_h speculative decoding. Batches above the graph limit run in eager mode, which presents as a 4 to 5 times regression.


Acceptance is read from vllm:spec_decode_num_accepted_tokens_total and vllm:spec_decode_num_drafts_total immediately before and after each measurement. SGLang exposes only the running ratio avg_spec_accept_length, which accumulates from server start, so a harness reading it once at the end of a run reports a blend of everything measured on that server. The signature is recognizable: values go flat across datasets and land on each server's lifetime mean.
## 10. Conclusions
Nemotron 3.5 Lightning ships an outstanding speculative decoder, enabled by default, and it is the headline result of this work. Native multi-token prediction is worth 1.46 to 1.96 times unaccelerated decoding on its own, across both node types and both concurrency points measured. At an equal draft budget it accepts more tokens per verification step than a head trained specifically for this target, in all six single-stream cases, and it holds the highest absolute throughput recorded anywhere in this study. An organization deploying this model has all of that on the first day, on stock vLLM, with nothing to train, no second artifact to version and no draft head to keep in step with the target as it is updated. A default this strong is a rare thing to find already in place.
The EAGLE-3 head leads in two measured regimes. On H200 at a single stream it exceeds native multi-token prediction on code by 1.11% and matches it on mathematics, over twenty repeated measurements per arm. Between 4 and 32 concurrent requests it leads on mathematics on both node types, and on code at every step in that range except four concurrent requests on H200, where the two arms are level. On SGLang with a tree it reaches an acceptance of 4.95, the highest figure in the study. Native multi-token prediction is the better choice on B200 at a single stream and above 64 concurrent requests on both node types. Both paths carry the single-stream output residual against unaccelerated decoding reported in s _ection 5_ , and task accuracy shown equivalent under concurrency at a ±0.05 margin, so the choice is a per-workload one.
The engineering transfers beyond this model. When this work started, no EAGLE-3 tooling supported a hybrid Mamba-2 target: s _ection 3_ records the SpecForge backend, the auxiliary hidden-state capture and the draft geometry correction that made one trainable, and the SGLang commit is offered upstream. Many open models ship no multi-token prediction head, or one a serving stack cannot reach, and for those targets that route is how the same 1.2 to 2.0 times on vLLM is obtained. The measurement design is the other half: establishing where each head leads took 2,091 individual measurements, and the two findings that a smaller study would have missed are that acceptance does not indicate when speculation stops paying, and that the configuration with the highest acceptance is not the fastest one to deploy.
An organization starting from here would take a high-value workload whose data cannot leave its environment, measure the serving configuration against that workload rather than against a published figure, and hold the result to the baseline the model already provides. On this model that baseline is 1.46 to 1.96 times unaccelerated decoding, which is a demanding place to start from and an excellent one to deploy against.
**_This write-up covers speculative decoding.[Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains](https://research.thoughtworks.com/library/post-training-nvidia-nemotron-3-5-lightning-enterprise-domains) is its companion, and the two are submitted together. Every figure here is stated with the conditions that produced it, and the software versions are in _section 9 _. The draft head was trained and measured on Thoughtworks-operated AWS instances._**
##  Keep reading 
  * [ Insights Teaching a model to stop writing like a model By  **Allen Roush** How can we make an AI model write less like a model and more like a human?  ](https://research.thoughtworks.com/library/teaching-model-stop-writing-like-model)
  * [ Insights Cultural counterfactuals By  **Phillip Howard** , **Xin Su** , **Parag Mahajani** Discover the 'Cultural Counterfactuals' dataset. We help you uncover hidden bias in AI vision models related to religion, nationality, and socioeconomic status.  ](https://research.thoughtworks.com/library/cultural-counterfactuals)
  * [ Insights Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains By  **Gustavo Lujan** Using post-training techniques to improve model performance.  ](https://research.thoughtworks.com/library/post-training-nvidia-nemotron-3-5-lightning-enterprise-domains)