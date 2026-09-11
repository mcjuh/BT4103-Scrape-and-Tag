<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/understanding-bias-ai | Title: Understanding bias in algorithmic systems | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Understanding bias in algorithmic systems 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons | Podcast guest  danah boyd
December 28, 2018 | 21 min 6 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/understanding-bias-ai#transcript)
Listen on these platforms
## Brief summary
For this bonus episode, Rebecca Parsons, Thoughtworks’ CTO is joined by special guest danah boyd, a sociotechnical researcher at Microsoft Research. They explore how bias is introduced in algorithms, the damaging impacts this can have and how this can be mitigated.
**Podcast Transcript**
Rebecca:
Hello and welcome to the Thoughtworks podcast. My name is Rebecca Parsons and I'm the chief technology officer for Thoughtworks. In today's special episode, I sit down with danah boyd, principal researcher at Microsoft research, founder of Data and Society and visiting professor at New York University's interactive telecommunications program. We discuss everything from the early days of online content moderation to bias in AI. I hope you enjoy the conversation as much as danah and I did.
Rebecca:
Hello, danah. I'm thrilled to get a chance to talk to you.
danah:
Thanks for having me.
Rebecca:
You just spoke to us about bias and data and misuse and use. Let's start first with what you have learned in dealing with education systems and what that actually implies for businesses and executives.
danah:
One of the blessings and curses of having been with social media since its earliest days was the ability to see the good, bad, and ugly of how everybody is using these systems. I will never forget in the earliest days of trying to do content moderation on social media, we originally were just like, well, if we let anybody post their thoughts on the internet, it'll be amazing. They'll share such sophisticate ideas, it'd be great. And the first day they're like, "Oh porn, why are people posting porn?" And of course people are going to post blog.
danah:
And then you start in these moments where you try to challenge things. I remember when AOL was concerned that people were talking about anorexia in a positive sentiment on their platform and they decided that they would ban that term. They would just make it so nobody could post about anorexia, about anything, prevention or participation or anything. It took less than 24 hours for people to start talking about their best friend Anna and just being like, "Oh, I had a great day with Anna and it was wonderful. And we talked for a long time." And that's encoded messages.
danah:
So one of the things I've taken after years of looking at all of these misuses, reappropriation of technology is that we have to think not simply of what we designed the technology to do, or how we think we will integrate it for all of the good things we imagine or we want, but we have to constantly question and reflect on all of the other incentives of every other actor in this ecosystem. And the more complex our systems get, the more that we rely on data, the more that we integrate technology, the more we are going to see different kinds of adversarial manipulations and just plain bias and limitations of our systems. And that just requires a new way of thinking.
Rebecca:
And do you think people who actually design these systems or have the vision for the product, it doesn't feel like their best place to figure out how it could be misused because they're so focused on the positive good. So how do we go about protecting against that when we're not often in a position really to be able to understand how it's going to be misused?
danah:
I think that's completely accurate. I think that when you think in terms of product, you imagine potential and long ago we also figured out that you don't necessarily imagine profitability and business. And so we figured out long ago that you need a set of different actors with different responsibilities sitting in that C suite. You need co-founders, you need somebody who has a financial mindset, somebody who has a legal mindset. We're at a point right now where we've elevated the chief security officer, the CSO, in some organizations and less so in others.
danah:
I think we have to build a structure organizationally where we're thinking positive and negatively at the same time in a sophisticated way. And the thing from a product place is that the most sophisticated product people will not be paralyzed by hearing the misuse. They'll see it as an opportunity for innovation. Like, "Oh, okay, if I know people are going to do that, then I have to do these three things." And you're like, bingo. And that ability to innovate and co-construct a technical system is going to be so essential because these technologies are situated within social environments, so they have to be socio-technical from the get go.
Rebecca:
And do you think that this is the moral equivalent of a chief security officer or does it have to be a range of people? In order to look at this from different lenses, I'm thinking college students versus people of color versus Muslims. Do we need to bring people with those different perspectives or do you think we can learn to channel some of those different perspectives?
danah:
My belief is that organizations have to own these issues. And the question is how they own them well. It can be owned in the boardroom, it can be owned in the C suite. There are different ways in which both of those work, but owning it is not necessarily just the final voice on it. So it's not just about having one person who is being the moral authority, if you will. It's about having somebody who can build the processes to hear and listen and think in a more sophisticated way.
danah:
And that means being the person who channels those voices, not just the person who owns it, but the person who owns it owns the processes to make certain that that happens. And that's what I think we're missing right now because right now when it's too spread out, nobody owns the processes for integrating that into the decision making frameworks. In the same way that a CFO owns financial structures but doesn't own all the decisions in the business, right, and in fact, when you build a business with a CFO, owns every aspect of business, you've got a bigger problem.
Rebecca:
Yes, particularly when the own technology.
danah:
Right.
Rebecca:
And really, that lands badly.
danah:
So it's more than about have you have somebody owns it for the processes and build the structures to hear. Especially to your point, depending on what topics we're talking about, diversity of experience, diversity of background are so critical in making certain that you think beyond your world.
danah:
This is also one of the reasons why I'm glad that even in the security space that we've moved away from thinking that an organization can solve security themselves. Even the simplest move of moving to bug bounties because when you move to bug bounties and you build the process to involve external actors in trying to mess with your system, when you build red team structures, you start to realize that living inside your organization, you'll never see things in a way that an outsider sees you. And so like how do you bring the outside in constructively.
Rebecca:
Mm-hmm (affirmative), which is really just an extension of what we've learned along the way in user experience design and customer experiences. We have to look at it from our end user, our customer's perspective as opposed to our own.
danah:
Absolutely. And as you know, getting UX into a conversation wasn't overnight.
Rebecca:
No, it was not. And it's amazing how many people feel like they understand until you go out and ask the questions. And people have a way of having different ideas than we want them to have, don't they?
danah:
But that's also where you... I think the parallels there are actually quite elegant because you think your user, I know how to use this, so everybody must use it the way I use it. And as you know from user experience, like that's not at all with a discipline is about. And the same unfortunately happens with ethics and moral thinking, which is like, well, I mean the values are very clear. Doesn't everybody understand the values? And it's like nope.
Rebecca:
That's not [crosstalk 00:06:51]
danah:
And I think you're right that maybe that's a better paradigm than even thinking about some of the security because at least with security, like classic security, people don't think immediately like, oh, I know security. In fact, they're usually be like, "That's somebody else's job." So I think you're right that there's something about that UX narrative as part of this frame.
Rebecca:
So we know AI systems that are trained on data respond and encode the biases that exist in that data. People don't intend the systems to be biased. And in fact, sometimes they work to make them unbiased. But how do we actually understand the level of a bias and how can we mitigate it and whose responsibility is it really to govern these? And how should we look at that process? Please don't tell me we need the bias police.
danah:
One of the challenges about everything that involves humans is that everything is biased. And so part of it is realizing that we are never going to achieve the ideal even as we work consistently for the ideal. And the result is that it makes us start to think about like how do we set up the processes to constantly improve rather than solve for. And that's where, when it comes to bias in an algorithmic system, part of it is to just be constantly interrogating and being reflexive.
danah:
And the irony for me as having a double background in computer science and anthropology is that I find that both of those are really critical for this conversation. Anthropology brings this idea of reflexivity, that you are position in an environment is constantly shaping, shifting, influencing. And so that's a mindset that have people have to look for that. When you sit down with anybody doing data work and watch them through their cleaning processes, they are trying desperately to deal with, what they will talk about as anomalies, right? But giving them a framework for thinking about anomalies becomes really important. So, that's where I think training is very viable.
danah:
Now governance happens at different levels institutionally. Part of it is, is that the governance processes in an organization. So start by asking questions and be like, "Are you doing your own internal accounting? Are you able to articulate the limitations where that data can and can't be used?" It's also where you start to see opportunities to make that transparent. So like, I've been having this conversations around GitHub and what does it mean to articulate in a repository about what the limitations of this particular algorithmic system can do given the constraints on data. If the data has these features, this will not work, or this will actually reinforce it as you never intended to. So how do we actually start to build that into the process? And that's where I see this opportunity at the technical layer.
danah:
In terms of broader scale governance, I think this is the question of how then are these systems being applied? And so when I look, for example, in [inaudible 00:09:36] of criminal justice, criminal justice is an imperfect process, always has been, and that's one of the reasons why we build checks and balances into it. That's why we build even due process. And so I think that there's a very rich and open question of can a system allow for the necessary forms of due process that we expect? If not, maybe it can't be implemented yet, and maybe there are domains and areas where we're just not ready. No matter what, we're not ready for it or where we have to integrate it into a process that actually can be interrogated.
danah:
And that's where I think domain specificity comes into play and the governance processes are going to look different and for better and worse, I think that there are going to be algorithm police in specific contexts, and there are ranges where I think that that just becomes more important, particularly when we're talking about the stakes being so high when we're talking about life and freedom.
Rebecca:
Yeah, it's one thing for them to get a recommendation wrong. It's another thing to make a decision in a criminal justice context.
danah:
Absolutely. And being able to understand that distinction, and this is what worries me of using code that's done for earthquake detection and thinking that that can be reused for predictive police say without really questioning some of the foundations of how those analytics work, what that data looks like, what the reinforcement processes are for the learning system.
danah:
We actually have to step back and say, oh, maybe, maybe not. And the other thing I think is really important is what level of maturity does a system have to have before it's implemented at scale? So I love talking to NASA engineers because they know that they have one shot. When that robot goes up into space, yes, they can do some things from a distance. But sitting on Mars, they're not going to be able to toy with that hardware and the way that they may want to. And so that has provided a level of sophisticated thinking where they understand the ramifications. And I think that we have to treat certain domains in [inaudible 00:11:25].
danah:
At the end of the day, you get a lousy ad, oh darn, but I don't want to be sitting back here 20 years from now being like, oh, just like that forensic's thing, we got that algorithm thing wrong and a lot of people went to jail. I don't want that to be the Innocence Project's work for the next 20 years.
Rebecca:
Well, and also when you think about, as you say, the feedback loops. If you do start with something that you don't understand and does have that bias in something like the criminal justice context, you get reinforcement of this bias. How much understanding do you think the public, the government, the criminal justice system needs to have of these algorithms before they can actually tackle problems like this?
danah:
So they need a level of expertise surrounding them, right? I don't expect a lawyer to understand every detail of the mathematics, just like I don't expect them to understand every detail of the forensic science. But I do expect them to have processes in place that allow them to incorporate that expertise into the system. I also believe that it's really important that the processes are in place for people who don't have that level of knowledge, not to suddenly become experts. I actually think that's where we reach a different danger, but how can they be supported effectively?
danah:
So take for example another domain of decision making, does everybody need to have the level of medical experience of their doctor in order to interact with their doctor? When we set that up, that's dangerous. Do they need to be able to ask questions? Yes. Do the doctors need to be able to share whatever information? Do we need to create a better bedside manner where people are actually able to articulate what those trade offs look like and the consequences? Absolutely.
danah:
What we have right now in medicine is a moment where doctors have been socialized into, "I will tell you what this is." Even though all of us know the tiniest bit about science and it was all probabilistic and when they come in and saying, "This is what the disease is, this is what you do." People immediately go to the internet and then they self-diagnose and then they're off on a totally different plan of [inaudible 00:13:20] and you've created a trust rupture and that trust rupture is devastating.
danah:
So the response from a doctor is to say, "Okay, here's what I know. Here are the set of different possibilities. Here's what you're going to find on the internet of a whole range of possibilities. Here's why I'm going to rule those ones out or say they're lower probabilities. Here's how I'm going to walk you through this and can we address this together? Because you're experiencing symptoms that I can't feel and I need your ability to articulate those. I'm looking at other mechanisms of evidence and how do we do this as a co-construction." And that is about changing the power dynamics.
danah:
And I use medicine as an example because generally speaking, you're hard pressed to find a doctor who doesn't want their patient to be healthy, and you're hard pressed to find a patient who's not trying to figure out how to be healthy by the best means possible. The power dynamics look different in a criminal justice environment, right, where it's adversarial, and so then how do you build the right structures so that you get the right, shall we call it defense, that you have the expertise around you. Right now we're not even doing that for the basics of law, let alone technology, and that's where for me the technology becomes such a tool of the state in an abusive way and that worries me to no end.
danah:
So that's where I feel like the innovations are much more likely to come in fields like medicine in the short term, then it feels like criminal justice, which is why I'm okay with saying let's just outlaw this until we can actually do it better. I'm okay with that in criminal justice right now.
Rebecca:
And if we look outside of criminal justice, what kind of rights do you think people have in understanding the basis on which some of these AI and learning systems, the basis they use for their decisions, like a credit score or like a loan application, things of that nature. We'll leave criminal injustice out because I think it is more fraud.
danah:
Credit's probably an interesting example to go down, because again in the 1970s the debates around the FICO scores were so intense and the idea was like, "Oh well, we'll just let you know and be able to ask questions of this." It didn't stop the prejudice. In fact, it actually reified it. And so one of the worries for me about transparency without mechanisms of accountability and without accountability to a particular value system is that transparency becomes performative as opposed to actionable.
danah:
So the question for me is sort of like, okay, what is the value that we've all agreed to? That's in many ways the governance standard. So is the value for credit that everybody is equitable under what terms? Can we agree upon those terms and what are the ramifications? Then once we agree upon those terms, how do we hold the agents of decision making accountable? What kind of meaningful standing do does anybody have? If you don't have standing before the legal bodies that are holding us, then transparency is just infuriating.
danah:
Once you have the mechanisms of accountability, then you have transparency in the question is to home. So is it individual, do I expect you to become an expert on whatever particular statistical models you're using? No. So then the question is who does that on your behalf? And that's where we turn to civil society organizations that have to get built up. And it's where I look at things like a privacy policy. Let's be honest, that is not about the consumer at all. That is not about a person. That is about competing legal entities, where hopefully some of them are able to compete on behalf of constituents, consumers, users, people. And if that is not a rich infrastructure, then it's just performative.
danah:
So I feel the same way with algorithmic systems. Let's also be honest that most of the systems, the engineers can't explain how they're working, and that's more than anything right now what I think we need do to make transparent. It's like we don't know. We don't know why that works. Obviously we can talk about that with neural nets, but across a lot of ML, we're just like, it seems to be a good fit given training data, and yeah, it's prioritizing these features. We don't even know what those features mean.
danah:
And that's where I worry that people as we get obsessed with creating accountability in the wrong ways, people will just make those features harder to interpret. Which is where I'm also very interested in advances of interpretability and explainability in machine learning and that's where it's a good reminder. It's like we're the tip of a field making effort as opposed to something where it's like, oh, the computer science have this and the public doesn't.
Rebecca:
Well, let's turn to something more positive. Where are you most optimistic about the impacts that these technologies, big data, AI and machine learning, can have on people in society?
danah:
I start by saying that I'm a scholar above all else. I believe in learning and there is nothing more complex than humans and the societies we create. And so to the degree that we are using every information around us to try to learn, to try to be more just, to try to find ways of making this world better. That's exciting. And that's where I look to many of the engineers turned philanthropists, and that's exactly what they're running around doing, and can we solve X, Y, Z? Interesting problem. Can we change the dynamics of mosquitoes? Right? You're just like, whoa, that's awesome. Can we help people get access to more information? And that's where you have complexities that are historical, right?
danah:
Carnegie was one of the great barons who pushed for libraries. He was also a bastard, unquestionably. And so we have to live with these dynamics simultaneously. So for me, when I look at the possibilities of medicine, the possibilities of trying to understand poverty, our understanding of poverty is a modern day phenomenon. What can we do to remedy it? What does it mean to communicate? When I talked to my grandfather about what war looked like in the forties or what it meant for him to not be able to communicate with family and the changes. That's so amazing.
danah:
So for me, I think part of it is I start with such a love of these technologies, but I don't believe that you can develop those technologies in a societally beneficial way if you don't understand their misuses. And I think that's the shift from when it's esoteric to when it's mainstream. I grew up in a world of social media where those of us who were in the internet in those days were self-identified geeks, freaks and queers. Right? And I claimed all three. And it was like, it was home, and it's now mainstream.
danah:
And I think that many of us naively thought that when it went mainstream, it would just bring the values and norms of all of us on the outside forward. It didn't, it never would have. And it doesn't mean that it's all horrible. It means that we are forced to grapple with humanity. It means that we built international systems and now we're forced to grapple with global governance.
danah:
And I think that's where, for me, it's precisely the love of these technologies and the potential of them to solve really hard problems, to augment human processes in brilliant ways. That is why I think we need to get our heads wrapped around how these things can be misused, because otherwise we are going to throw the baby away with the bath water and I don't want that.
Rebecca:
There's such potential to make human lives better if we can just accept the reality of what we're dealing with.
danah:
Yeah. And I think we also have to understand that there's never been a tool in history that has been designed to make human lives better that somebody hasn't used to oppress, always, always, always. And that's why human governance, societal governance, is part of a technology conversation, whether or not we want it to be.
Rebecca:
Well, thank you very much.
danah:
Thank you.
Rebecca:
Thanks for listening to this episode of the Thoughtworks podcast. Be sure to rate us and subscribe to us on whatever your podcast platform of choice is. Thank you.
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