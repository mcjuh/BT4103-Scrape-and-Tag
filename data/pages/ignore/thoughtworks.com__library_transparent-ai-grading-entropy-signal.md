<!-- Source: https://research.thoughtworks.com/library/transparent-ai-grading-entropy-signal | Title: Towards transparent AI grading: Entropy as a signal for human-AI disagreement | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Towards transparent AI grading: Entropy as a signal for human-AI disagreement
By 
Prasanna Pendse
Published: August 06, 2025 
Automated grading systems can efficiently score short-answer responses, yet they often fail to indicate when a grading decision is uncertain or potentially contentious. We introduce semantic entropy, a measure of variability across multiple GPT-4-generated explanations for the same student response, as a proxy for human grader disagreement. By clustering rationales via entailment-based similarity and computing entropy over these clusters, we quantify the diversity of justifications without relying on final output scores. We address three research questions: (1) Does semantic entropy align with human grader disagreement? (2) Does it generalize across academic subjects? (3) Is it sensitive to structural task features such as source dependency? Experiments on the ASAP-SAS dataset show that semantic entropy correlates with rater disagreement, varies meaningfully across subjects, and increases in tasks requiring interpretive reasoning. Our findings position semantic entropy as an interpretable uncertainty signal that supports more transparent and trustworthy AI-assisted grading workflows.
**Read the full research paper here:** [arXiv](https://arxiv.org/pdf/2508.04105)