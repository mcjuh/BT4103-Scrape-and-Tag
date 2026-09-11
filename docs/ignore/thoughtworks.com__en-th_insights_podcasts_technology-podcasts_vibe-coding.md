<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/vibe-coding | Title: We need to talk about vibe coding | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  We need to talk about vibe coding 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Prem Chandrasekaran | Podcast guest  Birgitta Böckeler and Lilly Ryan
April 02, 2025 | 36 min 53 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/vibe-coding#Transcript)
Listen on these platforms
## Brief summary
The term 'vibe coding' — which first appeared in a post on X by Andrej Karpathy in early February 2025 — has set the software development world abuzz: everyone seems to have their own take on what it is, how it's done and whether it's a bold new chapter in the history of programming or an insult to anyone that's ever written a line of code. 
Clearly, then, we need to talk about vibe coding — and that's precisely what we do on this episode of the Technology Podcast. Featuring Thoughtworkers Birgitta Böckeler (AI for Software Delivery Lead) and Lilly Ryan (Cybersecurity Principal), who join hosts Neal Ford and Prem Chandrasekaran, we dive into the different understandings and applications of the concept, and discuss what happens when a meme collides with reality.
## Episode transcript
**Neal Ford:** Hello, everyone. Welcome to the Thoughtworks Technology Podcast. I'm one of your regular hosts, Neal Ford, and I'm joined by another of our regular hosts today, Prem.
**Prem Chandrasekaran:** Hello, folks. Glad to be here.
**Neal:** We're joined today by two of our Thoughtworks colleagues who have a strong opinion about the subject we're going to be talking about today, and I'll let them introduce themselves, starting with Brigitte.
**Birgitta Böckeler:** Hi, my name is Birgitta. I'm a technical principal with Thoughtworks in Berlin. For the past one and a half years, I've been responsible in ThoughtWorks for building up our subject matter expertise on using AI for coding and for software delivery in general.
**Lilly Ryan:** I'm Lilly Ryan. I'm based in Melbourne, Australia, most of the time. I'm one of our cybersecurity principals. I've had a focus for the last while on how cybersecurity intersects with artificial intelligence technologies and the ways that people are building them into their applications.
**Neal:** Fantastic. We are here today to talk about what started as a viral post on social media that has been interpreted many, many ways, some good and some bad. Today, we're going to untangle some of the interpretations and the implications of what is now suddenly called vibe coding. Can someone here please define vibe coding and where this term came from, please?
**Birgitta:** This is where the problem already starts. We were talking about that before we started this episode. The speed of semantic diffusion in the AI space is really record speeds. For those of our listeners who maybe don't know about semantic diffusion, it basically talks about when there's a term that over time loses its original meaning or is being reinterpreted by people. Famous example is the term agile. Vibe coding was defined in a tweet.
I just looked up the date of the tweet again, February 2nd. That was like what, six weeks ago, seven weeks ago, not even, right? Since then, I've seen so many interpretations of this. The original tweet was by Andrej Karpathy. We're going to dissect that a little bit. Basically, I think the simplest definition that people took from it is you use an AI coding tool, you let it work on your code, and you don't even review anything that it does anymore. You just use it until it works. That's the simplest definition.
**Lilly:** As Brigitte says, that's about the most simple definition. What you end up building out of that is quite variable, just as with any other code, you can build anything you can think of. What's been interesting, I think, to observe from all of this is the kinds of things that people are thinking of and turning into apps that have been put into production almost as soon as they've thought of them. What comes out of that is always really interesting to observe. In this particular space, in this particular environment, that's led to a lot of very interesting kinds of situations.
**Prem:** I'd say one thing. I did see that original tweet that Andrej Karpathy made, and it felt like a bit of a meme at the time. It still feels like one. Here is where it started getting a little serious for us. One of our clients, a very senior leader at one of our large lines, actually said that they want to use vibe coding and use it in a manner that will actually reduce the number of members on the team and thereby reduce cost. They want to try it out in a very, very serious way. That's where it felt like, okay, we should definitely talk about this in a forum like this one.
**Birgitta:** That's where the definition thing comes in again. As consultants, we always have to ask our clients like, "In your context, what does this mean?" I think my suspicion is that some people maybe through this meme, through this tweet, have discovered a new set of features that has emerged in AI coding tools over the past maybe four months. Has been around for a little bit longer, but the last three, four months, it has really gotten more serious, which I would maybe call supervised agentic modes in coding assistance.
A very prominent, good examples of that are Cline, Cursor, or Windsurf, so three different AI coding assistance. GitHub Copilot is also working on something like that, but it's still in preview. That is a new mode in these assistance where I basically start with the prompt, or some people also call it chat-oriented programming. You start in a chat, and the chat fully drives your implementation with the help of the tool. It starts going, it starts changing multiple files for you, whereas previously, maybe six months ago, in most coding assistance, you would go like a few lines at a time. Now it actually starts changing multiple files for you.
**Birgitta:** It can execute terminal commands automatically, which can be really powerful. It can execute tests for you. It can look at the results of those tests and then immediately pick up and say, "Oh, it seems like there's like a little error still. Let me try to immediately fix that," so I don't have to tell it to try and fix it. They integrate with the IDE to pick up on linting errors and some compile errors and say, "Oh, it looks like what I just generated, there's still an import error. Let me quickly fix that."
You have a lot more of this like mode where it does all these things. That's like one of the possibilities that some people now think that vibe coding is this mode in the AI systems. I would say that originally, what it meant was a way of working with these assistants in a particular way. Andrej is talking about you embrace potentials, you fully give into the vibe, you forget that the code even exists.
You just let this agent do this. He's also talking about, "This can be really fun for a weekend project." There's stuff like that in there. I think it is one particular way how you can work with these assistants, and there's a bunch of other ways. Lots of people are starting to write about their workflows, which is really interesting, but this is one particular way, and it can for some stuff be really appropriate.
We always have to look for the appropriate practices in our situation, not a best practice or something like that. I think there's this spectrum of like, first it's just about using these new agentic tools to your advantage to try and make your team faster and more effective. Then there's also this extreme of using them in a way that you're not even looking at the code anymore, and that can potentially for actual important production code be a problem.
**Prem:** Yes. Look, the way that I interpreted it was that he took a bit of an extreme position, maybe for effect, or maybe he meant it. There's no real way to say because I don't know him. It feels like we don't seem to think that this is a real thing, which we would use on client engagements at Thoughtworks or anywhere where there is something serious at stake. Am I misinterpreting this, or is there some truth in that statement?
**Birgitta:** Everything depends. If I have to, let's say, whip up a quick utility script where I know it doesn't have a lot of blast radius in terms of security, maybe Lilly can say more about the security aspect. Sure, this can be really fun, actually. When I'm prototyping, or I sometimes get into this mode when I'm trying to do styling like CSS and stuff like that, I just let it do its thing and have my hot reload web browser open. When it looks like I want it to look, then I start looking at the code, because then usually, to be honest, in most cases, I delete 70% of the CSS attributes because there are too many. For a while, I actually go into the vibe coding mode, or like I said, prototypes or something like that. Like every developer practice, sometimes it's appropriate, sometimes it's not.
**Lilly:** I look at it as a way of getting into a flow state, and that is one thing people really enjoy about coding is the ability to sink into what they're doing and build something up from what they're thinking about and getting to that point faster. It's compelling. It makes it feel a lot more straightforward, I think, to get your idea into a working prototype space. That's something that has always been called out about coding assistants.
That, from a prototyping point of view, they're quite good at coming up with something that looks and maybe functions a bit like what you would like, or you can get something out in front of people really quickly, and that very quick moving agile way of saying, "What about this? If we interacted with it that way, is that actually going to work or do we notice very quickly when people use it that this is not going to work in the way we intended it to?"
That can be really interesting. I think for a weekend project, the way that Karpathy is talking about it, I used Adachat actually over the Christmas period. I wanted to learn how to use a couple of Python libraries for MIDI interfaces because I had been gifted a synthesizer, so I wanted to write some aleatoric music generation things, which was wonderful. It meant that from that point of view, with those libraries I wasn't familiar with, it got me started, and it got me sending MIDI sequences to the synthesizer. It was a fun thing to do for a couple of hours on a weekend.
I also noted that when it got to a certain point of complexity with the application itself, that was where it started to-- I'd like, "I like this, but actually I really want dark mode," and it could do dark mode for me, but what it would do in order to do that was create an entire new class that's like, "Okay, we call this dark mode now," rather than writing CSS and doing a toggle the way that someone might, if they were thinking through it. It's taking you very literally, which leads to a lot of this spaghetti stuff at the back end that Karpathy is calling out, saying, "Look, I don't even understand what it's doing anymore." That's part of the vibe. I'm not worried about how it's structured. Then when it comes to debugging, that can be an issue.
I liked Ada in particular, because with other tools that I had used, they didn't have any connection to stuff like git commits. Ada would stage them for me. That meant that I could roll back to a previous state because tools like this will often end up putting you in a place where you try something and it's just completely broken everything. Being able to roll back from that requires you to understand what you're doing. Staging git commits helps a lot with rolling back to a very clean point where you were before. If you're not aware of how version control works, how to implement it and so on and so forth, you find yourself in a mess and then a broken mess. That can be a problem.
**Birgitta:** Yes, there's actually also-- I know Ada has this way of creating a commit after each change. With these tools that I mentioned before, Cursor, Windsurf, Cline, they all have features now that keep track of the changes in progress on top of the Git changes for you. They like write to the files all the time, but there's always the current change set. At some point when I'm happy, I can say, "Okay, keep all," and then it starts building up transparency for me again for the next round of changes, but it's all the same Git changes. There's more and more advanced ways of tracking this coming up, but it can also be confusing when you first start using it.
In the beginning, I didn't understand what was going on at all. Is it changing my files? Is it not? What's the difference to my Git changes? You have to get used to it, and it introduces a little bit of complexity, but once you get it, it can be quite powerful then as well. Then you can also maybe go into vibe coding mode for 10 minutes. Then, like you said, when you feel like, "Oh no, like this is actually not doing what I wanted," you can just roll back. They have these like restore things. Git commits, of course, is the original way to actually fixate what was already working so it doesn't get broken again.
**Lilly:** What has been interesting to observe as this trend has escalated is the number of folks who are discovering from first principles what version control is and why it is necessary. Often to their own detriment and some of the things to read are just a bit like, "Oh, I'm sorry. I'm sorry that happened," but there are these things. Version control is complex and it's difficult to understand. First, you've got to understand why you need it in the first place. People will learn that.
Then secondly, you do have to understand a bit about how it works, whatever type you're using, whether it's Git, whether it's something built into one of these tools, because you are going to need to experiment and come back to a previous clean state in a lot of ways. Making something accessible to people who are new to software development is wonderful for getting people to explore their potential. This is now one of the spiky sides of it. There are many, but this is one of the first ones I see people running into. It's enlightening to watch folks discover these things from scratch.
**Birgitta:** You are right. It's not easy. I still remember when I was learning Git and I didn't take people's advice to actually first understand what the principles are, I kept saying to people, "I think I have a Git life crisis," because I couldn't for the longest time figure out how it works.
**Prem:** Yes. It feels like this. I must say that I'm a developer by vocation and by profession. Maybe I don't quite appreciate the situation that folks who have not actually coded for a living go through. I can empathize that now you've got this ability to create magical things without actually having to get into the nitty-gritty of having to understand or learning how to code.
What you seem to be saying now is that, if we can take an approach where we make small changes and then test whether it did the right thing and then commit that code in some way, metaphorically, maybe not using Git-- you talked about how these tools like Cursor and so on have this thing built in outside of the version control system itself-- you can actually go back to a working state.
Maybe this is something that is worth trying. Is that a use case for vibe coding where you go in small steps,you check that it works, and if it does work, then you create a snapshot of that and then you go forward? Then if you make a mistake, you say, "Okay, no, no, let's go back to that last known good snapshot." Is that a way to make this thing work for you?
**Birgitta:** You can make it work for real. It's just which situation you use it. Like I just said with the CSS. I just let it do the thing in that particular case. Although there is a little bit of a contradiction there when I would use vibe coding and for small changes, I think that's like a conflict, because that's not the idea of vibe coding to get back to a semantic diffusion. Because the smaller the change, the more you actually have to technically think about what is the next small iteration, and the smaller it is, the more you have to think about the actual implementation. The whole vibe coding idea is that you stay around the black box, kind of, and you don't think about the details. There's all kinds of tools in the toolbox now that let you go into that mode when you feel it's appropriate and helpful.
**Neal:** I have a few thoughts based on what we've been talking about so far. One, I think this is a valuable way to stay in flow state and reduce friction for annoying implementation details. The danger I think here is a mode that I've seen, this used to drive me crazy when I used to teach a lot of classes in person of developers who, when a mistake would occur, rather than try to understand what the mistake was, just make a random change and then try it again to see if it works.
This seems like it opens up the floodgate of just random change, see if it works, random change, without ever thinking through the problem. If you're using it as a way to remove friction from thinking, I think it's nice, but if you're using it as a crutch for, "Let's just keep trying random things until it works," that's going to, I think, generate problems for several reasons. First, as Brigitte and I have observed before, and in fact, Lilly's observation brought this up, LLM's approach to most problems starts with boil the ocean, not the simplest thing that will work.
Oh, I need a dark mode. Let's generate an entire new profile for the thing for one change, which could have been made somewhere. That's the danger I think of here is that it over-engineers things out of the box, which is great. If it's a tiny little thing, like you said, as a throwaway project, but the danger here, so replace the word vibe with the word prototype. We know the dangers of quick prototypes that can't go into production and the shortcomings of that. I think most of our clients understand that, but this is the same thing just at a deeper level because you're building behavior, not just user interfaces. This is really prototypical because most of this code, probably in its state, would not end up in development anywhere.
One last thing about this that I think is true for all of the prompt-to-code initiatives that I've seen, including CHOP, the chat-oriented programming. CHOP is the acronym I was seeing for that. For CHOP is that it mistakenly believes that the act of software development is nothing but writing simple algorithms about the behavior of systems. It is that, but it is also about balancing that behavior with the capabilities those systems need to be able to support, also known as software architecture. ChatGPT is great for generating business algorithms and solve problems and sort lists and those kinds of things, but solve this problem at scale with elasticity, with good security, that's balancing capabilities.
That's much harder for ChatGPT to generate even with human assistance. To assume that some vibe coding would pick up on the fact that we need some critical capability, scalability is not as big a deal if it's a weekend project, but toward Lilly's point, security, am I going to generate something from vibe coding that accidentally has a massive security hole and not realize it because I don't understand what the code does?
**Prem:** Look, it looks like I'm taking on the person of someone who really loves vibe coding. I'm going to go along with that notion for the duration of this podcast, at least. One of the arguments made for this kind of thing is that the LLMs now are just smart enough to be able to make that big leap as opposed to restricting yourself to something that has low stakes involved. It's not a weekend project. You can do this for something much bigger because the LLMs are just that much more smarter these days. What's your response to that?
**Neal:** I would say that we have a hard time training humans to be good software architects and good trade-off analysis. Invariably, when you ask an LLM to do the trade-off analysis an architect does, it comes back with three good suggestions and four terrible suggestions. Are you going to vibecode your way around the terrible suggestions that are going to do damage to your system, like security holes and those sorts of things? They're much better, but we're talking about things that even humans haven't mastered yet.
I don't think they're going to outstrip our ability to be able to do that.
**Birgitta:** Prem, to the point that you made about how LLMs are making such big leaps and are so much better now, I think we should mention, it's not just the large language models. A lot of the innovation in these latest features is actually the combination of the large language models with what's going on in the IDE, by the way. It's the tooling overall, it's not just the models. In terms of the big leaps and that they're doing so much more stuff now, I just published a memo on Martin Fowler's website where I've been writing a memo series where I write about my experiences and examples of where they go wrong, like the missteps.
There, I actually talk about the mode when I'm not vibe coding, so talking about alternative workflows, and I'm supervising the session. I steer and redirect all the time. All the time. While this has indeed become really powerful, and I'm actually feeling like I'm getting a little addicted to it, I don't want to work without it anymore, there are these things where my experience, like I have more than 20 years of programming experience and where it really, really is important. One category of things is just sometimes the code just doesn't work.
My experience, I actually have to know when to stop and do it myself or something like that. I think that's actually not so problematic when you have people who don't know what they're doing, because if they can't even get the code to work, that's very obvious, and then maybe that's not so much of a risk. Then the second thing is intervene where when you're on a team, your team might immediately notice that something's wrong within a few days, within that iteration. It's a concrete examples I've had of like it doing too much upfront work, for example.
I was trying to do a front-end tech stack migration and it wanted to do all of the front-end components at once and only then do the connection to the backend, which can potentially lead to a delay in making the right decisions. It would do brute force fixes instead of root because analysis like, "Oh, this Docker Build is running out of memory. Let me just increase the memory settings." Then I would go, "Yes, but why are we running out of memory?"
Stuff like this is something that the team might very quickly realize when the build starts getting flaky and they're like, "Hey, Brigitte, what did you do?" When it misunderstands requirements and I'm adjusting it and if I don't catch that because I don't pay attention because I'm vibing, then the business analyst, the product owner, the QA will come to me and we will have to go back and forth and it creates friction in the delivery process. I learned these things because I ran into them in my career.
I would hope that less experienced developers today will also learn them this way. The question is just on some teams, the throughput of this might be so much increased that they might not be able to buffer this. That remains to be seen. The really insidious category is the type of things where I intervene because I know they will have an impact on the long-term lifetime of the code base and on the maintainability. It's stuff like very frequently, the tools write verbose or redundant tests and test assertions.
It always creates a new function instead of adding to an existing test function, stuff like that. By the way, some of these things you can mitigate with new features as well, like something called rules or custom instructions, where you can say, "Always first check if there's an existing test instead of writing a new one." You can mitigate some of this, but they never follow everything to the letter. There's definitely a higher than X percent probability that this will happen to people.
Lack of reuse, overly complex implementations, all of the CSS code that I was talking about that I'm deleting. You have to pay attention. You have to have this experience. This category is insidious because the team might not even notice it in that iteration. They might notice it 6, 12 months out when they have to touch that code again. Again, I sometimes go into vibe coding mode, but it absolutely for proper software cannot be 100% of the time. If you do that, very, very probably you'll run into problems very, very quickly, but at the latest six months later when you have to change it again.
**Lilly:** Because there is some Discourse out there on social media at the moment where we're talking about this, what I have observed in that that's interesting to note is the folks who are probably most enthusiastic about this are doing so in the context of learning or of being in the position of building a startup and some startup service. I haven't seen as much of that applied to existing enterprise environments. It's probably some good reasons for that, as we've just discussed.
It is also interesting to note, as I said earlier about people learning for the first time why version control is important, sometimes very painfully. Also, understanding why it is important to be able to know what your code is doing and where. The maintainability that you touched on, Brigitte, is extremely important for the long-term health of anything. The security aspects of it, too, which we've mentioned a couple of times, have been interesting to note. There is one post that's been kicking around and getting a little virality.
As with a lot of things online these days, it's hard to know whether this is true, but it's also something that I can absolutely see happening because I have seen it happen in some circumstances. Someone talking about building their online service with cursor with zero handwritten code and saying AI is no longer just an assistant, it's also the builder. Now you can continue to whine about it or start building. Also, yes, people are paying for it. It's something that has been put online as the service.
Then a post two days later, I'm under attack ever since I started to share about how I built this software. Random things are happening, maxed out usage on API keys, people bypassing the subscription, creating random stuff on the database. As you know, I'm not technical, so this is taking me longer than usual to figure out. For now, I will stop sharing what I do publicly on X. There are just some weird people out there. There are.
**Birgitta:** Yes. Then somebody just responded-- Usually, when people say on the internet, "You don't know what you're doing," then that's what it sounds like in my head, like I just said it. He had one response where somebody said, "Maybe it's because you don't know what you're doing." That's what it played like in my head at this time. This poor guy was like discovering these consequences.
**Prem:** Yes. I do want to say one thing. Maybe this is the wrong parallel to draw. When I was starting out, people would be like, "You definitely need to know and understand intricacies of the C programming language." Some of them would actually come and tell me, "No, no. If you don't know assembly, do you really know what's going on under the covers?" I was trying to learn Java at the time. C was a thing in college, and I did it at college, but when I was graduating out, Java was becoming this big thing. Now I was like, "Okay, should I learn assembly? Should I get good at it? Is Java good enough?"
Because Java seemed to abstract a lot of things. For example, memory allocation was something completely we didn't have to worry about because the garbage collector would take care of and people would be like, "We don't know how to do it. You might not appreciate the problems that occur because of that." I reflect back and I'm like, yes, look, I did a whole bunch of Java professionally. I don't quite think I missed the fact that I never learned about allocating and deallocating memory intimately. I did learn about it, but really, it wasn't something that I missed.
**Birgitta:** Yes. No, I think in this context of what we're talking about right now, it's the wrong parallel to draw. Because compilers, for example, are deterministic tools. If you think about the examples that I just gave, they were a lot, for example, about duplicated code and stuff like that and maintainability of this. Some people say, "Oh, but the AI will maintain it in the future." I won't. It turns out the AI also needs the type of well-factored code that makes it easier for us to refactor things or to touch things.
Duplicated code is a great example. When you have in your code base two places that implement the same thing, and then you start changing just one, and then it becomes inconsistent, that's hard for AI as well. There's all kinds of like studies and click-baity numbers out there, but one of the ones that I really like is from a company called GitClear, where they have data on lines of code and how much gets added and moved and all of that in code basis. They recently published a second version of their data that they published one year ago.
The numbers have actually gotten worse in the sense that in those code bases, they found more lines of code added than before. It's easier to add code with AI than to change it. They found quite a further decrease in number of lines of code moved, which is a really good indicator of refactoring. Refactoring is going down. More duplicated code as well. They found quite an increase in the trend of churn. They define churn as lines of code you committed, and then you changed it again within two weeks because maybe you realized, oh, that was wrong, or you had a bug or something like that.
All of those things are going in the wrong direction in the trend. For me, it's not the same thing because the code that we generate with those, with the chop, with the chat, that's still the code that gets touched by the AI as well, and that gets deployed, and it's non-deterministic. There's all of these pitfalls that I just described before. For me, it's not the right parallel.
**Neal:** One other parallel to Prem's example is that the rule of thumb always was understand one level of abstraction below the one you're currently working in. It's great if you work in Java and never have to worry about memory management, but you're never, ever going to be allowed to touch my C++ code base because you'd be a hazard in that code base. The same is going to be true here, but it's even worse, as Brigitte brings up. This is not just an abstraction layer, it's a non-deterministic abstraction layer. The reason for that advice always was because abstractions always leak. When they leak, you need to know how it works underneath to fix the leak, or you're just lost. When it leaks non-deterministically, then now you've got some much more interesting issues.
**Lilly:** I think that there's always a line you have to walk with this sort of tooling. On the one hand, it is great to see people enthusiastic about learning new things and jumping in to try them. That is really wonderful. It's exciting to have people discover these problems. In some cases, a bit validating to have people discover these things and just, "Yes, that's right." This is why this is something that some people will "just know." People are not born knowing these things, and that's fine. That's life. It's exciting to see people learning things and using them.
I think also that calling out vibing as a mode of thinking through your code, as in just sort of feeling your way through the code, that's also very valid. It's a good observation. A lot of us enjoy coding because there is a flow state element to it. This enhances that to a certain degree, which is fun. The question is about when you switch gears, I think, and what you do with the result as well. If anybody's thinking about trying this stuff in context, making sure that you understand what you're doing, you need to understand the mindset that you're in.
You need to understand the environment that you're in as well, and also whether it is just something you are playing with prototyping, or whether it is something that other people are already relying on, or you intend for them to rely on, and/or maintain and/or use. There are different uses in different places for these things. I don't want to imply that none of that has its place. I realized we also haven't touched on issues of things like intellectual property, which also comes into it in a very distinct way. In terms of a learning tool and a tool for finding the fun and the play in work, I think that's wonderful.
**Birgitta:** In terms of the purposes, maybe, I wanted to add one last thing that was also in the original tweet that we haven't touched on yet, is that Karpathy talks about talking, not typing. In the tweet, he's saying he's using superwhisper. I've done this with the Mac dictation feature, and it's not that great because I have to talk relatively slowly for it to reasonably transcribe, but some of these AI live transcription tools are really good now. You can actually talk as if you're talking to a human, and fast.
There are some studies apparently now, I'm sorry, I don't have like a proper quote right now, but I've read a few things about how, when we talk and not perfectly type up a sentence, we actually sometimes provide more context and more useful context for the model as well. I find that an interesting mode as well, that cannot only be used with live coding, but also with other type of chat interaction workflows for AI-assisted coding. That's an interesting one to try as well.
**Neal:** Looks like we need to wrap up here. We've reached just about our time limit for our podcast, a fascinating subject. There was a request here to define what we mean by flow state. That's that flow, that uninterrupted state of thought that you get into when you're coding and the time disappears. It seems like our conclusion is that vibe coding is really good for that, but maybe not for production critical systems or a very important thing. A great example of one of the nuanced topics that comes up at breakneck speed in the AI age and software development. Any last words about this subject for our other host or guests?
**Birgitta:** I would say if, as a listener, you hadn't heard about these new features yet that even enable vibe coding, then I would say with all the risks that there are as well, and apart from the benefits, I don't think this is going away. I would encourage everybody to try this and get a feeling for it to understand the implications for your team. Yes, as a profession, we now have to develop our workflows and good practices to properly deal with this. It's an exciting time in a way.
**Lilly:** I would encourage people to view this as a tool among many others, something that can be very helpful, but whatever you're doing with it to acknowledge that your brain is the only thinking and reasoning thing in that workflow. This is something that can help you and help you get to somewhere more quickly than you could before, but you are still the one responsible for what comes out the other end of it. It's pretty important to understand at the end of what you're doing, whether you're in the vibe state or you switch states, what you've got on your hands when you're finished.
**Prem:** What do you seem to be saying is that a human still needs to be in control?
**Lilly:** Ideally, yes. We don't always make the best decisions, but we do have the capacity for reason.
**Prem:** Yes. On that note, it's the end of yet another very, very fascinating episode on the Thoughtworks Technology Podcast. Back to you, Neal.
**Neal:** All right. Thanks, everyone, for joining us. Thanks to Lilly and Brigitte for their great insights, and thanks, Prem, for acting as the advocate for vibe coding. Thanks, everyone. I hope you enjoyed it. We'll see you next time.
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
## Dive into the latest Tech Radar
[ Explore now ](https://www.thoughtworks.com/en-th/radar)
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