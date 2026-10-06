<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/three-new-fallacies-distributed-computing | Title: The three new fallacies of distributed computing | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The three new fallacies of distributed computing 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Prem Chandrasekaran | Podcast guest  Neal Ford and Mark Richards
June 26, 2025 | 46 min 56 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/three-new-fallacies-distributed-computing#Transcript)
Listen on these platforms
## Brief summary
Back in 1994, Peter Deutsch and his colleagues at Sun Microsystems identified what they described as the "eight fallacies of distributed computing" — flawed assumptions that often get made when teams move from monolithic to distributed software architectures. In recent years, software architecture experts and regular writing partners Neal Ford and Mark Richards have identified a further three new fallacies of distributed computing:  _versioning is easy_ ; _compensating updates always work_ ; and _observability is optional_.
In this episode of the Technology Podcast, Neal and Mark join host Prem Chandrasekaran to talk through these three new fallacies, before digging deeper into other important issues in software architecture, including modular monoliths and governing architectural characteristics. Listen for a fresh perspective on software architecture and to explore key ideas shaping the discipline in 2025.
**Learn more about the second edition of Neal and Mark's _[Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)._**
## Episode transcript
**Prem:** Welcome, everyone, to yet another exciting episode of the Thoughtworks Technology Podcast. I'm Prem. I'm one of the regular hosts on the podcast. Today, I've got with me two of our almost regular guests now, Neal Ford and Mark Richards. Do you folks want to quickly introduce yourselves again, please?
**Neal Ford:** Sure. I'll go first. I'm one of the regular hosts as well, but I'm also a frequent guest, and that's the role I'm playing today. Prem's putting a lot of pressure on us, claiming upfront that it's going to be an exciting podcast, and we'll see if we can deliver on that. I'm joined, as I often am, on the podcast with my co-author and frequent collaborator, Mark Richards.
**Mark Richards:** Hello, everyone. My name is Mark Richards, and I am, in fact, seems like, now, a frequent guest on the Thoughtworks Podcast. Thank you so much again for having me on yet another podcast.
**Prem:** Excellent. What are we talking about today? You folks are writing yet another book, and this time, it's the second edition of your Software Architecture Fundamentals book. What's the motivation for you folks to write the second edition?
**Mark:** In fact, it's already published. We did finish that up at the beginning of the year, and it was released in, I believe it was April, Neal. Is that correct?
**Neal:** That's correct. Just a couple of months ago, as we record this.
**Mark:** Software architecture does remain more stable, I will say, at least as a field, than other areas of technology. However, that said, it does change. Neal and I were reviewing our book, The Fundamentals of Software Architecture, the first edition that we published in February of 2020, and realized there actually were some things that changed in software architecture that we did not include in the book, and felt like it needed an update because of that.
**Neal:** Part of that came, in the interim, we collaborated with Raju Gandhi and wrote  _Head First Software Architecture_ , and as we were revisiting the subject again, we realized that there were some deficiencies in the original source material because the  _Head First_ book covers about a third of what the  _Fundamentals_ book covered. It also covers some things the  _Fundamentals_ book didn't cover, like one of the things, to Mark's point, that has become notably more popular in the intervening time, are modular monoliths as an architecture style.
We only, passingly, mentioned those in the first edition, but they got a proper full treatment for their own chapter in the second edition, just like they did in the  _Head First Software Architecture_ book. That's just one of the many changes that we were reacting to in the ecosystem.
**Mark:** One of the other aspects that we didn't touch on a lot in the first edition was the aspect of data within software architecture. We did add quite a bit, especially within the part two of the book where we talk about the architectural styles. We did add full sections on data implications and data topologies within each of those architectural styles we discussed in the book.
**Neal:** I think, in the first edition, it wasn't so much that we didn't talk about data. We just didn't talk about it consistently. Some of the styles, we talked about data like microservices. Data figured heavily in service-based architectures, but then we hardly mentioned it in layered architecture. We realized, and that's one of the other things we wanted to fix, one of the things that when you write a book like that, one of the great things about writing a book is, when it's done, it's finally done, which is a great relief, particularly for this particular book, which is quite the effort to get done.
Then it's very static. When you see things in it that you don't like, it's hard to fix because it's done. It's very frustrating when you're used to software because software is very soft and books are very, very hard compared to software. You can change the electronic version, but it's much more difficult to change the entire chunk of IP. Over time, we became frustrated. One big part of our book is the second section, which is a catalog of all the architecture styles.
For all of those styles, we have a bunch of prose about how they're different, and we compare them with some charts, et cetera. The sections in all those styles weren't consistent because we were just talking about the highlighting features of those styles. Then we realized, well, that leaves a gap for questions. How does this style handle the highlight from this other style? We made the styles much more like a catalog, where every style chapter is rigidly consistent in terms of the sections that it covers, and it covers every aspect of every one of the styles.
Great example of that, of one of the ecosystem changes, was we didn't have quite the nomenclature to understand the impact of team structure on architecture until team topologies came out. That gave us a great lens to think about that intersection. Every style now has a section that talks about how well does this align with some of the ideas and team topologies as a way of distinguishing those architecture styles.
**Mark:** Also, we didn't really touch, on the first edition, about some of the common risks associated with each of the architecture styles. We did do the quantitative analysis in terms of the star ratings of what it's good at, what it's not good at, but there were other orthogonal risks associated with some of these architectural styles, which we did add in the second edition, along with some governance techniques. How do we govern some of the aspects of these architectural styles?
Also, what are some of the cloud considerations with these architectural styles, and when to use them in cloud and when not to? Those were some of the additional things we added in part two of the book.
**Prem:** One of the things that you mentioned are the new fallacies of distributed computing. What are some that stand out for you, and can you tell our listeners why they matter today more than ever?
**Neal:** When we thought about this podcast, we did not want to just make it a "What's new in our second edition," because if you're not interested in buying a second edition of our book, then it's not a very interesting podcast episode. We thought we'd talk about some of the things that we added to the book that may be useful as a standalone. One of those was something that, since the book came out in 2020, we've gradually been building on over the last few years and finally wrote down in the second edition.
That's what we're calling the new fallacies. I'll give the background and then let Mark talk about the new ones. What we're riffing on here is, back in the 1980s, I think, Peter Deutsch and some other folks at Sun Microsystems put together a very famous list of the eight fallacies of distributed computing, which has its own Wikipedia page now. It's all these silly assumptions you make when you move from monolithic to distributed architectures, like bandwidth is infinite and latency is zero, and the network is homogeneous.
I tell people that are new to distributed architectures, you should really study that list that Peter Deutsch created because you'll learn them one way or the other. You'll either learn them by reading the list or you'll painfully learn them one at a time as part of your professional career. I think reading the list is an easier way to learn them, but you can do whichever you prefer to do. That's the background.
Then Mark and I have talked about these so long, and we've also talked about distributed architectures like microservices so long that we realized that we've identified some new ones. We've, a little tongue in cheek, started adding to the eight, and we've come up with three more that we finally documented in the second edition of our book. We've been talking about these live for quite a while and figured it was finally time to document them. I'll let Mark start talking about the new fallacies that we've come up with.
**Mark:** These fallacies really were born out of what Neal was talking about in terms of lessons learned and experiences [laughs] just like the original eight were. Our first new one, fallacy number 9 is versioning is easy. Just version it. It might seem like it's easy just to simply version a shared library or version an API or a service. There's a lot of complexity that both Neal and I have experienced with versioning any sort of software or artifact.
One of those first complexities is when you make a version change, how do you communicate that version change to all the users of either your software or that particular software artifact? How many versions should you maintain of a particular artifact? If I have a shared library, a JAR file or a DLL or a jem, should I keep out three versions, four, 10? What about an API that maybe the public is using?
Then the third complexity we identified was, if I want to deprecate a version, what is my deprecation strategy? How do I communicate that deprecation to the many teams and users using that particular artifact or API? Also, what if I need to deprecate a version due to a breaking change, something that's no longer supported, and I have a team using that particular artifact that says, "Well, we're in a three-month code freeze, we can't change"? These are the inherent complexities involved with versioning, and not just simply determining the versioning numbers or whatever the dot notations are.
**Neal:** It's also the scope of deprecation. Is it per service? Is it per domain? Is it per API? Is it per system? It's one of those things that's like, "It's an easy solution. Oh, just version it," and then suddenly you realize that you're falling into a tar pit.
**Prem:** Definitely, versioning is not easy.
**Neal:** Exactly.
**Prem:** That's number one. What are the other two?
**Neal:** The second one I'll talk about. Every time you see a presentation about microservices, and they're talking about transactional workflows in microservices, traditionally known, or colloquially known as SAGAs, they talk about the role of, what if you can't rely on a database to do a consistency for you? You have to implement eventual consistency. One of the patterns that you use to do that is have some mechanism, either an orchestrator or one of your domain services. After you've found an error, issue a compensating update to fix up the ones that you've already fixed. You can bring back a consistent view of the world.
If there are three services involved in a transaction, you're able to update the first two, but you can't do the third one, the role of the orchestrator in that case would be to go to the first two and tell them, "Roll back your changes so that the whole world looks consistent from a workflow standpoint." That's known as a compensating update in the microservices world.
That brings us to our second fallacy, which is that compensating updates always work. When you see somebody do a presentation of microservices, at some point, they wave a magic wand and then say, "Oh," then a compensating update occurs, and then everything is back the way it was before. Then they never talk about, "Well, what if the compensating update fails? There are really two different error scenarios that bring up a lot of interesting side effects and boundary conditions, et cetera, that you have to take into account when you build systems like that.
We don't like those magic wand that sweep complex things under a rug, and that's definitely one of them. That's the number 10, which is compensating updates always work, because they don't, and when they don't, it can get really messy.
**Mark:** Then we have a third new fallacy, fallacy number 11, which is, in distributed architectures, observability is optional. This was born out of frustration of both of us experiencing the fact that observability is not treated as a first-class citizen in a lot of the systems we work on. In fact, it's a last-minute thought or a bolt-on after all the functionality is done. In fact, this fallacy points to the fact that observability is not optional, and it should be treated as a first-class citizen to be able to analyze both the operational aspects of a particular system as well as the non-operational or process aspects of that system.
Without observability, we have no insights into whether we are scaling, whether we're scaling but tomorrow we won't be. Those are just examples of some of the operational aspects. This fallacy, we both feel, is very key and important for those working, especially in distributed architectures, to really understand what data we need, where do I get that data, and how to validate all of the capabilities of that architecture, both operational and non-operational.
**Neal:** The other thing that we added to the second edition of the book was we updated, really just added to, didn't change the laws of software architecture, which, again, were a little bit tongue in cheek in the first edition. When we were writing the first edition of the book, we were quite ambitious, and we thought, as we go through all this material, we're going to see if we can identify things that seem universally true throughout software architecture, and we'll call those the laws of software architecture.
We were hoping to find 10 of them, and we found two in the first edition. The first of which was that everything in software architecture is a trade-off, which we still stand by, and that has survived quite nicely. There was a corollary in our first edition that, if you think you've found something that isn't a trade-off, you likely just haven't identified what that trade-off is yet. In this second edition, we actually added a second corollary to the trade-off law, which is, you can't just do the trade-off analysis once. For complex problems in software architecture, it's always about trade-offs.
It would be nice if you could just go into an organization and take a complex problem and just think really, really hard about it for like two or three days, and do the trade-off analysis one big time, and then be done with it forever. That's what we're going to do for the rest of time. The problem with a lot of software architecture decisions, though, is that there are a lot of variables involved.
Those variables are always slightly shifting and changing. One of the examples we give in our book is, "Oh, shared library or shared service." You can come up with this whole list of pros and cons. Then every time you make that evaluation, some of those are going to change. How many platforms are you supporting? What volatility can you support? Et cetera. Really complex questions in software architecture.
It would be nice if we could make one decision about orchestration versus choreography, or mediation versus brokering, or shared libraries versus services. Every time we encounter those situations, there are enough differences present in our ecosystem that we have to respond to them differently every time.
**Prem:** Another thing which is very important that you cover in this book is this aspect of measuring and governing architecture characteristics. Can you shed some light on what you mean by that, why it matters, how you can do it?
**Mark:** Boy, we can probably fill up seven Thoughtworks podcasts with this topic. It follows on that 11th point we talked about with the fallacy of observability is optional. This is one of the reasons why we created the fallacy, because it's not optional, and it leads to the measuring and governing of architecture characteristics. It's interesting. We talk about mostly governing operational characteristics of an architecture. Things like scalability, responsiveness, fault tolerance, availability. Those are four key ones that we do have a lot of observability tools and platforms that tend to measure those aspects.
However, in the second edition of the book, we really took a step beyond just the simplicity of those kind of measurements of architecture characteristics, and looked at other aspects of an architecture or architectural style that we govern and measure as well. Let me give you a great example, and then I'll let Neal give some examples. Let's talk about event-driven architecture.
Event-driven architecture, we may choose for its high levels of scalability and fault tolerance and responsiveness, as I mentioned before. There's other aspects we added to the book in terms of governing these kind of architectures. For example, with event-driven architecture, we rely on asynchronous processing, with highly decoupled services that trigger events and then respond to those events.
One of the things we can actually measure and govern is the amount of static coupling that we have within services in an event-driven architecture. That static coupling can be in the form of event payloads, the rate of change of an event payload. When we change the payload of an event that's being triggered, it may be responded to by dozens of services. When I implement that change, I can potentially break all 12 of those services, making my highly decoupled event-driven architecture quite brittle.
This is one out of many examples where we start talking about the structural aspects in terms of the governance—for example, in mine here, coupling—as a good example of something that we tend to forget about when we start focusing on operational characteristics. These things are just as important as those typical operational ones from a measurement and governance standpoint.
**Neal:** Yes, that's another thing that we made more consistent in this book. We had, in the first edition, a chapter about governance, and we still have a chapter about governance here talking about automating with architectural fitness functions using tool like ArchUnit or NetArchTest or tools like that. Then, for each one of the styles, we also talked about the particular challenges of governing those styles.
Mark mentioned some of the challenges in event-driven architectures. We mentioned some of the challenges in modular monoliths and layered architecture. That's another thing we want to make more consistent because, well, Mark and I are on a bit of a crusade here to try to reclaim the governance word in software architecture because it has such a bad reputation because, for so long, it meant mindless bureaucratic things that don't seem to add any value, but just a punch list of things that are annoying.
It doesn't have to be that. The real idea behind it is not only do you define these important capabilities of your architecture, but you should be able to govern them, to measure them, to see, are they still true, and to test them. That's the essence of agility in architecture is fast feedback. I did a change, we just made, did it break something? How quickly can I find that out?
That's really the aspect of governance that we're trying to attack here and trying to shine a light on each of these styles. All these generic styles, they all have pros and cons associated with them. Given that we've made an intelligent choice, there are still negative aspects of this that we have to mitigate. How can we do that via governance?
**Mark:** I want to also provide another good example because Neal, you mentioned an entire chapter that we added to the book on the modular monolith, which has become quite popular as a choice of a monolithic style, either as a stepping stone for distributed architectures in the future or even near future, or as a final resting place. When we start talking about governance and those kinds of things within a monolith, that structural aspect can-- well, the importance of it is the success of that architectural style working.
For example, a modular monolith is broken apart or partitioned by domain, or specifically within this architectural style, a module. What we do is we delineate our functionality by domain or subdomain represented as a module. There's three kinds of governance and measurements that we can take on a modular monolith to ensure its success outside of all the characteristics that we've identified. For example, does all the source code inside our modular monolith adhere to the specific modules we identified and those corresponding domains? That's one.
Another way we can govern is the amount of communication between those modules. This is such an important measurement and governance because we want those modules to try to remain as independent as possible. We do get times where they do communicate. If our modules, the way we delineate this modular monolith, are all communicating too much, what that usually means is we have not delineated our domains properly or not partitioned our architecture properly based on those types of modules and what they represent.
These are just forms. Oh, a third might be even the independence of each of the modules. How much do they need to communicate? These are all structural-related governance and measurements that provide yet another example of what we added to the book to really help architects understand these architectural styles, but also appreciate the need for measurements and governance within every one of these architecture styles.
**Prem:** One more thing that was pretty intriguing, which you talk about, which is usually not discussed that often, is the scope of architectural characteristics. You talk about this thing called the architecture quanta, which was, I think, originally introduced in the Building Evolutionary Architectures book. I think you dedicate an entire chapter to this. Can you talk about what you mean by that, and again, why it matters?
Neal: That started in the  _Building Evolutionary Architectures_ book because Rebecca Parsons, Pat Kua, and I, part of the-- That book is primarily about this idea of architectural fitness functions, which we call the mechanics of building evolutionary architectures. We also wanted to address the structural question of given the generic topology of an architecture, like microkernel versus microservices or layered architecture versus microservices, are some of the structures inherently more evolvable than others? If they are, why?
That was the original motivation for this quantum idea, which was closely aligned with a bounded context, but in an architectural sense. It more or less defined a bounded context, but from an architectural standpoint. That was sufficient for the evolutionary architectures book. It was also quite influential on Zhamak Dehghani on her thinking about the way data mesh works. She credits this quantum idea as a way of consolidating her thinking about the scope and boundaries of things in distributed architectures.
Then, as time has gone by, we've realized that this is a really useful perspective. We've done a lot more fleshing out of this idea. We actually ran across, as we were writing software architecture, the hard parts, this book called _What Every Developer Should Know About Object-Oriented Design_ by Meilir Page-Jones, which is a book from 1993. Mostly a book about an object-oriented analysis design technique that nobody outside the author and a handful of other people ended up using. He also defined this concept of connascence.
If the people listening don't know what that is, there's a website called connascence.io that highlights connascence. It's really a language that describes coupling. I won't go into all the details of that.
**Mark:** Good luck spelling it [laughs].
**Neal:** Yes, it's C-O-N-N-A-S-C-E-N-C-E, I think. You'll be able to Google around and find it. That's really a language that describes levels of coupling. I won't go into that. It's a useful exercise. The other thing he identified that we found quite useful was this distinction that Mark was alluding to of static versus dynamic coupling in a distributed architecture. We tell people who come to our class that when they come to our class, you came in with one term for coupling, which was just coupling, and you're going to leave with at least two, which is static and dynamic.
Static coupling is how things are wired together, the dependencies of things. If I need to bootstrap this service, what dependencies need to be there? Broker, database, et cetera. Those are the static dependencies. That also helps define a scope for a set of architecture characteristics. That's what this quantum idea has really become is a modern way of assessing the scope for a set of particularly operational architecture characteristics.
If I have a single database, that's going to determine the level of scalability and responsiveness that I'm going to have in this particular service. That defines a scope for those operational architecture characteristics. Then the dynamic side of that also defines what happens in distributed architectures. Let's say I have two services running, A and B, and A is running at 10 times the scale of B. What happens when they start calling one another in a distributed architecture? If A calls B synchronously, what happens?
A's performance drops down, the responsiveness drops down to what B's is because it's blocking and waiting for the response from B. That's what we refer to as dynamic entanglement in a software architecture. In microservices, this is a reality because one of the selling points of microservices is that each service can have its own set of architecture characteristics. Therefore, each service may have a different level of scalability and responsiveness and elasticity. That dynamic entanglement is something that you have to analyze. It's easier with asynchronous communication, but that's the impact of synchronous versus asynchronous. That's this whole idea.
That's why we ended up dedicating an entire chapter to this because it's a really useful way of analyzing some of the most difficult issues in distributed architectures by separating, coupling into static and thinking about dependency separately from what happens once I've resolved my dependencies and these things have to start communicating with each other. Like many complex problems in software, decomposing it into two slightly simpler problems allows you to understand it a little better.
That was the motivation for that entire chapter. That's one of the things that's been confusing people for a long time because it is an abstract concept. One of the things that we really wanted to do in the second edition was to try to flesh that out in as expansive a way as we could. It expanded quite a bit, including a few word salad. It was an attempt to create as precise a definition as possible. Some of the phrases got long to become more precise. I think, at the end of the day, it makes a lot more sense now. I guess our readers will ultimately let us know about that one way or the other.
**Prem:** Great. The next topic that I wanted to cover was on architecture styles. You covered a variety of them, but a couple that may not be as popular. For example, you talk about space-based architectures. What exactly is space-based architectures? It's not something that is as prevalent as something like microservices or event-driven. Can you shed some light on that?
**Mark:** When we set out, well, seven, or eight, nine years ago, I guess, to write the first edition of the Fundamentals of Software Architecture, we wanted to give a holistic view of software architecture in three parts. Of course, we were limited by space. As Neal's very fond of saying, this could have been a 20,000-page book or a 200-page book.
There's a lot of, well, I would say good architecture books that focus on maybe one or two of the most popular architecture styles. What we wanted to do was really expand that breadth of knowledge about different architectures. One of those that was unique is space-based architecture. Neal and I, before microservices came out, used to refer to this architecture as a domain-specific architecture, meaning that it was built to solve one particular problem. That was of elasticity and high levels of scalability.
These kind of systems that, how do you support 1 million concurrent users or even 5 million concurrent users? Concert ticketing systems that have these spikes of going from several users to several tens of thousands of users instantaneously within the first couple of seconds. These are extremely hard problems to solve in architecture. Space-based architecture is, in fact, one of the ways of solving these kinds of problems.
It's called space-based not because of outer space or because of cloud, but because of a computer science term, a pattern called tuple space, which means multiple parallel processors with shared memory. The idea of space-based is this: any system, when we start talking about these kind of levels of scalability and elasticity, will have one single limiting factor. That's the database. The database will always become a problem in highly elastic and highly scalable systems.
What space-based does is effectively removes the database from the transactional or operational equation. Everything in space-based, all data, is cached in memory. Consequently, if you remove the problem, then you no longer have that constraint. This I just want to say is one architecture I'm really fond of. I'm fond of it because of this one reason, because this architectural style solves a particular problem and it forces us as architects to think about other kinds of problems, other kinds of constraints that we have that are preventing us from maybe it's high availability, maybe it's high agility, maybe it's great testability.
We always have constraints as architects. This architectural style causes us to really think outside the box in terms of, is there a way to remove that constraint? Is there a way we can shape an architecture to overcome a particular constraint we have to solve a problem? I really like that about space-based architecture. Turns out that it used to be, in the first edition of the fundamentals book, the longest chapter.
As a matter of fact, I had to trim it down from, I believe it was, Neal, 85 pages down to 60, I think, just due to the sheer weight of it. I will have to tell you, it is no longer the largest chapter in our second edition. I'm wondering, Prem, if you could guess, it's in part two, the architectural styles, which chapter became the longest?
**Prem:** I have not actually measured that way, but let's see. If I have to guess. I don't know. Is it in Part 1? Give me a clue.
**Mark:** It's in part two — it's one of the other architectural styles.
**Prem:** Wow, okay. Maybe modular monoliths or maybe microservices would be my guess.
**Mark:** Two very good guesses. As a matter of fact, I figured you would guess microservices. That is the third longest, but it turns out it's event-driven architecture that, all of a sudden, became almost a sub-book of itself within the second edition [laughs] just because of its increased popularity. Thank you, microservices. As a matter of fact, Prem, speaking of microservices, I'm glad you said that, because, as I mentioned, space-based, we always considered this specialty architectural style.
Microservices breathed a new life into space-based architecture. Its limits, talk about solving constraints. How do you take 12.5 terabytes of data in a database and put it all in memory within services? The answer is you don't, you can't. This was always a constraint within space-based architecture. Let's talk about microservices, single-purpose services, with much more limited data that it acts on.
If you form this hybrid between microservices and space-based architecture, suddenly it's no longer a specialty domain-specific architecture, but now can be applied to a whole host of problems because those services in space-based are in the form of microservices with much less data in memory. These are other examples of these wonderful constraints I was talking about.
**Prem:** I can totally believe that event-driven is your longest chapter because, yes, personally, I believe that if you've got monoliths and synchronous APIs, and then now if you want to get looser coupling, then event-driven is probably the way to go. Again, there are constraints with that as well, like everything else. Then I have another question for you guys in terms of the microkernel architecture. What exactly is that? It's also something that doesn't get a lot of press. Maybe, Neal, you can shed some light on that.
**Neal:** Yes, it's a shame because it's one of those architecture styles that once you identify it, you start seeing it everywhere because it's so common. The basic idea of a microkernel is it has a core and it has plugins to allow you to add new behavior to it or change existing behavior. It's fantastic as an architectural solution for customizability. It's also a great illustration of the third law that we added in the second edition.
Our first edition had two laws. I mentioned everything's a trade-off. The second law that we did in our first edition was that why is much more important than how, which is also still true. We added a third law based on-- When we wrote the microkernel chapter in the Head First Software Architecture book, we realized that not everything that supports plugins is a microkernel, but every microkernel supports plugins.
In other words, a browser is not really a microkernel because it's purely functional without any plugins. Something like a linter tool, well, yes, it'll parse the code for you, but if you don't build any linting rules to plug into it, then it's useless. Eclipse is a great example, the old school Eclipse. If there are no plugins in it, it could barely open and close text files, and that was all it could do. We defined, in the Head First book, and this made it over into the Fundamentals book, and we were surprised that our editor allowed us to do this, we invented a word, the degree of microkernelity, of how much behavior is in the core and how volatile is the core, because that's the real key is, is it a microkernel or not?
That leads to that third law, which is one of the reasons that software architecture decisions are so difficult, is that so few of them are nice, convenient binaries; they almost all live on a spectrum somewhere. Is it a microkernel? It depends, because there's a degree of microkernelity that you have to assess as to how much bit functionality is in the core. That's another reason that architects are always so grumpy. It's hard to get in these really definitive objective battles about things because everything's a messy spectrum trade-off.
**Prem:** What you seem to be saying is that the more stable the microkernel is, the more the degree of microkernelity. Is that the point?
**Neal:** It is. In fact, the less functional it is without plugins, the more of a microkernel it is.
**Prem:** Now that you say it that way, Trino, the distributed SQL engine, pretty much works the same way. The way that it works is, it has a bunch of these connectors, which allow it to talk to a bunch of databases like relational or Mongo or HDFS and so on and so forth. Without those plugins, it's pretty much useless.
**Neal:** Integration hubs are great examples of microkernels. Continuous integration servers are great examples of plugins. You don't plug anything into it, what is it going to do? It's just going to sit there and wake up every hour and then-- [laughs] It's one of those things. The BFF pattern, the Backend for Frontend pattern that Sam Newman talks about, that's a microkernel, because you're plugging in different user interface agents to handle from the same API.
Every time customizability comes up, microkernel is lurking there in the wings. We talk about it as an architecture style that's quite useful to solve this common problem, which is customizability. That comes up in a lot of different contexts, whether it's operational customizability, like continuous integration, or user customizability.
We talk about, in our book, what if you're something like an insurance company in the United States, where you have standard policies, but then every state can have their own fiddly rules about how you apply some of those rules. A microkernel is perfect for that, because you build the core insurance engine in the middle, and then every state gets their own plugin to modify what needs to happen uniquely for that state. Because they're all plugins, they're all isolated architecturally from each other, so they don't interfere with one another. It's a really, really useful architecture style.
**Prem:** I've got one more question before we call it a close. Towards the end of your book, you talk about how architecture is about making teams effective. This is something that not a lot of architecture books seem to cover. This is definitely something a lot of us would be very interested in learning more about. Can you touch a little bit on that, please?
**Mark:** I'm assuming you're referring to our Architectural Intersections chapter, the last chapter. We added several last chapters.
**Prem:** This is the Chapter 24, which says "Making teams effective." That one.
**Mark:** This is often an overlooked aspect of software architecture. One which I have found, through my 40-plus years of actually working in this field, becomes one of the more important aspects of architecture. It's one of the reasons architecture sometimes doesn't work. Making teams effective was the title we gave for basically collaboration and leading and guiding teams as an architect, and the importance of being able to guide the development team through the implementation of an architecture, regardless if that's greenfield, brownfield, or even continually modifying that architecture to add or remove or update the features.
This is a real key aspect, a full third part, as a matter of fact, of the book in terms of the techniques and soft skills. I will say one that is, unfortunately, often overlooked, and Neal and I cannot stress enough, that half of being an effective software architect and making architecture work are mastering these soft skills, the people skills of architecture.
**Neal:** Yes. In fact, we purposely made the entire third part of the book about those soft skills, because the way you become a software architect is demonstrating good technical skills, and then you often get blindsided by these soft skills, which we always put in air quotes, because it's often the most difficult things that people run into. Trying to make a team effective is a great example of supporting a team and being able to figure out how to do that. It's not an easy thing to do, and it requires some practice and skill.
**Mark:** Prem, I just wanted to add, specifically in the chapter you're calling out, in the second edition, we do show some tools and techniques for how much involvement should you actually have on a development team. In other words, you can really fully derail an entire team by being too involved and too much "in their face." The opposite is true as well, where if you're not there when the team needs you, how can you possibly expect them to implement the architecture correctly?
**Prem:** You have this speedometer where you've got control freak architect on one extreme and armchair architect on the other, where one is someone who wants to exercise more control and involvement, whereas the other one is almost no control, no involvement. I guess the message is that you need to be somewhere in the middle to be able to be effective for the teams that you're trying to serve.
**Mark:** It's not necessarily, Prem, to be in the middle somewhere. It's just to really understand, given certain factors, how much involvement should I have? That's the tool we introduced there. Based on things like team familiarity, team size, the duration of the project, the complexity of the project, and these factors to really gauge that dial, to your point, Prem, may point all the way over to control freak, which means most of my time, most of my day better be with that team or they're not going to succeed, yes.
It's rather than finding it in the middle, it's finding out how much involvement I should have. Hopefully, it's in the middle, that would be perfect because then I could actually lead and manage multiple teams. Too many times it's too an extreme.
**Neal:** It's also about modulating that. By the way you couched the question, it sounds like you've seen both of those types of the extremes in the wild. I think part of the instinct for new architects, which is a lot of what this book is targeted for, is to lean more toward the control freak because now I have the power suddenly, and now I can control all the decisions, and now I can finally implement things exactly the way I want. You have to resist that, but not so much that you become so laissez-faire that it becomes chaos. Finding that right level, putting on the team, the context, I think, is really important. Thinking about what that level is, I think, is the useful exercise.
**Prem:** Absolutely. Thank you very much, both of you, for indulging us yet again today. I'm hopeful that this is yet another exciting episode, as we have called multiple times. Signing off one more time. Thank you very much. Until next time, see you folks.
**Neal:** Thanks, Prem. Always a pleasure.
**Mark:** All right. Thank you.
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
## Explore a snapshot of today's tech landscape
[ Read the latest Technology Radar ](https://www.thoughtworks.com/en-th/radar)
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