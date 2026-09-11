<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/themes-technology-radar-vol-31 | Title: Themes from Technology Radar Vol.31 | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Themes from Technology Radar Vol.31 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas | Podcast guest  Ken Mugrage and Neal Ford
October 17, 2024 | 39 min 39 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/themes-technology-radar-vol-31#Transcript)
Listen on these platforms
## Brief summary
Volume 31 of the Technology Radar will be released on October 23, 2024. As always, it will feature 100+ technologies and techniques that we've been using with clients around the world. Alongside them will be a set of key themes that emerged during the process of putting it together. We think they offer another way into the Radar and give a unique insight on some of the most interesting issues impacting the software industry. 
In this episode of the Technology Podcast we discuss them: coding assistance antipatterns, Rust being anything but rusty, the rise of WebAssembly and what we describe as the "cambrian explosion of generative AI tools." To do so, Alexey Boas is joined by guests and podcast regulars Ken Mugrage and Neal Ford. Ken and Neal provide an insight into the conversations that happened during the process, and offer their perspective on the implications of these themes for the wider tech industry. 
## Episode transcript
**Alexey Boas:** Hello, and welcome to the Thoughtworks Technology Podcast. My name is Alexey, I'm speaking to you from Santiago in Chile, and I will be your host this time. This time I'm joined by Ken Mugrage and Neal Ford. Hello, Ken. 
**Ken Mugrage:** Hi. Nice to see everybody again. I'm normally one of the hosts as well, but going to be playing the guest role a little bit. I'm based just outside of Seattle, Washington, the United States.
**Alexey:** Great to have you with us, Ken. Hi, Neal. How are you doing?
**Neal Ford:** I'm good. Neal Ford, based in Atlanta, also one of your regular hosts. As you can tell, we're a bunch that likes to talk to each other a lot because we act as hosts and guests a lot for our podcast. Lo and behold today, three at least sometimes hosts, but two acting in the role of guests for a very good reason. We're not just randomly here as guests, but we're here to talk about something that we actually know something about.
**Alexey:** Yes. That's something I'm particularly excited about, and it's a fun topic we have today. We're here this time to talk about the themes of the Thoughtworks Technology Radar Volume 31, and both of you can-- and you are part of the Doppler group. That is the group that puts together the Radar and writes the Radar. Very exciting to have you here talking about the themes. Just for the sake of transparency and to be very honest with all the listeners, we're recording this before the Radar publication, so it's an insider's view about the process to some extent.
Also, some of the things might change before the publication comes out. Before we dig into the themes, Ken, could you, for the sake of the listeners who don't know the Radar, maybe tell a little bit about what the Radar is and how it comes about?
**Ken:** Yes, sure. I'd be happy to, and I'll ask Neal to keep me honest because although I've been using and attached to the Radar for many years, this is my first time actually contributing to creating it, which is quite the view. What is it? Basically, it's a report that we put out twice a year. It's a snapshot of different areas. We section into tools, techniques, platforms, languages, and frameworks that our teams are using. How are we using them? Are we assessing them? Are we thinking about them? Are we trying them out on real, paid projects? Are we adopting them? Are we using them for client work? Is it on hold, so we're not using it?
It started out as a communication mechanism well over a decade ago of us just being able to share in a global organization what's going on, what are the experiences of other Thoughtworkers around the globe. Then, 31 episodes ago or 31 issues ago, we started publishing it to the public. It's very useful. I definitely would check it out. Just thoughtworks.com/radar, if I remember correctly. Then, also just a little teaser, there is another podcast out there on building your own radar. On this one, we're going to talk about ours and some of the themes that came up, but we highly encourage people to build your own because your context is different than ours. (Do watch for that episode as well!)
**Alexey:** Yes, thanks a lot, Ken. Personally, I quite love the process as well. I've had the opportunity of seeing that applied in a particular project company, and the process building it, the discussion it generates is just amazing. Quite recommended. Might be interesting to have a look at that other episode. Neal, maybe you can tell us about what the themes are and how are the themes crafted from the discussions. Maybe, you can give us that insider's view before we delve into the specifics.
**Neal:** Absolutely. To highlight one of the things that Ken said, this is basically a curated list of things that come from our project. There's a group of people that gather twice a year to curate and put this thing together. If you go to thoughtworks.com/radar, it's the most recent version of our Radar, but the people who get together in that group, the only thing that we create are the little summary write-ups for each one of the items that show up on our Radar, which are called blips. You'll hear the term blip throughout this episode. A blip is one of the items on our Radar. The nomination process for those blips always come from our teams that are actually solving problems.
This is a unique perspective on the global software development ecosystem because it's purely worker derived. It's all from the ground up. We gather together as a group and filter through all these nominated things, see where the commonalities are, think about things that are appropriate for our Radar that are in scope, that make sense, or things that are outside of our scope. This is a week-long discussion, very intense, as Ken can now attest to. [chuckles] It's a very, very exhausting week because there's a lot of very intense discussions to try to figure this stuff out.
Inevitably during the week, and this wasn't true for every Radar, but three or four radars in, we noticed that over the conversations this week, we kept mentioning X. X doesn't show up anywhere on the Radar, but it was a huge part of our conversation. We had this idea, "Well, let's summarize our conversations around this idea of themes." For every Radar, we have three to five themes. These are the things that kept coming up over and over within that meeting that generated the most interesting conversation.
Very often, half or more of the things that led to the theme didn't actually make it on the Radar but led to a very interesting, intense, and nuanced conversation, and therefore was one of the themes of our Radar. This is the actual only organic content created by this group that puts the Radar together. It's done à la minute. It's done at the very end of the week. Just after we've figured out what the Radar is going to look like, that's when we summarize and put together these themes and write them up. For Volume 31 of our Technology Radar, we have four themes, which is our typical sweet spot. We shoot for three to five, and we managed to come up with exactly four this time.
Let's talk about what our four themes are for Volume 31. This will come as a surprise to absolutely no one listening to this podcast, that one of the things that we talked about a lot in this Radar session is generative AI and how it's used to assist software development in all its different facets. We talked about LLMs, but much more conversation about the surrounding ecosystem, more about that coming up and one of the other themes that had to do with AI.
The first of our themes, and this is where Alexey was talking about, we haven't hammered down the titles yet because we're still in the drafting phase of putting the final version of our Radar together, but the first one is going to deal with AI anti-patterns. That title is too broad. We want to limit it to AI anti-patterns for inadvertent AI anti-patterns maybe, or anti-patterns for overconfidence in AI leading to anti-patterns, or some wording like that. You'll get to see what our final wordsmithing led to, but the idea behind this theme was mostly around techniques.
That's one of the categories in our Radar, is techniques, around techniques that we see some anti-patterns starting to pop up. Patterns, of course, but also anti-patterns, including really common notion that you can do actual pair programming with an AI and replace part of the pair with a human. That's just not true. Our colleague Birgitta has written about this extensively, but that's one of the common anti-patterns that, "Oh, you get the same benefit of pair programming by using generative AI as a pair." That's not true at all, so that's a common anti-pattern that we see. Overreliance on coding assistance suggestions. we trust it too much.
"Hey, it's magical. It must be magical all the time." You run into a problem there with trusting it too much and then because it was generated, not going back and doing the kind of due diligence you would do, even if another human created it because, "Oh, LLM created it. It must be okay. It must work." That's obviously a big problem. The last one of these that we called out specifically, that we suspected on our last Radar, but have concrete evidence for now is code bases are growing in size because generative AI when it solves problems tends to do so via brute-force, which means bigger code bases.
We see things like pull requests getting bigger on average and check-ins getting bigger on average. Of course, that puts an overall burden on the entire engineering process for testing and validation, and just the sheer bulk of code can become overwhelming.
**Ken:** I think one other discussion that was interesting on this one, it's not core to it, but it was adjacent, is not a new concept. It was the concept of the uncanny valley of the thing that looks like something that you're familiar with. You assume it's the same. Really, got popular in software development around mobile apps however many years ago where, "Oh, yes. A mobile app and it looks just like the webpage. Therefore, it must operate like a webpage, but it doesn't." The problem with the generative AI stuff, or one of a long list of potential problems, is that they look and sound like an authoritative source. You say, "Hey, how should I do this?"
They come back with all the confidence of a veteran and say, "Like this." As we all know, they might be making it up because the real purpose of an LLM is to sound authoritative. It's not to give you an accurate answer. People forget that. It's a large language model, not a large information model. It was just really interesting that we see these anti-patterns all the time where developers ask it a question. It gives them a very logical-sounding answer, a reasonable-sounding answer, they accept it, and they move on. It turns out later that 2 + 2 actually doesn't equal 7. Like I said, blips, it didn't make it, but we're definitely part of this.
**Alexey:** It's interesting. You mentioned Birgitta, and she talks a lot about cognitive biases in the life of a developer. It's interesting how some of those kick in. As you were saying, Ken, we tend to trust something that comes out of an LLM just because it seems authoritative. Once you've seen a solution, it might become harder to think of a different, more creative solution. There's also an anchoring process as part of that and things like that. Being mindful of that broader biases phenomenon might be yet even more important when using those tools.
**Neal:** I was going to say, when possible, we try to add a call to action to our themes if there is a useful outcome from the discussion, rather than just ranting about something that we noticed during our meeting! This one was nominated actually as a separate theme and got wrapped into this one, which also happens a lot. Part of the reason it got wrapped into this in our solution to this problem of the AI anti-patterns, whatever the title becomes, is to double down on good engineering practices, testing, verification, deployment pipelines. Don't start short-circuiting those things just because AI is making things more magical.
In fact, we're actually big proponents of-- Back in the Building Evolutionary Architectures book, we defined this idea of an architectural fitness function. One of those categories are these internal code quality, the structure of your code, cyclomatic complexity. How complex is this function or method? When you talk to human developers about that, they yawn and roll their eyes because we know we shouldn't create hyper-complex methods or functions, but AIs haven't gotten that message. Generative AI will solve something with 50 switch statements versus using something like strategy design pattern.
That's where some of those structural fitness functions really come in handy to put some guardrails on your generated code to make sure that it's not using ridiculous brute-force or something else that you would not accept from a human developer and refactor some of that as it happens rather than let it build up a huge pile of a technical debt. That's this idea of doubling down on good engineering practices and other proven governance and validation techniques. As you lean more on generated code, you need some sort of corresponding check to make sure that you're not, as Ken was saying, accidentally over trusting the thing and leading yourself into a bad trap.
**Alexey:** These tools do not replace things like pair programming, so it's going back to those things, pair programming, TDD. The mindset is not trying to get rid of those techniques to go faster in a way, but instead to rely even more on them so that you can make better use of those tools. Is that right?
**Neal:** Yes. My a little overworn and a little weak metaphor for this has always been the spreadsheet, that before spreadsheets, accountants had to do math by hand and adding machines. It took forever. When spreadsheets came along, it made them massively more productive. It didn't teach them accounting principles. It just got rid of the busywork part of their job. That's really what generative AI should be for us, is like a spreadsheet getting rid of the busywork, pattern matching, and things that they are really good at and let humans still do the logic part, as Ken said, that generative AI is particularly bad at.
Even though it's particularly good at acting like it knows what it's talking about, very often, it doesn't. Having the twin, use it for what it's good for, and then validate what it produces for you, I think is not bad advice in at least the current state of the art.
**Ken:** The other one that jumped out at me on this one, and then I realized we have to move on. Again, a little bit of a spoiler to the last theme is that we see a lot of people trying to use AI just for the coding part of software development. They bought somewhat into the tools thing of, "Oh, yes, if I use this coding assistant, I'm going to be faster." Another thing that Birgitta has written a lot about is, it's also helping come up with the stories and threat modeling and that sort of thing. Spoiler to the last one, but it really is that it's more than just a coding assistant.
It's not actually a terribly good coding assistant, so it's a good thing that it's more than that.
**Alexey:** One, I wonder if any of that came up during the conversations, but I saw some interesting analogies on how should you approach these tools. It's not a cogeneration tool. It's more something you interact with. There was a discussion of using that as a rubber duck to try to validate your thinking and go through that thinking once again or even as an alien companion. The alien part is interesting because you have to know that it's someone who doesn't really understand our world and really not someone actually or something that doesn't really understand things, so can just hallucinate or things like that.
There are some interesting metaphors that can be useful when actually using those tools.
**Neal:** I think one, in particular, outside of the coding assistance is using it for gap in risk analysis. Don't let it generate ideas. Let it look at your ideas and see if it can find gaps or missing pieces. I know a lot of our business analysts are using this to find places where, "Oh, should we be paying attention to this versus that?" I think that's where it's good versus raw knowledge generation. Check your work.
**Alexey:** What's the next theme that came up in the discussions?
**Ken:** I find this one particularly interesting because as a first-time participant in the process, I'll be honest, it didn't jump out to me. That's why what Neal said about looking at what happened in the conversation that didn't become a blip is so important because the pattern, it immediately jumped out to everybody else there. Myself and one other person were like, "Yes, this comes up a lot, but okay." We didn't catch what it was. It's the fact that Rust has gradually become the system programming language of choice. It's showing up in lots of places.
People are talking about a Python tool, "Oh, it's written in Rust." "Oh, there's this embedded work that we're doing." "Oh, we're doing it in Rust." Really curious. I'm curious from Neal, you mentioned when we were talking earlier, this has been coming up for a couple years now this way. It just snuck into our consciousness.
**Neal:** We have several really big fans of Rust on the Radar as an assistance programming language. This is one of those things that cumulatively, it seems like we as a group have said the word Rust more than most of the other technical words. I was saying before our call as we were chatting the word Postgres, and that almost became a theme. Every Radar, we end up talking about Postgres one way or the other. Rust is the one that we highlighted on this one because as Ken mentioned, we keep seeing that, "Oh, well, there's a part of the Python ecosystem that could be a lot more performant. It's been rewritten by this tool, and it's written in Rust."
The epithet that we put in the theme that is most commonly associated with Rust is blazingly fast. That has a special place in our heart as the Radar because you see these terms that come up in marketing all the time in the technology ecosystem, Webscale was one of those. About five years ago, everything was Webscale. Now everything is blazingly fast. Apparently, that's the thing that's most valuable to people right now is blazingly fast. Rust happens to be blazingly fast, which is why we tongue-in-cheek call that out on the Radar.
This will mean very little to most of the people that are the audience for our Radar, both for context and also region, but I really wanted to name this theme Rust Never Sleeps because it's a great old saying that Rust never goes away. It's constantly working in the background. It's also the famous name of a rock album from the 1970s. That was voted down by-- Very often, we're trying to create this for an international audience, so some things that we talk about just don't translate well to an international audience. The most famous example of that, this is parenthetical, was many radars ago, we created this concept we call the security sandwich.
The idea was don't just do security at the beginning and the end, and don't do anything in the middle like a sandwich. Boy, did that not translate into other cultures at all. Our translators fought mightily with that. We have to be very careful about two contextualized titles or something like that. Outside of that, Rust is a great language, and it's that sweet spot of good abstractions, fantastic performance, good ecosystem, and support. Like I say, we have a lot of fans, and it's very popular and continues to be.
**Alexey:** Yes. Neal, I was one of the translators struggling with the security sandwich at the time! [chuckles] Fun to remember that!
**Neal:** We love our metaphors, but sometimes they go way too far. We got to be careful about that.
**Alexey:** They're good usually. I like them. The thing about Rust, it's more of recognizing a process that has been going on for a long time than a specific inflection point that we're seeing happening now. It's more of a longer journey to cross. It's not going to make it into the theme's name, but it never sleeps analogy conveys that message. It's something that's been there for a while, and we're seeing it just continuing to be there for a while.
**Neal:** I love the metaphor because it's slowly working in the background and visibly, but it's just always there. That's the idea of Rust Never Sleeps. I thought that was a nice metaphorical title, but it alas got voted down! [chuckles] I think the reason it bubbled up and became a theme on this one and not for example, the previous Radar or two ago is because it really did come up even more this time than it has in previous radars. It was notable how many times it came up. We started noticing these patterns all the time during the meeting. This is definitely one of those that popped up this time.
**Alexey:** How about the third theme then?
**Neal:** We love our acronyms in the technology world. The gradual rise of Wasm or WebAssembly, this is another big surprise, something that's been percolating in the background for a long time now, but has gradually been gaining steam. Suddenly, all four major browsers now support Wasm 1.0. What is WebAssembly? It's a binary instruction format for a stack-based virtual machine, which does not sound like something that a lot of people would be interested in. It's a very nuts and bolts kind of a thing.
The thing that's fascinating about it are the implications of being able to run things within browser sandboxes because Wasm is basically a virtual machine that runs entirely inside a browser using JavaScript. You can translate existing applications into the Wasm binary format and have them run. During our meeting, we actually saw a post by PragDave Thomas, well-known figure in the technology world, who said that he had just seen a demo of getting Mastodon to run inside a Wasm sandbox.
Mastodon is a very large Ruby on Rails application with C-extensions to the Ruby language using a Postgres database on the back end, and they bundle the entire thing up into a Wasm bundle and ran it in Chrome. That's stunning. It really does give you the kind of native execution speed and browser independence that we've been wanting forever because these really are self-contained sandbox containers that run completely inside the browser, which means they honor the browser security models and that kind of stuff. This is a really interesting possibility for a portable and cross-platform development.
It's fascinating because it's so powerful, but it's so in the weeds in terms of technology because you have to learn two languages to use Wasm. You have to learn Wasm itself, and then you have to learn another programming language that produces Wasm binary. It's almost like having to learn-- You don't have to learn Java by code, use a Java compiler, but it's similar. It's the bite code format, and then some other language produces that. I think that's part of the complexity of adopting this, and this is not something that I think is going to impact day by day development because it's very low-level capabilities. The kinds of things that's going to enable teams to do, particularly taking legacy applications and run them in better environments is really, really exciting.
**Ken:** I also think there's an opportunity here for somewhat new use cases. We just recently recorded, our listeners may have heard it, an episode on DuckDB. That's a specialized database that's often uses an embedded database for doing analytics. Some of our data scientists and data engineers are really excited about it. If you look at the website, "Oh, it runs in Linux and Mac and whatever," it also runs in Wasm. A data scientist can have their database and do a bunch of what the things that they need to do right there in their browser without having to install anything and that sort of thing.
During the discussions, we had our discussions, I was like, "Wait. Security, I don't want everything running that way." Everyone is like, "No, one of the strongest sandboxes you have on your system is your browser." Then the ease of use, the gray-haired person in me that's been doing web development longer than I care to admit scares me a little bit, but then it's also really exciting. Just I'm curious to see where this goes.
**Neal:** To Ken's point, I think you're going to start seeing a lot of things targeted as a WebAssembly, as one of the back ends they run against, which means that it'll run completely inside a browser. This is a philosophical question that didn't really come up during the meeting, but I thought about after the fact, are browsers now the new mainframe terminal? If you can run the entire application in your browser, how is that different from some sort of terminal emulator or something like that that's running the entire thing locally? I don't know. [chuckles]
We keep moving computer around in our ecosystem backwards and forwards to the server, to the middle, the client. This is just another interesting move to the client, and it opens up new possibilities.
**Ken:** What was the Sun Microsystems byline? The network is the computer, or the system is the computer or something like that?
**Neal:** Exactly. Yes.
**Alexey:** Amazing.
**Neal:** It's job security for all of us technologists. We keep moving targets around, so we'll never be done. Wasm though is fascinating. 
**Alexey:** All right. How about the last one? Ken, you had hinted that it's AI-related as well, so what is it exactly?
**Ken:** Yes. Again, as Neal said with the first one as a surprise to no one, the working title here is the Cambrian explosion of the AI-adjacent ecosystem. All of the tools that are used in AI and by this, I don't think we mean the ones that just put AI in their marketing material. There's a lot of tools that are basically the same thing they were four or five years ago that now are an AI tool. It's like, "Okay, how did that happen?" Really, I hinted at it with that it's more than just a coding earlier, so it's the full path to production. Guardrails systems to make sure that you're doing the right thing in compliance and security came up a lot, vector databases, prompting tools.
Just, there's all sorts of things that are evolving that frankly need to evolve. If you look at any revolution, if you look at the history of the, I know this is very geo-based, but the Gold Rush in the United States, a few people made their fortune mining gold, but most of the people who made a fortune built shovels. It's the same thing. It's just really interesting to see the explosion of tools around it, and it's very easy, by the way, to be cynical about this. It's very easy to call it venture capital driven development, or what have you.
There certainly is some of that, but there is also some things that our listeners should really pay attention to, things that will help them throughout the entire life cycle.
**Neal:** I like your mining analogy, and Levi Strauss is one of those that made a lot of money off of something that wasn't mining tools. This is exactly the reason the analogy is so apt, is because mining for gold is cool, but to mine for gold, you need stuff. You need picks. You need pants. You need pans. There are a lot of mundane details until you get to kneel in the river and actually pan for gold, and that's exactly the same with generative AI.
"Okay. It's great that the talking dog does all these tricks. Now, we need to put the talking dog into production. Oh, that requires a whole lot of mundane details about evals and guardrails and vector databases and enhancements, and all those things. That's the ecosystem we're talking about, and we expected it to grow at about the same rate as we've seen some of the other generative AI stuff. We were surprised to see exactly how explosive that growth was. Part of it, I think, is because you can't really tinker with LLMs. They're black boxes, and they are what they are. As developers, we build stuff around them to address them.
We've mentioned Birgitta's name a bunch of times here because she's one of the AI experts at Thoughtworks, and we've been talking about AI a lot. One of the great public services that she does during the course of the Radar is to curate the AI-related blips that we're talking about and organize them so that we can get a handle on it overall before the thing is over. Here are some of the categories that she came up with to put blips in. To give you a perspective, 38% of our Radar when we were done were AI-related blips. No other topic except AI in past radars has ever dominated that much of it.
JavaScript probably got close in its heyday, but here are the categories that we came up with that included some of these blips. AI-assisted software development, of course, but we also have local inference, which is inference done on things like a transformer.js, which is inference done inside JavaScript or on devices, different model types, fine-tuning LLMs. We have several of those on trial. Cloud services that address AI one way or the other, including things like agent builders in the cloud. RAG of course is a very popular topic and a lot of things around RAG augmented output for generative AI, evals and guardrails, which are ways to validate what's going on with your language model.
Structured outputs, which are things that transform things that come out of it. Also, building agents. We actually saw a lot of growth in the space of, "Okay, the language model comes up with some sort of language-based conclusion. Let's wire that into an API that now takes action on something. That's all these agent-based systems. There are a bunch of frameworks that allow you to wire LLM output to APIs to varying degrees of sophistication and adventurousness. Prompt optimization and tracking, of course. Information retrieval, vector databases, that's where RAG, et cetera, and all that augmentation come in, and observability for LLM applications.
Can we get a view into the black box to see what the thing is actually doing? Those are just the categories of AI stuff, which I think supports this idea that there's a sort of Cambrian explosion of things around that ecosystem.
**Alexey:** That's amazing. I like the Gold Rush analogy. I think it makes sense. Even getting more philosophical, I think Brian Arthur said that the creation of technology propels the creation of more technology because you need more technology to support the technology itself. It's almost seeing that process happening live, so it's amazing.
**Ken:** Also, it was interesting during the conversations how often even that categorization was up for debate. Does this thing belong here or there, or what have you? The reason I bring that up is I think it's important for organizations to decide, "Okay, we're going to trial this thing, or we're going to adopt this thing." What is the problem that it's trying to solve for us and agree on what that problem is? What we want to avoid is the thing that we've all seen where, "Hey, did you write the unit test?" "Yes, sure did." The thing they wrote doesn't look anything like a unit test to me. It looks like something completely different.
If you're using one of these things and, "Oh, okay, I'm using this as guardrails to make sure that we don't do this thing we're not supposed to do," but somebody else thinks you're using it as RAG to make sure your answers are more accurate or what have you, that's a problem. I know it's school for 12 year olds, but I like putting definitions on the wall. I like putting up a thing that says, "This is what unit test means here. This is what functional test means here," and I think this is a category where that's true. "Hey, we've chosen this part of the AI-adjacent ecosystem. We chose it to solve this problem. That's what we should use it for."
By all means, experiment, see what else it can do, et cetera, but it's going to be pretty important that people understand why they're doing these things, or what's going to invariably happen is they're going to end up with 17 tools that do the same thing and zero tools to do the thing they were trying to do.
**Neal:** We're seeing some of that in the coding assistance space now, which is really, really crowded with all these different variations. Some of us who were around for the JavaScript chaos on the Radar, this feels like that only probably a little bit worse than even the JavaScript because there for a while. When JavaScript was declared the one true language, everybody was creating JavaScript frameworks for one kind or another, and that finally calmed down some. We're seeing the same thing here, and this one has potential to get even crazier than the JavaScript ecosystem did before it calmed down.
We'll see what the next Radar brings. It's always interesting to see what's coming up next. We are fighting the seeming inevitable trajectory to make 99% of our Technology Radar about AI. We won't do that. I don't think it will ever completely dominate our ecosystem. Boy, it comes up in conversations a lot because it's such a rich area, and there's so much innovation, just explosive innovation happening in that space.
**Alexey:** All right. We covered the four themes. We talked about AI antipatterns, Rust, Wasm growing and this Cambrian explosion of AI ecosystems. Before we close, just since you were part of the discussions, anything that almost made it as a theme or any other topic that was very present in the discussion, something like that, that you could share with us?
**Neal:** The one I was talking about that I actually nominated as a theme, didn't quite make it, was Postgres because that's the other thing that seems to come up constantly in our conversations over the years. Lots and lots of Postgres stuff. We noticed a lot of stuff around Databricks actually. We didn't end up making that a theme because we didn't realize if it's just an increasing awareness within Thoughtworks or whether that's really an industry trend or whether it's just a Thoughtworks trend. We didn't want to comment on that more broadly, but we do see a lot of nominated blips and a lot of work in Databricks within Thoughtworks right now.
Those are the main ones. Like I say, several of these got merged together like the advice to double down on good engineering practices. Part of the reason we didn't put that as a theme is because of several radars ago. We had almost that as a theme, so we didn't want to repeat ourselves too much. Probably the main one that got a lot of votes and ended up not quite making it is a big discussion about documentation and the struggle that everybody has about documenting things, particularly in large organizations. We had a bunch of blips writing about that, about proposed solutions, and nobody has seen a really great solution for that kind of institutional knowledge management.
We were thinking about putting a theme about that, but we didn't really have a good solution to this problem. We were just noticing the problem. We tend to try to make things a little more actual than that, but that was definitely a big part of the conversation this time.
**Ken:** Yes, I think that's the other plug for the other podcast we're doing on creating your own radar, is that's one of the things that came out of it is that for all of these things, it's the discussion, it's the working together on the things, that is the valuable part. At least in the moment, the thing we don't have a good thing for, what about six months from now? How do we see the change record? How do we see why they came up with that? Listen to the other episode about in the moment and stay tuned as we solve the problem of documentation in enterprises, which I'm sure we'll do any day now.
**Neal:**[chuckles] It's a great teaser.
**Alexey:** Amazing. I guess that brings us to the end of this episode. Thank you very much Ken and Neal for joining and for sharing with us, and thank you all listeners for joining the conversation. It was a great conversation and amazing to have you with us. Thank you so much.
**Neal:** Yes, thanks.
**Ken:** Thank you.
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
[ Read the Tech Radar ](https://www.thoughtworks.com/en-th/radar)