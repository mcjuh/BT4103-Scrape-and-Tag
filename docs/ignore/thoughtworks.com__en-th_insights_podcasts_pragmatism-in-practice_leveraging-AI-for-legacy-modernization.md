<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/leveraging-AI-for-legacy-modernization | Title: Leveraging AI for legacy modernization | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Leveraging AI for legacy modernization 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Karen Dumville | Podcast guest  Erik Doernenburg
October 15, 2024 | 19 min 08 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/leveraging-AI-for-legacy-modernization#transcript)
Listen on these platforms
## Brief summary
Many businesses struggle with outdated systems that impede progress and efficiency. In this episode, Erik shares insights on how AI-assisted software engineering, especially using Large Language Models (LLMs), can revolutionize legacy modernization. If you are a business leader, wanting to understand the benefits, challenges, and future prospects of this approach, this is the podcast for you
### **Episode highlights**
  * Erik describes software development as creative work, and a team sport, in which the technology landscape is always changing. We need to talk to multiple people. We need to learn new technologies.


  * He says large language models (LLMs) are excellent at modifying text, interacting with text, and taking text as input and producing output, which is why they can help us with many different software delivery tasks.


  * The benefit LLMs bring is that they can explain what code does, and can even describe the intent of what the code wants to achieve. This is a valuable benefit for software developers to understand an existing large code base with the aim of replacing or modernizing it.


  * LLMs, in conjunction with a reverse engineering tool, give developers a deep understanding into a code base they're not as familiar with. It can be hard to find people with the engineering skills that you would for this in a human-centric way.


  * To prepare to use AI in legacy modernization, it's crucial for data to be available in a format that allows it to be utilized by an AI system. 


  * Large language models are a technological breakthrough. They're giving us countless opportunities, but that doesn't automatically invalidate the tools that came before. The power lies in combining the newly-found power of the large language models with all the years' worth of reverse engineering, into an approach that ultimately makes modernization much faster.


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
### **Transcript**
**Karen Dumville: [00:00:00]** I am Karen Dumville, and I'm here today with Erik Doernenburg, CTO Europe at Thoughtworks, who is going to share some insights with us on how AI-assisted software engineering can revolutionize legacy modernization. Hi, Erik. Thank you for joining us today.
**Erik Doernenburg:** Hi, Karen. Glad to be here.
**Karen:** Well, let's get started. Can you introduce yourself, and share a little bit about your background in software engineering and AI.
**Erik:** As you said Karen, I'm CTO of Europe at Thoughtworks, which means I'm a technologist. I have a background in software engineering and computer science. I've literally done AI since the 1990s. This has been around that long, and I've always been and therefore that's the reason why I'm at Thoughtworks. Always had the pioneer at an early wave of adaptors of new technologies, and I'm now seeing the application of GenAI, and large language models in software engineering as something that is currently state of the art.
**Karen:** Terrific, thank you. Let's jump in. Can you explain what AI-assisted software engineering entails, and describe the role of large language models, LLMs in this context?
**Erik:** Software development really is creative work. It's a team sport. The technology landscape changes all the time. We need to talk to multiple people. We need to learn new technologies. There's new concepts coming up. We need to process information. A lot of what we do with both the understanding of new technologies, but also the actual expression of what we want to program, what we want the computers, the systems to do is in textual form.
In the infrastructure today with infrastructure as code is everything is captured in text. By chance large language models are excellent at modifying text, at interacting with text, taking text as input and producing output. That's what not only we but many others have also noticed. That is why large language models can help us with any number of tasks while delivering software. Either new software or what we talk about today dealing with existing legacy [00:02:00] software.
**Karen:** Great. Just expanding on that, what specific advantages do large language models offer for legacy modernization particularly when compared to traditional methods?
**Erik:** When I talk about legacy modernization in this context, what I mean is taking your systems usually decades old. Like from the '90s usually mainframe systems, or say a Java-based system from that early wave of Java software in the early 2000s. Taking that and replacing it with new software. I'm not talking about changing the decades-old COBOL code, I'm talking about taking that system and creating a new piece of software. What the LLMs really do here, what they offer the traditional approaches can't do is, they can go through large amounts of information and summarize them.
For example, they can process the unstructured text. They can perceive connections in code that you would otherwise not necessarily see. I'm always giving that as an example. We talk about million lines of code in contexts like this. If you print a million lines of it wouldn't do it just to give you a sense of the size. If you print a code base with a million lines of code on paper, that's a stack of paper that is one and a half meters tall. If you're now saying, look through that or find all the places where certain policy is implemented, find all the connections between those.
As a human being, I literally can't read through the code base. I need to rely on something. So far we've often used tools that look at the structure or just as text, almost like you press Ctrl+F and search for something. The benefit the LLMs bring is that they have a deeper connection. They can explain what the code does, not only step by step, but to a certain extent, they can describe the intent of what the code wants to achieve and not every little step. That's really a huge benefit for software developers to understand an existing large code base with the aim of replacing or modernizing it.
**Karen: [00:04:00]** Sounds like a great benefit. In what ways can reverse engineering tools be integrated with LLMs to enhance and speed up legacy modernization?
**Erik:** That's an excellent question, and that is something that we've learned over the past year I would say. Initially, the assumption was that you could just feed information into a large language model, and the model would answer the questions. That gave a lot of different issues in the end. One of them were these threaded hallucinations where the model would make up things that weren't actually correct. Also it wouldn't really be concise enough in their answers, especially when it comes to understanding code bases.
What we've seen as an industry in many different areas is a pattern, and computer science people call it RAG, Retrieval-Augmented Generation. That is a way that allows us to nudge the large language model in the right direction by giving it specific information that we find with other means usually with a search. Then that way help the large language model to come up with better answers and approach. By the way that reduces the hallucinations too. It's not even an absolute minimum, it's not really in that area of application an issue at all anymore.
What we then said is, okay, if we take the large language model and we need to feed it additional information in this RAG, in this retrieval-augmented generation approach, where does the additional information come from? The simple approach is, and that is being used when you're writing new software outside legacy modernization, anything that the software developer, the engineer has opened in the editors, and take all those windows and feed that as additional context. With legacy modernization, that is not the best approach.
What we've seen is we've used traditional as you said, Karen, reverse engineering tools that understand at a structural level the old source code. We are pre-processing this before we actually begin the modernization, stick that into another system, [00:06:00] a database in technical terms, and use that information as input to this retrieval augmented generation step. We are basically taking the proverbial best of both worlds. We're taking the structural understanding that existing reverse engineering tools have, but we combine it with that higher-level understanding that an LLM can give us.
The combination of both has really helped us to understand existing code bases better and especially that's something we didn't talk about so far. A lot of the old code is written in languages. The mainframes often programmed in COBOL that many software developers today are not so familiar with. That again is something where the reverse engineering tool can unearth the underlying structure, and the large language model then on top can help the developers understand how that code works.
We assume of course that today's software engineers master today's tools, and write the new software. The large language model in conjunction with the reverse engineering tool really gives the developers a deep understanding into a code base into technology that they're not as familiar with. It's often hard, to be honest with you, to find people with the engineering skills that you would need to do this in a human-centric way.
**Karen:** Brilliant. Now, my next question is a two-part question. What practical advice would you offer to developers and companies looking to adopt AI-powered approaches for legacy modernization? How can developers and companies prepare to effectively use large language models for legacy modernization?
**Erik:** Let's start with the second part of the question maybe. When it comes to preparation, it is often making the data available in the first place. As we see in many other areas of the use of AI, of GenAI solutions, the data is often not in a format that allows it to be utilized by an AI-based system. When we are talking about legacy modernization, [00:08:00] make sure that the source code is actually accessible to the AI solution. Make sure that you have a tool that can-- we talked about the reverse engineering tools that can actually understand the programming environment that you have.
We had this with a client in the UK recently. They were using specific dialect of the COBOL language, and we first needed to figure out a tool that could actually parse, understand, and ingest the information there. Make sure that you have those in place. Documentation I mentioned before. If you can try to figure out what is the right documentation. Oftentimes when a system is 20-year-old, you have documentation, and you don't really know anymore is that the right documentation?
You might even find that the documentation contradicts itself. That there's a document from the 1990s that says something different from 2010, and you don't know which is right. You can even use an LLM maybe to find out these cases, or you could actually try to figure out, does the documentation contradict what is in the code. So doing that. As a last thing that you could do to prepare is to have automated tests.
That can be a difficult thing to achieve, and I'm saying don't do this just to do it. If you can and there's a good way of doing it, maybe have a number of end-to-end tests that you can keep running to see if you're making tweaks to the software if you want to validate a hypothesis on the old code that you can make sure that you're not breaking functionality. That is more, I wouldn't say a bonus. It's something that should consider, but not do blindly.
Whereas getting your information available, the documentation ready to be fed into the large language model or the source code of course and the reverse engineering tools that of course is a must. In answer to the first part of your question on the practical advice, do not expect shortcuts. There is no system, at least to my knowledge and based on everything I've seen, that will completely translate the software for you.
The practical advice is take the large language model, take the GenAI-based system [00:10:00] as a guide, as something that helps you navigate the old code. Familiarize yourself to a level that did make sense to you, that old code. Of course, as I said before, you don't have to know it in detail because the combination of reverse engineering tool together with a large language model will actually support you very well in that.
**Karen:** Great, thank you. Moving on to a slightly different topic. What ethical considerations should organizations keep in mind when utilizing large language models for legacy modernization?
**Erik:** Yes, that's of course a topic that often comes up, and rightly so in the use of any AI system. I would say the good news here in this field of software engineering is that we are not struggling as much with the ethical problems here. A lot of the standard problems that you see in machine learning models, for example, bias in the training data is not so much an issue here. In fact, I would argue bias in the training data could be an advantage in this case.
If you will, in the same way as we all have our own idiosyncrasies when we speak a natural language, organizations will have a certain style, a whole style of writing code. Certain patterns that they prefer, the development team prefer. If you now have a language model that is biased towards those patterns, it sees in the code. It is actually here a benefit because you want to replicate that bias that you have in the system. Whereas of course in other systems that we have where we're dealing with personal information or financial data, then we don't want that bias.
One of the bigger problems really isn't here anymore. Another big problem of course from an ethics perspective is the in transparency or opaqueness of the decision-making process. This was of course in the press even years ago about using AI-based systems or algorithms for making credit decisions. Then of course as a financial institution, you would be obliged, I would assume so anyway, to be able to explain how a credit decision was arrived at.
[00:12:00] When we talk about legacy modernization, that in turn is not an issue really because as a software developer, I don't care, to be honest. As long as the model can tell me, the combined system can tell me where I can find the pieces of code that deal with a policy, I'm happy because that's what I need to replicate. I do not really necessarily or actually not at all care about how the system arrived at that. That's the second one that is not really an issue. The third and last one that I'm going to talk about are hallucinations.
The hallucinations, as I said before, are really minimized by the use of the retrieval augmented generation pattern. The answers the system is giving are really-- and they are that prone to hallucinations because of the approach. In the end, if it spits out something that doesn't work, it doesn't work, you know what I mean? It's obvious because it's program code and you can understand it that way. I would say a lot of the ethical concerns that we normally need to take into account when we want to use an AI-based solution don't really apply in this field.
**Karen:** That's definitely a benefit for people. How do you anticipate the role of large language models in legacy modernization changing over the next few years?
**Erik:** I think what we have done in the past years, we've understand the broad direction that we need to go in. I wouldn't necessarily expect a major change in the way those tools are set up. What I described before, the idea that you take a foundational model and retrieval augmented generation, that pairing, is a pattern that I don't necessarily see changing. We have understood this, it works, it works in other fields and it works really well here. The combination with traditional structural reverse engineering tools is also something we've discovered and it has proven itself.
I think that broad direction of using the tools and that kind of combination is something will be here to stay. What will change is the [00:14:00] experience. We will learn more about the experience, we will fine-tune the approach, we will get more detailed data over the years that can help us refine how we do this. The broad direction will be similar. I don't want to get too technical in this podcast, there are areas when it comes to the programming patterns, something that is called select and carry, for example, while using the so-called window size, the context for the prompt. These are areas where we need to investigate and experiment.
For example, is a larger window more information always better, or is it better to do pre-selection and send a smaller set of data to the large language model? That again, that's what I meant with the tuning. These are areas that I think will evolve. One last aspect that is relevant that can change and is likely to change is where the large language model is running. At the moment, it is very common and for the right reasons to use a foundational language model.
Training your own models is usually, especially in this area, really not worth it. It's very expensive, it's difficult, it's hard to get enough training data. What we are using are these foundational models and they usually run in the cloud. For many organizations that's not an issue. They run business software in the cloud. They have software-as-a-service solutions that holds their data in the cloud. In other areas, it may not be so easy, and there's also in certain organizations a hesitation to move things into the cloud.
Of course in legacy modernization, you're talking about the crown jewels, the source code of your mainframe systems. Some organizations are, for the right or wrong reasons, reluctant to do so. What we are seeing is coming from the consumer space, actually a trend towards, so-called small language models. Small is-- well, the size of our brains still not small at all. It's still quite large, but it is a language model that can run on a powerful workstation for a developer or on a single server [00:16:00] that is maybe on-premise in an organization.
The small language models are interested in the consumer industry is driving them to run them on the phones, on Android phones, on iPhones, on the new so-called Copilot PCs that Microsoft has just on build. That innovation we can take to bring some of the approaches to legacy monetization from the large language models, the small language models. If anything, what we are seeing at the moment from the consumer approaches, it may actually work.
The small language models obviously are not as powerful as the large ones, but some of the limitations they have might even be beneficial. The limitations they have might not be so bad so to speak, that we can't use them. That's maybe an area where we see some change, that we'll see a switch from these gigantic foundational large language models to small language models that can then be run locally. Then you don't have any issues with compliance, et cetera because you can control the environment in which these tools are running entirely.
**Karen:** Terrific. Some insights on things to come. Just to wrap up now, what are the top three insights you would share about large language models, generative AI, and their impact on legacy modernization?
**Erik:** The first one, I can't overstate it enough. It is not going to be a tool that does direct translation. Do not expect this magic machine that you feed COBOL code and that spits out contemporary code. It is a tool in the toolbox of software engineering teams that do the modernization. It still will accelerate the work they're doing significantly, and it will also get us over the skills shortage of people who know the legacy technologies. It is a tool for experienced development teams, not a magic translator.
The other two hail a little bit in comparison, and here I'm showing that I'm a software engineer, so they're a bit more technical. One of them, as I mentioned before, is the application of retrieval augmented generation. That is really something that I can't stress enough. That is [00:18:00] exactly how you want to do it. Do not expect to train your own model, take a foundational model and use retrieval augmented generation. Then as a third point, combine that with traditional approaches.
Large language models are a breakthrough. They're giving us opportunities we didn't have, but that doesn't automatically invalidate the tools that came before it. The real power lies in combining them, in combining the newly-found power of the large language models with all the engineering and decade's worth of reverse engineering, combining them into an approach that ultimately makes modernization so much faster.
**Karen:** Thank you, Erik. I really appreciate your time today and sharing your thoughts on this topic. Thank you for our listeners in joining for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcasts. Or if you enjoyed the show, help spread the word by rating us on your preferred podcast platform. Thank you, Erik.
**Erik:** Thank you.
**[music]**
**[END OF AUDIO]**
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
More episodes 
Episode name 
Published 
From Ferrari to AI-powered banking: How Piergiorgio Grossi is building innovation at speed at Credem 
August 27, 2026 
Why AI alone won't modernize legacy systems 
August 13, 2026 
Designing the technology organization of the future 
July 23, 2026 
AI and the workforce: Beyond efficiency to real value creation 
April 23, 2026 
The velocity trap: Why GenAI is exposing broken foundations 
April 08, 2026 
Navigating the messy middle: A guide to real product organization transformation 
March 26, 2026 
The soul in the system: Humanizing AI Strategy 
November 24, 2025 
Measuring what matters in the age of AI 
September 16, 2025 
From bronze bullets to big impact: AI-first software delivery 
July 30, 2025 
Powering innovation: Thoughtworks’ AI journey 
April 25, 2025 
The change agent’s playbook: How to lead bold transformations 
March 26, 2025 
The ethics of data 
March 12, 2025 
The human side of data 
February 25, 2025 
The foundations of data strategy 
February 11, 2025 
European Health Data Space: The future of healthcare 
January 28, 2025 
Product innovation: Charting your own course 
January 14, 2025 
Revolutionizing data: How PAYBACK transformed with data mesh 
December 09, 2024 
Leveraging AI for legacy modernization 
October 15, 2024 
From crisis to confidence: Building reliable IT systems 
October 04, 2024 
Cross-domain collaboration: Removing barriers to data 
September 12, 2024 
Building a future-ready tech organization: Vialto's blueprint for success 
August 28, 2024 
Data modernization in action: Lessons from The Crown Estate 
August 15, 2024 
Authenticity in action: Cultivating a culture of respect 
May 15, 2024 
Beyond barriers: How AI is overcoming language barriers and driving inclusion 
April 24, 2024 
Wealth management transformation: Not just a destination 
March 27, 2024 
Future Fit Strategy: Transforming Falabella with Technology 
February 26, 2024 
How to become a truly customer-centric organization 
January 29, 2024 
Product thinking: More than just ‘product’ 
January 10, 2024 
The power of product thinking 
December 04, 2023 
From stagnation to success: Unleashing the power of technology and business transformation 
November 27, 2023 
Head & heart: The art of modern leadership 
November 06, 2023 
Tech-enabled sustainability: Closing the execution gap 
October 24, 2023 
From analog to AI: Embracing human-centered AI strategy. 
September 04, 2023 
The real cost of tech debt for your business - and how to fix it. 
April 05, 2023 
How to win the innovation challenge 
March 02, 2023 
How action shapes thought 
November 09, 2022 
Leveraging full potentials 
October 05, 2022 
Wicked intelligence 
September 08, 2022 
People and partners in modernization success 
June 27, 2022 
Backstage: Spotify's secret to developer effectiveness 
June 13, 2022 
Unlocking business value with the ITV Data Mesh playbook 
May 26, 2022 
The future of digital payments 
April 28, 2022 
Decision science to build resilient supply chains 
April 12, 2022 
The power of data and tech in the public sector 
March 23, 2022 
Accessibility for business value 
March 02, 2022 
Digital sustainability and the 2040 corporate pledge 
February 09, 2022 
Healthcare tech trends put patient at the center 
January 26, 2022 
Product thinking in the new era of cloud 
October 27, 2021 
CIO Interview: A digital mission for social impact 
September 28, 2021 
The value of creative AI 
September 14, 2021 
Data governance: The foundation of data-driven organizations 
July 28, 2021 
Technology proficiency: the new imperative for business growth 
July 15, 2021 
ABCD Model for Leadership: Drive 
June 30, 2021 
ABCD Model for Leadership: Curiosity 
June 23, 2021 
ABCD Model for Leadership: Belonging 
June 16, 2021 
ABCD Model for Leadership: Awareness 
June 09, 2021 
CX: Building a customer engagement framework 
May 27, 2021 
Data-Driven with Data Mesh 
May 13, 2021 
Green cloud optimization: Reduce your digital footprint, increase your bottom line 
April 21, 2021 
Looking Glass report: Tech trends and advice for your enterprise 
April 06, 2021 
The journey to enterprise modernization starts with value 
March 17, 2021 
Driving innovation with connected devices 
March 09, 2021 
Evolving the culture for an agile workforce 
March 02, 2021 
Moving the needle in technology leadership: Focusing on customer success 
February 15, 2021 
No-code platforms and the art of the possible 
February 03, 2021 
Resilience, curiosity and belonging: The drivers of successful change. 
January 12, 2021 
Building a strong data foundation to power tomorrow’s public healthcare services 
December 10, 2020 
Tech Concepts Every Exec Should Know 
November 19, 2020 
Building Business Resilience in the Cloud Era 
August 28, 2020 
Bridging the Gap: Bringing Technology into the Boardroom 
July 08, 2020 
Risk Management for Building Robust Organizations 
May 22, 2020 
Solving the Legacy Dilemma 
May 07, 2020 
Reimagining Value Delivery with Blockchain 
February 14, 2020 
Creating a Product Organization Within Your Business 
January 17, 2020 
The Collaboration Blind Spot 
December 13, 2019 
Creating an Online to Offline Mindset 
November 22, 2019 
Small Changes, Big Effects 
November 08, 2019 
Unlocking the Power of Customer Experience Data 
October 25, 2019 
Edge: Value-Driven Digital Transformation 
October 11, 2019 
Digital Fluency: Becoming a Modern Digital Business 
September 26, 2019 
Building Products with Purpose 
September 12, 2019 
Learning to Unlearn: Changing the Behaviors That Hold You Back 
August 29, 2019 
Harnessing Uncertainty to Survive Disruption 
August 22, 2019 
Digital Transformation: Disrupting the World of Fitness 
August 01, 2019 
Your Data Science Journey 
August 01, 2019 
The Future of Artificial Intelligence 
July 26, 2019 
## Don't miss out on the latest episodes. Subscribe today
[ Subscribe ](https://podcasts.apple.com/us/podcast/pragmatism-in-practice/id1474372829)
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