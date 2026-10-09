<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/green-software-engineering | Title: Green software engineering | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Green software engineering 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons and Alexey Boas | Podcast guest  Isabelle Carter and Ken Mugrage
April 22, 2021 | 31 min 2 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/green-software-engineering#transcript)
Listen on these platforms
## Brief summary
There’s increasing awareness of tech’s carbon footprint but to what extent can software developers help? Is it possible to measure the energy efficiency of your code? Can you write code that saves energy? Our podcast team unpick the art of the possible when it comes to green software engineering.
**Podcast transcript**
Rebecca Parsons:
Hello, everybody. Welcome to the Thoughtworks technology podcast. My name is Rebecca Parsons, the CTO of Thoughtworks, and I'm one of your regular co-hosts and I'm joined by my other co-host Alexey.
Alexey Boas:
Hello, everyone. I'm Alexey Villas Boas speaking from São Paulo. Very happy to be here.
Rebecca Parsons:
Great. And today we are joined by two guests. Isabelle Carter is a developer working with the office of the CTO on research projects. And Ken Mugrage is another member of our office of the CTO who has a long history in thinking about issues of dev ops and continuous delivery. So welcome, Isabelle and Ken.
Isabelle Carter:
Thank you.
Ken Mugrage:
Thank you.
Rebecca Parsons:
And today what we want to talk about is green or sustainable software engineering. And I want to start by contextualizing this a little bit because we aren't going to talk about all of the issues around green cloud. And we know that's a big part of how organizations are looking to achieve their sustainability goals, but we have a whole other podcast that's going to be focused on that. So what we want to talk about instead are things more at the software development level. So things around how we create our code, how we measure our code, how we test our code, things of that nature. So to start off first, what are the reasons that this is even an important topic? I mean is this just green washing?
Isabelle Carter:
I mean, I would say it's not really, even if we ignore the obvious answer of the environmental impact, there's definitely a business case to be made for trying to create more energy efficient software. Reducing the energy impact will save costs. Cost is the big one. You have reduced the cost of your data centers of the offices you're in, so that's a really easy benefit to see. Outside of that, there's also battery life, particularly for mobile devices, but outside of that as well, and things like sensors and autonomous devices, if you can increase the battery life of those, it'll also save money in the long run.
Rebecca Parsons:
Let's say I'm conscious of the energy consumption of the code that I write. What do I do? How do I get started? What kind of tools or frameworks or algorithms or whatever is out there to help me?
Isabelle Carter:
I would love to just pick up something and hold it up on a pedestal and say, look at this. We should all be using this, but unfortunately there's nothing like that quite yet. There are tools out there to measure the energy consumption of software, but nothing quite as developed as we would hope. There are two primary categories when it comes to measuring the energy output of software, there's physical device measurement, which is a physical device that you hook up to the power supply of the machine, and that will measure the total power consumption of the machine. And you can get the energy from that. And then there's software that'll do it as well. The software side is where it's going to be, in the future, easier to actually measure the energy consumption of software. The problem is, is it hasn't gone that far yet.
Isabelle Carter:
The area where it's best would be mobile devices around Android and iPhone. They have some pretty great interfaces that allow you to dig deeper than most other things and to find out where the energy is being consumed. Beyond that, when it comes to the server and desktop side, it's all kind of a mess. Most of it's from academic research, but there are a few tools like Power API, where you can, if you take the time to set it up, which would be a process, where you can get some good data out of it, it would be very raw data though. And it would be a lot of work to actually go through and set it up. And most of the tools are very specific to architectures as well. So measurement is a huge barrier into writing energy efficient software. And so going forward in the future, I'm hopeful that someone will build up upon these tools and it will become much easier to get that data from it.
Ken Mugrage:
Yeah. So this is also one of those areas where the continuous integration and continuous delivery comes in because the tools aren't out there today, that's very, very true. But even if we had a magical tool tomorrow, if somebody releases a thing that's going to make really accurate measurements and allow you to set a baseline and all the things that we'd want to do to really track improvement, just a simple matter of running those tools in a continuous way is going to consume quite a bit of energy. You know, so if I am trying to make my energy consumption better and I run my pipeline a hundred times over a week or so with different configurations to see what the outputs are and so forth, depending on the application and how many users it's going to have, or how scalable it is, or what have you, I may have consumed more energy just in baseline and making a small improvement, then I'll end up saving over the life of that release or that deployment. So it's a really challenging thing where measuring it could be a higher impact than running it.
Isabelle Carter:
You might even have to consider trying to measure that measurement going on in CD.
Alexey Boas:
That's quite interesting. It feels like when we look back at some of the history of computing, we have come from a world of limitations of resources, but now it feels like we got used to infinite computing cycle resources. So the computer's on, so it doesn't matter if it's computing or if it's not. And then this is exactly going the opposite direction that no, no, we have to pay attention to that. But apparently we got to used to just using up resources freely, and then not caring about that.
Isabelle Carter:
Well, speed's been the name of the game forever now, and now we're at the point where, as you said, we have pretty much all the speed that we could ever want. I mean, we still want more, but we've kind of forgotten this energy aspect.
Rebecca Parsons:
So what do we know about how to approach making our software more energy efficient? Have we learned anything, really, anything that we could extrapolate from?
Isabelle Carter:
There's a fair amount known about making energy efficient technology. Most of it would be around the hardware side and then there's the green cloud, but in our sliver and actually writing green software, there's less knowledge, but there is some, and some of it's highly specific. It gets down to the level where there's good empirical data on the performance of programming languages when it comes to both speed and energy efficiency. Some of it's fairly obvious like C, C++, and Rust are very fast and very energy efficient and things like Ruby and Python, not so much, they're on the lower end. A surprising point would be Java. Java is actually pretty much middle of the road for all the metrics and does a pretty good job. So if performance is a concern and energy efficiency is a concern, you can look at what programming language you're using and make a choice based on that and what your goals are and get a very easy when they're outside of that, you can look at design patterns, there's some benchmarking on the design patterns, in their energy efficiency, things like the decorator pattern are really energy inefficient and intensive, but things like flyweight are really energy efficient.
Isabelle Carter:
And then there are ways to mitigate that energy inefficiency from some of those design patterns, through compiler transformations and things. So there are some very specific things you can do, you just have to know about it. And that information is not really that easily accessible. Most of these examples I'm mentioning are from academic papers and vast majority of us don't take the time to read academic papers unless you're kind of an academic nerd like I am.
Isabelle Carter:
And so that knowledge gap and barrier is a real issue here. And figuring out how to inform developers about these things is going to be important going forward. To name some other examples would be like thread management, depending on the problem you're solving, the style of thread management you use is going to have an impact on your energy. AIML, the dataset, they're the larger, it is the more energy inefficient it's going to be. As far as unknowns go though, I think the biggest one that stands out to me would be the relationship between object oriented programming and energy efficiency. That relationship is unclear how it's not a straightforward issue because these things really depend on multiple factors. You know, the programming language you're using, the hardware you're using, all these different things come together to affect this.
Isabelle Carter:
But what is that relationship between the objects you're creating, how they're interacting in the energy efficiency or inefficiency? That's a question that I don't know the answer to because it's fairly unclear, especially given some of the data that's out there. Sometimes it looks like when I'm looking at the data from different papers, it looks like it doesn't have that much of an impact, but then there are things like the decorator pattern where it's creating a lot of these smaller objects to the backend that you don't even think about or see. And because of all that, it's making it highly energy inefficient. So there's something kind of fundamental there that isn't quite understood yet about why that's inefficient and what is the relationship there.
Rebecca Parsons:
Well, and as a compiler person from long ago, one of the things I found interesting about the research you uncovered around things like the decorator pattern is, because the way it's a structural issue with how the compiler normally treats your use of the decorator pattern, which results in the creation of these objects, that there is kind of a structural optimization that can be done so that you can cheerfully write the decorator pattern code, but you could envision an optimization, a compiler optimization that during the compilation phase, could do a transformation on that to something that is more energy efficient. I was actually rather surprised because C++ relative to languages like C and Rust can be much more complicated in terms of being able to do a good job of optimization. And I think the positioning of Java in that has a lot to do with the work that's been done on the Jit compiler over the years. And so you can see how you can get a general uplift from some of this underlying compiler optimization technology, which I think is a fascinating area to explore.
Isabelle Carter:
Yeah, I think you're absolutely right. And one of the things that stood out to me about the decorator pattern is, it really is mostly cosmetic and for the developers, and that has such a big impact on the performance and energy efficiency, it kind of makes me take a step back and think about the times of refactored code and made it to where it's more readable. What was the real impact of that refactoring? Did it make the code actually better by some objective metrics or did it just look pretty?
Alexey Boas:
And then you have some of what Ken was talking about as well. Right? So if the code is harder to maintain and you introduce a bug, then you are going to need more energy to fix the bug you’re going to run into inefficiencies because of the bug and all that. So when we take that broader systemic approach, it doesn't get very much more complicated as well.
Ken Mugrage:
Yeah. And frankly, just that whole development process, you know, one of the things that we talk about in a continuous delivery world is the fast feedback, the feedback loops of, I made a change, whether it's to try to gain more energy efficiency or not, whatever the change is, I've made a change and I want to get feedback as quickly as possible if that broke something in my application, that's really the whole point of continuous delivery. And so there's a tension there, like there is, I think a lot of times in technology between, I want the fastest feedback I can get, I want to be able to deliver things. I want to run all of the tests all of the time. I'm not particularly a fan of the patterns that some people apply where they've tried to take away to say this change I made will only affect this part of the code. So only run those tests. Quite often, that's just simply not the case. And so frankly, and there's no good answer for it. At least I don't have one, but we have to acknowledge that there's these tensions out there that we're wanting to do things to get faster feedback loops and to get continuous delivery and continuous deployment and others, and those have an impact. And we need to at least be aware of that.
Isabelle Carter:
I mean, you're absolutely right and what you're getting at gets to a larger issue of balance. There are a lot of different variables that need to be balanced here and throwing energy efficiency into the mix only complicates things because the impact when you optimize for energy efficiency is going to have unforeseen impacts on your performance. And then there's also as you're optimizing, as we've been talking about continuous deliveries, is as you optimize, you're going to be spinning energy. So are you going to end up in the red or are you going to end up in the black?
Ken Mugrage:
Yeah. And I mean, one of the things that I've seen that helps this for sure, maybe not on purpose, Rebecca likes to talk about second and third order effects. But when, if you have a small component architecture, whatever label you want to put on it, microservices, or what have you, the smaller the code base of the thing that you're changing, the lower the number of tests, the lower of things you're running and doing it, but of course there's the trade-off for complexity. And so it's just this interesting thing where your pipeline can be faster and you'll use less energy, and hopefully your changes are easier to track and test and those types of things, but you are getting your trading complexity for that. And so it's a balancing act.
Rebecca Parsons:
And it has to be balanced as well against, what is the cumulative energy cost of this thing running and production. Isabelle mentioned training of machine learning models. If you only train the model once a year, but you run that model, say as fraud detection for every credit card transaction that comes through, you would probably think about, well, let's worry about the energy efficiency of the model because it's running billions and billions of times. And I'll perhaps worry a bit less about the energy costs of the training run, because I'm only going to do that once a year. And so it is this grand trade-off of what am I looking at in production, and how does that relate to what's happening in the context of the software development life cycle, whether that be model training, whether that be our bills, et cetera. And so, and it's often very difficult, I mean that's a pretty blatantly obvious example. You know, if something's happening for every credit card transaction that happens, you know that's going to be running a lot, but it's perhaps not always quite as obvious where the bulk of energy consumption would come from. And therefore, where should I think about optimization?
Alexey Boas:
And Isabelle, you did mention one thing that I'm curious about that I know that you looked at that and it's in your research. So about energy efficiency being a new variable that adds to the complexity. So, I mean, my intuition would tell me that there's a strong correlation between energy efficiency and speed, but if I'm consuming less energy, I have fewer competing cycles, things run faster and it's not the same thing, right?
Isabelle Carter:
It's not, and it's pretty unintuitive. And it was surprising to me at first, but there is a direct relationship between time and energy. The formulas that commonly gets used involves both time and power. So there's definitely a strong connection there, but it's not straightforward. There's a lot of data out there that just shows that sometimes as you increase the performance or make it faster, you end up spending more energy. And sometimes the opposite happens as well. So we all want things to be fast and highly performant, but the cost of that in many cases is a highly energy inefficient code. And so is the opposite. So if you want to make something energy efficient, you also need to keep in mind and have this balancing act going on of, okay, well, it needs to be fast enough to actually meet our needs, but we don't want it to be energy inefficient.
Isabelle Carter:
So you might have to take a step back and make it slower to get some more energy efficiency and trying to balance that is difficult. One of the best examples I can think of where the energy efficiency and performance don't quite align, it's with thread management. In the data that's out there, in some cases, as you increase the amount of threads, you get higher performance, as you would expect, but the energy efficiency, you end up spinning much more energy, the more threads you throw into the mix. And so it really depends on the type of problem, and you have to keep this in mind and try to balance it. And that balancing act is very difficult. I don't know how to advise someone to do that yet. That's something that would come down to your requirements, having discussions, figuring out what your needs are. And there's not really a methodology out there that really talks about that.
Rebecca Parsons:
So it seems like we have lots of different trade-offs that we've kind of alluded to. I want to drill in a little bit more to the trade-offs of the software development life cycle. You mentioned speed of feedback and application complexity, any thoughts on how we even begin to try to model or make the trade off decisions of, is the delay of the feedback on the functionality, is that delay better or worse than what we're doing from an energy perspective and any thoughts really on how we might even go about thinking about this?
Ken Mugrage:
Well, that's actually a really tough question because I always want to say the fastest feedback possible. Every change runs the pipeline, every change runs every test, et cetera, because there are other efficiencies gained by that, being able to fix the smallest amount of code when something changed and when something breaks, et cetera, there's lots of gains by getting that faster feedback. But I think like a lot of things, you have to take a realistic view on it. So what I mean by that is, if I think I'm going to gain two or three minutes faster feedback, and yet I'm giving up, like the multi-threaded example is a great example, it's a little bit faster, but it's orders of magnitude more, well, could be more inefficient, then I have to be realistic about that.
Ken Mugrage:
You see a lot of times, especially when people are talking about continuous integration, even before the continuous delivery, oh, all my tests run in 23 seconds and woo hoo, you know, I mean, that's great, but first off, it's a signal to me that you're probably not really running all of the tests. You're probably not running. And by that, I mean all of the categories of tests. If you're really getting feedback that quickly, you're probably not running security compliance, et cetera. But maybe depending on the risk of your project, that's okay. You know, if you're at a large enterprise and you're creating the service that provides animated gifs to the chat server, maybe it's okay to only run the security stuff when you're a little bit farther to the right down the pipeline so that you can get the faster feedback and not be using that energy and that time upfront.
Ken Mugrage:
But if you're running credit card processing, especially if you're my bank, please do run the compliance and security tests in that first batch. So it's really about looking at it case by case. I think it's not something I've ever seen done, but I think having something like, you see risk mitigation plans. So if we're collecting this kind of data, these are the kinds of compliance checks we have to do, those types of things. You know, maybe it'd be good for organizations to come up with those guidelines. So we want self-organizing teams, at least teams could look at the guidelines and learn from that and know when to apply the different things because there's really no easy answer to it.
Rebecca Parsons:
So let's pursue that a little bit more. Do you think we're at the stage of maturity and understanding about the energy efficiency of code to be able to come up with some general principles or is that still too early?
Isabelle Carter:
Personally, I think it's probably still too early. There are some rules of thumb that I could quote off, but they're highly specific things. I think that for most people trying to write energy efficient software is probably not worth the investment at this point in time. For larger corporations, it makes sense. They have the time, they have the money, they have the personnel and the resources to invest in it. But at the moment it is a rather large investment to do. I mean, there are super easy things people can do, some of them I've mentioned already, like effective thread management, when your design patterns, effective caching, reducing the IO operations or doing them in bulk because they're highly energy inefficient. But beyond that, trying to get some principles and on the level of actually writing the software, that's very difficult, predominantly because, the thing that I always go back to in my head is, there's not a great way to get the data.
Isabelle Carter:
Like when you're doing performance optimization, the main thing you need is data. It's really hard to optimize performance if you don't know how fast it's going, same with energy, but it's a significant investment to get some of these tools up. And you might even have to rearchitecture in order to use some of the tools that are more effective, because they are very specific, some architectures. So it's a huge investment upfront, you're going to spend a lot of money on the energy to get that going as we've talked about. And then it gets hard because you may not be able to measure what you want to measure, pretty much the best you can get is per process level. And that's not going to tell you a whole lot about where you're spending that energy. So it's hard to give some of these guidelines, especially on a smaller case basis.
Ken Mugrage:
You alluded to something there that I think we often overlook, especially, I mean, the four of us on this podcast are technologists at core. And Isabelle, you mentioned upfront when we're talking about why even do this, that there is real business value here of, using less energy costs less money. There's also the business value of air quotes here that you can't see, doing the right thing. There's business value to that, frankly we see all the big, I know there's going to be a separate podcast on green cloud, but all the cloud providers touting their drive towards energy efficiency and so forth. Other enterprises can do that. Increasingly, research that we've done for like the Thoughtworks Looking Glass, as people are making buying decisions based on the habits of organizations. So if you can demonstrate that you're putting effort into this area, people will choose you versus a competitor. So there are benefits to doing this that aren't measurable in the quantitative way that we as technologists want it to be. But I really do think there is a value to doing the right thing.
Isabelle Carter:
You're definitely right. I guess more of the level I was talking about is, are you getting that benefit if you try to apply it to the software you're writing? On a smaller scale basis, absolutely not, on a large scale basis, I think there is definitely a potential with the way things look right now, I'm hopeful in the future that things will continue to evolve and it will become much more straightforward and manageable to do energy optimization, just like performance optimization.
Rebecca Parsons:
So let's push on that question a little bit, if and when we get to this carbon neutral net zero future, will we still even care about this? Is this one of those things that, we're just in this time when climate change and sustainability have a huge focus?
Isabelle Carter:
The super cynical side of me says that the world's going to end so probably, it's not relevant, but I think it will, predominantly from the cost perspective.
Ken Mugrage:
You see, and I'm less sure, because let's say that we had the perfect renewable energy data center somewhere. So whether it be wind or solar or whatever it is, there are still real costs there, windmills break. They can require maintenance there, et cetera. And so even if we're not completely destroying the planet at the time, we're still doing things that require investment. These technologies aren't ever going to be cheap. I mean, they're going to be a lot cheaper, I hope, but there is still an investment there. You know, we have a hybrid car that was, I think, four or $5,000 more than the non hybrid version. You know, the technology is still a little bit more expensive and maybe we get there, but you still have to maintain those things and build those things.
Isabelle Carter:
Yeah. I think part of the way I hear the question is, if we don't have to care about the environment, do we care about energy efficiency? And I think yes, because I mean, as you were saying, it directly relates to cost and if you can make it more energy efficient, you're reducing the cost.
Rebecca Parsons:
Well, and I think in particular, when you start looking at more mobile devices, more remote sensors, those are just going to increase in numbers, not decrease. And each one of those, there's the cost associated with recharging it. And even if there isn't a climate impact or environmental impact, there is still the cost.
Isabelle Carter:
You're absolutely right. And that's in large part, the reason why the tools around measuring energy efficiency for software are pretty highly developed when it comes to mobile devices.
Ken Mugrage:
No, I think I just wanted to reiterate that I strongly believe there's a do the right thing factor here and the tools aren't there yet. And frankly, I don't have a lot of confidence that the tools will get there just because of the nature of the computing landscape. As we move more to edge computing for all kinds of reasons, less and less of the energy consumption is on my server, if you will. So I'm providing a service that the energy consumption is happening on a remote device, or at the edge, because I want to take advantage of low latency, things like 5G and Wi-Fi 6, et cetera. So I don't have a lot of confidence that the tools are going to get there, frankly, but I think we can make incremental improvements and that's better than doing nothing.
Isabelle Carter:
I'd say I, by and largely, agree. I hope the tools get there. I think the best shot that we have for the tools getting there is somebody picking up an open source project that's created out there, like power API, and helping that grow, or someone like Amazon creating a tool that they use internally and releasing that. I think that those are the two ways, but those are both long shots, but even if those tools don't get there, I think we can care about doing the right thing in terms of technology and put our efforts in the areas where it is more developed like green cloud and managing your servers, going with more environmentally friendly hosting services and things. I mean, there are things we can still do to make sure we're doing the right thing, even if we can't necessarily make our software more energy efficient right now.
Rebecca Parsons:
Well, Isabelle, Ken, thank you, Alexey. Thank you as well. I really enjoyed thinking about all of the different trade-offs, as we often say when we talk about so much about technology, it's always a balancing act. There are always trade offs and this, by introducing a new variable, we've introduced lots of different balance points that we need to consider. So thank you very much, Isabelle and Ken, and thank you all for listening to the Thoughtworks technology podcast.
[ View full transcript ](javascript:void\(0\))
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