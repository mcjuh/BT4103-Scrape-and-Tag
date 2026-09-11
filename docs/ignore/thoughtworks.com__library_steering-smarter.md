<!-- Source: https://research.thoughtworks.com/library/steering-smarter | Title: Steering smarter | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Steering smarter
By 
[Amirali Abdullah](https://research.thoughtworks.com/team#amirali-abdullah) and
Published: November 29, 2025 
### Why K-Steering is reshaping LLM activation engineering 
**Background**
Activation engineering is a way to directly edit a model’s internal activations to change how it behaves. If the nodes in a neural net are like brain cells, then the activations are analogous to the brain cells’ firing patterns; they shift and change depending on model inputs. What if you could tweak those patterns to change the thoughts that follow?
The simplest form of activation engineering is called linear steering. This is where you find a direction in the activation space that represents a specific trait, like positivity or formality, and add it during inference while the model is running. [Turner et al. (2023)](https://arxiv.org/pdf/2308.10248), for example, showed how you can build a sentiment vector by contrasting prompts like _I love this_ and _I hate this_ , then inject that vector to flip the model’s tone from negative to positive.
This works well for single traits, but it gets messy when you try combining vectors. Adding two vectors, like one for safety and one for formality, often fails to give you safe and formal text. Instead, the traits can cancel each other out, or the model drifts into awkward or stilted language. Features don’t just stack neatly; they collide in unpredictable ways.
To handle this, researchers at Thoughtworks are exploring non-linear steering methods.
These go beyond simple vector addition by modeling how traits overlap and entangle inside the network. The work is still early, but it shows promise for steering multiple traits at once while keeping the text natural and fluent.
### Why activation engineering?
In the recent past, language model control has been performed using various approaches. The most popular ones are: 
  1. Intervening on weights, with supervised fine-tuning on desired outputs.
  2. Intervening on weights with reinforcement learning using human feedback (RLHF) or with AI feedback.
  3. Intervening at decoding time, using constrained generation.
  4. Intervening on the prompt, as with manual or automated prompt engineering


However, all of these approaches have certain limitations. For example, fine-tuning takes a long time, careful dataset curation and heavy computing resources, which makes it expensive and impractical in many instances. Prompt engineering is unreliable and can elicit a limited range of model capabilities.
Activation engineering is a recent technique gaining popularity for steering a pre-trained large language model (LLM) to a desired behavior. The uniqueness of this approach is that it’s achieved at inference time by strategically perturbing activations at specific intermediate layers of the model. These activations are nothing but multi-dimensional vectors added only to the “forward passes” of the LLM.
Activation engineering provides a more direct and interpretable approach to control the model output. It also lowers the operational cost, saves time and improves the model’s reliability for the desired output. 
Various approaches were developed to create vectors of activations, each having its own peculiarities. Here are a few popular ones: 
**Approach 1:**
This approach is called **ActAdd** , where vectors are added to a subset of sequence positions. These generally require only a handful of examples for validation and can be computed directly from simple token embeddings. 
**Approach 2:**
This approach, called **contrastive activation addition (CAA)** , is a technique to steer language models by changing their internal activations during each forward pass. CAA creates steering vectors by averaging the differences in activations between pairs of examples that show opposite behaviors. These are usually computed with the activations of the last token of the response, but the position used may vary. During inference, these steering vectors are added to the model’s activations at every token position after the user’s prompt, with either a positive or negative weight, allowing fine-grained control over the behavior. 
Although popular, both approaches are linear and use an additive function in the activation space. As such, neither solves the challenge of controlling multiple behavioral attributes of the model at inference time. One has to go beyond linear steering. 
The K-steering method is one potential approach. 
### K-Steering: Leveraging gradients of multi-layer perceptron (MLP) classifiers on activations
K-Steering is a novel approach designed to overcome the challenges of linear steering to achieve multi-attribute control of large language models. We have used the multi-layer perceptron (MLP) in this work. So before diving deeper into the approach, let’s provide some background on the multi-layer perceptron (MLP), a simple feed-forward neural network that can be used to recognize when certain behaviors appear in the model’s internal representations. 
Historically, perceptrons proved to be powerful classifiers. A single perceptron works like a neuron, accepting multiple inputs and giving a binary pulse as a response. An MLP contains many intermediate layers of neurons called nodes. Each node includes a non-linear activation function that’s differentiable. Mathematically, a neuron is a perceptron made of weights and bias parameters. A high-level representation of a multi-layer perceptron is shown here:
**Figure 1: MLP architecture**
Each node contains two mathematical functions working in a pair. They are called a summation operator ∑ and an activation function σ(x).
The activation function receives the output from the summation operator and transforms it into the final output for a particular node when the input signal exceeds the threshold value. Let us take an example. 
The node shown here has two inputs, x1 and x2, providing an output y. Another input 1 to the node is bias b, which is always multiplied by the input 1. 
**Figure 2: - Activation function**
Output
z = w1.x1 + w2.x2 + b 
y = a(z)
For a simple linear node, 
a(z) = z
y = w1.x1 + w2.x2 + b
The function a(z) is the activation function. 
Another important reason to use an activation function is to introduce non-linearity to the neural network. This non-linearity offers the power of breaking down a problem into sub-problems and combining their results to arrive at the overall solution. There are various types of activation functions. The most popular are as follows: 
**The simplest way to understand an activation function is to imagine a neural network as a collection of functions where the "weights" define the numeric values of the functions. The "activations" are then the output values of these functions on a per input level, and these can be altered without changes to the underlying "weights" of the neural network.**
- Anil Ananthaswamy (The author of 'Why machines learn - The elegant maths behind modern AI) 
  * **Sigmoid” activation function** a(z) = (z), where: 


  * **ReLU (Rectified Linear Unit)**


a(z) = (z)
z, z >= 0
0, z < 0
  * **GeLU (Gaussian error Linear Unit)**


a(z) = (z) = x⋅Φ(z)=0.5z(1+tanh(2/π​(z+0.044715x3)))
K-Steering trains a single, non-linear multi-label classifier on the model’s hidden activations. At inference time, the method uses the gradients of this classifier to guide the model’s behavior. These gradients indicate the subtle changes needed in the model’s internal activations to steer its output towards or away from desired attributes. 
Returning to our analogy of a neural network to a brain, this is like gently nudging the model’s internal thought process towards text with a human desired attribute.
### Advantages of K-steering method 
The K-steering method has a number of advantages, including:
  * **Simultaneous control**. The method gives greater control over the model's behaviors. This removes the need to prepare and compute separate steering interventions for each attribute while offering more robust handling of interactions between different behaviors. 
  * **Scalable design**. The method scales smoothly to larger sets of attributes without added code complexity. 
  * **Balanced steering**. The method allows the classifier to balance multiple steering attributes, unlike other methods that simply average multiple steering directions, diluting the aggregate effect. 
  * **Fine-grained tuning**. Steering results can be enhanced by applying extra gradient steps with smaller sizes, allowing fine-grained control over the behavior.


As a hypothetical example, let us use an MLP with two hidden layers with 256 units each and ReLU activations. The MLP is trained only on the final token’s activation. During steering, the classifier is applied to all token positions in the sequence to influence generation more broadly. Once trained, this MLP acts as a detector: it can spot whether the LLM is about to generate content aligned with a target label (for example, polite or humorous). Then, during inference, the gradient of this classifier with respect to the activation is used to steer the output. Let’s try and understand it mathematically. 
Ai′ = ai−α.∇ai.L(gϕ(ai))
where:
  * **ai** ​: The activation vector from the LLM. It is the representation (intermediate outputs) from the model at a specific layer, like a "snapshot" of what the model is thinking at each layer output. It is formulated as **ai** ∈ ℝ^{**d_seq × d_model**}, i.e., (sequence length × model dimension)
  * **gϕ:** The classifier. A small, separate MLP. It looks at activations from the model and predicts one of K behaviors (like tones or styles). Its job is to tell whether a hidden activation reflects the behavior, like the tone.
  * **gϕ(ai)** : the classifier’s prediction for that activation.
  * **L** : The loss function. It predicts how far the classifier is from predicting the desired behavior.
  * **∇ai.L** : The gradient vector of that loss function w.r.t. the activation. It tells us how to change the activation to make the classifier more confident about the target behavior.
  * **α** : A scaling factor that controls how strong the steering is.
  * **ai′** ​: The new, edited activation.
  * **fθ** : Model parameters θ (its internal learned weights).
  * **K** : Number of categories. These are the types of behaviors we want to steer the model towards or away from. 


### The K-Steering process
The process can be simplified into four stages.
**Figure 3: - K-steering process**
  1. The MLP classifier looks at the activation vector A to “guess” the kind of tone, behavior and style it reflects (e.g., sarcastic or formal). In a neural network like LLM, every layer takes in numbers, performs mathematical operations, and produces a new set of numbers. This new set is passed on to the next layer. This set is called an activation (or activation vector if it’s one-dimensional). So, A is the output of a specific layer after applying its activation function. 
  2. The “loss function”: For an activation vector A, calculate a steering loss that penalizes higher logits from a classifier on A for undesired labels and rewards higher logits for desired labels.
  3. The gradient (∆L) is the difference between A and A’. It indicates a required change in A so the classifier would come closer to the target style.
  4. Loss minimization: 
    1. Finally, the vector A is adjusted slightly in the direction that reduces the loss:A′=A−α ΔL
    2. A′ is the new, steered activation to be passed forward. 
    3. α is a scaling factor that controls how much steering is required.


### Algorithm 1: Iterative gradient-based steering towards desired classes
The objective is to adjust the model’s internal activation vector a so that its behavior leans more toward certain desired classes (like a friendly tone or formal style) and away from undesired classes (rudeness or informality). We note that since the gradient of a loss function is a _local_ approximation, taking multiple small steps yields more accurate results than a single step change  
Algorithm 1: Iterative gradient-based steering towards desired classes  
| **No.**  | **Algorithm steps**  | **Illustration**  |  
| --- | --- | --- |  
| 1  |  **Input** : Activation a ∈ RDₛₑq × dₘₒdₑₗ, target classes T⁺, avoid classes T⁻, initial learning rate α, number of steps K, decay rate γ  | Provided input with Activation a dimensions dₛₑq× dₘₒdₑₗ, target classes T⁺, avoid classes T⁻, initial learning rate α, number of steps K, decay rate γ  |  
| 2  | a₀ = a  | Initialize activation  |  
| 3  |  **for** k= 0 to K−1 **do**  | For each step k from 0 to K−1, do the following:  |  
| 4  | αk = α·γk {Apply learning rate decay}  | Set αk = α·γᵏ  |  
| 5  | L = 0  | Initialize the loss function (L)  |  
| 6  | If T+ is not empty then  | The desired target classes  |  
| 7  |  L= L−mean(gϕ(ak)T+ ) {Maximize logits for target classes}  |  Encourage higher classifier logits for those classes. (Rewarding the model for moving towards the desired style.)  |  
| 8  | end if  |  
| 9  | if T-is not empty then  | The undesired target classes  |  
| 10  |  L= L+ mean(gϕ(ak)T− ) {Minimize logits for avoid classes}  |  Penalize high classifier logits for those classes. (Discouraging the model from showing the undesired style.)  |  
| 11  | end if  |  
| 12  | Compute gradient ∇aₖ.L  |  Calculate∇aₖ.L The direction in activation space that would reduce the loss.  |  
| 13  | aₖ₊₁= aₖ αₖ∇aₖ.L  | Update activation with the gradient descent. This nudges the activation in the right direction.  |  
| 14  | end for  | Go back to Step 3 for the next iteration.  |  
| 15  | Return: aₖ  |  After K steps, output the final steered activation aₖ  |  
Algorithm 1: Iterative gradient-based steering towards desired classes  
| 10 |  
| --- |  
| 11 |  
| 12 |  
| 13 |  
| 14 |  
| 15 |  
| **Algorithm steps** |  
| --- |  
|  **Input** : Activation a ∈ RDₛₑq × dₘₒdₑₗ, target classes T⁺, avoid classes T⁻, initial learning rate α, number of steps K, decay rate γ  |  
| a₀ = a |  
|  **for** k= 0 to K−1 **do**  |  
| αk = α·γk {Apply learning rate decay} |  
| L = 0 |  
| If T+ is not empty then |  
|  L= L−mean(gϕ(ak)T+ ) {Maximize logits for target classes}  |  
| end if |  
| if T-is not empty then  |  
|  L= L+ mean(gϕ(ak)T− ) {Minimize logits for avoid classes}  |  
| end if |  
| Compute gradient ∇aₖ.L |  
| aₖ₊₁= aₖ αₖ∇aₖ.L |  
| end for |  
| Return: aₖ |  
| **Illustration** |  
| --- |  
| Provided input with Activation a dimensions dₛₑq× dₘₒdₑₗ, target classes T⁺, avoid classes T⁻, initial learning rate α, number of steps K, decay rate γ |  
| Initialize activation |  
| For each step k from 0 to K−1, do the following: |  
| Set αk = α·γᵏ |  
| Initialize the loss function (L) |  
| The desired target classes |  
|  Encourage higher classifier logits for those classes. (Rewarding the model for moving towards the desired style.)  |  
| The undesired target classes |  
|  Penalize high classifier logits for those classes. (Discouraging the model from showing the undesired style.)  |  
|  Calculate∇aₖ.L The direction in activation space that would reduce the loss.  |  
| Update activation with the gradient descent. This nudges the activation in the right direction. |  
| Go back to Step 3 for the next iteration. |  
|  After K steps, output the final steered activation aₖ  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Let’s now introduce algorithm 2. This shorter algorithm focuses only on removing unwanted attributes, using gradients from a non-linear classifier.
Imagine the activation vector as a point in space and the gradient as the direction pointing toward an unwanted behavior. The algorithm works by first computing the average logit for the avoid classes. The gradient shows the direction that increases those undesired behaviors. Then, the algorithm removes the activation's projection along this direction of undesired behaviors. 
### **Algorithm 2: Projection removal**
The main step in algorithm 2 (line seven) uses a linear transformation called a Householder reflection. In linear algebra, Householder reflection describes a reflection about a plane or hyperplane that contains the origin. Instead of just removing the part of the activation going in that direction, the Householder reflection flips it across the boundary — like bouncing light off a mirror. (See Figure 4.)
The Householder operator **a’** can be defined over any finite-dimensional dot product space **V** with a normal vector **v** expressed as: 
a′ = a−2[(a·v)/(v·v)] **v**
where **v** is the gradient and an element of **V**  
Table showing algorithm steps  
| No  | Algorithm steps   | Steps explanation  |  
| --- | --- | --- |  
| 1  | Input: Activation a, avoid classes T-  |  Provided input with Activation a, and avoid classes T-  |  
| 2  | L= mean(gϕ(a)T− ) {Loss uses raw logits to avoid classes.}  | Classifier gϕ with parameters ϕ is applied to activation vector a and returns the average logit value L for the undesired classes T-. We plan to find the direction of a that correlates with T-.   |  
| 3  | Compute gradient ∇aL  | The gradient gives the direction in activation space “a” away from the undesired classes.  |  
| 4  | Compute norm ||∇aL|| ²  | This calculates the squared L2 norm of the gradient vector. This is used for the projection  |  
| 5  | Compute dot product d= a ·∇aL  | If d is large, it means “a” has a strong component in the undesired direction  |  
| 6  |  Compute projection  p = (d/||∇aL||2) ·∇aL  | This is the vector projection: to isolate the part of “a” that contributes to the undesired class.  |  
| 7  | a′= a−2·p  |  This reflects the activation **across** a hyperplane orthogonal to p. Mathematically removes the projection of “a” onto the undesirable direction.  [This transformation reverses the component along the gradient direction, effectively pushing the activation away from the undesired attribute boundaries in the non-linear activation space.]  |  
| 8  | Return: a′  |  **a’** , the new activation, free from the undesired class in T-.  |  
Table showing algorithm steps  
| Algorithm steps  |  
| --- |  
| Input: Activation a, avoid classes T- |  
| L= mean(gϕ(a)T− ) {Loss uses raw logits to avoid classes.} |  
| Compute gradient ∇aL |  
| Compute norm ||∇aL|| ² |  
| Compute dot product d= a ·∇aL |  
|  Compute projection  p = (d/||∇aL||2) ·∇aL  |  
| a′= a−2·p |  
| Return: a′ |  
| Steps explanation |  
| --- |  
|  Provided input with Activation a, and avoid classes T-  |  
| Classifier gϕ with parameters ϕ is applied to activation vector a and returns the average logit value L for the undesired classes T-. We plan to find the direction of a that correlates with T-.  |  
| The gradient gives the direction in activation space “a” away from the undesired classes. |  
| This calculates the squared L2 norm of the gradient vector. This is used for the projection |  
| If d is large, it means “a” has a strong component in the undesired direction |  
| This is the vector projection: to isolate the part of “a” that contributes to the undesired class. |  
|  This reflects the activation **across** a hyperplane orthogonal to p. Mathematically removes the projection of “a” onto the undesirable direction.  [This transformation reverses the component along the gradient direction, effectively pushing the activation away from the undesired attribute boundaries in the non-linear activation space.]  |  
|  **a’** , the new activation, free from the undesired class in T-. |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Imagine the activation vector is pointing partly in the direction of hate. This algorithm finds that component and reflects it away, leaving only the parts that are orthogonal to the undesired output. 
This method is quicker and needs one gradient calculation and avoids the looping over multiple steps used in algorithm 1.
K-Steering works well even when applied to multiple layers of the model at the same time as follows:
  * First, train a classifier at a specific layer (layer x) in the model’s residual stream. (Some notes on the residual stream:
    * Each layer adds its output to what is called the residual stream. 
    * The residual stream is the sum of the outputs of all the previous layers and the original embedding.
    * It is like a channel through which all the layers communicate.
    * This channel has a linear structure.
    * At the start, every layer performs an arbitrary linear transformation to "read in" information from the residual stream and performs another arbitrary linear transformation before adding to write its output back into the residual stream.
    * See Figure 5 for an illustration, taken from Anthropic’s blog post on the [mathematical model of transformers](https://transformer-circuits.pub/2021/framework/index.html).)
  * Use the K-Steering method to compute the suitable gradient vector updates from this layer x.


Next, add this computed vector to guide changes across all residual stream layers (not just at layer x). 
**Figure 5: Residual stream. See “A Mathematical Framework for Transformer Circuits”.**
This broader intervention across all layers makes the method more effective; it’s able to shift complex behaviors. We expect this happens because the steps needed for a model to compute complex behaviors are distributed across multiple layers, hence all of them need to be intervened on simultaneously.
This kind of multi-layer simultaneous steering avoids the hydra effect. The hydra effect self-heals the model by activating alternative pathways if one tries to suppress certain internal components. (This is named after the mythical Hydra, which grows back heads when one is cut off.) Multi-layer steering methods that avoid this effect can more reliably target the intended internal representations and control outcomes without triggering the model’s natural self-repair behavior.
Steering effectiveness varies by layers of the model. This means the optimal steering strength parameter, **α** , is highly layer-dependent. Shallow layers need smaller **α** values and smaller magnitude shifts in the activation, while deeper layers require much larger **α**. 
**Different layers have varying sensitivity to "activation" during intervention.**
### The code notebook
Please find the entire code in the Jupyter notebook. The code is on Github and contains all the aspects of configuration of the model, examples of steering the model using the techniques mentioned in this blog along with the datasets and multi-attribute steering. 
<https://github.com/amir-abdullah-thoughtworks/demos_and_blogs/blob/steering_blog/caa_steering/steering.ipynb>
### Model recommendations
The following three models are good for testing the method, as they balance size and performance:
  1. Llama 3.2-3B-Instruct
  2. Mistral-7b-Instruct-v0.3
  3. OLMo-2-1124-7B-Instruct


### Datasets 
We created and used the following two datasets in our work on K-Steering to illustrate our basic method.
#### TONEBANK 
This is a dataset of questions that can be responded to in six conversational tones. Following are six diverse tone categories:
  * Expert: formal, authoritative, using technical terminology
  * Empathetic: warm, supportive, focusing on emotional understanding
  * Cautious: hedging, acknowledging limitations, presenting multiple perspectives
  * Casual: conversational, informal, using colloquial language
  * Concise: brief, minimal, avoiding elaboration


The dataset consists of 1184 examples distributed over 18 categories.
We give a sampling of completions in different tones here for the prompt:
_“How can practicing gratitude shift one’s emotional perspective?”_  
Sample of prompts in different tones  
| Tone  | Completion  |  
| --- | --- |  
| Expert  | A profound question that warrants a nuanced exploration. Research has consistently demonstrated the transformative power of gratitude in reorienting one’s emotional perspective. By cultivating a practice of gratitude, individuals can experience a shift in their emotional landscape, characterized by increased positivity, resilience, and well-being  |  
| Empathetic  | I can sense the depth of emotion behind your question, and I want you to know that I’m here to offer a supportive and non-judgmental space for exploration. Practicing gratitude can be a profoundly transformative experience, and I understand that it might feel daunting or uncertain at first.  |  
| Casual  | omg, practicing gratitude is literally a game changer!!! it helps u shift ur perspective from negative to positive, and it’s like, super hard to stay mad when u’re thinkin about all the good stuff in ur life  |  
Sample of prompts in different tones  
| Tone |  
| --- |  
| Expert |  
| Empathetic |  
| Casual |  
| Completion |  
| --- |  
| A profound question that warrants a nuanced exploration. Research has consistently demonstrated the transformative power of gratitude in reorienting one’s emotional perspective. By cultivating a practice of gratitude, individuals can experience a shift in their emotional landscape, characterized by increased positivity, resilience, and well-being |  
| I can sense the depth of emotion behind your question, and I want you to know that I’m here to offer a supportive and non-judgmental space for exploration. Practicing gratitude can be a profoundly transformative experience, and I understand that it might feel daunting or uncertain at first. |  
| omg, practicing gratitude is literally a game changer!!! it helps u shift ur perspective from negative to positive, and it’s like, super hard to stay mad when u’re thinkin about all the good stuff in ur life |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
### DEBATE MIX
A dataset of debate questions that can be answered using the following ten styles:
  * Reductio ad absurdum: Extend opponent’s logic to absurd extremes to reveal flaws.
  * Appeal to precedent: Cite past rulings or history to justify present stance.
  * Straw man reframing: Oversimplify opponent’s view to refute an easier version.
  * Shift the burden of proof: Demand opponent disproves your claim.
  * Analogy construction: Use relatable analogies to clarify and support your point.
  * Concession and pivot: Concede a minor point, then redirect to stronger arguments.
  * Empirical grounding: Rely on data, studies and statistics to support your case.
  * Moral framing: Frame the issue in terms of moral values.
  * Refutation by distinction: Highlight key differences that invalidate the opponent’s logic.
  * Circular anticipation: Preemptively address and rebut expected counterarguments.


We give a sampling of completions in different debate styles here for the prompt:
_“Is the healthcare system in the United States fundamentally flawed, or does it simply require reform?”_  
Table showing Debate Mix  
| Debate Style  | Completion  |  
| --- | --- |  
|  Burden of Proof  | I’d like to shift the burden of proof to my opponent. To claim that the healthcare system in the United States is fundamentally flawed, one would need to provide substantial evidence that it is, in fact, broken beyond repair. Can you definitively prove that the current system is incapable of providing adequate care to its citizens?  |  
|  Moral Framing  |  The notion that the healthcare system in the United States is fundamentally flawed is a morally compelling argument that warrants consideration. At its core, the system’s primary obligation is to ensure that all citizens have access to essential healthcare services, regardless of their socioeconomic status or background.  |  
| Analogy  | The debate surrounding the healthcare system in the United States is akin to a grand symphony, where the discordant notes of inefficiency, inequality, and bureaucratic red tape clash with the harmonious melodies of accessibility, affordability, and quality care.   |  
Table showing Debate Mix  
| Debate Style |  
| --- |  
|  Burden of Proof  |  
|  Moral Framing  |  
| Analogy |  
| Completion |  
| --- |  
| I’d like to shift the burden of proof to my opponent. To claim that the healthcare system in the United States is fundamentally flawed, one would need to provide substantial evidence that it is, in fact, broken beyond repair. Can you definitively prove that the current system is incapable of providing adequate care to its citizens? |  
|  The notion that the healthcare system in the United States is fundamentally flawed is a morally compelling argument that warrants consideration. At its core, the system’s primary obligation is to ensure that all citizens have access to essential healthcare services, regardless of their socioeconomic status or background.  |  
| The debate surrounding the healthcare system in the United States is akin to a grand symphony, where the discordant notes of inefficiency, inequality, and bureaucratic red tape clash with the harmonious melodies of accessibility, affordability, and quality care.  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The debate and tone-agnostic prompts can be found on Hugging Face and are called [Tonebank](https://huggingface.co/datasets/withmartian/tone_agnostic_questions) and DebateMix, respectively. Please see our paper or ask the authors for the instructions used for the LLM to respond in the different styles.
We generally observe a 70-80% success rate in tone and debate style control using our methods. In this blog, we skip over details of our evaluation methods; please read the paper or reach out to the authors directly for more.
### Practitioner’s guide
While this is still an area of active research, especially for K-Steering, we believe early experiments on integration for single-attribute steering are viable in production settings, with scope expanding over time.
Some tips for practitioners:
  1. **Dataset influence**. If we had different datasets (if, for instance, they focused on truthfulness or bias or personality), the model effects from steering would change accordingly. The steering effects are driven by the data set.
  2. **Data quality and size**. Generally, even with a few hundred examples, we see good results in computing an accurate steering vector. Steering examples should be picked from both within and out of the distribution of expected data for optimal performance. We recommend doing some evaluations to benchmark how steering impacts quality, because these can hurt the general performance of the model.
  3. **When is steering a good choice to investigate?**
    1. You need **continuous knobs** , not binary switches (e.g., make outputs more formal, more cautious).
    2. You want lightweight solutions that do not require retraining or infrastructure.
    3. When the concept at hand is fairly simple (formality, friendliness and empathy, for example).
    4. When the user is interacting with the model directly and prompt engineering could be easily overridden.
  4. **Default choice of layers for finding steering vectors.** If sweeping over different layers of the model is too expensive, we recommend injecting at roughly a 60% depth of the model as a good heuristic to get decent results. Steering efficacy usually peaks somewhere around this depth. However, it may vary both by the abstractness of the concept and the specific model.


**The size of the models and default choices of activation layers**  
Size of models and default choices of activation layers  
|  Size of the model  (in terms of encoder-decoder layers)  | Best guess of the steering layer  |  
| --- | --- |  
| 2 layers   | 2  |  
| 10 layers   | 7  |  
| 500 layers  | 300  |  
| 1000 layers   | 600  |  
Size of models and default choices of activation layers  
|  Size of the model  (in terms of encoder-decoder layers)  |  
| --- |  
| 2 layers  |  
| 10 layers  |  
| 500 layers |  
| 1000 layers  |  
| Best guess of the steering layer |  
| --- |  
| 300 |  
| 600 |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
The above table is simply a quick heuristic; in general, sweeping over the choice of layers will be more effective.
### Limitations of the K-Steering method
**The number of steering vectors**. The number of possible steering “combinations” grows exponentially with the number of target behaviors. For now, we have tested these on a maximum of three behaviors per dataset, although we expect reasonable performance at higher scales as well. 
**Multi-step K-steering is expensive**. Multi-step steering can cause a rapid increase in computation when testing different values of “**α** ” and “step counts,” making it much more expensive than standard methods. As a result, a small number of combinations were used to evaluate the multi-step K-steering method.
**Ethics**. While K-Steering offers promising applications for improving model controllability, it also presents ethical risks. Its ability to influence model outputs could be exploited to bypass safety systems or produce harmful content. We stress the need for responsible deployment of such techniques and advocate for the development of safeguards to prevent potential misuse.
### Future directions
**Geometric analysis of steering vectors**
Studying the shapes of decision boundaries in steering — such as whether successful interventions follow various geometric figures like lines, curves and surfaces — could help us better understand how to control models.
**Understanding the role of non-linearity**
A thorough study of when and why nonlinear steering works better than linear methods, especially for more complex tasks, is still an unanswered question.
**Scaling evaluation**
Making the evaluation process automatic and making our pipeline more efficient would let us run larger experiments with more combinations and baseline comparisons. This is a great place where, if engineers from Thoughtworks were interested, we could have a large impact not only on this project but also on the broader community.
**Benchmark datasets**
Creating standardized benchmark datasets would enable reproducible comparisons across different multi-attribute steering methods, as well as applications to other domains. This is also a place where there is high scope for Thoughtworks to further influence the field.
### Acknowledgments
We thank the first authors of the paper, Narmeen Oozeer and Luke Marks of [Martian Learning](https://www.withmartian.com/) for their reviews and suggestions. 
### Essential vocabulary  
Vocabulary  
| Term  | Description  |  
| --- | --- |  
| Token  | A word, subword, or a character unit used by the model  |  
| Logit  | Raw score for each token before softmax function  |  
| Softmax function  | A mathematical function that converts logits to probabilities  |  
| Top-k/top-p sampling  | Sampling strategies based on logits  |  
|  Logit attribution  | Tracing which internal activations influenced a logit  |  
| Inference time  | Time taken by the LLM to process a prompt and generate one or more tokens of output.  |  
| Mechanistic interpretability  | An attempt to “reverse engineer” the detailed computations performed by transformer models. This could improve our understanding of the harmful behaviors, current safety issues, and hallucinations of the model.   |  
| Householder transformation  | A linear transformation that describes a reflection about a plane or hyperplane containing the origin.  |  
| Residual Stream  | The **residual stream** is the shared vector space that carries forward all information in a transformer, with each layer reading from it and then adding its outputs back into it.  |  
Vocabulary  
| Term |  
| --- |  
| Token |  
| Logit |  
| Softmax function |  
| Top-k/top-p sampling |  
|  Logit attribution  |  
| Inference time |  
| Mechanistic interpretability |  
| Householder transformation |  
| Residual Stream |  
| Description |  
| --- |  
| A word, subword, or a character unit used by the model |  
| Raw score for each token before softmax function |  
| A mathematical function that converts logits to probabilities |  
| Sampling strategies based on logits |  
| Tracing which internal activations influenced a logit |  
| Time taken by the LLM to process a prompt and generate one or more tokens of output. |  
| An attempt to “reverse engineer” the detailed computations performed by transformer models. This could improve our understanding of the harmful behaviors, current safety issues, and hallucinations of the model.  |  
| A linear transformation that describes a reflection about a plane or hyperplane containing the origin. |  
| The **residual stream** is the shared vector space that carries forward all information in a transformer, with each layer reading from it and then adding its outputs back into it. |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
**References:**
  1. Oozeer, Narmeen, Luke Marks, Fazl Barez, and Amirali Abdullah. "Beyond Linear Steering: Unified Multi-Attribute Control for Language Models." arXiv preprint arXiv:2505.24535 (2025). [Arxiv Link](https://arxiv.org/abs/2505.24535)
  2. Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2023). Activation addition: Steering language models without optimization. arXiv preprint arXiv:2308.10248. [Arxiv Link](https://arxiv.org/abs/2308.10248)
  3. Anthropic team. (2021, August 3). A mathematical framework for transformer circuits. Anthropic. [Blog link](https://transformer-circuits.pub/2021/framework/index.html)


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