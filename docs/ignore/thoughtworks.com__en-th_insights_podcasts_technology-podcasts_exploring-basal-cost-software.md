<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-basal-cost-software | Title: Exploring the Basal Cost of software | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring the Basal Cost of software 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Evolutionary architecture ](https://www.thoughtworks.com/evolutionary-architecture)
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Neal Ford and Birgitta Böckeler | Podcast guest  Georgina Giannoukou and James Lewis
October 20, 2022 | 30 min 11 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-basal-cost-software#Transcript)
Listen on these platforms
## Brief summary
The “Basal Cost” of software is an idea from [Eduardo Ferro Aldama](https://www.eferro.net/2021/02/basal-cost-of-software.html). The term is borrowed from biology, where the Basal Metabolic Rate refers to the number of calories a human body burns just to maintain normal functioning. Applied to software development, the concept is intended to help us pay much more attention to the long term costs — like additional complexity and maintenance — of building a new feature.
In this episode of the Technology Podcast, James Lewis and Georgina Giannoukou join hosts Neal Ford and Birgitta Böckeler to discuss the Basal Cost of software and explore how it can help organizations and software development teams better manage product and system complexity.
## **Episode transcript**
**[Music]**
**Neal Ford:** Hello and welcome to the ThoughtWorks Technology podcast. I'm one of your regular hosts, Neal Ford, and I'm joined today by another of our regular hosts, Birgitta.
**Birgitta Böckeler:** Hi, I'm Birgitta Böckeler. I'm a technical principal out of the Berlin office of Thoughtworks.
**Neal Ford:** We are currently in Barcelona for the Doppler meeting where we put together the radar and one of the topics that's actually several years old that we never got a chance to talk about, we're going to talk about today with a couple of our colleagues. I'll let them introduce themselves.
**James Lewis:** Hi, I'm James Lewis. I'm a Technical Director for Thoughtworks based out of our London office.
**Georgina Giannoukou:** Hello, I'm Georgina Giannoukou. I'm a Lead Developer from the Madrid office.
**Neal:** Today we're going to talk about the basal cost of software development. Would someone please describe what that is? It's a metaphor.
**Georgina:** Yes, I can go ahead. Basal cost of software is a term coined by Eduardo Ferro back in 2020 in his blog post, Basal Cost of Software, which basically outlines that the cost of features, not just the cost of initial development, but the cost of maintenance, the cost of onboarding, and it increases and maintains after until the feature is dead.
**Birgitta:** What is that term? I was stumbling across this word, basal first. Can you go a little bit into his metaphor?
**Georgina:** Yes. It's a metaphor from the basal metabolic rates that is human requires the amount of calories burned just by existing, not doing anything. If we put it in software features, it's the same, basically. It reminds us that besides building something new and always building new things, we need to understand that software will cost us in the meantime and that will reach the capacity of the team building those features until the point where they can't innovate anymore. That's why it's important and we need to dig a bit deeper.
**Birgitta:** I think there's multiple things that create that cost but Eduardo in his article is focusing on — I would say cognitive load things, right? Like existing code.
**Georgina:** Sure. We need to understand if you break it down, it's the sole cost of dependence, for example, technical dependencies. Then the cost of onboarding new members to this feature, the cost of supporting, also the cost of adapting this code to new ways of writing code. Also the support to the end user as well as support to the internal users. In the end, it is a form of technical debt. Basically, if we ignore it completely, we'll just reach — increase the cognitive load of the team. Plus then we're not going to be valuable enough. It's going to be code that we're not going to be able to maintain in a valuable manner, in a sense.
**James:** Here's a challenge based on that. In biology, metabolic rates change. The way we use our energy changes as we get older. As animals age, more and more of the calories they're consumed are used just to keep the body going to repair cells, to create new cells, to essentially try and reverse aging but eventually, the body can't do that anymore and all the energy it's taking in goes to cell repair and at some point, you can't get enough energy and the cells are too old. Essentially people die, mammals die. Does that imply then that all software has this finalized lifetime?
**Georgina:** Yes, if you consider, for example, legacy code written in software that's not supported anymore, for example, there's this famous code of, we're not in the business of creating new software, we're in the business of evolving existing code. This is part of the challenge. Basically, yes.
**Birgitta:** That's interesting that taking that metaphor even further is your basal cost at some point, just repairing, repairing, repairing, and you can't get around to anything else anymore, right?
**James:** That's exactly that, yes. And that's what happens with animals, with mammals. You're consuming more and more energy as you get older. Also, the other thing is, as you grow, as you progress from a baby thing to a grown thing, the way that you're directing your energy also changes. I wonder if there's parallels with that as well.
**Georgina:** We have a lot of course, from developers, the initial development of the feature, and then everyone's testing it and waiting for a response and then it dies out because you need to build new things, you need to maintain a few things, so all this excitement dies out eventually.
**Birgitta:** I also like how in the blogpost he distinguishes between, yes, you have all that stuff to maintain that you just built, but then also the more features you have, the more impact it's going to have on the new stuff you're building as well because you always have to take into account all the things you've already built and shoehorned into that. The more of that you have, the more you also have to use when you build something new.
**Georgina:** He basically outlines that the capacity of the team is finite. It's something we see over and over again when we reach that point and then the team gets to a firefighting mode where they're just supporting old features with zero capability of innovating.
**Neal:** That's a particular danger zone for a company to get to once you reach a point where you can't build anything new and you're just fighting to keep the old stuff alive, that's not good [laughs] because fighting the old stuff to keep it alive generally doesn't get better all by itself. At some point, you reach a tipping point where — 
**Georgina:** We see that the first immediate action is just increasing capacity by adding more developers, which is definitely not the solution. For example, if you increase the capacity of the team, but still, as an example, deploy once a week. You never really know what's going on with your software and how valuable it is. You're not solving the problem, you're still creating more basal cost.
**James:** I would argue that most of the clients I've dealt with over the past 20 years would be delighted with once a week, to be honest.
**Georgina:**[laughs] True, true, true. You're right, but not very frequently I'd say.
[laughter]
**Birgitta:** Then what can you do to avoid that state of only repairing cells and not [chuckles] creating new ones anymore?
**Georgina:** I think we can exit this metaphor now because at least now in human biology — [laughter] and mammals' biology, we can live forever, at least until today. For example, we can reduce basal costs by first keeping it in mind, understanding that when we propose a feature and we start building it, it's going to be there for us like a backpack in our bag, let's say. There are multiple techniques. I'll start with the basics, for example, just introducing some Extreme Programming techniques into your software development process outside in NTBD where you just build exactly what you need to build for this use case.
Also, for example, accepted criteria for different types of product development. For example, if you're going to build something that you want to put in production right away, make sure that it's done in a way where it's irreversible, easily changed, easily maintained in a sense, and in the most simplest way. Whereas for example, if you're doing spikes and something that you don't really care about adding so much value just yet, maybe your acceptance criteria will be lower and that's okay. To find these different ways of working, you can't build everything the same way. This is something I can think of off the top of my head for now.
**James:** I'm nodding frantically in the background, obviously you can't see that but I could pass one more XP practices, pairing, refactoring, red, green, refactor, all those sorts of loops, the simple things that you can do to keep your code as simple as possible and most simple.
**Birgitta:** Can you be a bit more explicit, how those practices affect the things we are talking about before?
**Georgina:** For example, let's take the sole thing of deployment frequency for example, and getting to see how much value your feature is adding as soon as possible will help you build less things or at least will avoid you from building things that are adding zero value and then you just have to throw away or refactor forever. Then pairing of course TDD — outside-in TDD specifically — because it drags you to only build the smallest use case and the code just necessary for building the small use case and in a way that it is refactorable so that's also important.
Then, of course, product has to be very close to that. By product I mean the product development team, the product owner as well. The business need to understand that we need quick feedback, we need not hiding software under feature flags for months, for example, because this adds to the basal cost. One very nice technique is when you enter a company and you see, "Okay, how much code is not adding any value to the end user, how much code is hidden under feature flags, how much code is running on a way that is not sufficient?" You start eliminating those points and then you think about "How I'm going to build new ways."
**James Lewis:** I can never remember who the quote is from. It's either Dan North or Martin or Jez Humble or Dave Farley. It's one of those gang.
**Neal Ford:** All quotable people.
**James Lewis:** All quotable people. I really like the idea of, in relation, actually, to this metaphor.
**Neal:** Maybe it was Kent Beck…
[laughter]
**James:** Maybe it was Kent Beck! Okay sorry, they've all quoted Kent Beck! I really like that in relation to this metaphor as well, because what we say if we want to get fitter if we want to try and help ourselves with our bodies and make our bodies fitter and more healthy, then you do exercise, you eat good food and sometimes exercise — especially when you start — I took up running during the pandemic, during the lockdowns, and that really hurts. But I did it a bit more, and I did it a bit more, and finally, it didn't hurt so much. I think that's definitely true here with these practices: if it hurts, do it more!
**Birgitta:** They require discipline, right? A lot of this stuff is discipline. Then that's like, yeah, having an annoying trainer that tells you to go on and on and on.
**Georgina:** Besides discipline, Extreme Programming also says a lot like courage. The team has to have _courage_ to push for those practices, not be afraid to delete code, not be afraid to hang on to codes that maybe they will need at some moment. Also be very close to risk, a sense of safe risk, in a sense.
I hear a lot of the practices that help create basal costs are practices avoided because people are afraid: “what will happen if I deploy this and I break production and I don't know how to do it safely?" or, "What if I write the test first, and that takes me so much time?" Even if you don't write the test first, then you're going to end up taking the same time as if you're writing the test first. These kind of things require courage. Of course, you don't have to change the whole organization or the whole company but a small team can start.
**Neal:** A famous dysfunctional quote was, "we don't have time to write tests, we're spending too much time debugging."
[laughter]
**James:** Probably.
**Birgitta:** I mean, it's all about — a lot of the things that you were saying Georgina and that's what Eduardo Ferro answers blog posts on as well, the simplicity, the art of maximizing the amount of work not done from the Agile Manifesto. I was also just reminded of the seven wastes of software development. I don't know if y'all know this from Mary and Tom Poppendieck. An analogy to the seven wastes of lean manufacturing. One of those is also the amount of work not done. That was what you were talking about as well, all the code that you actually don't have in production yet.
**Neal:** Well, I think he actually shortchanged the metaphor because he was mostly talking about cognitive load. There are at least two other aspects of this metaphor that I think are really interesting. One of them is exactly what James just talked about, which is fitness. I always heard the term bit rot, but Wikipedia calls it system rot. It's this assumption, the assumption that as you get older, something degrades automatically.
A lot of people just believe that if you look at a 20-year-old piece of software it must be terrible inside. A lot of that is just because they haven't had good fitness around things like cyclomatic complexity and other things that are governable by fitness functions and metrics and other sorts of things that you can do. Not just from a domain standpoint that he's mostly focused on, but also from an architecture and a technical standpoint, to make sure that you don't eat twinkies everyday, to push the metaphor a little bit from an architectural standpoint, but you eat vegetables.
**James:** I also remember I was asked to take a look at the code base for a prospective client that shall remain very nameless in this case. It was interesting. It was a pretty old piece of software, maybe 10 years old, it was an old Java web app. It was pretty core to their business. They asked us to take a look and help them understand whether they should refactor it, whether they should rewrite, whether they should break it out into bits and rewrite different options. We took a look at this codebase and we ran the usual sets of tests of cyclomatic complexity and the dependency matrices and all these kinds of things. We had some good news and some bad news. The good news is it's cohesive; the bad news it's all of it that's cohesive, all two and a half million lines.
**Neal:** Cohesive like a big ball of mud!
**James:** Exactly. Yes, it's not very coupled, because it's all cohesive. Then we came across this one class, and it has recounted 60 if-else statements. I was chatting with Dan North about this, and he said, "Well, of course, what else you're going to do?" because you get to the point of the maintenance cycle, where you've got 45 if clauses. You're not going to change it, you'll just add another one.
I think that brings us on to something else we were talking about, which is the overhead of once something is quite done what happens in maintenance mode? Is there space, is there budget for people to make changes in the way it was, whilst it was under active development?
**Neal:** Well, I think that's why — to your point earlier — you should treat software like a living thing. It's not done, it's still growing. There's still metabolism going inside whether you want it to or not. That's the other interesting aspect of this basal metabolism idea is the run cost. I think that's becoming a lot more apparent to people because they're having to spend for cloud resources as they use them rather than upfront.
There's an ongoing cost to running software that I don't know if a lot of companies have a completely good handle on. I mean, maybe a little more 20 years ago, when budgeting was clear, but I think it's getting fuzzier and fuzzier for people as to _what does it actually cost to get this functionality out to market? What is it costing me? What's the bottom line on this discrete piece of functionality?_
**Birgitta:** You also, James, just started touching on _how do you measure it?_ How do you measure the fitness is, of course, one of Neal's favorite topics as well. [chuckles] “What is your current state of this basal cost of software?” You mentioned cyclomatic complexity and stuff like that. What would you all say are other things how to measure how well you're doing in that area?
**James:** I've been extending the biological metaphor further in different directions. I've been using four key metrics actually, as an example of metrics you can use to get a sense of how healthy you are.
**Birgitta:** The DORA metrics?
**James:** The DORA metrics. Yes, so, obviously they’re the five key metrics now. The idea that if you go to your doctor you feel you're not quite right, or you go for a checkup, and they'll take your blood pressure, they take your pulse, they take your temperature, or maybe looking at your eyes, will look in your ear, whatever it is they do. They'll be able to see if something's wrong, maybe not what it is, but they'll be able to give you a general idea of your health. I think that's the same for the five key metrics, they'll give you a general idea of how fit you are, then you can work using all the techniques we've already talked about to improve those metrics.
**Birgitta:** They measure your delivery performance. If your medium and long-term delivery performance is good, you cannot actually do that if your basal cost is just piling up, piling up, piling up, right?
**James:** Yes, I would expect actually, going into the metaphor further, if an animal suddenly develops a cancer, then that will be reflected in actually their basal metabolic rate because it's going to shoot up because you've got all these cells — which is why people lose lots of weight and things. You could see the same thing, essentially, by monitoring the four key metrics. If something suddenly takes a dive, if suddenly, there's not enough investment made in particular areas or there's big issues, you lose team members, there's too much churn, then you're going to see these things reflected in your time to market, your error rates or this delivery.
**Georgina:** The other way to very empirically describe this is, look at how much your team is doing support. Do you suddenly have to have a couple of pairs of teams just to support the basic feature? Or how many months of refactoring we have to do on certain systems? So yes, that will reflect on the deployment frequency, will reflect on a lot of things, but just empirically we look at how much people complain about support they need to do.
**Birgitta:** Onboarding time is also a metric I think that is often overlooked. How long does it take somebody to be productive on the team, right? Because that then represents the cognitive load all the things they need to learn to be able to push a commit to production?
**James:** Seeing as we've got the guru, software architecture, author extraordinaire in the room... I wonder whether you could comment, Neal, on how you feel the software architecture and the _large_. We've been talking about much the small here; what about in the large, how that affects this?
**Neal:** Well, certainly, if you look at integration architecture or enterprise architecture, a lot of those things affect the healthy organization. There's a lot of dysfunction between the application architecture and enterprise architecture because application architects are very tactical, they have to be because they're shipping code. Enterprise architects are often very strategic and very in the clouds and thinking; it's hard to reconcile those things. If you look at any of the frameworks that supposedly monitor the health of the enterprise as a whole, they're mostly awful.
It's just layers of bureaucracy that they've added instead of feedback loops. That's one of the great lessons of software as you replace bureaucracy with feedback loops. I think that goes back to what we're saying earlier: we can give people generic advice, but generic advice in software is problematic and in software architecture in particular because nobody has a generic architecture. Everybody has a very specific architecture. I think it's really important to figure out what beyond the four key metrics what are the indicators of health in your organization because — We'll just torture this metaphor until it just screams [laughter] — if you are a professional athlete, you have a way different medical profile than someone who is a desk worker and your doctor is going to take that into account. And in the same way, when you evaluate your architecture, a lot of companies, we talked about web scale envy for a while; a lot of companies think, oh, we need to scale like Amazon. No, you don't, you're not Amazon! And you're wasting a lot of time and effort and a lot of energy, it's just like somebody, a weekend warrior going and trying to weightlift all the weight. Well, you're spending a lot of energy for that, but not getting much value out of it. So I think that's —
**James:** Probably damaging yourself as well.
**Neal:** Potentially damaging yourself and over-prioritizing something at the great expense of something else. I think the key thing is: understand what the basal cost of your system is and what do you need to optimize and what can be optimized. This is a great time to reevaluate that if you are, in fact, moving some things from on-prem onto the cloud, and start thinking about what was the run cost of that, and what is the run cost of this?
One of the things that came up in our meeting yesterday was a lot of people seem to think that moving to the cloud is some kind of cost savings measure. Very often it's not at all; but how are you going to know that if you don't know what your run cost was — the basal metabolism of your existing system was before you move it to life support on a cloud.
**Birgitta:** I would also say, I think the run costs are something that is quite intuitive or quite transparent to a lot of people. Oh yes, sure, I have to run this so that costs money, but this _other_ part that we talked about, like the developer cognitive load, all of those things — often people (other than the developers) don't see that as actual cost. I think that's also the first step: have more awareness of that. The typical example would be an organization that works more in a project mode, like change requests after change requests — done, we move on, done, we move on. That's often not considered there.
Then you move into a team that is a product team and that also does all of this maintenance and all of that. Then suddenly, maybe the product owner is like, "Oh, wait a second. There's these two people now who actually have to respond to tickets, but I always have them for my feature work but that actually makes it transparent. This cost is there, regardless of if you see it or not. The first step I think is to make it visible and make everybody aware.
**Neal:** Well, and exactly that point: I saw a quote recently that said, "Your current state is the results of your current habits." That's true for organizations as well. I worked with a company not too long ago that was constantly battling support tickets to the point where at some point they looked around and said, there's a huge cost. So they reprioritized that and started getting development teams involved in that to get to root cause analysis — so they got really obsessed with that. After some intense effort for a little bit of time, the number of support teams went way down because they fixed the root cause rather than just constantly battling the same thing.
I think a lot of companies end up getting on a weird hamster treadmill of doing the same thing over and over again. My friend Venkat Subramaniam tells this great story where he was working on something and he fixed a bug that was like, "Oh, this is a weird bug," and then somebody called and complained. He said, "Well, one of my jobs every day is to print the stacks report and I couldn't print it today;" and said, "Oh, we broke something." He went and looked and what this guy had been printing out every single day and putting in a filing cabinet was a stack trace, because he'd been trying to go to this page and had created a Java stack trace of about 20 pages. The stacks report because it said stack right on the top of it and they had a filing cabinet full of sh–...
He had just been doing that every day because he didn't know why-- he goes like, "That's the stack report. That's one of the reports that I create every day." Just looking at the weird little overhead things like that I think is always valuable as an organization, if you can find them. The problem is finding those things. And that's actually, I think, one of the weird benefits of the out-of-town consultant effect, which is that if you rode in an airplane to get to a meeting, you have more credibility than the people who rode in a car to get to the same meeting.
Part of that's true because you can come in and notice things like that, that you become snow blind to in an organization — because it's just always been that way — and so point out. That's the advice I give people is try to be your own out-of-town consultant, go try to look at all these processes and all these things that you're doing and ask, "Is that really a smart thing or is that just something that's been grown up over time and we're just doing?" I think that's an overhead that a lot of companies endure without thinking about too much, that would be low-hanging fruit.
**Birgitta:** Then maximize the amount of code _not written_.
**Georgina:** Yes. Or wait until the last minute or until you need it. Also, what you talked about Neal reminds me of Conway’s law and how it's easier to see the impact of the way the business works into how the software is designed when you're from the outside. It's very difficult to pinpoint those things when you're inside the system. I think that's maybe a weird way, but interesting to see how the basal cost of the software is there because of the way the organization communicates and interacts and whether it's acceptable, for example, if the whole company works in this mode of fix, fix, fix, fix then it's no big deal for the tech department as well, because this is the way we do things.
We saw this very specifically on companies that were not technically tech companies initially; they're, I don't know, fashion companies or retail companies, but suddenly — especially post COVID — they have to become tech companies because their business is based on technical solutions now. Getting to the end user is very important and they try to implement the same techniques that you get a design of a t-shirt out to production in two weeks and that's it then the t-shirt is sold and goodbye with it, and okay, this is how our tech organization is going to work as well. [chuckles] It's definitely not the best way do that and it's very hard for this cultural change to happen.
**James:** Coming back to what you were saying a minute ago, you're saying about keep it — minimize the art of work not done. I think it does come down to simplicity a lot of the advice around this, doesn't it? It comes down to doing the simple things. I think we talked a bit about XP practices.
**Georgina:** Small six steps.
**James:** Yes, refactor, but also just simple project management stuff, like don't ramp your team too quickly, make sure you're onboarding is taken care of, understand the effect of experience on codebases and things. Don't expect too much from too junior a team. All these different things that I think sometimes get lost in the wider picture. 
How often do you hear people say, "Oh, we need more people, really fast; we’ll add 10 people, brilliant." It's only 10, it's not 30, it’s not mythical man-month territory; still, 10 people at once is way, way too many! You can have a disaster.
**Georgina:** I think this comes to a hard point where we see a lot of companies are being pushed to innovate lately and there's a lot of competition. And, especially old school companies, they need to innovate in some sense, they need to move to this digital transformation age. Whereas the non-tech department, let's say if the business will always think that more people will create more efficiency and this is hard for the tech folks to manage. Because at the end of the day, the developer just get requests, but then their manager gets more requests and then their manager doesn't understand why something has to be maintained and why something needs support and why can't we build this new thing just right away. And the answer in most cases is put more teams just write more software — create more basal costs in the end.
**Birgitta:** Efficiency is not even the thing you should strive for, but effectiveness right?
**Georgina:** Yes, and value, of course: are you building something that's valuable in the end?
**James:** I'd question that, actually. I think that you can strive for efficiency, but not necessarily cost efficiency. I think you should start for flow efficiency.
**Birgitta:** Yes, It's often like a misunderstanding of what efficiency should be in software development.
**James:** Yeah — I don't know any CFO who doesn't want efficiency…
**Birgitta:** Yes, it shouldn't be constant 95% team utilization.
**James:** Exactly! That's absolutely the wrong metric.
**Birgitta:** Yes.
**Georgina:** Which reminds me of the slack time in teams in general, where you measure the capacity of the team and you pull out the next part, what the team is expected to do or the next sprint, and you literally put 100% capacity. And it's like, there's no slack time there for the team to even touch any previous refactor to think about what are they doing, whether it makes sense. I think that's another way to help in minimize basal costs, always consider slack time inside a capacity office.
**Birgitta:** Yes, exactly.
**James:** I'm obsessed at the moment with complex adaptive systems, complexity science, and one of the things about capacity is if you reframe it as if you have a motorway, or like a highway, if you entirely fill the highway up with car, if you entirely — bumper to bumper — and then said go, how fast do you think the cars will go? The answer is not pretty fast. 
[laughter]
**Neal:** All right, fantastic. Well, thanks very much. It's a great overview from multiple perspectives on the basal cost of software. Thanks very much our two guests.
**James:** Lovely to be here. Thanks.
**Neal:** Thanks from us. Hope you enjoyed the podcast and we'll see you next time.
**[Music]**
**[END OF AUDIO]**
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
[ Explore Technology Radar ](https://www.thoughtworks.com/radar)