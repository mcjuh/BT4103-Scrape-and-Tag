<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/models-open-source | Title: Models of open sourcing software | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Models of open sourcing software 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Rebecca Parsons | Podcast guest  Brandon Byars, Aravind SV and Zabil Cheriya Maliackal
October 01, 2020 | 30 min 59 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/models-open-source#transcript)
Listen on these platforms
## Brief summary
Open source has become an important model for building interest and trust in a software project. But there’s no one-size-fits-all approach to open source. In this episode our podcasters explore different ways to approach open source and examine whether end-of-life has to mean obsolescence.
**Podcast transcript**
﻿Alexey Boas:
Hello, and welcome to the Thoughtworks Technology Podcast. My name is Alexey. I'm the head of technology for Thoughtworks Brazil, and I will be one of your hosts this time together with Rebecca Parsons. Hello, Rebecca.
Rebecca Parsons:
Hello Alexey. Hello everybody. I am Rebecca Parsons. I am the Chief Technology Officer for Thoughtworks and one of your co-hosts. And today we are joined by three guests, and we're going to be talking about various aspects and approaches to open source. So first, I'd like you all to introduce yourself. Brandon, why don't you start?
Brandon Byars:
Hi, Brandon Byars, been at Thoughtworks about 12 years now. Currently playing a couple of roles, the market tech director for the central market in North America, and while our head of tech for North America is on sabbatical, I'm filling in for her role as well.
Rebecca Parsons:
Duck, you want to go next?
Aravind SV:
Sure. Hi, I'm Aravind or Duck. I'm a consultant at Thoughtworks with a development background, working with C#, Java, Ruby projects in the insurance, healthcare and retail domains over the years. Over the last few years, I've been a product manager for GoCD, an open source continuous delivery server started at Thoughtworks.
Rebecca Parsons:
And Zabil.
Zabil Cheriya Maliackal:
Yeah. Hi, I'm Zabil. I've been with Thoughtworks for roughly 12 years. During that time, I've been a developer working on a lot of projects, but most of my time actually has been spent working on a lot of open source projects, like the openMRS, Rapid FTR, GoCD, And now I'm the product manager for Gauge and Tyco.
Alexey Boas:
Okay. And then perhaps all three of you could talk a little bit about the projects you're going to talk about and mention them the projects you have experiments with. So Duck, why don't you start talking or telling us a little bit about GoCD?
Aravind SV:
Sure. GoCD, As I mentioned, is an open source, continuous delivery server started at Thoughtworks way back. I think it started its life being called Cruise in the 2007, 2008 timeframe. Before that we were responsible for multiple tools in the continuous integration space, but it felt like there was something missing in the next step of that journey.
So GoCD or Cruise started off by being the initial implementation of the idea of delivery pipelines and what would later be called continuous delivery. In fact, Jez Humble, one of the core authors of the continuous delivery book was the first product manager of of GoCD. And at that time it was a closed source commercial product, but around 2013 or so, we were quite frustrated that continuous delivery wasn't as widespread as it could be. So we open source GoCD around early 2014 and came up with a few optional commercial components.
It gained a lot of interest at that time, and as the technology landscape changed, it improved to work closely with containers, containers schedulers, image registries, infrastructure as code, pipelines as code, et cetera. And at the end of 2019, we decided to open source the previously commercial components as well. And currently it is completely open source and we're working with the community and a small steering committee to help decide its future direction and find a neutral home where it can continue to thrive.
Alexey Boas:
Thanks so much sounds exciting. You get to hear more about the history and experiences with GoCD. Zabil, can you tell us a little bit about Gauge and Tyco?
Zabil Cheriya Maliackal:
We started Gauge and Tyco around about 2014, and by starting it had the solid foundation of our reputation and testing. If you've been following talk books we know that there's a lot of popular testing frameworks that came out of Thoughtworks, like Selenium, WebDriver, even in a widely used tools like Mockito. So Gauge and Tyco came out of of these experiences, out of our testing experiences. And it does a test automation framework where Gauge is a test runner, is a framework for writing your specifications that mock down and then running them. Tyco is a browser driver, you can use it to automate browsers and we've been working on it for the past six years.
Alexey Boas:
Okay. Thank you so much Zabil. And how about Mountebank, Brandon?
Brandon Byars:
Sure. So it started about the same timeline as what Zabil was talking about. I think I wrote it over the Christmas holiday in 2013 and released it the following January. And it is, there's a joke that my ex-colleague Pete Hodgson used to say that every Thoughtworks dev has to cut their teeth building their own mocking framework, and so at the time that's kind of how I viewed it. I've subsequently learned that there was a name for the class of tool that Mountebank is, it's called service virtualization, which is taking the stubbing idea and extending across process boundaries so that you can stub out HTTP calls, it's quite common. Actually the very first use case of Mountebank was a binary Java serialization format that was crossed boundaries using an ESP at the time. And so it allowed us to stub out some downstream dependencies in a way that allowed us to test all kinds of interesting scenarios that were otherwise difficult to test.
Alexey Boas:
Cool. And I guess it's going to be interesting to talk about the different perspectives and different evolutions of these open source projects. So we have two that were heavily company sponsored, and one that is more personally driven. And Brendan, while we were discussing this previously, I remember you talking about three prongs for open source projects, product, architecture, and communities, the third one. How does that go? Did I remember that correctly?
Brandon Byars:
Yeah, that's right. And that's one of the learnings I've had approaching seven years now of maintaining this product. Like a lot of developers, once upon a time I was quite passionate about trying something out in code and then Git Hub was a useful platform to host the code and I would call that open source, but when I released Mountebank and then people started using it, I realized there's obviously a lot more to maintaining an open source product than just getting code into a public repository.
And so those three lenses are kind of how I think about it nowadays. There's a, I think, a very significant product lens. In fact, that's been probably my biggest learning, maintaining open sources is how to think about support, how to think about your releases and documentation adoption, how to do the appropriate handholding, how to think about features that fit inside the product and those that should not fit inside the product.
Architecture and community kind of go hand and glove. The developer community obviously contributes to open source. That's one of the benefits you can crowdsource some feature in bug development, but it has to fit both within the product lens in terms of, is this the right feature for the product, and the architectural lens in terms of, does this fit the evolveability of the product over time? Is this a natural extension point? Do I need to refactor something that I had in the past so that it could be a natural extension point in the future? And balancing those three prongs, and Mountebank is one maintainer, it's just me, so I tend to be leads across all three of those, but in theory, I can as product scale, you could think about different roles for those different activities.
Alexey Boas:
Yeah. That's interesting. We see some open source projects that evolve as a product more organically, adding features and things like that. And Duck, you talked a little bit about GoCD. That seems to have a very strong product driver based on an opinion that grew in the community and Thoughtworks itself, about how to do continuous delivery and et cetera. And then it builds on that. Is that right?
Aravind SV:
Yeah. That's right. It definitely started out with a strong vision. Even though it was company sponsored, I guess that happened a little later, it started off as an idea from what we had learned from working on projects across Thoughtworks, across the world within Thoughtworks. But it definitely had that core vision about continuous delivery, about delivery pipelines, and so on.
But as Brandon was saying, it's hard to stay with it when people in the community want to do things with it that you don't necessarily want to be a part of the code base of your product. It's really hard. It was really hard, at least for me, to say no at the beginning. I felt that often that leaves a bad impression with potential contributors, turning them away, that goes to the other prong that Brandon mentioned around community. But if you allow everything, then people contribute changes that don't reflect the vision of the project and then go away leaving whoever is left to maintain that going forward I felt.
A middle ground I've seen as a well thought out extension mechanism, which can go somewhere and giving freedom to people while keeping the code of the project simple and clean. And I think we ended up doing that with GoCD. Once we learned that lesson, the hard way I suppose. One thing about division is, for example, GoCD and Thoughtworks in general actually have been very vocal about the benefits of trans based development for instance, over long lived feature branches.
And this was a sticking point that we refuse to consider branch based work flows for a long time, telling people that they shouldn't be doing it, but eventually the direction of software development, I feel, moved towards branches, especially in the form of pull request, which are just branches hidden behind a different name, and that affected GoCD. It didn't make sense to hold onto that vision after a while. And that vision had to evolve to encompass the branches as well. We still tried to keep it out as a core code base, into that extension mechanism that I mentioned, but that meant we couldn't integrate very well with branches, maybe as well as some other tools in the space could. So it's a balancing act. It's definitely a challenge.
Alexey Boas:
Thanks. And how about Gauge and Tyco, Zabil? My understanding is that it's also founded on strong opinions on how testing should be done, and does it drive its vision from that?
Zabil Cheriya Maliackal:
Yeah, it does. If you look at the fetus of a product and our testing approach also, many of the times, one point of contention was flaky test. And so people just wanted a feature to keep rerunning test until they past. And while we always wanted to focus on features where tests are independent, they are not flaky, when they are flaky there is a problem that you need to solve. So you can say most of the features has been opinionated. And if you look at my role, and probably Duck's role, via product managers and before these open source projects, so we had a large part in our roles to spend a lot of time defining the vision, reaching out to users, and also bridging between our opinions as a company, on how practices should be going into these products. So yes, it is a bit different from other open source projects.
Alexey Boas:
And Duck, you did mention saying no. So one question I'd like to ask you all three is, once you open source a project, and you open it up to the community, does that increased productivity, all of a sudden you start moving much faster? Or does it become more difficult because things get pulled in different directions?
Brandon Byars:
It is more difficult, is the simple answer. But sometimes that friction in Mountebank's case has driven the product forward and directions that I wouldn't have naturally taken it there because I just didn't have the perspective that needed. It's more difficult because of probably two primary reasons, that sort of conflict with those other two pillars outside of the community. One, people have ideas of things that solve their point problem that they're facing, but that don't fit the general product direction of Mountebank. So Mountebank, the core of it, is meant to be protocol agnostic, and somebody has a specific problem for example, and web, and they want to change the core in a way that doesn't even think about the other protocols because they don't use them. And that doesn't fit the product vision that I have to have to work with on this. Duck was saying you have to sometimes learn how to say no artfully.
The second reason it's complicated is because there's just obviously a wide variability to the quality of community submissions from the pull requests. Some people who submit pull requests are full time developers, most of them haven't spent the time to understand the design of the code because why would they, they're just trying to contribute to open source would be good citizens. And so a lot of times you have to spend quite a bit more time with the back and forth to help them understand the constraints, and then to think about the documentation and the appropriate tests, then you would have had you the feature yourself.
But the good part of that is you get, in Mountebank's case for sure, I have seen it extend in directions that I never would have thought of and that I'm quite happy to have taken the product in those directions in terms of scale, in terms of supportability concerns. And so I've gotten a lot more visibility to how the community uses it and what that definitely informs product direction through opening up the community, but it does mean there's quite a bit of maintenance on the human side.
Aravind SV:
Thinking back, I had the opportunity to see GoCD from when it was commercial to when it went open source, and I would say the open source part of it has definitely been much more work. Maybe it is about growing that community, right? That is an aspect that you don't have to worry too much about if you're closed source. Apart from all the things that Brandon already mentioned.
But one thing that I would like to add to what Brendan was saying around contributions is that, I think I mentioned this earlier, sometimes there are contributors who come and stay with you for a long time, and they're the ones who tend to overtime understand the architecture and what you're trying to do, and we were lucky enough to have some of those. And they're the ones who ended up contributing major chunks to the code base.
And there are others who are very thoughtful about it, but they're more of a drive by, like add a feature and go away, kind of people. So there are different kinds of people who try to contribute and managing that becomes a challenge in itself. There was a point where, as Brandon was saying, it might be easier to write it ourselves. So there was a point where I would say yes, and then rewrite whatever they had written. And that was not sustainable, not the right thing to do, and wasn't really teaching people about what we were looking to do around the vision of the product. So that stopped pretty quickly.
Zabil Cheriya Maliackal:
I'd like to add something on this from the Gauge and Tyco's perspective because when we started Gauge, we moved from a product that was closed sourced to a completely new product, which was written from scratch. And one thing we did from day one is build Gauge in a way that it's as extensible as possible, so it has a plugin architecture it uses. It deliberately built it in a core and a plugin model.
So what we've seen over time is a lot of people use the plugin model without having to touch the code so much, and they are able to extend it in a way and use it in their own alignment without interacting or asking us to add many of the features into the code. This already used a lot of note in managing the community.
Brandon Byars:
Yeah. And if I can just tag on to that. So I did not originally create Mountebank in sort of that micro kernel plugin architecture, quite intentionally. I tried to keep it monolithic because I thought that would simplify adoption. There were fewer knobs to spin when you start to use it. And over time, and it's funny listening to both Zabil and Duck talk, over time I've had to make it a microkernel architecture so that you could, and people have, create their own LDAP extension, their own GRPC extension, because that was the only way that I could be really thoughtful about the contributions I manage, and the contributions that don't need to come through me, but the still evolve the overall ecosystem. So I think there's an interesting pattern that you're seeing across all three of these products towards that architecture.
Alexey Boas:
Yeah. That's very interesting indeed. And I imagine it would allow... It would go back to the other two prongs. It would be much easier to manage community, and at the same time it could allow for, experimentation of features and things like that, that are not integrated into the core, but are just extensions that people might choose to use or not to use them.
And how about the evolution of these products, their life cycle? So we have a couple of different examples here. So Duck, you did mention the history of GoCD moving from company sponsored to community sponsored. I guess the same thing is happening to Gauge and Tyco. We also see products that start being built by one person and then get adopted by a company and things like that. So other some patterns of life cycles and some lessons learned from that?
Brandon Byars:
Yeah. I think those are some of the patterns. So, GoCD and Gauge, obviously they have some corporate sponsorship. With Thoughtworks you see open source products like Kubernetes that have sponsorship with Google, React. And that's a common pattern and that's a good one because when you use those tools, you know the company behind them, and there's still a community outside that company, but you have at least some sense of longterm commitment to the product.
The challenge with a lot of products that start individually is there's a less certain path to long-term ownership because it's very easy for me, for example, maintainer of an open sourced product to say, "Well, I've heard of the life priorities at the moment. So what are my exit ramps for that?" A lot of successful ones start off open source and then become corporate managed over time, and either through a foundation, or through a commercialization of the product. So you see that with some of the SmartBear products like SoapUI and Cucumber. And I think that's a very successful path. I think all long running open source products that are individually managed need to think about what is sustainability beyond my time mean? Either I can set up a bit of a federated governance model and there's enough community contribution that works, or I need to think about how do I get it into a foundation? I need to think about how do I commercialize this in some respects?
And that's really interesting because when I started open source a long time ago, I never would have thought of the path from open source to commercialization as success because it's a bit more of the militant Richard Stallman view of the world. But now when you think about ownership, that's really the only thing that you can't rely on a single person, multiplied by a factor of 10 or a hundred or a thousand, with the number of open source products who use enterprise as a solid foundation or even as architecture. So I think if you need to think about the different pathways and life cycles of open source products.
Rebecca Parsons:
Well and thinking about to that life cycle, when you consider the rate of technological change, some of these products can become obsolete. And I think this is a discussion that I've had an internally where it's like, "We can't stop supporting that, but that isn't the way we would do it anymore." It no longer makes sense and so I do think one of the decision points in the life ycle of an open source product is what does end of life look like? And product vendors go through very considered processes around how do I bring end of life to a product? And if we're going to advocate thinking about the product aspect of an open source project that end of life is something that does need to be considered. When is this no longer relevant?
Aravind SV:
Yeah. And I think that's, end of life, is not necessarily as bad as we make it out to be. We seem to think of it as... And it happens all the time. Maybe we need to think about an architect for that when we use things, but we tend to see it as a major event. Of course there are Google like believers known for end of lifeing products left and right, all the time that people are used to, so that's something that they have a challenge with.
But I see, for example, Dex, if you know, D-E-X. They have a... I mean, cannot have made it an end of life where this was set in stone. And that is the implementation which you can refer to forever. That is a different kind of end of life that he envisioned for that.
I see people seeing activity as an indicator for stability and life of a project, but in the case of Dex and other things like that, it's not necessarily true. I've seen this more in the list speaker system where something is stable and it was doing one thing well, and they've just left it, and it doesn't mean it's dead. It's just doing what it did well. Maybe it'll become obsolete like Rebecca said, but that doesn't mean inactivity doesn't need to mean end of life.
Zabil Cheriya Maliackal:
Plus I like to add on what is mentioned over here in the example of Dex and the products that we are doing also. Most of the products that we started is to validate an idea and show that it's possible. For example, GoCD, it was around continuous delivery and the ideas that just we're talking about, the ideas we had implemented over here.
When we started Gauge and Tyco. And Tyco also, it was about smart selectors being able to select without using X spot and all of that. And these ideas are the more important point of the project. They get adopted by other projects and they make their rate or influence other projects or the industry in the practices. And possibly that is the measure of success that we are looking at in this projects.
Alexey Boas:
Yeah. I think that's a very interesting perspective in my view, it goes back to Brandon's community prong because when you build a solution to a problem and you have a community around that, a community not just of users, but of people implementing that solution and learning, you're influencing and changing the industry in a different way with the project.
So open source projects can make an impact that's different than closed products because of that. So if people are learning about a solution and then the industry moves or the problem moves in a different direction, technology moves in a different direction, but people have learned about that and can build on top of that. So that creates an impact and shares a solution that can be learned and evolved. And that doesn't mean end of life. It just means that it has evolved into something completely different, but these invisible effects, any visible impacts, I think they're much more pervasive when talking about open source.
Brandon Byars:
Yeah. I think it's easy to point to a number of examples where that's true. So you look at Spring, who has been very successful in the Java world, but if you remember when Spring came out, that there was a bit of an explosion of these inversion of control open source projects that were roughly came out a little bit before, roughly the same time as Spring. Most of them didn't survive, but that was a big paradigm shift for the industry thinking in terms of these modular components and pro Joe's, instead of these big J2EE components that added some friction to the development process.
Duck's talking about GoCD, but Thoughtworks first continuous integration tool was called Cruise Control, which is where the Cruise name came from. Nobody uses Cruise Control anymore but it changed the industry in terms of how we think about automated tooling for continuous integration and bled into what became continuous delivery. A lot of the testing tools, Selenium I was mentioned earlier, when some of the earliest Thought workers were thinking about this tool for testing browser applications, the name really, as I understand it, this predated my time of Thoughtworks, but the name really this idea of Selenium is your antidote to Mercury, which was one of the big commercial testing products that operate under a different paradigm. And there wasn't a developer friendly. It wasn't as easy to integrate into integration pipeline.
And the fact that none of the, Selenium is still around, but the fact that Cruise Control and some of those early inversion of control containers aren't around is okay because they changed the way that we think about software and the paradigms have been adopted by other tooling, both open source and commercial. We built an open source tool in the mobile space called Calatrava, which allowed some portability between mobile platforms in a way that was pretty unique at the time. And while that product isn't around anymore, some of the ideas that have been adopted and this getting Xamarin is a commercial tool, that adopted similar ideas in that space.
That's one of the great things about open sources, it gives you a lightweight way of throwing ideas out into the ecosystem. And even if your tool adoption isn't what moves the needle on that, that the idea is behind it oftentimes do.
Rebecca Parsons:
It is unfortunately though, very difficult to measure impact. You've got this nice number adoption, or if it's a commercial product, dollars in revenue, but trying to measure impact and quantify impact is difficult. But it is something that we have intentionally fostered this notion that what's important to us, when we're looking at these ideas, is the impact that it does have on the industry.
Brandon Byars:
Yeah. And even adoptions not easy to measure and open source oftentimes as well. I don't know that any of them, unless you commercialize it, it's not necessarily true that any of those numbers are easy to measure, but impact is certainly the hardest.
Rebecca Parsons:
Yes. Adoption does not equal downloads.
Alexey Boas:
Okay. And I guess this takes us to the end of the episode then. It was a great conversation and awesome to have you all with us. Thank you very much for joining.
And if you have any feedback for us, don't hesitate to reach out or to leave a rating or comments on your preferred platform. Thank you so much for listening. Bye everyone.
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