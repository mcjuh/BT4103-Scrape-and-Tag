<!-- Source: https://research.thoughtworks.com/library/is-paper-reviewed-llm-benchmarking-ai-text-detection | Title: Is your paper being reviewed by an LLM? Benchmarking AI text detection in peer review | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Is your paper being reviewed by an LLM? Benchmarking AI text detection in peer review
By 
Sungduk Yu , 
Man Luo , 
Avinash Madasu and
Vasudev Lal
Published: February 26, 2025  | Last updated: February 05, 2026
Peer review is a critical process for ensuring the integrity of published scientific research. Confidence in this process is predicated on the assumption that experts in the relevant domain give careful consideration to the merits of manuscripts which are submitted for publication. With the recent rapid advancements in large language models (LLMs), a new risk to the peer review process is that negligent reviewers will rely on LLMs to perform the often time consuming process of reviewing a paper. 
However, there is a lack of existing resources for benchmarking the detectability of AI text in the domain of peer review. To address this deficiency, we introduce a comprehensive dataset containing a total of 788,984 AI-written peer reviews paired with corresponding human reviews, covering 8 years of papers submitted to each of two leading AI research conferences (ICLR and NeurIPS). We use this new resource to evaluate the ability of 18 existing AI text detection algorithms to distinguish between peer reviews fully written by humans and different state-of-the-art LLMs. 
Additionally, we explore a context-aware detection method called Anchor, which leverages manuscript content to detect AI-generated reviews, and analyze the sensitivity of detection models to LLM-assisted editing of human-written text. Our work reveals the difficulty of identifying AI-generated text at the individual peer review level, highlighting the urgent need for new tools and methods to detect this unethical use of generative AI.
**Read this[research paper on arXiv](https://arxiv.org/abs/2502.19614).**
**The dataset for this research[is available on Hugging Face](https://huggingface.co/datasets/IntelLabs/AI-Peer-Review-Detection-Benchmark).**