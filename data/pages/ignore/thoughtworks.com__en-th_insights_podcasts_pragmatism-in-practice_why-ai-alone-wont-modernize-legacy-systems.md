<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/why-ai-alone-wont-modernize-legacy-systems | Title: Why AI alone won't modernize legacy systems | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Why AI alone won't modernize legacy systems 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Christina Stathopoulos | Podcast guest  Shodhan Sheth and Alessio Ferri
August 13, 2026 | 30 min 21 sec 
Listen on these platforms
## Brief summary
AI is rapidly reshaping enterprise tech conversations, but successfully transforming legacy architecture requires far more than just automated code generation and powerful models. 
In this episode, host Christina Stathopoulos joins Thoughtworks' Shodhan Sheth, Enterprise Modernization Platform and Cloud Lead, and Alessio Ferri, Lead Software Engineer, to discuss how technology leaders can balance AI innovation with engineering discipline, organizational change and real-world governance.
_(Originally hosted on EM360’s Tech Transformed podcast.)_
**Transcript** [00:00:00] Intro: Hello and welcome to a special episode of Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. Now, today's episode was originally aired on Enterprise Management 360's Tech Transformed podcast. Host Christina Stathopoulos is joined by my Thoughtworks colleagues, Shodhan Sheth and Alessio Ferri, to tackle a critical issue for tech leaders, modernizing legacy systems with AI. They discuss why AI isn't a silver bullet, how to safely build guardrails for AI in production, and why winning team buy-in is just as important as the technology itself. Without further ado, let's hear their conversation. 
[00:00:56] Christina Stathopoulos: Welcome to Tech Transformed, the podcast that explores how technology is reshaping the enterprise landscape. I'm your host, Christina Stathopoulos, founder of Dare to Data. AI is changing the conversation around legacy modernization, but successful transformation requires much more than powerful models and automated code generation. It demands things like engineering expertise, governance, and especially a clear understanding of where AI delivers value and where it doesn't. 
Joining me today to unpack this topic are Shodhan Sheth, enterprise modernization platform and cloud lead, as well as Alessio Ferri, lead software engineer. Both are part of Thoughtworks' global legacy modernization service development team, where they focus on applying AI to modernize complex enterprise systems. Shodhan and Alessio, welcome to the show. It's fantastic to have you both here today. To kick it off, could you each introduce yourselves, tell our listeners a little bit about your backgrounds, your roles within Thoughtworks, as well as briefly how you're applying AI to enterprise transformation. Let's kick it off with Shodhan. 
[00:02:10] Shodhan Sheth: Thanks, Christina. Great to be here. As you mentioned, we work in the capacity of being responsible for our global modernization solutioning for our customers. One of the big areas we work in modernization is core system modernization, which has always been the need of the hour, but has always been off-putting for businesses because it tends to be time-consuming, high effort, and generally comes with a big price sticker on top of it. Effectively, the last two, three years, what we've been trying to focus on is how we can use AI to make that journey for our customers cheaper, faster and lower risk. 
[00:02:53] Christina: Perfect. We're going to dive right into that today first. What about you, Alessio? 
[00:02:59] Alessio Ferri: Sure. Hi, Christina. Glad to be here. Thank you for inviting me. I'm Alessio Ferri. I'm a lead developer at Thoughtworks. Joined the company about four years ago, and I come from a background of software development. I've been doing legacy modernization for a long time now. Since joining Thoughtworks, I have looked at applying the latest and greatest of the technologies that we have in our toolbox to make these kind of engagements possible with our clients, really tackle the core problems that legacy systems bring for our clients. 
[00:03:36] Christina: Building on that piece about AI and enterprise transformation, it's true there's no shortage of headlines suggesting that AI can transform legacy modernization practically overnight. From your perspective, Shodhan, how can technology leaders distinguish between all of this marketing hype versus practical, measurable applications that actually create value for the business? 
[00:04:00] Shodhan: Before I answer the actual question, maybe something I'd like to add is that I find a lot of times people ignore things that are hyped because they think it's just hype or be obsessed about things that are hype. I think the answer is somewhere in the middle. I often say that value and hype are not exclusive. Hype can just absolutely mean that the value is out-promised. There still might be value in something that's hype. I think that's an important consideration. 
In terms of your actual question, my mental model is that most things can be judged by a cost-time value equation, and so that's what I ask leaders to do. I think I basically ask them to keep two things in mind. Understand problem-solution fitness, so understand the problem that they're trying to solve and if it's fit for a solution. Too often, people have a tendency to use a solution for any problem, and we've seen lots of those things in the past where blockchain was a solution to every problem, or [unintelligible 00:05:03] was a solution to every problem. Then part two is have realistic expectations on that time-cost-value equation I'm talking about. Again, they don't have to be super scientific about it. Can do some back of the paper napkin math and figure out if that equation is in their favor or not. 
[00:05:21] Christina: I liked how you distinguish between-- first, you said that there's mainly two different types of people, those that just ignore the hype because it is hype, or those that just become almost obsessed with it. You say that there is a middle point here. Also distinguishing-- saying that even amongst the hype, there can be value there. Then you have to evaluate that. You have to start with the problem, understand the solution. Perfect. I think underneath many of these conversations with enterprise leaders is a fundamental technical challenge. I want to shift the conversation a little bit. 
Generative AI systems are inherently probabilistic, while enterprise software has traditionally been built around deterministic, predictable behavior. From an engineering standpoint, Alessio, what does that tension look like in practice, because we're practically talking about opposite ends of the spectrum, probabilistic versus deterministic? Also, how should developers think about approaching this in a responsible way, especially when they're dealing with enterprise software? 
[00:06:28] Alessio: I think there's some confusion I'd like to touch upon because I think there's very different applications of AI when building, for example, enterprise systems or even non-enterprise systems, which is on one end, I might use AI to build the stuff that then I deploy in production. On the other end, I might deploy instead AI within the things that I'm running in production. Those are very different. They require very different operating modes and guardrailing around. 
For example, I could ask a model to go and draft an architecture for an application that I want to build or even generate the code of the thing that I'm building. Those are problem spaces where it doesn't really matter if every time I ask these questions to the AI, the output is slightly different because I still operate as a software engineer. I still sit within the loop, and I can still judge, and I can review, and I can run deterministic tests, and I can integrate with our CI pipeline with the things that other developers are building and make sure that everything is still passing and green. 
In that case, for example, we're using AI as a technology that helps us deliver traditional software in the way we've always delivered software in the past decades. There is a lot of harnessing around the coding tools, the coding agents that developers use to ultimately create the solutions that they run in production. 
On the other end, and that's where people get nervous, is when I deploy, instead, AI within the system that I'm running in production. People get nervous because, honestly, because of that non-predictability nature of the technology. Although I would like to say that I think it's one of the greatest strength of this technology, the fact that it's very flexible and adaptable to many circumstances that we might not have accounted for for the system that we build and run in production. I think one practical advice that I would give developers is not try to make the model deterministic, but instead provide it with the tools that allow it to operate safely and reliably, and potentially even with repeatability built within it. 
I'd like to give an example. If I'm, for example, a customer on a marketplace and I'm looking for a product that I want to purchase, and that product happens to be out of stock, in a traditional system for doing cross-selling, we'd have to build the rules within the system so that it would suggest similar products, and then the customer would go and buy it. Those edge cases are a burden for developers because we need to build all of these edge cases up front. We need to think of them up front. AI could, for example, deal with situations like this where it realizes, "Oh, okay. This product is out of stock. I can suggest another product so I can still fulfill the order from the customer." 
There's different spectrums as to how much I employ AI in these, for example, contexts. I might, for example, apply AI to discover a path that works and guardrail it with inventory services and stuff that allows the AI to suggest things that actually exist and are available to purchase. Once a path has been discovered, that path could be codified so that it can be repeated over and over and over for many other customers. That is a much more repeatable pattern than instead, for example, applying AI every time at runtime to suggest products. 
Clearly, there is a cost aspect as well. AI is much more expensive than traditional compute on servers that these applications run on. Also, you we lose that repeatability aspect, and that requires a series of guardrails in which the AI operates in production, such as, for example, ensuring that the workflows that the AI operates within are durable. Every time the AI is employed, we can't always predict what it's going to do. We need to build workflows that are durable where they can be resumed, they can go back and retry actions that have previously failed because AI was employed. 
That's why I like to think of AI in a much safer way, to think about it as explore first and then codify so that that path that's proven to work can be repeated over and over in a much safer way. 
[00:10:55] Christina: You made that important distinction between using AI to help you as a software developer versus when you're actually embedding AI into the workflows, into the system. To clarify, it sounds like that second choice is more where the real complexity comes in, because that's where you have to add in the guardrails, you've got to make, as you said, somewhat repeatable or predictable systems, but still within that having the probabilistic options that it can be flexible and present even things that we didn't consider. 
It's interesting because a lot of conversations, discussions about AI modernization, they usually start with the technology itself. Even now we're speaking a lot about the tech that we have, but in practice, a successful transformation depends just as much on things like people, processes, and governance. It's not just about integrating AI into a software stack. I'd like to hear from both of you on this one because I think it's quite important. What parts of the modernization journey tend to be underestimated? What do you think about that, Shodhan? 
[00:12:02] Shodhan: I think there's an old adage, "Technology is always the simplest problem to solve." The people process problems tend to be harder to solve. That's because in technology, we've always achieved a hard degree of automation. By definition, if you can automate and repeat those things, they become easy, because you keep learning from mistakes and you've, at some granularity, learned from as many mistakes as you could. Which is why I think the people process side is so hard. 
I'd also say there's two novelties in the modernization journey in addition to the fact that people process side was harder. One is what we've already talked about. How we conduct software delivery has changed, how we conduct modernization has also changed. That also uses a lot of agentic approaches. Two, the end state of modernization has also changed. When the CSPs came, the end state of modernization was being cloud-native. Now the end state of modernization is some level of agentic in your product. All of these changes are happening at rapid pace and any form of change is hard, and because this just relentless space of change, I think it makes it even harder for people and processes. 
I think with everything, again, I like the CSP example a lot. CSPs democratize access to compute. Then a few years later, there was FinOps because people were spending money like crazy. There are similar cycles that have to happen in this space as well. Tokens is a big topic now. It wasn't a topic one year ago in terms of the amount and the financial amount of money that's being spent. I think there are lots of these things that are changing, and it's important that leaders have empathy that any form of change is hard and this is just a super cycle of change. I think that makes it super harder. 
[00:14:19] Christina: Alessio, do you have anything to add on or maybe to elaborate on one of these points? 
[00:14:25] Alessio: Yes, I think something to build on what Shodhan said. I'm sure that if we look at agents and legacy modernization on Google, we will get a lot of posts that talk about the fact that these coding agents can understand code and rewrite it and modernize it. As Shodhan said, that's not really the hardest part because when we think about legacy modernization, especially when we look at code, code doesn't really tell us the intent of a system. For us to modernize, we need to able to express intent and how we want to change that intent. What code tells us is how something has been built. It doesn't tell us the why or even what. The what is something that we need to discern from the how it's built. Then we need to go up even higher and say, but why have we built it this way? For us to really be able to effectively modernize a legacy system, we need to have these answers, which unfortunately don't lie in code. That is really a complex thing that can't just be addressed by generating or analyzing code on its own. 
What we tended to do before AI, and we still do today, is access documentation because usually that's where you would see, you would understand the intent. Even user stories that have been written to generate that system, over time, if user stories existed, would even tell you why am I doing something? What is the persona in here? What am I trying to create in terms of value for that persona? If we have access to all this information, then great, that helps us a lot. Unfortunately, in reality, many times documentation is stale, and it doesn't really reflect that part. It doesn't really give us those answers, and so we always tend to fall back onto the subject matter experts within organizations so that they can help us build these mental models and understand the what and the why something has been done in that way. 
Honestly, accessing SMEs is very difficult because they're always very busy keeping these enterprise systems up and running as they should. Sometimes they're not even working in the organization anymore. They've left, they're retired, Shodhan and I work a lot on mainframe modernization. These are systems built 40, 50 years ago. It's difficult to find SMEs around that can answer many of the questions that we have. There's no doubt that AI can help with the reverse engineering, with the code generation, but we shouldn't forget about these other two questions, which are really important to effectively execute modernization. 
[00:17:10] Christina: They can help us with the how, but not the what and the why. That's where the SMEs come in. That's why documentation is so important. I think it's clear that modernization is just as much an organizational and even a leadership challenge as it is a technical one. All of this, I think, creates a very difficult balancing act for executives. 
On one hand, they're being pushed to move quickly and to unlock value from AI. Everybody's feeling that pressure today. On the other hand, they are still responsible for keeping these critical systems reliable, managing all of the risk that comes with that, and delivering predictable outcomes. This one's for you, Shodhan, what advice would you give CIOs and CTOs who are trying to navigate all of this? 
[00:17:59] Shodhan: I'll try to build up on some of the examples Alessio already used and the bit that we talked about of hype versus value. I think it's about sticking to the basics. I think I see three grooves of value when using GenAI. The first groove is in your SDLC process. You're still building similar software that you were building before, but you're using agentic tools and methodologies to build software. There's clear value there. If you've not started embracing some of those tools and approaches, start now. I think there's enough evidence out there to say that you don't need to-- it could be overhyped, but there's still value, as we said before. 
I think groove two is using agentic to improve your business process or improve the product you're delivering to your customers. I think that still there are limited cases. That's a very domain-specific, industry-specific question. I think that's still an area to explore. There's definitely areas where there have been positive results, but there's also definitely areas where there have been not-so-positive results. That's an area where harnesses need special attention because you still need to, as we've talked before, achieve repeatable, consistent, trustworthy outcomes, irrespective of the fact that somewhere in the kernel of that software, there's something that's non-deterministic. I think a lot of our conversation about problem-solution fitness harnesses is also applicable for this. 
Then the third groove is a bit out there, where there's nothing but an agent automatically discovers anything and everything. I feel that's more of the hype area right now. Of course, there could be a bleeding-edge startup or a lab doing that, but I don't think that's ready for enterprise adoption. It could be ready for exploration, but definitely not adoption. I ask my customers to think in that frame of mind. Software delivery, definitely get started. If it's about your business product, consider a bit more carefully, but there's definitely also value there. If it's a bit more like, "Oh, if everything should be agentic, be a bit careful about that. That feels not well thought-out. 
[00:20:24] Christina: It is linking back to what we had talked about earlier about understanding how to find the value within the hype. There might be some value there, but we also can't get over-obsessed or put all of our expectations into it. Now I think this is good advice for leaders that are thinking about where they need to place their bets. I'd like to bring this down even to a more practical level. You've both worked on applying AI to legacy systems as part of the Thoughtworks development initiatives. Without turning this into a product discussion, a lot of your work is very hands-on. For you in particular, Alessio, as a lead software engineer, what have you learned about building practical platforms and workflows that help teams move faster, but still keeping them in control? 
[00:21:12] Alessio: Yes, that's a difficult question, but I think what we've learned is understanding clarity of, having clarity of what it is that you want is one of the most important things. Allowing people, empowering people to be in control, in a loop that's non-deterministic, like when we are building software with AI requires people to have clarity of what they want to get out of something. That clarity is difficult to have because that demands to have a lot of upfront details that we don't know about yet. 
Traditionally, these things would be done by brainstorming with the team and figuring out the details as we go. Many times, we still need to employ that and we can't go and just kick off on AI without having that clarity built upfront by working together as a team, because otherwise there's too much room for the AI to do things that we don't notice, we don't know about, and we lose control of what it is that we're building even. 
Really, understanding and having clarity on what we want also helps us understand what we're going to get because if we have clarity of what we want, we are really best placed to judge, am I getting the things that I wanted? Which sounds basic, but it's not really, especially if I'm generating large amounts of code with AI. If I don't have that clarity upfront and I don't specify that, then it's much less likely that I'm going to be able to validate what is coming out. That really talks about the applying AI for software engineering, what Shodhan was saying earlier. 
Another thing that I think is super important of lesson learned that we've learned is don't be greedy. Yes, AI helps us move faster, but moving faster doesn't mean that we need to chew more than what we did before. We can still chew the same amounts that we were doing before and just move faster and iterate through those iterations much faster than before. That really keeps people in control. We're still building the same way as we were doing before, it's just a lot faster, those iterations. There is a side effect to that which we talk about, which is cognitive load. There's a lot of stuff that we need to keep in our head, a lot of quick decisions that we need to make as we are developing code nowadays, which is clearly challenging for developers. It's challenging for me. There's a lot of stuff that needs to be decided, almost on the spot. 
Another thing that I would say specifically for the stuff that we have built on the reverse engineering side of legacy systems is having traceability over the entire chain and obstructions. Being able to verify and trace back a claim that the AI is making in a piece of code that it's writing, where that claim comes from in terms of a product requirement document, where that claim is found in the legacy code, and having this entire traceable chain is very important because that's where evals, where all of these things can then operate in. Most importantly, not just evals, it allows developers to go back to the original source and spot check and, if required, to understand what it is that this modern part is replacing of the existing system. 
Abstractions, I would say, is the last as in abstractions have always been helpful to us, not just developers, but to us humans. We've always used abstractions so that we could compartmentalize complex things so that they could fit within our heads and we could reason with them. One of the things that's really empowered us in the things that we build is building those abstractions so that we can really empower both agents, but people most importantly, to understand large amounts of piece of information coming from potentially legacy systems, and empowering those peoples to digest that information, to reason through it. Abstractions and traceability, they're very connected things, but those are really the things that allow people to go faster but responsibly being able to trace back the entire chain. 
[00:25:45] Christina: Abstractions, traceability, and then even if I rewind back to that second point that you were making, I think there's lots of studies coming out recently where they're finding that people are just being very overloaded, like you said, the cognitive overload that we can't take more than we can chew, as you had mentioned. I think a lot of people are feeling the pressure that they should be taking more than they can chew because they have the AI there to help them. If you take too much, you still need to be there, like you said, to verify the output. You still have to apply your own expertise and ensure, and the context and your know-how, so we do need to be careful with that. 
Now, one thing that I think keeps coming up throughout our entire discussion today is just this pattern that the real value of AI comes from augmenting human expertise, not simply automating it. As we wrap up, one last question for the both of you. What's the one lesson you would most like our listeners to take away when it comes to using AI for legacy modernization? I'll throw it back to you, Alessio. 
[00:26:52] Alessio: I think for me one of the things that I always think about is the nature of the problem, like the problem fitness, the solution fitness that Shodhan was talking about. I think there's something around the fact of employing AI in places that accept or welcome more non-determinism in legacy modernization, for example. One of the things we started with was reverse engineering, because reverse engineering many times, even before AI, was a non-deterministic process.
I could go to an SME and ask a question, and then two days later ask the same question to the same SME and get a different answer, but the point is not so much about the answer that I'm getting on the spot, but it's the mental model that I'm building as I ask questions, as I read the code, as I read the documentation. I think, like in our case, for example, we focused on that because the nature of the problem really welcomed non-determinism and allowed people to build much faster those mental models that empower us to make the difficult and right decisions that are required for an enterprise to do modernization. 
[00:28:03] Christina: Okay, good point. What about you, Shodhan? What would be your advice? 
[00:28:07] Shodhan: I feel that I've seen a lot of obsession over the latest version of a new model, and I understand that context windows grow, and the models get more powerful, but actually the value unlock is in the harness that the human helps create. I often say, if there were no new versions of models, we still have enough innovation in that space to carry on for five years. To adopt this technology better, the focus needs to be on harness. As I know, I don't have access to version X of this model, which is the latest and greatest. I often ask people to focus on the problem, build a harness to solve that problem, and then all things will become easy. [00:28:50] Christina: Great advice from both of you. This brings us to the end of our episode. Shodhan and Alessio, thank you so much to both of you for sharing your insights, your expertise. I'm sure our listeners will have plenty of valuable takeaways from today's discussion. I know I took a lot of things away from this. As well, to our listeners, our Tech Transformed community, if you'd like to learn more about the topics that we covered, visit thoughtworks.com. Thanks so much for tuning in. If you found this episode valuable, please follow, rate, and share. Join the conversation on X and LinkedIn at EM360Tech, or visit our website for more expert insights. 
[00:29:31] Outro: What a great conversation. That just leaves me to say thank you for tuning in to this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcasts. As always, if you enjoyed the show today, please do help us to spread the word by rating us on your preferred podcast platform. We would be really grateful. Thank you, and we look forward to seeing you next time.
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