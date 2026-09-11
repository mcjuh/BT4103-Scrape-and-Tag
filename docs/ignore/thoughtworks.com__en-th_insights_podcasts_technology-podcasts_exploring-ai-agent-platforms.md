<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-ai-agent-platforms | Title: Exploring AI agent platforms | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring AI agent platforms 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Ken Mugrage | Podcast guest  Ben O'Mahony and Fabian Nonnenmacher
January 22, 2026 | 37 min 59 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-ai-agent-platforms#Transcript)
Listen on these platforms
## Brief summary
If AI agents really are the future of how work will be done — in software engineering and beyond — the platforms on which they are built, run and maintained will be crucial. This is a topic two Thoughtworkers, Ben O'Mahony and Fabian Nonnenmacher, are currently writing about.
Although not due to be published until early 2027, the first two chapters of _Building AI Agent Platforms_ are now available as part of O'Reilly's 'Early Release' scheme. Its goal is to provide readers with a complete roadmap for developing AI agent platforms, from agent development to architectural principles to observability and governance. 
In this episode of the Technology Podcast, the authors speak to regular host Ken Mugrage about the book, why agent platforms are a critical part of any AI strategy and some of the challenges of developing and maintaining them. Listen for an early look at what looks set to be a valuable book in the world of AI development and to gain a clearer perspective on what agentic AI really means at the start of 2026.
**Learn more about[ _Building AI Agent Platforms_](https://www.oreilly.com/library/view/building-ai-agent/0642572243906/).**
**Ken Mugrage:** Hello, everybody, and welcome to another episode of the Thoughtworks Technology Podcast. My name is Ken Mugrage. I'm one of your regular hosts. I'm joined today by a couple of our Thoughtworkers that are also writing a book that's pretty interesting about AI agents. I'll allow them to introduce themselves, and then we'll get started. I guess, Ben, I'll start with you.
**Ben O'Mahony:** Hi. Nice to meet everyone. Ben O'Mahony. I'm a principal AI engineer with Thoughtworks. I've been here for two years or so, working in the global AI service lines, before that, working in traditional ML, and VP of Engineering for a number of different small startups. Lovely to get on the podcast, and maybe introduce my colleague, Fabian.
**Fabian Nonnenmacher:** Hi, everyone. I'm Fabian Nonnenmacher. I'm based in Hamburg, from Thoughtworks Germany. I'm now five years with Thoughtworks, and different to Ben, I'm coming more from the software engineering side, was a classical Java developer, and now, in the recent years, shifted more into the AI space. Happy to be here.
**Ken:** Great. Welcome, both. As won't come as a surprise to anybody, AI is everywhere. That's all we talked about in 2025, including, frankly, many things that weren't AI that we just pretended they were, different machine learning things or different if-then statements that we would pretend with AI, but really what we're trying to do, at least at Thoughtworks, and you'll see it in all of our stuff if you're watching socials and stuff this week and next and so forth, is AI that works.
What is the actual "How do I implement this?" Where are you going to get benefits out of it? What we want to talk about today is this idea of building an AI agent.
We're going to start with just some definitions, because we were actually chatting right before we started recording, and not surprisingly, these things are all defined differently. A lot of people think an agent is just a chatbot, and that's not the case. I guess what I'll do, I'll start with Ben, what is an agent?
**Ben:** The multi-million dollar question, right? [laughs] The reality is that almost nothing really is truly agentic in a lot of the things that are going on, even, say, for example, like a Claude Code, which a lot of people are very used to using, it is triggered by a human, so it has no agency of its own until it's given agency. I would say, no, it's not an agent. I think, again, when writing a book, we've got in and researched a lot of these things, a lot of different definitions.
Certainly, my opinion is that you can spend a lot of time arguing over a definition, and it's really not productive. I think we open with this Dijkstra quote, which we loved, which is basically this idea of the question of whether a machine can think is about as interesting as whether a submarine can swim, right? It's not that relevant for what you're trying to get done. Actually, again, that's the thing that cuts through to the AI that works, which is, what do you want to do with it?
Define that accurately, and then you know if you're moving on the way. If the goal is AI, just as the same if the goal is a microservice, it's completely useless, right? It doesn't do anything. What's the actual use case? What's the product? How do you want to build it? Those are the things that we care a bit more about. What's an agent? For us, I guess it's something that has this agency where it can actually have an impact on the real world, and to some degree, make semi-autonomous decisions, I suppose. Fabian, maybe you want to jump in. You're a bit harsher on the definitions, often. [Laughs]
**Fabian:** Like you're saying, I think at the end, it's about "What do you want to build?" AI opens a lot of opportunities. I think people often use the word "agent" for every application that somehow has AI built in. What I find a bit more helpful is to say that an agent has a certain degree of being autonomous, and what I like from the software perspective, that it has control over the control flow, actually. If you have an application, you have your for loops, if conditions, and so on. If you give the agent the power to a certain degree to make these decisions, then it's for me an agent.
**Ken:** That's very helpful. The full title of, actually, your book is Building AI Agent Platforms. "Platform" is another term that's incredibly overloaded. If folks are familiar with our Thoughtworks' Looking Glass report, a couple of years ago, there was a big thing on different kinds of platforms, whether it be developer or B2B or what have you. Again, for the purposes of our discussion and purposes of your book, what is a platform when it comes to AI agents?
**Fabian:** I think it's everything that helps teams to build applications, or in our context, then, AI applications, and now we can go a bit deeper that, actually, in our opinion, starts from good documentation that you give guidance to the teams, but of course, then what it often also consists is what probably most people think about a platform, a set of self-services to spawn up infrastructure and all these kind of things.
I think that is the key. It's always about improving the development speed of the teams using the platform, making sure their time to market is faster or in higher quality, all these things that are indirectly supporting them.
**Ben:** I completely agree. Just to add, we're not looking to redefine "platform," which has been defined to death, right? I think when we were looking through, because again, this was one of the things that we started at the beginning of the book, "What is a platform?" all that sort of stuff, we have to get our definitions right internally. I think the article on martinfowler.com from Evan Bottcher is one of the really good ones: a foundation of self-service APIs, tools, services, knowledge, and support, which are arranged as a compelling internal product.
That kind of "arranged as a product," that is the thing for me that then starts to have that continuous thinking. It's not just good enough to throw things out there. You have to start thinking of the user journeys through the platform and how they go about building AI agents, in our case, or anything else in any other platform. Again, it's the assembly of those things together.
I think an interesting example that we saw, and I draw on in the open source, was this new distribution of Linux by DHH, which isn't really a distribution of Linux at all, but actually just an assemblage of different tools on Arch Linux, so Omarchy. Really, it's just put together, looks quite nice. I'm certainly a Mac user at Thoughtworks, unfortunately, but that idea of just assembling these tools in a way is like your minimum viable platform, right?
Again, when you're greenfield, and you're using a hyperscaler, then often you are just, at the beginning at least, putting together a curated experience on top of a cloud, right? You're actually not necessarily at the beginning doing a huge amount extra of putting in domain and learning and that sort of thing. You're really just helping people get to grips with the hyperscaler infrastructure.
**Ken:** We've actually spent, gosh, the last decade a little bit more building platforms, enterprises, everyone's built their developer experience platform in their-- pick a name. Is this another whole new one? Can they leverage what they have? People are like, "I have another? I just built that platform. What the heck?"
**Fabian:** That is the key question, and with all this hype, there's often this sense of doing things from scratch, but actually, I think that's also our message that we want to bring across. A lot of things are similar. There are maybe a few new aspects to consider, but if you think about a chatbot application, is it so different to a microservice, or if you talk about a pipeline that uses an LLM to extract data or reformat data in what form of whatever, is it so different to a data pipeline?
I think it's way more important to identify first "What are the platform capabilities already available, what are the pieces missing, and what are maybe the few extensions really needed now in the context of AI?"
**Ken:** Can you give us an example of a couple of those extensions, what they might be?
**Fabian:** One example are evaluations, for me. When we develop software, we have tests, test have this advantage. They can either pass or fail like a clear binary indication if we are good or not, and when we work with LLMs, we have not only non-deterministic output, but often also open-ended output. It's not that easy to grasp it, what it actually is, and validating that an LLM behaves correctly is one of the key challenges when developing applications.
That means, what are, here, the capabilities a platform needs to support this? This includes having services that track these experiments that, maybe, can run variations of the experiment, and getting always these evaluation scores.
**Ben:** Again, especially in the chatbot space, which is very open-ended as opposed to the workflow, which tends to be much tighter or tightly bound, you actually want to also have these nice routes from your monitoring and observability, which, again, probably do need to be enhanced for generative AI because now you care a lot more about each individual trace because it's a conversation with context and different things going on, right?
You don't just want to look at a bunch of logs and see where the errors are or count up the errors over a certain period of time, and you might want to do that as well. You actually want to go in and inspect that to see what type of failure has happened in the running of the application. You then want an easy, quick way of taking that to your development environment and making sure that you don't fail in that same way again, so extracting that data really quickly and easily and then saying, "Okay, great, I've got that. Now I'm going to add that to my suite of evals, and I'm going forward."
Actually, what we see when you're building the AI application, building up that data set of interactions from the real world, is also another asset that needs to be managed and is separate to some degree from the functioning of the application. It should really be treated as a data product. It should be maintained. It should be pruned as well. Again, a lot of the time, you see this; we see this with test suites as well, the number of [laughs] test suites that maybe just need a bit of tender love and care.
Your evals data set is really important for that because it's the only way you can really see what's happening in the real world and replicate it locally, have those fast iteration cycles. Again, like Fabian says, it's still not as fast as that true test feedback that you can get, but it is really important in the development of AI applications.
**Fabian:** I want to quickly cycle back to the definition we gave earlier on an agent, that an agent is an application that controls its own control flow, and that is the key part where tracing becomes irrelevant because now it's invisible. You don't know what's going on, and tracing is the view in to see what's going on. Of course, it's then not only important in production, like we want to see, but also already during development and during these evaluations to really see what's going on.
Again, it's not completely new. I would say we had the same problem with distributed systems already. If you had a microservice architecture of 100 microservices, you knew it was still deterministic. Well, of course, running things in parallel, [laughs] that's a bit, but it was just too complex to understand, "What is the, actually, call hierarchy?" That's where we are used to tracing already. I would say now, in the context of AI, tracing also becomes more important on the level of an individual application that you see what's going on inside of this application.
**Ken:** I may be missing the quote. I think it was Charity Majors, or at least that's the first place I heard it, was that microservices turn outages into murder mysteries that you have to try to solve, but the same kind of thing.
**Ben:** Or the other one, the definition of a distributed system is that a computer you didn't even know exists can break your program. [Laughs]
**Ken:** Well, great accidental segue to my next question. If we're talking about autonomy, and don't worry, I'm not going to go to Skynet, but if we are talking about autonomy, and yes, we see examples. I was at Microsoft Build, and they showed shopping for a vacation. "Oh, I'm going to need a tent and a sleeping bag," and it went off, and it bought those things.
We have to trust that it bought the right thing. [Laughs] In a world where we're trying to give autonomy to software, whether we call it agentic or call it whatever you want, but autonomy in general, what's the security and guardrails look like? How do I keep that thing from going out and buying itself a bigger GPU?
**Ben:** Definitely more work is needed here for sure. There seems to be this odd sort of idea that-- and again, I opened with the submarine question. Is it thinking or not? Put that to the side. There is a piece here. Firstly, if something is doing some thinking for you, that doesn't mean that you should do zero thinking. [laughs] That's a really key thing, is just because you have something that thinks doesn't give you the ability to not think.
You have to think really carefully about these. When we've seen this work well is when it's intentionally done from the beginning, and you start with the evaluation of what you want to happen. Now there's another way of doing it, which is very open and can be very interesting and exciting, and certainly in a startup, probably the way to go, which is that you are using it in a much more exploratory way.
You don't necessarily know precisely where the value is, and you're using an AI agent interface with a customer to try and find value, and that then improves the application from there, which is a totally valid method, but it can be quite risky again, because as soon as you open something to the internet, that's where things go wrong. Certainly, I think one of the really good patterns that has been used is that sort of triangle.
If you've got access to internal data, the ability to execute code, and open access to the internet, then you've got that trifecta of bad things because that's just a data exfiltration event waiting to happen. It's surprisingly quick and easy to do that if you just naively put together an AI chatbot and expose it to the internet. What we're seeing with a lot of our customers is that they are mostly using AI for internal use cases. In that case, there is a much lower bar, quite rightly so, because you have, to some degree, you're already within a trusted organization, and you're already within some security environment, so there is a little bit more safety.
Yes, for sure, we think there, you should still go zero trust, and you should have this inheriting of permissions, and for the fully works case for coding, for me, I think there's still that point where I want someone to click Merge PR or push, so that there is, at that point, some commitment that they're standing behind the things that they are pushing towards. If you don't feel comfortable putting your name to that and you say, "Oh, it's a computer, I'm not making the decision," well then, you need more guardrails. [Laughs]
**Ken:** What's the role of the platform in there? Because I know one of your future chapters is on low-code, no-code, and we talk about guardrails as a great term, actually, whether we're talking about AI or not. What's the role of the platform? We're trying to enable people, we're trying to get business users, and that sort of thing to push things into production.
Is it the platform's job to make sure they're not getting into the portion of the document repository they're not supposed to be getting into? Is it the responsibility, really, of a finance person that's pushing a thing? What's the platform's role there?
**Ben:** Again, I think it's this idea of like, you want sharp tools. We use the kitchen analogy a lot because I love cooking, and if you give someone a blunt knife, they're not going to produce a very good meal. [laughs] They have to have the ability to do that. Now, you don't want to put them completely set free, but a finance person, for example, should have the authority in their day job to go and deliver, do things, right?
If they share a spreadsheet, for example, with someone who's doing some work on it, and that person breaks the spreadsheet, well, you gave the person the spreadsheet, and they might've broken it, but you gave them the spreadsheet. There's some of that sort of, "I didn't back it up. I didn't save a version, send a copy of this specifically," like that. It's kind of similar to that.
You need people; if you want people to do anything valuable, they need to be able to break things, and that's scary for a lot of enterprises, but that's the trade-off, and you need to make sure that you've got, then, your more generic guardrails, things like offensive content filters, stuff like that. These are relatively simple to introduce at the infrastructure layer, and you can just have that.
Again, you may want to some degree centralize access to AI through a gateway, a way you can monitor the traffic and understand what's going on and flowing through there. Now, the problem is, what we've seen with 99% of the AI gateways that have been produced is that they are this sort of grim wrapper that is not the superset, but the subset of all the capabilities, of all the different APIs that people want to use.
You're missing out on a huge amount of the benefits of working with a massively, frequently evolving number of different APIs from different providers that are adding tools and different paradigms and ways of working with it. If you harden your AI gateway to the point where you're just wrapping things, you've basically created a rod for your own back. I would try and find something that's a little bit more like monitoring, but not actually intercepting everything.
**Ken:** I guess, for Fabian, especially since you come more from the software side of it, which is where I come from quite a while ago, what is the role of templates and reference implementations and those sorts of things to help people know what to do right or what to do, not to do? What's that role here?
**Fabian:** I think the AI space is still relatively new for a lot of people, and so it's really just about also bridging this initial gap. The other thing that we are seeing, there are also so many ideas out, that you can do with AI. I think everybody who probably built, already, a small agent or small application knows a few lines of code, and you have a very impressive application, which was unthinkable for a lot of people a few years ago.
This is also the space of innovating, trying out new ideas. These templates should also help that you can basically create an agent, deploy it in minutes, and having it then, of course, secured. A good thing is if you have it inside the enterprise, something like this, that is the space where these very quick prototypes live typically, and that's that. The other thing is, again, it makes sense to have a bit of shared tools in an enterprise.
On the other hand, it's an extremely fast-paced space. There is, every week basically, a new library framework, and therefore we don't think it's a good idea to enforce any of these technology decisions, but with reference implementations and templates, you can give a bit of guidance, and then learn from each other if everybody uses the same things.
**Ben:** We actually had a very funny experience when we were working. Me and Fabian worked together on building one of these for our client, and another team turned up, not Thoughtworks team, different consulting company, turned up with a three-month assignment to build this RAG agent on Confluence data, which just happened to be the onboarding demo that we do and set up in about 12 minutes [laughs] for onboarding people to the platform to walk them through the different processes because it covers a lot of different things, including the auth and that sort of thing.
They turned up, a team of eight, ready to do the infrastructure, ready to do all this sort of stuff. We're like, "Here it is." [laughs] Obviously, proof of concept, so still some stuff to tweak, but for sure, that time to value was like, "Oh, this is great. This is what we need." That's agile. Now there's a hundred other things you can do, right? Now that that's been done, it doesn't mean that people aren't needed, it means we could just do more work more fast and more fun.
**Ken:** You just touched on something pretty important. I recorded an episode of this podcast a few months ago. We were talking about citizen developers and the difference between a proof of concept and a production application. We've all known, again, not AI-specific, somebody, "Oh, I did a weekend, and I got this thing working, so we can just put it in production," right?
What's that evolution like? I want to get them excited. I want to get them playing with it, but maybe they didn't know about the guardrails, or maybe they didn't know about access permissions, or inherited permissions, or whatever it happens to be. What's that evolution look like? How do we get people from "This is cool" to "I can trust this"?
**Ben:** This is the state that we find a lot of projects in, is that if you don't define what good looks like early and often and revisit it and continuously do that, then lots of pain is ahead and lots of iterations that don't show you any directional improvement. It feels like you're making progress in some ways, but otherwise, you're like, "I have no idea what dimensions I'm improving upon," and that's just because a large part of the execution is often via an API or a model that you don't own or control.
Trying to guide that into something that works is really challenging. For me, I think, again, I'm totally happy putting something in production very early and getting lots of very good feedback, and then maybe taking it out from production, certainly behind feature flags or something like that, just the basic users to get those early warning signals that you've done something wrong.
For me, it's very similar in some ways to the software process, where the best way of finding out if it breaks is to put it out there and test in prod, and actually see those things happen and then fix them. Your monitoring and observability has to be on point. You have to have at least ideas of areas where it might go wrong. If it's exposed to an end user, you probably want some red teaming, trying to break it, and really trying to actually stress-test this thing, because if a lot of the decision is happening outside of your control, you need to work out where that can go, and you need to fence off those areas deterministically, ideally, where you're not just doing prompt tuning; you're actually specifically checking for different things.
This can be as simple as assertions for specific words in the code that try and find whether someone's talking about X, Y, Z. A competitor, for example, can be really simple to then redirect and interrupt that flow so that the chatbot doesn't say something you don't want it to say. It can be down that purchasing routes, and start to look for signals that you might see in fraudulent transactions, for example.
Again, also, lots of this can be done deterministically and in the APIs that the agent's going to interact with as well. It's not just about the agent; it's about the whole system and hardening that.
**Ken:** It's funny. We at Thoughtworks use the term "sensible defaults," and we've got people can look at our website and others, and it's funny how often in the last year and a year and a half, we've been talking about AI, where it comes back to standard, sensible defaults, is using automated testing and using all the things. I always find that really interesting, how it's the same but different.
**Ben:** Well, the thing to me that's so surprising for the AI coding piece is how much easier it should be now to put these sensible defaults in, right? If you can code faster, well, then you've got more time to put in these, and what you find is that doesn't tend to be the case. People don't think about those things until it's too late. For me, it's like, "Right. Actually, what are those sensible defaults? Can we put them in early?" Yes, it might be painful to iterate, but actually, you've got them in there, saving you from some of these footguns that you're going to find later on. Sorry for interrupting, Ken.
**Ken:** No, no, not at all because actually switching gears just a little bit again and just taking advantage of the fact that both of you work on clients, and you do these every day, the pace of change has come up a couple of times, obviously. We've talked to clients that did a legal review on some AI tool, and that took 90 days, and then, okay, now you can use this IDE with this particular large language model, or whatever it happens to be, and that's the approved one.
You can't use anything else, because we don't want our IP leaking out, and that sort of thing. They see, they hear you talk, or they whatever, and they're like, "This stuff doesn't work," because they've got bad tools, frankly, and yet, at the same time, we have these enterprises that have thousands of developers. If I have 3,000 developers, and they lose an hour, that's 3,000 hours that that costed me, right?
What is your advice to organizations on "How do they keep up with the pace of change? Do they try?" and just the actual implementation, how do I make it so that before I give it to my 3,000 developers, that I have some level, and yet I'm not handcuffing them to where they can't take advantage of the thing that's going to come out next week, because it is?
**Ben:** A lot of these exploits and problems that have happened and made the news in the last month or so have not really come from AI; they've come from open source libraries being installed, which every developer is able to do, and can sometimes be very subtle. For me, this is really an organizational problem, right? Again, going back to the AI coding, the speed of coding has never really been the speed of the rate-determining step.
If you're looking, with systems thinking, at the entire organization, as you should be, because you can't really operate in isolation, then that's the part of the bottleneck that needs to be released, right? Again, you can go into these ideas of like, "Right, what are the sensible defaults? Are there areas that we can do it?" I definitely don't suggest keeping at the bleeding edge. I think you should bleed responsibly. [Laughs]
In an enterprise, there'll be different parts of your development portfolio that make sense to be bleeding edge, but there's going to be, also, stuff that you want, like, "I don't even necessarily want to go at it with enterprise legacy modernization stuff that we've been working on because the value's not there. It's working. Just, we can leave it for now." You've got to think about all these different things.
For me, I don't really mind that you're not at the bleeding edge for everything. You should be at the bleeding edge for stuff that gives you a competitive advantage. If it's just AI, then it's not a competitive advantage, right? Staying at the bleeding edge is not a competitive advantage. Leveraging that on your domain in a clever and interesting way ahead of your competitors, that is cutting-edge for me. That's how I'd think about talking to it to product companies and companies actually building this stuff.
**Fabian:** Because we also talked about the role of the platform here, I think the wrong idea is that you can use a platform to enforce all of that, to enforce that nobody is ever going to develop an application that breaks any compliance rules. I think the way of thinking should be different. What does the platform need to offer to make it easy to build secure, compliant, whatever applications? Because otherwise, it would be a footgun. It's like you would limit and restrict the platform so much that it basically has zero to a little to no value at all.
**Ben:** That's when someone says it's time to build a new platform. [laughter] Circling back to the other thing at the top, someone's like, "This platform doesn't work. Let's build a new one." You're like, "Right. Well, yes, I think there's another one." Another, I've done so much looking into quotes, so I'm full of them now, but it's just like, if someone doesn't build something that you didn't expect, it's not a platform, and I think that's it.
It's like you've got to have that freedom for people to innovate on your platform, and you can't innovate if you are that restrictive, and it takes 90 days to get approved for something. By that point, it might not be worth doing. It might be solved in a different way, deterministic by another team, right? Totally fine. Look, it doesn't have to be anything AI-related, but that's the ways that I think about it and talk to our clients about it.
**Ken:** Moving towards wrapping up, I guess I'm going to ask each of you to just give a couple of minutes. What have I not asked you? What do you want people to know that I should've asked you that I didn't? Either one of you that wants to start first can do so.
**Ben:** The question I suppose would be, what should you not do for a platform, for an AI agent platform? For me, actually, a lot of the time we see platforms doing too much. You talked about the pace of change. It takes a lot of-- especially with the pressure that has been coming on the organization to do something about AI, I think a lot of the times what we've seen is people trying to put in abstractions too early, people trying to build absolute castles when really actually it takes a lot more bravery to say, "No, this should be rough and ready."
This is a frontier platform. It's a place for exploration, and there's going to be parts of it that are going to be very well-known and understood. Actually, we should leverage already hardened services for that. If you've already got workflow engines, why build a new one and try and harden it yourself? Use that, utilize it, add in some specific guardrails, and that's it.
That's the thing. For me, it's like there's so much that you shouldn't do. The number one thing that I see that people should not do is prompt management, and that's, I think, a little bit controversial because people are saying this argument of prompts should be versions, they should be-- I'm like, "Yes, just put them in code. We already have a whole thing for version control. It's fine."
It's not difficult to put text in version control. We've been doing it for years. Co-locate it, I think. If you really want to do A/B testing, you could use feature flags and all sorts of A/B testing tools that may allow you to do this experimentation very quickly and easily. Dedicated prompt management, prompt sharing, I'm just like, "Why would you share the prompts? You could just share the application if it's good. If it's not good, then why would you share it?" [laughs] That's the one thing that I see as a signal of overemphasis on prompt sharing and prompt iterations in a way that's completely divorced from existing experimentation.
**Fabian:** I think I want to quickly share what I find exciting also about this AI in the AI space is that the roles that diverged in the last year, data scientists, data engineers, software developer, that in a way, they are coming closer together again. We see AI engineering, as a discipline, has elements of all of these disciplines, and that's the same for a platform.
It's not about reinventing the wheel; it's more about combining these capabilities that often already exist and really making these nice and easy-to-use integration than getting to this point and say, "Okay, we need a new platform, the AI platform that is going to be totally different." It's more about combining things that already exist. That is both true for the platform and for the practices that we use, like evaluation. What we talked about earlier is very similar to what data scientists are used when they validate their models.
**Ken:** Great. I want to thank you both for your time. For the listeners, the book is called Building AI Agent Platforms. There is the first two chapters are actually available on oreilly.com, if you want to check it out and get a sample. Do we have an expected date? I know that's hot. I hate to ask authors that, but when do you think it's going to be done?
**Ben:** We wanted 2026, but O'Reilly have put 2027, and they know a bit more than we do about writing books, [laughs] so maybe we stick to that, so hopefully Q1, 2027.
**Ken:** Great. In the meantime, you're releasing chapters on the O'Reilly platform if people want to check it out, right?
**Ben:** Yes, exactly. We thrive on feedback. We love feedback. Tell us how we're wrong in every single specific way. Again, this is that hardening-for-production process that we're going through right now. We want your feedback, and we want you to tell us we're dumb for any number of reasons. That will help us improve.
**Ken:** Great. Well, thank you again for your time, and we'll talk to you soon.
**Ben:** Thank you so much.
**Fabian:** Thank you.
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
## Explore a snapshot of today's tech landscape
[ Read Technology Radar ](https://www.thoughtworks.com/radar)
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