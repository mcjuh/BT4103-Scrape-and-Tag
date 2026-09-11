<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/using-generative-ai-legacy-modernization | Title: Using generative AI for legacy modernization | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Using generative AI for legacy modernization 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Ken Mugrage | Podcast guest  Shodhan Sheth and Tom Coggrave
November 28, 2024 | 33 min 19 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/using-generative-ai-legacy-modernization#Transcript)
Listen on these platforms
## Brief summary
Legacy modernization is an enduring challenge — and as systems become more complex, the difficulty of understanding and modelling a system so it can be modernized only becomes more difficult. However, at Thoughtworks we've seen some recent success bringing generative AI into the legacy modernization process. 
To discuss what this means in practice and the benefits it can deliver, host Ken Mugrage is joined by Thoughtworks colleagues Shodhan Sheth and Tom Coggrave. Shodhan and Tom have been working together in this space in recent months and, in this episode of the Technology Podcast, offer their insights into finding success with this novel combination. They explain how it can be implemented, the challenges and experiments they did on their way to positive results and what it means for how teams and organizations think about modernization in the future. 
  * Read Shodhan and Tom's [article on legacy modernization and generative AI](https://martinfowler.com/articles/legacy-modernization-gen-ai.html) (written with Alessio Ferri).


## Episode transcript
**Ken Mugrage:** Hello, everybody. Welcome to another edition of the Thoughtworks Technology Podcast. My name is Ken Mugrage. I'm one of your regular hosts. Had a little bit of a special edition this time. I'm at the Microsoft Ignite Show. We're recording this here in late November and was lucky enough to coincide with the schedules of a couple thought workers I think you'll find interesting. Today we're going to talk about some legacy modernization meets generative AI. My guest today, Tom Coggrave. Tom, do you want to introduce yourself?
**Tom Coggrave:** Yes. Hi, folks. My name's Tom Coggrave. I'm a technologist here at Thoughtworks where I've been looking to how we can speed up the way in which we do modernization for our clients. I'm particularly looking to mainframe modernization of late.
**Ken:** Great, thanks. Shodhan Sheth, you want to introduce yourself please?
**Shodhan Sheth:** Yes. I also am an technologist at Thoughtworks and play a similar role to Tom and also focus on all things legacy modernization.
**Ken:** Great. One of the common jokes here at any large event is don't play a drinking game around the word AI or the phrase AI because you won't survive. We know everybody was flooded with AI. Y'all are doing some really interesting hands-on practical work that's actually been going on for quite some time now. For understanding the shift, how is generative AI helping you comprehend these complex, longstanding code base for modernization?
**Tom:** I guess when you think about an existing legacy code base, we're talking about something that's maybe 20, 30, 40 years old, likely in the many millions of lines of code. One of the problems with that is, I guess, the amount of time it takes humans or individuals to actually get through that code, read through it, understand it, build a mental model in their head, and then be able to then explain that back on to other people to work out what to do about the problem is huge. That takes years. We've worked at organizations in the past where they measure the amount of time it takes for new mainframe developers to get onboarded as around 5 to 10 years before they really become truly effective across the whole code base.
When we think about this new technology that's come in, generative AI, it's not all powerful, but it's very good at being able to elaborate and summarize and explain documents, large amounts of text. What is a code base? It's a more of a structured set of documents, but in effect, it is documents with text inside it. That's how we're seeing generative AI being able to help with comprehending these complex, longstanding code base is through being able to explain it to humans and summarize the key facts and key parts of it to humans at a much faster pace than previously has been able.
**Ken:** How did you do it before now?
**Shodhan:** I think in the legacy monetization has been a longstanding problem. There are many solutions pre-GenAI, but in our experience, they tend to be fairly mechanical, and they don't help with the issue around making it human scale. I'll try to explain it. When you're looking at anything beyond, I don't know, 1,000, 2,000 lines of code, it doesn't fit your brain. It becomes a non-human scale. Machines are really good at it. Humans are not, but it's keeping that in their head. These reverse engineering tools or comprehension tools that existed weren't really solving that problem.
You ask one of these reverse engineering tools about, "Hey, explain to me how this business process works," and it'll give you 200,000 or 500,000 node flow chart. That's not something humans can consume because you can't remember those many things at the same time. I think one of the things that has changed with GenAI is it can abstract it up. I think that's one of the key benefits of using technology. It gives you a human scale answer, and then you can dig deeper. It could give you an answer that's maybe enough to just give you a high-level perspective how that business process is working, and then you can query further.
I think that's how humans work in terms of understanding large pieces. You first get a high-level answer, then you dig into different parts, whatever parts you might be interested in. There were tools before this, but I think the efficacy was not great, and I think that's what's changed now.
**Ken:** Do people just fire up their OpenAI or Google tools? What have we done to help you with this process?
**Tom:** When we first started, yes, that was actually the approach that we took. A lot of people in the industry, I think, were seeing a similar thing to this. There was a lot of excitement around firing up ChatGPT, pasting in chunks, lot of chunks or files worth of code and seeing what it could help with. Some of the early intel tooling that we explored use this approach. It was more to do with prompt engineering, about tuning that prompt to be able to get just the right amount of information out of the piece of code that we're looking at. Since then, we have come to recognize, I guess over the course of the last 18 months.
We've recognized some of the limitations that you run into with that approach. Not everything's to do with understanding a given piece of code is in the same file as that piece of code. You have dependencies, the data schemers tends to live elsewhere. To understand any one element of code, you have to be able to look around that as well. Also, unlike a good essay where you have a beginning, middle and end, code isn't necessarily organized in that way. There's a different structure and flow to a document of code. You have to be aware of that when you're reading through it so that you don't correlate things together that aren't related.
We recognize these structural challenges or these challenges that can only be dealt with by thinking about the structure and nature of code and start to expanding the tooling that we were looking at to be able to take advantage of that using things like pauses and dependency graphs to be able to power the understanding of that piece of code or the explanation of that piece of code a bit better with related information and be able to walk through it more easily.
**Shodhan:** As Tom was saying, we went through lots of different experiments to figure out the right answer for this problem. The problem being, how do I understand a large legacy system? One, I guess, insight we had whilst we were going through those experiments, some of them not successful as well, the trick is to give the LLM the right context. In a large code base, getting the right context is a hard problem. Somebody uses analogy that it's like an open book test. If you know where the answer is, it becomes so much simpler problem.
If you don't know where the answer is, then book doesn't help, and legacy systems are not a book because they're not that well written, but I'm sure you can understand the analogy that LLMs need to be given the right context for them to generate the right answer. That's where our engineering is focused at. All the engineering is focused on how do we get the right context for the question from the user.
**Tom:** Yes, it's a little bit about optimizing to get just the right thing because of the context window, the limitations as well.
**Ken:** I should have mentioned it at the top, but y'all are two of three authors of a fairly large article on this, which we'll link in the comments so people can read it. One of the things you talk about there is that the challenges of legacy modernization. We've already touched on it a little bit, but from an organizational perspective, what are the kinds of challenges that you see people that generative AI specifically helps mitigate?
**Shodhan:** I think at the highest level, we allude at the cost, time, value equation of legacy modernization. I always feel there was a time where we used to talk about stuff like, "Hey, that's rocket science or it's not rocket science." I think there's something that industry needs to do when it's easier to launch rockets in space than to modernize legacy systems. The cost, time, value equation of legacy modernization is alluding into that, how much effort is it to modernize legacy systems versus some other things happening in the world. I guess primarily one of the hypothesis we are applying is a lot of the cost, time is also because of the cost of delay of understanding legacy systems.
Because one characteristic or many of the characteristics of legacy systems are around the fact that documentation is stale or absent. There are no good safety nets around it. The SMEs around it have either disappeared, moved on or are just not there. That adds a lot of cost or delay to that monetization program. That's one element of it. The other element of it is now addressed by a lot of the forward engineering GenAI tools, coding assistance and the like, which is the legacy system is 30, 40, 50 years of investment of an organization. It's quite a bit of quanta. The expectation is to reproduce it in months or years.
By nature, it just takes time to replicate something that you've been working on 30, 40, 50 years. I think what we are trying to do is figure out the right pockets where GenAI can impact the cost, time, value equation of these legacy monetization programs. Code comprehension is definitely one area where we found a lot of success. Coding assistance is another area that I think we've all as an industry seen some success. It feels like this is still the tip of the iceberg. There's more areas to explore and see how we can make that impact better.
**Ken:** You touched about years and decades there. Some of the systems I've worked on, we have no idea why things were even in there. Not only what was the purpose or whatever. In your article, you actually talk about-- I don't think you use these terms, but backporting and getting the requirements from the code. Somehow looking at the code and trying to understand, "What is this trying to do?" What's that process? What's that look like? What are the benefits to doing that?
**Tom:** I guess, what is the purpose or what's the process of modernization? Modernization is there to typically replace or refresh a set of technology that you can no longer maintain or no longer is fit for purpose. Isn't allowing you to change at the pace that you need to. However, it still is performing a vital-- I'm sorry, it's gone very wrong. It's typically performing a vital function for your business. At least parts of that function will still need to continue in the new modernized world. When we're talking about kernelization, one of the things that we need to do is get the requirements. We get the understanding as to what the code is doing or what the system is doing.
Using generative AI, we're seeing that we can speed that process up using, I guess, generative AI. The process itself looks like I think what we were describing earlier, using generative AI large language models and abstract syntax trees and parsers and code dependency graphs to be able to walk through that, provide exactly the right context to that LLM and prompt it to produce descriptions about what the code is doing, which we then can treat as requirements that we decide whether to take force or not. Another hallmark of legacy systems is that the processes that are in place are there because they haven't changed, I guess.
They haven't been updated as the business has changed over time, so people may still be or the employees of the company may still be following processes that are out of date or that unnecessarily complex. For us, one of the reasons why we like to have, I guess, a human in that loop or a modernization process that involves re-engineering and rearchitecting, reimagining what the future looks like is so that we can get rid of the craft, the dead code of business processes, as well as the dead code itself when we're going forward. The benefit there is that using generative AI, obviously, it's going to be much less time, hopefully, much faster to get those requirements out. Then you still need that human in the loop to get rid of what's not needed as well.
**Ken:** You touched on something that I think is important there. The human in the loop. One of the things that I know with different Thoughtworks topics whenever we talk about generative AI or AI or machine learning or what have you, is the necessity of having someone that knows what good looks like. How does that work? Is that a factor here? Because I could just write a program that translates a thing, but what is that human in the loop? Whether it be tools or processes, or sticks or carrots, how do you get the human in a loop that knows what good looks like to participate?
**Shodhan:** We are talking about two maybe different areas of application for AI, and maybe the answer is different for those two. In the area that we just talked about in terms of comprehension, it's almost an easier answer because the consumer is a human. I think there's less of a question of how to get them in the loop because they're at one side of the equation. One side of the equation is the legacy system, and then there's some technology in the other side of the equation, consumer is the human. We're not saying these technologies give you 100% accurate answers.
There's also some skill involved in terms of crafting the prompt, et cetera. Because you can almost interrogate the technology about your legacy system, the human is constantly involved in that process. When we talk about translation, I think there the human in the loop factor is different, and to be honest, we don't know what is the right answer or at least I personally don't know what is the right answer. I think that area requires more experimentation because we come from a more deterministic approach in that sense as people who are big fans of continuous delivery.
What we like to do is like, "I've written the code and converted the code — It should now automatically move towards production." That doesn't look like a feasible or viable process based on where these technologies are today. I think there's more experimentation and more trialing needed to figure out what is the right process so that there's enough confidence in the output. There's probably a threshold after which-- assuming it's not a system that has life impact, assuming it's not that system, you can reach a threshold of confidence where you're like, "Maybe this can work in more automated fashion." I don't think that pipeline exists today or that process exists today or we're not aware of a very successful version of that.
**Ken:** One of the things that we also struggle with I think as technologists-- I guess I'm going to be a little careful here because we like to refer to business users, and I have to admit, I have a very personal bias here where whether you're writing automated tests or you're a developer or you're selling the system, it's all part of the business. That said, most of what we're talking about is from a technical like, "What is this function doing," et cetera. One of the things we hear from people in the "business" is modernization. You're just taking functionality that I have and rewriting it in a different language. What are the high-level explanations that we can share with the non-technical stakeholders, put it that way, during a modernization project? Does this help with that at all?
**Tom:** When you're kicking off with a modernization program, we talked a little bit about some of the challenges that businesses are trying to overcome by changing that technology stack. Even within that monetization program, there tend to be a priority that you can apply to aspects of the system, so choose the order in which you might want to modernize or to understand that high level, what are the things involved in that system so that you can make decisions about whether you need to necessarily reimagine or re-engineer those functions, or whether you can potentially look to now buy something off the shelf to support them.
It's quite hard. If we're talking at a level of, say, stories, or even epics, in terms of the requirements you've extracted from that existing code, it's very hard to abstract sufficiently to be able to compare whether what you've got in that code is fulfilled by an existing system. Taking a very, very basic example, if we talk about identity systems, back in the old day, you had to roll your own. A lot of legacy systems will have their own identity and access management capabilities built into them. Nowadays, you don't typically do that. It's a huge risk to run your own, one of those.
Most people these days will be buying off the shelf or licensing a SaaS product to do that. It's that decision about being able to replace those functions, those capabilities in the existing system that you need to be able to abstract to a sufficient level to know that there's something out there in the industry to do that for you. It's that ability to abstract from low-level detail to something higher level that enterprise architects and business users can discuss about, allows you to make those decisions. Generative AI, as we were saying before, is quite good at summarization. It's quite good at explanation.
Taking that capability that GenAI has to be able to abstract those low-level details up into something that allows you to, I guess, compare and contrast existing solutions or even prioritize amongst those things as you go forwards is super useful. It's very helpful. It allows you to, I guess, speak at a level where a business person would understand that this is a function that your organization does or doesn't need to do. That we find super helpful in our modernization programs, and we're using generative AI to make that faster as well.
**Ken:** It's interesting because you mentioned identity and so forth. I think anybody that's involved with one of these projects knows there's a lot of code in there that simply isn't doing anything anymore. It might just not be executed. They've replaced it with something else, so it's just dead code. It might be duplicate, it might be just unused. Can this help identify some of that? Have you been able to pull out some of the cruft in this way by understanding the system better?
**Shodhan:** One early experiment where we've seen a little bit of success but I think we need to see more to call success. What I would say the thing that struck us was syntactic duplication has been around for a while. It's easy to spot that, "Oh, these two statements are exactly these two statements here." There are lots of static analyses that do that. With legacy systems, again, because code has been authored at very different parts of time by very different teams, the duplication is more semantic in nature. It's not easy to spot. One lead we have, I would say, maybe not success is by doing some bottom-up clustering of code, we have been able to spot in one occasion common functionality across legacy code bases.
That would be the notion of semantic duplication. I think we still need to apply it at more places to see if it's an approach that scales or was it just that one scenario where we were able to spot it, but I think that's one lead we have. Right now, the other perspective being is we've not folded in observability into this tool that we are building. It's based on the notion of code.
If you were to fold in observability, if you were to mix and match how the code is structured and what is being used when through your observability data, then it possibly gives you more data points on figuring out this part of the system hasn't been used for the last two years or something of that sort. That's something that a lot of people ask us. It is something that I guess is on our roadmap to look at, but we've not looked at it right now.
**Ken:** Of this whole topic, how much of this is still experimentation and how much is this the stuff that you can go do today?
**Shodhan:** We categorize what the tool does in terms of these different scenarios that a user or persona might be using. Their scenarios are like, "Hey, I want to understand how this feature works," or, "I want to understand how many validations and business rules there are in this part of the process." That's in production for multiple customers that we worked with. We would say that's going on pretty well. Questions that are of the nature of how and where, so, "Hey, can you tell me where is this implemented?" Et cetera, those things are pretty good. The what questions, like "What business capabilities does this large legacy system serve?"
We would say that's more experimental in terms of how we're approaching it and we want to see more proof points of success before saying, "Yes, this is a good problem, solution fit." Then there's other areas around auto-generated documentation. I think a lot of the industry has seen a lot of success with that. I would say though, those three main buckets would be the main ones. I think the what type of questions like, "Tell me what business capabilities does this large system serve?" I would say still experimental from our perspective. Then a lot of the how and where questions like, "Explain to me how this works", or, "Tell me where this piece of functionality is implemented", or, "Tell me what is the impact of changing this part of the system?" Those things are in production.
**Ken:** Yes. I ask that because one of the things we hear a lot is like, "Hey, we've done a lot of good experiments with AI, but none of it's in production." In this case, using two out of three buckets are ready to go. 
Then shifting gears a little bit, modernization isn't always just about, "Hey, I had a monolith and now I need microservices or whatever." There's also completely different paradigms now. We have software-defined vehicles where some of the car codes like driving down the motorway, et cetera. How does this help with that, or does this help with that? You want the same thing, you need the person to know what their fuel economy is and when the gas tank is empty. It's completely different paradigms. Does this help there at all?
**Shodhan:** I think this is one way we hope it will help. Again, we would say there's still a lot of experimentation to do. The common classic cliche example being the fact that the mainframe operating or development paradigm being very different than today's cloud-native microservices, Java development paradigm. Translating between those two paradigms, I guess, in our opinion, has not yet been achieved. There are lots of code translation tools out there actually, and the common view is-- it's COBOL to JOBOL. You'll see COBOL in the shape of a Java class, but it would have similar variable names that it had in COBOL.
It would have similar method calls as they were there in COBOL. That wouldn't be modernization because you modernize it to decrease your cost of change. Now, if a new Java system is as difficult or more difficult to understand than the COBOL system, then you have not achieved your goal. There's lots of translation tools out there. We are hoping with GenAI, that translation can be higher quality.
Because one of the challenges is how do you translate procedural code to object-oriented code? How do you translate the variable names that were written 30 years ago that were more optimized for maybe storage or the constraints of hardware at that environment to today's computing paradigm, which is completely different? It's an area that we think there is some hope, but again, there's a lot more to do before we can say, this is an area that this can help.
**Ken:** I just two more questions to close it out and these are going to be pretty speculative. Fair warning. I know both of you live in the modernization world right now but just in general, if you crystal ball, is generative AI, the miracle that they would have us believe in the Keynote we saw this week?
**Shodhan:** Predicting future is always hard. We have seen, I guess, there is precedent of multiple technologies being on the hype cycle and then not doing as well as we thought. Overall, we feel we need to be cautiously optimistic. A bit of caution to make sure you don't believe in everything that's being said. It definitely can't solve all the problems of the world. Our focus is always on problem solution fitness, so find the problem that's a fit for this solution rather than just trying to apply it at all places. I think there's still a place for traditional AI. All the other forms of AI that were there, pre-GenAI.
Again, one learning that we've had through development of this tool is actually GenAI works better when you pair it with these tried and tested other technologies. A lot of this tool is abstract syntax trees, graphs, these are all technologies and approaches that have been there for 20, 30 years. We've married it with GenAI rather than just GenAI being the answer to everything. I think we are definitely being cautiously optimistic and investigating more revenues where we think it can help. To be honest, time is the best future teller.
**Ken:** Somebody on a previous podcast said we still need to know if else not everything's AI. Tom, what about you? What do you think about the future? Where's GenAI going to be effective or not? I know these are guesses, folks. I don't mean to put you on the spot but I think your guesses are better than most people's facts.
**Tom:** One area I'm particularly hopeful for, maybe not excited, I guess. One thing I think could be very powerful especially in the field of modernization or looking just a little bit further ahead in terms of modernization is around the safety nets that we might want to have in place for that we need to get put in place to be able to do that modernization. When you're taking some 40-year-old system and try to move to a new modern architecture or a new modern version of it, you need to make sure that where you are replacing a function that has been there for a long time, the pace at which you can do that is limited by the quality of the tests or the existence of tests which aren't always there in these cases.
I think one of the areas that I'm excited or hopeful that we'll see is how can generative AI help us get more safety around the existing systems to build to not just describe what they do, but almost provide test cases for how that works right now so that we can then cross compare, I guess, in the future as well. That's definitely one area I'm super excited about. I guess I'm very excited by a lot of the experimentation that's going on around, I guess, the creation of software by generative AI agents or by all these things. I think as Shodhan was was saying, there's going to be a necessary set of framework or infrastructure that sits around these LLMs to be able to ensure the right context is given to the LLM at the time when we're generating code or when we're trying to create a system.
There is complexity in that. I think there's one level of complexity to be able to extract and understanding out of an existing system and represent that in graphs or whatever, but it's probably an extra couple of orders of magnitude harder to be able to retain that context as we're building out a new system at on the other side of that, almost in in reverse of the understanding explanation side of things. I'm excited about that. I think it's probably a little way off, hopefully, going to be proved wrong. I think it's probably still a little way off at this point.
**Ken:** What are the key considerations and best practices you recommend whether or not they're using Thoughtworks and our tools frankly but for an organization that's wanting to leverage GenAI for legacy system, what are some concrete next steps they can do to try to help ensure success?
**Shodhan:** I'll maybe repeat some of the stuff that I've already mentioned. Don't look at Gen AI as the one-stop solution, the silver bullet. At least in our experiences, all production solutions are a combination of technology paradigms that are married with GenAI. The other one I would say is focus on problem solution fitness. If you're doing something new, treat it as an experiment, be ready to pivot and learn from that experiment and try different approaches. Then the other thing I guess is that this is a different paradigm in terms of the determinism that we are used to. It does take a while to start becoming comfortable with that.
There are some, I think, new skills that we will have to add to our-- prompt engineering is the most commonly talked about skill. Now, it takes some experience to figure out the right crafting of those prompts in the right way to ask it a question, the right context to provide it. Those are all things that organizations will have to learn with or without topics if they want to survive in a GenAI world.
**Ken:** Tom, what do you think? What's your actionable advice there? It's okay if there's some overlap.
**Tom:** I think I'd probably just build on a couple of things that Shodhan was sharing there. One of the things that allowed us to get around that experimentation point that Shodhan was making, I think the fact that we at Thoughtworks had internal access to some of these tools to be able to experiment and drive this stuff forward was actually part of the reason we've made as much progress as we have. I think a call out for organizations would be, how can you quickly put these tools safely into the hands of your teams, your employees so that they can discover ways in which to improve their processes, change the way in which they're doing things hopefully for the best of the overall organization?
Definitely a call out is to enable access there. I think the second one is building what Shodhan was saying around different approaches. One specific example that comes to my mind is around where previously developers have written xUnit tests to specify the behavior of this stuff. We can't expect that with generative AI. It's about shifting to look at evaluation techniques, for instance, using LLM as judge is one of the ones that's doing the rounds at the moment to be able to validate or to be able to evaluate the quality of the output of some of these generative AI-based systems.
It's that mindset shift of determinism to how do you deal with non-determinism but still get confidence in the system you're building is definitely a shift in making certainly me feel uncomfortable, but getting through it.
**Ken:** Thank you both. I appreciate you taking the time, especially you're here in Chicago for an event and got to head home to London. Bery much thank you. Thank you to our listeners, and we'll see you next time.
**Shodhan:** Thanks, Ken as well. Bye. Thanks, Ken.
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
[ Read the latest Tech Radar ](https://www.thoughtworks.com/en-th/radar)