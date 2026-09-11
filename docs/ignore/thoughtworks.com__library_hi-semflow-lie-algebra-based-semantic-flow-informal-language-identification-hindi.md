<!-- Source: https://research.thoughtworks.com/library/hi-semflow-lie-algebra-based-semantic-flow-informal-language-identification-hindi | Title: Hi-SEMFLOW: Lie algebra–based semantic flow for span-level informal language identification in Hindi | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Hi-SEMFLOW: Lie algebra–based semantic flow for span-level informal language identification in Hindi
By 
Tanmay Tiwari , 
Vibhu Gupta and
Rohit Saluja
Published: May 16, 2026 
Informal Hindi text frequently contains multi-token slang and idiomatic expressions whose correct identification requires consistent span boundaries. Transformer-based token classifiers, despite strong contextual representations, often produce fragmented or structurally invalid BIO sequences due to largely local predictions.
We propose Hi-SEMFLOW, a Lie algebra–based semantic flow framework that models span consistency as a continuous refinement process over label logits. Instead of discrete structured decoding (e.g., CRFs), Hi-SEMFLOW learns context-dependent transition operators derived from antisymmetric generators and propagates structural information through smooth, fully differentiable transformations. This formulation integrates structural bias directly into end-to-end training without requiring dynamic programming or hard decoding constraints.
Experiments on the HiSlang-4.9k benchmark show that Hi-SEMFLOW improves span-level F1 by up to 2–3 absolute points and yields consistent macro-F1 gains across Hindi-pretrained encoders. Extensive ablations demonstrate that continuous geometric refinement provides a flexible and effective alternative to discrete structured decoding for span-centric sequence labeling.
**Read the[research paper on the ACL Anthology website](https://aclanthology.org/2026.chipsal-1.14/).**