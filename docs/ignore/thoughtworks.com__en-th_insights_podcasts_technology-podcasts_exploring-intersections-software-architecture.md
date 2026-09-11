<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-intersections-software-architecture | Title: Exploring the intersections of software architecture | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring the intersections of software architecture 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Prem Chandrasekaran | Podcast guest  Neal Ford and Mark Richards
January 09, 2025 | 43 min 32 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-intersections-software-architecture#Transcript)
Listen on these platforms
## Brief summary
Software architecture necessarily intersects with a diverse range of critical things, including implementation, infrastructure, data and engineering practices. All these elements require serious consideration and reflection if you're to architect effectively. 
To discuss these various intersections, Thoughtworks' Neal Ford and his long-time collaborator Mark Richards join host Prem Chandrasekaran on the Thoughtworks Technology Podcast. They dive into why these intersections matter, what they mean for software architects and how individuals and teams can go about addressing them. 
## Episode transcript
**Prem Chandrasekaran:** Welcome, everyone. My name is Prem Chandrasekaran, I am one of the regular co-hosts of the ThoughtWorks Technology Podcast. Today we're joined by Neal Ford and Mark Richards, and they are going to be talking to us about the intersection of architecture and a variety of aspects of the software development lifecycle. We're going to do this in two parts. In today's episode, we're going to talk about what these intersections are, and in an upcoming episode talk about how these correlate with code and implementation. With that, let's get started. Hello, Neal, and hello, Mark. Would you quickly introduce yourselves?
**Neal Ford:** Sure, I'll go first since you probably have heard my voice a lot. I'm sometimes a guest and sometimes host of this podcast. I'm sitting in the luxurious guest chair today to talk about this since this is some IP I'm creating with my consistent teaching and writing partner, Mark Richards, who's also joining us today. Hi, Mark.
**Mark Richards:** Hi, and thank you actually for having me on yet another ThoughtWorks Podcast. I think this is my third one if I'm not mistaken, maybe even fourth, so it's great to be back on the podcast.
**Neal:** Well, nothing if not consistent! [Laughter]
**Prem:** Excellent. It's great to have you both. Let's kick off today. What is this thing that we're calling the intersection between architecture and implementation? Sounds very intriguing.
**Neal:** We have a term that I did a little poking around and discovered, which I love but is way too obscure to talk about without providing some context, which is the term nexus. It's the term nexus, but it has the little hat over the U and it's pronounced nexus, and the definition is it's plural nexus. It's a combination of nexuses, which is also legal, plural, but it's really this idea that there's not one intersection of architecture and implementation. It's the intersection between architecture and implementation, and data, and infrastructure, and engineering practices. In fact, nine different places that we've concretely identified where architecture intersects with other parts of the organization. I've long said that architecture is unique in that we have a unique perspective on our ecosystem because we understand technical capabilities. We understand business constraints. We understand what infrastructure capabilities are available. Maybe we understand where the enterprise strategic direction is going, and so that's taking advantage of this unique vantage point that we have inside organizations.
**Mark:** Well, and it carries on from actually both of our books, Neal. I should say all three. [laughs] The Fundamentals of Software Architecture, Our Architecture, the Hard Parts, and our recent Head First Software Architecture, where we developed a lot of qualitative analysis in terms of comparing various architectural characteristics between different architecture styles to know really which architecture would be most appropriate for given situations. Yet, the problem is we do that, and architecture still doesn't work. This is really that next step of realizing that architecture rarely lives alone, and as a matter of fact, there's a lot of external forces that influence a software architecture, and vice versa. There's a lot of architecture can influence a lot of external forces. We call these external forces intersections of architecture, and our real goal of all this material, including this podcast, is really to align architecture with these different facets of the environment.
**Neal:** Yes, and eventually be able to express it a lot more directly than we are doing now, but we want to, so this is really a two-part podcast. The first part here is really describing these intersections of what we're talking about here because it's, I know, impossibly vague and abstract right now. We're going to try to make that more concrete. Then the next time, the next installment of when we talk about this, we'll talk more concretely about how we're actually documenting all of these intersections. Let's start with a good example of the first one that Prem mentioned, and probably the most obvious one, which is the intersection between architecture and implementation. Mark, what do we mean when we talk about that intersection?
**Mark:** [chuckles] Well, I've got a question for you first, and Prem, I bet you can answer this. What are the famous words that every architect says when asked a question? Should I use A or should I use B?
**Prem:** Well, I know that that's a very standard consulting answer. It depends.
**Mark:** Exactly. It depends. Well, it turns out that there's another common phrase that most, if not all architects use. When asked a question about A or B, the other response is, well, that's an implementation detail. This is really the crux of that intersection between architecture and implementation. If we don't pay attention to how that architecture is implemented, quite frankly, it rarely works.
When we talk about this intersection of architecture and implementation, there really are three areas within this intersection that architecture has to be aligned with. The first is an operational alignment. The next is a constraints alignment. Then the third is a structural alignment. The way we write source code, the way we implement our architectures, we have to adhere, for example, to certain constraints. Maybe in a traditional layered architecture, the presentation layer is not allowed to access the database directly. It has to go through all the layers. That happens to be a constraint.
Maybe we have a particular constraint within microservices where we have a group of services that cannot and will not communicate with other services. They have to remain standalone. These are constraints that we have within an architecture. If we choose to implement those constraints differently, it's an example where the architecture becomes misaligned with the architecture. A classic example is where an architect chooses, for example, microservices to have really great elasticity, really great scalability, and also a nice change control. With that scalability, let's say to a half a million users, microservices is actually a good choice. Architecturally, it will scale to a half a million users. The developers then notice that services need to communicate with each other, and this coupling is going to slow things down quite a bit. The developers choose, let's say, to use in-memory replicated caching so that if I need data from you, for example, Prem, instead of having to ask you for it, we're just going to use a shared in-memory cache where each of us have that in-memory cache. This way, I have your data, and I no longer have to talk to you. This is decoupled. It's much faster. This is actually a really smart move.
However, both of these decisions are good. Based on the scalability of a half a million users, once we go into production, you can suppose what happens after about 40,000 users because of that in-memory data grid, which is in memory, we run out of memory [chuckles] in our virtual machine, in our pod, whatever that container is, very quickly. This is an example of operational alignment where the architect focused on scalability, but the developers ended up focusing on performance and decoupling. This is a prime example where an architect has to be involved in the implementation of that architecture to ensure alignment.
**Neal:** To overuse a metaphor a little bit about building architects and software architects, there are serious constraints on when people are building a building about just randomly removing a wall, like a load-bearing wall, we need the same constraints as software architects because as people are implementing our code, it could be, well, these two components don't talk to one another in this diagram. Look, I can just draw a line between them, now they're talking to one another, or implicitly do that by doing an automatic import, and suddenly now things have dependencies that they shouldn't have. This is a way of expressing some of those load-bearing walls that are critical for the structural support for the application.
**Prem:** What you both seem to be saying is that it's definitely possible for architects to design something that is architecturally sound and also implementable by the team?
**Mark:** Correct. Yes. The fact that the goals of the architecture and those constraints and those decisions are actually adhered to, and the structure of the code matches the structure of that architecture. Yes, this is perhaps the most common misalignment that at least I see and I think Neal sees as well in terms of having architecture actually work.
**Neal:** Nice thing about this is there's lots of really nice tooling around traditional architecture fitness functions with tools like ArchUnit, or NetArchTest, or PyArctest, or TS-Arc, these are all tools that allow you to create that governance alignment. That's the stuff we talked about in the Evolutionary Architecture book, but this is where the current IP that I'm working on goes way beyond Evolutionary Architecture because we focus mostly on things like implementation, but now we're going much deeper into all these other intersections, including a really critical one that people don't nominally think of as having a serious intersection with architecture, which is data.
**Mark:** Oh yes. Another very common overlooked intersection where, unfortunately, and this has just been my experience that still even today, too often, architects treat data and well, developers, we all treat data as kind of an orphan, something that really doesn't matter too much. In fact, choosing the wrong topology for your architecture can have devastating impacts. When I say topology, what I mean is the three basic kinds of topologies we have, which are monolithic databases, we can have domain-based databases where we break up the data by specific domains. Then all the way to the other end of the spectrum, which is the dedicated data, or what's known as the database per service topology where it's typical in microservices where each service has its own data. That's what forms that physical bounded context.
It's interesting out of all the eight common architecture styles, it does, in fact, matter which topology you use for the success of that architecture. Most of us are familiar with the monolithic topology constraints in terms of scalability, change control. These are two things, fault tolerance that can plague an architecture. If we're choosing an architecture style for those reasons, and we're using a monolithic database, we likely won't achieve those kind of capabilities. As a matter of fact, if we even look at something like event-driven architecture, raises the question, we talk about events and triggering events, responding to events, but where's the database in event-driven architecture? If we use a monolithic database topology, we might not achieve the high levels of scalability and responsiveness and elasticity that we enjoy from event-driven architectures.
By the same token, if we use the other extreme, a database per service, where every service in our event-driven architecture has its own database, we've got great elasticity, great scalability, great fault tolerance, except when I need your data because now I don't have access to that data anymore, and I have to start asking you for it, which all of a sudden synchronously couples our lovely asynchronous architecture. You can see there's quite a range.
**Neal:** You should describe the two anti-patterns that we've identified, or you identified in terms of granularity and messages.
**Mark:** Oh boy, you mean from event-driven architecture? The swarm of gnats is one you're referring to, right? Yes, the swarm of gnats of anti-pattern. This is a anti-pattern Neal and I coined, where a gnat is a small flying insect that both Neal and I know very well from our locations, where you're going out for a walk or you're outside and these small, almost invisible little flying insects, just hundreds of them swarm right in front of your face. Consequently, this anti-pattern comes from the granularity of derived events within event-driven architecture. The fact of triggering too many fine grained events is where this anti-pattern comes from. I still like this name, Neal. [Laughs]
**Neal:** It's a great name because a lot of people have experienced gnats. One other important aspect of the architecture and data intersection has to do not just with topology, but the behavior. We have all grown up to understand that the relational database is magical and it does magical things for us, and we hate to give up on magical things. Magical things like referential integrity checks, and cascading deletes, and foreign key checks for us, and atomic transactions, and all those wonderful things. We sometimes have to give those up when we move to a topology like Mark was talking about in distributed architecture.
One of the common arguments you have as an architect is when you go to data engineers and try to describe this whole idea of breaking data up into tiny, tiny pieces. That's just not the way they're wired. That's not, since they were little bitty data engineers, they were taught that it needs to be monolithic and joined together. That the only way you can do some of those things is within the database, like referential integrity, for example. You can actually do this from an architectural standpoint. Just like we talk about eventual consistency when we talk about transactionality, we can also talk about eventual referential integrity, and eventual cascading deletes, and eventual foreign key checks by building into the architecture things like durable message queues that say, "When you delete this from this service, post a message to a durable message queue that guarantees that that cascades to all the other services that should no longer have a reference to that." Now you're fixing that foreign key constraint across your architecture, but you've changed. Fundamentally, a foreign key constraint is governance. We rely on the relational database to do that, but we can also implement it ourselves if we have to go to distribute data for the reasons Mark was talking about for scale, or elasticity, or availability, or fault tolerance, or something like that.
**Mark:** Also it has to do within the intersection of data, again, not only with the topology, but as Neal was saying, the type of database that we also use. There is an alignment that happens here as well, where in fact relational databases are a great example where the ease of learning and data modeling is, rates pretty high on a relational database as does overall consistency and transactionality. However, if scalability, elasticity, throughput, and fault tolerance, and partitioning are your main primary concerns, then relational databases present an alignment risk. The type of database is actually interesting because what really drives the type of database that we should use is the nature of our data. If data by nature is relational, a relational database works well. If we're storing a bunch of key value pairs, KV database like DynamoDB works really well. The same thing with associations with graph data, that's when we would use things like Neo4j or any of these other kinds of databases. What are the other misalignments that can occur is what these databases are good at and what they're not good at. When we talk about scalability, throughput, availability, ease of learning, the cost associated with these.
**Prem:** I have lots of questions on this because this is one of my pet topics, right? Here is a question for you folks. How do you see architecture playing a role when having to manage the balance between, let's say, a real-time or a batch processing data architecture? Is that a relevant question in this context?
**Neal:** Well, it is because there are a whole bunch of different trade-offs that you have to think about there. The first thing you'd have to do is delineate what trade-offs you're talking about there, and what impacts that have. For example, a batch processing is a steady stream, but then what happens if something happens during the batch processing, and you get a failure? How quickly can you recover? How quickly do you have to recover? Versus in a message-based system, what happens if you lose messages? One of the common patterns in systems like that is to say, okay, if we're handling a stream of messages, don't do error handling as part of the stream. As soon as you get an error, kick it off to an error handler and keep processing messages, which is not an option in the batch world. Those, that absolutely has an impact on architecture, but also things like infrastructure, which is actually our next intersection because now with modern capabilities like infrastructure as code, you can legitimately set up a self-healing system that says, "Oh, we got messages coming in and my queue is starting to fill up. I'm going to spin up an alternate queue and start deferring messages to that and spin up more infrastructure." Of course, there's obviously a limit to this when you fill up Amazon Cloud and the bill comes, but we have some unique capabilities here around handling some of those things in a graceful way.
**Prem:** How does cloud-native architecture redefine the relationship between architecture and infrastructure? Maybe you answered some of that, but that was something that I was going to ask, but--
**Neal:** This was actually going to be the exemplar example of these intersections, but since you asked it now, this is a perfect time to talk about it because we're talking about data and infrastructure, which are the things that are impacted here. This is a great example. I wish I could take credit for this example, but I can't. On a previous episode of our podcast, it was February, I think it was 22, we had Dave Farley on the Thoughtworks Technology Podcast. Mike Mason and I interviewed Dave Farley. Dave Farley is famous for being one of the architects of LMAX, which famously coined the term for mechanical sympathy because they designed this really incredible architecture that took advantage of the size of the CPU's cache and a bunch of crazy stuff like that managed to achieve six million transactions per second, famously.
Then Mike very wisely asked Dave the question, "Well, with cloud, does mechanical sympathy even matter anymore? Does anybody care about that?" Dave said something that's a great insight and it's a great illustration of this intersection concept that we're talking about. Why do we normalize data? Besides the fact that Peter Cote told us to, and I guess we're supposed to do all the stuff that Peter Cote told us to do, but why do we normalize data?
Well, since time began, CPU is cheap and storage is expensive. One of the reasons that we normalize data is we carve it up so we can store it as efficiently as possible and then piece it back together as we need it. Makes perfect sense. We cooked that into our brain so much that, of course, you normalize data, but when you move to the cloud, it's the manipulating and moving it around that's expensive. Data at rest is essentially free. Instead of normalizing your data in the cloud, you should duplicate it and shard it everywhere. Now, talk about a mindshift. Good luck architects going to your data engineers and telling them, "Hey, all that normalization you're doing, forget it. We're not doing that anymore. We're going to stop normalizing our data and see what interesting conversations that generates within your data engineers and your organization."
**Prem:** Let me play devil's advocate for a second, right? Absolutely. I totally understand with the cloud, the semantics now change. You probably don't have to normalize as much as you probably did when we were in a lot more constrained environment. Then it still comes with some overhead, right? Now, I've got 15 different copies of my data and who knows where. Then now when something changes, you have to go update it in 15 different places.
**Neal:** That's right. Well, I'm sorry, we never promised you that we were going to have perfect solutions. It's about trade-offs in software architecture. Again, if you have that behavior in a cloud, you can do eventually referential integrity and consistency and say, "I've got this in five different places. I have fitness functions that say when this disappears here, make sure that it also disappears from those other places." That's a good example of translating something that nominally happens in a database, but we need because of architecture concerns to move it to a cloud environment replicating the same governance behavior, but in a different way through architecture.
**Mark:** Well, it's interesting too because this whole discussion about these trade-offs always seem to boil down to CAP theorem. CAP theorem basically says you can have a network partitioning, which is the P or consistency, C, availability or network partitioning. It's an interesting case that in distributed architectures, which most, not all, but most cloud-based architectures are necessarily, or I shouldn't say necessarily, but typically distributed. That only leaves us architects with two choices, consistency or availability. It's not surprising if you look at our star ratings in the Architecture of the Hard Parts book for all of these databases, these are two of the main trade-offs. Relational databases give us the consistency without the availability. If we move over to something like a KV database, or even a document database, Colomer especially, consistency drops down to one star, but we get four to five stars on availability. This is just yet another manifestation of CAP theorem in action. What we look at with that typically is not saying, oh, well, then you can't use Colomer because maybe the nature of our data fits in Cassandra, for example, or Druid really really well. The way we spin this kind of intersection or alignment is based on what risk we are incurring because of the nature of our data, and the kind of database we're choosing. If we're in cloud environments with highly distributed data such as DynamoDB, our risk is with consistency. That's going to be one of the main things we have to trade off and think about in this alignment.
**Neal:** It is teams which seems at first blush like, "Well, how can you talk about the intersection of architecture in teams?" We have a lot of respect for the ideas by Team Topologies and this idea of stream-enabled teams and enabling teams. What this approach to software development encourages you to do is to think about how would you objectively measure some impacts like this between architecture and something like teams. If you were trying to figure out, for example, so part of Team Topologies is this idea of you have a stream-enabled team or a stream-optimized team, an enabling team that's giving them advice and assistance, et cetera, or a specialty team, now the question is, are those teams slowing down your stream team? The goal is to make that as fast as possible. Now if that's our goal, how can we measure that in a way that's consistent with architecture?
Well, you can measure things like how many merge conflicts are coming in from the specialty team, or the enabling team into the stream-enabled team? The more merge conflicts that are coming in, the more they're imposing things and the more they're having to handle merge conflicts and the more it's slowing things down. This is a measure of team impact for having something is the contribution they're making actually improving things or are they creating so many complications that are actually instead slowing things down? Another way to think about this team intersection is how much effort does it take to implement a brand new feature? One of the famous things that we talk about is the Inverse-Conway-Maneuver where you really want domain-specific teams rather than separated by technical capabilities. The question you have to ask yourself is, well, what if you're trying to build something like microservices, but you still have all your user interface people sitting in one place, or your developer somewhere else, or your data engineer somewhere else? You have to replicate that communication structure by Conway's law. How do you do that? You do it with Jira tickets. Measure the number of Jira tickets it takes to implement a new feature. If that's over 10, you've got communication issues in your organization. It's a way of looking at the architecture, which is supposed to be domain-focused, but our organization is not domain-focused, and it's creating a bunch of artificial churn and friction that we can actually measure and try to address by observing that.
**Mark:** Also, if we look at the shape of various architectures, one of the aspects of that shape that does tend to influence team topologies the most is the overall modularity level of the particular architecture style. The less architectural modularity we have in our architecture, the less effective enabling teams or complicated subsystem teams will actually be because we're going to be getting in each other's way, as Neal just said. That alignment is also a key indicator of, do we have these right teams and can we even leverage these different team topologies due to the shape of our architecture.
**Neal:** Let's talk about another intersection, which is engineering practices. One of the things you can use this approach to do is to, when you make messy trade-offs, can you mitigate the bad parts of the trade-off? A common messy trade-off that you encounter in a lot of projects is a monorepo versus separate repo per service. Let's say that you choose a monorepo for good reasons, lots of trade-offs. What's the big danger that you have if you use a monorepo and you're trying to build some distributed services? Well, the problem you run into is that it's very very easy to create accidental coupling points between components in that system because all the code base is there, the same code base, and it's easy. In fact, your IDE may just helpfully do that for you as part of an auto-import, and you don't even realize you're reaching across an ecosystem to grab those things. One of the ways that, okay, we've decided to use a monorepo, now let's build an architectural fitness function in something like ArchUnit, or NetArchTest, or PyArctest that says, "Make sure these components never get coupled to one another in any of my compilation targets." That's really the fear in the monorepo. Once you translate, what is the actual fear, the danger of using a monorepo? Once you translate that into architectural terms, you can build architectural checks to make sure that you haven't accidentally done that, and now take advantage of the good parts of the monorepo and avoid some of the pitfalls that come along with it.
**Prem:** I do have a question related to this, right? This is probably controversial in that, on a team, should architects enforce engineering practices or is that just solely the implementation team's domain?
**Neal:** I would say that goes back to the earlier answer to the question we had, which is, it depends. I think it depends on a lot of things, the size and sophistication of the team and the organization, do you have a dedicated infrastructure team or is that something that you're doing or is it a shared responsibility and that sort of stuff? I think that I don't see any good place where there's a strict isolation between those two roles. There should be definitely feedback and collaboration, but I think it's organizational as to exactly how involved that is. Some of it has to do with how complicated the thing is they're building too. If you're building some very complicated space-based architecture, there's probably a lot more intersection between those parts.
**Mark:** Also, I think where that alignment comes in, it depends, but it also depends on the type of capabilities that we're looking for in the architecture. Let me give you an example of what I'm talking about. Let's say that our capability or architectural characteristic is extremely high levels of agility. The ability to respond quickly to change due to a very aggressive time to market needs for this particular company. When a bug is identified, a new feature comes out, that change has to get to our end users as fast as possible. There are architecture styles that support high levels of agility. Microservices has five stars for agility. The N-tiered layered architecture has one. [laughs] When we look at the shape of that architecture, the alignment now starts to play into the engineering practices as well. If we didn't need or if we're not experiencing high levels of change, if we don't have a lot of maintenance, then these engineering practices become less significant than if we do incur high rates of change, and we do have high need for agility because some of those engineering practices may impede maintainability, may impede testability, deployability, our deployment pipelines, and that's when this alignment starts to matter the most. That's another one of those, it depends moments. [Laughs]
**Prem:** That leads us to the next one, which is the intersection between architecture and business. How do you navigate this tension between meeting short-term business goals and long-term architecture vision? Always a catch-22.
**Mark:** Sure. Oh, yes. When we talk about a business environment, what we're talking about is, for example, is your business undergoing extreme cost-cutting measures because they're losing market share, they're losing money, or are they aggressively expanding into other markets? The type of architectures we have will influence that business's ability to do those things. Maybe it's undergoing a high regulatory compliance as a necessity within your business or competitive advantage. The size of the business also impacts our architectures, small business versus large businesses. Large businesses typically need more scalability, need the ability for evolutionary architecture or evolvability, adaptability, whereas small businesses typically are more focused on the cost of that architecture from initially creating it to ongoing, the complexity of the business matters and things like constant change.
When we talk about the business environment, one of the other very important intersections that comes into play with business is with the domain as well. As a matter of fact, Neal and I call this domain-to-architecture isomorphism. Isomorphism really meaning, does the shape of one thing match the shape of another? When we talk about our business environment, does the shape of our problem domain match the shape of our architecture? Those of you listening are probably saying, "Mark, what in the world are you talking about, shape? What do you mean?" Well, every architecture has a shape associated with it. For example, microservices is a prime example. The shape of that architecture is simple purpose functions deployed as separate units of software with each owning its own data. That's the shape of that architecture style.
Now, what about the shape of our domain? What in the world do you mean? Our domain has a shape, of course, it does. That shape may involve things like time to market, the nature of data must be consistent. Maybe I've got highly semantically coupled data or maybe my business domain has highly semantically coupled functionality. What are the nature of my changes? Are we constantly replacing our presentation layer, our user interface, but all of our business stays the same, our data stays the same. That change is technical in nature. That's that shape of that problem domain. If we take the shape of an architecture like Layered, where that's functionality is grouped by technical categories, that's a great alignment. [laughs] Whereas if the nature of our changes are domain-based, we want a domain-shaped architecture in that case. Every business problem also has its own shape, the way of describing the needs and constraints within that business problem.
**Prem:** I do have a question related to this, right? I'd like to think of the business requirements as the problem domain and the architecture as a solution domain, right?
**Mark:** Sure.
**Prem:** Now, what do you do when the shapes of these two do not match? What are your options?
**Mark:** Well, there's really only two parameters. That is, we could change the business domain or we could change our solution. This is something that Neal and I both are working on a lot of material for, which is iterative architecture because the shape of our problem domain may match right now, what happens in four years, five years? Suddenly, it's like putting a square peg in a round hole. Prem, this actually does happen. It's up to the architect to always ensure this alignment of that shape. Generally, we will do architectural refactorings, and iterate on that architecture as the shape of our problem domain continues to change. Where we run into trouble is when we don't pay attention to that alignment.
**Neal:** Yes, inevitably business can change faster than architecture and we're always playing catch up on trying to, and this is one of those alignments that we're constantly trying to achieve, and we're always a half step behind. That's actually, I think by its nature, we're always going to be a half step behind.
**Prem:** I don't know who coined this, but I think I saw this person on the ThoughtWorks radar called Inverse Conveyor Maneuver. Yes, I guess that's probably relevant in this context.
**Neal:** Jonny LeRoy coined that. He was considered the Department of Naming Department when he was here. [Laughs] He was good at coming up with names for things. Let's talk about one last intersection, which is, I think it's required by law that you have to mention generative AI, at least at some point during every podcast or public pronouncement by a company these days. Of course, there's a huge intersection between architecture and generative AI, but there are actually two kinds of intersections. It's important to tease those things apart. The first of those intersections is the shiny one, which is, ooh, let's customize the LLM or build RAG and augment the output and all those sorts of things. That's the very operational side of LLMs. Certainly there's a huge topic area, but that's really more of a specialization, almost more like analytical data or user experience or something like that.
The general concern we have as architects and AI is operationalizing it. It's a shiny demo right now, but putting that shiny demo into production is tricky because now we need to get it to work at scale. Now we need to make sure that we have evals and guardrails and the appropriate context, and the correct filtering is going on. It's producing the right stuff and validating the output and all these things, reservability for LLMs. 38% of the blips on the radar had to do with generative, AI and almost none of them were LLMs. It was all ecosystem support for LLMs. That's, I think, the near-term huge intersection we're going to see. It's certainly useful for doing things like code generation. Mark and I have actually had some great success of using the language part of LLMs to translate from pseudocode into platform-specific fitness functions. That is actually the topic of the next installment of the podcast because we've got a lot of stuff to say about that and why that's an interesting approach. That's another great use of GenAI because at the end of the day, large language models are language models and they're really good at translating from one language into another one. You can definitely leverage it to bootstrap yourself into some of these building some of the protections and defining some of the intersections we're talking about. You can use it to go Meta and help you describe the other intersections that we identify as well. What we've done today, is used a whole lot of hand-waving to describe each one of these intersections. We're software architects at heart. We want a much more concrete way to express these intersections. That's what the second part of this podcast is going to be, which is this idea of architecture as code. Take the intersections that we've talked about, but express them in code. Just like a building architect creates a plan that the builders follow, we can create plans for data intersections, implementation intersections, infrastructure. We've got a lot of details about how to do that. That's what we're going to cover in the next episode is how to make these descriptions of these intersections much more concrete.
**Prem:** With that, we come to the end of this episode of the Thoughtworks Technology Podcast. Thank you very much Neal and Mark. We look forward to the next episode where we will talk about how architecture intent can actually be translated into working code.
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
## Explore a snapshot of today's technology landscape
[ Read the latest Tech Radar ](https://www.thoughtworks.com/radar)
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