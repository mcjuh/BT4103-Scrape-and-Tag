<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/paradigms-vs-labels | Title: Exploring programming languages via paradigms vs labels | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring programming languages via paradigms vs labels 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Vilas Boas and Rebecca Parsons | Podcast guest  Luciano Ramalho
May 16, 2019 | 23 min 28 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/paradigms-vs-labels#transcript)
Listen on these platforms
## Brief summary
There are always intense debates to be had when programmers try to decide what the best language will be to accomplish any given task.
In this episode, our co-hosts Alexey Vilas Boas and Rebecca Parsons are joined by Luciano Ramalho, renowned author and Principal Consultant at ThoughtWorks Brazil to explore programming language features and the benefits of thinking about languages in terms of labels — fundamental language features — rather than paradigms, such as object-oriented or functional languages.
Does thinking in terms of labels help you adopt different programming styles? Can focusing on labels make language syntax less daunting? Can you have too many labels? Listen in to hear the team in exploring new ways of thinking about language choices.
**Podcast Transcript**
Alexei Boas:
Hello and welcome to the Thoughtworks Podcast. My name is Alexei and I'm the head of tech for Brazil and I'll be one of your hosts this time together with Rebecca Parsons. Hello Rebecca.
Rebecca Parsons:
Hello Alexei. Hello everybody. My name is Rebecca Parsons and I'm the chief technology officer for Thoughtworks and one of your co-hosts on the Thoughtworks Podcast.
Alexei Boas:
And we are here this time with Luciano Ramalho. So Luciano, it's a pleasure to have you with us. Would you mind talking a little bit about yourself?
Luciano Ramalho:
Well, thank you very much for having me, it's a pleasure to be hanging out with you guys again. So my name is Luciano Ramalho, I'm a principal consultant at Thoughtworks in Brazil. And I guess my main to fame before I joined Thoughtworks in 2015, was that I wrote a book called Fluent Python and people who have read that book have probably noticed that I have a lot of interests in other languages besides Python because I mentioned... I often will compare Python features with other languages. Sometimes I find the pattern feature better than most other language, sometimes not. Sometimes I think I am mentioning features of other languages that I wish Python had. So that's a little bit about me.
Alexei Boas:
It's good you mentioned Python features because I guess we're here today to talk a little bit about language features in general. And if I remember correctly, it all started with a provocation say is Go objects oriented or functional and then you started talking about language paradigms and well, they might be a little bit outdated these days. So what are your thoughts on that Luciano?
Luciano Ramalho:
Yeah, so I was part of a conversation that had to do with the issue of what kind of design patterns can you use in Go and whether some functional programming style makes sense in Go or not. And then I started thinking about that it is a funny thing about my biography is that I have a degree in library sciences that I took because I became interested in this subject of information architecture around the time of the web bubble. I was developing... I was working with very large news portal and in my library sciences course, one thing that I learned was the distinction between ontologies that are [inaudible 00:02:24]. and other classifications, systems like a tag-based classification systems and then I realized there are a lot of discussions that I had read that were interesting about design patterns.
Luciano Ramalho:
The most intriguing points of view were informed by this opinion that the best way to think about design patterns is not whether your language is object-oriented or not, but more specifically what kind of features it implements and then features sort of become like labels. So a certain language for instance, going back to the original question is Go object-oriented or is it functional? It's neither, it's a very pragmatically designed language. The designers of Go we're not thinking about doing an exemplary object-oriented language, but it has features of object-oriented languages and it also has features of a functional programming languages. So the features are the key I think.
Rebecca Parsons:
Well, I think an interesting part of this too is that as soon as you get out of pure languages, language paradigms are meaningless. But the features that are generally associated with the pure language in a particular paradigm, they do help describe what kinds of things are easy to implement or difficult to implement. And of course we get into this whole question of as long as a language is turning complete, you can write anything in any language.
Rebecca Parsons:
It's just more difficult than others. I've actually written a text editor in Fortran and that's not very easy to do. I wouldn't advise it, but it was the only language that worked on that particular machine at that particular time. And so I think that by talking about these language features, we can start to get to a point of thinking about when would you use the language? And I'll ask you a question that I get asked lots Luciano, is there the perfect language and if so, what is it?
Luciano Ramalho:
Well, the first answer is of course, no. But it's funny because some people like for instance, Paul Graham that is now well known as a venture capitalist with Y Combinator, but he's actually probably one of the few people in the history of mankind that became very rich programming in Lisp. And it's obvious if you read many of his blog posts that he thinks that Lisp is the perfect language and maybe if there is a language that can claim to be the perfect language, it is Lisp because of the fact that it's so extensible because it has syntactic macros. So it's so extensible that you can really... And that's why it's the favorite playground of language theorists, right.
Rebecca Parsons:
I would assume that it's Scheme rather than Lisp, but it's the same general idea.
Luciano Ramalho:
Yes, totally. Yeah.
Alexei Boas:
Yeah, that's great. Also in my view and going back to the paradigm versus label thing, I think thinking about labels instead of paradigms also lends itself better to different programming styles. And even you don't have the ideal language to a task, but using the language in different ways and using the key features to specific tasks that you have. For example, nowadays if you have data intensive applications using vectorized styles make a lot of sense in specific contexts and settings, et cetera. And thinking about labels I guess gives you more flexibility and freedom to think in different mediums depending on the task that you have. So...
Luciano Ramalho:
Oh yeah. And I remember something that Rebecca said about Haskell when we were preparing this... Remember what we were-
Rebecca Parsons:
Yes, I get very frustrated when people emphasize either the strong typing or the pure functional nature of Haskell. But to me the thing that distinguishes Haskell is laziness. And when we think about how to solve problems, solving problems in a lazy language is very, very different than if you have a strict language. There are things that you simply can't readily express without effectively building the construct of laziness into the language if you don't have laziness. And to me just focusing on either the type system aspects or the functional aspects and monads and such of Haskell really misses that truly powerful feature. And I would really love more people to be talking about and thinking about how to exploit laziness particularly in things like data intensive applications.
Luciano Ramalho:
Yeah, totally. Yeah, and it's interesting because there is another language feature that is kind of associated with laziness, at least it's the way lazy evaluation is implemented there at a low level. That has to do with generators and streams and that's something that's emerging as a popular feature in several languages. And that is being leveraged more and more with another kind of data thing, civil application, which is applications that are dealing with constant streams of data coming in and out. Which is the way that laziness works, but we don't have the same kind of a lazy evaluation in other languages but the underlying constructs, the low lower level constructs for instance, coroutines and so on that allow that to work is becoming increasingly available in other languages.
Alexei Boas:
Well, the ability to express an infinite set with a sheer construct is definitely very useful in specifically in data intensive applications. But then so we mentioned laziness, is that an example of one label for example? So is that what you're talking about or do you have other examples and...
Luciano Ramalho:
Oh yeah, totally. That's a very good example. Another example that is I guess closer to most people is the idea of first-class functions, which is something that for instance, in the Java language it took a long time to arrive. I remember watching a presentation about 10 years ago where somebody said, "Okay, so this is the list of the 10 most popular JVM languages and the only one that doesn't have first-class functions is Java." Because likes of Groovy has, Clojure has, Scala has, Kotlin has and in other languages like Python, Ruby. But anyway, one thing that I went to give as a reference to our readers is to look up a presentation by Peter Norvig who's a professor of computer science at Stanford. He has a presentation deck called design patterns in dynamic languages where he talks about features and how they relate to design patterns.
Luciano Ramalho:
And for instance he says that if your language has first-class functions, then you have to rethink some of the classic design patterns. Like for instance, the strategy design pattern, the command design pattern become much simpler when you can pass around functions and it's something that now we have with Java 8 as well. So that's one example. So first-class function is another label, laziness another label, streams another label, so that's the idea. I think we should start talking more about these principles that are fundamentals that when you understand a principle like that not only you have a better grasp of a specific language that you're using, but then you can make better decisions about the programming styles or design patterns that you can use. And it also helps you a lot when you're going to learn the next language because then you recognize and so okay, so that's that label that I already know and this language also has that so I can apply that.
Rebecca Parsons:
Yeah, I think that's important as well by focusing on the features, what design patterns, how do you use particular design patterns and languages with particular labels. It gets us away from thinking about the syntax of the language. And I've seen so many people who struggle with moving from a language like Java to a language like C# when it shouldn't really be a struggle because these are primarily syntactic differences. Yes, of course the ecosystems are very different, the libraries that are available might vary, but the language itself, they share many of the labels.
Rebecca Parsons:
Now, they've been going in not quite lockstep, C# evolved as a language more quickly for a time than Java did vice versa earlier in its history. But there are a lot of similarities between those languages. And if we focus too much on syntax then we're really boxing ourselves into a language and it makes it more difficult to think about, okay. Well, let's learn Kotlin and let's look at what those language features are and get away from this focus on syntax. Syntax is incredibly important for the ease of writing and reading a language. But if you're going to learn a language, personally I think you should learn it on that label level. And the syntax is just an implementation detail as we are learning a language. It's critical when you're designing a language, but it's an implementation detail when you're learning a language.
Alexei Boas:
Yeah, and I guess the one good thing about labels is that it forces us to think one level down from paradigms at least, right? For example, can we say that object-oriented is a label or would we say that inheritance is a label and then you can have... Or even things like reflection and things like that. So it forces you to look at a lower level and then you can combine them in different ways and once you have an understanding of those basic labels, you can pour the learning or the concepts that you have to different languages. Does it make sense?
Luciano Ramalho:
Yeah, totally. I think object-oriented maybe is too big as a label because it's usually one of the so-called paradigms, right? But if you think what people mean when they say object-oriented, that's a collection of labels. But sometimes like for instance, let's talk about a label that's probably the first one that occurs when you talk about object-oriented which is inheritance. And it's interesting because there's been a very clear trends away from inheritance as a central mechanism at least implementation inheritance. So even in the design patterns book which is from 94, they have the introduction which is I think is the best part of that book. They only quote two design principles, two object-oriented design principles that the authors propose in that introduction and the two are program to an interface not an implementation and favor object composition, overclass inheritance.
Luciano Ramalho:
And if you think about for instance again Go, which is a modern language designed by people who have a lot of experience designing other languages before Go, it has this object concept you defined types that have methods, receivers and so on. And it has interfaces but it doesn't have inheritance of any kinds. And it actually has a mechanism of composition where when you embed the type in other, methods of the embedded type can appear on the surface of the other one without you having to write code to do that. So the delegation is sort of automatically done. And I actually found a quote that somebody watched Ellen Hollow who is an author of several object-oriented programming books.
Luciano Ramalho:
He said that he watched... He was at a meet up with James Wozniak where somebody asked what is a feature that he would live out if he was to do Java again and he said classes. But then after people stopped laughing, he explained what he means was implementation inheritance. He likes interfaces and interface inheritance but not implementation inheritance, that's it. So something that he said maybe he wouldn't do again. So that's an example of one label that people promote is like the most important feature of object-oriented programming and maybe it's not such a big deal and maybe it's overused and people should start thinking about other labels that are associated with object-oriented programming that are more useful.
Rebecca Parsons:
Yeah, I would definitely agree. I see object-oriented as a collection of labels because it is too big. And when you think about a language like Smalltalk versus a language like Java, how you think about objects are a bit different. And saying that there is one label that... Yes, there are common characteristics, but there are a lot of differences between those languages and so I think it allows us to have a more precise and useful conversation if we say actually object orientation, functional dynamic, all of these are our sets of labels of which you might have different, potentially overlapping sets.
Luciano Ramalho:
Yeah, I agree. I think it's useful to think of the sets of labels that our language has instead of focusing on the sets that define a paradigm because that's really not very well defined. But when you think about the set of labels that our language has... So I guess we're kind of in this podcast introducing terminology because we are using the word label over and over again. And what we mean by that is a shortcut for language features like fundamental language feature. But it's cool. Maybe we are inventing this terminology now. So this is what we mean by the acquisition between paradigms and labels, yeah.
Alexei Boas:
And I think I won't resist asking this. Can a language have too many labels? Scala comes to mind so can that happen or?
Luciano Ramalho:
Oh yeah, yeah. I think those are two examples of my opinion languages that went overboard in adopting features. And one consequence of that, that I see people mentioning in large organizations that use those languages is that because the languages are so big and have so many features, people tend to focus on the features that they understand better. And in teams actually developed dialects which are subsets of the language. But then in a larger organization you may have different teams using different dialects which creates problems when you move people around. Have you seen that Rebecca?
Rebecca Parsons:
Yes, although I think even in a simpler language setting you can still have that problem when you have teams that agree if we see a problem like this we are going to use this particular implementation style. But I do think it is more problematic in these languages with too many labels. And I think also that you end up with more power than you necessarily take advantage of. And in my experience, just like if you're using too powerful of a message queue or anything like that, anything where you have more things available than you use, you're introducing drag.
Rebecca Parsons:
It's a form of technical debt and so if you're going to adopt a language like that, you want to adopt it for its full feature set, not just say "Okay Scala looks enough like Java that I'll just write Java code in Scala syntax." You really want to say I'm adopting this language because it gives me things in addition to what I could get if I was using Java. And very often we don't have those kinds of conversations. It was the same thing with C and C++ it was supposed to ease the transition for people writing C into C++ but getting object features and you ended up with a language of that just had everything.
Luciano Ramalho:
Yeah, and it's interesting because again, talking about Go is a language that is very pragmatically designed and it's a reaction to C++ they say that in some of their design documents. And most complaints that people have about Go, is that it lacks features. Nobody complains that Go has too many features.
Rebecca Parsons:
Now what I will say about Scala though is when you're looking particularly now at a language choice, you're looking at an ecosystem as well and the ecosystem that has been built up around Scala is significant and I think that's something that we really need to take into account as well. There may be more things in the base language than programming language purists like you and I would want but it's got a very powerful ecosystem around it and I think that's something particularly when we think about labels, we might want to extend this notion of language labels to the ecosystems. Is there a ready implementation to support streaming or to support messaging or things of that nature. And that's something that back when we were worrying about COBOL and Fortran nobody ever thought about in fact it really started around C++ with the rich libraries that were built up around C++ when we had to start thinking about language ecosystems.
Luciano Ramalho:
Yeah, and this is the most amazing thing about the Java ecosystem of which a Scala is a part, but it also because of the features that Scala implements it grew the ecosystem in ways that maybe people were just using Java it wouldn't have gone because there were things more difficult to express for instance. Like stream for instance, which is now it feeds back into Java. I agree the ecosystem is super important.
Alexei Boas:
It looks like we could have a separate episode on ecosystems then. Okay, I guess then this brings us to the end of the episode this time. It was great conversation and great to have you with us. Thank you very much for joining.
Luciano Ramalho:
Well, thank you very much Alexei and Rebecca.
Rebecca Parsons:
Thank you both. I've always loved to talk about programming languages.
Alexei Boas:
All right.
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