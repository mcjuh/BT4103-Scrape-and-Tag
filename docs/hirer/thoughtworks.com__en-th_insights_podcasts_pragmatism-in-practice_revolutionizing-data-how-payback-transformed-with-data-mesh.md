<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/revolutionizing-data-how-payback-transformed-with-data-mesh | Title: Revolutionizing data: How PAYBACK transformed with data mesh | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Revolutionizing data: How PAYBACK transformed with data mesh 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Karen Dumville | Podcast guest  Norbert Wirth
December 09, 2024 | 32 min 19 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/revolutionizing-data-how-payback-transformed-with-data-mesh#transcript)
Listen on these platforms
## Brief summary
In today’s fast-paced digital landscape, many companies struggle with outdated data architectures that hinder their ability to scale and innovate. VP of Data, Norbert Wirth, explores how PAYBACK transformed its data infrastructure by adopting a data mesh approach, revolutionizing the way they handle and leverage data. If you're a business leader or tech professional looking to understand how data mesh can enhance analytics speed, scalability, and drive better customer insights, this podcast is for you.
### **Episode highlights**
  * Norbert advocates for moving towards a more product-centered structure as a necessary precondition before starting to think about data mesh, with the decentralized concept of ownership and looking at data as a product.


  * Norbert suggests that a key success factor is to understand how to adopt data mesh to your own needs. 


  * With a centralized approach, data engineers are often detached from the business side, which can be frustrating for them. Data mesh can help to overcome this, empowering the people who handle the data to understand the respective business need. 


  * Norbert advises that if you're thinking of implementing a data mesh, you need to understand the concept first, then look at your own organization to see what aspects of data mesh are most important for your organization.


  * The concept of ownership can be the "biggest nut to crack". Norbert suggests that if your peers and the developers and the product owners are used to the old model where they're throwing any data-related request over the fence and the centralized team is taking care of it, it can be very hard for them to get into the mindset of owning data products. From a change management perspective, Norbert believes this is one of the biggest challenges.


  * Finally, Norbert concludes that data mesh shouldn't be viewed as an "off-the-shelf" solution. Instead it's a concept, an idea that requires a change in mindset. It has technology implications. It has impact on the ways of working for teams. With data mesh, Norbert advises that you need to get your head around the concept, and to understand that setting up a mesh alone will not do the trick. Establishing the right mindset and making sure people understand the benefits of this new approach are both key to data mesh success. 


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
### **Transcript**
[00:00:00] Karen Dumville: Welcome to Pragmatism in Practice, a podcast from Thoughtworks, where we share stories of practical approaches to becoming a modern digital business. I'm your host, Karen Dumville, and I'm here today with Norbert Wirth, VP of Data at PAYBACK. Hi, Norbert. Great to have you on the show today.
[00:00:19 Norbert Wirth: Hi. Great to be here.
[00:00:21] Karen: Great. Many of our listeners will be familiar with PAYBACK, but it would be great if you could share a little bit about the organization and your role.
[00:00:29] Norbert: Well, PAYBACK is a multi-partner loyalty program. What many people don't see, it's also a big marketing ecosystem. Obviously, we run a loyalty program for many, many partners. Consumers can basically collect points at many, many retailers and also online shops, and they can redeem these points. Yet at the same time, and that's the marketing platform side of it, we can then also address consumers with specific offers and specific marketing messages for our partners.
My role there, again, VP of Data, well, it's a large umbrella. I'm basically taking care of all our data engineering, but also the data science and machine learning engineering and AI side of things, and the whole analytics side. Like I said, it's a large umbrella, but I keep telling people, it's everything that should work closely together that sits in this data organization.
[00:01:30] Karen: Thanks for that, Norbert. Today we're talking about your journey to Data Mesh. What motivated PAYBACK to consider transitioning to a Data Mesh architecture?
[00:01:41] Norbert: The journey started quite a while ago. Back then, we had a really painful bottleneck in our data engineering team. We were operating a central data warehouse. We had a big data cluster, but all of that was centrally managed and historically grown. I think it's pretty obvious and many companies will experience that if such data infrastructures grow over time, you get a lot of complexity there. It's very hard to make any changes because of all the dependencies and so on and so forth.
At the end of the day, you end up with data assets that only real experts can touch because it's dangerous to make changes. Now I think on a positive note, it was very well managed on our side, but still we have this huge bottleneck. Any change request we had to implement for the business had to line up in the backlog. We had to prioritize sometimes really tough decisions to see what does the team work on next. Some changes we had to wait for quite a long time. That was a wee bit painful, I would say, for our business colleagues.
On the other hand side, back then, we were also aiming for a larger-scale transformation of how we develop our products and how we run our products. This for us was one of the main triggers, I would say. We went from a very well-side-oriented structure, again, must sound very familiar to some of our listeners, at least, to a much more product-centered structure. I would say that was really the necessary precondition to even start thinking about something like a data mesh with the decentralized concept of ownership and looking at data as a product. These were the main factors. I would say really the big pain was the bottleneck situation.
[00:03:41] Karen: What were the main challenges PAYBACK faced in its data infrastructure moving towards data mesh?
[00:03:47] Norbert: The centralistic legacy data operating model, even though it was very professionally managed and very well developed, it was this huge bottleneck. Since it was on-premise, we had to basically pay the always-on cost for the maximum capacity that we might ever need, which is very, very painful. We had growing complexity. Complexity was literally growing week over week over week. Every new change, every new fact that was added increased that complexity and made it harder to implement any smart changes that maybe should be done quickly.
Innovation was slowed down because, again, anything that affected the data assets had to line up in the backlog, and we had to find time and priority had to be negotiated so that the teams can work on it. I would say complexity, backlog, bottleneck situation, these were really the main challenges we were facing. Of course, you have to keep in mind that we are a very data-oriented company. For us, data is not a byproduct. We have enormous volumes of data that run through our organization, and therefore we really couldn't have a bottleneck in such a critical spot.
I would say, yes, these were the main, main challenges. Of course, still, it was, I would say, a brave decision to then say, "Okay, let's go for a data mesh," because one of the benefits of a centrally managed approach is, yes, you have the professionals taking care of it. With the right governance in place and with real professional development standards in place, it is safe, even though it's slow. It was still a brave decision, I would say, moving towards data mesh.
[00:05:42] Karen: Yes. It sounds like it was a non-negotiable for you. Why did you believe that it would solve your challenges, and how did you assess some of the potential benefits?
[00:05:53] Norbert: At the end of the day, we had to find something that would be a good fit to the overall transformation journey we were on. Again, we moved away from a tech silo approach, where each change was basically handed from team to team to team, and every team would just do their bit, again, dealing with their technology. To something that would be suitable for a concept where teams really own their products comprehensively or holistically, I should say.
We were back then already thinking of introducing a very product-centered structure with multidisciplinary teams, and the idea that these teams could handle their products real end to end. Then, of course, if you look at the options that you have, if you have to decide about a new data operating model, data mesh is almost a natural choice. However, it's also worth mentioning that back then we couldn't find many other companies that already had experience with data mesh.
We really had to think about the ways to adopt the concept and so on. I'm sure we'll dive a little deeper into that because that was really, really important for us. I would say it's a key success factor to understand how you have to adopt data mesh to your own needs. Another key point that I was hoping for was to resolve this dilemma that with a centralized approach, your data engineers are always detached from the business side. That's utterly frustrating for them.
They work really hard, they're super professional, they're wonderful people, but every now and then a request pops up and they really don't understand, they can't understand why are we actually doing this. Then again, with a centralized model, you have to sort of establish a connection to the business colleagues, you have to ask them to explain, no one ever has time, it's very cumbersome. Again, I would call this really one of the central dilemmas of centralized data operating models.
The big hope, again, with data mesh was to overcome this, and get people who handle the data and really implement new things in a data operating model, also understand the respective business need. Why? Because you create smaller units where everyone sees why are we doing this? What are we aiming for? What's going to be the output, and ultimately even what's going to be the business impact. Why is this going to make things better? Why is this going to have a bottom-line impact or a top line impact even?
[00:08:38] Karen: Talking a little bit about cloud now. What role did cloud technology play in enabling the data mesh architecture at PAYBACK?
[00:08:46] Norbert: Well, I would say it had a huge impact. Again, back then, this was also one of the main strategic decisions that we took that we were basically trying to leave mostly the on-prem infrastructure behind and move to the cloud. We had a couple of hopes, I would say, related to the cloud. One big hope, of course, was to be able and simply use available services. Not building everything yourself or not being hooked up with a software infrastructure provider.
Again, with always-on costs that you can hardly manage to something where we can basically leverage services as we need them and don't have to reinvent or build everything on our own. Of course, one big factor related to the cloud and especially thinking of moving all our data assets was elasticity. The cloud is elastic, sounds a bit weird, but of course, if you need more capacity, you can have it. I mentioned earlier, we have enormous amounts of data running through our organization.
Elasticity for us was a key factor. In the old world, we were always limited by the bare metal that we had. In the cloud, this problem would have been gone. I would say, yes, cloud was a, was a huge driver. It made it sort of very promising. I also have to mention that the cloud move also made things slightly more challenging because at the end of the day, we did various modernization steps at the same time. We moved from a centralized data operating model towards a data mesh structure that we had to adapt to our needs.
We moved from on prem infrastructure to a cloud infrastructure. One shouldn't underestimate, again, that both are major transformations and you really have to deal with it. You need to do the upscaling on the cloud technology. You need to change people's mindset regarding how to run a data mesh and how to behave in the data mesh environment. Overall, yes, cloud was a huge enabler and is a huge enabler, but also was an additional challenge, especially regarding the upscaling.
[00:11:09] Karen: You touched on a little bit before about how you had customized data mesh a little bit and made it more specific to your situation there, PAYBACK. Can you talk a little bit more to that? How did you adjust data mesh to fit PAYBACKs unique needs?
[00:11:25] Norbert: That's a really good question. I would say, the obvious point is that if you think of implementing a data mesh, you need to understand it first. Understand the concept and then look at your own organization to see what of that is really very important for us. What do we need to tweak? It really makes sense for us. It will work for us. One key element from our perspective was that we take the platform idea of data mesh very, very serious.
Again, I mentioned data for us is key. Data is at the core of what we're doing. It was pretty clear that we can't just say, okay, now we switched to data mesh. Every team implement your data products however you like. That would have led to chaos and would have given me a lot of sleepless nights, I would say. Therefore we realized that the platform aspect of data mesh is key and platform not in a sense, here's a set platform that does everything for you.
Platform really more in a sense, here's a toolbox and these tools are fine to use. Please, if you feel like you want to do things differently, talk to us first. We have to see whether that fits. Again, platform was a key element, platform in a sense of toolbox. We also realized that for us, the discoverability, again, given all the data that we have, the different data assets, discoverability is a very important component. It was pretty clear that without a proper data catalog, that really makes it easy for teams across the organization to find data assets, we couldn't even start implementing a data mesh. The data catalog had to be there and functional very, very early. Again, these two aspects are more prioritization steps that we took versus the concept because back then if you were reading about the idea of data mesh, no one could tell you have to start with this and then you do that, and then you do that. We have to learn really where to start and what's key for us. What's very, very important.
I would say the biggest adjustment that we made was that we understood we need to work with tiers of self-serve readiness. This probably needs a little bit more explanation. Obviously, we have large teams of really professional data engineers. For them setting up data products, if the tooling is right, it's not rocket science. What we were aiming for was that also a full stack developer can easily set up a, I would say more basic data product. We had different skill levels in the organization and in these teams.
We therefore came up with the idea that we basically distinguish four different tiers to see how ready is a team to already work with the data mesh. Most basic level is they're not ready. Let's face it. They need full support. They can't do anything on their own. Then the tier number two would be a team that sort of can do first steps, can take ownership, and so on. Tier number three would be, they can do most things on their own using the available tools.
Tier number four would basically be. they are fully capable of operating and developing in a data mesh setup. These tiers could be picked team by team, so that not all teams have to be on exactly the same level. Quite frankly, even many, many months or even years now down the road, that's still relevant. It's still important to appreciate that not all teams are on the same level and can act fully independently.
Last but not least, one of the key things we learned when we sort of adopted data mesh to our needs was that the concept of ownership is probably the biggest nut to crack. If your peers and the developers and the product owners are used to the old model where they're basically just throwing any data-related request over the fence and the centralized team is taking care of it, it's very hard for them to get into this mindset of, I own my data products. This required a lot of discussions, a lot of work. That was from a change management perspective, I would say probably the biggest nut to crack across the whole organization.
[00:16:15] Karen: Sounds like a really great approach. Now that it's implemented how has the implementation of data mesh at PAYBACK enhanced the speed and scalability of analytics to drive better customer insights and operational efficiency?
[00:16:32] Norbert: All right. Even though I'm by default a very optimistic person, and I would say, yes, we see it works really well, but I would say it's still a little bit early days to really judge. What we do see is we see data products that have been successfully set up, and we see how this makes people's life a lot easier. We've gained speed from here is a need for a data product to this data product is life. This journey is a lot faster than it was in the old days, again, where a team couldn't do anything independently. I would say that's a huge efficiency gain that we see.
I'm fairly optimistic that, again, once all teams are really fully operational and we're also finally done with all the migration steps, this is going to be the biggest impact that simply a team can be active on their own. Can create their own data products without waiting for other things to be resolved that sit in the backlog of the central team. This, again, the speed element I think is a key element. Another huge benefit I see is that the data mesh makes dependencies a lot more visible. If all data sits in a central data asset, over time you have incredible dependencies.
This table depends on 20 other tables and so on and so forth. It gets hugely, hugely complex. If you disentangle that, and that's what we start seeing now really, and you have distinct data products where it's clear how one data product, for example, a source-aligned data product communicates with a consumer-aligned data product. These dependencies become a lot more visible and clearer, and that also makes it somehow easier to manage them.
[00:18:39] Karen: Just expanding on that in terms of talking about data products, in what ways does transitioning to a data product mindset contribute to PAYBACK's transformation into a product delivery organization?
[00:18:52] Norbert: It's really been a necessary component of it. Again, we transitioned from the silo structure that I mentioned earlier to a very product-centered domain model. I still don't see how else we could have supported that from a data perspective. I would say it was a huge contributor because it's enabling teams to do their own things and also create their own data products from source-aligned, which is always the first step because it's relatively easy to consumer-aligned.
Let's just say a team is developing an application or a product, and this product is producing data. Now, the source-aligned data product is a very clean step to make that data available to the rest of the organization, and that can now, with the data mesh approach, it can easily be implemented. In most cases even directly by the team, or in more complex cases still with the support of a central data engineering team.
Then turning that into a data product that, for example, talks to business users or even external users to create a consumer-aligned data product. is also possible for the teams themselves. It was heavily consistent with the whole idea of the product-centered domain model. I would, again, have a hard time seeing what other operating model could have supported it so well.
[00:20:23] Karen: Thinking a little bit about the future, how does data mesh adoption support PAYBACK's future growth and innovation within its data-centric strategy?
[00:20:32] Norbert: it's no secret that if you want to innovate, if you want to come up with new products, be it AI products, be it some sort of more traditional machine learning or data science-type products, or even more generic applications, it's been very hard often to get hold of the right data.
I would say with this new structure, we've really massively improved discoverability and we made it much easier to find the right data needed for your specific use case or your idea. I would really say it helps us to innovate faster, and it makes the data side of innovation clearer and more transparent. Now key element here is obviously the data catalog, and I mentioned that earlier. For us, it was very clear from the get-go we need a good data catalog, otherwise, it's not going to work.
Now with this setup, the teams can spend more time on model development, they can spend more time on thinking about the application they want to build. If I obviously think of Gen AI cases that we're working on or Gen AI use cases that we have in mind, for example, with the implementation of rack architectures. Thinking of data products, the AIR is very, very beneficial because you can make it clear with the rack architecture, what does my model have to be connected to?
You have distinct data products that really serve as an important source here. I'd say overall, mesh can really be a significant facilitator for innovation, especially by improving discoverability, but also making it very clear what distinct data assets do I have, what do I want to connect to? It's not just a big, big thing and you need to sort of find the data that you're looking for. It's really clear. It's those two data products that I need. Overall, huge enabler and helps teams to focus on the actual innovation.
[00:22:48] Karen: Great. Now, moving to teams and the idea of people, they're always such an important aspect of any project. How did you manage the team support and the cultural change during this transformation?
[00:23:01] Norbert: That's really a big one. I would say at the beginning, there was very much explaining and very much sort of offering trainings and so on and so forth, but also showing the benefits. People want to understand why are we doing this. You can't just say, here's the strategic decision. We move towards data mesh, la, la, la, do a corporate broadcast, and hope that everyone gets it and then they will sort of work in that direction. No, you really, really can't.
On all levels, you need to educate people. I would say in particular amongst the data engineers because again, they're very, very professional people. At PAYBACK they're doing an amazing job, but again, for them, it was a huge mindset shift. Moving away from these very well-maintained central data assets to a structure where they were maybe at fear of losing control to some extent. We really had to explain over and over again, what's the idea and how do we adopt it to our needs.
I think one of the things that really helped was that we were always very clear. We're not doing a textbook implementation or a naive implementation of a data mesh. We're looking very carefully at what we need and what suits us. That's the path we'll choose that help people to really sort of accept the idea and then also get excited about the idea. There was also a lot of change management needed with the product teams. Because as I mentioned earlier, they were not used to that.
They were not used to taking ownership. Also on that front, you had to do a lot of explaining and a lot of trainings and sometimes also convincing, I have to say. Because again, it's easy to throw a request over the fence and then just complain that it takes so long. Just saying, now, okay, we changed that. You can take ownership, but then you also have to really do things. You have to develop and you have to run it on your own. That is something you will only accept if you understand why is that good for me and how does that help me.
Again, the benefits, you have to be very, very clear about those. Overall, I would say, yes, communication, explaining training is key and not taking things for granted. For example, yes, mesh propagates, consider data as a product and ultimately we talk about implementing data products and then running them. This terminology for many people doesn't make any sense. For data experts, it does, but for a product owner or for a developer, they don't understand what you mean by that.
I think it's really key to step back and sort of look at that message through the eyes of the receiving person and really find the right language to explain what do we actually mean. How does that work? To really help people get their head around it. Because I think at the end of the day, people want to understand why are we doing this. You need to explain it to them in their own language. Then when they get it, they will get excited about it. Then they're motivated to walk in that direction.
[00:26:26] Karen: That makes a lot of sense. Now, I know you've authored a great white paper, which I've seen, and I think it's on thoughtworks.com. we'll link that here somewhere in the material. What advice or learnings would you share with other organizations considering data mesh adoption at this point?
[00:26:47] Norbert: The important advice probably goes back to where we started. You can't just look at something like data mesh as an off-the-shelf solution. It's a concept, it's an idea that requires a change in mindset. It has technology implications. It has impact on the way of working for teams. It's really not like what many, I would say, software vendors promise you. Buy my software. It solves all the problems for you and you will be in a happy place.
Which by the way, is often over-promising as we know. With data mesh, you have to really get your head around the concept, and you have to understand that setting up a mesh alone will not do the trick. Transforming the legacy structures, that's a big challenge. Establishing the right mindset and make people understand what are the benefits of this new approach. That's really key. You can't successfully implement a data mesh if there's no organization that is ready to handle it.
Some form of product centricity, some set up where teams really own the products they do end to end and understand why they're doing it. That's a good setup to be successful with a data mesh implementation. If an organization is, for example, totally centralized in every sense. All the other development work is still structured in tech silos, then the idea to launch a data mesh it's not a good one. It's not going to be successful.
On the organizational side and also in the tech setup, you need the right infrastructure and the right mindsets so that the mesh can actually work. Therefore, again, maybe key advice from our perspective for data-heavy organizations, the platform aspect of the data mesh, the self-serve platform aspect has to be taken very, very serious. I wouldn't feel comfortable with teams just implementing data products however they think fit.
I also think a data catalog to really ensure discoverability is a key element of the data mesh because you will have a distributed setup later on. You will have to make it very easy for teams to find what they're looking for. Last but not least, and I had many discussions on that topic. Governance structures are very, very important and should be taken very, very serious because the initial data mesh papers, they were always talking about this federated computational governance.
I think many people just read that and thought, wow, interesting concept probably means that you automate governance or whatever, and then it's good. No, it's not. Governance is something you need to really think about and you need to come up with ways and ideas to involve different stakeholders in, for example, a governance council. That's what we've launched.
For example, you need to come up with rules that are convincing. How can a rule be convincing? Because with the rule, you also communicate why are we doing it and why is it beneficial. I think aspects like this have to be taken serious. Again, I wouldn't advise that anyone should try a naive mesh implementation if the organization is not ready for it and if they're not willing to really see how they can adapt it to their specific needs.
[00:30:35] Karen: Lots of good advice there. Thank you, Norbert. One final question for you, a bit of a future-facing question. How do you think data is going to evolve in PAYBACK?
[00:30:46] Norbert: For us, it's pretty obvious that the relevance of data will increase even further in the future. We're together with our partners, with all these retailers that we're working with closely. We have so many ideas to leverage data that we haven't even tapped into in the past because of bottleneck problems and so on. We are always after creating a more revolving consumer experience. All this, in our case, is data-driven.
It's pretty obvious that the relevance of data will increase even further and I don't see a point where this would stop. I think this is an ongoing challenge for us, but it's also super motivating for my teams and for me. No matter whether you look at data engineers or data scientists or AI engineers or whatever, it's heavily motivating for them because they see what contribution they can make also to the future success of, again, PAYBACK and our partners. Yes, it's going to be even more relevant.
[00:31:50] Karen: Terrific. Sounds like you've got a lot in front of you. That's all we have time for today, Norbert. Thank you so much for joining me and our listeners for this chat. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcasts. If you enjoyed the show, help spread the word by rating us on your preferred podcast platform. Thank you, Norbert.
[00:32:13] Norbert: Thank you very much. Bye.
[END OF AUDIO]
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