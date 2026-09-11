<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/micro-frontends | Title: What’s so cool about micro frontends? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  What’s so cool about micro frontends? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons | Podcast guest  Cam Jackson
July 11, 2019 | 25 min 14 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/micro-frontends#transcript)
Listen on these platforms
## Brief summary
Rebecca Parsons and Cam Jackson, a senior consultant at Thoughtworks Australia explore the trend of breaking up a web application into decoupled micro frontends, and how such an architecture can improve delivery quality and efficiency for the teams working on frontend code.
**Podcast Transcript**
Rebecca Parsons:
Hello. My name is Rebecca Parsons. I am here today for the Thoughtworks podcast and I'm speaking to Cam Jackson and we're going to discuss micro frontends. Welcome Cam.
Cam Jackson:
Thanks for having me.
Rebecca Parsons:
Tell us a little bit about yourself and how you got involved in frontend technology and micro frontends in particular.
Cam Jackson:
Sure. So I'm a developer here with Thoughtworks. I've been working as a consultant for about five years, a little over five years. I didn't join as a frontend developer, just as a developer consultant. My first project was actually very infrastructure focused, so no frontend work at all. And then I sort of just fell into doing frontend work over the years and that's where I've spent most of my time doing. And I certainly enjoy it. But you know, I really think of myself as a full stack dev. But yeah, probably what I've spent most of my time focusing on is the frontend world. And I guess the work that I'm most interested in and proudest of is helping large organizations to scale their frontends development processes and practices across many teams and across some really complex products.
Rebecca Parsons:
Great. So what is a micro frontend? I mean everybody's talking about microservices. Is it just microservice ish stuff applied to frontends? What does it really look like?
Cam Jackson:
There's certainly a lot of parallels to microservices. So I sometimes start by talking about that because that's what more people are familiar with. I can give you a sort of a dictionary definition, that I use, which is that micro frontends is an architectural style where independently deliverable frontend applications are composed into a greater whole. So there's a couple of things in there. There's the composition part of it, which is probably not that exciting. I mean most UIs are being built using composition as the main sort of pattern for putting things together. Probably the more interesting part is that independently deliverable bit. So we usually end up with something like each micro frontend is maybe a page in part of a greater product or maybe there might even be several micro frontends on the one page.
Cam Jackson:
But the important thing is that each one of those micro frontends should be end to end independently deliverable. So that usually looks like each micro friend has its own source code repository. It's got its own set of dependencies. It's own automated test suite and a delivery pipeline that takes it all the way to production and it's probably owned by a single team. So that's pretty powerful. What we usually end up seeing there is if we need to add a new feature to our product, a single team can pick up that feature and take it from analysis all the way through to production on their own. Nice and autonomous and independent from all the other teams and without having to do lots of coordination.
Rebecca Parsons:
And is there something in the overall architecture of the application that enables that level of separation? I mean, do you require a particular frontend to backend style architecture to really make this work?
Cam Jackson:
I think the main thing is making sure that if you're drawing boundaries within your application in terms of I guess where the seams are, they definitely need to be very business oriented and feature oriented. If you've built teams around kind of bounded contexts and domain concepts, it works really well. So you know if you've got a products page and your application having a products team that owns that page, that works really well and it works even better if they also own the backend part of the stack because it means again they can go end to end full stack features all the way to production without having to wait on other teams to do stuff for them.
Rebecca Parsons:
And it's amazing how often people think that it's so much more efficient to have those, you know, frontend technology team in this back end technology team and then you have to coordinate all those teams to get anything into production.
Cam Jackson:
Yeah, definitely. And I also try to steer people away from even just within the frontend space having I guess horizontal teams that focus on things like having a styling team or a forms team or a validation team. Like those shouldn't be teams. There should just be things that each one of your product teams has to do.
Rebecca Parsons:
Even if there's a certain level of consistency, you're trying to maintain a consistent style that doesn't mean you need a team to maintain a consistent style. So what are the problems that are actually addressed through micro frontends?
Cam Jackson:
I guess the one that we've already been talking about is team autonomy. So particularly in larger organizations that's where I see this pattern happening the most. There's a lot of coordination that ends up happening between teams. For one team to put a feature into production they've got to work with lots of other teams. They've got to coordinate their release processes, talk about who owns which piece of code. Micro frontends tries to avoid all of that by saying each feature should live just within a micro frontend and you don't have to coordinate with anybody else to put it into production. So that's probably the biggest one which comes up front. You then see a little bit deeper at the technical level. You can sort of detangle the various parts of your application or your product. When all of the code for a product is located altogether and you've got maybe a hundred developers all working on the one product, you always get this kind of accidental entanglement or coupling that happens across different parts of the application.
Cam Jackson:
No one really intended for this section over here to be related to this other section, they shouldn't really have any common code, but somehow they just always end up with some shared global state or some module that they both depend on. It now becomes really difficult to make changes to one without having to make changes to the other as well. So microphones kind of help us to draw I guess thicker boundaries around different parts of our product and say when I work on this part of it, I shouldn't need to look at this part over here.
Cam Jackson:
The other one that comes up, and actually a lot of people sort of accidentally fall into doing something like micro frontends is when you're trying to do incremental upgrades of your tech stack. So we see this all the time, it's probably a pretty familiar story to people, you've got your frontend which was built in an old technology and it's a huge monolith that might be all done in backbone JS, maybe it's an angular 1.0 thing, which has been around for a while, and it's old tech and nobody really wants to work on it and no one really understands it anymore because everyone's moved on since it was first built. So we want to do an upgrade, we want to do a migration from that to some newer technology, which is nicer to work with.
Cam Jackson:
Now obviously what we want to avoid is stopping all feature development so we can rewrite the entire thing, that very rarely works out. So we want to find ways to incrementally upgrade it. I guess the strangler pattern is a pattern that people often talk about on the back end side of things where we're able to just gradually extract out piece by piece and rewrite or replace small parts of the application until eventually there's nothing left of the old thing. I think people have been doing that for a long time on backend code, but it hasn't been done so much on frontend code. So you often see people saying, well I've got this big angular 1.0 thing, I'm going to take just one page because that's the page I need to work on right now and as I add new features to it, I'm going to rewrite it in react for example. If you do that several times very quickly, you've accidentally implemented micro frontends just by doing that. I see a lot of people getting into micro frontends just because they're trying to do an upgrade of their tech stack.
Rebecca Parsons:
So one of the critical design decisions when you talk about microservices is that domain or that boundary around the microservice. From a business domain, from a bounded context perspective, how you draw those boundaries is critical. Do you think that this accidental falling into a micro frontend architecture, how good are those boundary choices? I mean when you look at it dispassionately, are those sensible boundaries? I mean you, you could make the argument that since that's kind of the way it was designed before because they were pages, it's probably not so bad, but what's your sense about that?
Cam Jackson:
Yeah, I think you're right. I think it tends to work out really well. I think there's a lot to be said for designing our code in the way that our users would think of it. If we have the mental model from a technical point of view of how our application works, if it matches with how our users think the software should work or what the different sections of the application are, I think that usually goes pretty well. Definitely I think there's almost doing it in the frontend space is easier to draw those boundaries because you just look at the application in your web browser and say well that page there, that looks like a micro frontend, let's split that out and I think that applies to frontend code in general. I'm trying to figure out what should be a component and what things should compose together. You can often just look at the design and if you just draw boxes around the different parts of the page that serves you pretty well I think for figuring out how to divide up your code as well.
Rebecca Parsons:
Are micro frontends new or is this just something that we've figured out a name for?
Cam Jackson:
Yeah, I think it's not particularly new. When I first started trying to write about micro frontends, I sat down with Evan [inaudible] to get his inputs on it and one of the things he said is, "I feel like I was doing this 15 years ago and we were just doing everything was rented from templates on the server and we just did server-side includes. The page was composed together out of all these HTML static fragments on the service side and each one of those fragments was owned by a team. Is that micro frontends?" Initially I sort of thought, no, no, no, that can't be micro frontends. That's old school. But when I started to actually think about all the benefits and what the important attributes of micro frontends are, I couldn't really think of a reason why it's not micro frontends.
Cam Jackson:
So I gradually came round to, yeah, it doesn't matter what the technology is and yeah, it's not necessarily a new pattern. I do think it's helpful to give names to things, even if we've been doing them for a while. I would say that I think there's a renewed focus on these kinds of patterns because web applications are only getting more and more complex and they're getting bigger. I think as user experiences get more, it's more important to have a really solid user experience in your product. So we often see more code getting pushed to the frontend than we used to have. That means we've just got more frontend code to manage and so it becomes more difficult to manage the complexity in that because as things get bigger they get more complicated. So there is a renewed focus I think, in finding ways to divide up our products into these independent frontend pieces that can be worked on by teams independently of each other.
Rebecca Parsons:
So if we were doing this 15 years ago, or at least Evan was, where did we go wrong? Do you think there was some kind of dynamic that pushed us away from thinking about our user facing applications in that way? To these monoliths, which apparently we adore when we're not despising them.
Cam Jackson:
Yeah. I think part of that is traditionally frontend development. It sort of been seen as a bit of a lesser form of development by some people. That's certainly not what I've ever thought. Especially the first time I tried to do it, I realized, wow, this is really hard. And I suddenly had a lot more respect for the people who actually do it. So I think, yeah, maybe partly why we haven't been as good at this is we haven't given it the attention it deserves. And I think people who have are probably the people who've been doing this for a while and are going to say, so what I've always been dividing up my frontend code into these nicely segmented pieces, but maybe a lot of other people have not been treating frontend code as you know, real proper code that deserves attention and deserve some thought into its architecture so that's now something that I think more people are trying to do.
Rebecca Parsons:
The radar for the win once again. Several years ago we said treat JavaScript as a first class citizen. We need to think about engineering practices, design practices, all of those things in the same way, even if it's just frontend codes. So why did you choose to write about it now?
Cam Jackson:
Well, I chose to write about it a couple of years ago. I mean-
Rebecca Parsons:
I know how that goes.
Cam Jackson:
Anybody who's tried to write a long article or even a short article probably knows that it takes a lot longer than you think. It was a couple of years ago, mostly just because that's what I was spending most of my days doing and I was looking around me and seeing people who were doing something like this pattern were having a really good time with it and people who were not, some of them are doing really well, but a lot of them were really struggling. And so I saw almost everywhere I went, several clients in a row, there was a similar story. Oh we've got this big old frontend thing and it's really hard to work on and we're all stepping on each other's toes. We want to find ways to split it up. So it just seems to be a common theme that was popping up everywhere I went. And so I thought maybe this thing needs a name and maybe we need to sit down and as I guess as a profession, talk more about how we're doing this and how we can do it better.
Rebecca Parsons:
So one of the things about microservices, and I do see a lot of parallels really between microservices and what we're talking about here. Martin has the article, you have to be this tall to be able to do microservices. So there are clearly times when it's just not worth paying the cost. Do you feel the same way about micro frontend?
Cam Jackson:
Yeah, for sure. After writing my article though a lot of people were sort of saying this seems way too complicated, why would you do that? For sure there are times where the benefits that you get don't outweigh the extra complexity because there is a bit more complexity in doing things this way. If you are a one person company or even if you're a one team company, there's probably not much point in trying to do something like this. I mean as long as you are thinking about where the seams in your application are and I guess where the boundaries are between different things, it's pretty easy to start pulling things out later on. If your needs are small and simple, it's probably not worth it. I guess the other way of phrasing that is if you don't have the problems that micro frontends are supposed to solve, then there's probably not much point in it. If you're not trying to scale an organization to a hundred people working on the same product, if you're finding that you don't really have problems with lots of coupling in your monolith code base, and if you're not trying to move from one tech stack to another, there's probably not that much benefit in doing it.
Rebecca Parsons:
What is the source of the complexity? I mean it's pretty clear in the microservices world you've got all kinds of errors, for example, that just can't happen if you've got a monolith. Are there similar parallels or is the source of complexity different when you think about micro frontends?
Cam Jackson:
I think there's a couple of sources of complexity. Frontend code is a bit different in that even if we're trying to slice things up from a technical point of view, users still need to see a single application. Users shouldn't know the different pages in the app are deployed independently. It should feel like a single cohesive app or a single product. So that's probably where a lot of the complexity comes is saying, well we've got these five different teams working on one product, and they're meant to be independent from each other, how do we make sure that what they end up producing looks like a single product?
Cam Jackson:
So there are a bunch of things you can do with that. Having a well-documented design system or a shared library of reusable UI components, that goes a long way to making sure everyone's doing the same thing and just having people talk to each other. I mean, just because our teams are independent and they don't have to coordinate, it doesn't mean that they shouldn't collaborate. So you still want people talking to each other. You still want people saying, "Hey, I solved this problem already there's no need for you to solve it again", that's always something that we should be doing. And I think, I guess that's where the technical leadership becomes really important, to have people who are bringing those teams together to make sure they're all moving in the same direction.
Rebecca Parsons:
It also seems to me when I think about how microservices tend to be encapsulated and communicate with each other and then you think about it from the frontend perspective, particularly in the case where you have multiple micro frontends on a page. As a user, I expect all of those things to know about each other so that if I type something in one place, I type my zip code in over here, the little FedEx search box knows what my zip code is. Is that something that introduces additional complexity? How am I actually going to share this context across these multiple frontends when I still want them to be able to be deployed independently?
Cam Jackson:
Yeah, definitely. I mean integration is always the hardest thing, right?
Rebecca Parsons:
Absolutely. That's what makes it fun.
Cam Jackson:
Right. So figuring out ways for micro frontends to talk to each other or communicate or share knowledge is the hardest thing to do. Well without also making it so that we've got all that coupling that we were trying to eliminate in the first place. So I think the main thing is to be deliberate and explicit about what communication there is between micro frontends. And I think that's what we were doing wrong before is that we weren't deliberate or explicit about it. It was just everything knew about everything and that's why things were so tangled. So now that we've separated things, they still probably need to talk to each other a little bit. So if we put some thought into thinking about what is the contract here, what does this micro frontend expect of this other micro frontend, then then things are going to go a lot better.
Cam Jackson:
So you know, whether it's just using events or messages to publish something onto the page, to one micro frontend can say, "Hey, this piece of state changed and anybody else who's interested in that can listen for it and do what they need to do", that tends to work pretty well. What I usually tell people to avoid is direct state, which is shared directly across micro frontends. I mean shared, mutable state usually goes badly and I think the analogy for backend code would be having an integration database. So it's an anti-pattern that we talk about a lot is microservices that share a database because now they're completely coupled to the same domain model. You can't evolve your database or change out your models without having to change everyone all at once. So I think particularly when you look at a library like Redux for example, Redux on the frontend says there's a single global store, which is where we put shared state and everybody shares the same store, it works pretty well.
Cam Jackson:
But if you've got multiple micro frontends, I would say if you do want to use Redux, each micro frontend should have its own store. Don't share a single store across everyone because that's a great way to have a bunch of global state, which you can now never change the design of that state. You can never rename a field basically because renaming a field would require everyone to go and rename the field in their own code bases. The other thing which is I guess the complexity which is unique to the frontend side is styling and CSS collisions. And again this is not a new problem like we've been struggling with, you know two different people tried to use the same name for their CSS selector and they conflict or having specificity battles over making sure that my selector over overrides your selector.
Cam Jackson:
We've been, we've been having that problem with CSS forever, but it becomes worse when you've got multiple teams who are meant to be separate from each other. If they're all writing CSS which sits in the same scope, that's going to be a complete mess. So without getting into too many details, there are a whole bunch of different ways that you can solve that. It doesn't really matter which one you pick as long as your guiding needs to be when I'm writing some styling code and you're writing some styling code, we both need to be confident that we know what it's going to look like in the end. That mine is not going to override yours and yours isn't going to override mine.
Rebecca Parsons:
And we can continue to cheerfully ignore each other.
Cam Jackson:
Yes (laughter).
Rebecca Parsons:
Do what we need to do. Absolutely. Because that's of course one of the benefits we're trying to achieve here is to allow those teams to work in the play independently.
Cam Jackson:
Yep.
Rebecca Parsons:
So how do people go wrong when they're trying to work with micro frontends?
Cam Jackson:
I think what people struggle with sometimes is balancing this kind of a spectrum of centrally controlling and standardizing everything versus complete chaos where nobody talks to each other at all. I think both extremes of those spectrums are pretty wrong, but it's hard to find how to find the balance in the middle and different organizations will have different cultures around that sort of thing. You know, definitely if you're a startup which has grown into a big organization, there's probably more of a culture of move fast and just do whatever you want and that works well to a point, but one day you realize that, Oh my God, everyone's doing completely different things here. It's affecting the consistency of our UI. It's affecting our download sizes because we've got five different frameworks on the same page, so that's not good.
Cam Jackson:
At the other end what you sometimes see in I guess more corporate places is the desire to over standardize and over centralize. And so everybody has to do everything exactly the same way. We all have to use exactly the same versions of every single dependency. All of our build pipelines have to look the same and all of a sudden, well, you may as well have just built a monolith. If you're forcing everyone to endlessly coordinate and do things the same way and every single decision has to go to a committee, it would probably be faster to just do it in a monolith and stop pretending that you're doing micro frontends, I guess. So that's a balance which is really difficult to strike and that's probably where I spend a lot of my consulting time is trying to help people find the right balance. It would be different for each organization.
Rebecca Parsons:
Do you think it varies much by the style of application where that balance point is or is it more really organizational and cultural?
Cam Jackson:
Yeah, I think it can as well. I mean if you're building something for the general public, it's probably more important that things are really fast. So you want to put more effort into deduplicating dependencies and maybe sharing dependencies so you can reduce the number of bots. And the consistency of the user experience is absolutely paramount. If you are building, and I've seen this a few times, if you're building an internal product, which is basically just a portal into a bunch of, maybe slightly related but relatively independent little applications, it probably matters a little bit less that everything is totally consistent. And so in situation I would probably optimize more for speed of delivery and letting people do their own thing a little bit more. Because it doesn't really matter if things look slightly different in the various different internal web applications.
Rebecca Parsons:
So is there anything else you wanted to say that I didn't ask you about?
Cam Jackson:
I don't think so. I think the main thing is I really just want people to be thinking about this stuff. Like I said earlier, for a long time frontend development hasn't been seen as real development. Whether people go and do micro frontends or whether they do something completely different. It doesn't really bother me. Obviously I like working on micro frontends. That's why I'm writing about it and talking about it. But if they want to choose a completely different pattern that's awesome and I love that as long as people are actually putting the effort in, putting the thought in and treating frontend development as real development and trying to do things properly.
Rebecca Parsons:
Thank you very much. This has been the Thoughtworks podcast and we'll see you next time.
Neal Ford:
Hi, this is Neal, one of your regular hosts. On our next episode of the podcast, we're going to talk about something that you can't even Google. This concept that comes from our colleagues in China, called Zhong Tai, you'll get the correct pronunciation in Chinese in the episode. It's an interesting way of thinking about encapsulating platforms as business models. So please join us for the next episode.
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