<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/navigating-perils-multicloud | Title: Navigating the perils of multicloud | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Navigating the perils of multicloud 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Ashok Subramanian and Rebecca Parsons | Podcast guest  Bharani Subramaniam
February 25, 2022 | 46:03 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/navigating-perils-multicloud#transcript)
Listen on these platforms
## Brief summary
A multicloud strategy, where you have a business-critical application that’s engineered to run across multiple cloud platforms, can be appealing for a number of reasons, including reliability, regulatory and risk. But, like most architectural decisions, there are trade offs. Here our podcast team explore the intricacies of multicloud and the implications of making that journey.
#### **Full transcript**
**Ashok Subramanian** : Hello, and welcome to the Thoughtworks Technology Podcast. We are joined today by my co-host, Rebecca.
**Rebecca Parsons** : Hello, everybody, good to be here.
**Ashok** : We really want to discuss a topic that's been going around for quite some time but doesn't really seem to have too many elegant solutions in place, and hopefully, our guests today can shine a lot more light into what the reality of this problem actually is and what potential solutions could be there. Our guest today is Bharani. Bharani, would you like to introduce us?
**Bharani Subramaniam** : Sure. Great to be here. Bharani Subramaniam. I'm one of the Heads of Tech of India. I'm happy to be here.
**Ashok** : The topic today is multicloud, and we're really going to explore what multicloud actually is, and for organizations that are going to go through a journey of being on multicloud, what are the kinds of things that you really should be aware of? Before we start, I think it would be best to try and really shine some more light on what really is multicloud?
**Bharani** : That is an interesting question. To me, a multicloud means that you have this business-critical application that you want it to be portable across two or more cloud providers. A lot of people confuse this with, "I'm using the best of breed across two cloud providers, and is that a multicloud?" I think, as Thoughtworks, we kind of see things apart, and one, we call it as a polycloud where you use the best each cloud provider has to offer and invent an application the same way you use multiple languages to your microservices architecture, and we call that polyglot programming. People usually confuse multicloud with polycloud. A multicloud to me is that you have an application that completely works in one cloud, but you make it cloud-neutral so that given a choice, you should be able to run across two or more cloud providers.
**Ashok** : Great. This is effectively making sure that any service or application as far as the end-user is concerned, or even the maintenance of the service, they don't really know or care about which cloud it might be running. Okay. Is this something that you're seeing a lot of today? We hear of a number of vendors that come with different tools in this space. Is this something that you're actually seeing in production, organizations having solved this problem?
**Bharani** : Yes and no. A lot of people are interested in what they could do with this multicloud, but you need to have a level of maturity, and you need to have a consistent revenue from this application for you to even start in the multicloud journey because, like Martin Fowler puts it, "You need to be this tall to have a microservices architecture." A simple way to look at multicloud is you need to be twice taller.
It is going to cost you money, it's going to cost you time in engineering effort. So, yes, quite a few businesses are interested, but people are proceeding with caution because not every business is at the scale of Netflix and Ubers of the world, but they're interested because once you're successful as a digital startup, and if you are at a level where the business feels there is a perceived risk to the brand due to the walk-in with one vendor, then people embark on this journey of going multicloud.
**Ashok** : There are different flavors that we've seen of organizations. I think one of the things that tend to see more often is effectively the types of services that you run between one cloud or another. I think one of the things you'd also mentioned about-- you need to be sort of this stall. The kinds of scenarios that you see, what is actually driving it? One is definitely criticality of service and availability. At least in some markets of the world, we're also beginning to see, depending on regulatory pressures, people wanting to have answers to, "What do you do if your solution fails on one cloud provider?" Are there any other drivers that you see for this subtlety?
**Bharani** : Yes, I think those two are pretty important, what you just mentioned, Ashok. We have seen one other use case where, let's say, you're a digital native startup and your business has grown and you're expanding geographically, and you expand into countries where the usual cloud providers are not either existing, or you have better leverage if you have to go with the different cloud providers in that country. We have seen cases where, let's say, for example, I want to establish my business in China, and I don't have the same cloud providers in China. We have seen cases where geographical expansion has forced business entities to consider multicloud.
The point that you're making on regulatory compliance is valid. I believe there is a lot of confusion in interpreting-- when you directly interpret what used to be applicable to traditional data centers to the cloud. When you're operating your own data centers, the regulators do demand that, "Okay, if something goes wrong, what are your procedures to have a failover?" If you apply the same principle to the cloud, I think it's fair for regulators to ask those cloud vendors who are really big, and they operate data centers much more effectively, then do it.
At end of the day, it's still a data center. It's fair from a regulatory perspective to say, "What's your policy? How are you going to handle if something does go down?" We have seen those in financial sectors where if you are running a digital bank, or with the current pandemic, more and more people are relying on digital banking needs. The services are business-critical. It makes sense for the regulators to come and say, "Tell us how your services will behave if one of your vendors goes down," or, "Do you have too much dependency on one cloud provider?"
**Rebecca** : Well, I've been thinking about that. We've had this discussion internally as well, again, particularly as it relates to financial services organizations. The major cloud providers all have availability zones. That is, to my way of thinking, the analog of a disaster recovery site for an on-prem data center. Well, yes, it's a completely different data center, separated by geography, all of those kinds of things, so you get to the point of saying, "Okay, are we really worried that Amazon Web Services are going to shut down tomorrow?" Is there a basis, really, for the regulators to say, "No, it is not sufficient just to go to a different availability zone, that it has to be, yes, you can both run on AWS and GCP"?
**Bharani** : I think that is a fair question. In fact, we do advise our clients that expanding across data centers of the same cloud provider is probably the first step in increasing your availability. There are situations where these availability zones, if you take a country like Singapore, it is a relatively small region. These availability zones, if they are located inside the same country, there is still a risk that if there is such flooding in Singapore, I'm sure those availability zones are going to go away, but you're absolutely right.
There is no reason why that is not an approach you can take. There is also this-- this goes back to your reputation of the brand, or a single business entity does have an influence on your business, then it really comes down to, "Are you willing to pay the cost of going multicloud?"
In most of the cases, I would say that going across multiple availability zones is more than sufficient. What we have seen is people don't completely deploy their application across availability zone. What we have typically seen is that I have this database instance, I want to get that across multiple availability zones, but people don't run their compute layer across availability zones. Then the regulator's point is valid is that if something goes down, then you would take a fair amount of time to recover your service because you have to deploy, you have to bring up the services from the other instance. Very rarely we've come across an instance where an application is distributed end-to-end across all layers of the stack across multiple availability zones.
**Ashok** : Yes, I think another probably-- view on this, maybe a few years ago, the set of services were fairly limited across most of the major cloud vendors. As they have expanded and provided much more richer, higher-order services, their own internal complexity has increased as well. The probability of failure seems to have gone up as we can see with more recent outages. It's harder trying to balance between using services for convenience versus the increased probability of failure that comes along with that as well. I think it's really good-- sets it quite nicely into-- yes, we are now on the track of figuring out that this is probably a challenge that needs to be solved. What are common approaches that you've seen? If you are going to go trying to distribute your service across multiple cloud providers, where do you start? How do you start?
**Bharani** : Yes, it's a great question. I think you would probably start with some sort of inventory of-- you have this single application, but no application lives in its own isolation. You have a number of services that this application depends on. Usually, what we have seen is organizations do tend to keep this in their inventory, they document their services, but what you really need is this graph of what are all the use cases, what are the user journeys and system journeys, and how they're mapped to the systems.
You need the complete data flow because you are trying to lift the entire ecosystem of the application and distribute it across the data centers. For you to do that, you have to follow the data and build this graph. Basically, this is your starting point to take a deeper look at the system and say, "Okay, this is how I'm going to partition my traffic and split it across the cloud provider." That is going to take most of the effort, I would say, before you start deciding on what approaches you're going to take. Having this dependency graph does make sense. I would start from there.
**Ashok** : So, actually figure out what is that you need to really distribute, and in order to get that to distribute, what is the dependency check? Are you using cloud provider-specific services? Are you looking at data residency in certain locations and so on? Okay. Once you have established the starting point, are there any principles that you could say that need to be thought of as you're considering what future architecture might be like, considering the fact that more systems are unlikely to have been designed to be distributed across portable clouds from the offset?
**Bharani** : What we use as a basic engineering principle for building an application still applies in this case. Even when you are taking a fully functional application that's running in one cloud and trying to make it portable, you can still approach it from the point that you would incrementally build this digital clone because if, let's say, you decide that you need to go multicloud and you completely fork your development graphs, "Okay, I'm going to have a different set of team working on a different branch that's going to build this product which is going to be portable across," it's highly likely that you're going to break things that are already in place, and the feedback loop is going to be longer.
A good starting point is that you continue to make the changes in the main branch as the rest of the product development is going on, but you make incremental changes and you test not just in your current infrastructure, but also in the target infrastructure, which is more than one cloud, and this way, you'll be sure that when you're making it portable, you're not breaking what is already in place.
Make it incremental-- it's going to be a long journey, but even if you, at some point of time, decide this may not be the approach, you don't have a lot of wastage, right? At the max, what you have is that you might have reduced the number of dependencies that you have in the current flow. That's probably the worst thing that can happen as supposed to completely forking and having two different products, one tied to one cloud provider, and another being a tied to another one.
**Ashok** : Would you say in order to run a test that-- trying to figure out whether you are reducing the dependencies, running your stacks, say, in your entire deployment pipeline, maybe your infrastructure that you use for testing could be on one cloud provider and your production infrastructure could be another as a path towards that, would that be something that would make sense?
**Bharani** : I have come up first one case where they have the complete test environment in one cloud vendor and their production in another. This may sound like an extreme case where you want to test for portability, but I wouldn't recommend this approach because you don't catch what you used to catch when you are with one program. If you're testing against one and deploying in another, it is going to be portable, but you may not discover bugs that are going to be in production, and that's going to be too late for you. I would recommend a test enrollment to mirror production as much as possible, so if you are going down the multicloud approach, have the same number of cloud providers, preferably the same cloud providers in the test environment.
**Ashok** : Okay. Yes. I think that's a good tip, definitely. I think we always talk about environments that are there prior to production, middle production, so, yes, definitely something to think about in that journey. I think there is another aspect to it in terms of-- I think you touched upon when you were talking about availability zone and you talked about having data, or having data replicated, when you are having a service that potentially sit on any cloud provider, how do you manage for things like cost of the amount of data that's moving across? Should we be doing something like that, or is that something to be avoided?
**Bharani** : The thing is, it's important to start with this notion that your cost is going to be double when you do a multicloud. It's good to start from the fact that you accept that it's going to double and you can apply a number of optimization to actually reduce that, but if you really think about it, if you have one unit of data, no matter how you partition, just because you want things to be reliable, you are going to replicate it in some capacity.
It's going to double storage cost for sure, but the storage cost doesn't scale linearly. It's relatively cheaper as supposed to the compute and other services that you consume, but you have to mirror those anyway, so it's good to start from the point that it would be 1.5 to 2X at least because when you are in this journey, there would be a period of time based on the size of application for it to get stabilized.
When you're developing, your test infrastructure is going to add to your cost because you're having two cloud providers in your test environment, and you're also migrating data. At one point of time, you may have more duplicates than you want to have. If we plan for 2X and then optimize, I think that's a much better approach because otherwise, you going to have a bit of a shock. A big shock, actually.
**Ashok** : When you talk about this 1.5 to 2X, that's just on the infrastructure cost, right? You are not really accounting for the additional engineering effort that needs to really go to try and manage this across.
**Bharani** : Exactly. In fact, it was not everything. I forgot to mention about network. If you have two cloud providers, depending on how you manage the traffic, there would be some amount of EKS fee because you're going to route traffic from one cloud to another. There are ways to manage that, but the networking cost also adds up, and you're right. The biggest cost is going to be the cost in engineering, and the cost of time-to-market because it is going to take significantly more time to build this cloud-neutral app because you're not completely leveraging everything the cloud vendor is offering, right? That is not to say that if you have to make it neutral, you have to target the least common denominator because if you just leverage cloud for its computing and networking resources, that is a loose scenario. You lose and you take more time. Then the vendors also lose because you're not using their services. All of that adds to the cost, and infrastructure is just a part of it.
**Ashok** : Actually being mindful-- if you would say, a principle should also be about trying to map the business capabilities and independencies as well in a certain way in your architecture to reflect that so that you don't end up designing something that ends up being too cost-prohibitive just because you haven't really thought about access patterns and data locality.
**Rebecca** : Going back to the least common denominator thing for a moment, have you seen useful patterns or principles to use, to decide, should I build an abstraction layer above the services and come up with a cloud-specific implementation that takes advantage of at least some of the different cloud vendor services? Because they have roughly the same capabilities, but often implemented in different ways. How do you decide when it's worth doing something like that versus when you do take it a bit lower down and just use some of the more basic resources of the cloud provider?
**Bharani** : Very good question, Rebecca. When we talk about-- let's take an example, let's say I want to store something in an object-store. Things like S3 is almost a commodity right now in the sense that pretty much all cloud vendors give you some sort of next-gen compatible API, so you don't have to build this yourself or host your own ObjectStore. You can rely on matured services that are almost a standard right now.
The same goes for, let's say, if you are leveraging services like RDS from Amazon, there are equivalent services in other cloud vendors. In the end of the day, it's going to be database connectivity, and that's common. Things do get tricky when we go to the API orchestration layer, for example, Kubernetes. There are so many flavors of Kubernetes right now. What AWS has is the same, but it's slightly different from, let's say, what Google offers in GKE.
Our advice is, this layer of abstraction is useful for you to build it against in such a way that you leverage the hosted services of the cloud providers, so you don't have to host your own Kubernetes and make it the least common denominator, but you have to do it in a way that the control plane is native to each service, but you have some control on the data plane so that you minimize the differences. This also gives this flexibility to developers that, whenever I want to talk from service A to service B, my network layer on the data plane is going to be common no matter where it is deployed.
Because we have seen a lot of surprises, especially in the data plane on the network layer of Kubernetes, so it makes sense to build that kind of abstraction or high-level of competence like Kubernetes. I say, as an abstraction, not to say that you need to have your own Kube-API layer and make it common. All these systems have standardized all the interfaces. It's up to us to leverage them in a way that you don't have to build a lot to build this thick layer of abstraction because the cost of maintaining that would be very high because all these products iterate very quickly and you want to let them stack.
As long as you fit into the model where I will have a pluggable plane to maintain this abstraction, then you're good. Just as an example, let's say that I want to standardize the data plane in such a way that my services should be able to talk from one cloud provider to another, the CNCF has an article which we can link, there are N number of ways you can do it. You can do it via service mesh or you can do it at the network layer. If you build your abstractions such a way that, "Okay, I'm going to have common service mesh and I'm going to use that as a way to talk across pods," that's a good abstraction to build on. This gives you this flexibility where you don't have to maintain this abstraction other than saying, "This is my standard topology that I would use for Kubernetes."
**Ashok** : You touched on data again over there, especially around the fact that if a service at the application layer is distributed, its access to the underlying data in order to satisfy the end-user request might potentially be split across as well. Are there any patterns that you would suggest or recommend in terms of how to think about data or data locality, and should you really think about doing multiple rights, or do you recommend that actually you pin your rights to anyone and then replicate?
**Bharani** : Yeah, when it comes to data access pattern I think a simple rule to keep in mind is that you always aim to make the reads happen locally irrespective of how many data centers or how many cloud providers that you work with. You aim to read the data locally because reading over the network is going to be slow. 
Based on this, if you think of it in a traditional set up where you have a single cloud provider, you will have your primary data stored to an N number of secondary read replicas. And in this setup you will have all your rates routed to the primary data store, and all the reads happen out of one of the secondary replicas. 
If you extend this model to multicloud you get a topology where your reads can be spread across the cloud providers, but the write has to be routed to the correct cloud provider which is acting as a primary. So that’s the first access pattern. It’s very easy to set up but it’s not very flexible because you still can’t scale your write uploads. 
Which takes us to the second pattern where you still enable the local reads, but we try to enable the local write, and here local I mean within the same cloud provider. So one way to do this is if you can partition the data, and you make sure that each cloud provider kind of owns its own partition. So this way if you get a request and you can route the request to the right cloud provider then you can enable write at least within the same cloud and without routing the same request to the other cloud provider. Because for its own partition there can be a primary cloud database to handle the write and the reads can replicate from this primary data store. So this is just the same traditional primary and secondary replicas and one cloud provider being extended to multicloud center where you achieve local reads and you achieve local writes within the same cloud provider, because you’ve fundamentally partitioned the data. And these partitions are independent. So that’s the second access pattern.
I think the third one is slightly difficult because you have to fundamentally change your data layer. This is an option where you embrace the new types of data stores where there are no primary or secondary instances. Every single instance is a primary instance. We call these kinds of data stores new sequel data stores. An example could be CockroachDB or Titanium DB. 
So this is a flexible setup, but at the same time it’s most likely that your API is not built for these new sequel data stores so you have to refactor a lot to adopt this. To fit in this new sequel paradigm. But they do give you a lot of flexibility because you don’t have to think about explicitly partitioning your data because these databases do it for you. So to summarize I would think of thinking about it with the simple rule that we always try to enable reads from local. Writes can be scaled if you partition. And these two patterns work for relational data stores. And the third category if you want to embrace the new sequel, there will be an upfront cost because you have to refractor your API, but it could be a much more flexible option for you.
**Ashok** : Suppose that complexity bubbles all the way down the stack as well, and complexity in terms of trying to-- not just for a developer who's actually building or writing in the system, but also all the way into operations and operability as well of that, I suppose.
**Bharani** : Yes, totally. There is no easy answer there, unfortunately.
**Ashok** : Rebecca, I think you have only said it's all a question of trade-offs, architecture.
**Rebecca** : Exactly. Our favorite word.
**Ashok** : Which of the difficult decisions that you're going to end up taking along the way? I think touching on this around operability and observability, when you're running in a single cloud rack, you might want to take advantage of a lot of the tooling that you get out of the box. When you're running across multiple clouds, what are the approaches? What would you say should people be thinking about in terms of any standard in this space?
**Bharani** : This goes back to the useful abstraction discussion that we had. When we talk about observability, usually when people build an observable stack, you have distributed tracing in place and you leverage some kinds of services from your cloud providers because maintaining that infrastructure does require expertise and time, and investment, I've seen most of the applications where this observability is consumed via service.
One thing to keep in mind is that if you are building for a multicloud, if you embrace a standard like OpenTracing, you will always be able to achieve this portability because pretty much all the vendors are catching up. If your microservices only depends on OpenTracing libraries and OpenTracing API, it's going to be relatively easy to plug in either a hosted solution for this or even consume the native services because this is almost becoming a standard right now. I would just embrace OpenTracing and not build any custom tooling for this because solving distributed tracing is a really hard problem, and where you already have this complexity of multicloud, you don't want to solve that with the least common denominator in mind, so I would just take that OpenTracing.
**Ashok** : I think the natural extension of the operability is, I think toward the start of this, you were talking about, well, if you are running your test environment in one, then production in different cloud, you actually won't really know what's in the failure scenarios that might happen, but actually, failure does happen. What might be a DR strategy in this case actually look like?
**Bharani** : Yes, it's interesting, right? I think it's kind of assumed that if you are going down the multicloud, I would recommend reliability over something like DR because what tends to happen with disaster recovery is this word "disaster". People subconsciously associate that with, "Okay, the entire cloud is going to go down, and how am I going to respond," whereas now it's more of, "I'm getting a lot of requests or something is wrong in this one particular service. We have paid such a premium to be spread across two cloud providers. Can you fall back to the other cloud?"
I think if you have that reliability mindset, it's better to think of reliability than, "What will I do when you have a disaster exactly," because what usually happens is you will have all of those in place and you will not automate the switchover, right? I think it's fair to say that if you are going down the route of multicloud, if you think of a manual switchover, or even a very coarse-grained switch-over of, "I will only failover when my entire stack is down," or, "I will only failover my entire DB is down," you're not getting the best out of all the investment that you put in. DR is still important because you still need those backups, but prioritizing reliability over recovery is really key.
**Ashok** : It's almost-- you have to shift your mindset similar to a lot of the other things that you spoke about earlier in terms of how you approach, what might have been a traditional approach to disaster recovery. I think we briefly touched upon this earlier about the effort. You spoke about the majority of the organizations. Probably not underestimating the amount of effort this takes because I think one thing to bear in mind is, these aren't static platforms. In fact, they're probably-- each of the cloud providers, they continue to release services at a mind-boggling pace, really are targeting multiple moving stacks on either side.
Both from an organization majority and developer experience point of view, are there things that you would say, "Actually, before you go on this journey, just make sure you should have been doing--" when you say, "You should be this tall," could you elaborate a bit more for listeners what, in your view, "this tall" might actually mean?
**Bharani** : Yeah, in addition to the complexities in the data layer that I just spoke about, one other topic that I would request organizations and developers pay attention to when they are embarking on this multicloud journey is networking because obviously you have a lot more choices to make in your network design. The goal is to make it simple because going multicloud is going to complicate a lot and you really need a simplistic network design to begin with. For example, you need to think how you’re going to route the requests in your multicloud setup and where will this logic reside? Is this going to reside in the front end or the back end? And if you desire to do this on the back end, where are you going to put this logic? Because this logic should also scale, otherwise it’ll become a single point of failure. 
So there are a number of choices to make, and should you have to manage this routing logic and the routing infrastructure yourself or can this be given to a different provider? So there are a number of choices to make in your network design so I would encourage you to pay attention to that. In addition to the choices you have to make in the data layer because it is going to get complicated. We spoke about the three different patterns. Irrespective of which pattern that you choose for your multicloud setup, the amount of data is going to increase because you’re going to keep multiple copies. Whether you partition the data or you embrace new sequel, your volume of data is going to go up, and you’re going to keep more copies for reliability and for scaling. So I would encourage everyone to pay special attention to data and networking if you’re going to embrace multicloud.
**Ashok** : That's some very, very good and sage advice to people who might be considering going down this journey, or even maybe looking at your existing levels of maturity on just a single cloud provider if you aren't. Most organizations at least have some aspect of on-premise and cloud, how well you deal with that to start with before you start embarking on-- that was really great insights, Bharani. Thank you for sharing this with our listeners. I am sure anyone who is sort of embarking on this journey or even actually is on a single cloud point at this point, there will be some good takeaways for them from this episode. Thank you very much. Thank you for taking the time, sharing. Thank you to my co-host, Rebecca, for joining us on this podcast.
**Rebecca** : Thank you, Ashok. Thanks, Bharani. I think that's quite a cautionary tale. Hopefully, people will think about the cost-benefit trade-off of this and decide if they really want to go multicloud.
[ View more ](javascript:void\(0\))
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
Jim Highsmith: a 54-year agile journey 
August 26, 2021 
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
## Explore the latest Technology Radar
[ Explore ](https://www.thoughtworks.com/radar)
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