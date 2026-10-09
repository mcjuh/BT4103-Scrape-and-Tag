<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/low-code-no-code-platforms-ten_percent-trap-limits-abstractions | Title: Low-code/no-code platforms: The 10% trap and the limits of abstractions | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Low-code/no-code platforms: The 10% trap and the limits of abstractions 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Mike Mason | Podcast guest  Scott Shaw and Xu Hao
December 01, 2022 | 30 min 25 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/low-code-no-code-platforms-ten_percent-trap-limits-abstractions#Transcript)
Listen on these platforms
## Brief summary
Low-code and no-code development platforms have been heralded in recent years as a solution to engineering talent gaps and as a trend that will properly democratize technology, allowing even non-coders to build applications from scratch. However, despite the marketing rhetoric, such platforms pose considerable challenges: _how do they fit alongside existing development projects? To what extent do they enable or restrict our ability to build the kinds of software we want and need?_
In this episode of the Technology Podcast, Neal Ford and Mike Mason are joined by Scott Shaw and Xu Hao to discuss the state of play in the world of low-code and no-code. They explore the different types of platforms that have emerged in the space and ask what organizations need to consider before they invest time, energy and money in integrating them. 
## Episode transcript
**[Music]**
**Neal:** Hello. Welcome to the Thoughtworks Technology Podcast. I am one of your regular hosts, Neal Ford, and I'm joined by another of our regular hosts today, Mike Mason.
**Mike:** Hi, Neal. Very happy to be here in person for a change. This is great.
**Neal:** We are, in fact, in person here in Barcelona as part of the Doppler meeting. One of the discussions that perpetually comes up in our Doppler meetings is around low-code/no-code environments. We have two of the Doppler team members here to discuss this topic. One, you're already familiar with, because he's normally one of our hosts, but he's a guest today to talk about this — Scott Shaw.
**Scott:** Hi. I'm Scott Shaw from Melbourne, Australia, despite my accent.
**Neal:** The other is from China, our colleague Xu Hao.
**Xu:** Hi. My name is Xu Hao. I come from Thoughtworks China.
**Neal:** As I mentioned, we're here to talk about low code-no code environments, which is a big topic. It's a big marketing push by a lot of organizations in the current day. We have, as Thoughtworks, traditionally been a little bit… not the biggest fans of these kinds of environments for reasons we'll get to in a second. But it's probably a good idea to talk about the spectrum of what these tools look like. What are some of the examples of no-code/low-code, and what are we talking about here?
**Xu:** Usually, for me, it's, I would like to separate the no-code from the low-code because they have, clearly, a different target audience. When we are talking about no code, they pretty much focus on the people who don't have any technology background. They don't want to write any code, but they would like to create a small application. One of these examples I can think of is WordPress. Today, they have a really vibrant ecosystem. You have a lot of plugins you can use. Based on WordPress, you can build your eCommerce website like designing lines of code. That is a no-code for me.
Also, the low-code is more targeting someone who already knows how to write code, but in a particular domain, they want to write less code or some sort of like this scenario.
**Neal:** We used to, tongue and cheek, call some of those environments “cartoons to code” where you draw lines between things to create connections or for workflow engines, those kinds of things.
**Mike:** Doodle way.
**Neal:** Doodle way! Exactly. That's another of our derogatory terms for tools like this. I think a lot of that disdain comes from, there's a whole generation of case tools, these computer-assisted software engineering tools that were supposed to write code for you that were all these doodle way kind of tools that we got burned by, but as Xu Hao was saying, this is really a spectrum from one end or the other of how much code do you actually write. That gets more into the low-code kind of stuff.
**Scott:** Yes. I think even with no-code — many of the no-code platforms, you still have to write an expression at some point when it comes down to the leaf of the tree, you have to write some kind of expression and understand basic logic operations.
**Mike:** We've been looking at low-code platforms recently. I think one of the things that became really obvious to me was that because they are a form of abstraction — like all of the things that we use in software; like JavaScript is an abstraction in some way over assembly language, which is an abstraction over CPU opcodes. All of these are raising levels of abstraction. You need to understand a certain amount of what using that abstraction is going to actually do for you at the end of the day.
So when you're writing an expression in a leaf node in a GUI editor, you actually need to understand, okay, what's that going to do, roughly, to the architecture and composition of the no-code thing or low-code thing that is produced at the end of the day?
Personally, having looked at this stuff for a while, I think one of the problems is this vendor hype around not needing technical people anymore because actually, to get the best out of these things, I think you do need fairly technical people. If you don't have technical people you tie yourself in knots. Then the traditional programmers come along and say, "Hahaha, what a nice mess you've made. Let me dig you out of that hole."
**Neal:** A perfect example of that is the common problem that you run into often with rules engines, which are specialized low-code/no-code environments, as you are writing expressions. The problem you run into there, very often: rules engine sounds great, let the business people write the business rules, but then they don't really understand abstraction.
When it comes time when I have this complex workflow that needs a slightly different step, they don't understand abstracting common behavior, they just copy and paste so that your rules engine, over time, becomes these copy and pasted almost identical workflows that nobody can understand anymore because you don't have abstraction, which is something fairly technical kind of thing to be able to understand.
**Scott:** I think it's really important that the abstraction or the metaphor matches the domain — matches the problem. I think a good example of that is Excel. If you're an accountant, an Excel spreadsheet is perfect. If you have columns of numbers and you have to do operations on those numbers and have that be reactive, that's great. We've all seen people squeeze Excel into places it should never have gone and use it for all sorts of things. It's so convenient it's really hard to avoid doing that. We're all tempted to do it. I've done it too.
**Neal:** Yes. We have — Thoughtworks as an organization — never misused spreadsheets or Exel for anything… [Laughter]
**Xu:** I think one thing is, some of the low-code platforms that provide an abstraction that may be oversimplifying because some of the low-code platforms are going to say, “okay, everything is a business process,” or “everything is a workflow,” or “everything is a form.” Some and better are going to say everything is a form plus a workflow. “Everything is X.” That is actually one of the problems. As a developer, we know, even when we say everything is an object, then we're still getting into trouble 'cause we're running into real code.
**Neal:** Well, that brings up one of the first low code-no code platforms, HyperCard, where everything was a card. You could build really sophisticated applications with the Apple HyperCard in the early Mac. It had this card metaphor, which-- but gets exactly to this question of abstraction. How far can you push that card abstraction until it finally just breaks? We've taken a document presentation format and built an entire application ecosystem on top of it with HTML and HTTP. We're guilty of misusing abstractions ourselves for–
**Mike:** A programming language that was created in a weekend for a crate of beer or something..!? I don't think that's actually true, but that's the apocryphal genesis of JavaScript…
**Neal:** Let's talk a little bit about why we have traditionally not been a huge fan of this and come up with derogatory terms for them. Why is some of that starting to change? We are seeing so many of these. Something that doesn't die off on its own evolves and becomes useful in many cases. One of my criteria that we've used for a long time — this is actually in the Evolutionary Architecture book; we talked about how evolvable these things are — is that, too often, people focus on the benefits you get from this low-code environment — quick, rapid application development etc., but they don't look at the things you're giving away.
One of the things I always say is, you can choose a low-code environment if it supports things like versioning and the ability to diff and having a refactoring IDE and the ability to unit test all of your little bits at whatever level you want because you have all of those things within regular code— and you have to give that up in a lot of these environments. Some of them support some of those things, but abstraction is another one of those things. The ability to have refactoring and extract methods, etc., which is more and more sophisticated but needed in more cases. A lot of the low code-no code tools don't support that.
The last bit I'll say about that is something that we talked about — I've talked about for a long time — that all of these fall into, eventually, which is why the fourth generation languages, which were all the rage for a while eventually faded away, is that them and low-code/no code environments suffer from what we call the last 10% trap, where the first 80% of what you want to build is very fast and easy, rapid, the next 10% is possible, but the last 10%, you can't get far enough underneath the abstraction to actually get that done.
You always want a hundred percent of that, which is ultimately the failure of HyperCard, the reason we're not using HyperCard for everything, because, at some point, you reach the limit of that abstraction and you can't get underneath it to build useful things. We always go back, for that, to very general-purpose languages. That was always my criteria. Anybody else have any criteria they want to add to that?
**Xu:** I actually have two criteria. One is actually the modern no-code/low-code platform is actually getting better. One of the criteria is that you have a separation between production and development mode. The early generation of the low-code platform, they don't really have a sense for, “here is my production environment.” You usually have a back office or you have a different mode. Then what you put in there goes into your production environment. The reason low-code platforms they're getting better in this area. I don't know. Today, maybe they're doing much better.
Another criteria that is interesting — if I'm using a low-code platform, is there a way I can change back into the normal development environment? The reason being, I think that's a fundamental logic for this low-code platform. They assume the user is going to be an absolute beginner because for an absolute beginner, you don't understand things. You don't really understand how everything goes but you want to do something quick.
That is actually true even for a proper programming language because I still remember when I starting doing, like, Delphi 20 years ago. At first, I go to the UI builder that is much nicer, then later when I have more experience, I can write the whole UI maybe totally from a coding perspective. I'm actually from a total beginner I become a more advanced user.
Most of the low-code platforms just assume all the user is going to, let's stay for an absolute beginner forever. That will become a true frustration because you don't want to really do similar thing for two, three years. You already know a better way. You already roughly know how the things work. You're going to figure out a way to become more productive. That is, for me, is there anything so I can change the whole thing back into code? That is actually really important for me.
**Mike:** I think a little bit on that — there has been a rise of professional low-code platforms. I think they're labeled where the intention is that people to get good at using them and understanding them and even understanding a little bit about the abstractions that they should create to avoid that copy-paste problem.
**Scott:** I think you should look at what the learning curve is to become that expert. If it requires deep expertise, then you have to ask yourself if you're really getting the benefits that you were expecting to get from the low-code platform, because it may be harder to find people with that expertise than it would be to find programmers in the first place.
**Neal:** That I think gets to where we're seeing more and more of these show up, but these really rarefied domains where you would build years of expertise. There are a lot of these tools around orchestration and distributed architectures, for example, or building these workflows, business-based workflows. We see a lot of these low code-no code environments for that, where building up several years of expertise is actually useful because these 80% workflows are really common. The kind of things that we used to build in Microsoft Access and things like that, forms-based applications.
I think we are seeing more of those platforms support years and — not a career's worth of development, but more than a few years worth of development worth of payback to learn it.
**Scott:** I think often that expertise is needed around the deployment process and around the separation between production and test that Xu Hao was talking about. Yes, you can do it, you can separate those things with a lot of the tools, but doing that sometimes means you need to get out of the covers. You need to understand the guts of the system. You need to know a lot of secret variables and switches and forms. I think that defeats the purpose.
You need to be able to not just develop an application, but develop an application in a professional way that's well engineered and do that within the context of the tool that you've been given without having to go around and go under the covers to make it happen.
**Mike:** I think we have to realize that we're coming from a particular perspective here, which is we are used to developing software using traditional coding techniques, armies of developers who are reinventing what we hope is the cutting edge of the best way to do software always. We haven't even started talking about things like AI-assisted programming and then stuff like that. — That will be for a different podcast…
The thing that I think is quite interesting about low-code platforms is that in many ways, they're not a competitor to what we already do. I think it's more of an end. There is more software in the world that people would like to create, but that we can't necessarily create with the current set of programmers that we have. If we have a different set of tools for people, maybe they can take that on.
I think one of the things that I found interesting when I was looking into this stuff was, we would look at the software delivery lifecycle and Thoughtworks would have a lot of opinions about that having written the book on continuous delivery and stuff like that. We'd have some fairly strong opinions on what we think a good SDLC looks like. But some people who are picking up low-code platforms don't really have an IT department or don't have much of one, and certainly don't have developers who have a strong inclination towards TDD, continuous delivery, and all those kinds of things.
For some of them, picking up the out-of-the-box software lifecycle that a low-code platform gives you, is actually a step up. Even if the versioning isn't exactly what we would like, and you can't actually view the diffs in the way that we would want to, the fact that there is some version control, the fact that there is some separation between environments and some notion of promoting an artifact to another environment, that might actually be quite a useful increase in — that might actually be a good step up for some [crosstalk]
**Scott:** Yes. Particularly when you're talking about internal applications where you don't have a customer experience you're trying to worry about, utility applications. I have a lot of empathy for the businesses that want what intuitively seems like a really simple application, or you want to make a change to an existing application. "I want to change the color of this button," and you get a quote back for $200,000 to make that change. That's ridiculous, and so I understand what the motivation is, and it's definitely the tradeoffs are there, many times.
**Xu:** I think the scenario, like you described, is more towards no-code rather than low-code because — I can share some of the cases. One of the cases is really popular in China, that is actually in Taobao. That is one of the largest eCommerce website probably like in the world. Most of the site around Taobao, they only have 5 to 10 people — really small business, they don't really have strong IT department.
In order to have your inventory data working properly and you can integrate your own spreadsheet with the Taobao system and with the payment, these sort of things are really difficult. Then Taobao has an ecosystem. They build a ecosystem. It's more like a marketplace strategy, so if you're a business owner, you can pick up all those plugins or similar applications. They have some customization features and then they have this integration. If you're using other software, they can much more easily be integrated with Taobao. That is more like no-code — most of the time, you don't really need to write code, but you need to know how to config this plugin.
Now, an example is the product we integrated from China many years ago, that the golden data. That is really, really simple. You have a form-based application that is heavily used by our admin team. They were actually using that to create a form, like sending out, collecting some data, and then just quickly processing that. That actually supporting 80% of our operation procedure within China. Also for that product, they're heavily used in even smaller businesses.
One or two people — really, really small business. They don't even connect with Taobao yet. They're more like on WeChat. I was sending out a form into a group of people if they want to buy something. There's just fill in the form. I have people processing the form at the back end and then sending out the product. That for me is more towards the no-code scenario rather than a low code because, in that case, you shouldn't even think about anyone to write a code.
**Scott:** It's a very specific domain too. I think there's some tools — some of these platforms are trying to be completely general. That's where I think you could get into trouble. You expect it to solve all of your problems with one package. I think being as narrow and targeting it and being disciplined in your business about where you use that, where you apply it, because there's… Vendors are going to want you to use it for everything in the end. It's really important. I think it's up to you to draw the boundaries for the architects or the people who are defining how the product is going to be used.
**Neal:** That's a good way to arrive at our first piece of concrete advice that we can give from this discussion, which is: manage expectations for these things. This is one of the reasons I think that we have traditionally been annoyed at these tools because they are so overhyped by the marketing departments and these tool vendors and that always annoys people — when you see someone promising the moon when you know they can't actually deliver the moon. Managing expectations I think is important because for exactly the case that Xu Hao was talking about, you don't expect to be able to build a sophisticated application with this series of plugins, but you know what your limits are.
The exact same is true I think for the most pervasive, by far, low-code environment on earth, which is Excel. But people are happy in Excel because you don't try to build excel into a web browser or some other different application because you understand the abstraction so well and you understand its limits so well and so You don't try to turn it into some Frankenstein monster — which is unfortunately not true with some of these low code-no code tools which sell themselves as the solution for everything. I think that's really important: understanding what it's good for and importantly what it's not good for.
One of the piece of advice I give teams when they're evaluating these things is, the normal way you evaluate something is the Hello World. If you can't get Hello World to work in low code-no code, then what are you even doing there? That should be beyond trivial. You should try to find some of the edge cases you think will push up against where it will break to see exactly where the edge of its capabilities are because then you can plan to supplant that with something else, or should we use this or not? Understanding its extent I think is really important early on.
What's some other concrete advice we can give people as to ways of choosing these things intelligently? Because they are here, they're never going to go away and they are useful in many situations, so in what situations are they useful in?
**Scott:** I think it's really important that you be able to get your data out. Because no matter how great your platform is, at some point, you're probably going to want to migrate away from it. At some point, you're going to want to replace it with another tool or another platform or even just upgrade. There are so many of these tools that I've seen that the data checks in, but it doesn't check out.
You have to go through extreme histrionics — or maybe there's no way. That actually applies to a lot of ERP tools as well. But I think you should look at what are the facilities that I have for just dumping and getting all my data back from the vendor.
**Xu:** For me, the key thing for the whole podcast is really know your audience. Hopefully, is going to be the real user for this low code-no code platform. One of the trends we have seen in the industry when we're talking about DevOps, we're actually building a lot of tools in our application to enable the operations people so they can actually do this sort of thing. We're actually starting to be building our own low-code or no-code environments because it’s already built into your application anyway.
Most of the time, you're going to have a bunch of scripts, you're going to run, you're going to generate a health-check page and then usually you're going to have small functionality helping you to do a really quick thing like on there. You probably want putting in more functionality in there. We are already seeing some of time, they have really, really at once DevOps, they're starting to build in their own low code-no code platform for their operation people.
That is actually, if you think about, if you know your boundary, if you know this… maybe like Homebrew low-code platform is a better option rather than buying something.
**Neal:** I think that's important too because that becomes a design consideration for the tools you build, is composability. The units from… very famously was designed for all those things to be composable so you can wire them up in all interesting ways. If you do the same for some of your observability and other kinds of ecosystem support, then you can start building simple little tools to wire them together in ways where the sum is better than parts,
**Xu:** Yes, sure. In that case, you may find a low-code platform really appealing quickly because you already have all this composable action and then you need a workflow engine to match them up. You're probably going to find a low-code platform like it's right there for you. I usually now is thinking, starting with a low-code platform, but maybe end up with a low-code platform that may be in another, like otherwise
**Mike:** I would add a couple. One is it's okay to have the right tool for the job, and it might be that you want more than one low-code platform in the building because they do do different things, have different metaphors. A lot of them come at very different price points, frankly. Those are reasons that you might want more than one.
Secondly, using low code-no code is a technology decision and it's technology related. These things should be done at least with the involvement of the IT department. I think it's a big mistake either for IT to abdicate responsibility for that or for non-technology pieces of an organization to say, okay, well, we're doing this and steamrolling the technology folks who should have an opinion. I think it needs to be a partnership for it to be successful.
**Scott:** I think you need to check with your design department too. [laughter]
You need to — seriously — if you're planning to use the front-end aspects of some of these tools, you should decide how important the user experience is for you. How important is it for you to be able to customize and tweak that customer experience? I think there are ultimately going to be limitations, even though they're getting better and better at that over time. I think you really ought to check with the customer experience people, the researchers, and the designers as to… Even if it's an internal application, you might want to give a level of personalization or customization that the tool doesn't really support.
**Mike:** That the tool doesn't really support is super critical there. This is coming back to Neal's last 10% trap. One of the things that I worry about is if you give a low-code platform to some competent technologists, they will twist it into doing whatever you ask them to do, which might actually be a really bad idea. You should stop at that last 10% that the thing can't really do because to get to that point, you should have made choices knowing, going into it eyes open, that it's not going to do X and Y and Z and that we don't want to–
All the vendors will say, "Well, you can just drop down and write real code." No, you shouldn't, though, right!? That's not the point of the tool! If you find yourself compelled to do that, then you’ve got to reevaluate that decision.
**Xu:** They're actually going to stop you from operating towards a newer version.
**Scott:** I think you also want to think about how the features of this tool extend beyond the boundaries of the tool. You're probably going to want to consume APIs for example. How flexible is that mechanism for consuming APIs? Are you actually going to actually have to change for the development that you're doing in other parts of your organization? Are you going to have to adapt so that your low-code tool can consume that data? I think that's an important thing to look at.
**Neal:** Not only that but things like testing. That's one of the things that the modern generation of these tools support more engineering practices like being able to support your data but also being able to support things like deployment pipelines and continuous integration and some level of testing beyond just testing the entire system all the time. That's one of the things that make us less mad at these tools, is that they're playing nicer with the ecosystem support that we like to see for the other bits of our software.
**Scott:** They're getting better at checking into normal social control systems too — about being able to dump out a text file that defines all the system and lets you check it in with the rest of your assets and version it with the rest of your assets.
**Neal:** So, any last remaining advice for people out there who are struggling to try to figure out? Should we use this low code-no code environment or should we write it from scratch, or?
**Scott:** I think having some really clear guidelines that if you're going to adopt the tool, make sure that everyone in the organization who is going to be affected by it knows where you should be using the tool and where you shouldn't be using the tool and what the boundaries of that are. It's really important to have some criteria to define how complex an application written in a low or no-code tool can be.
How many operations can you have on a single graphical page or how many branch points can you have in a single flow? Those kinds of things — I think it's really important to set some limits because there's going to be a point where you really need to stop and use a different tool, use something that's more sophisticated.
**Xu:** My last bit of advice is actually the better developer you are, maybe you're going to be more productive with the low-code platform — it's not the other way around. Because if you think of a low-code platform as a the developer experience tool or productivity tool, that, maybe, is another way to look at those sort of development tools.
**Neal:** It's less code you don't have to write! Fantastic! Thanks to both of our guests for this fascinating conversation, Scott and Xu Hao.
**Scott:** It's been great.
**Neal:** Thanks, Mike, and we will see you next time on the Thoughtworks Technology Podcast.
**[END OF AUDIO]**
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
## Find out what's happening at the frontiers of tech
[ Explore Technology Radar ](https://www.thoughtworks.com/en-th/radar)