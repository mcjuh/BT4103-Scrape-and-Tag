<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/mitigating-cognitive-bias-when-coding | Title: Mitigating cognitive bias when coding | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Mitigating cognitive bias when coding 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Alexey Boas and Rebecca Parsons | Podcast guest  Birgitta Böckeler
May 19, 2022 | 34:47 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/mitigating-cognitive-bias-when-coding#Transcript)
Listen on these platforms
## Brief summary
We’re all subject to cognitive biases. And whether we’re aware of them or not, they can have a profound impact on the code we write — especially when working in an agile environment, where we have to constantly deal with uncertainties. We take a deep dive into where our biases emerge, the impacts they can have and how we can mitigate them to improve the quality of our code.
#### Full transcript
**Alexey Boas** : Hello, and welcome to the Thoughtworks Technology Podcast. My name is Alexey. I'm speaking from Santiago in Chile, and I will be one of your hosts, this time together with Rebecca Parsons. Hello, Rebecca.
**Rebecca Parsons** : Hello, everyone. This is Rebecca Parsons and I am coming to you from the Pacific Northwest. We're talking to our colleague today. Birgitta. Birgitta, would you like to introduce yourself?
**Birgitta Böckeler** : Yes, hi, everybody, I'm Birgitta Böckeler. I am based in Germany. I am one of the technical principals at Thoughtworks in Germany for Thoughtworks.
**Alexey** : That's wonderful. We're very happy to have you with us this time, Birgitta. Thank you so much. The theme this time is cognitive biases. I'm sure many people have heard of them. It's going to be thrilling to explore some of the connection and impact of them to software development and the day-to-day life of developers.
Birgitta, I know you are very passionate about the theme, personally seen at least a couple of talks that you gave on the subject, quite excited to-- looking forward to talk to you a little bit more on the topic. We all know it's a complex topic, right? Maybe you can start by talking a little bit about what cognitive biases are. Can we start with the definition sorts?
**Birgitta** : Yes. You're right, it is a complex topic. I'm a developer by trade, right? I'm also kind of an amateur at it, right? I think it's becoming more and more commonly talked about. For example, you might have heard a lot of people mention this book, Thinking, Fast and Slow, over the past few years. It feels to me like almost every second talk I see at a software development conference, somebody mentions this book in some context.
This is also one of the sources of where this idea of cognitive biases comes from, which is behavioral economics. The author of the book, Daniel Kahneman, was one of the originators of the school of thought. Basically, the context is that, as humans, we usually like to think that we're very rational, right? In the cases where maybe we're not rational or logical, it has to do somehow with emotions, that we're being emotional. That's why we can think rationally or logically.
What Daniel Kahneman and his colleagues and people in the field and around the '60s, I think, came up with what's this theory that maybe we're not that rational, as rational as we like to think we are, but that there are these things happening in our brains, these little errors, these little bugs, you might say that kind of affect our thinking and make us sometimes make errors, little errors in judgment. I'm introducing these as bugs or errors, but on the other side, they're actually also "features" because they kind of keep us sane.
They help us deal with the world with all of the information that is always coming at us, and our brain always has to take so many quick decisions and interpret everything that's going on around us. Those things usually keep us sane, but then there are situations where we also make little misjudgments and it's important for us, to know that maybe we're not always as rational as we think we are.
**Alexey** : That's great. You're right. It's impressive, how often the topic comes up in contexts you wouldn't imagine. Then how does it connect to software development? How is it relevant to software projects or to our context in general? How does it materialize?
**Birgitta** : Software development is a discipline where we have to deal with a lot of uncertainty. We can see that, for example, in the need for agile development and the principles of agile development because it's all about embracing change, right? Kind of recognizing that change is going to come at us all the time and new information and new context.
With working in an agile way, we try to prepare for that change all the time and be resilient to it. I think it kind of nicely shows how much uncertainty we have to deal with. A lot of the cognitive biases actually come from our inability or not great ability to deal with uncertainty. I once read about this study that said that uncertainty is actually even more stressful for us than knowing that something bad is definitely going to happen. That's how bad we kind of are at dealing with this.
As I said, us having a hard time dealing with uncertainty and ambiguity leads to a lot of these cognitive biases kicking in. We have to kind of-- maybe not always be aware of them, but if we think about things like architecture, there's this neat little definition of architecture that our colleague, Martin Fowler, I think uses a lot, that architecture is the stuff that is hard to change later.
Especially when we're making decisions about architecture or about things where we think they're going to be hard to change later, I think in those situations, it's especially important to be extra aware of where we might be making these little errors in judgment and maybe try to mitigate them a little bit.
**Rebecca** : Well, I guess I would say too, one of the things that we've really learned over the last several years is the extent to which software development truly is a social activity. We need to talk to people, we need to try to understand their problems, and there's a lot of people interaction. These biases exist in humans. So, in any significant human activity, we're going to have to deal with the existence and consequences of these biases. I find it quite interesting to think about, "Okay, so what would the implication of something like this be in software development?"
**Alexey** : Yes, that's quite true. It's interesting. I'm no expert either, but as far as I know from what I read, it helps a lot in dealing with quick decisions in the face of uncertainty. You need to decide that you need to run away from the lion, and then the biases kick in and just help you make a sane decision that will protect you.
Many times, we need our rational brain and deeper thinking in places, and full function to understand the complexity of situations we have, and software development is definitely one good example. Can we dive into a couple of examples? Birgitta, can you share with us, I don't know, maybe some of the biases or a couple of stories, and some examples of what you've seen over your career.
**Birgitta** : Yes. We can maybe start with the area of decision-making. I already just talked about architecture decision-making, and maybe in that area, it's especially important to be aware because of decisions that might be harder to change later. One of my favorite biases in this area that really blew my mind a little bit when I learned about it is called the outcome bias.
This one basically is about us often equating the quality of a decision with the outcome of the decision. To give an example, let's maybe start with the area of decision-making because I already just talked about how in architecture decision-making, it's especially important to be aware of these things because we might be taking decisions that are harder to change later.
One of my favorite biases in this area is called the outcome bias. That says that often we make the error of equating the outcome of a decision with the quality of the decision. Basically, we take a decision. At some point, in the future, we have hindsight, and we know the outcome of the decision, if actually what happened after that was good or bad. Then we often say, "Oh, that was a good decision," or we say, "That was a bad decision," but often purely based on what the outcome was, but the outcome doesn't necessarily say anything about how good or bad the decision-making process was because that depends a lot on the information as well that we had at the time or how we approached making the decision.
An example maybe is, when you choose a framework, when you choose a technology you want to use, I had this case once years ago, when React was still quite new, and my team wanted to choose a library to implement state management and this flex architecture pattern in React. We chose this library. It was still quite early days in React. Then a year later, turned out, we had actually-- "the wrong choice". We had taken the wrong choice because there was another library that came up, Redux, which is still quite popular today, that turned out to be the winner among the open-source libraries coming up at that time.
When we made the decision, we probably couldn't have known that based on the information that was there. There were different libraries around, they were at similar stages of maturity, so you could say in hindsight, "Oh, that was a bad decision. Now we have to all migrate to this more mature library." At the time that we took the decision, maybe our process was actually okay. We did the research, we did a spike, and that was a good approach that maybe I would use again.
An opposite example about technology choice might be, your cousin sister works at Netflix and uses the technology, and you hear about it at a dinner table. You're like, "Oh, yes, we should try that as well if it's good for Netflix." You use the technology and then actually it works really well for you, and then you say, "Ah, that was a good decision that I used that," but was it really a good decision? Did you really do the research? Did you check if this technology fits your use case?
If for the next decision you take the same approach again, then you didn't really learn from the decision. It's certainly important to take into account what the outcome was. I think we often jump over the step of analyzing how we took the decision and what information we had.
**Rebecca** : Very often we don't attempt to understand why we ended up where we did in a particular situation, in particular, when something goes wrong. It's actually one of the things I liked about this notion of a blame-free retrospective is you can say, "Okay, we did all of the right steps. Now, what was it that caused this ultimately to be the wrong decision? Well, something unanticipated happened. Was it really unanticipated, or was there something that we missed?"
If it really was unanticipated, then there was no way to get a right answer. You couldn't have ever got to the right decision because there was no way to have the information that ultimately would've swayed the decision in the right way. I think it's difficult for us sometimes to really try to dig in and it's much easier to just move on. I agree with you, I think this is a fascinating bias and I think it does tell us a lot about the value of truly introspecting the consequences of the individual decisions that we make.
**Birgitta** : I also like that you mentioned blameless postmortems or blameless retrospectives because I also think being aware of this bias, not only as an individual but as a group, or the other way around, if we do this, if we fall into the trap of the outcome bias, it often reduces our compassion for ourselves and for others. For ourselves, maybe beating ourselves up about the result of a decision, even though we put a lot of effort into it and did a lot of research and got a lot of information, or also I think it's quite common in tech actually for people to point fingers at each other for-- in hindsight, when you know the outcome, say, "Oh why did they do it this way?" after something crashes or after something doesn't scale up to an unexpected spike in users maybe.
I think that often actually leads to overengineering because if there's a culture of finger-pointing if you fail without people actually questioning further, "Why did they do this? What information did they have?" then you don't feel safe maybe engineering just enough for the moment, but you feel like you have to make a lot more certain that it will go well because maybe you're afraid of your peers' judgment because you already expect them to not question how you took the decision.
**Alexey** : That fear of judgment is really strong, and I guess a lot of the power of blameless conversations and blameless postmortems come from-- it's because it helps you see those kinds of things in a social context. One interesting phenomenon that can happen is just you select the information. If I'm not mistaken, that's the confirmation bias because you will select information, the data based on your previous beliefs, and then when you look at the made decision, you will see, "Oh, this worked out well. Look, the decision was great, and this worked out." Maybe even the result wasn't as good as it seems because you were selecting the information based on the belief you were going forward.
Many times once-- that might be another bias in itself, but I'm not sure, once someone has made a decision and declared it, the person is also attached to that decision to some extent, so it's really, really powerful to really create those dynamics in which those learning conversations can happen in a fear-free environment after all.
**Birgitta** : There's another bias attached to this as well that I think if you're actually trying to investigate further, "Okay, was this a good decision or bad decision," we also have to be careful of self-serving bias because we might then say, "Oh--" whenever there's a bad outcome, we're like, "Ah, this was bad luck," and whenever there's a good outcome, we say, "Ah, that's because I took such a great decision," or the other way around.
We have to try and be honest with ourselves as well there, and all of this is related to-- the goal is to learn from our decisions and learn from the past. I read a lot about this outcome bias and self-serving bias, the connection, all of those things in a really great book that I would also like to recommend, it's called Thinking in Bets by Annie Duke. She's a former really successful poker player.
She talks a lot about analyzing her poker game and her decisions that she made throughout the game and batting on things and telling herself afterwards, "Ah, these were really good decisions," because she won. "That was my skill," or when she was losing, it was like, "Oh, I just had bad luck." Then going through that and learning more to really investigate how she was playing and improving her game as well by trying to overcome outcome bias as much as possible and self-serving bias.
**Alexey** : Birgitta, we've been talking about decision-making. There's one topic I'd like to hear from you about. When we have architectural decisions or you did mention the things that are hard to change, as Martin likes to put it, when it comes to those kinds of thing, we've been trying with agile software development to create different techniques for those kinds of things like evolutionary architecture and lots of other techniques, so how does this topic relate to biases? Are some biases that kick in, in those moments of long-lasting decisions?
**Birgitta** : I think it's not exactly like a bias, and by the way, there's all kinds of terminology in that space that I found; biases, heuristics, sometimes the same thing has different names. Some are more researched than others, so if any of the listeners actually try to dig deeper into this topic, be careful, there's lots of stuff out there, but there's one thing in psychology about need for closure.
There's actually a quote from this book I mentioned earlier, Thinking, Fast and Slow, that I noted down before the recording today and it says at some point that "sustaining doubt is harder work than sliding into certainty." It's similar to what I mentioned in the beginning about how we're having a hard time dealing with uncertainty. Then this need for closure often pushes us into making decisions because we just want to reduce the ambiguity, and the more decisions we already take today, the more certainty there seems to be.
I think that might be one of the reasons that makes it really hard for us sometimes to go in steps and ask the question, "Oh, do I have to take this decision now?" Rebecca, in the Evolutionary Architectures book, you all write about the latest responsible moment for decisions, and as one of the techniques to achieve that. I think sometimes it's really hard for us to do that.
**Rebecca** : Well, and it is one of the very common questions we often get is, "Okay, you're telling me I need to wait till the last responsible moment. What is that? How do I know when that moment is?" It's that related question of, "How long do I have to wait before I get to put this uncertainty behind me?" I think one of the things that we try to emphasize in evolutionary architecture relative to this is that the last responsible moment is really determined by how critical this decision is to the things that are going to determine the success or failure of your architecture.
One of my favorite examples in this is I was working on a trading system early in my Thoughtworks career, and people hear "trading system" and they think, "High throughput, low latency, got to worry about performance," but in this particular trading application, they would maybe do 100 trades a day. Anything that had to do-- and yes, I did say a day, anything that had to do with performance and such was irrelevant. What they really cared about was never losing a message.
Decisions around the communication architecture and how we kept track of messages and how we knew when things got stuck, those were the decisions that were really going to impact the success or failure of the system. That was where you wanted to concentrate. I think this, to some extent, helps mitigate to some extent this need for closure. It's like, "Well, but I don't really have to worry about that one. I need to worry about these. Now, let me put my stress over these decisions here." I do think there's definitely a relationship between that need for closure, and what we talk about in evolutionary architecture.
**Birgitta** : I think that also leads to one of the things-- we haven't really talked about it yet, but there's, of course, certain mitigations, or things in the way that we work that we can do to help us tackle some of these biases. One that helps with a lot of them is always thinking about how can I get more information. Is there a chance I can get more information? Can I learn more about reality somehow?
Whenever we jump to conclusions too quickly or want to decide quickly, it keeps us from getting more information and learning more about reality. We have to stop that at some point, of course, but that is definitely one of the things when I feel myself shut down and not wanting to learn more, then that's sometimes a warning sign. Also, with this need for closure, it sometimes becomes especially hard to tackle the bigger group of people that is working on something.
If you're a small team of four or five people who trust each other, it's easier for us to defer a decision because the context is also smaller and maybe we think it's more probable that we'll think about it later. The bigger the group of people, the more complex everything is, yet the more we feel like we have to take decisions and also put in these guardrails for everybody, which often leads to this over-governance. As an individual, I feel I need to make this problem space a bit more safe. So I just take these decisions, and then tell people what to do, for example.
**Alexey** : Birgitta, any examples closer to coding that you've seen or that come to mind?
**Birgitta** : Yes, when we debug, that is also an area closer to coding where I've certainly often felt like sometimes-- we've all had this bug that we've just looked into for forever. At some point, you feel like you don't even know anymore, the things that you tried. You just tried this and that and that, and just can't figure out what it is.
There's a few things probably that can trip us up here. For example, also quite, where, availability bias or availability heuristic that says that it's a tendency of ours to think that if there's something that's easy for us to remember, that's easy to recall, that it is also important or it's maybe more true. I had this example a few years ago of where a developer had just joined our team. They had worked in another team across the hall before, and they joined the team and they were debugging something in our application. They had just recently for days debugged another problem in that other team. They pretty quickly came to the conclusion that it must be the same thing, even though that bug that they had had on the other team had actually been like a freaky little thing that wasn't even that common, but they spent a lot of time trying to prove that this other bug was a similar thing.
I think it was something with encoding in the browser or something. I don't know. I think that also happens quite frequently that we just remember, "Oh, I just read this thing," or, "This just happened to me," or it's also often the more extreme stories that are easier to remember. Then sometimes, apparently according to this bias, we then also think that it's more important, but they're actually the extreme cases, the averages sometimes are not even that easy to recall.
**Alexey** : How do we manage that? We talked a little bit about-- when we talk about evolutionary architecture and the latest responsible moment, can we get more information, and as a way to try to help us see if we are under the influence of a bias, are there any mitigation strategies or ways to deal with them? Maybe, maybe not. That's an interesting point. Any advice on that, Birgitta?
**Birgitta** : In the debugging case, I think I have certainly started to be a lot more rigorous with myself when I debug. I really try to make a plan. I try to apply the scientific method. Try to come up with my hypotheses, what could be the thing? Sometimes I even look at the hypotheses and try to see, which are maybe the more probable, the more common ones because much more often a bug is just caused by the thing that we change last, or in terms of-- it's like Tomcat running out of memory, which I've seen countless times.
That's much more common than some freakish, little weird-- it's much more common often that it's like Tomcat running out of memory than a rare condition. I look at the hypotheses and then maybe I exclude some just by probability, and that's actually another whole area of biases, probability, statistics. Our brains suck at statistics. That's also another one. Whenever something is about statistics, I try to not believe what my brain is first telling me, but I try to investigate a little bit more.
Yes, scientific method, my hypotheses, how can I try to prove them, and then I really try to write them down, so I don't get into those rabbit tools of debugging. We talked about gathering more information, and then, of course, another thing in software delivery is just agile principles and methods because, as I mentioned in the beginning, it's about embracing uncertainty, embracing change, and that's what those methods are there for. Iterative development, going in steps, and again, that is also about gathering more information. Yes, I think all of those agile principles also help us.
**Alexey** : Yes. The conversation about retrospectives feel like another great strategy about that; so bringing in more people and having open conversations, maybe you can elicit allies that will help you see biases in yourself. I think it's easier for you to see biases in other people than in yourself. I'm not sure if I've read that somewhere, but that sounds true. Eliciting other people's support feels like a nice strategy. Does it make sense?
**Birgitta** : Yes, definitely. I can't remember the name right now, but there's a bias about when you know a lot about cognitive biases that you think that you're more immune to them, and then you become overconfident about them. I think another really important aspect of this as well, which is confidence. On the one hand, diving into these biases can actually make you second guess everything and can make you super insecure.
That's something to balance definitely, and as I said in the beginning, we also need them. We need to feel lucky that we have them because they make us deal with the world, but when it comes to this confidence, still saying, "I'm not sure," asking questions, thinking that it's okay to change our minds. Those are also really important, again, for trying to see reality as much as possible, so we can take better decisions, build better software, and be more compassionate with the people around us.
I think this type of behavior, saying, "I'm not sure," asking questions, changing our minds, is actually often associated with lower confidence, and it's actually often seen as a bad thing. People will give you feedback that maybe, "Oh, you should be more confident." I think it's contextual. I think there's no, like, "Okay, I am confident at level 80% or something," but I think we need to adjust it based on the situation.
In those situations where I take important decisions, I actually want to be less confident in the process of taking the decision while I get to my-- and then maybe increase my confidence of course. If I feel like immediately I know exactly what to do, but it's a really important decision, then I at least want to double-check and see what's going on.
**Rebecca** : Yes. I think that's an important point. Another mitigation that occurs to me, and Alexey actually alluded to this, is getting more people involved. It reminds me of the book by Thomas Kuhn The Structure of Scientific Revolutions, where he talks about how these paradigm shifts within science occur. He's actually the person who coined that term "paradigm shift".
One of the things he said is that very often the new theory that emerges comes not from somebody in the discipline itself, but from an adjacent discipline because they are looking at the problem in that slightly different way. They are bringing their own sets of biases and perspectives into that decision-making, but because it's slightly skewed from that of the people who are deep into the problem, they can see things that others can't.
It reminds me of a debugging example once very early in my career. Someone who was working for me came in and she said, "I just can't figure out what's wrong with this code." I asked her to just tell me what the code was doing line by line. She got to the line that was wrong, and she said, "Thank you so much, you're so smart, you helped me figure this out." I was like, "No, I just forced you to look at it and tell me what it did," but she was so blinded because she thought she knew what it did, that she couldn't see the problem.
**Birgitta** : It's rubber ducking, right? Rubber ducking. Another great strategy against cognitive biases. It's great that you say that about looking for other people to keep you in check or keep you honest, kind of because that's also what Annie duke, the poker player I talked about earlier, she also talks about that a lot in her book about having a group of people, other poker players to discuss with and to analyze your game and they keep you honest to, for example, not fall into self-serving bias, but really call yourself out for misjudgments that you did.
**Alexey** : That's great. I guess we're coming to the end of the episode. So, maybe just ask you, Birgitta, if people want to know more about this, where should they look for you? You did mention Kahneman's book, Thinking, Fast and Slow, Annie Duke's Thinking in Bets, any other sources you recommend for people who want to dig deeper into the topic?
**Birgitta** : Yes. Thinking, Fast and Slow, I would say, is a really one of the big ones there, but also warning, it's quite dense. You cannot read this before going to sleep in the evening. I still haven't finished the whole book, to be honest. It's quite a big one, but every time I read a bit of it, it blows my mind. It's really great. Annie Duke, Thinking In Bets.
There's also a book called The Art of Thinking Clearly by Rolf Dobelli. That's also quite nice because it's basically structured by-- there's a few pages for bias, and then he gives an example. You can also jump around in the book. Then there's a podcast, You Are Not So Smart, that I also quite like, and the host of the podcast also wrote a bunch of related books. I forgot the name of the host at the moment, unfortunately, but yes, those are some places to get started.
**Alexey** : Well, it was a great conversation and great to have you with us. Thank you so much.
**Rebecca** : Yes. Thanks, Birgitta.
**Birgitta** : Thank you too.
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
## Explore the latest Technology Radar
[ Explore ](https://www.thoughtworks.com/radar)