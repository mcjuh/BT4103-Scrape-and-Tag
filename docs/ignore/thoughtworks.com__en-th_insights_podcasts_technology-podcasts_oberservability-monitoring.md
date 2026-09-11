<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/oberservability-monitoring | Title: Observability does not equal monitoring | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Observability does not equal monitoring 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons and Neal Ford | Podcast guest  Bharani Subramaniam and Prasanna Pendse
July 23, 2020 | 30 min 16 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/oberservability-monitoring#transcript)
Listen on these platforms
## Brief summary
When working with modern distributed systems, complexity is a given. But how can you make observability a characteristic of your systems, such that your operators get feedback in the event of an outage? In this podcast our co-hosts Rebecca Parsons and Neal Ford talk to Bharani Subramaniam and Prasanna Pendse about the monitoring and observability in cloud-based systems.
**Podcast transcript**
Rebecca Parsons:
Hello everybody and welcome to the Thoughtworks Technology podcast. My name is Rebecca Parsons, the chief technology officer for Thoughtworks. I'm one of your hosts and I'd like to introduce the rest of the panel for today. Then we'll talk a little bit about observability and monitoring. So Neal?
Neal Ford:
Hi, everybody. I'm Neil Ford director and meme wrangler at Thoughtworks and another of your regular recurring hosts. And today we have a couple of our colleagues who are quite interested in a subject we're going to talk about today. So I'll let them introduce themselves. Bharani.
Bharani Subramaniam:
Hello, this is Bharani Subramaniam. I'm head of Technology Thoughtworks, India.
Prasanna Pendse:
Hello. This is a Prasanna. I'm also the head of Technology for Thoughtworks, India. We can fight that out later. We have three actually. With two of us here.
Rebecca Parsons:
Okay. So we'd like to talk to you today about observability and monitoring. And there wasn't necessarily a whole lot to talk about when everything was running in a JVM on a single process, you know, life is good. But we have encountered multiple situations where we've had to start to tease apart the distinction between these two things when we're in a distributed architecture world. So let's start with the basics. Bharani and Prasanna Pendse, how do you define the difference between the activities of monitoring and observability and what the outcomes are that we're trying to achieve?
Bharani Subramaniam:
Right. I would define monitoring as a continuous process of checking the output of the system, right? So it can be anything like is the process alive? Are we getting the heartbeat or the list latencies that's satisfying the SLA. So those are the things that we usually call as monitoring. Whereas observability is more of how well can you measure the internal state of the system based on its external output? Right. So when we talk about observability, we usually think about what are the service calls that are getting call when this user performs this action in the system. As opposed to just checking the status of the system.
Neal Ford:
So there's an implication in observability of being able to peer inside. Whereas monitoring is more black box. Is that the distinction?
Bharani Subramaniam:
Yeah, that is the distinction. So...
Prasanna Pendse:
And monitoring is an active action that somebody is doing. Whereas observability is characteristic of a system in the sense that observability is and monitoring is continuous action that is performed. Observations of a system that is observable, but usually monitoring does not try to change the system that is being monitored, right. So you just kind of observe the things that are happening without anything special being done on that system. Whereas for a system to be truly observable, it needs to do something extra to expose this internal state.
Bharani Subramaniam:
Yeah, exactly. So like what Rebecca was mentioning before, if you just had a single process running on a single machine, then monitoring is enough. But if you have multiple processes running in a bunch of machines, even if you have the instrumentation coming out of the system, you need something to stitch them together to give a coherent feel and hence we need them observability.
Rebecca Parsons:
So it is both given the white box, black box distinction that Neil was making at a high level, the objective is the same. You want to understand what's going on in the system. But at the lower level actually with monitoring or I guess with a single system or a single process on a single machine, there is less you have to worry about because you just look at the outputs. And where we have distributed systems, just looking at the output from the different systems in isolation doesn't give you an end to end view of what's going on.
Prasanna Pendse:
Right. When you're in the world of a single system, monolithic code base and all of that, tools that do instrumentation can actually instrument pretty well, especially in the Java world. And can inspect what is inside the code base in terms of function calls and all that stuff without having any real change being made in the system. But they would struggle to tie together why one system behaves in a certain way and another system behaves another way. What is the linkage between these two, especially when you multiply that by 10,000 servers doing lots of different things. It's very difficult to chase down a single event, single malfunction and be able to root cause it without having observable people into the systems.
Rebecca Parsons:
Okay, so then how do I go about achieving observability? What kinds of things do I do? What kinds of changes do I make to the system to end up with something that has this characteristic of observability?
Bharani Subramaniam:
We've had this observability for a while now. I think the problem has always been what are the tools that we choose that is always a lock in and what happens to the court that the frameworks and libraries are using? So until this time, that has been a challenge of how would you place what's going on with the system. But with standards like OpenTracing this is now more approachable than it was before. So if I have to observe my distributed system in production, if the team implements OpenTracing in their code business with the heterogeneous nature, you can have agents and clients running for your own framework and languages. And you can instrument them with open standards. And you can observe the system in production is because it's talking the standard API.
Neal Ford:
But if observability requires action on developers, how can you ensure that developing teams are going to put the observability code in their code base? This seems like a major problem because if you're relying on this for insight and then somebody forgets to put it in there, then you lose the insight. Right?
Bharani Subramaniam:
That is true. So we are talking about a maturity level here. So if you have a fairly complex system, but you are okay to live that observing the boundaries of the system. Then there are a lot of turnkey solutions out there, lots of frameworks. There are middleware for OpenTracing so you don't have to write code, you just have to turn them on. And you can to a fair degree observe what's going on. That will take you to a level. But if you have to really understand what parameters when passed to this API is slowing down your system, you really have to depend on the developers putting that code in. Because there is no way to instrument that part from the outside. But if you just want to raise the boundaries of the system, this can be done in a turnkey fashion.
Prasanna Pendse:
So taking on a bit of a skeptical view to this, one of my questions or one of the questions that a client of ours been ask us, is either way what you're saying is, I need to buy AppDynamics or DynaTrace or New Relic or one of those things and turn them loose on my ecosystem as the first step.
Prasanna Pendse:
Why does this distinction particularly matter to me? Whether these things are running on a single machine or they're running against a cluster and with this tool, the Open Tracing turn on?
Bharani Subramaniam:
Yeah. And that's a really good question. So, I would answer that by asking the question to the team back. I mean people often say they embrace microservices architecture and they are following DevOps practices. And I usually ask this probing question of then, "What about OpsDev practices?" Right. So we have everything in our system to commit code faster to have continuous integration going on. You automated your infrastructure, you do all these things to make your operation life easier. What is it that you're put in the system for the operators to give feedback back to the development teams from production in case of an outage? So if you are running a distributed system, you need to invest on putting this information in your code. So when you have a date, well the problem of something going down in production, people should be able to support it.
Rebecca Parsons:
But isn't that what we used to use logging for?
Bharani Subramaniam:
Good question. But again, back to the same problem of if I just had one APA server running and I had this client, I think just tailing the log would be enough. I don't think that's the state anymore, Rebecca. So you have the N number of API and with Kubernetes people just changed replica set. And you now have 10 magic instances of the same API. Different hosts could have different time and actually stitching all this together and then having a system to actually view this, you would in the building what is already out there. So you don't have to reinvent this whole wheel of how to observe a system. You could just start off OpenTracing for that use. Most of the tools that is out there now adopt OpenTracing so you may not even know that your current monitoring tool is actually having absorbed the place right now.
Neal Ford:
Yep. That's companies like Netflix does a lot of innovation in this space. As they were innovating in microservices. And I saw a presentation from one of their DevOps folks. And they said that one of the ways they handle the problem of making sure that everything has observability code in it, is they use aspects to automatically wrapper every method. So that they know there's a consistent view from an observability standpoint. And it also strikes me since Rebecca and I are on the call, I can't resist mentioning that you could also use architectural fitness functions as a way to verify that every one of your functions touches observability and broadcast something as a way to automate that.
Bharani Subramaniam:
Yes, absolutely. I think the same initial question around logging, that part also applies. So even when we were in a single system, you had to log things in a particular way with a particular format in order for automated tools to be able to understand what was happening. And as you get into aspects of fitness functions is also a way of ensuring that you are doing that. Simple example that has existed for a long time was that if you don't log a credit card number by mistake. So having some fitness functions, that test started the way of doing that. Now in this system, one of the first steps that people may move towards is adding some kind of a correlation ID in your logging system so that you can trace, what happened in one thing and then have that thing go in throughout the stack for a particular call.
Bharani Subramaniam:
Right. But one of the challenges with that approach is it is not something that is portable from one type of a system to another. Meaning your database system may not actually know what your correlation ID is that an application server created. And before the request hits the application server, the web layer has done a few things that we have no way of tracing as a part of the same transaction because it could have made 30 other calls. And those get potentially tagged as different correlation IDs. And so tying all of this thing back becomes again, very specific to the particular platform that you're using. And then you add messages being tossed under Kafka and a hundred consumers doing something else with it. Then it goes to some other parallel universe. And tracing all of that stuff becomes a nightmare. Without having something that there's a standard way in which all of these different systems can specify, what transaction are we actually talking about?
Neal Ford:
Well, it strikes me that the skeptic persona just got answered by the pragmatist persona because that's a great answer to the question you posed earlier. Because the universe is different now. 10 years ago and we could rely on internal monitoring and logging. We didn't have Kafka and message queues and microservices and distributed architectures and all this crazy moving parts. So you can't assume that one part of the engineering ecosystem is going to stay static while all the rest of it changes and grows and into something completely different. So that's yet another rationale for, "Yes, we need more sophisticated tools to watch things because our architecture is way more sophisticated now."
Rebecca Parsons:
So I'll continue to play skeptic here. Why wouldn't I just use domain events? So if I've got an event driven architecture, I've got all of these domain events running around. Why is that not sufficient?
Bharani Subramaniam:
Yeah. For the same reason the correlation IDs are not yet sufficient. You still need a system to know which event occurred before which event. And yes, tying this together in a distributed fashion, it's not easy. Because you can't just rely on the timestamp from the systems because you may have systems that does not synchronized. So if you end up solving all of that, you are basically solving open tracing. So it's better off just to embrace the framework. Than reinventing the distributor trace. And the domain events are valuable. I don't think what we're saying is they're valuable, they're valuable to track what's happening in your business. Like is your revenue going up, number of orders going up, what does your conversion rate look like? All of those business metrics still need to be monitored. Somebody needs to be paying attention to that.
Bharani Subramaniam:
And collecting that, charting it, showing it, all of that is still valuable. But that's not the same thing as kind of the problems that OpenTracing is there to solve. Which is trying to debug something where something has gone wrong and you're trying to figure out exactly why did this order not go through. And or why do these class of orders not go through? And so they're having an ability to trace through is very important. But having a heterogeneous state where you have different types of technologies that were written in different eras, you will have a very difficult time kind of manually trying to trudge through that. And using some of these OpenTracing adapters you can get a deeper insight into even the older tech stacks as well as the newer ones.
Rebecca Parsons:
So Neil and I often get asked, "Okay, you talk about a fitness function, but what do these things look like?" So if I was going to add one of these architectural fitness functions to ensure that I had the right level of observability, how would I go about doing that?
Neal Ford:
I can start answering that question. There are a lot of tools like ArchUnit that will allow you to look at... So for example, let's say you decided to use aspects as a way to enforce observability. You could write ArchUnit to say, "Make sure that every a method that I make a change to in this code base is decorated with an aspect that does observability." So you can write those kinds of verifications with ArchUnit and the JavaWorld, a net arc test and the .Net World. So there are definitely some structural checks like that you could write as fitness functions. Even in a language like JavaScript, most of the linter tools or static analysis tools like PMD and Java, ESLint in the JavaScript World will let you look at the structure of your code and make some decisions about it. It's not quite as clean as something like ArchUnit, but it's definitely possible.
Prasanna Pendse:
And you'll need that at the time where you'll need that to test whether a given code base actually is emitting these events in a particular way or not, especially for the ones that are automatic. But I think there are other aspects also that you need to pay attention to. One is that the tech estate is generally quite diverse and not all of them will have something like aspects. And so there you will need to do something maybe a little bit more static. But there are also ways of keeping track of this in a dynamic way. So actually the OpenTracing tool set itself will give you that visibility and you can test against the output of that. When you run tests on a distributed system for a given transaction where there's a no op transaction, or something of that sort where you have the thing go through the system and you can test that that transaction goes through the system in a way that you expected to go through. So that's more of a runtime validation, a runtime fitness function.
Bharani Subramaniam:
Yeah. Or I would say if you can afford a service match in your infrastructure, you can also do this at the boundary of the network layer so you don't have to implement anything in your code, but you can trace the calls that happens to an API at the network boundary. Until this matches is pretty good for that.
Neal Ford:
Another good example of how the engineering practices have grown up to meet the demands of the more complex architectures we're building. So speaking of a service mesh, one of the things that we talk about in the evolution architecture book is this idea of what we call a Goldilocks Governance. One of the problems you have in microservices is the let a thousand flowers bloom problem of every artisanal development stack in the world. The problem you run into then is how do you monitor and create consistent observability across that entire stack. And so the idea of Goldilocks Governance is maybe that becomes the constraint on how many platforms you want to support in your microservice architectures.
Neal Ford:
How well supported are these platforms by the monitoring and observability tools that we've decided to standardize on as an organization. For example, monitoring tools like Nagios will run on a variety of different platforms. The common pattern in microservices is to create a sidecar component per platform that can plug into the monitoring infrastructure. And that way operationally you have a consistent infrastructure. Even if you have different implementation platforms for a different services.
Rebecca Parsons:
So how broadly available are tools respecting the open tracing standard? Is this available on most of the platforms that we see or is it still relatively limited in its uptake?
Prasanna Pendse:
Well, I think one thing is that open tracing is not officially a standard yet. At least according to their website it looks and behaves like an official standard, but it's not quite a official standards body that is authorizing that. However, a lot of tools have adopted it as if it were a standard because it provides a common playground for people to inter operate.
Bharani Subramaniam:
Hmm. Interesting. I think 2017 open tracing, was standardized is under CNCF. I don't know if that qualifies it for being an open center.
Prasanna Pendse:
Sorry, according to their website, so the first CNCF is not an official standards body.
Bharani Subramaniam:
Okay.
Prasanna Pendse:
The OpenTracing API project is working towards creating a more standardized API and instrumentation for sort tracing. So it's not like an IEEE standard or something of that sort. It is a new body that isn't officially one. But to answer Rebecca's question around tooling... Bharani you seem like you were saying something and I interrupted earlier.
Bharani Subramaniam:
Yeah, yeah. So I was going to say you answer to Rebecca in terms of tooling, we have Zeplin, we have Agar. There are a bunch of tools out there that supports most of the popular languages and frameworks out there. Be it Golang, Java, JavaScript, Python. There are adopters for all of these languages and most of the frameworks in these languages.
Neal Ford:
So it sounds like you would say that it would be considered a good piece of advice to use something that supports that standard, right? That would be a best practice of using air quotes here. But that would be considered a good idea in this space. So what are some other good ideas in this space? We touched on correlation IDs earlier, right?
Bharani Subramaniam:
Yeah. One other question that we often run into when we adopt open tracing is... Look, I have this logging and I need to log and I have open tracing. You can also log as a part of a trace. So which one should I use? Right? And this is one of the early questions that people seem to ask when they adopt OpenTracing. And the advise will always been, if you want to lock something that is attached to a user journey, you're much better off adopting open tracing for it than using your normal logger. But if you want to log something for the system, something is not working or something is down, you are logging for the operator. So you paired off adopting the existing logging framework because the thing with OpenTracing is that it's a choice given to the operators to turn on and off.
Bharani Subramaniam:
So if the production is observing a lot of transaction, you can go from constant sampling to let's say 20% of the traffic. If you are using OpenTracing to log a system events that are chances that it'll get dropped. So another quote unquote good practice is that stick with normal logging for system and application events and stick with open tracing for user journey deleted domains.
Neal Ford:
And it sounds like another best practice was don't use domain events. That feels to be like the same kind of eakiness of using domain stuff for keys and relational databases rather than generating keys. So that would be another considered good practice in this space is don't use domain events.
Prasanna Pendse:
I think the way, actually Bharani and I were talking about it earlier. The way it looks like is that OpenTracing itself is its own domain. That this is a specific concern from a operation standpoint and it has its own language and it has its own concerns. That is orthogonal to whatever business you're in. And so standardizing on that language allows you to get better at managing these distributed systems. So it has words like spans and baggage and things of that nature, which may not be in your business domain. But they help in standardizing a conversation from one operations team to another.
Rebecca Parsons:
Well, and also based on what Bharani was just saying about when to log versus when to use the open tracing system. It sounds like now we actually have three domains. We have the peer system. Gee, I've got a processor that's not answering me or whatever we might log at the system level. And then we have the business domain where we're talking about orders and sales. And then we have this open tracing domain. Which is helping us understand how a given business event has been realized through a series of activities that spread across our distributed architecture.
Prasanna Pendse:
Right, right. And I think across all of those domains as well as kind of the earlier technical advice that we have been giving to people, one of the dangers in the way a lot of tools are approaching this, is that they're trying to incentivize people to get locked into their stack. And this tracing is one way in which some of the disorder tooling provide their own ability to do monitoring. And what happens is that your entire operations team becomes kind of geared, your metrics collection, your dash boarding, all of that thing gets locked into a given tool. And sometimes for technical reasons, you may choose to move away from that tool to something else. And then all of that becomes a bottleneck. All of that prevents you from moving on. So OpenTracing kind of separates the concerns between the tool that actually does the work and the tool that does the monitoring. And observability is kind of the layer that enables you to separate those two concerns.
Prasanna Pendse:
So yeah, so kind of the best practices would be to avoid getting logged into a tool specific monitoring solution.
Bharani Subramaniam:
Yeah.
Prasanna Pendse:
And kind of try to separate us.
Bharani Subramaniam:
I was going to say, I would say plus one, oftentimes we see beams where the choices are constrained by what kind of monitoring tools are out there. I think that is sort of a 90 part that we have seen. So OpenTracing now you've seen the freedom where you can choose whatever pool to collect. But you can stick with the standards so you commit evidence that are for open tracing and the standards actually make the whole thing work.
Rebecca Parsons:
So are there other implications within my infrastructure, within my technology estate that I have to take into account, to be able to support observability?
Prasanna Pendse:
So one of the things that happens in this kind of a world where you have logging. You have the actual business events that are flowing through, you have these open tracing type events that are happening and probably other types of events that are flowing into the network. There's a lot of data that you're now moving back and forth in your data center. And so one of the challenges I think people have is the network infrastructure wasn't actually created for that much data to be moving through. And as we go through more modern systems, especially for example, you have Telemetry that is tracking user behavior. And you're not outsourcing that to an analytics company, but you're actually getting those events back into your system. And doing your own analytics and having real time changes in what you present to the user based on that. Those kinds of systems again the network traffic goes up and so there will be an impact to the kind of switches that you have and all of that.
Prasanna Pendse:
Martin talked about you must be this high to do microservices. I think that rule applies here as well is that yes, things are going to get more complicated. But you should venture into this world of distributed systems and microservices only if your need justifies all of the complexity that it brings with it. And this is one other aspect of that complexity is how do you actually trace things across lots of different systems in a way that is efficient on your network. Or how do you actually then change your network to be able to handle this.
Prasanna Pendse:
And that applies largely to people who they have their own data center. Obviously in the world of cloud providers, this becomes a little bit easier. Although if you end up needing to change that, like some of the cloud providers provide InfiniBand band connections. I'm not suggesting that you need Infiniband to do observability, but as your network needs grow cloud providers are probably going to provide better, faster connections than your data center can in the timeframe that you have to meet the business needs.
Rebecca Parsons:
Well, hopefully now we all understand the difference between observability and monitoring. And why we need to think about observability really as its own domain when we are architecting distributed systems, microservices based store or otherwise. So thank you Bharani, thank you Prasanna for joining us and we hope to see you all next time on the Thoughtworks Technology podcast.
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