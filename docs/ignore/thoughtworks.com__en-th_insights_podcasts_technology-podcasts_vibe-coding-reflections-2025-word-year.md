<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/vibe-coding-reflections-2025-word-year | Title: We still need to talk about vibe coding: Reflections on 2025's word of the year | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  We still need to talk about vibe coding 
Reflections on 2025's word of the year
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Prem Chandrasekaran | Podcast guest  Lilly Ryan and Neal Ford
November 27, 2025 | 46 min 23 sec 
Listen on these platforms
## Brief summary
Vibe coding was, remarkably, named word of the year by the Collins English Dictionary at the start of November 2025 — pretty good going for a term that was only coined in February. We first discussed it on the Technology Podcast back in April, and, given its prominence in the collective lexicon this year, thought we should revisit and reflect on the topic as 2025 draws to a close. 
Lots has happened in the intervening months: MCP adoption, the evolution of agentic coding tools and practices like context engineering have had a significant impact on the way the world is thinking about and using AI. 
To talk about it all and reflect on the implications, Thoughtworkers and regular podcast hosts Prem Chandrasekaran, Lilly Ryan and Neal Ford reconvened for a follow up to our April conversation. Taking in everything from the term's semantic slipperiness, its security risks and the challenges of maintenance, this is a discussion that, despite going deep into vibe coding, also touches on a huge range of issues in the technology industry today.
Before we enter 2026, looking back on the good, bad and the ugly of the last 12 months of experimentation is essential if we're to build better software for the world in the future. This episode aims to be a guide through that process.
  * Listen to our [April episode on vibe coding](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/vibe-coding).
  * Read Ken Mugrage's blog post exploring the shift [from vibe coding to context engineering in 2025](https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/vibe-coding-context-engineering-2025-software-development).


**Prem Chandrasekaran:** Hello, everyone. Welcome to yet another episode of the Thoughtworks Technology Podcast. My name is Prem. I'm one of the regular hosts on the podcast. I've got two of my colleagues here, Lilly and Neal. Do you folks want to introduce yourselves?
**Lilly Ryan:** Hi. Yes. I'm Lilly. I'm a Principal Cybersecurity Engineer here at Thoughtworks.
**Neal Ford:** Hi. I'm Neal Ford, also one of your regular hosts. We couldn't actually figure out how to assign host and guest for this particular episode, so we're all host and guest for this because this is a part two follow-up episode about vibe coding. About six months ago, the three of us, plus our colleague Babitha, recorded a podcast about vibe coding that happened right at the time that vibe coding became a popular meme. We'll talk about that in just a second.
This is a follow-up six months later as to how the world has consumed and encapsulated the concept of vibe coding, and what it has become over the course of the last six months. One of the things that we talked about in that previous episode, in fact, we started a previous episode with this concept of semantic diffusion, which Martin Fowler, our Chief Scientist, I think defined, or at least popularized this idea that any term that you put out there, when it's used enough, the meaning of it will start diffusing and people will start applying whatever meaning they want to it.
We should probably start off this podcast with giving a definition that we can work with throughout this podcast as to what vibe coding is. Because one of the things that we're going to talk about is the wide variety of definitions and attitudes that exist out in the world. Who wants to give us a working definition of vibe coding as it currently stands?
**Prem:** It started with this tweet that Dr. Andrej Karpathy made, where he said that he just gives into his vibes. He does not look at the software that's produced. He just chats with the AI, and then at the end of it, he gets some working software. If it doesn't work, he just takes error messages and that kind of thing and then pastes it back to the AI, and then it magically corrects things. Basically, a form of producing software where the code that is used to produce the software almost vanishes into the background. The focus is mainly on producing the software itself and looking at it from the outside. That is what it meant, at least, at the time. Right now, Lilly, do you want to want to venture a definition?
**Lilly:** I think the entire internet at this point has had a go at venturing a definition. It seems trite to me to go to the dictionary definition, but I think it's relevant in this case because Collins Dictionary, a few weeks ago, announced that vibe coding was their 2025 Word of the Year. It's a phrase of the year, but it's Word of the Year. I thought they would wait until December till announcing this, but they go ahead and do it in November.
What they define it as is the use of artificial intelligence prompted by natural language to assist with the writing of computer code, which is a bit of a different thing to what Karpathy was talking about back in February. Certainly, something that I've seen as conversations about this have unfolded in the intervening months, that vibe coding means whatever you want it to mean. Quite often, in your context, it's often used as a pejorative term. It's sometimes used as a complimentary term.
I think the word vibe in here is really the operational part for me. Vibe implies, to me, something that is very flow-based. We said this in the first episode that we recorded on this topic, that the flow state part of this is really the compelling part to a lot of people. That it enables you to roll with the ideas that you've got and see them come to some kind of fruition. The vibe is also a very loose thing. While that's good for prototyping and experimenting, it's also not the kind of thing you want handling healthcare data.
There's a question then about what it means now to different people. To me, that word vibe still really comes back to I've prompted something into existence, and I haven't really checked to see how it's put together. I haven't really put too much thought into the overall context. I just wanted to see what would happen; here is the result. That is not what everybody means by it, but it's certainly how I think about it when I hear that term vibe coding, specifically these days. What about the rest of you?
**Neal:** Engineering is a merger of craft plus science. Vibe coding, to me, feels like leaning into the craft side and letting the annoying science stuff go to the side. I'd really love to have a building, but all the engineering stuff, the building is annoying, I have to do all that math. I'd rather just build a beautiful facade and that sort of stuff. I think that's where the vibe thing comes in, is because it's a fun vibe and it's the fun part, the creative part without the annoying responsible part.
It's nice to build a beautiful building, but then if you forget to put doors and locks on it, then people are going to crash into your building and do stuff that you didn't want in your building. That is ultimately the downside of this is too much vibe, not enough engineering. [chuckles]
**Prem:** I interpreted it slightly differently. It never was the original form, or at least I never took it to be the way that it was originally defined by Karpathy. For me, it was, we produce software for our clients in usually enterprise scenarios. That kind of style just does not work. For me, it was getting help from the AI to produce software, but at the same time putting in a bunch of guardrails so that both the AI and the human, or the humans who are involved, can actually evolve the software without fear of what breaks, which has always been the case with things like TDD and continuous integration and everything related to the Agile moment.
This was just yet another way to apply that without you actually having to manually type in the code yourself, which is what we were used to doing previously. I wrote an article on that as well, and I called it Vibe Coding. Why? Because I gave into the hype at the time, and a lot of folks criticized me by saying, "Oh, you're not really talking about vibe coding. You're talking about something else, which is AI-assisted development, but this is not vibe coding."
**Lilly:** Back in October, I think it was [Simon Willison posted something about this](https://simonwillison.net/2025/Oct/7/vibe-engineering/) as he has wanted to referring to vibe engineering as that distinction, the way that he was thinking about it to say, "All right, well, you have your vibe coding where you're coming up with code and the output is code," but vibe engineering, the word engineering implies a lot more of that rigor that Neal was talking about earlier.
To put it with the word vibe is a bit of a contrast in terms and could perhaps make it a little oxymoronic, I don't know, but it does describe a bit more of what you are talking about, Prem, that I think having a bit more context around it, putting in some guardrails, having a way of steering what you want that's not just about that conversation that you are having, that exchange that you are having with a large language model at the time, but also that you have given it a structure within which to operate overall.
That, I think, reflects a larger trend across the industry in general, which was nascent when we were speaking about this back in March or April, and has certainly hit the mainstream now where a lot more folks are talking about how best to work with agents, with assistants, with bits and pieces plugged into the sides of things that can help you with the rigor that's required for the kinds of actual engineering that we're talking about, these parts that will make it reliable or make the output shaped more toward what we want rather than whatever the large language model is pulling out of the latent space based on the prompt that you gave it.
That has, I think, a lot to do with the emergence of the model context protocol at the same time earlier in the year, which, as it has matured, and it's still only what, 10, 11 months old at this point, but it's got a lot of maturing to do. As it has moved into the spotlight, has brought in with it a lot more of these tools and compatibilities and plugins and things that allow people to pull in context from different places at different times to inject what they need into that context window so that what comes out the other end is guided not just by whatever the user happens to type into that prompt box, but also by documentation that might be relevant at the time that's gone and been fetched.
That you could have sub-agents doing things, which you could at the time that we were speaking, but it was a lot less common then than it is now. Given the speed at which things work, I feel like I'm talking about something that happened 10 years ago, and it wasn't, but that is the speed we're operating at.
**Neal:** Well, that is the speed of how fast generative AI is affecting our ecosystem. I think that's a reflection of how the definition of vibe coding has shifted almost in lockstep with the rise of agentic AI, because what was originally the original definition of vibe coding suddenly became much more powerful when you have autonomous agents, because you can tell them, "Build me a fitness function and make sure that passes before you move on to something else."
That was something that was much more cumbersome if you're just doing code assistance, but now you have these autonomous agents, and now it becomes, as Prem was talking about it in an earlier conversation, building specifications that build some of these better safeguards. I'll let him talk about that, but I think that's more of a reflection of a more modern definition of vibe coding, at least I think what Prem would like for it to be, which incorporates agentic AI to build a lot more of those engineering safeguards in the code.
**Prem:** Absolutely. Lilly, you mentioned the model context protocol. That gives us a hook to move into the next segment of-- Looks like the tooling has matured a little bit since our first conversation. MCP wasn't a thing, at least at the time, but now it's almost de facto. Are there other tools like that that have actually made something like this a little bit more viable, or is MCP it? Is that the game changer here because now you're able to pull in context rather flexibly from a bunch of sources?
Like you may have your requirements management system, you may have your CI/CD system, you may have your production logs, and whatever else like that to pull in the right context, and then now inform the software that you build. Are there other things like that in your experience?
**Lilly:** With the shift that has happened away from trying to make the next new Big Bang model with a massive step-changing capabilities, I think being a bit more realistic and talking about what can fine-tuned smaller models do? What can our models do if they are focused on this specific task, or that? What has been very helpful in these kinds situations has been the ability to switch between different kinds of fit-for-purpose tooling, not just through the model context protocol, but also through the types of large language models that you might want to use, or even the types of deterministic tool sets that you might want to use at the right moment, for example, to switch.
I can see that this is built into a lot of things, like Cursor, Claude Code, and so on. To switch between a less robust model with fewer parameters and so on, for some of the things like Git commits and things like that. Something with a lot more capability, a larger context window, and more parameters to deal with the actual coding itself, I think, is a big step change, a very useful one, and also one that makes better use of resources is a big one for me.
I really like that focus that's coming to play on what language models can do when they're not large, massive models, but actually coming back to that very foundational philosophy of that tool for a purpose, rather than saying this is one thing that can be anything to anybody, which comes with a significant number of risks and opportunities, but also risks to be able to say, "I know exactly what I want out of this, and I don't want to have to spend time coaxing it out of this extremely broad amount of training data that's gone into this.
I know exactly what I need from this context, and it's this thing, and I need a model that does that." That's both better for resources broadly speaking in terms of time, money, the environment, but also, it gets you what you need faster if you actually know what you want, which, when we're talking about building software, once we've done prototyping.
In our context, where our clients are at, they often have an idea of what they want. We don't need that broad brush stuff. That is experimental, and it's very useful for certain phases of things, but not for what we're doing when it comes to delivering reliable software that actually works in front of customers.
**Neal:** What you're suggesting there, which I think is correct, is there's a spectrum of capabilities here that has emerged over time. It's not a binary of using AI versus not. In fact, one of the pieces of advice on our most recent radar was, "Don't use AI for deterministic things," because you're just wasting energy and resources, because if it's deterministic, you don't need AI for that.
That would be one end of the spectrum and then a full-blown LLM at the other, but now, right-sizing usage is along the tool and engineering chain, I think, is a good indication of understanding capabilities and trying to right-size for context resources and some other balances like that.
**Prem:** You talked about models, you talked about the model context protocol, and then the third thing that I'll say is our ability to prompt, as well, has probably improved. I do see a lot of prompt templates that people use to try, and I won't say, predictable output, that's probably not possible, but at least something that borders on getting to that place of getting somewhat reliable, predictable output. Those three things, for example, in terms of the model, there is Cursor's Composer 1, which is a purpose-built model. It's not one of the frontier models from OpenAI or Anthropic, or Google's Gemini; they have purpose-built. It's blazing fast, I might add.
They don't obviously tell you the internals of how they have built it, it's closed source, but it's purpose built and it's cheaper than some of those frontier models, and it actually does a pretty good job. I can't really say that it was any worse than any of the other ones. Yes, those kinds of tooling do seem to be getting a lot of investment in, and I guess we're probably going to continue for the foreseeable future.
**Lilly:** A thing I've also seen evolve has been not just how the code comes to be, which is often what vibe coding is getting at with the term, but we've had the opportunity to see what it looks like when code written by an AI, an LLM ends up in production and runs for a period of time and what that means for maintainability. No code that comes from anybody, from a human, from a machine, whatever it is, is going to be perfect when it's written, and it's certainly not going to remain constant over time.
The environment shifts around it, even if the code itself is as well-balanced as it could be at the time that it was put together, and from a security point of view, which is my main focus, maintainability is really where that difficulty comes into it. We've made it even easier, I think, now for people of many different kinds of backgrounds to write and produce code, which is an excellent thing when it comes to people figuring out what they want, being able to make the tools that they want to support the needs that they have.
Where that, I think, extends is do we have vibe maintenance? How does it work when we project it into the future? Because sitting in the security side of things, often the things that I see are the bits that break. I don't get to see a lot of the good use cases because otherwise people don't call me, and that certainly biases my perspective, but it does mean that this is an increasingly active concern because we've seen as it has gone on applications breaking.
This was something we mentioned in the first episode that we did about this, that people were hacking vibe-coded applications as people were publishing them, especially the ones where people were very prominently discussing how they were building this out with vibe coding. We've also seen data breaches in the intervening time with apps that have since been found to have been "vibe coded," and by that I mean, written almost entirely by large language models without the developers themselves reviewing the output or having the skills to review the output, which is a problem.
Not to mention that when code is produced quite often it doesn't come with non-functional requirements like accessibility and like security. Unless you're explicitly asking for something to be secured, it's not going to do that. The application will work just fine in that happy path case without it, and those kind of things, I think, are really starting to surface up. They're things that many folks predicted, especially when this all kicked off. We started to see more and more concrete examples as time goes on, because maintainability is the really hard part in my view.
**Prem:** That actually raises the question, are there any good patterns that have emerged, or are there clear anti-patterns that you would want to stay away from?
**Neal:** What I was going to say is what Lily was talking about reminds me of nothing is static in the software development ecosystem. As vibe coding becomes more popular, I fully expect that exploits will start looking for the hallmarks of vibe-coded sites and start trying to exploit them explicitly in a very rapid fashion.
I remember, this is back many, many years ago, but back when Windows had a lot, let's say, serious security problems, and I remember at the time, the instructions for installing Microsoft SQL Server at one point said, unplug the computer for the internet and put the CD in and install it, and then install these five patches, because the description was the background radiation of the internet is that if this server is plugged into the internet, by the time you install it before you can install the patch, it will have been infected to the point where it's unusable anymore.
That's what I fear for some of the vibe-coding, because there are going to be holes that show up consistently in a lot of these vibe-coded solutions that I think will be-- The rapid exploit will be shocking, because as we know, several malicious MCP servers have already shown up in the wild, for Lilly in particular. I think she, because of her position, focuses a lot on the very specific security as a non-functional requirement or architecture characteristic. I think all of these architecture characteristics are ones that are the things that people carry less about in the vibe coding world than in traditional software development.
**Prem:** What you're saying is blindly trusting the code that AI wrote is a clear anti-pattern. We still, as humans, even if it is authored largely by AI, have a responsibility to review what the AI wrote, because at the end of the day, when a commit happens, it happens against the human's name. We can't say that it was the AI that wrote it. It wasn't me. That's one thing that we have to be very cognizant of, is what you folks seem to be saying?
**Neal:** I actually think that's a spectrum as well. If I'm using it to generate a quick prototype, then I care less about internal code quality, and cyclomatic complexity, and even security, and some things like that, if it's never going outside the firewall. If I'm building a medical record system, [chuckles] I'm going to be obsessed about that kind of stuff. I think it's purpose-fit. I think the mistake a lot of people make is getting-- It's just like anything that you enjoy doing.
You don't do the responsible steps that are required for that thing, and actually figuring out what those are as you're building the thing. I know many cases where spreadsheets become massive, complex applications just because they just kept growing over time, and there's a problem with vibe-coded solutions as well of that organic growth.
**Lilly:** Not everything needs to be incredibly gold-plated at the time that it's produced. We spoke earlier about prototyping, and about experimenting, and about the craft, the art, the fun, and the enjoyment of building things. Those are different parts of that spectrum that you were talking about, Neal, where we've got, at one end, enterprise software that has not just customer expectations, but legislative requirements and all kinds of other things that it needs to meet, which is right at the other end of that spectrum from playing around.
Both of those things could be hacked, but whatever you're using the tool for, it's important, I think, to bear that end context in mind. What I see, though, is not just in the code, although there's been a lot of focus put on what types of vulnerabilities are in LLM-produced code, but that it's also in how it's published, how it's put out to the world. There are certainly now a lot of platforms, like Lovable, Replit, and so on, that can help with that and make it a lot easier to put something out there.
That was true even before LLM-assisted coding was a thing. When it comes to publishing things online, I've seen very well secured code that is tested and all kinds of other stuff be published and the administrative endpoint is just right there online, straight up exposed to the internet, or folks putting it together may have really strong application experience or focused entirely on the application and not on the infrastructure, so that you've got that background radiation of the internet that you mentioned earlier, Neal, which is only intensified over time, hitting open EC2 IP addresses and scanning it automatically because that is just how the web works.
It's how the internet works. It's not part of how people think about an app necessarily. The entire concept, that whole spectrum of the things that need to go into producing a piece of software, and if it is the intention to put in front of other people, doing so. Those are all the responsibilities that a developer has to bear in mind, I think. It's not just that it's made coding easier, but it's made it more and more important that people have a clear picture of what they're doing, if they're intending to do it with any seriousness, and that they're pulling all of that into the work that they're doing, as they do it, that has to be not just the app, but also the infrastructure, the logic requirements, and everything else that goes with it.
**Neal:** One of the things that we talked about on our most recent radar was the thing that we put on hold, which was AI-accelerated shadow IT, which are people vibe coding little solutions and then putting them beyond the firewall to be useful for something and then surprising someone.
Toward Prem's asking us for advice, maybe that's a piece of advice is getting more diligent or formal in an organization about when does vibe coded solution need to pass through a threshold where we do need to start caring more diligently about some important things like security or code quality or whatever the case may be before it ends up being accidentally being published somewhere where it's going to get something in trouble.
I don't think a lot of organizations, because in the past, it wasn't possible for someone in the accounting department to create an application that does significant stuff with databases and can really cause some trouble somewhere. I think that's a new attack vector within the organization of your business, people accidentally attacking you by putting stuff where it shouldn't be.
**Lilly:** The ongoing maintenance responsibilities, too, that the applications generally solve problems people really do have, and that haven't been solved any other way. It is an enabler, and it needs to be looked at in practice over time. Whose responsibility is it to maintain that application once it has been produced? If the accounting department hasn't traditionally been in the business of building applications, they also probably haven't been in the business of maintaining applications either. They've got different skill sets and different specialties.
**Prem:** Looks like this style of development is here to stay. I can speak for myself, and I can tell you that I would not want to go back to the old style of manually typing in code the way that I used to do with an IDE like IntelliJ. I used to think of IntelliJ as the thing that made me complete, where it would almost complete what I was doing, and almost predict what I was doing, and it felt magical, but now this is several notches higher than that.
Where the difference is, I would not even pick up something to do, versus yes, I'm very confident that I can do it in a very short amount of time. That's the kind of difference that I see personally. I'm not vibe coding in the literal sense of how it was defined. I am engineering it, or at least I'd like to think that I am.
**Lilly:** Given that we're passing the host hat around a little bit in this conversation, I had a question for the both of you, which was something that we've discussed internally at Thoughtworks quite often, that many AI coding assistants are presented as a pair or a co-pilot, and as an organization where we've traditionally had really strong opinions and takes about what pairing is, what it means for software development success and so on.
Can you vibe code as a team, or is this a solo activity? Is this between you and a machine? Can you vibe pair with others, and what does that code mean for its legibility to others or its ability to be consumed in a team-based context?
**Prem:** Here are my experiences. With AI, I've mostly been working solo, but before that, I used to pair quite often with a lot of our colleagues. We did try the part where you've got a human pair, and then also the AI. My experience was that was very clunky, to be honest. It was a lot more easier when it was just me and the AI. My pair probably felt the same way as well, where now, in the case of a pair, we would alternate between the keyboard versus the thinking role. It almost naturally flowed.
Whereas when we were three of us, it felt like a crowd. I'm like, "Now, who's doing the thinking now and who's doing the coding now? Looks like the AI is always the one who's writing the code for most of it. Are we both thinking? Are we not always on the same page? What happens when you're not on the same page?" It was just hard to manage, at least for me, but I must say that I've not experienced that beyond a few occasions. The majority of the time, I've been solo, and I've found it pretty rewarding to be honest. It's been a lot of fun where the AI actually points out a bunch of things that I would not have thought of.
It almost felt like a real human being there, and not only that, a real human who will never look at their email, a real human who will never take a bathroom break, that kind of thing. To remain in a flow state was surprisingly easier, because they're not looking at their phones, they're not looking at their watches, they're not moving away from their desk. They're just there until the time that you want them to be there. Then, when you don't want them to be there, you just walk away, and everything ends right there, so just felt pretty interesting. Although I'm a big proponent of pair programming, I must say. It just makes me much better.
**Neal:** In my opinion, what you do with an AI cannot be considered pair programming. It's something else. It's quite useful. It's like one and a half programming, because the other aspect of pair programming, besides just splitting the work, is it's literally different cognitive loads, so driver versus navigator. Driver is worried about syntax and getting the test to pass, but navigator's thinking, "Should this class really be here? Should we refactor this?"
Those are two different cognitive levels, and you can't achieve that as a solo. When you're using AI, what you're doing is relegating the driver role to AI, and you become the full-time navigator, which is okay, but it's also more tiring than switching, because one of the beautiful things that I used to like to do a lot was ping pong pair programming, where I create a failing test. Now you have to make that test pass and create another failing test, and it forces you back and forth between those two roles.
That is actually refreshing, because it forces you from the macro level to the micro level constantly, and you just don't get that when you're using AI purely as a driver. It's useful to create more code, but I don't believe it creates this high-quality code, because that constant shifting from micro to macro is the thing that gives you much higher quality code from pair programming versus a solo.
**Lilly:** One of the reasons I asked that was because I think that it does tend to become a very solo effort, vibe coding. I've never seen it work well when there have been two humans involved, which makes it an interesting way to develop your own processes on something. I think also makes them harder to communicate to anybody else on the team. When it comes to how this is applied in a team context, I'm seeing a lot of unexplored tensions there, broadly speaking, where people will sometimes refer to large language models as teammates, which is an anthropomorphization I don't especially think is appropriate.
I think that they do. I think what you said earlier, Prem, is pretty important, that it's helping to elaborate on your own thoughts and get into your own ideas. What you said, Neal, about being 1.5 is probably about right. It extends yourself, but it doesn't bring anybody else, any other human beings, into that context with you. When it comes to what's produced with that flow, what are the good practices for making it work in a context where you have an entire team that relies on the stuff that you're coming up with, and relies on sharing the context that you are developing in your little solo flow?
**Prem:** It's an interesting experience. I think we probably need a little bit more time to actually pass judgment on whether it works in a situation where there's more than one human involved, along with an AI, but so far, so good, I guess.
**Neal:** One of the things when you write, you find out what metaphors work globally and which ones don't. This one actually surprised me. I've been trotting out this metaphor in a lot of European countries, and they don't get it, so I'll ask my two cohosts here, "Do you know about the phrase yak shaving as a computer science activity?" Both of you know yak shaving. Turns out a lot of people don't know yak shaving. They don't know what in the world you're talking about.
I need to describe, this is part of a computer science hacker terminology. Yak shaving is this process where, oh, I need to solve this problem, but then it generates another little problem that I need to solve, which generates another little problem. You get six or seven problems down the stack, and you realize, "Wait a minute. I'm trying to solve a problem that's way more difficult than the original problem I needed to solve, but you're in that problem-solving death loop, and you can't."
That's what yak shaving is. Where it came from is unimportant. It's a silly cartoon, but my observation is that LLMs and particularly agentic AI is fantastic for automated yak shaving. I need something done, I don't know exactly how to do it, but just go figure that out. I think that's where it's actually quite useful for a pair, because a pair can focus more on the holistic design and architecture of the system and let the LLM yak shave the solutions for things with some checks and safeguards, including some specifications, include things like tests and fitness functions.
I haven't seen that done a lot, but it seems to me that that might be a pair plus an apprentice. Of course, the problem that immediately comes to mind is the sorcerer's apprentice, and you give these agents this autonomy, and suddenly bad things happen. I think that metaphor is inevitable when you start talking about agents.
**Lilly:** There's a question about how-- a question that comes up often when discussing vibe coding is how to play with this type of tooling without de-skilling yourself. There's a lot that I've learned through the inevitable yak shaving, especially as I was developing skills for myself, like professional coding and software skills. Problem solving and experiencing yak shaving is I think an important part of learning. How do you play with the tools that you've got at hand without de-skilling yourself? What do you see as being important for people who are learning using this tooling to bear in mind as they're using it?
**Prem:** It's a very important point. I'll give you a real-world example where I'm working with a team, and this is a fairly junior team. It was an interesting, challenging feature that needed to be built. To my surprise, they built it in very quick time. I was like, "Wow. That's interesting." It worked. They showed me a demo, and they're like, "Wow. This is working great." My question was, "Okay. What did you do? How did you do it?" They were unable to answer that question.
That was like, "Oh. Wait." This was a bit of a friendly audience. I said, "Look, if this was a more formal audience, then this would not reflect very well on us. We cannot have the situation where we don't know what exactly got built, although it might appear to be working." That's a thing that I think we all have to guard against. It's like what used to be Stack Overflow-driven development. People would do that or Google-driven development.
Where they would look for a certain recipe, they would find it, they would find the first post on Stack Overflow or Google, and then just paste that exact same code into the ID and check it in. Then they have no idea what happened. That kind of experience can get taken to the extreme here, because this is probably a hundred times, I don't know how much, but definitely a lot more powerful than that. Here, you don't even have to do some digging and searching and all of that.
You just ask a question, and it just vomits out a bunch of stuff that looks right. Then now you're like, "Okay. It seems to be working. Is it the best thing? I don't know. It just works. Why the hell do I care? Let me just get done with this and move on to the next thing." The temptation is really, really high. It is on us to resist that temptation, because it's only going to get worse by putting in a bunch of safeguards to prevent that from happening.
Otherwise, all of the things that Lilly, you mentioned and Neal, you mentioned about security being a problem and so on and so forth are just waiting to happen. It does subvert that learning process, because previously, at least I would have to understand what is going on with that Stack Overflow piece of code, or at least I would try. Now, I'm like, "If I'm not even looking at what code is getting produced and just seems to work in large batches, then yes, it's definitely a problem.
In fact, Thoughtworker Unmesh actually wrote on Martin's blog exactly about this problem, where he said that it completely subverts the learning process. There is a joy in going through the grind a little bit, but now it's instant gratification. Now you're like, "You asked the question, and you've got the answer, and you can move on. Oh, wow, that's pretty easy."
**Lilly:** That's the vibe, right?
**Neal:** Exactly.
**Prem:** That's something to guard against. I can say this, it was when you're tired, especially, and you're like, "Okay. I just want to get this done. It's not working. I just want to get it done and be out, I guess." It's very, very tempting. I've tried to resist, but I can't say that I've succeeded all the time because the temptation is too high to basically get something working and move on. Definitely, the safeguard against that is to have more code reviews and ask those kinds of questions in terms of why have you made this kind of a decision? You should be able to answer those questions pretty authoritatively, even though an AI might have written your code. Refactoring is not optional in a lot of cases, I think.
**Neal:** Building and generating much more verification code in form of unit tests and functional tests, and fitness functions than you probably would if you're doing it as a person, because you want the automated test to go and to send the agents off to make sure this meets all these criteria before we move on from that. I remember one of the things that used to drive me crazy when I used to teach a lot of online programming classes are students who, when they were at something like a compiler error, they just make a random change and then compile again without thinking about it.
It always drove me crazy. That's exactly what an LLM does, because there is no reasoning. It's just making a random change and see if I can get it to compile. That's exactly the safeguards that Prem was talking about. I think it's the responsibility of us as software engineers. A lot of the problem that came about when rapid application development came out. You could build slick-looking user interfaces very fast, and people immediately thought, "Oh, well, it's done."
The constant prototyping problem. We have the same problem with vibe-coded solutions now. It's like, no, even though it's pretty and it seems to be functional, there's a lot more rigor that needs to be put behind it before it can actually be a real grown-up application.
**Prem:** That's a very, very, very, very pertinent point where you cannot start trusting the AI to do the right thing. You might have given it all sorts of prompts to say, "Okay, you shall practice TDD, you shall write functional-style programs." You'll encapsulate, and all the goodness that comes with good code. When it is under duress-- I mean, it seems to get under duress as well-- It will do things like extests and then say, "Everything's working." If you are not paying attention, that kind of thing will happen.
The point here is that you have to be on your guard all the time. It's like you've got these cars these days with apparently self-drive, and I do not trust the cars because my life is at stake. I almost have to pay a lot more attention when I'm in one of those cars. I own one of those. I'm like, "No, I'm not going to put it in self-pilot, because it actually stresses me out more than when I'm driving myself." I can draw parallels to that kind of thing. You don't know what it's going to do next, and that unpredictability should keep you on your toes, and if you don't remain on your A-game, you might be in for a nasty surprise.
**Lilly:** All I keep thinking is that there is no such thing as vibe maintenance. If you're writing code that you intend to share with others to collaborate on with other humans, and that you want to put in front of users and have it work, you can do that somewhat with some of the coding assistants that are available. That they are a bit of maybe a 1.5 type of thing. They definitely, as you said earlier, Prem, enable people to do things that just simply wouldn't have gotten done in the past, and that they can help a lot with some of the friction involved.
When you put them into a production environment, they evolve, and the world evolves around them. If you don't understand how they're put together, that's where that understanding becomes a crucial part of how you succeed with this in the future and why, I think, we've seen quite a lot of prototypes that have come out that look very slick and that struggle to become production-ready software because the rigor that needs to go into it is not just about what it can do right now.
It's, how do people know how to patch it when there's a vulnerability that comes out of the blue in five months, or when it breaks, who knows how to fix it? We had this issue with the first couple of waves of lowered no-code applications that have come across the industry in general. I think it's even more pronounced now because folks are writing code directly, and pushing code in ways that ostensibly software developers should be able to understand and work with. If nobody in the team has built up the work in context, nobody can maintain it, which is going to be core to getting any value out of it over time or any real use.
**Prem:** Absolutely. On that note, it's fair to say that this style of software development is probably here to stay, or at least feels like it is going to be here for a while, but there are quite a few rough edges. Handle with care is what our message continues to be, it looks like.
**Neal:** Trust, but verify.
**Prem:** Trust, but verify is- [Laughter]
**Lilly:** I like that.
**Prem:** -is exactly right.
**Lilly:** You know I would like that, Neal.
**Prem:** Right. Absolutely. Trust, but verify is apt, and you have to do that all the time. You cannot get your foot off the gas, so to speak. On that note, thank you very much, folks.
**Neal:** It's great chatting with you all again. Let's do this again in another six months and see where vibe coding has turned up then.
**Prem:** Absolutely. Totally-
**Lilly:** Absolutely.
**Prem:** -up for that. Thanks a lot.
**Neal:** Thanks.
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