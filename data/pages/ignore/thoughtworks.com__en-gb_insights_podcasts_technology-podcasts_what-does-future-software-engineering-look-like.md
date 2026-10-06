<!-- Source: https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-does-future-software-engineering-look-like | Title: What does the future of software engineering look like? | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  What does the future of software engineering look like? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts)
Close


Podcast host  Ken Mugrage | Podcast guest  Kief Morris and Andrew Harmel-Law
July 09, 2026 | 46 min 25 sec 
Listen on these platforms
## Brief summary
At the end of June, Thoughtworks and Martin Fowler convened an unconference-style event in Switzerland with a range of industry leaders. The aim was to reflect on the current challenges and learning around AI assisted and agentic software engineering and discuss the implications for the future — and, most importantly, what actions need to be taken today.
To review the event and dive into some of the topics that surfaced, host Ken Mugrage is joined by Thoughtworks colleagues Kief Morris (author of _[Infrastructure as Code](https://www.thoughtworks.com/insights/books/infrastructure-as-code-3rd-ed)_) and Andrew Harmel-Law (author of _[Facilitating Software Architecture](https://www.thoughtworks.com/insights/books/facilitating-software-architecture)_). They highlight some of the key ideas and issues that emerged from the event's conversations, ranging from developer identity to harness engineering.
**Learn more about the European edition of the[Future of Software Engineering Retreat](https://www.thoughtworks.com/about-us/events/the-future-of-software-development-europe-2026).**
**Read Andrew's recent blog post that asks whether[non-functional requirements could be a vital guardrail for AI-generated code](https://www.thoughtworks.com/insights/blog/architecture/non-functional-requirements-missing-guardrail-ai-generated-code)**
**Ken Mugrage:** Hello, everybody, and welcome to another edition of the Thoughtworks Technology Podcast. My name is Ken Mugrage, and I'm very honored to be met with a couple of our Thoughtworkers from our UK offices. I'll let them introduce themselves. Andrew, do you want to go first?
**Andrew Harmel-Law:** Yes. Hi, Ken. Thanks for having me. I'm Andrew Harmel-Law. I'm a tech director, like you said, based out of the London office.
**Ken:** Great. Kief?
**Kief Morris:** I'm Kief Morris, distinguished engineer, wrote the book Infrastructure as Code, so I'm largely known as that. Also based out of the London office.
**Ken:** Part of the reasons that we have two of our folks from the European office is that Thoughtworks recently hosted an event in Europe last week around the future of software engineering. We were really privileged to meet with, gosh, I guess about 80 folks from really around the world, but mostly from Europe, that are real leaders talking about the future of software engineering.
Now, it's easy for me to say that, leaders, but I will have to let you know right up front that we did run the event under what's called the Chatham House Rule, which that rule states that we cannot use the names of any participants or their organizations. This gives people the ability to speak freely, without worries about misquoted, to give their personal opinions, and so forth. It's really important to an open discussion. I encourage you to check it out. It does make it a little hard because we're going to tell you that these were knowledgeable people, and you can either believe us or not. [chuckles]
We did a similar event a few months ago, and it was interesting. I was privileged to be able to go to both. Just a couple observations, and then we'll get into some things. First off, it was observed by somebody else that in the previous event, which was in the United States, it was very much about, "Oh, look at this cool shiny stuff." It was this year, so these things were not brand new, but there was still a lot of, "Oh, we think this might work and this might work," and so forth.
In this event, it was a little bit more practical of, "We know this can work, but we need to answer these questions." Part of that is cultural between two different areas, of course. Part of that is just a different group of people. It's probably some observation bias, if I'm honest. Some interesting takeaways to get into here. First off, and I know this is audio only, but you're listening to three White [chuckles] people with gray hair. Kief has less gray hair than Andrew and I, who've been around a while. We heard people calling you 30-year-old COBOL legendary code. [laughs] It's like, "Give me a little bit of a break here."
Anyhow. It's interesting how fast things are moving. I guess first off, just, if you don't mind, I'll go to each one of you and get some of your impressions overall of the event. Any major takeaways. We'll go through some individual questions, but I'd just like to get your gut feel. I've started with Andrew before, so Kief, I'll start with you.
**Kief:** That comment was interesting. I did talk to a few other people like yourself who were at the event in February. I wonder if part of that difference also was the timing because February was the point where there had been the new models dropped in December. That point has been identified as a turning point where suddenly the models got really good at coding, and it became a lot less about trying to, I don't know, squeeze something usable out of them and a lot more of, "Oh, now it's producing stuff." I think that was fresh.
That was what? Five, six months ago. Now we've been doing it for a while. I think now the kind of focus is on, "Oh, we've learned a lot about what challenges this creates, having models that can produce good code," but yet there are a lot of challenges in how they do that and how do we make them work the way we need to work, get the results we want to get. I feel like a lot of the conversation was focused around the challenges that we've discovered and are trying to figure out.
**Ken:** Andrew, your impressions?
**Andrew:** Plus one to everything that Kief said is definitely things that struck me was because now it seemed more inevitable this time that this stuff is useful and we can't pretend as software professionals that it isn't useful. Now, there were lots kind of themes, but one of the big ones that stood out to me was the fact that people were like, "Where do I sit in this whole thing now?"
We know the typing went away. There's less typing, but it's like, "How much do I still need to bring to the party?" A good phrasing that I heard was that, "How much do I need to trust this stuff?" Some people were like, "You should trust it completely." Other people were like, "You could build 17 different copies and then just see what they're all doing." Other people were like, "No, you need to look and inspect it and all this kind of stuff and be very, very careful about what it does."
Lots of discussions were about that, and then that fed back to another thing that's making me think a lot is we evolved ways of building and running and operating and evolving software in a world where we created the software by hand, effectively bespoke, and now other things are potentially doing that with us as partners, or maybe Dark Factory is got mentioned as well. Maybe we'll talk about that.
Now we're like, "Where do I sit in this? Which skills do I still have that sit in this? Where are the leverage points for me and all of this kind of stuff?" It wasn't scared, like, "None of us have jobs anymore." It was more like, "Where are we recalibrating?" That was loads of the conversation. Then you get specific conversations about this and that kind of stuff.
**Ken:** I was having a discussion at lunch with somebody, and he was saying, and this is a person that, again, had been around for a very long time, and was saying, "Where before I would try to describe six different ways of working, now I just do six prototypes." It was like, "Okay, but how big is that codebase, and what are you working on?" Doing six prototypes is one prompt maybe, but it's some number of tokens.
Then I asked the big question at the end, "How do you actually run them, or how do your customers run it?" I guess, Kief, we hear about AI for generating all these, and I'm just going to do seven different versions for user experience. How do I run this stuff? What does it do to the infrastructure's code calculus? I know there's not a clear differential between application and infrastructure, but where's that last mile come in?
**Kief:** We had two sessions that come to mind. I can't remember if you mentioned that. There was the open spaces session, so it was a lot of general discussion rather than people presenting. Two of the sessions around that that came to mind was, so one, we talked about path to production to pipelines and this kind of stuff, which to me was about how do we prove the software is production-ready?
I think that relates a lot to what are you using the software for? In a lot of cases, people are building software like, "Oh, I'm going to make a tool for myself to do a thing," and that's fine, or like, "Me and a couple of people on my team are going to use this thing," but when you're doing it with software that the company is going to use or that is your company product, it's a whole other level from knocking something up with a Replit or what have you, and "I've got this working software," to like, "This can scale to 1,000s, or 10,000s, or 100,000s of users and it's going to be secure and it's going to be stable and all those good things."
I think the kind of conversation we had in that one session was around how do we use the pipelines to make sure that our code is going to be ready to deploy. We talked a lot about where do we fit agents into the pipeline? How far do the agents get involved in what happens after you push to the pipeline, then automatically take the results of, say, a failed pipeline stage and then make corrections and push another build through and so on?
Some of the stuff we discussed in that session was around that gets expensive with the infrastructure as code. [laughs] You're deploying some AWS resources over and over, and the agents tend to thrash a lot on some of that stuff. That's something I don't think anybody seemed to have really solved.
**Ken:** I have a friend that works at Apple, and he said if he's doing Python or whatever, he'll use agents and doesn't even look at the code, but if he's using something like Swift or whatever, okay, wait a minute, they don't have as much training data. What's the maturity of some of these tools when it comes to running Terraform versus Java? We were talking about how much more effective they are in code. Is that true on infrastructure as code as well? Is there a big enough training set, or does that still require more oversight?
**Kief:** That's a good question. I don't think we talked in the sessions as much about that specifically, but my experience has been that the LLMs know a lot about infrastructure and they can talk about it a lot, but when it comes to building code, genarating infrastructure code, and then deploying it, they make a lot of silly mistakes. I don't think they're as strong, maybe, as they are with writing UI code. There's code that can be run and tested locally. I think that's why they thrash a lot more, is like, generate some code, and then they try to deploy it, it doesn't work, and so they go back and forth and like, "How does this actually work?" I think they've got a ways to come.
One of the things we did talk about was around using-- These things where there are shortcomings in how the agents handle stuff like we talked about in the path to production, we also talked about in operations and diagnosing runtime stuff and those sorts of things. That providing more forward kind of guidance, like skills and so on that are a bit more directive to like, "Here's how to do this," may be necessary to get better results in those cases.
**Ken:** When you take skills, are you talking about specifically like-
**Kief:** I'm talking about age and skills.
**Ken:** So that it's the person's ability.
**Kief:** Like the markdown, where you say-- Well, I think there's a combination. We talked as well in sessions overall about harnesses and all this kind of stuff. As Andrew mentioned, the trust, how do you get the trust to code? A lot of the conversation was around what are good ways to do that. Skills, as in the markdown files that you give to agents to say, "Here's how to carry out a task." The agent's MD, cloud MD, and specifications is one thing, but that actually tools, like scriptable tools that are executed and do particular tasks in a predictable way, are a bit of a stronger. There's levels of strength of assurance that you're getting these things to do things in the way that they should.
**Ken:** The loaded question that I don't really expect an answer for, are agents members of our teams? I guess, Andrew, you talk a lot about team structure. Conway's Law and myself are about the same age, I hate to admit. Where does that come into play? If Conway's law, if our code-- I'll let you tell people first. What is Conway's law?
**Andrew:** Conway's law is that the communication structure of your organization, your software will follow the communication structure, not the org structure, but the communication structure of your organization. Generally, this whole thing it's like if you have numerous teams and they communicate in certain ways, then you'll see that kind of-- It's like if you have three teams building a compiler, then you'll get a three-pass compiler.
**Ken:** What's that look like when it's one human and 73 agents?
**Andrew:** I was paying really close attention to this because, as people might know, I'm a TDD nerd and I love bounded context. There were sessions about modularity, and modularity never really worked. It's not like modularity was clean before agents got involved and now it's getting all messed up. There were sessions about that, and like is this an opportunity to maybe make things better? I've been doing experiments that I talked about a little bit in a few sessions. I've been trying to figure out how much of domain driven design agents know and stuff.
Then meanwhile everyone just seems to be-- Like Kief said, we're coming out of the phase where we've all realized this. The agents and the LLMs can do some very interesting stuff and stuff that we didn't think they could do. A lot of people were just throwing requirements at them and then generating code and stuff. As long as you didn't look at it too closely, it did functionally what it was supposed to do. Maybe non-functionally the edges were a little bit blurred. We weren't so much worrying about the structure.
The things I've seen, and I heard of this from a few other people as well, is because agents can roam around anyway and they're very sycophantic, they want to do what you've asked them to do and make you happy. If you want them to do that while still discovering and evolving and protecting some boundaries in a codebase, they highly possibly will not respect that. Even if you start with something clear, the edges can get blurred very fast, and you might have to wait and then tell them to unblur, and then they'll get blurred again.
Lots of discussions we were having was like, is it time to go back to individual microservices in separate repos purely because one agent, you can say, "You can access this repo, but you can't access this repo"? To Kief's point about different levels of firmness that you can put in things, because sometimes you need to be quite firm and quite predictable. Like, "This agent can't change this because it has no rights to change this codebase in this repo."
This again was another conversation that spilled over into the hallways afterwards. If the boundaries were easy and obvious to find in the first place, we'd be good at it, but we're not good at it because these boundaries are quite difficult to find, and then they evolve over time. If it was easy, there wouldn't be the entire blue book of domain design from Eric Evans.
All of this kind of stuff, it feels like, to me anyway, that there's another layer, like what Conway is saying. Somewhere on the interface between teams and the software that they build, where we're encoding this explicitly maybe into our agents' forms or agent pools or whatever, and the teams that are controlling them to get this kind of architecture and maybe inverse Conway or whatever it's called to hopefully drive these things in a sensible direction, but at the moment there's a lot of people been like Kief said, everyone is been building a lot of stuff.
**Ken:** For either one of you, what do you think about this concept? One of the things that came with the sessions was giving people-- and I use this term because this is a term that was used in this session. I personally am not a fan of using this applied to agents, but they said they gave their agents personalities in that this agent is a cynic and this one is an optimist and this one, what have you. What do you think about that overall concept? Should agents have different ways of looking at the problem?
**Andrew:** I've got a psychology degree, so human beings, we're very good at anthropomorphizing stuff. It already worries me how much we're anthropomorphizing stuff. I wouldn't give them personalities. You could give them hats. There's the Edward de Bono Black Hat, Green Hat. I've been messing around with different agents being different domain experts.
You'd want a domain expert to be like, "This boundary context is mine. Therefore, I understand it. I'm going to watch out for other agents straying into my ubiquitous language," et cetera, et cetera. I think that makes sense. I would worry about, like you said, the terminology. You could see people, me included, we'd say things like reasoning, and then we'd be like, "Well," or we'd be backing away from some of the potentially not entirely proven language about some of the powers of what the LLMs can do.
**Kief:** I'm really uncomfortable with anthropomorphizing for a number of reasons. Obviously, there's the psychological things that people get into. There's also just that whole idea when you have the business leaders talking about, "I'm going to have agents rather than people and all that." That's just wrong in a number of ways. I think it's practically wrong, even if you're want to be cynical and focused on, I don't know, the bottom line or what have you. I still think it's not a good framing, a helpful framing.
I had an interesting conversation, and this was like a follow-up afterwards where I was talking with a couple of people from the conference, and one of them was talking about, like, "Oh, I want to make more use of agents. My eyes have been opened a bit to what people are doing with these teams of agents and all that." They were talking about, "Oh, I have a BA agent and a QA agent," and so on.
I was reflecting that I started doing that at one point, and that was useful almost I would say like training wheels as a way to get started with agents, but where I quickly came to-- In a lot of the sessions, we had a lot of talks about workflows and those kind of things. I think where it comes down to for me is it's like thinking about those workflows and which parts do you want to hand off to an LLM to carry out, and then what are the handovers between the humans?
Whether it's a prompt or whatever, I'm going to indicate to an agent, "I want you to do this." Then the agent comes back and says, "I've done this." Then I have a look. Am I happy? How do I feed it back, and so on, but it's very task-oriented. I think that's a more useful framing as we think about what tasks you need to get done and what are the agents doing.
Having an agent where you've scoped it and saying like, "This is the task that you're going to carry out. Here are skills and tools for you to use," and I think attitude in terms of, you might want something that is, say, "Okay, take an adversarial approach, a skeptical approach." Sure. I think you can do that in a way that's pragmatic without anthropomorphizing it.
**Ken:** A lot came up in sessions I was in about the platform teams. I doubt very many of our listeners have seen me speak, but when I do, I rant about DevOps team and how it shouldn't exist and that sort of thing. Is a platform team just infrastructure? I air quote for "just infrastructure." Who owns the harness, the organizational knowledge, that kind of stuff? Any thoughts on those either one of you?
**Kief:** You touched on it, Ken. It's like, this is the conversation we've been having for a long time about once you get past having a single team that's building software, daily running software, once you get through it, you get to multiple teams, a lot of stuff going on, how do you share? How do you cooperate, collaborate? It's always a tough balance, because you can say, "Oh, okay, we're not going to have platform change. Every team is going to do their own thing," and then you get a lot of divergence and not much alignment. Then I can potentially have a lot of friction from teams doing things in very different ways.
I've seen one organization where they were having an e-commerce flow. They divided up their teams like different parts of the e-commerce flow. You said one did the search, one did the product catalog, one did the shopping basket, one did the checkout. They're all each doing things like their own tech stack. Even the UI uses different JavaScript frameworks across each of these. It's like, okay. Clearly we need some level [chuckles] of coordination and collaboration and also learning. I think especially right now because we're still learning how to do this, and I think there's opportunities for us to share and learn.
We're talking about things like harnesses. How do you build a good harness? None of us knows. Rather than everybody trying to build their own thing, what can we do? All of that with that trade-off, then if you have a separate team that says, "We're going to own that and you're going to use what we create for you," that tends not to work out very well. I'll leave it there and pass on the baton.
**Ken:** Andrew, you've spoken a lot about decision-making authority. Where does that fall in this?
**Andrew:** Exactly. I think the decision-making thing and who gets to decide-- famously, I forgot to mention my book at the start because I need more training on that. My book is about facilitating software architecture and, fundamentally, decentralizing decision-making. I write this book, and then AI comes along, and basically decision-making has got hyperdecentralized to the extent that maybe a bunch of decisions are being made by machines that we didn't even intend to make decisions. There's that.
The other thing that came up a few times, which was super interesting to me was, and where platforms came up again, and I think non-functional requirements come into this as well as someone who tries to wear the architecture hat, what's new about this, one of the big things that's new about LLMs is the exec can vibe code stuff, and then they want to deploy it and run it. Kief mentioned this, alluded to this a little bit earlier.
Now, the empowered people, and you mentioned this a little bit, Ken, I think as well, there's more people who can write this stuff now. It was bad in the old days when everyone just YOLO'd things into production, but now, the variety of things that could be YOLO'd into prod could be even broader than ever, A, because it reduces things and reduces cost and makes things more predictable. That feels like a good target thing for platforms.
Also, if there are certain things, like if you're in a regulated environment, lots of attendees were, they're like, "There are certain things we just can't do. You need to be GDPR." Everyone needs to be GDPR compliant, but then, in certain industries, they need to have certain PCI compliance and stuff.
You could lecture people on it, or you could build a platform which goes, "If you use these things up to and including harnesses and skills and whatever, then we have blessed these because we think they won't just give you the functionality, you prompt the functionality, but we're pretty confident that they will give the non-functionals as well. We'll store it in a certain type of database. We'll not store certain types of data. We'll replicate it in some way." Then it strays into some of the conversations that Kief mentioned around about building these things is super easy, but running them might just got more complicated. Again, like operability, observability, and all this stuff. I think it's very interesting.
To go back to your question about decisions. I think the key thing now is lots of this it's in my book. People used to make decisions without even realizing it to begin with. Now a lot more people are making a lot more decisions that could be a lot more significant without thinking about it because it didn't confront them. I think surfacing that kind of stuff, to Kief's point, is like giving people tasks, maintaining responsibility for the decisions that you should be responsible for, et cetera, etcetera, I think it's going to become key.
I think a lot of that was surfacing in people's thinking. They're like, "I don't want to know every detail about every single thing that every agent is doing, but I do need to have control over the things which I'm responsible for, because I can't blame a robot," et cetera, et cetera. That might have come across as pessimism. I would classify it more as European realism than anything else. People were like, "This thing is definitely magical. Now, how do we harness the magic for the forces of good and not chaos?"
**Ken:** It's funny you use the word "control" in there. I am unashamed of the fact that I do use tools like Claude and that stuff to summarize, and summarize of, what? 40 different sessions for this discussion. One of the things that showed up there is a recurring "theater" of control critique. I guess, Kief, what are your thoughts there? Do we actually have control, or is it just theater?
**Kief:** It's really, really interesting. This came up in a couple of different contexts, this idea of how much autonomy do you give to the agents, how much do you just let them get on with something, and what do you have to check? It's a couple of the context. There's obviously the coding one, generates code. Do you have to inspect every line of code?
There are some people who are very much in the camp, "Yes, you do," and there are those in the camp where it's like, "Oh, you don't have to anymore as long as it gives you what you want." Then there's a whole bunch of questions around, "How do you validate that it gives you what you want?" which is where the harness stuff comes in, which is also talked about in the context of building knowledge graph.
There was one really interesting session where we talked about building a knowledge graph for your organization, your domain, and your business and making that available to agents in a RAG way to where it can draw the right information that it needs without having to fill its context with everything. How do you build that knowledge graph? Is that something that humans build? Actually, then we were talking about, "I can get agents to do it, but then how do you know that they're doing the right thing?" and so putting that onto it.
Then the third context was when we were talking about the operations, the day 2, what happens when you have stuff in production and can use yourself for troubleshooting. Again, there's a real divide between those who are like, "It's fine to use them. Use agents to gather information and present you with options, and so on," and even some people were a little bit uncomfortable with having it suggest, "Here's courses of actions you can take," because that might then bias you and you might not think about other courses of action. You might trust that too much.
Then the people who are like, "Oh, just let it go ahead and fix things." All right. That was just really, really interesting. Do we have control? I think a lot of this comes down to, did we ever have control? Ken, when you were talking about what's just surfaced and looking across the sessions, I think a number of times the whole thing of pull requests was brought up around where you have people out there saying, "Oh, you have to have pull requests to manage your agents because otherwise you can't."
It's like you can't catch all the things that they might do wrong. It's like, "Are pull requests ever a guaranteed way to catch that a human is doing something wrong in the code, much less an agent, or is that just theater?" Has always been just theater. That was a really interesting observation.
**Ken:** Andrew, I'd ask you to do the same question because I know you have an interesting outlook on this.
**Andrew:** It's literally the first chapter of my book. I would argue we've always had a lot less control than we thought we did. My hypothesis, again, it's interesting. I'm not sure I agree with everything I wrote in the book now. I agree with most of the stuff around the book, but the framing of some stuff because I'm like, "Crikey, now I'm being confronted with even more anarchy than I thought I was advocating for."
We always had less than we thought. There's an Alberto Brandolini quote, which I love, which is one of the three things that informed the book. It was like, "It's not the design that goes into production; it's the developer's assumption." Now, the developer, the person who wrote the code, might be an LLM, and it'll have assumptions because it's a large language model. It knows a lot about a lot of stuff. That's interesting.
It was always probably impossible to guarantee that the diagram you had of your domain model on Confluence was the thing that was actually running in prod because we all knew it wasn't, but some people could kid themselves. Now it definitely isn't. Figuring out which bits we care about most, and which bits we think we need to intervene in, and which things we need to be-- Some other folks were like, and I think I agree with this, a crusade against word determinism, which seems to have caught on, but predictable, which things we need to be predictable, where we need to invest confidence.
**Kief:** Can I challenge something? You were just talking about the diagrams as an example of the architecture diagrams and Confluence. We know they're never up to date, and all that. Isn't there an opportunity now where it's like-- we're too lazy to update it, but can you just have the agents update the diagram and so it could actually be more up-to-date than it was before?
**Andrew:** That could be the level of engagement. This is the thing. This is why, literally, I'm still-- this is about beauty for open spaces, but then it takes six months to process everything. We totally could. Like you were saying, the knowledge graph, and basically, the bigger the knowledge engineering thing, I think that might be a term that we end up using more because we cannot have the knowledge.
Someone needs to be doing the thinking somewhere, maybe with a lot of assistance. Maybe we're devolving lots of details to other things, but that feels more important. How we go about it, I think, is not clear. I was in a session where we were like, "How much do we want to hold on to practices like test-room development?" Different people had different opinions. The reasons why we do TDD, for me at least, to break open the process of generating code into thinking about what it does, thinking about how it doesn't, thinking about the design of the implementation. Those three steps are still relevant, and we care about them more or less in certain degrees. All of this kind of stuff, pulling that to the right level, I think would be very interesting.
**Kief:** There's another point I wanted to capture on this, which is, a lot of these conversations we have about the control and what do you trust the LLM to do, what does a human have to monitor, and all that, I think one of the things that we fell into a lot was this idea of thinking that it's static. Like, the answer is this right now. Whereas, actually, in terms of the debugging and troubleshooting production systems, I think there's probably different classes of problems, where there are some things where it's like, "Okay, you could have the LLM."
Again, if you're not just having, say, Claude, look at the system, watch it, and fix anything that breaks, just do whatever you think you ought to do. More specifically, here's an alert for a specific thing that happens, trigger an action, that might be an LLM making some decisions on there because it requires a bit of flexibility and stuff that you can't predict as much ahead of time. There might be some very narrow-scope things you could do today and give it that latitude.
Then, over time, as we learn this stuff, the sort of stuff you were just talking about, Andrew, all the governance stuff and the information gathering, all that kind of stuff, we'll get better and better at that and be able to provide more focused and more confident. I think we'll increase our maturity as an industry in what we can trust the agent to handle autonomously.
**Andrew:** I tried to float this, but I don't think it stuck as a benefit, again, of open spaces. I think there's a concept of surprise. Again, my degree a long time ago was in cognitive psychology and stuff. Control is one thing. We can't be in all the right places to do control, but we want to control things more where we want to be surprised less. There might be some stuff where we don't care. If you've used one of 17 different JavaScript frameworks, but I don't care, then that's not very surprising because someone will use it. If I'm like, "This probably needs to meet these regulatory requirements," and if I find out that it is writing PII all over the logs, I'll be surprised and it'll be a bad thing.
I think that's something that LLMs can watch out for. Things like embodied systems, which we didn't really get onto because they're not LLMs, that's one thing that some models of that are tending towards. Watching the running systems and keeping an up-to-date mental model in some form or other, like a predictive model of what the system is doing and should be doing, and then looking for anomalies and all that kind of stuff, that feels like it's still way off, but it might not be as far off. I keep thinking this stuff is years away, and then it happens three days later.
**Ken:** I recorded a podcast some number of months ago with Nathan Harvey, who was not at this event, so I'm not breaking the Chatham House Rule. They were talking about AI amplifying whatever is there, whether it be good or bad. The example he used was the high school band that's maybe not very good. If you put an amplifier in front of them, you don't get good music, you just get louder bad music. I guess I would ask you, folks-- we've trusted untrusted sources before. There's ways to manage this. I'll start with Andrew, I guess. Stack overflows and things. Now, it's AI reading, not us. What are all your thoughts about the amplifying what we have?
**Andrew:** My take on this is that if we understood things were important and we did certain things consciously, then we probably understand that they're a big deal, and so therefore, important to us. I think if we didn't, we just followed the-- If we cargo culting, we might have looked like we were doing the same thing, but we just were cargo culting it. We were doing test-driven development because I ended up with a good test coverage, or I did test-driven development to think my way through a problem space. It might look very similar, like the type things on the screen, but the motivations might be different.
I think that you definitely could end off going off in those different directions. I think the intent is still a really big thing. What I do think, however, is, like Kief said, very smart people were saying, "I just give some really good prompts to some LLMs and then get 17 different versions of the system." It wasn't like if I know a lot about this practice, I'm going to be hyper-controlled, and if I don't, I'm going to YOLO stuff. That was the interesting dynamic to me. Some people were like, "This stuff--" I can suddenly benefit from multi-threading myself and doing all of these things.
Seeing how different people are relating them and their skills to the tools and the possibilities of all of these tools, I think it's still very much up in the air. I think lots of people are still trying to figure out this stuff. Things that did stick, however, seem to be no one debated like, "We move in smaller steps because it reduces risk." You want to save code to source control. At some point, you've got some kind of ground truth that you can come back to, et cetera, et cetera. You need to have observability on your systems and all these kind of things. You need to communicate and have appropriate knowledge boundaries and things, but other stuff seem to be very different people, like very different viewpoints from my perspective.
**Kief:** On the amplification thing, I think one of the things that tends to-- I felt it tends to expose if your team builds software and you've got those gaps or those things that, yes, we would feel like we should do TDD and have good unit test coverage or what have you, or have good unit tests, actually meaningful unit tests, but we don't. We're not really where we want to be with that. We have some kind of CI/CD-ish kind of stuff going on, but there's still manual steps or things that we have to fix up after it gets deployed or something breaks.
I think there's a lot of stuff that we used to get away with by just working around and all that. We didn't necessarily have to have, or many teams didn't have to have the really hardcore strong engineering habits and practices that they might have liked to have had because of the pressure to go fast and all that stuff. Now, AI spits out codes so fast, at a pace where it's just those things fall apart. You can't be constantly pumping things through a pipeline if it needs somebody to tidy up after every release.
There's a good example where someone talked about being worried that if you don't review every line of code, the agent might slip something in where in the development environment, it connects to the production database to work around something or what have you, or to get data. Gosh, that's why you need to have somebody review the code so it doesn't do that.
No, you need to have infrastructure and systems that don't allow something running in your development environment to connect to your production database. It's like, again, a lot of times we just get away with that stuff. We've gotten away with that kind of thing. Now, the people use the analogy of a plumbing system, where you're now pumping a lot more pressure into the pipes, and so things are going to start bursting here and there. I think for me, that's one of the kind of things that you see with that whole amplification that you get.
**Andrew:** Stuff that might have been working by accident because you just weren't going at a certain speed suddenly you are going at a certain speed, and you're like, "Oh, we don't know how to change gear. We're now trying to go 70 miles an hour in first gear." It turns out that the system doesn't like that.
**Kief:** Or the brakes don't work very well when you're going that fast, but they were fine when you were going 20.
**Andrew:** Yes, because you could break with your feet when it was going slow. Now, it turns out when you crash, it's a-- You have to go back to the NFRs thing. I think it just never fails to amaze me that the number of places I go where NFRs are implicit and stuff. I'm just like, "This stuff feels very important." Now I think more and more people are going to realize that at least thinking about certain key ones for whatever they are, whatever is key for your system, maybe I'm just being hopeful, but it feels like it's going to become bigger.
**Ken:** Are there any answers emerging?
**Andrew:** It's a good question. It would be interesting to me because now there feels like there's not a marketplace, but there's more like people are sharing agents and skills and stuff. Maybe, to the point Kief were making, like, how much do you care about the inside inner workings of your code? Maybe the old rising tide raises all boats. Maybe it just because lots more of this stuff is becoming downloadable from some skills database or something, then you can just drop it in, and then you'll be magically working in a world where everything works. I'm not sure. I'm skeptical when I say it out loud, but maybe.
**Kief:** I think we're going to have to get better at testing that stuff. That's one of the things we talk about harnesses and harnesses, and we talk about harnesses and harnesses. It's a thing. I think we're still not-- When it comes to skills and things like that, when I see some teams, there are a few people there I know who have really strong processes around using agents for the whole taking issues reported to an open source project and putting it through a pipeline to test and make sure it's okay, and they use skills for that.
They're using evals heavily on the skills. It's not just about bringing down stuff from the outside, especially those kind of agent things in marketplaces and whatnot. How do you have something rigorous in place to make sure it really does what you want, it doesn't have any kind of security implications, injection attacks, those sorts of things? I think this is something that, in terms of answers, I think one of this is like, it's just we're learning to up our game, and we have to continue to learn to up our game at this stuff.
**Andrew:** I used to work with someone who they were a delivery manager, and their measure of a healthy project was, number one, how much you'd hear teams talking to each other, and number two, what they were talking about. They could be talking about stuff which was panic-driven, so that was bad, or they could not be talking to each other. That was probably also bad as well if there was no communication. Some healthy level of seemingly important conversations between the important teams in the right way. I don't think that's going to go away. Maybe what they talk about is going to be different. You'd be like, "Why is no one worrying about PII or something?" or like you said, like separating production from development environments.
**Ken:** In terms of wrapping up, I want to ask you both the same question. Your answer, I'm just very curious because you are both very experienced in related but different places. Going forward, at least for the foreseeable future, which I think in today's day is about ten days, [laughs] but not being glib, in the foreseeable future, what survives and what changes? What have we been doing that we should keep doing? What do we need to start doing or stop doing?
**Andrew:** Again, I wrote about this in my reflections blog post. The things that I think are going to stay the same, but I think it will become more explicit, is the thinking about the system and all of the different levels and being conscious about the system and the structure of the system and what the system needs to do.
One of the big things I think that affected software architecture was product management came along and forced us to answer the question that Eric Evans asked. It's like, "What is the goal of the software?" It's not to scale Kubernetes in a horizontal way or have the appropriate number of Kafka brokers. It's understand this business problem and solve it. I think it'll, hopefully, focus the conversations on that and maybe on how it gets down to implementation. That feels more important now than ever, especially as we could be going faster, and we could be building lots more smaller pieces that talk to each other. I think that is really important.
What's going to go away? The thinking I think is so important. I think some of the practices that we've got used to help us think might change, but I think that doing them will still survive in some way. I'm expecting to see maybe even more collaborative modeling, for example. I'm expecting to see more awareness, like I said, of non-functional requirements, that kind of thing… I now sound like I'm wishfully thinking.
**Kief:** I think the focus is going to largely be on the slightly higher levels, the architectural kind of stuff, and the stuff you were just talking about, Andrew, about NFRs, CFRs, that kind of stuff. The conversations around that have to sharpen. The things that we've had for a long time but we need to get better at. I think what will be interesting is, I don't know, but the lower-level stuff. Andrew, you mentioned the quality thing, and do we care about what goes on inside the code and so on if we get what we want? I think defining what we actually care about at that kind of higher level of abstraction and then understanding what guidance do we want to provide to the agents to get that.
A couple of examples, as you mentioned, there's a lot of talk about TDD. Do we still have the agents do TDD? Do we think that it's a healthy thing to have them do, or do we think it does not really matter anymore? There's things like code design, readable code, and all that. Does it matter if we're not the ones reading it if the LLMs are fine reading it? Do we care much about variable naming and all that kind of thing?
I think those are questions to be answered by understanding, again, those higher-level things. Why should those things matter? Why do we care about TDD and good quality code? We think it helps make the code more maintainable so that after you get that first release out the door, you can continue to deliver, make changes to it, and when something goes wrong, you can diagnose it quickly, you can find the fix and fix it without having unintended consequences. We think those are the things that you will notice, that users will notice, and that business stakeholders will notice.
I think there is a whole interesting bit of research to do over time to find out how much those lower-level things actually impact on those higher-level things that we care about. We may find that there are some things we still do care about. Maybe we still do care about TDD. Maybe it still does drive some good things that make the code maintainable even when it's LLMs maintaining it.
I guess I am giving you more of a question [laughs] than an answer, Ken, in terms of what stays the same. I think it is more that emphasis on we have to get better at thinking about those higher-level things, because we have always, again, been a bit lazy about it, or always struggled with how we articulate to management why should they invest in things to make the things that we think make delivery better. We've always struggled to articulate those things. Now we have to articulate it to the LLMs and tell them to do it and measure whether they're doing it, which is really interesting.
**Ken:** Great. I want to thank you both. I guess one little last tidbit for the listeners. There was actually a section at the conference. I don't remember the title of it, but it was something to regards to, "What's on the agent's reading list? Do books still have a place?" I can tell you that as a podcast host, there's only so much you can learn on a 40-minute podcast or on a 30-second YouTube short.
Depth does matter, and so please do check out the books by both Kief Morris and Andrew Harmel-Law. They're important foundational information. Nothing more important than a foundation when your building is shaking. Again, thank you, Kief. Thank you, Andrew. It was great seeing you in person, and I look forward to our next discussion.
**Andrew:** Thanks, Ken. Thanks for having us.
**Kief:** Thanks, Ken.
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
[ Read Technology Radar ](https://www.thoughtworks.com/en-gb/radar)