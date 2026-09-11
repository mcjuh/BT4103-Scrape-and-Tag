<!-- Source: https://www.deloitte.com/uk/en/Industries/financial-services/blogs/llm-strategy-is-it-better-to-train-or-use-out-of-the-box.html | Title: LLM strategy – is it better to train or use ‘out of the box’ | Deloitte UK | Seed: https://www.deloitte.com/us/en/services/consulting/services/mergers-acquisitions.html (Deloitte) -->

Link opens in a new tab
opens in new window
[Skip to main content](javascript:void\(0\))
Welcome to Deloitte 
If we have selected the wrong experience for you, please change it above. 
Perspective: LLM strategy – is it better to train or use ‘out of the box’
[ Print ](javascript:window.print\(\); "Print")
[ Share  ](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/llm-strategy-is-it-better-to-train-or-use-out-of-the-box.html# "Share")
Perspective
19 Feb 2025
10 minute read
# LLM strategy – is it better to train or use ‘out of the box’
## Embracing the Generative AI Revolution in Financial Services Recommendations for Future Success (Part 4 of 5)
Authors: 
[ Print ](javascript:window.print\(\); "Print")
[ Share  ](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/llm-strategy-is-it-better-to-train-or-use-out-of-the-box.html# "Share")
Over the past 18-months, large language models (LLMs) have evolved rapidly, offering businesses powerful tools for tasks like content generation, natural language understanding and automation. However, as organisations continue to explore the use of LLMs, they will need to navigate critical decisions about whether to train their own or instead use pre-trained models ‘out of the box’. This article delves into the strategic choices that organisations must make when implementing LLMs, in a process balancing flexibility, cost, performance and governance.
#### Navigating the evolving LLM landscape
As LLMs evolve, so too do their capabilities, as well as their performance in different use case scenarios. This rapid development requires businesses to adopt a flexible, iterative approach to LLM deployment, one that emphasises agility and continual improvement. The key here is to embrace flexibility, adopting a test, deploy, iterate approach:
  * **Agile LLM deployment:** organisations need to create a framework for continuous testing, deployment and monitoring. This will allow them to adapt to the latest advancements in LLM technology as they arrive.
  * **Sandbox environment:** building a ‘sandbox’ will also allow institutions to test their new LLMs thoroughly before production as well as fine-tuning established ones without disrupting their existing implementations, supporting a rapid process of prototyping and innovation.
  * **A/B Testing 1 :** the use of A/B testing will also help organisations to compare the performance of different LLMs for specific tasks. This can help in selecting the most effective models for specific use cases.


In these ways, by implementing a dynamic framework for LLM testing and deployment, institutions will be better able to stay at the forefront of AI advancement, allowing room for agile iteration and refinement where needed.
#### Better to build, or better to buy?
As organisations adopt LLMs, they will each face a crucial decision around whether to build and train their own custom models or use pre-trained models from providers. The decision itself hinges on the specific needs of the organisation, their available resources and their appetite for risk, since both approaches have their ‘pros and cons’ (see Fig 1 below).
Figure 1: Prons & Cons of Different Model Choices  
Figure 1: Prons & Cons of Different Model Choices  Figure 1: Prons & Cons of Different Model Choices   
|  Training Custom Models  |  Using Pre-Trained Models  |  
| --- | --- |  
|  Offers highly specialised, domain-specific performance tailored to the organisation's unique requirements.  |  Pre-trained models from a range of providers can be fine-tuned with minimal resources to suit specific tasks, offering instituions a cost effective and scalable solution.   |  
|  Training a model from scratch requires significant investment in data, computational resources and expertise.  |  May lack the depth of customisation that specialised tasks demand.  |  
**Source:** _Deloitte Experience_
Assessing an organisation’s specific requirements, budget and domain expertise can help them decide whether to invest in training their own custom models or leverage pre-trained LLMs.
#### Fine-tuning and the upgrade path – maintaining performance and compliance
Once an organisation has fine-tuned an LLM with proprietary data, maintaining that model’s performance over time can present fresh challenges, especially as new versions of base models are released. Implementing a clear upgrade strategy for fine-tuned models can ensure they stay up-to-date and continue to deliver value to the organisation. As part of developing a sustainable Gen-AI upgrade path, consider the following:
  * **Model evolution:** develop a process for regularly evaluating fine-tuned models against newer versions of the base LLM.
  * **Retraining and updates:** implementing a strategy for retraining fine-tuned models will also help organisations incorporate improvements from updated base models without losing the customisation afforded by their fine-tuning efforts.
  * **Large vs. small models:** There are certain use-cases where a smaller model (e.g., one of 8 billion parameters vs. a larger model of 120 billion or more) can be more efficient, being both easier to tune for specific tasks and where frequent retraining is needed. 


#### Navigating the regulatory landscape – transparency and accountability
As LLM adoption increases, so too will regulatory scrutiny. Ensuring transparency, accountability and explainability in how these models operate is essential to maintaining compliance with evolving regulation. In developing a compliance strategy for their LLMs, organisations should consider the following:
  * **Logging and monitoring:** tracking LLM usage, including inputs, outputs and data handling, will help businesses to create an auditable trail of data around how the LLM has been used.
  * **Explainability mechanisms:** likewise, firms should develop systems that explain how and why inferences are calculated, providing transparency to users and regulators around the reasons for specific outputs.


By implementing robust logging and monitoring systems for LLM usage, and by staying informed about regulatory developments, firms will be best equipped to ensure their LLMs maintain continuous compliance.
#### A multifaceted approach to LLM evaluation – moving beyond accuracy
Evaluating LLMs requires more than accuracy. Given the complexity and variability of language tasks, organisations need to adopt comprehensive evaluation frameworks that also address robustness, fairness and reliability. This type of extended framework should include:
  * **Diverse metrics:** assess LLMs based on a variety of metrics. Key measures will include dialogue coherence, response relevance and user satisfaction for chatbots, while BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Orientated Understudy for Gisting Evaluation) scores will be better suited to machine translation and summarisation tasks.
  * **Adversarial testing:** conduct adversarial testing to identify weaknesses or biases in LLMs, ensuring they perform reliably even under challenging conditions. This should include an evaluation framework that goes beyond accuracy to include diverse testing techniques and metrics tailored to your specific use cases.


Adopting a multi-faceted approach to LLM evaluation, using both automated and human-centric methods, can help ensure models are robust, fair and aligned with the needs of the business.
#### Other critical challenges
While LLMs are powerful, they also have inherent limitations that can impact their reliability and effectiveness. Recognising and addressing these challenges is key to responsible LLM deployment. In particular, organisations need to be ready to tackle the following issues:
  * **Prompt Brittleness:** LLMs can be highly sensitive to changes in input prompts, leading to inconsistent or unpredictable outputs. However, prompt engineering can be used to carefully design input prompts to ensure they produce the desired responses more often.
  * **Corpus Confinement:** being trained on static datasets, the ‘knowledge’ of LLMs can also become outdated over time. Regularly updating training datasets or leveraging retrieval-augmented generation to access external knowledge sources can help firms offset this challenge.
  * **Bias Amplification:** LLMs can also reflect and amplify biases present in their training data, potentially leading to unfair outcomes. However, by implementing bias detection and mitigation strategies during the training and inference phases, and by conducting regular audits, this problem too can be effectively managed.


Similarly, even the most advanced LLMs have other limitations, such as context length constraints, high resource requirements for fine-tuning and challenges around interpretability. Understanding these limitations is essential for setting realistic expectations and ensuring responsible AI usage. For example:
  * **Context Length:** currently, LLMs can only process a limited amount of context at one time, which can sometimes result in an incomplete understanding of longer documents. However, using attention mechanisms, or chunking up longer documents, can both help to preserve context and improve comprehension.
  * **Fine-Tuning Bottlenecks:** fine-tuning LLMs can also be resource-intensive, requiring large amounts of high-quality data, computational power and energy. In this scenario, transfer learning techniques and cloud-based platforms both offer opportunities to reduce the burden of in-house fine-tuning.
  * **Tokenisation:** LLMs process text in chunks called ‘tokens’, and suboptimal tokenisation can lead to information loss, if the tokenisation is too course, or even bias amplification. For example, a tokenisation scheme that splits compound words or phrases might lead to an LLM misinterpreting their meaning or failing to capture important cultural nuances. It is therefore essential to evaluate your tokenisation methods carefully, opting for sub-word tokenisation when appropriate, which can better handle complex linguistic structures.
  * **Interpretability:** as noted earlier in this series, LLMs often function as ‘black boxes’, light on explainability. This can make it difficult for users and validators to understand how they arrive at their outputs. Integrating explainability techniques like attention visualisation will help to inject valuable insights into LLM decision-making processes, turning the ‘black box’ into a ‘glass box’.


Actively addressing the limitations of LLMs through prompt engineering, regular data updates, and bias mitigation can all help to support the reliability, fairness and currency of their outputs. By acknowledging and proactively addressing the limitations of LLMs, firms that implement regular audits and optimised processes will be best placed to maintain model quality and compliance.
In conclusion, choosing whether to train custom LLMs or use pre-trained models instead requires careful consideration of a number of context-specific factors. These include cost, performance, regulatory compliance and domain-specific needs. However, by adopting a flexible, iterative approach to LLM strategy, and by embracing the inherent challenges and limitations of these models, organisations can unlock the full potential of LLMs while mitigating the risks.
In our [next and final article](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/embracing-the-gen-ai-revolution-summary-recommendations-for-financial-institutions.html) in this series we pull together the insights and recommendations from this and our other pieces to provide a simplified summary of the challenges and mitigations available to financial institutions as the proceed along the Gen-AI path.
### Key contacts
####  [Peeyush Aggarwal](https://www.deloitte.com/uk/en/about/people/profiles.peaggarwal+5f32a4b8.html)
Global Data and AI Lead Partner
peaggarwal@deloitte.co.uk
[ +44 (0)20 7303 2334](tel:+44%20\(0\)20%207303%202334)
####  [Sulabh Soral](https://www.deloitte.com/uk/en/about/people/profiles.ssoral+9d80be73.html)
Chief AI Officer, Consulting
ssoral@deloitte.co.uk
[ +44 (0)20 7007 2123](tel:+44%20\(0\)20%207007%202123)
### Our thinking
### [ From adoption to value creation – how to unlock the full potential of Gen-AI  Generative AI (Gen-AI) is already demonstrating its ability to drive significant individual productivity gains.  Perspective 10 minute read  ](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/from-adoption-to-value-creation-how-to-unlock-the-full-potential-of-gen-ai.html)
### [ Safety first – the critical role of risk management and governance in Gen-AI adoption  While the transformative potential of Generative AI (Gen-AI) should not be underestimated, the financial services sector faces unique challenges in ensuring its safe and responsible adoption.  Perspective 10 minute read  ](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/safety-first-the-critical-role-of-risk-management-and-governance-in-gen-ai-adoption.html)
### [ Scaling for success – enterprise adoption strategies for Gen-AI  Generative AI (Gen-AI) has the potential to revolutionising industries, including financial services, but a key step towards realising its full potential is the ability of institutions to scale the right infrastructure to ensure Gen-AI can be adopted across the enterprise where needed.  Perspective 10 minute read  ](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/scaling-for-success-enterprise-adoption-strategies-for-gen-ai.html)
### [ Embracing the Gen-AI revolution – summary recommendations for financial institutions  This series of articles focuses on how firms in the highly regulated world of financial services can best embrace the Generative AI (Gen-AI) revolution.  Perspective 10 minute read  ](https://www.deloitte.com/uk/en/Industries/financial-services/blogs/embracing-the-gen-ai-revolution-summary-recommendations-for-financial-institutions.html)
## Here’s how we use cookies
We use cookies to better understand your preferences so that we can bring you the best, most personalised experience possible. By using this website, you agree to the use of cookies as outlined in [Deloitte’s online cookie notice.](https://www.deloitte.com/uk/en/legal/Cookies.html?hidebanner=true)
Accept optional cookies  Decline optional cookies
Tailor your cookie preferences