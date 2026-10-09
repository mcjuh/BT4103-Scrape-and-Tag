<!-- Source: https://research.thoughtworks.com/library/cultural-counterfactuals | Title: Cultural counterfactuals | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Cultural counterfactuals
By 
Published: July 20, 2026 
Assessing biases related to religion, nationality, or socioeconomic status based solely on visual cues of a person or group remains a difficult task for today’s large vision language models (LVLMs).
Most prior research focuses on easily visible traits like gender, race and age proving that models perpetuate stereotypes and show performance disparities across these groups. In short, there are three challenges regarding model biases. They are:
  * **Hidden biases:** Harder-to-visualize traits (religion, nationality, socioeconomic status) also show stereotypical bias, which typically increases when visual information is ambiguous. 
  * **The cultural inclination:** Many models suffer from a strong Western bias and struggle to recognize other cultures. Crucially, a model must actually possess enough cultural awareness to recognize a cue before it infers. 
  * **The counterfactual method:** To isolate exactly what triggers a bias, researchers use "counterfactual image sets" — images that are identical except for one specific variable (e.g., changing the person while keeping the background the same). Our research is the first to use this method to analyze cultural bias among the LVLMs.


To address these challenges, we created a synthetic dataset named “cultural counterfactuals”. The dataset contains 60,000 counterfactual images which allows us to isolate and measure hidden cultural biases in popular LVLMs by changing the background context while keeping the person exactly the same.
_A counterfactual means contrary to the facts. A counterfactual follows an “if…then” structure about the past. At its core, a counterfactual is a concept or statement about what might have happened if things had been different._
### Fundamentals
LVLMs generate text as its output based on the input consisting of images and text. As the output text can exhibit social bias, alarm has been raised. Today’s techniques that use multimodal datasets are based on certain attributes like physical appearance of a person in the input images. However, experiments have shown that we need a few more attributes to correctly quantify the social biases produced in the LVLS’s output. One of the strong attributes is capturing the cultural context visible in the background of the input images. 
**Why do we need a new dataset?**
There are many photographic datasets available for VLMs today. However there were three reasons we decided to create a new dataset:
  1. Today some of the photographic datasets focus on certain annotations for a few cultural contexts. These annotations do not depict the individual within the context. Example: Eiffel Tower (Paris) or Khajuraho temples (India). 
  2. Many datasets entangle the two critical aspects: (a) the appearance of a person in the image and (b) the background context. Therefore, it’s impossible to tell whether the biased text output produced by the model is influenced by either (a) or (b) or both. 
  3. Purely computer generated images in the dataset could introduce model hallucinations or incorrect depiction of nuances in culture and civilization.


To address these issues we created a new dataset with controlled image generation. We now describe the structure and the process of its creation. 
### How did we create the cultural counterfactuals dataset?
The cultural counterfactuals dataset was generated using a simplified process pipeline:
  1. **Source image acquisition:** We first acquired real photos of cultural contexts from the web and synthetic images of people with a diverse range of social attributes (race, age and gender). The original images were verified to have human annotated labels for distinct cultural contexts, but no persons. These images were acquired from three existing datasets with labels for religion, nationality and socioeco-enomic cultural contexts. We created prompt templates combining intersectional social attributes (race, age and gender) and generated 7,200 people images using the FLUX.1-dev model across 144 unique templates. A powerful AI model (Qwen2.5-VL) double-checked the images to ensure their accuracy. 
  2. **Generating counterfactuals:** We then used a state-of-the-art image editing model to insert synthetically generated person(s) into the real scene. We repeated this across various cultural settings to build the "counterfactual" pairs. A prefiltered person image and cultural context image (places of worship or residential images of various kinds like bunglows, apartments, or slums) are stitched together and passed as input to the FLUX.1-Kontext-dev image editing model. Most of the time this process produces a viable counterfactual image. However, in certain cases it fails. For example, the cultural context may not be recognizable because it is hidden behind the subject. This necessitates a mechanism to control the quality of the output generation. 
  3. **Controlling quality:** We therefore applied a multi-stage, automated filtering and regeneration to automatically eliminate failure cases and ensure the cultural context remains distinct (clear and not ambiguous) and highly recognizable from the generated image, resulting in a high-quality dataset suitable for reliable diagnosis of LVLM biases. Here are the subprocesses:
    1. **CLIP filtering:** To filter out failed image fusions, CLIP-ViT-L/14 (a variant of OpenAI’s CLIP model) similarity scores are calculated between each generated counterfactual image and its two sources. Outputs are discarded if their similarity score falls below 0.75 for the context image or 0.85 for the person image.
    2. **Context detectable filtering:** To ensure the cultural context remains recognizable post-fusion, RMBG-2.0 is first used to remove the person from the counterfactual image, eliminating classification bias. Qwen2.5-VL-32B-Instruct then classifies the isolated background context. If the model misidentifies the context, the counterfactual image is discarded.
    3. **Regeneration:** Failed images enter an iterative regeneration pipeline executed over five rounds (one original context round, four new context sampling rounds)
       * **CLIP Failures:** Regenerated up to 25 times using different random seeds and varied guidance scales.
       * **Context Failures (and unresolved CLIP failures):** Processed through the same 25-attempt loop, but with a newly sampled context image to replace unblendable sources. This loop successfully preserved over 98% of the data, producing a human-validated final dataset of 59.8k images across 10.3k counterfactual sets (remaining failures were discarded).


  * **4. Human validation:** After all the above steps a human validation study confirms that the mitigation is successful.


### Dataset details
The Cultural Counterfactuals dataset is the first-ever image dataset designed to diagnose model biases related to religion, nationality and socioeconomic status. It included nearly 60,000 images grouped into counterfactual sets. Each set features the exact same person depicted in different cultural backgrounds. We built a bias-checking framework and used it to analyze more than nine million responses from five different vision-language models.  
Table showing the dimensions of the data set  
| Dimensions  | Contexts  | Images  | CF sets  | Context labels  |  
| --- | --- | --- | --- | --- |  
| Religion  | 6  | 30,978  | 5,163  | Christian, Muslim, Jewish, Shinto, Hindu, Buddhist  |  
| Nationality  | 8  | 21,352  | 2,669  | France, Germany, Morocco, South Africa, Brazil, USA, China, India  |  
| Socioeconomics  | 3  | 7,497  | 2,499  | Low, Middle, High income  |  
| **Total**  | **17**  | **59,827**  | 10,331  | —  |  
Table showing the dimensions of the data set  
| Dimensions |  
| --- |  
| Religion |  
| Nationality |  
| Socioeconomics |  
| **Total** |  
| Contexts |  
| --- |  
| Images |  
| --- |  
| 30,978 |  
| 21,352 |  
| 7,497 |  
| **59,827** |  
| CF sets |  
| --- |  
| 5,163 |  
| 2,669 |  
| 2,499 |  
| 10,331 |  
| Context labels |  
| --- |  
| Christian, Muslim, Jewish, Shinto, Hindu, Buddhist |  
| France, Germany, Morocco, South Africa, Brazil, USA, China, India |  
| Low, Middle, High income |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Images were acquired from various official sources from the internet. The religion, nationality and socioeconomic context prompts are used both for filtering source images and for evaluating whether the context can be detected in the counterfactual image. We manually reviewed 100 randomly sampled counterfactual images each to validate the quality of our dataset. We also annotated an equal number of images with religion, nationality and socioeconomic contexts. We provide examples of complete counterfactual sets for religious, socioeconomic and nationality cultural contexts. We provide examples of failed counterfactual image generations which were automatically identified by our dataset filtering & regeneration pipeline.
To validate dataset quality, 100 randomly sampled counterfactual images each were manually reviewed and an equal number of images were annotated with religion, nationality and socioeconomic contexts. This work presents examples of complete counterfactual sets for these cultural contexts, alongside examples of failed counterfactual image generations that were automatically identified by the dataset filtering and regeneration pipeline.
The five evaluated open source LVLMs are described in the table below:  
jkahdjka  
| Model  | Parameters  | Type  |  
| --- | --- | --- |  
| Qwen2.5-VL-7B-Instruct  | 7B  | Instruction-tuned  |  
| Gemma-3-12b-it  | 12B  | Instruction-tuned  |  
| InternVL3-8B  | 1B, 8B, 14B, 38B  | Instruction-tuned  |  
| LLaVA-v1.6-Mistral-7B  | 7B  | Instruction-tuned  |  
| Molmo-7B-D-0924  | 7B  | Base  |  
jkahdjka  
| Model |  
| --- |  
| Qwen2.5-VL-7B-Instruct |  
| Gemma-3-12b-it |  
| InternVL3-8B |  
| LLaVA-v1.6-Mistral-7B |  
| Molmo-7B-D-0924 |  
| Parameters |  
| --- |  
| 7B |  
| 12B |  
| 1B, 8B, 14B, 38B |  
| 7B |  
| 7B |  
| Type |  
| --- |  
| Instruction-tuned |  
| Instruction-tuned |  
| Instruction-tuned |  
| Instruction-tuned |  
| Base |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
### Examples of counterfactual sets in various contexts 
**Religious contexts**
**Socioeconomic contexts**
**Nationality context**
### Evaluation and insights
In the previous sections we discussed how we have built, filtered and cleaned our image dataset. Now let us review our evaluation framework. The framework breaks down into six primary layers of evaluation. We achieved this by carefully selecting five open-source LVLMs and then evaluating nine million responses. (We have provided a link to the paper for Interested readers at the end of this blog.) 
In brief, the questions and the insights of our evaluations were as follows:
**1. Context classification and refusals**
We begin by checking two baseline behaviors. We used GPT-5-nano as LLM-as-judge:
  * **Cultural awareness:** Can the model recognize the culture in the image? If it can't, it's hard to accurately measure intentional bias.
  * **Refusal rates:** Does the model simply refuse to answer prompts for certain cultures? High refusal rates can lower the model's toxicity scores, masking underlying biases.


**Insights**
  * It was easier to identify cultural dimensions like religion and nationality than identifying socioeconomic status.
  * Socioeconomic context presents a universal hurdle across open-source architectures, consistently yielding lower classification accuracy.
  * For a particular model family, model accuracy generally improves as parameter size increases.
  * Refusal behaviors are not triggered by text alone; specific visual background elements can drastically increase refusal rates.


**2. Sensitivity analysis**
The context sensitivity is the degree to which the keywords generated for a particular individual change across contexts within a counterfactual set. We measure the set-level variation using Jaccard overlap. The framework measures how sensitive the model is to the changing cultural context. The model is unbiased with respect to the particular context if its output is constant w.r.t. the specific cultural context. If a model can accurately detect the cultural context and is highly sensitive to that context, then bias might be present. 
**Insights**
  * In the relationship between cultural awareness and sensitivity, we realized that high sensitivity does not necessarily indicate bias; it may also arise when a model is unsuitable or does not reliably recognize the intended context. 
  * Culturally-aware models like Gemma-3-12b or Qwen2.5-VL exhibit relatively stable sensitivity. 
  * Increasing model size scales a model's output stability, making its responses more reproducible and less prone to random variation.
  * Filtering sensitivity data to isolate true awareness reveals that low-performing models lack the consistency in their generated responses.


**3. Numerical prompt**
We have prompted the models for numerical responses regarding salary and rent recommendations. They isolate cultural bias from racial or gender bias by calculating the deviation from the mean within a counterfactual set:
- average deviation for context c - total set of all counterfactual sets  - numerical output for context c within set s - overall mean numerical output within set s
If the output of the model does not change when the cultural context changes, then the deviation within the set S will be zero.
If the model suggests a lower salary for a young black woman standing near a mosque than the exact same image of her standing near a church, the metric isolates the mosque context as the sole variable driving that economic penalty.
**Insights**
  * Visual background cues influence statistically biasing quantitative measurements like salary and rent recommendations for the prompts.
  * Bias patterns are not uniform across the models. Different models react to the same cultural and geographic backgrounds in completely inconsistent and unpredictable ways.


**4. Toxicity**
To measure how cultural bias affects AI, we used a metric called MaxToxicity. A MaxToxicity score of zero means the model generated the exact same level of toxicity for every cultural context within a counterfactual set, showing no bias. A higher score means the model under test singled out at least one specific culture and generated much more toxic content for it compared to the others.
**Insights**
  * When exposed to varied visual contexts, different model architectures exhibit different baselines for generating toxic content.
  * Toxic and biased responses aren't spread evenly; they heavily target specific religions and low-income backgrounds, recycling old, real-world biases.
  * We have reported 95th percentile of MaxToxicity, which characterizes rarer cases of large toxicity differences across contexts which are nevertheless significant when LVLMs are deployed at scale.


**5. Topic model**
To see how cultural context influences the AI's writing, we took the most toxic responses and grouped them into common themes using a topic model. Then we manually checked these themes to find keywords that looked like stereotypes against specific groups. Finally, we calculated how often each cultural group appeared within those themes. This created a ranked list showing exactly which cultures the model under test unfairly singled out and over-represented in negative stereotypes.
**Insights**
  * Harmful assumptions get significantly worse when multiple traits, like race and religion, combine in one image.
  * The background context alone drives biased responses, even if you change the person's race.


### Conclusion
Our contribution to LVLM bias mitigation is threefold. Here is the visual depiction.
This study demonstrates that large vision-language models carry measurable cultural biases shaped by visual cues, with severity shifting across religion, nationality and social class. Models differ substantially in cultural awareness — more capable models such as Qwen2.5-VL and Gemma-3 show greater sensitivity while smaller models remain ill-suited for culturally sensitive deployments. 
Crucially, biases across race, religion and national markers interact in unpredictable ways, meaning correcting one axis of bias leaves others intact, underscoring the need for more diverse training data and context-specific fairness evaluation.
The cultural counterfactuals dataset introduced here proved effective in surfacing latent, context-dependent biases that conventional benchmarks tend to overlook. Models with demonstrated refusal behaviours around negative stereotyping should be preferred wherever cultural neutrality is a hard requirement. Ultimately, progress on cultural fairness in vision-language models demands sustained effort across data curation, model evaluation and deployment governance — no single intervention is sufficient.
### For deep dive 
Cultural Counterfactuals: Evaluating Cultural Biases in Large Vision-Language Models with Counterfactual Examples - [Link](https://arxiv.org/abs/2603.02370). 
**END**