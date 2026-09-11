<!-- Source: https://research.thoughtworks.com/library/concept-consistency-score | Title: Concept consistency score | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Concept consistency score
By 
Published: February 27, 2026 
#### A novel interpretability metric measuring accuracy and fairness among CLIP neural networks 
CLIP (contrastive language image pre-training) is a large-scale vision language model (VL), a foundation model that is used for vision classification tasks. The model is also effective for video retrieval, image generation and image segmentation. This is because the CLIP architecture connects text and images while discarding the common approach of aiding visual learning by applying rigid manual labels. 
CLIP models are trained on a diversity of images that are abundantly available on the internet with a variety of natural language supervision. The models are popularly used as an ensemble model-architecture, which expands both their scope and functionality. Ensembling means that instead of asking the AI one single question like "is this a dog?", we can ask a few variations like, "Is this a photo of a big dog?" or "Is this a photo of a small dog?" or "Is this a blurry photo of a dog?"
By combining the answers from all these different prompts, the accuracy of the model can be improved. Similar to the “zero shot” capabilities of GPT family, the CLIP model can be instructed in a natural language to perform a variety of classification benchmarks without directly optimizing for the benchmark’s performance. The model can be applied to any visual classification benchmark by simply providing the names in text format of the visual categories.
The challenge is, in spite of its widespread adoption, the inner mechanisms of CLIP remain opaque. It is surprising. Critically, we also have limited understanding of the model's inherent limitations and the social biases it may have embedded during pre-training. This makes the model’s inferences difficult to interpret. To address this interpretability gap, we have introduced a novel metric: the concept consistency score (CCS).
### Why CLIP?
Let us understand the basics first. Deep learning neural networks are fundamental to computer vision models. These networks, however, pose several challenges around training methodologies and database architectures. For instance: 
  * Datasets used to train the networks are labor intensive and expensive to create. 
  * Datasets teach only a narrow set of visual concepts, we call them properties, so models are limited to a single task.
  * Neural networks trained on datasets perform well on benchmarks but fail most of the times on stress tests and in real life applications. 


CLIP as a type of foundation model is a response to the above mentioned challenges and provides opportunities to make modern DNNs more effective for computer vision applications.
Development of CLIP took nearly a decade and was largely inspired by the work of Ang Li and his co-authors who demonstrated that their approach could generalize effectively the existing vision-classification tasks, including the benchmark dataset ImageNet.
This key concept was then built upon and enhanced by several concurrent research streams and novel architectures. For example:
  * Modern transformer architectures provided the powerful, scalable foundation needed to process massive multimodal datasets.
  * VirTex explored autoregressive language modeling in a vision-language context.
  * ICMLM helped researchers investigate using masked language modeling for image-text representation learning.
  * ConVIRT validated and refined the contrastive objective (the core learning mechanism) used in CLIP.


### What is the concept consistency score (CCS)?
The concept consistency score (CCS) is a metric as well as a framework that directly measures how consistently the individual attention heads within the CLIP model align with or focus on specific concepts or properties. Later, our soft-pruning experiments reveal the model shortcomings that high CCS heads preserve the model’s performance, but also amplifies its social bias. The measurement demonstrates a dual-edged sword.
### CCS: The powerful interpretability metric balancing performance and social bias
This duality underscores the power and importance of the CCS framework as an interpretability metric. We need to understand how the visual concepts encoded at the attention head level and how these concepts underpin both the model’s strengths and its social failures.
### CCS process
The framework helps us analyze which visual concepts are learnt by individual attention heads and how consistently these concepts are processed throughout the model’s architecture. The models also throw light on the decision making process of attention heads. Here is the process describing the CCS in brief:
  1. Use text descriptions and Identify interpretable structures within the individual heads of the last 4 layers of the model. 
  2. Employ TEXTSPAN algorithm to identify the most appropriate text descriptions for each head. 
  3. Assign labels to each head representing the common property shared by description. (Using in-context learning with ChatGPT.)
  4. Use GPT-4o, Gemini and Claude as automatic judges, compute CCS for each head.
  5. Based on a defined threshold, classify the CCS score into high, moderate and low categories.

  
High CCS score  
|  High CCS score - Performance benefits  |  
| --- |  
|  **Concept capture** : Essential for the model to reliably grasp critical concepts (properties). |  
|  **Out-of-domain detection** : Plays a key role in identifying data points that fall outside the model's expected distribution. |  
|  **Concept-specific reasoning** : Enables better, more targeted model explanations and debugging. |  
High CCS score  
|  High CCS score - Performance benefits  |  
| --- |  
|  **Concept capture** : Essential for the model to reliably grasp critical concepts (properties). |  
|  **Out-of-domain detection** : Plays a key role in identifying data points that fall outside the model's expected distribution. |  
|  **Concept-specific reasoning** : Enables better, more targeted model explanations and debugging. |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))  
High CCS score  
|  High CCS score - Amplification of social bias  |  
| --- |  
|  **Social bias** : Spurious correlations amplify social bias |  
High CCS score  
|  High CCS score - Amplification of social bias  |  
| --- |  
|  **Social bias** : Spurious correlations amplify social bias |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
### The concept of CCS
To better understand the concepts (properties) learned (in pre-training) by the transformer layers and attention heads of the CLIP-style models, we introduce CCS — a metric that evaluates the alignment between textual representations from transformer heads and predefined concept labels. Beyond simple alignment, it also tracks consistency across different heads. This approach makes model interpretability actionable, offering a clear path for pruning unnecessary components and debugging errors. 
Let’s discuss each step in detail.
**Step 1: Extract text representations**
Extract five textual outputs {T₁, T₂, T₃, T₄ and T₅} from each layer and attention head of the CLIP model. These outputs are called TEXTSPANS. They are textual approximations of the concepts (properties) encoded by each head. 
**Step 2: Assign concept labels**
Analyze the above set of five TEXTSPAN outputs using in-context learning with ChatGPT. Identify the dominant concept from each head and label it as Cₕ. This process ensures the label is data-driven describing the most salient feature learnt by the head. 
**Step 3: Assess the consistency of each head with regards to the assigned concept labels**
Employ three foundation models as external evaluators (judges). (Here we used GPT-4o, Gemini 1.5 Pro and Claude Sonnet). For each Tᵢ associated with the head h, GPT-4o determines whether it aligns with the assigned concept Cₕ.
alignswith
Where, 
-||- an indicator function that returns 1 if Tᵢ is consistent with Cₕ and 0 otherwise.
We also define CCS@K value as a fraction of the number of attention heads that have a CCS = K. A high value shows that a greater proportion of heads exhibit strong alignment with a single semantic property.
Where,
  * H - total number of attention heads in the model 
  * CCS(h) - CCS of head h
  * -||- indicator function that returns 1 if CCS(h) = K and 0 otherwise.


Once we get the CCS scores, then we categorize every attention head into three levels - high, moderate and low:
  1. **High CCS** : When all of its associated text descriptions align with the labeled concept, indicating that the head is highly specialized and likely encodes features relevant to that concept. 
  2. **Moderate CCS** : When the heads exhibit partial alignment, with three out of five text descriptions matching the concept label, suggesting that they capture the concept to some extent but not exclusively. 
  3. **Low CCS** : When the heads have zero or only one matching description, implying minimal relevance and indicating that these heads are largely unrelated to the given concept. 


### Evaluating LLM judgements with human evaluations
An important question is whether LLMs as judges are reliable and aligned with human values. To answer this question, we conducted a human evaluation study where we compared the LLM judgements and independent human evaluations. We manually assessed the semantic alignment between each span and its corresponding label. The metrics agreed between human and LLM evaluations including Cohen’s kappa Spearman's rank correlation coefficient and Kendall’s tau. Cohen's kappa values exceed 0.8, indicating extremely substantial agreement, while the correlation scores consistently surpass 0.7, confirming strong alignment. These results suggest that with caution, we can use LLMs as evaluators in CCS analysis. 
### How robust is the CCS metric?
We analyzed the robustness of CCS computation to the number of TEXTSPAN (K) descriptions using varied datasets like CIFAR-10 and CIFAR-100. It became evident that performance remains stable across all K values with variations typically 1-3% accuracy across many CLIP models. The performance ordering is consistent irrespective of the value of K, indicating our concept alignment assessment captured meaningful patterns. 
The performance doesn’t seem to improve consistently with higher K values suggesting a smaller number (around 5) of TEXTSPAN descriptions are sufficient. This helps avoid unnecessary computational time and costs. 
### Concentrated concept ratio (CCR) 
As our results have shown, larger models' performance degraded less when high CCS attention heads are pruned. Was it due to redundancy i.e. multiple heads attending the same concepts? To investigate this, we have introduced a new metric called Concentrated Concept Ratio (CCR). This metric captures the extent to which parameters are redundantly represented across multiple high-CCS heads. 
multi
Where,
Cₘᵤₗₜᵢ - number of unique concepts that are concentrated on more than one head 
Hₕᵢ𝓰ₕ - set of attention heads with high CCS
CCR - concentrated concept ratio
  * A higher CCR: Greater redundancy
  * A lower CCR: More distributed and unique representation of concepts across heads


### CCR Results
**Regarding heads**
Our results showed that larger models displayed lower CCR. It means these models are more resilient to pruning of high CCS heads.
**Regarding layers**
Our results also indicated that deeper layers didn’t show significant concept duplication. This suggests redundancy across layers is not a dominant factor and the observed robustness in larger models is more likely due to distributed head-level representations rather than functional duplication across layers.
**Data sets**
We have used various datasets to generate CCS scores for different tasks :   
Data sets  
|  **Task1:** **Image classification**  |  **Task 2:** **Out-of-domain classification**  |  **Task 3:** **Video retrieval**  |  **Task 4:** **Measure the bias**  |  
| --- | --- | --- | --- |  
| CIFAR-10  | Imagenet-A  | MSRVTT  | FairFace  |  
| CIFAR-100  | Imagenet-R  | DiDeMo  | SocialCounterFactuals  |  
| Food-101  |  
| Country-211  |  
| Oxford-pets  |  
Data sets  
|  **Task1:** **Image classification**  |  
| --- |  
| CIFAR-10 |  
| CIFAR-100 |  
| Food-101 |  
| Country-211 |  
| Oxford-pets |  
|  **Task 2:** **Out-of-domain classification**  |  
| --- |  
| Imagenet-A |  
| Imagenet-R |  
|  **Task 3:** **Video retrieval**  |  
| --- |  
| MSRVTT |  
| DiDeMo |  
|  **Task 4:** **Measure the bias**  |  
| --- |  
| FairFace |  
| SocialCounterFactuals |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
### Models
The following models were used in our research analysis:
ViT-B-32, ViT-B-16, ViT-L-14, OpenAI-400M and LAION2B 
### Conclusion
We performed soft-pruning analysis by zeroing out attention weights of heads with extreme CCS values (CCS = 5 and CCS <= 1). We discovered many interesting insights from our analysis. The key ones were: 
  1. Heads with high CCS were essential for maintaining model performance. Pruning these heads caused a significant performance drop in zero shot accuracy, while pruning low CCS heads had a minimal effect. This demonstrated that CCS effectively identifies heads encoding critical and concept-aligned information. 
  2. CCS not only identified functionally important heads but also captured model-specific and training-specific differences regarding the organization and utilization of conceptual knowledge. 
  3. CCS proved to be a reliable and interpretable metric for identifying concept-aligned heads. The metric demonstrated that high CCS heads are critical for concept-aligned tasks.
  4. High CCS heads proved crucial for general vision language tasks as well as zero-shot video retrieval.
  5. High CCS heads were important for out-of-domain detection and targeted concept-specific reasoning.
  6. High CCS heads were vital for temporal and cross-modal understanding
  7. High CCS heads often encoded spurious correlations contributing to increased social bias. Selective pruning was necessary to reduce the biases without the need for expensive fine tuning.


### Limitations
  1. CCS metric was used and tested on CLIP models only. Other vision language models were out of scope for this research. 
  2. Manual verification methods could be scaled up without the need to manually verify all concept labels. 


### Links
The original research paper can be accessed [here](https://arxiv.org/html/2503.11103v2).