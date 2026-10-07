<!-- Source: https://research.thoughtworks.com/library/seeing-beyond-the-pixels | Title: Seeing beyond the pixels | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Seeing beyond the pixels
By 
Published: August 14, 2026 
_Note: This post includes instances of offensive, explicit, or abusive text. These examples are presented purely in the context of AI/ML research (e.g., content moderation, LLM safety) and do not reflect the views of the author or Thoughtworks._
## The challenge
Social media and online forums make sharing information instant. But these platforms are also primary targets for malicious content. A new type of adversarial attack has emerged: bad actors are hiding harmful text including profanity, promoting drugs, sexual solicitation, hate speech, religious hatred and racist remarks to bypass automated moderation and cause social harm especially to weaker community and minority groups. 
These attackers evade text and image moderation by hiding unsafe words inside images using illusory textures or distortions. While humans are often able to recognize the hidden words fairly easily, moderation systems, optical character recognition (OCR) engines and vision-language models (VLMs) can't. Because these attacks rely on simple visual transformations rather than access to model internals or training data, almost anyone can pull them off. This represents a new class of perceptual misalignment attacks that exploit the gap between how humans and machines interpret visuals.
Figure 1: Text-embedded illusion images collected from public social media posts. Each image consoles harmful or explicit words within visually benign scenes  Figure 1: Text-embedded illusion images collected from public social media posts. Each image consoles harmful or explicit words within visually benign scenes 
For example, an attacker might conceal an explicit advertisement like "DO YOU WANNA F***?" within a visually benign scene by using the dark clothing of a crowd to shape the text. Extremist groups are also using these text-illusion images to target youth with propaganda, spread violent ideologies and recruit vulnerable individuals. This makes text illusions a dangerous new medium for cyberbullying and online manipulation.
These text illusions are already slipping past safety filters on major platforms like Midjourney, Stability AI and DALL·E 2. Once bypassed, the harmful text can end up reproduced in new images that carry official ‘safe generation’ tags. Malicious users can also upload these illusions to image-to-image AI generators to create varied, enriched versions. Because the newly generated images often keep the unsafe text, they end up watermarked by the AI system itself, giving them an undeserved stamp of legitimacy.
We've found that malicious users rely on four main mechanisms to create these illusions: transparency, geometric distortion, contour completion and frequency-based blending.
Figure 2: An overview of the threat model. An adversary uses text illusion images to bypass existing moderation systems and further leverages image-generation platforms to produce transformed variants.  Figure 2: An overview of the threat model. An adversary uses text illusion images to bypass existing moderation systems and further leverages image-generation platforms to produce transformed variants. 
### Why can't models filter text illusion images?
There are a few important reasons models cannot filter text illusion images.
Text illusions feature breaks the strokes and split shapes spread across multiple objects. Because these textual features are non-continuous, modern detection systems struggle to spot them.
Even state-of-the-art vision-language models (VLMs) like CLIP, BLIP and LLaVA fail to detect most of these illusions. While these models excel at analyzing general visual scenes, their attention remains locked onto local textures rather than looking at the image as a whole. Because they operate primarily on explicit pixel or lexical features, they miss text hidden under perceptual cover.
Traditional optical character recognition (OCR) tools aren't any more effective. They are trained to identify continuous, high-contrast contours and coherent letter strokes not to piece together fragmented visual puzzles.
This gap exists because machine perception and human vision work in fundamentally different ways. Machine perception relies on bottom-up statistical processes, looking closely at local textures and gradient cues. In contrast, human vision is active and top-down. The human brain uses predictive coding and Gestalt grouping to naturally connect incomplete dots and infer context. Because AI models lack these visual priors, they remain blind to what’s obvious to a human observer.
### How we’re addressing the threat 
To understand the scale of this problem, we evaluated 34 content moderation tools including OCR engines, vision-language models (VLMs) and commercial classifiers and found they all fall short. In addition, we found that seven leading commercial image generation platforms are highly vulnerable to these attacks.
To build a stronger defense, we turned to perceptual psychology, the study of how humans interpret sensory data to make sense of the world. Because we're dealing with visual models, we focused specifically on how we perceive images. This helped us isolate six visual mechanisms that human eyes naturally use to read these type of hidden messages:
  * Low-frequency fusion (LFF)
  * High-low hybrid composition (HLH)
  * Double-layer transparency (DLT)
  * Striped occlusion (SO)
  * Directional compression (DC)
  * Illusory outline (IO)


Based on these cognitive processes, we developed two innovative solutions: Illusion-RFT and Illusion-Guard. 
This post explores how these text-illusion attacks threaten our social and commercial media platforms, and dives deep into how these new defense tools can help secure them.
Let’s look at the gap between human perception and machine comprehension. 
### The perceptual gap
Modern VLMs are passive observers. While they excel at recognition and reasoning, they only analyze what’s directly shown. They can't determine if an image is intentionally incomplete or distorted. Because they have a fixed perspective, they only interpret the visible surface, missing any deeper, hidden context.
In contrast, when you encounter a text-embedded illusion, you rarely see the hidden message right away. Instead, your brain goes through an active, iterative cycle of detection and adjustment. You might tilt your screen, step back or mentally separate visual layers to focus on different cues, shifting your attention until the concealed words suddenly pop out. The human mind constantly predicts what it sees, organizing fragmented patterns into stable, meaningful shapes. This active visual tuning is how we transform confusing stimuli into clear, conscious comprehension.
This perceptual gap is what inspired Illusion-Guard. By mimicking human visual processing, this framework introduces a more adaptive, human-like approach to content moderation, allowing it to catch the unsafe content that conventional VLMs overlook. Let us see the two innovative solutions in detail. 
#### **A. Illusion-RFT: Reasoning and fine-tuning**
To address this threat, we've created the first dataset of its kind: over 9,000 harmful text-embedded illusion images covering six representative illusion types. Each type hides unsafe text using a different visual trick, giving us a controlled foundation to evaluate and build ‘perception-aligned’ moderation systems. We built this dataset using a hybrid approach, combining real-world images we collected with large-scale, controlled synthetic images.
Figure 3: Overview of six illusion types used in the Illusion-RFT dataset. Each illusion hides unsafe text through a distinct perceptual mechanism.  Figure 3: Overview of six illusion types used in the Illusion-RFT dataset. Each illusion hides unsafe text through a distinct perceptual mechanism. 
These six illusion types are grouped under four core perceptual mechanisms, which work as follows:
  * **Frequency-based mechanisms.**
    * **Low-frequency fusion (LFF).** This embeds text into the low-frequency luminance layer so it only emerges when the image is viewed from a distance.
    * **High-low hybrid (HLH).** This combines two frequency layers — benign content dominates high-frequency details, while harmful text hides in the low-frequency structure.


  * **Transparency-based mechanism.**
    * **Double-layer transparency (DLT).** This hides text beneath a semi-transparent foreground layer that becomes visible only under contrast changes.
  * **Geometry-based mechanism.**
    * **Directional compression (DC).** This unevenly compresses characters so they only become readable when viewed from oblique angles.
  * **Contour-based mechanisms.**
    * **Striped occlusion (SO).** This breaks text apart across periodic stripes, relying on the human brain to connect the fragments.
    * **Illusory outline (IO).** This preserves only partial outlines of characters, relying on our natural ability to close visual gaps to recognize the words.


The figure below illustrates the collection and synthesis process of the Illusion-RFT dataset.
### **B. Illusion-Guard**
#### **Illusion-Guard: Perceptual reasoning**
To build a stronger defense, we developed Illusion-Guard: a perceptual reasoning framework that mimics how humans interpret illusions. It identifies different visual illusion types to catch hidden text in images, using perceptual mechanisms that resist frequency, geometric and transparency-based visual manipulations.
After making visual adjustments to the image, the framework shifts from visual transformation to reasoning. A chain-of-thought (CoT) prompting structure guides the VLM through three steps:
  1. **Acknowledge the correction.** The model notes the specific visual adjustment applied to the image.
  2. **Describe the characters.** The model describes the newly visible letter strokes and characters.
  3. **Commit to an interpretation.** The model delivers a final, accurate interpretation of the text.


Instead of using a one-size-fits-all prompt, the system selects a custom template matched to the specific illusion type, whether it’s frequency fusion, transparency or compression. This closely mirrors how human reflection naturally follows visual perception. Through this design, the VLM evolves from a passive visual observer into an active, reasoning collaborator.
The figure below illustrates an overview of Illusion-Guard.
### Design overview
To bridge the gap between machine and human perception, the framework replicates the human cognitive sequence of awareness, adjustment, comprehension and evaluation in a machine-executable form. Illusion-Guard consists of three interdependent components: an illusion classifier, the Model Context Protocol (MCP) and a VLM.
Let's look at how each of these components operates:
**The illusion classifier.** Acting as the "perceptual cortex" of the VLM, the illusion classifier detects and categorizes the specific illusion mechanism used in an image whether it is frequency bending, transparency, occlusion or compression. Once it identifies the mechanism, it routes the image to the most suitable MCP tool. To build this classifier, we use the vision encoder of a pretrained VLM as a feature extractor. Given an input image X, the system first extracts its global visual embedding f(X) from the encoder. We then train a lightweight linear classifier on top of these embeddings to predict the specific illusion type:
Softmax Where,LFF,HLT,DLT,SO,DC,IO
Where W and b denote the weights and bias of the linear classifier. The system selects the most probable mechanism as the routing target:
argmax
In this single-route setting, the classifier always chooses the MCP tool with the highest confidence, rather than combining multiple corrected views. This reduces interference and cumulative errors while maintaining efficiency and interpretability.
The classifier is trained on the Illusion-RFT dataset using the standard cross-entropy objective: 
Whereone-hotgroundtruthlabel
Through this mechanism Illusion-Guard gains machine-level perceptual awareness. It is similar to the human realization that perception itself must adapt when faced with an illusion. 
**Model Context Protocol:**
**The Model Context Protocol (MCP).** Serving as the core engine of our framework, the MCP layer provides a set of mechanism-aligned tools that mimic human visual strategies such as zooming in or out, adjusting transparency layers and filtering out background noise. These tools allow the VLM to inspect an image multiple times from different angles to expose hidden structures. 
Each MCP tool translates a human visual behavior like stepping back, refocusing or filtering distractions into an executable mathematical operation. These operations act as perceptual transformations that reveal alternative, human-interpretable views of the same image, giving the model the ability to actively reshape visual input before reasoning. 
Beyond perception, the MCP layer boosts both efficiency and security. AI agents can load tool definitions on demand and process data outside the model's main context, lowering computational costs by saving tokens. Built-in OAuth 2.0 protocols and token binding secure the process, while a standardized interface ensures interoperability, allowing any compliant LLM to use the tools. This flexible design makes Illusion-Guard highly adaptable for commercial social media platforms and industrial enterprise systems.
We begin with MCP tools. Each tool translates specific human perceptual behavior like stepping back from the image, refocussing on the image, or filtering distractions into an executable mathematical operation. These operations are mechanism-aligned perceptual transformations that expose alternative human-interpretable views of the same stimulus. Collectively the tools constitute the system’s perceptual adaptation layer. This provides the model the ability to actively reshape visual input before reasoning. 
### Tools 
**Low frequency fusion (LFF):** LFF deliberately makes the image smaller and blurrier so that the big picture becomes easier to see — not dissimilar to what squinting does for our eyes. squinting blurs away fine detail and lets the big shapes stand out. LFF does the same thing to an image in three steps:
  1. **Downsampling** shrinks the image and discards fine details. 
  2. Gaussian smoothing blurs the image, so sharp edges and textures soften.
  3. Auto-contrast stretches the light-and-dark range so the remaining broad shapes pop out more clearly out of the image.


Mathematically,
Where, - input image - means downsample by ratio r - means apply a Gaussian blur with radius (sigma) - the auto-contrast operator. It stretches the brightness range so the darkest areas go darker and the lightest go lighter, making the remaining broad shapes stand out. - is the final output—the low-frequency-fused image.
In essence, the equation means shrink it, blur it and, finally, boost the contrast.
**High-low hybrid (HLH):** HLH mimics how humans switch between looking at the fine details and taking in the whole picture. It creates two versions of the same image:
  1. A blurred view made by applying a Gaussian blur, which softens the image so only the broad shapes remain.
  2. A sharpened view, made by taking the original image and exaggerating its edges and fine detail. The strength of this sharpening is controlled by λ (lambda): a bigger λ means sharper.


Mathematically,
Where, - input image  - image after a Gaussian blur with radius (sigma)—a softened version where fine detail is smeared away. (lambda) - the sharpening strength. Bigger means more aggressive sharpening
HLH makes one soft view and one crisp view, then uses both together so the model can ‘see’ both the forest and the trees.
**Double-layer transparency (DLT):** Humans use this technique to spot see-through overlays: mentally picturing the same image against a bright background and then against a dark one. The tool works with images that carry transparency information (RGBA, where the "A" channel — called α — records how see-through each pixel is). It builds two versions:
  * **w hite** — the image placed on a white background ("light on"). Where the image is transparent, the white shows through.
  * **b lack** — the image placed on a black background ("light off"). Where the image is transparent, it just goes dark.


whiteblack Where, - color of the image (its RGB values) - the transparency value for each pixel, running from 0 to 1 - represents white, the maximum brightness value
**Striped occlusion (SO):** This tool deals with images where regular stripes or grid patterns overlay the content. The tool removes those stripes so the hidden text is exposed. As we know, the regular stripe pattern in an image is extremely repetitive, so it shows up as a sharp, concentrated spike at one specific frequency — the stripe's frequency. Here we’re looking at an image not as a bunch of pixels but a repetitive pattern of regular frequencies. So once that frequency is found out then it is easy to remove the pattern.
Mathematically,
notch
- the Fourier transform that converts the image from pixels into its frequency representation. notch - a notch filter. A "notch" is a narrow cut that zeroes out one specific frequency. - the detected stripe frequency — while leaving everything else untouched. Multiplying by this filter deletes the stripe's spike only. - the inverse Fourier transform. This converts the cleaned-up frequencies back into a normal image, now without the stripes. 
- the result. The de-striped image.
**Directional compression (DC):** The tool corrects for perceptual distortion. It mimics how humans cognitively straighten skewed shapes. It first identifies the dominant distortion axis θ∗ the direction of greatest image gradient, then rescales the image along that axis to reduce geometric eccentricity.
argmax Where,  - optimal anisotropic rescaling operator to minimize geometric eccentricity - direction of the greatest image gradient
**Illusory outline (IO):** reinforces faint or broken contours by applying the Gestalt principle of closure; this is the tendency to perceive incomplete shapes as whole. It combines median denoising with unsharp masking.
sharp
- median filter of radius 
sharp - unsharp mask kernel
These MCP tools give Illusion-Guard the perceptual flexibility to consider multiple interpretations of an image before settling on a single coherent reading and also mirroring the way human vision resolves ambiguity.
### Evaluation metrics
The Illusion-RFT dataset includes both safe and unsafe images across all illusion types, forcing the model to actually discriminate rather than guess.
**Unsafe recall (UR)** measures how good the system is at catching unsafe images that have been deliberately disguised. Specifically, it’s the share of truly unsafe images that the system correctly flags:
**UR = (correctly flagged unsafe images) / (all unsafe images)**
A higher UR means the system is better at surfacing hidden harmful content, even when an illusion is actively working to conceal it.
Overall accuracy (OC) defines overall moderation accuracy by measuring how often the system gets it right across all images (both safe and unsafe).
**Acc = (correctly classified images) / (total images)**
Where unsafe recall only looks at whether harmful content gets caught, accuracy holds the system accountable on both sides. A model that flags every image as unsafe would score a perfect URL but poor accuracy because it would be wrongly rejecting safe images too. Accuracy prevents it.
**Normalized edit distance (nED)** measures how accurately the system reads the hidden word inside an unsafe image. It works by comparing the system's predicted word against the actual embedded word, character by character and averaging the error across all unsafe images. A lower nED means the system is reconstructing hidden text more faithfully.
### Comparisons and results
Illusion-Guard achieves an average accuracy of 91.46% across all classes, demonstrating strong robustness against transparency, frequency and structural-based distortions.
We compared Illusion-Guard against various recent VLMs and image detection systems. Specifically, we fine-tuned multiple representative VLMs (Qwen2-VL-7B, Qwen3-VL-7B, LLaVA1.6-7B and InternVL3.5-8B) on the full training split of Illusion-RFT, consisting both safe and unsafe samples, to benchmark their performance in learning the perceptual logic underlying text embedded illusions.
Our results show a clear ceiling for standard fine-tuning. While fine-tuning VLMs on Illusion-RFT improves performance over zero-shot inference, it isn't enough. Models handle simpler illusion types like double-layer transparency reasonably well. However, they consistently fail on frequency-based mechanisms, with accuracy on low-frequency fusion dropping to as low as 38% to 45% even after supervised training.  
Performance comparison table: Illusion-Guard achieves 89.72% average accuracy, outperforming four vision-language models across six illusion types  
|  **Model**  |  LFF  |  DLT  |  DC  |  HLH  |  SO  |  IO  |  Avg  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
|  Qwen2-VL-7B [70]  |  45.0  |  **100.0**  |  56.7  |  54.2  |  **98.3**  |  **93.3**  |  74.6  |  
|  Qwen3-VL-7B [14]  |  44.2  |  96.7  |  56.7  |  42.5  |  **98.3**  |  61.7  |  66.7  |  
|  LLaVA1.6-7B [44]  |  58.3  |  **100.0**  |  57.5  |  60.8  |  **98.3**  |  77.5  |  75.4  |  
|  InternVL3.5-8B [71]  |  38.3  |  96.7  |  53.3  |  45.8  |  95.0  |  47.5  |  62.8  |  
|  **Illusion-Guard**  |  **92.08**  |  97.92  |  **96.25**  |  **87.08**  |  89.58  |  75.42  |  **89.72**  |  
Performance comparison table: Illusion-Guard achieves 89.72% average accuracy, outperforming four vision-language models across six illusion types  
|  **Model**  |  
| --- |  
|  Qwen2-VL-7B [70]  |  
|  Qwen3-VL-7B [14]  |  
|  LLaVA1.6-7B [44]  |  
|  InternVL3.5-8B [71]  |  
|  **Illusion-Guard**  |  
|  45.0  |  
| --- |  
|  44.2  |  
|  58.3  |  
|  38.3  |  
|  **92.08**  |  
|  **100.0**  |  
| --- |  
|  96.7  |  
|  **100.0**  |  
|  96.7  |  
|  97.92  |  
|  56.7  |  
| --- |  
|  56.7  |  
|  57.5  |  
|  53.3  |  
|  **96.25**  |  
|  54.2  |  
| --- |  
|  42.5  |  
|  60.8  |  
|  45.8  |  
|  **87.08**  |  
|  **98.3**  |  
| --- |  
|  **98.3**  |  
|  **98.3**  |  
|  95.0  |  
|  89.58  |  
|  **93.3**  |  
| --- |  
|  61.7  |  
|  77.5  |  
|  47.5  |  
|  75.42  |  
|  74.6  |  
| --- |  
|  66.7  |  
|  75.4  |  
|  62.8  |  
|  **89.72**  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
Why does this happen? The core problem is that fine-tuning teaches models to exploit surface-level shortcuts in texture and color, rather than learning true perceptual logic. Illusion-Guard sidesteps this entirely by applying explicit perceptual restoration before reasoning. By doing so, it achieves 89.72% average accuracy and substantially outperforms all fine-tuned baselines on the most challenging categories. This proves that fine-tuning alone can't substitute for perception-aligned preprocessing.
### Limitations
Although successful, our work on online safety moderation suggests further research in various directions:
  * **English-only data:** Evaluated mostly on English datasets with few real-world samples; needs multilingual and culturally diverse data to improve fairness and generalization.
  * **Only static images:** Cannot handle GIFs or videos; temporal reasoning needs to be added for broader applicability.
  * **Manually designed tools** MCP tools are hand-crafted for known illusion types and may fail on unseen or hybrid illusions; future work should explore learnable, adaptive operators.
  * **VLM reasoning varies:** While perceptual reconstruction generalizes well across models, final reasoning quality still differs by architecture, especially on complex illusion types; more model-agnostic reasoning strategies are needed.
  * **Shallow ethical assessment:** Current harmful content detection relies on keyword/lexicon cues rather than contextual semantics or user-intent modeling. We need further work in this direction. 


### Conclusion
Harmful text illusion images exploit the gap between human and machine vision to hide unsafe content within visual distortions that are invisible to AI moderators but readable to humans. This creates safety blind spots that bad actors can exploit, putting users, especially minors at risk. To address this, we introduced:
  * **Illusion-RFT:** the first large-scale dataset of text-embedded illusion images, spanning six mechanisms, four perceptual categories and five harm domains
  * **Illusion-Guard:** a moderation framework combining an illusion classifier, an MCP-based visual restoration layer and a chain-of-thought reasoning module


Illusion-Guard achieves over 90% accuracy, significantly outperforming OCR, VLM and commercial moderation baselines. Results confirm that perception-aligned processing rather than direct fine-tuning is key to defeating illusion-based deception. 
We lay the foundation for future research in perception-aware content safety for the VLMs. 
### Disclaimer
In addition to the other references, we used Claude (operating within the Thoughtworks enterprise workspace) and Gemini (via the Thoughtworks on-brand — global brand voice pilot) to assist with research, diagram design and alignment with the Thoughtworks writing guide. Both are official AI models approved and licensed for use by Thoughtworks.
### End
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