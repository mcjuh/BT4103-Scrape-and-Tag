<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/infrastructure-as-code-in-2025 | Title: Infrastructure as code in 2025 | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Infrastructure as code in 2025 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Ken Mugrage | Podcast guest  Kief Morris
March 20, 2025 | 29 min 07 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/infrastructure-as-code-in-2025#Transcript)
Listen on these platforms
## Brief summary
Nearly ten years after the first edition of _Infrastructure as Code_ was published by O'Reilly, Kief Morris is publishing a third edition of the book. But why a new edition now? What's changed in technology and business over the last decade?
Quite a lot, as it happens. To talk about what's new — both in the infrastructure world and in the book itself — Kief Morris joins host Ken Mugrage on the Technology Podcast. They discuss each edition and what's new in this one, and dive into the infrastructure challenges and issues that need to be tackled in 2025, from tooling and deployment to maintenance and infrastructure evolution.
**Learn more about the[third edition of Infrastructure as Code](https://www.thoughtworks.com/en-gb/insights/books/infrastructure-as-code-3rd-ed).**
## Episode transcript
**Ken Mugrage:** Hi, everybody. Welcome to another edition of the Thoughtworks Technology Podcast. My name is Ken Mugrage. I'm one of your regular hosts. I have with me today, Kief Morris. Kief, you want to introduce yourself?
**Kief Morris:** Yes, thanks, Ken. I am a distinguished engineer for Thoughtworks around infrastructure engineering in particular. I've been with Thoughtworks for about 15 years now. I've basically been working with infrastructure, automation, infrastructure as code for, gosh, probably 25 years now since before it was called that. Yes, that's my rough background.
**Ken:** We're here specifically to talk about a book you read called Infrastructure as Code. We're actually in volume three right now. When was the first volume published? When did it first come out?
**Kief:** The first edition came out in 2016. The second edition was in 2020, just in time for lockdown. That was a little bit difficult in terms of then getting out and talking to people so much. Third edition is coming out next month as we talk now. That'll be March, towards the end of March and early April, depending on which edition and where you are.
**Ken:** Cool. I guess first off, just what is the importance of infrastructure as code? Why should people be paying attention to this as an area, other than because of your awesome book?
**Kief:** [chuckles] I guess a lot of it is around, as you get a lot of infrastructure and especially as you're using cloud, you need to be able to manage it in a way that keeps it consistent and keeps it well managed. How do you make sure that stuff is updated with latest versions of stuff and kept patched? How do you make sure that you have consistency across environments, especially when you're doing things like your software delivery path to production? How do you make sure that when you deploy software in one environment, it's going to work okay the same way in the next? Code is really, as of now, at least it is the most effective way we have of being able to make sure that we can define what we want and then reuse that and reapply it and change it in a really manageable way.
**Ken:** Then just at a high level for our listeners, how do you define infrastructure?
**Kief:** That's a good one because it's like a platform where it means different things to different people. To a lot of people, it means the stuff that I don't build that I have available to me to deploy on or whatever, or to build on. For the purposes of infrastructure as code, I define infrastructure as the resources that are provided by an infrastructure as a service platform like your AWS, Azure, and so on, or data center. It's low-level resources that you need to assemble and put together in order to build and provide higher-level stuff.
When you think about, say, engineering platforms and a lot of the stuff like that, that's out there these days, I think of that as a layer on top of using your infrastructure to build your platform. That is what, say, developers use to build and people use it to test and deploy and run software on top of. I see three layers, really.
**Ken:** Cool. Since the first edition, or actually, I guess, since the second edition came out, what should people, if they've already read that edition, do they still get the third one? Is there enough different? What's changed in four years, five years?
**Kief:** I think a lot has changed. It's funny because when O'Reilly approached me to say, I think it'd be a good time to do a new edition. At first, I was thinking, well, it didn't feel like as much has changed, but since it did between the first and second. The first edition focused a lot on servers and how to build and configure servers. Things like Chef and Puppet and that level of stuff. Things like Terraform and CloudFormation and that level of thing were out and that was in the first edition of the book, but it wasn't as much of the focus.
The second edition then moved along a lot more into that of how do you-- less around servers, although again, it's still in there and more on how do you provision cloud infrastructure and make that work. I wasn't thinking there would be as much to do in this one other than some tidying up and presenting things maybe nicer since I'd obviously learned stuff in the years in between about how to talk about these things. I found that there's actually a fair number of things.
I would say the third edition has three sections and each of those has an area that I would say is fairly new or strong, much stronger emphasis now in the third edition. In the foundational section where I talk about, I've always talked about in this section of the book, things like how change is important. It's important to be able to manage change to your infrastructure reliably and that being one of the fundamental purposes of it. In the third edition, I talk a fair bit more around thinking about the business value.
In other words, not thinking of infrastructures as something that's generic that you lay out and then it's up to somebody else to worry about how to use it in your organization, but thinking about how do we make sure that we are building our infrastructure and managing it in a way that makes it easy for the business to grow in whatever way it needs to grow, to manage costs, especially these days. I think one of the big things that's changed in the industry is how much more focus there is now with the changes in the economy and everything else around, we need to consolidate.
Up until before, say, 2020 and even the '21 and so where a lot of the emphasis was on we need to build stuff and digitize and do all that stuff and get out there. A lot of stuff was built willy-nilly. Now it's a lot more, we got to consolidate. We got to figure out how to manage things. It's thinking a lot more around what are the business things that you need to be able to support and then what does that mean in terms of infrastructure and how should you think about your infrastructure. That's one big thing. Then the second section is really around design of infrastructure.
The thing that struck me as I was working on it is, so the second edition focused a lot on stacks. That is the idea of what is the deployable unit of infrastructure? How should you structure that? How should you break that up? If it gets too big, how do you integrate them and so on? Again, the third edition has a lot about that because that's still really important. Something that I think is getting more emphasis these days, and if you look at tool vendors and so on, it's that level above that of how do you put stuff together?
I've talked about the component model for infrastructure. I talk about like modules and libraries at one level, stacks is another level. Now infrastructure compositions being, how do you put those things together and manage them as groups? You see a lot more, I think tooling out there, things like what they call the tacos toolings, the Terraform automation control, something like that. I can't remember. Sorry about all the letters stand for, but it's these tools and services that are out there to deploy your infrastructure.
Those are focused a lot on how do you assemble this stuff? In the old days, and it's still what a lot of people are still doing is writing really custom scripts to put that infrastructure together, manage that orchestration and composition of infrastructure. I think we're moving towards realizing that we can't all-- So many infrastructure teams to spend all their time wrestling with that stuff with their custom scripts. There's got to go be more standardization of how to do that. I talk more about that.
**Ken:** I'm curious on that topic. We always talk about do tools enable things, or do they define things? The tools in this space, if you buy tool A, do you need to do things in tool A's way?
**Kief:** That's a big issue because I'm thinking something I do touch on a bit in the book is-- I talk a lot about, there are different patterns and practices and ways of doing things, different ways, not just like, "Here's the one way to do it." That's not what my book is about. It's about here's different ways that are out there. I do show my opinions on like, "I think some ways are better than others." Most of the tools that are out there tend to have their opinions about this is how you should organize your stuff.
Also, the third thing that's new in the book is very related, which is around how do you deploy infrastructure? Again, these tools and services tend to do a mix of two things, depending on the tool. One is how do you structure infrastructure code and orchestrate it? Then how do you trigger and manage deployments of your infrastructure to different environments and so on? Again, they're all opinionated on that. I don't feel like as an industry, we have settled on the right way to do it. I think most of the tools tend to work around the limitations of the tools they work with.
Terraform being the 800-pound gorilla in the space that either, quite, probably the majority of users tend to be using, and even those that don't, Terraform tends to influence thinking around these kinds of things. I think that these tools often the way they are right now is working around the limitations of the design decisions made in Terraform and other tools. This is a long meandering answer to your question, but, yes, these tools, they all have their opinions and you do end up having to build your stuff around what their opinions are. I think one of their risks with all of this is that I don't think it's settled.
We don't know which of these tools is going to end up still being around in a few years' time and which approaches are going to win out. I think as a cautionary thing, you need to have a really clear eye on how you're using these tools and being ready to adapt and be ready to move as things change.
**Ken:** Cool. Thanks. That was the first two areas of change. What's the third part of the book?
**Kief:** The third was that deployment. I snuck it in as I was talking around that. There's things like, can people apply concepts of GitOps to infrastructure as code? People talk about infrastructure as data is basically GitOps for infrastructure as code, where you have your infrastructure either within say a Kubernetes cluster or something like that, or a tool similar to that does a control loop. Basically, rather than I'm running a command, Terraform apply, push your changes out to your environment, it's like, well, you put your code somewhere and then something sees how the code has changed, and I'm going to apply that to the environment. Maybe even does a continuous reconciliation on that.
Again, this is one of those areas where there are a lot of different ways to do it and it's not necessarily all that mature, but I think there is this overall thing of, we need to think more about how we deploy infrastructure code, especially if you componentize it. This is more of an emergent thing than a dominant thing in the industry right now, thinking about it much more in a pull way. For application-driven, I talk about application-driven infrastructure, design and deployment. This is where you think about, so what does my application need as an application developer?
How can an application developer specifies the infrastructure I need? Then when the application gets deployed, the right infrastructure is automatically provisioned for the application rather than the old-school way, which is where your infrastructure team builds an environment as a big single thing. There it is. Now application developers can go and figure out how to get their applications running in it. Being much more, I guess, vertical thinking. You could look at it. I think that's one of the big emerging trends.
**Ken:** Something I'm hearing, and please correct me if I'm wrong, because I know at Thoughtworks we've been talking big A agile for literally decades and that sort of thing, is that just in time isn't good enough for this, that they really do have to plan this and think about it. Am I accurate on that? How does that--
**Kief:** Just in time and planning for which?
**Ken:** For infrastructure in general, if you're working on your cat meme app, I can say, here's the user stories that are important, this sprint or whatever, and work on those. I hear you talking about much more deliberate planning with infrastructure as code and thinking about long-term effects and your decisions and that sort of thing. How do you work that into an agile way of working?
**Kief:** I think the key is, again, it's thinking about those applications or your cat meme application or whatever, what does it need? Especially if you're building that in an agile way, in an incremental way, okay, what are the first iterations of that need? I think this is where it really helps when you have a good communication going between, either the same team has got the people building the applications and infrastructure, or if it is separate teams, they're communicating a lot to where it's like, "Okay, the first iteration, maybe we don't need database storage. We're just going to show how it works and what have you."
You don't have to build all the infrastructure upfront that you're going to need at the end, but what's the infrastructure we need right now for the first iteration of the software? Then even where you do start building things like say a database or what have you, maybe you can increase the fidelity as you go. One example I like to use is monitoring systems. You can say, "We're going to deploy and run our own Prometheus clusters, and we're going to have in our elk stack or what have you for log management and all these kinds of groovy things." It's like, "That's a lot of work to build. Maybe the first iteration, we just use what comes out from the cloud provider. We use CloudWatch and things like that. Then iterate over time and build that up."
I think that's part of how you get the agile approach to it. You don't have to think about the full infrastructure and have it all fully designed and built before you can even start, deploying your simple versions of your application, if that makes sense.
**Ken:** Yes. Shifting gears a little bit, I'm going to put you on the spot just a tad. What's next? This is the third edition. What didn't make the third edition? What's in the fourth edition? No, I don't mean to scare you. What have you done for me lately, Kief? No, not that. What are the things that are on the bleeding edge that you didn't want to put in a book yet but that people should be thinking about?
**Kief:** Yes. I actually touched a little bit on it, where I talk about types of infrastructures, code, and so on. Then I think there's some interesting things going on that'll be interesting to see where they end up. It's one of those where it's like in a couple of years' time, you may look back on what I wrote in the book and say, "Well, wow, that didn't hit. That's disappeared." One is, there's infrastructure from code. This is the idea that in your application code, maybe make annotations or references to whatever.
It's like what I was just saying around, okay, this part of the code, I'm going to need a database. You specify there, I need a database. These are the things that I care about from a code point of view. You might say things like, this is the kind of data that I'm going to store. It's personal data or it's transitional data, ephemeral data, what have you. Then when that application is deployed, whatever handles the application deployment pulls the right infrastructure and builds the right infrastructure to meet those needs. There's a couple of things out there. There's, I think, Winglang and Darklang. I know there's others which are playing in this space.
I think that's quite interesting. I'm a little bit skeptical, I guess, of whether that could really define all of the infrastructure and all the aspects of things that you need. To me, I think what's important about it is it's showing how we could empower developers, again, moving away from that developer has to raise a ticket. Can you make me a database? Then several rounds of back and forth where the database doesn't work. It's not doing what I need to do, blah, blah, blah. Just say, how can the developer say what they need and get it?
That's one cool thing. Another is what you might call infrastructure as a model or infrastructure as a graph, let's say, or graph driven infrastructure. System Initiative is one company that's working on this. There's another called Config Hub. There's a few others rattling around out there. These are people who've said, "Hey, maybe code isn't the thing anymore. Maybe there's a lot of limitations and mess that comes from the way we manage codes and worry about the repositories and branches and all that stuff."
If you think about what happens with infrastructure code, when you execute it, the tool builds this model desired state, "this is what the infrastructure should be." Maybe even has a state file where it represents what it thinks the current infrastructure is out there in the cloud, and then does the reconciliation and all of that. These things, what they do is bring that to the center and open it up so that becomes something you can interact with. You can write code, but you're attaching it to things within that.
It's like a graph basically of here's all the infrastructure. Then you can build up, this is what I think the infrastructure should be. You can use code for that, or you can use an interface for that or you can have it dynamically happen in response to events. There's all kinds of possibilities of what you can do when you open it up that way and expose that graph and make that something that you can interact with. I find that pretty exciting. I'm wondering whether the next edition of the book really will be infrastructure as code, or will it be infrastructure automation, [laughs] where code is one of the options, but maybe there's other options which are really gaining ground by that point. We'll see.
**Ken:** Yes. One of the things that you mentioned briefly in the book too was the importance of the concept of day two requirements. What is that?
**Kief:** Yes. That's the idea that I think a lot of times when we think about building infrastructure, including when we think about building it as code, we think about building it. We think about, "Okay, this is the infrastructure I want. Fine." Then it's like, "Well, what do you do next? How do you patch that infrastructure? How do you make fixes to it when you find out something is broken? How do you make improvements to it? How do you expand it when it's like we need to add new things to it?"
I think that's where a lot of the ways that people build infrastructure because of the way the tools are-- the mindset of the tools, I guess, and the way that we're taught when we look at guides and stuff for how to build infrastructure as code, I don't think it really handles that very well. We end up where that becomes really, really hard, and teams spend a lot of their time trying not to break things.
That's where a lot of what I talk about, and some of the things that I mentioned earlier around the componentization, but also things that I've been talking about since the first edition of using pipelines and automated tests for your infrastructure code can really help as we've learned over the past I don't know, 25 years or however long with software, having test-driven development, having continuous integration, continuous delivery for software code makes it easier to make changes. You can be more confident, and you can work faster, and the refactoring tools and those kinds of things have all made it that easier. I don't think we've really brought that into our infrastructure code so much yet.
I think those are really the key things, even though we've been talking about it. Like I said, it was in the first edition of the book, nine years ago now. It's still not really the norm. That has a lot to do with the tooling still doesn't make it easy to do that. I think our habits are still a little bit old school. It's still not necessarily all that different from when we were doing stuff with physical servers in the data center. We're using code for that, but we're doing it in the same way, which is, again, very day zero focus, day one focus rather than day two.
**Ken:** I did wait till we're more than 20 minutes in, at least from a recording time perspective. We'll see what the editors do. I have to ask the question, doesn't AI just make this all magic? Can I just ask my AI overlords for infrastructure?
**Kief:** I think AI can help. I think it has a role as it does with software, can help us to understand. Some of the cool things I've seen done with AI and some that our colleagues are doing, we're like looking at legacy code bases and the AI gives you a way of understanding and comprehending the code of what do I need to change and what needs to be involved in guiding you and it amplifies. I don't see us at the stage where you can just say, "Hey, build me an environment for my application," and it's going to do it necessarily in the way that you would want. Especially then you say, "Okay, now I need a testing environment, a production environment," and they'll all end up messy and different and so on.
I think it's a space to watch. I think one of the things that I've found in using the co-pilot-y type tools is that a lot of them are focused more on software than on infrastructure. I think they're useful, but they don't know infrastructure as well as they know software. I think as well, as I mentioned, we were just talking around the fact that we haven't learned an infrastructure as much around how to do code as well in the same way that we have a software. Again, TDD and testing and all that, the AI tools don't have anything-- They learn based on what's out there, and there's not a lot of great stuff out there, great examples of how to do this really well. I think infrastructure code needs to progress further and faster, and so the AI is going to follow what us humans do.
**Ken:** Yes, I think that's, admittedly was a little bit of a softball, probably a question. We talk about with AI that you have to know what good looks like and what it's trained on, frankly.
**Kief:** We humans don't know what good looks like with infrastructure yet. We're still figuring that out.
**Ken:** Yes, and that's the thing. I've heard from more than one person that, "Oh, it's DevOps. We're just going to have our developers run an AI tool that creates their infrastructure because they don't need to know about that and danger, Will Robinson."
**Kief:** Yes, it's good to be able to know about it. It's what I always say about platforms and layers of abstraction and all that. It can be helpful to not have to think about those details until you do need to think about those details and be able to. If you've had AI build it because you don't understand it and what AI builds is hard to understand as well. Yes, that can be a problem.
**Ken:** When consuming, when reading the book, what kind of book is it? Do I read it cover to cover? Is there a reference chapters? How do people consume the work?
**Kief:** One thing I guess I would say is that it is somewhat high-level in the sense that it focuses on design patterns and practices. It's not specific to particular tools and particular cloud platforms. The examples are pseudocode-level type examples. This isn't like learn how build AWS infrastructure with Terraform from scratch. This is something that you're going to use. Either you've already been working with these kinds of tools and you have an understanding already and you're thinking about, well, how can I organize things a bit better and get further with it or in conjunction with some material that specifically goes into the specifics of cloud platforms and infrastructure tools, whichever tools that you're using.
I think I would skim the full thing, even if you don't go into details and everything, just to know what's in there and then go back and dip into the areas as you need them, I would say. Because it covers design topics in the middle, how to break infrastructure apart. Then when you do that, what are different ways to configure infrastructure? What are different ways to integrate different pieces of infrastructure? The last section is on delivery and that's pipelines and testing and a little bit on ways of organizing teams. I guess it's less that you can leave some chapters till later and more some parts of the chapters might be-- you might just need some part of the chapter.
The one where it talks about, well, our organization is like this. We have a team that is small and does infrastructure and software together and so there are other parts of that chapter, which are then like, what do you do when you have a bigger team and lots more moving parts? Maybe you don't need that part yet, that kind of thing.
**Ken:** Did you notice as you're writing or editing at any point, other key like actionable advice takeaways, was there a theme anywhere? Gosh, it seems like we're, we keep mentioning the importance of X. Does anything like that jump out at you?
**Kief:** Generally I talk about it as applying software engineering practices to infrastructure code. Most of the book, really that's a lot of what it is. When we talk about design, it's like, well, think about principles and practices that we use for designing software, coupling and cohesion, and things like that. Then with delivery, it's things like, again, TDD, continuous integration, pipelines. I think the theme is really just to be aware and think about what we've learned in software engineering and software delivery and how we can apply that to infrastructure code.
**Ken:** Cool. I guess, final thoughts, anything I didn't ask you that I should have, what should our listeners know about key for the book or infrastructure or whatever you want?
**Kief:** I really think the important thing and the important thing with this edition and the important thing as I'm working with clients these days, is really making sure to think about things in the point of view of what is the infrastructure used for starting from there. Thinking about applications and workloads that run on your infrastructure as making sure you have an understanding of that and designing starting from there down. I think that's a difference to the way that a lot of people naturally think and the way that a lot of organizations are designed to where they really put these things into silos. I think let's just have more conversations and more collaboration across the layers of the stack.
**Ken:** Cool. As always, thank you very much for your time. Thanks, everybody, and have a nice day. Bye-bye.
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
## Explore a snapshot of today's technology landscape
[ Read the latest Tech Radar ](https://www.thoughtworks.com/radar)
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