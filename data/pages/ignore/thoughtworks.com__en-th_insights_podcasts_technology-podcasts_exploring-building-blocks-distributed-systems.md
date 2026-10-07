<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-building-blocks-distributed-systems | Title: Exploring the building blocks of distributed systems | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring the building blocks of distributed systems 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Scott Shaw and Rebecca Parsons  | Podcast guest  Unmesh Joshi
February 22, 2024 | 35 min 46 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-building-blocks-distributed-systems#Transcript)
Listen on these platforms
## Brief summary
Distributed systems are ubiquitous yet complex. They can be particularly demanding for software developers and architects tasked with dealing with the sometimes unpredictable nature of the interactions between their various parts.
That's why Thoughtworker Unmesh Joshi wrote _Patterns of Distributed Systems._ Published at the end of 2023, the book explores a number of patterns that characterize distributed systems, and uses them to not only help readers better understand how such systems work but also to solve problems and challenges that often arise.
On this episode of the Technology Podcast, Unmesh joins hosts Scott Shaw and Rebecca Parsons to talk about his book, explaining where the idea came from, how he put it together and why it's important to get beneath neat abstractions to really get to grips with the inner workings of distributed systems.
**Learn more about[Patterns of Distributed Systems.](https://www.pearson.com/subject-catalog/p/patterns-of-distributed-systems/P200000011305/9780138221980)**
## Episode transcript
**Scott Shaw:** Welcome, everybody, to the Thoughtworks Technology Podcast. I'm going to be the host today. My name is Scott Shaw, and I'm joined today with co-host Rebecca Parsons. Would you like to introduce yourself, Rebecca?
**Rebecca Parsons:** Hello, everyone. This is Rebecca Parsons, another one of your regular co-hosts. I'm the CTO Emerita, and we are joined today by another Thoughtworker based in India who has just written a book — or finished a book! [chuckles] Unmesh, would you like to introduce yourself?
**Unmesh Joshi:** Hey. Hi, everyone. I'm a principal consultant at Thoughtworks and been with Thoughtworks for 16 years now. As Rebecca said I’d been involved in writing about distributed systems for the last few years which is now compiled into a book which is out.
**Scott:** That's quite an accomplishment. Unmesh and I worked together 10 years ago or more back in Pune, India, so it's a pleasure to be talking to you again. The book is called Patterns of Distributed Systems which is a pretty big topic, and I think it's also something that's probably not that well documented elsewhere, and so I think this is a unique book and probably fills a needed gap in the market right now. I wonder, how was it that you first came to want to write a book? How did this get started initially?
**Unmesh:** It's a long journey. I think it started back in 2015, 2016, when some questions started coming to my mind. Typically if you see the digital transformation projects or any project for that matter, you work on for last several years, they involve cloud services, cloud like Amazon, GCP, and Azure and also products like Kafka and Cassandra and other distributed databases, or Kubernetes now that everyone uses that.
I was like everyone using it or started using it back then 2017-ish. I was trying to learn all of these things, struggling my way through it. At the same time, there was some interesting work that a team in our Pune office was doing, and I just happened to work with that team to help them out. This was for writing software for a large optical telescope called Thirty Meter Telescope, and a lot of problems that they had to solve, essentially keep data distributed and distributed copies of data in sync have different telescope subsystems coordinate and work towards some task.
All those I thought were similar to what I was learning about systems like Kafka or cloud services, but for this Thirty Meter Telescope thing, the challenge was that they had to build things from scratch. There was a need to understand all these things in a little more depth so that you are confident that the decisions that you are taking are right. At that time, I started going a little more deep and trying to understand all these things.
Things like Paxos, for example, or things like Lamport clock. When I went to books, the books were very theoretical, I thought. They explain a concept; they talk about asynchronous systems and synchronous systems, even things like Lamport clock or Paxos, but there is always some mathematical abstraction or description in terms of pseudo code, and you don't really see how Lamport clock is used in practice.
There was that huge gap now that I struggled with. What I decided was to really go to open-source code bases, and that's the beauty of open-source. I think there is so much code available for you to look at. I started going through Kafka's code base and Cassandra's code base and various other code bases. Then I figured out that-- I could connect dots. What I was reading about and what I could see in the code I could connect those dots, but there were also some gaps.
What was explained in the book versus what was actually implemented, there were some gaps. What I decided to do was-- Kafka as a whole is a big system. It does so many things, so if I focus on maybe step by step, if I have to build something like it what all decisions I need to take and what are the different components I need to code. I started doing that. I coded my own miniature Kafka. I coded my own miniature Cassandra and I made sure that the code is not toy code.
It resembles what I actually see in production code of Kafka or Cassandra or similar tools. That worked pretty well because then I had real code to look at. When I was talking to people they also had real code to reason about, and that worked pretty well on that Thirty Meter Telescope project. I did a couple of workshops using this technique. Just don't talk about distributed system theory, but let's say let's build Kafka-like thing in a few days.
This approach of tackling one problem at a time and then the next problem, and then weaving multiple things together, and then you have this big system which looks complex. If you look at it as a whole, it looks complex, but once you focus on one thing at a time it's a bit easier. Then I happened to talk to Martin about what I was doing, and Martin has done this kind of thing in the past with various systems, like his Patterns of Enterprise Architecture book, I think is a similar thing done to the world of object traditional mapping frameworks.
He liked the idea and he actually suggested that I write patterns because the small components and small problems I was trying to solve one at a time, now he thought that can be very well explained as a pattern. That's where it started. That's when around start of 2020, the start of the pandemic, I started documenting these patterns, and in last three years, I think we got to a stage where we had enough patterns to maybe explain something like Kubernetes or Kafka and then we decided to compile it into a book.
**Scott:** It was helpful, I guess, that we were locked down in a lot of places, and you were stuck at home, I imagine and had a lot of time on your hands to write?
**Unmesh:** Lockdowns and during the pandemic, I think that gave me a lot of time to work on these things.
**Scott:** Did you find it was a difficult transition from writing code to communicate to other people, to writing in English, to describing these things in English in a concise way? Did it take you a while to get into the pattern of writing patterns?
**Unmesh:** No. Actually having code in front of me or in front of people while I explained things in English, that actually worked pretty well. I think that's one of the beauties of the patterns approach. I think that patterns, you have some well-defined names. Like Lamport clock is a well-known name, or a write-ahead log is a well-known name. Or even Paxos is a well-known name.
When you read just English with, let's say pseudo-code or some abstraction you need to imagine things, and then you make some vague impressions in your mind of what that thing really is. Now, as opposed to that, when you have real code in front of you which highlights what Paxos looks like or what Lamport clock looks like, it's actually very easy. Even for me, writing was easy after the code and some examples were done.
The hardest part was to get that code that shows the essence of a particular pattern, and then writing about that around that was the easier thing.
**Scott:** I think that's interesting. I think it reflects the approach to technology that we have at Thoughtworks, which is you can talk all you want about your opinions, but until you write the code, you don't actually know and the opinion is walk, code, talk. I think that's the way we try to ground things usually in practice. I think that's an interesting way to approach it.
**Unmesh:** Martin often calls and, I like his sentence, he says code is like mathematics of our profession because when you write code and execute it, you cannot cut corners. When you're drawing on the board or writing about something. You can cut corners and that's true about a lot of books on distributed systems as well. Even if the focus is to prove that something works, there are certain assumptions and those assumptions might fail in practice or you can very well ignore some of those assumptions that are out there.
If you're not aware of those you can run into real issues in production.
**Scott:** I wonder how many other people have been through this experience. I know I did years ago when I first naively tried to start building distributed systems and then ended up reinventing a lot of the things. I pulled this book out because this was a really influential book for me. I don't know if you can see it, but it's Jim Gray's book on Transaction Processing. I was so relieved when I found, oh, somebody's actually documented how these things work and I think your book is probably going to be similar for people.
It's ironic that we live in a world where distributed computing is ubiquitous. With the cloud, everything is distributed, and yet there are so many abstractions and tools and open-source frameworks that remove a lot of the details of that away from us. That, even though we're using it more, I think developers who are just starting in this probably learn less about it because they don't have to actually build it themselves. Do you try to get beyond those abstractions?
**Unmesh:** Oh, yes. That was one of the one of the main goals that to go beyond abstractions and to show real code. I really liked when I saw Jim Gray's book that you showed, because that was something that I wanted to do with distributed systems. It's sad that Jim Gray's book came in the 1990s. It's excellent because it does the same thing that I wanted to do with distributed systems.
It doesn't leave things to imagination. It gives you very concrete things that you observe in systems at the code level. You can read and be sure that this is something that you can expect. For even things like as I said, the book has four broader sections, one bigger chunk is about replication. One is about how you manage time in distributed systems and then how you manage a cluster server to communicate with Azure. Those are the third sections.
Something as obvious as replication has a lot of complexities. I think it's not obvious to developers when they read about replication because the term, at least people think that it's a well understood term where in practice it is really not because because replicating data on multiple servers and then making sure that they agree on the data that's replicated it requires consensus.
Really systems which give you that a guarantee really need to implement something like Paxos or Raft. Now you see that most systems, or most data systems including Kafka and all the newer databases which implement this replication, they implement Raft or Paxos as that replication mechanism. Having concrete understanding of what goes on in something that's at least perceived to be obvious is important. I think in the book I try to go into the details of at the implementation level, how this replication mechanisms work.
**Rebecca:** One of the things I was wondering about a feature, if you will, of patterns is that you can talk about when they are applicable. Given the fact that some of the things that you're talking about are somewhat fundamental notions, there are, for example, lots of ways you might decide to use distributed time. As you were looking at these different code bases, did you mostly run across essentially the same implementations, or were there times when there might have been different implementations for one of these more fundamental constructs that you were able to examine?
**Unmesh:** Yes. I think again, the strengths of the patterns approach is, you look at multiple things, and the rule of three is generally followed that you look at at least three things before you call something as a pattern and then there is this concept of similarity. In various systems the implementations are similar, but not exactly the same. Patterns allow you to document what similar thing is across these systems. There can be variations that you then document as well.
About the replication and distributed time as I said, if you consider replication that I said is complicated than what people think it is. If you consider Raft implementation that's used in products like CD or more modern new SQL databases and you look at Kafka's replication protocol there are similarities, but they are not exactly the same. For example, the way Kafka maintains high watermark and Raft has something called a commit index to differentiate between what is a stable portion of the log and what is the portion that you're not sure about.
It is the same the way they use something that I call as a generation clock or Kafka call it epoch and Raft calls it its own term, but that's really to detect if there are stale leaders out there which are trying to cut across your new leader. Those things are similar but not exactly the same. What I have tried to document is the similar portions with differences documented as well.
For distributed time, it's similar, I think. Lamport clock is very, very fundamental and all key value stores use it essentially to detect ordering of rights, but what you see in practice is a variation of that Lamport clock called hybrid clock that's used. Because Lamport clock as as it's documented, is just a simple integer counter that you use, and then you pass it across all your messages and they're stored with the values that are stored as well to make sure that you detect which rights happen before other.
In practice in the data world, you typically will like to have real date time and real timestamp attached to these values to detect which values are written earlier and later. This Lamport clock technique is is used along with system timestamp. You use that counter, but a system timestamp as well. I'm saying system timestamp, but this is another thing that's not well understood. I think that different servers when they use system time, the time that your machine gives you, or the server gives you, there is no guarantee that those will be in sync.
That's a big problem in practice because then you can have issues where your newer rights, if they are assigned an older timestamp or a lower timestamp, they can get overwritten by something that was written before but was assigned a higher timestamp. That's a big challenge. Most practical systems, they combine this Lamport clock technique along with this system timestamp, and that's the hybrid clock technique that's used in a very similar way across all data systems.
Like, MongoDB uses it the same way, CockroachDB uses it the same way, YugabyteDB uses it the same way. Other advantage of, again, the patterns approach is that if you see all these systems, they are written in different programming languages, from Scala to C++ to Rlang, to Golang, to Rust. The broader implementation structure of all these things, it remains the same, even if the language of implementation differs.
**Scott:** It's interesting. I see some parallel between the work that you've done and the Jepsen Project in verifying perhaps the claims of some of these systems and actually digging into the details to see how they really work. Even with open source, there are so many claims made that are a little bit superficial that don't really go into these details. I'm curious if you found any contradictions when you were digging into the code or errors or things that didn't quite work the way they were advertised.
**Unmesh:** Not contradictions, but things that are omitted from the descriptions. Like Paxos, for example, it's very, very popular replication algorithm or consensus algorithm. There are some obvious things. Paxos stops at the point where it says that okay, multiple nodes now agree on one value or one command to execute, and then one of the nodes knows about it. Then, how do you make sure that all the nodes know about it?
Because in a distributed database, for example, it's not enough for one node to know about it. You need to have all the replicas to remain consistent or to have the same data. Paxos doesn't talk about that. What's called full replication that you make sure that everyone finally reaches the same state, Paxos doesn't talk about that. This looked like an obvious question that anyone would ask.
I was searching in implementations, there are some implementations of Paxos which are popular in academic circles, but they don't solve this problem, and they don't even talk about this topic. It's really fascinating and surprising that it required a new PhD thesis, that's Raft, which clearly talked about that. This is also a problem that you need to solve, along with basic consensus. It gives you the complete description of that.
Or there are people or the implementations which claim that they use Paxos like Cassandra. They use their own extension to solve this particular issue. That extension works, I think, but that's an extension to what is proven by Paxos. There were things like that. That's the advantage that I found while working on this, that you get these questions. Even when these questions that people hesitate to talk about, they are real questions that can bite you in your production implementations.
Like with Raft, for example, Raft's leader direction and any Paxos implementation, for example, can go into LiveLog. All the nodes, they just keep on tripping the leaders and just go into a phase where there is data detection happening with no real work that any node is able to do. This is a real problem. Even if you have good Raft implementations, they can go into this problem. A couple of years back, I think there was an outage in Cloudflare system. It was, I think a six-hour long outage.
This primarily really happened because of this LiveLog in the Raft implementation of its CD. This can happen in your Kafka cluster or Kubernetes cluster, which use this Raft algorithm. Some of these loopholes in these implementations, you at least need to be aware of that, okay, something like this can go wrong. Even if the documentation doesn't say aloud, that this can go wrong. This can go wrong in practice.
Or even things like I talked about hybrid clock. With hybrid clock or the basic characteristic of Lamport clock, that you only get partial order. When I say partial order, if there are two independent writes happening on two different nodes, you cannot really figure out which happened first and which happened later. It's only when two nodes are talking to each other or writing to the same key, let's say, you can detect the order.
If there are independent keys written on independent servers, you can't detect the order. For that, Google has their own infrastructure with something called as true time. Open-source implementations, which can be deployed on a data center or different cloud settings than Google, they don't have luxury of this true time. Then what they need to do is they need to assume what can be the maximum clock drift or clock skew across servers. I have documented this as a pattern called as clock-bound wait.
That you just wait to make sure that the timestamp at which you are writing, all the other servers have actually reached that timestamp before you make that write visible to others. Some of these are subtle things. If these assumptions go wrong, that maximum clock skew if you assume to be, let's say, 200 milliseconds, and in reality, it's 500 milliseconds or more than that, which can very well happen, then you can see those writes done in the opposite order to what they really are done. These things, I think you will get to know or at least question some of the documentation.
**Rebecca:** I think that speaks to the whole purpose, though, of writing a book that lays out not just the pretty abstraction, but the reality of the implementation details because you're not going to run across a problem, most likely with a pretty abstraction. You're going to run into a problem in production when reality hits the code. It is truly amazing how often people will use libraries and system tools like this without really understanding what's under the hood.
You can understand that because maybe it works 99% of the time. It's a lot of work to do what you've done over the last three years to really understand these things. I do think that the role that this book has is it provides the mechanism where you can get-- it's the middle ground, if you will, between the nice pretty abstraction and somebody having to troll through the entire commit history of Kafka to figure out how it works. This is a nice middle ground.
**Unmesh:** Absolutely, I think. One of other observations I had when I started my career, just to relate to the times we are now, to the times back in the late '90s, I think. As an industry, I think when we don't know how to make sure that people understand certain concepts, people fall back on certifications. You see the times where everyone is asking for Amazon certifications and GCP certifications and stuff like that, because we don't know how to make sure that people understand how these systems work.
Understanding these patterns or the basic principles of how, for example, Amazon builds the services that it provides, it gives you a good way to understand broader spectrum of systems. You don't need to do individual certifications because those are surface level things that you will get below with that. I think something like this will help solve or breach that gap that we are pacing today.
**Scott:** There's so much that a software engineer has to know today. What of this material, or how deeply into this material, do you think people should have to delve just to reach the lowest bar in qualification to work in cloud or with Kafka or something?
**Unmesh:** In the book, we actually have divided it into two parts. That's very typical of patterns' books, I think. First section just gives the overview of the patterns, and it talks about all the problems and just a cursory view of how a particular pattern solves it, and then how they link together. To start with, I think it's easier to just get this broad view of what things can go wrong and how different implementations tackle it.
Then when you are working on something and maybe need to deep dive into one specific thing, then you can go and read a pattern that talks about that thing. That's the best way to use this, I think. Yes, because that's another aspect of pattern's book as well. I mean, you can't read it end to end. It's a hard thing to read, end to end. You have to focus on one thing and read it.
**Scott:** Given our limited attention spans now, I actually like that. I like that I can pick it up and absorb one thing and then put it down till the next time.
**Rebecca:** We did a [podcast about three years ago](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/patterns-distributed-systems) when you first started writing, what would you say is the major change in the things that you've talked about, from that first podcast to today? Was there one big section that you wanted to finish and that's been done in that time?
**Unmesh:** Oh, yes. Two major things. I think documented patterns of distributed time, that's a major chunk. Also detailed out things like Paxos and replicated log, which are foundational to any consensus mechanism used for replication. Those two are the major changes since last time we talked.
**Rebecca:** Have you soured on ever writing a book ever again? [laughs]
**Unmesh:** Yes, possibly. After some break that I need.
**Scott:** Will you be doing any workshops?
**Unmesh:** Yes. I'm doing workshops, four already, which I was doing once a quarter, I think, while I was working on the book. I will do more of those in future, I think.
**Scott:** I'm sure there's going to be an audience for it. There'd be a big demand for it. Some of the conferences that I've been to, I think people would be really interested. Anything else you wanted to say, Unmesh?
**Unmesh:** No. Just read a book and send me questions if you like. One of my hopes is that people will get questions and openly start talking about obvious things that might be missing from popular implementations. Yes. I like to use this term wise fool. Wise fool is someone, you know the story of Emperor's new clothes, and it's the key that says that the emperor is wearing no clothes, so when everyone was hesitating-- so we need more of those talking about obvious things and discussing them aloud.
**Scott:** Yes. I agree. Well, once again, congratulations. I think this is a huge accomplishment, and you should be very proud of yourself for having got through that. I'm looking forward to reading more of the book. I've read some of the patterns, but I'm looking forward to reading more of them, and best of luck.
**Unmesh:** Thank you. Thank you, Scott. Thank you, Rebecca.
**Rebecca:** Thanks for joining us.
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