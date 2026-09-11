<!-- Source: https://research.thoughtworks.com/library/turning-up-the-heat-min-p-samling-for-creative-and-coherent-creative-outputs | Title: Turning up the heat: Min-p samling for creative and coherent creative outputs | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Turning up the heat: Min-p samling for creative and coherent creative outputs
By 
Minh Nhat Nguyen , 
Andrew Baker , 
Clement Neo and
Andreas Kirsch and Ravid Shwartz-Ziv
Published: July 01, 2024  | Last updated: November 20, 2025
Large Language Models (LLMs) generate text by sampling the next token from a probability distribution over the vocabulary at each decoding step. Popular sampling methods like top-p (nucleus sampling) often struggle to balance quality and diversity, especially at higher temperatures which lead to incoherent or repetitive outputs. 
We propose min-p sampling, a dynamic truncation method that adjusts the sampling threshold based on the model's confidence by using the top token's probability as a scaling factor. Our experiments on benchmarks including GPQA, GSM8K, and Alpaca Eval Creative Writing show that min-p sampling improves both the quality and diversity of generated text across different model families (Mistral and Llama 3) and model sizes (1B to 123B parameters), especially at higher temperatures. 
Human evaluations further show a clear preference for min-p sampling, in both text quality and creativity. Min-p sampling has been adopted by popular open-source LLM frameworks, including Hugging Face Transformers, VLLM, and many others, highlighting its considerable impact on improving text generation quality.
**Research submission[here](https://arxiv.org/abs/2407.01082).**