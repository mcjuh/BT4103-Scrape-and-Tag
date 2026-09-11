<!-- Source: https://research.thoughtworks.com/library/robustness-retrieval-augmented-generation | Title: Investigating the robustness of retrieval-augmented generation at the query level | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Investigating the robustness of retrieval-augmented generation at the query level
By 
Sezen Perçin , 
Qutub Sha Syed , 
Aleksei Kuvshinov , 
Leo Schwinn and
Kay-Ulrich Scholl
Published: July 20, 2025 
Large language models (LLMs) are very costly and inefficient to update with new information. To address this limitation, retrieval-augmented generation (RAG) has been proposed as a solution that dynamically incorporates external knowledge during inference, improving factual consistency and reducing hallucinations. Despite its promise, RAG systems face practical challenges-most notably, a strong dependence on the quality of the input query for accurate retrieval. In this paper, we investigate the sensitivity of different components in the RAG pipeline to various types of query perturbations. Our analysis reveals that the performance of commonly used retrievers can degrade significantly even under minor query variations. We study each module in isolation as well as their combined effect in an end-to-end question answering setting, using both general-domain and domain-specific datasets. Additionally, we propose an evaluation framework to systematically assess the query-level robustness of RAG pipelines and offer actionable recommendations for practitioners based on the results of more than 1092 experiments we performed.
**Read the complete research article here:[ACL](https://aclanthology.org/2025.gem-1.38/)**