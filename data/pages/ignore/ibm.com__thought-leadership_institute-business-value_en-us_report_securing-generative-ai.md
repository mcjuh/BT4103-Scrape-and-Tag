<!-- Source: https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai | Title: Securing generative AI: What matters now | IBM | Seed: https://www.ibm.com/consulting (IBM Consulting) -->

# Securing generative AI
In partnership with AWS, we explore what matters now for cybersecurity leaders to protect their organizations’ generative AI solutions.
[Download the insights (will open in a new tab)](https://www.ibm.com/account/reg/us-en/signup?formid=urx-52780)[Subscribe for more insights from IBM IBV (will open in a new window)](https://www.ibm.com/thought-leadership/institute-business-value/en-us/newsletters)
### Innovation versus security: It’s not a choice, it’s a test
As organizations rush to create value from generative AI, many are speeding past a critical element: security. In a recent study of C-suite executives, the IBM Institute for Business Value (IBM IBV) found that only 24% of current gen AI projects have a component to secure the initiatives, even though 82% of respondents say secure and trustworthy AI is essential to the success of their business. In fact, nearly 70% say innovation takes precedence over security.
This perceived trade-off contrasts with executives’ views of the wide-ranging risks of gen AI. Security vulnerabilities are among their biggest areas of concern. 
**Executives expressed a broad spectrum of concerns regarding their adoption of gen AI.**
These worries are well-founded. Cyber criminals are already benefiting from both generative and traditional AI. More realistic [email phishing tactics](https://abnormalsecurity.com/blog/2023-ai-generated-email-attacks) and [deepfake audios](https://edition.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html) are making headlines, as are data leaks from [employees’ careless use](https://www.cnbc.com/2023/05/02/samsung-bans-use-of-ai-like-chatgpt-for-staff-after-misuse-of-chatbot.html) of public tools such as ChatGPT.
Looking ahead, potential threats to critical AI systems are even more troubling. As AI-powered solutions become more capable and more ubiquitous—integrated within critical infrastructure such as healthcare, utilities, telecommunications, and transportation—they could be as vulnerable as they are valuable, especially if security is an afterthought.
While a consolidated AI threat surface is only starting to form, [IBM X-Force® researchers](https://www.ibm.com/reports/threat-intelligence) anticipate that once the industry landscape matures around common technologies and enablement models, threat actors will begin to target these AI systems more broadly. Indeed, that convergence is well underway as the market is maturing rapidly, and [leading providers](https://digitalis.com/news/the-players-set-to-shape-the-ai-landscape-in-2024/) are already emerging across hardware, software, and services.
The gap between executives’ angst and action underscores the need for cybersecurity and business leaders to commit to securing AI—now. With new IBM IBV research showing many organizations are still in the evaluation/pilot stages for most generative AI use cases such as information security (43%) and risk and compliance (46%), this is the time to get ahead of potential threats by prioritizing security from the start.
To address the need for more specific guidance on where to begin, the IBM IBV and IBM Security have teamed with Amazon Web Services (AWS) experts to share leading practices and recommendations based on recent research insights. Part one of this report provides a framework for understanding the gen AI threat landscape. In part two, we discuss the three primary ways organizations are consuming gen AI and the related security considerations. Part three explores resource challenges and the role of partners. Part four offers an action guide of practical steps leaders can take to secure AI across their organizations. 
### Perspective
###  [Understanding the generative AI threat landscape](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#collapseCollapsible255)
Generative AI introduces new potential threat vectors and new ways to mitigate them. While the technology lowers the bar even further for low-skill threat actors, helping them develop more sophisticated exploits, it also enhances defenders’ capacity to move faster with greater efficiency and confidence.
Sources: [Okta blog](https://www.okta.com/blog/2024/01/how-cybercriminals-are-using-gen-ai-to-scale-their-scams/), [Cyber Magazine](https://cybermagazine.com/articles/cybercriminals-are-creating-a-darker-side-to-ai), [SlashNext](https://slashnext.com/blog/exploring-the-world-of-ai-jailbreaks/), [Bleeping Computing](https://www.bleepingcomputer.com/news/security/6-prompts-you-dont-want-employees-putting-in-microsoft-copilot/), [Ars Technica](https://arstechnica.com/security/2024/03/thousands-of-servers-hacked-in-ongoing-attack-targeting-ray-ai-framework/)  
|  [**PART 1:** ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p1)[Seeing threats in a new light](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p1)  |  [**PART 2:** ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p2)[Three AI enablement models, three risk profiles](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p2)  |  [**PART 3:** ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p3)[The leadership dilemma](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p3)  |  [**PART 4:** ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p4)[Action guide](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#p4)  |  
| --- | --- | --- | --- |  
### PART ONE: Seeing threats in a new light
For generative AI to deliver value, it must be secure in the traditional sense—in terms of the [confidentiality, integrity, and availability of data](https://www.youtube.com/watch?v=EqNe55IzjAw). But for gen AI to transform how organizations work—and how they enable and deliver value—model inputs and outputs must be reliable and trustworthy. While hallucinations, ethics, and bias often come to mind first when thinking of trusted AI, the [AI pipeline](https://squarkai.com/whats-an-ai-pipeline/) faces a threat landscape that puts trust _itself_ at risk.Each aspect of the pipeline—its applications, data, models, and usage—can be a target of threats—some familiar and some new. 
**Some emerging threats look familiar while others are entirely new.**
Conventional threats, such as malware and social engineering, persist and require the same due diligence as always. For organizations that may have neglected their security fundamentals or whose security culture is still in the formative stages, these kinds of threats will continue to be a challenge.
Given the increasing adoption of AI and automation solutions by threat actors, organizations without a strong security foundation will also be ill-prepared to address the new twists on conventional threats introduced by gen AI. Take phishing emails as an example. With gen AI, cybercriminals can create far more effective, targeted [scams](https://darktrace.com/blog/email-attack-trends-how-phishing-attacks-are-becoming-more-sophisticated-and-harder-to-identify)—at scale. [IBM Security teams](https://www.ibm.com/reports/threat-intelligence) have found gen AI capabilities facilitate upwards of a 99.5% reduction in the time needed to craft an effective phishing email. This [new breed of email threats](https://darktrace.com/blog/email-attack-trends-how-phishing-attacks-are-becoming-more-sophisticated-and-harder-to-identify) should moderately impact companies with mature approaches to identity management, such as standard practices for least privilege and multifactor authentication as well as zero-trust architectures that restrict lateral movement. But those who lag in these areas run the risk of incidents with potentially devastating reach.
The reality is that security deficiencies are indeed impacting a significant number of organizations, as results from an [IBM IBV survey](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/security-cyber-economy) of more than 2,300 executives suggest. Most respondents reported their organization’s capabilities in zero trust (34%), security by design (42%), and DevSecOps (43%) are in the pilot stage.These organizations will need to continue investing in core security capabilities as they are critical for protecting generative AI.
Lastly, a set of fundamentally new threats to organizations’ gen AI initiatives is also emerging—a fact recognized by nearly half (47%) of respondents in our survey. Prompt injection, for instance, refers to manipulating AI models to take unintended actions; inversion exploits cull information about the data used to train a model. [These techniques](https://securityintelligence.com/posts/mapping-attacks-generative-ai-business-impact/) are not yet widespread but will proliferate as adversaries become more familiar with the hardware, software, and services supporting gen AI. As organizations move forward with gen AI solutions, they need to update their risk and governance models and incident response procedures to reflect these emerging threats. In a recent [AWS Executive Insights podcast](https://aws.amazon.com/podcasts/cwl-the-value-and-threat-of-generative-ai-for-security-teams/), security subject-matter experts emphasized that threat actors will go after low-hanging fruit first—threats with the greatest impact for the least amount of effort. When choosing security investments, leaders should prioritize those use cases, such as supply chain exploits and data exfiltration.
**Emergent threats to AI operations require updates to organizations’ risk and governance models.**
### PART TWO: Three AI enablement models, three risk profiles
A simple framework outlines an effective approach to securing the AI pipeline—starting with updating governance, risk, and compliance (GRC) strategies. Getting these principles right from the beginning—as core design considerations—can accelerate innovation. A governance and design-oriented approach to generative AI is particularly important in light of emerging AI regulatory guidance such as the [EU AI Act](https://artificialintelligenceact.eu/). Those who integrate and embed GRC capabilities in their AI initiatives can differentiate themselves while also clearing their path to value, capitalizing on investments knowing they are building on a solid foundation. 
**Securing the AI value stream starts with updating risk and governance models.**
### Perspective
###  [A glimpse into new and proposed AI regulations around the world](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#collapseCollapsible256)
AI regulations are evolving as quickly as gen AI models and are being established at virtually all levels of government. Organizations can look to automated AI governance tools to help manage compliance with changing policy requirements. A sampling of regulations includes:
**Europe**
  * EU AI Act


**U.S.**
  * Maintaining American Leadership in AI Executive Order
  * Promoting the Use of Trustworthy AI in the Federal Government Act Executive Order
  * AI Training Act
  * National AI Initiative Act


**Canada**
  * AI and Data Act
  * Directive on Automated Decision-Making


**Brazil**
  * AI Bill


**China**
  * Algorithmic Recommendations Management Provisions
  * Ethical Norms for New Generation AI
  * Opinions on Strengthening the Ethical Governance of Science and Technology
  * Draft Provisions on Deep Synthesis Management
  * Measures for the Management of Generative AI Services


**Japan**
  * Guidelines for Implementing AI Principles
  * AI Governance in Japan Ver.1.1


**India**
  * Digital India Act


**Australia**
  * Uses existing regulatory structures for AI oversight


Source: [Global AI Regulations Tracker](https://legalnodes.com/article/global-ai-regulations-tracker)
Next, leaders can shift their attention to securing infrastructure and the processes comprising the AI value stream: data collection, model development, and model use. Each presents a distinct threat surface that reflects [how the organization is enabling AI](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/): using third-party applications with embedded gen AI capabilities; building gen AI solutions via a platform of pre-trained or bespoke foundation models; or building gen AI models and solutions from scratch.
Each adoption route encompasses varying levels of investment, commitment, and responsibility. Working through the risks and security for each helps build resilience across the AI pipeline. While some organizations have already anchored on an adoption strategy, some are applying multiple approaches, and some may still be finding their way and formalizing their strategy. From a security perspective, what varies with each option is who is responsible for what—and [how that responsibility may be shared](https://cloudsecurityalliance.org/blog/2023/07/28/generative-ai-proposed-shared-responsibility-model).
**The principles of shared responsibility extend to securing generative AI models and applications.**
####  Using third-party applications embedded with generative AI
Organizations that are just getting started may be using consumer-focused services such as OpenAI’s ChatGPT, Anthropic’s Claude, or Google Gemini, or they are using an [off-the-shelf SaaS product with gen AI](https://cloudsecurityalliance.org/blog/2023/07/28/generative-ai-proposed-shared-responsibility-model) features built in, such as Microsoft 365 or Salesforce. These solutions allow organizations that have fewer investment resources to gain efficiencies from basic gen AI capabilities. 
The companies providing these gen AI-enabled tools are responsible for securing the training data, the models, and the infrastructure housing the models. But users of the products are not free of security responsibility. In fact, inadvertent employee actions can induce headaches for security teams.
Similar to how shadow IT emerged with the first SaaS products and created cloud security risks, the incidence of [shadow AI](https://www.fastcompany.com/90972657/what-managers-should-know-about-the-secrets-threat-of-employees-using-shadow-ai) is growing. With employees looking to make their work lives easier with gen AI, they are complicating the organization’s security posture, making security and governance more challenging.
First, well-meaning staff can share private organizational data into third-party products without knowing whether the AI tools meet their security needs. [This](https://www.fastcompany.com/90972657/what-managers-should-know-about-the-secrets-threat-of-employees-using-shadow-ai) can expose sensitive or privileged data, leak proprietary data that may be incorporated into third-party models, or expose data artifacts that could be vulnerable should the vendor experience a cyber incident or data breach.
Second, because the security team is unaware of the usage, [they can’t assess and mitigate the risks](https://www.fastcompany.com/90972657/what-managers-should-know-about-the-secrets-threat-of-employees-using-shadow-ai). Third-party software—whether or not sanctioned by the IT/IS team—can [introduce vulnerabilities](https://securityintelligence.com/posts/mapping-attacks-generative-ai-business-impact/) because the underlying gen AI models can host malicious functionality such as trojans and backdoors. [One study](https://www.gartner.com/en/newsroom/press-releases/2023-03-28-gartner-unveils-top-8-cybersecurity-predictions-for-2023-2024) found that 41% of employees acquired, modified, or created technology without their IT/IS team’s knowledge—and predicts this percentage will climb to 75% over the next three years, exacerbating the problem.  
|  **Key security considerations**
  * Have you established and communicated policies that address use of certain organizational data (confidential, proprietary, or PII) within public models and third-party applications? 
  * Do you understand how third parties will use data from prompts (inputs/outputs) and whether they will claim ownership of that data? 
  * Have you assessed the risks of third-party services and applications and know which risks they are responsible for managing?
  * Do you have controls in place to secure the application interface and monitor user activity, such as the content and context of prompt inputs/outputs?

 |  
| --- |  
####  Using a platform to build generative AI solutions
Training foundation models and LLMs for generative AI applications demands tremendous infrastructure and computing resources—often beyond what most organizations can budget. Hyperscalers are stepping in with platforms that allow users to tap into a choice of pre-trained foundation models for building gen AI applications more specific to their needs. These models are trained on a large, general-purpose data set, capturing the knowledge and capabilities learned from a broad range of tasks to improve performance on a specific task or set of tasks. [Pre-trained models can also be fine-tuned](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/) for a more specific task using a smaller amount of an organization’s data, resulting in a new specialized model optimized around distinct use cases, such as industry-specific requirements.
The open-source community is also democratizing gen AI with an extensive library of pre-trained LLMs. The most popular of these—such as Meta’s Llama and Mistral AI—are also available via general-purpose gen AI platforms.
### Perspective
###  [Risk or reward? Adopting open-source models](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#collapseCollapsible258)
In contrast to proprietary LLMs that can only be used by customers who purchase a license from the provider, open-source LLMs are free and available for anyone to access. They can be used, modified, and distributed with far greater flexibility than proprietary models.
Designed to offer transparency and interoperability, open-source LLMs allow organizations with minimal machine learning skills to adapt gen AI models for their own needs—and on their own cloud or on-premises infrastructure. They also help offset concerns about the risk of becoming overly reliant on a small number of proprietary LLMs.
Risks with using open-source models are similar to proprietary models, including hallucinations, bias, and accountability issues with the training data. But the trait that makes open source popular—the community approach to development—can also be its greatest vulnerability as hackers can more easily manipulate core functionality for malicious purposes. These risks can be mitigated by adopting security hygiene practices as well as software supply chain and data governance controls.
Source: [Open source large language models: Benefits, risks and types](https://www.ibm.com/blog/open-source-large-language-models-benefits-risks-and-types/)
Platforms offer the advantage of having some security and governance capabilities baked in. For example, infrastructure security is shared with the vendor, similar to any cloud infrastructure agreement. Perhaps the organization’s data already resides with a specific cloud provider, in which case fine-tuning the model may be as simple as updating configurations and API calls. Additionally, a catalogue of enhanced security products and services is available to complement or replace the organization’s own.
### Case study
###  [EVERSANA and AWS advance artificial intelligence apps for the life sciences industry](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#collapseCollapsible257)
Given regulatory requirements, life sciences companies need generative AI solutions that combine security, compliance, and scalability. EVERSANA, a leading provider of commercial services to the global life sciences industry,[is turning to AWS](https://www.eversana.com/2023/07/24/eversana-amazon-web-services-to-pharmatize-artificial-intelligence-across-the-life-sciences-industry/) to accelerate gen AI use cases across the life sciences industry. The objective is to harness the power of gen AI to help pharmaceutical and life science manufacturers drive efficiencies and create business value while improving patient outcomes.
EVERSANA will apply its digital and AI innovation capabilities coupled with Amazon Bedrock managed gen AI services to leverage best-of-breed foundation models. EVERSANA [maintains full control over the data](https://aws.amazon.com/bedrock/) it uses to tailor foundation models and can customize guardrails based on its application requirements and responsible AI policies. In its first application—[in partnership with AWS and TensorIoT,](https://aws.amazon.com/partners/success/eversana-tensoriot/) the team sought to automate processes associated with medical, legal, and regulatory (MLR) content approvals.
EVERSANA’s strategy to leverage gen AI to solve complex challenges for life sciences companies is part of what EVERSANA calls “pharmatizing AI.” Jim Lang, chief executive officer at EVERSANA, explained, “Pharmatizing AI in the life sciences industry is about leveraging technology to optimize and accelerate common processes that are desperate for innovation and transformation.” This approach has led to streamlining critical processes from months to weeks. EVERSANA anticipates that once it automates its MLR capabilities, it can further improve time-to-approval from weeks to mere days.
However, when organizations build gen AI applications integrated with pre-trained or fine-tuned models, their security responsibilities grow considerably compared to using a third-party SaaS product. Now they must tackle the unique threats to foundation models and LLMs referenced in part one of this report. Risks to training data as well as the model development and inference fall squarely on their radar. Applying the principles of ModelOps and [MLSecOps](https://www.techtarget.com/searchitoperations/news/366552019/Meet-MLSecOps-industry-calls-for-new-measures-to-secure-AI) (machine learning security operations) can help organizations [secure their gen AI applications](https://venturebeat.com/ai/exclusive-what-will-it-take-to-secure-gen-ai-ibm-has-a-few-ideas/).  
|  **Key security considerations**
  * Have you conducted threat modeling to understand and manage the emerging threat vectors? 
  * Have you identified open-source and widely used models that have been thoroughly scanned for vulnerabilities, tested, and vetted? 
  * Are you managing training data workflows, such as using encryption in transit and at rest, and tracking data lineage? 
  * How do you protect training data from poisoning exploits that could introduce inaccuracies or bias and compromise or change the model’s behavior? 
  * How do you harden security for API and plug-in integrations to third-party models? 
  * How do you monitor models for unexpected behaviors, malicious outputs, and security vulnerabilities that may appear over time? 
  * Are you managing access to training data and models using robust identity and access management practices, such as role-based access control, identity federation, and multifactor authentication? 
  * Are you managing compliance with laws and regulations for data privacy, security, and responsible AI use?

 |  
| --- |  
#### Building your own generative AI solutions
A few large organizations with deep pockets are building and training LLMs—and [smaller, more tailored language models](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/) (SLMs)—from scratch based solely on their data. [Hyperscaler tools](https://aws.amazon.com/machine-learning/trainium/) are helping accelerate the training process, while the organization owns every aspect of the model. This can afford them performance advantages as well as more precise results.
In this scenario, on top of the governance and risk management outlined for applications based on pre-trained and fine-tuned models, the organization’s own data security posture takes on greater importance. As the organization’s data is now incorporated into the AI model itself, responsible AI becomes essential to reducing risk exposure.
Being the primary source for AI training data, organizations are responsible for making sure that data—and the outcomes based on it—can be trusted. That means protecting the source data following strict data security practices. And it means protecting the models from being compromised or exploited by malicious actors. Access controls, encryption, and threat detection systems are critical pieces in preventing data from being manipulated. The trustworthiness of an AI solution may be measured by its ability to offer unbiased, accurate, and ethical responses.
If organizations do not practice responsible AI, they risk damage to their brands from faulty—even dangerous—output from their gen AI models. Despite these risks, fewer than 20% of executives say they are concerned about a potential liability for erroneous outputs from gen AI. In other IBM IBV research, only 30% of respondents said they are validating the integrity of gen AI outputs.
If secure and trustworthy data is the basis for value generation—and [much of our research indicates it is](https://ibm.co/c-suite-study-cdo)—leaders should focus on the security implications of (ir)responsible AI.Doing so can highlight the various ways AI models may be manipulated. In the absence of bias or explainability controls, such manipulation can be hard to recognize. This is why organizations need a strong foundation in governance, risk, and compliance.
As an extension of the organization’s data security posture, software supply chain security also becomes more consequential when creating LLMs. These models are built on top of complex software stacks that include multiple layers of software dependencies, libraries, and frameworks. Each of these components can introduce vulnerabilities that can be exploited by attackers to compromise the integrity of the AI model or the underlying data.
Unfortunately, adoption of software supply chain security best practices is still nascent at many organizations, according to recent IBM IBV research. For example, only 29% of executives indicated they have adopted DevSecOps principles and practices to secure their software supply chain, and only 32% have implemented continuous monitoring capabilities for their software suppliers. Both practices are vital to helping prevent cyber incidents throughout the software supply chain.  
|  **Key security considerations**
  * Do you need to bolster data security practices to help prevent theft and manipulation and support responsible AI? 
  * How can you shore up third-party software security awareness and practices; for example, ensuring that zero-trust principles are in place? 
  * Do you require procurement teams to check supplier contracts for security vulnerability controls and risk-related performance measures?

 |  
| --- |  
### Perspective
###  [Why responsible AI starts with security ABCs](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#collapseCollapsible259)
As AI moves from experimentation into production, the ABCs of security—awareness, behavior, and culture—become even more important for helping ensure [responsible AI](https://www.ibm.com/topics/responsible-ai). For AI to be designed, developed, and deployed with good intent for the benefit of society, trust is an imperative.
Consistent with many emerging technologies, well-informed employees and partners can be an asset—especially in light of new multimodal and rich-media-based phishing tactics enabled by gen AI. Enhancing employee awareness of the new risks leads to proactive behaviors and, over time, a more robust security culture.
As AI solutions become more integral to operations, a standard practice should be to communicate new functionality and associated security controls to employees, while reiterating the policies in place to protect proprietary and personal data. Established controls should be updated to address new threats, with the core principles of zero trust and least privilege limiting lateral movement. Emphasizing a sense of ownership about security outcomes can reinforce security as a common, shared endeavor connecting virtually all stakeholders and partners. Responsible AI is about more than policies—it’s a commitment to safeguard the trust that’s critical to the organization’s continuing success.
### PART THREE: The leadership dilemma—generative AI requires what organizations have least
Developing and securing generative AI solutions requires [capacity, resources, and skills](https://hbr.org/2023/11/what-ceos-need-to-know-about-the-costs-of-adopting-genai)—the very things organizations don’t have enough of. In fragmented IT environments, security takes on higher levels of complexity that require even more capacity, resources, and skills. Leaders quickly find themselves in a dilemma.
**AI-enhanced tools**
AI-powered security products can bridge the skills gap by freeing overworked staff from time-consuming tasks. This allows them to focus on more complex security issues that require expertise and judgment. By optimizing time and resources, AI effectively adds capacity and skills. With improved insights, productivity, and economies of scale, organizations can adopt a more preventive and proactive security posture. Indeed, [leading security AI adopters](https://ibm.co/ai-cybersecurity) cut the time to detect incidents by one-third and the costs of data breaches by at least 18%. New capabilities are also emerging that automate management of compliance within a rapidly changing regulatory environment. 
The shift to AI security tools is consistent with how cybersecurity demand is changing. While the market for AI security products is expected to grow at a [CAGR of nearly 22%](https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-ai-cyber-security-market-220634996.html) over the next five years, providers are focusing on developing consolidated [security software solutions](https://www.trendmicro.com/en_us/what-is/cybersecurity-platform.html). To facilitate better efficiency and governance, solution providers are rationalizing their toolsets and streamlining data analysis. This more holistic approach to security enhances visibility across the operations lifecycle—something 53% of executives are expecting to gain from gen AI.
**AI-experienced partners**
Business partners can also help close security skills gaps. Just as with the transition to cloud, partners can assist with assessing needs and managing security outcomes. Amid the ongoing security talent shortage that’s exacerbated by a lack of AI skills, organizations are seeking partners that can facilitate training, knowledge sharing, and knowledge transfer (76%). They are also looking for gen AI partners to provide extensive support, maintenance, and customer service (82%). Finally, they are choosing partners that can guide them across the evolving legal and regulatory compliance landscape (75%). 
Executives are also in search of partners to help with strategy and investment decisions. With around half saying they are uncertain about where and how much to invest, it’s no surprise that three-quarters (76%) want a partner to help build a compelling cost case with solid ROI. More than half also seek guidance on an overall strategy and roadmap.
**Executives are turning to partners to help deliver and support generative AI security solutions.**
Our results indicate that most organizations are turning to partners to enable generative AI for security. Respondents indicated they are relying on internal development for only 9% of their gen AI security solutions. While many respondents are purchasing security products or solutions with gen AI capabilities, nearly two-thirds of their security generative AI capabilities are coming through some type of partner—managed services, ecosystem/supplier, or hyperscaler. Similar to cloud adoption, leaders are looking to partners for comprehensive support—whether that’s informing and advising about generative AI or augmenting their delivery and support capabilities.
**More than 90% of security gen AI capabilities are coming from third-party products or partners.**
###  PART FOUR: Action guide
Whether just starting to experiment with generative AI, building models on your own, or somewhere in between, the following guidance can help organizations secure their AI pipeline. These recommendations are intended to be cross-functional, facilitating engagement across security, technology, and business domains.
**Assess**
  * Define an AI security strategy that aligns with the organization’s overall AI strategy. 
  * Ask how your organization is using AI today—for which use cases, in what applications, through which service providers, and serving which user cohorts. Once you answer these questions, then quantify the associated sources of risk. 
  * Evaluate the maturity of your core security capabilities, including infrastructure security, data security, identity and access management practices, threat detection and incident response, regulatory compliance, and software supply chain management. Identify where you must be better to support the demands of AI. 
  * Decide where partners can supplement and complement your security capabilities and define how responsibilities will be shared. 
  * Uncover security gaps in AI environments using risk assessment and threat modeling. Determine how policies and controls need to be updated to address emergent threat vectors driven by generative AI.


**Implement**
  * Establish AI governance working with business units, risk, data, and security teams. 
  * Prioritize a secure-by-design approach across the ML and data pipeline to drive safe software development and implementation. 
  * Manage risk, controls, and trustworthiness of AI model providers and data sources. 
  * Secure AI training data in line with current data privacy and regulatory guidelines, and adopt new guidelines when published. 
  * Secure workforce, machine, and customer access to AI apps and subsystems from anywhere.


**Monitor**
  * Evaluate model vulnerabilities, prompt injection risks, and resiliency with adversarial testing. 
  * Perform regular security audits, penetration testing, and red-teaming exercises to identify and address potential vulnerabilities in the AI environment and connected apps.


**Educate**
  * Review cyber hygiene practices and security ABCs (awareness, behaviors, and culture) across your organization. 
  * Conduct persona-based cybersecurity awareness activities and education, particularly as they relate to AI as a new threat surface. Target all stakeholders involved in the development, deployment, and use of AI models, including employees using AI-powered tools.


IBM Institute for Business Value survey of 2,500 global, cross-industry executives on AI adoption. 2024. Unpublished data.
IBM Institute for Business Value survey of 2,000 global executives responsible for supplier management, supplier sourcing, and ecosystem partner relationships. 2023. Unpublished data.
[Download the insights(will open in a new tab)](https://www.ibm.com/account/reg/us-en/signup?formid=urx-52780)[Subscribe for more insights from IBM IBV(will open in a new tab)](https://www.ibm.com/thought-leadership/institute-business-value/en-us/newsletters)
How can IBM help you?
[IBM Security (will open in a new window) IBM Security Discover AI-driven cybersecurity solutions that evolve with your business. ](https://www.ibm.com/security)
[IBM Security Services (will open in a new window) IBM Security Services Transform your business and manage risk with a global industry leader in cybersecurity consulting, cloud, and managed security services. ](https://www.ibm.com/services/security)
[Artificial intelligence (AI) cybersecurity (will open in a new window) Artificial intelligence (AI) cybersecurity Improve the speed, accuracy, and productivity of security teams with AI-powered solutions. ](https://www.ibm.com/ai-cybersecurity)
How can IBM help you?
[IBM Security (will open in a new window) IBM Security Discover AI-driven cybersecurity solutions that evolve with your business. ](https://www.ibm.com/security)
[IBM Security Services (will open in a new window) IBM Security Services Transform your business and manage risk with a global industry leader in cybersecurity consulting, cloud, and managed security services. ](https://www.ibm.com/services/security)
[Artificial intelligence (AI) cybersecurity (will open in a new window) Artificial intelligence (AI) cybersecurity Improve the speed, accuracy, and productivity of security teams with AI-powered solutions. ](https://www.ibm.com/ai-cybersecurity)
You might also like
[The CEO’s guide to generative AI: Cybersecurity  Translations available The CEO’s guide to generative AI: Cybersecurity Explore three things CEOs need to know and three things they need to do now to apply generative AI to cybersecurity. Bookmark this report ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/cybersecurity)
[Data security as business accelerator?  Translations available Data security as business accelerator? Data security can be the unsung hero in driving competitive advantage. Learn how delivering trusted data can spark innovation. Bookmark this report ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/data-security)
[AI and automation for cybersecurity  Translations available AI and automation for cybersecurity Security leaders are using AI for cybersecurity to boost visibility and productivity across security operations. Bookmark this report ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/ai-cybersecurity)
[Upstream oil and gas in the AI era  Upstream oil and gas in the AI era AI isn't failing in upstream oil and gas. What's failing is scaling its value across the enterprise. Bookmark this report ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/upstream-oil-and-gas-in-ai-era)
[Orchestrating agentic AI for intelligent business operations - French (will open in a new tab) Orchestrating agentic AI for intelligent business operations - French Learn how agentic AI is set to extend automation of business operations, elevating the workforce and expediting outcomes. Bookmark this report ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/agentic-process-automation-french)
[Orchestrating agentic AI for intelligent business operations - German (will open in a new tab) Orchestrating agentic AI for intelligent business operations - German Learn how agentic AI is set to extend automation of business operations, elevating the workforce and expediting outcomes. Bookmark this report ](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/agentic-process-automation-german)
AskIBV AI Assistant
BETA
How can we help you?Interacting with this button will open IBV Insights AI in a new window Interacting with this button will open IBV Insights AI in a new browser windowClose Interacting with this button will close IBV Insights AI Beta Launcher
Focus sentinel
Open chat history
AskIBV
BETA
AI Explained
## AskIBV 
BETA
AskIBV combines advanced AI with the IBV’s trusted, data‑driven research and executive interviews to deliver exclusive insights and perspectives you won’t find anywhere else.
Loading AskIBV insights AI
Focus sentinel
Overview Annual report Corporate social responsibility Inclusion@IBM Financing Investor Newsroom Security, privacy & trust Senior leadership Careers with IBM Website Blog Publications Automotive Banking Consumer Goods Energy Government Healthcare Insurance Life Sciences Manufacturing Retail Telecommunications Travel Our strategic partners Find a partner Become a partner - Partner Plus Partner Plus log in IBM TechXChange Community LinkedIn X Instagram YouTube Subscription Center Participate in user experience research Podcasts United States — English Contact IBM Privacy Terms of use Accessibility
IBM web domains
ibm.com, ibm.org, ibm-zcouncil.com, insights-on-business.com, jazz.net, mobilebusinessinsights.com, promontory.com, proveit.com, ptech.org, s81c.com, securityintelligence.com, skillsbuild.org, softlayer.com, storagecommunity.org, think-exchange.com, thoughtsoncloud.com, alphaevents.webcasts.com, ibm-cloud.github.io, ibmbigdatahub.com, bluemix.net, mybluemix.net, ibm.net, ibmcloud.com, galasa.dev, blueworkslive.com, swiss-quantum.ch, blueworkslive.com, cloudant.com, ibm.ie, ibm.fr, ibm.com.br, ibm.co, ibm.ca, community.watsonanalytics.com, datapower.com, skills.yourlearning.ibm.com, bluewolf.com, carbondesignsystem.com, openliberty.io 
About cookies on this site Our websites require some cookies to function properly (required). In addition, other cookies may be used with your consent to analyze site usage, improve the user experience and for advertising. For more information, please review your [cookie preferences](javascript:void\(0\)) options. By visiting our website, you agree to our processing of information as described in IBM’s  [privacy statement](https://www.ibm.com/privacy).  To provide a smooth navigation, your cookie preferences will be shared across the IBM web domains listed [here](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/securing-generative-ai#truste_domain_list). 
Accept All More options