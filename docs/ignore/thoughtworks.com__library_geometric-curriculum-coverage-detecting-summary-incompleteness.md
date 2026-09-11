<!-- Source: https://research.thoughtworks.com/library/geometric-curriculum-coverage-detecting-summary-incompleteness | Title: Geometric curriculum coverage for detecting summary incompleteness via Hausdorff distance | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Geometric curriculum coverage for detecting summary incompleteness via Hausdorff distance
By 
Published: June 27, 2026 
Evaluating whether automatically generated summaries preserve all essential concepts from source material is a critical challenge for educational AI systems. Existing metrics measure average semantic similarity, which fails when a summary correctly covers most content but omits a small number of critical concepts – the well-covered majority drowns out the missing minority. 
We reframe this as a _geometric curriculum coverage problem_ and propose Robust Semantic Hausdorff Distance (RSHD), which adapts directed Hausdorff distance from computer vision to measure whether every source concept has a nearby summary counterpart. A key finding is that incompleteness detection requires navigating a _sensitivity-robustness tradeoff_ : classical Hausdorff is maximally sensitive but fragile to noise; mean residual is robust but blind to omissions; partial directed Hausdorff strikes the sweet spot between them. 
Experiments on SIGHT and UniSumEval across five encoders show RSHD outperforms all unsupervised baselines, achieving AUC up to 0.763 on SIGHT and 0.887 on UniSumEval.
**Read the r[esearch paper on Springer Nature [paywalled]](https://link.springer.com/chapter/10.1007/978-3-032-29788-4_8).**