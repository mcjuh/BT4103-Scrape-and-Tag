<!-- Source: https://research.thoughtworks.com/library/teaching-model-stop-writing-like-model | Title: Teaching a model to stop writing like a model | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Teaching a model to stop writing like a model
**An 'antislop' fine-tune of Nemotron 3.5 Nano**
By 
Published: August 11, 2026 
## The problem, in one word: slop
Ask almost any modern open source language model to write a short story and watch what happens. Somewhere in the first few paragraphs, a character will speak “in a voice barely above a whisper.” The air will smell of ozone. Someone’s heart will hammer against their ribs. And there is a good chance the protagonist will be named Elara or Kael.
None of those phrases is wrong. Each one is perfectly serviceable English. The problem is frequency. In our research we found that some phrases appear more than a thousand times more often in model output than in text written by humans. The name Elara showed up 85,513 times more often in one model’s creative writing than in human writing. Readers notice this. They may not be able to name the specific phrases, but they develop a reliable instinct for text that feels machine made, and that instinct is largely built on repetition they cannot quite articulate.
We call this slop. It is the single most recognizable signature of AI generated prose, and it degrades output quality in a way that standard benchmarks do not capture at all. A model can score well on reasoning, math and knowledge tests while still producing writing that any attentive reader will flag as synthetic within a paragraph.
## Why AI language slop is hard to fix
The obvious fix is to ban the offending words. That fails badly in practice.
Language models do not see words. They see tokens, which are fragments of words. If you ban the word “catatonic” and the model’s tokenizer splits it into “cat” and “atonic,” you have accidentally banned every word starting with “cat.” Do this across a few thousand phrases and the model’s vocabulary develops holes it cannot route around. In our experiments, straightforward token banning caused writing quality to collapse once the ban list grew past a couple of thousand entries.
Simply asking the model to avoid these phrases does not work either. Telling a model “do not write about tapestries” reliably makes tapestries more likely to appear, a phenomenon researchers have named the pink elephant problem.
## Our approach
We published a framework [called 'Antislop' earlier this year](https://arxiv.org/pdf/2510.15061), together with Samuel Paech, Judah Goldfeder and Ravid Shwartz-Ziv. It has three parts that work together.
  * **Finding the slop.** We generate a large sample of the model’s writing and compare the frequency of every word and phrase against how often humans use them. What comes back is a fingerprint of that specific model’s verbal tics. Different model families have different fingerprints, so this step has to be run per model.


  * **Suppressing it during generation.** Rather than blocking a banned phrase before it starts, our sampler watches the text as it is written. When a banned phrase appears, the sampler rewinds to where the phrase began, makes that particular word less likely, and writes forward again. Because the check happens after the full phrase has appeared, there are no false positives on innocent words that merely start the same way. This handles thousands of banned patterns without damaging the model’s vocabulary.


  * **Training it in permanently.** The sampler works well, and it also slows generation down considerably, because every rewind means redoing work. So we use the sampler to teach the model instead. Every time it rewinds, we record a small lesson: _at this exact point in this exact sentence, the model reached for word X, and here are the better alternatives it could have used_. Collect tens of thousands of those lessons and you can train the preference directly into the weights with a method we call Final Token Preference Optimization, or FTPO. The trained model then runs at full speed with the improved writing habits built in.


The reason FTPO matters is precision. Teaching a model to stop preferring its favorite words requires nudging some fairly strong preferences, and a clumsy nudge damages everything nearby. FTPO adjusts only the specific choices that need adjusting and holds the rest of the model’s vocabulary steady while it does so.
## What we did with Nemotron 3.5 Nano
We ran this full pipeline against NVIDIA’s Nemotron 3.5 Nano EA2 checkpoint on two H100 GPUs over about thirteen hours.
The pipeline generated 1,000 samples of creative writing from the original model, compared them against a human baseline built from published fiction and online writing communities, and assembled a list of 4,267 overused patterns. It then regenerated the same 1,000 prompts with the sampler active, recording a preference lesson at every point where it had to intervene. That produced roughly 13,000 training examples. We trained on those and merged the result back into a standard model checkpoint.
To evaluate honestly, we held back 400 writing prompts that the model had never been trained on, generated from both the original and the tuned model with identical settings, and turned the sampler off entirely. That last detail matters. With the sampler switched off, any improvement we measure has to come from what the training actually changed inside the model.
## Results  
Table showing the results of an antislop experiment  
|  What we measured  |  Original  |  Antislop  |  Change  |  
| --- | --- | --- | --- |  
|  Overused patterns suppressed  |  0%  |  **66.4%**  |  Two thirds removed  |  
|  Writing quality (0 to 100)  |  54.3  |  53.3  |  No significant change  |  
|  Vocabulary richness (index)  |  100  |  98.4  |  Essentially unchanged  |  
|  MMLU, general knowledge  |  0.838  |  **0.843**  |  Slightly better  |  
|  GSM8K, grade school math  |  0.924  |  **0.936**  |  Slightly better  |  
Table showing the results of an antislop experiment  
|  What we measured  |  
| --- |  
|  Overused patterns suppressed  |  
|  Writing quality (0 to 100)  |  
|  Vocabulary richness (index)  |  
|  MMLU, general knowledge  |  
|  GSM8K, grade school math  |  
|  Original  |  
| --- |  
|  54.3  |  
|  100  |  
|  0.838  |  
|  0.924  |  
|  Antislop  |  
| --- |  
|  **66.4%**  |  
|  53.3  |  
|  98.4  |  
|  **0.843**  |  
|  **0.936**  |  
|  Change  |  
| --- |  
|  Two thirds removed  |  
|  No significant change  |  
|  Essentially unchanged  |  
|  Slightly better  |  
|  Slightly better  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Two thirds of the model’s identified verbal tics are gone. Writing quality, scored by an independent language model against a six part rubric covering grammar, coherence, repetition and overall craft, is statistically unchanged. We ran this as a paired comparison over 150 outputs per model and the confidence interval on the difference crosses zero, meaning we cannot distinguish the two models on quality.
The capability benchmarks are the reassuring part. A common failure mode when tuning a model for style is that its reasoning quietly degrades. Both general knowledge and math performance came out slightly higher after tuning. Those gains are small enough that we read them as noise, and the important finding is that neither moved backwards.
Vocabulary richness deserves a note. When other researchers apply more conventional preference training to this problem, the model’s vocabulary tends to contract as it learns to avoid banned words by simply using fewer words overall. We measured a collapse to as low as 74% of baseline with those methods. Here we measured 98.4%, which means the model found genuinely different phrasings instead of retreating into a smaller vocabulary.
## Agentic benchmarks
MMLU and GSM8K are both several years old, and neither is agentic. Neither one tests whether a model can carry out multi step work using tools, which is how most people actually deploy these models now. So we ran a second round on harder and more current evaluations.
The most relevant of these is τ-bench. It places the model in a customer service role, hands it a set of tools that read and write to a mock company database, and has a separate language model play the customer. Scoring a point means completing the customer’s actual request correctly, which typically takes ten or more conversational turns and several chained tool calls, with the model needing to look up the right records before acting on them. We ran both the retail and airline domains, three trials each, for a total of 495 task attempts per model.  
Agentic benchmarks  
|  What we measured  |  Original  |  Antislop  |  Change  |  
| --- | --- | --- | --- |  
|  τ-bench, customer service agent  |  0.640  |  0.624  |  No significant change  |  
|  MMLU-Pro, harder knowledge and reasoning  |  0.703  |  0.713  |  No significant change  |  
|  HumanEval+, code that has to actually run  |  0.750  |  0.707  |  No significant change  |  
|  IFEval, following explicit instructions  |  0.387  |  0.387  |  Identical  |  
Agentic benchmarks  
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
Every one of these differences sits inside the measurement noise (statistically not significant). The confidence interval on the τ-bench comparison runs from roughly seven points down to four points up, so the two models are indistinguishable on it. MMLU-Pro came out marginally ahead for the tuned model. IFEval came out identical to three decimal places, because IFEval measures whether a model obeys explicit output constraints such as word counts, required keywords, and formatting rules. If a style focused fine-tune were going to break something, that ability is exactly where the damage would show, and it is untouched.
Taken together with the creative writing results above, this is the outcome we hoped for. The model writes noticeably less like a machine and performs the same on knowledge, reasoning, code, instruction following, and multi step tool use.
Running the identical IFEval prompts twice through the identical model at temperature zero gave 0.4025 and 0.3870, because the serving stack batches requests in ways that make even greedy decoding slightly non deterministic. Anything under roughly two points here is unmeasurable, whatever the point estimates happen to say. For the same reason we ran τ-bench across three trials rather than one, since a single pass over a fifty task domain carries more than ten points of sampling noise on its own.
## What the model was actually overusing
The list the pipeline produced is worth reading on its own, because it is a candid portrait of how this model writes when left alone.
Atmosphere and sensory description dominate. The air "smelled of ozone", "tasted of ozone", "grew thick, grew heavy," "filled lungs" and "turned crisp", over and over. Characters constantly "adjusted their collars", "adjusted their straps" and had their Adam’s apples bob.
Names were remarkably concentrated. Elara, Elias, Silas, Kael, Kaelen, Clara, and Julian carried an enormous share of the model’s cast, usually attached to templated dialogue tags along the lines of “Elara said", "her voice” and “Silas said", "his voice.”
At the level of individual words the model leaned on absently, acrid, ached, arced, barked, stared, trembling, blinked, froze, muttered and flickered. That last one is notable, because in earlier work we profiled 67 different models and found flickered among the top overused words in 98.5% of them. It appears to be close to a universal tell.
Our favorite discovery is that the pipeline flagged the phrase “Raid: Shadow Legends” as statistically overused. Somewhere in its training the model absorbed enough mobile game advertising that it reaches for the phrase unprompted while writing fiction.
## Limitations we want to be straight about
We would rather flag these ourselves than have them found later.
One writing metric did move. Of the six quality criteria we scored, five showed no significant change. One did. Consistency of tense, pronouns, and narrative perspective declined by a small but statistically real margin. We think the cause is structural. FTPO works by adjusting the model’s very last decision before it commits to each word, and grammatical agreement is exactly that kind of last moment decision. It is worth monitoring in any deployment.
We did not test very long writing. Our evaluation covers outputs of roughly a thousand words. Repetition problems become most visible in much longer work, over tens of thousands of words across multiple turns. Our claim that quality is preserved is well supported at normal lengths and untested beyond them.
Suppression could go higher. Nemotron 3.5 Nano uses a mixture of experts architecture, which changes where a fine-tune can safely attach. We took the conservative route and trained only the model’s final output layer, which is the same restriction we applied to large Llama models in the paper, where it also produced around 66% suppression. Models with more conventional architectures reached 83% to 92% under our full method. There is real headroom here for anyone willing to work out how to safely tune inside the expert layers.
The ban list would benefit from human review. The pipeline is automatic and it occasionally flags ordinary vocabulary that happens to be rare in our human reference texts. Words like antiseptic, archivist, and antechamber ended up on the list. The effect is mild, and an hour of manual pruning would improve the next run.
## What we are proposing
We would like to explore co-releasing this Antislop checkpoint alongside Nemotron 3.5 Nano.
The case is straightforward. The tuned model writes noticeably less like a machine while performing the same or slightly better on standard benchmarks, and the method that produced it is published, reproducible, and MIT licensed. Everything from this run is available, including the trained model, the adapter, the full ban list, the training data, the evaluation harness, and every log.
Adding the long form writing evaluation, expanding to 2,000 prompts and three refinement passes, and hand reviewing the ban list would cost roughly eight to ten hours of compute and would give an even stronger artifact plus the one piece of evidence we are currently missing.
##  Keep reading 
  * [ Insights EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning EAGLE-3 speculative decoding for NVIDIA Nemotron 3.5 Lightning By  **Gustavo Lujan** Experimenting with speculative decoding using the EAGLE-3 draft head.  ](https://research.thoughtworks.com/library/eagle-3-speculative-decoding-nvidia-nemotron-3-5-lightning)
  * [ Insights Cultural counterfactuals By  **Phillip Howard** , **Xin Su** , **Parag Mahajani** Discover the 'Cultural Counterfactuals' dataset. We help you uncover hidden bias in AI vision models related to religion, nationality, and socioeconomic status.  ](https://research.thoughtworks.com/library/cultural-counterfactuals)
  * [ Insights Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains Post-training NVIDIA Nemotron 3.5 Lightning for enterprise domains By  **Gustavo Lujan** Using post-training techniques to improve model performance.  ](https://research.thoughtworks.com/library/post-training-nvidia-nemotron-3-5-lightning-enterprise-domains)