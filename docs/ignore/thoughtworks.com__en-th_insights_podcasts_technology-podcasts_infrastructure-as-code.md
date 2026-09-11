<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/infrastructure-as-code | Title: Exploring infrastructure as code | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring infrastructure as code 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons and Neal Ford | Podcast guest  Kief Morris
February 25, 2021 | 34 min 35 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/infrastructure-as-code#transcript)
Listen on these platforms
## Brief summary
Our team catches up with Kief Morris to hear about the release of his updated book on infrastructure as code. They explore how tools, practices and patterns from software engineering can be applied to managing infrastructure — and how IaC has evolved in the years since Kief wrote the first volume.
**Podcast transcript**
Rebecca Parsons:
Hello everyone. My name is Rebecca Parsons. I'm one of your co-hosts here on the Thoughtworks Technology Podcast, and I'm here with another one of my co-hosts, Neal Ford.
Neal Ford:
Hello, everyone. Welcome to the Thoughtworks Technology podcast. And today we have one of our colleagues joining us, who knows all about infrastructure as code. In fact, he knows so much about it, he's written two volumes or two versions of a book, volume one and the second edition of Infrastructure as Code, our colleague based in the UK, Kief Morris. Hello, Kief.
Kief Morris:
Hi Neal, hi Rebecca. Thanks for having me on.
Neal Ford:
And so you can guess, what we're going to talk about today is infrastructure as code, which is what Kief has been working on for the last little while.
Rebecca Parsons:
So Kief, let's get the basics out of the way. How would you define infrastructure as code? Why is this interesting?
Kief Morris:
Yeah, okay. There's several answers to that. Why is it interesting? Why is it interesting to me? I've bounced across software development and systems administration roles, going back 25 or more years now. And so it always seemed like a natural thing to me to try to figure out how to write scripts and code or whatever to make the jobs of systems administration easier. The way I define infrastructure as code, clearly it's about using code to define your infrastructure, but it's more than that, and the way I think about it is about how can we then use tools and practices and patterns and so on from software engineering and apply that to our infrastructure. And then obviously, us having that agile ways of thinking about engineering and stuff, it seemed the natural thing to try to apply that then to infrastructure. Like how do we do test-driven development? How do we do continuous delivery? How do we do even things like microservices and so on? How do we apply those concepts to the problems that arise from when you do use code for all of your infrastructure?
Rebecca Parsons:
When I think about code in general, I'm trying to solve a particular kind of problem. And the scope for the kinds of things that we do with software has just exploded. It used to be very simple, but over time as the technology has improved and such, we've got all kinds of different sorts of problems that software solves and with different kinds of languages, different kinds of frameworks, different kinds of systems tools, we use those different tools to solve these problems. Can you tell me a little bit about the specifics of what is the problem or what are the kinds of problems that infrastructure code has to solve?
Kief Morris:
I mean, overall for me it's about the infrastructure is there to support software and applications, is something to run those things on. So, that's the main problem. And obviously as you say, software and applications are doing more interesting things, if you think about what was going on with data and machine learning and all of that, then suddenly you have to think about how do you make the infrastructure able to support all that. So that broadens a bit the scope. But I think most of what happens with infrastructure and code is really around trying to in some way simplify it or make it more reliable or make it work better. And so there's different parts of the puzzle of what the infrastructure coding, I guess, has to do in order to make that work.
Kief Morris:
So with an infrastructure system, with a system you have to think about things like environments, okay? I want an environment to run my application or my set of applications in, and then I want to be able to wire the things together. So there's, another lens, I guess, to put on it. If we think about the infrastructure that you're managing, like cloud has made this much easier to manage as code. It's been a big enabler for this, the idea that you now have an API that exposes all of those infrastructure resources. And so one level of what you're doing with infrastructure as code is saying like, "Okay, which resources do I need and how do I wire them together? To run my application, I need a server or maybe a cluster of servers. I need some networking, load balancer maybe. I need some storage to attach to it."
Kief Morris:
So it's just declaring, "Here is the stuff I need. Here is how they fit together." And that's the core of it. When we think about infrastructure as code, we typically think about that. But then you get into the kind of problems around that of, "Okay, I have an environment, I have code that defines an environment, but then I want multiple instances of that environment. I want to have a test environment. I want to have a pre-production environment, as well as my production. It's not, how do I configure those? They're not all going to be exactly the same. Ideally they should be consistent in that okay, they have that server cluster or database cluster and networking, but it's like, obviously and our production environment might be quite large to handle the full load that we might have. My development environment probably doesn't have all of that. So how do I scale that down?
Kief Morris:
So you have to think about configuring it. How do I manage the configuration of what goes into each environment? Then you have to think about the orchestration of the different pieces. So what order do I provision these things? Or how do I make changes to things? How do I upgrade things? And that all gets, it gets a lot messier than just that straightforward, give me a server and some networking.
Neal Ford:
This seems like the inevitable consequence of, you go back 20 years and your typology, you didn't need infrastructure as code because it was a database server and an application server and a front end. And so it was easy to catalog, I just catalog the whole ecosystem. But you were just illustrating, with cloud and now search and distributed systems, and things are getting more and more complicated. Just like in the early days of, you could do integration by hand when it was just a few people integrating things. But as it gets more and more complex with more moving parts, you need to automate more and more of that. And you need to go to something where you can declare with some certainty exactly what's here and what's not there without relying on just the simplicity of it being self-evident.
Kief Morris:
But we also had problems even back in those old days, right? Because, okay, you would hand build those environments and you view them as fairly static, but they so often got out of sync in a different ... You'd fix something or optimize something in one environment and not another. And I remember having those problems of like, we deploy our software onto our staging environment. We test it, we'd be happy with it. We deploy it on our production environment and it doesn't run, you know? And so, it was, we always had that, but it's just the pace of it I guess has increased.
Neal Ford:
But it works on my machine.
Kief Morris:
Exactly, yeah.
Rebecca Parsons:
So, how tight is the relationship between the ideas of continuous delivery and what you're trying to achieve with infrastructure as code? In that description it sounded you couldn't do continuous delivery without something like this discipline now within our infrastructure as code?
Kief Morris:
They definitely are complimentary and I don't think it's any coincidence that all this stuff arose around the same time. So kind of around, I'd say 2009, when DevOps as a term emerged and infrastructure as code as a term emerged and when Jess and Dave and other folks were developing the concepts of continuous delivery and articulating that into the book. It was also not coincidentally at the time when I joined Thoughtworks, because it was all this exciting stuff was happening. That was interesting to me. And it's, yes, because it's complimentary and it's like, in order to do continuous delivery, you really need that consistency across environments, because you're saying, "I'm going to push my code. And then I want scripts to be able to deploy it to each environment in turn and just work. I don't want to have to go and do things in a very snowflaky way on each environment."
Kief Morris:
And DevOps came into it because it was like, "Well, we've got our development environments and our test environments that we're working in, and the development team owns those, and then you've got the folks who own the production. You throw this stuff over the wall at them, and then there's that real big impedance mismatch of like, "Well, how do we get this to deploy and run in our production environments or even staging environments?" And so saying, "Look, we can just write some code which says, 'This is how the server is configured.'" And we can run that same code across all the different environments. That just smoothed that path to production to make continuous delivery much easier to do.
Rebecca Parsons:
So we have infrastructure as code. What's the language of infrastructure as code?
Kief Morris:
YAML.
Rebecca Parsons:
Now there's a scary thought.
Kief Morris:
It's interesting. One of the debates that's cropped up increasingly over the past couple of years in particular is this whole thing of, so it's when we started out with procedural languages and scripts, right? So I would write Perl scripts to configure Unix systems back in the day. And then we got into with things CFEngine Chef and Puppet. It was declarative. And I think there was a combination of things there. One was that it was useful to be able to write something which says, "This is what I want. I want this package to be on my system and to have these configuration parameters applied to it without having to also write the code of how to apply the package. What to do if there's a failure? What to do if the package is already there, but it's an older version? What if it's a newer version?"
Kief Morris:
Having to write all of that logic was quite painful. And then your scripts were harder to understand because it mixed all this stuff together. And so the neat things about these new tools was, they said, "Just declare what you want. And, oh, by the way, we'll provide you a domain-specific language, which expresses those concepts." So a package, a file, a user account, things that you cared about on a server. And so the declarative thing and the domain-specific language thing was really quite powerful and liberating in a way. And then similarly, when we got into managing cloud infrastructure, it started out again with scripts. So I would write Ruby scripts to revision, create an EC2 instance and connect a sub-net to it or whatever.
Kief Morris:
But then I was having to write the how again, and then it was when Terraform came out and then cloud formation, tools like that, which did the same thing again of saying, "Here's a domain-specific language, which gives you a model of what are the actual resources of infrastructure and allows you to declare what you want, and the tool works out how." And I thought that was great, but it's interesting, in the past couple of years we've seen a lot of people, and especially from development background and Thoughtworks we've got very kind of development as our strength, and a lot of people very much come from that kind of background. And so, a lot of people saying that, "I don't want a declarative language. I don't want, especially YAML and whatnot. I want something that's a turn in complete, a real programming language that I can write code in."
Kief Morris:
And I think my first reaction to that was, "Well, that seems a step backwards." Going back to writing scripts and conflating the logic with the how to do something with declaring what you want. But where I think I see it actually come into play, where the biggest messes come from, I think, is when it's writing reusable infrastructure code, and especially libraries where you say, "I'm going to write a library that will build a server, and that library should know how to build different types of servers, depending on what I'm asking of it. Can you build me a web server? Can you build me an application server?" And so when you look at like, say Terraform modules, which are written in DSL, which is primarily a declarative language, you get code which is trying to do dynamic things.
Kief Morris:
It's trying to say, "In this situation with these arguments, do this, otherwise do that." And it becomes very messy. And that's where you can certainly start looking at that code and say, "Why am I trying to write some dynamic program essentially in a declarative language that doesn't make as much sense." And so I think that's where new tools like Pulumi and the AWS CDK and these kinds of things are giving us an opportunity to explore new ways of writing our infrastructure code, making more use of reusability and those kinds of things.
Neal Ford:
So, but how much of this do you think is a shortcoming of the tool, versus immaturity in the engineering practices in that space? Because for a long time JavaScript was not considered a first-class citizen. So, nobody wrote unit tests for it, or did the common engineering practices we do now, but then some point you realize, "Wait a minute, most of my system is written in JavaScript. It's not a config language anymore, and you need to learn about modularity and reuse, et cetera." So exactly the point you were talking about trying to build an infrastructure library that's too smart, that can build this thing or that thing or that thing, and you end up building a complicated conditional. Well, if you're an experienced developer, you don't do that. You use something like the strategy design pattern, or you use dependency injection, or some other sophisticated technique to avoid all the duplication and other messy stuff. So how much of this do you think is just a lack of being able to apply good engineering practice because you find yourself in that world, versus just an inherit shortcoming in the tools and space?
Kief Morris:
I think it's a combination, and it's like, it feeds each other. So I mean, infrastructure as code is still fairly new, we're still learning. Wouldn't say design patterns. I think one of the things I'm finding is that all of the design patterns and principles from software do apply to infrastructure as code, but it's like how to apply it to infrastructure as code. How do we make that work? And then the tools I don't think are there, because as an industry and the way we're using it, we haven't been doing that, so the tools haven't quite matured to support those. And so that feeds itself. And then you see, like when you look at like, you're learning a new infrastructure tool and you read tutorials and they're telling you to do things which are actually not good design, just because that's what people do.
Kief Morris:
It makes me think back to the days of like, PHP and ASP and all those kinds of things where it was like, "Hey, wouldn't it be useful, we've got HTML, which gives us a presentation. And I need to get data from my database. Why not just have the code to make my SQL statements in my HTML and I can have my tables wrapped around an SQL query." I'm going to seem real-
Neal Ford:
What could go wrong?
Kief Morris:
Yeah, what could go wrong? It's really convenient, right? And I think it's a similar thing where we hadn't quite worked out how to make the best use of these things and what are good design and therefore, what are the right languages and things to make it easier to use good design?
Rebecca Parsons:
You should be warned, Neal and I are both languages geeks. So I want to push you on this a little bit, because you're trying to get an OO programmer or a procedural programmer to think about how they might solve a problem in Prolog. It's a different mental model for what computation is, it's a different modeling exercise. Let's explore a little bit. Is it just that the people who are designing these DSLs are too steeped in an imperative construct? And so the abstractions that they naturally think about are more tuned to some kind of imperative language, as opposed to the declarative?
Rebecca Parsons:
If we push a little bit on the places where you feel this breaks down, is it just that the abstractions are wrong? You talked about servers. Why would you, if application servers and database servers and web servers are so different, why would you smush them all into one library? Is there some kind of module system or some way to replicate what we get from the strategy pattern as part of the abstraction? I mean, I'm not yet convinced, and it's just always so easy to say, "Let's just put in a loop and conditionals and be done with it." And once again, you have a DSL that explodes into a general purpose programming language that happens to have a few more data types.
Kief Morris:
Yeah. I think if you look at, so, and I'm not a language geek, so it's really interesting having this conversation and getting that lens on it. When I look at most of the infrastructure languages, I'll focus on the ones that are around cloud stuff, so Terraform, CloudFormation, these kinds of ones, really are they, what they present to you are the resources that the cloud provides. Really they support the API, right? So each of these, the cloud platforms have an API, which says, easy to instance, virtual machine instance. And then they have parameters to pass into the API, which tells you, "How much RAM do you want and CPU's and all that stuff?" And these languages are just that put in a ... Declare that. EC2 instance, values to put in, attributes to pass to the API. That's really all they are.
Kief Morris:
And then when you get into the, "Well, okay, as a user of this language, I want to write some reasonable components, because I've got 20 development teams and they all want to do things, and I want to make it easier for them and give them some libraries to use." The tools I have are just that declaration of those elements, those infrastructure resources. And they put in things like, so you have some basic things like, "How can I make parameters to pass into my modules?" And they might give you some crude things that you can use as conditionals and loops and all that. And then I've got to try to make a reusable component out of that. So the abstraction layer is that very low level thing.
Kief Morris:
And I think for some people that works really well. So as somebody from a sys admin background, who says, "I know what infrastructure I want, and I know how to wire it all together from those primitives. That's cool, that works well for me." But if we start thinking about the abstraction level is, "Well, I want to provide to a development team an application server and related infrastructure." So to start thinking about, to my mind I think what we want to do is have a domain model that is above those primitives.
Kief Morris:
That is more at the level that an application developer cares about. I want a database. I want some servers to deploy my application onto, and I want to be able to route traffic to them. I don't want to have to think about the details below that level necessarily. And it's hard to build that with the declarative languages that we have. I think that's what seems easier to build with these things like Pulumi or so on which are like an object model, right? I can make an actual object-oriented, I can make some class diagrams that represent that layer.
Neal Ford:
Yeah, I think it's interesting getting the abstraction just right, because normally we write code to describe a purely abstract problem, some sort of business problem domain, leasing, or something like that. But you're building code that is a very, very focused concrete abstraction, which is, this code's going to turn into machinery that actually produces output, inputs an output and that kind of stuff. So I think finding the abstractions that are exactly right to that world is maybe even more critical, because there's a lot of leeway when you're building castles in the sky in terms of what attractions you use. But if you're building something as physical as what you're building, it seems it limits the number of attractions you can effectively use there.
Neal Ford:
And there's probably some sort of sweet spot. I mean, exactly toward Rebecca's point, instead of putting a loop in a language that, if you do something more functional and have something that returns you the list of all the servers that match this criteria and then apply this thing to all of them. Well, that's sort of a loop, but it's not really a loop. You're really doing a map operation, functional programming. So, that concept mapped into infrastructure seems a useful thing without necessarily going to loops or other imperative, or even object-oriented paradigms. I think finding the right paradigm for that infrastructure as code, it may be more critical in this area than it is in other problem domains.
Rebecca Parsons:
Particularly since the domain is getting inherently more complex. And if you look at the evolution of, we'll stick with the cloud scenario, with the evolution of the services that are available from the different cloud vendors, that underlying primitive layer of the API is just becoming more complex. And it is going to be even more difficult to try to stitch these things together when you got a proliferation of low level constructs without really the right abstraction layer on top. I mean, I understand why the cloud vendors are giving you that low level thing, because that's their API and they're asserting, "Okay, these are the things that I'm going to make available to you." It doesn't necessarily feel like it's their responsibility to craft some of these higher level abstractions that would be useful to a different audience.
Kief Morris:
I think to some extent they are, the things they're putting together. Some of them are abstractions or combinations of stuff. So if you look at things like clusters, like a Kubernetes cluster, for example, they're kind of in assembling all those kinds of things servers and some of the networking and all that together, and then they're putting an API on it. So they re kind of putting that together, and the code level just then sits on top of that. So then that's a, you're now at different layers of abstraction and what's being provided by the cloud provider and what you're trying to define as code and configure as code just is interesting.
Neal Ford:
Well, it's inevitable. I mean, when we think about computers, we don't think about spinning metal discs with rust on them and arms and binary. And it's just more and more abstractions. I mean, our entire computing life has been one abstraction layer after another. So this is just another layer of abstraction on top of the ones and zeros.
Rebecca Parsons:
And they all link at different rates.
Kief Morris:
Because ultimately that's the idea of the cloud native thing is it's like they're going up to the server list where it's like more and more stuff is being abstracted. So you have to think about less of the details of what's underneath. And you're still putting code on at each of those levels, but you're having to manage less or define less with your code, because the platform is giving you a bit more.
Neal Ford:
I would argue a little bit that you think about less details. It changes the details you have to think about.
Kief Morris:
Yeah. And hide stuff, right? You do have the whole thing of then it becomes a lot harder to understand what's really going on and why things are behaving the way they're behaving. I think another dimension, there's a couple more dimensions to it, and we're talking about them. I'm really interested in this whole thing of like, "What's the kind of, I don't know, the domain and the domain model of this stuff?" Because there's the aspects of things like, "Okay, what are the actual resources that you want to have provisioned and that you want to wire together?" And then how do you configure? So if you have, like let's say you have some code that you want to use to create multiple environments, because you want those environments to be consistent. So then how you configure different instances?
Kief Morris:
And that's one of those places again where I think you start seeing messiness creep into how people write code, because it's you have your code, which says, "Here's my server." And then you have like, if an environment is dev, then pass these parameters, if it's QA, if it's staging, if it's production. And so that to me feels like a different concern. So like going back to the kind of good software design, you want to have separation of concerns. And it feels like having the same code do both of those things of declaring what infrastructure you want and how to configure it in different situations are a mixing of concerns.
Neal Ford:
I like your UI example of JSP, or ASP, or PHP, or something like that, which is the classic example of mixing concerns. But you can see the exact same mixing of concerns in the infrastructure code too, so.
Kief Morris:
And then there's a whole other dimension, which is the change to stuff. And I just have to think a little bit about how the comparison of software. But when we often think of infrastructure, one of the pitfalls we fall into is thinking about it as, you build some infrastructure, you build an environment, and then it's there. And the tricky thing is, what happens if I need to do an upgrade, or I need to do a patch or I need to do a change. And with infrastructure, going back has always been the hard part. It's always been easy to build your infrastructure design and build your infrastructure. But then it's like, how do you make a change to it without disrupting everything? And that's something that I don't think infrastructure code tools have really worked out.
Kief Morris:
You can do things like a plan where Terraform will tell you, "Okay, these are the changes I'm going to make if you run me." But you don't really have that ability to intelligently say, "How do I make changes to my running infrastructure in the least disruptive way." And you really have to go outside the tool. What I recommend to people. And the webinar that I had with Thao [Dang] a while back, we talked a lot about how to refactor infrastructure. And the way I always say is to do like you do with databases and where you use code to change schema, where you do the multiple changes to do the kind of expand and contract. Add the new thing, move a thing over, then move the traffic over, then remove the old thing. And that's what you have to do for with infrastructure code. And I feel that can't be how, that can't be the best we can do. There's got to be a better way, but I don't know exactly what that looks yet.
Neal Ford:
Well, one of the interesting things about infrastructure code is there's a temporality built into it. One of the things, the observations we made in the Evolutionary Architecture book is architecture's abstract until it's operationalized. In fact, I would say that you don't really understand your architecture until you've put it in operations and you've upgraded at least once. Because that's when you really find out when things break, et cetera. And so I think that's exactly the same thing we're looking at here that there's a time element in infrastructure that you know it's going to change over time. Nothing is static in that world.
Neal Ford:
And so how do you manage that Delta over time? We don't think about that in business applications because we have discreet drivers that make us change things, changing market, or changing requirements or whatever, and it's all controlled. It's much less controlled in the infrastructure world and much more reactive than proactive in that world, because you know, an upgrade comes out and it forces you to change something. And that can have a disruptive effect if you didn't plan for it. So I think some of the abstractions in the domain models there need to take that temporality into effect much more strongly than in "regular," I'm using air quotes here, "regular" code versus infrastructure code.
Rebecca Parsons:
So the second edition of the book is out. What are the major drivers for the second edition? I mean, how would you describe, was it everything changed, or were there specific changes within the capabilities, the things that you were trying to describe that you felt needed a second edition?
Kief Morris:
In the kind of the, I don't know, the tooling and the industry and the space of what's there. And then a lot's changed in terms of, I think what we've learned, sort of what I've learned, and good ways to do this. So just as some examples, the first edition was subtitled, Managing Servers in the Cloud. Because that's where most of the action was, was configuring the servers. And that's become less of a thing these days is there's a lot more on clusters and those kinds of things. So it's not that that's gone, but it's like it's no longer the central element of it. Other things that have changed are, well the adoption of cloud has become a lot more mainstream. So I found out, as I was going through the first edition manuscripts and looking at what to bring over, there was a lot of stuff trying to persuade that like, "Oh, you really should use a cloud rather than trying to do it all in your data center."
Kief Morris:
And it's like, "We don't really have to make that argument anymore. We're past that." And there's the obvious stuff like, I have maybe a few pages on containers and Docker in the first edition, much less container clusters. And now it's much more of a thing I always get asked, "How does infrastructure's code fit in with clusters and with serverless?" And so I had to talk more about it.
Kief Morris:
But I think other than that that's happened as we've seen. And we've seen this on projects here with our clients where it used to be, using infrastructure as code and where I came into it was going to clients and do continuous delivery and saying, as we were saying earlier, "You really should automate how you configure your environments to make them more consistent."
Kief Morris:
Now we're showing up at clients and they've already got it. They're in the cloud. They've got some of these tools and they're doing stuff, but it's in kind of they're struggling, right? Maybe it's grown out of control. And so one client I was working with, they had a Terraform project that would take up to two hours to run terraform apply on the project.
Kief Morris:
And it's interesting. It's interesting from the perspective of what we do as Thoughtworks is we're often going into clients who have these big code bases, application code bases, and helping them to sort it out where they've gotten to. And now we're starting to do the same thing with infrastructure. And so if there's a lot more, I focus a lot more in the second edition about design, those kind of software design principles. And I talked a lot with James Lewis and kind of noodled around like, how do we apply some of the concepts from microservices and just generally software architecture into the infrastructure.
Kief Morris:
And it's because it's, how do you tame those big systems where it takes two hours to run terraform apply while at the same way we tamed big applications that took two hours to compile or whatever, right? It's like, we've got to break it into smaller pieces in order to do that and to be able to change it and evolve it while we have to write tests for it, and we have to do pipelines for it. We have to think about things like the separations of concern between the parts of our infrastructure, loose coupling and cohesion and then all of the same things, stuff that we have to do with our infrastructure code now. And so that was a lot of what's gone into this book that wasn't in the first edition was how to apply that thinking.
Rebecca Parsons:
How to dig your way out of the hole that you built, applying what was in addition want. Now that we know more.
Kief Morris:
Yeah, yeah, yeah.
Neal Ford:
Well, but it sounds like it's your opinion that in the near term at least that the maturity in that space is going to come from learning about better engineering practices, testing, abstractions, even, heaven forbid, something like interdependency injection may eventually make its way into that world [crosstalk 00:32:14].
Kief Morris:
Yes, talk about interdependency injection, yeah, because that's definitely a thing. And it's that there's the kind of the state of the industry where we are now that I don't think as an industry we've quite grasped this. And so, you'll see lots of tutorials, even from vendors suggesting things where it's like, write some code that reaches out and grabs the things that it needs from some other part of the system in another part of code, which we learned not to do that with our application code, but we need to relearn some of those lessons. Hopefully we'll learn them a bit faster since since we've seen examples.
Neal Ford:
One of the things that we ask a lot of authors, particularly authors of second additions was, "What was it like doing writing the second edition of a book that you've already written the first edition?" I remember having some conversations, actually, this is a random thought. But you and I both spoke at an Exconfig event in Europe the end of 2019. I can remember a cab ride in Barcelona for some reason where we were talking about what was going into the second edition. So what was it like writing the first and then revisiting it for a second edition?
Kief Morris:
In some ways it's liberating, because it's like it gets pent up. Because as soon as the first edition came out and then you're talking to people, giving talks, going and visiting people, and you're immediately learning stuff that it's like, "Ah, I should have put that in there." And so that accumulates over the course of years. So it's great to be able to get it out. It's just, I rewrote so much of it. I thought about, I didn't manage to run a tool on it to compare to see how much, what percentage of the content is different. But it was, I would say 80% probably of rewrite.
Neal Ford:
That's actually been my experience that people who revisit books like, "Ah, just a few tweaks here and there," then you end up rewriting the entire thing, pretty much. Well, that's great though, because now we have brand new material, especially in an area that's moving as fast as infrastructure's code. So it's great that there's a second edition of your book out. It's great that it includes now more learnings from the real world and will allow people to accelerate hopefully even faster in adopting some of these things.
Rebecca Parsons:
Well, Kief, thank you so much for your contributions through the books, as well as joining us today on the Technology Podcast.
Kief Morris:
Thanks for having me. It's been a really fun conversation.
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