<!-- Source: https://research.thoughtworks.com/library/semantic-flow-refinement-recognizing-low-legibility-handwritten-answers | Title: Semantic flow refinement for recognizing low-legibility handwritten answers | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Semantic flow refinement for recognizing low-legibility handwritten answers
By 
[Manikandan Ravikiran](https://research.thoughtworks.com/team#manikandan-ravikiran) and
Rohit Saluja
Published: June 27, 2026 
Transformer-based handwritten text recognition (HTR) systems decode text in a single left-to-right pass while keeping visual encoder representations fixed, preventing later contextual evidence from resolving earlier visual ambiguities. We propose Semantic Flow Refinement (SFR), a lightweight two-pass decoding framework that interprets decoder hidden states from an initial pass as a _semantic flow_ and uses them to refine visual tokens via cross-attention before final decoding. Building on a TrOCR baseline augmented with stroke-direction supervision, SFR introduces no additional training data or encoder modifications. On a low-legibility student handwriting benchmark, SFR achieves CER = 1.19% with TrOCR-Base – surpassing the previous best result of 1.69% CER obtained with TrOCR-Large – demonstrating that contextual refinement can substitute for model scale in challenging HTR settings.
You can read the full article here (paywalled): [Springer](https://link.springer.com/chapter/10.1007/978-3-032-29788-4_9)