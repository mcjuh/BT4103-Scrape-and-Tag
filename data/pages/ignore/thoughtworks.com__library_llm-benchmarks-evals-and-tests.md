<!-- Source: https://research.thoughtworks.com/library/llm-benchmarks-evals-and-tests | Title: LLM benchmarks, evals and tests | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# LLM benchmarks, evals and tests
By 
Published: October 31, 2024 
### Introduction
Evaluating applications built on **large language models** (LLMs) is challenging due to the complexity of understanding model behavior, the variability in outputs, the difficulty in interpreting decision-making processes and the need to measure performance across diverse tasks and real-world scenarios. Unlike classical machine learning models, which operate in structured and well-defined tasks, LLMs generate open-ended responses across an infinite output space.
This particular complexity renders traditional evaluation metrics, like **precision** and **recall** , insufficient. This means **LLM evaluation** demands new methods to measure things like coherence, relevance, safety and reasoning. Moreover, ensuring the real-world reliability of LLM-powered systems requires comprehensive evaluation which goes beyond model-centric **benchmarks**. Such evaluation needs to address how models interact with **prompts** , how they make **decisions** , and how they function inside the **full application stack** when deployed.
### **Why is evaluation so hard?**
**“Classical” AI models** are easier to evaluate because they typically handle structured data, which often have a **smaller number** of engineered features. In addition, these models are **purpose-built** for specific, well-defined tasks like classification, regression and clustering. This “limited scope” makes it easier to define specific well-established and interpretable **metrics** for testing, like precision and recall for **classification** , or root mean square error (RMSE) and mean absolute error (MAE) for **regression**. Since classical model behavior is **more predictable** , the relationships between inputs and outputs can be understood more easily. However, with LLMs, evaluations become complex because the model can generate entirely new, unexpected responses that don’t always fit neatly into pre-defined patterns of behavior.
Suppose we have a classification model tasked with predicting whether an email is either "Spam" or "Not Spam." We evaluate this model on 100 test emails. Here, we can easily calculate metrics like precision, recall, and accuracy because all predictions are confined to these two classes.
  * **True Positives (Spam identified correctly):** 40
  * **True Negatives (Not Spam identified correctly):** 50
  * **False Positives (Not Spam classified as Spam):** 5
  * **False Negatives (Spam classified as Not Spam):** 5


From this:
  * **Accuracy** = (True Positives + True Negatives) / Total = (40 + 50) / 100 = 90%
  * **Precision** = True Positives / (True Positives + False Positives) = 40 / (40 + 5) = 88.9%
  * **Recall** = True Positives / (True Positives + False Negatives) = 40 / (40 + 5) = 88.9%


Now, imagine an LLM tasked with the same goal: identifying whether an email is "Spam" or "Not Spam." You may hope that the LLM only chooses from just these two labels, but practically speaking - it will hallucinate something outside of these constraints at some point.
Suppose the LLM generates these outputs for the first 10 test emails:
  1. "Spam"
  2. "Not Spam"
  3. "Promotional"
  4. "Unsubscribe Offer"
  5. "Spam"
  6. "Not Spam"
  7. "Not Spam"
  8. "Spam"
  9. "Questionable"
  10. "Spam"


While "Spam" and "Not Spam" are valid outputs, responses like "Promotional," "Unsubscribe Offer," and "Questionable" don't fit the original two-class system. What do we do with these? Should they be counted as false negatives or some new category altogether? What does that do to the statistical conclusions we can draw from these calculations?
Let's assume:
  * **True Positives (Spam identified correctly):** 40
  * **True Negatives (Not Spam identified correctly):** 40
  * **False Positives (Not Spam classified as Spam):** 10
  * **False Negatives (Spam classified as Not Spam):** 2
  * **Hallucinations 1 (Spam classified as “Promotional” or similar):** 3
  * **Hallucinations 2 (Not Spam classified as “Promotional” or similar):** 5


In this case, calculating metrics like precision becomes tricky. Should the hallucinations count as false negatives or be ignored entirely? How does that choice affect the way we interpret these metrics? Let’s say we treat hallucinations as incorrect classifications (e.g. bucket them into False Negatives and False Positives):
  * **Accuracy** = (True Positives + True Negatives) / Total = (40 + 40) / 100 = 80%
  * **Precision** = True Positives / (True Positives + False Positives + Hallucinations 2) = 40 / (40 + 10 + 5) = 72.7%
  * **Recall** = True Positives / (True Positives + False Negatives + Hallucinations 1) = 40 / (40 + 2+ 3) = 88.9%


Or if we just disregard hallucinations altogether?:
  * **Accuracy** = (True Positives + True Negatives) / Total Valid Outputs = (40 + 40) / 92 = 86.96%
  * **Precision** = True Positives / (True Positives + False Positives) = 40 / (40 + 10) = 80%
  * **Recall** = True Positives / (True Positives + False Negatives) = 40 / (40 + 2) = 95.24%


So for Accuracy, we have a range between 80-86.96%, Precision: 72.7-80%, Recall: 88.9 - 95.24%... How do we actually interpret this? Do we even have enough data to make conjectures about things like hallucination rates?
This obviously gets even more complex as task complexity increases, but this foundational breakdown of “statistical trust” is at the heart of why evaluating LLM-powered systems calls for a new way of thinking.
#### LLM-powered systems
LLMs are the core of modern **generative AI systems**. A typical GenAI system consists of the LLM in addition to interfaces for processing prompt input and system output, application logic and other wrappers for system deployment and security. Each one of these elements needs to be tested in an **environment** the system is developed to operate in. 
These models are inherently **stochastic**. That means they produce different outputs even when they’re given the same input on different runs. This **randomness** is due to mechanisms like **sampling** while generating output (e.g., beam search or temperature-based sampling). This introduces **challenges** in **classical software testing paradigms** , since the insertion of randomness may cause “flakey behaviors” in otherwise simple tests. That’s not to say that everything about an LLM-powered system requires a complete recalibration in terms of testing strategy, but it begs the question: how should one think about the **relationship between benchmarks, evals, and tests**?
### Benchmarks, evals, and tests
The AI industry is awash with model-builder claims of achieving “state-of-the-art” (SOTA) performance on various benchmarks. These are often used as selling points for one model over another, or one offering over another. Without diving too deeply into how this particular frenzy is driven by a lot of snake oil (don’t worry, we’ll get to that soon), let’s first frame where benchmarks, evals, and tests should sit in our mental model of “software reliability in GenAI”: 
  * **Benchmarks provide a consistent point of comparison**. They are standardized datasets and tasks used to measure the general capabilities of models across the industry. For example, benchmarks like SQuAD or WMT test LLMs on tasks like question-answering or translation, giving a sense of overall performance. However, benchmarks are static and limited—they likely won’t capture the unique challenges or context your specific application faces.


  * **Evals focus on understanding** how your LLM-powered components behave in your specific application environment. While benchmarks offer a general comparison, evals go deeper into the intricacies of the system's performance on real-world tasks. For example, if your GenAI system is a chatbot, your evals might include how well it maintains context in long conversations, detects user emotions, or handles ambiguous queries. Evals allow you to probe deeper into the “why” behind system behaviors, offering insights into failure modes, edge cases, and emergent properties that are specific to the involvement of an LLM.


  * **Tests are all about validation**. They ensure that the system or software behaves as expected, often using pass/fail criteria. You might imagine, then, that in order to **validate** you must first **understand** the requirements of the system in the production environment. In LLM-powered systems, it would make sense to create tests on top of evals to action on the understanding.


In summary: 
  * Use benchmarks (with grains of salt) to compare model capabilities directly
  * Use evals to measure and understand the performance characteristics of your system
  * Use tests to validate and action upon these learnings (e.g. “fail” if some set of metrics dip below acceptable thresholds)


### How should I think about “evals”?
The GenAI world has found it very difficult to define the term **evals** (evaluations). At the moment, most practitioners approach evals from the lens of evaluating a model’s **output** in the context of the application.
While this approach is pragmatic given the current state of thinking around the technology, we believe that the scope should be expanded to include a model’s **input** and **decisioning** (as best as it can be approximated) as well. 
In the same way that “good” software testing tests a system in its entirety – from atomic components to complex interactions across modules, effective LLM evals should help practitioners **understand** not only the quality of the outputs in a vacuum, but also how shapes of input may affect those outputs and how a given model’s decision-making mechanisms may operate against the backdrop of the use case.
To provide some perspective on these three buckets, some examples are provided below – however bear in mind that evals is very much an area of active research so this list is meant more to paint a picture of the “art of the immediately possible”, rather than to serve as a comprehensive list of all ways to evaluate an LLM-powered system.
**1) Evaluating the input:**
  * Input sensitivity testing
    * Evaluate how small variations in the input affect the model’s performance on the task
    * _Example_ : An LLM chat application is evaluated using perturbed user queries (e.g., "What is the capital of France?" vs. "What's the capital of France?") to see if it provides consistent and correct answers.
  * Input importance analysis
    * Test how specific tokens in a given input may have outsized impact on the content and quality of a given generated output
    * _Example_ : A RAG-based application may use a system prompt that inadvertently causes the model to disregard some of the context brought in from the retrieval system. This can happen simply because of a quirk in prompt formatting, it may not be an explicit instruction provided by the prompt designer.


  * Ambiguity detection
    * Evaluating whether the given context provides enough information to accomplish the task.
    * _Example_ : “Tell me about our last quarterly earnings.” – was the right context retrieved for the given task for the model to synthesize an accurate answer?


**2) Evaluating the output**
  * Uncertainty measures
    * Measuring the intrinsic uncertainty in the model’s output
    * _Example:_ For a given prompt, how certain was the model about the content in the output? About the structure of it?
  * Hallucination detection
    * Identifying instances and types of hallucinations in a given model’s output
    * _Example_ : For a task generating news summaries, an eval might assess how often the model introduces hallucinated facts that are not present in the original article. 
  * Coherence and Fluency measures:
    * Assessing the grammatical correctness, readability, and logical consistency of the generated text.
    * _Example_ : For a chatbot or dialogue system, you might use BLEU or ROUGE scores along with other LLM judges to measure how fluent the text is and whether the conversation flows naturally.


**3) Interpreting model decisioning:**
  * Feature Attribution
    * Evaluating which input features (words, phrases, or tokens) are driving the model’s decisions.
    * _Example:_ In a sentiment analysis task, evaluating which tokens the model is heavily relying on to classify a sentence as positive or negative. A human can use this to figure out if the most important tokens match their expectations for sentiment classification.
  * Neural Activation Pathway/Circuit Analysis:
    * Evals that assess how internal layers and neuron activations contribute to specific decisions. This is often used in mechanistic interpretability to understand which hidden representations are activated and how they evolve as the input is processed.
    * _Example:_ Extracting hidden representations from a given model (e.g. LLaMa) to evaluate which patterns of activations consistently occur when processing specific types of inputs (e.g., detecting factual statements vs. opinions).


This is an active field of research, with advancements in model/application evaluation happening at an accelerating pace. We expect that the evaluation landscape will change drastically over the next year as more companies try to bridge the gap between GenAI POC and production.
### How should I think about “benchmarks”?
At their core, benchmarks aim to provide a standardized way to **compare models** against a consistent set of tasks and datasets. For example, benchmarks like GLUE for natural language understanding or SQuAD for question answering offer a snapshot of how well models perform in specific, controlled environments. However, while benchmarks can be useful for gauging a given model’s general capabilities, they don’t tell the full story and often get misused. 
  1. **Static by nature** : Benchmarks are inherently static. They represent a fixed set of tasks and datasets that models are tested against. This makes them great for comparing performance across models, but they are often detached from the rapidly changing and dynamic environments in which LLMs are deployed. In production, models are expected to handle inputs they’ve never seen before, often under conditions not reflected in benchmarks.
  2. **Surface-level insights** : While benchmarks can indicate whether a model performs well on specific tasks (like translation, summarization, or sentiment analysis), they often provide surface-level insights. A model might achieve high scores on a benchmark but still struggle with edge cases or domain-specific challenges that aren’t captured in the benchmark data. For instance, a chatbot might ace a conversation benchmark, yet fail to engage in real, nuanced customer support interactions.
  3. **SOTA and the leaderboard race** : The AI industry’s fixation on “state-of-the-art” (SOTA) performance can create a misleading narrative. Models that top leaderboards are often designed to perform well on a particular benchmark or trained directly on the benchmark data, but this does not guarantee their effectiveness in broader or more complex use cases. The focus on benchmark scores can also encourage over-optimization for these tasks, sometimes at the expense of generalizability or robustness in real-world settings.
  4. **Not reflective of system complexity** : Benchmarks tend to evaluate models in isolation, without considering the complexities introduced when the model is integrated into a larger system. An LLM might perform well on a benchmark that tests its language generation, but how it performs when integrated into a workflow with APIs, databases, or other microservices is an entirely different matter. Real-world systems often involve many more variables, including latency, user interaction, and varying data quality, none of which are captured by traditional benchmarks.


Benchmarks should be viewed as one piece of the puzzle. They offer useful data points for comparing different models but should not be the sole deciding factor when evaluating the viability of an LLM for a specific task. A high benchmark score might make a model a candidate for consideration, but additional evals (specific to your application environment) are critical for assessing its true fit.
### How should I think about testing (with regards to LLMs)?
Testing software is not just about validation (though that’s a huge part of it), it’s ultimately about accelerating development by providing continuous feedback, reducing errors, and ensuring system reliability. LLMs introduce variability and complexity into the development process, making traditional testing techniques more difficult to implement directly. However, when tests are built on the foundation of evals and integrated into the development workflow from the beginning, iterations become faster and outcomes more reliable.
Concretely:
  1. **Decompose the system** : Break the LLM-powered system down into smaller, testable components – the best way to do this is to think of the LLM as a black box that takes text as input and returns text as output. Identify the chain of components that bump up against this box, like those involved in constructing the text input or processing the output from the LLM, and test those separately. As an example: treat “retrieval” and “generation” separately in RAG systems – test the retrieval system (e.g. are the most relevant docs being pulled? Is the chunking strategy working the way you expect?) independently from generation (e.g. all of the evals).
  2. **Evals as the basis for testing** : By building the right evals, you gain a clear understanding of how the generation component of the system behaves in real-world contexts before writing tests. As you might iterate on various parts of the system, being able to track how upstream modifications affect the generative properties of the application make it easier to build an intuition for how you might iterate.
  3. **Integrating tests-on-evals in CI/CD** : Evals should be embedded in your CI/CD pipeline, running after every model update. This provides early detection and a record of performance issues in real-world conditions, while automated tests validate that the system operates within acceptable parameters. As a general rule: try to put evals as early as reasonable in a CI DAG so that you can build a detailed understanding of the variability you may see in the performance of the system over time.


### Conclusion
Evaluating LLM-powered systems requires a shift in how we think about benchmarks, evals, and tests. Instead of simply over-indexing on model benchmarks, it’s important to think about the distinct purpose of each: Benchmarks are for model comparisons, Evals are for understanding the performance properties of the system, and Tests are for validating that those properties fall within acceptable bounds. This space will continue to evolve quickly, as organizations are realizing that a big reason why GenAI proofs-of-concept are not making it to production is because they’re simply not being measured in ways that build trust and confidence.