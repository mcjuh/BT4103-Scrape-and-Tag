<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/xr-in-the-enterprise | Title: XR in the enterprise | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  XR in the enterprise 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Rebecca Parsons | Podcast guest  Margaret Plumley
February 11, 2021 | 25 min 39 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/xr-in-the-enterprise#transcript)
Listen on these platforms
## Brief summary
Once the preserve of gaming and consumer electronics, extended reality (XR) — a combination of virtual and augmented reality — is now finding applications in the enterprise. This might be in testing and training situations or data visualizations. Here, we explore the implications this technology has for the enterprise software development lifecycle.
**Podcast transcript**
Alexey Boas:
Hello, and welcome to the Thoughtworks technology podcast. My name is Alexey Villas Boas. I'm the head of technology for Thoughtworks, Brazil. And I will be one of your hosts this time, together with Rebecca Parsons. Hello Rebecca.
Rebecca Parsons:
Thanks Alexey. Hello everybody. My name is Rebecca Parsons. I'm the chief technology officer of Thoughtworks, and excited today to talk with our guests, Margaret. So Margaret, would you please introduce yourself?
Margaret Plumley:
Thank you for inviting me to be here. My name is Margaret Plumley. I'm a product strategist in the XR practice lead for North America. Very excited to be a part of this podcast.
Alexey Boas:
Happy to have you with us, Margaret. Thank you so much for joining. And so the conversation today is about XR, extended reality. And then why don't we start with the definition? So Margaret, can you guide us through what extended reality is, and the difference between all the acronyms AR, MR, VR and et cetera?
Margaret Plumley:
Sure, absolutely. So, AR, augmented reality, MR, mixed reality, VR, virtual reality. The X is often used as a variable to mean any of the three, or extended reality. And VR generally means if you have a full headset, and the entire world is virtual, versus AR where you're augmenting the world that you are in, and mixed reality is somewhere in between the two generally, used when you're referring to smart glasses. But yeah, lots of acronyms, and you can even add more technologies in there and combine it with things like IoT, and have all the acronyms you want.
Alexey Boas:
Well, and it's definitely getting more and more interesting as time goes by, but at the end of the day, these are not new technologies, right? So, how have they evolved? And what has changed? What is new these days about these things?
Margaret Plumley:
You're right. A lot of these technologies, especially virtual reality have actually been around for quite some time. The biggest changing that we've seen, is in the hardware price and weight. The price has gone down by about a decimal point, so has the weight and the number of cables. In fact, you can for a couple $100, buy a very good virtual reality set. And also the software is off-the-shelf. Gaming engines like Unity and Unreal are being used. So you don't have to write everything from the ground up. And the consumer applications of course, are the ones that are driving this. So they're driving down the cost, and they're driving up the usability of things like Unity and Unreal, and enterprises are able to harness this. We're seeing these consumer headsets are being used in everything from training for retail, to training for medical students. And the enterprise itself has gone from proof of concept to KPI, because they are actually seeing the return in using these applications.
Alexey Boas:
Yeah, that's cool. It's really like the technology is going beyond just a cool booth at an event to real use cases inside the enterprises, right?
Margaret Plumley:
Yeah, they are. They've really gone from... Most people when they think of AR, VR, they think of games, they think of consumer, but they've actually been used in enterprises with really positive return. You're seeing actual cases where time on task is reduced by anywhere from eight to 30% in industry. So, there are some very real enterprise level applications out there with very real results.
Alexey Boas:
And from a software development, or from an application development perspective, so how do things change when they develop things for XR versus developing a web application, or other technologies that are more common?
Margaret Plumley:
Well, the world is the interface, right? Even on AR, when you're using your phone, it's not just the rectangle that you're designing for, that rectangle is just a magic window into a larger world. And this changes how you think about designing. You're no longer drawing shapes on a flat surface, you're putting objects in the real world. And it also changes how developers need to think. About 20% of it is a new scripting language, but 80% is a whole new world. You're creating 3D objects, you're applying shaders and lighting, and it's actually a 4D world, because you also have time. You can have all the triggers that you have in a gaming world, and you can apply them to the real world. So, you can use these gaming triggers in the industrial world, where you can walk up to some sort of machinery, and it shows you the IoT in your mixed reality glasses. So you can look at a piece of machinery and it shows you, what the current status of it is, but that also means that development and design, you need to think in terms, not just all three dimensions, but also in terms of these triggers that go with it. But because of that, it's also an exciting new challenge, both for the designers, and the developers. There's a lot of innovation here, there's a lot of green field, and a lot of opportunity.
Rebecca Parsons:
Well, isn't it also conceiving of what the solution to the problem even looks like? I mean, we as technologists have been trained to look at a problem, and think of a solution to it. And when you think about, okay, how would I imagine a customer support interaction within a virtual world? Even how you think about addressing the problem is a challenge. So, what are kind of the skillsets you think people really need to bring, in order to think about the world as the interface?
Margaret Plumley:
That's a good point. And it is a question of making sure that you think about the entire ecosystem, and you don't turn the technology into just a shiny thing. Anytime you have a support issue, you might not necessarily need to have a remote assist AR application, but you do need to have some sort of a support ticket. So, it really is a matter of looking at that entire ecosystem, that goes with the problem that needs to be solved, and what technology you do and don't use. AR isn't always the answer. You shouldn't need to download an app, have the latest phone, have an unlimited data plan, to be able to find the entrance to a hospital, right? Sometimes you just need a big arrow on a sign. So, it's really important to think about, what is the problem that you need to solve? And what is the right tool to do that? And how do they all interact with each other?
Margaret Plumley:
And how does it interact with the entire ecosystem of what you're doing? If you're building a training system, you want to make sure it interacts with the LMS, with the learning management system, same for any of these other things. If you're doing AR shopping, then you want to make sure that it interacts, not only with your shopping cart, but also with your stock system. You don't want to show some incredible thing that they love, but you know what? That was last season, and you don't have it anymore. So you want to think about that end to end, not just the end to end user experience, but also what is that end to end technical solution.
Alexey Boas:
Yeah, I find it very interesting, what you say about how design changes, and when we think about more traditional applications, the development of web application, or even a GUI application, you always have that frame of reference, which is the screen. And you can use that as a powerful limiting resource, to think about the interactions and the things that people do, but that changes completely when you have the world as the interface as you put it. So, I wonder how the design process itself changes with things like even prototyping. So, do we have the tooling to do that, or the techniques? So what have you seen in that sense?
Margaret Plumley:
Well, you see a little bit of everything, and trying new techniques is always part of the fun of designing something new. And it's also important to understand where your old techniques don't work. If you immediately start with a 24 inch screen to design an application, even for mobile, it's not going to work. So if you are designing for the world, you want to prototype in the world. I mean, I've sat around when I'm thinking about doing things, I'm sitting in my house, and I'm putting tape on the floor, and I'm hemming things up on the wall and I'm saying, "Okay, what would it be like if I were to walk through, and I was looking for this? What would I want to see? And where would I want to see it?" So, it's actually a lot of fun. You get to be very creative here, and you get to go back to cutting things out of paper, and using tape and scissors to put it up, but it actually works. You need to build these sets, and I think, anybody who has a background more in theater or in architecture, because they're used to moving through a world that becomes very helpful when you're designing for this world, because you do have to design differently.
Alexey Boas:
Yeah, it's interesting you mentioned other areas, and architecture, and theatrical arts, because from one perspective, some of these techniques, they have been very developed in gaming, and in filmmaking, right?
Margaret Plumley:
Yes, they absolutely have. A lot of the techniques come from there, a lot of the tools come from there, and it actually... You have a lot of the talent comes from there as well. I mean, I used to work, as you know, in the film industry where I worked with some amazing artists, and a lot of them have gone on to be working in VR, in AR, and building these kinds of worlds where you can build, because you have that level of talent, you can build hyper-realistic worlds, that they are fully immersive, which is part of why it's so successful to do things like training in VR, is because you can recreate this entire world. I mean, you have applications where doctors learn surgery in VR, right? Because you can create that world. You can create things to help people practice these sort of rare and dangerous cases.
Margaret Plumley:
Like, how do you learn how to handle working in construction, on a freeway? Well, you kind of don't want to just throw somebody on a freeway with trucks going by, but you can create something in virtual reality. And those are one of the brilliant cases, these training applications are so fantastic. And because you do have a lot of the tech, and a lot of talent that comes from movies and games, you can create a fantastic environment in which to do these things. In fact, there've been really fantastic results, not just in terms of the ability to complete a task, but if you look in the medical world, on the one end of it, there's doctors being able to practice surgery. I mean, how do you practice surgery on a human being? Do you want to be the first time somebody has done that surgery?
Margaret Plumley:
Do you want to be the doctor doing it for first time on a person? Having the ability to do it in VR, is helpful. And also for patients, like there've actually been studies on where, before a patient goes through a procedure, if they are able to experience it in VR, then when they go through it for real, their fear is reduced. And therefore, their response to the treatment is actually higher, because they don't have that stress aspect. There are a lot of incredible results that you get from this training because you can't create a whole reality.
Rebecca Parsons:
Now, you've talked about some of these really exciting applications, but if so much of this technology, and so many of the approaches come from the gaming world, what about making it enterprise ready? What about making it something that a medical school would feel comfortable turning their doctors, or their medical students more precisely loose on? What have you experienced in terms of moving these processes and techniques into the enterprise environment?
Margaret Plumley:
They've actually been very successful. And you see that in training, you see tremendous success, you see tremendous success in medical, but a lot of times, you don't see success because it's happening in silos. And I think that's where a lot of it falls down, is if somebody tries to turn it into a shiny thing, and doesn't take into account the rest of that whole experience, then that's where you don't have the success. If you want to create something that is a really good experience, it needs to be, again, end to end experience for both the person who's experiencing it, and for the company that's building it, right? It needs to take into account, training the LMS, you need to take into account, like, what is the right answer? Right? Is this the right time to do VR? Is this the right time to do AR? What are we trying to achieve here? So, there is success when it's done right. You just have to make sure you think about, how do you tie it together? How do all of the pieces hook together? If you look at something like even task completion, you're seeing tremendous gains in that because people have the tasks lined up in front of them, but unless you build that properly, and unless you hook it up to everything, it's not going to work.
Rebecca Parsons:
And we've talked a lot about the design aspects of this. When you think about the software development life cycle as a whole, one thing that comes to mind to me is, the differences in testing. Just the number of degrees of freedom, that you have in this four-dimensional world as opposed to this, first this will happen, and then, and that, and that. What can you tell me about approaches, particularly in these more mission critical settings, for thinking about testing?
Margaret Plumley:
Yeah, that's definitely a big issue, because you need to think, and you need to rethink, like, what's your schedule for doing anything? And what is your methodology for doing everything? Because when you're testing, you'd have to make sure that, did the code do something, but it's very important that did it do it right? And can you apply your old methodologies to it? Like you want to do continuous testing, but that interaction, and there is the complexity of multiple devices. If you are in say a training in a school situation, then you can control what devices people are using. You can say, okay, you're using this model of this headset, and test just on that, and test exactly what people are doing, versus if it's a broader sense, if you're doing something where it's more... You're building something for your customers, and you don't know what device they're using, you have a much broader test or testing spectrum, and you also have to consider multiple things like, do they have the data connection?
Margaret Plumley:
Do they have the app? But then you want to make sure that you're testing the right thing like, do people just learn how to game the system? Right? Are they learning how to respond to the triggers that you built up? Especially in a training system, this is so important, that you make sure that they didn't learn how to react to your training system, like back when we were all playing Pac-Man, you learned exactly which moves to take to finish the level, is entirely different to learning how to actually complete a task. So you do have to think about your testing in a different way, and part of it is the mechanical tools, and part of it is actually, what are you testing?
Alexey Boas:
Yeah, that kinds of goes back to some of the things that you're saying, and some of the challenges for the broader adoption of, thinking in silos, and thinking about the whole system, the whole integration with the rest of the enterprise. And when we think about the enterprises, that sounds interesting to me, because it's connected to some of the other things that we usually believe in, like have, well, integrate the teams, multifunctional teams, we can think about different aspects. So you will probably need people who know about the specific AR, VR, XR technologies, but also about the business of the enterprise, and also about the rest of the technology ecosystem. So, is that something that is key for, in your opinion, for a successful adoption?
Margaret Plumley:
Oh absolutely. You still need to make sure that you, again, going back to those core questions of, what problem are we trying to solve? Who are we trying to solve it for? And what is the right answer? And making sure that you do have the right people involved. It's like any new technology. You don't want to just take the new technology, and try and stick it on there, if it isn't the right answer. So you want to make sure that you have the right skillsets, but that you're also, listening to everybody else who's involved, everybody from training to support, because anytime you add a new technology to your ecosystem, you add all the other aspects that go with it. You add the support, you add the training, you add all those other parts. So, you do need to pay attention to all of those, and make sure that everybody knows how they fit together.
Rebecca Parsons:
So, can you tell us about some other potential applications, or application areas that we haven't really talked about? And people think of things like training, and that's kind of easy to get your hand around, but what other kinds of applications that have been explored? Or thought about?
Margaret Plumley:
One of the ways that you see this technology being used, is just exploring and experimenting. If you look at places like NASA, they want to walk on Mars, right? And this is where you combine the technologies, where you take the images coming back from the rover, and you can build a 3D world, and then you have scientists around the world who can put on their magic glasses, and they can all be on Mars together. And you find that this is especially important now in the era of COVID, where people are apart. So you can sit there, and you can walk together on Mars, and you can look at things, and you can point at things. You also have other cases where you can glue all these technologies together. You think about any event, like say, you're running in a marathon, and you want to know, how far am I from the entrance to the exit?
Margaret Plumley:
Where's the nearest restroom? You can have a watch that buzzes, that shows you in one symbol where the next water station is, at the same time, the friends who are watching you run, can pull up their phone, and see where exactly you are, so they can get that picture of you coming around the bend, and the people who are running the event, know where everybody is in case there's an emergency, and they need to get people out. And you can apply that to any kind of an event where you combine all of these technologies, and they have different uses for all the different user types. A lot of times when you build a solution, you're building it for one target user. But in that case, I just mentioned three. I mentioned the person who is running, I mentioned the person who's watching them, and I mentioned the people who are running the event. And you can think about tying all these technologies together to serve multiple people in it.
Margaret Plumley:
And then, another one is when you look at things like travel, and history, and learning about a place that you're in, you can have things like AR apps, where when you go to these historic locations, you can actually relive events in those places. So if you think about tourism and traveling to different places, and again, you can combine technologies where if you need to rejoin your tour, the map in your phone knows exactly where you are, where you need to be, when you need to be there, and can tell you when to get back, but meanwhile, it can give you all the historical context of what went on, where you're standing.
Rebecca Parsons:
Well, and one application I saw a couple of years ago, which I thought was fascinating was, they were actually using a virtual world as a data visualization technique. So, you would map the data into this world as objects in the world, and then you could manipulate it. And you had various gestures to zoom in, to get more detail of a data set in a particular space. And it was really quite natural watching people, just sort of walk into this part of the room, and they were sort of engulfed in this hologram like thing, and here they are manipulating a data set and trying to draw conclusions from the data, with it being presented in that way. And for inherently three-dimensional data, that's actually quite a rich way of thinking about data, as opposed to trying to figure out how I can on a screen, really get the kind of three-dimensional projections, whereas you can be in the middle of the three dimensions, and really get a sense of it. So I thought that was actually quite an interesting way of using it, and taking advantage of that inherently three-dimensional nature of a world.
Margaret Plumley:
Yeah. And you could do that of thing, and you could walk up to an actual object, and see the visualization around that object, and see how does air flow around the aircraft, see the lifts, see the drag, actually move things in real time, and see how they change. You'll see this sort of thing a lot in architecture, and construction, where you can stand on a construction site, and you can show, how the construction site will change over time, and how it will impact lines of sight, and how it will relate to the environment. So being able to walk out to say where a freeway or where a building will be built, and stand there and say, "Okay, this is where the traffic will flow." Or, "This is how high the building will be." Or, "This is where the pipes will go, when they're built." You're seeing this a lot in architecture and construction actually, as you're seeing the guys who are going to wire the building, walk into this empty space and say, "Okay, I need these wires here. I need those pipes there." And being able to see all of it as you're standing there. So it's really incredible to be able to see it on site, where it's going to be.
Alexey Boas:
And one thing I find it hard to get my head around when I look at some of these things is, the sheer number of different areas. And of course, in my case, it's likely because it's far away from the things that I know. So you have a new technologies, you have to think about design changes completely as we've discussed, testing changes completely. You have even to think about things like graphical design, textures, sound. I know this might be a tough question but, do you have any advice for an enterprise software developer trying to learn some of these things? So, where to start, just take a look at Unity, or have a look at the tooling, or are there other things that people who want to learn more about how to develop these kinds of applications should pay attention to?
Margaret Plumley:
Yeah. There are a lot of professional organizations out there that can be a tremendous resource, both in terms of just inspiration for what people are doing in this area, and also in terms of information for how to do things, and how other people solve problems. I mean, there are newer organizations like the VR, AR association, which focuses obviously very clearly on that. There are other organizations, like for instance, when you look at SIGGRAPH, which is computer graphics, which in the past has been a lot of scientific visualization, and movie-making, and gaming, and now has a lot of AR, VR as well. So there are tremendous communities around this. There're also meetups, and a lot of tutorials online for learning how to use things like Unity and Unreal. So there are a lot of professional organizations out there to look into, and just see what people are doing, and how they're doing it, and get inspiration from them. And I really recommend going to a lot of these conferences, and just keeping in touch with the industry, and what's going on.
Rebecca Parsons:
Great. Well, it seems like we have an exciting future ahead of us.
Margaret Plumley:
Yes we do. It's really an exciting technology, an exciting green field, and it can be anything you want. You can build other worlds, or you can augment this world. So it's really exciting to see how it's coming together, and how people are pulling multiple technologies together, just to make a more exciting place.
Rebecca Parsons:
And multiple disciplines. I mean, I was involved with some people who were putting together a university college around digital arts, and they had screenwriters, and choreographers, and visual artists, and composers, as well as technologists, and all of the new kinds of collaborations we're going to have to work out. That should prove interesting for our industry, but I think it's really exciting.
Margaret Plumley:
It is. And if you look at places like NASA, they have people who used to work in the film industry, they are helping them to imagine these worlds that exists. How do you explore space? Well, it's a combination of a scientist with the facts, and an artist with the imagination, to try and communicate it back to your common person. What does Jupiter look like? What does it look like to go to an exoplanet? What is this experience? So there is this fantastic combination of art, and science, and technology that's coming together.
Alexey Boas:
And we're coming to the end of episode then. It was a great conversation, and a lot of joy to have you with us, 
Margaret. Thank you so much.
Rebecca Parsons:
Thank you Margaret.
Margaret Plumley:
Thank you for having me here. It's always good to talk about new and exciting technologies.
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