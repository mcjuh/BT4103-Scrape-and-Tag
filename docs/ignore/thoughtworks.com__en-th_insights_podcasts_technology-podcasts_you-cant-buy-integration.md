<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/you-cant-buy-integration | Title: You can't buy integration | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  You can't buy integration 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons and Neal Ford | Podcast guest  Brandon Byers
November 04, 2021 | 40m 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/you-cant-buy-integration#transcript)
Listen on these platforms
## Brief summary
There’s often debate around the build-versus-buy decision for digital capabilities. But when it comes to integrating disparate systems, the convenience of some modern integration tools can result in point-in-time integrations: ones that are never intended to evolve, with all the complexity and cost that entails. Here, we catch up with Brandon Byers to explore the limits of low-code tools and the perils of thinking you can buy integration.
#### Podcast transcript
**Neal Ford** : Hello and welcome to the Thoughtworks Technology Podcast. I'm one of your regular hosts, Neal Ford. I'm joined today with one of the common co-hosts that I do podcasts with, Rebecca Parsons.
**Rebecca Parsons** : Hello, everybody. This is Rebecca Parsons and happy to be here talking with our guest, Brandon Byars. I'll turn it, Neal, back over to you to introduce our guest.
**Neal** : All right. We are joined today by a member of the Doppler Group that helps put together the Technology Radar. He's also Head of Technology of North America. You may know him as the creator and open-source of Mountebank and a similar book, but today we're talking about something completely different than the things that he may be known for, for something that Brandon encounters a lot in his life in the consulting world. Today, we want to talk about integration and common integration approaches to wire systems together. Let's hear your premise, Brandon, about how you can or cannot buy integration.
**Brandon Byars** : Thanks, Neal and Rebecca, for having me. What has been my experience in the recent past is I am involved in a lot of engagements in client conversations, in particular, where there's an industry that's lagging a little bit in the digital adoption, so it might be energy or insurance, and they are trying to catch up, but they're, like everybody, trying to leapfrog competition.
What happens, of course, is everybody looks for the shortcut. Why wouldn't you? The common shortcut that I find myself arguing against oftentimes is this idea that you can buy integration. I have to put that in context because I think a build-versus-buy decision point is a very healthy decision point for a lot of digital capabilities. I have no expectation that organizations should build all of their suite of digital products.
In fact, I think increasingly you can buy a lot of them around revenue management, around fraud detection, in addition to the traditional ERP style applications. The idea that you can buy integration is quite appealing. You have these integration products out there that market effectively, "We can make your integration much easier." My premise is that those tools get significantly overused.
They are effectively domain-specific programming languages that are commercial. You still have to build your integration inside those tools. We can talk through a few examples. Oftentimes, doing so devalues integration itself and converts, intentionally or not, the idea of integration from what I believe should be a strategic concern for your business, which is where agility comes from, to a tactical concern of how to wire two systems together.
While I think there is certainly a place for a number of these tools, my premise is that I believe that they are significantly overused and over-marketed. I've had to consult with a number of our clients to try to draw appropriate integration boundaries inside their ecosystem.
**Neal** : Why is integration so common? Give us a broad definition of what you mean by integration and the problems faced here.
**Brandon** : By integration, what I mean is exposing the digital capabilities of your enterprise. A lot of folks view integration as simply a data exercise, and obviously, getting access to data is a component of that. If you are, for example, a utility provider and somebody needs to register a move address event, there's a lot more than data that you need to satisfy that capability.
You need to be able to transact operations against a system that may interact with other parts of the business in terms of notifications and so forth. There's a workflow that's involved with that. Doing so outside the core system of record is done through integration. I might have a customer-facing portal, I might have a B2B partnership, I might have just a digital product that is facing the business but that simplifies access to some of the systems of record so that I can remove the need for expertise of the underlying system.
Obviously, exposing those capabilities, exposing the data through clean APIs, through clean events, that's primarily what I mean by integration.
**Rebecca** : Many of these systems, one of their selling points is, "Well, we have this adapter that will let you connect to Oracle financials, SAP, Salesforce, all of these different systems." Where do you draw that line between what you really don't want to buy and what you really don't want to build?
**Brandon** : It's a great question because there is real complexity with interfacing in some of these systems that predate the current digital era. If you are trying to integrate into SAP, there are specific protocols in SAP. They have IDocs, they have this remote functional interface. They, over the years, have built up some capabilities that expose SAP data and what we would consider more common integration patterns nowadays like a REST API over their NetWeaver Gateway.
Regardless of the technique, having something that facilitates that glue logic to connect to SAP can still be useful, having something that connects the glue logic from the Salesforce can still be useful. The problem is when we think that is what integration is all about is that system connection. When you get the data out of SAP at the end of the day, you still have field names that are based on the table names in SAP, which are based on abbreviations in German, and they're very unintelligible.
By the way, the business interprets them differently, so that, for example, this is a real example, the equivalent field names of Name1, Name2, and Name3, in a B2B context, the doing-business-as-a-legal-entity name was Name1+ Name2 in Thailand but Name1+Name2+Name3 in Belgium because of geographical differences and then just because they had a standard team right across the world doesn't mean they have a standard interpretation of that schema from the business units across the world.
The intelligence to get the actual meaning out of the data, the transformation is also a part of integration. A lot of those integration tools take the ETL mentality, this three-layer mentality. MuleSoft has a very famous three-layer API architecture where they talk about a system APIs, which is that glue code, then process APIs, which is the transformation and experience APIs, but the reality is the transformation, the conversion of data, the meaning, the exposition of capabilities and workflows requires clean interfaces that are really hard to do well and maintain over time in these tools.
I have no objection to using whatever you can to facilitate the glue code that's usually the cheapest and easiest part of the problem to solve. The harder product problem to solve and the part that requires real architectural skill to evolve over time and to maintain the purity of the interface so that you can protect the rest of the ecosystem from having to have any SAP expertise at all, they should not care about SAP, they should care about customer information or order management as a capability that speaks the language of your business and to protect that interface, it's really hard to do that well in a low-code environment.
You can still integrate with a low-code environment if that facilitates the glue, you just have to be careful about how to bound it. We talk about the bounded by in the TechRadar, and this is a great example you can bound one of those integration tools so that they just solve that glue for you and then evolve through the much more complex set of transformations to protect the interface over time in a general-purpose language.
**Neal** : Yes. That's one of the lessons I think we learned from too much orchestration in the traditional service-oriented architecture world is that this is a classic example of misunderstanding trade-offs in architecture because the way you get to something reusable is abstraction is like, "Oh, we could use this abstraction in multiple places," but the thing that makes it really useful in an organization is slow rate of change, which has low volatility because the more rapidly it changes, the more brittleness it introduces in your architecture.
That's exactly true if you're wiring directly to an SAP or an ERP API or their data. That's going to change rapidly, and that's going to make your architecture brutal because everything has to slow down every time that changes to coordinate on that change. That's part of what you're talking about, well-crafted APIs, which are ones that encapsulate volatility so that you have a very slow rate of change at the integration layer.
You can't just automatically get that low-code tools because their adapters aren't necessarily wired too closely to the APIs that they're trying to build, or they're trying to take over all of your integration problems.
**Brandon** : Yes, that's right. I really like this term that I read in one of Google's anthologies books that really get a lot of different contributors with a consistent editorial process. It was the recent one: Software Engineering at Google. Obviously, scaling to 50,000 engineers is a problem that only Google and similar organizations have faced. They talk about the difference, in that book, between programming, which you learn if you're like myself if you went to college and you learned programming in college, and software engineering, which they defined as programming over time.
The difference when you factor in the time component is where all of the discipline of software engineering comes from. I learned basic iteration, sequence, conditionals, basic abstractions, like everybody else who went to college for a comp sci degree did at that time of my life, but the discipline of testing and refactoring and deployment and observability, and all these things that enabled software to change over time is part of software engineering.
The reality is that a lot of low-code tools excel at programming, they don't excel at programming over time because you can't easily diff the source code. They don't enable parallel development tracks in the same module. The testing and the observability and deployability are impoverished compared to general-purpose languages. You have to recognize that's part of the trade-off that you accept when you start to use some of these low-code integration tools.
That's why I think it's important to put them in the appropriate bounded box, like what Rebecca was talking about with the glue code towards SAP, and bound it just to that, because, Neal, you're absolutely right, the most important part of a good API, in my opinion, for an enterprise is the interface, not the implementation. Protecting that interface and protecting the cleanliness of it is how you get scale as an organization, it's how you get agility as an organization.
That's what enables you to build a new digital product quickly because you have a clean interface to build on top of, you don't need all the system expertise down below. Protecting that interface over time as you scale adoption to multiple digital products requires quite a bit of programming-over-time concerns, you have to maintain backwards compatibility as much as appropriate, you have to be able to change rapidly in the face of new requirements, you have to have an abstraction, a frame of abstraction that you can evolve over time in a way that's backwards-compatible.
Those are often hard to do well, in a lot of these low-code tools. We use this expression, "point-to-point integrations," quite often, which you probably have heard before, but it's the idea that I have System A and System B, and I just have a direct wire between them. It's like every time I need to add a new digital appliance or electrical appliance in my house, I wire directly to the service head instead of using the circuits in the panel as the intermediate abstraction on these outlets, this intermediate abstraction.
I think the same thing is true with integration, you can have the direct wires, and obviously, that's bad for agility. What is as bad or almost as bad as point-to-point integrations is point-in-time integrations. These are one-off hops that enable you to wire up System A and System B, and maybe System C is somewhere in the mix, too, to solve a particular business problem.
Then because the abstraction was never meant to evolve, it was never meant to change over time, the next time you need some new capability, instead of reusing it and evolving it, you re-implement. Over time, you end up with a number of integrations that become impossible to rationalize, nobody can understand them as any sort of framework for reusability.
They really just were meant to solve point-in-time problems. Therefore, that's how they get around this problem of not being good at programming over time, as they create new integrations over time. I think that is a source of significant organizational tech-debt because, over the years, the more of those point-in-time integrations you have, it's like pouring concrete over your ankles. It makes you move slower as an organization. It makes your digital uptake much slower.
**Rebecca** : It also strikes me that the point-to-point integrations really codify the actual system or technology boundaries that are being accessed. From the perspective of business processes, an aspirational business process doesn't care whether the entire implementation of that lives completely in SAP or lives partly in Salesforce and partly in SAP and partly somewhere else. If we focus on a point-to-point integration, then that point is a system.
That glue code is talking to just SAP. It's not getting a little bit from SAP, a little bit from Salesforce, and mushing it together, and something that makes sense within my business context. I like your point about it being a point-in-time integration, but I think it also does reinforce the technology boundaries. That's something quite frankly I think we as IT professionals have done for too long is it doesn't really matter to the business process which box, on an architectural diagram, a particular piece of functionality lives in.
The business process cares about the behavior of that thing, and can I get the behavior to work in the context that I want? Putting in those abstraction layers allows you to construct more complex entities that might, in fact, be the conjunction of data from different parts of the system. That's particularly important when you start looking at mergers and acquisitions where different people have drawn different boundaries around their boxes, and now you want to have an integrated business process.
**Brandon** : In fact, I would say that it's one of the easy anti-patterns I look for in my consulting is how they talk about APIs. If they talk about an SAP API or they talk about setting-- MuleSoft has this terminology system APIs. The idea of a system API is it's their glue code, so it ties to a particular system. I think that's fine as an implementation detail, but that is inappropriate as an architectural strategy, for all the reasons you just said, Rebecca.
I think that if any user of your API needs to understand the underlying system of record, then you have designed your API poorly, and you have coupled the underlying system of record to the digital public system on top. That is why I think the primary goal of a good API and I use the phrase API broadly to include events, the whole purpose of a good API is to tame that complexity, is to centralize the interpretation and the complexity, the orchestration, the resilience, whatever is needed to integrate to these systems of record so that you can hide them from the users.
If that means that I'm having to get some data from an Oracle ERP and SAP system or from a Salesforce, an older Siebel system, or even from a data hub inside the organization to pull this data together to answer some questions through the API, that's an implementation detail. All of these low-code tools think in terms of implementation. That's actually what they do well is they simplify implementation.
They don't think in terms of interface and how to protect the interface from leaking accidental complexity to the rest of the organization. It'd be right to call it that way. I think that's the central purpose of good API design is to hide that implementation complexity.
**Neal** : I recently worked with a client that had-- and you'd never believe the actual numbers. I'll just say more than 20 different Salesforce implementations because each of them had a unique contract, a unique footprint, and they'd thought about merging them all, but it's like, "Oh, that's just so much work. We'll just support the ridiculously larger-than-20 teams of different Salesforce integrations."
This stuff happens all the time in large organizations, but it's one of those problems, and I think it's one of those misunderstood problems in architecture is how important contracts and APIs are because it seems like such a simple thing. "I'll just need to wire those two systems together." It seems like something that surely I can buy a generic solution to this because doesn't every large organization in the world have this exact same problem? Into that void come vendors who say, "I have a generic solution to this problem," and therefore, you get this exact problem you're decrying right now.
**Brandon** : I think what's important to realize is that when you buy these low-code platforms, you are effectively buying a programming language. Most general-purpose programming languages have been to monetize the language itself, the compiler is likely free. We might buy some of the ecosystem, like the IDE that developers use. The real policy is in developer labor, with most general-purpose programming languages.
When you buy an integration low-code tool, you are paying for the language, it is a commercial language that limits the developer ecosystem. A lot of folks go down that route hoping to lessen the cost of developer labor. Of course, that has a number of knock-on effects. One, the tool itself promotes this point-in-time view of integration as a tactical concern rather than a strategic concern.
Two, the fact that oftentimes the developer labor replies to the problem that is less experienced in general, their whole purpose was to lower the cost of developer labor. They don't necessarily recognize some of the abstractions as well. You're paying a double price with the tool itself, and the second-order effects of the talent that you attract from the tool limit your ability to create strategic abstractions for your enterprise.
I think the problem is that we haven't yet found, I think, a common language to speak to the business about that because the business gets excited about bringing in some new capability, they want to bring in some new revenue management capability. From their minds, they just need to integrate into SAP, but that's not what they're paying for. They're paying for dynamic revenue management, whatever that might be.
The reality is, those integration obstructions are what enable you to do that quickly. If you take the macro view, you zoom out a little bit and you look at Amazon, which is obviously world-class in the space, they've gone through the effort of creating very clean interfaces between their business units. When you go to Amazon.com and you might not know, but you're looking at a third-party seller, and it says "Fulfilled by Amazon."
That is a third-party seller storing their inventory and shipping their inventory out of Amazon warehouses. The reason Amazon can do that is because they put a very clean API interface initially internally for their own fulfillment and then they were able to externalize that. They've done the same for their call center. They've obviously done the same for infrastructure with AWS.
The ability to attack adjacencies, the ability to move at speed requires this ability to tame complexity of organizational business unit boundaries and to speak in the language of the business, and to hide the underlying system complexity. I think the idea that I just want to get this revenue management system wired to SAP and treat anything in between as tactical maybe delivers that revenue management project quicker than you would otherwise have it delivered but at the cost of long-term agility for your organization. I think that's one of the key messages that we need to reframe in terms of how we talk to the business around integration.
**Neal** : One of the other interesting evolutionary changes we've learned about in software architectures back in the days of orchestration-driven, service-oriented architecture, the idea was, let's base the entire architecture around orchestration in the center because there are fundamentally two different ways to solve the integration problem.
You can either push the problem to the center and build a bunch of adapters and let it manage all the integration logic, which the traditional old-school enterprise service does, or you can push all the edges, and that's the more modern approach with things like service mesh and what you're talking about, Brandon, which is building your own API, carefully crafted APIs around the boundary points that you choose versus the ones that tools choose for you.
**Brandon** : The tools you use have a heavy influence on the architecture that you end up with. A lot of the tools influence smarts in the middle. In the microservices world when the first article came out with James Lewis and Martin Fowler, one of the principles they talked about was smart endpoints and dumb pipes. A lot of these tools are the pipes, and they try to put a lot of smarts, they sell a lot of smarts into it.
A lot of them have the heritage from this ESB world. I mentioned MuleSoft earlier. MuleSoft has an API platform that's quite popular. They have a heritage of an ESB tool. I look at ESB architectures, and I see a lot of similarity with ETL tools because a lot of them are "Let's get the glue to the underlying system, which is the extract, let's have the orchestration transformation in the middle, and let's load it, and you can map that pretty directly to a lot of these integration tools," which is trying to centralize logic and trying to put a lot of the smarts in the pipes.
I think the trend that you're calling out is absolutely right. We're seeing a trend where a lot of that logic is moving to the edge. Sometimes that means creating additional nodes at the edge and treating them as first-class products that we might not have otherwise done so. Treating APIs as digital products themselves with a user base that happened to be the consumers of the API and involving them with product management practices means that they become nodes on the edge themselves.
That furthers this decentralization of a lot of the middleware that we're seeing. I think even tools like API gateways are under some amount of threat from service meshes because policy that used to, and it's quite common and still is applied at the gateway level even if the API itself is built in a general-purpose language outside and we're just proxying through, a lot of that policy now can exist in the service mesh at the edge at the sidecar.
You can use an SDL, and you can apply a lot of the same policies that you might in an [unintelligible]. I do think that that trend is going to continue. I think it takes advantage of Moore's law much better. I think it takes advantage of the scale of trying to build throughput in an organization for delivery because it provides more autonomous delivery mechanisms.
I think we will continue to look for ways of scaling both the abstractions and the developer effectiveness as we move, as we continue that trend. Plus one to your point, service meshes have provided a really good approach to continuing that federation of logic.
**Neal** : And a different way of thinking about those cross-cutting concerns that are separate from your domain. I want to call out that you used the magic product word there, which I think is a really good encapsulation of this idea you're talking about that it's software over time because a project is a snapshot in time, but a product lives forever. Thinking about your APIs as products puts longevity in there and thinks about evolution. How am I going to version myself over time when other people need to connect and get different information, or how do you manage that? I think product thinking is a nice shorthand way of encapsulating a lot of the benefits you're talking about.
**Brandon** : I think it has advantages also to think about it as a product when you think about the interface itself because if you think about Google search, it's a dead-simple interface. Now, can you imagine the complexity underneath the hood? It's enormous to satisfy the search across the entire world's internet in milliseconds and to give contextually relevant information.
There's all kinds of information Google could have asked us as users to make that more effective. They could have asked us for geographical information, or recency information, or some clarification, or a special language to piece together the search terms. Of course, they have advanced capabilities that let you do that, but by and large, I just type in what I'm thinking and do a search box, and I get results immediately.
We have to take that same type of digital product thinking towards API interfaces. We have to simplify them as much as possible because we're trying to hide the ecosystem from the underlying systems of record, we have to evolve those over time. A phrase I use a lot in architecture, and especially in API architecture, is that our goal should be to create the future and to abstract the past.
We want to create the interfaces so that we can evolve the business in the direction that we need to go. Adopting the past is where a lot of architectural skill is required because you have to build up. That might be some orchestration, it might be some caching, you might need a data hub, you might need the resiliency mechanisms, different integration protocols.
That's really challenging oftentimes in these legacy environments to convert these systems of record that were never meant to be API-enabled into something that is a cleaner interface for your business. That is absolutely central to product thinking. It's no different than this phone in my hand. I'm sure there's a lot of complexity that goes into providing this simple interface, but if it didn't have that simple interface, we wouldn't have so many users of phones.
You're absolutely right. Product thinking is central to scaled architecture, and product thinking is also a shift from the centralized model that you were asking about earlier where we tried to put a lot of logic in the middle and there was all enterprise architecture controlled to now where we can have a lot of autonomous development teams working in parallel. As long as they have mission alignment, the tooling exists for them to work at the edges to manage adoption of their digital product.
If their digital product is an API, that means other delivery teams, but they can still manage it as a product, put a lot of the cross-cutting concerns there are at the edge, and then work in parallel with much more efficiency than we could in the model where everything was centralized.
**Rebecca** : I do have one question here from a trade-off perspective. You mentioned earlier the initial microservices article, and since that article, there have been all of these discussions. "Do I start with a microservices architecture? Why do I need the complexity of a microservices architecture because it introduces failure modes, for example, that are not possible?"
How much of what you've been talking about today do you think a startup that has zero lines of code needs to worry about? It's very clear in these large enterprises with that history and with that past that they have to take account of because it is their reality. How much of what we've been talking about today is something that the Day 0 startup just doesn't need to think about?
**Brandon** : I think a Day 0 startup's primary mission in life is proving that people will pay money for the product that they're offering or the service that they're offering. If they feel that the cheapest way to do that is through a low-code platform, then that's absolutely the right choice in my mind. If they need to get proof of value and they're racing and they're trying to beat the competition or they're trying to get there before their investment runs dry, then use whatever tooling gets you to that marker as quickly as possible, but be prepared to throw it away because it will not grow with your business.
On the other hand, you're right if you start off with all-general-purposes language, you start off with a high cost of development labor, and let's say that you're not a digital product, and this is a part of the ecosystem that you're building as a primary value creator. If you start off in a distributed microservices architecture, you're going to pay a big complexity tax early that is going to slow down your learning about your product-market fit, which is the primary early driver. I do think it's a good point early on in the life cycle if you don't yet have product-market fit established, if they're the cheapest way possible, just be prepared to throw it away.
**Neal** : Before we leave everything on too negative a note here, let's summarize some of the good advice that you're providing as a way to avoid this very-- It's a very easy trap for organizations to fall into because it's one of those things you seem like you could buy your way out of, but like you said, it's really a failure to evaluate trade-offs in many cases.
The low-code environment, you called out the problem of inability to diff, but there's also IDE support and refactoring that's part of that software engineering life cycle. Most of these tools that are tied to a particular vendor don't support sophisticated refactoring and the supports you get in IDEs. Where's the trade-off? Where would you use this approach, and where would you not use it? Some delineated advice for our listeners.
**Brandon** : Yes. There's a few areas where I think using low-code tools makes sense. The backdrop, of course, as I've already stated, is I think they are overused and over-marketed, and I don't certainly blame product companies for marketing their wares I would do the same if I were in their shoes, but I think we as architects need to be aware that every product company is wanting to try to overmarket their services. That's how they grow.
I think that we have to be careful about the context in which we use them. One, Rebecca mentioned the startup community. Again, if that is the quickest path to learning about product-market fit, I think that's a good use case. One that I hinted at previously is bounding the use of low-code tools to solve tactical implementation problems because these tools think in terms of implementation. As long as you are approaching your integration strategy with the mentality of the primary focus is protecting the interface and the evolvability of that interface over time, then you need to be able to control the ownership.
A lot of the low-code tools or ecosystems that want you to solve as much of the problem space as you can inside the tool, then when their complexity ceiling is hit, jump out of the tool, and then maybe you go on to a custom-built Java application, for example. I think you need to invert the ownership there. I think you need-- Let's say if you're programming Java, you need a Java application to own the API space, but there might be this shim that connects, for example, like Rebecca was talking about, to SAP, and maybe that shim is the low-code tool because it has an adapter baked in, so it can do the protocol translation for you.
The primary ownership is your job at API code is still a general-purpose language and still manages a lot of the programming-over-time concerns, but you've simplified an implementation task through the low-code tooling. Another area that's a bit niche but common enough that it's worth pointing out is I've run, a few times now across a few different industries, this scenario where there is this really long tail of B2B integrations.
For example, it might be that you sell your parts through dealers, a dealer ecosystem. A number of the dealers have a standard order management system, but as you start to cross down the long tail of your partners, there's a lot of smaller dealers that don't have IT capabilities that have a wide variety of systems, so if you rely on them to integrate into some beautifully built API that you have, you just won't actually get them to participate because they don't have the IT savvy to do so.
A lot of times in some of those B2B integrations, the person or the organization providing the API may actually build the integration themselves to incentivize some adoption of it. To do that well, you more rely on the B2B partners that do have IT capabilities to do it themselves so they can manage that ecosystem. Those that don't, you want to recognize that there's a lot to build.
A lot of them will change very slowly because they will involve lawyers and procurement and organizations that aren't built to change rapidly in a digital world. To capture that long tail with B2B be to be integrations, there is some value in using some low-code tools to do those translations because a lot of them also rely on legacy cross-organizational integration patterns like an FTP drop, or they might have a lot of them.
I worked in a healthcare organization where you had to translate it up to ASCII because it was a mainframe drop via FTP. A lot of these tools have those kinds of transformers baked into them. "Grab from FTP on this Cadence up to ASCII. Here's a basic transformation and then pass it on to a canonical API that's custom-built," but that adapter layer if you're trying to capture the long tail of B2B integrations, it's a cheaper way of doing it as long as you feel comfortable that each of those adapters you build isn't itself going to have to evolve rapidly. Generally, that's a pretty safe assumption in that context.
**Neal:** Okay, great. Well, it's a great topic. This is a great example of what I refer to as the superpower of consultants because we get to see lots and lots of different projects, a lot of different approaches, and you see the same kind of approach taken over and over, and you start seeing the places where it works and doesn't work. Thank you very much, Brandon, for giving us some of your real-world experience on encountering this problem out in the real world. I think you're correct. It's really just a cry to be more careful about evaluating your trade-offs that something seems simple but it turns out complicated in the long run.
**Brandon** : Yes. Thanks for having me. I have an article that's nearly done. I will be publishing it in the near future. Keep your eye on it. It'll be called You Can't Buy Integration, to try to make that buy-versus-build trade-off a bit more explicit and then unpack some of the trade-offs that we talked about but definitely appreciate, Neal and Rebecca, you folks having me on so I can talk through it and certainly look forward to getting some feedback via Twitter on @BrandonByars and feel free to message me or trouble me, whatever's appropriate. I'm happy to engage.
**Rebecca** : Thanks, Brandon. An enjoyable conversation.
**Neal** : Hello, everyone. On the next Thoughtworks Technology Podcast, join me and Rebecca Parsons as we talk to Saleem Siddiqui about his new book, about Test-Driven Development.
[ Read full transcript ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
Listen to more episodes 
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