<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-fitness-functions-help-govern-measure-ai | Title: How fitness functions can help us govern and measure AI | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  How fitness functions can help us govern and measure AI 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Evolutionary architecture ](https://www.thoughtworks.com/evolutionary-architecture)


Podcast host  Ken Mugrage | Podcast guest  Rebecca Parsons and Neal Ford
March 06, 2025 | 42 min 01 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-fitness-functions-help-govern-measure-ai#Transcript)
Listen on these platforms
## Brief summary
AI is inherently dynamic: that's true in terms of the field itself, and at a much lower level too — models are trained on new data and algorithms adapt and change to new circumstances and information. That's part of its power and what makes it so exciting, but from a business and organizational perspective, that can make governance and measurement exceptionally difficult. How can we know that our AI is optimized for the right thing? How can we be sure it's oriented towards what we want it to be?
This is where the concept of fitness functions can help. Broadly speaking, fitness functions are ways of measuring the extent to which a given solution is fulfilling its goals — so, in the context of AI, they can help teams ensure that AI systems are serving their intended purpose.
In this episode of the Technology Podcast, Rebecca Parsons and Neal Ford — authors (alongside Pat Kua and Pramod Sadalage) of _Building Evolutionary Architectures_ , the book which brought fitness functions into the software architecture space — join host Ken Mugrage to explore how the fitness function concept can help us better manage the dynamism of AI and, in doing so, overcome the challenge of bringing such systems into production.
Learn more about [_Building Evolutionary Architectures_](https://www.thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition). 
## Episode transcript
**Ken Mugrage:** Welcome, everyone, to another edition of the Thoughtworks Technology Podcast. My name is Ken Mugrage. I'm one of your regular hosts. A little bit of an interesting panel today; we have both hosts and guests at the same time. I'll let them introduce themselves. First, Dr. Rebecca Parsons.
**Rebecca Parsons:** Hello, everybody. Rebecca Parsons, former CTO Emerita of Thoughtworks. I have been a co-host for many of these podcasts, but in this particular case, I'm the guest to talk to you about fitness functions.
**Ken:** And Neal Ford.
**Neal Ford:** Again, I'm another regular host of the podcast, but mostly here as a dual duty of both co-host and also a guest because Rebecca and I co-wrote both editions of the Building Evolutionary Architecture book, which defines this idea of fitness functions. One of the frequent questions we get in the current day and age, of course, because no one can talk about anything except generative AI in the technology space, is, well, how does this concept of fitness functions apply to AI?
**Ken:** Yes. For the listeners, it's interesting. We were just talking to the three of us before we started recording that this is something we've been talking about for a couple of years. Obviously, AI has been out for decades, but generative AI really kicked it off. We're like, okay, how do you test these things? You have bias. You have the "ilities," which I'm sure one of our guests will get into a little bit.
Fitness functions come up over and over. We thought we'd take a look at it. First off, I guess just somewhere where everyone's on the same page, Rebecca, do you mind giving just an overview? What are fitness functions? Why do they matter?
**Rebecca:** There is a strong influence from the field of evolutionary computation, whether it be genetic algorithms but also more traditional optimization, where you have something that is your definition of good. Now, one of the easiest examples of this is the traveling salesman problem. You have a list of cities that this individual is supposed to visit, and you need to order those cities to minimize the distance that the person has to travel.
It's that minimization of the sum of the distances that is the fitness function. We use that in optimization techniques as a way of trying out different formulations of answers to see how I can get closer and closer. Now, with something like the traveling salesman problem, and many other optimization problems, you can't guarantee that this is the best answer because of algorithm complexity, and we won't go into that.
As soon as you start to get into something a bit more complex, where you have two different things that you're trying to simultaneously come up with a good answer for, we get to use Neal's favorite word when talking about architecture, which is "trade-off." If you want to maximize throughput on a production line, you have to minimize retooling. If you also want to optimize the variety of things that you're doing on that assembly line, well, you can't maximize both of those because every time you do something new, you have to retool the line, which brings down the overall throughput of the line.
You have to decide, "What is the right balance point between overall throughput and the variety of things that you're putting on the line?" Again, that measure of how many different kinds plus throughput of the overall line, that is, again, your fitness function. The single most important thing about a fitness function is that you and I will never disagree on whether it passes or not, on what the value is.
Something like cyclomatic complexity less than 20, completely objectively defined, you just run the formula for cyclomatic complexity. Maintainable? No, because you and I can disagree. One of the challenges we have with a fitness function very often is taking this vague notion that we have that we want our code to be readable and maintainable and all of those kinds of things, is what does that translate into in terms of a fitness function where there are things that we can measure where you and I will not ever disagree on whether something passes or not?
Now, in the vast majority of cases, we want to be able to automate these things, and that's where the true power of a fitness function comes in is once you've got a fitness function that's monitoring whatever characteristic, you don't have to think about it anymore until the fitness function flags up and says, "Hey, pay attention to me. Something's going wrong."
That allows you to apply our human brain power to things like, "What is the right balance point between the heterogeneity of our manufacturing line and our overall throughput? Where should that balance point be?" Because that's something that, well, you have to discuss. Maybe it's security versus throughput. Maybe it's resilience versus some other characteristic. We're having to make decisions about, "What constitutes good?"
For some things, like if you want to maximize the throughput on a manufacturing line, that's easy. What is the measure? What do you want the limit to be? When you start talking about something more complex, then you actually have to have a discussion of "What is the trade-off? What is the sufficient amount of heterogeneity that I can get, and I'm willing to pay for that with the decline in overall throughput? Where is that point?"
That's where the real work of fitness functions comes in, is turning some of these vague notions or some of these trade-off situations into something you can measure and then test.
**Neal:** I was going to say I really like Rebecca's example of throughput because one of the ways that we distinguish traditional kinds of testing, like unit tests and functional tests, is that, and this really didn't come to us until we wrote the Head First Software Architecture book, which you can split the architecture design into behavior, which is your domain, but then capabilities, which is where the "ilities" word come from because it's describing capabilities.
Rebecca's example is perfect for that because throughput, notice she didn't once say what we're manufacturing. It could be widgets or books or yoga mats or whatever. Throughput is a capability of the system, not the thing the system is about. That's exactly true for fitness functions. We're measuring capabilities, the ilities of software, scalability, elasticity. This runs parallel to traditional kinds of testing.
We're only testing the architectural behavior of the system, which brings us to what sort of interesting architectural things, challenges does AI present that we can get to what Rebecca is talking about, which is something that we can agree on as an output for the outcome of the capabilities of one of these things?
**Ken:** One of the concepts in the evolutionary architecture book is the idea of guiding evolution. I don't remember anything that has moved as quickly as AI has been in the last couple of years, whether it be new models or new players or, heck, new billing, right? I want to change from this vendor to that vendor because it's a fraction of the cost. Do you feel like these fitness functions are a way to put boundaries around that? How can they help people in the incredibly fast-moving world that we're in right now?
**Rebecca:** Well, I think I'd start with, what are your expectations around your use of these models? It's those, again, behavioral characteristics. A very obvious fitness function that you might want to put into place for a product is to monitor, "What is the cost of the activities?" That's pretty straightforward. That's transactions time per transaction unit cost equals total cost.
You can set a limit on it, or maybe you can set a rate on it, and you can throttle things if you're consuming your budget too quickly. There are other ilities that are also quite important. Latency is a big deal. People have talked about the fact that if you use the free version of some of these models, then it takes longer to get a response than if you're paying for preferred access to the model.
Latency is set to become more important with these chain-of-thought reasoning models that are coming into play, where they're building in the notion that the answer is not going to be instantaneous because it's got to think about it. We like it. Studies have shown this all the time for humans. When you ask a question and if the person you're asking the question of actually pauses, you get the feeling that they really are considering your question. They're listening to you before answering, as opposed to me asking Neal a question, and he immediately blasts the answer back.
It's like, "Well, he's just telling me what he thinks I want to hear or what he wants me to hear. I don't care what the question was, I'm going to give you the answer that I want to give you." We're less tolerant of that with technology. All kinds of studies also show that if you don't get a response, people are abandoning pages, abandoning carts because it's just taking too long. This whole notion of latency is going to become a big factor in how people view the success of some of these models. That's before we even get into things like bias and hallucinations and things of that nature.
**Neal:** Exactly. To Rebecca's point and to what Ken was asking about, if we need to move things quickly, it encourages us to define the capabilities that we need to address what kind of latency is acceptable in this architecture and build a fitness function around that, which allows us to swap out another model and see, "Does it still meet our capabilities that are required for success?"
This is a particular challenge when you move from prototype stage into production because now we need to do it at scale. What kind of impact does that have on responsiveness or latency or this host of other things? The ability to quickly play what-if games by, "Well, let's build an anti-corruption layer for that capability and swap out this other thing and measure its capabilities in a realistic environment," I think, facilitates this idea of being able to move quickly and swap things out at a rapid pace to match the ecosystem. Of course, we're never going to be able to match the ecosystem. It's always going to out-sprint us, but at least we have more of a fighting chance.
**Rebecca:** This is a point we make for even the more traditional applications of evolutionary architecture, if you're not evolving your fitness functions, you don't have an evolutionary architecture either because, as the technology capabilities increase, you might want to set your objective higher as a result of the increased capability. You need to constantly reevaluate, "What are the social and cultural characteristics? What are the business model characteristics? What's the regulatory framework? What are your customers' expectations? The technology landscape, how do all of those things come together that might affect how you define good?"
At the end of the day, your composite fitness function, what I say is your target architecture is now the conceptual composition of all of your fitness functions because that's what you're trying to get the architecture to achieve. That's what you're trying to get your system to achieve. We wanted to demonstrate these capabilities to this level, and this is what we're trying to achieve. We're focusing on the outcome and not the implementation.
That's one of the big shifts in thinking about things like architectural governance that we get from thinking in terms of fitness functions is we're focusing on the outcome. Are you demonstrating this capability or not, as opposed to the implementation? Are you using this particular approach?
**Neal:** Well, in fact, and this is a little bit of a sneak peek for the upcoming technology radar, one of our themes is about how quickly observability is advancing, both in traditional distributed architectures and around generative AI. To Rebecca's point, if you're not keeping up with observability, you're going to miss a lot of capabilities that are growing like mushrooms after a rainstorm.
We always see these hotspots of innovation in the software world that literally give you new ways to measure things or new ways to assess things, more objective ways to measure things. It's important that you keep evolving your fitness functions. Lest we frighten people into, "Oh, this is going to be a huge burden," these things always change much more slowly and less aggressively than unit tests or functional tests because unit tests and functional tests are literally changing all the time because you're growing your behavior and changing it all the time.
You don't change your capabilities that much. You establish those capabilities objectively, and then you verify them very often. It's rare that you change the fundamental responsiveness or performance numbers in your architecture without other major changes, but you incrementally add behavior all the time. You do need to keep them alive, but it's not a huge burden because once established, now, it's basically just acting as an ongoing safety net to make sure that we haven't broken something important.
**Ken:** A lot of what we've been talking about so far is systems that are using AI, but it may be a shock to some folks that there are systems out there still that aren't using AI — legacy and others! That said, especially developers and folks like that are really looking at AI tools to enable them to work faster. We talk about AI-first software delivery inside Thoughtworks quite a bit, et cetera. What about using the AI stuff that's out there to work on fitness functions for other systems? Have you been looking at that at all and how to help create and maintain these?
**Neal:** Yes. There are really two aspects that we're thinking about broadly when you talk about fitness functions and generative AI. One is using them, using generative AI as a coding assistant, just like you would as a software developer. One of the challenges people have is, well, I'd really like to write a structural fitness function, but now I've got to learn this new API or an ecosystem that has Java and .NET.
Well, I don't have to maintain a Java fitness function and a .NET fitness function, which is cumbersome. My co-author on the Software Architecture: The Hard Parts book, and the upcoming book we're going to do, Architecture as Code, we've actually had great success by leveraging generative AI to describe the constraint we want in architecture, basically in pseudocode, and then telling generative AI, "Give me a Java fitness function that matches the outcome of the pseudocode."
It's shockingly good at this, but in hindsight, we shouldn't be so shocked about it because it's a language model. It's really good at translating from one language into another in pseudocode to Java or pseudocode to .NET. What this allows you to do is to create a really terse declarative language that describes the structure of your architecture, the constraints of your architecture, what systems should be able to talk to one another, what systems should not be able to talk to one another, and then use generative AI to generate concrete fitness functions that you can put as part of your deployment pipeline or continuous integration and validate these things as you're making changes to the system.
It's almost like it's a step between a traditional architecture decision record, which is succinct text, but text-based and diagram-based. This is a step between that and the actual implementation of a fitness function, which is sort of a pseudocode representation. This gets around the barrier that architects don't have to learn a completely new API or have to write the same fitness function multiple times. They just express it once and then code-gen the alternate versions of it.
**Rebecca:** Well, one of the interesting aspects of this, and this is something that I often get asked about, "How do I define a fitness function?" Some of them are incredibly straightforward. You don't want memory usage to exceed this, or you need this amount of throughput, or you want this kind of response time. Those are all very easy. One of the examples that I know I use, and I think Neal uses it as well, a very clever fitness function, which I think now in the generative AI days, people would have approached this very differently, but this was pre-LLM.
The lawyer for this particular organization asked, "Well, of course, all these open-source projects are going to notify us when they change their license terms, aren't they?" Of course, the development team just sort of laughed because, no, they don't even know who is using their open-source product. The lawyer said, "Well, then we can't handle this. You must be able to tell me."
They came up with a very clever, simple fitness function, hash all the license files, and compare the hashes every time you do a build. If they've changed the license file, the hash will almost certainly fail the hash check. It sends an email to the lawyer. It doesn't try to do anything about understanding what the change is. It just says, "Take a look at this. This file has changed."
Now, as we say now, people probably would have tried to be more clever and say, "Feed them both in and tell me semantically how these things are different," but then still they'd have to send it to the lawyer. It wouldn't really have accomplished much, but very often, figuring out, "What kind of thing can I define to establish the capability or describe the capability that I'm looking for?" That's the real work in a fitness function.
That's the intellectual work in a fitness function. As Neal points out, there can be implementation challenges behind these, but you still have to figure out, "How do you give it the prompt? How do you come up with the pseudocode?" That does require you to think about, "Okay, what am I trying to measure here, and what is the best way to go about doing that?"
**Ken:** That makes me wonder if the concept of coming up with even the pseudocode is helping you understand the business better, right? What are you really trying to get to? Is that an intended thing, or is that an unintended consequence or?
**Rebecca:** I think it's very intentional. At least there isn't really any way you could approach this other than you have to think about this in the context of your business model and your customers and the technology landscape and all of those things. Even though, as in the throughput example, as Neal pointed out, I made no reference to what it was that was coming off that line, it is a business trade-off decision on what is the right balance point between the heterogeneity of the output and the overall throughput.
That isn't something that some architect sitting in an ivory tower can decide all by himself. It is a business decision. We have to think about this in the context of what we are trying to achieve overall as an organization. Now, the hash file example, that's still a business question. They were trying to address the problem of "How do I make sure the crown jewels of my proprietary code aren't accidentally leaked because somebody changed a license file and now I have to make my crown jewels public?" That's a business concern.
**Neal:** I think at the end of the day, the beneficial side effect of this is it encourages architects to try to objectively define things because once you get to objective definitions, you can verify them and test them. It also facilitates-- We see, too, many organizations where they use a lot of vague terminology, like, "Oh, we want really good performance." Okay, well, write me a fitness function for good performance.
"That's meaningless. Tell me some numbers within a range of how you want performance." Now, I can write a fitness function for that. Just the encouragement of boiling it down to concrete measurable things because very often in the exercise of getting down to concrete measurable things, you'll realize what the real constraints are that you're up against early rather than very late in the development process when you realize, "Oh, this will never actually achieve that level of performance." That is a very intentional benefit of going through this analysis to figure out what your fitness function should be.
**Ken:** Who owns these? Let me tell you why I'm asking that. I used one of these tools the other day to refactor a Littled application with the expectation that now the test would fail, and it didn't. I'm like, "What the heck?" Well, it turned out this tool went and refactored the test, too. It's like, "Well, didn't really want that to happen." If it had been, not to get too in the weeds, but in a separate code base or something else, that wouldn't have happened. Who owns the fitness function in an organization?
**Neal:** My answer to that question is usually yes.
**Ken:** Okay.
**Neal:** Architects typically write them, but developers are going to trip them and fail them. It's really, really important to have developers understand what these things are for because they're going to be the ones that make them fail and then have to fix them, which is a little bit annoying, but it's really the same function as unit tests and functional tests. Look, this is insurance for the future.
If I break this fitness function now, that means I was about to make a change that's going to break some capability that's important. It may be a small thing now, but left unchecked, this is going to be a disaster in six months. It has to be joint ownership. One of the things that very early on when we were writing the first edition of the book, we realized that we were giving architects a very sharp stick with which they could poke developers if they wanted to.
We told them, "Please don't use the sharp stick to poke the developers. You shouldn't create an antagonistic, a police state with fitness functions. This has to be collaborative because you need to share the understanding." In the same token, developers are going to run across things that really should be encoded to set the functions, and they should create a feedback loop back to the architect to do that.
As I said before, the burden of these things is not nearly so high as adding a new unit testing framework or a practice like unit testing because once established, these mostly just sit in the background and hum along and only warn you if something dire is about to happen. I think you want a warning if something dire is about to happen, even if it does because short-term inconvenience.
Rebecca: Yes, and I think there are particularly more complex enterprises. You probably have some hierarchy of architects. Neal just used the architects on them because they're architectural characteristics. Some might be for a business unit versus the entire enterprise. We like to get the ownership and the decisions around those fitness functions as close to the team as they can get because, there, you can start to bubble up.
"Well, wait a minute, this thing you've just given me, this conflicts with something very specific in my environment. We have, now, one of these conflict trade-off situations where we have to have a discussion about it." The more understanding that the team has about why these fitness functions exist and what they're trying to protect, the more fruitful those conversations can be when something new does come up and it conflicts somehow.
There's things that are done at an enterprise level, probably related around cyber would be one example, whereas some other things, if you're working on a primarily internal application where you've got a small department of people doing a function, your scalability requirements are going to be very different from something that is customer-facing where you want that to have to scale because you want to increase your customer base.
You don't necessarily want to increase the number of accountants or whatever the internal function is. They should be as close as possible to where the problem is because that's where the understanding of what those right levels are resides.
**Ken:** There's a couple of things in an application that's built around AI, or especially in the new world of generative AI, that have been an issue with applications forever, but they really come higher up. It's the bias, of course, but then also the relatively new concept of hallucinations. Are fitness functions helpful in either of those areas? If so, how?
**Rebecca:** In particular, when you think about bias, yes, you can write fitness functions for it. Let's say you're doing some kind of credit application or credit scoring, something like that. You can set up mock profiles that exhibit different characteristics and see whether, "Okay, does this version of my credit scoring product discriminate on the basis of gender or race or whatever?" That's where that intellectual process comes in.
Where are the likely sources of bias, and how can I best expose them? Again, being focused on the outcome, not the implementation, you don't really care at the fitness function stage why that credit score for the man was higher than the woman when everything else was identical. You don't care about that. You just care about "This is demonstrating bias because, all other things being equal, it gave more money to the man."
When you start to talk about hallucinations, I think that becomes more difficult. I still think fitness functions have a role to play. It could be something trivial, like if you can determine that this answer came from a source, can you actually hit the source and have it retrieve something other than a "not found"? That would take care of many of the issues for things like made-up articles, made-up case law, things of that nature, because if you tried to hit that, it would come back as not found, whatever that might be in terms of case law, as an example.
That's not going to stop all hallucinations, but it at least gives you a place to start. This goes back to what I was saying before about how the intellectual effort around a fitness function is really understanding where the problem might come from and how can I test that? How can I define it in such a way that we can actually test that?
**Neal:** Yes, that's a great example of, okay, LLMs have given us all these brand new capabilities in our system, but then how do we check those things, objectively measure those things? That's a great example for hallucinations. Can we follow this link in a protected sandbox or something? Because we've seen examples now of people putting-- if an LLM commonly hallucinates something, a link, we see malicious actors put a bad code behind that link so that naive people will pull that into your project.
Having a fitness function that checks in a sandbox to make sure that it's a legitimate site, et cetera, would be one way to protect against that. To Rebecca's point, and this actually goes back to a question that Ken asked earlier, this really encourages the team to start thinking about, "How can we objectively measure the capabilities of this black box?" Because this is unique in most things in the software development ecosystem, where while software sometimes acts non-deterministically, it is actually deterministic, but LLMs are not. They're fundamentally not deterministic.
Coming up with ways like for bias, a great example because it may give you different answers with the same inputs, "How do you check to see the important parts of that can we objectively measure versus the minor differences that may occur because of wording or semantics, but the fundamental meaning of it, is it aligned with what we want it to be?" Another great example of a fitness function around an LLM is actually a pattern that we saw identified by one of our teams, which is "How can I make sure that the output of my inexpensive LLM is good enough?"
They basically built what I would call a parity fitness function that took some of the output of a lower-cost LLM, ran it through a more expensive LLM, and compared the results to see if it was in an acceptable threshold. That's a cost-saving fitness function for an LLM, but it's very much a parity or fidelity fitness function to say, "This is something that's running in the background to verify we've made a business choice for this less expensive LLM. Can we objectively measure? Are we getting the right, an acceptable level of what we want out of this solution?"
**Rebecca:** Some of them are trivially obvious. Very early on, for example, many people put in filters to make sure that people were not sending to the open internet models personally identifiable information. You can scan for some of these things and say, "No, you cannot do this because that's wrong." In cases like that, it's pretty easy to define what you're trying to achieve.
You're trying to protect people's data, or you're trying to protect your intellectual property, and therefore, these things can't go out. That, again, is a fitness function that is monitoring, in this case, more a person's behavior rather than the system's behavior. Again, the capability that you were trying to achieve is data privacy or protection of intellectual property, things of that nature.
**Ken:** What I'd like to do is ask you each to put on your futurist hats. I know you love it when I do this, and you can pick your own timeframe. I guess, Neal, I'll go to you first. What should people be watching for in what timeframe?
**Neal:** It's a great question, of course, and I can guarantee that whatever we speculate about now will be wrong. The more into the future we speculate, the wronger it will be. That's almost a given when you put on some sort of genie hat like this. The main challenge I think we're going to face in the near term is not actually the really cool, interesting part of LLMs. It's the drudgery of productionalizing this stuff.
As architects, as tempting as it is to want to crack into the LLM and fine-tune it or build all these capabilities, that's really more of a specialization. This is like sitting down with your data scientists and pushing them out of the way and starting to mess around in their notebooks and stuff. That's probably not what you should be doing unless you have expertise in that area. What we do have expertise in is putting these things in production.
It's great to do these little demos, but then having a demo operate at scale can sometimes be really challenging. I think what this is going to do is put even more emphasis than we've had in the recent past on coming up with, "Well, what does success mean in terms of capabilities here? How can we actually measure those things?" Ironically enough, once you've identified those objective measures, you can have the LLM help you generate the guardrails around itself to be able to check those things as you move forward.
As you said earlier, Ken, we are in a perhaps short-term, maybe longer-term, bursty growth era in the software development ecosystem. It's more important than ever if you're going to play what-if games with all these different capabilities. There are all these different capabilities that are coming up. We identify hotspots of innovation. Again, on our most recent radar, we highlighted the R in RAG for retrieval-augmented generation.
We didn't highlight the augmented or the generation part. It was R's time in the spotlight. The next radar, it's going to be something else. As we have all these capabilities with explosive growth, it's good advice from the domain-driven design world to put some of these capabilities behind anti-corruption layers, which is just a fancy word for an interface, so that you can swap it out with new things that are coming down the pike.
You also want fitness functions to verify that "Oh, I've easily swapped out one RAG database for another one. Now, does it still meet my performance, my responsiveness?" That's the safety net for allowing you to have an aggressive stance toward incorporating some of these Gen AI elements because you can get rapid feedback for, "Is this making things better? Is it just clouding things or degrading something that we didn't expect it to? Oh, look, we get much better responsiveness. Oh, look, it doesn't scale."
Finding out that balance of things, this goes back to what Rebecca was talking about, balancing these concerns. This helps you do that because you have objective measures for what's going on. I guess my time frame is like six months in the future. That's as far as I'm willing to speculate.
**Rebecca:** I always say my crystal ball is still broken. I've been involved in AI for a very long time. I have seen the succession of AI winters. I am starting to see more references to where we are on the Gartner Hype Curve. Different people put it closer to the precipitous drop into the trough of disillusionment. One of the things I think we are starting to recognize is there are capabilities that truly are revolutionary in what we've come up with with LLMs and how we can use them.
It is not a silver bullet. I think one of the reasons, for example, that we see such a low rate of actually productionizing many of these pilots is the fact that it's one thing to clean up your messy data so that it works for your group of nice, well-behaved customers who aren't going to complain too much, but trying to scale that to your entire customer base is much harder.
I think one of the things, just like in many of the data science applications that were coming out before LLMs hit the scene, if you don't have a good database to work from, you're not going to be able to deploy these intelligent products that rely on that data. I think one of the things that we are going to see, again, in that short term, is a lot of resources being thrown at, "How do I clean up my data?"
This may, in fact, be the time when we finally get rid of those "Well, in the period of time between November 4th, 1985, and January 12th of 1986, this field meant that." There were landmines like that all over these enterprise datasets. People talk about bit rot and how code deteriorates over time. Data, the older the data is, the much more likely it is that it doesn't say what you think it says. I think we're going to have to deal with that.
I also think that we need to distinguish the Gen AI trajectory from the AI trajectory. What people think of Gen AI in terms of things like natural language and all of that, there are capabilities that are being developed in other disciplines that I think we're going to see move productively more quickly than some of the things. I don't think we are on the cusp of AGI, and I'm not even sure that I think that AGI is the right kind of objective at the moment.
This might be more wishful thinking than anything else, but maybe we can start to understand, "Here's the sweet spot. LLMs have a sweet spot, just like every framework has a sweet spot. Here's the sweet spot. This is the stuff that it does really well. Let's figure out how we can exploit that."
**Ken:** Great answer. It's all about the data. [laughter] Yes. I want to thank both our guests. Again, the book, fitness functions are a big part of it but there's a whole lot more to it, is Building Evolutionary Architectures: Automated Software Governance, by Neal Ford, Rebecca Parsons, Patrick Kua, and Pramod Sadalage. Am I saying his last name correctly?
**Neal:** Sadalage. Pramod Sadalage, yes.
**Ken:** Thanks. Sorry. Sorry, Pramod.
**Neal: I** had to learn how to pronounce his name when he became a co-author, so it's a tricky one.
**Ken:** It's available at a bookseller near you and your Kindles and all that neat and happy stuff. Again, thank you, Neal Ford. Thank you, Dr. Rebecca Parsons, for your time.
**Rebecca:** Thanks, Ken.
**Ken:** My pleasure.
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
## Explore a snapshot of today's technology landscape
[ Read the latest Tech Radar ](https://www.thoughtworks.com/en-th/radar)