<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-green-cloud | Title: How green is your cloud? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  How green is your cloud? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons and Alexey Boas | Podcast guest  Danielle Erickson and Dan Lewis-Toakley
May 07, 2021 | 29 min 34 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-green-cloud#transcript)
Listen on these platforms
## Brief summary
Following on from our Earth Day episode on green software engineering, we turn to the concept of Green Cloud. Reducing your IT operations’ carbon footprint is more complex than simply moving to the cloud. We explore how developers can gain insights into the energy usage of their cloud operations and the tools and techniques they can deploy to minimize their cloud-related emissions.
**Rebecca Parsons:**
Hello everyone. My name is Rebecca Parsons and I am one of your recurring hosts on the ThoughtWorks technology podcast. I'm joined by my cohost Alexey.
**Alexey Boas:**
Hello everyone, I'm Alexey Villas Boas, one of the regular co-hosts speaking from San Paulo. Great to be here with you all.
**Rebecca:**
And today we are talking with two of our colleagues who have just open-sourced a tool to help people understand the carbon footprint of their cloud. So I would like to welcome Dan Lewis-Toakley and Danielle Erickson to our podcast. Welcome Dan.
**Dan Lewis-Toakley:**
Thanks Rebecca, it's great to be here.
**Rebecca** :
And welcome Danielle.
**Danielle Erikson:**
Thanks Rebecca, happy to be here.
**Rebecca** :
Let's get started. Internally and externally, people are talking about green cloud. Well, what does that really mean? Is it just as simple as saying, "I don't have to worry about it I will let my cloud provider do it"? Can you help us understand this concept a little bit?
**Dan:**
Yeah, so we often hear from people that we're 100% on Google cloud or Microsoft Azure, and they offset 100% of the energy power in their data centers so I'm already green, right? What do I have to do? Well, that's not quite the full story. So the energy that powers hyperscale data centers, like the major public cloud providers, is in no case 100% renewable. And in many cases, a very small amount or no amount of renewable energy power in those data centers. And so carbon emissions are still created in the first place when you are utilizing their various services.
**Dan:**
Now those two cloud providers I mentioned do purchase energy attributes to match that non-renewable energy in their data centers, but it doesn't remove carbon from the atmosphere, it's already created in the first place. It's just a market based solution. And so as technologists and IT organizations, we have an opportunity or maybe a responsibility to understand the carbon emissions that are created when we use all the various services from cloud providers to not only understand and start to measure, but to optimize our usage. So you can reduce the amount of energy and reduce the amount of carbon emissions associated with your usage.
**Dan:**
Some examples of that could be as simple as maybe moving a compute workload from a dirtier region to a more renewable region. Another example could be maybe you have a large amount of storage in an Amazon S3 bucket that's readily available, but you haven't used it for years and you don't have plans to utilize that data. So you might as well move it to Amazon Glacier, which it might take half an hour for you to access that data, but it's far more energy efficient and less carbon emissions associated with it.
**Dan:**
Another common example is you might have a large number of virtual CPU's deployed in a cloud provider but with very low utilization rate, maybe 10, 15%. If you can reduce the amount of virtual CPU's but increase the utilization rate, that will lead to far less energy produced and emissions created in the first place. So there are many opportunities for developers and engineers to find ways to quantify and then reduce carbon emissions.
**Danielle:**
Yeah, I guess I would say another piece of what we talk about green cloud is trying to not only think about your cloud in terms of cost and what's actually running, but monitoring it ongoing for these improvements for carbon emissions. A lot of people do look at optimizing for cost as an ongoing thing and monitoring for that, but we also want to do that for your emissions as well. So looking over time to see if there's spikes or see if things are going down and you have actually made improvements. So that's one big piece of green cloud.
**Dan:**
There's an interesting relationship between cost and carbon emissions. And it's often a good proxy if you reduce your costs, you can also reduce emissions, but it's not always the case. One example I like to share is that let's say you have terabytes of data stored in a region in Australia where I'm from, which is not the most renewable region for cloud providers, and you want to move that to maybe let's say Belgium, a region in Belgium that is far more renewable.
**Dan:**
From an environmental sustainability perspective, that's a win. It's a really good win. However, most public cloud providers have significant egress costs of moving data from one location to another. And so while it might make sense from a green cloud perspective, it might not make sense when it comes to cost. So it's all about thinking about these trade offs and factoring in carbon emissions or sustainability metrics alongside other cross functional requirements like cost or performance or security, because it's not always true. Our goal is to try and find the sweet spot where we can reduce costs and reduce emissions.
**Rebecca:**
Well, and that I think brings us nicely to the next thing I really wanted to talk about is this open source tool that your group has created to really help people understand the carbon footprint. And if we can't just use cost as a simple proxy, we need to understand that footprint in a very different level. So can you tell me a little bit about this tool and why it was developed in the first place?
**Danielle:**
Yeah, so we kind of realized that there was this bit of a gap in the understanding of our technology and specifically the cloud and our carbon emissions, our carbon impact. So we wanted to see what was possible. We did a little bit of research and there's a few things out there. One thing in particular is these Cloud Jewels, it's a methodology that allows you to, what they did is they calculated their energy usage for GCP, Google cloud.
**Danielle:**
But we wanted to see if we could actually take this and build something that developers could use in practice. So we did a little bit of a proof of concept to see what was possible, especially to get a picture of emissions for organizations that are multi-cloud users. So you can really see what's happening across the board. And that way developers in their day to day, we wanted to create a tool that would allow developers and technologists in their day to day to see the impact their choices are making. We wanted to allow developers and technologists to get a full picture of their cloud carbon emissions, especially if they're using multiple clouds and also to be able to see that over time and monitor it with the changes they're making as they go throughout their day to day.
**Danielle:**
So we heard that this is something that not only is important as we all know for climate change, but it's something that does motivate people. Developers are more motivated to work on sustainability related improvements as opposed to cost related improvements. So building a tool that would help them do that is something we wanted to try to do. And then on top of that, we really wanted to build something open source so that it can be customizable and extensible for a variety of different organizations of different sizes, of different cloud providers. And just being able to cater that to your specific needs. So that's the inspiration of the tool and the story of how we got to the specific solution we came to.
**Alexey:**
Well that's amazing, it really helps developers shift their mindset and look at carbon emissions and energy efficiency as a separate across functional requirement and then bring that into the day-to-day of development monitoring, just the way we do with several other things at the end of the day. I'm really curious to delve a bit deeper into the details of how the tool works and then what's the methodology and the estimation. So Dan you did mention that cost is a good proxy for energy efficiency, but not exactly that. And Danielle, you did talk about that Etsy Cloud Jewels. Can you explain a little bit about the methodology, how we look at that and how is it different from just performance in a more abstract way?
**Danielle:**
Yeah so as an overview, the tool works on a pretty simple calculation to estimate your emissions. So first we take usage data from the different public cloud providers. Then we'll classify it into different types, so compute, storage, networking. And then we do have a section where it's a bit unknown. Some of the usage types are less easy to identify at this point. So once we have that compute, storage and networking classification, we can then convert it to energy. And then from energy, using public grid factors, we convert it to emissions. So that's how we get the number of carbon emissions for your cloud use at a high level.
**Dan:**
Just to do a bit of a double click into it, the tool currently supports Microsoft Azure, Amazon Web Services and Google Cloud, and the data source is the cost and usage or billing data around those cloud providers. So for AWS, we use Amazon Athena to query the cost of usage reports to get all those types of usage rows that Danielle has broken down. With Google cloud we use Big Query to create the billing export table. And then with Microsoft Azure, they have an API called the consumption management API that we pulled. And the data types and the values and the units are different across all of them, but we get, with a bit of data transformation and understanding those data sources, we can get them in a format that allows us to classify them as Danielle said, as compute, storage or networking.
**Dan:**
We haven't added memory yet to the estimation, we're researching and trying to find a way to quantify memory in terms of energy, that's on the short term roadmap. And then there's also some usage rows that are either unknown or unsupported. For example, a license fee, unlikely to have any actual energy usage associated with a fee. We would say that is unsupported. As Danielle said earlier, we leverage Etsy's Cloud Jewels methodology that they published last year, but we've updated and improved coefficients based on additional research. And we also applied that to Amazon Web Services and Microsoft Azure as well. So it's not just Google Cloud.
**Dan:**
For compute, one way that we've improved the coefficients is that the min and max watts that are produced at either zero or 100% CPU utilization, we're dynamically determining what those coefficients are based on the underlying micro architecture for the instance type that you have selected. So what that means is that all three of the public cloud providers publish a list of all the instances that you can select. And alongside that, they publish the micro architectures that are used. In some cases, it's a single micro architecture, such as Intel Haswell. Other times it's a group of micro architectures. And so when it's a group, when we don't quite know exactly what it is, we take the average and apply that as the coefficients.
**Dan:**
So that's a little bit more details on how we determine energy estimations per compute. And then for storage, it's very similar to Etsy's Cloud Jewels, but we've just updated it to be 2020 and 2021 relevant coefficients. Basically, given an amount of terabytes of storage provision, we can estimate that it's X amount of energy associated with it. One interesting thing with storage is that we look at the storage amount provisioned, not the storage amount utilized. So you might have let's say an EBS volume with AWS that has 20 gigabytes of storage provision, but you're only using two gigabytes. We look at the 20 view, because that's what we expect the energy is being utilized to power that storage device. So something to think about.
**Dan:**
The one additional interesting thing about storage is that oftentimes in some cloud providers, if you deploy provisions from storage, it automatically by default also provisions at multiple different availability zones, and so we're looking into what that can mean in terms of energy associated with it. And you might've only provisioned 10 gigabytes, but there might actually be energy associated with 30 gigabytes if it's available across multiple availability zones. So that's something that we're also looking into.
**Dan:**
When it comes to networking, over the years, there's been many studies and academic papers that try to determine a coefficient for a given amount of data transfer and what that means in terms of energy. There's been a high variance in those coefficients with some articles saying it's quite high, some quite low, but overall the trend has been steadily downwards over the last decade or so. And so we've made some assumptions about hyperscale data centers in that because of the way they've architectured their networks, they likely have the most energy efficient transfer between data centers at the highest speed rate possible.
**Dan:**
And so we looked at all of those studies and decided to use the lowest coefficient available under that assumption. And with all of this methodology, we very much so welcomed feedback and contributions because there are a number of assumptions that we make going into it. So once we have energy, then we take into account the power usage effectiveness of the cloud providers. So power usage effectiveness is basically figured that is how efficient is that data center. And it's the ratio of the total energy required to power the entire data center over the energy required to provide the services. So for example, lighting lights in a database provided services to the customers.
**Alexey:**
Yeah so intuitively, it's trying to capture the building, the energy necessary for the building. So lights, fans, ventilation systems, all those kinds of things that go beyond the computer itself, right? Is that intuitively what the effectiveness is trying to capture?
**Dan:**
Yeah, that's a good summary Alexey, and we use publicly available information. Google Cloud actually published their trailing 12 month PUE values from 12 months ago. And they do that every quarter, which is great. And we haven't got a statement from the Microsoft Azure team as to their PUE, and with Amazon Web Services we use reasonable default based on public articles that they've published in the past. So yeah, it's definitely what you say Alexey, it takes into account all of the energy required for the data center.
**Dan:**
Then finally we use publicly available emissions factors, as Danielle said, to convert that energy into carbon emissions in a carbon dioxide equivalent. In the US we use the EPA's figures that they report on a regional level. Outside the US, the EA in Europe. There's also ... Carbonfootprint.com produce a report every quarter.
**Dan:**
In the case of Google Cloud, however, they recently published their regional grid emissions factors on their website publicly. In the case of Google Cloud, we're able to use the figures that they'd actually published and set at the emissions factors for their data centers.
**Alexey:**
Amazing. Thanks for sharing. I find it amazing to realize how different it actually is from, just, performance, and then the amount of complexity that exists on top of that. The energy efficiency of a data center is an interesting one to me, because it, as developers, forces us to think beyond the thing we're building and the resources we're directly using.
**Alexey:**
One similar conversation that we had that I found quite eye opening, at least for me, was ... We were discussing energy efficiency of algorithms, and we have a separate episode on that. At some point we were discussing, "Yeah, but when considering energy efficiency, you have to think about, how many times do you build your packages, and how many times have you deployed it?" Because all of that is consuming energy. That's part of the whole account for energy efficiency.
**Alexey:**
Whereas when we think about performance, all that is free, and we're just focusing on how fast the algorithm runs, for example, when the program runs at the end of the day. It's quite fascinating. We have to look much broadly than we usually do when developing applications. I find it quite fascinating.
**Rebecca:**
Here I am, I'm a developer, and I am working in an organization that is taking sustainability seriously. I have this tool that you've made available to help me understand these emissions. Now that I have a more nuanced understanding of the relationships, how does carbon get used? How as a developer would I use your tool to help me in my day-to-day work?
**Danielle:**
Yeah. The first step would be to connect to each one of your cloud providers. The nice thing about the tool is that it gives you a place to see all of these in one place. Previously there really wasn't, at least to our knowledge, a way to see everything in one spot.
**Danielle:**
I think that's one of the ways that this tool can be really helpful, because you can see everything in a unified view at one time, or you can break it out and compare. Say you want to compare your GCP usage to your AWS usage and see what that looks like. You can do that with the tool and view one at a time. You can also drill down and look at particular accounts or particular services and see that your EC2 usage is absolutely enormous, but other usages are less. Or certain accounts are really causing a lot of emissions, or your cost is really high for certain amounts, and you can compare that to your other accounts.
**Danielle:**
With that view of being able to compare, contrast, and see everything in one place, we're hoping that, in the day to day, that'll help you. You can keep that in mind and you can make decisions based on ... when you're working on these things. We really hope that it's data that can help you take action.
**Danielle:**
Then, additionally, on top of that, what we've been talking about, to this point, is helping you get a holistic picture. That holistic picture is something that we've heard from a lot of organizations that would be really the most helpful overall.
**Danielle:**
However, if you do want to get more fine-grain detail, or a little bit more deep dive into your carbon emissions for a specific service or specific accounts, we do have the opportunity in the tool to switch the approach a little bit. Instead of using the billing data, we can hit service APIs. In that calculation, we use the actual CPU utilization. We can get that back from the API and then use that in the calculation. It's a much more accurate snapshot in time of your carbon emissions.
**Dan:**
I might also add that the repository is a TypeScript monorepo with a number of different packages. We decided to go in that direction because we're still learning about the different ways in which individuals or organizations might want to use the software.
**Dan:**
You might want to use the client-side dashboard with the data visualization and the charts that we've built in the client package. But maybe, as a developer, you've already got your own database tooling, and you just want to deploy the API maybe in a Docker container that we provided, and have that data served up in different places for your usage.
**Dan:**
We also have a command line application, if you just want to run it by a command line and get the data maybe shown as a table. Or you can just save it to a CSV file, if you then want to import that into other places. We've tried to provide flexibility and options for developers, because we know there's different use cases, and we want to try and support as many as we can.
**Rebecca:**
What's next? What are some of the other things that are on the roadmap for this tool? Because I feel this is quite empowering to me as a technologist to be able to understand, based on the work that I do, what kind of impact am I having on the planet? You've got a lot there already. What's next?
**Danielle:**
Yeah. Looking into the future, I think there's a lot of opportunity for this tool. Like you said, having that picture of the emissions that you're causing really can be empowering for developers, but we hope that this tool can become a little bit more than that, and really be an enabler. We'd like to eventually build in as many recommendations that we can to help you optimize your Cloud use.
**Danielle:**
Some of the things Dan mentioned previously we'd like to build into the tool, so you get suggestions of ways you can shift things around, or maybe you can see a projection of what the future might look like if you make certain changes. All of that is a possibility, and something we would like to explore in the future.
**Danielle:**
Then I think, in addition, in our effort to make this applicable to as many users and organizations as possible, we'd like to add in additional cloud providers and support more usage types and different services, so keep just expanding the things that we already have so that it fits whatever needs different organizations have.
**Dan:**
One thing I'm particularly excited about for the medium and longer-term roadmap is that, if we can have a mechanism for users of the software to optionally opt in to sending some of their energy and carbon emissions to, maybe, some sort of centralized data source data location, maybe with some additional anonymous data like the size of the company, or the industry, or the size of the IT organization, we can actually start to understand trends across industries and across organizations, and start to maybe get a picture of, what does good look like when it comes to Green Cloud in my organization's eyes and my end type? What does not so good look like? 
**Dan:**
And I would love a future where I, as a developer, can log into my Green Cloud portal and hook up my cloud providers and instantly see what maybe my Green Cloud score is based on all those other data types. And then have a list of things and recommendations that I can do to improve that. And through that process, set some standards about what Green Cloud best practices looks like. Because right now the data is not even super available, but the future could hold a lot of potential for that sort of direction.
**Danielle:**
And then building off of that, if we are able to have these types of metrics and standards and ways to measure how we're doing, think there's an opportunity to have this as the default way of thinking as we develop software and technology. So it's something that is a cross-functional requirement that is similar to the way we think about security performance and other things.
**Dan:**
One final thing to add for the longer term road map is, if there's some way that we can build in these energy and carbon emission metrics as part of our CICD pipelines and have developers getting early warnings about you find deploying this code or these instances, then what does that mean in terms of my energy and carbon emissions in a more automated way? We need to think through how that can actually work practically, but definitely there is a desire for it to have early warning, or triggers, or gateways maybe, before you have to [inaudible 00:25:55] step in the CICD pipeline, so you see don't a huge spike and then have to pick something at a later date that can model that and prevent it happening before it does.
**Danielle:**
And additionally, if there's ways to build this in other ways, like maybe you can get opinion slack when you have high usage going through your pipeline, or maybe you can have tests around it. So you know even before you push things and possibly even, I think we mentioned before, if there's existing dev portals, you see that as you're going through your day to day development. So carbon is always in your face. It's always there. You're always thinking about it.
**Rebecca:**
So Dan, you mentioned earlier that you're anxious for feedback and for getting people involved. As a developer, or as a technology practitioner, how can I get involved? What kinds of help would you like? What would you like me, leaving this, listening to this podcast, being excited about doing next?
**Dan:**
Well, I think that the best place to start is to go to cloudcarbonfootprint.org. We have a website there that has all the information you need to get started with the tool. And I think we would just, as a starting point, love developers to look at the documentation, check out the code base and give it a rough try and try out the tool and through that process give us feedback. We really want this tool to be a community driven effort where lots of feedback is happening and members of the community are helping shape the direction of where we go next.
**Dan:**
So we very much so welcomed forks of the repository and pull requests. It's still early days. We only launched it last week, so it's still small, but we're hoping it builds over time. Also with the website, we've got a Google group, a discussion forum that you can join if you have questions or need support. Or if you want to help contribute and shape the roadmap, you could also send an email to that group and be part of the group. Danielle, did I miss anything?
**Danielle:**
I guess the other thing is, if you're interested in working a little bit more closely with us and providing feedback, you're also welcome to reach out on that front. We have in the past, worked closely with organizations to look at their individual usage. And through that understanding, for different organizations, what this tool could be, or how we could shape things. So that's an option too.
**Rebecca:**
Well, thank you so much, Dan. Thank you, Danielle, for talking with us today about Green Cloud and the carbon footprint tool. And we hope that this provides a mechanism for technologists to introduce aspects of sustainability into their day-to-day work, which is ultimately what we all have to do to make a difference overall. To make the world as a whole, a more sustainable place. And thank you, Alexey, for joining me and thank you all for listening to the ThoughtWorks Technology podcast.
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