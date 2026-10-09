<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/why-full-stack-testing-matters | Title: Why full-stack testing matters | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Why full-stack testing matters 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons  and Ken Mugrage | Podcast guest  Gayathri Mohan
October 05, 2022 | 31 min 12 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/why-full-stack-testing-matters#Transcript)
Listen on these platforms
## Brief summary
Although many books have been written on software testing over the years, Gayathri Mohan's _Full-Stack Testing_ , released earlier this year with O'Reilly, is unique: by taking a comprehensive look at many different aspects of testing across the development lifecycle, it emphasizes the importance of a truly holistic approach. 
In this episode of the Technology Podcast, Gayathri joins hosts Rebecca Parsons and Ken Mugrage to discuss the book, her experience as a QA and testing's important and changing role in the future of software development.
## Episode transcript
**[music]**
**Rebecca Parsons:** Hello, everyone. Welcome to another edition of the Thoughtworks Technology Podcast. My name is Rebecca Parsons. I'm the Chief Technology Officer for Thoughtworks and one of your recurring co-hosts. I'm joined by my companion co-host, Ken.
**Ken Mugrage:** Hi, my name's Ken Mugrage. I'm a Principal Technologist with Thoughtworks and also one of the regular hosts.
**Rebecca:** Ken and I are joined today by Gayathri, who has recently published the book entitled Full Stack Testing. We are here to talk to her about her journey writing the book. Welcome, Gayathri.
**Gayathri Mohan:** Hello. Thanks, Rebecca, for the introductions. Thank you, Ken. I'm very happy to join you both today on the podcast.
**Rebecca:** Let's start with some of the basics. Writing a book is an awful lot of work. What prompted you to actually write it in the first place?
**Gayathri:** Yes, definitely, Rebecca. It's just a behemoth of tasks to be done. Particularly, I think my experience working with multiple clients and the discoveries that we have been doing with our clients made me realize that there's a lot of scope in this field to actually be written as a book. For example, I've seen clients where there has been no culture of testing at all or there has been just a silo testing team, who just went about executing some hundreds of test cases just during the release.
Some clients had production defects and they had to pay penalties for their production defects, which would've been caught during a proper testing phase. Such kind of engagements and when we go there and we had to do enablement and also set up the testing team from the beginning rounds up, there's a lot of content that I could see that could be actually captured as a book. There was the right set of audience for it as well. I just thought maybe it'll be useful to give it a go.
**Rebecca:** One of the things I find so differentiating about this book is its breadth. We see books on performance testing or we see books on accessibility or things of that nature. You really have run the gamut of so many different aspects of testing. What was the genesis of that idea?
**Gayathri:** I felt like the testing discipline itself was just consolidated into manual and just automation testing. Especially when we talk about manual and automation testing, it's just about functional requirements as well. There was very little focus on the non-functional or cross-functional requirements testing. The terms, just manual and automation testing encompasses everything into it. The focus on those particular cross-functional requirements and non-functional requirements get lost into it.
That's one of the primary ideas of actually creating the book with a focus on the breadth of testing. To show that testing is, though, you can consolidate it into manual and automation testing, it's just not about functional requirements, but there is a huge list of cross-functional requirements that needs to be tested and to be accounted for in the testing strategy. That's the motivation to cover the breadth of tools, techniques around all these areas.
**Rebecca:** You commented frequently in the book about being —I think you called it the champion for testing or the advocate for testing. How would you characterize the role of a quality analyst and the responsibilities that everybody has to think about quality and testing?
**Gayathri:** I think every role has something to contribute to the team. A QA's role, I think, primarily owns a large part of testing, but not definitely the only role that contributes to testing. I see the QA role being the champion of testing on the team to take ownership of empowering the team to do the right kind of testing, the right stages of the delivery cycle. For example, starting from the BAs for testing for accessibility, it needs to start from the product design stage itself. The BAs and the UX folks have to start thinking about product design testing, making sure that the accessibility features are included in them.
Also, during the development stage, the accessibility features have to be tested for and included as part of the development itself, and then comes the manual testing phase where the QAs pitch in and also do write some functional automation tests, and also actually care for accessibility-related features like screen readers and everything. Owning this feature and empowering the team to do the right kind of testing at every single stage is very crucial for the team to successfully deliver a quality product. That's how I see the QA's role. Mainly being the champion for testing and also contributing towards the knowledge regarding testing in each of these phases.
**Ken:** It's somewhat related. In the last little bit over a decade, we've seen the movement to DevOps and continuous delivery and all that. You just covered a little bit, but how has the role of QA evolved over just the last few years to deal with those kinds of silos and so forth?
**Gayathri:** I think if we have to go back a little and look at the QA's role, we had some siloed QA teams. The development will happen and then a code will be passed onto the testing team, and then they'll do the testing at the end just before the release and find out a lot of issues and then push it back. It was also coming out as testing-as-a-service in the last few years. Some companies still do that.
We had agile testing coming into picture, where we said we need to have cross-functional teams and integrating testing as part of — the delivery cycle is going to be key for quality. There were a lot of focus during that period. Once again, I feel like today we have a startup culture where testing is taking the backseat and the time to market is taking priority. I see the role of a QA as a very fluid role.
Even today, I think certain teams place a lot of emphasis on testing like I said in the previous conversation about how some teams didn't have a testing culture at all. Some teams had a lot of emphasis on functional automation. Similar to that, I still see the role has been considered a very fluid role. The QAs sometimes go and pair heavily with the BAs to knock down the requirements, and sometimes they're still kept as a siloed team.
Sometimes the cross-functional requirements are outsourced. It's not even considered part of the delivery team. It's outsourced for another team to do — For example, an external performance testing vendor is involved or a pen testing team is involved for testing. It becomes a very fluid discipline and something that is sometimes kept aside and not taken care of enough.
This time, I feel like the QA has given their skill sets for them to take over the testing territory and drive some of these outcomes that we spoke about earlier as part of a CI/CD, adding tests in the right layers and focusing on cross-functional requirements, automation, starting testing right from the software requirements stage, working with the BAs, UX till through the delivery stage.
**Ken:** That's really interesting about QA being part of the role in breaking down those silos. One of the things you talk about a lot in the book is not just the quality of the software from the bug perspective, but also how effective is it? What is a QA's role in building the right thing, the effective software versus just build it right?
**Gayathri:** Oh, that's an excellent question, Ken. Very interesting question as well. I think the QAs on the team literally are the end-user representatives. I think when we have to QA a particular piece of code, I think we are empathizing with the end users and making sure that we bring out their point of view. Whatever doesn't make sense for the end user is actually something that the QAs bring out abruptly.
This one was a good story that I remembered. In Thoughtworks University, when I joined as a grad, we used to have a lot of fun ways to learn about QA'ing. One of the games that we played was building a software, building a product with the Legos, and making sure that the BAs come up with the right requirements and the developers build the right thing with the Legos and then ask QAs going and testing the Lego product to make sure that it meets the end user's needs.
I remember very vividly that the BA wrote, "Build an airplane and it should be able to fly." The developers actually built a toy Lego airplane and passed it on to testing. As QAs, the first thing that we did was just flew the plane and it crashed. [chuckles] It was a fun way to teach us that what is necessary for the end user is what the QA role is about. Anything that doesn't fit into the end user's use case, it just doesn't fit into the product.
The same thing have applied into day-to-day software delivery as well. I've seen, for example, when we go into mobile, for example, you take the product, the QAs go and test it, and they come up with questions like, "Okay, I'm a left-hand user, and what about the right-hand users? Can the button be in some other place? I'm driving the car. Now, I want the voice-enable feature to use the product, so how about that?"
Several of these questions do come up from the QAs, which I've seen make the product to be built in the right way rather than just making sure that whatever the requirements are passed and it is working just up to the requirements. I think I answered the questions about build the right thing versus build it right from a QA point of view.
**Rebecca:** One of the things that has been a particular issue for me and some of the client work that I've done in the past is the problem of test data generation and getting the right test data in place to be able to properly test the application. Obviously, as we get more and more data-intensive applications, this whole idea of how do we properly test is becoming more important. How do you see that problem evolving?
**Gayathri:** Very valid observation, Rebecca. I agree with you. Test data creation is one of the areas where I still see a lot of innovation can happen. Test data is going to be the primary factor for producing the right test results. If your test data is wrong, then the test results are going to be wrong as well and there's no point in testing it. Especially when it comes to scale, test data creation actually has been really problematic, especially in terms of multiple vendor data formats. There's graph-like connected tables, which takes a lot of input that needs to happen.
Different forms of input data like files and various other formats of input data. Scale has made it even worse definitely. One of the options that we usually tend to suggest is to use the production data as test data to actually be able to produce test results that are close enough to what is actually going to happen in production. Once again, I think that is an area where we have to tackle all the security-related issues. We need to take care of BA information. There are some obfuscation tools. There are some techniques like scrambling and automatization and all of that, but still, an area where some innovation can definitely happen to alleviate some of these problems.
**Ken:** One of the terms you use in the book and others use as well is the term "continuous testing." How does that play alongside or what's the difference between continuous integration and continuous delivery?
**Gayathri:** I think you would've definitely heard about this, Ken, and you're a master of the subject. I came across this term, "continuous testing," via one of Jez Humble's book. I think the book Accelerate talks about it. The concept has introduced something like continuous testing is one of the capabilities for performing continuous delivery. Alongside continuous integration, I think continuous testing is another capability that we need to do continuous delivery.
The differentiation primarily is, I think, when we're talking about continuous integration, we're talking about having short-lived code branches, being able to integrate the code in frequent intervals, small changes, incremental changes, and all of those stuff. Continuous testing is a capability where we have automated tests as part of the CI pipelines, both for functional and cross-functional requirements, and the capability to run them in the development environment.
Not only that, but we are also including a stage where there is mandatory manual exploratory testing after the code is deployed. The manual exploratory testing is an important phase of continuous testing, where there are new scenarios that are being discovered during that stage. All the scenarios that have to be automated then gets automated so that the continuous testing process happens. By way, we are able to do continuous delivery, all in the process of being able to keep the code production ready at any point in time.
**Ken:** There was a quote I took out of the book that said, "A wise way to balance the testing capacity in a project is to perform manual exploratory testing to find new test cases and automate them to aid in regression testing." Instead of TDD, should all your tests be coming from this manual testing, or is this in addition to TDD? How does that fit?
**Gayathri:** Definitely not. I think TDD is a very important way to achieve automation. I think the context of the particular statement that you're quoting is-- so I've seen teams where I've--- I've told you that there are some silo testing teams and there are 400 test cases, which is manually executed every time. A release has to happen. When more features get added, there are more test cases. The only solution the business could think of is, "Okay, let's add more people to the testing team, and now let them start testing."
That's an absurd way to manage the testing capacity itself, not really utilizing the testing team's full power. That's what I was addressing when I was saying that when you are using the testing capacity, use it to perform manual exploratory testing. That way, you could actually gain some value out of the people that you hired. You could actually find new test cases, find some new places that your developers and your BAs haven't thought about. Once again, automate that. That way, you'll be able to attain the right balance between just hiring more people and also getting the right value out of them.
**Rebecca:** Yes, and I want to follow up on that because I believe that exploratory testing doesn't have the level of prominence that it should. I think that's effectively what you said. Very often, people are just focusing on, "Okay, I'm going to automate what's here." To me, the real value of a QA is, "Okay. Now, let's look at this in different ways." One of the things I often say is a development team is a finely-honed machine to get requirements out the door.
They're working from a known context. Part of the value of the QA is to explore around the edges of that context. How do you learn to do that? What is the process that you went through in making the switch from, "I'm just going to think about automating these things," to "Now, I'm going to go push the boundaries"? What does it take to do that well?
**Gayathri:** That's a fantastic question, Rebecca. Definitely, as you said, manual exploratory testing is one of the key areas that the QAs can contribute to. When it is actually skipped, then there's a lot of edges that is missed and just the requirements that is actually thought about is only focused upon. The experience that I went through in gaining that skill particularly, I can talk about that.
There are some techniques definitely that are prescribed in the industry. There's some help there like boundary-value analysis. There are some all-pair testing. All of those techniques are still available. What is important in manual exploratory testing for me is to have that mindset of curiosity and also the tendency to challenge. Basically, you go ahead and challenge what is already known.
The mentality of just putting yourself in the end user's place and also figuring out what has been missed, how can I break it, or that's kind of challenging mentality along with the curiosity to know how exactly your application is behaving in certain situation creates that or even amplifies that skill. That's how I went about-- I would say one can actually trigger that skill set learning.
**Rebecca:** It sounds like it's probably the really fun part of being a tester. [laughs]
**Gayathri:** Absolutely. [laughs] It's almost a crown when you actually discover something that's totally outside the boundaries.
**Rebecca:** We touched on data a little bit, but I want to go back to it because, obviously, data quality is such an issue. When we're looking at things like machine-learning models that are built off of data, obviously, the data is what determines the model. What kinds of things are we learning as an industry about data cleansing and data quality and how do you see the role of QA in the broader questions of data governance?
**Gayathri:** Data quality is definitely one of those evolving areas. Data has become the primary asset for any company these days. The scale at which the data has been presented for testing is also one of the key areas that a lot of learning has to happen yet. Having said that, I think there are a lot of tools already in place for testing the data quality itself. We have automation tools that can actually check for certain types of data like the data tapes.
We can actually have some contracts in place for ensuring the data comes in certain way. There are some approaches already in place. The one way I tend to look at the data testing itself is basically to understand, what are the data systems that we are dealing with? Is it database or is it event-driven systems? Is it a bad job? Putting together some test harness specific to that particular data system is a way that I've approached this kind of data testing.
When we are dealing with database, there could be some concurrency-related test cases. There could be some data type-related test cases. When it comes to bad jobs, there could be data skew-related test cases. Understanding what is the kind of data system that we are dealing with and putting a test harness around it has been one of the ways that has worked for me so far.
**Ken:** Switching gears just a little bit. We talked about the breadth of the book. You have a chapter on mobile testing. There was another quote there that I stuck in my head. It was that the shape of the testing pyramid, if you will, from mobile is often inverted, depending on the characteristics and features of the app. A lot of our clients, they have applications that are web and mobile, so how do we balance this when the total solution isn't one or the other?
**Gayathri:** I think it totally depends upon the type of the application that we are dealing with. For example, if the application is going to be logic-heavy like a banking system and then we're just having a banking mobile site, mobile app, and also a web application, then all of the logic is going to be abstracted for us into the services layer. There's going to be a very thin presence on the mobile UA layer.
Whereas on the other hand, if we are looking at some sort of gaming or site mobile apps, then there are a lot of native interactions that need to happen on the mobile application. That's where, I think, the mobile pyramid gets inverted. Then there are a lot of native elements that need to access hardware and all of those or specific stuff. Then the mobile testing pyramid naturally gets inverted because there are very little that we can do to create automation tests. We have to rely on a lot of manual testing and also end-to-end test scenario.
Whereas on an application, which has a lot of logic like a banking site, there's a lot of logic and there is abstraction in different layers. We could definitely adopt the testing pyramid. It totally depends upon what are the kind of features that we are dealing with. The only thing that we can do is understand the nature of the application and probably plan for testing capacity accordingly. If it's going to end up in an inverted testing pyramid, then plan for additional capacity around manual testing it and also putting together a thin end-to-end testing automation in place.
**Rebecca:** Let's turn our attention now to some of the more flashy things. What's the role of AI these days in supporting testing and a QA?
**Gayathri:** Yes, AI has definitely started to penetrate into the testing space, especially in test automation space. There are several features that they tend to offer. One that actually caught my eyes, which was something that I was longing for for a very long time, was the cell-feeling capability. The AI could actually figure out why the test is failing and actually prompt us with what changes can it make to the test so that it'll pass.
That has been something that I've been wanting for a very long time mainly because sometimes it'll just be the ID change. There'll be tens of tests that are failing, but the functionality and the feature, the look and feel everything will be the same. This kind of cell-feeling capability where it identifies that the element hasn't actually really changed, but only the ID has changed. Prompting for just a click on the button and it goes and changes all the ID naturally is a great benefit.
Some of these kind of features are coming up and it is starting to come up into the testing space. Although most of the tools are still in the beta stages, I see that there's a lot of potential that the AI can take up in the test automation space. They're even saying that it could author test if we just have to go on the screen manually and show what the test cases have to be. That is still yet to prove itself, but some of the fancy features are coming into play.
**Rebecca:** What does the future hold, do you think? Where do you see things moving overall in thinking about testing?
**Gayathri:** I feel like testing is a space where a lot of research and innovation can happen. I feel like there are a lot of tools that are also coming up day by day. We have to see, there are so many tools in the same space itself for testing certain things. Still, there are a lot of challenges that are pending to be solved in the testing space. For example, there are legacy enterprise systems that deal with mainframe systems. We have to move them.
What about testing the mainframe systems and then move to a new estate? What is the solution there? There are also problem statements. Now, we have a huge tech estate and there are lacks of tests that are there. Now, how do we handle that many tests and that many failures? What about the infrastructure there? There are also emerging technologies that are coming up like the AI and XOR space. What about testing and automation there? I'm really looking forward to seeing how some of these problem statements are being solved and I'm going to have a chance in solving some of them as well.
**Rebecca:** Excellent. Well, thank you so much, Gayathri, for joining us. It's been a fascinating exploration of all things testing. Thank you, Ken, for joining us as well.
**Gayathri:** Thank you. Thanks a lot for having me, Rebecca and Ken.
**Ken:** Thank you.
**[music]**
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
## Find out what's happening at the frontiers of tech
[ Explore Technology Radar ](https://www.thoughtworks.com/en-th/radar)
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
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://www.thoughtworks.com/en-th/about-us/privacy-policy)
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