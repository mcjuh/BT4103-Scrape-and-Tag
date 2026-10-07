<!-- Source: https://research.thoughtworks.com/library/rethinking-skeleton-based-action-recognition-action-class-prediction-distribution | Title: Rethinking skeleton-based action recognition from an action-class prediction distribution perspective | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Rethinking skeleton-based action recognition from an action-class prediction distribution perspective
By 
Yingying Jiao , 
Haipeng Chen , 
Yingda Lyu , 
Yuheng Yang and
Zhenguang Liu
Published: April 01, 2026 
Action recognition has long been a fundamental and compelling problem in the field of computer vision. However, one aspect that has been overlooked so far is that current action recognition approaches often produce an unfavourable multi-peaked distribution when identifying the action class of a given motion sequence, which is ambiguous and hard to learn for neural networks. Moreover, current methods heavily rely on neural networks to extract action features for differentiating actions, lacking theoretical constraints ensuring that action-specific features are selectively extracted and ambiguous features common to multiple actions are effectively reduced. These shortcomings culminate in inadequate action recognition accuracy.
Motivated by this, in this paper we seek to tackle the problem from three aspects: 1) We try to eliminate ambiguity by enforcing a smooth single-peaked distribution instead of a multi-peaked one for action-class prediction. 2) We theoretically analyze the lower bound of the label prediction log-likelihood and derive a training objective, which focuses on the extraction of action-specific features and the reduction of ambiguous features. 3) We further advocate feeding the model with richer information, including positive information like body-part structures and negative information like masked inputs. Empirically, our approach sets the new state-of-the-art performance on five large-scale benchmarks. 
**Read this[research paper on IEEE Xplore](https://ieeexplore.ieee.org/document/11466462) [paywalled].**
**You can find the[code for this project on GitHub](https://github.com/ActionR-Group/DPM).**