<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/multicloud-exploring-the-challenges-and-opportunities | Title: Multicloud: Exploring the challenges and opportunities | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Multicloud: Exploring the challenges and opportunities 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Prem Chandrasekaran | Podcast guest  Rashmi Tambe and Sunit Parekh
June 01, 2023 | 37 min 46 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/multicloud-exploring-the-challenges-and-opportunities#Transcript)
Listen on these platforms
## Brief summary
When cloud first hit the mainstream more than a decade ago, its attraction was rooted, in part, in its apparent elegance and simplicity. As it has become an established norm in the industry, such simplicity has given way to more fragmentation and complexity. The growth of "multi-cloud" and adjacent terms such as "hybrid cloud" and "poly cloud" mean that cloud is a field that needs to be sensitively navigated by technology leaders and their organizations. 
In this episode of the Technology Podcast, hosts Neal Ford and Prem Chandrasekaran discuss multi-cloud with Thoughtworks colleagues Rashmi Tambe and Sunit Parekh, who co-lead the Enterprise Modernization, Platforms and Cloud service line. In the episode they discuss terminology, the challenges of migrating to multiple cloud platforms, governance issues and some common antipatterns. They also offer advice for teams considering exploring the potential of multi-cloud.
#### Full transcript
**Neal Ford** : Hello, everyone, and welcome to the Thoughtworks Technology Podcast. I'm one of your regular hosts and I'm joined today by another of our regular hosts, Prem.
**Prem Chandrasekaran** : Hello, Neal. Thank you for the introduction. I play the role of Head of Tech on our West market, and I'm also one of the regular hosts on this podcast. Over to you.
**Neal** : We are talking today about a burgeoning topic about strategy patterns from multi-cloud deployments. We have two of our colleagues here and I'll let them introduce themselves.
**Rashmi Tambe** : Hey, everyone. Good morning. Good evening to everyone. My name is Rashmi Tambe. I'm based in India. I lead this service line called EMPC which focuses on enterprise modernization platforms and cloud. Very happy to be here. Thanks for hosting us. Over to you, Sunit.
**Sunit Parekh** : Thank you Neal and Prem for hosting us here. I pair with Rashmi leading the enterprise modernization digital platforms and cloud service lines in India and service offerings that we offer to our customers. Happy to talk more on multi-cloud along with everyone. Thank you.
**Prem** : Wonderful. I'll get us kicked off, Neal, like you said. The first question, multi-cloud is an oft-used term. Can you tell us what exactly multi-cloud actually means by defining it?
**Sunit** : Sure. Multi-cloud is used in many different quotations you might hear. Multi-cloud refers to the practice of using multiple cloud service providers, both public and private for your compute storage cloud-native services. Many enterprises choose multi-cloud for leveraging best-of-breed services, avoid one-vendor lock-in and address business continuity and scalability of their applications. In short, multi-clouds are when you are using multiple service providers.
There are many flavors to multi-cloud. A lot of people call it multi-cloud or hybrid cloud when they're using on-prem. One of the cloud service providers they call and use it as a poly cloud when they're using two different cloud service providers for different use cases. They're using it in a portable cloud mode also, or the distributed cloud as well.
**Prem** : Wonderful. Thank you.
**Neal** : You mentioned some of the different deployment models there and some of the different names. Can you differentiate some of the different deployment models there between hybrid and poly and portable versus distributed, when we talk about multi-cloud?
**Rashmi** : Sure. Usually, the journey to cloud starts with mono-cloud or it's sometimes also called uni-cloudcloud. When an organization chooses a public cloud provider to start the cloud journey, usually the journey starts with lift-and-shift or rehost of certain applications. Then comes hybrid cloud. We've seen this with banks mainly wherein the customer-facing applications are deployed on public cloud but the backend systems and legacy systems or the mainframes are still on on-premise or the data center. This is a classic hybrid cloud setup.
It then starts becoming complex with a little bit of maturity when an organization starts looking at more than one public cloud provider. The choice usually is on using best-of-breed services from the cloud providers. You're making use, for example, we've seen certain patterns like using AWS and Azure for container workloads, but maybe explore GCP for data and machine learning workloads. That's when you are making best-of-the-breed services, you're leveraging best-of-the-breed services. That's when it becomes a poly-cloud deployment model.
Portable cloud, as the name suggests, it's a choice for an application to be deployed on either of the clouds or many clouds, which makes it-- fundamentally, the application architecture has to be cloud-agnostic for an application to be run on any cloud provider whenever needed. Usually, this happens in an active-actice, active-passive kind of a mode across multiple clouds.
Last but not least, for larger organizations who have grown either organically or inorganically, they have workloads running on diverse environments. You have your on-prem environments, multiple cloud providers, you have edge workloads. All of this getting managed centrally from one public cloud provider is usually a distributed cloud setup. This usually applies with, for example, telecom companies, large companies across geographies' workloads. That's when distributed cloud becomes very, very common.
**Prem** : Wonderful. Thank you.
**Neal** : Is it inevitable once a company reaches a certain size that they're going to end up on multiple cloud providers? Because it seems like every large client we have at some point comes up with one of the several reasons you posted for we need to be on multi-cloud.
**Sunit** : Yes, true. There are many reasons that we have seen in the industry that people adopt multi-cloud. First and foremost is best-of-the-breed. Based on the use case and the problem they want to solve, they decide to choose and go to certain cloud service providers. Sometimes based on the regulatory compliance requirement of the local government or local data laws, they need to choose different cloud service providers as well for business continuity as well. There are reasons that companies don't want to get vendor lock-in, and that's why they choose cloud-agnostic architecture and deploy to another service provider for compatibilitiness. There are plenty of reasons.
There are some geopolitical reasons as well where certain cloud service providers are not available in certain country or region, and because of that, they have to go towards the other cloud service providers. Yes, true, multi-cloud for the large enterprises which are global businesses end up in multiple cloud service providers for sure.
**Rashmi** : Just to add to Sunit's point, another reason is the, in general, inorganic growth of organizations when they keep on acquiring newer companies which are on different cloud providers. The multi-cloud becomes an inevitability because you have multiple companies in your portfolio on different cloud providers, which would mean that you are now on a multi-cloud environment.
**Prem** : Great. Multi-cloud challenge seems like a lot of work. What are some challenges that you see when organizations are looking to adopt a multi-cloud strategy rather than sticking to just one single cloud?
**Rashmi** : Some of the prominent challenges are the cross-platform or cross-cloud infrastructure automation and having uniformity in it. For example, if you're using let's say AWS cloud formation with AWS, and if you're using Google Deployment Manager with GCP and now you have simple policy, for example, a dev machine cannot exceed a certain size, If you are using these disparate automation tools, you are going to write the same policy for two different cloud providers. I'm giving a very, very simple example here.
Usually in an enterprise setup, as all of us are aware, the compliance policies, the security policies, they are very, very complex and you will end up doing it across cloud providers. Generally, we give advice of using something like Terraform, which brings a little bit of a uniformity when you are doing infrastructure automation.
The other challenge is-- as we started the podcast, we said multi-cloud is a pretty cliché or often-used word, and when people say multi-cloud, they're usually talking about application portability. If you think from the first principles angle, sometimes we think that people are not thinking about do they really need portability? What business problems are they solving by making an application portable and investing into cloud-agnostic architecture, which is time-consuming? Why do you need portability? Sometimes people should ask the questions, do they need portability? If yes, then what sort of architecture patterns are you going to apply to achieve that eventual portability?
**Neal** : That brings up an interesting question that I'm sure you get a lot in this space is, "I want to be agnostic across all cloud providers because it would be strategic for me as a company to be able to support any cloud provider I want to." What's the fallacy at the heart of that strategy from a company?
**Rashmi** : If you have decided to go on cloud, why not make most use of the underlying cloud platform? If cloud transformation is part of your growth and scale and revenue growth, why not make most use of that? If you're saying that you need to be agnostic across cloud providers, I think it again goes back to the original question. Being cloud-agnostic would mean making use of services or self-managing most of the services. For example, you would not use managed communities, you would manage your own communities yourself. You would not make use of managed databases, you probably want to manage your own databases.
All of these architecture decisions are costly, time-consuming, and yes, you can take those decisions, but we give certain guidelines what type of workload should be chosen for a complete cloud-agnostic architecture because then you are looking at, for example, you're looking at business continuity, you're looking at very high SLA for a consumer-facing application where you are looking at active-active, active-passive across cloud providers, then yes, you should do cloud-agnostic.
In general, a very blanket statement that, "Hey, we want to be cloud-agnostic at a company level," I think people should do a double-click and what actually it means in terms of architecture efforts and timeline and budget as well. I think that's how some of these questions should be tackled.
**Neal** : My analogy for this, I think you're exactly right, is that-- there were the two models that the industry followed. One was the SQL relational database, and the other was J2EE application servers. There is a standard for SQL, an ANSI standard, but it's so weak that it's useless without every vendor adding their own proprietary behaviors. Therefore, you get locked into a particular database vendor forever and they make a lot of money on those things.
The counter to that was J2EE, where there's tremendous pressure in the community that we want a J2EE standard. As soon as they inked that standard, the value of application servers plummeted to zero because open-source came along and completely ate them.
As much as we would love for cloud providers to provide some sort of generic API, they will never do that because they want your subscription money. They need the cash flow, and so they're going to actively make sure that you can't effectively create one thing that talks to every cloud provider because it's in their best interest, as you said, to provide unique services to entice you to use more and more of their cloud and less and less of their competitors' because there's a huge arms race going on there.
I think it's a misnomer to think that there's ever going to be some standard cloud API that works across all clouds because it's very much not in their interest to do that.
**Sunit** : Yes, and that's very true. That's why when we have to look at all different types of workloads that exist in our ecosystem, we need to classify them. If they have a very business criticality and we are into the cloud-specialized architecture, then we are in a risk zone, that we are dependent on the cloud service provider heavily. In the case of our application, which is not very business-critical, and if you're building it in a cloud-agnostic way and not leveraging cloud, we are into a very expensive zone where we are putting a lot of money to build agnostic, whereas the value is not that much.
Our analogy is that, just be careful about these two zones when you are choosing your application architecture, which is leveraging cloud services.
**Prem** : Wonderful. Look, moving to one-cloud or migrating to one-cloud seems complex enough and now you're talking migrating to multiple clouds. This seems like you're saying you need to be really, really tall metaphorically to be able to pull this off. What are some common failures, mistakes that organizations make when they're trying to move to a multi-cloud strategy?
**Sunit** : The first thing that we talk about whenever we are adopting multiple cloud service provider, at our organization level, we should have a very clear business objective defined, why we are going with this multi-cloud. We don't want to be just fancy or just for the sake of trying out something. It's very important that what business value we are going to get, what business problem we are trying to solve by going to the multi-cloud services.
Second that I would say is leverage the automation infrastructure as whole while going to multiple cloud service providers. Continue to do that. Make your choices which are agnostic to cloud service provider, choosing tools like Terraform for infra-provisioning, HashiCorp vault for security purposes, Open Policy Agent for policy rollout, and have those strategic thinking in place before you start your journey there. These are the common couple of mistakes that people make while just starting with the journey on multi-cloud in ad hoc way.
**Prem** : On a related note, let's talk about trade-offs. Now, you mentioned a bunch of mistakes that organizations can make. What should organizations be cognizant of in terms of trade-offs and choices when they are looking to adopt multi-cloud?
**Rashmi** : First and foremost is when you are looking at multi-cloud, you should assess your team's capability to do multi-cloud. I'll go back to my earlier example. If you're thinking of doing machine learning in GCP, because originally GCP started as, "Hey, we can do data workloads really well." If you are following that fancy and say that, "I want to use GCP for my data workloads, for building my data, for doing machine learning modeling there," I think, fundamentally, you should look at whether you have capability in your team.
When you made that choice, do you have the capability to support that? If you do not have the capability, do you have plans for uplifting your teams to come to that level where you can do data lakes on GCP. If not, are you outsourcing? Are you hiring? That has to be thought about.
The second, when you make these choices for example, another choice that I'll talk about is, although Sunit talked earlier, your business-critical application, are you making a choice of making this available in a active-active or active-passive or in a disaster recovery manner? Are you making a choice of doing this on multiple clouds? Can it be done on different AZs? In the same cloud provider if your active-active can be on two different AZs, then why are you looking at a multi-cloud-based active-active DR strategy for your organization? These are some of the hard questions.
Just because you have another cloud does not mean to set up a DR set up on another cloud. You could do it in the same cloud on a different AZ. That's also possible.
These are some of the questions that should be asked when you make those choices.
Another trade-off or another thing that I can think of is the whole cost factor. See, nowadays cloud as a cost-optimizer driver, that shine is lost. Cloud is no longer a cost-optimizer or cost-saver for an organization. You are going to spend money in cloud. If you're going to spend money in one cloud, obviously, when you're looking at two clouds, then you are going to spend even more money in two clouds. If you have not thought about a very good way of doing cost management, then that's also big problem if you're making choices of these across a cloud or choices of your application.
**Sunit** : I want to add couple of more trade-offs that we have seen. The first one is defining the clear guidelines for application or workload deployments. If you have two-cloud service provider as a choice, we need to have clear guidelines defined which kind of workload we want to deploy in which cloud service provider and what are the benefits of that. Now, these guidelines once published, it's very clear path to production for every application or workload that they are building and trying to deploy.
Second that I would like to talk about is the operating model. When you are working with single-cloud, you have your single-cloud operating model defined very well, working fine, but when you are moving to multiple-cloud service provider, now, are you going to have two choices of tools for doing the same thing across cloud service provider? We need to make sure that we have to make now choice and trade-off. Should we have two different tools or should we think of a unified way of solving that problem?
Now, one classical problem that we have seen is the observability. When you have two-cloud service provider, your applications are deployed across. Sometimes you want to correlate the observability data, but they are in two different observability tools. Now, it's very tricky to correlate data manually or to say look at two screens and all, so make a choice; investment in unified tool, or have one setup where data is published. Tools like Datadog, New Relic, many tools are there in the market which can give you this capability.
Even observability data from on-prem can be pushed to these tools, and you can have correlation across on-prem and multiple cloud service provider. I would suggest two main things again, have unified operating model, have trade-off and choices there, and second, have a clear workload deployment policy defined for your organization.
**Neal** : I think what you're getting at there is intent. I see a lot of organizations just letting their cloud strategy grow like a weed rather than building a garden out of it, and then you get into big trouble. It's amazing how fast you get into big trouble with ad hoc deployments and 16 different ways to do stuff. I want to touch on something that both of you mentioned in that answer, which is, first of all, cost. A lot of organizations still seem to think that it's cheaper to move the cloud and it almost never is. It's strategic and there are reasons to do that but cost savings is not one of them in almost any case.
You were mentioning observability. I want to raise that up one level and talk about the reason you use observability, which is governance, that now you're moving your operations to someone else. Now, how do you govern that if you don't own it anymore? That seems like a big topic area and multi-cloud strategy.
**Sunit** : Yes, very true. Again, we see that similar analogy that we have applied in our cloud adoption and cloud journey for a single cloud, we have to amplify it for the multi-cloud. That's trickier whenever we are dealing with the multi-cloud. We apply five lenses to our cloud governance. First is the cloud cost management. Now, if you are dealing with cloud, cost management is going to bite you heavily if you're dealing with multiple cloud.
Second, how you are going to manage your access across different tools, different applications, across cloud. You have to get your identity and access management right, and govern that very well. We have to apply our compliance policies and securities uniformly across the cloud and we need to have a good governance there. That is your third lens of governance. Fourth lens is to have better resource provisioning and deployment. If you are doing different ways of provisioning resource across two cloud providers, we are going to end up in chaos there again.
The fifth one is around data. Who has access to what kind of data including observability, logs. Access is important here. Apply your governance across these five lenses following three key principles. First, make all the governance-related information visible on dashboard and have metrics around that. Once you have visibility and dashboard built, it is easy to put automated governance with fitness functions alerts on top of that.
Third stage is to shift left this governance earlier in your software development lifecycle. You can monitor them early rather than very late in the game. Apply five lenses and three guiding principles to approach your governance.
**Prem** : It sounds like you're suggesting that there needs to be this abstraction layer or an experience layer between the organization and these cloud providers. Did I get that wrong or are you suggesting something else?
**Sunit** : True, and that's what we have to build as a common frictionless experience for our development teams so that when they want to deploy their application, they have one common tool or abstraction which can be leveraged to provision infrastructure or monitor their applications or govern their infrastructure.
**Rashmi** : Just to add to that, Prem. When you say a common infrastructure, I think it can be easily seen as we are throwing yet another tech to solve the problems created by tech, so two cloud providers coming together, creating problem, and then we are throwing more tech to solve that problem.
**Neal** : That's job security, right?
**Rashmi** : Yes, true. There are two schools of thinking here. I think nowadays with multi-cloud, at least I'm hearing a lot of chatter around something called a super cloud or meta cloud which is this abstraction layer which sits on top of these clouds and gives you a unified way of all the things that Sunit talked about. One school of thought is the same that I said, you're throwing tech to solve the problems that tech has created.
The other school of thought is also that if you do not do this, eventually, you will still have to. For example, simple cost management. You are going to look at CloudWatch logs and you are also going to look at some other cloud providers' logs, and you're going to compare, which means that you're going to spend manual hours to do that. The best way to handle is to have that layer which provides you a single pane of glass to do both the things. At the end of the day, yes, it's a tech to solve tech.
**Neal** : It sounds like we've been doing this enough now that you've started building some ideas of patterns and anti-patterns around the strategies. You've got some principles and some of the things laid out. A pattern is not a best practice, a pattern, in this specific scenario, this is a good solution to this problem. Can you talk a little bit about some of the emerging patterns that you've seen in this space? You've already been touching on a lot of those, but also anytime there are patterns, there are also anti-patterns. Do you see any of those commonly starting to pop up in particular contexts?
**Sunit** : I see couple of anti-patterns when adopting multi-cloud. One is looking at multiple cloud service provider without having the application deployment metrics. People go with one business unit using AWS, one business unit using GCP within the organization, rather than choosing one cloud service provider for one purpose, leveraging it with the maximum potential, and having that consistency across the organization. This is one anti-pattern that I've seen.
Second anti-pattern is proliferation of tooling. When they go with multiple cloud service provider, people start leveraging tools across whatever they like, whatever they have come across, rather than taking a step back, looking at what we are using, can we leverage the same tool for the other cloud service provider also, or not, and then making a choice there. As we talked about having the operating model defined for multi-cloud as well, rather than jumping the gun, "Oh, when we are in GCP, let's use GCP way of deploying applications. When we are in AWS, let's do AWS pipeline." Now, these are the two anti-patterns that I've seen mostly.
**Rashmi** : Some of the patterns that are coming up is being able to manage, for example, if you have containerized workloads across diverse environments, how do you manage them uniformly? How do you apply policies uniformly? We're seeing, for example, Google Anthos talks a lot about being able to manage your workloads irrespective of whether they're running on-premise, whether they're running on other cloud providers, whether they're running on Edge.
There is increased chatter around how do you manage your container workloads across cloud providers using some of these tools. There's also Rancher, there is Kublr. I think IBM Satellite also claims to do cross-cloud management. That could be one emerging pattern.
The other thing which we already touched upon briefly, the portability part, we've seen certain customers. They would come and approach us and say, "Hey, why don't you tell us how to do multi-cloud?" In the first discussion, and these are the customers were on-premise, they would tell you that, "Hey, I want to make my application portable between AWS and Azure, or Azure and GCP." One of the things we tell them that, "Hey, you've not even started your cloud journey. Thinking about application portability is probably a third, fourth, fifth step for you."
You first need to start about how and why you are starting your cloud journey, what sort of problems you're solving, if you're looking at two cloud providers, why you are doing that, then comes application portability. Call it pattern or anti-pattern, I think there is a lot of, again, throwing tech to problems kind of a mentality which does not really solve your business problem.
Just because your contemporaries or some leader or the software in the industry is talking about multi-cloud, people just get fascinated and they are like, "Hey, I want to make my applications portable." This is also one of the things we advise our clients that, "Hey, let's take a step-by-step journey. Let's not directly jump there."
When you have applications deployed across clouds and when these applications need to talk to each other, for example, either in a on-demand fashion or sometimes in batch mode, there's a need for new data movement when your databases are talking to each other, your maybe Kafka messages, messaging architecture is talking to each other. Many times these kind of architectures become overly complex. I would like to take an example to explain this better.
Let's say you have a taxi aggregator company, you use that in Singapore, the user goes to US, the user's data from the Singapore shard needs to be copied to a shard on US, many a times, if you are not doing these proper sharding techniques at a database level, you will see a lot of latency in data copying. You may not see your loyalty point when you move around, or there is a lag in the notification. Eventually, there will be a consistency, but there will be the latency.
At an architecture level, you will have to be flexible and you'll have to define what are those matrices that I'm going to track very closely and what are those numbers. For example, it's okay if you have a latency of few minutes. If you're going to live with that kind of a number, then your architecture can become a little bit less complex. Sometimes this over-prioritization of, "Hey, I need to have everything in sync," et cetera, that can make your multi-cloud architecture extremely complex especially when you have multiple applications sharing data with each other.
**Neal** : Another question. These cloud providers are constantly changing and adding new capabilities. I know they try to maintain backwards compatibility but sometimes fundamental shifts happen. A common mistake I see a lot of architects make is they think that once they've got an architecture solved, it's like solving an equation, they can just drop the whiteboard marker and walk away, but software is a constantly changing and evolving thing.
How do you avoid, if using multi-cloud providers, the constant churn of the API for this cloud provider has changed and now this one's changed, so it becomes a game of whack-a-mole? Is there any way to try to avoid some of the impacts of the rapid evolution of the cloud providers?
**Sunit** : In today's world, there are tools which can help solve many of these problems. We talked about Terraform where the actual service provider driver takes care of most of these internal things of service interacting with the AWS or GCP, and we are dealing with the DSL part of it which helps us to abstract out that API-level coding and work on the DSL.
Same way if we take example of policy, if you want to roll out a security or a compliance policy using tools like open policy agent which uses Rego as a language to define a policy. Now we have to go and apply this policy into AWS and GCP, and the underlying tool takes care of that interactions. Choosing some tools which takes abstracts out this information and doesn't let you directly interact on the API is one way to solve these problems of ever-evolving upgradation of the cloud service providers.
**Prem** : Any closing thoughts that you want to discuss? Anything that we might have missed asking that you really, really wanted to answer before we call this a wrap?
**Rashmi** : One of the key message or key takeaways that we've been advising clients, and this might sound a little rude also in terms of do it only if you need it. For example, if you do not need multi-cloud policy, if you do not need that portability, if you do not need to add those complexities, and if your teams are doing just fine with one cloud provider, why not continue with that?
If you are a smaller company, a smaller startup, you almost should never look at multi-cloud. There's no reason. Your focus should be go deep down with one cloud provider because your business or your revenue or your growth depends on how quick you are going to do product launches to the market. The time to market is important for you and not get trapped into, "Should I use this? Should I use both?" That's not needed.
One of the key message that we tell clients is, do it only if you need it because it adds complexity, it adds cost. You are going to need capability, you're going to need cloud SMEs to handle issues that are going to eventually occur, so this has to be a very thought-through decision. That's one of the key things that I would like to talk about. Sunit, you want to go next?
**Sunit** : Just do it only if needed, but eventually, you are going to need it. I will say that, if you end up into that situation, then have a structured approach and take a step back, create your proper strategy of adopting multi-cloud. Start as a first step of evaluating your workloads. Don't rush. What kind of workloads you want to put in which cloud service provider, why, what are the benefits? Understand all the problems there.
Second, create unified operating model to manage multiple cloud service providers and have a automated governing structure for your cloud environments. That's our advice to everyone. Have a structure approach when you take up multi-cloud.
**Neal** : Fantastic. Thanks so much for joining us today and giving us your insight that you've been gathering working with clients on their multi-cloud strategy. It's great to hear it. Continue building more context and patterns around this.
**Sunit** : Thank you.
**Rashmi** : Thank you.
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
## Find out what's happening at the frontiers of tech
[ Explore Tech Radar ](https://www.thoughtworks.com/en-th/radar)