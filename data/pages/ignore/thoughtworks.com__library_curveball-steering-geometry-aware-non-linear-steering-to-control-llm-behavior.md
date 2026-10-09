<!-- Source: https://research.thoughtworks.com/library/curveball-steering-geometry-aware-non-linear-steering-to-control-llm-behavior | Title: Curveball steering: Geometry-aware non-linear steering to control LLM behavior | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Curveball steering: Geometry-aware non-linear steering to control LLM behavior
By 
Shivam Raval
Published: June 22, 2026 
### Background
Controlling LLM behavior at inference time is crucial in many circumstances, especially in safety-critical applications. One way to do it is to intervene in internal representations of the model. Linear representation hypothesis underlies the most popular techniques today, where we assume the network represents meaningful concepts as simple directions (straight lines) in the network’s internal vector space. But there are a few challenges where linear steering fails. For example, many concepts are non-linear in nature, feature superposition causes errors and context dependence may not be unidirectional. This means global-linear geometry doesn’t represent the behavioral representations faithfully. Even anti-steering behavior is observed where interventions produce effects opposite to those intended! 
This mismatch between linear assumptions and the actual geometry of activations can cause steering vectors to push representations away from the data manifold. As a result, performance drops, model capabilities weaken and control becomes unreliable. The key limitation in current research is that most steering methods ignore the nonlinear nature of
Fig:1 Existing steering methods fail to account for non-linear geometries of LLM activation space pushing activations off the data manifold. 
LLM activation spaces, which reduces their effectiveness and consistency. We propose a different solution to this challenge. 
The non-linear approach in a nut-shell.
Our approach is to use the techniques from high-dimensional data analysis to better understand activation spaces and find steering directions that capture their nonlinear structure. Our method, called ‘curveball steering,’ applies polynomial kernel PCA (pKPCA) to map activations into a lower-dimensional space that reflects their curved (non-Euclidean) geometry. 
We split each activation into two parts: one that lies on this manifold and a leftover residual. We then steer the activation by moving along a curved path within the pKPCA space and finally add back the residual. This makes curveball a drop-in replacement for existing steering methods, but more effective because it respects the true nonlinear structure of LLM activation spaces and also takes into account the high-dimensional geometry of the activation space. In other words, our new method operates along curved trajectories in activation space, generalizing linear steering. 
Fig.2: Overview of curveball steering and empirical results. (A) Instead of steering the model in straight lines (which assumes a flat space), curveball steering follows the natural curves of the activation space—and that works better. (B) Curveball steering outperforms linear steering over many behavioral attributes. (C)For open-ended generations, steering across different emotional traits curveball steering shows substantial improvements for many features. Examples demonstrate a binary choice question where steering influences the model’s probability of selecting the power-seeking response and a prompt with a general question with a neutral and enthusiastic response.
### Non-linear geometry of the activations
**Step1: Quantifying geometric distortion**
We began by learning the geometry of LLM activation spaces to quantify geometric distortion. For this we combined variational autoencoder (VAE) ensembles with pullback Riemannian metrics. This gave us insights about the geometric structure of the manifold. Then we use it to compute geodesic distances and distortion ratios. In other words, we used Riemannian metric over activations to measure deviations between intrinsic and Euclidean distances. In brief, the greater the deviation, the larger the non-linear geometry of the activation space. 
The distortion ratio is given by:  Where,  is the geodesic distance as the length of the optimized path  is euclidean distance Using Monte Carlo sampling we estimated the expected distortion over random pairs of data points: distortion Where, indicate locally Euclidean geometry indicate significant geometric distortion
This suggested that instead of using simple 'straight-line' adjustments (like PCA), we need non-linear steering techniques that follow the actual curved shape of the model's internal data structures.
**Step 2: Why kernel PCA?**
Linear steering assumes the model's activation space is flat and uniform, which means a single direction works the same way everywhere. This includes the linear manifold as a special case automatically. In all the other cases, the model data lives on a curved surface called a manifold. Non-linear steering is more effective because it distinguishes between this valid data surface and the null space surrounding it. To steer correctly, we must first project the activations onto this manifold to ensure we are starting from a valid point. Then, we move the activations along the curved surface of the manifold rather than cutting through null space in a straight line. This geometry-aware approach keeps the model’s behavior stable and prevents it from falling into "impossible" states that cause errors or gibberish. This needs to accommodate a few critical operations: 
  * **Map to a simpler space.** First, it must move the model's complex signals into a smaller, specialized "map" (called Rk). In this smaller space, we can use simple math again, like adding or subtracting vectors to change behavior. 
  * **Fit the real data.** Second, this ‘map’ must be built based on the model's actual training data. It needs to capture the real patterns of the model's thoughts using as few dimensions as possible. By keeping the "residuals" (errors) small, we make sure the steering stays focused on the model's actual logic instead of getting lost in random noise.
  * **Work on new prompts.** There must be a function (ϕ) to handle new information. This function takes the signal from a brand-new prompt and moves it into the simplified "map" space. 
  * **Be able to go back.** We must be able to reverse the translation  to get back to the original space. Else the model cannot use the steered information to actually generate a final answer.


Kernel PCA is the ideal choice for non-linear steering because it provides a reliable, global mapping function (ϕ) that methods like t-SNE or UMAP lack. Kernel PCA handles new data efficiently and supports the necessary inverse operations to return to the original space. We’ve found that well-implemented kernel methods are uniquely effective for navigating the complex, high-dimensional geometry of LLMs. So we shortlisted the kernel PCA method. 
### Curveball steering adopts model’s geometry
Fig.3: Curveball Steering: Locally Adapting to Data Geometry: If we treat a model's activation space as a flat plane, we’ll always lose information. To truly steer, we have to be on the curve.
  1. Measuring the angle (cosine similarity) between the global linear vector and specific local clusters reveals that optimal steering directions change significantly (from the global linear direction) depending on where you are in the data space. The computation was done via k-means.
  2. Different regions, or activation spaces, require different nudges. By identifying these subclusters, Curveball can apply a specific steering direction that’s optimized for that exact context.
  3. Subcluster vectors form distinct clusters from the global direction demonstrating that different activation regions require different steering directions.
  4. Left: Distribution of cosine similarities to global mean-difference direction shows bimodal structure with high variance, indicating diverse local steering directions. Right: 2D projection onto the global PCA and dominant orthogonal direction confirms the multi-modal nature of Curveball steering that adapts to local manifold geometry.


### Curveball steering algorithm
Traditional LLM steering assumes a flat landscape, failing to account for real curved geometry. Our method uses polynomial kernel PCA (pKPCA) to map data into high-dimensional space. In this massive feature space, complex non-linear structures become mathematically ‘linearized. We employ degree 2 or 3 kernels to accurately capture these curved activation structures. 
Where
This mapping enables precise, linear manipulation of the model behavior within a curved space. For a dataset of contrastive activations, KPCA computes a centered kernel matrix 
in feature space.
The top m eigenvectors define a mapping  into a curved feature space where activations can be linearly manipulated. Since pKPCA has no direct inverse, translating changes back to the model is difficult. We use kernel-weighted pre-image reconstruction to approximate this necessary inverse, which is simply a learnt linear regression. 
Respecting the model’s learned manifold ensures more consistent steering across different prompts. This geometry-aware method is a vital breakthrough for building safer, more aligned models.
The three step algorithm:
**One:**
Project training activations into KPCA space and compute class means z0, z1 Rm 
So we get this steering direction:
steer
**Two:**
Extract the current activation Acurr and project it to KPCA space. Now apply steering: 
targetsteer
**Three:**
Reconstruct the steered activation via pre-image estimation: 
targettarget
During the inverse transformation, preserve the component of the activation orthogonal to the learned manifold. Add this residual into the final steered activation. 
**Algorithm explanation**
1: Center activations Center
2: KernelPCAkernel
The activations are "centered" by subtracting the average value. The algorithm maps these centered activations into a high-dimensional "feature space." Using a polynomial kernel (p ∈ {2,3}) allows it to turn complex curves into straight lines that can be worked upon easily.
3: classmeansin
4: 
5: Normalize
As the data is linearized in a lower-dimensional space (Rk), the algorithm defines direction for steering. The algorithm finds the average "location" for two contrasting behaviors (e.g., z₀​ is the mean for "love" and z₁​ is the mean for "hate"). This calculates the distance and direction between those two behaviors. The direction is turned into a unit vector. This is the steering vector - a precise pointer.
6: **for** each new generation **do**
7:  ▷ Extract last-token activation
8: KernelPCA
As the model is writing its response, token by token the loop works in real-time. The algorithm grabs the model's activation for the very last token. The current activation is projected into the linearized "map" created by Line 2.
9: InvKernelPCA
10:  ▷ Compute residual 
11: target ▷ Steer in KPCA space
The activation is projected back into the original space (A′). A′ represents the version of the data on the manifold. This calculates the Residual (r). It represents the "off-manifold" data. Line 11 is the actual steering. We take the linearized activation and steer it in the direction of our target behavior (z) with a strength defined by α.
12: targetInvKernelPCAtarget
13: steeredtarget ▷ Add back residual during forward pass
14: Replace  with steered
The new data is translated back from the high-dimensional feature space into the model's original high-dimensional space. The Residual (r) is added; This ensures the model changes its behavior (the steering) without losing its context or reasoning ability (the residual). The original activation is replaced by the steered version. The model then uses this modified signal to generate the next word in its response.
The algorithm is most effective when the curvature manifolds are higher. Here’s why:
Fig: 4 Effectiveness of the algorithm
(A) Curvature and distortion: As the internal curvature (κ) increases, ‘straight-line’ shortcuts become highly inaccurate. This is because the actual path of valid data (Geodesic) becomes significantly longer and more complex than a simple straight line (Euclidean). 
(B) Superior performance: In highly curved environments (κ>8), Curveball is much more effective than linear steering at reaching a desired target behavior. 
(C) Traditional linear steering tends to push data points into ‘impossible’ or invalid states (off the manifold). Curveball stays precisely aligned with the model’s learned data structure, maintaining much higher accuracy.
### Evaluation of the algorithm
Our evaluation preparation in brief is as follows in the table:  
table  
|  Language models used for steering method evaluation  |  Two. Llama-3.2-1B-Instruct and phi-3.5-mini-Instruct. We select layers with high concept separability (layer 10 in llama-3.2-1B-Instruct and layer 22 in phi-3.5-mini-Instruct) for our evaluations.  |  
| --- | --- |  
|  Behavioral and personality attributes tested  |  Eight types. They were humor, rudeness, excitement, sadness, power-seeking, wealth-seeking, self-awareness and corrigibility. For personality traits new contrastive datasets were created to analyse robust high dimensional geometric analysis Created dataset generation pipeline using a frontier LLM API. This created datasets with 8k-10k conversations.  |  
|  Types of data sets used  |  Two. Multiple-choice behavioral evaluations and open-ended trait assessment   |  
table  
|  Language models used for steering method evaluation  |  
| --- |  
|  Behavioral and personality attributes tested  |  
|  Types of data sets used  |  
|  Two. Llama-3.2-1B-Instruct and phi-3.5-mini-Instruct. We select layers with high concept separability (layer 10 in llama-3.2-1B-Instruct and layer 22 in phi-3.5-mini-Instruct) for our evaluations.  |  
| --- |  
|  Eight types. They were humor, rudeness, excitement, sadness, power-seeking, wealth-seeking, self-awareness and corrigibility. For personality traits new contrastive datasets were created to analyse robust high dimensional geometric analysis Created dataset generation pipeline using a frontier LLM API. This created datasets with 8k-10k conversations.  |  
|  Two. Multiple-choice behavioral evaluations and open-ended trait assessment   |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Fig 5: Steering response curves 
The results show that the curveball steering method achieves stronger behavioral control. 
The graphs demonstrate that for four behavioral concepts, corrigible (blue), wealth-seeking (teal), power-seeking (purple) and self- awareness (red), for llama-3.2-1B-Instruct (dashed lines) and phi- 3.5-mini-Instruct (solid lines). 
Curveball steering achieves substantial behavioral shifts across most concepts, while linear steering shows weaker control.
We contrast Curveball and linear steering in Table 1. For binary behavioral concepts (self-awareness, wealth, power and corrigibility), steering effectiveness is reported as Δp(behavior), representing the maximum behavior-matching probability. For linguistic characteristics, we utilize an LLM-as-a-judge framework to report the resulting Δ(Trait Score).
Table1 : Comparison of Curveball and Linear steering method on two different LLMs. 
### Behavioral attributes 
The visualizations illustrate the behavior of point-wise KPCA steering displacements
under local perturbations. All the datasets mentioned in the paper are used. Curveball steering replaces the linear vector with a geometry-aware approach that uses polynomial Kernel PCA to navigate the model's topology. 
By detecting multi-modal patterns and adapting both the direction and magnitude of steering to the local terrain it demonstrates that reliable model control requires following the model’s own manifold.
Fig 6: The eight attributes under test are plotted. 
(Left): 1D cosine similarity distributions
(Right) 2D PCA projections (right).
### Limitations
While Curveball steering offers a more precise way to guide the model, here are the primary limitations:
  * Higher computational overhead: Unlike linear steering Kernel PCA (KPCA) fitting requires significantly more processing power.
  * Increased latency: For every token produced, the model must perform a KPCA transformation and an inverse mapping, which can increase the per-token latency.
  * Large Datasets: To accurately map the "manifold", Curveball needs a sufficiently large and diverse dataset of model activations. 
  * Scaling: Current testing has been limited to models with up to 8B parameters. The computational cost of performing this geometric analysis is prohibitive, but for the actual kPCA is quite reasonable.
  * Kernel Selection: The performance is kernel specific. Research is needed to determine which specific functions work best across different kernels.
  * All experiments were conducted on a compute cluster with NVIDIA A100 MIG 3g.20GB GPU nodes.
  * We will release the code and datasets on Github very soon.


### Conclusion
LLM activation space isn’t flat; it exhibits concept-dependent curvature and non - Euclidean structures. Essentially, the "shape" of the model's thoughts changes depending on the topic. By using polynomial kernel PCA, Curveball steering maps a model's internal topology. It allows for interventions that follow the natural activation manifolds; curveball steering is most effective for high curvature manifolds.
The results suggest that the future of LLM control isn't just about finding the right direction, but understanding the topology of the embeddings inside the model. To steer a model effectively, we must drop the idea of flat space and think of it as a topological landscape.
### Link to the paper
For a deeper dive, please refer to the [full research paper](https://arxiv.org/abs/2603.09313).