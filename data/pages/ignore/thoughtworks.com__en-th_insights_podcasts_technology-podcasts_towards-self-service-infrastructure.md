<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/towards-self-service-infrastructure | Title: Towards self-serve infrastructure | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Towards self-serve infrastructure 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Mike Mason | Podcast guest  Evan Bottcher and Zhamak Dehghani
January 13, 2020 | 27 min 21 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/towards-self-service-infrastructure#transcript)
Listen on these platforms
## Brief summary
Traditional, centralized approaches to infrastructure management risk creating organizational friction and bottlenecks for dev teams. By defining a standardized tech stack, you immediately make it harder to satisfy your teams’ diverse needs. Co-hosts Neal Ford and Mike Mason are joined by Evan Bottcher and Zhamak Dehghani to explore how to benefit from self-service options.
**Podcast Transcript**
Neal Ford:
Welcome everyone to the Thoughtworks Technology podcast. I'm one of your regular hosts Neal Ford.
Mike Mason:
and I'm Mike Mason, also one of your regular hosts.
Neal Ford:
And we're joined today by two of our colleagues on the Doppler group within Thoughtworks, which is the group that puts together the Technology Radar.
Evan Bottcher:
I'm Evan Bottcher, I'm from Melbourne, Australia and I'm a principal consultant.
Zhamak Dehghani:
I'm Zhamak Dehghani and I'm from the San Francisco office and I'm a tech principal here.
Neal Ford:
And Zhamak is normally one of our hosts, but today she's a guest so that she gets to talk more because she has strong opinions about this. So one of the things that frequently comes up when we meet face to face to put together the Technology Radar a lot of very interesting conversations that get spawned by of what we call blips on our radar. And this podcast is a good example of a very interesting conversation that spun up and we wanted to capture some of the essence of it as a podcast.
Mike Mason:
Yeah. So this specific discussion that we had in the meeting was around using pull requests somehow to cause infrastructure changes to happen rather than using a ticketing system. But that's not where we're going to start with. This kind of spawned a whole discussion about what we mean by self-serve infrastructure because I think it's a kind of a pillar of platform strategy that we talk about at Thoughtworks.
Mike Mason:
We talk about reducing friction for teams. We talk about self-serve infrastructure, but we wanted to kind of dive in, in a podcast into what we mean by that, why that's important. So maybe you guys could start with talking about some of the traditional challenges that teams face and how self-serve infrastructure, whatever that is might help.
Zhamak Dehghani:
Sure. So I think traditionally operations or infrastructure management has been under often the control of a centralized team. And that centralized team had the best intentions in their hearts that they wanted to provide the quality service or the quality infrastructure to the rest of the developers in the organization while putting guard rails and security and all the quality concerns into that infrastructure.
Zhamak Dehghani:
But organizationally and the process wise, the way it has been organized is that the rest of the organization for their needs would come to the centralized team and they will ask for the pieces of infrastructure that would enable the business value that they're trying to unlock in the application they're trying to build. And they come with their tickets and they're creating, basically contributing to a centralized backlog and they're competing for where on that backlog the work needs to be placed.
Mike Mason:
And when you say infrastructure, you mean like servers and firewalls and bits of... What do you mean?
Zhamak Dehghani:
Yeah, so all of the above, I think you can really apply the same paradigm at different layers of that stack. Even for clients, let's say that they are on the Cloud and they have pieces of that infrastructure already kind of self serve, then managed provided by the Cloud, their compute, their storage. There's still another level of governance or guardrails or ways of using that that gets implemented and controlled often by a centralist team.
Zhamak Dehghani:
So it could vary in range from your compute, your storage, your network, your observability, your monitoring tools, your storage or data pipelining, infrastructure. It's a very diverse range and then you can go up and down that stack in terms of organizational maturity, how much organization has invested to build other higher levels of abstraction on top of it. But I think that centralization has led to a lot of organizational friction that hasn't worked out really well because you've created the centralized bottleneck essentially.
Mike Mason:
So it's a bottleneck in that there's kind of a slow response for teams. Is it that kind of a thing? Like, I know we often talk about governance Kind of in a derogatory way, but you know, you can see why organizations would want to put some controls around infrastructure so it's not the wild West. But is its slowness or inflexibility? Or what's the key problem?
Zhamak Dehghani:
I think, I mean when you centralize control ownership capability into one team, you're immediately has created a high point of friction absolutely in terms of response time. In terms of flexibility as well, because once when you centralize something in one group, that group intend to optimize locally for their efficiency. So what then you would see is this idea of harmonization that they would try to satisfy a very diverse set of needs with one way of doing things. So you don't get that level of like diversity that you would need so that you have very different types of needs and applications.
Zhamak Dehghani:
So imagine like CI/CD pipeline is a good example. Often a centralized team becomes responsible for not only providing your CI/CD agents, but also providing templates for your pipelines. So then local optimization means they're going to provide a typical template of a CI/CD pipeline that might be okay for a typical application, but as soon as you are an anomaly in the organization or you move away from that typical configuration, then that doesn't fit your needs. So I think it's you become rigid, you're not nimble to responding to change and you're also very slow to the needs of the rest of the organization.
Neal Ford:
Looks like devil's advocate for a second. You also get consistency and consolidation and canonical representations of things and single source of updates. So how do you address some of those problems if you move? I mean not, I don't suspect you're advocating here that it becomes the wild West where let a thousand flowers bloom on your infrastructure, right?
Zhamak Dehghani:
Okay, so go ahead.
Evan Bottcher:
In some organizations have gone that way. And so they've allowed for a proliferation of team-managed infrastructure, which has that upside of that fast turnaround time and the ability to tailor the underlying infrastructure to their particular needs in their particular domains, which is great. But as you say, that leads to this excessive proliferation of different technologies. So there's somewhere in between. The cost of the over-centralization and too much constraints without enough self service, are very real.
Evan Bottcher:
It costs you at all levels of your delivery lifecycle from standing up new services and environments and configuring them correctly through to delivering, change in your software and systems and identifying problems and troubleshooting. It's usually a problem of access and availability of tools to be able to resolve incidents quickly. So it's really impact on customers, not just in time to market but also in time to restore service when something goes wrong. So, it is something that you do definitely need to address.
Mike Mason:
And I really want to echo what you said there. It's not just about developers being grumpy because they've got to ask somebody else for stuff. There's real tangible customer negatives to the slowness and them not being able to do a deploy, figure out what's going wrong, look at the logs, all of that stuff has as real negative impacts for the organization.
Evan Bottcher:
Well, Inability to scale too, because ultimately you need to scale. Quite often these platform teams, there's just scaling up the number of teams that are building product, you need to scale up the number of humans that are doing work in the centralized ops or platform team or whatever you've labeled it. In order to service all those teams' needs in a timely manner and always the demand for new environments and new tooling and new very tooling without stripping the capability of a centralized team.
Neal Ford:
I think one of the dysfunctions you see in organizations like that is if you have a centralized team and you view software mostly as overhead then you immediately start cranking down the budget as much as you can on that centralized team, which makes their response time even slower and it makes the problem even worse within the organization. So freeing some of that up to individual teams will help you spread some of that pain around the organization, but you’ll get a much faster response time for individual teams. And it has to do with the attitude about how you use software.
Evan Bottcher:
Well yeah, as you say, the attitude about how you view software and infrastructure and everything. So if you're seeing these sort of operations and platform teams as a cost center as something that you need to manage to take cost out... And certainly consolidating these things is an effort to reduce is an effort to reduce diversity and or variation. Allow for more freedom of people to move around the organization, allow for, have a better cost optimization, but that's not the primary objective. The primary objective is to speed time to market and speed resolution problems that that's where the focus needs to be. A lot of that comes to how we view platforms and infrastructure internally as rather than just servicing demand, but actually as a compelling product.
Evan Bottcher:
And this is a really key bit that we've been talking about for quite a while. We've had some things on the radar in the past around this where we see that the successful organizations that people where they have a clear idea of what their internal platforms are, how they service their internal teams as a product.
Evan Bottcher:
The role of the technical product manager is a really key thing here. Someone who can advocate for a better experience for teams within the organization for reducing friction, for taking away burden, reducing risk and they understand the benefits of using their platform and are able to guide the development of self service and better quality and more reliable platforms. Even if it's those things take away a little bit of choice for the teams around what tools and things they use. They understand that that's going to be a compelling place or compelling a product that the other teams would want to use.
Zhamak Dehghani:
Build upon that. I think that the idea of a product, there are a few things that are kind of in that ward product. One is this experience of the users that they can just pick up the product and use it and in a self-serve way, you know, solve their problems. So that comes with a lot of other other things that have to be put in place. The older guard grills that we talked about, the constraints that we want to put on the infrastructure or on the teams to make sure we are secure and we're not compromising availability. That All can be now abstracted in the implementation of these self-serve infrastructure or self-serve interface to the infrastructure while still giving flexibility to the teams to use the product within those guardrails. So the abstraction of the complexity and abstraction of the guardrails into that layer, the capabilities that we call self-serve.
Zhamak Dehghani:
The other thing is that, that role, Evan mentioned the role of the technical product owner or a platform product owner or infrastructure product owner. That person is an evangelist essentially for the organization to go out and market this as a product to developers to produce great documentation examples of how to use the code so that it can be that those self-serve infrastructure pieces can be discovered easily, can be used easily with good documentations and examples and it doesn't need a lot of handholding yet. And other tickets on the backlog to use the infrastructure pieces.
Zhamak Dehghani:
And the third piece of that is how do we measure success for this piece of infrastructure as a platform? What do we really care about here? And whenever I've built with our teams, any sort of self-serve kind of technical product, one of the key measures that have kind of asked to put in place and kind of measure over time is the lead time to use all of that infrastructure. The decrease lead time to create something valuable on top of that infrastructure. For example, we're building data, ans self-serve data infrastructure right now at a client. So one of the metrics for that self-serve dating frustrater is how long it takes for a data engineer to come and use this self-serve infrastructure to build their first pipeline and get it to production. So lead time to creating these what we call like data products or data pipelines in a way. And I think that's a good starting place to see how effectively you are serving your customers.
Evan Bottcher:
That's an excellent place to start. And quite commonly in talking to organizations that are trying to do this, they look at again... A trap is to start to look at cycle time as your time to make changes to your infrastructure for the platform team itself. But actually that's looking very much internal to the team that can actually look really good. But actually the level of service you're providing to the organization can be quite poor and you really need to start the clock on cycle time when the tenant, the consumer of the platform and delivery team and product team in your organization says, "I want to provision a new piece of infrastructure. I need to make a change or I need to be onboard." That's when the clock starts and that's really important to measure.
Evan Bottcher:
Another interesting measure is to look at the level of manual effort that the team's doing. Just in general terms, we talk about automation, but automation isn't like binary. You have to have absolutely everything self-service. Otherwise we would just pass through every product in the cloud catalog and let every team use every product in AWS or GCP or Zero, whatever the cloud provider is. And we would have this proliferation. We wouldn't have the value add. The automation, if your platform team is doing manual work, you need to be looking at that work suspiciously to look at that and understand what categories of work that is, how much of it is failure demands?
Evan Bottcher:
Something that you should have had an automated or self-serve way of doing and how much of it was value add as in supporting another team performing something that's kind of in that, "Okay now and then we'll need to do this type of work." And the traditional way was I'm measured an incentivized based on the number of tickets, the number of inbound requests that I can serve as an intern. Actually we need to look at how many tickets we didn't have to service. And that's, I think what the technical product manager will do is, is to look at what's missing in our product catalog. What's missing in our offering that's causing all of this extra work for us to do.
Mike Mason:
How do you feel about consuming teams choices in the platforms they use? Because a lot of the time we talk about, if this was a product, you would be competing in the marketplace with other products. But developers within an organization, they often have a mandate got to go use this thing. And there's a lot of some cost problems where some part of an organization says we're going to go build this super valuable thing, but then they just force people to use it and they don't really kind of compete for those customers of that internal product. Do you think it's acceptable to mandate stuff... Because I mean if you're not mandating use of your fancy new self-serve infrastructure, then we're back in the wild West. If teams can just choose whatever they want to... What they're going to use.
Zhamak Dehghani:
It's a wonderful question I have two thoughts on that and maybe I'm a little bit idealistic, but if you go right now to the market and you want to buy a product, does the product creator come and mandate to use their watch or to wear their shoes? It's kind of your choice and at the end of the day it's the quality of the service or the quality of the product and how it fits your needs would help you make a decision hopefully. And I think it should be the same for technical products within the organization as well. And it should be if the technical infrastructure built in a way that it really removes a whole heap of overhead that I have to go through hoops to create and it would really make using easier and more convenient than building it myself, then hopefully that's a good reason for me to use that product.
Zhamak Dehghani:
So even if we don't have diversity of the offerings of infrastructure, self-serve infrastructure and we just have one, it should be the evangelism and the success stories... The first use case is really important to show the success of that product to kind of virally, that product stopped being used. So hopefully that's like one side of it, and maybe it's a bit too idealistic, but I hope that instead of forcing, we can create gravity and create pool for other folks to come and use it by really showing and demonstrating the benefits. The other side, I actually think it would be wonderful to have diversity of the offerings of infrastructure as code and not have a monopoly of all of the infrastructure is in within one team.
Zhamak Dehghani:
But what would happen is often when you get started, you have no choice but to start somewhere, right? Start with the 80% population that you need to serve rather than that 20% like really different population than you need to serve. So like any product owner you would do a market fit analysis and find out what fits the majority of the market that you have, which in this case like developers that want to build applications or data pipelines and whatever it is that you're trying to solve the market population that you're trying to serve and, and build for that first.
Zhamak Dehghani:
And that means yes, that the rest of the organization will be in the wide wild West and they will be doing their own thing and they may not have the best experience building it but we have to get started somewhere and I think it's a problem if we think that where we bootstrapped building any infrastructure and how it looks like at the bootstrapping time, it's exactly the same model of operation three years down the track. This would evolve over time.
Neal Ford:
Toward the end, how difficult is it to get this started? What challenges do you find getting this in place within the organization?
Evan Bottcher:
One of the common things that I observed is that we've tried to take what was a data center-based centralized operations team and just translate one for one into modern technology. What we used to be virtualization, now it's cloud and so traditional ticketing, ticketing systems, provisioning, needing a project code for provisioning a tiny piece of infrastructure essentially not looking at the capabilities of the underlying cloud provider, but really just thinking about this as a data center shift into the cloud.
Evan Bottcher:
Another really common place is another really common challenge is where people have decided to go and build the platform in isolation of use. And so, we're going to spend three months going to stand up our self service portal and... I've come along and seen what's happened and there's a webpage where you click at five times and hit the checkout because I'm purchasing or provisioning some cloud-based compute and the teams have built a web-based checkout system that I can't automate.
Evan Bottcher:
One of the values of the Cloud is to be able to integrate an automateable provisioning, kind of scriptable environments and infrastructure as code into my deployment lifecycle in mind, my development life cycle. And so that's completely detached. That has been built completely detached from how I actually work as a consumer of the platform. So I always recommend that building the platform in isolation of customers is going to lead you in a bad place. So find a consumer who needs the service, build it in-situ, allow the people to use the platform capabilities and then harvest those from for the next consumer seems to be a much better strategy.
Zhamak Dehghani:
Plus one to everything Evan said, it's just so spot on this bottom-up approach to building platforms in isolation is just a recipe for failure. But also it's an art as well because if you think about using these usage patterns or use cases or the teams that need to build a platform as a vehicle to execute building the platform, you need to be careful to not over-fit the implementation of that platform to one use case to one team. So maybe it's one team, maybe it's one or two or three teams that have a slightly common cluster of capabilities that they need. But there are slightly different, so you build a platform with through use cases, with collaboration with your consumers. You have the luxury in the organization to be able to work with your consumers but also not over fit to their needs and not overcommit to features that are not needed.
Zhamak Dehghani:
And again, bring that product thinking to building it. I think going back to where we started Mike with, is ability to do a pull request on a piece of infrastructure configuration by the consumer team is a good self-serve function when you get started. So thinking about that minimum viable, I don't know, I experience for the developers to experience self-serve to a degree, it may not be a fancy website to go and click, which is kind of useless and it's more lower level, but they still have a sense of autonomy and a sense of contribution to what change they need and maybe that's a good place to get started. So not over committing to what should this platform experience look like, what is the acceptable experience when you get started and then build and evolve it from there.
Evan Bottcher:
So to expand on that a little bit, which was the original discussion in the radar sessions this week, investing in automation and self service and APIs and tooling is expensive where you're trying to build a compelling offering on top of whatever underlying cloud provider or provide what are the constraints or added value? So we have seen this a number of times at some very frequently used things become something that is completely automated and self service. But it's actually quite reasonable to have a middle ground of certain types of cloud platform provisioning. Examples I've seen are around data pipelines on a centralized compute costas or actually core infrastructure networking and things like that that you change infrequently that the platform team provides a repository that's connected up to a fully automated build and deploy pipeline.
Evan Bottcher:
But the teams who make use of the platform contribute by making code changes in a brunch and then making a pull request which is reviewed by the platform team and merged into master and then the automation takes over and deploys whatever changes. So it's balancing this appropriate investment in platform automation and self service for the frequency of the change that's required. Something you do once every six months, maybe you don't need an API upfront for that and you wait until you observe all the different types of manual effort that the centralized platform team needs to do and focus the investment in automation on those things.
Neal Ford:
But it strikes me as a good way to evolve capabilities too. If you allow teams that need a new capability to deliver that to the centralized platform through a pull request and it becomes available to other teams over time. And so that's a kind of an odd demand way of evolving capabilities from a centralized store.
Zhamak Dehghani:
Yeah, absolutely. I think we talk about harvesting quite a lot as opposed to building up front. But to be able to even harvest people, you what people are building, you need to give some sort of a framework for that harvest to be contributed back to the shared infrastructure and pull requests are a good place to start.
Neal Ford:
Well, we could definitely talk about this subject for quite a while, but the reason we're in San Francisco is to actually build a radar and we have to go do that now. So we want to thank Zhamak and Evan for their great contributions this morning.
Mike Mason:
Yeah, thanks very much. Thanks for listening.
Neal Ford:
We'll see you next time.
Zhamak Dehghani:
Thank you.
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