<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/tracking-technology-stacks-practices-experiences | Title: Tracking technology stacks, practices and experiences across teams | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Tracking technology stacks, practices and experiences across teams 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Ken Mugrage | Podcast guest  Camilla Crispim and Renan Martins
July 11, 2024 | 36 min 59 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/tracking-technology-stacks-practices-experiences#Transcript)
Listen on these platforms
## Brief summary
Understanding your technology estate and how it's being leveraged is critical for organizations; it impacts everything from financial planning to capability development. But given the rapid pace of change — even inside a single company, let alone the wider industry — how can this be done effectively? One approach we've landed on at Thoughtworks is something called a Tech Dash: it's a method of internal research that surfaces information about an organization's technology use and even software developers' experiences. 
In this episode of the Technology Podcast, Camilla Crispim and Renan Martins talk to hosts Alexey Boas and Ken Mugrage about the value of a Tech Dash and explain how it can help track technology use. They also discuss where the idea came from and how they put it into practice across Thoughtworks Brazil.
## Episode transcript
**Alexey Boas:** Hello, and welcome to the Thoughtworks Technology Podcast. My name is Alexey. I'm speaking to you from Santiago in Chile, and I will be one of your hosts this time, together with Ken Mugrage. Hello, Ken.
**Ken Mugrage:** Hi, folks. It's Ken speaking, as always, from Seattle, Washington, United States. Welcome.
**Alexey:** This time around, we'll talk about the Tech Dash. That's a practice and an accompanying tool we've developed in Thoughtworks to better understand technology uses, technology practices, and excellence in our teams. For that, I'm thrilled to have Camilla Crispim and Renan Martins here with us. Maybe we can do a quick round of introductions. Camilla, would you mind introducing yourself?
**Camilla Crispim:** Sure, yes. Thanks for the invitation. It's a pleasure to be here. I'm Camilla. I'm based in São Paulo, Brazil. I'm a principal consultant at Thoughtworks, engineer advisor, also part of the group that puts together the technology radar. I've been part of Renan's team, and that's where everything about the Tech Dash started.
**Alexey:** Amazing. A pleasure to have you with us Camilla. How about you, Renan?
**Renan Martins:** Hi, everybody. It's great to be here. Thanks for inviting me to share about Tech Dash. I'm Renan Martins. I'm the regional head of technology of our digital engineering center in Latin America currently, but Tech Dash came about a few years ago when we were leading technology in Thoughtworks Brazil.
**Alexey:** That's great. Amazing to have you with us. Before we get into exactly what the Tech Dash is, Renan, maybe you can tell us a little bit about the overall context at the time, the challenges we were trying to address.
**Renan:** Sure. Absolutely. Basically, we were in the midst of a rapidly evolving global landscape. Particularly at Thoughtworks Brazil at the time, we were experiencing a very rapid growth, something around 40% year over year. For us, it was essential to maintain a high level of awareness around our technology landscape, around our technology excellence in software development. Reason being, because this excellence is something we pursue actively here and has always been a core part of our identity. As a head of technology for Thoughtworks Brazil at the time, I was responsible for ensuring that our deliverables and everything we delivered to our customers consistently resonated with this standard.
With this growth, it became increasingly challenging because it was like hundreds and hundreds of teams and a decreasing average tenure among our team members as well. To address these challenges, we launched, at the time, an initiative called Tech Assurance Brazil, which eventually evolved into having Tech Dash as a tool being built. Our goal was basically to address this challenge and offer broad visibility into the current technological state of our teams and also help multiple stakeholders from different areas in our business that were also navigating these changes.
**Alexey:** Then perhaps you can talk us a little bit about what is Tech Dash. It's a tool, but it's also more than that, right? Maybe let's get into definition of sorts or something. What is it?
**Renan:** Yes. Tech Dash is basically a tool and a process altogether basically to bring technology, data visibility, bring it to the surface. It's a way for us to collect and know the technology stack, the practices, tools, platforms, frameworks, you name it, that the teams use in their projects. We also collect some subjective information such as the comfort level that the team has with each individual technology stack, and also some practices, and how they are going about implementing them. With that type of data, we intend to promote continuous improvement, data-driven decision-making and reflection in our teams so that they can pursue this excellence. You asked about what Tech Dash is, but I will take the opportunity to talk about what it is not as well because it's equally important, Alexey, I think. It's not a scorecard, it's not a tool to assess teams. It's not a tool for comparing teams by no means. It's basically a way of us to getting to know the technology state, the technology data from our teams. That is extremely important as well to highlight.
**Alexey:** Cool. Camilla, maybe you can talk to us a little bit about how does it work for a team. Before we get into benefits and those kinds of things, but still on trying to understand what it is, how does it work, and what does the team need to do, and how does it affect its day-to-day.
**Camilla:** Basically, the team needs to fill out a survey which asks pretty much all the information that Renan mentioned before. One concern that we had is that for many years, we used to have spreadsheets at Thoughtworks where, once in a while or every month, you would have to fill out, let's say, a Google form or something of that nature. Technology stack practices and all that, they don't change that often. One concern that we had when we were putting together the process, and later the tool, was adoption. We didn't want it to be just yet another form or yet another way to ask people and people not being able or not wanting to answer that.
What we did was we basically did a mechanism to repeat the answers from one month to the next month. Then what the team needs to do or the tech lead or the tech representative of that unit, they can go and update what needs to be updated. They don't need to fill out all over again, and they just recap, is this still true? We can change what needs to be changed, but that comes pre-filled in. I believe that helped a lot, and that was one of the things back in the time when Renan and I, we were tech leads, and we were like, "Yes, I didn't like to do that, so maybe we need to fix it." That was one improvement that we brought to life, and I think it worked quite well.
**Alexey:** Yes, that's great, keeping as lightweight as possible, right? Yes.
**Camilla:** Yes. Just to add on what you asked, the tech lead of the team usually have added rights to go and fill out that information, but in practice, what we've seen is a very collaborative sort of process where the team gets together to answer the questions. That helps to have a broad view, not a single-person view. I think that emphasizes the software development as a team sport sort of thing. It asks about how comfortable is the team with a certain stack and not individuals. It is definitely not about individuals. It is focused on the team.
**Ken:** On that end, what have you done to encourage people to be as open and transparent as possible? Even if it is just about the team, sometimes in other organizations, certainly not at Thoughtworks, but in other organizations, people are hesitant to necessarily say when they're struggling, or if they're struggling. What have you done to encourage that?
**Camilla:** Even at Thoughtworks, Ken, it was a concern at the beginning. It is not supposed to be a way to measure performance, people, definitely not to compare, and so on. We did a lot of conversations with the teams and within the portfolios to ensure that that message was getting across and showing also people the insights that we were collecting and how we wanted to get to build a community as we used to have in our offices before the pandemic because that was right after the pandemic. We lost a lot about the natural, let's say, knowledge sharing and hearing the other team, the other table talking about something that you could help.
We also brought to life those examples so people could understand the benefits that they would also get and giving them enough information for them to trust the process and to trust us. That's definitely not something that's easily done. It is required, trust is required regardless, and inside of Thoughtworks as well, but Renan can probably speak about a broader view on that.
**Renan:** Yes, I think you touched on very good points, Camilla. I fully agree that creating the right environment is key in this type of initiative, and it involves a few critical steps. I think first we made sure to emphasize transparency and trust. Everyone using Tech Dash needed to feel secure that the data they provided wouldn't be used punitively but rather to support their growth and improvement, and also that they're part of a broader community and ecosystem. For myself, for example, as a head of tech or some other leaders like Camilla in one part of the portfolio, for us to understand that there is a capability gap, for example, where we would need to take some action either through learning and development or through some other mechanism to support everyone, we would need to understand individual teams for that purpose alone.
Not to assess or compare them. They would understand, for example, that by providing the data, they would be enriching the community as well because people would be aware that, oh, there is a team over there working on another client, another industry in a completely different context, but that is similar to me because we are sharing the same technology stack. That by itself created something that they share, that they have in common, and that it would be something important for everyone to contribute to. The subjective information, what allows us more strategically to understand which technology stacks were resonating more with developers, the ones they were feeling better about, the ones they were being able to use and implement better and feel better, have provided a better developer experience as well.
We know how important these things are for high-performing teams. We were able to see some cases where a certain technology was actually gaining a lot of adoption and developers were feeling good about them, the teams were feeling good about them. We could understand, upon some investigation, why was that, and come up with some important recommendations at the industry level through our different publications. That is super, super strategic for us, but yes, all of that is only possible if we have that safe environment, which our culture, I fully agree, Ken, is fully supportive, and everyone assume that trust and transparency everywhere.
**Camilla:** Say, I got to be honest—
**Alexey:** Go ahead.
**Camilla: —** here and say that I quoted Rebecca a couple of times when talking to people, and say, "Look, I can't solve a problem that I don't know that exists. I'm here to help. We are here to help, but we got to know what is going on. This is just one way for you to tell us."
**Alexey:** Yes, of course. The upside of that safe environment, it brings benefits in many different dimensions and not just in collecting those kind of things and so on. Investing in that is definitely really, really important for organizations. Renan, you started to talk about some things I wanted to ask a little bit more about, so the benefits and the value that Tech Dash can bring to the organization. You mentioned a little bit about creating communities and connection to the teams, but also things about understanding the whole ecosystem, what's happening in teams, and things like that. From that perspective of technology management, and since you had the head of tech role at the time, for Brazil, what's your perspective on that value? When you think at that portfolio level, and I imagine that's something very common for many organizations who need to understand the whole spectrum of things, teams are doing on the ground and things like that, how does Tech Dash provide value from that perspective?
**Renan:** That's a great question, Alexey. I think it does provide value at the different levels. From the individual level, someone who just needs to figure out who else is working on a similar technology, reach out to and start collaborating, and learning, and sharing, and eventually driving that forward, like in building best practices and learning how to use that technology and evolving it. At the portfolio level, Alexey, I think things gets really interesting because we can then identify bigger trends. For example, certain technologies that started small but gained adoption very quickly.
For us, that showed that that technology has something special with the community and the practitioners, so we could investigate and we could understand why. We could see that the technology was changing based on some business decision we have taken, for example. We were expanding, at the time, the type of services and solutions we were offering to our clients. We were focusing a lot about data and AI, for example. We could see a lot of more data stacks present in our teams over time, which was telling me that it was working, and we were growing that type of capability internally in our business.
Just to give one example of something we noticed, I even have some examples of things we noticed at the time. I think it's worth mentioning, for example, at the time, we noticed TypeScript taking over the front-end ecosystem basically, so, a lot of new TypeScript projects and teams using this technology. We noticed that, for example, Kubernetes and containerization was something booming up to a point of majority of teams, by far, was using containers in non-production and production environments. We could see that, oh, that was actually a big shift.
There is no more space for solutions without considering them at all in that scenario. It was an important thing for us to know about and a constant in our delivery teams. Another thing we noticed was Kotlin, which started in the mobile world, in the mobile space. Then eventually we noticed that Kotlin was being used a lot in the backend, JVM-based type of services, and Kotlin being used in the backend. That was interesting to see how the community was adopting and why the reasons. That type of insight and analysis was only possible by having the collective information, the consolidated and the 10,000 feet view of how the portfolio was shaping from the technologies stack perspective, for example.
**Alexey:** Yes, that's cool. One of the coolest things I've always found about a global consultancy like Thoughtworks is that you get to see what's happening everywhere in several different industries and places in the world. Then if you can aggregate those things, you can really start to see some of these industry trends and things like that. I guess it's kind of the same organizational structure that allows us to build a technology radar, and maybe we can see some of that.
**Camilla:** Yes, it was very nice to make the parallel between things that appeared on the radar a couple years ago and how that was coming to life or spreading and becoming broader like the trends that Renan mentioned before, like Docker Docker Docker. I think it was a team in 2017 or something like that.
**Alexey:** Renan, just to close the loop on that, benefits for the organization, you talked about the industry, but at the beginning, you talked about some of the things in the organization. Does something like Tech Dash allow you to see adoption of new techniques we are trying to spread in the company or identify patterns and things like, oh, everyone is using this tech stack, so let's fire up a joint learning development program on these type of things? What is the connection between, that and what have you seen? It feels like that's very useful for all types of organizations that can think of gathering that kind of information from their teams to think about more centrally defined or centrally managed initiatives, programs, and supporting.
**Renan:** That is absolutely right, Alexey. I think Tech Dash is a great tool to track that type of program. If you are an engineering leader of a highly diverse, heterogeneous organization who has many different teams working on different products, maybe as a result of multiple acquisitions, for example. You have a very heterogeneous type of environment, and you want to understand, for example, first of all, what is all these technology that you're working on and working with, and how comfortable your teams are in terms of using them, and also what's working, what's not working.
If you are, for example, driving some change that would result in technology adoption from the teams, Tech Dash could tell you how you are progressing over time at a monthly basis because we take snapshots every month, for example, to spot that trend in what's changing. For us, it's extremely important because, as a consultancy, we have hundreds and hundreds of teams working on a variety of different industries and with technologies. For us, it's important to understand this landscape and how the teams are doing with these technologies.
Spot trends, and spot common practices, and tools, and frameworks. This all helps us internally to make sure we are delivering what we need to deliver at the excellence level that we expect, and also to foster the collaboration, the continuous improvement that we talked about so far. It's definitely useful for many organizations that are looking into that.
**Ken:** One of the things I'm curious about, we talk about tech stack and tools, and those sorts of things, but also this tool, one of the reasons that we're talking about it is usage of these methods in this tool has grown globally inside the organization. Are other parts of your organization, and I really honestly don't know the answer to this, using it for different reasons? For example, central banking is very different in different parts of the world, and so different tech stacks, and so forth, might use something like a blockchain in Brazil where they wouldn't use it in the US. Are these helping business leaders with recruiting and planning too, or is there thoughts to go that direction, or am I just being strange?
**Renan:** Yes, it definitely helps to spot those cases where, for example, they're rare in the portfolio as well, at the global level, that brings a lot of benefits. For example, working within a blockchain implementation is something not very common. We could definitely find one project working on one region with something similar, and then connect the teams. That's possible after having a centralized tool capturing these data and bringing it to the surface.
As far as helping other areas, yes, definitely. For example, learning and development in any organization is interested in learning what are the capabilities we need to do what we need to do to build the products and deliver the services we need to deliver, and what is the state of that capability in the business today. If there is any gap, we need to bring learning and development and specific actions. Because we ask the teams how comfortable they are with certain technologies, we can definitely understand that for certain technologies we need more learning and development initiatives.
We can even identify, for example, at the client level, at the team level, if there is any gap. That could help staffing. If you have a challenge that you need to solve through software and you need to staff a team, you need to understand, for example, if you have that skill and capability inside the organization, and if you have done that before. Looking at past data, historical data can help you understand that and bring those who can help, for example, deliver that solution better. In Thoughtworks, for example, in the demand organization, when we are talking to customers about a specific type of solution, it's very important for our demand team to understand if we have done that before and at scale or not, and where and when, and bring cases and talk about examples.
Tech Dash is actually a great place for you to go and understand where we use that type of technology and practice, and bring examples to prospects and clients, for example. Yes, it can help many areas within the organizations.
**Camilla:** To this point, Renan. I think as an advisor, I can benefit a lot from the data that is inside of Tech Dash because I get a consistent view of trends across the globe. I can advise business leaders to say, "In your field, this is what's happening, not only in Latam but also in other regions. You might want to consider this when you're putting together your tax strategy or your business strategy." That is very, very helpful, and in general terms, I think that if you as a tech leader or a business leader, and you want to have data-informed strategy, having a tool such as Tech Dash would help you, and it would benefit you in knowing how to put together that strategy, as well as following up whether you are getting closer or not so close to your goals.
**Alexey:** Beyond consolidating, but Camilla, you started to talk a little bit about the tech leads, and I'm curious about that perspective. Because you both mentioned forming communities and finding people working on similar things, from a team's perspective, can a tech lead use information in Tech Dash, and then understand well, people with similar problems, similar technologies, and those kinds of things? Does that work, and how does that dynamic work and serve those teams on the ground?
**Camilla:** Yes, for sure. Not only the tech lead but anyone in the team, actually, anyone within Thoughtworks can have a look at Tech Dash and see what might be the project available and what type of stack they are using. If you're willing to learn about that, you may invest some time in learning it and might ask to switch project or something like that. Also, if you are struggling with something or facing a business problem, and you can link to other teams that do really well in a certain area, that would help you in a way, get help as a self-service help, in a sense, where you don't have someone in between to tell you where you should go to ask for support or point you to someone that could help you, which was something that Renan, and I, and other leaders in the technology space used to do when we were smaller.
Now we have this self-service way for you to spot on which teams, which people could help you moving forward. Even not only if you are struggling, but you are seeking to become a leader in a space or you want to specialize in something, then you can find that information in an easy way.
**Renan:** One good example would be, I think it's a common challenge today, how many of our teams are using generative AI in the context of software development, which tools they're using. That is something that you can quickly understand, and from there, have the conversations that you need to better develop a strategy or take some actions. That is just one example, and at different levels, we can have people searching for data with different intents as well.
**Alexey:** That's cool. You have been putting the tool and the processes together for one challenge. That's quite common in the industry, right? Understanding what the teams are doing, what do they do in common, and how can you extract patterns, learnings, and connect people doing similar things. What learnings would you have to share to other people? Any advice? Any things that were critical in that journey that other people should pay attention to? Maybe you can share some of that wisdom to our listeners.
**Renan:** Yes, I would start by acknowledging that technology data is extremely important and can tell you many things at the team level, product level, org level. Find a way to track that data is critical for engineering leaders, but also for business leaders. The technology data can tell you a lot about what's going on in your teams. Since technology is every day more embedded into the business and the products and services and everything, it's going to tell you an interesting story when you start analyzing what's going on over time.
That would be the first, is to make sure that that data is being tracked and analyzed just like any other important data you currently track in your environment, in your business.
Secondly, I think in order to do that effectively, you need to build an environment of trust and transparency within your teams, especially around the subjective type of information you want to collect. We talked about that already in terms of the comfort level and how well the teams are using that technology. What they want to share, the lessons learned, the mistakes, all the things that we are interested in.
Unless there is that safe environment, they won't share to the extent that you as a leader would like. Ensure that the data is collected and used constructively to drive improvement, not as a punitive measure, is super important. Yes, from a leadership perspective, also I think it's essential to allow tech changes to happen organically informed by this data. The only constant we have in technology is that it's actually changing all the time. If you have a tool like Tech Dash or any different tool or process to track technology, your goal should never be to make sure everyone is compliant and using the very same technology stack across the board throughout the entire year or two years, otherwise, you are focusing on the wrong thing.
It should allow change to happen, and it should welcome that. It's more about knowing how the change is happening and what it's telling you, and how can you drive improvement from that? I think the intent of having a tool and a process to track that data is super important. I think that data can really help and inform your tech strategy, your next steps and guide the teams more effectively, including the subjective information. We know how important it is the developer experience and how people feel the wellbeing of teams, and how well they feel when they are working with certain technology, relates to the high-performing teams in your org. Pay attention to that as well.
**Alexey:** How about you, Camilla? Any final thoughts you want to share?
**Camilla:** Yes. I think looking at the team level especially, it is important that the team has access to these data so they could go through the reflection process and getting insights, and thinking about how to improve. I think a key thing in this whole process and usage of Tech Dash is, in fact, the continuous improvement and pursue of excellence, part of it. We do want people to continue improve, and they should will to do that as well. I think looking at how they are doing, and where they could be, and what they can achieve is very helpful and very powerful for the team, but also for the organization as a whole. This also contributes to the adoption of the tool and the process. It is not about being in a scorecard, it should be about improving consistently and throughout the months and the time.
**Alexey:** Yes. Amazing. Thanks, Camilla. It's been a really fun conversation. Even though Tech Dash is an internal tool and process to Thoughtworks, there are many, many insights here that apply almost anywhere. Thank you so much for sharing all of this. Unfortunately, we're coming to the end of our conversation. It was a great one and amazing to have you with us. Thank you so much for joining.
**Camilla:** Thank you.
**Ken:** Thank you.
**Renan:** Thank you, Ken and Alexey. It was great to be here.
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
[ Tech Radar Vol.30 ](https://www.thoughtworks.com/radar)