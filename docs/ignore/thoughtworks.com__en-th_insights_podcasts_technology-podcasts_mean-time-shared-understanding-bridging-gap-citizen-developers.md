<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/mean-time-shared-understanding-bridging-gap-citizen-developers | Title: Mean time to shared understanding: Bridging the gap between citizen developers and developers | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Mean time to shared understanding 
Bridging the gap between citizen developers and developers
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Ken Mugrage | Podcast guest  Christopher Hastings and Scott Davies
September 18, 2025 | 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/mean-time-shared-understanding-bridging-gap-citizen-developers#Transcript)
Listen on these platforms
## Brief summary
Although the concept of the 'citizen developer' isn't new, with the rise of AI the relationship between those building software without much technical experience and seasoned software developers is becoming more significant. That's not to say there's conflict exactly, but there are often competing interests and demands — which can lead to tension, organizational friction and governance challenges. 
On this episode of the Technology Podcast, host Ken Mugrage facilitates a debate (of sorts) between Christopher Hastings, Global Tech Product Lead at Thoughtworks (and citizen developer) and Scott Davies, Head of Technology for Thoughtworks Europe (very much in the developer camp). 
They discuss the needs and interests of both sides, how to avoid regressing to the dark ages of shadow IT and how citizen developers can be properly empowered by engineering teams. 
## Episode transcript
**Ken Mugrage:** Hi, everybody. This is Ken Mugrage. Thank you for joining another episode of the Thoughtworks Technology Podcast. Kind of a cool thing today. A few of us are here in our Thoughtworks Berlin office talking about AI for software development and a bunch of things. We set up a little bit of a cage match that people that you think, I don't know, have some controversy between them, but it turns out, they actually like each other. What we're going to talk today about is empowering the citizen developer and what we can do to make both sides actually win, if there are sides. Got two great guests today. I'm going to let them introduce themselves. I'll ask Scott Davis first.
**Scott Davies:** Hi, I'm Scott Davies. I'm head of tech for Thoughtworks Europe.
**Christopher Hastings:** Hi, I'm Christopher Hastings. I'm a global tech product lead.
**Ken:** Basically, what we have here is Christopher runs a lot of our research around AIFSD and as such, correct me if I'm wrong, prototypes like lots of applications and things like that, but you don't consider yourself a developer. Is that right?
**Christopher:** I am not a developer. My background of being a developer is I took one Python class and the rest of it has been what can I Google, throw up in a Jupyter Notebook, and survive from there. If you ask me about anything more complicated than that, I make Scott angry.
**Ken:** As a head of technology, you're responsible for some of our technical quality and that sort of thing. There's the phrases that people throw out like shadow IT and those types of things. Does that scare you?
**Ken:** How? If he's off in a corner doing something, then how are you getting that feedback? How is it helping you?
**Scott:** Particularly in the space of prototyping things, these are great tools now. We'll talk a bit probably about tool chains in a bit, but now we're in the situation where you can iterate and build something that you can show somebody in minutes. That used to take, for a Fidelity-like prototype, that would take days normally, but you and I can riff on something now, you can show me quick, give me a bit of feedback, I can talk to you about some other things and we can go again. We can just keep going around that really quickly. That used to take so long and it also required lots of synchronous time from both of us.
**Christopher:** As a product manager, one of the things that I'm trying to do to communicate about if I'm effective in my role is not just being able to talk to whoever our user or customer is about what it is they want to build and why. It's also to understand, on the other side of the table, what's your job, what tools are you using, how do you work, how do they play. The last thing on the planet I would rather do is to go read documentation about how to get something working. I do need to understand those tools and I need to be able to see how they work and have a mental model of that.
**Scott:** It's the same coming the other way, right? I need to understand what goals you're trying to achieve and what you're trying to do, your business process, your interactions, all those things, but that shouldn't be a barrier to us getting going. I think this is a way of you showing me something far quicker, we can iterate and go back, we can talk about how we can make it enterprise-grade, we can put the guardrails in place, we can do all that, and we can get the corporate look and feel and all those other things.
**Christopher:** We're still talking about the happy case, right? The happy case being you and I can get on the same page, but I think there is a bleeding edge that we are rapidly coming into, whereas me having prototyping tools or access to-- however that looks like, causes problems for people on the technical side of things because I come back and without the understanding of depth, I come back and say, "Hey, I made this thing. It took me 15 minutes. Why is it taking you guys so long?" Or, "Hey, I've done this. Just make it like that." You go, turns out, you actually don't know how to design anything. I go, but I see it. From my limitations of understanding from my role, I'm a bit more technical than many.
**Ken:** What are the things he needs to be aware of that-- I mean, this is a developer that does think, I can just launch this on my own now.
**Scott:** I think there's a whole bunch of facets. There's the security angle, who has access to data, how you control it, should we be updating it, should it go beyond the boundaries of our organization, are you using tools that are outside the corporate boundary, is our data leaking out? All those kind of things. Usual privacy concerns.
Then there's the corporate standards. We've got a glossary. We've got a main language that we use interchangeably. If we're going to use the tool or whatever across the enterprise, it shouldn't be your language for things. It should be our language for things. It's got this, this, this. We all agree that's an order. If it doesn't have this, it's not an order. Great. The other thing is understanding how it fits in with the rest of the IT estate. For example, you built tool and it's great, but if it updates something and you expect something to happen in another system, we need to consider how that's going to happen as well and what the transfer of data is.
**Ken:** What's that process look like? You mentioned guardrails and things like that. Is that supported by-- the other thing you mentioned was toolchains. Is that supported by part of the toolchain? Is that a manual, you're checking boxes? What's that look like? How do we help people?
**Scott:** When we talk about these things, I think where we're at right now with certainly the types of tools that you're using are evolving at an incredible rate. There's a new kid on the block every few days. From an enterprise perspective, that's interesting because you've got the, how do we update this tool that you've built in six months time? Some of the toolchains are quite fragile. You might have used three or four different tools and taken something that ChatGPT, split it out, and put it into something else to generate prompt for something else. It's putting a tool that's developed an app for you.
It's like from a technologist background, I'm like, "How do I recreate that? How do I make sure that we've not just generated something that's a one-off?" What I want to do is work together with you and we'll work out how to do that. You might show me the app. It's a tool for understanding, isn't it, right? I want to understand your business process, how you work. I think traditionally what we've done, we've spent a lot of time building systems for people and expecting them to adapt the ways they work to the way the system works.
We talk a lot about that and how that's wrong. Users, people have a goal and an objective to complete. Sometimes these systems get in the way. Having the feedback from you that this is how you need to work is an opportunity. It's not like a threaten from that bit. What we do need to do is work out the guardrails around data, security, ownership, lifecycle of the app. That's where we need to work together.
**Christopher:** The best lifecycle of an app for me in my world is zero days. I don't want to maintain something. I don't want to think about security. I don't want to think about guardrails. If you ask me about security, I'm not going to even know where to begin. There are things in this experience that are dangerous for me. One is a good example of MCPs. There's an XKCD comic that I remember. The entire internet is built with all these building blocks and down on the right corner is this one thing that is a package maintained by a single individual.
For me, I go, okay, cool, but those, from what my brief understanding of security is that's also tons of vulnerabilities. Now I have the ability to call MCPs, download them anywhere. It's like popping into GitHub and saying, "Oh, this MCP that all I have to do is apparently drop in this very easy interface magically can do the thing I want." Now it's on my local machine. It has a lot of the permissions that I would have access to. Suddenly, I don't even know, but I'm going to just go and Google and Claude and other things. To a certain extent, I don't want you to know that I'm here. As I said, I don't want to start figuring out how do I green light stuff because I'm trying to create and prototype.
**Scott:** If we go back a little bit, you don't have to go back too far to think about the, there was the shadow IT thing, right? I don't view this as shadow IT because shadow IT was people's response to the IT department not being responsive enough. It was their way of getting shit done and just getting on with things. This isn't that. This is a tool for communicating and for us to interact and get to where you need to get to. To support you and the outcomes you need for the business. The quicker we can do that, the better it can be. Because as you say, your concerns are different. We've talked about security. We've talked about a few other things. There's cost as well to the organization.
**Ken:** That's what I actually wanted to get to. In a little bit of a role reversal, Christopher, just because of your particular position, you actually were part of the team that managed which tools to look at and so forth and control some of the API keys. Scott had a situation where he was trying a new tool and he ran out of credits before he even actually started the app. How do people manage that?
**Christopher:** I think there's going to be a couple of long-term strategies that we're seeing that are effective. Right now, a lot of what we're doing is just relying on what the backend for the tool is. Within Anthropic, they have something right now set up where you can set it up within workspaces and they manage it and you just dump people in and say, "Hey, here's what you've got." Now, there have been a couple of moments where a single person can say, and use Opus and run up those credits and take it for everybody else. In which case we say, "All right, number one, you were warned. Number two, you're now quarantined. Number three, you're out." That's how that works.
You do have to be careful on it because I'm not going to understand what does a token cost really look like. What would help people in my role or people like me who have less familiarity is if there was a better concept of what does my design workflow need to look like? Maybe for another podcast, there's a conversation about if you're going from user experience to designing user workflows, designing prototypes, and now I have a web dev and that's sort of a design tool chain. I think there's also another workflow for people that are designing things that are much more backend, where you still have users and customers though, where it looks something like I start in Claude Code, I have a massive design chat, I mean design in the strategic sense rather than something with UI.
I have this chat, figure out what I want. I try and break it down to the right requirements and prompts and things like that. Then later, I pop over and go to some other tool to then develop the code itself. How do I make sure that I'm using the tokens in the right way rather than trying build the whole enchilada. I'm from Texas. That's sort of phrase we use. Building the whole thing in one shot and say, "All right, let me try this." Now, oh, that didn't work. Let me try it again and build the whole thing. There is a iterative product-centric thin slicing that has to occur.
**Scott:** We need to work together on things like data as well because you're not just going to, in the enterprise, just say, "Right, we open up every data source there is just so that we encourage people to do this kind of development." Other people might be using that. You might be slowing down the website. It might be all these other things. We need to put the guardrails in place. We need to work together. I can help you identify the sources of data as well. You wouldn't necessarily know where they are in the organization.
**Christopher:** I think there is a place where it does start to blend over into almost shadow IT. There may be an upskilling path to say, "How do you better create a developer out of someone like me who literally has one Python class, hates reading documentation, and doesn't even know necessarily at times where to begin with the rich history of what Thoughtworks has brought to the table." I don't know where to begin. I don't know that I should. How do I then do things in the right way, hand it off at the right time? I just want to just create something in a lab that can maybe get three other people's, 5 or 10 other people's feedback to go, this is great and useful, and then go knock on somebody's door and say, "Can you make this nice and shiny?"
**Ken:** He's done a proof of concept. You now understand what he's trying to do. Are you taking his code and--
**Scott:** The first bit is the communication of the idea. The intent and the output that you want, or the outcome. It's taking that, I need to go away and identify where the date comes from, do all that kind of stuff. What's the impact in the integration and all the other systems? I'm going to look at exactly what you've done, and we're going to get designers to look at the screens. We're going to get them made the way that fits in with the culprit brands and everything else. It doesn't mean I'm going to 100% take your code.
**Christopher:** In fact, I've got an example of that. The idea from the DORA metrics being like the mean time to value. I think there's something else here, and I'm not suggesting this to be like an official metric. It's like mean time to shared understanding. That's really what I want to reduce because I had a development team I was working with. I'm very familiar with concepts behind AI. I know things about model training and how to fine tune, and I know how you can use prompts and build MCPs and things around that.
I was working with some developers that didn't have as much more modern experience as I did because I get really addicted. They're onboarding, and people are trying to upscale it all the time, but they didn't have the same shared understanding that I did about, this is what I want, this is what I think it can do, this is how I think it can do it. I found myself struggling to communicate that. For what was meant to be a quick and dirty prototype to start our thin slicing and sort of build up that value, I didn't feel like they were getting me.
I'm doing this on my ability to communicate rather than their ability to understand, just to be clear. I'm not trying to throw anybody on the bus. I literally woke up at like 4:30 one morning and I said, "I've got to do this better." I hopped on with Claude, I created a virtual environment with a Jupyter Notebook, and already, I'm further down this chain than some product people. Let me just create these two, grab an API key that I've got. I'm not doing secrets management, I'm doing this very, very poorly. I'm just saying, all right, now let me put this all in Jupyter Notebook cells and build off this workflow so I can describe the experience and prototype the experience so that by the time I get down to, here are my requirements, here are my NFRs, here's the test cases, I've played with it enough that I know that I'm asking real IT people, not me, for what I want. Because I don't even know that. I'm doing my best, but I'm going to be wrong.
**Scott:** You don't know the architectural decisions I've made, right? About how we're going to run, what languages we support and operate, what skills we've got. You talked a bit about this, like what's the handover? Where does that happen? You want this to live, right? You don't want this to be a, hey, work this week and you come to me next week and say, "Scott, I've stopped working."
**Christopher:** On the second part of that was that I went to the team and I said, "Here's what I've made." They said, "You did that?" I said, "Well, Claude and I. My buddy Claude." They said, "Okay, but you did that?" I said, "Yes. They went, "I've never seen any prototyping done in quite this way, like this, by someone who was not in a developer role." They said, "One, that's amazing." The second question was, "Do I have to use your code? Because I don't know anything about how to structure it and principles of things like clean code and other things." I understand the concept, right? You want your code readable, but I'm not going to tell you the most elegant compute efficient way to structure that. I just wanted it to work, to illustrate, can this be what I have?
**Scott:** It's not going to have the tests in it, the unit tests and all the automation that we expect. But what you can start to bake in, which I find really valuable, are examples. Give me an example of what it looks like in the real world. Oh, an order number looks like that. Oh, it's got hyphens in it. I didn't realize it had hyphens in it. Those eight digits, oh, that's a letter at the end. Give him real examples you can give without waiting for the system to give me examples. I can start to construct tests from those as well because then when I show it to you, does it work for the orders that I have? Oh, yes, look.
**Ken:** We mentioned a little bit earlier about guardrails and Christopher used the trigger word of API keys. Give our listeners some concrete examples of guardrails you can put in that they should be doing in their enterprise to make sure that things like authentication keys aren't leaking out. What are some concrete things that our folks can take you into work tomorrow?
**Scott:** Wow, that's a big list.
**Ken:** It's a big list.
**Scott:** There's like keys in general. You don't want a shared key, for example, that's used for lots of different things, because then typically what happens is somebody assigns it higher permissions than it needs to have, and then you get all sorts of things happening that shouldn't happen. There's no traceability then when something goes wrong, what's broken, you might pass on the key to your friend, all these things can happen. We spent a lot of time thinking about the security posture of the enterprise, it's not something we want to compromise. We still want to go fast. We still want to get feedback. We still want to do all these things.
**Christopher:** You guys are familiar with the idea of a minimum viable product. Is there not some version of a minimum viable product for citizen developers, is the phrase I've been using, it describes my role. Is there not something like that exists that says, "Here's how you do management of your environment variables, here's how you set it, here's how you change it, here's how you get access to it, here's how you set up a virtual environment." These sort of like basic, if you get these four things right, this covers 80% of the scenarios that we need for security and privacy that are non-malicious.
**Ken:** That's where I was wondering, we were talking earlier offline, honestly, with Scott about empowering, not just helping and being happy about it, but actually empowering the citizen developer. Are there things you can give them that are already the framework of the scaffolding?
**Scott:** There's no reason why I can't give you that, or I couldn't give you like mock data that we've got somewhere else, or perhaps we've got like a test environment, and I can share with you the data model from that environment and explain to you a bit about how it works, you get out of it what you want, and you say, "Hey, where's this?" I'm going to signpost where that is. At the same time, I mean, we talk a lot about sensible defaults and we talk about it in the development space for like, these are expectations that we all have of each other. When we come together about ways of working, we can extend those things. We can provide guides that help you do what you need to do without getting in the way. We can then double check. I can come and talk to you and say, "Hey, have you done this? Have you looked about where the keys come from or the data access that you need? We can have a discussion. A placeholder for a discussion. I think that's really important.
**Christopher:** Are there things you need from me? As a citizen developer, I want to produce things regularly and I want to be able to take it back to delivery teams to at least do a proof of concept or maybe to scale within the organization to some degree, not necessarily like a massive production thing because not my wheelhouse. What do you need from me?
**Scott:** I could give you the style guide that we have for the organization so at least the things that you produce look like the rest of the things that we have.
**Christopher:** Is that for the code? Tell me what a style guide would do for me.
**Scott:** When you produce these prototypes, they look like the rest of the organizational ones. The right branding, the logos in the right space, fonts of the right signage.
**Ken:** Why is that important? I think I know, but for our audience, they're like, well, I just want the form to be right. Why is that important?
**Scott:** I think it's important, not from a, like you said before, I'm not going to 100% use what you've given me, but it sets the expectation about how it's going to work and it will help with communication because somebody needs to make sure, hey, is that going to work on a mobile? Yes. I love your design. You've got 400 things on the screen. We need to break that down because on a mobile, that won't work. Using the style guide, you'll at least get all the different size formats that we support, rotation, all those things.
**Christopher:** I hear you, but I don't want to. The reason that I'm saying that is because I'm just trying to get across a simple concept. Then the moment you asked me to do a style guide, I go, "I don't know how to plug it in." If it's a import style guide--
**Scott:** We will help you do that!
**Christopher:** Even then, I feel like I'm moving out of my lane of just trying to discover and communicate what is valuable to build. For me, I go, I don't want to. If there is, almost, one-click solutions that can give me, in another language I've heard described as, lik,e a design system, how do I import that into whatever I'm doing and whether that's co-designed and what people are… To a certain extent, I'm going to go, "I don't care." I can't care because I don't have the wisdom to know where that domain boundary is, where I go down, and I'm going to get frustrated and it's going to keep me from doing my regular job. I'm doing what I feel like is trying to do yours.
**Scott:** Yes. You're trying to like go through that innovation bubble, aren't you? Trying to like quickly get an idea across or show something and get back to your day job. Yes, I get that.
**Christopher:** That said, I'm going to argue against myself now, perhaps. I do think there is something that is there about how do we make sure that we can still make it easy to hand off to you. Internally to Thoughtworks, we have done some really cool work around design systems and using those in some of these prototyping. I think there's a lot of other apps that are relying on those same kind of things. I feel like it's almost like, is there a wishlist that I should have? Then in that wishlist, how do I make it easy for me to pick up within certain tool stacks?
**Scott:** Depends on what tool stack you use. Obviously, we can do things like accelerators. We can give you a prompt that's a starter point that already drags in the design system, all the other assets we have. Maybe it can include all the domain terms that we use in our business so that there's no, we call this A, and you call it a B. The other thing I think I'd be really interested in when I come and talk to you is, this is great, you've done this thing. What else in our organization does it interact with or who?
The thing that you've done, does it relate to somebody in accounts? Does it do things? What's the workflow? Where does this data go? What do you need to happen after or before, or the constraints around what we're trying to do? That's the discussion we need to go through when we have this wonderful sharing moment. We're aligned, right? We're on the same page now about what you're trying to achieve. You're telling me a bit about the process and your ways of working.
**Ken:** You all want to work together, but it's not a silver bullet. I think there's an expectation among some folks. I mean, hype is hype, but there's an expectation that, hey, we just get these tools and it's magic and everyone's happy. There's still work to be done around understanding, right? Where are the lines?
**Scott:** In the past, this would have taken, for you to share with me, would have taken a long time. To get to the level of understanding, like you said, the minimum shared understanding, would have taken probably weeks. We can probably get there in a couple of iterations in days, or hours. I think that's the advancement, is that the communication sharing bit is where we're really at right now. Obviously, we're exploring AIFSD usage at the code level. This is the, I think this is the emerging bit now.
**Ken:** Christopher, you mentioned, and I know this, you're more technical than a lot of product managers and so forth, but for the product managers that are listening, how did they get started? I see people trying a different tool every week and they never get good with any of them. Does it matter very much? How do people start?
**Christopher:** My short answer would be, I'll kick part of this over to Scott. My short answer is go get a subscription to Claude, get your organization to give you the subscription. You have the chat interface interaction because that has been a key unlock. I say this for a couple of reasons and for both that path and that tool. The path is because if you are doing it in an organization level or if you opt out, as I understand the rules have changed recently, if you do those two things, you can then say, don't train on my data. That checks the boxes for Scott around security. Fantastic.
Now, the second piece of that is that it has so many built-in prototype visualization tools automatically that I can do it. It will write code and then show it to me what it looks like. I can do that to then generate and say, "Oh, let me iterate here. Let me iterate here." Quickly do this in a way that is natural language for me without me needing to know anything about API keys, environmental variables, or anything else like that. That would be my starting place.
**Scott:** I agree. I think it's like, the barrier to you sharing some of that shouldn't be having to learn Figma. You shouldn't have to learn a tool that feels really unfamiliar and it's got sharp edges. Like you say, natural language. You can build up as well. I think whatever tools you use, you need to be able to build up. You need to like, oh, okay, I've given you something. You show me something that's not quite what I wanted. I'll build on that. I'll give you a bit more information and you can go around that loop quicker.
I think those are the things. You don't want to spend hours learning a tool. Yes, we can all go on YouTube and watch a how-to-use video for an hour or whatever, but you don't want to do that every time a new tool comes out. If the model of interaction for you to get what you want is natural language, that's going to be a lot easier. You can use it when the tooling changes. You can save those independently of the tool if you want. They all save them anyway, but if you want to get out of that tool and go somewhere else.
**Christopher:** The one piece of advice that I would offer for anybody on models is that they've got a couple of different types. You've got reasoning models, Anthropic, and you've got Opus, but if you've got ChatGPT, you've got GPT-5 and all these others. I would say at first blush, don't believe that a bigger model is going to magically solve the problem that you're going to address. There's something in prompting called one-shot prompting, multi-shot, trying to figure that out. I think as a product person, it is, take your thinnest slice, try to illustrate one's concept that you think is at the core of which you want to be able to visualize, and then evolve.
Then when you hit a wall, which you will hit, honestly, the best practical advice is ask Claude to say, "Hey, tell me where I'm at, rewrite a prompt for me to get me to where I am." Now that you and I have had our back and forth and we've chatted through our requirements, give me a new prompt, kill it, start a new chat, and fire it up. Otherwise, you start to get degradation because context windows get too big and everything else. Practically, that's the other place that I would start.
**Ken:** I guess for closing, I'm going to put you both in a spot a little bit and ask you to assume identities because the truth is, we work for a company who we develop software. Regardless of what your role is, our thing is developing software. That's not the case for all of our listeners. Some of them are banks. Pretend that you're a product manager that's not doing software development-related products and that you're an IT person that doesn't trust an accountant to write software. What's the one thing you want the accountant, I'll start with Scott, what's the one thing you want the accountant to know that's going to help them take better advantage of this?
**Scott:** I think some of it is expectation. It comes back to what you say. I would say, don't accept the first thing that comes back. Go around again, iterate, try something different, ask the question in a different way, prompt in a different way, and try and get some different things. Again, you will find all of these tools. It's very easy as well to get distracted, don't get me wrong. You can end up down some great rabbit holes.
I think trying to describe what you're trying to achieve in several different ways and refining, like you said, you go through this mode of refining the interaction, and then you get to a point where you think, I'm good enough now, can I compact all this and get it into a distinct message? It's like giving a presentation. You need to tell people what you're going to tell them, you tell them, and then you tell them what you already told them, but each of those is at a different fidelity.
**Ken:** Then, Christopher, I know you have a background in education and economics, so you're that banker. Why is it so important to you to get this stuff out fast? What do you need from him?
**Christopher:** Well, one, and what I hear Scott describing is diving deep into prompt engineering, and there's some resources we can link to that can help people who are getting started. Quite honestly, I need to know that there's a stance in the organization, that they're there to help me do my job, because typically, the experience of somebody who is on the other side of it is that it's going to take way too long to get my ticket responded to, it's not really going to be helpful, they're going to deny and recycle for the smallest little thing.
IT does not seem like a friendly organization. I honestly don't want them to know I'm even doing anything. The biggest analogy that I've got to what I think we've seen, history repeats itself, everything we're seeing now we've already seen before, I think the biggest in-organization development of that is the way people use Microsoft Excel. That is citizen developers bypassing dashboards, bypassing a data organization to send information around and change it. I think we're going to see a lot of the same patterns there.
**Scott:** I don't want to go back to shadow IT. I want to enable you. I need to be there. I need to be on the front foot because this is going to happen.
**Ken:** I mean, we need to embrace it. It's funny, people, I think, assume that a company like the Thoughtworks would be afraid of this. It sounds like we still need each other.
**Scott:** It goes all the way back, doesn't it, to the Agile manifesto? I'd rather have interactions, the big documents, things like that. Feedback's the most valuable thing. The more we do of that, the more we understand each other, because we're yet to results.
**Christopher:** I want to go back. I want to talk about the Agile manifesto for a second. One of the counter trends that we're seeing here, we want to be agile. We want to be user responsive. We want to be able to collect feedback, and we're trying to move away from what was waterfall development and the horrors of, we have to document everything. The flip side of that that I'm seeing is that we have to get everything right into a prompt in order to get it to generate things the right way. How do we face that as helping different developers? I think there's something there, and I didn't want to-- the Agile manifesto triggered it, but I don't know that this is the conversation for it.
**Scott:** We don't necessarily work in pairs of the same role, so why don't I take the same approach? I'll come and pair with you. I'll help you understand where I'm coming from. You can help me understand what you're trying to achieve, or we'll get closer and closer, and we'll get there quicker. We will get there quicker. I don't think you have to bear the brunt, and I don't have to bear the brunt of receiving something that's thrown over the wall, because that's what nobody wants, and I don't want to go back to the shadow IT thing. Let's embrace it. Let's get together. Let's do this. We can now do this in days and hours, not months, weeks. Hopefully as well, you're going to knock on my door again next time as opposed to I'm not speaking to those guys again.
**Ken:** Well, we are IT. We'll find a way to make them unhappy. I want to thank you both. I know, as I mentioned at the start, we've had a long week of meetings this week. They've been energizing and tiring at the same time, so I really appreciate you taking the time to talk to our listeners.
**Christopher:** Thank you, Scott. Thank you, Ken.
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
[ Read Technology Radar ](https://www.thoughtworks.com/radar)
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