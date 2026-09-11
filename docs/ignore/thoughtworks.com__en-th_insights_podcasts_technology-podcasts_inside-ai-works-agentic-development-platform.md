<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/inside-ai-works-agentic-development-platform | Title: Inside AI/works™: An agentic development platform | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Inside AI/works™: An agentic development platform 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rickey Zachary | Podcast guest  Bharani Subramaniam and Shodhan Sheth
February 19, 2026 | 40 min 05 sec 
Listen on these platforms
## Brief summary
In January 2026, Thoughtworks launched AI/works™, an agentic development platform. It promises to make the capabilities of AI agents a reality for the enterprise, helping in areas including understanding complex legacy code, forward engineering new software solutions and agent governance. 
How, though, does it actually work in practice? And what does it mean for the organizations and teams Thoughtworks works with? 
In this episode of the Technology Podcast, new host Rickey Zachary is joined by Bharani Subramaniam (CTO for Thoughtworks India and the Middle East) and Shodhan Sheth (Head of Enterprise modernization, Platforms and Cloud) to discuss AI/works™, taking in how the platform emerged from a number of recent Thoughtworks projects to how it's delivering value to businesses today. 
As well as an inside perspective on Thoughtworks' new platform, the episode also offers a deep and timely exploration of questions and challenges the rapid rise of AI agents in software engineering has surfaced across every part across industry. 
**Learn more about[AI/works™](https://www.thoughtworks.com/ai/works).**
**Ken:** Hi everybody. Welcome to a special edition of The Thoughtworks Technology Podcast. It's going to be very, very short. What I'd like to do today is introduce you to a brand new host that's joining the technology podcast going forward. Very excited. Please meet Rickey Zachary. Rickey, why don't you introduce yourself to the listeners?
**Rickey Zachary:** Of course. Thanks, Ken. Hello, everyone. My name is Rickey Zachary. I've been at Thoughtworks for about five years. Right now, I'm the practice area lead for engineering platforms. I'm extremely excited to join the technology podcast, primarily because I think that it's going to give me an opportunity to not only grow myself, but also share some of the learnings that I've had, share experiences, and be able to bring a unique perspective about what we're doing with our clients to the listeners on the podcast.
**Ken:** Great. Well, we're really excited to have you. Really looking forward to what you do, and the listeners won't have to wait long, because that's it for me, and on to Rickey's first episode.
[Intro music]
**Rickey:** Welcome to The Thoughtworks Technology Podcast. I'm the host for today, Rickey Zachary. I'm here with Bharani and Shodhan. I'll let them introduce themselves. Bharani?
**Bharani Subramaniam:** Hey, thanks, Rickey. Bharani Subramaniam, CTO of India and Middle East. I've been with Thoughtworks for 16 years now. Happy to be here.
**Shodhan:** Thanks as well, Rickey. This is Shodhan. I lead our modernization services, and I've been in Thoughtworks a little bit more than Bharani, beat him by two years.
**Rickey:** Awesome. We're here today talking about our recently launched AI/works platform. We're working with clients all of the time, what would you say was one of the biggest signals that said we should probably be doing a lot more investment in AI and taking a more platform-based approach? Bharani, what have you been seeing?
**Bharani:** I think I can trace it back to one of our clients in India where a significant number of Thoughtworkers, 30,40 people, we've been building things for this client. We were having some early success, but the entire work would get piled up in one lane-- Like, it's not tested, or it's tested, but we can't put it to production because it's stuck for, let's say port to be open and things like that. The first spark of, "We need a platform to do this better," came from this fact that we can build things faster with AI, but there is still a number of things to be solved in the path for production. That's where the whole platform thinking approach came, is that we need a platform to solve all these problems or address all these problems in a systemic way. That was the first spark, at least for me.
**Rickey:** Shodhan, what have you been seeing?
**Shodhan:** I think Thoughtworks customers have always asked us how to repeat the outcomes that we have achieved outside of Thoughtworks, right? And I think we've always talked about our approaches and frameworks, and written about them, we've written lots of books about it. What was not there was codifying our approach into a platform to achieve better repeatability. I think customers have always asked us that question, and I think for me, that tipping point was when we saw some promise in a technology that could help us codify that, the special source of Thoughtworks into a platform to achieve the same outcomes, and repeatable outcomes.
**Rickey:** Interesting. Yes, I also see a lot of customers wanting repeatable outcomes at enterprise-wide scale. We're all on the team actively building the AI/works platform, we all have different components that we're working on, and we're building them on the platform. Bharani, I know you're working on a piece of the platform. Explain what the AI/works platform is from your positioning, and give a broader detail about what the AI/works platform is.
**Bharani:** Sure. I'm going to take a step back, if that's okay. One other pattern that I observed, and others also observed, is that there are a lot of things that we do in production: for example, for the sake of security, performance, and monitoring. Because building with AI has introduced a bunch of tools, we need to start monitoring for cost in development. We need to start monitoring for leak of data during things are being built, not just when they are in production. That was another shift for me.
The reason why I started with that is, the significant part of the work I do with the team is building that layer that gives you a common gateway for tokens, like API Gateway, or AI Gateway in this case. So that there is one place where we can say, as an outermost layer, can we ensure safety so that everything on top of the platform gets that as the lowest? I say that as the lowest common denominator because security is like layers of onion. You should have many many layers as possible, but this is the layer that actually protects the weakest link on the ecosystem. I would say the big part of the platform is how we handle security via guardrails and give visibility of what's happening in the system through a central observability, so those are the two big parts.
There's also a third element of the platform, which is actually governance. A lot of us react differently to this word, governance, but the clients, if you talk to the chief security officers, they love this, because there needs to be a way for them to prove that this person using this model has done this. We need that for the lineage as well, so the third part of the platform that I work on is, how do you govern this whole thing? Be it cost via limits of spend, or be it observability, or data, where you can query what this team did on this day that resulted in this software. It's not to say that it has to be intrusive. The whole aim is to give these choices to people to build software in a way that's more safer and traceable.
**Rickey:** Shodhan, I know you're focused on the legacy modernization portion. Where does your component fit into the AI/works platform, and what do you think about the larger platform and how the components you're working on it fit in?
**Shodhan:** I guess for me, AI/works is more-- Like, for a client, it's engineering that makes AI/works. I guess we had this sort of insight early on, and it's still true, that just by itself, generative AI is not the answer. There's sound engineering around generative AI, like the control plane that Bharani was talking about, but for every company, it takes sound engineering to make it less hallucinative, to make it more reliable, to make it more faithful. For me, the reason we as Thoughtworks are building this platform is to put that engineering rigor around AI to make-- to have the best of both worlds. We want the rigor that we've learned from the last 20, 30 years, but we also want the benefits of AI. For me, that's what I think about AI/works.
As you said, I guess, as part of my job, I focus a lot on legacy modernization. I guess we started with a simple thesis initially, which I'm sure a lot of you will relate to, that with legacy systems, whether you want to modernize them, or even keep the lights on, or replace them with COTS product, I think what you need is insight into what that system is doing. If you don't have the knowledge about what that system is doing, any of these parts are going to be difficult for you, but modernization is probably going to be the most difficult part. Even keeping the lights on is going to be cumulatively and consistently expensive.
This is a hard problem to solve because, again, another characteristic, or another set of characteristics of legacy systems is that documentation is generally stale, and the SMEs who knew it are either absent or no longer there, or they're very few, and they form central points of failure. And generally, there's no sort of automated test, that's something that, as modern engineers, we rely a lot on. Again, with that thesis of like, we need to solve the problem of insight into your system as the first thing, irrespective of the path you want to take, that's the component that we started building out, and that's now part of the AI/works platform.
**Rickey:** Awesome. I know that there's other components that are there as well. As a follow-up, we talk a lot internally about this idea of code-to-spec and then spec-to-code. How do you think, Bharani, the platform is enabling that workflow to be operationalized at scale, both with the safeguards that you mentioned, but maybe also-- I think that one model is better for enabling one of those workflows versus another model, how does some of that interconnectivity work within the platform that we've been seeing?
**Bharani:** This is interesting, because in theory, you can jump from-- I have this old system on my left side, I will reverse engineer, and then on the right side is my to-be system. But in practice, it's really hard to do that, because you can't just go from A to B, or you can't go from A to C without going through B. The most important part that the platform plays in bridging the gap is what we call a context library. In some sense, I keep saying that-- A lot of people ask me this question, how is AI/works different from any other platform that is out there? In terms of technology, I feel it's very difficult to have a differentiation, because in a way, AI is leveling the field, not just for us, but for everyone. But what I feel is very unique is this history that Shodhan was talking about, and we call it the hive mind internally. Like, how have the teams across the world and Thoughtworks solved these similar problems in the past, which could, I would say, enrich the information that we are seeing for this particular client?
Rather than just be the plumbing to connect the reverse and forward engineering, I think the role the platform plays is, how can we channel this collective knowledge that we have built over time as a relevant context? And this is easier said than done. The mechanics of how to give the context, I think is a solved problem. What is not solved is, how do you create it? We have these 20 years of history in the company, it's not that every problem that we have solved is relevant for the current problem, so we have, I would say, two challenges. How do you curate and keep it relevant, and how do you know it's relevant for this problem? I think I would say we play-- when I say "we," the runtime platform of AI/works, plays a significant part in giving those capabilities so that the forward engineering can orchestrate which piece to which is relevant, which is not relevant, and then they can go ahead from there. I think that is the most critical part.
**Rickey:** Agreed. Yes, I agree with that, mainly because in working with both of you all, what I'm seeing is that that's necessary to make sure that we have interconnectedness between the flow. I know that there's been a lot of debate in the industry about what is the actual system of record for that flow. Is it the spec? Is it the code? We're not here to parse that out, but I think that by providing that context at the relevant points within the flow, I think it's important, because then you can have interconnectedness and you can treat the spec and the code as first-class citizens there.
Shodhan, we both share a similar background in doing some legacy modernizations there. What do you think-- For supporting some of the legacy modernizations, you talked about discoverability. What do you think are some of the key tools within the AI/works platform that help accelerate that discoverability? Because I know I've been on COBOL program modernization programs in the past, and it's very difficult. We normally bring in a ton of people that have deep expertise in COBOL. What do you think are some of the tools that are helping us to accelerate that understanding for people that may just know Java or may know another language and don't have deep expertise in COBOL?
**Shodhan:** I guess from a solution perspective, again, our starting thesis was, you don't have SMEs, you don't have documentation, you don't have tests, but you have a gold mine in terms of structured data as code. We always believed in this adage, code is data. I say it's a gold mine because, A, it's structured, and B, it is the most accurate reflection of what's happening in your organization. Documentation can be wrong, diagrams can be wrong, but the code accurately reflects, because that's what's happening in production, so we start from there. If the code is your most accurate representation of what's happening, how can we use generative AI to use that structured data as the source of truth, but be able to project that data in ways that help both humans and machines move forward in their modernization journey?
I guess for me, the combination of human and machine is important there, because at least right now, we believe this is a platform enabling services solution. It's not a solution where you have a product, you click a button, and boom, you get a modernized output at the end of it. We focused a lot on how to use that code and project it in various forms so that humans can start understanding what's going on in their system, and as we've been talking about, produce specifications that machines can use to forward-generate a newer form of that same behavior.
I guess in our journey in building specifications for humans, we've realized that we need to build it in different formats. Humans love to start with high levels of abstraction, and then keep zooming in into areas of interest. If we only took a strictly textual specification approach to this, any 10,000 lines of code would be about 10,000 lines of specification of English language, right? It's not a human-scale problem anymore, so we need to provide summaries and abstractions so that humans can understand it, and for them to be able to interrogate those answers in more and more detail wherever they want it. I guess that is the main goal of the component that we were talking about in terms of discoverability, which is being able to provide specifications in different formats for both humans and machines.
**Rickey:** I'm going to follow up on that because I'm working on a product modernization with a client right now, and the ultimate conclusion of that-- You know, we start with the specification, we start with the code as the data, but a lot of times when we're modernizing, we want to also optimize both product user journeys, the capabilities that are there. What are some of the techniques that we're using from a capabilities standpoint to help to understand what the scope of the system is and those types of things so that we can more accurately forward-engineer a new product that's going to meet client needs?
**Shodhan:** I guess we-- I mean, two other techniques to throw in that we've always been fans of is, A, incremental modernization, so it's not a one-off, and B, that the unit value of modernization is greater when you bring some change in it. Those changes, as you described, could be things like, I want to change the behavior in my to-be system, or I want to compact some things that are not useful to me anymore. Those changes could be of different forms, but the unit value of modernization increases the more changes you make.
We allow for humans, or we assist humans to make these changes via two forms of specifications. One form of specification that we build out is a capability map, so that gives you sort of a town plan view of a large system. One way we've seen designers use that specification is to take build vs. buy decisions. By giving the humans this sort of projection of large systems where they can take different decisions for different capabilities is something that they've not had. Previously, that exercise would have been a couple of weeks, or even more, locked in a room with a bunch of SMEs doing that. That's one example to do it.
The other way that specification can also be used is to figure out your increments, as I talked about. Large systems are not currently-- you cannot replicate their behavior in a second or whatever, is the right sort of time duration to use. You have to do it incrementally, but that needs the problem of, what is an increment to be solved? Again, humans have this experience to do this and can do it, but again, we're trying to use technology to solve.
The other type of specification that we've started building more recently right now is to borrow from the event storming techniques, which again, we would love to sort of go into the room and draw out for large systems, because that'll quickly give you an idea of the business process that's happening. So, X command acted on Y aggregate and resulted in A event, and that triggered more things. Again, using our base knowledge graph that we build out, we project an event storm map of the system, and again, you could use it in a few different ways. A, it goes back to that primary hypothesis, it gives you more knowledge about what your system is doing in a human-understandable way. B, as the designer of the to-be system, it gives you a canvas to make decisions around your to-be system.
**Bharani:** I was going to add that I think there's a lot of confusion when we say spec, what is the spec? I was going to ask Shodhan, in your mind — The last two things that you said, to me, they are like projections or dimensions to understand what is already there, and I would personally not call that spec.
**Shodhan:** I think it's about how loose and tight you want to be with the word, so I agree. Like, at one level, you could say they are specifying the system at a level of abstraction for humans to understand. At another level, you could say because they're not-- Specifications have a mathematical connotation, because they're not exact, they're not specifications, but you're right. My natural instinct is to not call them specification.
**Bharani:** The reason why I think it's important to give that distinction is, a lot of people think a spec is similar to what was there when they were doing Waterfall, and this is not that. Maybe we need to invent a new term. Another confusion, maybe it's worth spending one more minute on this, is what I find most confusing with spec is we write what needs to be done, as in the functionality, and also how it has to be implemented in the same document. To me, it is confusing because they are two different things, not just now, but they are also two different things that happen at two different times. Like, I want this piece of functionality maybe that is also evolving, but could be slowly evolving, as opposed to how that has to be implemented, we might have to iterate that five times faster than what is required. That's why I feel we are now ill-equipped to call everything a spec. We need a new term, and maybe we need something more structured. That's another problem that I have with spec, is what is the structure?
**Rickey:** There isn't. GitHub has one, Amazon has one, there's a bunch of these companies generating these, there's not a standard specification for it. There's not a standard specification for the specification. [Chuckles]
**Bharani:** Yes.
**Rickey:** Bharani, you mentioned something earlier in the conversation that I want to revisit, when we were talking about this idea of platform governance. I do a lot of platform engineering, that's the majority of the work that I do with business and engineering platforms. One of the things that has come up time and time again as organizations shift from these individual tool decisions, what that journey looks like is, "Hey, we're an enterprise, and we went out and bought a bunch of GitHub Copilot licenses," rightly so. Then I want to turn the corner from that and make my AI investment worth it at enterprise-wide scale while still balancing the governance, and the controls, and a lot of those things. How have you seen the idea of the AI/works platform evolve from kind of point-to-point solutions being implemented by enterprises, to now us trying to provide clients with enterprise-wide business value while still maintaining the security posture there?
**Bharani:** Yes, I think this is very interesting, and we bump into this every time. We can have our own opinions, but when we go into a client ecosystem, like you said-- Hey, I don't have LiteLLM, I have a Kong AI Gateway. I don't have Copilot, I have Claude. Or, I don't have Claude, I have Copilot. I think these things come up all the time. That's why when we thought of the architecture, it's more of, these are the components that are required, but you can swap out anything and everything. For example, let's say they have strong guardrails already set up in the enterprise, we can hook into that. If they are an AWS shop and they are already using Bedrock, we can use the Bedrock all right.
I think we are very flexible from that aspect. Like, we're not tied to a provider or an implementation, but the fact that we need to have a central place where we can control for governance is the mandatory thing. Other parts are very fluid, and we're also discovering-- Like, a bank would need much stricter guardrails than, say a retailer, for example. Moreover, different parts of the platform-- Let's say if you're building something very sensitive, for example, you're dealing with pins and debit card pins, maybe you have to be compliant for PCI DSS even at build time, so that's a different thing, so we need to provision and segment part of the platform for a certain subset of use cases. We've seen flavors of this, and it'll always be very reactive, but we've talked through to some extent to have flexibility in the implementation.
**Rickey:** Another follow-up about what's in the control plane, what's in the platform. A lot of our clients are constantly struggling right now with the actual proving the value of their AI investment. How are we instrumenting the data around the SDLC to help them prove the value of not only the AI investment, but just using the AI/works platform?
**Bharani:** You had to ask this question--
[Laughter]
**Bharani:** Yes, this is a great question. Let's be honest, we-- When I say we, the whole industry is struggling and will struggle to articulate productivity and measuring and metrics because they are inherently hard things to solve, not that we don't want to solve it. The response from my perspective for this is that whatever toolsets that you're currently using without AI or with AI, I think keep continuing to do that, because otherwise, if your baseline is different, we would be happy with the productivity gain, but that won't be reflecting reality. Like, say if you're using DORA metrics before using AI tools, continue using it after so there is a common frame of reference. Or if you're using something like Flow metrics, continue to do that.
From the AI/works platform perspective, we are flexible, and this is the part that we are still actively building. One option is we will integrate with Apache DevTools. That way, we can tap into the ecosystem of tooling that's already been integrated. We don't want to reinvent everything for every client, so that is one approach, but this is something we want to test and learn as we go ahead.
**Rickey:** Agreed. I asked that because I know that we're thinking about that quite a bit. Shodhan, I wanted to also follow up with a technical question. You mentioned this word, ingestion of the code. The code is the data, and we're ingesting the code. Why are we ingesting the code? What kind of value do you think that that provides? Because I have a lot of clients that come to me and say, "I could just give the code to a Claude Opus 4.0 or 4.5, or a Gemini 3, and it'll summarize the code." What do you think is the value-add of that ingestion portion that we're doing, and why do you think it's so valuable?
**Shodhan:** I would say I think there are probably two answers in there. One is scale. I think most of these tools can probably do a pretty good job at 10,000 lines of code or that sort of scale about, but we work with a lot of large legacy systems, and large could mean hundreds and thousands, could mean millions, could mean tens of millions. At that scale, these tools just don't work, partly because of their context window limits. And as other people have mentioned before, it's not just a context window limit problem. One of the well-known tricks of working with LLMs is to give it the right context. The example I always use is it's like an open book exam. If you know where the answer is, great, you found it. If you don't know where the answer is, the book doesn't help, right? If you just give LLMs a lot of context, they're going to struggle and actually hallucinate even more than you would expect, so we built this solution to be able to scale to large code bases.
Then I guess also, the other projections we talked about, like the event storming map and the capability map, these are things that are build-on layers of the base ingestion that we've done. We've done some benchmarks with these other tools that are out there, and the amount of detail and faithfulness with which they can represent that information is much more lacking. So, I would say primarily, scale, but secondly, you need more than things like "explain me this code," which I agree is a solved problem, and you probably don't need things like our platform to help you explain the code. But when you start going beyond that, especially in the areas I work, "Help me find an increment, help me figure out how do I change the business process of this whilst I want to modernize," I think that's where you need, as I was saying, engineered solutions that can marry the benefits of generative AI and the benefits of all the hard-learned lessons that we've had for the last 20 years.
**Rickey:** Yes, that's a great answer. I'm going to use that in my next conversation.
**Shodhan:** With me?
**Rickey:** No. Bharani, one more follow-up question about the metrics, not as hard as the last one. One of the things that I think I'm personally fatigued on is this idea of the productivity metrics. We've been talking about productivity metrics for the greater part of four or five years, and AI has only accelerated that, but from a platform within the AI/works platform, I know we talk a lot about interconnectedness of the workflows. I think I liken them to the idea of AI-powered and enabled golden paths. Do you think that the platform enables shifting some of the feedback loops to the left a bit more for some of the developers, and what are some of the techniques that you're seeing us explore and build into the platforms to solve that problem?
I ask that because I think that that is an answer to the productivity question, which is-- well, we're going to get AI operationalized at scale into the hands of developers sooner, and we'll worry about the larger productivity metrics, the hours saved as a byproduct of that, and be able to reduce toil and cognitive load. That question about, what are some of those techniques to help shift left? What do you think we're thinking about in the platform around that?
**Bharani:** I think this is great-- I'll add to what Shodhan said earlier, AI is good, generative is great, but it's only going to be as good as the input that you give to it. One of the rules of the platform is, what other richer forms of input we can feed into the developers so that at that time that they build the software, it is well-informed. A concrete example could be that, I am building this critical part of the journey of the product. This is not an auxiliary feature, I have to be very careful. This change, what is the impact on the performance going to be? When I'm touching that part of the system, what's the current P99 latency that I have access to? Without a platform, you have to juggle around three or four systems to get that. One of the goals of the platform is, how can we give that context to the developer?
It is not going to be easy, because what we are talking is we need to take telemetry from production and give it to a developer when they want it. There is a lot of security approaches to be corrected, but if you are only using AI to do the same thing that you used to do, just better, faster, that's not going to be enough. We should be enabled to do things that are different, which was otherwise not possible. AI could be an enabler, or a platform could be an enabler. That's the role of AI/works, is that, how can we enrich not just the stories and features and context of the solution, but other things that are happening in the production ecosystem back to the development?
**Rickey:** Go ahead, Shodhan.
**Shodhan:** I guess I want to add something to this as well. I think there's over-obsession with how much gain in productivity, like, "Oh, can you achieve a 60% productivity gain, or a 70% productivity gain?" Whereas in reality, the focus just needs to be on improvement, because this is like the-- My financial education started pretty late, so I learned this pretty late. Like, compound interest is cumulative, so when you start making improvements, they accumulate over time. That's more important than obsessing about a target of improvement that you want to hit. That target will come, but the more important thing, and that's where the whole feedback loop and all those practices reinforce, is that as long as you constantly, consistently, continuously keep improving, you'll get to the best place that's possible.
**Rickey:** Yes, I think that's a great response. I really like that.
**Shodhan:** You're not going to use it?
**Rickey:** No, not that one.
[Laughter]
I think the other part of that conversation which triggered in my head is that a lot of the AI tools and the platforms that are external to Thoughtworks are really focusing in on the developer. However, there's an opportunity for the use of AI to-- I think one of the terms is 'democratize engineering.' How do you see the work that we're doing on the AI/works platform even shift further left and make the SDLC more of a PDLC? I was having a conversation about UML, that was a language that we used to talk to each other as developers. Do you think now that-- We were talking about words, do you think now there's the need for a new concept or a new word that talks about this language that we're going to use to talk within the platform between product managers and owners, developers, SREs? Or will the spec, as we've been saying kind of loosely, is that going to answer that question within the platform?
**Bharani:** I think this is the deepest question so far. I say that because, yes, spec is going to be the vehicle that carries that information across the stages of SDLC, but we almost took our workflow for granted for a long time. I think that workflow is changing, because good or bad, the granularity of work is changing. I think we had Agile, and we still have Agile, and it is meant to have a quick feedback loop with certain constraints in mind, because we couldn't iterate at and build things at capability-level before, but you could do now.
The best part of Agile is it keeps evolving. The question now is, what is this Agile agentic workflow that we should have on the platform or encourage people to follow that path on the platform? It could be as simple as-- We used to promote pairing within the same discipline before, like a dev and a dev pairing. I think we should promote a lot more of a product owner and a dev pairing, a dev and a QA pairing, or even a QA and a product owner pairing. This interdisciplinary pairing is almost a mandatory thing right now, because a spec won't be complete if it is not complete from all the dimensions.
In some sense, we are shrinking the time, which is putting a lot of constraint on what a spec is, but the shrinking-- In one dimension, we are shrinking the time, in another dimension, we are increasing the unit of work, so we can't pretend that the way we build is not going to change. Do we have all the answers on AI/works? I'm sure we don't, but we are experimenting. This interdisciplinary pairing, we have seen it work very well in a few instances, with or without the platform, so we want to definitely codify that as much as we can in the platform so that-- you used the word, like it's a paved path. It's a paved path so that it's easy if you follow this path, it doesn't mean this is the only way to do it. That's how I see it.
**Rickey:** I'm going to ask one final question just to kind of close this out. Again, we're all working on the platform, what is one feature in you all's respective areas that you think, "Hey, that's going to be something that I'm really looking forward to, really exciting to experiment with and bring to our clients"?
**Bharani:** For me, how we can use the new ways of working, but still not forget software is still a social activity. We still need to build evolutionary things. I mean, you can't go from 0 to 100, right? So, it is going to be small incremental evolution, but that-- What was a small unit of work could be a large unit of work, but it has to be iterative and evolutionary. I think that's one thing I'm excited. It is very hard to do that in the platform, but it is also the challenge that I'm ready to take on.
**Rickey:** Shodhan?
**Shodhan:** Yes, good question. I guess, again, sort of focusing into my area of work, modernization, there's this translation required from what your as-is system is to your to-be system. So far, most of our work has been focused on, how do we unravel the business logic of your as-is system? Now, we started focusing on a different persona, the designer of your to-be system. So, what tools, what vehicles do we give them so that when they see more of the as-is system, they can take meaningful, intentional decisions that help them change and build a better to-be system that's more fit for purpose for themselves? I think we just started on that journey, and I think this is an important persona to address. Modernization is almost incomplete without that, so that's the thing I'm most excited about.
**Rickey:** Great. Thank you all for joining The Thoughtworks Technology Podcast. I appreciate having you all join me.
**Shodhan:** Thank you.
**Rickey:** If you want to learn more about AI/works, you can go to the thoughtworks.com website. We have a landing page there where we have video demos, and we've got a ton of different content to explore.
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
## Check out the latest edition of the Technology Radar
[ Explore now ](https://www.thoughtworks.com/radar)