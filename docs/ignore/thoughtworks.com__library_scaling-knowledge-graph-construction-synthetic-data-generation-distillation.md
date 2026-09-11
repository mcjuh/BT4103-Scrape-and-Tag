<!-- Source: https://research.thoughtworks.com/library/scaling-knowledge-graph-construction-synthetic-data-generation-distillation | Title: Scaling knowledge graph construction through synthetic data generation and distillation | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Scaling knowledge graph construction through synthetic data generation and distillation
By 
Prafulla Kumar Choubey , 
Man Luo , 
Xiangyu Peng , 
Caiming Xiong , 
Tiep Le , 
Shachar Rosenman , 
Vasudev Lal , 
Phil Mui , 
Ricky Ho and
Chien-Sheng Wu
Published: October 22, 2024  | Last updated: March 01, 2026
Document-level knowledge graph (KG) construction faces a fundamental scaling challenge: existing methods either rely on expensive large language models (LLMs), making them economically nonviable for large-scale corpora, or employ smaller models that produce incomplete and inconsistent graphs. We find that this limitation stems not from model capabilities but from insufficient training on high-quality document-level KG data. 
To address this gap, we introduce SynthKG, a multi-step data synthesis pipeline that generates high-quality document-KG pairs through systematic chunking, decontextualization, and structured extraction using LLMs. By fine-tuning a smaller LLM on synthesized document-KG pairs, we streamline the multi-step process into a single-step KG generation approach called Distill-SynthKG.
Furthermore, we repurpose existing question-answering datasets to construct KG evaluation datasets and introduce new evaluation metrics. Using KGs produced by Distill-SynthKG, we also design a novel graph-based retrieval framework for RAG. Experimental results demonstrate that Distill-SynthKG not only surpasses all baseline models in KG quality (including models up to eight times larger) but also consistently improves in retrieval and question-answering tasks. Additionally, our proposed graph retrieval framework outperforms all KG-retrieval methods across multiple benchmark datasets.
**Read the r[esearch paper on arXiv](https://arxiv.org/abs/2410.16597).**