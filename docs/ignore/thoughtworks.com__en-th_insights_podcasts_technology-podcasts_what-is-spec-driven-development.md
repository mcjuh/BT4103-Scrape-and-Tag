<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/what-is-spec-driven-development | Title: What is spec-driven development? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  What is spec-driven development? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Birgitta Böckeler | Podcast guest  Laura Tacho
May 28, 2026 | 45 min 39 sec 
Listen on these platforms
## Brief summary
Semantic diffusion, combined with the pace of technology change, makes talking about AI-adjacent practices and techniques incredibly diffficult. There are few better examples of this issue than the term 'spec-driven development'. Although it's not new — its coinage precedes our current AI moment — it has become ubiquitous over the last six months or so as software professionals attempt to develop a vocabulary for talking about how they're developing methods for working successfully with coding agents.
On this episode of the Technology Podcast, Birgitta Böckeler is joined by Laura Tacho — Developer Experience at AWS — to discuss all things spec-driven development. From competing definitions to different interpretations, implementations and workflows, the discussion provides a frank and grounded look at one of the most discussed and debated terms in modern software engineering.
  * Learn more about Laura's work by [visiting her website](https://lauratacho.com/)
  * Read Birgitta's article on spec-driven development on [Martin Fowler's website](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
  * Find out more about the [Future of Software Development Retreat](https://www.thoughtworks.com/about-us/events/the-future-of-software-development) mentioned on this episode.


**Birgitta Böckeler:** Hello, everybody, and welcome to the Thoughtworks Technology Podcast. My name is Birgitta Böckeler. I'm a distinguished engineer at Thoughtworks and a regular, sometimes host, sometimes guest on this podcast. Today it's just me and one other person that I'll have a conversation with. I'm very happy to have Laura Tacho here today to talk to me about spec-driven development. Laura is the former CTO of DX and recently joined AWS as a senior principal technologist. Hi, Laura. Thanks for taking time to talk to me.
**Laura Tacho:** Hello. Very nice that we've been talking about doing a podcast for a couple of years now, and it's finally worked out. I'm glad to be here.
**Birgitta:** We'll have a conversation today about spec-driven development. [Chuckles] I have a bit of history with that topic because when it first started getting traction was around September, October last year, and I wrote up my observations of what I was seeing. That memo on Martin Fowler's website actually still, to this day, eight months later, gets a lot of traffic.
I actually personally have been staying a little bit on the sideline since then for several reasons that we can maybe talk about, but let's start with definitions maybe, and then get into a conversation of where we think this is eight months after it started gaining traction. What is spec-driven development in your perspective, Laura?
**Laura:** I'm so glad that you asked this question because what I observe from the companies that I work with is that there are lots of different practices that people all call spec-driven development. It's really like a wide array, and there's not a lot of standardization. When I think about spec-driven development, a couple of things have to be true. I define spec-driven development as a framework or a workflow for creating well-defined specs as part of the planning process before coding begins, and then that spec is an artifact that then is handed off to, typically, an agent to complete.
I think we can get into a question of if the agent is a requirement as well, if spec-driven development only applies to AI, augmented engineering or not. Maybe a conversation for a different time. Spec-driven development is a workflow that allows teams to get very clear about user requirements, plan it, create an artifact, and then use an agent for the actual implementation.
**Birgitta:** Usually, also, you use the agent to do the planning to all of that, right?
**Laura:** Yes. I think that's where we get into some very sophisticated workflows. This isn't just writing a really, really good prompt. This is actually using your agentic AI tools to facilitate the authoring of a very, very well-documented spec that has a lot of edge cases, test cases, very comprehensive, and so that agent understands it has everything that it needs to go build something. How does that differ or align with your definition of what a spec is?
**Birgitta:** The word "spec" is still super fuzzy. Sometimes it's just a more elaborate prompt. Sometimes it's 50 markdown files. Sometimes it's just 10 markdown files. It's also a difference between what it is in reality in the, let's say, frameworks that call themselves SDD frameworks, spec-driven development frameworks, and what people are talking about when they talk to each other, or what the ideas are in people's heads that maybe haven't tried it yet.
For example, there's this blurring of the lines between functional specification and the specification of the technical solution. There's some people, I think, especially people more removed from the actual hands-on development work, who sometimes have this idea in their head, "It's just about describing the functionality. That's something I can do as a non-technical person," and then AI just creates it. Whereas a lot of these frameworks also facilitate this whole solutioning process.
If you just leave it to AI, if you're being too unspecific, it can be as variable as AI decides to introduce a persistence layer with a database versus AI does not decide to do that. It's an extreme example, but it has actually happened to me. That's still very fuzzy. Of course, there's some people who say, "Oh, the only properly detailed spec is a test. Don't we already have executable specs." That's, of course, a different, let's say, bounded context, maybe almost, than spec-driven development. We, as a mass of people, have now decided to use that term for it in this bounded context, of these frameworks that you described.
**Laura:** I think a lot of times when I discuss spec-driven development with developers and also with engineering leaders, they're often also describing greenfield projects. That's a very different flavor of spec-driven development when you don't have an existing codebase to contribute to versus spec-driven development for a brownfield project. I don't love that word, "brownfield," but of existing services and systems where, to your point, the technical specification is really critical because there's existing architecture that needs to be considered in your spec and in the development of whatever feature is being attached to or changed within that system.
There's a lot of different styles which would all really fall under spec-driven development because I think SDD, spec-driven development, is more describing the behavior of having a workflow and then an artifact with specifications, unless something that we could throw a linter at and say, "Yes, that's spec-driven development," or, "No, that's not, that doesn't pass the linter." I don't know if we'll ever get to that point.
We're describing similar, if we think about what we have now, test-driven development, behavior-driven development. All of those things are describing patterns that developers and teams use in order to develop in a very certain and specific way, but it's still a little bit fuzzy around the edges. We're letting people self-identify into spec-driven development right now, and that just leads to a lot of drift and a lot of fuzziness in the name.
**Birgitta:** I think the key here really is, for me, not a fuzzy spec. It's the workflow part. It's that these tools that call themselves SDD tools, they walk you through a workflow. As you already just said, and I totally agree with that, there is not one workflow for everything that we do. Brownfield, greenfield is one example. Is it a bug or is it a new feature? Is it a small feature? Is it a big feature?
As developers as well, we don't work the same way all the time. What I see in some organizations now is they see these frameworks, and they ask us as consultants, "How do we scale this?" One of the things in their head is we just have to figure out one of these tools or come up with our own workflow, and then every developer will use it, and then we're good, and then everybody has to use this. Again, it depends a little bit on the situation.
In terms of the workflows, also when you look across the space at all the different tools, they always have a very similar flow, and then just the details of the implementation are different. How well they support different types of feature sizes, feature types, and so on is different, but it's always some form of discover and plan, designer solution, implement. This is very simplified. Some of them have six or seven steps. Some of them just have three steps. Usually it's optional for you as a developer which one you choose. Ultimately, I think it's about the workflows. That's much more at the core of it than this spec thing.
**Laura:** I think this is a nice time just to pause and hold that thought for everyone about not getting too hung up on the specific tool or on implementation details but more focusing on the workflow and the process of spec-driven development and having that be the goal of going through the process of discover and plan, implement, evaluate, those kinds of workflows, versus just thinking, "Oh, if I just start to use this tool that I know does spec-driven development, then all of a sudden I'm going to be able to use it."
It's not as simple as that. It's a behavior change and it's a process change, so we can't ignore the human aspect or the team aspect of this as well, where a tool isn't going to solve necessarily all of the problems, even if a tool can really help support teams get better at their planning process. Again, going back to what we talked about before; use AI to plan and to write the specs. These aren't something that developers are just authoring by hand or even business stakeholders are authoring by hand. It's all happening in the same development ecosystem.
**Birgitta:** That's also one of the questions I had in my write-up from October, and a question that I still have, and I think we still, as a profession, haven't figured out, which is, who is the target audience for this, or who is the target user? They seem to be targeted as developers, mostly, right now, because they're usually built into the coding agents in the form of skills and stuff like that.
Even though I do know lots of stories at this point of also product managers using Claude Code and losing their fear of using a terminal for that and all of that, it's still very much catered to developers. I hear a lot of stories of developers then doing this discovery phase of the workflow or figuring out the details of the story or the feature and then going right into implementation where I'm still wondering-- it's not quite explicit with the authors of these workflows as well.
They could be saying, "This is the future. Developers will also be the product managers or developers will also figure out the functional details of the story," or they could explicitly say, "The goal here is for a requirements analyst to use a more old-fashioned word and a developer to pair on these first phases, and then the developers continues." It's somehow not quite clear. I mostly see people using these by themselves as developers, which I just think is going to be a problem at some point in terms of the alignment.
**Laura:** Could not agree more. Could not agree with you more. I think one thing that I've been talking about, it now feels like forever, but it's only been 18 months. It's hard. I sometimes think Claude Code wasn't even GA at this time last year. It feels like this has always just been the world. I think you and I work in this world a lot. One of the things that I've been sharing with engineering leaders for the last three years is that if we want organizational lift, so increased productivity from your product development teams, essentially, we're looking to actually influence revenue.
We're trying to build better stuff for our customers and end users. We're not going to get that just from engineering alone. To your point about-- we've got spectrum and development workflows oftentimes really built into the IDE where developers are spending their time. Well, it's not a job that only developers can do.
Developers can flex into what a lot of companies are now calling product engineers or even I've heard the term AI-native engineers, multidisciplinary engineers, Renaissance engineers. Renaissance developers is another one. They can flex into that, but there are all these people on the business that have incredible expertise in figuring out exactly people that are field-facing product managers. They have the knowledge and expertise about what needs to be built and scoping that down. It's very important to get those people into the venue where SDD is happening, which means that they also need to be using the same tools that developers are using.
We see this start to happen. One of the last things that I did before I left DX was a impact report looking at AI trends. Justin Reock, who's the deputy CTO, has picked that workstream up and published the second version of it to give updated data now a quarter later. One of the things that we started to see was the proportion of product managers and designers using tools like Claude Code or Kiro or Codex was just increasing. It has, I think, steadily increased. Also, the number of engineering managers who use AI tools like agentic IDEs and then also looking at their PR count is an interesting indication of people are just getting a little bit closer to the code.
In order for spectrum and development, I think, to have the organizational impact that it can have, we really need multidisciplinary teams sitting at the table and in the same workspace working together. I don't think that really any of the organizational problems that we're trying to solve with agentic AI can be solved by engineers alone. We can build a lot of tools, but it's not a single-threaded solution.
**Birgitta:** Part of it is a tooling question, of course. There's still so much potential of how we can evolve these tools. I know there's a project at GitHub Next right now. I forgot the name, unfortunately, where they're also trying to create a collaboration thing where all the artifacts and all the conversations are in one place about a feature to improve that collaboration. Maybe making the interface more intuitive for somebody who usually doesn't deal with the code.
Of course, it is super powerful if a person who lives and breathes the product and the requirements and knows all the stakeholders and knows all of that space, if they can use a tool that also knows the code base without them having to understand what the code does. I was using one of these workflow tools the other day, and I was going through a discovery phase with it. It was actually making really good suggestions or pointing out gaps in my rough input that I had given it that were based on it reading the code base. That's actually super powerful that these people now don't have to go to a developer all the time and ask them, like, "How do we do this again? What is it really like in the code?"
Part of this is a tooling question, and there's still so much potential, I think. The other one is, like you said, organizationally. I still think software delivery is still a team sport and will still stay a team sport. Just having one silo where we create more and more code throughput and then have another silo where we create more and more requirements by different people, that won't work-
**Laura:** Doesn't help. [Chuckles]
**Birgitta:** -just in terms of flow and theory of constraints, all of that type of stuff, but then also deciding that developers will just do it all, that's also not a solution. There's this thing where everybody seems to think that they will be able to do it all, and the other people will be out of a job, and not the other way around. Maybe product managers who can now actually access the code, maybe they will come out on top. It's not a zero-sum game. That's, I guess, what I'm trying to say.
**Laura:** I think that's a great way to think about it, is that software development is still a team sport. Now we really have tried to solve this alignment problem for a long time. I remember posting something on LinkedIn probably over a year ago where I said, "You know what? The thing I find most interesting about," we were still calling it AI-assisted development, I think at that point, now we can call it agentic development, is that it's actually forcing teams to really look at the requirements and the intended outcome for the user before starting to build something.
We've really tried to do that in software engineering for a really long time. We've got tons of tools out there to try to document user requirements, user stories. We've got all these different methodologies and workflows and practices to take a big requirement and break it down into small things and make it digestible. I've seen all sorts of stuff, as I'm sure you have. Everyone who's listening out there, I'm sure you've seen a wide variety of good practices and bad practices when it comes to requirements, completeness, and how things are broken down in your ticketing system.
I look at spec-driven development and I think, "Oh, this is us trying to solve the alignment problem still again," but maybe it's going to stick this time. Maybe these workflows and practices, because we are actually keeping the thread the same, we're keeping a thread between the spec and the implementation. I should say that I hope that's still true because, as you said, right now, we've got teams using AI to come up with the spec and then going into implementation, and there's not a put-down or a handoff of that work.
To your point, what you just said about what will happen if spec-driven development morphs into something where it's just a team over here writing a bunch of specs and then a team over here who's implementing a bunch of specs. I think that doesn't actually solve the alignment process, and then we lose what spec-driven development has enabled us-- why it's enabled us to move faster is because it is start to finish, and we have one loop, and we're not just creating a backlog of specs and then a backlog of implementation.
I am worried that that practice is just, it's too tempting to do that because it's really close to how a lot of the teams work right now. I would say, going back to that very definition of spec-driven development, I would say that if you're doing that, that is not spec-driven development. Maybe through this conversation, I've identified one more of my qualifiers for how I would define spec-driven development versus not is that it has to stay in the same loop and there's no handover or handoff or backlog of specs. A spec should never end up in a backlog.
**Birgitta:** Maybe we just need different words at some point. We just published an episode on harness engineering that I actually also wrote up, tried to come up with definitions. I feel like, "Oh, we need three more words at least, and I hope that we'll develop some of those." In terms of the handoffs, I think there seem to be two things happening at the same time right now. One is all that's old is new again in a positive sense.
As somebody who's worked with extreme programming practices for a long time and worked in environments where it was really agile by principle and not agile as a methodology, I see some of these things and I go like, "Interesting." For example, everybody says now, "Oh, it's the--" Product engineer is now a trendy term, and it means the developer has to care about the product. I was like, "We used to just call that an agile developer. That was the whole point." That's in the sense of what's old is new again.
It's interesting to see some people finally embrace some of these things because there's additional incentives. The systems that they were in before, it wasn't worth doing some of these things because of how things around them were set up. Then at the same time, there's the negative side of what's old might be new again. I assume you're also of a similar generation as me, so you have worked in some waterfall environments before.
I think it's not even worth arguing with waterfall these days because the vast majority of developers these days haven't even worked in what-- they don't even know what that means so they haven't experienced the pain that led to some of the things. Because a lot of stuff in waterfall feels very intuitive, it's a lot about control. If only we just think really hard about the requirements first, and then everything will be good at the end.
A lot of the stuff that came with agile is counterintuitive. It goes counter our need for certainty, our need for control. I think it's very easy now with these things to fall back into that and actually sit there for two days for one feature and just work with the agent to get the spec just right so that then in one perfect, beautiful go, it can create the perfect code. It's also then on people who have experienced that to suss out what are the things here that we shouldn't fall back into, but what are also new opportunities where circumstances have actually changed and we can look at how we can leverage AI to do things even differently than we were doing six, seven years ago.
**Laura:** What's old is new again. I said the physics of great software haven't changed, which is that it has to be software that's reliable, completed quickly with high quality that solves a customer problem. That hasn't changed. Also, things like having short feedback loops being very beneficial to both developers and the business, that hasn't changed either.
I think that it is really tempting with spec-driven development to get back into that, like, "Okay, now I'm in planning and I have to plan every little thing," and looking at the process and thinking like, "Oh, how do I iterate on the spec? Is that allowed?" That's a real question that I've gotten. How much planning is enough planning? How much planning is too much planning for a spec?
I think this is where we have to learn from the past and understand that we don't want to go back to full waterfall where we're just lke, "Because it's so easy, now we can just generate arbitrarily large change sets at the drop of a hat," assuming you've got enough tokens. It's still not a good practice to do that. Even if we can do it and we can do it much easier, it's still not a good practice to do that. It's still a good practice to start small, to iterate.
A lot of those agile principles are still true. Then it's also true that bigger changes carry more risk. Even with the additional quality checks and monitoring and observability that we can do with agents and predictions and all these things, smaller change sets carry less risk. The fewer bits that you move back and forth, the better. We have to be really careful.
I think that's one thing that I've seen a lot of developers and engineering leaders struggle with spec-driven development, is just trying to get the balance right between how much planning is the right amount without going over, but also not going under where we're just putting something into prod where no one really understands how it's working or it's not well-tested and those kinds of things.
**Birgitta:** Somebody reminded me last week when I was talking about this as well, like, "How can we still have short feedback loops?" and how they were saying, "It's all about learning. How can we learn new information? How can we gather more data as soon as possible?" Ultimately, that's also about reducing waste. If you build a spec in the sense of my, I don'tknow, 25 markdown files that do the planning, I have all of that.
Then finally, we do the implementation and we just need a two-second look at the website or something, and we see, "Oh, I hadn't thought about that." That's why we had these smaller iterations previously. I agree with you. It's something that we still struggle with with these frameworks. I think some of them do it better than others.
We just talked a bit about the past, looking at some of the more extreme futures that people are painting in the context of spec-driven development. In my write-up, I called it "spec a source." This idea that in the future, will we have specs, whatever a spec is in the future, exactly, some kind of specs where we edit the spec when we want to change something and we never even touch the code anymore, but the spec becomes the source? What is your view on this vision?
**Laura:** I remember, so Birgitta, we were both at the Future of Software Development Summit back in February. Some people might have a party to celebrate the 25 years since the Agile Manifesto. We all thought it would probably be a better idea to just go in a couple of rooms and think really hard about heart problems and actually come out with close to no answers but a lot more questions. It was a really great event.
We had one session about spec-driven development and other what's the artifact, and I raised my hand and said something to the extent of, "When we're thinking about the future and thinking about what we're committing, it might not be source code. It might be the spec; it might be context. What is going to be that permanent artifact where we can rewind time and go back to that point in time?"
Someone in that session had a comical, funny reaction where that person raised their hands and said, "Oh my goodness, but source code, it is the source of truth," but that led into a conversation of like, "What if it doesn't have to be anymore? What if we can always get to working software from a spec and actually it doesn't matter how it works to a certain point?" I think that framing is something I think about a lot when I think about what should be committed, how should specs evolve alongside the code that they're responsible for, that they've informed? There's quite a few different techniques to do it.
Birgitta, you wrote about this in your memo. We've got the spec that evolves next to the source code. We've got the spec that is frozen moment in time, and then we have different artifacts that inform the changes. Maybe it would actually be helpful if you wanted to give a quick breakdown of the different ways that you've seen teams operate with spec-driven development, because I'd love to talk to you about then what the future might look like in terms of are we committing source code or not?
**Birgitta:** Again, this goes back to me thinking, oh, we need more terminology. I just came up with three new terms at the time. The first one, spec first. That's what I see most people do at the moment, I think. It's like a mix. You create the description of the feature that you're currently working on, and then you throw most of it out again. Some people keep it in the repository as history for the agent, but it's kind of like, like you said, frozen in time, and it's archived or deleted.
Then the second level is spec anchored, where maybe you have an area of the feature in your codebase that you describe, and then every time you work on a change of that feature, you go again through the spec and have then the agent derive the changes from the spec. You try to keep the spec and the code consistent with each other, which is a challenge in itself. It might be a little bit easier with AI, but it's still like when you have lots of artifacts lying around, there might be a lot of overhead.
Then that last one is the spec outsource that I described before. This vision of just editing something other than code. The thing is, again, we don't know what that means, spec. The question would be, if we think about what would that spec look like, that it's this idea of a raised abstraction level, I guess. A new raised abstraction level. When you think about what would we want that spec to look like, then you have to think about what do we want to achieve with this. Do we want more people to be able to maintain software? Do we want fewer people to be able to make software?
More people in the citizen developer sense, like different skill profiles, and then fewer people, it's just much more effective. You just change this thing and it magically happens because people see creating the code and all of that as a tedious thing that you want to outsource. That's one of the things because then when you think that through and you're like, "What would that form of spec have to look like?"
I actually, at the beginning of my career, a long time ago, I worked for a while on two projects even for quite a while, or three, doing model-driven development. This idea that you create some kind of model of your functionality of your software, either we started out with a UML stereotype, like UML-based language, and then later went to a textual, a DSL language, actually, to describe our screens, for example. Like, "Here are the different fields that we have. Here's a button. When you click that button, the following thing happens."
I went through the experience of working on that DSL and the code generators for it, and just constantly we had to expand this language. It was like a formal language, so it really had to be parsable, so it really had to describe everything. With language models, of course, we have a lot more flexibility about how we describe things. I just went through that experience realizing how many things there are to consider, like which fields are editable based on who's logged in, which fields are not. There was constantly these things we had to add to it.
I think everybody who's used these tools has had the experience that you write something like, "This is the functionality I want," and you forget a detail, like a default value, a what is the format of this customer number? Every time you generate it, AI makes a different assumption about the format of the customer number and the regex you need to validate it. Not just like my anecdotal experience just now from model-driven development. We know historically that we are not good at writing down in a lot of detail what we want. The way that we write down in detail what we want is the code right now.
The question is, chasing this spec that we can edit alongside code, will we get to the point where we're like, "Oh, now it's just code," or, "Now it's just tests, executable specifications." That's my hang-up that I have with this, maybe influenced by this history as well. Ultimately, what spec can we get to that actually gives us meaningful added value on top of writing the code?
**Laura:** I do agree with a lot of what you said. When I was at DX, and you can find this in some of their public research, documentation is consistently, even now, the top pain point for developers, lack of great documentation. Spec-driven development, we ask the question, does this solve the alignment problem between the business and engineering? Maybe it can help solve some of it.
One of the other questions I think about is, does this solve documentation? What we're proposing is this documentation that evolves at the same time as the code evolves, and they're always in sync because they have to be in sync? I think about everything old is new again, but everything old is new again. We've struggled with documentation for decades. It's a huge problem.
What I think that spec-driven development does is it changes the incentive structure. In the past, developers writing really good documentation didn't benefit them immediately. It benefited maybe them in the future when they had to come back to it, or it benefits some ambiguous other developer that's onboarding onto their team. It's not that we're not nice people, and we don't want to help those people, but there's no immediate gratification.
What spec-driven development does is it changes the gratification to almost immediate where if your spec gets out of sync with your code, then anything you try to build on top of it is going to be wrong and requires more rework. The developers and systems that developers build-- because I also don't imagine a future where if I say, "Hey, this bug exists, go fix it," and an agent fixes it, that I would say, "As part of fixing it, go update the spec," as well. It's not that I'm going in there and updating it.
We've created now a much more enticing incentive for teams to keep their code self-documented through the spec and to keep the spec up-to-date. I think it's that behavior change that I think it's a good thing, and I think that helps these spec-driven development workflows take root.
One question I have a lot about what we commit as the artifact is source code changing does commit. We can see change, but it doesn't really capture intent. I think that the intent is captured really well in the spec. Maybe now we just have a centralized place for that intent to be captured, which is in the spec. Whereas before it was in an email, in a Slack message, in a Jira ticket, in Linear, in whatever. Now we just have one central place for it that's easy to search. I think that's overall a good thing.
Time will tell because if it's not benefiting developers and they're feeling stress or pressure to deliver more quickly and don't have time to build systems around keeping those things in sync, then they also lose incentive to keep doing it. I think these next 6 to 12 months are going to be really interesting with how teams are evolving alongside spec-driven development evolving as well.
**Birgitta:** The documentation connection is interesting to me because what you just said about what if the spec is just the place where we have the intent in one place. That sounds like what we have been telling ourselves about documentation since the age of time. If only you put it in the right place in Confluence, and then it's only in one place. We know that never happens. There's always duplication. I'm always about with wikis and all of that.
Of course, you want to try and keep a little bit of structure, but then you also have to embrace the chaos, and you need a good search function and all of that. What AI gives us now is also that the persistent documentation is not as important anymore because we can get on-the-fly documentation. I can ask it like, "Look this up in the codebase. What's happening there?" or create a sequence diagram for me, which I would never persist anywhere because they get outdated too quickly so it's not worth the effort. Now I can actually get a sequence diagram in the moment when I want that type of visualization.
There's these tools out there that create a knowledge graph of not only your codebases, but your wiki, some of your Slack conversations, all of your tickets, and so on. The promise of some of them is that that actually does help you discover the intent based on all the connections in the knowledge graph between this piece of the code and everything else. There's some of this on-the-fly thing.
Then the other thing with documentation is, yes, it's now actually a lot easier to keep track of a lot of decision records, for example. Another one of those things that finally more people are doing. There's more decision records. The question is also, yes, do we just do a check, check, check? We now have decision record files in the repo. We now have these things documented, those things documented.
Yes, probably it's a good thing because it helps the agents. That's why we're doing it. That's a new incentive to make it easier for us to use the agents and get better results. Does it really help us is the question. I usually get overwhelmed by all of these files that these workflow tools generate. Then you actually, through the process, you go and you review these markdown files, which usually I would be reviewing the code maybe, but now I'm reviewing these markdown files, and they're very long.
You hear everybody say, "Oh, yes, you have to read what it says because if early in the workflow process, you miss a wrong assumption or something like that, it will go all the way through." I'm like, "Are you really, really reading all of these markdown files that get generated? I just can't believe it."
There's this experience thing as well, this finding the balance between having a lot of stuff that the agent can actually use and that we also have documentation about what it decided in the past and almost this memory for the future agent. How do you actually make it human-consumable as well? Is that the new review experience? I don't know. It doesn't really excite me that much or it doesn't make me that confident either.
**Laura:** One of the things that we talked about heavily at the Future of Software retreat was, is this stuff for humans at all, and should we be fine with the fact that we're creating a lot of artifacts that a human is actually never going to interact with? Are they still valuable? How do we know that they're bringing value and not just creating more garbage and more stuff to maintain?
I think that's the concern that I have is that maybe we solve the documentation problem and we solve this problem of centralizing requirements, intent, and user outcomes in one place, but the maintenance problem of keeping it all up-to-date and all pointed in the right places is still a really hard thing. That's a place that I have seen some examples of teams that are doing it well, but not so many. It's not been productized or commoditized quite yet.
I think that will be an area of rapid innovation and research and new thinking as teams adopt a spec-driven development and then have to build out all the peripheral workflows and systems and products that are going to support that workflow. We'll see. I think it's going to be, like I said before, a really interesting 6 to 12 months with these teams that are really going hard with spec-driven development and finding a way for it to work for them.
**Birgitta:** That's good wrap-up question for both of us. The term "spec-driven development" is about eight months old now. Where do you think this will be in eight months, Laura? [Laughs]
**Laura:** It's so hard to predict because I see such a wide range of organizations in their adoption journey. I see some organizations that have small teams that are multidisciplinary, that are using spec-driven development with, let's say, a product manager, a designer, and a couple engineers, and then shipping that stuff to production environments, user-facing environments, and doing it safely, reliably, easy to maintain, all those things.
I also see organizations who are still struggling to get users to use code complete in an IDE. We've just got such a wide spectrum. I think for spec-driven development, first and foremost, I think that this is a technique for professional software teams and for teams who are trying to produce software. I think that's a really important distinction. This isn't a technique that I'm going to use for my-- well, maybe actually, it is. It's not a personal prototype. I'm probably not going to use spec-driven development. I'll probably vibe code that. I'm just going to give a prompt with natural language and see what happens. That's not what spec-driven development is.
I think as more teams mature and start using this professionally, we're going to see the gaps of what is the answer? Should specs evolve next to the code? Should they be throwaway? I've seen a lot of interesting things like modernization projects where we can actually generate a spec just based on observed behavior of the software and then generate a spec and then generate new technology. I think there's going to be a lot of different use cases aside from just teams using spec-driven development to ship software to their end users.
I'm definitely excited. It's a workflow that I've seen have an incredible positive impact. I think that the on-ramp is challenging. I hope that in the next eight months, we'll see easier ways for organizations to give their engineers, their software development teams, their product managers, their designers, their developers, the skills that they need, and the time and the space to start practicing it if they want to. That's what I hope will happen. What about you?
**Birgitta:** For me, it's like one — let's get maybe a negative prediction out of the way for us! — a backlash against markdown files. Maybe it's already happening. Maybe fewer markdown files, or maybe it's more in this way of just acknowledging, looking ourselves into the eyes, as we say in German, [laughs] and say, "Look, we are not reading these markdown files. Let's just be honest about it. They are useful for the agent. How are we going to deal with that?"
I'm also interested to see how all of these markdown files and also these new things that are happening with keeping agent traces with commits and stuff like that, if it will lead to an overload of agents and lots of inconsistencies and lots of weird behavior because they're picking up the wrong context from somewhere because there's just too much. That is maybe the concern I have.
In terms of the more positive thing, it would be what we talked about before about how are we going to bridge the gap between people on a team to have all of these things that are in these workflows right now but actually make it a lot easier for everybody to work on that and have different projections on what's happening, and, like I said, make it much easier for product managers, requirements analysts to actually have tools that have access to the code so that they have additional information. How can we actually use this to get people to talk to each other still or keep them talking to each other and not just each of them in their little cubicle talk to their agent? That would be an evolution that I would like to see in the space.
**Laura:** I think over the next eight months, this idea of the shared organizational intelligence layer, the shared context layer, org-wide, is going to be a huge area with a lot of development and innovation and a lot of different solutions coming out because software development is a team sport, but if we have a Team A that's doing something really well on part of their service and Team B over here also using spec-driven development doing things, how can we better facilitate sharing of workflow skills, things that are going to help them both benefit? I think that's one area where I'm seeing a lot of cool progress. I'm interested to see what that will bring as well.
**Birgitta:** Maybe then in eight months, we have to talk again, Laura. [Laughs]
**Laura:** Yes. We should schedule it now because we have a history of wanting to talk on a podcast and then life gets in the way. Yes, eight months, we'll come back and see if-
**Birgitta:** Exactly. There's so much going on.
**Laura:** -any of our predictions were accurate or where we were wrong and where we were right.
**Birgitta:** Thank you so much, Laura, for joining me for this. This was really good to reflect back on where we are and where this is going. Thank you all for listening and see you on another episode of the Thoughtworks Technology Podcast.
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
## Explore a snapshot of today's tech landscape
[ Read Technology Radar ](https://www.thoughtworks.com/en-th/radar)
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