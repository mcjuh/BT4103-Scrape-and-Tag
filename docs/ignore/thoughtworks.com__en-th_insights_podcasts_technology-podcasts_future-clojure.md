<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/future-clojure | Title: The future of Clojure | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The future of Clojure 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Rebecca Parsons | Podcast guest  Stuart Halloway
December 10, 2020 | 39 min 11 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/future-clojure#transcript)
Listen on these platforms
## Brief summary
The Clojure programming language has seen some radical changes in recent times — not least of which is a change in stewardship of Cognitect, the company that provides technical support for Clojure. Here, we catch up with Stuart Halloway to find out what Cognitect’s acquisition by financial services firm Nubank means for the future of Clojure.
**Podcast transcript**
Neal Ford:
Welcome, everyone, to the Thoughtworks Technology Podcast. I'm one of your regular hosts, Neal Ford, and I'm joined today with another of our regular hosts...
Rebecca Parsons:
Rebecca Parsons. I am another one of your regular hosts here on the Thoughtworks Technology Podcast, and I'm the Chief Technology Officer. And Neal, I'd love for you to introduce our guest.
Neal Ford:
I would love to do so. It's my very long-time friend, Stuart Halloway, who is the team lead on Datomic and a distinguished engineer at Nubank, but he's much more involved in Clojure than just Datomic. That's just the job that he's chosen within the Clojure ecosystem because he's been involved for a long time. And that, of course, is exactly what our podcast is about today, about Clojure, which Rebecca and I are big fans of. So, we'd like to welcome Stuart Halloway. Welcome, Stuart.
Stuart Halloway:
Thanks. It's great to see both of you remotely in these crazy times.
Neal Ford:
For those that have not been following what's been going on in the Clojure ecosystem, some quite interesting things have been happening over the last year or so, not necessarily to do the language, but more the stewardship of the language. Stu, would you like to give us a high-level overview of how your life has changed a bit over the last little while?
Stuart Halloway:
A few months ago, Cognitect joined the Nubank family of companies, and that was a relationship long in the making. Nubank was an early advocate of Clojure and Datomic in their business and really standardized on it across the business. They built, as far as we can tell, at least the people who are talking about it, they built one of the largest Clojure code bases in the world. The last estimate I saw was 2.7 million lines of Clojure code, several hundred microservices written in Clojure. And really, Ed Wible and other people at Nubank looked at starting back with the out-of-the-tar-pit paper. They looked at what they thought was wrong in software development, and they had a really big problem to solve. They really wanted to make banking more accessible and bring banking to the unbanked, and starting in Brazil, but now, in a lot of other places. And they did not want to stumble over incidental complexity as they scaled. They expected they needed to be hypergrowth to accomplish their goals in that industry. And they picked Clojure as a strategic bet that the simplicity and stability of language would help them do that.
Stuart Halloway:
They've also participated in the Clojure ecosystem, speaking at ClojureCons and other conferences, and really, these kinds of corporate deals are amazing when both parties share the same DNA. When you meet together, and you talk about how you work, and what you want to work on, and what you consider to be the hard problems, and you have that shared vision, then there's not an impedance mismatch. It's not like there's two different companies that are in an overlapping business, but have nothing in common, except what they're trying to work on or something like that. And so, that made this an obvious match.
Stuart Halloway:
And a testimony to that is that my job hasn't changed very much. I was leading that Datomic team and a committer on Clojure before the deal. I'm leading the Datomic team and a committer on Clojure after the deal, and now, have more resources. So, Ed summarized it as, "Like before, but more so." And in particular, there's no desire at Nubank to change how we work because how we work is what they bet on. And so, they're like, "Just do more of it, and show us how you do it." And it's been great to see how they do it, and seeing how they operate, and how they take Clojure's core notions of simplicity, and then, replicate that out at scale so you can have a 600, 700 software developers working in it and bringing on people that have no background in the language or in software development and train them up. So, that's amazing and eye-opening to us as, prior to this, a small company, seeing the amazing growth and success that they've been able to have.
Neal Ford:
A few things about your first statement there. Just to clarify, Nubank is a bank based, originally, in Brazil, right? And so, a bank has basically acquired, or you used the word joined, which is doing a lot of heavy lifting there. Can you tell us what joined means there, that Cognitect joined with a bank? Because that sounds not like the typical trajectory for an open source ecosystem and language.
Stuart Halloway:
Clojure has never been typical in any number of ways, and a reason for that is... And people who have met Rich Hickey or talked to him for more than five minutes know, he approaches every decision in his life, at least, when it's called up, from First Principles. And so, whenever it's like, here's how open-source works, or here's how databases work, or here's how language works, he will pick that apart and say, "Well, that really is composed of 17 sub-components, and these 12 are things that we've all just cargo culted along because they're what everybody else did, and nobody thinks about it. These other five are really the important things, so we'll double down on those, and maybe, make different decisions on others." A lot of people have a notion that there's one way to do open source, and that notion is usually, however they do it.
Stuart Halloway:
And the success of GitHub has created one very large tribe that have a set of common practices and approaches to things that become one gravitational center there for how it's done. But the fact that there are dozens of approved, and probably hundreds of less well-known open source licenses, and equal variability in development models, when you can start to look, there's a lot of different ways to do things. And so, Clojure was created. Rich took an unpaid or a retirement savings-funded sabbatical for several years to create Clojure, and gave it away as an open source project. And we built, at Relevance first, and then, when we merged with Rich's and our joint venture to form Cognitect, we built a business around helping people use Clojure. And so, that is one model for how you pay for open source. So, you build an open source thing, and then, you provide consulting services around it.
Stuart Halloway:
Another way to make money with open source is to not need to make money with open source. And so, big companies make a piece of open source and throw it over the wall because they had it. They already built it, and they decided that they would benefit in various ways from having that technology via open source. Another way to make money in open source is to say, "We're going to make something that is open source, but it's sort of poisoned." So, it is one source, but then, when you want to use it at scale, it has a plugin or something like that, that changes the rules. And it leaves people maybe a little bit like, "Okay." People who like open source can start using it. And then, eventually, some business head comes along and looks at the scale of use and says, "Oh, we're in trouble here. We have to actually... The way that to do a license, we have to pay for that."
Stuart Halloway:
We didn't want to do that, but we do like the idea of software developers getting paid. So, we also started Datomic as a commercial product, as it has been and remains. And so, Datomic has, for years now, funded the development of Clojure. Revenues from the Datomic and from Cognitect Clojure consulting, those things have poured money back in... And Alex Miller works full-time on Clojure. On the other side of this deal, we are going to be expanding that team and having more people work full-time on Clojure. So, there's a lot of different pieces that come together there to make it go.
Stuart Halloway:
The other thing is that Clojure doesn't take a huge number of people to move forward. It is a Lisp. It has a small core and principles that are very carefully applied, especially at the bottom. And so, it doesn't need, and probably wouldn't benefit, from having 100 people or 1,000 people working at the bottom. And so, it takes a relatively small investment. If you find the right point of leverage, smaller investments have great value. And Clojure is a great example of that, where... I'm sure Rich doesn't working for several years without pay was a small investment. But relative to the overall industry, a very small investment that none of us had to pay for, has this huge value downstream.
Neal Ford:
You were talking about different ways of managing open source. I know that Rich has been very adamant about not accepting pull requests from Clojure as ways to modify the language. And his point is that building the code to add some new features, the simple, easy part of that, thinking about the long-term implications of what that does and how to interact with all the other features is a lot of very heavy work. And if he did nothing but look at pull requests, he would constantly reject pull requests because they haven't thought through all those things. And so, it's a different way of evolving it, where a lot of people think open source means that, "Hey, anybody can gang in at any time and make whatever core changes they want," but it's hard to create a stable ecosystem if you do that.
Stuart Halloway:
Well, that's right. Separate from pull requests, any high volume of change... And change is really a dangerous word. Rich gave a talk about this, where he pulled it apart into different words. There is non-breaking enhancement, non-breaking edition. And then, there is taking the name of a thing and having it mean something else. So, you've got a function, or a class, or whatever, a namespace, that meant something in some particular release of your software, and then, you decide you didn't like what that was, and so, you make it mean something else. And people do this all the time. We even have a discipline for keeping track of the cluster effery of the whole thing called semantic versioning. We're going to say, "We're going to break you. And then, we have this whole technology about telling you how we broke you."
Stuart Halloway:
And there's no shortage of names. When I was getting my start, Microsoft dealt with this problem in the olden, olden days. When they decided that they did not have the right semantics around the function, they would make a new function and put a suffix two on it, or a suffix EX. In a couple of places, I don't know if you remember those old Microsoft APIs, there would be, "Do something EX2 EX," where they've made a couple of different versions of it over time. And as silly as that might seem, it's actually better than what we do now. We would be much better off to have new names for new things, even if the names aren't awesome. And even if we already took the good name and we have to put a suffix or something like that.
Stuart Halloway:
And so, Clojure just... We don't do that. We do not take a name that's out in the world and release a new version of Clojure that makes that name mean or do something else. And I feel this on the other side. Datomic has a fairly constrained set of open source libraries that it uses, and they're actually good libraries, and they're well curated, but they don't have this particular discipline. And so, I have an annual, or more often, go through the code base and find places where there was a security patch on the XML library that you have to take, but oh, by the way, they also changed the meaning of this thing. So, now, you can't just get the security patch. You have to say, "I'm going to go and do this yak shave of tracking down what broke and what changed." And there was no need for it. There's no need for that to ever happen.
Neal Ford:
Well, and exactly that point. That's not the way websites work. You don't go to a particular version of Facebook or... Internally, it may be a different version, but the semantics of the thing that you're going to, the name, stays the same because you're always going to the same place. You don't have to know which version of something you're going to because it's all completely hidden inside.
Stuart Halloway:
Well, another great example of it is the several hundred Amazon web services that are out there now. For the vast majority of that stuff, you write a program that uses DynamoDB or S3, and guess what? It's still going to work 10 years from now. There's just not a, "Oh, oops, sorry. It's Dynamo." And there is a new version of Dynamo, in particular, has a new library. But the old stuff works. NI infinity. And I hope that that continues. Amazon, I think, has a great discipline around that.
Neal Ford:
Well, that's also one of the hallmarks of Clojure. I know one of the goals that Rich had when he created Clojure was to create a language that would be very stable over long periods of time. And that's something that I think Clojure... I've heard lots of anecdotal tales about people taking quite old Clojure projects, but they'll be able to build them pretty successfully because not a lot has changed. To your point, you haven't changed the semantics of things within the core Clojure, on purpose, anytime.
Stuart Halloway:
Right. And I wrote the first Clojure book, which is over 10 years old now, and the code still runs. So, there are things in there that would be fairly unlikely to be used in a modern Clojure program. In some cases, there are new features that do a certain task better, or a better fit for a task for which some feature might've been used in the past. So, defstruct is an example of a language construct that doesn't get used very often, but it's there. It's not going to break your program today or next year.
Rebecca Parsons:
Well, and it is a challenge, as a language designer, to be able to think enough about the consequences of some of your early choices to be able to maintain that discipline. I know that's something that I've heard from other people in Rich's position in different language ecosystems. If you're not careful, you can make one very early decision that actually wipes out a fair amount of your design choices, unless you were willing to introduce those breaking changes. And so, that thoughtfulness into the core and really thinking about, "Is this what I want to do," and understanding what those potential consequences are, that's what makes designing a good language so hard. And there aren't that many people who are very good at it and who could maintain that level of backward compatibility for so long.
Stuart Halloway:
I also think that it helped, and this is maybe more just luck in this case, but this was not Rich's first rodeo. Rich had, as I did, came up working in mutable object-oriented languages in the C family of languages. So, C, and C++, and Java, and C#. And he became increasingly frustrated with the expressivity and especially the... Or the lack of expressivity and the fragility of things built with those languages at scale and the trouble that they had dealing with change and concurrency. And so, he looked at a bunch of other languages, and liked some, and particularly liked languages in the Lisp family and Common Lisp and found that he could not get those things. So, it was the same problem that Paul Graham had. You could build something with that and you could succeed with it for a while, and then, somebody says, "We've got to rewrite this in something that we run here."
Stuart Halloway:
And so, Rich had had several efforts at combining Lisps with the JVM prior to Clojure. So, maybe, all the mistakes are in there, Rebecca, so we don't have to know about them. And then, the other thing is just that emphasis on platform, that Rich did not want to build the most awesome academic language ever. He wanted to build a language that he could use, where he was using Java and C# to build production systems. And so, therefore, it was designed, originally, to run both on the JVM and the CLR. And then, Rich pulled his effort back to the JVM. And then, since the original release of Clojure, other people have picked that back up. And so, now you have a Clojure on the CLR. Obviously, you have ClojureScript compiling JavaScript, which was something that we started and led at the beginning, but is now led primarily outside of Cognitect by David Nolan and others. And then, a variety of other dialects and things that people are doing like the babashka for shell scripting in Clojure and those kinds of things.
Neal Ford:
It may be impossible to untangle this, but how much of the stability do you attribute to, certainly Rich's design philosophy, but how much you attribute that to it being in a Lisp? For example, if he had chosen a C-based language instead, could you impose that same kind of stability as there's something inherent in Lisp that makes it easier or more capable of doing that?
Stuart Halloway:
It's a great question. I think that you can have this kind of stability anywhere that you have the will to impose it. The JVM has done a great job of imposing stability. Brian Goetz and other people have done great work there over a longer period than Clojure has been around of maintaining stability. But there are some advantages. And the big advantage... I think a Lisp helps a lot, although you could probably get this some other ways as well, is that the constructs in Clojure are very general, and therefore, there are very few of them. And so, there's just not a surface area that you have to manage.
Stuart Halloway:
And this is the thing that OO, as practiced, got horrifically wrong, which is there's specificity everywhere. You sit down to build anything, and instead of using generic things, like I've got lists, and maps, and structs, you make a class. And beginning programmers are taught, make a concrete class for this, make a concrete class for that, make a concrete class for another thing. And you should almost never do that. When you're making those kinds of concrete things, you're designing a new abstraction. And most of the time when we're working, we're not designing new abstractions. We're assembling puzzles out of abstractions that we already have, except when you do it in object-oriented programs, you have to put an adaptor everywhere because none of the puzzle pieces fit with any of the other puzzle pieces because they're all entirely bespoke. And so, I think that is the...
Neal Ford:
But it just means you get to create more objects and classes. What's wrong with that? Because it's all made of classes and objects. So, you just get to create more and more, and more.
Stuart Halloway:
It's definitely a full employment act for programmers, that we build things that way. And I think that it takes a sensibility and a sensitivity to complexity and pain. And one of the challenges that we have as programmers... I think most of us who write code, one of the things that's really fun is getting into a flow state while you're actually typing in code. I love that. And I can remember, for decades, looking up, four Mountain Dews and eight hours later, and having just been in this awesome flow state, and that's good. I think we should seek to find flow in work. I consider that a key element of satisfaction in the life well-lived is finding that kind of flow. But that flow can just as well be expended building mountain after mountain of complexity, that you then climb, as it can be done building something simple. And getting into that flow state is completely orthogonal to whether or not you've done good design work and whether or not you're maintaining a focus on design as you continue to build things.
Neal Ford:
Yup. You're making great progress, but in no particular direction.
Stuart Halloway:
Right. Or in a direction that will only be discoverable later. But you could have just gone that way. And one of the things that I still struggle with as a designer is the baggage of... Even when they're good thoughts, the baggage of the thoughts you thunk before. So, I was just working on something in Datomic this week where I sat down with Rich and showed him a design, and he was like, "This is terrible." And I said, "Yeah, there's a lot that's bad about it. And it's built out of pieces that we have from doing other things." He's like, "We got to revisit this problem as if you didn't have any code yet." And then, you may decide, having decided what you're going to do, okay, we'll take some compromises here, and we have some existing code that can help us do this. It's not perfect. That's a kind of tech debt you can pick up, using something that's not quite right for the job, but it gets you 90% of the way there. It's a dangerous set of choices to make.
Stuart Halloway:
Another thing that's really nice about Clojure, and this has been especially true as we have started looking at Nubank code bases that are fresh to us, is the surface area is so small. The literal area of source code associated with an idea is so small. And so, sometimes, you'll say, "Oh my God, we made this really big design mistake," in retrospect, or maybe even in prospect. We screwed that up. We made this terrible design mistake on this particular piece of software. And after thinking about it for a week, we can spend an hour and move two small things in one file and have adopted a different design that solves the problem. Whereas my experience, especially with C, and C++, and Java, is that when you've made those kinds of mistakes, they are ramified in 100 or 1,000 places throughout the code. And then, you need tools to help you clean that up, and we have yet another cottage industry of refactoring tools and things like that to help us clean up the messes that we make.
﻿Rebecca Parsons:
You mentioned getting a chance to look at this extensive code base from Nubank and bringing a different set of eyes and probably looking at a way of using Clojure to solve a particular set of problems that had evolved in an organization very different from yours. Have you learned anything about how people who are not as tightly woven into the core of Clojure actually make use of the language to solve these problems? I would imagine that would have been a fascinating exploration to see across that broad of a code base, how people were actually using your creation.
Stuart Halloway:
It's amazing. And it really is. Because we worked as a consultancy for a decade with Clojure, we got to look at a lot of people's code with Clojure. And what we would quite often see is that people would write a Java app in Clojure, or people would write a Ruby on Rails app in Clojure. And not surprisingly, it would have weaknesses that you associate with idiomatic Java apps or idiomatic Ruby on Rails apps because that's, in fact, what they are. And people go to what they know. One of the important things in a Lisp, and I said this somewhere, and it got people excited, is that the boiler plate is always your fault. Right? If there's a boiler plate, and I'm not saying that can't be boiler plate. A lot of times, it's easier to have boiler plate than to come up with the abstraction that would get rid of it. And that's a a trade-off that you're making as you go along.
Stuart Halloway:
But with the expressivity and the macro capabilities, anything that's repeated anywhere, you could make go away. And so, then the question is, what does that look like at scale? And how do you teach a team that's going to be 600 developers, instead of six, how to use it? And I think that Nubank did, before we were Nubank, did some very, very smart things. They have a lot of shared ownership and trust around code. So, people can look at the code, other projects, and other teams, and contribute to it. There is a set of common libraries for common tasks. There is a willingness to explore, but also, let's avoid stylistic variation. If you're employee 300, and you just got hired, you can plan on being part of the early 10% within a few years.
Stuart Halloway:
And so, we have to come up with ideas that are going to easily scale the transfer of those ideas. And so, there's a lot of rigor around not things like arguing about spacing, or parentheses, or things like that. But there's a lot of rigor around project setup and templates. So, if you want to make a new microservice, it's like, "Okay, here's a checklist. Here are the things that go into making a new microservice, do-do-do-do-do, boom. You now have a new microservice. You have the ability to deploy it. You have all the different pieces." And so, that's not something you see in core Clojure. It feels a little more frameworky. It's not, in fact, a framework. You're not living inside of it, and it's calling you. But there's a lot of convention, and it's regularly followed.
Stuart Halloway:
I haven't looked at every line of code, but it's followed well enough that you can come in, and look at a project, and figure out what's going on in short order. And this is a common challenge for me. One of the things that I do on the Datomic team is I'm the final backstop on a lot of support issues as they come in. And so, you get people's reproductions. And they'll say, "I have this problem. I did this thing in Datomic with this query, and X happened, and it was bad." A lot of times they just say, "It failed." And then, you have to ask, do the Sherlock Holmes thing, and figure out what's actually going on. But in that situation, people often have a pile of unrelated code that they built an entity framework.
Stuart Halloway:
And so, the first thing you say as, "Well, there are thousands of people out there using the Datomic query API, and there's just you using the entity framework. And so, just on a statistical basis, if I had to guess where the problem is..." Not that that's always true, right? It's not always true. But that's the first thing you have to get rid of, is you have to factor back down to what the core thing is. And so, one of the things about the common Datomic library at Nubank is it doesn't do a ton of stuff. It does. It does.
Stuart Halloway:
It enforces conventions and so forth, but it's not this complicated set of abstractions on top of what Datomic's doing, such that me or the Datomic expert, who's not an expert in the Nubank code base, I can go in there and look at it, and figure out what's happening quite quickly. And this stands in stark contrast to most other people's Datomic code that I look at. Where the first thing that they did is they said, "We want to have these 17 developer conveniences, and we're going to write wrappers in the library that does all of them all the time." And then, you have to understand what those all are. Those are often complected together to really get a grip on where a problem might be.
Neal Ford:
Well, you accidentally build a leaky abstraction. You build an abstraction, but then, they all end up leaking in interesting ways. And then, you have to find the leaks and the abstractions that are on top of the ones that were already there.
Stuart Halloway:
Right. And there's that saying that the cobbler's children have no shoes. The abstractions that developers build in the heat of combat for themselves, the things that we build around testing and automation, those things, are often really bad. They were built, they were incredibly incremental and feature-driven. I know. I need to build this software. Nobody cares about the software getting built, except that they want to use it, so everything I'm writing to help build the software is just, nobody else cares. And it's just a pile of, "Well, I needed that, and I needed that. And I needed the other thing." And build systems, often, is a great example of a thing that feels like that.
Rebecca Parsons:
We spent a lot of time talking about the history and the heritage, perhaps that's a better word of Clojure in particular, and Datomic, to some extent. What do you see looking forward? Are there directions yet to be explored? I know for example, a few years ago, Clojure Spec was introduced. What kinds of things do you see coming within the Clojure ecosystem?
Stuart Halloway:
Importantly, I think a lot of what will come will be in libraries. There's been very few things that have come along late that are examples of, oh, well, this really changes everything, and you want to rethink from the bottom. Clojure's protocol abstraction came late. And so, if that had been there at the beginning, some of the core stuff could have been built differently. This wouldn't matter to end users. But a lot of stuff since then has been in libraries. And so, core async, go blocks, and a lot of the things that the go language does there, and spec for specification of data, are two great examples of things that are done primarily in libraries. And so, I think we'll continue to see work in those areas. In particular, there will someday be a spec2, I would imagine. There's a lot of design work on it.
Stuart Halloway:
One of the other secrets though to doing this right is being patient. And so, Rich and I, and Alex, and others have talked about spec. We had talked about the ideas behind spec for years before we started writing it. And we have talked about ideas for how to do it differently for years since then. And I totally get people's frustration. Oh, I want to have spec2 and more stuff there tomorrow, but we would rather not ship something until it's fully formed in our minds. And so, that kind of innovation continues, and the pace of it, and even the ordering of priorities is not deterministic. We have, both with Clojure and with Datomic, we manage our internal planning around problem statements, not around lists of features.
Stuart Halloway:
And a lot of times, after you think about, if you get 100 problems in the list, which is kind of overwhelming, but you get them in a list, and maybe get your top 10, and you're looking at those problems, you'll discover, to your surprise, that there's a possible solution that knocks off more than one item on your problem list. And if you had just gone feature by feature, you wouldn't have been able to get there. And spec was a great example of that. Spec was validation of programs at boundaries, is one of the things that feeds into spec. You have a web service and people are calling into it. You want to, at the door, make sure that things look right before you proceed. Generative testing was another problem that spec addressed. With specs in place, you can generate inputs and outputs. And so, there are these different pieces that come together.
Stuart Halloway:
Spec is particularly challenging. I think it can and should be better. And it is a hard area for people to do well because it's very easy to, and it's got the word spec right there. It's really easy to introduce too much specificity. Clojure is a language that's about generality, and people ask questions like, "Well, maybe the first thing we should have done with spec is write spec the whole Clojure language. And then, we could stop people from writing broken programs that are misusing Clojure APIs." But specifications tie things down. And it's way easier to tie things down too much than to maintain generality. And people that use statically-typed languages struggle with this all the time. You have more than one way to express the same idea, and the more general expressions are often quite hard to come up with. And it's easy to pour concrete. I don't think static typing causes concrete, but used a certain way, it spreads concrete pretty quickly. And it's much easier to use it that way than to do the thinking.
Neal Ford:
Just to clarify. Now that Clojure is owned by a bank, do you have to have a bank account in Brazil to be able to use Clojure or to download it? I was just wanting to make sure that it is still actually a fully open source, and there's no evil intent by your new corporate overlords to make it into a purely financial services language or anything like that.
Stuart Halloway:
It's a great question. Obviously, it's a question that will come up again and again, no matter how many times we answer it, so maybe we should just loop this section into the interview in three different places. Clojure's license and contribution model has been consistent since the beginning and continues to be that today. And that's important because it's something that businesses build on, and if you don't have confidence about that... And it's designed not only to do that, but to actually make it not capable of being rolled back. It's part of what these licenses are about. Obviously, anybody who has contributed to Clojure can choose to stop contributing tomorrow. I can take my toys and go home. Well, actually, I can't. I can just go home. That's right. Any toys I've made already, they're there for everybody. And so, that's important, and it's important to Nubank.
Stuart Halloway:
I say "they" because this is I'm thinking about pre-deal. They wanted to do this deal because they want a thriving ecosystem around something that's working for them. And we would be happy to see Clojure as the dominant language for financial services worldwide. That's a benefit. We would be happy to see it be a dominant language in other domains. And in fact, there is, and I wanted to mention this in one of your earlier questions, financial services, in my experience, are incredibly aggressive at trying alternative languages, and not just Clojure. Scratch a bank, scratch a micro trader, you scratch any of these organizations, and you will find 10 times the variation you might expect in terms of languages and things that are being tried because they... Here's the thing. By definition, they're about money. If they find an edge, their translation from having that advantage into money is about as direct as you can get. They already have the money.
Neal Ford:
They're always scratching and clawing for innovation, wherever they can find it.
Stuart Halloway:
Which is great because you want to... You're solving business problems and you want to connect the dots to what's the actual objective here. And this was our experience even prior to Clojure running a consultancy, was that that financial services companies are very aggressive in assessing new technologies. Although, and this is really a credit to Nubank's culture, a lot of financial services companies are a little bit more secretive about what their secret weapons are. They're like, "Oh, this is really good, so we're not going to talk about it." But I think that it's been a great...
Stuart Halloway:
When I first got to know Nubank and was working with them on a consulting basis and supporting Datomic, So over the last several years, I was always nervous about, "Hey, what what could we say in public about what's being done here?" And the answer was always, "Say whatever you want. Don't give away customer data," which I don't have access to anyway, by the way because I don't trust myself. But yeah, how we work is something that we're excited about, and we consider it a calling card. Come and work at Nubank, and you can work this way too. And if you're not allowed to say what that is, it's very hard to tell that story.
Neal Ford:
Well, I think when I first heard it, it struck me as kind of odd because it's an unusual pairing, but it's not that unusual than a database company buying a language, like Java, when Oracle acquired Sun. It's a one commercial entity acquiring something that provides value to them internally and continuing to support it externally as well. Just because it's a bank is sort of an unusual circumstance, but not unheard of by any stretch.
Stuart Halloway:
And I think we have fairly limited set of models for how these things can work. But they can work however they work. As long as they're solving problems, that's what matters. Again, I think it's a huge advantage, Clojure's relative small size and generality makes us agile. In important senses, they're not about how quickly we make new software. We're not expensive for what we do. We deliver a large value for a relatively small use. We don't take up a huge footprint in an org. We're tiny inside of Nubank, the part of the team that's working on Clojure and Datomic, and that's fine.
Neal Ford:
Well, great. It's great to catch up and hear what's happening in the Clojure ecosystem. I've always been a big fan. So, I'm glad to see that it's found a new home and seems to be thriving. So, hope things continue well for you and all of your compatriots. How's your progress on learning Portuguese? Are you learning Portuguese now?
Stuart Halloway:
I stalled out on that. I was working at it for a while, and several Cognitects are learning Portuguese. Obviously, David Chelimsky knows Portuguese pretty well already. So, we have that going for us. But no, I need to up my game there.
Neal Ford:
Well, awesome. Well, hopefully, you'll get to travel to Brazil again soon and practice some of your Portuguese.
Stuart Halloway:
I hope so. And I hope that we all see each other in a safer, gentler world sometime soon.
Rebecca Parsons:
As do we.
Neal Ford:
Indeed. Well, thanks very much. It's always a great pleasure, and it's great to hear what's happening in the Clojure world these days.
Stuart Halloway:
Neal, Rebecca, it's great seeing both of you. Thank you.
Rebecca Parsons:
Thanks for joining us, Stu.
Neal Ford:
Join us on the next episode of the Thoughtworks Technology Podcast, where we talk to Gregor Hohpe about his metaphor-rich book, The Architect Elevator. And we go crazy with all sorts of IT metaphors and make them all relate back to one another somehow. So, please join us for our next episode where Mike and I talk to Gregor about enterprise architecture and lots of other metaphors.
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