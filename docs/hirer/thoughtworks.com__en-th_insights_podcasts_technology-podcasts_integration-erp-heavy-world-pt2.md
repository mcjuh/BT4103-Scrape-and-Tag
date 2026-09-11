<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/integration-erp-heavy-world-pt2 | Title: Integration challenges in an ERP-heavy world — Pt 2 | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Integration challenges in an ERP-heavy world — Pt 2 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Ashok Subramanian | Podcast guest  Aleksandar Serafimoski, Anastasia Belozertseva and Brandon Byars
November 12, 2020 | 39 min 39 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/integration-erp-heavy-world-pt2#transcript)
Listen on these platforms
## Brief summary
In the first part of this two-part episode, we looked at the challenges encountered when an agile software development mindset runs up against ERP-heavy integration environments. Here we look at some of the solutions that can ease the path toward legacy modernization.
**Podcast transcript**
Ashok Subramanian:
Hello, and welcome to this edition of the Thoughtworks Technology Podcast. I'm one of your regular co-hosts, Ashok Subramanian.
Neal Ford:
And hi, I'm Neal Ford, one of your other regular co-hosts. And we are joined, or I should say rejoined today by three of our colleagues. I'll let them introduce themselves, starting with Anastasia.
Anastasia Belozertseva:
Hi everyone. My name is Anastasia Belozertseva. I am a developer with Thoughtworks. I've been with Thoughtworks for around eight years, and I've been on all sorts of different engagements in this time.
Brandon Byers:
Hi, I am Brandon Byers. I'm a technology director at Thoughtworks, approaching 13 years in.
Aleksandar Serafimoski:
Hello, this is Aleksandar Surfmosky, I am a lead consultant at Thoughtworks working as a developer. I've been at Thoughtworks for eight years, and I'm out of the Chicago office.
Neal Ford:
And you may recognize those voices because we have done a podcast with this group before talking about some of the challenges encountered when dealing in an agile software development mindset with a ERP heavy integration environments. And our last episode, which is not required listening for here, but will certainly give you some context, gave an overview of a lot of the challenges you face in those kind of environments. Today, we want to focus more on the solutions to some of those challenges, and some ways to work around some of those problems.
Ashok Subramanian:
And just to give our listeners some context of the probably space and what we're discussing, Anastasia and Aleksandar, want to describe and give maybe a 30 second summary of the context and problem space before we start discussing what your experience and lessons learned in this were?
Aleksandar Serafimoski:
Yeah. So the context from the previous meeting, where we talked about some of the journey and what were the challenges that we faced was that Anastasia myself and Brandon worked at a Fortune 10 energy company that had a highly customized ERP system. Which basically created a lot of challenges for them in order to innovate and build new products based on the data that was captured in their ERP system. When we initially came in, we were tasked with coming up with a strategy on, how do we expose this data that can be consumed by different consumers in different applications that they were building, while being able to move quickly and then decrease some of the cost? And so that's where our recommendation was moving from point to point solutions to reusable APIs that can be easily reused, well-documented and self-service so that teams can grab the data that they need, they can innovate, and they can do it all by themselves without needing to find the right person and communicate with them.
Ashok Subramanian:
Great. Thank you. I think that's a really good context to start off the conversation. Yeah, so you were describing in our last conversation about using APIs as a strategy or technique to create these abstractions all with legacy, which allows teams to start moving more rapidly than they were able to previously. And you describe some of the techniques that you had used. So what were some of the learnings or your experience along the way?
Aleksandar Serafimoski:
Yeah, I can start. And I think probably Anastasia has some things that she wants to add. But I think the biggest learning that we face was that when executing this type of a strategy, there's not a silver bullet solution. So approaching everything pragmatically, analyzing the pros and cons, and understanding what is the solution that works for you the best, was one of the biggest learnings for me personally. I know Brandon, when we worked together, he's a big fan of the pros and cons tables. And we went and created a lot of those, which allowed us to evaluate different solutions and then understand what would be the best for us in a given context. I think the second learning point for me was the ability to communicate the strategy over and over again. Because when you're coming into organizations where they've done point to point solutions, there is a certain type of a mindset.
Aleksandar Serafimoski:
So taking people within that organization on the journey from one type of a mindset to another type of a mindset, was a journey that we executed and went through a couple of times. Because, as you know, these organizations are very big. And so you might go through this lessons with one department and then comes in another department that wants to use the data and they have the same questions. So being patient, taking people on a journey, and maybe even creating some advertising light reading material is definitely a good strategy for moving forward. Anastasia, do you have anything to add on top of that?
Anastasia Belozertseva:
Yeah, sure. I think there are a few things that I can think about. I think what is worth noting is, you mentioned having a strategy. And I think having ways to communicate a strategy is very important. So in our case, we leveraged an API style guide that was recorded in Git. We leveraged architecture decision records that were also recorded in Git. And we build a community of practice to share these learnings, socialize these learnings, and also have a way to also spread them outwards and communicate them to various teams involved.
Anastasia Belozertseva:
I think another learning that we had is agreeing on some key metrics. So your metrics of success for your various APIs. And agreeing on metrics that make sense to both the technical and the business audience. So for us, for example, what we thought was important is, first of all, keeping track of how many consumers we're able to help out. Also, what is the various functionality offered? So be it synchronous integration or asynchronous modes of integration with our services. And also some metrics when it comes to availability, your response correctness, as in how many air response your API is producing versus your regular 200 type of responses. And how available your API is, and what the uptime of it is.
Anastasia Belozertseva:
And also what are the performance metrics for each one of the end points? So, what are those SLIs that your consumers can expect from your API? So having those metrics and having a place in time during the cycle of UAPIs where you consistently record those metrics, but also socialize them with everyone involved with all of the stakeholders and consumers and such, I think is going to help you just spread awareness about the work that you're doing, the work that the teams are doing. And also will help you gain respect and just build rapport with your consumers.
Neal Ford:
So you're almost making it sound like the job of architects is to make pragmatic decisions and socialize them responsibly, rather than define silver bullets laying around. That's just an amazing perspective on architecture. Matches a reality, but not much of what you find in the press. But that is really the essence of the job is the social side of it is at least as important as the technology side. And silver bullets are rare.
Brandon Byers:
Yeah, I think the focus on silver bullets is interesting because one of the observations about working in organizations who have a long history with large, monolithic ERP systems, is it's not just a technology challenge, it's often times a cultural mindset challenge. And for a lot of these companies they legitimately are not software development organizations, and the ERPs run their business. But also that means that they have a history of buying COS products to run their business, even outside the ERP.
Brandon Byers:
One of the friction points that we had to overcome was thinking about, okay, so now we need to think about some interesting integration pathways. Well let's buy a product, let's bring in, hey, MuleSoft's an API product, let's bring in MuleSoft as an API product and have it solve our problems. And there's nothing wrong with MuleSoft, but what happened in practice is that people would use the ESB elements of MuleSoft for orchestration to grab data from system A and shovel it into system B, into all those APIs. And check the architectural box that says, "Hey, we've met the mandates for new integration patterns." And a lot of the effort that we had to do was say, yeah, you're not a software development company, but you're also not a math company.
Brandon Byers:
That doesn't mean that you don't rely on math to run a multi-billion dollar business. And likewise, you need to rely on some software development capabilities from a multi-billion dollar business. That you can still buy COS products and SAS products to bring in new capabilities, but you need to own the glue. And if you're really serious about providing agility in these different life cycles from the experiences that you're buying, than the ERP that underlies a lot of the data and capabilities that you need to support those experiences, then you need to think about these APIs as first first-class products with some software development capabilities to support them, rather than just making a product and a silver bullet consideration.
Neal Ford:
I think that's an important point that, I mean, you're building glue between these things, but it has to be responsible glue. One of the challenges I've seen in organizations like this is particularly in places that do things like manufacturing, they're used to buying manufacturing equipment, and it is really turnkey. They bring it and install it, and you turn the key on and it just works. But you'd never imagine them going, okay, we bought another piece of factory equipment and it doesn't have the kind of power we want. So crack into the power generator on that piece of equipment and splice on to it and supply power to the other one. You'd never see a company doing something like that because it's wildly irresponsible for that piece of equipment.
Neal Ford:
And yet you see the exact same kind of integration where, well, we can't really get that data, so just crack into its database and we'll just slurp the data directly out of it without thinking about the side effects of amperage and overload and other sorts of things that string as metaphor that I have. But a lot of this, I think, goes back to that cultural mindset of software is not like the other things they buy, which are much more self-contained products. And software, particularly when you integrate it, kind of leaks all over the place.
Brandon Byers:
But on the other hand, we also use that experience to our advantage. A metaphor that I used a few times in some of these sessions where we were trying to change mindsets was to talk about jump-starting my car battery. And I would say, it didn't start, so I'd pull my girlfriend's car next to it and open up the hood and look at the batteries. And then I have jumper cables. But what I didn't do is then peel off the rubber on the jumper cables, open up the battery, pull out my chemistry textbook to understand how anodes and cathodes work, and where to plug the wires in to start it. Because I had well-defined components with well-defined interfaces. We wanted the same thing for their integration, we wanted to take that same componentized mentality that they were used to in the example that you pulled out, Neal. And so you can think of your integration loop in a similar way so that every single integration isn't bespoke.
Ashok Subramanian:
I think it's also maybe a good reminder for one of the blips in the radar where we have ESB on hold. So I suppose your recommendation is still, continue with that recommendation even though it's probably about eight years old, still holds, right?
Brandon Byers:
It's aged well.
Neal Ford:
It's one of those tricky things though, because there is some nuance there. But Brandon actually got to the problem with ESBs and all those similar tools is the slippery slope problem. If you only use it for exactly what it was designed for and exactly what the niche you need it for, you'll be fine. But there's this temptation to start using it for everything, and it just spreads and grows.
Aleksandar Serafimoski:
And that's once we saw, I think not only with ESBs, but with the ERP system. And that's another thing from the tech rater that we brought in, which is the concept of abounded buy. Don't buy something, and just because it allows you to add more functionality, add it. Because, hey, I bought it and I'm going to reuse it for 10 different things. Buy something for what it's specifically intended to do, and then if you need something else, find another tool that does it well and connect them well. The example that we use for this was quite interesting. I think in the 80s or 90s there was the TV and the DVR that were meshed together. And so you got a player for free, a cassette player for free, but maybe it didn't have the best functionality.
Ashok Subramanian:
I think one of the points we were discussing, and you had mentioned was around capturing some of these metrics and making sure you're actually communicating that instead of spreading the message within the organization. Were there any techniques that you would recommend, some that worked better for you than others? And some examples of how you decided which KPIs would be the best to capture.
Anastasia Belozertseva:
Yeah. As we've mentioned in the past, either in the previous episode, what was really important for us while building these domain services is to make sure that we have a dedicated product owner for each one of those services. So treating the main services, not as a project with a specific timeline, but as a long living technical product. And the product owner here can bring in the domain knowledge from their organization, but also make sure that you're building the right product, help you define the technical strategy with the involvement of some of the architects and such, and really support without any time bounds.
Anastasia Belozertseva:
So one of the techniques that we use is that we really leverage this product owner in helping us define the metrics that are not just relevant for the technical audience, but also relevant to the business audience. And we also leverage this product on a figure to keep us on track when collecting these metrics. Because also, when you're talking about collecting metrics, it's also important to have the right architecture to support it, to support the easy collection of these metrics, make sure that you are able to prioritize it in a timely fashion, make sure that you are able to make sure that it's easy for you to collect them. Right?
Anastasia Belozertseva:
So we definitely leverage this product on a figure to help us with all of that, and to help us get the right prioritization. And make sure that we do have enough wiggle room in our sprints to play those kinds of stories. And we also use this product owners to help us identify the right audience within the company, because these product owners oftentimes were very familiar with the business and very familiar with the right stakeholders. And we established a particular timeframe, so a quarter was a good timeframe for us. So each quarter we would send out a type of survey to our product owners for all of the domain services that we had within their organization. And those product owners together with the team, would help us fill out these surveys and fill out the numbers for all of the points that we have identified. And then that would all get compiled into one single presentation, one single document that was then shared across the organization and with the rest of the stakeholders.
Neal Ford:
So the talk about metrics is quite interesting, because it's a great way to find out what a company's overall attitude about software is. Because if the only thing they really track is cost, then they view software purely as overhead and not strategic at all. And it's hard to get them to invest time and effort and value into software if they view it purely as overhead. And so that's one of the dysfunctions we've seen in large companies is they only track cost and total cost of ownership of all these things without doing any other metrics toward business value. So it sounds like one of the things you managed to do is find some good metrics that actually illustrate business value. And those are often different in different situations, even within the same company.
Anastasia Belozertseva:
Yes. And I think one of the most important metrics that we started tracking early is the number of consumers for our APIs. And I can't stress enough how important it is for every service desk should be aware how many customers are able to benefit from their services. And maybe at some point that becomes kind of irrelevant when you're getting to a large number of consumers, but early on you can really translate that number into an actual value add. You can actually measure that with dollars or any other currency. And that's something that speaks to the business.
Brandon Byers:
And last time we talked about how the organization had shifted to a lot of buy-in for this approach, creating an organizational unit that managed some of the domain APIs that supported some of the digital capabilities that they were bringing onboard. Obviously that required some internal ROI if they had to calculate one of the lead managers over the process had built some discount cashflow model that went out a few years. And showed roughly the 18 months, even with quite a heavy upfront development cost, that some of these APIs and some of the learning of how they integrate into the ERP. They have a payback that's due to increase adoption and the time savings per adoption with course correction calculations, but that was sufficient to influence quite a few minds within that organization.
Ashok Subramanian:
And I'm assuming, because you were already looking at treating this as a product, you could actually think about some of the metrics that you need from within the perspective of the product itself that made sense. Rather than how traditionally in organization that tend to be a separate concern to a different MI team, or someone else would actually be generating those reports and metrics possibly a few months down the line. And that's something that you were able to do that a lot earlier because you considered that as one of the key features of the APIs that you were building.
﻿Aleksandar Serafimoski:
Yeah. I think that definitely makes sense. I think the product mentality, and purely considering it as a product that has consumers, and APIs are not only on implementation detail allowed us to concentrate on the consumers or in the people that interacted with these APIs. And allowed us to talk to them, collect feedback, and then also understand the metrics that are important to them in the business, and then connected to specific budget things, and so on and so forth.
Ashok Subramanian:
I think we've spoken about quite a number of things that worked and you were able to learn from them. Maybe if you try and start touching upon some of the things that you might consider or do differently next time. Or the things that you've actually tried and you said, well actually the next time should avoid doing them. Any lessons that you could share?
Aleksandar Serafimoski:
I think something that, at least for me, I wanted to spend more time on, or I think we should have spend more time on, is work on a central catalog where we can discover the APIs. There was something put in place which was functional, however, we didn't put in enough infrastructure around it for automatic publishing of documents, and so on and so forth. So a central catalog is a good starting point. Something else that I think a lot of companies that are managing APIs do is a example code that shows you how to interact with their API. So getting started in order to allow people to get quickly jump-started on interacting with your APIs within an amount of minutes. I think being part of that, I would also would have wanted to do more of that. Of course, these are not black and white decisions. We did have a lot of requirements, and so they were prioritized a little bit lower. But I would definitely want to get more experience playing with those two specific things.
Brandon Byers:
One of the things we haven't talked about much, a lot of the APIs that were built, supported internal enterprise use cases, but there were some partner APIs that we helped them build as well that were business to business. And the partners on the other side had, in some cases, world-class IT capabilities. In some cases, no IT capabilities. What we did not get enough momentum on, and probably was almost a prerequisite, especially as we start to get to the upper edge of the curve in terms of partner IT capabilities, were some of the developer experience for the outside world and how to manage that process. Nor did we have a really robust solution for the lower edge, where the partners didn't have a whole lot of IT abilities.
Brandon Byers:
Which, by the way, I think it was a great environment where some of those low tow tools would play a role in helping them solve just the scale of the problem. But I do think that there should be some focus on thinking about this is, to some extent, an extension of your brand when you present APIs to the outside world. And thinking about the branding of it and the infrastructure that supports that before you get too far ahead of yourself.
Anastasia Belozertseva:
Yeah. And I was very involved in some of those conversations during my engagement, because a lot of the APIs that my teams were working on were these partner APIs that Brandon spoke about. And I will second what he said. It's really important to focus on those boundaries, especially if you are planning to integrate with external clients, it's important to focus on those boundaries earlier on. Because a lot of times you will have to involve various parts of your organization, especially if you're talking about a company the size of the company that we were working with. The parts of their organization that may be involved are your network team, because you have to start developing a DNS and C named strategy. And that's something that goes very hand-in-hand with your brand.
Anastasia Belozertseva:
That's what Brandon just spoke about. So from the brand and marketing perspective, it's important for you to have a consistent experience, whereas this inwards or outwards. But the outward one is the one that's probably going to be harder to change, which is why it should definitely require more thought when you develop this strategy. In addition to that, it's also important to think about the authentication strategy with the external clients, and having an consistent way for your clients, for your partners, to connect to your APIs. And then also having a strategy on distributing those credentials to your partners, renewing those credentials, if needed, and also just making sure that your partners feel comfortable with the level of security that you can provide.
Anastasia Belozertseva:
Of course, hand-in-hand with authentication goes authorization. And solving authorization for one API may be easy, but if you're talking about multiple APIs, you probably need to start also talking about some shared authorization entitlement services, where those needs can be used by various partner APIs. And that will also require a lot of thinking, some design and such. So of course, hindsight is 20/20, and that's something that if I could go back, I would just dive in to right away as opposed to just leaving it as an afterthought.
Neal Ford:
You mentioned authentication authorization, and we've been talking about ERPs. Are there special challenges around authentication authorization and ERPs which like to own that themselves?
Anastasia Belozertseva:
Yeah. Definitely yes to the challenges. I think when you are talking about integration, you oftentimes don't think about who exactly you're integrating with. For example, you may be integrating with people. Your APIs may be integrating with one system, or it can be integrated with multiple systems. And having a strategy on how to approach those different types of integration is important. So for example, the questions that you may have to ask is, if I have an ERP that supports multiple systems, do I want that ERP to have just one client credential, or do I want that ERP to have multiple client credentials? And I think there are pros and cons to both. And I think we can spend many more podcasts talking about authentication and authorization. But those are the kind of questions that we encountered. And we didn't necessarily, I don't want us to just say that we had the right answer, because once again, I don't think there is a right answer. There are just pros and cons.
Brandon Byers:
Well, and if I can just add a little bit of really interesting context on top of that. The ERPs expect to own identity and authorization for the processes inside them. And so when we start adding on this API layer with OAuth flows with identity provider that gives OAuth scopes on top of it, we are duplicating some of the authorization rules that already exist inside the ERP. Number one, number two, in many cases we're duplicating the identity itself. And so we have to find a way to bridge the identity of the enterprise and the modern identity. So we have to find a way to bridge the identity from the outside world to the ERP itself so that we can correlate the two.
Brandon Byers:
And that isn't just a technical challenge in some cases. And this is me driving outside of my lane. Sometimes it's also a licensing question in terms of user access to the ERP itself, so you actually need to involve legal in some of those conversations.
Ashok Subramanian:
I think we've had some great lessons learned and things that you probably could do differently. Is there anything else that you would like to share that you think really next time we do this, you probably would do a bit differently?
Anastasia Belozertseva:
Yes. I would like to talk a little bit more about asynchronous integration. I think if I were to do it all over again, I would prioritize transaction heavy business scenarios as the first scenario start path when building our services. As I mentioned in the past, the types of integration that we were offering with our services was restful and also event based. The reason why I bring up transaction heavy business events, because first of all, I do think that in a situation where you're modernizing your business, those are the type of events where if you're able to offer asynchronous integration between your services, you're really able to bring that wow effect. So think about a scenario where an order creation within your ERP is supposed to trigger multiple downstream workflows. For example, when an order is placed, there's probably some invoice generation that needs to happen, there is some communication with the customer that needs to happen.
Anastasia Belozertseva:
There's some inventory checks and maybe inventory refills that will be triggered. There's some shipment processes that will have to start. There are a lot of things that need to happen. In a world where all of those processes are customized within your ERP, it may be really, really hard for you to scale those workflows. And may be hard for you to make them happen quickly. In a world where you are able to have your order creation inside you ERP, and then have an asynchronous event coming out of your AP. So have your service can seen that event, do some level of transformation, and then generate an event that's consumable by your external systems. And then go ahead and throw that event on to Kafka or a RabbitMQ as some other type of event bus. That can actually be very, very beneficial within your business, because now you're able to trigger all of these downstream business processes with a lot less coordination.
Anastasia Belozertseva:
So in our case, for a lot of our domain services we oftentime prioritize our restful interface. And I wish we were also prioritizing eventing early on, so that we could bring more value to the business. And so that we could bring some savings in this particular area. Another thing that I will say is that a lot of times for a service, or for a set of services, if you have a lot of synchronous integration between those services, this could actually be an indicator that you haven't drawn your boundaries correctly. What this could be an indicator off, is that you're actually on a path or is a distributed monolith, which is not much better than your regular type of monolith. If you're able to demonstrate that your services can actually integrate easily via events, that could be just another way for you to be a little more sure about the boundaries that you've created and a little more sure by your architecture.
Anastasia Belozertseva:
There's a reason, for example, that when you place an order, oftentimes your credit card is not going to get charged right away. In fact, a lot of times your credit card is not going to get charged until a few days afterwards. And that's because payment is oftentimes a really great example of a process that can happen asynchronously. Here, the boundaries are correct. So this is what we're looking for. And if you're prioritizing these event based integrations, proving to yourself that they achieve work and you're able to satisfy your use cases via events, that can be a really nice pat on the back.
Neal Ford:
Yeah, it's one of the super powers of architecture, is getting asynchronous messaging to work. Because it has an impact not just on coordination, but virtually all of these operational architecture characteristics, like performance and scalability and elasticity, and all those things that benefit from basically it's the difference between building a single threaded versus a multi-threaded system versus a architecture. I think that's good advice. Because that's the, you know, get the hard boundary conditions working first. And that's in many cases are going to be the hard boundary condition, because a lot of these ERP systems want to be very synchronous and transactional. And if you can pry some of that control away from them, that gives you a lot of flexibility within your integration architecture.
Ashok Subramanian:
So one of the things we speak about, or we spoke a lot about on the technology journey and making sure that, how do you make successful visible? Now in terms of the people and taking the organization on the journey, and getting people who've been used to working in a very different architectural style, pattern, systems, and almost showing them the promise of what is possible, what did that journey look like? Any tips for our listeners to be able to take away and learn as to what worked in that context?
Aleksandar Serafimoski:
Yeah. No, absolutely. I think, taking the employees, your employees or the employees of a company that you're working with on a journey is quite important. Without the journey or without the education it feels like an overnight chain saying, "Oh, we did the ERP, now we're going to do modern architecture, go to it." Which basically doesn't work. Right? So we were lucky to have executives who bought into this vision. And so what we used to do is we developed a program which is very similar to TW, which is our own Thoughtworks University training program for people who come out right of university. So we took some of the sessions from that program, we created a specific training program which was around six months. And it evolved starting a new APR, a new project, all the way from the inception.
Aleksandar Serafimoski:
So agreeing on what are the deliverables, and getting shared vision of the product. And then pairing with Thoughtworks developers for six months where we divided it into, I think, three stages. So the first stage was the Thoughtworkers would drive and then the client developers would follow. Then we had a second stage where they would actively pair. And the last stage was the clan developers driving and the Thoughtworkers following. These allowed us to offer training that was tailored specifically to them, and then offer consistency in training across the globe, because we had development teams in multiple countries and multiple time zones. I think without training the client developers, this whole strategy would've fallen apart. Because once Thoughtworks leaves, if no one is there to support it moving forward, basically there's no future for this strategy.
Neal Ford:
Okay. One last question for you, if given the choice of your next project of doing a Greenfield microservice project or working on another ERP integration project, which would you pick?
Aleksandar Serafimoski:
Personally, I would probably pick the ERP integration. I think there's a lot of different challenges that it introduces, along with scalability. And it pushes you to think and do solutions where there's no silver bullet, like we mentioned earlier. And I find that super interesting and exciting. So for me, it's ERP. Anastasia?
Anastasia Belozertseva:
Can I say both? Where you have an ERP and you have everything to modernize some of your ERP, some of the processes that I hit in within your ERP, but you also have an opportunity to build something Greenfield at the same time. Of course, both is sort of a joke. But I think that ERP definitely has so many challenges that we're still just unveiling. That, yeah, I would probably go with that as well. I think the question of data democratization is something that I found very interesting, and it's something that we were solving during our previous engagement. And data democratization and then data federation is something that I would definitely would like to be involved in going forward as well. And I think there are a lot more opportunities for that if you are coming into this ERP heavy world.
Brandon Byers:
And look, I don't think there's any question from a technology standpoint, I'd much rather do Greenfield microservices and cloud and continuous delivery from the start. But my authentic belief is that these longstanding legacy evolutions represent probably the hardest problem in IT to solve. And when organizations have multi-decades and billions of dollars in some of these systems with standardized business processes around it, and an inability to adapt to the market. In some cases, it's an existential threat for very successful companies in a digital world. Solving the hard problem is rewarding, even if it's a much longer run and you don't get to necessarily play with the latest tools in the toolbox.
Neal Ford:
So the good news for all of us, it sounds like from all three of you, that there's hope. That while this is a big problem that's lurking out there, there are solutions to this problem. It just takes some work to get there, but it's not something you'd run screaming away from there. There's hope. And there is a city on the hill there somewhere.
Brandon Byers:
Absolutely agree.
Anastasia Belozertseva:
[crosstalk 00:39:01] It's a marathon.
Neal Ford:
Yeah, there you go. It's a marathon, not a sprint. All right. Well, thank you very much. Fascinating insights and a great opportunity to plug into your experience and expertise in that project. So thanks very much for coming on the podcast, we really enjoyed it.
Mike:
Hi, my name's Mike. And on the next episode of the Thoughtworks Technology Podcast, join us to learn about the future of digital trust.
[ View full transcript ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
More episodes 
Episode name 
Published 
Open-weight models: What are they and when should you use them? 
September 03, 2026 
AI-generated code: What has to be true for us to trust it without looking at it? 
August 20, 2026 
Scaling the enterprise harness: How to achieve AI agent controllability across an organization 
August 06, 2026 
Embracing hybrid AI: How Lenovo is leveraging local, on-device AI 
July 23, 2026 
What does the future of software engineering look like? 
July 09, 2026 
What does code mean in 2026? 
June 25, 2026 
Database branching: Overcoming the bottlenecks of shared database environments 
June 11, 2026 
What is spec-driven development? 
May 28, 2026 
What is harness engineering? 
May 14, 2026 
Anthropic Mythos: Hype, reality and the actual security implications 
April 30, 2026 
Key themes in Technology Radar Vol.34 
April 15, 2026 
How it feels to be a software engineer when AI is changing our relationship with code 
April 02, 2026 
Be brilliant at the basics: Inside Looking Glass 2026 
March 19, 2026 
Durable computing: What is it and why now? 
March 05, 2026 
Inside AI/works™: An agentic development platform 
February 19, 2026 
Unlearning, experimentation and engineering rigor in an agentic world 
February 05, 2026 
Exploring AI agent platforms 
January 22, 2026 
Architecture antipatterns and pitfalls: Good intentions, bad habits and ugly consequences 
January 08, 2026 
Are we entering the 'age of intent' in digital interaction? 
December 23, 2025 
AI-assisted software development in 2025: Inside this year's DORA report 
December 11, 2025 
We still need to talk about vibe coding 
November 27, 2025 
How developers can get the most from new AI coding workflows 
November 13, 2025 
Themes from Technology Radar Vol.33 
October 30, 2025 
What does an AI strategy with humans at the center look like? 
October 16, 2025 
What we're talking about when we talk about context engineering 
October 02, 2025 
Mean time to shared understanding: Bridging the gap between citizen developers and developers 
September 18, 2025 
Organizational design and Team Topologies after AI 
September 04, 2025 
Context engineering: Tackling legacy systems with generative AI 
August 21, 2025 
Navigating AI opportunities at MYOB 
August 07, 2025 
Caring about documentation in the LLM era 
July 24, 2025 
Why the tech industry needs Expert Generalists 
July 10, 2025 
The three new fallacies of distributed computing 
June 26, 2025 
MCP and SRE: Why the future of IT operations is agent-driven 
June 12, 2025 
Unpacking Google I/O 2025 
May 29, 2025 
Accelerating mainframe modernization using generative AI 
May 15, 2025 
Exploring the fundamentals of software engineering 
May 01, 2025 
Themes in Technology Radar Vol.32 
April 17, 2025 
We need to talk about vibe coding 
April 02, 2025 
Infrastructure as code in 2025 
March 20, 2025 
How fitness functions can help us govern and measure AI 
March 06, 2025 
Architecture as code 
February 19, 2025 
Decoding DeepSeek 
February 06, 2025 
AI testing, benchmarks and evals 
January 23, 2025 
Exploring the intersections of software architecture 
January 09, 2025 
Who should make software architecture decisions? 
December 26, 2024 
Generative AI's uncanny valley: Problem or opportunity? 
December 12, 2024 
Using generative AI for legacy modernization 
November 28, 2024 
Data contracts: What are they and why do they matter? 
November 14, 2024 
Themes from Technology Radar Vol.31 
October 17, 2024 
Build Your Own Radar: Using the Technology Radar as a governance tool 
October 03, 2024 
Exploring DuckDB: A relational database built for online analytical processing 
September 19, 2024 
Software service granularity: Getting it right 
September 05, 2024 
Measuring developer experience 
August 22, 2024 
How can AI support designers? 
August 08, 2024 
Sensible defaults: A way to think about our technology practices 
July 25, 2024 
Tracking technology stacks, practices and experiences across teams 
July 11, 2024 
Inside Bahmni: An open-source digital public good 
June 27, 2024 
How to assess your organization's security maturity 
June 13, 2024 
Continuous delivery vs. continuous deployment: What should be the default? 
May 30, 2024 
Themes from Technology Radar Vol.30 
May 16, 2024 
Building at the intersection of machine learning and software engineering 
May 02, 2024 
Refactoring with AI 
April 18, 2024 
How to measure your cloud carbon footprint 
April 04, 2024 
Technology through the Looking Glass: Preparing for 2024 and beyond 
March 21, 2024 
Diving head first into software architecture 
March 07, 2024 
Exploring the building blocks of distributed systems 
February 22, 2024 
Software-defined vehicles: The future of the automotive industry? 
February 08, 2024 
Beyond the DORA metrics: Measuring engineering excellence 
January 25, 2024 
Asynchronous collaboration: Getting it right 
January 11, 2024 
Looking back at key themes across technology in 2023 
December 28, 2023 
Leveraging generative AI at Bosch 
December 14, 2023 
Jugalbandi: Building with AI for social impact 
November 30, 2023 
AI-assisted coding: Experiences and perspectives 
November 16, 2023 
What's it like to maintain an award-winning open source tool? 
November 02, 2023 
Engineering platforms and golden paths: Building better developer experiences 
October 19, 2023 
Managing cost efficiency at scale-ups 
October 03, 2023 
Exploring SQL and ETL 
September 21, 2023 
Driving innovation in radio astronomy 
September 07, 2023 
XR with impact: Building experiences that drive business value 
August 24, 2023 
Leadership styles in technology teams 
August 10, 2023 
Making design matter in technology organizations 
July 27, 2023 
Generative AI and the future of knowledge work 
July 13, 2023 
Scaling mobile delivery 
June 29, 2023 
Making privacy a first-class citizen in data science 
June 15, 2023 
Multi-cloud: Exploring the challenges and opportunities 
June 01, 2023 
Scaling up at Etsy 
May 18, 2023 
TinyML: Bringing machine learning to the edge 
May 04, 2023 
The weaponization of complexity 
April 20, 2023 
How we put together the Technology Radar 
April 06, 2023 
Inside India's Drug Discovery Hackathon 
March 23, 2023 
Serverless in 2023 
March 09, 2023 
My Thoughtworks journey: Rebecca Parsons 
February 23, 2023 
How to tackle friction between product and engineering in scale-ups 
February 09, 2023 
6 key technology trends for 2023 
January 26, 2023 
Tackling system complexity with domain-driven design 
January 12, 2023 
Shifting left on accessibility 
December 29, 2022 
Data Mesh revisited 
December 15, 2022 
Low-code/no-code platforms: The 10% trap and the limits of abstractions 
December 01, 2022 
Welcome to the fediverse: Exploring Mastodon, ActivityPub and beyond [Special] 
November 24, 2022 
Rethinking software governance: Reflecting on the second edition of Building Evolutionary Architectures 
November 17, 2022 
Reckoning with the force of Conway's Law 
November 03, 2022 
Exploring the Basal Cost of software 
October 20, 2022 
Why full-stack testing matters 
October 05, 2022 
Acknowledging and addressing technical debt in startups and scale-ups 
September 22, 2022 
XR in practice: the engineering challenges of extending reality 
September 08, 2022 
Agent-based modelling for epidemiology: EpiRust and BharatSim 
August 19, 2022 
Mastering architectural metrics 
August 12, 2022 
Building a culture of innovation 
July 28, 2022 
Starting out with sensible default practices 
July 14, 2022 
Better testing through mutations 
June 30, 2022 
Patterns of legacy displacement — Part two 
June 16, 2022 
Patterns of legacy displacement — Part one 
June 02, 2022 
Mitigating cognitive bias when coding 
May 19, 2022 
Following an usual career path: from dev to CEO 
May 05, 2022 
Software engineering with Dave Farley 
April 21, 2022 
Tackling bottlenecks at scale-ups 
April 07, 2022 
Coding lessons from the pandemic 
March 24, 2022 
Is there ever a good time for a code freeze? 
March 10, 2022 
Navigating the perils of multicloud 
February 25, 2022 
Compliance as a product 
February 10, 2022 
The big five tech trends for 2022 
January 27, 2022 
Fluent Python revisited 
January 13, 2022 
Creating a developer platform for a networked-enabled organization 
December 30, 2021 
The art of Lean inceptions 
December 16, 2021 
The hard parts of data architecture 
December 02, 2021 
TDD for today 
November 18, 2021 
You can't buy integration 
November 04, 2021 
The rise of NoSQL 
October 21, 2021 
The hard parts of software architecture 
October 07, 2021 
Machine learning in the wild 
September 24, 2021 
Delivering innovation at scale 
September 09, 2021 
Securing the software supply chain 
August 12, 2021 
Making retrospectives effective — and fun 
July 22, 2021 
Patterns of distributed systems 
July 08, 2021 
Refactoring databases — or evolutionary database design 
June 24, 2021 
Making developer effectiveness a reality 
June 10, 2021 
Team topologies and effective software delivery 
May 20, 2021 
How green is your cloud? 
May 07, 2021 
Green software engineering 
April 22, 2021 
Twenty years of agile 
April 08, 2021 
Talking with tech leads with Pat Kua 
March 25, 2021 
My Thoughtworks Journey: Patricia Mandarino 
March 11, 2021 
Exploring infrastructure as code 
February 25, 2021 
XR in the enterprise 
February 11, 2021 
Getting to grips with data visualization 
January 21, 2021 
Computational notebooks: the benefits and pitfalls 
January 07, 2021 
The architect elevator 
December 24, 2020 
The future of Clojure 
December 10, 2020 
The future of digital trust 
November 27, 2020 
Integration challenges in an ERP-heavy world — Pt 2 
November 12, 2020 
Democratizing programming 
October 28, 2020 
Integration challenges in an ERP-heavy world 
October 16, 2020 
Models of open sourcing software 
October 01, 2020 
Applying software engineering practices to data science 
September 17, 2020 
Using visualization tools to understand large polyglot code bases 
September 03, 2020 
Machine learning in astrophysics 
August 20, 2020 
Programming languages geek out 
August 06, 2020 
Observability does not equal monitoring 
July 23, 2020 
Working with 50% of code in the browser 
July 09, 2020 
Realising the full potential of CD 
June 25, 2020 
Testing the user journey 
June 12, 2020 
Continuous delivery in the wild 
June 01, 2020 
Lessons from a remote Tech Radar 
May 13, 2020 
The future of Python 
April 30, 2020 
A sensible approach to multi-cloud 
April 17, 2020 
Digital transformation: a tech perspective 
April 02, 2020 
IT delivery in unusual circumstances 
March 20, 2020 
Continuous delivery for today's enterprise 
March 06, 2020 
Fundamentals of Software Architecture 
February 21, 2020 
Cloud migration — part two 
February 10, 2020 
The price of reuse 
January 24, 2020 
Towards self-serve infrastructure 
January 13, 2020 
Martin Fowler: my Thoughtworks journey 
December 27, 2019 
Building an autonomous drone 
December 13, 2019 
Cloud migration is a journey not a destination 
November 28, 2019 
Getting to grips with functional programming 
November 14, 2019 
Compliance as code 
November 01, 2019 
Data meshes: a distributed domain-oriented data platform 
October 18, 2019 
Edge — a guide to value-driven digital transformation 
October 04, 2019 
Tech choices: CIO or CTO? 
September 20, 2019 
Microservices as complex adaptive systems 
September 05, 2019 
Supporting the Citizen Developer 
August 22, 2019 
Getting hands-on with RESTful web services 
August 08, 2019 
Zhong Tai: innovation in enterprise platforms from China 
July 25, 2019 
What’s so cool about micro frontends? 
July 11, 2019 
Unravelling the monoglot monopoly 
June 27, 2019 
Breaking down the barriers to innovation 
June 13, 2019 
Delivering strategic architectural transformation 
May 30, 2019 
Exploring programming languages via paradigms vs labels 
May 16, 2019 
Multicloud in a regulated environment 
May 03, 2019 
Can DevSecOps help secure the enterprise? 
April 18, 2019 
A11Y — Making web accessibility easier 
April 04, 2019 
Continuous delivery for modern architectures 
March 21, 2019 
Delivering developer value through platform thinking 
March 07, 2019 
Architectural governance: rethinking the Department of ‘No’ 
February 21, 2019 
Serendipitous Events 
February 08, 2019 
Diving into serverless architecture 
January 24, 2019 
Seismic Shifts 
January 10, 2019 
Understanding bias in algorithmic systems 
December 28, 2018 
Microservices: The State of the Art 
December 14, 2018 
Evolving Interactions 
November 29, 2018 
The state of API design 
November 15, 2018 
How we build the Tech Radar 
November 01, 2018 
IoT Hardware 
October 18, 2018 
Continuous Intelligence 
October 04, 2018 
Distributed systems antipatterns 
September 13, 2018 
Agile Data Science 
August 23, 2018 
## Check out the latest edition of the Technology Radar
[ Explore now ](https://www.thoughtworks.com/radar)
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