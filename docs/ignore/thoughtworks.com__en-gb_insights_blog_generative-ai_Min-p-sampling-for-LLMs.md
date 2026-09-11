<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/Min-p-sampling-for-LLMs | Title: Min-p sampling for LLMs  | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Min-p sampling for LLMs 
A novel and efficient method of balanced text generation 
[ Engineering Stack Back ](https://www.thoughtworks.com/en-gb/engineering)
Close


By 
Published: September 22, 2025 
_**Min- sampling is an MIT-licensed technique — a Thoughtworks AI researcher is one of the authors of the research that developed it. Thoughtworks is also the first organization to integrate it in a client setting.**_
At the core of LLMs is their ability to predict the next correct word (or token) to their previously generated output in response to the input provided. The input content gets converted into tokens and then into embeddings; at the output layer, the embeddings get reconverted into tokens. 
The challenge, for the model, lies in the process of identifying the right token as an output for a given input. This process is statistical and stochastic in nature. It’s called sampling. In other words, LLMs generate text by sampling the next token from a probability distribution over the vocabulary at each decoding step.
Sampling is a strategy to help the model pick a word from the list it's given. If it chooses only the top options the output will be fairly safe but not very creative; choosing randomly from the whole list, meanwhile, can lead to deeply chaotic outputs. chaotic. _The magic, when it comes to LLMs, lies in the middle._ Striking this balance, however, isn't easy.
One solution is **min sampling,** a stochastic technique that varies its truncation threshold based on the model’s confidence, making the threshold context-sensitive. The thresholds are relative and depend on how certain the distribution is for that token. 
##  Sampling techniques and their limitations
**Min** sampling is a response to the limitations of existing sampling techniques. Before getting into the details of  _**min-**_ sampling, let's take a look at established approaches and why they often fall short when it comes to LLMs.
  * **Greedy decoding and beam search** are independent and commonly used quasi-deterministic techniques designed to select the most likely next token at each step during text generation. Both techniques prioritize the highest-priority choices, which means they can miss more diverse and highly creative outputs.
  * **Temperature** is a kind of a risk controller. Low temperature makes the model play it safe, while high temperature encourages it to take risks and explore less likely words for more creativity. 
  * **Top(stochastic) sampling** is a family of techniques. Top- sampling selects the next token from the most probable candidates at each step of generation, but the technique doesn’t adapt to changing levels of model confidence — with low -values, the model becomes overly conservative, which limits its creativity. At high temperatures, it generates noisy and incoherent outputs.
  * **Top- (nucleus) sampling** works by dynamically selecting the smallest set of tokens whose cumulative mass probability exceeds a pre-defined threshold: . However, the method can still produce repetitive and incoherent text, especially at high temperature settings. Lower “” makes the output more conservative, whereas higher “” invites the model to make riskier choices. 
  * **Dynamic threshold sampling** adjusts the token threshold based on model confidence. This does, however, require careful tuning of model confidence. High temperatures (T>2) flatten the probability distribution, which means many tokens get similar (ie., low) probabilities, which can lead to degeneration, repetition or even nonsense — even with top/top- .


The graphic below provides a visual comparison of each of the above sampling methods: 
Figure (a) shows initial token distribution. Figure (b) shows top-sampling. Figure (c) shows top- sampling. Figure(d) shows min- sampling. 
Creativity is just hallucination when we want it; hallucination is creativity when we don't want it. 
## Min- sampling: An innovative technique 
Considering all the drawbacks of sampling techniques discussed above, we want to introduce you to a new technique called “min-” that dynamically adjusts the sampling threshold based on the model’s confidence at each step of decoding. Min- sampling dynamically adjusts its threshold based on the model’s confidence focusing on likeliest tokens when confident and allows more diverse options when uncertain. This dynamic threshold balances coherence and diversity better than top- and top- sampling. 
The core idea is simple: stop using fixed cutoffs. Min- sampling is a stochastic technique that varies its truncation threshold based on the model’s confidence, making the threshold context-sensitive. The thresholds are relative and depend on how certain the distribution is for that token. 
Confidence is measured using the probability of the single most likely token, _max. If _max is high, the model is confident — this means we need to be more conservative. If _max is low, the model is uncertain, so we can afford to explore more options. This improves sensitivity to context and uncertainty. On top of that, the technique balances coherence and creativity even at high temperatures. 
By addressing the longstanding diversity-quality tradeoff, the min- sampling technique represents an advancement in generative language modeling. It can enhance applications that require both high-quality and diverse text generation.
## How does min- sampling work?
## Implementing min- sampling
### Integrating it into decoding pipelines
Min- requires minimal changes to standard LLM decoding pipelines. 
Min- sampling has been implemented as a logits processor. A logits processor is a small, modular component in a language model decoding pipeline that adjusts the raw logits (the model’s unnormalized prediction scores for each token) before sampling or selecting the next token. It's like a “filter” for the model’s raw outputs before the selection of the next token is decided.
After applying temperature scaling, the scaled threshold is computed and tokens with probabilities below this threshold are filtered out before sampling. These operations are efficiently implemented using vectorized computations, which adds only a negligible overhead to the decoding process.
### The Code repository 
Min- sampling has been integrated with widely-used open-source frameworks such as Hugging Face Transformers, vLLMs, SGLand and many other repositories. The code implementation is available on [github](https://github.com/menhguin/minp_paper). 
### The advantages of min- sampling 
**Min- sampling has a number of distinct advantages when compared to some of the techniques discussed earlier**. 
  * **It balances creativity and coherence**. The min- technique adjusts dynamically the sampling thresholds to different contexts within the same generated sequence based on the model’s confidence in its outputs. The other techniques allow either overly diverse (incoherent) or conservative (repetitive) token choices in the token sampling pool.
  * **It’s robust at high temperatures**. The min- technique scales the truncation threshold proportional to the model’s confidence, preserving output coherence at higher temperatures. This is valuable for tasks that benefit from higher creativity, like storytelling or content creation.
  * **It’s simple**. The min- technique requires minimal computations, so it can integrate with existing LLM inference pipelines easily without substantial overhead. 


### Real-world applications
The real advantage of Min- technique is where “coherence” under “high temperature” is expected from the model.
  * **Diverse reasoning paths.** It can facilitate problem solving and brainstorming by creating varied output paths via adaptive temperature. By encouraging diverse reasoning paths, it can improve problem solving and brainstorming. Results show that min- sampling at higher temperatures can outperform greedy decoding, achieving a better balance between diversity and accuracy than traditional deterministic methods.
  * **Agent training and exploration**. Recent research in reinforcement learning is using the min- sampling technique to generate high-quality and diverse training data for curious agents. It was implemented with a temperature of 1.5 and a min- parameter of 0.3 for the Llama 3.1-8B Instruct model. This demonstrates min- ’s potential for improving reinforcement learning for agent exploration. 
  * **Red-teaming**. It can generate diverse samples to help identify vulnerabilities.
  * **Advanced reasoning models**. Min- sampling settings are recommended for [DeepSeek-R1](https://www.thoughtworks.com/insights/blog/generative-ai/demystifying-deepseek) implementations. The [document](https://huggingface.co/unsloth/DeepSeek-R1-GGUF) by Unsloth (2025) specifies that a min-p value of 0.05 “helps counteract very rare predictions” particularly beneficial for their quantized 1.58-bit model. This demonstrates how min- effectively balances token selection in both high-temperature creative settings and reasoning-intensive applications.


### Future research
Today, min- stands as one of the most reliable sampling techniques where high-temperature incoherence is a bottleneck. However, there are still many challenges that still need to be addressed:
**Min-z and top-N techniques**
While min- shows considerable promise as an adaptive alternative to fixed top- or top- sampling, it nevertheless has certain limitations. For instance, it relies on the mean logit value that makes it sensitive to skewed or heavy-tailed distributions. This means a small number of extreme logits can distort the threshold and lead to either over-truncation or under-truncation. Also, the thresholding mechanism in min- provides only a rough balance between precision and diversity; it may lack the adaptivity needed for fine-grained control in dynamic settings. Recent extensions such as top-Nσ and min-z highlight promising directions: incorporating distributional spread and median-centered normalization yields more robust and information-efficient truncation, particularly in the presence of heavy-tailed logits. 
**Human evaluation scope**
The min- technique has gained popularity within the open-source community for creative writing tasks, where its value emerges most strongly in interactive, exploratory settings rather than static one-shot evaluations. This distinction suggests evaluation on dynamic platforms such as Chatbot - where users iteratively interact with models — may provide a more faithful measure of its practical utility. 
**Combining uncertainty and CoT decoding methods**
Recent work on combining uncertainty with chain-of-thought (CoT) decoding highlights a complementary perspective: high-certainty token choices are most effective for producing accurate final answers, whereas more diverse, lower-probability tokens enhance the intermediate reasoning process. This distinction suggests a natural extension for future research — integrating min- (and its variants such as min-z) with CoT-inspired decoding strategies. 
**Applicability to other domains**
Extending min- to other generative tasks, such as code generation or multimodal models, could reveal broader applicability and benefits across different domains.
**High temperature regimes**
High-temperature regimes remain comparatively underexplored, yet min- sampling offers a pathway to unlock new opportunities for exploration, experimentation and application. Recent reinforcement learning research has begun employing min- for trajectory data generation, highlighting its effectiveness in producing training data that’s both diverse and high-quality.
**AI safety and interpretability**. Follow-up research is required applying min- technique to mechanistic interpretability for AI safety and alignment. Specifically, its use in uncertainty-aware generation, neuron activation filtering and structured latent selection to enhance model robustness. 
### Disclaimer
Min- sampling technique aims to improve the diversity and coherence of text generated by large language models. We acknowledge the following “ethical” considerations:
• **Potential misuse**. Min- could potentially enhance the fluency of misleading or harmful content. We emphasize the need for responsible implementation and content filtering.
• **Safety risks**. Normally, increasing temperature makes text generation more random and diverse. A concern is that too much randomness could let the model “slip past” its safety fine-tuning, i.e., generate unsafe or restricted content it was trained to avoid. There’s currently no evidence that using Min- technique creates this problem.
• **Transparency**. To ensure reproducibility and enable further research, we have open-sourced our implementation and provided extensive details on the experimental setup and results. Refer the Github link in the Code repository section above. 
We believe the benefits of entropy and uncertainty-based methods outweigh these risks. We strongly encourage safety and alignment research leveraging uncertainty and entropy, as this can clearly benefit robustness, truthfulness, and reduced hallucinations 
**Learn more:[Turning up the heat: Min-p sampling for creative and coherent LLM outputs](https://arxiv.org/abs/2407.01082)**
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
## Related content
  * [ Generative AI Evaluating LLMs using semantic entropy  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/Evaluating-LLM-using-semantic-entropy)
  * [ Generative AI LLM benchmarks, evals and tests: A mental model  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/LLM-benchmarks,-evals,-and-tests)
  * [ Generative AI How to improve AI outputs using advanced prompt techniques  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/improve-ai-outputs-advanced-prompt-techniques)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Elevate your expertise
[ Explore our Engineering page ](https://www.thoughtworks.com/en-gb/engineering)
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
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://www.thoughtworks.com/about-us/privacy-policy)
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