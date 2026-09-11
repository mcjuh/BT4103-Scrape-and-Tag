<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/future-python | Title: The future of Python | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The future of Python 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Mike Mason | Podcast guest  Luciano Ramalho
April 30, 2020 | 33 min 27 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/future-python#transcript)
Listen on these platforms
## Brief summary
The increased emphasis on machine learning in the enterprise also seen resurgent interest in Python. What makes Python different from other languages? What are the main features that make it unique? And where will Python go from here? In this episode, our podcasts chat to Luciano Ramalho, from Thoughtworks Brazil — a renowned author of books on Python — about dunder methods, fast fails and what’s new in the upcoming second edition of Fluent Python.
**Podcast transcript**
Alexey Boas:
Hello and welcome to the Thoughtworks Technology podcast. My name is Alexey, I'm the head of technology for Thoughtworks Brazil, and I will be one of your hosts this time together with Mike Mason. Hello Mike.
Mike Mason:
Hello Alexey, my name is Mike and I'm a global head of technology here at Thoughtworks.
Alexey Boas:
And this time we're delighted to have Luciano Ramalho. Luciano is the author of the O'Reilly Fluent Python book. Hello Luciano, would you mind introducing yourself?
Luciano Ramalho:
Hello. Yeah, I'm proud to be a principal consultant at Thoughtworks in Brazil in the São Paulo office, and I joined Thoughtworks about four and a half years ago and I am now working on the second edition of my book as well as helping with other things at Thoughtworks such as preparing our great X-conference that's going to happen in April in São Paulo and other things.
Alexey Boas:
Oh, that's awesome. Well, looks like very good timing for us to talk about Python then since you were working on the second edition of the book. And now, Python has featured in our own Technology Radar quite a couple of times recently and many of them connected to data. So maybe why don't we start there. So Python is quite popular for data. Why is that so Luciano?
Luciano Ramalho:
Well, that's very interesting because I've given it a lot of thought. I think it's probably the main thing that has helped with Python's popularity recently together with another thing, the fact that it was even before data and Python or Python in the domain of data was so popular, many American universities, top universities like MIT and so on, adopted Python as the first language that they teach in their computer science programs and other programs. So I think those two things helped with the increase of popularity of Python recently. But the story of Python with data goes very far.
Luciano Ramalho:
In fact, just before I joined you here, I was looking at the history of the SWIG project. SWIG, S-W-I-G, is a system for generating bindings between C++ and other languages. It's mostly used by scripting languages like Python, TECO, Ruby, et cetera, to be able to connect with libraries written in C++. And SWIG was started by Dave Beasley. Dave Beasley is probably the most famous Python speaker and book author in the world. And Dave started SWIG in '95, so only four years after Python was released, and he was working at the Physics Lab. Initially, he was supporting another language, but then in '96 right in January, he released the first version that supported Python. So it's a long story.
Luciano Ramalho:
Anyway, since that happened, there was a lot of projects, scientific projects initially in the physics domain but then in other domains they started doing this integration between Python and libraries written in C++. And like I said, that happened a long time ago. And then suddenly what happened was when this new approach to artificial intelligence emerged that we call now machine learning, which is heavily based on math, when that came around, it turned out that Python already had everything that was essential for doing machine learning because of the work of the scientists with the language over the previous years.
Luciano Ramalho:
So I think that's one explanation. The fact that the libraries that people needed to do numerical computation, statistics, linear algebra, et cetera, were already in place, plus the fact that Python is an easy language to pick up, but it's not a toy language. It's a very powerful language that takes you very far. And so I think those are the two factors that made it popular in machine learning.
Mike Mason:
And machine learning and all this stuff that you can do with wiring up data pipelines and all that kind of stuff in Python is what has made it maybe more popular recently, but I mean what about beyond data? You were talking about it being ... you didn't quite say an easy language to learn, but you said it was maybe a friendly language.
Luciano Ramalho:
One of the things that I always felt attracted to Python was the fact that people use it for lots of things. There are other scripting languages that are more confined to certain domains, but Python is not like that. If you go to a large pattern conference like PyCon US, EuroPython, PythonBrasil, and so on, you're going to see talks about all kinds of different things. For instance, there's a lot of stuff happening in IoT, right? There is one alternative interpreter for Python called MicroPython that actually runs on microcontrollers. And so for instance, when a few years ago BBC launched a project called the Micro Bits, which is a tiny microcontroller with a LED display and a few sensors, sort of like an Arduino, but friendlier to get started. When that came out in Britain, they distributed that ... every student, I think of 10th grade in Britain got one of those Micro Bits.
Luciano Ramalho:
And the Micro Bits is programmable in Python, natively. And there's other things like Fruits, this company in the US that makes very interesting gear for playing with electronics and programming. They built on top of MicroPython and did a whole environment called a secret Python and now they're releasing one board after another that you can program in Python. So that's one example of a domain. But also in biotech, there's a lot of work being done in biotech for several years and ... of course web programming, right? Web development. It's important to remember that YouTube was built on Python and more recently, Instagram. It started basically as a Python. And those are two projects that we're able to achieve in a web scale, really global scale with essentially a Python code base.
Alexey Boas:
Cool. Well, that speaks for widespread use and several different applications. What about the language itself, Luciano? Of course, you're very passionate about the language. What is it in the language that you love? What are the main features that you feel are unique to Python and that make a difference and make it stand out?
Luciano Ramalho:
Yeah, well, there is several things. And in fact, recently I presented a keynote in China and another one in Brazil that was just about that. They were called the Beauty of Python, and in it I tried to pick up what I like most. And so one of the things is the fact that Python has the concept of an iterator built into the language at a very deep level. So the for loop for instance... remember when in Java, I think it was Java 1.5 there was the enhanced for loop, also known as the for-each loop. So Python was always like that. The for looping pattern was always that way.
Luciano Ramalho:
And it worked with a lot of native data structures that come implemented in the language. But it's also super easy for you to create your own data structure that will play along with the for-each kind of for loop that Python has.
Luciano Ramalho:
And by the way, when I was studying this subject for a talk a few years ago, I discovered that this idea of having the iterator Python built into the language is usually with a key word called yield that you put in a function that makes the function suspend and produce a result and then resume when needed. So that's how the functioning interacts with the for loop.
Luciano Ramalho:
Anyway, this was another invention by the great Barbara Liskov, did you know that? So the famous, Barbara Liskov of the Liskov substitution principle, she created the language along with her PhD students called CLU or CLU, and CLU was the first real language that had this idea of built-in iterator and the yield keyword. So the way Python does that is very similar to the way it was done in CLU.
Luciano Ramalho:
So another thing that I like is, I think Python is easy to learn because the syntax is very simple. There's a very good document in the Python documentation called, I think it's called PEP 3000 and it's about things that we are not changing Python 3000. That's like forever, right?
Mike Mason:
Like when we get to version 3000 this will be the same.
Luciano Ramalho:
Yes, exactly. Exactly. And one of the things there is that the parser is an LL(1) parser. So that's a very simple parser, And it means that the code developers, they want to be bound by a simple parser. Because if the parser is simple, then usually that means that the language is also easy to read. Of course, there's a balance there, right? Because the simplest syntax of a famous language is the Lisp syntax, right? Of the s-expressions. But that's actually a problem that's so simple that makes it hard to read because everything this looks the same and that's becomes a problem.
Luciano Ramalho:
But anyway, Python finds ... I think Guido van Rossum the creator of Python, now retired. He has a very good sense of finding the middle way between alternatives that may be too extreme. The syntax is simple so that makes it easy to learn. Another thing is the fact that the language has this idea of the special methods also known as the dunder methods because they are declared with two double scores in front and back, so they're called dunder methods.
Luciano Ramalho:
Anyway those dunder methods, when you reach a certain level of usage in the language, and that's basically the focus of my book is to bring people to that level. When you understand how the dunder methods work, then you realize why the language is so consistent. Because for instance, to implement something that is iterable, you implement a method called dunder iter. If you want to implement addition, the plus operator, then you implement a method called dunder add. And because those methods are pretty fines, they're pretty established in the language, everybody knows how to grow new things in a way that's consistent with the traditional ways and one-
Alexey Boas:
So like that you can use common language constructs and they are going to behave appropriately for different types of things. But you can read that quite easily because the syntax is familiar but it's behaving as it should for that specific case, right?
Luciano Ramalho:
Exactly, yeah. You know that wonderful feeling that you have when you're learning in some kind of language or framework that is very well designed and then you start making educated guesses and then you're right most of the time, oh, if that works with strings, maybe it works with this as well. And it does. And it works with result sets from a jungle query on a database as well. There's a lot of stuff like that in the language. So that's another thing that I like very much. And just to contrast, I don't want to bash any language but I like Go very much, but one thing that I feel that I miss when I'm programming in Go, is that Go has, for instance, it has a kind of a for-each syntax is called for range in goal, but that only works with five built-in types in the language. You cast yourself, make it work with your own data structures.
Luciano Ramalho:
So that kind of frustrates me. Python you don't feel like your constraints because pretty much everything that's built-in that's written in seeing the language you can emulate right in Python as well.
Alexey Boas:
Okay. So you're saying by is easy to learn. And you mentioned three things. So simple syntax was the first one. Examples like the dunder operator and bringing that consistent feel to the language. Is there a third one?
Luciano Ramalho:
Oh, here's the thing about the dunder methods is important to understand that somebody learning Python doesn't need to know that they exist, but they are already benefiting from them. Because of the fact that the way the language is structured for people who develop libraries and frameworks, it makes it easy for them to provide APIs that are consistent to the novice users. So the novice user doesn't need to know about dunder methods at all or operator overloading, we don't expect people ... we don't want to be doing that on a daily basis, but yeah.
Luciano Ramalho:
And so that's how I think the language is very well designed because it's simple to get started, but then you start uncovering other things about it and then you get other insights and then suddenly you become somebody that can do anything that the pros can do in the language because it doesn't prevent you for doing that.
Mike Mason:
One piece of it that you, you mentioned when we were figuring out what to talk about on the podcast, you said that fails fast.
Luciano Ramalho:
Oh, yeah.
Mike Mason:
Can you talk a bit more about that because I think that's something that might be useful to people?
Luciano Ramalho:
Oh, totally. Yeah. So I've always been a big fan of the so-called scripting languages. I don't like that word too much because it's usually used in a derogatory manner. But anyway, I've always been a fan of very high level dynamic languages. And one problem that many of them have is the fact that sometimes bugs are hidden, for instance, because the typing is weak. So JavaScript has that problem of doing crazy conversion. So you have to learn that you can never trust the equals operator. You have to use the triple equals because otherwise you're going to be beaten, right?
Luciano Ramalho:
Now, in contrast with pretty much every other scripting language that I've learned, Python has a more strict philosophy that we call fail-fast. And so for instance, one example is when you retrieve a value from a dictionary, right? You provide a key and then you want to get a value from the dictionary back or from the hash or mapping or whatever you call it. Anyway, every language, pretty much this days has this constrict, but in Python, if the key is not present, it raises an exception. Other languages give you something that's undefined or some default value like none, that sometimes will bite you later because you were expecting something, the thing wasn't there and you got this value so you didn't get an error and then you have to figure it out later.
Luciano Ramalho:
So another example is called the splat operator or unpacking. When you have several values that you want to assign in parallel or when you went to pass a list of arguments to a function, other languages, sometimes if you pass more arguments they will be silently discarded, if you pass not enough arguments, then if you assign some default value like undefined or none to the remaining arguments, Python doesn't do any of those things. It is strict in many ways where other languages let bugs pass. So I think that's very good. It's really a pleasure because you're working with this highly productive dynamic language, but a lot of bugs are easy to catch because of this characteristic.
Alexey Boas:
Cool. So you talked a little bit about the history of Python with the scientific community and some of the fundamentals that you love and that are cool and make it a joy to use Python. But what about the new and shiny Luciano? What's the cool stuff in Python? What's, what's the new things?
Luciano Ramalho:
Well, for us who work in big systems for our clients, for Thoughtworks clients, one thing that is probably a lot of people are going to welcome is the introduction of a static typing in the language. It's an optional thing, it's actually very similar to the way that TypeScript works and also Dart the new language that Google is using in their flutter framework. So the idea is that you're not forced to declare types and also that type errors are not caught at runtime and the type annotations have no effect at runtime. But the idea is you put those annotations and then you can use in your ... well, they help your ID to detect errors just by looking at the source code. And also you can put ... there are command line type checkers like my PI, there's another one from Microsoft and other one from Google.
Luciano Ramalho:
Some big companies have their own type checkers now, but they are now all consistent because the language adopted a standard syntax and semantics for doing that. And so you can put in your pipeline to have my Pycheck, do a static type check on the source code before I commit even. So that I think is something that's going to be big in the context where we at Thoughtworks work.
Luciano Ramalho:
Another thing is the ecosystem around data and scientific computing in Python and analytics and so on never ceases to amaze me. It's incredible. One thing is that's really super impressive is the Dask project, D-A-S-K. So Dask is a way for you to program in an API that is very similar to the NumPy API that everybody that uses Python for those things know. So they emulate part of the NumPy API, they are raised and so on. But they do it in a way that you can distribute the computation on clusters of machines.
Luciano Ramalho:
And I saw a demo of that in at a talk here in São Paulo and it was super impressive because the person who opened a Jupyter notebook and then was doing Dask computations and then he typed a special commands in Jupyter notebook and then suddenly a big chunk of the screen was taken over by a dashboard showing in real time the computation happening in the nodes. What nodes were idle, what nodes were busy so that you could reconfigure, maybe you had a pipeline with a several steps of map reduce for instance, and then you could graphically see that some steps needed more machines and other steps you could reduce the number of machines.
Luciano Ramalho:
So that's Dask and it's super impressive and it's all open source. One of the things that really I love about Python that I need to mention is that it's really open source language to the core. There was never a huge corporate backer in the history of Python that controlled it. And so it's a community project and the governance is very transparent and of course people in this domain of analytics and scientific computation have always had their voice. And that's why the language also adapted to their needs over the years. But I think it's a great example of a language that shows real open source governance that works.
Mike Mason:
That's pretty cool.
Luciano Ramalho:
Yep.
Mike Mason:
Those are some of the exciting things now. What about the future? You mentioned Python version 3000 earlier. Is there a new version of Python coming? Do we need to look out for that?
Luciano Ramalho:
Well, the switch from Python 2 to Python 3 was very traumatic. I started using Python in '98 when it was Python 1.5. So I went through the change from 1.5 to 2.0 and that was very smooth. Pretty much most programs just continued working with no problems. But in Python 3 they decided to fix some things that were very fundamental. The most fundamental things that they wanted to fix that was impossible to do without breaking backward compatibility was reorganizing the support of Unicode in the language because the strings in Python, the default string literals were not Unicodes and there was an alternative Unicode type in Python 2.7 that was okay, but it was not the default so people missed.
Luciano Ramalho:
Anyway, with that change, with what required breaking a lot of stuff, they decided to do other breaking changes and it took about 10 years for ... yeah, Python 2.7 lasted 10 years. It was frozen last January. Since January the community doesn't support Python 2.7 anymore. I think lots of vendors are still going to support it like Red Hat and other vendors because there isn't a huge install base. But anyway-
Mike Mason:
And what was-
Luciano Ramalho:
... because of ... go ahead.
Mike Mason:
Why were people stuck so long? Well, we've got all these libraries and frameworks and code bases and we-
Luciano Ramalho:
That's interesting. The first thing that took a long time was that people needed ... if I am an app developer, I need all of my dependencies to be compatible with Python 3, right? So I had to wait for that. So that took about five years, I would say for the main projects, even the whole universe of the NumPy libraries, the SciPy libraries and Django and so on, took them a few years to be able to release versions that supported both Python 2.7 and Python 3. But now, it's just the problem of priorities when you have a system in production and you have a ... yeah, maybe-
Mike Mason:
Do you think like ... sorry, do you think commercial language vendors have done any better on that? It would seem ... I actually don't know the answer to this, I'm just curious. Whether, for example, Microsoft has done a bad job on getting people to stay up to date on versions of C# or whether Java has done any better to encourage people to move to new versions. I guess it depends on whether there was a major breaking change like the one that you talked about.
Luciano Ramalho:
Well, I don't know. I don't follow those languages so closely anymore so, but let me just say that this whole thing, I think it's passed us, it's amazing that the language survived and even grew a lot during those years of troubles and recently I was talking about that on Twitter with some other people and actually quoted, Windu in one of my tweets and Windu came and said probably there won't be a Python four at all because there's no need for that. We are going to do incremental releases and then we can use just ... now 3.9 is in alpha and the next is going to be 3.10 and 3.11 and so on. So I don't think we're going to have ... the community sufficiently traumatized to not make that mistake again. Yeah.
Alexey Boas:
Okay, great. And how about the book Luciana? So you're writing a second edition of your quite popular Fluent Python book. We can mention that, right? That's not a secret is it?
Luciano Ramalho:
No, no, it's not a secret.
Alexey Boas:
Okay, fine. So why a second edition then? What's in this new edition? What are you working on?
Luciano Ramalho:
Well, the first edition came out in 2015 so although I focused on Python 3 at the time and it was Python 3.4 at the time, there were some things that most of ... almost every line of code in the book, in the first edition still works except for one part that was there asyncio library because it was provisional at the time. So I ran the risk of covering it because it was a hot new things, but because it was provisional and everybody knew that the API could change and it did change. And also the syntax evolved to become nicer. They introduced two keywords, async and await that are very similar to the similar keywords in C#. So they introduced those impact and then made all of that kind of asynchronous programming more readable. And so that was a major reason to do the updates. And of course, the whole new topic of type hints that did not exist at the time. So I think those are the most important changes in the second edition, covering type hints and talking about the new way of doing asyncio.
Mike Mason:
And just for people who may know have read the first edition, it's called Fluent Python, tell me more about your approach in the book in general.
Luciano Ramalho:
Yeah, so the book is aimed at people who already know Python. All right? Yeah, it's actually evolved from a series of courses that I used to present that were called Python for people who know Python. And so, the idea is, you know Python, you use it every day, but do you really take the most advantage of it? Because being an easy language to learn means that sometimes you don't study it so deeply because you can get away doing things in a simple way, but then often you're using it with a very strong accent from another language and missing things from the other language. But you don't know that there are other things that do the same things, but in different ways in Python. So that's the focus of the work and that's why it's called a Fluent Python. But it's-
Mike Mason:
I-
Luciano Ramalho:
Yeah, go ahead.
Mike Mason:
I can relate. I'm sure all my Ruby code looked like Java. [crosstalk 00:31:23] anyone who actually knew Ruby,
Luciano Ramalho:
Exactly, it a book is about idiomatic Python. And I think it was the first book in the market. I don't know if ... it was if the first book in the market that covered special methods in the first chapter because I assumed that you know Python, so here's something that if you don't know, you need to know so that you get a deeper understanding of all the language and why it's so consistent. So it starts with special methods, but then it goes all the way to meta programming meta classes. It gets really weird by the end. I really enjoy writing. It's one of my favorite things professionally.
Mike Mason:
Yeah, we are glad that you do because then we get those wonderful books, so.
Luciano Ramalho:
And I want to thank Thoughtwork sincerely from the bottom of my heart for supporting this because I'm working part time at Thoughtworks because they let me work on the book as well, so that's really great.
Alexey Boas:
Okay, Luciano, thank you very much. I guess we're coming to the end of the episode. It was a great conversation and great to have you with us. Thank you so much.
Luciano Ramalho:
Well thank you so much Mike and Alexey Boas. It was a pleasure talking to you.
Mike Mason:
Thank you Luciana.
Luciano Ramalho:
Bye-bye.
Alexey Boas:
And thank you all for joining and if you have any feedback for us, don't hesitate to reach out or leave a rating or comments on your preferred platform. Thank you so much for listening. Bye.
Neal Ford:
On the next episode of the Thoughtworks technology podcast. We're joined by two of our colleagues Prassana and Bharani to talk about the distinction between observability and monitoring and some good ideas of what to do and what not to do. So please join us on our next episode.
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