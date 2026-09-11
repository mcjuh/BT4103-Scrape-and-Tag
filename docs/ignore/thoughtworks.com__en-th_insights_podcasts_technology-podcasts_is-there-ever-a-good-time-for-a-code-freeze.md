<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/is-there-ever-a-good-time-for-a-code-freeze | Title: Is there ever a good time for a code freeze? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Is there ever a good time for a code freeze? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Neal Ford and Mike Mason | Podcast guest  Cassie Shum and Ian Cartwright
March 10, 2022 | 25:14 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/is-there-ever-a-good-time-for-a-code-freeze#transcript)
Listen on these platforms
## Brief summary
Many organizations regard code freezes as a way of reducing the risk of downtime during periods of peak demands. But associating outages with changes often masks a wider lack of faith in the deployment process — which is potentially where your focus should be. Here, our podcasters explore the negative impacts of code freezes and also the instances where code freezes can be beneficial.
### Full transcript
**Neal Ford** : Welcome, everyone to The Thoughtworks Technology Podcast. I'm one of your regular hosts, Neal Ford. I'm joined today by another of our regular hosts.
**Mike Mason** : Yes, this is Mike Mason. This is very exciting because we're actually in person in New York office, one of the first in-person meetings that we're doing this year, where we put together the Radar. As part of the Thoughtworks Technology Radar discussions, we often have some pretty interesting things to talk about that sometimes make it into podcasts.
That's what we're going to be doing today. Neal and I are joined by Cassie Shum. Hi, Cassie.
**Cassie Shum** : Hello.
**Mike** : We're also joined by Ian Cartwright, all the way from Hamburg. Hi, Ian. How are you doing?
**Ian Cartwright** : Hi, there.
**Neal** : One of the things you may have heard us talk about before in this podcast is the category of things that were too complex to blip on our Radar. We're here putting together our radar, and a topic that arose a lot of passion that ultimately alas, fell to the too complex to blip category, is the topic of code freezes considered harmful. That's what Ian and Cassie are here to talk about. Let's start by describing what the bad thing is. What is a code freeze?
**Cassie** : A code freeze is essentially either a team or organization mandated freeze on all commits from developers and engineers to the codebase. This usually, as I've seen it lasts for potentially many weeks up to even up to a month or two. This is usually done because there is fear that any code that goes into the codebase, at this time would actually break something major in production. This is normally done before a big event like a Black Friday for e-commerce or a big banking transaction day where it would be very detrimental to the organization if anything bad happened in production on those certain days.
**Neal** : Everyone knows that when you have a whole bunch of bits, and you get them all arranged that you should let them settle for a few days to make sure they all align correctly. Is that where the reason for this comes from?
**Cassie** : Yes, I think a big reasoning, as well as the QA cycle as well, is usually quite long, and that is the time where a lot of both automated and manual QA happens to ensure that when we hit those important days that there's a steady situation on that day.
**Neal** : Ian, why is this a bad idea?
**Ian** : I think, I guess we can come on to it. I think there are legitimate reasons why you would want to do a code freeze, but in general, is a bad idea, because what happens is two things. One is, everybody knows that data is coming. The business stakeholders know, the developers know, the QAs know. You get this mad rush, where business people say, "I really need that feature in because if I don't get it in now, it's going to be January." Everybody's rushing and trying to get that last-minute piece of work in. They make compromises and they rush to do it.
Ironically, through trying to de-risk the changes, we end up throwing more changes at it and doing everything in a rush, which in itself ends up creating problems. That's one reason it's a bad idea. I think the other is that it betrays a lack of confidence in the deployment processes. Instead of fixing that, we just say, let's just try not to do deployments when we think it will be a risky period for our business. The root cause is we don't trust our own deployment processes.
**Mike** : I think a lot of organizations have organizational PTSD about some previous event where something went spectacularly wrong, and somebody, usually high up says, "What the heck happened? How do we make sure that never happens again?" Somehow code freezes before there's the solution?
**Ian** : Yes, absolutely. I can think of lots of clients where I've worked where they have code freezes where there's some traumatic event in the past, where the worst day of the worst month, they've had an outage and the business has lost a significant amount of revenue, and so the reaction if you like, is to fix the symptom. The symptom was we had an outage on that day, due to a deployment so therefore, don't do deployments.
**Neal** : Many years ago, I actually named that antipattern as the frozen cave person antipattern. It's almost like this horrible thing happened to somebody and they were flash-frozen and then awakened last week and that's the thing that they always bring up in every meeting but what happens if this happens again? It seems like a common antipattern in a lot of organizations.
**Cassie** : One thing to add as well is I think it also creates a very blame-centered culture. Because of some of these traumatic events, I also remember in some of my clients that it was the QA department that messed up or missed that actual bug that went in and ruined everything or it is this team or this particular feature team that payments is a good example where a lot of really important business logic goes into. This blame culture also propagates as well alongside the trauma and so with that fear just escalates into don't do anything and then that'll be the safest way to go about it.
**Neal** : I think that also helps prevent pushback because if you end up being the unlucky department that gets an ad for something like that, then you're very gun-shy in the future because we don't want it to happen to us again, because then they're going to take us out and lynch us or something. That creates an even more fear of responsibility, which we know is the opposite of effectiveness you create that culture.
**Mike** : I think some of it's not exactly justified, but you can understand where people get to. I feel like a lot of software systems have something I'd call implicit testing in them. If something's been sitting in production and running for a while and nobody's complaining about it, then even if you don't actually have automated testing or a formal QA process for that thing. The fact that it's been sitting there mostly okay, must mean it's mostly okay. If you don't have a good testing process, as soon as you change a single line of code in that thing that was previously okay, you lose all that implicit testing. Not that's a good strategy, but you can see why people fall into that.
**Ian** : I think related to that and I think many people have made this observation, so there's nothing new but what often happens is where you have a separate deployment team which is often the case in the organizations where we tend to see code freezes. They come to associate outages with changes and therefore, what can we do to reduce the number of outages? We'll reduce the number of changes. That becomes the tactic. The outage must have been caused by a change we made, therefore let's not make any changes. I think the other thing I've mentioned as well is the performance testing element of all of this.
Especially a lot of code freezes are introduced because you are going into a period of peak trading. You're expecting to see a lot of heavy demand on the system and quite often there's no real way to replicate that in any other time or any other place other than the actual event itself. There's a huge amount of nervousness and what tends to happen is, Mike, just as you were describing this, it's the system's been stable for four weeks and so, therefore, that means we're in a better place to cope with the peak in demand then if we just changed a bunch of stuff. Unfortunately, that rarely turns out to be the case.
**Mike** : Again, it is genuinely difficult to do this kind of testing. I do have a certain amount of sympathy for organizations. I remember working for a large lifestyle electronics retailer who at the time were doing everything with traditional fixed infrastructure and they had two data centers. In order to do a load test, they would have to take one of the entire data center out of the production load balancer and then just use that one half of their infrastructure in order to do their performance testing, which they still did do.
They could afford to because all of this fixed infrastructure is sized for the absolute peak transaction volume, which they knew they were not anywhere near because their annual sales cycle was not about to hit what they were doing performance testing. It is genuinely difficult especially when you have goodness and all kinds of downstream integrations as well. If you're talking retail, you've got payment gateways and banks and things that you're talking to, and that all need to be part of the test cycle. What's the alternative to code freezes then what should we be doing instead?
**Ian** : I think there's a couple of things, but one is when you do have outages firstly, you need to go and find the real root causes. Yes, you made a change but it's the way in which you made that change, maybe the lack of testing, or there's something in how you made the change. What you need to do is go all the way back and fix it at the point where you introduced it, not just put more and more gatekeeping in. That's one thing you can do to dry and address change freeze. The other is, and again, not a new observation, lots of people have said this, the more often you do something, the better you can become at it, and the lower risk it becomes.
Change freezes are often associated, they're not organizations who are doing a release every day, and then decide for three months, they're not going to do a release. They're often organizations who are doing a release once or twice a month, or maybe every three months. These are big, scary events anyway. Then if you add that big, scary event to peak trading hours, then it becomes, "Oh, my goodness, we can't do it." The other thing is, to start deploying much more frequently, and then it's much smaller changes, and you become more comfortable, and the risk gets smaller because you're making smaller changes. That's one way in which you can try and address code freeze.
**Neal** : Ian just finally mentioned the elephant in the room, which is humorous, because three of us are sitting in a very small room, imagine an elephant in this room, but which is risk, that's the root cause that so many organizations implement things like code freezes, because they put this on risk, it's too risky behavior. Ian's talking about a couple ways that you mitigate risk and that's really the root cause that you get as well, what can we do to ease your mind that something bad is going to happen if we started doing this more frequently? Whether it's better testing or--
Like Ian said, the more you do something it's not a big special event, it's just the thing we do every day and that becomes a lot less inherently risky, because statistically, it doesn't break most of the time, and only every once in a while. The more you build up all this accumulated stuff, the more likely it is to break. That's one of the great lessons from experience, continuous integration is doing it more often you end up doing a lot less of that integration stuff than if you do it all at the end.
**Cassie** : I would also add, like alongside that, yes, definitely mitigating that risk. There's that organizational safety aspect of it. Something that I've noticed as a result of these code freezes is what I mentioned before the blame culture, but then on top of that, it propagates. With the blame culture comes a hero mentality as well. Therefore, I have seen a lot of either the deployment team or someone who stays up all night, before the big event, and it goes off without a hitch. Therefore, that team gets a nice medal and gets really, a bonus, even sometimes I have seen that before.
Then, of course, people are either very scared to deploy and to do things because of the code freeze, or they are one of the people who are excited to be there at 2:00 AM if something goes wrong. With those two different things, that actually propagates a pretty unhealthy culture going forward. If you're trying to mitigate these risks, deploy often, it's about congratulating the hero culture and making it a safe environment for folks to feel safe to be able to deploy and push code and those types of things. That's a big one. We have seen different organizations who are able to deploy on a more constant basis, really look at things like blameless post mortems, really looking at, why did something happen?
It's not a blame thing, it's actually asking the five why's, what is the root cause, going back to what Ian said, what is the root cause to actually happen, and let's start working on those things. More often than not, we actually see that the symptoms are based off of really complex, big balls of mud monoliths, which is very hard to push go to anyway. What are the strategies that we want to put in place to decouple some of those things as a plan, as an example? Those are the things that should be invested in as opposed to covering the symptoms?
**Ian** : Yes, I think you've mentioned the big ball of mud there. Again, thinking about clients I've worked with, where they did have the code freeze. Another common factor was large, monolithic, complex architectures, where there was no graceful degradation. They had learned from bitter experience that the architecture tended to fail spectacularly in one big go, as opposed to seeing slow performance on certain things. It would just suddenly all stop working and so I think moving to more frequent deployments absolutely helps, but you may also need to make some changes to your architecture. Maybe introduce some patterns like circuit breaker.
If we are seeing very high load, maybe we make sure we don't pass that through to the legacy database or mainframe that will then crash completely that you protect those critical components from that load. I think the other thing that's out there as well, we were talking about very sync peak load and a lot of organizations say, the peak load is when we're seeing the most demand from our customers to use the system, it's not quite true. The peak load comes just after you had an outage on the busiest day.
That's the real peak load and I think that's something else that you often hear about these repeated failures, where the site comes back up five minutes later, it's gone again, the site go, they bring the site back up, everybody piles back in because they want to finish their buying what was in their shopping cart or whatever it was and the site goes down again.
I think the other thing is you have to architect full recovery from failure.
I think some organizations they've become so focused on avoiding failure, that they never stop to think. It will happen, you will have a crash, you have to plan for how you are coming back from that situation. The problem is if you haven't done that and you have an outage, it just adds to the trauma so suddenly it's taking two or three days. In fact, I worked for an airline who they actually had to suspend flights for several hours because what was happening is all the customers would come back onto the site to check the status of their flights and the systems would go down again and so, in the end, they just put a blanket.
"There are no flights today" on that website in order to get the load off the systems, because this massive behavior of users all coming back at the same moment, just cause this repeated crash.
**Neal** : This did end up in two complex to blip. We've been giving mostly one side of this story, but Ian mentioned early on the nuance of this. What are situations where it does make sense to do this and how can you mitigate the badness when there are situations where this is necessary?
**Ian** : I have one example, that's quite niche, but this was a client who was making scientific instruments. At the time they had no way to do over-the-air updates for their devices. It was blown onto a physical EPROM, I think the right term is, and then installed as part of the manufacturing process and so they would have a manufacturing freeze date and then make a huge batch of these machines, which would then ship out to the customers and if there was a mistake, you had to send an engineer to every single customer site with a bunch of new ROMs to plug in.
You want to code freeze. You want to know exactly what is in that software at the point it ships and that you've tested it and nobody is done a last-minute check-in that suddenly ends up in the code in an unexpected way so I think that was. I've heard the same from car manufacturers, although there that's changing because a lot of them are moving to over-the-air updates now. If you have a manufacturing deadline and it's going in a physical device, it's hard to update then something like a code freeze makes a lot of sense.
**Cassie** : Yes. I think another example would be around, we're not asking you to stop your code freezes today, especially if you have a lot of root problems that you need to uncover first because I would say that in some of the clients that I've had, we got brought in, maybe about three or four months before the Black Friday event. In that circumstance, I would say in the way we think about things in an iterative manner is how do we start instead of as an organization say, this is a massive code freeze that no one actually pushes anything to.
It's actually saying, "Hey, what are the areas that after you do the 5 Whys of where are the problem areas that we are trying to mitigate those risks essentially? It is okay to have very smaller code freezes on those specific areas as you're trying to fix the root problems, going forward but I would say then the next time that big event comes, hopefully, that code freeze goes away. Again, it's something that I wouldn't say, "Just remove all code freezes today," because there are inherent root problems that needs fixing and so I would say, start figuring out what the long-term strategy is on those things. Iteratively, start making those code freezes much smaller windows into the areas of the code that are quite risky at the moment either for performance or security reasons, and actually start looking at those areas.
**Neal** : I think that's super important perspective that too many architects don't take, which is that software engineering is really code over long periods of time. It's not the snapshots of one thing to another and you can't just instantly change one thing to another particularly large organizations. It's really about, can you make incremental improvements constantly? Even if you never get this mythical perfect in state, you can get better constantly and find the places where there are genuine risks that you want to isolate in places where it's a lot less risky, and you can be a lot more aggressive.
**Ian** : I have another example where I think-- When I describe it, you might think, wow, hold on, no one would do that. It's amazing how often I've seen it, which is, when you have organizations who have code freezes, you tend to get changed windows. These are periods of times when you are allowed to make a change. The problem is that, the same change windows is the operational people have, as the network people have, and the infrastructure people have.
I've seen several examples of where someone's trying to do a change to the software, and they haven't coordinated with the infrastructure team who are busy migrating a bunch of stuff to a new set of disks. The deployment is running incredibly slowly because in the background, all these RAID arrays have been rebuilt. There's just been no coordination and actually saying, we don't want too big changes at the same time, if they just coordinated a little bit more, probably we should not have done the deployment that day, it should have been paused. That, unfortunately, seems to happen remarkably often.
As I say, when you have these organizations who get very risk-averse, it tends to push everybody into trying to make the change during the same small window.
**Neal** : I've seen that with the QA in particular, you've got this small window and everybody's rushing to get stuff done. People who get caught up in the dogma of every iteration shall last this exact long, and the QA people get really stressed at the end of that. I've told a lot of people, "Why not just offset that one week?" That gives them a week and they're like, but the rule says that has to be, "You're stressing these people out, stop it." Exactly the Ian's point, thinking about the process of why things go out, rather than just saying dogmatically, this manufacturing metaphor that we've just read over and over again, helps get more effective performance.
**Cassie** : One thing to add to that is, I've actually seen this on a client side is that, we have stressed out the QA organization so much because of these dogmatic rules that, first of all, they're the ones who probably know the domain the best in your organization. I've seen an entire QA group resign after a very stressful situation, and now they lost all of their domain experts as well. That tail-on effect, it can be quite detrimental if that culture keeps propagating.
**Ian** : I do want to mention that something, if you like, the unspoken secret of change freezes. Most of them aren't really change freezes. What they normally mean is, the normal process of deploying software isn't happening. However, there are things that someone will say, "Quick, oh, my goodness, we've got a problem, quick make it change the prod system." There's almost always, they call it the tactical or the emergency deployment process, which in most places seems to be ignore all the testing and just do the change anyway.
If you like, here's the other irony of change freezes is, they're often not really change freezes. However, because there's no code change happening, because no one's meant to be checking anything in, what often happens is, the first release after the change freeze, you regress all the bugs that you fixed during the change freeze, because they never went into source control because you're not allowed to check in. You get this ironic behavior of the first release, not only if you've got all the pent up demand for the people who've not been able to get things done during the code freeze, you've also got you then regress all the bug fixes you did using your emergency deployment process.
**Mike** : Hopefully that gives listeners an idea of why we felt that was too complex to blip, since the blip there's a couple of paragraphs. Thanks very much for listening. Thank you, Ian and Cassie, for being our guests on this podcast. From Neal and I, thanks for listening. Please do give us a rating, however, you're listening to this, whatever platform you're listening on, and leave us a comment, telling us how you like the episode and what else you'd like to hear from us.
**Neal** : Thanks everyone, and we'll see you next time.
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