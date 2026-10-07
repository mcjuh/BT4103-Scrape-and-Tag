<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/fundamentals-software-architecture | Title: Fundamentals of Software Architecture | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Fundamentals of Software Architecture 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Evolutionary architecture ](https://www.thoughtworks.com/evolutionary-architecture)


Podcast host  Rebecca Parsons | Podcast guest  Neal Ford and Mark Richards
February 21, 2020 | 35 min 24 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/fundamentals-software-architecture#transcript)
Listen on these platforms
## Brief summary
Rebecca Parsons talks to Neal Ford and Mark Richards about their new book that promises to become the definitive guide to software architecture. The book provides a concise overview on what's needed to become a software architect.
**Podcast Transcript**
Rebecca Parsons:
Welcome to the Thoughtworks Tech Podcast. I'm here today with the authors of a new book called Fundamentals of Software Architecture. Neal and Mark, would you please introduce yourselves?
Mark Richards:
Sure. Hi, Rebecca. My name is Mark Richards. I'm an independent consultant and a hands-on software architect. I've been in the industry for almost 35 years now, 25 of those as a software architect. I'm the founder of developertoarchitect.com, a website I created several years ago as a giveback website to host a lot of references, books, videos, and lessons about software architecture.
Neal Ford:
You may recognize my voice. I'm one of the regular hosts of the Thoughtworks Technology Podcast, but I've figuratively moved over to the guest chair today because I'm also one of the co-authors of the Fundamentals of Software Architecture book. I'm Neal Ford, and I work at Thoughtworks as doing software architecture and a variety of other things within Thoughtworks.
Rebecca Parsons:
My name is Rebecca Parsons. I am one of the regular hosts, and I am the chief technology officer for Thoughtworks. Now, let's get started. The book is called Fundamentals of Software Architecture. Does the world really need another book on software architecture?
Neal Ford:
That's a really good question. We actually broached this question several years ago, almost exactly to the month, because he and I both realized we had a lot of material that overlap, that covered some interesting parts of the software architecture ecosystem, but we didn't have a really good idea at the time what a fundamentals book or even course would look like. Then we started putting together a training course and then Mark started iterating on that a lot and we both started working on it. You know this as well as we do that anytime you take some ideas like that and start iterating on them, just like in software, you can refine and hone those things and make them better and better over time.
Neal Ford:
Over time, we actually have carved this material down where we think we have a reasonably good idea of what the scope of a Fundamentals Book of Software Architecture would be. Certainly software architecture is a big, huge, sprawling topic, but there are some things that we think most software architects should have some good context for and those are the things that made it into our book.
Mark Richards:
Well, and also both Neal and I agree that the journey from developer to software architect is actually a very difficult one. Largely architecture is a multidisciplinary type of thing, I guess you would say. What we have found almost close to what, six years ago, Neal, I think it was that there really wasn't a concise guide out there for knowing how to become a software architect. We started to put our heads together because both Neal and I had a lot of material, disjointed but a lot of material, on software architecture. We kind of thought a good comprehensive book that really dealt more with our experiences in the industry rather than kind of theoretical ideas was really kind of the crux of saying, we should write this book for the industry.
Neal Ford:
And so we do.
Mark Richards:
But another reason, Rebecca, to your point about why yet another software architecture book, there's so many out there. Neal and I both observed quite a bit of change, especially in the past 10 years or the past decade, but even further in terms of where software architecture is going. A lot of the books still kind of hold onto some of these old axioms that we see basically becoming invalid. Another reason for why yet another software architecture book was not only to relay both Neal and I's pragmatic experience within architecture hands-on, but also to invalidate some of those old axioms and also bring it to kind of today's world.
Neal Ford:
Well, as you are very familiar, Rebecca, being the co-author of Building Evolutionary Architectures book. Building Evolutionary Architectures' my most recent book that we co-authored together, the software development ecosystem is in constant flux and it's constantly changing. It changes in these little tiny ways, but the accumulated effect of all those tiny changes is an entirely new world every so often. We make these assumptions in software architecture, but then those assumptions slowly become invalid and go away. I think microservices really brought that to everyone's attention because for a couple of decades the attitude in the industry was, well, software architecture is the stuff that's hard to change later.
Neal Ford:
But then you start building architectures where the notion of change is built into it and then suddenly it's like, well, no, that assumption is long no longer valid. We started looking at what other of these kind of overarching assumptions that you just carry around with you, what we're calling as axioms, how many of these other ones can you kind of cast aside because the modern ecosystem has gradually chipped them away until they don't exist anymore? Can you rethink some fundamental things about software architecture because the ecosystem has gradually changed and is a brand new place from the last time people made assumptions about these parts of software architecture?
Rebecca Parsons:
Before we delve into the specifics, more of these axioms that have been invalidated, what do you think is really behind the change that we've had in architecture? What has caused those axioms to be invalidated? What do you think is behind this dynamic ecosystem that we live in now?
Mark Richards:
Yeah, I think it's multifaceted actually. I think there's certainly... We can talk about two major facets of that, Rebecca, the first being business change, change within the business landscape, but also a significant change in the technical landscape as well. You want to talk about one of those?
Neal Ford:
Sure. Let's talk about the technology landscape. Five years ago, nobody knew what Kubernetes was, but now there are multiple conferences around the world with thousands of people dedicated to Kubernetes. But it would've been impossible five years ago to predict exactly something like Kubernetes because just the fundamental nature of the software development ecosystem is one tiny change triggers another tiny change which triggers another tiny change. It's a very chaotic kind of relationship where it's impossible to predict what sort of long-term implication, something like, oh, containerization, well, that sounds like a pretty small evolutionary staff beyond the virtual machine.
Neal Ford:
But then suddenly when that appears, a whole new landscape open up and all of these new possibilities and ways of thinking about solving problems, including some really nasty problems that we... On demand scalability is a great example of one of those things that some of us on this call have sweated bullets trying to build architectures to build those kinds of capabilities, and now it's a configuration setting on your cloud provider. That's very frustrating to those of us who sweated blood and shed tears trying to get those things to work that, oh yeah, I misconfigured my cloud. Hold on, I'll fix our scalability.
Neal Ford:
That's a great example of just how fundamental the ecosystem changes, but also how unpredictable it is because each of those changes is this tiny little incremental thing, but the cumulative effect can be massive.
Mark Richards:
That's right. Within that, the business landscape itself, change is so prevalent and also remaining competitive in today's marketplace is extremely difficult. Businesses are finding, at least this is in my experience, keeping current or even keeping competitive in this landscape is extremely difficult. If you take any kind of the large type of industries, banking, insurance, trading, any of these things that used to be so stable, small boutique banks and towns are showing up everywhere. Large banks are not only competing against other large banks for customers, but also now against smaller banks that are able to offer better rates on money market, CDs, and even checking.
Mark Richards:
Trading firms are competing against each other, brick and mortars, whereas a day trader, why would I spend 12.99 on a trade when I can online probably with the same broker spend 1.99. Even insurance is experiencing significant change and competitive advantage. Insurance companies not only are competing against each other, but small boutique insurance firms are opening up everywhere, especially in the Midwest here in the United States. This competition becomes very fierce. We won't even talk about retail. It's like all podcasts. But the point is, companies these days to survive have to be more agile. We can't turn a large ship for several years. It has to turn within a matter of months now. The problem is our architectures are not easy to change in a lot of these companies.
Mark Richards:
That agility within business trickles down to the actual ability to change an architecture itself to maybe sometimes even redirect that business. Yeah, these two changes combined are really the precipice for this.
Neal Ford:
Well, I think even within Thoughtworks 10 years ago, we used to really have to sell a lot of companies on this idea that agile was not this crazy idea, that it was actually a smart thing to do. We have to sell this idea a lot less often because the world has changed enough to make companies realize that we have to be more responsive. This is the shift that we talk about from viewing software as overhead and a cost center versus being strategic. That's a fundamental shift. But if you're in a business where you treat and all your other business' competitor is treated overhead and then somebody moves in to strategic, suddenly they have a huge advantage and it changes the kind of business landscape you're in.
Neal Ford:
That's another huge driver that, again, is unpredictable and the pace of which it's speeding up at least as fast as the pace of the technology landscape.
Mark Richards:
I mean, even DevOps, CI/CD, these are environmental changes cloud that directly impacts our architectures.
Rebecca Parsons:
Okay. Those axioms that I used to hold so dear, give me an example of one that you think is invalidated to the point where how we used to think about architecture is simply no longer valid.
Neal Ford:
We'll give you a couple of examples because that's really one of the... When we set out to write the book, we were really hunting for what are some fundamental assumptions that people have made that have led them to make less good decisions in architecture or delay decisions longer than they necessarily need to within an architecture. One of the things that we realized was something actually related to this measure that we created in the Evolution Architecture book around this idea of an architecture quantum because we realized as we started rethinking architecture characteristics, which is our name for nonfunctional requirements or system quality attributes, we have all-
Mark Richards:
Abilities.
Neal Ford:
Yeah. The reasons we like that name better. But when you really start thinking about those, the kind of base assumption was that those are at the system level. Because when we first started thinking about those, most architectures are monolithic. But now when you look at things like microservices, one of the magic powers of microservices is the different services can have different sets of architecture characteristics. The scope of how we think about architecture characteristics has now changed and is much smaller around service in a microservice architecture. If you go into the analysis of architecture characteristics with that in mind, it gives you a better decision criteria of deciding should I choose a monolithic architecture style or should I choose a distributed architecture style?
Neal Ford:
If we're in a distributed architecture, where should the boundaries of those architecture characteristics be? In other words, where's the scope of those things? Once I've established that, now I can figure out where data should live in a distributed architecture and then I can figure out things like communication techniques. Rethinking where the scope of those characteristics live give you a lot better analysis techniques for figuring out sooner what is the most appropriate kind of architectural style to solve this problem.
Mark Richards:
Right. That's a good example of a structural aspect. I want to talk about a process aspect of an axiom and that is that software architecture is really separate from software development. As a matter of fact, we invalidate that axiom. As a matter of fact, an entire part three of the book, we invalidate that axiom and really maintain that software architecture is actually part of the software development process and that this tight collaboration between architects and developers in today's world is absolutely necessary to get architecture to work. We've been kind of saying this for some time, just not knowing actually how to accomplish it.
Mark Richards:
Based on a lot of the experiences that both Neal and I have had, we conveyed some of those tips and techniques within the book, not only to state and demonstrate exactly why this tight collaboration, not communication, but collaboration, really has to exist between architects and software development teams, but also how to actually accomplish that as a software architect. That's another process related kind of axiom that we also invalidated within the book.
Rebecca Parsons:
Tell me a little bit about the structure of the book, what's in and what's out. I mean, I will point out that you've used carve down and concise, which are not normally descriptors of a book that's over 400 pages long. What's in? What's out? How's it laid out? What motivated the structure of this book?
Mark Richards:
Sure, Rebecca. Let me tell you about a little bit of the overall structure and have Neal dive into some of those aspects about our decision-making about including certain things. The book is really divided into kind of three main parts in which when we started to kind of organize the material into a narrative arc to actually give the reader a journey from developer to architect essentially. Part one really deals with a lot of the foundational aspects of software architecture. We provide a lot of definitions within there, lay kind of the groundwork for the follow-on sections in parts. Part two, it really focuses on the structural elements of architecture, the architecture styles.
Mark Richards:
As a matter of fact, I think we cover eight of them if I'm not mistaken, Neal, including things like microservices, microkernel, space-based architecture, service-based architecture, a whole host of others. We dive pretty deep into those patterns and styles of architecture, show a lot of examples of those architecture styles when they're used and when to use them. Then part three of the book is also dedicated then to the soft skills of software architect. Really focusing on those leadership and negotiation aspects. Very similar, Rebecca, to what I just talked about with that need to collaborate and be part of a development team. Part three is devoted entirely to that piece.
Neal Ford:
Yeah. One of the nice roles I get to play is the conference co-chair for the O'Reilly Software Architecture Conference. One of the things that we try to focus on in that conference are these talks that focus on soft skills like how to conduct a meeting and how to negotiate and how to resolve differences and how to sell your ideas to management. When a lot of architects come to us after the conference and say, "Those are the things that were really most valuable to me because you can learn technical stuff by reading online, but it's really hard to get a lot of those things.
Neal Ford:
We wanted to really make sure the substantial part of the book focused on those kinds of skills that frankly most developers don't focus on in their ascension toward becoming a software architecture because you're mostly focusing on technical skills and showing expertise in those areas. We wanted to have a strong part of it focused on presentation writing, have document things in architecture, but we also... The subtitle of our book is actually an engineering approach. We want to take a very engineering eye toward this, using a lot of agile engineering practices.
Neal Ford:
This is, again, toward that idea of taking all the things that exist in the modern landscape, taking a snapshot right now of what kind of capabilities we have in software development and architecture and operations, and apply those things as aggressively as we can to get better at designing and assessing and analyzing software architecture. We actually take several older metrics from the structure design and the object oriented design world and show architects how they can use it to analyze existing architectures to learn the 20,000 foot view of quality of some key metrics in the code base. We tried very hard as much as we could to focus on how much can we push software development toward an engineering discipline.
Neal Ford:
The other thing that we focus really heavily on is everything is a trade-off. In fact, we have some laws of software architecture that talk about trade-offs and how to assess trade-offs. We try to couch everything not as this is a best solution. We never use the term the best anywhere in the entire book. It's always this is one set of trade-offs, but there's a counter set of trade-offs. We try to focus very diligently on objectively looking at everything we could and seeing what the real trade-offs are.
Mark Richards:
As a matter of fact, Rebecca, that was one of the things that Neal and I did attempt to and I think accomplished in the book were these overarching themes that ran across every chapter and every section and sometimes every paragraph specifically again about that first law of software architecture that everything is a trade-off. One of the things that we do in the book when we mention something is to also drive home what is the trade-off of this. Rebecca, you probably know this after also writing many books that once you start writing, you keep writing and writing and you go deeper and deeper and deeper. One of the challenges that we did face, which I'm sure most authors face, is how deep to go in a particular topic. We have gone pretty deep on topics.
Mark Richards:
However, that was really the challenge point about what to include and not to include. Rather than removing entire sections, there are parts of the book where quite simply we weren't able to go as deep as we would have liked to. This would've been a six to 800 page tome if we had done that, but fortunately we do have another book which we are embarking on as kind of a follow-on for the hard parts of software architecture, which we actually can then go deeper into some of those aspects.
Mark Richards:
There were times is my point where we could have taken the opportunity to go much deeper in some areas, but would have lengthened the book to the point where we would have had to have skipped out a lot of really important foundational concepts that are important for newly minted architects, as well as experienced architects and even developers.
Neal Ford:
A great example of something that we left out just because we didn't have a great expertise and it would have greatly expanded the scope of the book is a lot about data architecture. That's a huge rich area that we just didn't have space to address, but we are going to try to address that in our next book, which focuses on some of those difficult problems around data architecture. But it's always a tricky thing when you have a big sprawling topic like this is where do you draw the line? A lot of pages got pushed off to another repository over time to figure out exactly what's the scope for this one.
Mark Richards:
Yup. Yup.
Rebecca Parsons:
Well, particularly with a topic that's as nuanced as software architecture, I mean, every question you get asked about software architecture, the answer always starts with, well, it depends on blah, and then you lay out all of the 17 different pieces of context you need in order to answer the question. For a topic this nuanced, I'm sure scoping was a significant problem for you.
Neal Ford:
It was a challenge.
Rebecca Parsons:
We've covered this a little bit, but what is your elevator pitch for how this book is different from other software architecture books, particularly those that are not aimed at describing a particular architecture, but as Mark has said multiple times about this journey to architecture and what does it really mean to be an architect?
Neal Ford:
Well, actually I believe that every 15 or 20 years somebody should do exactly what we've done because the ecosystem changes so much. I mean, if you tried to build an architecture with all the things that we only knew 15 years ago, you wouldn't have much of a useful system anymore. But the books that we rely on sometimes are 10 or 15 years old about this. I think that software architecture is one of those things that so fundamentally changes one little piece at a time that you really should take another stab at it, looking at can we take it in the context of all the new stuff, the modern stuff that's around? I think that's one thing that I don't think we'll be the last ones to do this. In fact, we shouldn't be the last ones to do this.
Mark Richards:
I hope not.
Neal Ford:
Somebody else should pick this up in another 10 years and do the exact same thing with all the other brand new toys that we have laid around.
Mark Richards:
I also think, Rebecca, there are, as you noted, several books on software architecture out in the world there. One of the things I think that differentiates our book from a lot of those is that within a single book we have brought together both the foundational aspects, structural aspects, process aspects, and probably more important, the soft skills of architecture, and have put those together in a cohesive fashion so that it actually does paint a whole journey as opposed to just a bunch of separate sections in a book. I guess that holistic view of software architecture I think is one of the things that differentiates our book from a lot of others that focus on either just the soft skills or the structural aspects.
Mark Richards:
One thing Neal and I noticed as we were spending many, many, many years writing this book was that these different sections all interrelate and all connect as callbacks to one another, part one the foundations, part two with the structural aspects, and part three with the soft skills and process piece. Any one of those parts really can't live separately either as a separate book or a separate kind of topic. One of the things that we did do through this book was to tie those together and continue to weave different sections in as one cohesive unit.
Neal Ford:
That was the other thing that helped us limit the scope. The things that didn't fit as well into that overarching narrative ended up getting pushed aside because we really were trying to make it all coherent and contextualized for someone who's in that role.
Mark Richards:
Another thing that I think, Rebecca, really differentiates this book, one of the things I was actually very excited about when writing this book was that there is a... What don't you think, Neal? 70 years of collective experience that went sent into this book, but the point is it's highly pragmatic. There's very little theory within the book, most of it. If we do have theory, we talk about the trade-offs associated with any given kind of approach or solution or technique. Those trade-offs, Rebecca, really came from our collective experience in software architecture for the 30 to 35 years each and for each of us.
Mark Richards:
I think this also differentiates it in that we've got two really good architects that are able to work together really well, put our heads together, and pretty seamlessly come up with the cohesive ideas for this book.
Rebecca Parsons:
Let me expand on that a little bit. How often were those trade-offs coming out of your different experiences with some of the things that maybe you both approached what on the surface looked like a similar problem when in fact it really wasn't because item nine on the contacts list completely different. I mean, did you find your experiences complimented, contradicted, overlapped, probably all of the above? Tell me a little bit about that.
Neal Ford:
Well, very much all of the above, but it was interesting to see the way we approached several different problems. Some of the discussions we had about different nuances of reliability and microservices is a great example of this because being a distributed architecture, generally distributed architectures take a reliability hit because you have to have network communications, you have files distributed computing.
Mark Richards:
Oh, but wait, the network is reliable.
Neal Ford:
There's the problem that you have, but you can use things like redundancy to give more instances in service discovery. There are a bunch of different ways to solve that particular problem. In fact, that led to what we ended up codifying, is what we call the first law of software architecture, which is everything in software architectures are trade-off. The first corollary to that law was if you think you've found something that isn't a trade-off, you just haven't discovered what that trade-off is yet. That's what we ended up doing a lot between the two of us is, "Oh, here's a thing that's good. Wait a minute. Now, if it's good, there has to be a bad. Where is the bad side of this?"
Neal Ford:
That was actually a really good process I thought because pretty much everything that we came up with, we tried to question and find what's the counter to that. If it was a bad thing, we tried to find the good and vice versa. But I think that's really ultimately the skill software architects should hone the most. It's not the collection of facts that you get out of a book like this, but rather given any circumstance, how can I become better at objectively assessing what the real trade-offs are so that I can make the better informed decision in this instance? Because you're never going to find a book that has your situation in it. But if you get better and better at trying to identify what the real trade-offs are, you've got a better shot at making good decisions.
Mark Richards:
Any architect will know the answer to any given question in architecture, of course, is it depends. That gets rather cumbersome and irritating at times. We were very careful in the book. Of course, if you search on it depends, you will see hundreds of, well, which one is better? It depends. But one of the things that we were careful about doing in the book was to say it depends on what. That's where we would branch out and say it depends on factors or facets of A and B and C and D and then we would dive into A, B, C and D to actually kind of not give somebody an answer, but rather help the reader with the thought process behind how do I analyze whether I should use a traditional layered architecture or microkernel.
Mark Richards:
That's one specific example, as a matter of fact, we do have in the book. We go through that kind of trade-off analysis in there to kind of answer it depends on what. Rebecca, that's too easy of a cop out answer I think. Architects can just wave their hands and say, "Yeah, it depends." Well, give me an answer. Well, it depends.
Rebecca Parsons:
That to me is one of the things that I like about this book is that it tells you the why's and it tells you the questions to ask and what to look for. In my experience, that's the hardest thing for developers to learn is there isn't the same kind of right answer. We can all pretty much agree on what clean code looks like, but what a good architecture looks like, that definition does not exist. If you think it does, then you haven't thought about the problem enough.
Mark Richards:
That's right. Rebecca, you hit the nail on the head. You said the magic word, which points to our second law of software architecture, which is that the why is more important than the how. You hit the nail on the head on that one. Yes. That we had coined as the second law of architecture. Yes.
Neal Ford:
We discovered that because one of the things that we do when we do like a hands-on workshop is we have people design architectures and we have them draw lines and boxes and the designs they come up with. We thought at one point, hey, we should keep those and build a catalog of all these designs that we very quickly discovered that if you don't also force them to write up why they made those decisions, then the diagrams are pretty much useless because you can see how they solved it, but you don't know why they made this decision versus this other one. That really led us to realize that, wow, the why of this is way more interesting than the how, which is really just a detail.
Rebecca Parsons:
You've talked a little bit about, so what comes next?
Neal Ford:
Well, so we've taken a lot of the ideas. This is actually a Mark's name. You're familiar with the book and the meme that came out a few years ago, JavaScript: The Good Parts. Well, we've coined to name Architecture: The Hart Parts because it turns out that... Why do you write a book about something like software architecture or an API? Well, you figured out some best practices for things and you want to write them down. Well, what happens when there are no best practices? A lot of things in software architecture, we don't really have best practices. We have two crummy sets of alternatives to choose from. Now, which is the least crummy alternative is the real key.
Neal Ford:
That's what our next book is going to focus on is a whole bunch of these really difficult problems like what is the correct granularity for your microservices? Wow, okay. There is no correct answer, but man, there's a lot of currently trade-offs that you have to assess doing that. Our next book is really going to focus on what happens to all of those problems where we have it and may never build best practices, and yet we still have to make decisions around those things in architecture. Communication, synchronous versus asynchronous? What's the proper granularity in distributed architectures? How do you manage data in distributed architectures, transactions, and all those things? That's what we're currently working on now is the book called Architecture: The Hard Parts?
Neal Ford:
We're starting to do some workshops around this. There's going to be a two day training at the O'Reilly Software Architecture Conference coming up in New York in February and in Santa Clara in June and in Berlin in November. We're going to do a two day version of that. Zhamak is another one of the podcast hosts and I are doing a one day version of that at the DDD Europe Conference coming up in early February this year. That's the new stuff that we're working on. We're actually very excited about that because we've been working on this book so long. We've literally just within the last two hours finish the copy, edit, review on this book. It is almost done, and we're very excited to move on for the juicy bits in the next book.
Mark Richards:
Exactly. As matter of fact, Rebecca, we're really excited about this new material. We are taking the same process on this new book approach as we did on the Fundamentals of Software Architecture. That book, if somebody were to ask us, "Well, how long did you work on that book?" The answer would be around seven years total, two years writing, but seven years because one of the things that we like to do is to create the material, vent out that material and iterates over that material in conferences, trainings, workshops, so that we can hone it to the point where by the time we get to writing the book, we've already figured out the structure and what things we want to write about.
Mark Richards:
The writing process becomes more an after effect of developing and honing the material. That's the approach we're going to be taking with the hard part stuff as well.
Rebecca Parsons:
Yet it still took two years of actual writing after five years of honing.
Mark Richards:
Yes.
Neal Ford:
It's funny that number because one of the things I like to do is read books by writers about writing, which is an interesting little sub genre in and of itself. There's a great book by Annie Dillard called The Writer's Life. One of the things she said in that book was every book takes two years. It's like, hey, she's right. No matter how much you try to hurry, it seems like they all end up taking two years to write. She's like a poet. I was really shocked to find out that my experience with most technical books end up finding a way to take about two years. The writing of this one ended up doing that. I fully anticipate the next one will probably take at least two years to write that.
Mark Richards:
Well, let's see. I bet it will.
Rebecca Parsons:
That's after you finish the honing.
Neal Ford:
Exactly.
Mark Richards:
Exactly. Yes.
Rebecca Parsons:
Well, thank you, Mark, thank you, Neal, for taking the time to talk about the book and best of luck with the honing process. I'm looking forward to seeing those juicy topics of what is the right granularity for a microservice.
Neal Ford:
We are too.
Mark Richards:
Yes.
Neal Ford:
Thanks a lot.
Mark Richards:
Thanks, Rebecca.
Neal Ford:
We'll talk soon.
Rebecca Parsons:
Next time on the Thoughtworks Podcast, I will be joined by David Farley and Jez Humble, the authors of the book, Continuous Delivery. They'll be chatting about how the term is being used, misused, and what things might look like in the future. Please join us. Thank you.
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