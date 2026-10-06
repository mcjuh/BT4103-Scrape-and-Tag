<!-- Source: https://research.thoughtworks.com/library/evaluating-llms-using-semantic-entropy | Title: Evaluating LLMs using semantic entropy | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Evaluating LLMs using semantic entropy
By 
Published: March 07, 2025 
### Introduction
Generative AI (GenAI) applications are advancing rapidly across various domains of human life. At the core of GenAI systems are large language models (LLMs), which serve as conversational AI, chatbots, language models, and other language-driven applications. LLMs are deep neural networks (DNNs) designed to process input and generate human-like responses. These models consist of multiple hidden layers, each containing thousands of neurons, positioned between the input and output layers. They are trained on massive datasets with billions of parameters. As stochastic models, LLMs excel in contextual understanding, coherent and fluent text generation, intelligent question answering, and language translation. Their development has revolutionized natural language processing (NLP) and its wide-ranging applications.
New models are being developed almost daily by organizations, research institutes, and corporations. Leaderboards are inundated with comparative analyses of these models' performance across diverse benchmarks. According to a recent [survey](https://web-assets-pdf.bcg.com/prod/it-spending-pulse-as-genai-investment-grows-other-it-projects-get-squeezed.pdf) by Boston Consulting Group, corporations investing in Generative AI anticipate a threefold return on investment (ROI) by 2027. Additionally, a [report](https://cio.economictimes.indiatimes.com/news/etcio-research/global-spending-on-ai-to-reach-632-billion-in-2028-report/112642446) by the International Data Corporation (IDC) projects that global spending on AI will reach approximately $632 billion by 2028, with the integration of Generative AI products driving a compound annual growth rate (CAGR) of 29%.
The reality paints a different picture. The performance of Generative AI technologies often falls short of their promises, with ROI failing to meet the hype. Many GenAI applications and products struggle to transition from proof-of-concept to full-scale production. Daron Acemoglu, a professor at MIT, [predicts](https://www.goldmansachs.com/images/migrated/insights/pages/gs-research/gen-ai--too-much-spend,-too-little-benefit-/TOM_AI%202.0_ForRedaction.pdf) that AI may impact less than 5% of all tasks and contribute only a 0.9% increase to the U.S. GDP over the next decade. Such contrasting perspectives create uncertainty around the adoption of GenAI technologies in everyday business operations.
### What explains these paradoxical viewpoints?
The primary reason is that GenAI applications often underperform, produce unreliable results or behave unpredictably. Additionally, the lack of quantitative evaluation methods fails to build trust among stakeholders.
**Trust remains a major concern for businesses when adopting Gen AI applications for critical use cases.**
### What weakens our trust in LLMs? 
Large language models (LLMs) demonstrate impressive capabilities in QA, reasoning, language translation, and other services. However, they have inherent weaknesses: they can generate false outputs that sound plausible but are entirely fabricated. This phenomenon, known as "confabulation," occurs when models confidently produce incorrect information. LLMs are also sensitive to irrelevant factors, like random seed values, making them unreliable. This undermines trust, particularly in critical domains such as medicine, finance, law and space sciences.
**Confabulations are false, unreliable and fabricated claims made confidently by LLMs in response to a prompt.**
### Syntactically different; semantically identical
#### Example: 1
LLMs can generate syntactically varied outputs for the same input.
**Input 1: Where are the Ajanta caves?**
**Output 1** : The Ajanta Caves are located in the state of Maharashtra, India. They are situated near the town of Ajanta, about 104 kilometers (65 miles) from the city of Aurangabad. These caves are renowned for their ancient rock-cut Buddhist monasteries and stunning wall paintings, which date back to the 2nd century BCE to about the 6th century CE. The Ajanta Caves are a UNESCO World Heritage Site.
**Input 2: Where are the Ajanta caves?**
**Output 2** : The Ajanta Caves are located in the state of Maharashtra, India, near the town of Ajanta, approximately 104 kilometers (65 miles) from Aurangabad. The caves are a UNESCO World Heritage Site and are famous for their ancient Buddhist rock-cut monasteries and exquisite murals, dating from the 2nd century BCE to about the 6th century CE.
**Input 3: Where are the Ajanta caves?**
**Output 3** : The Ajanta Caves are located in the state of Maharashtra, India, near the town of Ajanta, about 104 kilometers (65 miles) from the city of Aurangabad. These ancient rock-cut Buddhist monasteries and temples, dating from the 2nd century BCE to the 6th century CE, are renowned for their beautiful frescoes and sculptures and are a UNESCO World Heritage Site.
As shown, each response may differ lexically but remain semantically identical. Can this concept be used to measure model confabulations?
### Semantic entropy: A robust method to measure model uncertainty
As noted, trust in today’s transformer-based models can be enhanced by measuring the uncertainty of their outputs. One approach is an information-based method that uses entropy as a key measure of uncertainty. This technique assesses a model's question-answering (QA) ability by quantifying confabulations.
**Entropy reflects the "uncertainty" of a model. The entropy-based evaluation method is unsupervised and can be applied to any off-the-shelf model.**
Claude Shannon established the foundations of information theory in the 1940s, centered on the concept of entropy. Entropy quantifies the uncertainty in the output of a random process and plays a crucial role in modern machine learning models, including deep neural networks (DNNs).
Entropy measures the spread of the probability distribution in a model’s prediction for a given input. Higher entropy indicates greater uncertainty in the model’s output. Shannon's theorem provides the core equation for entropy, which states that: 
Shannon's Theorem H = conditional entropy
x = input sequence
p = model's prediction probability
The basic method of entropy estimation worked well for short inputs like words or sentences. However, it became clear that measuring uncertainty in longer sequences was more complex. To address this, Kadvath et al. (2022) introduced the concept of predictive entropy (PE). The following equation defines it: 
x = input sequence
s = generated sequence
N = tokens (where s is completion based on x)
= probability of generating i-th token
= preceding tokens
Prompt x is denoted as 
Applying PE to LLM evaluations still delivered inaccurate estimates as they were based solely on tokens. Researchers realized that measuring entropy in free-form generations is challenging because different syntaxes can convey the same meaning, making PE estimates unreliable. The solution to this issue was the invention of another method called semantic entropy. 
Semantic entropy (SE) was proposed by Farquhar et. al. which discussed a sample-based evaluation method. Here a single query (a line or a bunch of paragraphs) is fed into the model multiple times and instead of a sequence of words the difference in the meaning of the model’s response was captured. SE clustered sentences into equivalence classes based on their semantic similarity and finally computed the entropy over those classes. SE uses the following: 
c=equivalence class of semantically similar sentences
A higher degree of entropy indicates greater uncertainty, and vice versa. The meaning is more important than the token usage that generates the output. Semantic entropy (SE) enables free-form generation, overcoming the limitations of naive methods better suited to closed-vocabulary or multiple-choice tasks. The method acts as a semantic consistency check for random seed variations. However, it does not differentiate between aleatoric uncertainty (due to data distribution) and epistemic uncertainty (caused by limited information).
Let's examine another example to clearly differentiate between semantic entropy, naive entropy, and confabulation.  
Semantic entropy, naive entropy and confabulation  
| Sr.No.  | Question  | Reference answer  | Model answer  | Generations for entropy  | Semantic entropy  | Naive Entropy  |  
| --- | --- | --- | --- | --- | --- | --- |  
| 1  |  What is the capital of  Andhra Pradesh?  | Amaravathi or Visakapatnam  | Amaravathi is the capital of Andhra Pradesh.  | 
  1. Amaravati is the capital of Andhra Pradesh.
  2. The capital of Andhra Pradesh is Amaravati.
  3. Visakhapatnam and Amaravati are administrative capitals.

 | Not a confabulation  | Confabulation  |  
| 2  | What is the national animal of India?  | Bengal Tiger  |  The Bengal tiger is the national animal of India.  | 
  1. Bengal tiger is the national animal of India.
  2. India’s national animal is the Bengal tiger.
  3. The Royal Bengal tiger represents India.

 | Not a confabulation  | Not a confabulation  |  
| 3  | When was India’s first moon mission?  | October 22, 2008,  |  India launched its first moon mission in October, 2008.  | 
  1. India’s Chandrayaan-1 was launched on October 22, 2008. 
  2. The first Indian moon mission occurred in October, 2008. 
  3. India’s lunar mission began in late 2008.

 | Confabulation  | Not a confabulation  |  
Semantic entropy, naive entropy and confabulation  
| Sr.No. |  
| --- |  
| Question |  
| --- |  
|  What is the capital of  Andhra Pradesh?  |  
| What is the national animal of India? |  
| When was India’s first moon mission? |  
| Reference answer |  
| --- |  
| Amaravathi or Visakapatnam |  
| Bengal Tiger |  
| October 22, 2008, |  
| Model answer |  
| --- |  
| Amaravathi is the capital of Andhra Pradesh. |  
|  The Bengal tiger is the national animal of India.  |  
|  India launched its first moon mission in October, 2008.  |  
| Generations for entropy |  
| --- |  
| 
  1. Amaravati is the capital of Andhra Pradesh.
  2. The capital of Andhra Pradesh is Amaravati.
  3. Visakhapatnam and Amaravati are administrative capitals.

 |  
| 
  1. Bengal tiger is the national animal of India.
  2. India’s national animal is the Bengal tiger.
  3. The Royal Bengal tiger represents India.

 |  
| 
  1. India’s Chandrayaan-1 was launched on October 22, 2008. 
  2. The first Indian moon mission occurred in October, 2008. 
  3. India’s lunar mission began in late 2008.

 |  
| Semantic entropy |  
| --- |  
| Not a confabulation |  
| Not a confabulation |  
| Confabulation |  
| Naive Entropy |  
| --- |  
| Confabulation |  
| Not a confabulation |  
| Not a confabulation |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Let's analyze the third question: "When was India's first moon mission?" What caused the model to confabulate in this case?
### Semantic entropy
After querying three times with the same question,the generations pointed to a similar event, with different levels of precision. 
  1. Generation 1: Specific date → Closest to the reference answer.
  2. Generation 2: Month → Generalized meaning.
  3. Generation 3: Approximate timeframe → Further generalization.


In semantic clustering, these generations may not belong to the same cluster: Generation 1 is unlikely to cluster with Generations 2 and 3. This leads to multiple semantic clusters, indicating uncertainty about the output's meaning. Since the generations are spread across several clusters, the semantic entropy is high, reflecting the model's uncertainty about the correct answer's precise meaning.
### Naive entropy
Naive Entropy measures lexical variation: 
  1. The words used were not drastically different (e.g., all refer to Chandrayaan-1 and the year 2008).
  2. Therefore, naive entropy was low, as the outputs appear similar lexically, even though their meanings diverge. This broke the trust in the model. 


### Calculating semantic entropy 
The semantic entropy calculation method is unsupervised and works intuitively by sampling multiple potential answers to each question, then grouping them into clusters of semantic equivalence. Similarity is determined by whether the answers within a cluster mutually entail each other. Specifically, if sentence x entails sentence y and vice versa, they are classified in the same cluster. This method effectively identifies confabulations without requiring prior domain knowledge.
Calculating predictive entropy based on the probabilities of the generated token sequence (naive entropy) conflates the model's uncertainty about the meaning with its uncertainty about the specific words used. When detecting confabulations, the uncertainty about meaning is more important than the uncertainty about the word sequence.
The three steps to calculate semantic entropy to detect and measure confabulations of the LLM are as follows:
  1. **Generate a set of answers** : Given some context, x as an input, sample M sequences. They should be samples according to the distribution p(s|x).


a. **Input context** : Provide a context x as input to the LLM
b. **Sampling multiple sequences**. Generate MM sequences  and record their token probabilities 
c. **Single model use**. Use a single LLM for all generations, changing only the random seed during sampling.
d. **Sampling techniques**. Use temperature 1.0 with nucleus sampling (P=0.9) and top-K sampling (K=50)
e. **Best generation**. Generate one sequence at a low temperature (0.1) to approximate the model's "best" response for the context. Using a low temperature increases the likelihood of selecting the most probable tokens, which helps in assessing the model's accuracy.
**2. Cluster by semantic equivalence** : Estimate semantic entropy by clustering model-generated outputs into groups that express the same meaning. This grouping is based on the concept of **semantic equivalence**.
**Token space** : Let the space of all tokens (words, symbols, etc.) in a language be T.
**Sequence space** : The set of all possible token sequences of length N is Tⁿ.
**Equivalence relation properties** : E (ᐧ,ᐧ) must be:
  * Reflexive: E(s,s) (a sentence is equivalent to itself).
  * Symmetric: If E(s,s'), then E(s',s).
  * Transitive: If E(s,s') and E(s',s''), then E(s,s'').


Using this relation, we can group sentences into **semantic equivalent classes**.
For each class C, all sentences sC express the same meaning, E(s,s') holds for any s,s'C.
To build these equivalence classes, we:
  1. Compare new sentences against existing clusters.
  2. If a sentence shares meaning with any sentence in a cluster, we add it to that cluster.
  3. Otherwise, the sentence forms its own new cluster.


A sentence ss is semantically equivalent to another sentence s′ if:
  * s entails s′, and
  * s′ entails s.


For a new sentence, check if it bidirectionally entails any sentence in an existing cluster.
  * If yes, add it to that cluster.
  * If not, create a new cluster for the sentence.
  * By checking only one sentence per cluster (e.g., the first sentence), transitivity ensures correct clustering.


**Estimate entropy** : Once we have grouped generated sequences into semantic equivalence classes (clusters of sentences with the same meaning), we can estimate the likelihood of a sequence belonging to a particular class. This is done by summing the probabilities of all token sequences within that class.
  * **Cluster sequences** : Group generated sequences into clusters based on semantic equivalence.
  * **Estimate probabilities** :
    * For full SE, compute P(Ci|x)P(Ci​|x) using token probabilities.
    * For discrete SE, use the proportion of sequences in each cluster.
    * Compute SE
    * Use the entropy formula to calculate the uncertainty in the meaning distribution.
    * **Monte Carlo sampling** : Increase the number of samples MM for more accurate estimates.


### **Semantic entropy process for a QA application**
### Results 
We evaluated the model using six questions, asking each question 10 times and recording the model's responses. The maximum number of clusters created was three. However, the number of clusters depends on semantic entailment: if the LLM deems two sentences as entailed, they are placed in the same cluster. We set the confabulation warning flag at 7, considering any SE above 7 as a confabulation for the given input. The results are shown in the table below.
### Questions:
  1. If all swans are white, but this swan is black, is it still a swan?
  2. If today is Monday, what is tomorrow in another time zone?
  3. Is the light a ray or a particle?
  4. Is gravity a wave or a curvature in space-time?
  5. Is there a life after death?
  6. What is the capital of India?

  
Table  
| Q  | Naive entropy (NE)  | Semantic Entropy  | Semantic Entropy  | Semantic Entropy  | Total Semantic entropy (SE)  | Confabulation warning (SE >7)  |  
| --- | --- | --- | --- | --- | --- | --- |  
| Cluster 1  | Cluster 2  | Cluster 3  |  
| 1  | 2.302  |  0.179  | 0.230  | 0.230  | 0.639  | No  |  
| 2  | 2.302  | 0.250  |  0.361  | -  |  0.611  | No  |  
| 3  | 2.302  | 0.0  | -  | -  | 0.0  | No  |  
| 4  | 2.302  | 0.0  | -  | -  | 0.0  | No  |  
| 5  | 2.302  | 0.250  |  0.361  | -  |  0.611  | No  |  
| 6  | 0.0  | 0.0  | -  | -  | 0.0  | No  |  
Table  
| Naive entropy (NE) |  
| --- |  
| 2.302 |  
| 2.302 |  
| 2.302 |  
| 2.302 |  
| 2.302 |  
| 0.0 |  
| Semantic Entropy |  
| --- |  
| Cluster 1 |  
|  0.179  |  
| 0.250 |  
| 0.0 |  
| 0.0 |  
| 0.250 |  
| 0.0 |  
| Semantic Entropy |  
| --- |  
| Cluster 2 |  
| 0.230 |  
|  0.361  |  
|  0.361  |  
| Semantic Entropy |  
| --- |  
| Cluster 3 |  
| 0.230 |  
| Total Semantic entropy (SE) |  
| --- |  
| 0.639 |  
|  0.611  |  
| 0.0 |  
| 0.0 |  
|  0.611  |  
| 0.0 |  
| Confabulation warning (SE >7) |  
| --- |  
| No |  
| No |  
| No |  
| No |  
| No |  
| No |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
### Links 
Here is a[ link](https://gist.github.com/karrtikiyer/1b56b498cb734ac08e6e7db3570c3692) for all the details required to implement the semantic entropy calculator. 
### Conclusion
Confabulation, a form of hallucination in LLM QA applications, is difficult to address with traditional evaluation methods. Results show that naive entropy often fails to identify confabulations, while semantic entropy effectively filters out false claims. This approach focuses on evaluating meaning rather than word sequences, making it applicable across datasets and tasks without prior knowledge. It generalizes well to unseen tasks, helping users identify prompts likely to cause confabulations and encouraging caution when needed. Based on Shannon's information theory and statistics, semantic entropy is a reliable method for detecting confabulations in LLMs, fostering trust among stakeholders in using LLM-based applications for critical customer projects.
### Deep dive
  1. [A Survey of Uncertainty Estimation in LLMs: Theory Meets Practice](https://arxiv.org/abs/2410.15326)
  2. [Detecting hallucinations in large language models using semantic entropy](https://www.nature.com/articles/s41586-024-07421-0)