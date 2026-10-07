<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/accelerating-pharmaceutical-research-with-multi-agent-ai-system | Title: Accelerating pharmaceutical research with a multi-agent AI system | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Accelerating pharmaceutical research with a multi-agent AI system 
[ Blogs Back ](https://www.thoughtworks.com/en-gb/insights/blog)
Close


By 
Published: March 24, 2026 
In the pharmaceutical industry, finding the right information at the right time is a key challenge. Pharmaceutical organizations possess a wealth of research data stretching back decades, often in various formats (some of it even on paper). 
This represented a considerable obstacle for one of our pharmaceutical clients. But we also knew it offered a real opportunity: bringing together these vast sources of data, making them discoverable and usable for researchers would not only accelerate pharmaceutical research but also improve the quality, making it more reliable and accurate. In turn, that could lead to improved commercial impact and better outcomes for patients, too.
Having worked in partnership over a number of years, we initiated a project to do just that.
## What was the challenge and why was it important to solve?
The consequences of scattered and fragmented data — siloed across different teams, systems and documents — were significant.
  * Researchers had to spend a significant amount of time seeking and then combing through lots of sources.
  * Relatedly, answering what may appear to be relatively straightforward questions about past research could take much longer to answer than it should.
  * This would delay projects, meaning they’d sometimes miss important preclinical deadlines, which in turn meant it would take longer to get new products to patients that need it.
  * It also made it more likely for the research to miss out on important regulatory information, again slowing projects down.
  * It also led to increased costs — conducting comprehensive drug research is expensive.


## How did you implement the project?
The project broadly consisted of three stages. These stages represent an evolution in our approach and in technical implementation:
  * Search: Help researchers search and find the data they need. This was built with semantic search technology, including knowledge graphs.
  * Ask: Provide a way for researchers to actually ask questions about existing research and data. This built upon the foundations of search to add more sophisticated retrieval techniques and an easy-to-use conversational chat UI built with React.
  * Do: Provide researchers with tools that can not only help them find information but also produce a range of outputs, performing actions that add value, fast. This was done using a range of agents that performed a series of tasks together, ranging from research, to evaluation to content creation.


## What technical challenges did you face and how did you solve them?
The process of moving from search to ask to do raised a number of considerable technical challenges. In doing so, however, it demonstrates what’s possible with generative AI technology when used in a thoughtful and intentional way.
One particular challenge was how to ensure the AI was thorough and accurate: while the Ask capability we developed early in the project was useful, there were still some issues with hallucination and it would occasionally lack comprehensiveness in terms of the information it would deliver in response to user prompts.
This informed our approach to the agentic solution. It combined a four different agents: a writer agent (which could generate informative and easy to read outputs for researchers), a researcher agent (constructed to effectively navigate and retrieve information from the growing corpus of data being integrated into the tool) a document planner agent (able to output relevant documentation) and a reflection agent (which could sharpen and improve the accuracy and quality of generated outputs).
### Reflection agent
The reflection agent was critical here: it was programmed to act as a kind of check on the work of other agents, like the researcher and document planner. It was a way of adding in an additional step in the process which, although it increased latency meant the outputs were ultimately much more accurate and useful for researchers.
## What other innovations did you implement?
While the reflection agent played an important role in making our agentic solution effective, we also did further work on two key areas in a bid to ensure quality and accuracy: AI evaluation and improving data quality. Given pharmaceutical research is expensive, quality and reliability have direct commercial consequences.
### Evals
We implemented evals for the project with the help of Langfuse — an LLM engineering platform. A key part of this is curating ground truth, which we did with the help of client subject matter experts. This essentially functions as a kind of baseline (as the name suggests) for the accuracy of LLM outputs. 
This curated ground truth, alongside the question, retrieved context and the answer was an input into the eval stage, for which we used the popular library Ragas.
The key eval metrics included: 
  * Answer relevancy
  * Faithfulness
  * Context relevancy
  * Context precision
  * Answer similarity
  * Answer correctness
  * Context recall
  * Context precision without reference


These eval scores were then pushed back to Langfuse which, in turn, informed future outputs. This essentially created a feedback loop in which our system could become more accurate and reliable, reducing the risk of hallucination or relevant answers.
### Improving data quality
Another approach to improving the research tool was to improve the quality of our data. To be clear, the issue wasn’t strictly that the data across the organization was particularly bad, but instead that it was diverse and fragmented — in different formats, using different nomenclature and structures and with varying degrees of metadata.
The process worked like this:
  * Data would be extracted from PDFs into a JSON format and then preprocessed.
  * This would then go through a process known as chunking, where the data is broken up into discrete pieces.
  * After chunking it would then be organized into embeddings.
  * We then used GPT 4.0 for named entity recognition which would enrich the data, essentially turning what started as something highly unstructured into something highly structured and usable for the LLMs in the agentic system.
  * The final stages involved evaluation (using LLM-as-judge) and verification, involving input from a domain expert (i.e. a data scientist).
  * This process then fed back into the earlier embedding stages, improving how data came to be transformed from structured to unstructured.


## What was the impact and what’s next?
The multi agent system we developed delivered significant benefits to the client:
  * It reduced manual searching by 90%, turning the task from day-to-day drudgery to an occasional edge case.
  * It reduced the amount of time to draft regulatory reports from weeks to just minutes
  * Helped the client avoid redundant experiments, making research more efficient and cost-effective.


From a patient perspective, the technical innovations we implemented help them get the treatment they need faster and at less cost.
This work has focused on the preclinical domain — the next phases may involve bringing multiagent systems into the clinical domain and even integrating deeper research. While the impact of the work has been substantial already, scaling these innovations to other parts of the organization offers a tremendous opportunity.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
## Related content
  * [ Generative AI The future of software development: AI speed, human judgment  Learn more ](https://www.thoughtworks.com/en-gb/insights/articles/the-future-of-software-development-AI-speed-human-judgment)
  * [ Generative AI Inside AI/works™: An agentic development platform  Learn more ](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/inside-ai-works-agentic-development-platform)
  * [ AI and ML AI-first software engineering | Perspectives  Learn more ](https://www.thoughtworks.com/en-gb/perspectives/edition36-ai-first-software-engineering)


## We're helping organizations successfully leverage AI 
[ Find out how ](https://www.thoughtworks.com/en-gb/ai)
Thoughtworks respects your privacy and only uses cookies that are essential for this site to function. If you enjoy our content and would like a personalized experience please ‘’accept optional cookies’’. See our [Privacy policy](https://www.thoughtworks.com/about-us/privacy-policy) for more.
Manage preferences Decline cookies Accept optional cookies
## Privacy Preference Center
## Privacy Preference Center
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Functional Cookies
  * ### Targeting Cookies


#### Your Privacy
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://www.thoughtworks.com/about-us/privacy-policy)
#### Strictly Necessary Cookies
Always Active
These cookies are essential in enabling you to move around our site and use our features. Without them, services you ask for can't be provided. Registered Visitor Cookie: a unique identifier given to each registered user that recognizes you anonymously during site access.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies collect information so we can analyze how our visitors use our site but they don't collect information that identifies you. All information is anonymous and is only used to improve how our site works.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies allow websites and applications to remember choices you make and provide more enhanced, personal features. We may use information collected from functional cookies to identify user behavior and to serve content based on the user profile. These cookies can't track your browsing activity on other websites and don't gather any information about you for advertising usage or to record where you’ve been on the internet, outside our site.
Cookies Details
#### Targeting Cookies
Targeting Cookies
In order to keep our website services relevant, easy to use and up-to-date, we use web analytics services to help us understand how people use the site. Cookies allow us to recognize your browser or device and identify whether you've visited our website before, what you've previously viewed or clicked on and how you found us. The information is anonymous and only used for statistical purposes.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All