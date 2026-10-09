<!-- Source: https://research.thoughtworks.com/library/tinysql-progressive-text-to-sql-dataset | Title: TinySQL: A progressive text-to-SQL dataset for mechanistic interpretability research  | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# TinySQL: A progressive text-to-SQL dataset for mechanistic interpretability research
By 
Abir Harrasse , 
Philip Quirke , 
Clement Neo , 
Dhruv Nathawani and
Luke Marks
Published: March 17, 2026 
Mechanistic interpretability research faces a gap between analyzing simple circuits in toy tasks and discovering features in large models. To bridge this gap, we propose text-to-SQL generation as an ideal task to study, as it combines the formal structure of toy tasks with real-world complexity. We introduce TinySQL, a synthetic dataset, progressing from basic to advanced SQL operations, and train models ranging from 33M to 1B parameters to establish a comprehensive testbed for interpretability. We apply multiple complementary interpretability techniques, including Edge Attribution Patching and Sparse Autoencoders, to identify minimal circuits and components supporting SQL generation. We compare circuits for different SQL subskills, evaluating their minimality, reliability, and identifiability. Finally, we conduct a layerwise logit lens analysis to reveal how models compose SQL queries across layers: from intent recognition to schema resolution to structured generation. Our work provides a robust framework for probing and comparing interpretability methods in a structured, progressively complex setting.
**Read the complete research article here:**[arXiv](https://arxiv.org/pdf/2503.12730)