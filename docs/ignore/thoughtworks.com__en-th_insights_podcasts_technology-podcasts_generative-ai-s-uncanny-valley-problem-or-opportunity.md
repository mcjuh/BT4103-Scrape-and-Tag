<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/generative-ai-s-uncanny-valley--problem-or-opportunity- | Title: Generative AI's uncanny valley: Problem or opportunity? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Generative AI's uncanny valley: Problem or opportunity? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Lilly Ryan | Podcast guest  Srinivasan Raguraman
December 12, 2024 | 28 min 51 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/generative-ai-s-uncanny-valley--problem-or-opportunity-#Transcript)
Listen on these platforms
## Brief summary
With the rise of generative AI, the concept of the uncanny valley — where human resemblance unsettles, disturbs or disgusts — is more relevant than ever. But is it a problem that technologists need to tackle? Or does it offer an opportunity for greater thoughtfulness about the ways generative AI is being built, deployed and used?
In this episode of the Technology Podcast, host Lilly Ryan is joined by Srinivasan Raguraman to discuss generative AI's uncanny valley and explore how it might offer a model for thinking through our expectations about generative AI outputs and effects. Taking in everything from the experiences of end users to the mental models engineers bring to AI development, listen for a wide-ranging dive into the implications of the uncanny valley in our experience of generative AI today.
  * Read Srinivasan's [recent article](https://www.technologyreview.com/2024/10/24/1106110/reckoning-with-generative-ais-uncanny-valley/) (written with Ken Mugrage).


## Episode transcript
**Lilly Ryan:** Welcome to this episode of the Thoughtworks technology podcast. I'm your host, Lilly Ryan, and I'm speaking to you from the lands of the Wurundjeri people in Melbourne, Australia. Today I'm talking with Srini Raguraman, a principal technologist at Thoughtworks, about a piece that he recently co-authored with our other podcast co-host Ken Mugrage in the MIT Review. This piece is called Reckoning with Generative AI's Uncanny Valley. Today, we're going to unpack a lot of these concepts and how they interact with generative AI tooling in the way that we're seeing it today. Srini, welcome to the show.
**Srinivasan Raguraman:** Thanks. Thanks for having me here.
**Lilly:** What is the uncanny valley? This is a term I've heard a lot, but I've usually heard it in the context of robotics or animation or something like that. How does it apply to the collection of technologies that we're calling AI these days?
**Srini:** Yes. The concept of uncanny valley, like you said, you probably commonly associate with robotics, but we have seen this up here in other terms as well. For example, in the past when we are developing mobile application, we have been seeing that when you're building a mobile app, lot and often teams take a shortcut like, "Okay, I have a website. Can I wrap this into a app and release it?" When the users use that app, mostly it's functional, but they can also quickly at times feel cheated in the sense the experience doesn't match what it should be matching with the ecosystem.
That's the place where there's a little bit of surprise or bad feeling, feeling the negative side of things. That's why we've called this the uncanny valley and we see this up here in other technical domains like the site and cross-mobile platform stuff. We're also now seeing in LLM. What's special about LLM? I think LLM or generative AI for that sense, it's a non-deterministic software in some sense. It can give the same inputs, but not necessarily you will get the same outputs. You can fine-tune and instruct, try to prompt, and try to make it the same answer. Even then there is not sure that you get the right answers.
**Lilly:** That's in opposition to something like a calculator where you would input 1 + 2 and you would expect it to be 3 every single time. That's more of a deterministic approach. The non-deterministic, you're getting a lot of different kinds of output and the same input could generate a wide variety of different responses depending on what the model's got in its training dataset, how it's been weighted, that kind of thing, right?
**Srini:** Yes, exactly. A small change in input or a small change in something that the model relies on can have a quite different outcome or output. I think this is the behavior of LLM, which is actually quite useful as well because we can see the use cases of LLM where it's writing text or essays, where actually that's useful to not have the same essays for millions of people giving the same input. It's useful and also the other side of things where it can not be useful. This makes it what the surprise can be, either surprise or it could be disappointing. This disappointment is probably where it starting feeling at the uncanny valley.
**Lilly:** This uncanny valley thing, it really describes that creepy feeling that you experience when you're expecting something to be human and then something happens, there's some kind of output or appearance or something just even for a moment that reminds you or indicates that the thing that you're speaking to is not human. I think classically they spoke about zombies as falling into this category. It's a bit spooky. It's human-shaped, but the behavior, the movements, and that kind of thing don't feel the same.
For a lot of people, that's where that uncanniness can come from. I can see how it applies in this situation too where you have these moments where suddenly if you are interacting, say, with say a chatbot, in that case, you end up with something that really surprises you. When it comes to how we look at this in a business context, why is it important to think this through?
**Srini:** Like I said, the uncanny early experiences could be for many reasons. One of them, evolutionary responses. Our brain are wire to detect anomalies. It could be a neurological thing because you feel that way, pain, but it's also very common about the mismatch in expectation of the output. That's why I would probably dive back to the expectation on the capabilities of LLM. The capabilities of LLM is wide-ranging, and now if you'd see the market, there's a bunch of models. There's large language models that are even specialized small language models. How would someone make sense of this, whether this is a right model for me, for this context of the job I'm picking up?
If the mental model for picking that right model is not said, that also reflects on the user experience. It's not just about what the user can see. It's also how the developer's building around it, need to have to pick the right one. This have a bigger impact in business. Most commonly you're probably hearing a lot of people are experimenting or doing a PoC for our generative AI. You ask them, "Have you deployed to production?" The answer is mostly, "We are not sure about the implication or ramifications, so we are holding it at the PoC." I think that's where there's uncanny value experience, and the impact of that is quite evident in making or even productionizing the model.
**Lilly:** Because nobody wants to put that experience in front of a customer. We've seen many cases that have made the news where because of that experience happening in front of a customer, there's been a lot of negative backlash, brand reputation impact, that kind of thing. Yes, it's tough. I like the distinction that you drew there about the way that people are thinking about it in terms of their different roles. What kinds of mental models about this kind of current crop of generative AI technologies have you seen out in the wild?
When you're speaking to clients, when you're speaking to developers, and when you're speaking to members of the public, I think all three of those groups can really have some very different ideas about what generative AI is and can have different ideas in different contexts. What kind of mental models have you seen people have and what do you think are the helpful ones?
**Srini:** I could start with what I can hearing from clients or people who are first looking at the LLM. The first time they look at it is like, "Okay, this model can reasonably answer me and can learn from my interaction." The most common question they had is, "I deploy an LLM model. Now, based on how I'm using it, does it automatically learn from it?" Most people assume that it automatically learns from it, but it's not true. The LLMs, they have this certain modeling and then they can generate responses, but not necessarily learning from your question.
They have the concept of context window where they can use certain range of information to give us more a response that you're looking for. Outside that context window, there's not much of memory on its own. It doesn't learn from you. I also think this is partially driven by how the industry is approaching this. One common thing is when people experience interaction with LLMs, they feel like, "Okay, it feels like it's reasoning," but it's not really reasoning and it doesn't really have the basic capabilities, or it's not built like humans.
It is a probabilistic model, also called as stochastic, where it just generates an output based on bunch of parameters. It's not reasoning for you, but it feels like reasoning. This is tying back to the output looks more human, so you assume with that mental model, it can reason.
**Lilly:** You could for example, ask a chatbot something like, "Please explain how Leonardo da Vinci's Mona Lisa ties to the cultural aesthetic of the time in which it was painted." It could probably say something about that, but you could then ask it classic something like, "How many Rs in the word strawberry?" and it's not going to be able to get to that point. That that's quite a famous one. I know that OpenAI has named one of their more recent models codename strawberry because they were looking at, how do we solve this problem. It's fundamentally one of the things that I think the industry is looking at quite a lot, right?
**Srini:** Yes. The concept we're moving towards AGI, Artificial General Intelligence, that's the goal's probably useful or it has its own people looking outcome of it. It also leads to the common understanding of like, "Should I be worried about this or can it actually do all the thing I can think of?" That doesn't actually help people to be very realistic or to be actually interacting with these models with the right mindset. The common story, I think of the one thing I found as a mental model I heard in good terms out of framing for that, that's useful is the AI as the stone soup.
This is the story of three strangers coming into a village and they say, "Okay, do you have anything to make a soup?" The villages are like, "No. We have our food, but we don't want to share with you." They're like, "It's okay. We will make a stone soup, which is very delicious." They start making, putting stones, and start boiling water, and then they say, "Oh, it tastes nice." It just need a little bit of something. Do you have something? They quickly borrow things from the villages and slowly adding things like carrots or whatnot.
Slowly, actually the soup, the outcome is delicious. It's not because of the stones or the boiling from it or the things that's strange about. It's about the people, what the information they share, the data I share. I think this sets the context of the LLM as a good model where the outcome is actually determined by a lot of things that you share. It's not a magical thing to solve. You are aware of how the whole process works and what it translates into. I feel like this is a good analogy or metaphor that actually can help people to approach LLM or Generative AI with the right mindset.
**Lilly:** It gives you this basis from which to structure your own thinking by offering you the possibility of anything and then having it reflect back to you the things that you put into it and build on top of it over time as not quite a collaborator in that way that it is actively participating with you, but that it provides the framework for you and the people working with you on this to get something substantial out of it.
**Srini:** Totally. You also mentioned about what's the other mental models people are-- The common one I can see with business is they have this assumption, "I can replace something with this entirely." You can call it as an automation bias where they want to automate a big chunk of thing without understanding the ecosystem. I can quote a recent example with the coding assistance. With coding assistance and other stuff, the outcome they want to replace is writing, generating code. The coding assistance can generate code, but then does it makes easy to read those code in production when you're trying to debug? Those kind of things.
The assumptions people take is, "I can substitute some part of the current workflow entirely with the LLM or Generative AI," often leads to other problems where I think you can learn from the past where automation with humans and machines is similar thing where if you take for example, pilots using autopilot. When they are using autopilot, they're not exercising their regular skills, but they also need to know about how autopilot engages.
There's a bit of complexity that they also need to understand to be able to step in and disengage autopilot in a place where it's relevant. It's not like suddenly I have an autopilot, I have taken care of these things completely out of the human control and doing a best job out of it. It actually increases the cognitive load for the people to understand how the machines operate.
I think for a human-machine interaction, there's two bits that's very important. One is the observability part of it where you want to know what the process is replacing and how it's behaving. Given a Generative AI model, it's not a deterministic model, it makes it challenging. The other bit is able to direct the machine or the LLM to a specific task. You can do that bit of a prompting saying, "Hey, can you focus on this bit and change it?" Again, it's not as direct to as in you're driving a bike or you're driving your car.
The key bit of automation that actually makes this human machine or human automation works well is the observability and directing, but the nature of LLM challenges this. The nature of LLM is not quite adaptive for this kind of expectation. I think that's where the industry is generally moving about how we can improve the reliability or how we can bring the observability and the directability. That's probably where these mental models can help them to approach it very realistically.
**Lilly:** It's interesting that you talk about how it can be used to augment a lot of things, and you also mentioned the problems around things like pilots understanding autopilot. There's also a concern that if you're adapting too many automated models in your workflows, that you will replace the people who are learning from doing those kinds of tasks as introductory tasks. If they've just started out their careers and something can replace them in that space, how then do we get people who are going to be seniors in, say, 10 years' time learning the foundational skills right now? Is there an approach that you would recommend that people take if they are looking at these kinds of solutions such that you are not only helping people with these things but also helping people grow their skills from first principles?
**Srini:** Yes. I think that's a very interesting question in the sense also very important one. When you are replacing something, it's taking away the opportunity or the current process. It is important for people to study the ecosystem. What is the second-order effects of doing this and what it can imply? If there is an impact on another role or on another person, then opportunity is taken away. Then there needs to be other set of things that need to be pulled off. I read about this somewhere where the doctors using robotics these days.
They can actually make very minute operations very clearly, which probably previously required 10 assistants in the operation room. Now it's robotics with robotic hands. They just have to use the robotic to control and make the operation. Usually, they don't have that many assistants on the room. When the assistants look at it, they just look at the machine operating. They're not really looking at like the person, how they are controlling and other stuff. This changes the learning ecosystem for even new people and due to the cost and other things involved, again, only people who are experts are given opportunity to operate robotics.
When someone is new in their career, there's not enough ways for them to actually do a robotic operation unless they are experts. In a way, I feel like these LLM or these advanced techniques very useful tools for experts because they know what the machine can do, and they can also sense that it's not going right or things like that very effectively. Actually, their knowledge and the people's knowledge is the key bit in making that all outcome, maybe 10x effect right? At the same time, it breaks the metaphor of-- or not even a metaphor, but it breaks how other people can engage in this.
Maybe there needs to be a second simulation plays or a digital twin or those other things needs to be explored where people can safely move from novice into slowly able to run, but just replacing something have this secondary effects. Outside this, I can also think of the AlphaGo. I think the trend after AlphaGo is the player's ranking started stacking up. Previously, level X is probably the golden standard, but after AlphaGo, people learn from the interaction because experts can learn from that, the player ranking went really, really high and it's now somewhere differently.
Also, it changes how people can learn. Previously, something learned naturally, now people have to learn it by looking at how the machine performs. Someone said it's like learning from cheat sheets. You are missing that foundation. You are to jump from somewhere else to be effective at that point, but how do you bridge the gap? Yes, it raises a lot of interesting questions, to be honest.
**Lilly:** I think it puts a lot of responsibility on us when we're implementing systems like this to think through those second and third-order impacts on the world around us. Not for just solving the problem right in front of us, but for what that problem was doing in the world in the first place and whether while it provides a point of friction, that friction is also something that we have been learning from over time as a part of the larger ecosystem.
I liked the part in the article that you wrote where you were talking about using the uncanny valley sensation, that kind of misstep eeriness as a way of reminding ourselves that what we are dealing with here is not actually human and that it is a machine and that there are things that we need to be mindful of around it. This particular feeling is a good reminder of that and a good tool and that kind of thing. In terms of the way that people have approached the uncanny valley problem, if indeed it is a problem, in the past in many different kinds of fields, there are some folks who have tried to bridge that uncanny valley and say, "Right, the goal should be that we're getting right to the other side of the valley where we need to have something that will behave exactly like a human being at all times."
You see this in some applications of animation, for example, where this problem comes up where people are pushing the boundaries to try and have more and more realistic animation over time. At the other side of that, you have folks who are saying that the uncanny valley should just be avoided, that it's not actually worth bridging, that the goal is not about that, but it is to stay on this side of the valley and work with the thing within the limits that it has.
I think for me, one of the interesting applications of this mindset was, for example, when they were animating Toy Story, which was very early on with computer-generated images, and they chose this story based on plastic toys because they knew that they could animate something like that without falling into this uncanny valley trap, that this fit the level that the technology was at at the time, and that they could tell a good story within the bounds of what was possible, but that they firmly acknowledged that those boundaries were there.
Do you think that the uncanny valley should be bridged, or do you think it should be avoided?
**Srini:** I think it's more about being aware of that can trigger your set of things that you can. It's not something can be avoided. It is something to be looked at at every aspect of the work as in the Toy Story example you said. It is not just for the end user. It's also the people who are building it. It can show up in different places. The moment if you show up in different places is also a good reminder to how we can understand this better or how we can make it easier for someone else to actually work with us. I can think of end of the day AI feels like it can reason, but we know it's a probabilistic model.
Having that mental model helps you to actually approach it with what else people can assume from it, how we can bridge gaps around it, or how we can enable people to be aware of those things. Not giving them bit of a guided exploration or some guidance on it lead into a lot more assumptions building on top of it. That's where it leads to the place where it definitely going to be an uncanny valley, but the problem of that can be catastrophic for how they interpret it.
I think this happened in data explorations at other places as well. I would say, for example, even you're taking data algorithm, if it's blindly implemented, the outcome or outcome of the choice of the machine is just implemented without considering the context and other stuff, it can, and shown in many places that it is not a right outcome where people needs to actually question what the system is providing, why it's providing, and is the context is right, and they should have the ability to actually contextualize it.
**Lilly:** In addition to thinking about the uncanny valley as a mental model for working with Generative Artificial Intelligence technologies, in the piece that you wrote, you also talk about the kinds of tooling that people can implement to help minimize the likelihood of these kinds of uncanny valley moments. If the choice of generative AI tooling is something that people want to pursue and go ahead with in the context where they're trying to apply it, can you talk a bit about the ways that you would recommend people think about this in practice when it comes to minimizing those moments?
**Srini:** When it comes to minimizing these moments, I would probably say, for example, going back to the point of it is not a deterministic software. How we can make it more understandable, how we can make it reliable? There are modern techniques like evals or testing things or guardrails where you can make sure these kind of things cannot leak from building the system. You can also think about how people interact with it, not just the customers, the developers because their assumptions about the model actually can lead to an outcome that is not correct.
Every time a new model is coming out, there's a question also comes in like, "Is this better than the other one? How much better than this?" The question again is the context of the problem you're solving and a new model can do better in something else or it can be slightly better. As an engineer or a developer who's building this ecosystem, is to build measures and toolings, like testing techniques or establishing benchmarks like, "Okay, if my LLM can answer these questions reliably for these many things, then I can have some trust on it." I also put some guardrails which says these things cannot happen. It's building that foundation layer, you can call it, or a layer of things that can help you to have a good sense of that from my context of the problem.
Again, I stress the context of the problem because there may be off-the-shelf guardrails and other stuff which can be very generic. It may give you a false sense of promise saying like, "Okay, this is taken care of," but the context of the problem is the key is where your business use case or the problem you're trying to solve a very specific question. That's where you need to go back to the first principles and find out what is the right questions that I need to make sure if this model replies is still valid.
I think in a way, that's the role of the developers or engineers, is to make sure the shiny models keep dropping, but does it make sense to adopt, whether it's safe, whether it's safely built, how people are going to interact with the system or their controls? Are there controls in other places where they can actually adapt to this more? Those are the things I would say.
**Lilly:** Yes, it's the right tool for the right job and making sure that if it is the right tool, you're thinking through the context that it's going to be applied in, and those knock-on impacts on the wider ecosystem, I think. Is there anything that you would like to leave our listeners with today in terms of thinking through how the uncanny valley could be useful to them in their work?
**Srini:** Working with LLMs, I think previously, automation is probably done focusing on replacing mundane tasks or can we do this efficiently, or using machinery and other stuff. LLMs I think people are engaged in creative work with it, as in can you generate a nicer image, or can you generate a bunch of ideas or an approach? This is more of a cognitive work. When you're doing cognitive work, it is very important, even when you're working with someone else, in establishing what is the outcome you want to achieve, or my assumption about the other person or how they are thinking through. Is this correct?
It's reducing those feedback loops or how we can course correct. That becomes paramount. I think that's where for everyone, this concept of uncanny valley could be a good reminder about, "Okay, do I understand about the other side of the things enough? Why did I fall into this? What are the things can be looked after? Would someone else also allow this in a way? Is it something trivial or is it going to actually have a knock-on effect?"
I think this concept of thinking through this like, "What would I feel when this happened and why did I feel through this?" The constant reminder of it's a cognitive work. When you're working in a cognitive work, this common understanding and knowing about the other side of things is quite important.
**Lilly:** [background music] Well, Srini Raguraman, thank you so much for joining us today on the Thoughtworks technology podcast. I'm pleased to have you here.
**Srini:** Thank you, and thank you for having me.
[ Read more ](javascript:void\(0\))
[ Hide ](javascript:void\(0\))
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
## Start your enterprise AI journey
[ Learn more ](https://www.thoughtworks.com/en-th/what-we-do/enterprise-ai)
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