<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/patterns-distributed-systems | Title: Modern patterns shaping distributed system design | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Patterns of distributed systems 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons and Zhamak Dehghani | Podcast guest  Unmesh Joshi and Martin Fowler
July 08, 2021 | 42 min 32 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/patterns-distributed-systems#transcript)
Listen on these platforms
## Brief summary
In today’s cloud-first world, distributed systems are everywhere. Unmesh Joshi gives an insight into his work looking at distributed systems — from distributed databases such as Cassandra to messaging brokers such as Kafka or infrastructure components such as Docker — the common problems that arise and the approaches to solving these problems, which he categorizes as patterns.
**Podcast transcript**
**Rebecca Parsons:** Hello, everyone. My name is Rebecca Parsons, and I am one of your regular co-hosts for the Thoughtworks Technology podcast. I am here with one of my other co-hosts, Zhamak Dehghani. Zhamak, say hello, please.
**﻿Zhamak Dehghani:** Hi, Rebecca. Great to be here. Hello, everyone. It's wonderful to be here. I've been waiting for this episode, so I'm super excited about what we're going to talk about.
**Rebecca:** Today, we are joined by two guests, Unmesh Joshi, who works with us in our India office, and Martin Fowler who has been on, of course, several of these podcasts. Unmesh has been spending a lot of time recently writing up several patterns of distributed systems. In this episode, we're going to review the approach that he's been taking for these, as well as talking a little bit about why this matters now. Let's start with talking about, Unmesh, why is this so important now, and what are you really trying to bring out about distributed architectures?
**Unmesh Joshi:** All right. Let's, first, maybe contextualize when we say distributed, what it means. When we say distributed, essentially, there are, you can imagine, multiple processes or multiple servers, ranging from three to few thousand. They essentially manage some data. They are inherently stateful. They communicate by message passing. That's the characteristic of when we call something as distributed. One of the important aspects there is that these systems, they need to be operational, even if part of the system is failing. Even if there are partial failures, partial network failures, or a few servers fail, as a whole from client's perspective, the systems are operational.
If you see around any project or program that's going on today, when you think of digitizing something, digital transformation and stuff, you see things from databases, like MongoDB, to Cassandra, Dynamo, HBase, Neo4j, to Postgres, and MySQL, at all times. Then you have message brokers, which are Kafka, Apache, Apex, Pravega, and many more.
Then there are infrastructure components like Kubernetes, Docker Swarm, Consul, Nomad, and those sort of things. To add to one level, there are platforms like blockchain or frameworks like Akka and not to forget, there are all these cloud providers providing various services.
Now, the challenge here, if you see now, all of these can fit into this definition of distributed systems. The challenge here is how to understand them all. You go and read the documentation, that's going to be very product-specific. If you go and read any book that calls itself a distributed systems book, it's way too theoretical. We need a way to understand common problems that the systems are trying to solve and their designs are trying to solve and their recurring solutions, because a lot of the solutions are very common. In databases to message brokers to things like Kubernetes, there are recurring solutions. If we understand these things that add these recurring solutions level and problems level, it's a lot better to be a professional developer today.
**Zhamak:** It's interesting you scoped the problem space that we're trying to understand and have solutions for as there are systems that are distributed across servers. A quick question around that, would you consider the distributed patterns that you're trying to address here applicable perhaps even to a single process, but it has some sort of a multithreading and stateful threads, and the synchronization problems still remain, but perhaps not with the reliability issues that you will have when you spread across CPUs and machines?
**Unmesh:** I think the key aspect here is message passing. When if you have things running in a single process and they still communicate with message passing, you can have embedded Kafka or embedded Zookeeper. As far as they are communicating with message passing, they will fit into this definition.
**Rebecca:** Again, in terms of scope, when I think about distributed systems, I think of two different axes or motivations, if you will, to distribute. One is that you have perhaps a disaster recovery scenario, and so you're going to have multiple servers. You don't really know where transactions are going to be run, but they're really not collaborating, if you will, to solve a particular end-to-end scenario.
Presumably, that's less interesting in this context, as opposed to something where you are using multiple servers to actually address some kind of end-to-end problem, and they have to communicate with each other, they have to coordinate their activities and collaborate to create something. It seems like the latter is actually more the kind of distributed problem that you're attempting to address. Is that a reasonable analysis?
**Unmesh:** Yes, that sounds correct.
**Rebecca:** You've explicitly used the Patterns Approach, and Martin, of course, you've done significant work looking at different kinds of problems as patterns. Can you talk through a little bit why patterns was a good approach for this? Why you think actually using patterns in this context makes sense?
**Martin Fowler:** Yes. There's like really many other aspects of a large, complicated problem domain. The first thing to struggle with is how to break it up into pieces, so that you don't have to understand in detail the entirety of a large problem area. Instead, you can say, "Well, I can have a shallow but broad view, and then dive down into particular detailed areas as I need them, rather than having to go through the whole thing in depth." It's a kind of modularity principle of software but applied to levels of knowledge.
I'm always looking for ways to break a big problem up into smaller pieces that we cannot entirely understand independently, but a greater degree of independence. The reason that patterns, I think, are particularly appealing for this, is that they focus on particular solutions to these recurring problems, right? In any distributed system, you're going to have problems because you're going to get state updates on different nodes that might not necessarily be able to coordinate, and you've got to figure out some way of figuring out which state updates occurred in what order. That's a common recurring problem, and there are well-known solutions to this kind of problem.
Focusing on these solutions is then a good way of diving down into this. Yes, I need to understand how to serialize these multiple updates. It's a completely different problem of deciding how to deal with service coming up and down and becoming part of a cluster or not. I can understand one of those with only having a hazy idea of the other. The point is that by focusing on these solutions, it gives you a way to break the problem up into these kinds of chunks.
Of course, part of the notion of patterns as well is that the solutions are not precise prescribed things with mathematical precision. They have this similarity to them so that you see the same basic idea in different places, that same basic solution. It's never quite entirely the same, but it has that similarity. Thus, if you get to know the pattern in one place, you can apply that knowledge to other places. In this case, you see a particular pattern for handling these ordering of different things in Kafka, you can apply that knowledge and say, "Oh yes, the Cassandra thing is not exactly the same, but it's similar." That recurringness of the solution is that ever-appealing part of patterns.
I think, say, the third thing that's important about patterns after the breaking the large topic into chunks and this focus on recurring solutions, is that we come up with a system of names for these solutions. Now, sometimes these names are out there in the world. When we talk about ordering of these different transactions, we often talk about these things called Lamport clocks, and that's a name that's out there in the world. A lot of people know about Lamport clocks already. Some of the names are fairly well known, but maybe not completely the case like high watermark, low watermark, leases are fairly well known.
Some might be particular to-- Well, we've got to coin them ourselves. When we talk about-- Unmesh is currently working on a pattern called version vector, which is somewhat used but not completely widely used. The point is, within the system of patterns that we're building, we construct a set of names who are consistent within this pattern family. Obviously, you want to try and use names that are well known out there, but sometimes, these names get a bit confused, so you have to pick on something and give it a greater degree of rigour than you might otherwise get.
Then, the last point that I would mention is that we also have this notion that patterns are useful but not in all contexts. When we talk about a pattern, not just do we explain how it works, we also explain when it's useful. Because most things are useful in some cases, but not in all cases. When we talk about patterns, we always try to lay out the context that makes them helpful and explain the context that you wouldn't want to use them, so that people can make an intelligent choice about when and where to use the pattern. When you're looking at some existing products and you're thinking, "Oh, why doesn't it have this?" The context will help you realize, "Well, maybe that is not the right context for this pattern to be in play here."
**Zhamak:** I would add one more to the why I love the pattern systems. As a user I think that, let's say, you're solving that complex problem, it gives you a really nice experience of discovering solutions to various problems that you come across, because you've got this now wonderful taxonomy to look for and find the solution to a problem, like you're looking at-- I remember from The Gang of Four books on the object-oriented design patterns, I know I'm looking at a behavioral pattern or a structural pattern, or if I'm looking at networking or distributor system patterns, I'm trying to find the synchronization patterns or concurrency patterns.
I have these tagging systems on the taxonomy that helps navigate your way across a large body of information and just find the one that is relevant to this moment apply to you, and they also make wonderful bedtime reading as well because before you fall asleep, you get to read one pattern, which is was what I was doing last night reading Unmesh patterns.
**Unmesh:** Yes, I would like to just add to that an aspect, that the patterns show real code. For me, I think that was the most important aspect of this work, because some of the names, and system of names is a very powerful thing, and more so if you can attach real code to that name and you understand in very concrete terms. If you take an example of a Lamport clock or just something as commonly known as write-ahead log, if you know maybe how a Java code in a database for Lamport clock looks like or write-ahead log code how it looks like, then when you read those names, you don't need to imagine things, you know what might be going on underneath these systems. That's, I think, for me the most important aspect of this.
**Rebecca:** This to me, also is one of the distinguishing features of the approach that you've taken, not just using patterns but how you're actually talking about the patterns and drawing on real implementations, because of course, many of these approaches have been around for a long time. I studied them back before fire was invented, when I was a professor and taught them. Yet, as you pointed out, in many cases, you just see the basic idea, the concept. Well, of course, you have to do concurrency, but actually, making some of these things work is hard. What is it that actually inspired you to describe these things from the perspective of actual open source projects? Where did that idea come from?
**Unmesh:** I can remember a few years back when I was working on a big digital transformation project, and we were using all the so-called modern tech stack. We have Cassandra, Kafka, Kubernetes, and whatnot, Akka actors, and everything. I was always trying to figure out-- All these things, when I read their documentation and try to understand how they work, there are similar-looking things in there. I don't really know. If I go and maybe look at Kafka source code, I don't know where to start and how to understand what's going on in there.
When I tried reading books, I couldn't map to what-- Let's say, if I read Kafka's code and read about write-ahead log in a book, I couldn't map those things to together. What I decided to do was create my own miniature Kafka. I actually tried to build a boot camp around that. Well, maybe if I set a target to myself, but if I can almost test drive a Kafka like implementation so that I solve small problems at a time, but then I plug them together to have a system like Kafka, maybe just as an attempt to understand what's going on at the code level. When I did that, it actually worked really well. I have these 14 or 18 test cases, which if you make them pass one by one, you have something like Kafka. A miniature one, not a production-ready system.
Because that worked really well, and when I was talking to people and run this boot camp where people could be in a few days of Kafka-like system, it's then that this idea of actually reading code and trying to figure out how to build that kind of a code step by step, that struck me. I'm going to talk to Martin about it when he give me this idea of building this with patterns or a system of patterns. That worked really well, I think.
**Martin:** Yes, one of the defining features it was seen of patterns from the beginning was that you should look at existing things and draw the patterns out from existing stuff. Often, there was this term that was around saying that you should see at least three examples of something in the wild before you can consider it a pattern or something of that kind, which I never felt was an absolute rule, but obviously, if you can look at existing systems and identify the patterns for multiple of them, that obviously is the best way to go.
One of the nice things about the open-source world is that you can actually do that. You're not faced with products that are opaque, instead, you can actually look at the code. Now, it doesn't mean that Unmesh has had to teach himself Erlang and struggle with C++ builds that take a ridiculous amount of time. It's certainly interesting in terms of language expansion that's been going on there. Again, with the source code, you can get a degree of understanding that you can't get from even the well, best-written technical documentation. The code gives you that level-- I've often said that code is like the mathematics of our profession. It's where we have to remove the ambiguity. We can't skip over any details. We have to be absolutely precise. That's why it's great to have code examples, and that's why it's great to have code sources for the patterns as well.
**Unmesh:** Right. I think that's the beauty of pattern structure because as Martin mentioned, the systems we looked at, the source code we looked at range from C++, to Erlang, to Scala, to Java, to Golang. The examples we are giving are applicable to all of them, irrespective of the programming language or the type of system it is. That's really beautiful, I think.
**Zhamak:** It's interesting. You went, can I ask why, what was the inspiration? You came from the point of understanding how Kafka works or how Zookeeper works. I'm really excited about your work because I feel like these patterns of distributed programming, it's actually a lost art. I have a hypothesis why it's a lost art, and I wonder what you guys are thinking. My hypothesis is that unless you're a person, a developer who's building the Zookeeper, who's the building the Kafkas, you deal with these problems, you have to know these patterns, but there's a majority of developers that have started working above those layers.
With the introduction of HTTP, the moment we went away from from writing bits and bytes that you have to synchronize and do design your messaging at that level, to passing a whole message and assume that protocols take care of the reliability of passing that whole message. The moment we went from consistency of our stateful services to eventual consistency of our stateless services.
It feels like as we moved higher up the stack and we built this distributed systems as micro services over internet, that push a lot of those complexities of distributed systems and resiliency of this down to the infrastructure, to the service meshes of the world, to the databases of the world, to the Kafkas of the world, the day-to-day programmer, like everyday program doesn't actually realize what's going on underneath, and they don't have to even deal with it for majority of the cases. I'm curious as what is the persona of a developer that should be reading this and is this relevant to everyone, or is it just relevant to people who need to understand or write Zookeepers?
**Unmesh:** No, I think my view on this is that it's relevant to everyone, because if you see the example systems that we looked at, it's like every project that we do as a software professional has one of those. As an industry, I think, what happens is that when we don't know how to how to understand all of this, we move towards super specialization. That's very visible today, and you know these cloud providers pushing for certifications or very specific product expertise, like you need a Kafka expert, you need a Kubernetes expert, and that kind of stuff.
What this patterns approach allows, in my opinion, is to have expert generalists, people who understand things at deeper level and can move across these technical specialties or technical domains. The other aspect of this, I think, is related to how services engages with a product organization, like how me as a software developer working on a project using Confluent Kafka or using AWS services, how do I engage with them? Do I understand enough of details to engage in a meaningful conversation, or I just rely on them to solve all my production issues? At that level, I think, and I like this term expert generalist, people who know core fundamentals so well that they can move between data engineering to infrastructure world seamlessly.
**Rebecca:** I think there's also something to do with the complexity of the problem. As our hardware has gotten faster, our techniques have gotten more sophisticated, personally, I think our architectural choices expanded significantly when we started having things disciplined like continuous delivery that helps simplify in day-to-day operation, the deployment of some of these more complex architectures, but we're also trying to solve more complex problems. We are addressing problems now that we simply did not have the compute capacity to solve, but there are still a lot of very simple problems out there that people are trying to solve.
If you were someone who was just trying to write a very simple application, perhaps it's not that relevant, but the way we're pushing on compute the problems that we are trying to solve, and not just the kinds of things that our engineering for research group is doing with radio astronomy and all of that, but in traditional transaction processing systems, and business risk analytics, and all of these things, more and more problems are going to require a distributed solution. Debugging these things, particularly when the problem is not well understood, to me, you have to have some level of understanding of, okay, what is the system, this architecture, this foundation that I'm building in? What is that doing to help me understand how I can actually properly solve the problem that I'm trying to solve?
We still haven't created those perfect abstractions that will never leak into our code. The more complex the code you're trying to write, the more likely those abstractions are going to leak into that. Having something like this that doesn't require everybody to spend the time that you had to spend, Unmesh, looking at the Kafka code and all of this to figure it out, to me, I think we do have a large class of software development professionals for whom this is relevant. Even though I will agree that there are going to be some people who probably never have to think about it, but I think the problem set that we're trying to address is growing to the point where it is more and more people are going to have to deal with this.
**Martin:** Yes, the curious thing about this is, I never want to write or care about a distributed system. I never want to build a distributed system. I want to solve business problems. Business problems are not something that inherently wants me to make a distributed system to solve them, but I'm often forced to use a distributed system because we want a degree of availability, a degree of performance, a degree of geographic-- There are other things that force us towards a distributed route.
When we're forced to the distributed route, weird things can happen that just don't happen on a monolithic system, and we have to be able-- Even if I don't want to be a distributed systems expert, I've got to have some appreciation of what's going on in that distributed system, so that when those weird things happen, I can go, "Oh, yes, I know what's happening here," and I can begin to have some appreciation of how to debug that or what kind of code I need to write to work around that. I need a certain degree of knowledge when I'm forced into that distributed system world, but we have to remember a lot of this stuff is stuff that if at all possible, you should avoid.
Unmesh and I were joking about how we've both been involved in writing patterns for stuff where we try to want to say to people, "Don't do this. Don't work in this area." I had it with object-relational mapping. "You don't want to write your own object-relational mapping system," but even if you don't, you have to understand enough of how they work to appreciate how to use them well, how they can go wrong, because sometimes, you can't avoid them.
I think distributed systems are like that, but more, much more pervasive than object-relational mapping systems. We can't avoid writing distributed systems these days in so many areas, and so we have to appreciate the kinds of problems they deal with, and what kind of behavior that manifests to what we would like to be a simple business application.
**Zhamak:** Yes, I really like the phrase expert generalist because I always liked the word generalist, but now, being an expert generalist so that you can have the appreciation, as you said, Martin, you can understand it, even though the trend of industry, the way we see it that reusable problems get pushed down into reusable solution, and then abstracted away, and that opportunity to actually understand what's underneath that abstraction also disappears with that, but as an expert generalist, just keep yourself refreshed and understanding.
**Rebecca:** Unmesh, we've been talking a lot abstractly about patterns, and distributed systems, and all of these things, let's get a little more concrete. Can you talk us through a couple of the specific patterns that you think are important and that illustrate the approach that you're taking, as well as the ways that people can make use of these patterns as they are developing systems?
**Unmesh:** All right. Yes, I think one of the most fundamental patterns that a lot of people know about, at least the name, is that of write-ahead log. Write-ahead log, if you have to now understand this in terms of problem-solution structure, what a write-ahead log is, or the problem that it's trying to solve is essentially if you have a server failure, you need to preserve all the data that's saved on that server without incurring the cost of flushing all that state to the risk for every write, because that state might be spanning across multiple files. There might be data files, index files, and many other things.
The common solution to this then is to store each state change that comes to a server as a command, as a serialized command in a file on a disk before you actually make that state change in your data structures. You maintain this single log where you keep on appending. This is like append-only Log, we keep on appending all these commands. You provide a unique identifier, which is monotonically increasing to these log entries. This is the most fundamental pattern. If you can see on the patterns page that we have on Martin's side, there is a code snippet, a very simple key-value store, how you can build that with a write-ahead log.
At core, you have this write-ahead log as a most fundamental pattern. When you maybe now look at a system like Kafka, you have to really make this write-ahead log distributed. You need a way to replicate this write-ahead log. While replicating, you also need to give some guarantee of consistency to the clients. Then this problem of replicating as well as giving some guarantee of consistency, you need someone to make that decision when to make a particular write visible to the clients. This is where then a common solution to this problem is how one of the server's elected as a leader, and then the rest of it becomes as followers. Then leader takes the decision on when to make any change visible to the client.
If you see, you can now plug these patterns together. That's the beauty of these patterns. As Martin mentioned some time back, the system of names, that you can describe these larger architectures like Kafka in terms of this pattern. You have durability guarantees with write-ahead log. You replicate this write-ahead log on multiple servers using leaders and followers. You use quorum to update something called as high-water mark, and that defines what entries can be made visible to the client.
You also need some ordering maintained while the data is transmitted over the network. This write-ahead log is transmitted over the network, and then a common solution to this is to use a single socket channel between servers. You need to know if the leader is alive because if it's failed, you need to select someone else as a leader. The common solution to that is to have a leader sending a heartbeat periodically.
Then there is this interesting problem where if you have a zombie leader, like for the rest of the cluster, it's failed, but from that leader's perspective, it's still alive. Then you have something called as a generation clock. Every generation of leader implements this clock so that you can detect if you are getting requests from older generation leaders. If you just now look at what I just described in a paragraph, our set of patterns that are a wave together, but this is actually what an architecture of Kafka or even some of the algorithms, the keras or Zookeeper or Zookeeper ZAB look like at the implementation level.
**Zhamak:** Yes, I think Apache Spark as well, like their claim about zero data loss and fault tolerance is using these patterns. Martin, I'm curious if you have any favorite patterns out of the ones that Unmesh has written?
**Martin:** Oh, I don't have any real favorites here. As Unmesh said, they weave together a good selection of things that we have been using for a long time but need to be described a little bit better. I'm afraid, no favorites. It's not like going around an art gallery. I don't feel I can pick one out.
**Rebecca:** Then how would you suggest the average software developer who wants to become this expert generalist--? Obviously, you'd have them start or utilize the resource that you're putting together on Martin's site, but do you have other suggestions for where people can go to really get their hands around or they really get their heads around these patterns and the problems that they're trying to solve?
**Unmesh:** I think one of the great sources is to go through the source code itself. Unfortunately, a lot of these systems are open-source, and they do openly discuss their design. Like one of the recent major architectural changes that Kafka did moving away from Zookeeper's have their own route for this code. There were open discussions about their design choices on their mailing lists. Getting involved in that and going to the source code, I think, is very, very valuable.
**Rebecca:** Sort of mimicking Zhamak's question a little bit, given all of the systems that you've looked at, which was your favorite source code to look at it and used as you were developing these patterns?
**Unmesh:** Actually, some of the earlier versions of Kafka, and even Zookeeper and Cassandra, I think, they were all good, even React, the Erlang code that I looked at, I struggle with Erlang a bit. I started with Kafka, so that remains my favorite one. Now it has become a lot more complex, but some of the earlier versions were a lot easier.
**Rebecca:** We've been talking about these patterns that help us to address some of the inherent complexities of distributed systems, can you give us one example of how these patterns actually work to take care of some of these issues with, for example, the zombie leader that you pointed out or some other concrete example of how these patterns actually resolve the issues that arise from the operation of distributed systems.
**Martin:** I think take an example of this, one of the things that we commonly see in distributed systems is the idea of a leader and followers, where you have one node that acts as a leader. One of the valuable things about doing this is that way, when you're doing updates, you're making rights, the leader is able to make sure these rights are correctly ordered and applied to the system. Then the reader passes out that information to its followers, and if I'm only interested in reading data, I can talk to a follower. I've got obviously much better availability and performance as a result of that.
What happens when I send a right to the leader, and I get an acknowledgment that the leader has received the right, and then the leader crashes. I now go-- Actually, let me take that back. Is that the best word--? I was thinking of what I'm thinking-- The trouble is in my mind that the patterns we're currently working on.
**Unmesh:** I think that's fine, Martin. I think because high-water mark is something that solves at least... because you go to the leader and leader writes something to its own log. Then it replicates it to the follower, but what if leader fails right there before that change goes to the follower? What happens to the plan? Now because from client's perspective, maybe if it can wait and get a failure that leader has failed, but what if this leader comes back again? It was zombie leader, it has not completely failed, but paused, because it has this now conflicting entry in its log because it wrote to its log, and client might have now because it got a failure that leader failed, so it kept retrying and it went to now a new leader that was selected from one of the remaining followers, and then it keeps writing these new entries.
This old leader now, which was probably not crashed completely, it needs to, as a system as a whole needs to do two things. One, the leader should realize that it was disconnected from the rest of the cluster and it's no longer a leader. That's where this concept of generation clock comes in. That any request that a leader sends to its followers, is always marked by the generation for which that leader was linked. This is a very common concept like in raft algorithm, there is a concept called a storm, but if you see Kafka, there is a concept called epochs. There are various kinds of epochs in there.
If this leader comes back up again and tries to send messages, they will be rejected. This leader then knows that I was the data follows life generations, and then it becomes a follower. That's the problem that is solved by an implementation of epoch or generation clocks, or they're also called as fencing tokens.
The other challenge this leader has is to know if it has any conflicting entries in its own log because it always happened that whatever clients gave it before replicating. That's where this concept of high-water mark comes in, that any communication that or any entries that a leader makes visible to the client are always entries for which it has guarantee that they are replicated in a quorum of servers, and anything beyond that might be a conflicting entry.
When this old leader comes back up, it can very well ask the new data for what is the latest high-water mark and discard all the old entries or conflicting entries that it has, and then it again, comes back in sync with the system now in a correct state. There's two patterns, this high-water mark and epochs or generation clocks. They help solve this partial failure that we probably had with leader either pausing, or going down, or getting disconnected.
Again, because this is a pattern, you will see this not just in Kafka but everywhere, this concept of generation clocks to detect stale leaders or stale servers. It's everywhere. It's even in Cassandra's gossip protocol. That's again, the beauty of it. Totally outside of leader-follower context as well to detect a stale server is done the same way.
**Rebecca:** Well, another fascinating discussion of some of the more systems aspects of the applications that we're building these days. I would like to thank Martin Fowler and Unmesh Joshi for joining us today, and I'd like to thank Zhamak Dehghani for being my co-host. Thank you all for listening to another episode of the Thoughtworks Technology podcast.
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