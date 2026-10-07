<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/unlocking-the-power-of-customer-experience-data | Title: Unlocking the Power of Customer Experience Data | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Unlocking the Power of Customer Experience Data 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Christoph Windheuser | Podcast guest  Radu Immenroth
October 25, 2019 | 24 min 11 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/unlocking-the-power-of-customer-experience-data#transcript)
Listen on these platforms
## Brief summary
Interest in data and what can be done with it has hit an all-time high, and organizations are rushing to capture more and more of it. In this episode, Christoph Windheuser, Global Lead of Intelligent Empowerment at Thoughtworks, interviews Questback CTO, Radu Immenroth to explore how Questback built the infrastructure needed to manage and use their vast amount of customer data.
**_Highlights_**
**Feedback data is about people’s thoughts and emotions,** how they experience specific situations, what they like, what they think will work in the future, and why they have done something. 
**Products are becoming more and more similar so for a lot of enterprises, customer experience is the key differentiating factor.** Feedback data, or experience management data, allows companies to measure the customer perception across a series of interactions, with the goal of closing any experience gaps. 
**The next generation of feedback software is infused with machine learning and artificial intelligence, making it smarter and more accessible to more people.** Questback is in the middle of it, delivering end-to-end software that gathers the data, does analysis, identifies insights, and recommends an action plan to fix any issues. 
**The use of AI and ML in feedback software allows Questback to scale the impact of human experts, it is not trying to replace them.** The bots need to be trained by the experts, and they will always phone home if a task is too hard to accomplish. 
**Questback creates feedback graphs which are built by experts and enriched with machine learning.** This combination of connectionist and symbolic approaches to AI is used similarly by Google, Facebook, LinkedIn and Salesforce to create knowledge graphs. 
**Quantitative feedback data is extremely important, but a lot of the true insight and aha moments come from comments or discussions.** Natural language processing and sentiment recognition make feedback easier for respondents, and are used to collect the data from comments, video, audio and biometrics. 
**We truly believe that the feedback data belongs to the respondents and to the organizations that got it.** We fully integrate GDPR rules into our data strategy and we follow the open data initiative to make it easy to take data out of our system and integrate it with your other data types including transactional, HR, CRM, and ERP. 
**Yes, digital transformation is about technology, but it’s actually more about people and enabling people to use technology.** It’s about agility, speed of innovation, being able to change course quickly, and try something out quickly. And from an organizational perspective, it’s about autonomous empowered teams. 
**Podcast Transcript**
**Sam:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. I'm your host, Sam Massey, and in this episode, Christoph Windheuser, Global Lead of Intelligent Empowerment at Thoughtworks, interviews Questback CTO, Radu Immenroth, to explore how Questback build the infrastructure needed to manage and use vast amounts of customer data. Enjoy.
**Christoph:** Welcome to a new episode of Pragmatism and Practice by Thoughtworks. Thoughtworks is a digital global consultancy company. In this podcast series we share stories of practical approaches to becoming a modern digital business.
My name is Christoph Windheuser and I'm the Global Head of Intelligence Department at Thoughtworks. Today I'm here with Radu Immenroth, CTO of Questback. Questback is an online survey and feedback software company. Questback provides the necessary feedback and insights from customers end to end employees that is at the heart of business success. Welcome Radu and thank you for joining us today.
**Radu Immenroth:** Hi Christoph. Thanks for having me. Looking forward to our discussion.
**Christoph** : Yeah, great. Maybe in the first place. Tell us a little bit more about Questback. For our listeners who may not be familiar with your organization.
**Radu Immenroth:** Sure, sure. So, we are a software service company. We're running in the cloud and we are basically gathering a specific type of data and then we help larger organizations. Typically, that's our customer base. Then we help them analyze the data and then take action based on the data.
So, what is the specific type of data? It is, as you rightly said, feedback data. So, data about what people think, feel, how they experience specific situations, what they like, what they dislike, what do you think will work or not work in the future, why they have done something or not to have done something, their thoughts, their emotions and so forth. So, this is the data that we are dealing with.
**Christoph:** Yeah, very interesting. Is this what we call experience management data? What is this exactly, what is the purpose of this? Why does it help companies?
**Radu Immenroth:** People relate to what we're doing more and more, speaking about experience management and about experience data. Actually so, and I would say if you compare the classical surveys, which were around 10-15 years ago due to the evolution into experience management, I think the key differentiator is that you are basically measuring the perception, the customer or employee perception, across the journey across a series of interactions between the people in the organization.
And, you monitor all these experience, you aggregate the data and then you basically show experience gaps. So, on a customer side, just imagine a journey where a customer does research online and interacts with your webpage or with your source of information online. It goes to the store, tries to find the product in the store, buys the product, installs the product, if it's something that needs to be installed.
Maybe, has some issues, calls a call center, gets the problem fixed. So, this would be a typical journey of a customer and customer experience management. In this case, would measure each and every interaction and would identify where maybe experience gaps can be found. And, basically with the goal of closing this experience gaps.
Because what we are seeing, I mean, especially in the customer infogix, speaking about costumer experience. Actually, the experience becomes the, almost the only source of differentiation in for a lot of enterprises. The products are becoming more and more similar so the differentiating factor becomes the experience. Basically, delivering a superior experience.
So, this is what this can be, I mean this is on a customer side and the employee side. You can think of a similar journey. You can think about somebody being recruited, being onboarded, joining the first projects, experiences that work with the team. You can look at it in a similar way. Measure all this experience, touch points, identify gaps and close them, in order to deliver actual superior experience in a differentiating source.
**Christoph Wind:** Oh, very cool. That sounds exciting. So, what is the Questback way of doing this? What is your secret sauce or how do you stand out on this experience management?
**Radu Immenroth:** Hmm. Yes. So, first of all, we deliver end to end. So, what we are helping with is the data gathering from a software perspective. We are helping with the analysis, with identifying insights into the data and we are delivering the actual planning, the follow up.
So, actually based on the insights. And, actually, the whole industry is actually on the verge of defining the new, a new next generation of feedback software and we are in the middle of it.
So, it is about software being smarter across all of this processes about the software being more accessible to more people. And, of course, what we're trying to do is we're trying to infuse machine learning, artificial intelligence in all these processes to make it smarter, to make it more accessible.
So, to give you some examples, if you're thinking of, let's start with the first part, the data gathering. I think of having an artificial intelligent powered assistant that could be a chatbot, could be whatever type of assistant that basically helps you with the data gathering.
So, you don't need to have an expert. You can actually have the chatbot for more simple feedback use cases that creates a survey for you based on your business goals. So, you just need to tell him what you would like to do and then the bot recommends the right feedback instrument, the right measurements topics, the right distribution channels and so forth.
Of course, what we're very conscious of is that we're not trying to replace the human, we are trying to scale, actually, the impact of experts because we know companies have these experts but they have a limited number and there are certain topics, which are easy to support.
And, those use cases, we want to support with artificial intelligence. And, of course, the bots need to be trained by these experts and the bot will always phone home. So, basically call the expert when there is a task which is too hard to accomplish.
So, it's about, you know, mastering like 50/60/70 percent of the very simple feedback cases where you need this expertise and can be provided about the artificial intelligence. So, but that's just the data and it gives you, if you're thinking further, the analysis, it's about joining, for example, data automatically knowing what matches.
It's about identifying automatically relevant points to look at. It's about identifying outliers, identifying interesting things to look at because you don't want to look at everything otherwise it's just not looking amongst reporting. It's about more defining on specific things, about trying to pick out the relevant information. And then, for the action planning, you can think about recommendations, what should you do. It's about organizing, orchestrating sessions with the teams to come up with the right action plan to fix certain issues that you have identified based on the insights of the feedback insights.
**Christoph** : That is a lot of interesting, very interesting stuff. Let's look a little bit more technical in detail. You said the basis for everything, of course, is data. You're gathering data from your customers. You're working on this data and producing new insights and information based on that data. Tell us a little bit about your data infrastructure. How do you do this? How are you organized internally to manage all this kind of data?
**Radu Immenroth:** Yeah, exactly. I mean without data there is no AI, right? So yeah, if you, again, if you're thinking about how surveys used to be a few years ago, you are thinking of every silo used to all the survey.
So, you want to do a customer survey, you would run it, it's out there for a month, you close it down, you, maybe, you export the data, report on it and then distribute the PowerPoints or the PDFs to the managers that need to see it and then it disappears somewhere on a comp board or on a digital comp board.
This next generation, this smartness needs data that is, that it won't break up the silos. So, think of, think about this example with the journey, right? On the customer side, you have 4/5/6/7 different surveys. They need to be joined together. So, you have the full journey analysis possible.
So, saying on the employee side, one way of doing this is we have developed a feedback data platform. And, in this feedback data platform, you can easily join data that has been collected separately and you can enrich it with mental data so it's more easily to harvest it and to find insight across.
And, this needs to be, of course, a self service data platform so it needs to be an enabler for old type of further teams that use the data either to suck it up in the enterprise data warehouse, for example, to connect it with transactional data.
And, here we're trying to basically to clean the data and to prepare it in the best possible way so it's as easy as possible to integrate it with other data or transactional data, say a state, HR data, CRM data, ERP data.
So, this is one important part of the data platform. And, on the other side, of course, we need to open up for data scientists and that can do artificial intelligence machine learning. They're modelling, directly, the data on a vast amount of data.
Last, but not least, we know we are in Europe, we are a European company. We have European customers and we have GDPR in place so we need to make sure that we are fully following the rules there. So, you have the right to be forgotten, you need to be conscious, you can't merge data without telling the customer or the respondent, actually. So, you need to actually to ask for permission to do this early on. And, this is part of our data strategy. We are fully supporting this process and I'm making it easy for enterprise to organizations to do this.
**Christoph** : Great. You mentioned that you have a lot of feedback data. This is kind of high level knowledge you have, which you gain from your customers and your feedback forms and do your work on this and then you, I think you create actions out of this recommendations for the customers. How do you manage this knowledge? Is this in a database? How does this work?
**Radu Immenroth:** Yeah, that's a good question. So, I think what I'm observing is where I'm observing like two different streams in artificial intelligence. One is the ones that truly believe only in machine learning and in, you know, all answers are in the data. And then, there are the other ones who believe in, actually trying to model the reality with experts. But, also what I'm seeing is that successful companies like Google, like Facebook, like LinkedIn, like Salesforce, are using a combined approach.
So, they basically use, on the one side, knowledge engineering with knowledge graphs. I think a lot of people know that Google is using a knowledge graph as a foundation for their search, which initially it is built by experts and then they enrich it with machine learning, with data found in the real world where you do your neural networks and so forth.
And, this is what we do as well. So, we have created the so called feedback graphs, which is a knowledge graph just like Google's or Facebook's knowledge graph. And, we use this to enrich data that is gathered from people in the real world and this gives us the best of both worlds. You could also say that we used the knowledge graphs to buy us our machine learning models so we can actually do machine learning more precise on a smaller amount of data. So, this is, yeah, in a nutshell.
**Christoph** : Wow. Wow. That's pretty cool. Because I know the research area and the combination of connectionism approach and AI and more symbolic approach and knowledge graphs. That is a hot research topic that's a lot of work going on. That's a really exciting area.
Let me ask something else in AI, another area where we do a huge progress at the moment and lots of things going on is natural language processing. And, I imagine your feedback data, these are not just check boxes, but you also will have a lot of free texts from customers and clients in this. And, this question is, are you using natural language processing techniques in AI to manage and work on that?
**Radu Immenroth:** Yes, but let me share a little bit more. So, indeed actually more and more feedback comments are unstructured. And, we see that, yes, the quantitative data so the likert scales, the five point scales and so forth are still extremely important. But a lot of the true insight, like the true aha moments where you really get the epiphany and understand something, often comes from comments or from discussions.
So, and, of course, we need to give this source of information, of insight to our customers. And, we use NLP for this. For, yes, of course, for comments and discussions. But, what we also see is a lot of, like, spoken feedback, right? More and more feedback comes per video or audio.
**Radu Immenroth:** So, we do it on transcription and then we do NLP on top of it. We are basically, I mean if we step back a little bit, the whole feedback industry, is moving from just using the five point scales to using other titles data.
Like, you know, data from your watch, maybe, that is delivering a biometric data or face recognition or more relevant for us sentiment recognition on the face or in the voice. So, we are generalizing our feedback instruments and this is part of the next generation of all feedback tools and I think this is part of the, again, behind that is actually our, we're trying to make feedback easier and smarter also for respondents because what we see is we have conflicted interest here.
We have a group of people that wants to have more and more feedback and then we have the respondents, which are bombarded with surveys. So, and this is a conflict, right? So, how do we fix this? We need to make sure that we protect the respondent as well. You know, we need to make sure that if you told me yesterday how satisfied you are working at Saltworks then I don't need, within one survey, that I don't need to ask you today again within another survey the same question.
So, maybe, I can remember that you stated this yesterday and I could just use your answer then. Of course, I need to ask you beforehand if this is okay for you. But, so reusing feedback, making feedback leaner, you know, getting quick pieces of feedback from you instead of a questionnaire where you need 15 minutes to go through it. Just a piece of, you know, spoken feedback. Just smiley. Just at the end of the week, how was your week? It was great because, and then as a short comment. So, we're trying to make feedback easier for respondents as well. And, NLP is an important part of this.
**Christoph** : Yeah, cool. This brings me to another question, when you want to get this feedback as smart, as easy as possible, you know there are other kind of data in an organization, which is the transactional data.
So, when you asked about, for example, a customer order or somebody bought something, you also have this information about the order. Is this the kind of transactional data you have usually in your ERP system? Are you also taking advantage of this data and is this going together with your feedback data to have a complete view on the transaction and the feedback on that transaction?
**Radu Immenroth:** Hmm. Yes, that's an excellent point because, of course, this type of data belongs together. So, you have the transactional operational data from your CRM system, your sales information or financial information, your cost information, your production information, which is a lot about the what. And then, you have the feedback information in it, which is about the why. Why has something happened, why hasn't sales team achieved their sales targets? Maybe they haven't been trained or they don't like their boss or something is wrong in the team or whatever.
So, this type of explanation, why, it belongs naturally to the what and yes we are able to suck in a certain amount of, a certain type of data and amount of transactional data into our data platform, but we don't want to be the aggregator of all data. That's not our business.
We are, basically, our core business is feedback and it's made me rather the other way round. If you really want to do in-depth analysis, let's give you an example. So, the same state you could integrate into our system would be, we have a lot of airline customers would be the frequent flyer status. That is a piece of information that you typically can suck in, but if you want to have a very detailed, granular information about what flight somebody was on, what went wrong, what didn't go wrong. This is more in the system and transactional systems and then we rather suggest that you maybe use your existing data warehouse or your data platform where you have all of your data in there and you're just suck in our aggregated feedback data in there and do the analysis across.
Important point is that we truly believe that the data belongs to the respondents and to the organizations that got it. So, we don't try to lock you in into our platform. This is really a strategy that we have. I's the opposite, we want you to take advantage of the data that you own. So, we make it very, very easy to take data out of our system and integrate it, analyze it with transactional operational data.
**Christoph** : Are you using open standards because I imagine you get data from a lot of different vendors, different systems and have to integrate this data.
**Radu Immenroth:** Yes, absolutely. So, we are now following very closely the open data initiative that was founded by my Microsoft, Adobe and a couple of other big players in the market. And, we are following that.
Basically, it's a mental data definition so you will know that an account that is defined in Microsoft Dynamics will be the same that an account defined in our feedback system because we use the same meta data. So, we're trying to follow this open data initiative to make it easier to integrate.
**Christoph** : Cool. Great. And, we are coming to the end of our podcast and one question, by the way. I think Questback, as you told us, is really a digital business already so that's all what you're doing. You're creating businesses digital value out of data to your clients. What would be your recommendations to other companies, which are on their way to become a modern digital business? What is important on that way?
**Radu Immenroth:** Yeah, that's a good question. I think we had some lessons learned there as well. Maybe, the most important insight is that the digital business, digital transformation is not so much about technology. Yes, it is about technology, but it's actually more about people and enabling people to use that technology. So, it's about agility, speed of innovation, being able to change course quickly, try out something quickly. And, from an organization perspective it's about autonomous empowered teams and it's about, of course, we use feedback internally as well.
So, we need to identify, are the teams that are working with technology truly autonomous? Are there any impediments? Do they need more organizational support? Is there anything that we can do to increase autonomy on the empowerment of these teams? And, this is the starting point.
And then, of course, you have the technology that needs to support us. From a software perspective, we are talking about microservices architectures, which make it more easier for autonomous teams to build software separately. We're talking about infrastructure as a service where you don't need to wait six months to get into a specific infrastructure set up, but you just have it instantly. We're talking about the experimentation platform. So, of course, the technology needs to follow. But for me, the key thing is to bring autonomy and empowerment towards the teams.
**Christoph** : Yeah. Cool. So, what are you doing to build your next generation tools for the future of Questback?
**Radu Immenroth:** All of what I just said. So, of course we're trying to establish just organizational set up. We are building the software infrastructure and we are, this is part of the plan to create smarter, actually the next generation of feedbacks. Smarter feedback, more accessible feedback, less intrusive feedback, which gives you better insight and deeper insight and where it's easier to take action based on feedback.
**Christoph** : Okay, Radu thanks very, very much for your time. I think that was very inspiring for us and our listeners. Thanks a lot and much success on your journey till the next level of feedback.
**Radu Immenroth:** Thanks a lot Chris old friend. See you soon hopefully.
**Christoph** : See you soon. Bye bye.
**Sam:** Thank you for listening. If you enjoyed this episode, help spread the word by giving us a rating on iTunes, Spotify, or wherever you listen to your podcasts.
[ View full transcript ](javascript:void\(0\))
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
## Don't miss out on the latest episodes; subscribe today
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