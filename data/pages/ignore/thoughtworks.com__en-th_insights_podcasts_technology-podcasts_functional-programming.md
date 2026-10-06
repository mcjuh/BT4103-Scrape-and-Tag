<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/functional-programming | Title: Getting to grips with functional programming | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Getting to grips with functional programming 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Alexey Boas | Podcast guest  Gregorio Melo
November 14, 2019 | 26 min 53 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/functional-programming#transcript)
Listen on these platforms
## Brief summary
Any developer that’s moved from an object-oriented language to a functional one knows how disconcerting the shift can be. It demands a completely different mindset. In this episode, our regular co-hosts Neal Ford and Alexey Villas Boas talk to Gregorio Melo about functional programming. He’s just written a book about functional programming, using Clojure as its basis. Together they explore why developers choose to learn functional languages and how they can make the learning curve less daunting.
**Podcast Transcript**
Alexey Boas:
Hello. And welcome to the Thoughtworks podcast. My name is Alexey. I'm the head of technology for Thoughtworks Brazil. And I'll be one of your hosts this time together with Neal Ford. Hello, Neil.
Neal Ford:
Hello, Alexey. I'm one of your other regular hosts, Neal Ford, based out of Atlanta, Georgia.
Alexey Boas:
And this time we'll have Gregorio Melo. Hello, Gregorio. Would you mind introducing yourself?
Gregorio Melo:
Hey, Alexey. Hey, Neal. Thanks for inviting me. Yeah. I'm Gregorio Melo, also known as Greg. I'm a software development consultant at Thoughtworks for the past eight years. And I'm looking forward to my sabbatical.
Alexey Boas:
How cool. When's that?
Gregorio Melo:
It's in two years time.
Alexey Boas:
That's wonderful. We're here to talk a little bit about Clojure functional programming. You just published the new book. Is that so, Greg? Unfortunately, it seems that, for the time, it's only in Portuguese. Let's hope that's not the case for long. What's the title of the book and what is it all about?
Gregorio Melo:
This year, I finished this personal project of releasing a book on functional programming that consolidates the way I learned the concepts around it. And it's called Functional Programming: An Introduction with Clojure. And it covers the basic concepts. And it tries to provide newcomers to functional programming, provide, a very low barrier to entry to functional programming concepts. And we cover things like high order functions, and function sets, first-class citizens, and other stuff that we normally see in many of these languages that provide functional features.
Alexey Boas:
Oh, that's cool. It's part of your learning journey that you're sharing with everyone. That's cool. Well, functional programming, many people have been talking about that. And what's your view on that? What's the current state of functional programming? Why is it more popular now in your view?
Gregorio Melo:
Yeah. One thing that, back in, I don't know, when I was a student, 10 years ago or so, I remember a professor of mine saying that we should study and learn some functional program, because our computers had more than one core, more than one processors in the computers. And the way we were working with programming languages wouldn't make use of these computing resources. And over time, computer resources over all have become cheaper. And most of the tooling around functional programming has evolved as well so that some of the stuff like managing state has also improved. And compilers have optimized a lot of the code that are produced at the end. And we see big companies adopting functional programming languages not so early but five or six years ago, you see the move from [Tea 00:03:08] and moving to Scala. I think that provide that huge hype. And of course, hype is very relevant when people are adopting a programming language. And you see Swift and Kotlin publicizing that they are functional programming languages.
Neal Ford:
Okay. You've said the Scala word. Why did you choose Clojure as your exemplar language for this book?
Gregorio Melo:
It's an interesting personal story. I have to bring to the table that I don't have a strong preference between Scala and Clojure. Because I see there might be room for either one or the other depending on what you're doing. But in 2014, I guess, I was in China working for a real estate agency and consulting for it. And we were doing Scala development. And I was new to functional programming back then. And I remember that my mind was still working in the object oriented mindset and I was bashing the keyboard trying to make the compiler work. And we had very good colleagues that knew functional programming that could teach us. But sometimes, we were on our own. And the mindset just didn't work.
Gregorio Melo:
And I decided to take a step back, learn the basics. And given that Scala is a hybrid language, and you can do object oriented stuff and functional programming stuff, sometimes, you end up with code that allows you to do stuff that you probably shouldn't be doing. And Clojure is very opinionated on this end. You wouldn't do object oriented programming on it. And I chose it so that I could focus on the functional aspects of it.
Neal Ford:
Yeah. I think that's interesting. Scott, one of our colleagues, said, at one point, he thought that Scala was too flexible. Because there are too many unknown ways to make the language and bend it with all these different mechanisms. But I think there's actually a deeper... I'm also a huge fan of Scala or rather of Clojure and have written code in both and have written a book about both, but I'm a huge fan of Clojure. And I'm curious to have your opinion about this as well. I believe that the programming language style like functional and dynamic versus static typing is much more a reflection of an individual versus an objective assessment about the capabilities of a particular programming language.
Neal Ford:
Because some people are great graphic artists. They can draw things. Some people are great painters. I can't do either of those. But some people are photographers. I can photograph things and I can write. These are all different creative media. And I think a programming language is also a creative media. And I think different people lean toward different programming styles. And I think Rich Hickey, if you gave him Scala, would be miserable. And if Martin Odersky, if you gave him Clojure, he'd be miserable. If you gave each of them their media, I think they'd be very happy. I think part of adopting a language, a functional language, or any language, is finding the sweet spot for the way that you like to express yourself creatively and find a language that amplifies that rather than something you have to fight with.
Gregorio Melo:
Yeah. I feel it's definitely a personal take on which language you choose to work with. I'm on the dynamic type languages team. I know that a colleague, that recently left my team, he's very keen on Scala. But we decided not to argue with one another about this.
Neal Ford:
That's probably for the best.
Gregorio Melo:
True. And I feel that I'm very opinionated on desk driven development. And maybe I'm not convinced that I should trust that much that if my program compiles, it will work. And I want more tooling. That's not just it. I will avoid regressions. And given my personal preferences on all the things combined, I lean towards Clojure.
Neal Ford:
Yeah, I think arguing with a colleague about Clojure versus Scala is like arguing which is better: novels or poetry? Well, it depends greatly. But I think you brought up an interesting thing in the Clojure world. I agree. I'm a huge fan of TDD as well. But in a lot of the Clojure community and a lot of the Lisp community, a lot of development and experimentation is done via the REPL rather than by test. And while I think it's a good thinking media in the REPL. I fear that not enough Clojure developers take that learning and capture it as a test before they move on. Because the great thing about interacting in a REPL is you can find out exactly what you need right away. But if you leave that and if you let that work entropy into the universe, and you've lost the regression of that. I actually think that Clojure works best when you use the REPL like that and then capture that as a unit test so that you can regression all those things after the fact.
Gregorio Melo:
Yeah. I think developing with the REPL is an amazing opportunity for us to code quickly, experiment quickly. But you mentioned regression. I think, for me, that's the most important thing, the most important reason why I'm doing TDD. I like the aspect of how you can develop an... The architecture that you end up with is more flexible or it's some sort of documentation, leaving documentation. But the regression part of it, avoiding regression's part of it, for me, is the most relevant stuff now.
Gregorio Melo:
One thing that I wanted to go back a bit when Alexey asked about Clojure. I could have learned with other languages as well. But I noticed that my life was tending toward JVM for the rest of it. And then, I decided to pick one that was running on top of JVM as well. That's it. And then, back to the REPL stuff. One thing that is very nice about the REPL, and in this Scala debate I think it's worth mentioning, is you can connect a development environment with the REPL. And the speed of the feedback that you get, how fast the feedback is, is amazing. You are coding stuff in your editor and you quickly see the output of the logic you are developing. That's pretty awesome.
Neal Ford:
I'm glad you mentioned that. Because I know a lot of our colleagues, who are serious feedback junkies who really want super fast feedback when you make a change to code and want to see that reflected in tests and output right away, really love Clojure. Because you could really wire up a Clojure environment that hot loads and is receiving really almost instantaneous results whether it's in a REPL or even running things like, incrementally running, unit tests and those sort of things. You can set it up as an environment that really leans towards super fast feedback.
Alexey Boas:
Yeah, that's interesting. You were talking about personal preferences and etc. It's also interesting to see many languages incorporating some of the functional aspects and functional tooling. We had one other episode that we recorded with Rebecca Parsons and Luciano Ramalho, the author of Fluent Python. And he was talking specifically about the death of paradigms, language paradigms, and how it's much more useful to think about maybe language features instead of a straight classification and trying to use that. Because languages have become the combination of the different features that they have. And I think that connects a lot to the personal preferences that people have. And it also plays to those choices that we have to make.
Gregorio Melo:
Yeah. I also like this take on talking about features instead of the paradigms. Because one thing that is really, really hard about functional programming is explaining what it is. And once upon a time, I heard that there is actually a curse that whenever you learn and you understand what functional programming is, you just cannot explain to anybody. That's the curse. You learn but you cannot explain.
Neal Ford:
You go so deep down the rabbit hole that you can't see out the top anymore.
Alexey Boas:
Yeah. That's interesting. How is the learning process of learning functional programming? Do you feel it's a steep curve? Do you feel it's something easy you can build on experience you have to restart from scratch? How was your experience?
Gregorio Melo:
If you're an experienced programmer, the learning curve might be... It might take you a while to feel comfortable developing that way, learn the functional programming concepts. I feel it's just like learning the very first language. When you're starting with C, for instance, and you have to learn what the pointers are, of course, I don't even remember what they are, now, but when you learn about declaring functions and doing loops, the first time you learn about recursion, that's difficult. Because that's a concept that you're developing.
Gregorio Melo:
When you come to functional programming from a different background, I think the turning point, at least for me, was when it came to my mind that most of the problems I would solve using recursion and accumulating results and pressing to the next execution of the function that I'm recursing upon. I think that was the turning point for me. Might be the turning point for a lot of people. But the thing is, just for those learning or they plan to learn functional programming, just take it easy. It's going to be a new thing for you. It's going to be new concepts. And just remember the first time you learned programming. When you understood what a class is, what an object is, that took a while, I guess.
Neal Ford:
The way I think about learning a functional programming language is, most of the time when you're learning a language, like when you move from C to Java or Java to C#, it's basically a lateral move. Because they have more or less the same behaviors with some nuance. If you move from Java to C#, you write Java code in C# at first and then you gradually become a C# programmer. But that's more difficult when moving paradigms from an object oriented language to a functional language. Because you're not moving laterally. You're moving vertically. And it's very difficult to write your old school Java code in Clojure or Scala for that matter. Because the paradigms don't match. I think recursion is actually a good example of that. Because when you're a new programmer, recursion is one of those things that was just mind blowing for a while. But then, you got your head around it and understood it. And it's like, "Oh, okay. That's a tool in your toolbox." And I think a lot of the functional programming stuff is exactly that same way.
Gregorio Melo:
Yeah. And then, you're used to, say, looping through a list and modifying values within this list. Now, you come to this programming language that has this concept of immutable data. And you're not supposed to change... You don't have variables anymore. You don't [inaudible 00:14:50] anymore. What? It's a different world that you're going to live.
Neal Ford:
Yeah. One of the most mind blowing things that happened to me in university was I took a language survey course. And the first language was Eta which is very strongly typed. And then, it was C which is basically compile a phone book. And then, they switched us over to Scheme which is a dialect of Lisp. But when he told the class there's no such thing as variables, everybody's head just exploded. Because we were so used to all these other languages and paradigms. There's another thing that you brought up before, I think is quite interesting, that a lot of languages like Groovy and Kotlin are adding functional features and becoming hybrid languages sort of like Scala.
Neal Ford:
But Clojure's very decidedly not trying to become a hybrid language. It is very true to exactly what it wants to be. And Rich Hickey, the creator, is very opinionated about what it is and what it won't be. And that's actually, to me, one of the appealing aspects of Clojure. I actually say that Clojure... The two languages I think I probably love the most are Ruby and Clojure to build things in. And I say that Ruby maximizes developer happiness, sometimes, to a pathological degree. Because it bends over so backwards to make it friendly and easy for you that you could build yourself into a mess. Whereas Clojure maximizes engineering happiness. Every decision in Clojure seems like it defaults toward the good engineering decision like immutability, the way that all the looping stuff, and the things they've added on top of it like transducers. And it seems like a language that leans into good engineering practices and doesn't seem interested in expanding in a lot of ways that would chip away at that overriding philosophy.
Alexey Boas:
Yeah, good. And Greg, how about the writing process for the book? How was it? At least my personal experience, that's what everyone says. It's hard to do. What would you do differently if you were starting over right now? What have you learned in the process?
Gregorio Melo:
There is one skill that I disappoint everybody with. That's routine. Over my career, I've learned to do planning. And I planned to develop this book. That was pretty awesome. I think I aced the planning comparison with how it was the year before I proposed the book. But that part wasn't the easiest one. I came up with the summary of what I wanted to talk about. And I developed an introduction of what I expected people to learn from that book. I proposed to the publisher in Brazil. It was accepted quickly and I started developing.
Gregorio Melo:
But the thing I wouldn't do again was to do the bursts I did on writing. One day, I would write for four hours after working. Because I felt like in the mood. And then, I would stay like 20 days without. I would spend 20 days without doing any sort of writing. And I think that's when you lose the... And I feel it's also a practice. If you do martial arts, if you do any sort of musical instrument, as well, it takes practice. And you need to do that deliberate practice that we talk about and we hear a lot out in the world. And writing, if you wait 20 days to write the next five paragraphs, that's a huge force that you have to use to push you out of inertia. One thing I would do is write more paragraphs every day or every other day.
Neal Ford:
Now, one of the good pieces of advice I read from, I've read several books on writing, which is an interesting meta category for writers, but one of the great pieces of advice I heard toward that is, always stop in the middle of a paragraph. Because one of the hardest things when you sit down is breaking the inertia. And if you stop in the middle of a paragraph, you know how to finish that paragraph. And that starts you writing. And it's easy to flow into the next paragraph. Always stop once you know the next thing is going to be. Because that greases the ability to get started again. But you mentioned routine. I think that is the most critically important thing for writing and coding as well. The more you do it, the better you get and the more natural it seems. And that is the Achilles heal for just about every writer I know is being able to establish a good consistent cadence for getting writing done. And yeah, it is the best thing you can possibly do.
Gregorio Melo:
Yeah. And I would probably misquote someone I don't remember who said this, but motivation, inspiration, they come from nine to five, 9:00AM to 5:00PM, sitting down and writing at that time. Eventually, the inspiration will come. There is also this thing I tried, and I think it was good. Was to constantly ask for feedback. I asked a lot of people to look at the drafts I had and provide feedbacks. And I got people from various background. Someone with a deep knowledge in Clojure provided me good technical insights. Someone that had no understanding of functional programming provided me really good insights on the book. That's something that you never should forget. And it's very easy to go crazy and decide to talk about everything. When ideating about the book, I wanted to add how to dockerize Clojure applications, how to write databases, and deploy to Heroku. And I would add too much stuff that, one, would go stale very quickly, probably, and another one, that it would take time that I could be invest in explaining a bit better the more important concepts and was the core scope of the book, actually.
Neal Ford:
Yeah. You said, when we were doing the prep, that you were really good about defining the summary first thing and then constantly going back and reconciling your writing against that. That's really impressive to me. Because I'm so bad at that. I really want to do that. But I really am terrible at that. Kudos for being able to do that. What I do, instead, is come up with a summary and then write and wander far afield and, then, eventually, just rewrite the summary. I think it takes a great amount of discipline to stay on task like that. But you're right. There's so many topics that you could get distracted by shiny things that keeping to task is-
Gregorio Ford:
Yeah, thanks. And I actually removed some good amount of stuff that was in the index. I wanted to talk about bringing the functional programming patterns and how you could apply patterns in how your object oriented partners would change when you apply the learnings in your day-to-day world object oriented language and compare that with Java. That would take a whole, I don't know, five chapters. And one thing that I almost got lost into, adding to the book, was spec. Spec was, I guess it was, released right at the moment that I was very motivated into writing. I don't know. At the end, I feel it was a good thing not to add spec to the book.
Neal Ford:
It is a fascinating thing. If people are interested, haven't heard of closure.spec, you should look into it. Because it's a way of optionally adding typing. But beyond typing, ranges and other sorts of validations but selectively to Clojure data structures. It's a very cool thing. I would never have been able to resist writing about it, I don't think. As a good way of summarizing that, when you look back on the book, if you pick this book up and someone else wrote it and you read through it, what's your fondest part of the book? What's the thing that you think, that when you set out, the thing, that you were most successful with. What's the thing you're proudest of that came out of the book?
Gregorio Melo:
I think it was coming up with problem domain and working up Clojure concepts data structure, for instance, and not using basic math, arithmetics, but actually working with maps that had different values on it and, then, making transformations and applying partial functions on top of this data. I'm biased, of course. But that's the second part of the book. And you start with a very basic problem domain. And then, you convert US dollars to Chinese yuans. And that's a concept that comes later in that part of the book. Yeah, trying to summarize. I think that using Clojure with a reasonable problem domain.
Neal Ford:
Yup. Coming up with a unified sample's always a tricky thing. It's a good skeleton to base a book on.
Gregorio Melo:
And one thing I wish I did, and there was one thing I removed from the book, was the exercises. That was a tip I got from Luciano Ramalho. I think it makes a lot of sense. But I decided to write the exercises a long time after the chapters were done, some of the chapters. Now, I would think about the exercise for the chapter later. And then, I lost the train. And I had to remove some of that I had. I wish I had added exercises. Because I think it would help those learning, yeah, to experiment with whatever they just learned.
Alexey Boas:
Yeah. In my experience, it was really surprising to realize how much work it is to come up with exercises and build the exercises. It's a lot of work. Even if you don't provide the answers, it's not just asking questions. You have to go through them and see that you have explained everything that's necessary for the solution and things like that. It's a lot of work, in my experience.
Gregorio Melo:
Yeah. The exercises have to make sense for the end.
Neal Ford:
Well, that's awesome. Well, congratulations on getting your book published. I know it's an enormous amount of work. And it's great to get it out there. And even more so that it's such one of my beloved subjects which is functional programming and Clojure.
Gregorio Melo:
Yeah, thank you. We did releasing event at Thoughtworks San Paulo on Wednesday. And I recommended one of your books, Neal, to the folks that wanted to learn functional programming, that Functional Thinking. Right? That was one of the books I used to learn the functional programming concepts. That helped me a lot.
Neal Ford:
I appreciate that.
Alexey Boas:
Okay. It was a great conversation. Thanks a lot for joining us, Greg.
Gregorio Melo:
Thank you. My pleasure. Thank you, Neal. Thank you, Alexey.
Alexey Boas:
And on the next episode we'll talk to Alexandre Goedert, head of technology for Thoughtworks Chile. And we'll talk a little bit about the challenges of giving life to a cloud migration strategy. Hope you'll join us for this conversation.
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