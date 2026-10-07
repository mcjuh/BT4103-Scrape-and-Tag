<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/unlearning-experimentation-engineering-rigor-agentic-world | Title: Unlearning, experimentation and engineering rigor in an agentic world | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Unlearning, experimentation and engineering rigor in an agentic world 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Ken Mugrage | Podcast guest  Nathen Harvey and Patrick Debois
February 05, 2026 | 39 min 20 sec 
Listen on these platforms
## Brief summary
In a world that's being transformed by AI agents and agentic systems, how do software developers unlearn what they know while also maintaining engineering rigor? 
In an in-person conversation with [Nathen Harvey](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/linkedin.com/in/nathen), Developer Relations Engineer at Google Cloud, and [Patrick Debois](https://www.linkedin.com/in/patrickdebois/), Developer Relations at Tessl, host Ken Mugrage dives into the ways individuals, teams and organizations are walking the line between experimentation and well-established engineering practices as they seek to innovate while ensuring resilience, reliability and security. 
**Thoughtworks is a[platinum sponsor of the 2025 DORA report](https://www.thoughtworks.com/en-us/insights/reports/the-2025-dora-report).**
**Ken:** Hello, everybody. Welcome to another edition of the Thoughtworks Technology Podcast. I'm one of your regular hosts, Ken Mugrage. Very spoiled this week, happened to be in person with a couple of folks I've known for many years. It's great to see you both. I'll let them introduce themselves. First, Nathen Harvey.
**Nathen:** Hi there, Ken. Good to see you. I'm Nathen Harvey. I lead DORA at Google Cloud. You might know of DORA. It's a research program that looks into how do technology-driven teams get better.
**Ken:** Patrick.
**Patrick:** Yes, my name is Patrick. I currently work at Tessl, and I'm usually known for my work around DevOps. I got really excited about this whole Gen AI craze right now, and this is my day-to-day job.
**Ken:** If it's okay, Nathen, I'm going to start with you. Part of the DORA thing is more of a AI focus this year. You talk about it not fixing broken teams, but amplifying what's already going on. Can you expand a little more on that?
**Nathen:** One of the people in our community has described it as you have a high school band, and when you hook up the band to the amplifier, maybe you didn't want to, it just got louder. It didn't get any better, just louder. Then you get a professional band, and you hook them up to an amplifier, and that's great. You can hear them better. They're a richer sound and so forth. What we're seeing in our research is that that's how AI is working. In a team where you've got good flow, good communication that's happening, solid testing, and so forth, when you add AI, throughput and stability are going to improve, you're going to be able to ship more, and so forth.
When you're working in a team where that's not the case, and the canonical example I always go to is, maybe your code review process, or approval process takes a long time. Now you've introduced AI, and you're generating 5x, 10x, 100x lines of code, and you're sending it through that same constraint of that review process, you're going to feel the pain of that review process even more acutely, because it didn't scale with your ability to scale code. That's really what that amplifier effect feels like.
**Ken:** Then, Patrick, you've been talking a lot lately about a shift from producer to a manager of agents, where humans aren't writing the code. If that's the case, where's the engineering happening?
**Patrick:** Like Nathen said, there is a point where you have to judge whether something is good or not, and that's takes practice and learning. Now I wouldn't go per se that far as we need to always have all the best practices at hand. That sounds very weird coming from me, but there is a certain truth to it, is that, sometimes you need to get something out, and it's all about the risk profile, if it's okay to get it out and the risk and the containment is actually okay, then you can push it out without having all the tests and all the rigor.
It is a game that is dependent on that. Now, in addition, while AI is, you need to know what good looks like, I also observe that when you're new to certain things, let's say you're learning a new language, it's actually accelerating your learning phase as well. Now you're stumbling still, maybe through it like you would do in the previous part, but you have almost the tutor that helps you all the time to get better. There is merit in both leaning into engineering and then having it assist you, and making sure you judge that right. We all have to learn it, and it's going to be the same for everybody, like what is that correct judgment that we need to call?
**Nathen:** Both of those instances echo the amplifier effect as well. We just need to get something out. We maybe don't have time to test it. We want to get some fast feedback on that. Do you have the ability to progressively roll out a change? Can you roll it out to a small subset of users and then get feedback, or is everything everyone all at once, because that changes the risk profile, which is exactly what you were talking about there? Then also this idea of using AI as a tutor or a way to help you learn about a new language, a new framework, a new domain, to me, that's the heart of engineering, is this curiosity, and we're always trying to learn.
Not everyone approaches new technology or their work that way. Again, we can leverage the AI to help us learn, or we can ignore the learning and just, "Damn the torpedoes. We're just shipped into production."
**Ken:** We talk about just in society, wage gaps and kind of stuff, and knowledge gaps. Are we in danger here of creating a permanent underclass, the folks that don't have that new journey rigor, and they're just rolling stuff out as fast as they can? Is there a danger here of making the gap get bigger, or what can we do to bring everybody along?
**Patrick:** I personally argue that they're all going to go to a learning phase. Imagine you're just pushing things out, your first failure happens. What do you do? "Oh, I have to have a better way of doing my observability, or see what happens, or deal with the failure, or I had forgotten a backup." People stumble their way. We would do that. Again, depending on the risk, that's the thing you do. That going as you learn is just inherent to that phase, in my opinion.
**Nathen:** I think you're going to continue to see that those failures are where the learning happens. To your point, Ken, are we going to have this stratification of the people that know the old way and are now leveraging AI, and so they're better? I don't know. I never learned how to ride a horse, but I can drive a car really well. I bet when the cars were coming out, there were people that were like, "Those people cannot drive a car until they know how to ride a horse."
I think this is what's so exciting, is that things are changing. You don't have to have been in a data center to know how to use the cloud. In the same way, in the future, you won't have to have written code by hand in order to be a software engineer.
**Patrick:** The ability almost to unlearn is quite important because we accumulate a lot of knowledge while we're learning. There's a certain paradox, you would say, "Oh, I'm getting better and better and better, but in my head I have adding checks, checks, checks that I need to do. Eventually, with all the knowledge, I become slower compared to somebody else who would just get it out." Now there's again a person getting it out, and they get it right. They are faster than us doing it slower. Again, there's a paradox in having all that knowledge that can hinder us in that perspective.
**Nathen:** Yes, for sure.
**Ken:** There's a lot about intent-driven delivery and spec as code. I know, Patrick, you've talked about this. You proposed that specs are the new code in one of your articles or talks recently. If we move towards that intent-driven, do we still need a traditional delivery pipeline? What does that do to how we actually take software from idea to cha-ching, to use John Willis' term?
**Patrick:** I would say that the engineering might happen now more at the layer of the context, and specs are one way of providing the right context for the AI agents to do something. Much like you have an informed person making decisions as they do certain coding and making sure that the agent knows what to do. Now it doesn't stop just on the specs. It will be while it is working as well, "Oh, we didn't have the best practices documented. We didn't have those things."
Now you can say everything that is context is a spec eventually, but it's also all context. Now, the problem we're currently facing in the industry, while I say, "Hey, specs are the new code," is that the systems have limits on context window. Now we are getting better techniques to load in at the right time, the right context, but there is still a lot of fiddling between the models understanding all the context. That's the challenging part. It's not yet true, but it might be more aspirational, but it does give already better results.
If you start writing up documents like we used to do in Waterfall, it's going to have the same effect. They're going to grind to a halt, and they have to comply with everything, and it's not something. There's an iterative process while they're doing inserting, you feed it the right amount of information, and then it does the job. The upfront design is again also with AI failing right now.
**Nathen:** I think it's super fascinating because, as you said, the context windows, and we even think about things like context pollution, are we providing the wrong information or too much information to the bots when we ask them to go and build something? I think techniques like progressive disclosure and working in smaller batches still are really, really important and can get you to a better outcome. I think that that's really fascinating. I also think that when it comes to the context and the specs, these are probably things that we want to start treating as part of our artifacts.
Checking in diversion control. You're already seeing people today sharing their agents.md or cloud.md files out on the internet. The thing that I find so fascinating about that is you have senior engineers with all of this skill that, for the first time ever, maybe are actually writing down, "This is my software development practice." The thing I find fascinating about that in particular is they've been very hesitant to write that down to help a junior engineer become a senior, but they have no hesitation writing it down to help a bot write better code.
The side effect of that is that it's written down in a public place now or in a shared place. You are helping those junior engineers start to build up that practice as well. I think it's certainly an optimistic view of how that's going. I do think that context becomes king, and being really clear about what problem we're trying to solve. I think that context also then can go feed into the feedback mechanisms that we have. The context is there not just to build the application but also to build the verification specs. How do we know that it did what we wanted it to do? That's important.
**Patrick:** The difference, I think, is right now the senior, or whoever engineers who write that context, it helps them, while in the past it helped the others.
**Nathen:** Yes.
**Patrick:** That's why a lot of people are doing this-
**Nathen:** Absolutely. Absolutely.
**Patrick:** -to get there. The versioning is interesting because writing a Claude MDE for yourself is what a lot of people do. It's almost like, "This is the BOP script that worked on his laptop." We've been looking into that, using more rigor, engineering evals to see whether your Claude MDE is actually good. Think of this as a linter that you actually see which of the pieces should be loaded, because, like we mentioned, when you overload that Claude MDE with too much information, you might put best practices, but they might already be in the model. Why are you putting them in there? Then the models evolve.
There's constant engineering on that piece happening. It might be less on the code, but now we have a new discipline and work to be done there.
**Nathen:** It's something that we probably should use software engineering practices to manage.
**Patrick:** Correct.
**Nathen:** It's checked in diversion control. We do code review of this file, and we build that shared understanding of it. I think that's really fascinating. I was just listening to another podcast. I won't mention it because, competition.
**Patrick:** Come on, tell it.
**Nathen:** On this podcast, the creator of ClawdBot was there. He was saying on this open-source project he's working on, "I don't want you to submit pull requests. I want you to open up issues that are a prompt that I can now feed to the agent, because that prompt that you're giving me, that tells me more about your intent. What are you trying to accomplish? I'll let the bot write the code, and then I can judge whether or not that's the right code to weave in." Maybe that's better, and maybe that's a place that we're moving towards. He called them not pull requests, but prompt requests. That's what we're after.
**Ken:** Interesting. Our goal here is to educate the listeners. If it's a useful podcast, please do tell them what it is.
**Nathen:** Yes. It was the Pragmatic Engineer podcast.
**Ken:** They all listen to that one already anyway. I guess, Nathen, we're all about metrics and those kinds of things, especially in your world. We have agents that can do 1000 pull requests. Does deployment frequency even matter anymore?
**Nathen:** Oh, a pull request does not necessarily equal a deploy. Yes, I think deployment frequency does still matter. I think that one of the things that DORA has shown over the years is that those teams that are better at software delivery performance, primarily measured as throughput and stability, those teams tend to have better organizational outcomes, higher revenue, better profit, better customer satisfaction, and, at least as importantly, better well-being for the people on the team. Whether it's an agent that wrote the code or a human that wrote the code, I don't think that changes.
That software delivery is still-- The reason we deliver software is for users. That drives our business forward. Being able to do that in a friction-free way makes it much better for me as a human. I think that the deployment still matters. Now, to your point, though, now we can have 100 pull requests. Maybe going back to what I said earlier, what's your process after the pull request has been opened? 100 instead of one might actually be harmful for your organization. I think it's important that we're thinking about the entire system, not just how quickly can we write code.
**Patrick:** I want to add to that because I agree that these traditional metrics, they stay useful, but one of the upcoming new ones, especially, no pun intended, with the context engineering, is how many touches does your AI need, given from your question, to actually get something that you want? That's something else that you can start to measure. That's pre-delivery, but it's part of the whole chain of delivering those things.
Then another interesting aspect that I saw is that while we're delivering pieces, and there's often business pressure on requests from end users, like, "I want this to be built," there are some tools that allow you almost to have the end user vibe code something on top of your application to actually see what they want it to build and then feed that back to you. It's not the prompts, but it's almost like they give you working prototype-
**Nathen:** There's a prototype.
**Patrick:** -on top of your product. It's like the ultimate feature discovery of people vibe coding on your platform. Anyway, it's fascinating.
**Nathen:** I love it. Super interesting times.
**Ken:** If intent is the primary driver, how do we prevent a future where no one on the team knows what's going on when something fails? I didn't say if, I said when. When an agent fails, if the intent was the driver, how do they understand the underlying system?
**Nathen:** I think there's two parts to the answer, maybe. The first part being, does it matter? I'm starting to see and participate in some conversations where we're questioning, does the way that we construct code, does that matter anymore? The way that we name a function, the cyclomatic complexity. If the agents can deal with it, let the agents deal with it. Maybe it doesn't matter, and yes, things are going to fail. Guess what? You're going to have an agent along, hopefully, or AI to help you troubleshoot that failure.
That said, I've dealt with enough failure in my lifetime with technology.
Yes, you want someone that understands how it works. Maybe there's another analogy here with automobiles. I certainly don't know how to fix everything in my car, but I can take it to a trained mechanic. Maybe there's something to that.
**Patrick** : If you're the engineer or you're the mechanic, you still got to know. A lot of people say, "We don't care anymore about the internals, and the agent just needs to know, and we just need to ask the right questions." It's hard to ask the right questions if you actually don't know what you need. That's definitely challenging. I would say that almost the AI needs to keep us able to understand when the failure happened. There's a concept called the moldable exception that actually adapts itself to show to the engineer to explain what it did in their terms, in their understanding, and not how it was built. That's an important feature of showing and learning from that.
Besides that, I often make the analogy between-- we've done years of automation in DevOps. I think it was John Allspaw who said, "Okay, you have your build system, and it works, and you automated that. That's great." Then it's been working for, let's say, six months, and then it fails, and nobody knows anymore how to fix it because we haven't done this enough. It's a little bit where the field of chaos engineering came in, inducing errors and failures, almost like a fireman that have to train and still understand.
We might have to almost train more to be ready for when it fails. Again, it's a risk game. It's okay if you're not investing in that if your risk is low, but if it's high, you need to be ready when that happened. That's the analogy that I think is suitable in this.
**Nathen:** I think the other thing that's true is we've always had specialties as well. If there's a certain class of failure in the application that I built, maybe it's a networking failure. I don't know anything about networking. I can't solve that. I'm going to have to go to a peer who's the network engineer. That's been the story of engineering forever. It's rarely an individual sport. It's nearly always a team sport. We saw that with DevOps. Software engineers that have no idea how the production infrastructure is configured, and maybe a system administrator who has no idea how that code came into being but can troubleshoot everything about the infrastructure.
I think we'll continue to see that specialty being required, and we'll see specialist agents that come and support each one of those roles, potentially.
**Ken:** It's interesting you said that because we always used to think of platform engineering as a tool to reduce the cognitive load in many times. Now, is the platform's job just to feed context, again, pun intended in this case? Is it more of a knowledge graph than an infrastructure now? What is a platform anymore?
**Patrick:** Wow, that's a wide question.
**Ken:** Yes, it is.
**Nathen:** I do think, to your point, the AI is going to give you better solutions when it has better context. One of the things that DORA researched and published last year in 2025 was the DORA AI capabilities model. Two of the capabilities there are having strong internal data platforms and making sure that the LLMs have access to those platforms. Maybe that does become-- Certainly part of the role of a platform is making sure that our data inventory-- We have good, well-connected data and that that LLM has access to that data, which includes, obviously data, but also things like policy.
What are our compliance or security regulations that we have to follow? Let's make sure that the LLM can see that as part of its context. I think the platform team, and in fact a strong internal developer platform, was one of those capabilities as well that unlocks AI. That's how you scale it across the organization to go from this team or this pocket of engineers over here is having a great time with AI. How do we make sure that we're seeing that across the entire organization?
**Patrick:** I do think if you think of a traditional platform team, they provide more infrastructural pieces or services these days. Yes, they can provide the LLM, and they can provide storage for your context, but I think the challenge there is who's going to actually maintain the knowledge across the whole org, that's the role. It's not in the data people right now because they're deeper and making sure it's consistent across, and who learned from all the things that people are doing.
Imagine you have all their coding sessions, how do you connect them together that if five developers hit the same issue that actually we're serving this as, "This is a piece that's missing in our context, and we need to improve that." That new knowledge observability across the agent context, that's a fascinating new role, and is it the platform? No, there's platforms all turtles down, but it feels like a new layer and a new flow of data and knowledge.
**Ken:** I like that, knowledge observability.
**Nathen:** Yes, absolutely.
**Ken:** Nathen, you already touched on it, but DORA looking more at developer sentiment, well-being, mental health, those types of things. How do people avoid it going from code toil to review toil?
**Nathen:** Boy, how do you avoid that? I think you have to avoid it intentionally. You have to build the right systems in place. In fact, I would say that if-- Maybe this advice isn't good today, but certainly two years ago, as you were just starting to think about, "Let's bring some AI into our software development lifecycle," I would've encouraged you to start with having it do code reviews for you. Don't start with it having to write code for you, because maybe you don't trust it yet. Build some trust by having AI do code reviews.
Now, it's not going to replace the human code review, but it will be the first pass on that code review. The thing that is absolutely obvious about AI doing code review is it will get to the code review much faster than a human will every single time, and it will be a comprehensive code review. Now, it might not catch everything, you probably still want that human code review, but I know for a fact just in my own daily work, I've done pull requests that an agent has code reviewed, and it has caught things that I can virtually guarantee a human would've missed. Now, these are small things like a typo, a misspelled word here, but the agent caught it, and I know that a human would not have seen that.
**Patrick:** I would say there's probably a spectrum of people doing coding. There's people who say, "Give me a ticket, and I'll solve it for you," or there's people at the other spectrum is like, "Okay, I want to build the best system, and I want to get value to the customer." I would say if you're in the last one, it is so addictive. Even if you get a lot of pull requests, you just want to get it out, you just want to make it better.
It's not a chore, it's actually almost like addictive, similar to the TDD loop, like, "Okay, can I get it out? Do they want that? Do they want that?" It can be very exhausting as well, but it's not a chore, and for others, it is indeed like a chore. It depends on where you are, I guess, in the spectrum, and what's your passion? Are you really caring about the business value, or is your job like, "Okay, I like to code, but this syntax is important to me, and that's why I'm really annoyed without all that AI coming in?"
**Ken:** Patrick, you've been quoted as saying expertise becomes the differentiator in a world where AI can handle the syntax. I don't know if it's a correct quote, but in a world where AI can handle the syntax, what specific skills should people be looking at? For listeners like a junior engineer or whatever, what are the skills that they should be looking at to make themselves more marketable, frankly?
**Patrick:** It's the skill to learn and it's similar to-- I don't know what the AI US terms or English terms are, like educational system, but you can have a very practical education that says how to do one through three, or you can have a broader education that actually says, think about a problem and problem-solving. I think in this case, you need to drive the AI so it's more at the layer of having problem-solving, figuring what you want versus the actual thing.
It's a skill you can learn, but it's probably more valuable with this new work than it was in the past, where they didn't let you take the time to actually figure it out. Now it's almost part of your loop to figure it out, which I like.
**Nathen:** Yes, I definitely agree with that. I think the other thing, though, that is true today is that when AI generates something for us, whether that's code or an email or a document, the people that are in the best position to evaluate the efficacy of that thing that it just generated are the people that understand, the people that know the code, know, I don't know, whatever framework you're working in, know the idiomatic way of writing that language.
You can look at what the AI has generated and determine is that idiomatic, is that following best practices? Is that right? An expert is going to always be an expert evaluator as well. With that, I think that a junior engineer or someone who wants to write a lot more software, whether it's them that writes it with their fingers or they're using an AI agent to do so, I think one of the things that's always been true is the best way to become a better software engineer, a better coder, is to read more code and then write more code, but reading over writing.
Just go read more code and be able to evaluate, "Is this code that the AI has given me, is that slop or is that good code?" and try to build up the intuition for that because I think at the end of the day, that's really what it comes down to.
**Patrick:** There's an interesting thing happening in a way that if you would start from a blank slate, and you ask 15 engineers to go writing, and they're all like, "Yes, but I think we should do that," and it's almost like inhibiting them from actually writing any of the code because it needs to be perfect, but once somebody has written, they would all argue, "Change this, please do that." It's the same thing with writing a blog post, doing it from a blank slate is hard and correcting something else.
That's also quite interesting use of an AI. It's like this is the first seed, and then you adapt, and you adapt, but you didn't have to go for the first boilerplate, the first thing to go there. If it gets it wrong, you're still spending a lot of time in correcting it. That's again, seems to be getting better, and the more context you give it, the less time you spend in that as well.
**Nathen:** Yes. One of the best ways to end those arguments over, like, "Let's just tweak this, tweak that," working code wins. Is this code from AI? Is it working? Is it doing what we expect it to do? Great. It wins. At least it wins for today, and we'll adjust it over time. It will always be an iterative practice. I don't think any of us expects to write a line of code and have that line of code running for 20, 30, or 100 years. Now, unfortunately, it's true that probably code that we wrote 20 years ago is still running in production, but that was definitely not our intent at the time.
**Patrick:** I had an interesting week. We had a new launch, and it was very hectic. It's like a typical launch, as it shouldn't happen, releasing features at the last minute. Everybody was giving feedback, and the usual flow would've been, "Create a ticket, there's some triage, and we're going to pick it up." What we just started doing is, "Okay, here's a ticket, brief chat on Slack, and then, okay, please AI bot, build a PR, let's review." It wasn't waiting until somebody picked it up. It was instantly in the chat, having that approval, "Okay, release."
That's just an insane feeling to see the speed at which you can ship things. I was writing docs, and I was not looking at the code, and I was constantly asking my AI, "Is my documentation in check with my code? Is it in check with my code?" I couldn't have done this in that close and speed loop without the AI. It's just so powerful. While I understand all the limitations, I think it's just here to stay to make us better.
**Ken:** I think most of my questions have been, but this is going to be a very leading question. From the same kind of thing, from an upskilling perspective, but at an organizational level, so I'm a CTO, I'm a VP of engineering, or whatever, the easy answer is, "Oh, be intentional," but how? What do organizations do to keep their people upskilled? Does Slack time play into it? That's where it's leading, because I think it does, frankly. What are the concrete things that a manager listening can do to make sure their teams are allowed to keep up?
**Nathen:** I think it's pretty easy. You just buy the licenses, and then everything works.
**Patrick:** As always.
**Ken:** Says the Google person.
**Patrick:** Wait, you have licenses?
**Nathen:** No, obviously, there are a bunch of things that have to happen. One of the things that I think is truer than it's been probably in my entire career is that things are moving so, so quickly. I do worry sometimes that organizations are going to rush to standardize their tools and their workflows, and by the time they standardize, they're going to be six, 12, 18 months behind what's state-of-the-art today.
I think that, to your point, we have to build in some additional slack. We have to adjust the expectations that we have on our engineering teams to allow for that slack. How do you fill that slack? It might be hackathons. It's definitely time to experiment and learn, and share what we are learning with each other across maybe an internal community of practice, something along those lines. I think that's super, super important.
**Patrick:** I think as a manager, you are an enabler there. Anything you can do on removing friction, limiting it to one tool, it doesn't work in this chaotic period, so you will have to approve multiples and allow people to play with it. You can have rules and ground rules to what applies where, but you've got to give that. Budget, it sounds weird, and we don't have unlimited budget, but it definitely helps in kind of like not having to think about tokens and spending while you are experimenting. That's again another thing. Then it's almost like rewarding it, bring out the cool stories what people did, bring in external expertise, bring in external stories, the learning.
I think the best learning is actually doing it in your day-to-day job. If you're allowed to do that, if you have a process in place, if you just have a few champions that you get going, I think that's similar to any change in an organization, whether that was DevOps or Agile or anything. You find the champions, you nurture them, you remove the friction points, and then you start building that community in practice. Now, bear in mind, whatever you think is now good will be outdated in a couple of months.
**Nathen:** Yes.
**Patrick:** It is evolving in a way that we are thinking about the problem different, about the solution different, and that's normal in this chaotic maturing period. This is probably the fastest that it's happened ever in the industry, where in the past, we had some time to absorb this, but now it's so fast, and that's why you've got to start today to do it.
**Nathen:** I just want to add one thing to the managers there. You said the manager should help bring out the successes. In the same way, they should be celebrating the failures. Something went wrong. Let's talk about that openly so that we can all learn as much as possible from that failure, where the AI took a misstep, where our context wasn't quite right for the AI. Whatever it was, we learn a lot from failures, and it can be a huge waste to sweep those failures under the rug. We want to learn from them and amplify those lessons across the organization.
**Ken:** There was a huge study at Google, gosh, might be close to a decade ago now, that said that psychological safety was the number one indicator of a successful team. Has that changed? The ability to talk about failures is that--
**Patrick:** I think that is the same.
**Nathen:** I would agree that it is the same. Yes.
**Ken:** Also, what role does corporate policy have here? Google talks about clear AI stances, as opposed to chasing the latest LLM or whatever. What role does corporate policy have in helping here?
**Nathen:** In our research, one of the things that we found, as you said, is that a clear and well-communicated AI stance is important. Now, DORA doesn't weigh in or have a strong opinion about what that stance should be, other than that it is clear and well communicated, because what we find in our research, when it's not, is that you have people that are maybe using some AI that they're not sure if they are allowed to, and that adds some additional friction and stress onto that worker. They are maybe delivering more, but maybe they are doing it in a way that they don't feel super good about.
The policy has to be, like I said, clear and communicated. Hopefully, it's not, "Thou shalt not use AI anywhere in this organization." If that's your clear and communicated policy, I can almost guarantee that someone is violating your policy. You have to be a little bit more open to that. To Patrick's point, though, I think that there has to be-- maybe it's not, "You can use any tool that you want," but "We do have a collection of three, five, seven different tools that you can play with, and let's go learn from each one of those tools, and eventually, we can start to converge. Today is not the time for convergence."
**Patrick:** Yes, clarity is important in that case. There's a certain level of experimentation that you will never capture with clarity, unfortunately.
**Nathen:** Yes.
**Patrick:** In a way, if you make it too broad, it feels bland. If you make it too specific, it becomes narrow. I'm not the policy writer, but it is an art to get that balance right.
**Nathen:** Absolutely.
**Ken:** It feels like we spent decades trying to make software more predictable. Should we just give up? Should we just understand it as a complex adaptive system, and we just need to constantly evolve with it or is predictability still hopeful or are we hopeful for predictability, put it that way?
**Patrick:** I think it's two different things. Making software more predictable I think is still a goal, but again, within the limits of the risk appetite, whether you want that or not. Then the delivery process itself has also a certain predictability, but that might also change in a way that we might not care about certain features as we did in the past, and we care about the other features now. That balancing act is still going there.
**Nathen:** Yes, I would agree with that. I think that as we're starting to accelerate our ability to do things, that gives us an opportunity to remember why are we doing these things. We're doing them for the users of the applications that we're building and maybe that gives us some time to get even closer as an engineer to what is it that the user's trying to accomplish. Back to your idea of this user vibe coded a solution on top of my application, that's an amazing form of user feedback that I can now do something with. I think allowing engineers to get much, much closer to that actual problem that we're trying to solve, I think that's really, really important.
**Patrick:** In my four patterns of AI native dev, I said, where a developer is become a little bit of an ops a reviewer, like what can go into production, they become a little bit of a QA by saying, "Here's are my requirements, here's my intent." They become a little bit of a product manager by saying, "Actually, I've tested it with users and this is actually the business value. Then they hopefully got our data as well, so they become the data analyst.
Now, good engineers don't stay in their development lane. They learn that they actually need to go across the other boundaries. I think AI is helping us as the engineer to do that and bear with us because the product engineers are coming into the coding space. [laughs] The QA are coming in this space. We're all changing, and the lines are blurring, but it means we're overlapping also in the domain and can help each other [crosstalk].
**Nathen:** Yes. Maybe the bots that are always on can help us start to explore those other domains a little bit more. Without putting a burden on my peers, I can put that burden onto the AI as I go and explore that other domain and then frankly, I can ask smarter questions to my human peers in the organization.
**Patrick:** Even more? [Laughter]
**Ken:** For a closing question, I'll let each of you individually, you all live in this every day, and talking to different organizations and what have you. I'll start with you, Patrick. What's something I did not ask you that you wish I had that you want people to know?
**Patrick:** I think the focus right now is still too technical, and it should be my opinion around the knowledge management. Probably within a year or two, that's the only thing we're going to talk about, in my opinion.
**Ken:** Nathen?
**Nathen:** Just going back to the whole amplifier metaphor, I think it's really important that you understand how your systems work today and then make a decision. Are we here to augment how those systems are working, maybe to improve those systems or are we here to radically change and think again from scratch, how are we going to build up these systems and these processes? That goes for something like software delivery. Are we going to improve our current software delivery process or are we going to reimagine a brand new software delivery process where we don't have any constraints.
The answer is probably yes in your organization, but you have to be intentional about where are we doing which one of those things, and then that probably comes back to your risk appetite.
**Ken:** Great. I want to thank you both for taking the time. I know that Patrick just came off a very long flight and Nathen just came off a shorter flight, but still not short. [laughs] Thank you very much for your time, both.
**Patrick:** Thank you, Ken.
**Nathen:** Absolutely. It's a lot of fun, Ken. Thanks.
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