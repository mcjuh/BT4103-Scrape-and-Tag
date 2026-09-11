<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/what-harness-engineering | Title: What is harness engineering? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  What is harness engineering? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Prem Chandrasekaran and Nate Schutta | Podcast guest  Birgitta Böckeler
May 14, 2026 | 40 min 51 sec 
Listen on these platforms
## Brief summary
'Harness engineering' is one of the most significant terms to emerge in software engineering in 2026. Broadly referring to the work done to control unpredictable AI agents and coding assistants, its use signals growing attention on what needs to be done to make agents reliable and consistent enough for production software in the real world.
On this episode of the Technology Podcast, Birgitta Böckeler joins hosts Prem Chandrasekaran and Nate Schutta to explore what harness engineering actually is, how it should be done and why it should matter to software engineers working today. Having written a number of articles on harness engineering for martinfowler.com based on her experiences with AI-assistance, Birgitta is well-placed to explain the core concepts and implications.
Taking in everything from the practices and ideas that pre-date and inform harness engineering to integrating harness engineering into existing workflows, listen for a conversation that will provide much needed clarity on what's an essential topic in the industry.
  * Read Birgitta's [article on harness engineering](https://martinfowler.com/articles/harness-engineering.html) on martinfowler.com.
  * Watch Birgitta's [video on harness engineering and coding sensors](https://www.youtube.com/watch?v=uLWOLmeHOSE) on YouTube.


**Prem Chandrasekaran:** Welcome everyone to yet another episode of the ThoughtWorks Technology Podcast. My name is Prem Chandrasekaran. Today I've got my co-host, Nate Schutta. Nate, do you want to quickly introduce yourself?
**Nate Schutta:** Absolutely. I'm Nate Schutta. The best way to describe me is 'architect-as-a-service' here at Thoughtworks.
**Prem:** Today, we are joined by Birgitta Böckeler, who is usually a host on the Thoughtworks Technology Podcast, but today she's playing the role of a guest. She recently wrote an article on something that's called Harness Engineering for Coding Agent Users on martinfowler.com. For me, that was the clearest mental model that I've seen for what teams running coding assistance day-to-day should actually use to build around them. Welcome, Birgitta. Do you want to quickly introduce yourself as well?
**Birgitta Böckeler:** Yes. Hi, Prem and Nate. I'm Birgitta. I'm a Distinguished Engineer at Thoughtworks and I'm based in Berlin in Germany. I have been a host in the past, indeed, but I haven't been on the podcast in a while, so I'm glad to be back.
**Prem:** Before we get into definitions and such, here's the question that I would want users to keep in their heads the whole time. If you're running a coding agent, Cloud Code, Cursor, Copilot every day, and you feel the gap between what these tools can produce and what you would actually trust, without supervision in some cases, this episode really, for me, is about closing that gap. Let's start at the beginning. What is harness engineering, and why are you writing about it now?
**Birgitta:** That was one of the challenges when I was writing the article, to figure out how to even define it, because also in these days of AI, people create a lot of content and there's a lot of discourse happening very, very quickly. There's a lot of throughput of communication as well. We just throw out a lot of terms and then get semantic diffusion really quickly. I ended up describing it almost an onion kind of model. You have the large language model as your ultimate tool that you use to do something, but then you put something around it that people have started calling the harness. A coding agent is a harness of an LLM in a way.
[Claude Code](https://www.thoughtworks.com/radar/tools/claude-code) is a harness. The [Pi coding agent](https://www.thoughtworks.com/radar/tools/pi) is a harness. There's lots of choices there. The way that they're harnessing is by putting together a bunch of tools that can be used by the LLM through this harness to do stuff. In the case of coding agents, that is editing files, reading files, certain code search tools. Maybe access to a language server, all of that type of stuff. Then they also orchestrate prompts. They have a system prompt. All of that is making the model much more useful to be able to code for us.
Then as coding agent users, as users of this harness, we can also expand the harness. That's the next onion layer out. We can take the ready-made harness Cloud Code or Cursor that some people have already thought very deeply about, like what are all the things we need for coding, but then make it more specific to what we are working on. If I work on a TypeScript code base, I want to think about what are specific things in my particular application and TypeScript code base that I also want to harness.
For example, we'll get into it later, like static code analysis or stuff like that, or what are additional tools I want to make available to it? What are my guidelines, my specifications and stuff like that that I feed into it? That's also what people have started calling a harness. I almost wish it was a different word, because that might make it easier. It's almost like two different bounded contexts. That's what people now call harness engineering. When you have conversations with other people about this, I would always try to make sure that everybody's talking about the same type of harness so that there's no misunderstandings.
**Prem:** Absolutely. You seem to break the harness into two halves, guides and sensors. Can you walk us through that distinction? What's the difference and why it matters?
**Birgitta:** I was basically just reading about what people are calling harness engineering. There was an article that got a lot of attention from a team at OpenAI that was called Harness Engineering. I think the author's name is Ryan Lopopolo. I was reading that. I was reading some other articles, listening to what our colleagues at ThoughtWorks are doing on different clients. I was just trying to find some vocabulary for what's going on. It's not really like inventing new things, but just trying to find some language for us to make it easier for us to think about it.
One thing is what you were saying, also that the guides feedforward. We're thinking about what we want the agent to do, and we're trying to anticipate what it might need and where it might do something wrong. My typical things in the early days of instruction files was like, remember to activate the virtual environment before you execute a Python command, or in this project, we always use the following coding convention patterns or stuff like that, because maybe we've seen the agent fail at something multiple times, so we're trying to anticipate that and tell it beforehand to give it a good chance to create the code that I want in the first place.
Usually, it's never perfect. Then, in the second step, we also want to give it feedback so it can do some self-correction, even before I, as a human, have my first look at the code. It's all about trying to direct where I have to put my attention. The feedback then can be stuff like very classic, a lot of people do that right now, is like a code review agent. It's like another little agent, another LLM that looks at the code that was generated in the initial generation and like finds flaws in it or find places where it maybe didn't comply with the guides that I gave it. That would be a type of feedback.
We also have, actually, a lot of tools available already historically that we've been using for years or sometimes even decades that can give automatic feedback as well that are more computational. That is not interpreted by an LLM, but is more deterministic. The classic example that we can dive deeper into later as well is static code analysis. For everybody listening who's been using coding agents for a while at this point knows that typical failure modes are very long files or classes, very long functions, cyclomatic complexity is high, or functions that have 10 arguments or parameters, which is often a smell for bad design.
We can actually give an agent that feedback. We don't have to type that out. A static code analysis tool can do that. It's just this constant loop of, what do I anticipate and feedforward so that it does a good job in the first place, and then also, how do I think about giving it feedback? Then those two things is a new job that I have as a developer that I work on. Whenever I see something go wrong, I think about how can I steer this in the future with a new guide or with a new feedback sensor or stuff like that.
**Prem:** For those of us that have been doing this since before AI existed, this seems an awful lot like what I would have done with an intern. I get a new intern for the summer, and perhaps we have a conversation about , "These are our coding standards, this is how we do things here." Then I would be watching their work for a while, observing and getting feedback. It feels to me like this is yet another example of nested feedback loops, which come up an awful lot in software engineering.
**Birgitta:** Yes. I literally once had a grad, so a person fresh from university, on my team, who we often paired with, but not always, because for grads, I always want them to figure out how to do stuff by themselves as well, not just always pair. Then, when they were not pairing with us, with the more experienced people on the team, the static code analysis tool that was set up was actually very helpful to them because some of these basics they didn't know yet. We were already used to some of this stuff.
However, the difference between a grad or an intern in AI is that this grad, at some point, very quickly learned it's not a good idea to have lots of arguments in a function. They learn.
Whereas with models, they, of course, also get better. We know that. There are certain things that we just cannot rely on that. At some point, they would just never do them anymore. The feedback is extra helpful when it's deterministic like that.
**Prem:** Right. You also seem to draw a line between computational and inferential. Can you give us an example of each and where that line actually matters in practice?
**Birgitta:** In context engineering, which harness engineering, it's a type of context engineering, I would say, what everyone seems to be focusing on heavily so far is basically lots of markdown files. A markdown file to describe the coding conventions, to describe the project context, the architecture, or also a markdown file in the form of a skill to do the code review. That is all then interpreted by an LLM. That's what in the article I call an inferential guides and inferential sensors.
Those are always up to interpretation by the large language model. They are particularly helpful on the feedback side, for example, when it's semantic stuff that we just cannot catch with something like static code analysis or regular expressions, stuff like that. They're super valuable there. I think a lot of teams have so far been underusing the computational guides and computational sensors. I think there's a lot of potential there.
On the feedforward side, there's different tools that we can make available to the agent that, again, increase the probability that they are good at manipulating the code in the way that we want. I mentioned language servers before. That, for me, would be an example of a computational guide, because with the language server, I can, for example, do stuff like, okay, I want to rename this core concept in our codebase, and we use this term all over the place and functions and class names and so on.
LLM, please find all the places where we're using it, but then execute the actual renames with the help of a language server or with JetBrains has an MCP server that uses all of their rename symbol functionality and stuff like that. It's very token-intense, so maybe I want to reduce that. Also, it's maybe a little bit more error prone, so I just give it this tool.
Another cool example of that is codemods. These category of tools that are really good at doing large-scale refactoring, in particular, in situations like version upgrades or library upgrades. Tools like OpenRewrite or there's also a few tools in the JavaScript space for that, I think. Again, I can make that tool available as part of my expanded harness to the agent so that it has a better chance of doing reliably what I want to do.
Then, of course, on the feedback side, I mentioned already a bunch of examples. There are so many computational sensors that I think we still have a lot of potential to get stuff out of them. I recently used good old static code analysis a lot in a project to set up, like I said, these low-hanging fruit, like long files, long functions, cyclomatic complexity, lots of arguments.
I was actually positively surprised how much potential there is in that, because we've always kind of like, yes, static code analysis is fine and all of that, but that ultimately doesn't guarantee us quality. Actually, when I use coding agents, it gets triggered all of the time now that I have it integrated and actually gives the agent signals of that design and it tries to rethink and break things down further, reduce complexity without me even having to look at it. Yes, I was positively surprised how much potential there is in that, I think.
**Nate:** That's interesting. Anecdotally, I just heard about a team that was complaining about all these markdown files in their repo. Perhaps the thing here is, well, use some of these computational tools. It also, I think, is a good reminder that just because there's new stuff doesn't mean we throw out all the older stuff. There's still value in these tools that we've used in some cases for decades on projects.
**Prem:** The main distinction that you seem to be drawing is that computational sensors or computational harnesses are 100% deterministic, whereas the inferential ones may not be. I don't want to put a percentage to it. It's more of a suggestion rather than an assertion, where for the static code analysis tool, it's deterministic. It's yes or no. There's no in-between answer, whereas with the inferential ones, although you might have told it to write great code, use only a cyclomatic complexity of less than 10, it might violate that when it's under pressure, which we don't really know when that happens, but it does happen.
**Birgitta:** Yes. The inferential ones are all about semantic interpretation, the interpretation that happens when the token prediction happens, which is their strength, but can also, in some situations, be a negative, or we want to complement it with the other stuff.
Then you can also think about how do you balance that, because then when I was looking at some of the possibilities like static code analysis, structural tests of module boundaries and stuff like that, then maybe at some point you can think, "Okay, this part I actually have covered pretty well with sensors and the AI doesn't even do it wrong that frequently. When it does it wrong, then the sensor gives it feedback. Maybe I can just delete a bunch of my guides upfront because I have this feedback setup on the backside."
Then on the other end, I was then wondering, but what if maybe I want to start using weaker models who then do certain things wrong more frequently so the sensor constantly triggers and I always have the self-correction, then maybe I want to have them back in the guides. I was just thinking about, just speculating about how the combination of strength of the model, what guides I have, what sensors I have, and how those will all influence each other potentially, what I want to use. Having these words to describe it helps me think it through.
**Prem:** Until the time that the token economics are pretty significantly subsidized, I guess we don't have to worry about it, but maybe that day will come very soon.
**Nate:** I think that day is coming already. We're already seeing the switch from all you can eat to we know we're going to charge you for what you use. I do think that's going to be one of the fascinating aspects of this as the subsidized tools using subsidized models goes away as investors want to see the return on the money they've poured into this space. I think we are going to have to get a lot more clever about some of that.
I was just talking to Chris Kramer about that. The constraints often do set us free in some ways and they forced us to get creative and try some things. I think a lot of what I'm hearing here in this, Birgitta, is that it's one is none, two is one, that we use these layers to catch these things because you can't just rely on, "Well, I had a system prompt that said, don't delete prod," so it's never going to delete prod, right?
**Birgitta:** What's also interesting about the static code analysis, we were talking about how it's like a tool from the past. There are two things. One is that now with AI, AI can help us build more of these sensors. We don't even only have to use those tools out of the box. For my little application that I'm working on, I actually created lots of custom scripts or additional little rules. Also, one big potential of this is that you put in your own custom messages for the different rules to give a little bit of self-correction guidance. That's also quite powerful.
Then the other new potential or opportunity for static code analysis is that one of the reasons in the past that we often got tired of it and it just started gathering dust in the corner, the server. One of the reasons for that was always that it was hard to get the signal to noise ratio right, especially when it came to the warnings. You would get all of these warnings and you would never take the time to suppress them case by case in the code base. You just had all of this noise and you just gave up looking at them.
Now with AI, for example, let's say this thing about long functions, I can tell AI in the guidance that I give it for that particular max lines function violation, I can tell it, "Hey, this might be a design smell, this might be too complex. Think about this and make a judgment call." If you decide that it's okay, it's just two lines over or that's just what this function is, we can't break it down further. Then you're allowed to suppress it for this particular function in the file, or increase the threshold slightly so that we can still get it violated in the future if it gets even bigger.
Then AI might sometimes take the wrong decision, but I actually have it documented in my code. I can even have yet another custom script that shows me all of the exceptions that it made and I just start my review there. That's maybe the first way because those are decisions that it took about the design. That's maybe a good place to start my review. This actually gives us the chance to wrangle, maybe, those warnings and actually keep a clean house for once and might, again, make static code analysis more useful than in the past.
**Nate:** We can make the AI do all the anal retentive things that we wanted to do, and in our best intentions, and then we're just going to not worry about those warnings. It's fine.
**Prem:** You make a strong case for keeping quality left, which is something that is, of course, for Thoughtworks teams that we've been seeing for a long while now. What does this actually look like for a team that already has CI, but is now layering all of these coding agents into the process? Is there anything that you have specifically for them, in addition to the static code analysis that you're talking about?
**Birgitta:** If you've already been doing all these things, you're much better set up to do this. You're much better set up to give these as sensors to the coding agent as well, of course. It's just a question of like, how do you run it also during the coding session? That would be the shift left, because I see a lot of stuff about where things just happen once a pull request is done. Then all of these review and sensors and start happening. I'm like, "Why is this happening after the pull request is created? Shouldn't this be happening even before commit, or at least some of those things?"
I think there's also a lot of potential for tooling here. I've been playing around a little bit with like-- we can experiment with tooling a lot now as well. I've vibe-coded some stuff locally, where I built a little sidecar that was running next to the agent and continuously executing all of the cheaper sensors like linting, the test suite and so on. Then the agent could just get an agent-optimized snapshot of what is the status of stuff regularly from this little sidecar. I think that's one thing about maybe some of the things that you're only running in the pipeline at the moment. How can you shift them even further left so things are already clean when they get into integration?
I come from a world where I think I haven't worked on a team that is pull request by default ever, because at the time when Git came around, I was in an environment where the teams that I was working with were doing trunk-based development by default. I always obsess about the perfection of the commit. I always want every single commit to be deliverable, to be clean. That's how I always think about it.
Test suites, by the way, is a special kind of sensor, I would say, because they're half inferential in computational clothing. They feel computational and deterministic because it's green or red, but a lot of people at the moment just let AI generate all the tests, and the tests might be testing something that we don't even want. This whole thing about the behavior is like a whole other beast, I would say, that is a lot harder to deal with. What is a bit easier is to think about test effectiveness and test quality, and acknowledge that coverage is not enough to tell us if tests are effective.
That's also what I tried in a code base, is like I had an AI-generated test suite, and it had pretty high coverage, but I found a bunch of unassertive things with mutation testing, lots of them actually. Regression was-- I think of the test suite in that sense as a regression sensor for the agent. It tells the agent you broke something or you changed something in the behavior that was there before. It can then, again "think, reason about" is that a good thing or a bad thing? What do I have to change? Is it actually testing the behavior I want? That's the hard part that where we really need humans to look at the test.
**Nate:** That's a really important consideration, too. I was actually just talking to someone who told me that their AI agent decided to comment out the authorization because, in dev, they didn't have the role to execute the specific function. The way the AI decided to get around that problem was just comment out authorization. My first thought on that was an intern or a new software engineer might do that. However, us as a senior engineer on the project would see that, take the engineer aside and explain why you should never, ever do that. Hopefully, they would learn they wouldn't do it again.
**Prem:** One thing that I've tried to do, and Kent Beck talks about this, it's a human responsibility to define what tests exist, and it's a human responsibility to even write them. That way, the AI is confined to just writing the production implementation, and you define what goes in and what stays out. I'm not as strict as Kent does it. My workflow is more along the lines of, "Okay, I'll describe to you what I want. I'll also let you write a few tests, and then I'll review those tests. Then make sure that the tests are what I want, and if not, we go into a revision loop until we are both satisfied, and then finally move to production."
That seems to have worked reasonably. I won't say that I've got it and nailed it completely, but it definitely mitigates the risk of the AI just wrote a bunch of tests that nobody really cares about, because the implementation demands it as opposed to the requirements needing it. That's something I would like to get your thoughts on. What's your take on that?
**Birgitta:** I haven't tried too much in this space yet, but I catch up regularly with our colleague Matteo Vaccari, who has a lot of background in the different testing traditions and all of that, and he's thinking a lot about this. One approach that he has used on multiple teams now already at this point, I think, is he's been trying to find a place where there's a good place for almost acceptance tests.
I think more broader acceptance tests are becoming a lot more popular now, because of this, which has advantages and disadvantages. Basically, for him, in a lot of these teams, it was the HTTP API entry point. Then at that point, you have functionality that always has input and output, and it's always like request-response in the case of HTTP APIs, which is useful. Then he's just custom-built himself a little test runner, where the input and output is always written in a way that is easy to review by human.
A comparison would also be BDD, behavior-driven development frameworks, that also have input-output scenario descriptions that are easy to review by human. Then, with that, he focuses a lot of his review on those tests. I don't know what he does with unit tests, actually, like, how deeply he reviews those as well. What I've seen in my code base is that those acceptance tests then really drive up the coverage, but then often they don't do as many assertions on every single little detail.
Then that's kind of dangerous that then we might have some gaps there that we can catch again with mutation testing. I think it's called the approved scenarios pattern or something. I've forgotten the name of the person who described it. There's a website somewhere about AI-assisted coding patterns. This approved scenarios pattern is what he's been using and has quite liked. It depends on what type of code base it is, what type of functionality. I still don't see really big patterns on the horizon on how to make this easier.
**Prem:** Nat Pryce and Steve Freeman in their GOOS book, _[Growing Object-Oriented Software Guided by Tests](https://growing-object-oriented-software.com/)_ , they talk about this approach as well, what they call outside-end testing, where they start with higher-level tests, acceptance tests, as you're calling them. Then move in to say, "We'll write more finer-brain tests. Then finally, when we are at a place where we feel like we've got most of it there, we'll try and retire some of those higher-level tests, and then rely on more on the lower-level ones," because obviously, these unit tests run much faster and cover a lot more. That does require a lot of discipline. It's a technique that has existed, obviously, for a long way.
**Birgitta:** There are so many things to rediscover. This testing thing is also an example, another concept I brought up in the article, is that then I try to think about sometimes, almost different dimensions that I'm harnessing, because in some areas, it's a lot easier than in others. For the behavior, it's a lot trickier, I would say, and we still need a lot more human involvement. Then for maintainability and internal code quality, the whole, like static code analysis stuff and structural tests and stuff like that, is a lot easier, maybe.
Then we can also think about other dimensions that were almost regulating with these feed-forward feedback loops, like our architecture fitness, for example. What are our executable architecture fitness functions that we can give as sensors to agents and so on? I think that's also useful to just think of it in different dimensions that we're regulating and not trying to do everything at once. Harness is just a word for all of those things, and you can do lots of little, small things in that big spectrum of sensors and guides and dimensions. [Chuckles]
**Nate:** What's old is new again, is what I'm hearing you say. I thought that was funny, you mentioned that the fact that we seem to constantly rediscover these things. I've seen that throughout my career. These things that we've learned, and then, I don't know, a whole new wave of developers comes in, and we need to reteach them these things over and over and over again. This is a lot of what I'm hearing in this conversation, is these are things that we have been doing for many, many years. I feel like shift left has been the defining concept of software engineering from day one. This just feels like yet another example of that and the importance of having layers of these things.
I think we've all been involved in some of those conversations about do we need you tests or do we need integration tests? It's like, yes, you need all of them and the exact ratios and percentages, it depends on your project and where you're finding pain. These fundamentals that many of us have learned the hard way are still as important today as they were when we were using zeros and ones.
**Prem:** Arguably more, even more important. Let me push on cost a little bit. I think Nate talked about it slightly earlier in this novel. We've got a lot of these inferential sensors now moving left. They're running pretty much, maybe after every change, definitely after each commit. Now you've got a pretty large organization. Now, is this something that is one sustainable and have we gotten to a point where the investment actually starts paying off, or is it too early to call that?
**Birgitta:** The investment of sensors, I think, can pay off in different ways. It's like one can be of less token usage, but another can also be just having higher quality code, in general. We've always thought about, in our path to production, where do we put certain things? We just talked about the tests and the test pyramid, and there's always this understanding that some tests are more expensive than others, both in terms of maintenance, but also in terms of how long they take to run. You always want to quick feedback loops, especially in the beginning.
Some of these inferential sensors also just take a while to run. They give me a longer feedback loop. That might be another reason why I don't want to run them constantly during my session. Then you think about, how do you distribute these things strategically across your path to production, across your pipeline? What do I run before I even commit, before I integrate? What do I run on a pull request or in the pipeline? Then what's also happening a lot that's also mentioned in the article from OpenAI, but I've heard stories about that from multiple teams at Thoughtworks as well, is what do you run continuously or on a schedule?
Let's say once a week or every two days or stuff like that. We have always done that with things like dependency vulnerability scanners. We also run them regularly, even when there's no change, because they relate to our environment. The environment changes around us. There's all of these different things to consider in where you put these, and for running them repeatedly. The OpenAI team calls that garbage collection. Because even with all of these guides and sensors and this harness that they designed, they still saw technical debt compound over time.
They have things running continuously, and that double-check and review all of these different dimensions, and see where the garbage is piling up or where the debt is compounding. Again, as an example, in the application that I'm working on, which is a small internal application, I have three of those in place that I could maybe run once a week or so, and then a human would look at the result. One is a security review that's basically a prompt derived from our internal security checklist for internal applications.
Another one is specifically, you could call it an architecture fitness review function that looks at, specifically for this application, some of the things that, how we want to handle data and not show certain data ever on the UI, and just double-checking that we really still doing that. It's about sensitive data and stuff like that. The third one is about dependency freshness. It's actually a script that looks for the dependencies that are quite old, over six months old or something. Then AI takes the result of that script and creates a report with web research and so on, about like, "Oh, this one seems to be deprecated," or "This one is really outdated, you should look for an alternative," stuff like that.
It's a nice example of a combination of first giving AI a leg up with the script, so you don't have AI go off on web research tangents, but you just have a deterministic script that tells it what's outdated. Those are examples for this continuously running ones. From the Thoughtworks teams that I've talked to, there were examples of an organization that had some tech debt in their APIs, for example, so they almost created API linters and API reviewers that would go through all of the APIs in the organization.
Of course, in some cases, you can also immediately trigger new coding agents that make pull requests to suggest the improvements, so that the human doesn't even have to do those, but review the pull requests. I diverged a little bit from your question, Prem, about cost. This is also something to consider when you really think about where do you put what and how often do you run it. Then, just over time, another way of how we're steering this, that we constantly want to balance these things, and learn from it.
**Nate:** That tech debt is a cost, too. I think that's an interesting thing here, that I think we've always had that as an ideal, that we would stay on top of our dependencies and that we wouldn't let that creep into our code base. There's just a certain level of that that you just can't stay on top of. As humans, we have other things, other demands. "Oh, this feature needs to get done. Oh, there's this critical defect," and so we end up sliding that aside. I think we've always had a little bit of, I don't know, maybe shame's too strong a word, but guilt over. Oh, the code base got out of hand again, but it feels like some of these tools, if applied, can prevent that or can take care of against some of that toil. Maybe we end up with much cleaner code bases than we've had in the past.
**Prem:** Then there is the odd question, who owns the harness? Do platform teams now build it for app teams, or does each app team own their own harness, or is it a combination of both? What's your thought on that?
**Birgitta:** There's lots of open questions. Also, what are other tools that can help us with this, or how do we keep things consistent and coherent, that the guides still match what we have in the sensors, all of that. Who owns it? I think it would definitely be a combination of things because it's hard to say the word the harness, and then immediately, you know what it is, because like I said before, I think it's lots of different small things. It's just like the system. Then people are responsible for different components, but it's probably a combination of both, that you have something from some platform, some central skills that everybody can use. Then there's like stuff that you have in your own code base.
Then you have to think about how do you update it, how do you distribute it, how do you version it, how do you test that it's actually making things better/ We call it like so highfalutin, like, "Oh, it's harness engineering." How do we actually know that what we're doing is making any difference? I also played around with that a little bit, and that's what I mean by there's a lot of potential here for tooling. Where I had my little sidecar also log all the time, regularly, the status of the sensors.
I could make some visualizations showing me during a coding session what some of these sensors-- the linting would suddenly be nine arrows, and then they would go down again because the agent would respond to it. I imagine you can also then take that even further and log what types of things are going wrong. Then you have statistics about what is the most commonly wrong thing that the sensors catch. Then think about putting that into your guides because it might even avoid the self-correction in the future. That's an open question.
Then also, all of these sensors, is it just going to get too much, both for the agents? I can already see the more rules I activate, it always finds more stuff. Is it just getting too much? When the sensors are actually in conflict with each other, how does an agent make the trade-off decision? That might get interesting as well.
Then also for the humans, if we have that garbage collection running all the time and all of these things, it will just create even more pull requests, even more reports for us to look at. Then how do we prioritize those still? Will we just get another version of the signal-to-noise problem that we had previously already? Will it just be at a higher level or in a more sophisticated way? There's lots of things to figure out to see how this turns out in practice, I think.
**Nate:** Seems like an interesting evolution of what we do as software engineers. I think there's been this, I would almost call it a fixation on software engineers, or we just write code and say, code is part of the job. It is maybe an output of the job. I think any of us who've done it for a period of time realize that that's not actually the only thing we're doing. We're not just typing for six, seven, eight hours a day.
**Prem:** If a senior practitioner, or any practitioner for that matter, is listening to this already, running coding agents pretty much every day, and they walk away wanting to do one thing on Monday, what is it that you would tell them?
**Birgitta:** Think about how you can cut your markdown by 50%. What would you do? [Laughs]
**Prem:** There you go. Thank you, Birgitta. I really appreciate it. The article is on martinfowler.com, called Harness Engineering for Coding Agent Users, and I would definitely encourage everyone to read it. Thank you all for tuning in. Until next time, it's the Thoughtworks Technology Podcast signing off.
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
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