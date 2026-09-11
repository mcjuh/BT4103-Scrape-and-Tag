<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/engineering-platforms-golden-paths-building-better-developer-experiences | Title: Engineering platforms and golden paths: Building better developer experiences | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Engineering platforms and golden paths: Building better developer experiences 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


October 19, 2023 | 38 min 18 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/engineering-platforms-golden-paths-building-better-developer-experiences#Transcript)
Listen on these platforms
## Brief summary
The concept of the developer platform and the discipline of platform engineering have been important in shaping how the industry thinks about enabling developers. But what does it mean to actually build and maintain a platform? How can you ensure it actually supports the people that need it?
In this episode of the Technology Podcast, hosts Ken Mugrage and Rebecca Parsons are joined by Chris Ford of Thoughtworks Spain and Aidan Donnelly, Director of Technology Platform at Personio, to discuss the importance of engineering platforms in organizations today.
Read Aidan's writing on [Medium](https://medium.com/@aidan.donnelly).
## Episode transcript
**[Music]**
**Ken Mugrage:** Thank you for joining the Thoughtworks Technology Podcast. My name is Ken Mugrage. I'm one of the co-hosts. I'm joined today by Rebecca.
**Rebecca Parsons:** Hello, everybody. Rebecca Parsons, CTO Emerita of Thoughtworks and one of the technology podcast co-hosts.
**Ken:** And joined today by a guest, Aidan.
**Aidan Donnelly:** Hi, everyone. I'm Aidan Donnelly, director of technology platform at Personio. Thank you for having me today.
**Ken:** Thanks for joining us, and Chris.
**Chris Ford:** I am Chris. I'm the Head of Technology for Thoughtworks Spain.
**Ken:** We're here today to talk about platforms, and it's a very large topic, something we've talked about quite a bit. I guess I'm going to start Aidan with you, just for the purpose of today's discussion, what do we mean by platforms? What is a platform? What are we talking about today?
**Aidan:** There's a number of different ways you can describe a platform team. Most generally it's an investment by a company and a group of people who are going to deliver something that will help other teams to do their jobs. It's an investment because you can do without a platform team and some companies do, but with a platform team, the company believes it's going to be more beneficial to centralize some aspects of a role rather than to distribute amongst multiple teams.
In my experience and in my current company, we're a B2B SaaS company, so the platform team owns both the cloud infrastructure and all the tools and processes to keep the infrastructure available and scalable and all the tools and processes which are used by software engineers to get their code onto the platform. The central investment is to give the engineers the best tools to write and build and test and deploy code. If the team does a good job, then the engineering organization is more productive, efficient, and has a higher quality output. Obviously, hopefully less issues arising in production as a result of good work by the platform team.
**Ken:** When we talk about Thoughtworks, we put platforms into three general buckets, very generalized. One of them is the business platform like your Ubers and that sort of thing. The next one down is like an API platform where I own a bunch of services and I'm going to average and put them out for other people to use. Then there's the infrastructure pipe or platform where people deploy code. It sounds like you're talking about more the last one there, the infrastructure where your development teams use it. Is that correct?
**Aidan:** That's correct. Of course, I'm a technical platform owner, so I'm thinking of the last one more specifically, but also as I mentioned in my introduction, how do you get to the infrastructure, how do you get code onto the infrastructure? The developer experience mission is part of the platform for me as well.
**Ken:** I was interested, you wrote a blog on Medium about that, where you described the platform as including the IDE and other things. Chris, what's your take on that? Do you think about those as part of the platform in your day to day?
**Chris:** I actually think that focusing on what the platform is made of is a false direction. Aidan earlier mentioned platform. He didn't say it's made of Terraform or it's made of servers, or it's made of what. He said it's an investment, and I think that's actually a really interesting way of approaching it. You could see platform not as a noun, but as a verb, so in the case of the distinction you raised earlier between business platform or internal business platform, they might literally be made of the same stuff. They might have the same business logic. They might, I don't know, provide recommendations, but it's the usage to which those recommendations, for example, a book that is the distinction.
I think you have to think about what a platform is for. You have to think of platform as a verb, not a noun. When it comes to the IDE, well, yes, I think if it's something that helps to manage the cognitive load of development teams, then it should be considered a platform. I mentioned cognitive load because that's a concept introduced by the Team Topologies book when talking about this kind of responsibility division. I think it's a really helpful thing to get us clear on what we're actually trying to achieve when we have platforms and platform teams.
**Rebecca:** You mentioned the phrase developer experience, and we've been alluding to this. I like the focus on experience. I hear sometimes people talk about developer happiness, and nothing like a platform can ensure happiness, but I think focusing on developer experience as a way of saying, "Am I providing the set of tools and such to developers to allow them to be more productive and more effective at delivering?" How would you characterize developer experience? What are the sorts of things that we focus on in terms of developer experience and then how does that manifest itself in these platforms and platform teams? What are they really trying to accomplish to reach this goal of improving developer experience?
**Aidan:** I think happiness is certainly an aspect of experience. We do want developers to be happy or to put it a different way, to be satisfied. If they're satisfied, it's an input into them doing a good job, which has outcomes that we can talk about perhaps. You mentioned efficiency, I mentioned quality, those are also aspects of experience because if you're looking at an engineer who has code in production, part of their experience is that it runs smoothly and perhaps they don't get woken up at night when things go wrong.
Everything that fuels into the end-to-end, smooth running of business code and production is part of the experience. Not to go into analogies too much right away, but if you can imagine like the experience you're having with an IDE or with a feature flag system or with a pipeline that's deploying your code and running tests, also translates to the experience of the end user, but if the engineer is simply happy in doing the first part of their role, that doesn't cover the full compass of experience for us.
We want them to have a long-term good view of what they've done and to see their work in production, and not to stretch the analogies too much, if you think about a physical tool in the real world, and it could be a screwdriver or a more complicated tool, you want the experience of using that tool to be good, but you also want the thing that's built with that tool to be good, and that I think is the encompassment of developer experience, the overall operation of the software and production is included in that.
**Chris:** I think the use of the phrase developer happiness is really interesting because I think ultimately businesses don't employ people just to improve their subjective emotional state. They might want productive people to work for them, and that's great, and probably intended people are more productive, but I think what works for that metaphor in the development sphere is that developers do want to do a good job, developers do want to be productive, so by focusing on that response from developers, it's a reliable proxy for whether they're productive, because to get back to developer experience, my subjective experience as a developer, that's quite a tantalizing profession, but I really, really enjoy being a developer when things go right, when the code works, when a test passes, when the build is green, but my experience is that actually a lot of my day when I'm a developer is when I'm stuck.
I think more so than other professions, a very large proportion of the time as a developer is spent on various, maybe you could call them yak-shaving activities that aren't the real task that I'm trying to accomplish, and that's where I really think platforms and developer experience comes in because I want to as a developer spend more time solving the problem. I really like solving problems. I get satisfaction both just for the problem itself and for the fact that I've made an impact on the world. There's all sorts of things that pull me away from that.
Maybe it's that I'm not that great or that interested in configuring network for the service of my production cluster, or maybe it's something about the build system, so if a platform or a platform team or an investment in a platform team, to go back to Aidan's comment, can help me to spend a greater proportion of my day on solving the actual problem, that's a pretty good way for me personally, at least, to improve my happiness as a developer.
**Ken:** One of the things that-- I know Aidan, you've talked about this in your blogs about the concept of being close to the money, with a platform team, who are the customers and how do you define that mission and vision? When there's all these things out there, there's the problem-solving, Chris just talked about, that kind of stuff, how do you define mission and vision for a platform team?
**Aidan:** What I mentioned being close to the money, it was reminiscing about a time when I was working on a system that was bringing in money and downtime was very easily equitable to value, so you knew that if you kept the platform stable and running, you could equate that to the value of your work. When you're further from the money, when you're deeper down in infrastructure, closer to infrastructure, or maybe when the business isn't reliant on revenue as a close connection to uptime, maybe your customers are paying you monthly and they can tolerate you being down somewhat, that informs how you measure your output as a platform team.
It also informs how you create a mission and vision for the team. I've done this a number of different ways. When I was working in Amazon and I owned a monitoring system, it was also a platform system. It was a centralized global system for checking for failures in the network. Our first mission statement was along the lines of two metrics called precision and recall. We wanted to make sure that we had all of the information and that we were precise in the alarms that we sent, but that mission statement didn't really resonate with anyone. There were nice metrics and we tried to influence them.
The mission that I came up with the team was more along the lines of being responsible for the outcome of availability, and in that platform team, that's really where we ended up in terms of saying that we are responsible for the availability of the network as a platform. You can say the same thing in a mission statement for an infrastructure platform team. You can point at the fact that maybe it's not your entire responsibility to keep the platform up and running because if you're dependent on the cloud provider, your availability is dependent on them to some extent.
You can certainly take ownership of it in your mission statement and do everything you can to identify the availability minutes that you'll save through the projects and through the work that you deliver. I could talk a little bit more about that in one aspect of it. The other way you can define a mission statement, going back to Chris's example, is as a developer, you can be blocked, and that's engineers' hours wasted. That's what we call it. Again, we can measure this.
We can measure the amount of time engineers are spending on specific tasks, whether it's busy work that they just have to do, like upgrades, dependencies of third-party libraries, it just has to be done, or whether it's something more specific like spending time trying to get a piece of infrastructure up and running using an infrastructure as Code Construct. If we measure how many times that happens, we can multiply that by how long it takes and we can get a figure of engineers' hours saved.
That equates to, if you multiply that out in the way that I do, at least you can come up with a number of headcounts, say like if you employed people full-time, would it be 5 people or 10 people that are doing that work? I think, Ken, it's a great question. It's a lot of different aspects to the answer, but there are ways that I have found that you can both express a mission for the team and to also quantify how you're succeeding in that mission.
**Chris:** What I really like, Aidan, about what you said there is that you're defining missions that it's valuable to be excellent at. I think the big trap of platform and infrastructure team is to be seen as something that is either or not there, and if it's there, that's fine, no one cares, and if it's not there, it's a disaster. Now, the problem with that is that applies to all sorts of commodified aspects of the business, so the desk chairs need to be there. If they're not there, it's a problem, everyone stops working.
We've got to work out to install the chairs, we put them back, and now we have them and no one pays attention, because maybe, let's say, to continue the example of desk chairs, maybe when economic times are good, it's worthwhile to buy really comfortable, really nice chairs for people, but then if times are bad, maybe we'll just go with the simplest thing possible because it's not core to what we're doing as a business.
I think defining your mission in terms of something that is of value to be excellent at allows you to be excellent. It gives you permission to do a really good job, and to be seen as a hygiene factor for the business is really a route to being seen as something that costs should be cut just above the point of failure, which is not really a respectful position for platform people to be in, and certainly not a comfortable one.
**Ken:** Let's take the chair thing perhaps a bit too far. If I put really, really, really comfortable chairs in one side of the organization and not very comfortable ones over by the coffee machine, people might actually end up further away from the coffee machine. In platforms, we talk about golden path or paved road. It's not, "Oh, developers, you must use this infrastructure platform." It's making it attractive to them. Aidan, do you have comments about that? How do you manage that, make it a place that people want to be as opposed to something where they're told to do?
**Aidan:** I have experience with golden path narratives, and we have a document that has a very nice picture of the golden path with lovely green grass either side of it. I'll come back to that in a second because it's relevant to what I'm going to say next. What we found is through the description of that golden path, what we're saying to engineers is, "If you follow and use these tools, we will give you our best support, so you will have a good experience.
We're using these tools because these are the ones we recommend, and if you get stuck," as Chris was saying, "we'll help you because we know exactly what to do. We know exactly how to unblock you." That's the golden path. What we found more recently is that people, to use the chair analogy, are sitting where you don't want them to sit because they just prefer to sit there, and no matter how nice the chair is, they're just going to sit where they want to sit. In reality, that means that they're using tools that are on the silver path or the bronze path, and we found it difficult to influence that decision because it's not a very hard rule that we're setting.
I was joking with some of my team saying we need to change that picture and have 10-foot drops either side of the golden path. In other words, there's no other silver path to fall into. It's just a straight cliff or something like that. I think we're coming around to this idea that we need to be a little bit more opinionated about the golden path in order to drive the best outcomes and to centralize our efforts in the best possible way.
**Rebecca:** I think to some extent too, the way to do that or a way to do that requires a great deal of communication between the platform team and the engineers, because from a customer perspective, the features of the platform, the customers of those features are in fact the engineers, and if there are engineers that are going off the golden path just because you don't want to make them miserable but it's like there really isn't any reason for you to do that, but there are sometimes people stray off the golden path because there is a reason. "We are the first people within the organization that need to use a graph database and there's no graph database capabilities."
Having that conversation with the platform team and understanding that, I think is important. I draw the analogy to many, many moons ago we had all of these architects who were going to do reusable components and yet they never talked to the people who might actually be using the reusable components to find out what they needed. How do you facilitate that conversation around when people aren't on the Golden Path and understand is this something that is just "I don't like the way you did it" versus "Well, actually, there's a feature that I need that isn't currently provided on the platform"? Can you talk a little about how that works in practice?
**Aidan:** Absolutely. I think I mentioned the bronze path and the silver path. One of our ways of dealing with this was to say we absolutely recognize that, first of all, people want to innovate, and that should be a good thing, so you should be allowed to check whether a tool or a language is better or a graph database is needed. Yes, sometimes it's just a requirement that comes out of nowhere, your company might make an acquisition of another company that has a different technology set, so you can't ignore that, you have to support it. I think the way, again, I'm currently thinking about this is to bring an element of operational readiness to the discussion.
Where I'd like to draw the line is where you can innovate and we want to see new solutions to existing problems or better solutions to existing problems, but you also have to acknowledge that the golden path includes operational support for that technology, and if you're going to innovate, you also have to show that it's supported in production, that it's got good availability, that you've got things like [unintelligible 00:19:15] in place, and that it's a proven technology that we can rely on. Then you can graduate up to the golden path, and if we take that decision jointly, we'll support that, and that's a good thing.
The golden path is not-- I was going to say written in stone, but what's in that document is not written in stone. We actually have little arrows that go up and down and say, "Here's how we're thinking. This is something that we're going to invest in and we're currently going to bring it up to that golden standard." Or, "Here's something that we're thinking is something to be phased out," so we're giving the indication to the engineers where we think something is headed.
**Chris:** One thing I think it's worth celebrating is that if you're a product steward of a platform, you have really privileged access to your customer, right? Many product owners have to speculate, or if they want to actually talk to one of their customers, have to go through some focus group mechanism, and then there's problems with artificiality, et cetera. If you are providing an internal platform to a company, you probably can talk to them over messaging system of choice, or you can email them or you can set up a conversation.
I think actually sometimes people are a little bit too reticent to just reach out and ask someone because they agree you should apply product stewardship to internal platforms, but you don't need to put up this wall or this barrier that doesn't need to exist when you're in the same organization with the same mission. That's actually a great privilege. The curse of it is that measuring of business value that Aidan mentioned is harder because ultimately you're providing services to developers who provide services to end customers. The blessing is that those internal customers are so much more accessible. They speak similar language to you, you can ask them about Java and infrastructure and they can answer about Java and infrastructure. That's actually, I think, a really joyful part of product stewardship of a platform that people should take advantage of.
**Ken:** Switching gears just a little bit, we talked a little bit about the outcomes and that sort of thing. Nothing you've written about, Aidan, is the best practices leading to outcomes. At Thoughtworks, we call them what we call our sensible defaults, because we work for a variety of clients, we don't think we don't use single best, we say, "These are the sensible defaults. They make the most sense in most cases." How do you do that in an order in an organization? How do you actually get those to align so we are all measuring the same thing and get those measurable benefits?
**Aidan:** Yes, let me pick the availability side of the answer I'm going to give, because if you start with a business objective like an availability SLA, three nines, or four nines, and you take a period of time like it's a month or a quarter, you end up with a number of minutes that you have as a budget that you can be unavailable for, otherwise, you're not fulfilling your assurance to the customer. Starting with that, if you've failed your SLA, you can figure out how many minutes you need to save, and the way I have done this in the past is to look at all of the incidents that have happened.
We're pretty lucky in my current company, we have a reasonably good hygiene of keeping a good documentation on incidents, and also the time to detect and time to recover. When we look back at a number of incidents, we can see where we've lost those precious minutes, and we can see the commonalities in the causes of those minutes being lost, and that enables us to think up and prioritize projects that are targeted to save those minutes. If you can imagine, let's say, for example, we look at a number of outages and 60% of them could have been prevented by the use of feature flags, then we take a project to say, "Well, we have a feature flag solution.
We just need to make sure that people are aware of it, they know what can be put under a feature flag, and maybe we'll write a little bot to remind people when they're publishing a merge request, but there's no feature flag associated with this, and maybe it would be a good idea." You can make a direct connection between what you're intending to do, which is to save availability minutes, and then you just wait another period of time and you look back and you say, "Well, how many instances of that root cause happened after I applied that project, after I tried to diminish that?"
That's currently how I'm approaching the problem of measuring the outcome of something you're trying to achieve. That example, feature flags, is a real one because everyone can agree that feature flags are a good thing, but prior to us looking at the outages, there was no reason for us to know how much more we should do in that area. The tool existed, it was on the golden path, the documentation said to use it, but something extra was needed in order to drive the outcome that we wanted.
**Ken:** Chris, if I could, building on the same thing. I know as a engineering manager, there's lots of practices that we highly advocate. They are our sensible defaults, peer programming, test-driven development, that sort of thing. What's the responsibility of the developer developing the application for uptime? How do we manage that? How do we make engineering rigor meet these same goals?
**Chris:** Yes, I think that's an interesting question. First of all, I think using a platform as a way of nagging developers into doing a good job is perilous, so I think like that path to training up developers to do a good job, to having the capabilities to knowing how to guide good tests or clean code or so on, it can be really tempting to use the platform as a vector to teach people about things because the platform is omnipresent, but it's a little bit dangerous because you don't want to introduce that kind of element of resentment where people feel like the platform is telling them what to do rather than enabling them.
I think that said, that really crisp division of responsibility that the job of the platform is to put tools into the developer's hands and then all the other things that you might do to in a developer community to think about how to spread good practices, et cetera, need to be in place. One exception I might say though is that like the reason why Aidan was able to give such a clear answer was that there was a common ubiquitous language for uptime, for availability that he's tracking. He's able to have a conversation across a wide variety of teams because we are speaking the same language.
I think actually that is one area where clarity and consistency really is a high leverage activity to a greater extent than implementation. I guess you probably talked about this on other podcasts, but the four key metrics, I guess it's the five key metrics now with availability being there as well, is something that really gives a common language. That can allow a platform team to understand what's going on with development teams.
It can allow development teams to know how they're doing relative to norms either inside the company or the industry, and it can help people not talk across purposes. In general, I think you get 80% of the value with 20% of the effort, if as a leader or as a manager you focus on the interface rather than the implementation, and definitions of metrics and ways to measure what's going on is some of the highest leverage interface management you can do, so focus on that would be my suggestion.
**Aidan:** I just pick up on that, Chris, and maybe it didn't come across, but the two missions of the platform as I see them, the first is the developer experience, as we talked about, and that is trying to make engineers happier and to be able to do their work in easier way, and that's a really good thing, but ultimately, the greater mission is to the end users of the system, and that's why I spoke about availability as being something that it's harder for engineers to hear that they need to do or use a tool better or use a tool more to the extent that it's meant to affect outcomes like availability. Ultimately, that's a slightly harder conversation that you talked about as nagging the developers. I know exactly what you mean. It's a delicate balance to draw because you don't want to be dictating to engineers. They're very capable and intelligent people, but I see a greater responsibility to the end user who's relying on the software to keep running, so just to make that distinction.
**Chris:** Yes, and I hope it was clear, I wasn't referring to your particular experience with that because I think you can tell from the way you're describing, but I think actually the first book I'd read if I took over a platform department might be Team Topologies. The second book I might reread might be Nonviolent Communication. In the sense that this kind of question about how you state your intentions clearly, state your near needs clearly, how you offer something to another group of people rather than the pushing on it in a way that activates defensiveness, I think is a really vital part of managing a platform, and I think people who think that the only qualification to managing a platform is technical intelligence are really likely to be into a hard fall if they don't also have excellent emotional intelligence, because they can be the best person in the world at crafting a technical artifact, but if they're not good at working within the human system, it's not likely to deliver the outcomes that it's intended to.
**Rebecca:** I think one of the issues too, and this is, again, a tension that we often see between people who are focused on delivery of end-user value and people who are responsible overall for the broader estate and things like availability and recoverability and such. There is a tension there because it can be from a, say time to market perspective, more effective to do something the wrong way. There is that balance between when is it the right decision to do something the wrong way initially, this is the whole technical debt discussion, but I think it's in some ways relevant here is with a platform, you can go so far as to make the wrong way, perhaps less destructive, maybe because of the security defaults that you make sure there are, many things like that. Fundamentally, there is still that tension. In your experience, Aidan, what are the right kind of forums for resolving those tensions?
**Aidan:** I think first and foremost, the platform team, which is figuratively in the engine room of the ship, say, needs to be very aware of the business, what's happening on the top deck. They need to be aware and draw a connection between what they're doing and what the business and what the end users want. What I mean by that is that the decision choices that you have in terms of doing something quickly and perhaps incorrectly or not to best practice versus waiting and doing it more rigorously and taking a longer time over it, really should depend on what the business is, what the business of the company is and what the end users want.
You can take risks sometimes that are calculated to get a product to market quicker or to get a feature in front of customers quicker if you're also aware of the potential downsides. What comes into the equation is, for example, the ability to detect issues in production quickly and to revert them or roll them back. If you can do that within minutes and you're very actively looking at, for example, a release that might be a little bit risky, then that adds into the decision-making factor. If you have a one-way door and you're doing something that might corrupt data or leak data, that's obviously something you take a little bit longer on because your customers-- well, pretty much every application is going to want to avoid that.
You can imagine in a, let's say, for example, a business system, some things are time critical and need to be available all the time or users are very much going to be affected and other things if they're down, might be possible to come back and redo later, so a user might be frustrated for a period of time, but they're not blocked in doing their job, they're just delayed. I think the point I'm making is that the platform engineers and platform leadership need to be very aware of the business in order to make those decisions.
**Ken:** Platforms many years ago were a single thing, I had a box I was going to put my software on. Now some stuffs in a public cloud, this is in a private cloud, and here's a SaaS provider and so forth, and so it's a much more complicated thing. Where do you draw the line on owning the platform? Who owns what? Is it the developers because they're using this SaaS thing? Is it the platform team because it's part of the business? Where do you draw those lines and how do you look at updating those and keeping those fresh?
**Aidan:** Great question and a tough answer I think. There's a couple of examples that I would give where the difference between infrastructure and application or service is not very clear. If you take a well-known example of a relational database, it's a piece of infrastructure, you can automate it's creation, you can scale it automatically, you can monitor it in uniform ways, but the logic inside it, what's in the database tables and how they're connected together and how they're queried is application logic. Who owns the problem if there's a slow query that appears over time and there's a root cause to that? It could be that a table is growing or there's a missing index.
Is that a platform problem that should be solved by platform teams constantly monitoring and fixing well-known relational database issues, or is that the ownership of the application teams, the product development teams to find and fix those issues and to maintain something like that? We've lent into that space in my platform team in having people that are more knowledgeable of the database schemas and noticing problems, reviewing issues, finding root causes of things like slow queries.
Databases are sort of a well-known technology now, but if you take a new technology, something like Kafka, again, it's a piece of infrastructure that can be deployed and scaled in a well-understood way, but the logic of what it's doing is not as well known in the industry. It's not something in my view that every engineer can take a look into and understand what's happening inside a Kafka system. The line can move sometimes closer towards the application and the service ownership, but sometimes you have a resource issue or a knowledge issue that you can't really service a piece of infrastructure because you really don't understand what's inside it, and that can lead to the line sometimes moving back and forth in the conversation, to give you one example.
**Chris:** I think reality is messy. When things are going wrong, they're usually going wrong in a way that we didn't intend things to go because otherwise we wouldn't call it going wrong, and so there's something unknown or unexpected or problematic about the situation, so in reality, you hope in the end that human beings talk to each other to figure stuff out when they need to. I think the ideal is that the platform team understands with clarity what service they're offering, and if what service they're offering is not functioning correctly, they should be able to tell that and correct it.
If they're promising to provide some kind of abstraction layer on compute being provided and that's not a compute that's supposed to be provided, is not provided in the way it should be, okay, that means that the contract that the platform has with the user is not fulfilled. Then if it's used in a way that is problematic, so the platform is working as coded or as described or as intended, but it's being misused, then my idea would be that the development team following that you build it, you run it, [unintelligible 00:36:59] would be responsible, then they would also be able to rely on the platform, not just as a technical artifact, but as a group of human beings, they can consult, that they can have a shoulder to cry on and they can ask for expert advice.
Now the trouble is reality, like I was saying, is messy, and you cannot always rely on an abstract definition of responsibility. Some kind of matrix somewhere to say exactly what team is responsible for what's been going wrong. I think ultimately success is when the development team is able to exercise their discretion, their autonomy, without being overloaded either by cognitive load or by things happening in a technical domain that they have no expertise on.
**Ken:** Great, thank you. Not surprisingly, like many other things, it comes down to the humans, which is a good thing actually because mostly we want to do a good job. Again, thank you Aidan and Chris for joining us. It's always great to hear how other folks address these, and Rebecca, for co-hosting. Thank you, listeners, and look forward to next time.
**Rebecca:** Thank you.
**Aidan:** Thank you.
**Chris:** Thanks very much.
**[Music]**
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
## Find out what's happening at the frontiers of tech
[ Explore Tech Radar ](https://www.thoughtworks.com/radar)
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