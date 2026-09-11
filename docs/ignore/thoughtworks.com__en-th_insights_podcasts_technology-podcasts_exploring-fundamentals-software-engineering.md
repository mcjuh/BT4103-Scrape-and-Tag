<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-fundamentals-software-engineering | Title: Exploring the fundamentals of software engineering | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring the fundamentals of software engineering 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Neal Ford and Ken Mugrage | Podcast guest  Nate Schutta and Dan Vega
May 01, 2025 | 27 min 51 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-fundamentals-software-engineering#Transcript)
Listen on these platforms
## Brief summary
You might think you know software engineering, but what are the really fundamental elements? What are the concepts, ideas and practices that are completely essential? What makes software engineering what it is?
Thoughtworker Nate Schutta and Dan Vega are attempting to address those questions in their upcoming book with O'Reilly, _The Fundamentals of Software Engineering_. Covering topics ranging from reading code through to the importance of learning to learn, it promises to offer a fresh insight into the skills and knowledge needed to be a successful software engineer.
In this episode of the Thoughtworks Technology Podcast, Nate and Dan join hosts Neal Ford and Ken Mugrage to discuss the book and to dive into what really are the fundamental elements of software engineering. Listen for a fresh perspective on the discipline and a deep dive that shows it's about far more than just writing code.
**Learn more about[The Fundamentals of Software Engineering](https://www.oreilly.com/library/view/fundamentals-of-software/9781098143220/)**
## Episode transcript
**Neal Ford:** Hello, everyone. Welcome to the Thoughtworks Technology Podcast. I'm one of your regular hosts, Neal Ford, and I'm joined today by another of our regular hosts, Ken.
**Ken Mugrage:** Hi, everyone. Ken Mugrage, as Neal said, one of the regular hosts.
**Neal:** We're here today to talk to a couple of authors of an upcoming book, _The Fundamentals of Software Engineering._ I'll let them introduce themselves, starting with Nate.
**Nate Schutta:** Awesome. Hi, I'm Nate Schutta. I also work with Neal, finally now at Thoughtworks, been adjacent for a long time, but finally on the inside, the umbrella now.
**Dan Vega:** My name is Dan Vega. I am a Spring Developer Advocate at Broadcom. I've been doing this software thing for 23, 24 years, a long time.
**Nate:** Well, let's not date ourselves. Let's not get into how much gray hair we have.
**Dan:** I actually used to work with Nate, and that's how we met. The idea for this book came up, and I jumped at the opportunity, and we'll talk more about it.
**Nate:** Well, at least it's somewhat, I think, due to your tweet, because you sent out-
**Dan:** I did.
**Nate:** -a tweet saying, "Here's my goals for the year. I think one of them was to play golf with me, if I remember right. I'm like, "That's an easy one."
**Dan:** We made that happen.
**Nate:** "That's an easy one." Then you said another one about writing a book. I'm like, "Speaking of which, I think I might be able to help you with that."
**Dan:** Yes, the rest is history.
**Nate:** Exactly.
**Neal:** Well, speaking of this book, I know Nate is very familiar with my book, Fundamentals of Software Architecture, because you use it to teach from. Why a book on fundamentals of software engineering? First of all, what's the difference between software architecture and software engineering?
**Nate:** In no small part, it was inspired by Fundamentals of Software Architecture. I make no bones about the fact that that was part of what sort of brought me into this, inspired me into that concept. What really got me thinking about this material was that I thought back to when I was starting my career, and I thought I knew what I was doing. You come out of, "I have a computer science undergraduate degree."
I naively assumed when I got into the real world that, well, because I have this undergraduate degree in computer science, I obviously must know what it means to write software. Then you get on a real project, and you very quickly are disabused of that notion. You realize, "Wow, there's this huge ocean of stuff that I really need to know about in order to be good at software engineering."
I think most of us sort of pick it up piecemeal, a little bit here and there. Then maybe you go to a conference and a talk, or you pick up a book, and you read about it. I thought nobody's sort of put together that 10,000-foot overview of "Here's the basics." It's not meant to teach you everything about all of them. That would be a 50,000-page book, but it's to give you the pointers to, "All right, well, this is why testing is important. Here's where you go to learn more about testing." We're going to give you just enough to be dangerous so that you now have that grounding and hopefully then push you towards learning more about those topics.
**Ken:** I have a question. One of the things I'm looking at table of contents for the book, and that really jumped out on me is the first part is reading code. Writing code comes after that. Talk about that a little bit. Where'd that come from?
**Dan:** Yes. I know Nate wrote that chapter, but I have a lot to say on this, too. As software developers, we inherently read 10 times more code than we write. For every one hour that we're writing code, we're somehow reading code, whether it's trying to understand code, whether it's trying to debug code, whether it's just trying to understand something, we do a lot more reading. Inherently, we all just, I think, spend much more time trying to perfect the craft of writing code than we do reading code. I know you have a lot of thoughts on this, so I'll let you jump in.
**Nate:** Yes, absolutely. For me, it goes back to how we teach this. I think about the way we structure a computer science program or a boot camp, and it's just "Start writing code." I thought to myself, "That seems kind of a weird way to do it," especially given if I was trying to teach you Spanish or German, I wouldn't say, "Now go write some Spanish." It's not where we start, and yet that's what we do in software.
To Dan's point, we spend so much more time reading it. You need to have good techniques for how to approach that. I feel like so many of the ways we try to teach these things starts from this greenfield world where we rarely have that luxury on a project. So often, we're being brought in with existing code that's been around for 5 years, 10 years, 20 years, and you're told, "Okay, go figure it out."
Without having some strategies to how to do that, it can be overwhelming. That was, to me, a very foundational way of starting this: that "You're going to have to learn how to read code, so get good at it. Here are some tips and techniques for how to do it."
**Dan:** Again, it goes back to you don't know what you don't know. They didn't teach you how to read code in boot camp or-
**Nate:** Because you didn't have to.
**Dan:** -a computer science degree. Now we're giving you that like, "Hey, you're on the job. One of these things you're going to have to get better at is reading code."
**Neal:** I think that's a great way to start, especially now that a lot of code is being generated not even by humans.
**Nate:** Correct.
**Dan:** Yes, that's true.
**Neal:** Learning to read code well is probably a skill that everyone needs to improve on.
**Dan:** Yes, for sure.
**Ken:** In that same section, I see a thing that says software archaeology. What is that?
**Nate:** This goes back to being on expert panels often with Mr. Ford, and we'd try to come up with a pithy way of introducing ourselves. I got in the habit of saying I'm a software archaeologist because it felt like most of what I was doing on a software project was trying to come in and figure out what came before me. "What can I learn about the society that built this that I'm now building on top of these ruins? Let me learn more about this wall that we discovered when we started excavating."
For me, again, it just ties into that, where so much of what we're doing as software engineers isn't writing brand-new code. It's "Here's this existing thing. I need to get my head wrapped around it, and I need to brush off the debris and try to figure out, 'What did the author intend here?'" Part of why I think we dislike reading other people's code so much is because, not only do we have to try to figure out what the code is trying to do, but we have to see it through the lens of the person who wrote it, and that's almost always different than the way we probably would have approached it.
It's like, "Oh, I never would have used that approach. I would have used this approach instead. Oh, that guy must have been an idiot." Fairly often, we look at it and realize, "Oh, wait, I'm the idiot that did it that way two years ago. Pops." That's always an eye-opening experience as an engineer. I just feel like that's a good analogy for what we do, is just brushing stuff off and trying to figure out what's happening here. What was the intent of the original author? What problem were they trying to solve?
**Neal:** I think testing is a good topic that goes into the engineering world that we didn't really touch on at all in the software architecture book because, it doesn't really touch on software architecture as much outside of this idea of fitness functions, which we touch on, but it's an important part of engineering, and I think that's a good example of the contrast between the pure abstract of code versus actually making it work, which I think that's where your book is really going, is, "Okay, I have this code, how do you actually make it work and do something?"
**Dan:** Yes, and I think we touched on testing, and again, you don't know what you don't know. We went into, "Yes, you were taught how to write the mechanics of writing a test, but why were you taught that? What are those tests going to do for you?" We go into that a lot because just telling people to write tests is not enough. They're never going to do it unless some boss is standing over them, telling you, "Please make it to 80% code coverage," right?
We go into, "Hey, tests really help with providing documentation," right? You document what you're doing in your code for the next person who comes along. It also gives you a lot of confidence that, "Hey, the things that I'm doing are not going to screw up the entire system." I know, as a developer that was one or two years into the job, that was always a big thing for me. I was a little bit nervous.
I'm working on this big project, and I don't want to do something that's going to screw up the entire system. Writing tests gave me that confidence that, "Okay, everything I'm doing is fine. It's not going to break the world. We're doing okay here." Yes, there's just a lot of things that go into tests that I don't think people understand at the surface. As Nate said before, we don't go deep into this. There are other resources. There are books and books on writing tests, right? We give you the reason why you should be caring about these things.
**Neal:** Let's talk a little bit about the filtering process because one of the challenges that Mark and I had, and then we had as we did the second edition of the architecture book, is there's just so much. Nate-
**Nate:** Oh, God, yes.
**Neal:** -talked about that at the beginning. There's just so much. How do you narrow it down to some reasonable [crosstalk]?
**Dan:** Well, this is good because this is my first book. I've written a bunch of things over the years, but never a book. This was a fun process for me. As Nate goes, I have a different approach than Nate. My approach is, "I'm just going to brain dump everything I know into a document, and then we'll whittle down from there because I want to over-teach someone."
I'm like, "Hey, this is all the things I know on this particular subject. I want to talk about all these things." In this particular book, that's not what we're trying to do. There was some early on stuff where I had to go, "Okay, I can't include everything because we just can't include everything." Try to be the person that is reading this book, and go, "What are just the essential things that I need to know, but give me some resources to go do some learning on later on?" That's been fun for me. It's been a process.
**Nate:** Oh, for sure. For sure. It is really hard because there is so much material there. For me, this grew out of a training I did on O'Reilly's platform that was about nine hours. I think there's probably closer to 12 hours of content. I think even just the nine hours that I typically present, I don't think I've ever gotten through all of that block anyway, because people ask questions, and you go in different directions.
It is a big challenge. I think without it turning into an encyclopedia, you've got to make some calls and just try to buff it down to "What are the essentials that someone needs to know?" You want that to be digestible. When someone first encounters testing, I want them to be able to read that chapter, get through it in 15, 20 minutes, and are like, "Okay, cool, now I know what I'm talking about. Here are some pointers to some more stuff. If I want to dive deep, here are some good books" or other links that we've given them. Hopefully, that'll get them off on the right foot.
**Dan:** I think one kind of conscious decision that we made is, "Hey, we'll point you to a GitHub repo where there's a lot of code." We don't include a ton of code snippets in the book, because that can get very verbose and run the page count up, right? That wasn't the idea there. We're like, "We're just trying to give you some of the why behind some of this." There's practical examples. You can even go have the robots write your code if you want. We're trying to give you some of the theory and the why behind it.
**Neal:** Well, and my theory that many people have heard before is that every line of source code you put in a book halves its shelf life. That's the other problem with too much concrete source code. Even Martin Fowler had to create a second edition of Refactoring, because of the Java util vector. [laughter] Yes, highly embarrassing, with the point of having to create a second edition.
I remember when I was in university, the least effective course I took was the software engineering course, because it was literally just a hodgepodge of topics. This was back when the instructors had literally an overhead projector and slides. He had two decades' worth of slides of random topics he had built up. He would just show one after the other. It's like, "I don't know what we're supposed to get out of this." I think the major challenge of this is actually the curation, rather than the subject matter, right?
**Nate:** Yes, I agree, and trying to draw that out in a way that people can see why these topics are here, and they build on each other. I fully expect that some people will encounter this material and will read it piece by piece. It doesn't have to be read cover to cover in one sitting. I would expect that, like this chapter on UI design. Well, if you've got to do some UI design, you've never done that before, read that chapter.
We'll give you enough of the basics and, more importantly, point you to some resources that we have found to be very useful. Now you've at least got a base understanding. Are you an expert? Of course not. At least you're not starting from absolute square zero.
**Ken:** I'd love to hear Fundamentals-type training books and all those kinds of things. As you mentioned, a lot of people don't have the solid foundation for these things. That said, you're also talking about all kinds of the stack here. If you're doing user interface design and talking about other stuff, are you trying to give people a place to start in the stack? Are you really trying to be all things to a little bit here and a little bit there, the whole T-shaped thing, if you will? Who should be reading the book, I guess?
**Nate:** I'm a lot more attracted to T-shape. Maybe that's just because of where I'm at in my career. It's certainly something Neal and I've talked about. That was really a great insight that, as an architect, we need to be broad, and you need to understand that there are multiple different approaches to a problem. I was on a call earlier today about some mobile stuff. It's like, "Well, yes, you could write a native iOS app and a native Android app. You could do the cross-platform. There's multiple different cross-platform things."
In the role that many of us are living in now, as we've advanced in our career, it's more important to know about those different options than to be the leading expert on those things. I think that's an important foundation for people to have, even early in their career, though, to understand that there is a breadth to this space. I think that's another thing that I probably wasn't aware of when I came out of university. It was just how many things go into really producing good, high-quality code and having successful projects.
**Dan:** Yes, and I would say early on, too, part of the journey is trying to figure out what you're passionate about. You may get into a position at a job where you're doing one thing, but you don't know anything else. Maybe you take a side project, and you have to build a UI for it, and you haven't done that before. It's like part of this early-on journey from coder to engineer is trying to figure out the things that you're passionate about to continue on in your career. Part of the breadth of this book is that, yes, you might be early on in your career, and you might be trying to figure out where your interests lie.
**Nate:** I think that's actually one of my favorite chapters, the one that you wrote, around career, and just-
**Dan:** Mine, too.
**Nate:** -pointing that out to people that there are a lot of different paths. I think for many of us, especially when we come right out of school or boot camp, we think that the only path is hands-on keyboard.
**Dan:** Forever.
**Nate:** "Yes, that's my life now for the next however many years." It's not. There are so many amazing ways you can practice this craft. You may not know what you like until you have a chance to see what it is.
**Dan:** I honestly thought like, "Hey, my career is I'm going to code until I want to be a manager." I thought that was the only path because nobody ever sat me down and told me that. I think part of this is just giving people the knowledge of like, "There are many career paths here, but you also have to be very deliberate with that."
Find, early on, what you're passionate about, and be deliberate because there are so many shiny new toys in this industry, and you cannot learn everything as much as you want to. You have to be very deliberate with your career path. Starting to understand the path now and how to get to where you want to go, I think, is very important. Things turned out okay for me, but I wish somebody would have helped me understand that early on.
**Nate:** Yes, I agree. I look back on my career, and it all fell into place very nicely, right?
**Dan:** Just magically.
**Nate:** Magically, somehow. There's these events that occur that, at the time, seem, "Wow, that's the worst thing that could have happened to me." Then it turned out to be the thing that led me to where I am now. It's like, "Thank goodness that happened to me." It would have been very helpful, especially when I was just getting started, to have a sense of what this path can look like. How can you build to that thing?
If that's something you decide you want to try, how do you even go there? You think about things like advocacy and things like that. How do you even get into that line of work? How do you start teaching at a university? What does that look like? Just to know what that path can be is, to me, very illuminating.
**Dan:** Right. I think we touched a lot on, in the career management chapter, building your professional network, and just how important that is. Again, something nobody ever told me. Somehow, I fell into this, made good connections, stayed involved in the community, and those things have turned into awesome opportunities.
**Neal:** We've talked a lot about some hot spot subject areas. Can you give us an idea of the general scope of the book? Not necessarily read the table of contents, but what subject areas do you touch on in the software engineering space?
**Nate:** As Ken mentioned, we start with reading, because I think that's important. Obviously, writing code is still something we do a lot of. That, to me, is a part of the genesis for me. I was sitting down on the couch one day, and I had this brainstorm around a listicle thing. N things to be a better software engineer, or something like that. I don't know if it was going to be a presentation or what I had.
I started jotting down these little things, these little nuggets that you pick up along the way. I thought, "Well, maybe I'll get to 10." Then I think I was around 35 or 40 when I realized, "Okay, there's more to this than I thought," right? Then I started talking to some people and sort of fleshing it out. It's all these little things that you pick up over your career. Let's get a light shone on that a little faster so you don't have to find it on your own.
To me, that's a huge part of it. How do you write good code? How do you read code? How do you test that code? What is architecture? Obviously, we can't replace the Fundamentals of Software Architecture. We point to it, unsurprisingly.
**Neal:** Which is a resource in the book.
**Nate:** Absolutely.
**Neal:** I'd be impressed if you could replace that whole book with a chapter.
**Nate:** Yes, that would be cask strength right there, if you could distill it down to that. I never learned about architecture when I was in university. That was something that, oh, the architect did some things, and you sort of picked it up piecemeal. Yes, and it's just trying to give people, take some of the mystery away from that, pull that shroud back a bit so folks can see what that breadth looks like.
**Dan:** "Hey, guess what? Becoming an architect is a path you can take as well. Let's talk about that."
**Neal:** Say that term "architect" with proper reverence, please.
[Laughter]
**Nate:** Hey, I'm an Architect as a Service!
**Ken:** Somewhat related, Neal and I were both actually in Bangkok at an event a couple of weeks ago. A couple of folks walked up to us afterwards that were students, and they were looking for a job. Since you do talk about career things, they asked me, "How do we make ourselves stand out to folks? How do we get people's attention?" Frankly, it's been a long time since I interviewed as an entry-level software engineer. Did any of that come out when you were working on Fundamentals and talking to people that are just getting started?
**Dan:** Yes, I don't know if it's directly, but a part of that is, again, starting to make connections. I think the biggest thing you can do while you're applying for jobs is trying to get involved in the community, whether it's going to a meetup, whether it's being involved with some type of project, however you can get involved in the community, doing that.
I think it is also trying to find a way to not be the 100,000th person who submitted a resume to the company, knowing that you submitted 10, 15 resumes today. I don't know, I'm not on the other side of that right now, and I'm in the same position as you, I haven't done that in 20 years, but trying to make sure that you find the right people to talk to send your resumes to, not just blast-emailing your resume to everybody who wants to read it.
Because I know a lot of these systems are basically just filtering out based on things that are in your resume, so making sure that you are taking your resume and filling it out for the job that is being advertised. Don't just take the same thing and blast it out to 20 people. If there is a specific job you're interested in, make sure your resume is tailored to fit the requirements for that position.
**Nate:** Yes, and I think it's also being willing to network a bit, right? I think that's something that we definitely don't touch on in most programs. In fact, I just had an undergrad in my workshop. I just did a developer architect workshop, and one of my attendees was an undergrad. He's going to graduate, I think in the fall, I think is what he said. What really impressed me about him is he was talking to multiple people in that room, introducing himself, and then clearly exchanging contact information. I thought, "All right, that kid's going to be okay. He's going to find something." That's not comfortable for a lot of us. I'm really proud of him for doing that.
**Dan:** You remind me of something. I was fortunate enough to speak at the Atlanta Java User Group maybe last year, and there was just so many people in the room, and we had a great presentation. You were there. We had a really great presentation. A younger developer came up to me afterwards and he said, "Hey, I'm really struggling to find my next position. I don't know what I should be doing."
I'm like, "Sir, you should not be talking to me. You are at a Java User Group. Go talk to all the people that are here. Network, find out where people work. Are they hiring? I'm not the person you should be talking to. I appreciate this conversation, but those are the things you should be doing." It's a sales position. You're trying to hustle, right? You got to get out. You got to talk to people. You got to set yourself apart. You can't just be the thousandth resume that they got today, right?
**Ken:** Dan, you just mentioned a Java User Group. I guess both authors, from your perspective, and I don't know if you address this in the book or not, people learning the Fundamentals, should they be picking a language? Should they be trying to understand structures? Should they be trying to understand what?
**Dan:** What's your favorite saying?
**Nate:** Well, it depends. It depends. I have this theory that a lot of us fall in love with that first language we learned, and then that becomes our favorite hammer, and we use it to solve every problem, and it's the greatest language that's ever been created. No language can surpass it. Obviously, we've got to have fluency in a language, and there's nothing wrong with investing in that.
We need to be aware of other languages, and we need to periodically, whether that's annually or biannually, whatever works for your sort of how you approach things, you do need to stretch and try something else and pick up a different language. It will change the way you write your basic language, and it will change the way your brain approaches these problems, and I think that's a huge, huge positive.
One of the things I try to encourage people to think about, though, is the length that a skill will be useful to you. If you look at everything you learn, there's a lifespan to that. In our world, some of the things you pick up, they have a lifespan of a fruit fly. They last about 24 hours, and then they die. Every JavaScript framework that's ever been invented seems to get about six months, and then everybody hates it, and we move on.
There's value in that, but I encourage people to think about some of these longer-running skill sets, these things that go on for your entire career. For instance, the soft skills, the things that we love to ignore as software engineers, are beneficial to you for your entire career. Somebody asked me a couple of years ago for book recommendations for software architects. I said, "Well, _The Fundamentals Software Architecture_."
He said, "Yes, got that one." I said, _"How to Win Friends and Influence People_ by Dale Carnegie." Not a technical book, older than everyone that's on this call, probably everyone that's listening to this podcast, and yet one of the most important books you can pick up for your career, in my opinion. I ran into that person a year later at that same event, and they said, "I read that book, it changed my career, it changed my life." I'm like, "Whoa, okay, great, fantastic." To me, it's appreciating that there is a whole pantheon of things you can learn and don't tie yourself just to learning the next API.
**Dan:** Yes, and I'd say early on in your career, you're in this discovery phase where maybe you're trying a couple of different languages, and you want to see what resonates with you. After that, one of the things we talk about in the book is like, "Hey, we have walked backwards from your goal, like, 'Where do I want to be in five years?' We got to set some real career goals here. If one of those is to be like an architect, right? You have to get very strong in one vertical."
I need to be very strong in, say, Java. I have to understand everything there is to know about Java. I got to be good at Java. I have to understand data structures and concurrency, and all the things that would make me a good Java developer. I'd say, once you're past that discovery phase, yes, you really need to hone in on some skills, whether it's in that particular language, but then there is that T-shape, like "What are the broad things that I just need to know a little bit more about?"
**Neal:** Okay, the book is in early release, right? From O'Reilly?
**Nate:** Correct.
**Neal:** How many chapters out now?
**Dan:** Oh, we just had two more drop.
**Nate:** I'm not sure. It's at least 120 pages, so however many chapters that is then.
**Dan:** Yes, I think five.
**Nate:** Six, five, something like that.
**Neal:** Six, I'm getting an indication. Let's do six chapters [Crosstalk].
**Dan:** All right.
**Nate:** Let's do six.
**Dan:** All right.
**Neal:**[laughs] Because somebody's looking at a website. [Crosstalk]
**Nate:** That helps. That helps. I don't have it in front of me.
**Neal:** Six chapters out. When's the anticipated finish date? I know you--
**Nate:** Fall, I hope. Fingers crossed.
**Dan:** Yes, that's what we're aiming for.
**Neal:** These things always take longer than they seem like they should.
**Nate:** Oh, yes, writing books, it's sort of like having a child. If you've never done it before, you have no idea what you're getting into, and you just dive in, and it is what it is. At least for some people, they get to the point like, "Well, I'm never doing that again." Then amnesia kicks in, and you forget about how miserable it was. Then you're like, "Sure, I'll do it again." That's been my experience with books. I think this is number seven for me. It's just this "I'll never do that again" until the next one.
**Neal:** Well, I read a great book. There's a whole genre of books by writers about writing. There's a book called The Writer's Life by a poet. One of the things that she said is that every book takes two years, whether you want it to or not. I thought, "I thought that was only technical books, but it turns out it's poetry books, too." They all take a long time. I think it's a great topic.
I think it's greatly needed because a lot of people coming out of university or boot camp, they don't know what the day job is, because all they've ever seen is code and simple little problems in university. Having a good guideline to what the day job looks like, I think, is a great way to bootstrap a career. I think that's a much-needed resource. You guys should stop talking to us and resume writing them.
**Nate:** Well, our editors would like that as well, I'm sure.
**Dan:** Yes, for sure.
**Neal:**[Crosstalk] Well, thanks very much for joining us today.
**Nate:** Thank you.
**Dan:** Thanks for having us.
**Nate:** Thanks for having us.
**Dan:** Yes, this is great.
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
## Discover a snapshot of today's technology landscape
[ Explore Technology Radar ](https://www.thoughtworks.com/en-th/radar)