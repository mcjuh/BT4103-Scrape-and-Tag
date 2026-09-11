<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/monoglot-monopoly | Title: Unravelling the monoglot monopoly | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Unravelling the monoglot monopoly 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Mike Mason | Podcast guest  Rebecca Parsons and Evan Bottcher
June 27, 2019 | 16 min 11 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/monoglot-monopoly#transcript)
Listen on these platforms
## Brief summary
Most organizations today face tension over how many programming languages they should support. But standardizing on just one is likely to be limiting — particularly when many enterprises favor giving dev teams a degree of autonomy. So if one is too few, how many is too many? In this episode, our co-hosts explore how enterprises can make practical decisions about language choices, so that their developers have the right tools for the right jobs.
**Podcast Transcript**
Mike Mason:
Hello and welcome to the Thoughtworks podcast. My name is Mike Mason and I am one of the hosts of the podcast and I'm here today with Rebecca Parsons, who's the CTO of Thoughtworks. Hello Rebecca.
Rebecca Parsons:
Hello Mike.
Mike Mason:
And I'm also here with Evan Boucher, one of our technical principles from Australia. Although I mean we changed job titles all the time. And you still technical principal or is it some other?
Evan Bottcher:
No, that'll do. I take care of engineering across Australia at the moment.
Mike Mason:
Excellent. So we're here in Shenzhen, China. We've been locked in a room together. We're part of the Doppler group that creates the Thoughtworks technology radar. When we do the radar, people suggest technologies that are moving and interesting now, or they suggest techniques, things in a positive light or possibly in a negative light. And one of the things that was put up this week, started off as node for all the things, which was, I guess you could call it a technique or a set of architectural decisions where organizations are choosing to use a node and JavaScript throughout their technology stack because they feel that coalescing on that one specifically, the language choice around JavaScript will provide them with a productivity benefit. And I think we talked about that whole node for all the things for a little while and ended up with a different name or monoglot monopoly, which I believe came from Johnny LeRoy because he's our department of naming department. And so we talked about monoglot monopoly.
Rebecca Parsons:
And unfortunately while that's awesome alliteration it's actually a very bad name because it's repetitive. Monoglot means there's only one and monopoly means there's only one. But the point is, what we were trying to say is regardless of what the language is saying, you're going to use only one language, exactly one language, is an anti-pattern. You don't get the level of efficiency that you're looking for. Even though it's a popular notion in many of the enterprises that we work with.
Evan Bottcher:
So in a past issue of the radar we, we blipped an item called polyglot programming. It's kind of hard for me to say today and polyglot programming is the idea of making a selection or making a choice of language and even the technology around that language that fits the problem in a really good sense in a particular context. So rather than forcing down a single path, then you'll actually use the right tool for the job and see a wider degree of languages and technologies in use.
Rebecca Parsons:
The problem with that is developers always love to try new things and as we've seen in microservices where you have dedicated long running teams creating their own microservices in the desire to give teams autonomy, which we're big fans of pushing decisions as close to the people that those decisions impact as possible. Many organizations have found that they get an excessive proliferation of technologies and while we clearly think one is bad, 45 is probably not a good number either. And so we want to try to explore the idea of how does an enterprise start to think about what's the right number? How would we get there?
Mike Mason:
I mean there's examples of this in the past I guess with for example, I know at Google their internal choices, they had maybe two or three language choices. Actually, I'm not sure what the number was, but there was certainly kind of probably C++ and Python and maybe something else. And if you chose one of those languages, I think you actually had to choose one of those languages, that the trade off was because it was an official Google language. You got support across the Google platform for it. So if you built something in that language choice, you got scalability and reliability and all the other nice ilities that the Google platform itself was providing for you.
Evan Bottcher:
And so this is a recurring theme and it is very relevant. Like Rebecca said, we're seeing this out of this rise of organizational structures that are pushing more autonomy out to teams and we are having to answer essentially what's the modern version of governance, the right type of lightweight governance to allow people to make sensible choices and choose things that are going to be highly productive. The negative side of working in a place that's got too much technology sprawl is that you really can't be really good at a wide number of things and it stops your flexibility of people moving between projects and platforms and causes a lot of pain.
Mike Mason:
I mean, on that topic of moving people between projects and platforms. I guess I'm curious, I mean, it makes sense that somebody would know a particular set of languages and tooling and if you move them out of their sweet spot, they wouldn't be as effective. But surely they would be able to come up to speed in that different piece of the organization using a different technology stack. So is that just a red herring, that argument that someone would be more efficient or everybody's got a little cog in the machine and we can move them around more easily if everybody needs to know the same stuff?
Rebecca Parsons:
Well I think it's a matter of degree. If you're skilled in an object oriented language and you understand the object oriented paradigm moving from a one OO language to another is relatively simple and yes, you need to learn the framework and the idioms that are more common in that language ecosystem. And it really has become language ecosystems now as opposed to just a programming language. But if you start to say, well, we're going to have a combination of a dynamic on typed language and an object oriented language and a lazy functional language and let's tack several different language families, I don't want to use paradigms. There's another podcast in the series that talks about exactly that. But the more you get that intellectual sprawl, the harder it becomes for any individual to develop any reasonable amount of skill. And one of the scariest programs I ever looked at was an individual I worked with who was incredibly skilled in Fortran.
Rebecca Parsons:
He was an electrical engineer, was working in device simulation. Fortran at that time was absolutely appropriate language choice. He moved to another organization that only wrote in Lisp and this gentleman wrote Fortran code in Lisp syntax because he just didn't quite get it. And so that's really the problem that you run into. Good developers do have the ability to move from language to language, but there is a limit and I think that's what we're really talking about on the other end. One is not the right number but neither is 45 and how do we go about governing that? One of the things that we've seen work in that governance question, we have this notion of our own Technology Radar, but we encourage organizations to build their own radar, to get the decision makers and the users in their technology organization together and talk about what should we be using? What should we be starting to phase out? And part of that governance mechanism can in fact be, we're going to impose the moral equivalent of WIP limits in each one of those spots to say, okay, well maybe it's not one, but please pick three or five depending on what the application is, how large the organization is. And so there are techniques that can allow you to balance that proliferation while still allowing teams to make their own decisions and give them some level of autonomy.
Mike Mason:
And I know Evan, you worked for an Australian client who I keep trotting out as an example for how to do things well and you know, they had elements of why we call the Spotify model working for them with lots of stuff going on and maybe more encouragement of collaboration and sort of spreading best practice rather than decision making by diktat. What was the situation there around technology choices?
Evan Bottcher:
Well there was a high degree of autonomy and there was a lot of choices. It's been a while since I've spent a large amount of time there. But I tell the story quite a bit of some of the decisions we made around technologies, and this isn't just language, this is any layer of the stack where I've always sort of said there's really three main slots if you like, for a technology choice. There's our default, our good default, we know how to do and you would pick it for every new thing that you're going to do by default. There's the one that we're getting rid of because it's no longer very good and it's been supplanted by the default and there's the one we're doing an experiment on and generally not much more than that.
Evan Bottcher:
That was a reasonable way of managing that work in progress limit. And that if you're saying that we've got a new default, then you're actually committing as a team to replacing over time the parts of the deprecated, the technology choices that are no longer the right thing. I think this is a good guiding, having a visible metaphor like the Radar. Other places I've seen technology playbooks like that have pretty much put in place the agreement on what these things are is great because we can share that and then you can say, okay, maybe there's a need to invest some engineering effort in making those things highly productive. Like make sure there's good tools and good deployment technology and good observability and good run time controls for this more limited set of technologies but not necessarily limiting that to just a single technology like we might've done in the early 2000s.
Rebecca Parsons:
Well, and the thing I like about that model is it does recognize that there may be aspects of a system, maybe it's because of deadline pressure, maybe it's because of the nature of the problem that there is in fact a different stack, a different language environment that might be more appropriate. And when I've heard you talk about that particular client before, the emphasis is on making it easy to do things the way everybody else does. If you do choose to go a different path, you have to make sure you reflect the observability and the monitoring standards. And you're probably going to have to implement those all yourself because it's not part of the standard. So it's okay, but it's okay within a context because we're not going to say, yes you can just throw some random new language into the mix. We want you to instead say you can use a new language if you really think this is the right thing to do, but to operate in our ecosystem you have to adhere to our language or our adhere to our logging standards, have the right kind of monitoring available and probably you have to be able to explain why this is the right choice for the organization rather than just participating in resume driven development, which unfortunately we also see a fair amount of.
Mike Mason:
And I think from my perspective, that's often a difficult thing for an organization to kind of self assess. Where are we at? And I mean Marlin Fowler talks about you must be this tall to ride in term for microservices. You need to have great dev ops culture in place in order for microservices to work for you on a bunch of other things. It sounds like in this case as well, a team needs to be pretty competent in order to make an active decision to move away from whatever the defaults are and onto something else. But the problem is that we all think we're above average drivers and it's actually quite difficult to self assess where are you really at? One of the other aspects that we talked about was kind of the competition for talent out there in the world right now and appearing to be on the leading edge of technology choices maybe can attract people to the organization. Like does that have an impact here?
Evan Bottcher:
By my observation, I think that sometimes the choice of more language choices and technology choices and increased autonomy is a very attractive thing for engineers to come into an organization. I do think there's a bit of a curve in place where sometimes in order to bring an influx of new talent and strong engineers, you do need to essentially allow for a wider degree of technology choices and it seems like there's a bit of a path that organizations go through and then rationalize and actually start to focus that energy more towards solving real business problems and functional problems by making a few set of technology choices much more productive.
Mike Mason:
So around the topic. What's the advice that we would ask listeners to take away with them?
Rebecca Parsons:
Well, I would say again to restate what kind of feels obvious, there's a whole lot of numbers between one and 45 and while we agree that 45 or 57 or any large number is too big, one is too small. And we need to enable organizations to figure out for themselves at this particular point time with the particular people that I have with my aspirations for growth, what that right number is, and then put in place the techniques and the guard rails to manage to that number to maximize the autonomous decision making while minimizing the drag that can result from too much variety.
Mike Mason:
Well Rebecca, Evan, thank you very much for joining me. This has been the Thoughtworks podcast. Please do leave us a star rating or a comment on whichever podcast platform you're listening to this on because that really does help people find the podcast and tune in next time for more info from Thoughtworks.
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