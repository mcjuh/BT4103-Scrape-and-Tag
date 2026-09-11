<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/integration-erp-heavy-world-pt1 | Title: Integration challenges in an ERP-heavy world | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Integration challenges in an ERP-heavy world 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Ashok Subramanian | Podcast guest  Aleksandar Serafimoski, Anastasia Belozertseva and Brandon Byars
October 16, 2020 | 39 min 46 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/integration-erp-heavy-world-pt1#transcript)
Listen on these platforms
## Brief summary
Enterprise resource planning systems remain business-critical for many organizations. But these decades-old and often highly customized systems weren’t designed to operate in a modern, distributed manner. This throws up huge integration challenges when organizations want to explore how to embrace new digital opportunities. We look at how to overcome some of these challenges.
**Podcast transcript**
Neal Ford:
Hello, welcome everyone to the Thoughtworks Technology Podcast. I'm Neal Ford, one of your regular hosts.
Ashok Subramanian:
Hello. And I am Ashok Subramanian, another one of your regular hosts. Today we have three guests with us today. Would you want to go ahead and introduce yourselves?
Aleksandar Serafimoski:
Sure. My name is Aleksandar Serafimoski. I'm a lead consultant at Thoughtworks. I've been with Thoughtworks for eight years and I'm based out of the Chicago office.
Anastasia Belozertseva:
I'll go next. Hi everyone. I'm Anastasia Belozertseva. I'm also a consultant at Thoughtworks. I have been with Thoughtworks for pretty much the same amount of time that Alex, eight years, working out of Chicago. Fun fact, myself and Alex started pretty much in the same day.
Brandon Byars:
Hi, I am Brandon Byars. I'm a technical director at Thoughtworks, coming up on 13 years.
Neal Ford:
All right. And today we want to talk about integration challenges in an ERP-heavy world. Something that we seem to be bumping into a lot lately at Thoughtworks. Our enterprises that are using big package software a lot and integration challenges. And our guests today have some thoughts about that. So, what would you like to say about that?
Brandon Byars:
Yeah, I can set some context that we can use as backdrop for the conversation. The reason the three of us are here together is because we both recently worked at a large client that is representative of, I think, the problem statement, which is, like a lot of large clients who are oftentimes going through acquisition, they have consolidated business process and technology with a large monolithic ERP system, 20 plus years back and gained some functional efficiencies in the process.
Brandon Byars:
But the world today is very different than it was back then. There's a lot of revenue streams through digital technology, even in [inaudible 00:02:14] industries has proven to be value-generative. And so they're looking at how to embrace some of these digital opportunities, but they have this legacy of large standardized ERP processes that are oftentimes over-customized and even something that naively sounds as simple as upgrading numbers, hundreds of millions of dollars multi-year, so they have a fairly large technological albatross around the neck while trying to chase some of these digital opportunities. And so, we've seen this across a few clients and we're trying to just share some of our perspectives on what we've learned and know some of the way forward.
Ashok Subramanian:
That's great. I think that's good context set in scene of what we are actually going to talk about. Do you want to dive into a bit more in terms of, well, when you do have these big monolithic systems and you go in and clients do want to ... what did you do? What was your take or your approach on that?
Brandon Byars:
So I'll start it off and then hand off to Anastasia and Aleksandar. In this particular example, I think this is a pretty common scenario across clients, there is recognition that they could bring in new capabilities outside the ERP, but to do that, you run into ownership problems because ERPs are meant to own a process end to end. Imagine taking some piece in the middle and trying to add some value with a different component of the ecosystem.
Brandon Byars:
And solving the problem of accelerating your digital journey and figuring out where exactly the ERP fits or doesn't is, at that scale, such a massive problem that you can't plan your way to a solution. The approach that we took with this client, and then others was to say, what we can do is provide some seams where the ERP may still be the system of record, but outside of that set of business expertise to manage that process, everybody else should get a much simpler abstraction of the workflow and see where we could find some opportunities to plug in new capabilities around inventory management or revenue management, and think through what that would mean in terms of providing business value in a way that didn't force anybody to fundamentally advance the state of the art in the ERP system because that's just too big of a hill to climb.
Ashok Subramanian:
So if my understanding is correct, what you tried to do is figure out ways in which you can wrap the ERP and hide away the complexity. Yet try and provide some obstruction for people to build new stuff on top of it, so no one has to forget out how to change the ERP and go through these long chain cycles.
Aleksandar Serafimoski:
Yeah, that is correct. The strategy that we had when we approached this issue was we wanted to build reusable capabilities or expose reusable capabilities outside of the ERP.
Aleksandar Serafimoski:
So, other teams within the organization can reuse them without needing to understand how is the data stored, where is that data stored, how to access the ERP. And so by doing that, we were able to save a significant amount of costs that other teams would have paid by raising tickets or talking to subject matter experts and so on and so forth. So, some of the guiding principles behind these capabilities was self-service, easy to use, and hiding some of that complexity comes with a monolithic ERP system.
Ashok Subramanian:
And the approach you took with that, I think you had mentioned some common abstractions. Could you talk a bit more about what that structure was and how did you go about identifying some of the seams that might be there?
Anastasia Belozertseva:
Yeah, I think when we're talking about abstraction at that level to separating, abstracting away ERP, what we're really talking about is introducing an API strategy. So building reusable services on top of the ERP that can communicate with the ERP and retrieve data from there, but integrations going forward for downstream consumers happened through these APIs.
Neal Ford:
One of the common side effects we see for APIs like that is an impact on team structure, because it's sometimes difficult to find people that have a full enough understanding of the domain to even build something useful on top of it. Did this have an impact on team structure in the places that you've seen this work?
Anastasia Belozertseva:
Yeah, I think that's a very good question. And I think one of the hardest tasks to approach this particular effort is to identify core business capabilities that can be abstracted using this API strategy. So shaping domains was definitely an effort that took some time. And we're just, at the beginning of that journey. A lot of times when shaping the domains, we relied on the SMEs domain knowledge, the SMEs that were on the ground and that were familiar with the business. And they definitely had a very large input into the final shape of the product. I think that being said, we all set what would be valuable exercise in this particular situation is running an event storming exercise to help you identify those core domains and core business capabilities.
Aleksandar Serafimoski:
I wanted to kind of build on top of that. I think definitely when working through these domains, it's quite important that you don't get into a position of analysis paralysis where you're trying to get the perfect boundary around the domain or decide what a domain is, but take a more pragmatic approach saying, "Hey, we'll expose a domain. We're going to learn by the usage patterns and the consumer feedback around these domain. And then we can evolve it from the original exposed domain in the future."
Aleksandar Serafimoski:
I think keeping that mentality, that's like, "Let's put something out, let's get some feedback, let's see how our consumers are using it." Talk to them and understand the true usage patterns and then evolve it from there. It's quite important, just so that you can show business value to the business. And then also you can collect feedback from your actual consumers rather than building the perfect solution and hoping that the consumers are going to come later on.
Neal Ford:
Well, I think that's a great example that architecture can be iterative. In fact, it should be iterative, especially when you're seeking for a particular design or trying to build something that you don't know what you're building yet, but you know that it's somewhere there in the future iterating toward a design like that is a good way to do it. As long as you have, like you say, a fast feedback loop.
Anastasia Belozertseva:
Yeah. I want to say definitely. I think that's very true. And I think another thing that I wanted to say is that we focus on various modes of integrations with these APIs. I think the two primary modes of integrations that we prioritize were restful integrations and also events. By delivering these types of integrations, we're able to demonstrate value quickly.
Brandon Byars:
I think there was an interesting point that we want to call out, which is a lot of these organizations that have large longstanding ERPs have a history and a comfort level buying products and integrating them to make them work. And oftentimes a point to point fashion. And it wasn't just the fact that there were APIs. It was the fact that the message was that's fine to buy these capabilities, but you have to own the immigration. You have to treat the immigration as a first-class technical product in its own right, that you manage with multiple consumers, even if those consumers are themselves package applications that are adding additional capabilities to your organization.
Brandon Byars:
And so being really clear about having clean interfaces around these, and then to Neil's question around team organization, team ownership, and then product ownership around these APIs, I think was the paradigm shift for that organization. That took some, obviously, influencing and evangelizing to get over the hump.
Neal Ford:
So Anastasia sort of snuck the word product in there and then Brandon just used it. This is something that we're seeing a lot in architecture is this perspective of product versus projects. And it sounds like that's something that you've encountered as well, the benefits of treating things, getting rid of the project mentality and going toward products.
Aleksandar Serafimoski:
Correct. The steps as Brandon and Anastasia mentioned where ... it was very important that we consider the APIs as long lift products, because these are the core capabilities within the organization that we can innovate and build on top of for a really long time, which involved assigning specific teams and specific budgets around those, along with a dedicated technical product owner that can prioritize any feature requests that are coming from other teams within the organization. And also advertise the APIs within the organization to say, "Hey, if you, for example, need to access the customer capability, which allows you to create a new customer, we have this API and you don't need to get into the details of the ERP system and understand how is that done?"
Ashok Subramanian:
You mentioned prioritizing integration styles, and you said you picked two REST and event typically these sort of legacy ERP systems, they tend to ... the newer sort of architectural patterns, there tends to be a mismatch between how they are designed to be used. And a lot of them tend to follow much more sort of batch-oriented or request response style access patterns.
Ashok Subramanian:
When you're trying to expand this for different kinds of use cases, how did you try and bridge that gap between different architectural styles and patterns? Was that a challenge or, in your particular example, it wasn't something that you faced?
Aleksandar Serafimoski:
Yeah, It was definitely a challenge because initially we just started with a request response type of pattern, but then because we had requirements that were more event-driven or more asynchronous communication, we needed to spend some time investigating what are the abilities of the ERP system and what can we get out of the box in order to address this?
Aleksandar Serafimoski:
I think, kind of connecting to Neil's question around team structure, it was very important that we get someone who had expertise within the ERP development cycles. And then, get their help in order to understand how we can achieve what we needed to achieve. Fortunately, for us, the specific ERP that we were using was supporting the pattern of asynchronous communication or kind of sending events. But I guess my suggestion is even if it doesn't support it, working on a solution within the domains that you're building outside of the CRP and then doing some work in order to hide the complexity of the ERP and still exposing these capability can also an important thing for the APIs that you're building outside of the ERP.
Anastasia Belozertseva:
And adding to that, Alex already mentioned that we were lucky that the ERP that we're all working with could actually support asynchronous events coming out of it, that the API could consume and then trigger for downstream systems to consume. What was really nice is that that introduced a level of abstraction on top of the ERP where we're reducing the dependency on the ERP, but we're also reducing the load on the ERP.
Anastasia Belozertseva:
The way we structured these events is that we actually had these events contained the entire state of the change. So, this is your flavor, some people refer to it as event-series type of event, as opposed to just an event that's a [inaudible 00:15:14] style of event. And by doing that we could consume all of the data that was needed for us to generate this downstream event for downstream systems to consume. We could create it just based on that initial event that we got from the ERP.
Neal Ford:
Okay. So, you've tiptoed into formats now. So how did you document and do governance on this? Because that's another important aspect of creating a catalog like this, is making it consumable by documenting and also governance, right?
Anastasia Belozertseva:
Yeah. I think when it comes to eventing, it's really important to approach this as a type of interface the same way that you approach your restful interface. So, your events carry a particular format. They can be versioned and your event should contain the version number in it, or somehow indicate the version number.
Anastasia Belozertseva:
You should have some sort of transaction ID for your events as well, so that you are able to trace it down the line if you ever need to do some level of debugging. Really, I think the same guidelines that you normally apply to structuring your restful contracts, you should be following the same guidelines when thinking about events as well.
Brandon Byars:
Cataloging was definitely a challenge throughout the organization because there was this notion of calling point to point integrations APIs and then document catalog, which decreases the signal to noise ratio of the catalog itself. But we did make an attempt cataloging events no differently we would event contracts, no different we would restful API contracts, and as much as possible try to keep them in sync.
Brandon Byars:
So, whether you approach the information or the capabilities synchronously or asynchronously, you were getting the same representation. There was a tool, and Anastasia or Aleksandar might be able to remind me I think it might be called AsynchIO that we were using for some event cataloging.
Aleksandar Serafimoski:
Yeah, for that I think it was called Asynch API, where we're able to drive out some documentation around the contracts. I think for the second part of your question around the governance part, what we did is we had, in order to improve the consistency and usability of these APIs, we provided some very lightweight governance, which was supported by solution architects that were staffed or worked with a couple of different teams.
Aleksandar Serafimoski:
They weren't the typical solution architects that would make decisions without consulting the teams. They were very involved with the teams understanding what are the requirements, what are the deadlines, and working with them in order to come up with creative solutions and address those constraints. Also as a foundation, there was certain types of documents that we would publish either from the tech leads or the specific solution architects, such as an API style guide and some patterns that different API is used on how, for example, to expose events. Or how do we think about the architecture when we're deploying in the cloud, and so on and so forth. I think all of this together allowed us to build trust between the solution architects and the different teams, and then also provided an easy to use platform composed of different capabilities, which had consistent interfaces.
Aleksandar Serafimoski:
The last thing that I'm going to say on this is in order to keep consistencies across the multiple solution architects, because we had around eight teams with, I think, four solution architects. We had kind of a center of excellence where all of the solution architects from Thoughtworks and the client side would meet once every two weeks where we talk about some of the concerns that are shared across teams, which was quite helpful because it was a very good knowledge sharing session and avoiding building silos, which can lead to potential problems in the future.
Ashok Subramanian:
I think it's been fascinating trying to learn about how your experience of using the APS to sort of build this obstruction over that. But one of the other challenges that we've seen with these kinds of ERP systems is how do you go about managing the different rates of change between the ERP and everything else that you want to move at different pace, because these systems tend to be quite ... they have a much longer chain cycles than what we are normally used to. What was your experience here and once you started building these APIs on top of that, how do you manage the difference in change cycles?
Brandon Byars:
I think the key driver for adding this additional abstraction in the middle of some of the integrations to the ERP, quite different than their historical service spots point to point approach orchestration was that we could support the evolution of the ERP on a different life cycle than the experiences that we were adding capabilities outside of the ERP. So, they could evolve independently from each other with very low coupling managed through stable and clean API interfaces that didn't speak the language of the ERP. They spoke as much, as we were able, the language in the business.
Brandon Byars:
And then define a clear interface into something like, let's say, order management or pricing. And not just a data feed that you can find in a data warehouse. I think that was important because what we saw is two things. We saw the capability to change the underlying ERP in relatively small ways without breaking consumers. And then we saw the opportunity to bring on new experiences on top with very little coordination, and in many cases, no coordination to the ERP itself, which was not something that that organization had a history of being able to do.
Ashok Subramanian:
And I think trying to extend that into where you had teams that were working with some level of integration with the ERP, how do you manage the different set of skills that are actually needed, or maybe the expertise on systems? Do you have those people part of these teams as well that were building the APIs? And what was your mechanism actually working with people with that set of expertise?
Aleksandar Serafimoski:
Yeah, so initially when we started, we were lucky because we got one of the people that was an expert within the ERP system to be staffed or to be helping out one of the teams that were building the APIs on top of it. And that was super helpful because he was not only an expert within the ERP system from a programming side, but also he had some knowledge around the life cycle of certain entities within the ERP.
Aleksandar Serafimoski:
And then also, where did the data reside and so on and so forth. So he wasn't technically directly assigned to the team, but he worked really closely with the team as an outside subject matter expert, which allowed us to create that successful integration with the ERP. And then, he was able to help out with some of the solutioning around how do we make the integration between the domain APIs and the ERP flexible enough, where if we need to change something, we don't necessarily need to reach out to a separate team every time and get on their backlog and get prioritized, and so on and so forth. If I was to think, or in the future, how would I approach this? I think having someone embedded on the same team, if that is available within the organization, it's quite good.
Aleksandar Serafimoski:
Or if you can assign a person who can support multiple teams through this experience also, that's another way that can be beneficial for the teams building the capabilities outside of the ERP.
Anastasia Belozertseva:
Something that I would like to point out as well is, I think you mentioned this a little bit, Alex, you alluded to it. One of the things that we were able to come out with is shared tooling when it comes to the integration with the ERP. So, we were actually able to productionalize this different integration pattern with the ERP be it through the API or through asynchronous events, and then share it as a library across all the different teams.
Anastasia Belozertseva:
So, that was a really big investment on day one, and it did take some time for it to be at a point where the library could actually be shared by and leveraged by different teams, but once we got to that point, the need for this subject matter expert, or this deep knowledge of how to connect with the ERP, that really went down by a lot.
Neal Ford:
Naturally the goal of creating an API around something like that is to simplify the access to it, right? Both from a technical standpoint and a domain standpoint.
Brandon Byars:
It wasn't just the API, what Anastasia is pointing out is really important because of the expertise that you called out around integrating to the ERP, we needed some shared tooling across APIs to make that integration easier and to establish some patterns to reduce our dependency on specialized skillsets.
Ashok Subramanian:
That's a really interesting that you mentioned about how you lowered the barrier to make it easier to build APIs on top of that. So could you expand a bit more on what this shared tooling was? And what was some of your experience of actually building the shared tooling? And how did you get it to actually scale across and make it easier to build more APIs?
Aleksandar Serafimoski:
We started on this project, I think, around April, 2018. And what we wanted to understand was if we can deploy to the services or the platform, the delivery platform that this company had set up for us. And so while we were doing that, we realized that the effort that we did around deploying in a CI/CD pipeline, and documentation, and testing strategy, every team that needs to deploy will need to go through the same steps.
Aleksandar Serafimoski:
And so we were able to go in and present these to the client around building a starter kit. That was an internal tooling that we built specifically for this company that allowed other teams that needed to build the APIs on top of SAP or a simple UI application to go in and generate code with a couple of clicks and a few input fields. It was very similar to Spring Initializr except it gave you way more things.
Aleksandar Serafimoski:
So, it can automatically deploy a database for you. It can automatically allow you to connect or hook up to eventing store like Kafka. It will give you a CI/CD pipeline. So within an amount of a couple of minutes, if you have all of the prerequisites in place, you can deploy all the way from dev to production.
Aleksandar Serafimoski:
And from that perspective, this was very successful because any other team that came in and needed to integrate with an ERP, needed to deploy to this delivery platform that they were using, could get a generated code base through self-service, through APIs, without talking to the team that is managing it in an amount of minutes. And they could save enough time and then dedicate that time on building business capability. So, this tool that I was talking about was specific to the on prem platform.
Aleksandar Serafimoski:
Anastasia can also talk about something that we did when we were building domains that were not connected to their ERP, but were just purely deployed in the cloud. We did some of that specifically with cloud tooling and cloud architecture, allowing teams to accomplish the same goal.
Anastasia Belozertseva:
Yeah. Before I even talk about cloud, there's also something that I wanted to point out. I think one of the reasons why this particular starter kit project ... and I'm sorry for using the word project, I should correct myself, the starter kit product. One of the reasons why it was successful, because it was a tool that was built by developers and was aimed to benefit developer experience as well.
Anastasia Belozertseva:
And it was really treated as a product, long living product, which had a dedicated product owner with enough technical experience to be able to support such a technical product and an actual community around it. And it had, I think Alex already talked about it, but it had three pieces that I would like to call out. So, there's the piece about cogeneration, so creating your starter ... in our example, it was Java, but it doesn't have to be Java, your starter Java project, creating starter pipelines to be able to deploy your project to higher environments.
Anastasia Belozertseva:
But then there's also the part around the shared libraries that allow easy integration with those ERP systems. So we kind of talked about this earlier, right? Those two pieces, I think, were really important for our particular case. And what that was able to achieve is improving developer experience across the world. So across all the teams, they got a chance to use this product, the experienced was definitely elevated. This also reduced the need for that specialized knowledge when it comes to the ERP specialized knowledge. And this tool was also somewhat educational because there were some skills that we had to bridge within this organization that was fairly new to API development.
Anastasia Belozertseva:
Alex, that's a very good point about being able to take this product to the cloud. The fact that this was treated as a product meant that it could evolve if there was demand for any additional features. And at some point during our engagement, maybe a year or so in, what we realized is that we were really, really good at creating services that were deployed on prem and supporting those services on prem. But we weren't very good at taking those services further, meaning deploying to the cloud.
Anastasia Belozertseva:
So what we were able to do is actually evolve this starter kit set of tools to allow for various paths of deployment, not just on prem, but also to the cloud. And what that could solve is ability to integrate easily with consumers, regardless of where they were hosted and regardless of whether they were internal or external to the company. You may ask, why is it that we chose for our initial set of services to be deployed on prem? And that would be a really good question. And I'll go ahead and answer it right away.
Anastasia Belozertseva:
And the reason behind it is data gravity. So the particular ERP system that we were integrating with was all hosted on prem. So one of the first things that we were really concerned with was performance. That's why on day zero, our goal was to get all the way to production and be able to satisfy clients on prem before making that next step. Once we were able to get to a certain level of maturity, that's when we started to evolve this product beyond on prem. And that's why we started introduced capabilities for it to be deployed to the cloud.
Brandon Byars:
And Anastasia did some really good work in that space. We previously mentioned the asynchronous integration patterns and what that allowed us to do, and she had a heavy hand in this process, was to take some of the events that we were pumping out of the ERP and effectively federate them globally. There's a long road to evolve that architectural style, but what that does allow you to get to is an ecosystem of federated caches, where some questions can be answered much more quickly if you're in Singapore, if you're in South America, and what could happen if everything had to come back to a US data center. So there were some synergies between the cloud strategy and the integration strategy and thinking about how to solve some real business pain points along the way.
Ashok Subramanian:
I think that really ties into one of the points Neil was making earlier on about evolution and the steps to get to a place where your, the way you describe your journey of moving from the data center and trying to solve some of the initial problems that you had to solve almost immediately for on day zero. And then, carefully chosen paths to how you would evolve this to move to the cloud and actually support clients who are getting globally distributed, as well. It's definitely a ... you know, one of the learnings that we've had in the team multiple times about not trying to solve the ultimate problem for everyone at the same time, but trying to take the steps along the way that you're also giving value back to end users and consumers.
Neal Ford:
I think that also illustrates the benefit of product thinking, because if you have a project, you've got to get it all done as within the scope of the project, because you're going to finish the project and everybody's going to turn the lights out. But if it's a product, you can literally start with a Minimum Viable Product, which sounds like what you did, let's prove that this works and then we can iterate on that design and keep adding value to it until you start demonstrating real business value.
Brandon Byars:
Yeah. And all buoyed by that shared community that Alex spoke to, so that as one product team would learn some lessons that can be adopted by other product teams.
Neal Ford:
And that's the best way to get adaptation for something like that, is make it viral so that you get word of mouth rather than force of will.
Aleksandar Serafimoski:
One last thing that I probably want to ... maybe we'll bring it up here or in the other one. I think it would be beneficial, at least in my opinion, to bring up that there was no silver bullet. And so this required a lot of pragmatic thinking and a lot of compromises and evaluating those. And, Neil, a quote that you used is, "There is the least worst architecture." I think when we were making these decisions, it was always about that. Like, "Let's evaluate something and let's understand what works in our case and what doesn't." And so on and so forth.
Anastasia Belozertseva:
And I think one of the key problems that the business was struggling with at the time that we came in is that they felt like the innovation was slow. They didn't have enough space for it. And I think when we came in, what we brought is that ability to innovate quickly by creating smaller services that they could work with by creating these abstraction layers, by clearing their road to production, and by being able to demonstrate value quickly, we allowed the business to innovate in a better way.
Ashok Subramanian:
So, you mentioned this evolution, and have described where you've sort of got to it slowly evolving from how do you design to get out from the data center to the cloud and providing these services for consumers that are globally distributed.
Ashok Subramanian:
Do you want to share a bit more about what some of the successes were? It seems like a really interesting journey from from day zero, you're faced with a big monolithic ERP and very sort of start to what you described is really interesting in terms of coming up with tools to enable rapid building of APIs, using different integration patterns and being able to service clients and customers in different parts of the world.
Ashok Subramanian:
So, from your perspective, some key highlights or successes. What was the client actually able to do going through in this journey that they weren't able to do before?
Anastasia Belozertseva:
I think if I were to sum up this conversation that we just had, some of the key success factors include acknowledging that ERP has its own place. And there is no harm in continuing to using it as a system of record.
Anastasia Belozertseva:
That being said, also recognizing that if you continue to write custom software, you end up within a large ball of mud that will be really, really hard to unpack down the line. So investing into an API strategy, it goes beyond just ERP strategy, will bring you a lot of benefits. So investing into some shared tooling and patterns that can be used by developers to ease this journey is going to make the life of your teams a lot easier. And then also, I think the paradigm shift come to project to product mentality is really, really important in this situation. So really treating your API as long living products with a dedicated product owner, dedicated life cycle, where you start small, you iterate on it, you demonstrate value every few weeks will really help you build trust and gain respect from your consumers, and also will allow you to innovate quicker.
Neal Ford:
All right, that's a great summary. So thanks very much, Anastasia, Aleksandar and Brandon for giving us some highlights on your recent experiences with dealing with integration architecture and ERP systems. So, thanks very much for your insights.
Brandon Byars:
Thank you, Neil and Ashok for having us.
Aleksandar Serafimoski:
Thank you.
Anastasia Belozertseva:
Thank you so much.
Ashok Subramanian:
We hope you'll join us on the next edition of the Thoughtworks Technology Podcast when we will be discussing approaches to successfully overcome integration challenges in the world of legacy ERP systems. Please, join us next time on the Thoughtworks Technology Podcast.
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