<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/fluent-python-revisited | Title: Fluent Python revisited | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Fluent Python revisited 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Ashok Subramanian | Podcast guest  Luciano Ramalho
January 13, 2022 | 55:35 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/fluent-python-revisited#trans)
## Brief summary
Ahead of the release of the second edition of his landmark book, Fluent Python, our team catch up with author Luciano Ramalho to hear about what’s happening in the world of Python — and why it’s popularity continues to endure.
### Full transcript
**Alexey Boas:** Hello, and welcome to the Thoughtworks _Technology_ podcast. My name is Alexey. I'm speaking from São Paulo in Brazil, and I will be one of your hosts this time together with Ashok Subramanian. Hello, Ashok, how are you?
**Ashok Subramanian:** Hello, Alexey. I'm quite well, thank you. Hello, everyone. I'm Ashok Subramanian. I am the head of technology for Thoughtworks in the UK.
**Alexey:** This time, we're very lucky to have Luciano Ramalho here with us. Luciano is a well-known speaker quite present in the Python communities worldwide. He's also the author of _Fluent Python_ published by O'Reilly. That book should be getting a second edition early in 2022. Hello, Luciano, it's a pleasure to have you with us.
**Luciano Ramalho:** Thank you so much, Alexey and Ashok for inviting me.
**Alexey:** Luciano, you've been involved and a big contributor to Python and to the community for a long, long time. We've all been hearing about how much Python has been growing in popularity over the last years. I'd be very, very curious to hear your perspective on that journey of Python and its popularity. How have you seen it grow? What's your personal perspective on that?
**Luciano:** Okay. My first job as a freelance software developer using Python I delivered in December of '98. I like to joke that I am a Pythonista since the last century. [laughs] It's funny because when we talk about language popularity, I have observed in my career that this is really a phenomenon that people have very different perspectives because of their surroundings. Each person has their own bubble.
Our bubbles are very strong when we talk about languages and frameworks. Since I've been using Python professionally since the late '90s, I know a lot of people using it. I've always known people using it professionally. Then you'll know a lot of about use cases and so on. It seems to you like the language is used everywhere. For instance, in 2006, I went to a Ruby conference. Then it was crazy for me to be in the middle of this other community.
That languages are very similar in many regards, Python and Ruby, but the perspective from the other community was very different about the relative popularity of the languages. I think Python took longer than Ruby to reach the mainstream in corporate software development. This is a loose term but let's talk about companies that are not necessarily technology companies, but uses of technology. In that area, or in that big sector of companies, I think Ruby had earlier penetration. Python was very important, for instance, in the sciences, early on, and also in the web world.
Google started using Python heavily. Google started using Python and C++. They were the main languages that they used and when they acquired YouTube, YouTube was basically a Python application when Google acquired it. There were important large-scale sites even more recent ones like Instagram that started mostly as Python applications. In the corporate world, Ruby, I think had deeper penetration, maybe because of its more orthodox implementation of object-oriented programming that appealed to people that were using Java, for instance, more than Python, that has some not so mainstream features related to object-oriented programming.
Yes, but now it's visible to everyone. The TIOBE index, which is widely quoted, Python has been a top-five language for 10 years there but now it has reached number one. Python is a top-five language in pretty much all the rankings that people mention, which is interesting to me. For me, for a long time, it was what I mostly saw around me.
**Alexey:** Yes, interesting. It's interesting to see the way Python grew in the scientific communities. It almost feels like it's growing inside a bubble and Python had a strong push from NumPy, Scikit and AI in general. Then when many of those things started being used by corporations in general, it feels like the bubble bursts and then there's a bridge between two different worlds, and it's quite interesting to see those things. I think those things happen in many platforms, and in particular Python seems to be one interesting example there.
**Ashok:** Yes, I think it's interesting looking at the Ruby example that you mentioned, because I think the popularity of Ruby as a language was driven more by the popularity of Rails almost to a certain degree. You almost needed that link of something that was really going to compel more widespread adoption. I think you mentioned Google being one of the main users of the language at scale. Alexey was referencing Scikit and so on from the scientific community. Do you feel that there was something in there that actually made that bridge for Python to now become mainstream in any place?
**Luciano:** No. Totally I think the jump in popularity that Python had in the last five years or so was driven by its importance in machine learning. The story of that is something that's been building for a long, long time, because I was just reviewing the timeline of the story. Python started in '91. Just like Linux was an open source project from the start when there was basically one contributor the creator, and then people started contributing to it, but it had a very slow start. Because it was never sponsored by a large corporation like Java, C#, Go languages. Go is a more recent example, but at that time in '95, '96 I learned recently more details about this story, because Dave Beazley who's another Python author.
Somebody that I really admire. He also great speaker. He was in the eye of the storm. He worked for the Los Alamos Lab of the United States government. They had a supercomputer, but it was very difficult to program and convenient to program. It had to be programmed in C++, Fortran or Assembly. That was all very cumbersome, and somebody in the research community from another lab, according to his story, Dave presented this as a keynote recently. According to his story people started talking about this idea of programmable applications. What they meant by that was that you have all of these libraries that already have the important numerical algorithms written in Fortran or C.
Then what if you could use a scripting language just basically to integrate and pass that back and forth between functions in those libraries. That would make the experience of programming the supercomputer, much more pleasant, much more productive. They started doing that with some proprietary or some homebrew programming language, but then Python popped up on the scene as something that people were using to experiment with that and also PEARL he mentions. Then for reasons that I don't know what precisely were the reasons, people started using more Python. Dave was actually responsible for the first release of SWIG, which is S-W-I-G, as a toolkit for creating bindings to expose C++ libraries to other languages.
In '96, he released a version of SWIG that had Python support, and then Python started to grow very fast in this community. When it turned out that there was this shift in AI from more a knowledge-based symbolic approach to artificial intelligence to one that's more based on statistics and also in tensors, linear algebra other mathematical abstractions. When that shift happened in the late '90s early 2000s, people realized that Python already had the bindings for all the libraries that people wanted to use to do that stuff.
Of course then Scikit-learn and other things were built on top of that but the majority of the infrastructure of the main numerical algorithms were already there and they were already battle-tested for 20 years of using the largest labs in the world. That's I think what gave Python a huge advantage over Ruby in the last few years because otherwise, they were competing in the web world. There was Rails and there was Django, but this phenomenon of machine learning really took off in Python because of the fact that Python have been in use in the scientific world for much longer.
**Alexey:** Luciano, how about these days, we see a lot of buzz about new features of language and how Python is evolving. What are you excited about the Python language these days?
**Luciano:** I'm really excited about a new development in the typing world. Here's the thing, Python adopted in 2015 a way of writing static annotations that they call typings, which is similar to the way that works in TypeScript. They are not mandatory, you don't need to write the typings ever.
If you do, then you have better tool support because the IDE can have a better clue of what your code is doing, and what is the type of a certain parameter that your function gets. Auto-completion works better, refactorings work better. It improves tool support. It also works like some documentation. I wasn't happy with the introduction of this static type system in Python at first. It happened shortly after I released the first edition of my book. I wasn't happy about it because I felt that it was impactonic.
To be really honest, I couldn't really put my finger on what was impactonic about it until they solved the problem three or four years later, which was when they released this new feature called typing protocol. Typing protocol is a way of supporting duck typing with static type hints, which is really interesting. For me, it was like a revelation of a whole new dimension when you think about typing. The dimension is usually if we're going to contrast say Python with Java. Python is dynamically typed and Java is statically typed.
Sometimes people, "Oh, Python is untyped. No, the only really untyped language is assembly where a byte is a byte and what does it mean? It depends on how it's being read. It totally depends on context but all languages are typed. The difference between aesthetically typed language and the dynamically typed language like Python will being JavaScript, is when the type checking happens.
If it happens before the program is run, so usually before a compilation stage then it's statically typed because the type checking is called static type checking because the type checker is looking at the source code, not at the running program. Just looking at the source code and based on what's written in the code, it determines or infers the types either explicitly or implicitly and that's static type checking.
Then on the other side you have dynamic typing which means that at run time if you try, for instance in Python to add a string with a number, you get a type error and that's dynamic typing. That's how it works. We thought about this axis, where it's an axis because then there's this thing called optional typing that was popularized by TypeScript. They were earlier languages, like DOT was a language. I'm told I never used it, but ActionScript the language that was used to program Flash, I think was the first widely used language that had optional typings.
Then DOT the language that Google created that now is used in Flutter and then TypeScript is the most famous example today. This thing called optional typing or sometimes some authors call it gradual typing makes this align. You have on one side static typing, on the other extreme you have dynamic typing and then you have gradual typing in the middle or shades of gray, let's see. Then, after I finished the first edition, I was very interested in languages that did concurrency better than Python.
We can come back to that topic later but it's not very difficult to find the language that does concurrency better than Python. I started studying Elixir and Go. Go is interesting because that is a statically typed language that has a concept of interfaces that is very different from the idea of interfaces in Java. They introduced this idea that became popularly known as static duck typing.
Let's just step back a little bit. We were talking first between the contrast or the opposition between static typing and dynamic typing. What is duck typing precisely? Duck typing is an idea that I think the Ruby community started talking more about it, more widely about i. It's something that has always been part of Python as well and JavaScript. The idea is let's say I'm writing a little interpreter and I have a function called parse and the function takes an argument that I'm calling source.
Let's say I'm using a dynamically type language so I don't need to say what the type of source is. then inside my parse method, I use source.read. I call the read method of source and I wanted to return a string. I'm going to manipulate whatever read gives me, the parse function will manipulate as a string. Duck typing means what is the correct type of the source?
The correct type type of the source arguments is anything that has a read method that returns a string. This is the essential idea of duck typing. The metaphor which was popularized or at least Wikipedia credits the metaphor the first public email written with the metaphor to Alex Martelli, who is a friend of mine and a tech reviewer of the first edition of my book. He also book author. Alex Martelli wrote, "Don't check what is the type of the object. If you need something that is duck-like, then check if it quacks like a duck or if it swings like a duck or flies like a duck or whatever subsets of duck type behavior you need."
The idea is if it quacks like a duck, it's a duck in the context. That's the essence and it turns out that there's an academic term for this and it's called structural typing. That's the opposite of nominal typing which is the approach that we find in Java, for instance, where in order to satisfy an interface, a class in Java has to declare that it implements that interface.
It has to implement the interface of course. The company is going to check both things that the class says that it implements the interface and that it actually implements the interface by providing the correct methods with the correct signatures. That's the Java approach. What the Go people realized was that you can actually get away with another approach which is you declare an interface and you say, for instance, in my parse methods, if I'm using Go and if I'm writing the parse method in Go. I can say that the source argument is a reader and a reader is an interface defining goal that defines one method, a read method that returns a string.
Now, how does the Go comparators determines whether the object that you're parsing as an argument satisfies the interface? By looking at the implementation as the object. The object does not declare that it implements. There's no syntax in Go to say I implement this interface. You just go ahead and implement it. What's the advantage of that? The advantage is that first of all it opens up the opportunity for those interfaces to emerge organically in a code base.
People realize, "Oh, we often need something that is sortable." Let me give you a concrete example. In the Python standard library there were a number of functions that were not correctly annotated with typings before the typing protocol came out. Just to recap. Typing protocol is a way in Python to declare interfaces similar to the way that they're declared in Go. The way is you declare an interface, and then you can use, for instance, as to when you annotate an argument that you require something that implements that interface, but the objects that provide the interface don't need to explicitly declare the interface. They just do.
That's really click typing, but because there is the explicit declaration of the interface in one place of the code base, and there is the explicit declaration of the type of the argument in terms of an interface, then it becomes something that can be statically typed. To go back to the example that I was going to give about emerging protocols. When I started studying the subject of protocols in Python, I noticed that there were annotations in the Python standard library in the type shared project, which is an external project of the Python Organization that has the typings for the standard library. There were annotations that were either too strict or too lax because they were created in those years between the initial release of typings in Python and the appearance of typing protocol.
Really there was no way to express the fact that several of the functions, for instance, what I discovered was I discovered about a half a dozen functions that really wanted something that was sortable. To be sortable in Python only requires one thing, to implement a less-than method which is called **[unintelligible 00:26:22]** __lt__ because it's an example of operator overloading. All parts of the standard library and the part interpreter itself that use sorting, only use the less-than operator. Anything that implements the less than operator, can be used, for instance, for the sorted function.
The sorted function takes an iterable of things that implement the less-than operator and so on. When I realized that there were typings that could be fixed by implementing this, like not by implementing, but creating this new protocol and then we could use the protocol to annotate the functions, I made this PR that fixed about five or six functions initially.
Later people discovered more. The last time I looked, there were 14 functions in the standard library that started using that same protocol. This is interesting because it allows those protocols which are standard interfaces to emerge from the bottom up instead of coming from the top down and they tend to be simpler because you're not, "Oh, I'm defining something that is a mapping interface." An interface that represents a hash in Ruby or a dictionary in Python, but that has lots of methods. You're creating a large burden on somebody that needs to satisfy that interface. That's the traditional way from Java and Python.
We have abstract based classes to do that, to define interfaces that are more complicated and that are defined from top down, because you define this interface and then you say your function requires something that implements an interface. The user has to provide all the methods even if they know that the actual context doesn't require all the methods, because the nominal checking means, do you declare that you implement that and do you actually implement that what we need?
What if the body of the function that consumes your object doesn't use all the methods? That's irrelevant. On the other hand, with protocols, you tend to be more minimalistic.
The good practice that the Go community has learned over the last 10 years or so is that protocols usually have one or two methods, mostly one method, sometimes two, rarely more. This reduces coupling. It makes it easier to mock things when you need to test. It's really a very interesting approach that Go introduced that TypeScript emulated, and now Python emulates as well. It's duck typing, which was always something, Ashok, linked to the idea of dynamic typing, but it's actually an independent thing.
Now, I wrote this diagram in the book that is actually a two axis. In the horizontal axis we have the static versus dynamic typing and the vertical axis is nominal types and structural types which is basically duck typing. We have languages like TypeScript and Python that support all four quadrants of this. If you think about this diagram in two axis there are four quadrants. Python and TypeScript support all four, Go supports three of them, Java as far as I know supports only one of them and so on.
I think this is something that excited me because I understand the importance of typings for large scale code bases with lots of maintenance. I was afraid that without protocols without this new idea of static back typing, which protocols brings. If we followed a strict regimen of statically annotating everything in our Python code basis, it would be suddenly programming in a slow version of Java.
**Ashok:** I think I really like the whole history and journey that you've described in that because it describes ways in which there's an aspect of figuring out what emergent behaviors can come and actually what are the best aspects that you can borrow from different communities and actually see its applicability across many different dimensions. It's fascinating the access description that you've given and something that I'm sure our viewers will be much more interested in exploring more of that in the second addition of the book as well.
**Luciano:** Let's make a bet. I bet that in five years Java is going to have something like protocols. [laughs]
**Alexey:** To me, the coupling argument is fascinating and you talked about taking a minimalistic approach to protocols and having small declarations. When you have nominal typing because you have the coupling between the implementer and the declaration, people tend to grow the interfaces because refactoring those, and going back to all the implementers and adding something else, it's a lot of work. You just grow the interface slowly, they tend to become bigger and bigger. Whereas, if you don't have that coupling, it's much, much easier to take a very minimalistic approach and each subset of actually the protocol can become its own type. Then you can have several different types for different perspectives, different usage of one major type. It's much, much easier to implement. That's quite fascinating.
**Ashok:** Definitely, anyone who has worked on large enterprise code bases, I think that pain is something that is quite obvious, and a feature like that would be a great benefit in those examples.
**Luciano:** Yes. Who hasn't ever had to implement matters that you know are not going to be used in that particular context, just to satisfy the interface declaration in the compiler? As we are talking about this, an interesting thing that comes up is that often in the nominal typing worlds of interfaces, you tend to declare interfaces together with the providers.
You have a collections library and then maybe you have a priority queue, and then you have an interface for that, and then the concrete implementations in the same library. Interfaces in the Go style or what we call protocols in Python often they are born on the client side. The code that wants to use something like in the example I was talking about, I have this this parse function and I can declare the reader protocol right before this function.
It's documented right there. What do you want? I want something. What do I need? I need something that has this read method. Already lots of parts of my code base support that, and more things than people will realize. Over time, you realize that, "Oh, we have these same protocol being defined in different places. Sometimes even with different names. Let's do a refactor and give it a canonical name so that people can reuse and talk and unify the language, make the protocol ubiquitous," but that's something that comes after. After the protocol has proven that it's useful because it's been used in many places. I like this approach. I think it's a very lean approach, a very agile approach to defining interfaces.
**Alexey:** It's interesting to see the connections there, Luciano. You mentioned how this was born in Go to some extent, and also used by TypeScript and et cetera, those connections. I wonder do you see any new ideas brewing in other parts or in other languages and things that you'd love see coming to Python in a way so that connection of connecting different languages, different bubbles as we were talking about before?
**Luciano:** I like to think of myself as somebody who likes to challenge certainties. There's this thing that I call taboo features. What are taboo features? An example of a taboo feature is operator overloading. I was very interested in Java early on. When Sun was promoting Java in the mid 90s, they had this Java world tour. I actually have a t-shirt from I think it's '95 or '96, around '97 maybe, around that time.
I went to the Java world tour here in São Paulo. I had never seen a language evangelist in action. People who are paid to promote a language, but I saw them. One of the things that I noticed was how they demonized features that Java did not have a preemptive defense against criticism, for instance, because Java was explicitly created to replace C++ in many contexts.
One thing that C++ had that Java did not have was operator overloading. People would say, "Oh, operator overloading, it's crazy." People would do crazy stuff about it, makes your code base incomprehensible and maintainable and so on. That was left out of Java but it was not left out of Python or Ruby, for example. I actually think since we were talking about the users of Python in science before, it's important that Python has operator overloading for that community so that they can overload the arithmetic operators to work with matrices, for example.
If you can't do that, like you cannot do in Go or Java or in some other languages, then writing expressions becomes really painful, if you can't use the infix operators. Operator overloading is an example of a taboo feature that turns out that, okay, people probably did misuse it in the '80s or '90s, with C++, but people learned.
I see Python and Ruby are both languages that are more than 25 years old, and I don't see a huge problem in those languages overusing operator overloading. I actually see them benefiting the community much more than becoming a problem. I'm going on about this thing of taboo features, because another taboo feature is syntactic macros, which is something that is really important in this world in Lisp and Scheme, those languages have this idea.
It's much more powerful than macros in C, which is a simple string substitution. Macros in this pack executable, and they change the abstract syntax tree. They're safer and much more powerful. Actually, a lot of the reserved words of Lisp and Scheme are implemented as macros. In Lisp, this also had a bad story, because this feature was added early on in the language, and then Lisp grew at a time when free software was not a thing, Open Source was not a thing.
You had those proprietary vendors selling different versions of Lisp with their own macros, and it turned out that each was a different language. It was super difficult to read somebody else's code written in another implementation of Lisp. Imagine you're looking at a dialect of Java with different keywords, that's very fundamental.
It create this babble of different dialects of Lisp that were incompatible. When they brought them together under the Common Lisp Standard, what they did was like the union of all the dialects. That became super complicated, because then now you have 13 different ways of doing everything. That's an example of abusing the future of macros but two languages that are really interesting and modern, also have macros. Rust and Elixir. In the case of Rust, is interesting to see that sometimes you see short Rust examples that they look like a scripting language almost. Rust manages to be very expressive because it comes with synthetic macros predefined that are useful to make some things that would require a lot of boilerplates without the macros easier.
The other example is an Elixir. Elixir also was created from the start using synthetic macros, a lot of its keywords are macros that actually build on top of more basic ones but that allows also an extension. Well, our colleague Martin Fowler has his book about DSLs with Rebecca Parsons. They wrote this book about DSLs and they talk about internal DSLs and external DSLs. An internal DSL is something that's written in the language, using idioms of the language.
Ruby is very good for that and people say that Rails is a domain-specific language for server-side web applications. José Valim, the guy who created Elixir, was a core contributor of Rails. He started worrying about the limitations of concurrency in Ruby, started doing research on it, and then decided to create this other language, Elixir, on top of the early virtual machine. He used this idea of macros early on for two things. First, to make for him easier to build the language itself and then to take this idea of domain-specific language and implement. He was also a core contributor of Phoenix, their main framework for web development in Elixir from the start.
Phoenix is really a DSL written with macros for writing server-side web applications. Then there's Ecto, the library for database integration, which is an example that I think is really interesting if you think about LINQ. Remember, when Microsoft added this LINQ feature that was pretty much borrowed from F#, or heavily influenced from F# into C#. LINQ is this completely new syntax embedded in C#. That's a pleasure to use for doing queries.
For working with databases, but you as a user of C# could not have done it because C# doesn't have synthetic macros. In order to integrate something like LINQ into C#, you have to change the compiler. Synthetic macros give people this power. Then you see it in using Ecto, which is a really beautiful library that also has early contributions from José Valim. It's a really nice example of how synthetic macros can help grow the language. I would like to see synthetic macros in Python. It's certainly a taboo feature. I believe people would be smart enough to mostly use it for goods. [chuckles]
**Alexey:** Nice. That brings back the idea of borrowing ideas and successes from other languages once again. You see the mistakes, but also the value that you can get out of borrowing those ideas.
**Ashok:** You were talking about the experience of first edition of the book that you wrote. Then now that the second edition is out now, any tales you want to share? Any stories? Any insights to our listeners of what it was like? Something that they probably won't get from reading the book, but they'll get from hearing this podcast for sure.
**Luciano:** Thanks for asking that. The thing is, I think a common characteristic of people who decide to write books is that they underestimate the size of the task. Otherwise, they wouldn't even start. I certainly underestimated the size of the task the first time and I underestimated the size of the task of updating the book five years later. There was this major topic of typing. I wrote about 200 pages of new content just because of types. Some of it affected some of the chapters that were already the most difficult ones to write in the first edition. Like the chapter about interfaces and ABCs, where I discussed this idea of, okay, so we have duck types.
We have this idea of duck typing in the language that's really a core idea of the language but then we also have the possibility of declaring ABCs, abstract base classes. The standard library comes with several of them predefined and you can use them at runtime to do explicit type checks. Now you have type hints, and now you have typing protocols.
In order to rewrite that chapter, I actually did something that I learned many years ago in another context but the idea was, I hanged all the 44 pages of the chapter in a wall. It was like a three meters by two meters of pages so that I could look at all of them at the same time. Of course, I couldn't read them all at the same time, but I could make annotations, put post-its and make markings to realize where I had to change the approach.
Besides the new content about typing, there is also a new chapter that I wrote about concurrent programming. Because as I mentioned before, so Python has this limitation which is common among so-called scripting languages, Ruby and JavaScript have similar limitations. Which is the interpreter is not written in a way that allows it to run multiple threads of Python codes at the same time because of the way the memory management happens, and so on. It's something that there's been efforts to change in the language, but it's difficult.
Now, there is a new effort that sounds promising if people are interested they can look for nogil. GIL is the Global Interpreter Lock, which is the thing that prevents Python bytecode from running in parallel. Nogil is a project that is experimental. Somebody did a fork of Python 3.9 and proved a proof of concept that have shown it's possible to remove the GIL and not lose performance if you add other things. We don't have that, this is still what we call in the Python world science fiction. Something that's a promise but doesn't exist. I wanted to address a question because I wrote a lot about concurrency in the first edition, but then I found there was this cognitive dissonance, which was okay, reading the book, my book is focused on the language and the standard library, you come out with an impression that Python is really not very good for doing concurrent programming. It's true. Well, certainly not as good as Java for instance. Then you think, okay, but how about Google? How about YouTube? How about Instagram? How about Reddit, there's a lot of large web properties out there that were written in Python, or a lot of Python, and you can't have that scale without some concurrency.
I added this new chapter, which is pretty different from the rest of the book because it's a chapter-- Well, the chapter is called _Concurrency Models Impact_. It starts with a very simple example that's most hello worlds, but a concurrent hello world written in in freestyles in Python using threads, using processes and using core routines, which is this new approach, similar to the new async functions in JavaScript. We also have async functions now in Python that are called core routines. After this example, it's a practical example to show the three approaches, then there's a part of the chapter that is mostly about architecture.
Because that's what I wanted to share with my readers, that if you want to use Python at scale, you have to solve this problem of the limitations of concurrency in the interpreter with an architecture that compliments. That means having multiple instances running, means having an application server like micro VSD or something, caching, message queues so that you can delegate tasks to other processes and that's a very new content that I wrote that I am excited about.
**Alexey:** Right. Good. Looking forward to the launch of the book in early 2022.
**Luciano:** Let me just say that the early release is already available in the O'Reilly platform. For listeners who are in developing countries, the least expensive way of accessing the O'Reilly learning platform is to subscribe to the ACM. acm.org has a program for people who live in developing countries that costs about 10% of what the subscription of the O'Reilly is.
With this 10% fee, you're buying access to most of the O'Reilly content and also all of the ACM content, which is huge as well. People can read the book online there. The Kindle and print versions will come out only, probably around April.
**Alexey:** Okay. Amazing. We'll make sure that's added to the show notes. [laughs] Then, unfortunately, we're coming to the end of the episode. It's been a great conversation. Thank you so much, Luciano, and great to have you with us. Thank you so much for joining.
**Luciano:** Thank you so much, Alexey and Ashok. This was very nice.
**Ashok:** Thank you, Luciano. It was wonderful. I think there's so much richness just listening to you in this episode that I'm sure readers of the book will benefit greatly. Thank you very much
**Luciano:** Okay, bye-bye.
**Alexey:** Thank you, bye.
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
Further episodes 
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