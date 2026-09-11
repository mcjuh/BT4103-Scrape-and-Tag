<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/multicloud-regulated-environment | Title: Multicloud in a regulated environment | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Multicloud in a regulated environment 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Mike Mason and Zhamak Dehghani | Podcast guest  Scott Shaw and James Lewis
May 03, 2019 | 24 min 59 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/multicloud-regulated-environment#transcript)
Listen on these platforms
## Brief summary
In this episode, our regular co-hosts, Mike Mason and Zhamak Dehghani are joined by Scott Shaw, Head of Technology for Thoughtworks Australia and James Lewis, Principal Consultant, Thoughtworks UK. They explore the challenges of delivering an effective multicloud solution and how to assess the criticality and sensitivity of workloads.
**Podcast Transcript**
Mike Mason:
Hello everyone and welcome to the Thoughtworks podcast. My name is Mike Mason and I'm here with my cohost.
Zhamak Dehghani:
Zhamak Dehghani.
Mike Mason:
Today we're going to be talking about multi-cloud strategy and especially within a regulated environment. We're joined by two of our extreme experts here in the room who we always, always enjoy having around. There's Scott Shaw, he's here from Sydney. Hi Scott.
Scott Shaw:
Melbourne actually.
Mike Mason:
Oh, Melbourne.
Scott Shaw:
I'll make sure that's clear. There's a lot of rivalry and Melbourne's way better.
Mike Mason:
Do you want to tell us a little bit about yourself?
Scott Shaw:
Oh, I'm the head of technology for Thoughtworks in Australia. There I'd lived for many years despite my American accent. And I help to look after the technology end of our business in Australia, but also I do quite a bit of consulting as well, so mostly around technology strategy and making larger scale technology decisions.
Mike Mason:
And we also have James Lewis. That's James microservices Lewis with us from the UK. Do you want me to say a little word about yourself James?
James Lewis:
Yeah, hi. Hey everyone. So I'm based in the UK, been with Thoughtworks a fairly long time now, about 13 years. And much like Scott, actually I'd spent most of my time advising clients or helping clients to understand how best they can make decisions about technology choice, technology strategy, that kind of thing. Don't write as much code as I'd like, I think it's fair to say.
Scott Shaw:
I think we're both in that position.
Mike Mason:
Probably true for most of us actually is not writing as much code as we'd like. So the hook for today's discussion is really multi cloud. And as we've been discussing uses of multiple clouds over the past couple of days. There's been a few times, Scott, where you've kind of... you've almost face palmed over a discussion or something that reminded you of a story in the past. And so we thought multi cloud was worth talking about. So first of all, let's do 30 seconds on what multi cloud actually is and then maybe why you need to think about it in particular way.
Scott Shaw:
Yeah, I think... so we had on the radar a time or two ago, something about poly cloud. And I think I make this distinction in my head at least between poly cloud where you have a variety of cloud providers and you choose the one that's best suited for the task, you may have a particular reason they may specialize in some way. So I think that's kind of a separate issue from do you need to have a selection of cloud providers to manage risk for some reason? And I think we're kind of moving in... in Australia at least the regulator for the financial industry, the APRA, has just released some new guidance for the first time in a couple of years.
Scott Shaw:
They're sort of catching up to the industry in terms of their guidance around cloud usage and it's all about managing risk and managing... and a lot of that is managing the risk of having a single cloud provider. Which for ordinary reasons like disaster recovery or availability, a single cloud provider can probably give you everything that you're getting from your on prem solutions. But when it comes to managing prudential risk, then you really need to have, in certain cases for certain extremely critical workloads or extremely sensitive data, some strategy in place to be able to move between cloud providers if necessary.
Mike Mason:
So what you're saying is, so for disaster recovery and availability kinds of things, multiple availability zones within a single cloud provider would be okay, but for these other use cases you're talking about, it needs to be an entirely different company. So Amazon plus Google as a backup or Google as a live thing that you would be using every day. What kind of timeline are we talking on the mitigation strategy?
Scott Shaw:
That all depends on the criticality of the workload. So I'm talking about... when I say, okay, it's relative to the criticality and sensitivity of the data. We used to talk about materiality a lot and businesses were hesitant to put material workloads. Workloads that were core to the functioning of the business, they were concerned about putting that in the cloud. We've kind of moved beyond that discussion. So a lot of businesses, in Australia at least, have moved material workloads into the cloud and shown the regulator that they have the right kind of risk management processes around that and that they can apply the right level of security. We're really talking about certain, a very small percentage of workloads that are extremely critical. Maybe they have sort of real time criticality where you to be able to move over between cloud providers and I guess it's hard to put a timeframe on it, but in days in some cases.
Mike Mason:
Could you give an example of one of those kinds of work loads?
Scott Shaw:
Well, people being able to do online banking transactions for example. Or perhaps transferring money between banks, a critical transfer that had to happen, that was time linked or foreign exchange transfer or something like that.
James Lewis:
Just to interject at that point, I mean we... see I'm the UK so this is local to the UK, but there's been quite a lot in the press recently of banks exactly [inaudible 00:05:58] and the impact of their failure is actually... you'll read about it immediately on the Twitters. If something like we can't access our business banking accounts, we can't make payroll. That's potentially thousands of people who are going to have a... that there will be a knock on effect on, right? I mean it's, I can't pay my mortgage suddenly because I've not being paid because all this kind of stuff. So I mean, I used to... when I was working with a big Spanish bank actually, one of the... they were awesome team and one of their sort of quite senior folks that he used to say, "We have to be quite careful about this bit because that's where the money is," right? Because I mean, the money doesn't sit in a vault anymore, the money says in ones and zeros on some of these extremely critical systems.
Scott Shaw:
It's true.
Zhamak Dehghani:
And I guess the mitigation strategy or techniques that you would use, they're still applicable on a spectrum of cases. Right now we're talking about this extreme case of the core business of a large financial institute regulated. And you may want to... for some of those have an opportunity of like live switching between one or the other. But if you think about the same requirements but for a business that is not so regulated, clients are still may want to have the opportunity of changing their minds about their cloud provider and moving from one to another. So this maybe the time between switching from one cloud to provider to another expense, but it's still a capability that a lot of clients would, I assume, would want to have.
Scott Shaw:
I think that's the main reason to consider multi cloud. The timeframe, you're right, is a lot longer. You have time to plan for those kinds of migrations. But if you have a lot of data or you have a lot of applications in one cloud provider, the time... you can't just do it instantaneously. You probably have limited bandwidth to be able to move those things. So really that's the main reason you would want to have a strategy in place is to manage the business or commercial risk of being tied in with a single vendor.
Mike Mason:
And I think I remember you also use the phrase competitive pressure as well, right? In order to be able to maintain a negotiating position with your, maybe, your main cloud provider, you would want to have plausible other options in order to kind of keep them honest while you were negotiating prices of services and so on.
Scott Shaw:
Yeah.
James Lewis:
It's interesting, right. It reminds me a little bit of the old backup restore kind of thing. It's like, "Great, we've got backups, right? We're backing up everything but we've never practiced restoring. I wonder how much..." Which is almost makes the back ups useless, right? Because if you can't actually restore any data, then what's the point to do the back up. Kind of reminds me a little of that. I mean how much planning do you have to do for this? How much thought needs to go in? How much work is that stuff?
Scott Shaw:
Well, potentially a lot. And that's where you have to... that costs money and time to do that, to put that work in up front, to have a plan, to have a backup strategy whatever it is. It requires investment. And so that's why you want to be selective as to where you apply that and which workloads you want to go to that level of risk management on.
Mike Mason:
I know we've sort of seen some organizations kind of think about a multi cloud strategy and we've seen it drive them towards some behaviors that we think are not optimal. Do you want to talk about any of those behaviors? I mean, lowest common denominator, usage of cloud is an obvious one, but I think you mentioned some over the past couple of days as well.
Scott Shaw:
I think the first thing people have to consider is if they're thinking about moving something from on prem into the cloud, they have to ask themselves, is everything that they have in their architecture on prem really necessary to replicate in the cloud? It's probably... there's this idea of cloud native architecture and you probably want to be designing things quite different. And there's a tendency for people, I think, to say, "I took advantage of this feature," whether it's a particular kind of switch or load balancer or whatever they may have had in hardware on prem, it was available there. That was the thing that the capital investment had already been made and there was no additional overhead to using that feature. They never really asked themselves, is this necessary? If I'm going to cloud, I'm going to pay for everything on an individual basis. Do I really need that feature anymore?
Scott Shaw:
So that's the first thing that people need to ask. I don't know if whether it's multi cloud or not, but the thing is that if you have to consider a multi cloud solution, those things become exponentially more expensive and difficult to replicate from an on prem solution into a cloud solution. So that's the first thing. I think the other thing is you need to have some rational basis of assessing the risk and criticality of your workload. Because everybody thinks their particular application is ultra critical. There's a tendency to overestimate, I guess, the criticality and sensitivity of what you have. And of course, you need to be conservative and prudent in how you manage those things, but you'd need to have some sort of rational predetermined way of scoring, I think, the criticality to know what sort of controls to put in place because they're expensive.
James Lewis:
Yes interesting. I mean, it's a hedge essentially against some future down side. To play devil's advocate, I mean how actually likely... I'm going to ask the group, how actually likely are these risks to manifest? And I guess what we're saying here the elephant in the room is we're basically either for commercial reasons or for risk management reasons. Saying that at some point Amazon or Microsoft or Google will go out of business or decide to stop offering cloud solutions. Is there a fractionally small chance of that happening? [crosstalk 00:12:33].
Scott Shaw:
I don't think it's so much them [crosstalk 00:12:34] I don't think it's them going out of business. I think it's the view as a business making a decision to move away from them. That's what the risk is. Is there may be some reason... yes, it's a low probability. If you're talking about certain prominent cloud vendors, then yeah, it's a low probability event. But there may be reasons that you may be in a competitive situation with them in another line of business that there may be some kind of sovereignty concerns. So there may be some kind of foreign government interference that people are worried about in some way. I mean, there's a variety of reasons why you might want to move. And that's not just cloud providers, really, I think this is causing people to stand back and look at their suppliers, their IT suppliers as a whole and being more cautious about getting too heavily involved with anyone and creating that really strong dependence. Because there's a variety of reasons you might want to move away from a given vendor.
Zhamak Dehghani:
I didn't do what Scott said on the... I mean, the clients that I have they haven't been on that extreme end, but they still wanted the option of being able to move from one cloud to another cloud. And one technique that we have been kind of emphasizing is automate, automate, automate. So automate all the cloud infrastructure, set up deployment of your applications, environment configurations so that the move from one cloud to another cloud is rewriting those scripts and modifying those. Are there any other techniques? I know that we talked about how we choose different capabilities that cloud providers give us to not lock us in.
James Lewis:
I think we talked about this in the last edition of the radar, certainly in the discussions we had in the room about how much Docker and Kubernetes is going to unlock in this sort of space. But I think that goes back to what you were saying Scott, about cloud lift and shift, which is also on the radar. Some issues are going on how it's not easy to suddenly deploy a 10, 8, 5, 2 year old system suddenly into Kubernetes cluster and expect it to work, right? I mean, the classic set of features that you'd sort of talking about I mean, the classic one is, "Oh, we've got this sand. We rely on this sand across multi-sites to do active, active or whatever to do replication. We don't have that anymore. How do you do that in Kubernetes?" But interestingly I think as an abstraction layer, I think that is something that potentially gives us the ability to, if you build with that as a target, to move between clouds more easily I think.
Scott Shaw:
I think it gives you walk up kind of strategy. You can start with the cloud providers native Kubernetes support, and that's much easier than having to build and manage your own Kubernetes cluster. And then if the time comes that you need to be able to consider portability, then you could implement your own Kubernetes infrastructure that goes across clouds. And I think there's a lot of promise there with containers and container orchestration to buy you some independence from the cloud provider. But I wouldn't go into it lightly. It sounds nice, but I think there's a lot to learn about building and operating your own cluster.
Zhamak Dehghani:
And another conversation we had around this was different services that cloud providers give us and how easy it is to pick a managed service. Like a managed event streaming capability, even if it's half-baked versus operating your own Cafco or an open source equivalent of that. I guess that becomes another access to evaluate locking with...
Scott Shaw:
I think that's the trickiest part of a multi-cloud strategy is understanding which of those platform services you want to go all in on with a single vendor. Because it's a slippery slope if you start using one, then there's a lot of incentive to use another and because they're often so intimately linked, you may not even have a choice. You may have to use one platform service like log management, for example. You may have to consume a whole raft of other platform services. And so that's where there probably need to be some governance or some guidelines to application developers as to which ones they are going to consume and which ones they aren't. If you're in this middle ground of moderately... I think what APRO in Australia called it the heightened risk or a heightened criticality. It's not the extreme end, but it's not at the low end where you just want to rebuild everything in another cloud if you have to move over, it's kind of in the middle. And that's where it's a bit tricky.
Zhamak Dehghani:
And I guess another... like in terms of... I know we moved away from this idea of generic cloud. I think we, we called it on the radar that you try to abstract everything away so you're at the code level. You have no idea whether I'm talking to an Amazon service or a Google service. And then the extreme of that could be quite, I don't know, not very effective. But there are some libraries that help you with that. A lot of kind of libraries in the Spring ecosystem try to abstract that services away. Is that something you think we would advice?
James Lewis:
I think that's a really hard question. Because it's all context dependent, right? Apart from be very careful as Scott was saying, consider the criticality of the systems that you... because you've always going to lose something when you're not targeting a specific provider. There's always going to be a cost to doing that. And so the generic advice around always try and target lots of different clients is, I think, probably wrong in many situations.
James Lewis:
I wonder whether we are sort of lagging and whether our thinking actually as an industry is lagging some what. Over the last couple of years we've seen so much change and it's very hard to keep up. And so there's sort of new patterns I think we're sort of seeing starting to emerge. There's a lag with what we understand that we can do with the technology we've got available now to what we can actually do-
Scott Shaw:
People's skills are catching up and-
James Lewis:
Yeah, right. The implication [crosstalk 00:20:03] things are changing.
Scott Shaw:
The tools are still... seems like we've been talking about cloud forever now. But we're kind of entering a new wave of tooling. And the Amazon API APIs were really great and when we first started using them it was a revelation. And they provide a really good developer experience compared to any alternative people had at the time. Now there's a new generation of cloud APIs and developer tools that are built on all that experience and are even easier to use and provide an even better developer experience. And it's taken time for, I think, the cloud providers to understand what it is that people want and what makes it easy and what sort of operations you're going to have to do repetitively and so on. And to create that abstraction layer that you were talking about Zhamak, means that you have to forego all of that experience that's been built up, and the understanding of how developers actually use these things. Because the cloud providers have already created a set of tools that are meant to be directly consumed by developers and people doing the deployment and operating these systems in the cloud.
James Lewis:
I guess where I was going, maybe to clarify is that the global is lagging the local with this kind of stuff. Like a bunch of developers running code can do all this really exciting, cool new stuff, right? But then this sort of strategy is then lagging behind the abilities that we get from using a lot of this stuff. It's sad, I mean you're talking about the Australian regulation how they just issued this new advice. I think it's the same in the UK. The regulators in UK, the government regulators, have sort of said actually here’s our new cloud UK policy, we can go to the cloud if we want under these circumstances. But it's several years after this sort of stuff has been available and there's a lot of people who are sort of, "We can just do so much more." I wonder if one of the things I've been sort of thinking about is what is business continuity mean now?
James Lewis:
Or what does disaster recovery mean if you're cloud native? If I can start an entire new environment, entire new kind of production data center up on demand by pushing a button, what is disaster recovery mean? We don't run active, passive anymore.
Scott Shaw:
I think people talk about resilience a lot more than they talk about disaster [crosstalk 00:00:22:44].
James Lewis:
But that's sort of level of thinking. I'm not sure how much that's permeating through to some of the bigger organizations yet. Where we're, I think we're still, maybe... I don't know if you know this thing about Eli Goldratt and his four questions you should ask when adopting a new technology. So he's got this lovely set of things... you should ask what's the power of the new thing that you're looking to adopt.
James Lewis:
You should ask what limitations do we currently have that this new thing could help us overcome. So things like we can run always on, right? We can be resilient by just being highly available. He then sort of says, "What current rules do we have to manage the existing limitations?" And all of that stuff is built into process and built into deployment processes and risk management and all these kinds of things that we've sort of built up over time because we've had to have them to manage our data centers and deployment processes and all this kind of stuff. And then he sort of says, "But then we forget to ask the final question, which is what new rules do we need?" And this is where we're sort of lagging.
James Lewis:
Is that what the new things do we need to put in place to take advantage of the new technology of the cloud. So you sort of said this, Australian regulators just got to the point of, "Okay, well maybe we can use the cloud now, right." But the new rules really, really lag.
Scott Shaw:
And I think everybody's trying to figure out what that is.
James Lewis:
Yeah, yeah. I see this a lot in big organizations where it's not just the regulators, it's ingrained thinking. It's 20 years of thinking about how we work with a particular set of tools and technologies, our data centers. And then you try and apply the same thinking to the new stuff but-
Mike Mason:
On that note, with those four questions to ask, I'd like to thank our guests here, Scott Shaw and James Lewis. My name's Mike Mason.
Zhamak Dehghani:
And I'm Zhamak Dehghani.
Mike Mason:
And thanks for listening. Please tune into the next one.
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