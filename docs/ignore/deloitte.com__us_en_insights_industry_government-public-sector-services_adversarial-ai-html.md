<!-- Source: https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html | Title: Adversarial AI | Deloitte Insights | Seed: https://www.deloitte.com/us/en/services/consulting/services/mergers-acquisitions.html (Deloitte) -->

Article 
15-min read
11 April 2023
# Securing government against adversarial AI
## Artificial intelligence is bringing new benefits to government, but new adversarial attacks against those tools mean government also needs new ways to safeguard them.
By Vinita Fordham,  Dr. David Caswell,  Allie Diehl
### Allie Diehl
Senior Consultant 
Deloitte United States
Allie Diehl is a senior consultant in Deloitte's Analytics & Cognitive practice focused on growing AI strategy and adoption across the federal government. She has lectured on AI at Georgetown University and helped design an advanced degree class. She graduated Phi Beta Kappa from The Johns Hopkins University with a double major in Economics and International Studies as a Hodson Scholar. She has previously worked as an equities research analyst and an actuarial analyst.
_aldiehl@deloitte.com_
Article 
15-min read
11 April 2023
  * [ Share ](javascript:void\(0\))
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")
  * [ Print ](javascript:window.print\(\); "Print")


  * [ Download (3 MB) ](https://www.deloitte.com/content/dam/insights/articles/2024/us164617_cgi_adversarial-ai/di-adversarial-ai-ad-review.pdf "Download PDF \(3 MB\)")
  * [ Share ](javascript:void\(0\))
    * ### Share this article
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")
    * ### Or copy link


In 2016, Microsoft released its AI-enabled chatbot Tay publicly to social media and retrained it based on inputs from its conversations with users. Shortly after the release, internet trolls launched a coordinated data-poisoning attack that abused Tay’s learning mechanisms, enabling the attackers to retrain it to tweet inappropriate content. This AI system’s integrity was compromised by bad actors, through _data poisoning—_ introducing malicious inputs to manipulate the model’s outputs. Machine learning (ML) models trained on open-source data or production data can be especially vulnerable to this type of attack.
As AI/ML solutions proliferate, the attacks on such systems also multiply. Some real-world examples include cybersecurity breaches, privacy attacks on patient records, and intellectual property theft. Attacks can even occur by way of physical manipulation, such as in the case of autonomous vehicles: A research study demonstrated that an autonomous driving AI system could be fooled into driving over the speed limit and misclassifying fake traffic signs.
Since this early attack, Microsoft has published open-source adversarial AI defenses through its publicly available repository, Counterfit. Such precautions are critical to avert successful attacks as more AI-enabled chatbots are released into production, especially within government services. Fortunately, data and technology leaders recognize the need for safeguards. In Deloitte’s  _2019 State of AI in the Enterprise_ report, organizations highlighted security and safety as their top concerns when adopting AI. But this field of knowledge—known as adversarial AI—has only recently emerged. At a practical level, organizations need AI guardrails against adversarial attacks and plans for defensive countermeasures. Addressing these new security challenges requires a multipronged approach, including cross-training of AI/ML and cybersecurity teams, setting security standards and bringing in experts, and securing the development life cycle.
#### Table of contents
  * [ The problem: A new breed of security challenges ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html#the-problem)
  * [ New technology brings new vulnerabilities ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html#new-technology)
  * [ Adversarial AI is not just traditional software development ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html#adversarial-ai)
  * [ The solution: A three-pronged approach ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html#solution)


## The problem: A new breed of security challenges
As ML applications become more prevalent and applied to areas where reliability, security, and safety are paramount, attention has turned to their potential vulnerabilities. As they upgrade their systems to include AI-based technologies, federal agencies are starting to encounter more adversarial AI challenges. For example, the Department of Justice is addressing data privacy or guarding against data tampering that impact tagging of facial recognition for potential use in court cases, where it would be used to identify suspects.6
However, building AI that can defend against this new breed of security challenges is not easy. A small number of government and industry leaders are working toward establishing AI-/ML-specific standards. For example, Defense Advanced Research Projects Agency’s (DARPA) Guaranteeing AI Robustness Against Deception (GARD) program is currently working to develop general defensive capabilities that are effective against a broad swath of adversarial attacks. As part of the countermeasures, they have developed an approach to capture improved metrics for AI robustness.7 These metrics seek to allow for future advances in the field to be shared utilizing a common understand of how they work.
### Share infographic
  * [ Share ](javascript:void\(0\))
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")


### Or copy link
Copy
Such examples remain rare, and attention to the challenge of adversarial AI is limited, as the field itself reached critical milestones as recently as six years ago with nearly half its publications occurring since 2020. As a result, government agencies are still working to comply with the 2019 Executive Order on Maintaining American Leadership on AI (EO 13859) to develop “technical standards [to] minimize vulnerability to attacks from malicious actors and reflect federal priorities for innovation, public trust, and public confidence in systems that use AI technologies.” The broader ecosystem of AI service providers is also still developing the necessary capabilities. Globally, venture capital funds invested more than US$230 billion into AI/ML companies from 2018 to 2021, including almost US$90 billion in 2021. However, less than 1% of this funding has gone toward AI/ML security research and infrastructure development startups.
## New technology brings new vulnerabilities
One critical shortcoming inhibiting progress in the field of adversarial AI is the lack of a standard framework for technical evaluations and governance. The lack of standardization makes it hard to benchmark the security levels of AI systems. Because this is an emerging field, there is no clear starting point for addressing AI security systematically.
Attacks can take place at any point throughout the AI/ML life cycle (figure 1), from training to inference—and point solutions cannot secure entire AI/ML systems (figure 2). Since defenses geared toward production models will not always account for vulnerabilities in their training, security experts should examine AI/ML systems throughout the entire AI/ML life cycle. For example, encryption techniques that protect cloud-based development activities will not secure a model trained on poisoned data—at that point, it is already too late. What’s needed is a mechanism to protect AI systems against threats such as data poisoning and associated model evasion—such as through embedded backdoor attacks or attacks which allow for future evasion attacks by creating an opening or “backdoor” for a specific type of adversarial input to trick the model—and privacy attacks in which malicious actors attempt to steal private data such as patient details, information on the data set or model, or the model itself.
### Share infographic
  * [ Share ](javascript:void\(0\))
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")


### Or copy link
Copy
## Adversarial AI is not just traditional software development 
There are marked differences between adversarial AI and traditional software development and cybersecurity frameworks. Often, vulnerabilities in ML models are connected back to data poisoning and other types of data-based attacks. Since these vulnerabilities are inherent in the model inputs, they cannot be “patched” through code fixes the way traditional software fixes are done. Furthermore, methods to patch known vulnerabilities tend to be expensive and only provide modest security improvements while impacting model performance severely. Complicating the problem even further, as models become increasingly bespoke or personalized to users, a single patch is less likely to fix the issue. In fact, it may even exacerbate it. Some adversarial AI countermeasures, while protecting against one type of attack, may increase vulnerability to others. As Andrew Lohn and Wyatt Hoffman, research fellows at Georgetown’s Center for Security and Emerging Technology, wrote, “One defense may protect against attacks that alter images to hide a tank, but that same defense may make it easier for attacks to adjust the images in other ways to make tanks appear where there are none.”
## The solution: A three-pronged approach
Adversarial AI attacks can pose a significant threat to machine learning models, making it important to address these challenges proactively. It is recommended to address these as early as possible in the AI development process and continuously evaluate and update the defenses as the threat landscape evolves. To address the challenges posed by adversarial AI, organizations should focus on three main areas:
  1. Cross-train the workforce to bridge the gap between AI/ML and cybersecurity expertise—the intersection of these disciplines provides the best defense against adversarial attacks.
  2. Set security standards and bring in the specialists, such as through AI red teaming and model governance, to evaluate the security of AI/ML models and suggest countermeasures and risk mitigations.
  3. Secure the model development life cycle by adopting the tools, techniques, and standards being developed in the rapidly evolving ecosystem around adversarial AI and adopting the most relevant and trusted tools and frameworks.


### Cross-training the workforce
Consider people first when evaluating security risks. Vulnerability to adversarial AI threats starts with the workforce. Those entrenched in the ML life cycle—data scientists, engineers, and other AI talent personas—prioritize model performance, which often carries a trade-off with model security. Organizations can empower their AI teams to better navigate performance-security trade-offs by cross-training the workforce to enable model governance. Data science and cybersecurity are the two technology areas for which organizations have the most difficulty finding talent with the appropriate skillsets. Cross-train AI engineers in security leading practices while cross-training security analysts in AI fundamentals is a great way to effectively identify the threat landscape and attack perimeter. This people-centric approach aligns with trends in the cybersecurity industry, which has moved from the concept of “shifting security to the left” (that is, introducing security checks during the development phase) to enhancing security everywhere. This change has been accelerated by the transition into the virtual world at the onset of the COVID-19 pandemic. As more work is done from the home office, security considerations must be taken across new networks.
Those familiar with the software development fields will recognize the term DevOps, a set of practices that combines software development and IT operations. Similar to DevOps, MLOps is a culture and a practice that aims to combine ML development and operations throughout the model development life cycle, allowing for the continuous iteration and delivery of models. It helps track model development and postproduction performance, and to plan for optimal retraining and redeployment. Successful MLOps can decrease time to production, reduce model downtime, and enhance model performance. By integrating security considerations into an MLOps workflow, organizations can take a proactive approach to combating adversarial AI threats.
There are many roles involved in the ML life cycle, from data engineering to deployment and mission specialists. For an MLOps plus security—or MLSecOps—approach to be successful, the different roles/personas must all work together to ensure model security at every step of the ML life cycle. Defenses cannot be siloed, nor are they the responsibility of a single stakeholder (figure 3). In this way, there is no singular “security persona,” but rather a combined effort enabled by experience-based cross-training. Collaboration tools and governance workflows can support coordination across the various personas and ensure that development decisions consider security principles throughout the ML life cycle.
### Share infographic
  * [ Share ](javascript:void\(0\))
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")


### Or copy link
Copy
Show More
MLSecOps responsibilities span across multiple roles involved in the AI/ML development life cycle. As all ML begins with data, **data engineers** play an important role in ensuring security through data governance. In the first phase of the life cycle, data engineers validate the integrity of training data. This validation step is especially critical given training data is often pulled from open-source or third-party data providers. During the later inference phase, data engineers employ detection and classification techniques to identify potential adversarial inputs and protect model integrity. **Data scientists** build security into the models by design. As part of the development process, they employ privacy-enhancing techniques such as differential privacy, a mathematical method for ensuring individual data points cannot be extracted from a data set. The role of data scientists also extends into the inference phase as they examine model outputs to detect vulnerabilities. For example, a data scientist may examine a model explainability plot, or a visual representation of model performance, to better understand the model’s underlying mechanisms and thus potential security vulnerabilities regarding how it handles edge cases. **ML engineers** further secure the life cycle through use of encryption techniques to protect data integrity throughout as well as validating the security of software and hardware components used during both the training and inference phases. **Business analysts** also have a role to play by setting strong policies around data and model protection, ensuring sourcing hardware from preapproved manufacturers. Further, to minimize leakage of sensitive data and proprietary ML models, they monitor externally published information to protect against reconnaissance efforts intend on informing model attacks. Throughout the life cycle, analysts consider vulnerabilities within the process that could be addressed through technical or nontechnical solutions and apply risk-quantification and benchmarking practices.
#### Set security standards and bring in the specialists
As part of model governance, organizations should develop and maintain a counter–adversarial AI framework. Dependent on the type of ML systems and applications an organization uses, different levels of defense and privacy thresholds may be warranted. Organizations can start with an assessment of AI projects, identifying those that involve critical systems and data and base recommendations on quantitative evidence. Currently, much of the evidence available about AI threats is based on academic metrics that are not always relevant in actual operations. Organizations should invent ways to measure both the vulnerability and the potential impact of adversaries attacking real-world systems.
Chief security officers, chief data officers, and other C-suite executives focused on AI should be proactive to ensure their organizations are using leading technologies in a rapidly evolving field. This includes understanding and evaluating the ecosystem for adversarial AI solutions when budgeting for investments. Although a small portion of funding is going toward AI/ML security research and infrastructure development, many private companies, academia, and governments are developing and investing in solutions to combat adversarial AI attacks. Academia and big tech lead the way in maintaining open-source libraries as well as through the publication of threat databases.
For example, in academia, researchers at Johns Hopkins University developed a set of tools called TrojAI to help test the robustness of ML models and protect them from trojan attacks. These tools generate data sets and models with trojans to test ML models quickly and at scale. In MIT’s Computer Science and Artificial Intelligence Laboratory, researchers developed a tool called TextFooler that uses adversarial text to test robustness of natural language models. Other popular open source frameworks—such as the Adversarial Threat Landscape for AI Systems (ATLAS), developed by MITRE with support from Microsoft and a broad coalition of private sector companies—use real-world examples to catalog possible attacks and corresponding defenses across multiple industry verticals.
As the landscape of both adversarial attacks and defenses is rapidly evolving, organizations should invest in AI red teaming. Originating in the cybersecurity field, a "red team" (or "ethical hacker”) works to expose vulnerabilities with the objective of making a system stronger. These teams should operate independently to assure an objective review as a red team must be able to keep sensitive data secure, while being transparent about identifying risks. “Red teaming” is new to AI but can be traced back to stress testing exercises completed by the Department of Defense back in the 1960s largely for cybersecurity. Now, many large tech companies employ AI red teams to look for AI security vulnerabilities (figure 4).
The composition of a red team will depend on the needs of the organization. It may consist of software developers and data scientists or those more focused on human factors or insider threats. If an organization uses multiple models trained on datasets with the same distribution (often the case for large computer vision or language models), an adversarial AI specialist would be able to identify vulnerabilities to highly transferable attacks. However, with unique tabular data (rows and columns), launching a successful attack would require more brute force trial-and-error and would not require an expert.
### Share infographic
  * [ Share ](javascript:void\(0\))
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")


### Or copy link
Copy
Show More
### Secure the model development life cycle 
Historically, organizations have focused security budgets on protecting hardware and software against attacks. However, AI models themselves are susceptible to threats outside of the traditional hardware-software dichotomy. Traditional testing methods can assess model robustness against random inputs but do not account for the complexity of a targeted attack like data poisoning. One such technique, adversarial training, is a defense technique by which a model is retrained with “adversarial examples” (such as those used in a data poisoning) included in the training data set but with correct labels. This teaches the model to ignore noise and learn from unperturbed features. Adversarial training is, in fact, one of the most popular defense techniques, showing great promise in academic studies.
Yet, like many adversarial AI defenses, it also has its disadvantages—specifically, it can only be used to protect against known attacks. The value and weakness of each defense approach illustrates the importance of exploring adversarial AI across the ML life cycle and applying multiple defenses throughout. While some measures, such as adversarial training, can be utilized by AI/ML developers throughout model development, other defense techniques, such as input detection, can identify unexpected threats later. These can be especially useful in situations where the development team utilizes pretrained/prepackaged models and does not have access to the training phase of the model life cycle.
## Now is the time to start
Deploying AI applications, such as intelligent chatbots, into the real world can open the door to adversarial attacks. Combating these risks requires a joint effort by the leaders of data, technology, security, and talent teams. Risk-mitigating decisions should align with the AI/ML life cycle through an MLSecOps approach—for example, validating which training data is being used to retrain a chatbot. Furthermore, governance controls can be put into place to prevent attacks on privacy or thwart hackers attempting to access safeguarded private information.
With the expansions of open-source libraries and tools, fueling the so-called “democratization of AI,” there has also been a  _democratization of adversarial attacks,_ which are becoming increasingly automated. As AI algorithms are increasingly incorporated into business and mission processes, organizations need to monitor the developments and investments in this space to stay up to date on current AI security and make strategic investments to help protect their models.
#### Vinita Fordham
United States
### Vinita Fordham
United States
Vinita Fordham is a leader at Deloitte focused on emerging and disruptive technologies, specializing artificial intelligence in the Government sector. Her career has been focused on driving technological paradigm shifts including leading many initiatives applying new technologies to solve unique “business” challenges for government agencies as well as mid- and large-tier companies. Before joining Deloitte, Fordham was an senior executive in the US government, focusing on next-generation technologies and leading large-scale digital transformation efforts.
_vfordham@deloitte.com_
#### Allie Diehl
Deloitte United States
### Allie Diehl
Senior Consultant 
Deloitte United States
Allie Diehl is a senior consultant in Deloitte's Analytics & Cognitive practice focused on growing AI strategy and adoption across the federal government. She has lectured on AI at Georgetown University and helped design an advanced degree class. She graduated Phi Beta Kappa from The Johns Hopkins University with a double major in Economics and International Studies as a Hodson Scholar. She has previously worked as an equities research analyst and an actuarial analyst.
_aldiehl@deloitte.com_
#### Dr. David Caswell
United States
### Dr. David Caswell
Managing Director 
United States
Dr. David Caswell is a managing director in Deloitte Risk & Financial Advisory working within the Cyber portfolio across Defense, Security, and Justice (DS&J) accounts. Dr. Caswell has over 20 years of experience as a technologist specializing in artificial intelligence (AI) and cybersecurity. He focuses on leveraging AI and analytics to enable cybersecurity for the Defense, Security, and Justice sector. His PhD research from Stanford University’s management science and engineering program developed AI technique applications for national policy decisions.
_dcaswell@deloitte.com_
  * [ Share ](javascript:void\(0\))
    * [ linkedin ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "linkedin")
    * [ twitter ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "twitter")
    * [ facebook ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/adversarial-ai.html# "facebook")
  * [ Print ](javascript:window.print\(\); "Print")


###  Endnotes 
  1. Jing Cao, “[Microsoft takes AI bot ‘Tay’ offline after offensive remarks](https://www.bloomberg.com/news/articles/2016-03-24/microsoft-removes-racist-comments-from-millennial-focused-ai-bot?leadSource=uverify%20wall),” Bloomberg, March 24, 2016.
  2. Tasha Austin, et al.,_[Trustworthy open data for trustworthy AI: Opportunities and risks of using open data for AI](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/open-data-ai-explainable-trustworthy.html)_, Deloitte Insights, December 10, 2021.
  3. Chawin Sitawarin et al., [DARTS: Deceiving autonomous cars with toxic signs](https://arxiv.org/pdf/1802.06430.pdf), Princeton University and Purdue University, accessed March 15, 2023.
  4. Github, “[Azure/counterfit](https://github.com/Azure/counterfit),” accessed March 3, 2023.
  5. The National Institute of Technology and Standards (NIST) defines Adversarial AI as “concerned with the design of ML algorithms that can resist security challenges, the study of the capabilities of attackers, and the understanding of attack consequences; see: Elham Tabassi et al.,  _[A taxonomy and terminology of attacks and mitigations of adversarial machine learning](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8269-draft.pdf)_ , accessed March 3, 2023.
  6. US Government Accountability Office, [_Facial recognition technology: Current and planned uses by federal agencies_](https://www.gao.gov/assets/gao-21-526.pdf), August 21, 2023.
  7. GARD Project, “[Holistic evaluation of adversarial defenses](https://www.gardproject.org/),” accessed March 3, 2023.
  8. Eugene Neelou and Alex Polyakov, “The history of adversarial AI,” Hack in the Box Security Conference, accessed March 15, 2023.
  9. Federal Register, “[Maintaining American leadership in artificial intelligence](https://www.federalregister.gov/documents/2019/02/14/2019-02544/maintaining-american-leadership-in-artificial-intelligence),” February 14, 2019.
  10. Caitlin Pintavorn, “[Adversarial attacks and the future of secure AI](https://caitlinpintavorn.medium.com/ai-ml-security-startup-market-map-investment-thesis-4f54eaed4b98),” _Medium_ , April 8, 2020.
  11. Andrew Lohn and Wyatt Hoffman, “[How traditional vulnerability disclosure must adapt](https://cset.georgetown.edu/publication/securing-ai-how-traditional-vulnerability-disclosure-must-adapt/),” CSET, March 14, 2023.
  12. Jen DuBois, “The data scientist shortage in 2020,” Quanthub, 2020; Deloitte, “[Solving the cyber talent gap](https://www.deloitte.com/global/en/services/risk-advisory/blogs/solving-the-cyber-talent-gap.html),” January 28, 2021.
  13. In his landmark 2016 paper, _Leading adversarial AI_ , researcher Nicholas Carlini defines “robustness” as a neural network’s (type of AI/ML) ability to “reduce the success rate of current attacks’ ability to find adversarial examples.” See: Nicholas Carlini and David Wagner, Towards evaluating the robustness of neural networks, University of California, Berkely, March 22, 2017.
  14. Austin, et al., [_Trustworthy open data for trustworthy AI_](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/open-data-ai-explainable-trustworthy.html).
  15. Johns Hopkins Applied Physical Laboratory, “[APL and the intelligence community tackle malware in the age of AI](https://www.jhuapl.edu/news/news-releases/200828b-APL-IARPA-TrojAI),” press release, August 28, 2020.
  16. GitHub, ”[Jind11/TextFooler](https://github.com/jind11/TextFooler),” accessed March 14, 2023. 
  17. MITRE, “[MITRE ATLAS™](https://atlas.mitre.org/),” accessed March 3, 2023.
  18. For example, see Uri Shaham, Yutaro Yamada, and Sahand Negahban, [_Understanding adversarial training: Increasing local stability of neural nets through robust optimization_](https://arxiv.org/pdf/1511.05432.pdf), Yale University, January 16, 2016; also see, Aleksander Madry, et al., “[Towards deep learning models resistant to adversarial attacks](https://arxiv.org/abs/1706.06083),” Cornell University, September 4, 2019.


##### ENDNOTE
###  Acknowledgments 
The authors would like to thank **Josh Rachford** , **Joe Mariani** , and **Pankaj Kishnani** for their support in the development of the draft. The authors would also like thank **Tasha Austin** , **Mekala Ravichandran** , and **Bruce Chew** for providing their insights and thoughtful feedback on the draft.
Cover artwork: **Sonya Vasilieff**
### related content
### [ Support for US climate action softened even before landmark Inflation Reduction Act Amidst growing economic uncertainty, climate change legislation seems to be less of a priority, according to Deloitte’s Global Sustainability survey Article  2-min read ](https://www.deloitte.com/us/en/insights/topics/environmental-social-governance/inflation-reduction-act-esg.html)
### [ AI around the world This interactive analyzes and presents AI use cases across the globe to understand the key factors that contribute to successful AI projects. Article  ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/global-government-ai-case-studies.html)
### [ The future of learning in government To get the most out of learning and development, it should be designed around the learner. Here are five design principles that can help do just that and transform employee upskilling in the public sector. Article  16-min read ](https://www.deloitte.com/us/en/insights/industry/government-public-sector-services/future-of-learning-and-development.html)
## Here’s how we use cookies
Deloitte uses strictly necessary cookies and similar technologies to operate this website and to provide you with a more personalized user experience. In addition to strictly necessary cookies, Deloitte uses optional cookies to enhance and personalize your experience, analyze site usage and traffic sources to understand how visitors engage with our website, deliver relevant content or advertisements, and facilitate data sharing with analytics and advertising providers. When you arrived at this website, Deloitte may have placed strictly necessary cookies and optional analytics cookies on your device. By clicking "Accept all optional cookies", you agree to the placement of optional cookies on your device. You can manage your cookie preferences or withdraw your consent to the use of optional cookies at any time by clicking "Tailor your cookie preferences". If you disable and withdraw your consent to the use of optional analytics cookies, Deloitte will not continue to receive data from the optional analytics cookies placed when you arrived at the website. Depending on your selected cookie preferences, the full functionality or personalized user experience of this website may not be available. Learn more by visiting[Deloitte's Cookie Notice.](https://cookienotice.deloitte.com)
Accept all optional cookies  Decline all optional cookies
Tailor your cookie preferences
Opt-Out Request Honored
## Privacy preference center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change your default settings. [Cookie Notice](https://cookienotice.deloitte.com)
###  Manage consent preferences
#### Strictly necessary cookies
Always active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences or filling in forms.
Cookies Details
#### Analytics and performance cookies
Analytics and performance cookies Inactive
These cookies allow us to track analytics by counting visits and traffic sources so we can measure and improve the performance of our website. They may be set by us or by third party providers to help us to know which pages are the most and least popular and see how visitors move around the website.
Cookies Details
#### Functional cookies
Functional cookies Inactive
These cookies enable the website to provide enhanced functionality and personalization based on your interaction with the website. They may be set by us or by third party providers whose services we have added to our pages.
Cookies Details
#### Advertising and targeting cookies
Advertising and targeting cookies Inactive
These cookies may be set through our site by our advertising partners. They may be used by those partners to build a profile of your interests and show you relevant advertisements on other websites.
Cookies Details
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
  * checkbox label label


Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm choices