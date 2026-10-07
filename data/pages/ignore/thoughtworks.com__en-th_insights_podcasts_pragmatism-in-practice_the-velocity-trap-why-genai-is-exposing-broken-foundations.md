<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/the-velocity-trap--why-genai-is-exposing-broken-foundations | Title: The velocity trap: Why genAI is exposing broken foundations | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The velocity trap: Why genAI is exposing broken foundations 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Stuart Hobbs | Podcast guest  Rob Zuber and Rickey Zachary
April 08, 2026 | 56 min 25 sec 
Listen on these platforms
## Brief summary
While 2025 was the year of shopping for AI, 2026 is the year of ROI. In this episode, Thoughtworks and CircleCI leaders discuss the 2026 State of Software Delivery Report, revealing why AI-generated code is creating bottlenecks rather than business value. Learn how elite teams are distancing themselves from laggards by rethinking compliance and testing, and why a Tiger Team approach is the fastest way to expose hidden technical debt and accelerate delivery. 
**Transcript** Stuart Hobbs: Hello, and welcome to Pragmatism in Practice, a podcast from Thoughtworks, where we share stories of practical approaches to becoming a modern digital business. I'm your host for today, Stuart Hobbs. Last year, Thoughtworks was proud to sponsor the 2025 DORA report on the state of AI-assisted software development. Over the past months, the industry has been dissecting the findings to understand how AI is amplifying engineering performance. 
Now, while the DORA report gave us some incredible survey-based findings and insights into how teams feel that they're performing, today, we're going to be looking at some hard evidence. I'm delighted to be joined by Rob Zuber, CTO of CircleCI, and my colleague Rickey Zachary, Thoughtworks head of platform engineering, to discuss CircleCI's new 2026 State of Software Delivery Report.
What makes this report particularly interesting and unique is that it's rooted in actual user data. I'm really looking forward to discussing today how the trends found in DORA's research last year are brought out by CircleCI's new insights. Before we dive in, Rob, Rickey, welcome. It would be wonderful if you could both introduce yourselves and maybe give us a quick glimpse into your first thoughts on the report's findings.
[00:01:28] Rob Zuber: Yes, thanks, Stuart. Really excited to be here. Great to see you again, Rickey. Yes, quick intro. I'm Rob Zuber, CTO of CircleCI. I've been with CircleCI a little over 11 years, so I've been thinking about software delivery for a really long time. Before that, I worked as a software engineering leader in many other places where I also thought about software delivery a lot. It's not new, but everything is new right now. It's a really fun time to be rethinking with all that context.
As far as the report, I think the thing that has stood out and that we end up talking to most people about is the spread of results, like the spectrum across which teams are finding themselves. All of the news is either highlights or averages, and that does not land with most people, right? Most people are having a much more nuanced or complicated experience trying to accelerate their business. We saw a lot of that, so looking forward to diving into it.
[00:02:33] Rickey Zachary: Great to see you again, too, Rob. As Stuart mentioned, Rickey Zachary. I lead our platform engineering practice at Thoughtworks. My day-to-day is primarily helping our enterprise clients build out engineering foundations on the platform engineering side. Those are things like CI/CD pipelines, developer platforms, internal tooling. That's really accelerating their engineering practice. AI is at the heart of that right now. As Rob mentioned, we're at this interesting inflection point where a lot of our clients are trying to do more with less, and they're hoping to capture AI within the SDLC to help accelerate some of those business outcomes.
For me, in the State of Software Delivery Report, one of the things that was interesting is I think that AI is actually having a bit of the effect that most organizations want it to have, which is creating more code. What we're starting to see is only the best organizations are taking that and aligning it to upstream and downstream processes, right? You can write more code. If your CI/CD pipelines are fragile or if your testing practice isn't as automated as it needs to be, you're not getting those results out into production to actually realize the business outcomes that you want.
I think more and more organizations are just focusing on that code generation when they're needing to spread the aperture a bit and look at some of the other upstream and downstream processes that are there. That was surprising to see. We're actually getting the results that we want, but we're not getting the overall business outcomes that most organizations are looking for. I think it's going to be interesting to have a conversation as to why that is and what some of those organizations that are succeeding are doing versus the other ones that aren't succeeding.
[00:04:21] Stuart: Fantastic. Thank you both. Right, so let's dive in. The headlines in 2026 have been all about the significant gains, but the CircleCI data tells maybe a more complicated story. We're seeing a divergence where elite teams are accelerating, but it seems like the average team is actually slowing down. Why is the hype not hitting the bottom line for everyone? Rob, maybe if I'd come to you first on this. As I said, the 2026 report highlights this performance gap. Maybe you can give us some insights into why you feel that some teams are accelerating while others are actually slowing down despite investing in AI?
[00:05:09] Rob: It's multifaceted for sure. Systems are complicated by their very nature, right? Software delivery is a system. There's a lot of pieces involved. I think the first pass is typically a discussion of theory of constraints, or where is the bottleneck in the process, and are we addressing the bottleneck? In a lot of organizations, code generation was not the bottleneck. As Rickey was mentioning, we have downstream processes that were barely keeping up with very slow code generation.
We try to accelerate one piece, and all we do is pile more work in the queue at the next stage in the process. Maybe that's fragile and breaking pipelines. Maybe it's some manual review processes that are necessary downstream. There's lots of different things that that could be. Again, that's the first pass for me. I think it's actually a little bit more complex than that.
If you look at the possibilities of super low-cost, rapid code generation, you actually can start to consider whether the process we've outlined is even the right process anymore. We put a lot of things in place in many software delivery processes, like the overall end-to-end process, because writing code is expensive. It takes time, it takes humans, et cetera. We do a lot of upfront thinking. We do a lot of early evaluation of our ideas and throw out ideas, do lots of user research and design testing, et cetera, et cetera.
Now, I could build five versions of something and just put all versions in front of a customer and pick the right one. The teams that are the best are not just really fast at each of the stages of a process, but know how to adapt their process to new capabilities. They're witnessing that everything is very, very different, and there are new possibilities that just were not open to them before, and actually adjusting the way that they think, right?
You can definitely accelerate, and you will be faster on the same process that we've already used. Again, I think the best teams, if you think about the core principles of Agile, like take yourself back to the Agile manifesto, not how that turned into whatever all-capital definition of this is how we Agile. What do we do? We talk all the time about what's working and what's not, and we adjust. That's really, for me, at the heart of those elite teams, not just their ability to tune bits of an existing process but to rethink the whole thing.
[00:07:45] Rickey: The part that you mentioned, Rob, that resonates with me and the conversations that I'm having with clients and some of those elite teams and some of those laggards a little bit is the value-stream mapping portion of that and actually being able to make that actionable. A lot of times, we go in with clients. We do a value-stream mapping, but they can't actually make some of those changes actionable, right?
They see where the friction is. Regardless if they're using AI to accelerate or not, they're not able to transform the organization, either at a process level, an operating-model level. I think the default for technology organizations, whether they think they're one or not, is we'll bring in a new tool, and that'll solve the problem. There is a lot there where you have to be able to uncover existing technical debt. That could be a bottleneck.
You have to be able to optimize what your testing strategy looks like. You need to be able to do supply chain management if you're in a highly compliant environment. There are all of these friction points that exist. I think focusing on code output alone is not a viable solution because you have all of these other parts of the value stream on the engineering side that really will either constrain your ability to move as fast as you want, or actually provide the unlock there.
I think the other thing that's really interesting that I've been noticing that was alluded to in the report, but maybe wasn't drawn out all the way, is I think a lot of organizations don't know that they're being more productive than they actually are because they're not measuring accurately. I know that we have a bit of measurement fatigue at the moment. We spent most of 2025 and 2024 talking about metrics and DORA and space and all of these things.
Having an ability to benchmark and say, "Here's where we're at now. We've introduced these AI tools. Now, we're actually productive. We have demonstrable data that shows that we're actually more productive," I think it's something that's really important because, a lot of times, we go into organizations and we say, "Actually, you all are fine. You're good. You just need to measure better."
I think those two things, in concert with each other, being able to make your plan actionable across all of those different dimensions, the process level, the operating model, and, of course, tools and engineering, is important, and then being able to measure the impact. I think I see more of the successful organizations moving in that direction, versus the ones that are just doing strategy for strategy's sake and just using individual AI tools for code generation.
[00:10:30] Rob: Yes, I think that the measurement point really lands particularly, you're seeing it, it's my conjecture. Given that 2025, I hear this a lot, 2025 was the year that we went shopping for AI tools because everyone just thought, "Well, it has to help." Then 2026 is going to be the year of, like, "Okay, what's the ROI on that?" If no one actually knows how to measure the return, then it's going to be really hard to calculate. There's two terms in ROI, and you're missing one of them.
The other thing you mentioned in there, to the point of shifting process, was compliance. Even not the most regulated industries, everyone's got some compliance concerns. They've got some security concerns. Compliance tends to be a model of, like, these are the risks in our process, and these are the controls we've put in place for those risks. A lot of those controls that people are used to have been built up over 25 years of doing software the same-ish way. I meet a lot of people who think that's the only way that you can actually do compliance is, "Well, this is what we've been doing for 20 years," or whatever.
When you fundamentally change how software gets delivered, and you have a remarkably capable new toolset, you have a real opportunity to rethink something that we might not traditionally describe as part of the SDLC. Certainly, as engineers, we like to pretend it doesn't exist or whatever. Those are the things that are going to end up being bottlenecks in your organization is, I'll say, legacy-ish, but techniques, approaches, et cetera, that have been defined for a process that's no longer the process, makes it hard to change.
[00:12:04] Rickey: I agree.
[00:12:05] Stuart: Yes, and I think we're certainly going to come on to talk a little bit more about those bottlenecks and the different potential bottlenecks. Before then, a question, Rickey, for you. You've touched on expectations. I'm interested, are you seeing boards asking for really significant, potentially 10x gains, but without necessarily realizing the technical debts or the fragmented data landscapes that are potentially standing in the way of this? Is this something that you're seeing in your work?
[00:12:44] Rickey: I wish the conversations that I was having with C-suites, the boards only expected 10x gains. [chuckles] I think that they're expecting 50 to 100x gains because that's proliferated the industry at the moment. I do think that they're not realizing that there are all of these architectural issues that could be there, legacy systems that act as boat anchors that are there to that unlock.
I think that most of the boards that I'm talking to and the C-suites that I'm talking to are expecting some strategy that allows them to get on the low end, a 10x improvement in productivity. They are not thinking about the underlying technical debt that's there. I think that part is extremely important because I've heard more and more organizations struggle with, "Hey, we've implemented this AI tool."
We actually are seeing throughput increase, but the AI code is now creating more technical debt at a much faster clip because we don't have some of those guardrails in place throughout the downstream process. I'm taking my technical debt, and I'm swapping it out for AI-generated technical debt, which is just proliferating their ability to do things. If you think about, "Hey, I've got an increase in throughput," but I have more rework.
I have more maintenance costs, I have more of these other things that I could have caught with maybe a more robust CI/CD pipeline, more checks, guardrails in place. If you don't have that, then I may be trading 10x in throughput for a negative 100x in rework, and maintenance costs, and those things, let alone the technical debt within the existing legacy estate.
I think that there is a huge disconnect and gap between the boardrooms and their expectations, and how does that translate to a potential business strategy, and then the on-the-ground implementation of that, because of all of those things that I mentioned. I also think one last thing. I think that, again, we mentioned the metrics piece that's there. Having actionable metrics and insights on those types of things, I mentioned throughput, I mentioned rework, I mentioned all of these quantitative ways to measure the impact of AI, you do have to have some visibility because we can't just go based on the vibes.
It feels like we're faster. It feels like we're more productive, being able to go back to the board and say, "Quantitatively, here's how the impact of AI has been." Regardless of my technical debt and my expectations there, it allows you to reframe some of those conversations with the board, or go back and start asking them for additional resources. "Hey, we've implemented AI. We've got 10x more throughput, but we've got all of these other parts and pieces of the value stream that's affecting our ability to actually have 10x business value on the backend."
[00:15:54] Rob: That gap can be really tough if someone's not in the space in between. I totally understand the expectation, or at least the desire, let's call it, at a board level. Apparently, there's technology out there that can help us do this better and faster, but it doesn't feel like we're getting it. I think it's the onus lands, I'm a CTO, I'll put myself in this position, on leaders to be clear about both what's realistic, what we're doing, and, to Rickey's point, an actual strategy, right?
Not just, "Hey, everybody, AI more," and everything will be amazing, but okay. As a technical leader, I should get it. I believe I do get it. These are places where we're really going to struggle. These are places where I feel like there's some opportunity. How can we fix those things? What is it about our systems that's holding us back? There's a little healthy skepticism, or at least disappointment, amongst engineering leaders that this was always holding us back.
It was holding the humans back. Now, we're sad because it's holding the computers back, but it's much more noticeable. If you're trying to go 10 times as fast, then you're putting everything in the system under a lot more pressure. My bike tire can hold 50 PSI. If I try to pump it to 500, it's going to explode, right? It's just not built for that. We're seeing that that pressure is exposing these things, but then we have to be realistic about it.
We have to create the space, and the time, and the strategy to say, "Okay, we'll go fast here, but over here, we have little work to do." Now, these tools are also great at helping us clean up those problems. Not just, "Hey, go fix the tech debt," but help me understand this, help me understand this, consolidate these two things together. Doing that work can also be accelerated. The kinds of cleanup that always got deprioritized, if we're honest, because nobody understood it, we have tools to help with that as well.
I think the point of strategy, like do we actually know how we're going to get from here to faster as opposed to be faster? The way that I always phrase that is long-term sustainable velocity or long-term sustainable throughput. Not just we were fast for a hot minute, and then we made this even bigger pile of garbage that we don't know how to work with, but we're building things that allow us to continue to be faster. I think understanding that and really splitting that difference, I think, is really important.
[00:18:26] Stuart: Indeed. We touched earlier on bottlenecks. I know that in the industry, we often talk about human bottlenecks, but I guess that the reality is more nuanced than that. Our current systems were built to keep pace with change produced by humans. Now that AI is boosting that output, it's the systems themselves, the testing and delivery processes that are failing under the pressure. Rob, it's human nature to fill in the gaps, maintain systems, manually approve changes to ensure safety. Why does this strategy fail the moment that we introduce AI into the mix?
[00:19:14] Rob: Well, a couple of things. There's the pace at which we can operate as humans is always going to be a limiter. Before AI, not before people started doing research in the '60s, but before AI was suddenly how we did software development, PR review time was the thing that everybody talked about. In every metrics tool, everyone's like, "Oh, I can't get anyone to look at this."
Even in Teams, I'll say even in Teams because I can't speak for everybody, where PRs were appropriately sized and arriving at a human-metered rate, it still took a lot of slack pings or whatever. "Can someone please take a look at this? I can't do my work until this gets reviewed." Everyone's caught in their own zone, right? It was already a problem. Then 10x, or to Rickey's point, 100x, the arrival rate, make each of them 1,000 or 2,000 lines of change, because that's really quick and easy to do.
Then put that in front of a bunch of engineers and say, "Oh, by the way, could you please review my 18 PRs that I had an agent write this weekend? I haven't looked at them, but if you could, that would be amazing." It's not particularly shocking that that hasn't gone well. I think that, yes, the systems beyond that are going to be problematic. They need to operate in different ways. I think the ceremony of PRs is probably the real question here.
Going back to the compliance thing, a lot of people have PRs as mandatory with a second reviewer because that's how we prevent security issues. Do we really? Have we had zero security issues since we introduced the pull request? I'm going to go with no. Humans aren't actually that great at this anyway. There's a point of discussion about, is this in line with the architecture and the design of the system that we are driving? If we're not answering that question until we've written all the code, that feels a little broken to begin with, right?
If what we're looking for is the quality of the work, I guess the quality of the testing, do we have coverage? Is the coverage useful? Is it mapping to the intent of what we were trying to build? We can also automate all of those things. Certainly, what we're doing internally and trying to sort out for our customers is doing that before a PR. If I know or the machine knows that this is not good enough, let me fix that before I ever put it up in front of somebody else.
Then at some point, I think that whole PR gate goes away. We model something differently to the point of changing the process because everything that requires a human in there is going to, by definition, operate at a much slower pace. We might be able to flag or pull out specific high-risk small pieces. That's what's interesting, I think, for some human intervention. The notion that we're going to do all this work at this pace and then line up a bunch of folks to just read it all, I think that's not going to last.
[00:22:27] Rickey: I would add in one thing that I'm seeing as well to that point is this interesting conversation that's across three dimensions. The whole point of adding an AI is amplifying something. Either productivity or amplifying our ability to have better throughput or better quality or better compliance, right? That amplification is a mirror of what you're already doing.
If you're already having some shaky foundations and you have struggles with PR time already, if you're going to do that as an organization and introduce AI, that foundation will just get amplified. That poorer foundation will get amplified that's there. If you already are struggling with quality and you introduce AI to produce more code, it's going to produce more code that is not following your quality standards and practices that are there.
I think if you're going to apply AI from an amplification standpoint, you should focus on maturing your foundations, making sure that you're tall enough to ride the AI ride if you're going down that path with using AI to maybe mature some of those practices and improve some of those foundational pieces. I think the second thing that we're starting to notice is that we're trying to apply some of these AI techniques, some of these machine-based techniques to human constructs that are there.
I think about Agile, and I think about a lot of the product portions of the organization that are saying, "Well, we manage all of our work in user stories and epics and features. How do I go from a spec that's supposed to be machine-readable to those things?" Well, the only reason that we really are using those traditional mechanisms is because they make it for humans to break down work and estimate work and those things.
If I can have a specification and the AI is actually doing all of that work for me and amplifying that code-generation practice, do I really need those types of constructs in an organization that is trying to get to 50x or 100x that's there? That amplification on the process side is there as well. I think that there's a third problem that's starting to come up, which is AI is making our human Band-Aids, so to speak, and processes that are stitched together a bit more invisible.
What I mean by that is that a lot of the organizations that I talk to when there's an outage, there's usually one or two people that are the go-to people that we have to bring into a room to go and figure out exactly what the outage was. I think that that's an issue with the process being broken. AI is just a Band-Aid on top of that. This is, again, amplifying some of these bad practices that are there. If we talk about, "How do we apply AI in those situations?" it would be, "Hey, before we go and do this big enterprise-wide rollout of all of these tools, let's see how we can use AI to strengthen those foundations so that when we roll it out, we are amplifying good practices."
Let's make sure that we're not compounding that problem by using some of those same, more traditional human-based practices instead of augmenting those with more machine-readable practices or trying to bridge that gap. Then I think third is, make sure that we don't have those bottlenecks there so that we can actually improve our top-line business value metrics that we want to get out of the implementation of AI.
[00:26:18] Stuart: AI as the amplifier, reinforcing the status quo, is definitely a theme that we're hearing more and more. Rickey, for example, if an organization has a disjointed data landscape, I'm assuming then that adding AI into the mix is actually then going to make the engineering process more complex rather than simpler.
[00:26:44] Rickey: Extremely complex. It's interesting, the disjointed data landscape. I've actually been thinking about this as I talk to clients in two ways. One is, I think, the more traditional way, which is, "Hey, I've got my actual data. I've got data lakes. I've got databases. I've got data warehouses. I have all of this data. Data products, a data mesh. I may have all of these things there. I want to actually build AI agents to go do business-facing or customer-facing processes."
Having a disjointed landscape in that space just means that, "Hey, I'm not going to be able to achieve some of those business results." I look at some of the clients that we have. Last year, while I was in Australia, that was trying to do customer service chatbots to help augment customer service. They just didn't have the data to support some of those workflows that were there. That disjointed landscape meant, "Hey, my outcome was I wanted to be able to improve call time, reduce call time, improve customer outcomes on customer service."
I'm not able to do that because my agents don't have access to the data, because it's so disjointed. I think in that dimension, I think more organizations are focusing in on that. I think the other thing that's starting to happen is that within the engineering ecosystem, we've traditionally had all of these very siloed portions of the organization from a data perspective, which is ServiceNow holding all of my ITSM and tickets and my CMDB. Then Wiz is over here doing some vulnerability management.
I may be using CircleCI for my CI/CD pipeline, and I'm generating telemetry from there. None of that is centralized. It's completely disjointed. It's not overtly machine-readable. If you want to start putting in agents to either optimize or operationalize some of the flows, container vulnerability management, any of those things, you have to do some work to actually centralize that, create pools of knowledge that the agents can actually read and action on instead of just thinking, "Oh, yes, we'll be able to use the same disjointed, fragmented data landscape on the engineering side to actually improve those outcomes."
We are working with a lot of our clients on, "Okay, how do we capture that information? How do we almost create a data mesh within the engineering organization so that we can start surfacing some of those things to up Rob's example of PRs and the peer review process?" If I don't have that data available to agents or to other AI-SDLC processes, how can I actually make more informed decisions, either with the human in the loop or fully autonomous? We're seeing that disjoining data strategy affect not only the business when we're trying to generate agents, but also the engineering organization as we start to try and make some of those optimizations. You have to converge those two strategies together and do the technical work to consolidate those things as well.
[00:29:54] Rob: I have a question, actually, for you, Rickey, on this because I was thinking about this the other day, and I'm curious what you're seeing. In adoption, folks trying to accelerate, none of us ever want perfect to be the enemy of good sort of thing. Data quality, as someone who's not in data but has lots of friends in data, has been the problem for as long as people have talked about data, right?
We've got to clean up this, we've got to clean up that, and then we'll finally have a good pipeline, and then we can finally do a good analysis. I think one of the things that's interesting to me about AI is that both in terms of the current LLMs, but also just how we model things in AI, is it's more statistical. Being able to say, yes, someone typed the name of this city incorrectly.
Therefore, our lead isn't mapped correctly. Therefore, we're not attributing the work to the right event or whatever. Most LLMs will figure that out. That looks pretty much like this. If we think about the actual vector math, those words look really, really similar. I'm going to just clump that in together and say, "That actually gets attributed to this event." In a way, I feel like maybe data quality isn't as big of an issue as it used to be. I'm actually curious if that's what you're seeing.
[00:31:10] Rickey: I'm seeing that as well. I think there's a threshold. I think it depends on what the outcome is. I would say that when I'm talking to healthcare and life sciences customers that might be doing clinical trials and that work, data quality might be way more important because the risk is much greater on some anomalous hallucination or something like that.
If I'm talking about other lower-risk activities, data quality has fallen a little bit lower because you're right, the LLMs do a very good job of inferring some of that data quality of getting really close and filling in some of those gaps that we had a lot of humans doing. We're doing a lot of manual or semi-manual ETL packages and doing matching and those things. The LLM does a pretty good job of doing that or acting as a facsimile for the humans that were traditionally doing that.
I think what that means is that data quality is less of a concern and the data architecture to be able to do things like, "Hey, we're going to liberate these data sources in an API-first manner. We're going to be able to connect to some of these agent flows regardless of what I think about MCPs." MCPs are in the mix a little bit there. I think it becomes more of an architectural problem and being able to compose some of those data sources together, versus the traditional model was, "Yes, we're just going to dump everything directly into Snowflake or Databricks, and then it's all data quality after that."
I think we're starting to see that shift in a lot of the conversations that we have, particularly on some of those lower-entry, pilot-based use cases that organizations are doing that are still high value. On the provability side, it could be very high-value business use cases there. I think that we are seeing that shift where it's like, "Well, as long as I get pretty close on the data quality, the LLM is going to fill out the gap for us." That is true.
[00:33:17] Rob: Yes. I think, coming back to SDLC, something I actually could talk about with some confidence. To me, it feels a little similar. I absolutely agree that people are being impacted by their lack of foundations. They should totally fix those things. The one message I wouldn't want someone to take away is we can't go faster. We can't adopt any of these things. We need an 18-month project, and we all know an 18-month project is actually an 18-year project, to make our foundation perfect, right?
I would push as hard as you can, see where it breaks, and fix that thing. Then push as hard as you can and see where it breaks and fix that thing. I think we're probably headed in that direction topically anyway. I think that "perfect is the enemy of good" theory or principle is really, really critical. Obviously, given what I do, I'm very big on foundations, but you don't have to stop everything and re-architect your foundation before you can try.
[00:34:16] Stuart: We've established right that the systems, processes, the data, disjointed data can be the problem. I think to allude to what you just said, Rob, the answer isn't necessarily setting up a whole long committee to try and find where the cracks are from many, many months. Now, I know in our previous conversations that you've both got an alternative that we can talk about, running a high-performance group that runs at AI speed to see exactly where the infrastructure fails.
Rickey, Rob, let's maybe move on to discuss this concept of the elite tiger teams, and why you both feel that this might be the fastest way to surface these hidden blockers that a traditional long-term audit might miss. Rickey, if you can, perhaps jump in here first. What is the tiger-team approach? Why do you think that running until it breaks is more effective than a traditional planning exercise?
[00:35:24] Rickey: Rob mentioned some of it right before this. What it does is a lot of organizations struggle getting started because there's a lot of either analysis paralysis, or they don't really know exactly where to start. They're trying to be a little bit too tactical in those areas. I think the other thing is that a traditional audit-based way of figuring things out. It really just tells you already what you know.
Most of the times when we're going in with a client, and we start with an assessment, they're like, "Yes, this is all great. We knew this. What should we do next?" I think taking this tiger-team approach where you're picking a new way of working and then having a team go and do some of that work, it really exposes what you don't know very quickly within an organization. It identifies the things that are breaking quite quickly.
It gives you a lot of data and feedback about how things are going to work in practice very quickly, versus a longer-running, "Hey, we're going to do all of this analysis up front, and then we're going to quickly figure out what should we do in this very structured approach." Rob mentioned it. An 18-month project actually would take 18 years from a transformation standpoint. You end up not doing everything that you wanted, but taking this very small tiger team-based approach really does all of the things that you want to do.
It uncovers the things that you want to uncover that you didn't even know. It starts to validate things that are working in practice. If you've got a very good metrics program in place, or even if you don't, you can start to set that up and start getting that data very, very quickly to create some of those things that's there. Also, I think one of the things that we're seeing more and more is that it actually creates a little bit of organizational urgency as well, where organizations will say, "Well, our tiger team is going and doing that, and they did it successfully. We got a three-month prototype or a three-month production system out of the door. How can we replicate that?"
We want the rest of the organization to really work like that. I think it does all of those things, but the one thing that I think it definitely helps is helping organizations to start small and have a high amount of impact, and then figure out how do they scale what's working from that instead of trying to do everything in one large transformation program that's there. We're seeing a lot of success.
Even when we come in and do an assessment and validate those things so that we can avoid some of those pitfalls, we immediately follow it up with, "Okay, let's start with a small tiger team that's going to pilot this new way of working." They're going to find things and stumble, and we're going to fix those in situ as we're moving forward instead of creating this large backlog of things that may or may not get done, competing priorities, all of these different things that happen in a traditional enterprise.
[00:38:31] Rob: Yes. The one thing that I would tack on that, I agree with all of that, is the agency and trust. Whatever this team is, is likely going to have very high-level support because someone's choosing to pull some people out of the organization, however it's structured, or to appoint a team and say, "Hey, you're a super high-functioning team. We want you to go figure this out for us."
We're a pretty small organization compared to who you all mostly support and work with. Even in our environment, the quality of feedback when you put out the survey to everyone in the organization, whatever, is often diminished by some combination of trust, learned helplessness, "I filled out this survey 20 times before, and no one fixed anything. Why am I filling this out again?" All of those things come into play.
When you show up and say, "Have at it, and when you flag something, we're going to go fix it," and then you do fix it, then you start to see some real momentum. People are like, "Wait. Oh, wait a second. If we don't like this, it's going to get fixed. Oh, by the way, we don't like this, this, and this." That stuff starts to surface with much richer, more real information.
Then, what we witnessed, I'd love to hear if this is what you're seeing, other teams near that team, whether we're talking cubical proximity from the '90s or Friends, are like, "Wait, why can't we work like that? I thought we just had to be not great here. I thought that was part of the job. Now, I see that it's possible," and so then that opens other people's eyes. That makes it really important who you have working in this kind of space.
Are they trusted members of the organization that people look up to and say, "Oh, wait a second. I actually really believe in how that person works, and look at what they're achieving. I want to be like them," sort of thing. There's a lot of that impact that then allows you to drive cultural change rather than, "Hey, everybody." We were talking about board-level edicts before, "Go AI." We've watched that, not just in AI fail as a change management mechanism for decades.
[00:40:46] Rickey: I agree. That network effect of, "Hey, I've got a team that's there that's adopting these new practices, and they're working in a better, more exciting, more dynamic way," that spreads across an organization, no matter how big it is. I always tell the clients and organizations that I work with that some of the folks at Google talk about how it's a techno-socio problem, a socio-technology problem. The interesting thing there is, is that I think a lot of times when we're doing these tiger teams, one thing that I like to add on when talking to organizations is the idea of building a marketing campaign almost around that, where you're actually showing, doing show and tells.
You're talking to other parts of the organization, because that does get them excited, right? It makes it from just a localized thing where, "Hey, I see over my cubicle wall, they're doing some pretty exciting stuff, too." It's an enterprise-wide initiative. Even though I'm starting with a small tiger team, it's like, "Well, if you want to find out what's going on there, look, they did this cool GitHub Copilot project, or they've created this really interesting golden path, or they're optimizing or sub-optimizing the CI/CD pipeline, and they're delivering faster and delivering more value to the business."
Having those larger go-lives or marketing campaigns around that, it spreads that network effect across the organization quite well. The tiger team is super important, but then the change management plan, as you're alluding to, Rob, is also super, super important because those traditional methods from a change management standpoint, top-down edicts or, "Hey, we've got this long transformation initiative, and everybody's going to get on board," these never work.
I've been in organizations where I'm like, "These never work. I'm just going to wait it out, and then we'll go back to the old way of working, and then I'll just be able to sit in front of my desk and knock out my code." Starting small, utilizing network effects, utilizing a marketing-based change management program for some of those internal initiatives, even if they're starting really small, extremely effective in what we've seen on an outcome and spreading some of that adoption across the entire organization.
[00:43:07] Rob: Something that you just said triggers me. We're a CI company. We think in increments. We talk a lot about foundations. Every incremental improvement that you make in your foundations, maybe discovered by this small team, is going to have an impact on everyone in the organization. Some of it is them adopting processes that now we need to get other people to adopt, but some of it is foundational stuff where it's just like, "Let's go fix this thing." The whole organization will immediately be a tiny fraction better. We all know that a tiny fraction better every day adds up exponentially.
[00:43:41] Rickey: It compounds.
[00:43:42] Rob: Yes, it compounds. Thank you. 
[00:43:45] Rob: Addition for exponents did not feel right in the moment. That compounds, right? We want that effect throughout the organization. Again, on the point of, like, "Don't let perfect be the enemy of good," every piece of improvement is a piece of improvement. That is the way that we get better. Again, going back to OG Agile, that is how we improve, is we look at what we're doing. We talk about what's working, what's not. We pick something, and we make it a little bit better. It's not, "We stop," and then we re-architect everything. Carrying that principle through the learnings that we get out of small teams experimenting is going to impact the whole organization, regardless of the size of the org. [00:44:28] Stuart: For our listeners that may be looking at and exploring, taking this approach within their own teams, can you highlight? What are the most common legacy policies or institutional habits that might bring this speed screeching to a halt so, hopefully, that they can avoid some of those walls? Rob, maybe you could touch on this.
[00:44:58] Rob: Yes, it's an interesting way of thinking about it. We've certainly talked about some examples, how we do PR review compliance and controls. I'm not saying throw your compliance out, but you're going to end up rethinking that a little bit. The way that I would really answer the question is that's the point. Don't try to avoid the wall. Run into it. Maybe wear a helmet. I don't know what the right metaphor is, but just run into the wall and say, "Cool, that was the first thing."
The thing that's going to come up is the thing that's the worst in your organization. Your organization is different from my organization. Again, I've been in the same org for over 11 years. Rickey talks to different orgs probably every day and sees a much broader spectrum. We have a lot of customers. We watch how they work. Everybody has different problems, but everybody has problems, right?
If you charge at it, you're going to find your biggest problem pretty quickly, and then the real key is fix it. "Well, that's always been like that. There's nothing we can do about it." That's when you're going to grind to a halt. If you look at it and go, "Well, that doesn't seem quite right. How did it get like this?" Doesn't really matter how it got like this, honestly. It's now preventing us from accelerating. That's our problem.
How do we fix that problem? How do we rethink that approach for the world that we're trying to envision putting ourselves in, and can we get that done? When you start changing some of those things, that's when you get the organizational momentum that's like, "Oh, wait, change is possible here." We can make a difference. Look, it's fun to run into walls. You know what I mean? It's fun to hit a thing, and then watch us fix it. That's exciting.
Running into walls day in and day out and being like, "Same wall still here, still can't get past it, can't figure out what we're going to do about it." That's not fun. That's when people start to check out and slow down and say, "Well, we're just not an org that can be good." The risk actually of itemizing, me itemizing is I would say, "Well, for me, these are the things I think about." Someone's going to go spend months fixing their PR process. It turns out they were actually great at the PR process. They're like, "Well, we heard on a podcast that we should fix the PR process." Go figure out what your problems are.
[00:47:07] Stuart: Don't preempt them. Just go for it, basically. Find out what's wrong by doing it.
[00:47:13] Rob: With some safety. Sorry. The last thing I want to look, if your problem is that you can't put stuff in production without breaking production, maybe my advice is not just throw everything into production. Keep at it. Reason about it, yes.
[00:47:25] Rickey: I agree with what you said, Rob. I actually think that that's the best way to do it is go in. Start trying to move really, really fast and figure out what's wrong and then fix it. However, I have started to see two very common points where, no matter what organization I talk to, these two keep bubbling up in addition to the two that you mentioned on the security compliance side and PR throughput that's there.
The one that it's not, I don't think any organization is struggling with right now, is actual code generation. I think GitHub Copilot and Claude Code and all of these different tools are making actual code generation much more optimized than what it was before. The LLMs will continue to get better and better, and that'll be there. The two areas that I'm starting to see bubble up more and more. One is very obvious: testing.
There's no organization that I've talked to, with maybe the exception of one or two, that is testing very well. The idea of, "Hey, I'm going to generate more code and not test well, or rely on manual testing processes and have a six-month testing cycle," is a recipe for disaster. You're going to have all of these different features and code that's just piling up on the beach like sand. I think most organizations struggle with testing.
I'm doing more and more post-AI implementation testing assessments and testing strategy engagements, and talking to clients about that because they've said, "Well, we introduced GitHub Copilot. Now, our six-month testing cycle is 12 months because we just can't coordinate that." I think one area that comes up is testing. The other area that's starting to come up more and more is the product and engineering interaction point, which is, I can create more code, but I'm not able to get more product requirements and specifications and all of these things out of the product organization to even generate more code.
That part of it is, "Okay, what is the new artifact that we should be looking at to help bridge that gap? Is it the specification? Is it something else that's completely new? Do we need to optimize that feedback loop quite a bit more, those things?" It's almost like an input and an output to the engineering process, as some of those things where it's like, "Hey, I can't get enough in to be able to make use of some of these AI techniques that we're using. I can't get enough out of the testing process to even get into production that's there."
I think that those are all of the parts and pieces that I'm seeing organizations focus on, but I do think that the biggest takeaway would be start small. Start identifying what those things are for your organization. Those might be the things, but it might be a ton of other things that are there that we've not even talked about in the short amount of time that we've been chatting.
[00:50:42] Rob: I want to riff off the product engineering thing for one sec because I've been in this business a really long time, and this is not new. Yes, again, it's exposed. It's much clearer how much overhead there can be. My favorite teams have always been the ones where product and engineering were just sitting together and talking all the time. Well, if we just write a more robust spec, then we'll get the right thing out of engineering.
Now, that's turning into, "If we just write a more robust spec, we'll get the right thing out of the LLM," kind of thing. For me, it's never worked. That feels like a fool's errand. Being really clear about what problem we're trying to solve and having engineers who care passionately about that customer problem and can adjust on the fly as they're building, and not just ignoring the PM, but rather like you really have that tight connection.
Here's some new information about the market. Great. We're going to go build this thing. That kind of fluidity to me feels like that's where teams are really going to win, as opposed to, again, I got Claude to write a bigger, more specific spec so that the engineer can read the spec and then just dump it into Claude. That doesn't feel like we're answering the right question, right?
I feel the term that's often used is "product engineers," meaning product-minded engineers. I think that approach, I think if you were an implementer waiting for all of the details from someone else, like from the engineering side, you're going to struggle in that environment. I really want to see a deep understanding of the product and of the customer from everyone involved, designer, product, engineering, everybody.
[00:52:29] Stuart: Wonderful. Well, look, thank you both. Before we wrap up, any kind of last words of wisdom or advice for our listeners before we go?
[00:52:42] Rob: If I had a new piece of advice, that would feel weird. I'm just going to say the thing. Get started. Small increments. Every increment is better. You are going to see issues in your system exposed. That's a good thing. Tackle those issues one at a time. Each thing that you fix, you're going to be a little better. Everyone's going to work a little better. It's a super exciting time to be in software delivery. I've been doing this for a really long time, and I'm having a ton of fun.
[00:53:11] Rickey: I would echo that sentiment as well. Getting started, starting on, building that tiger team, getting started. Fixing those things as they come up is extremely important. Having that tighter feedback loop, having a continuous innovation program using that to actually fix things as they come up is probably the biggest takeaway from what we've been talking about, in my opinion. Then, the only other thing that I would add is that, right now, I think where we're positioning AI, it's an amplifier.
If you've got some of those weaker foundations, it's going to amplify those weaker foundations. That's okay, because if you've got a call to action on fixing those immediately and making sure that we're able to fix those for that tiger team and then spread that incremental gain across the entire organization, extremely important. If you've already got strong foundations, AI is going to help you amplify those stronger foundations across the entire organization.
Those would be the two takeaways is to get started and know that you're going to start amplifying some of those stronger practices and weaker practices. On the weaker practice side, fix them as soon as possible. Just go and get started. Rob, I also echo your sentiment. I've been having more fun now on software delivery and writing things and engaging clients now that AI is here than at any point in my 20-or-so-year career.
[00:54:39] Stuart: Well, I think that's a super positive point to end on. Fun times ahead for everyone. Before we sign off, just a note that you can download the 2026 State of Software Delivery Report on CircleCI's website at circleci.com. Also, don't forget to check out a recent piece that Rickey has authored on his perspective on the report's findings. You can find that on thoughtworks.com. Don't forget, both Rob and Rickey will be on the ground at Google Cloud Next in the coming weeks.
We're actually hosting an executive roundtable to dive even deeper into these topics. If you're there, please come along. Don't forget to visit the Thoughtworks website for more details on this. That just leaves me to say, Rob, Rickey, my sincere thanks to you both for joining us today and sharing your insights. Thanks to you, our dear listeners, for tuning in for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcasts. If you enjoyed the show, help spread the word by rating us on your preferred podcast platform. We look forward to seeing you next time. Thank you.
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
More episodes 
Episode name 
Published 
From Ferrari to AI-powered banking: How Piergiorgio Grossi is building innovation at speed at Credem 
August 27, 2026 
Why AI alone won't modernize legacy systems 
August 13, 2026 
Designing the technology organization of the future 
July 23, 2026 
AI and the workforce: Beyond efficiency to real value creation 
April 23, 2026 
The velocity trap: Why GenAI is exposing broken foundations 
April 08, 2026 
Navigating the messy middle: A guide to real product organization transformation 
March 26, 2026 
The soul in the system: Humanizing AI Strategy 
November 24, 2025 
Measuring what matters in the age of AI 
September 16, 2025 
From bronze bullets to big impact: AI-first software delivery 
July 30, 2025 
Powering innovation: Thoughtworks’ AI journey 
April 25, 2025 
The change agent’s playbook: How to lead bold transformations 
March 26, 2025 
The ethics of data 
March 12, 2025 
The human side of data 
February 25, 2025 
The foundations of data strategy 
February 11, 2025 
European Health Data Space: The future of healthcare 
January 28, 2025 
Product innovation: Charting your own course 
January 14, 2025 
Revolutionizing data: How PAYBACK transformed with data mesh 
December 09, 2024 
Leveraging AI for legacy modernization 
October 15, 2024 
From crisis to confidence: Building reliable IT systems 
October 04, 2024 
Cross-domain collaboration: Removing barriers to data 
September 12, 2024 
Building a future-ready tech organization: Vialto's blueprint for success 
August 28, 2024 
Data modernization in action: Lessons from The Crown Estate 
August 15, 2024 
Authenticity in action: Cultivating a culture of respect 
May 15, 2024 
Beyond barriers: How AI is overcoming language barriers and driving inclusion 
April 24, 2024 
Wealth management transformation: Not just a destination 
March 27, 2024 
Future Fit Strategy: Transforming Falabella with Technology 
February 26, 2024 
How to become a truly customer-centric organization 
January 29, 2024 
Product thinking: More than just ‘product’ 
January 10, 2024 
The power of product thinking 
December 04, 2023 
From stagnation to success: Unleashing the power of technology and business transformation 
November 27, 2023 
Head & heart: The art of modern leadership 
November 06, 2023 
Tech-enabled sustainability: Closing the execution gap 
October 24, 2023 
From analog to AI: Embracing human-centered AI strategy. 
September 04, 2023 
The real cost of tech debt for your business - and how to fix it. 
April 05, 2023 
How to win the innovation challenge 
March 02, 2023 
How action shapes thought 
November 09, 2022 
Leveraging full potentials 
October 05, 2022 
Wicked intelligence 
September 08, 2022 
People and partners in modernization success 
June 27, 2022 
Backstage: Spotify's secret to developer effectiveness 
June 13, 2022 
Unlocking business value with the ITV Data Mesh playbook 
May 26, 2022 
The future of digital payments 
April 28, 2022 
Decision science to build resilient supply chains 
April 12, 2022 
The power of data and tech in the public sector 
March 23, 2022 
Accessibility for business value 
March 02, 2022 
Digital sustainability and the 2040 corporate pledge 
February 09, 2022 
Healthcare tech trends put patient at the center 
January 26, 2022 
Product thinking in the new era of cloud 
October 27, 2021 
CIO Interview: A digital mission for social impact 
September 28, 2021 
The value of creative AI 
September 14, 2021 
Data governance: The foundation of data-driven organizations 
July 28, 2021 
Technology proficiency: the new imperative for business growth 
July 15, 2021 
ABCD Model for Leadership: Drive 
June 30, 2021 
ABCD Model for Leadership: Curiosity 
June 23, 2021 
ABCD Model for Leadership: Belonging 
June 16, 2021 
ABCD Model for Leadership: Awareness 
June 09, 2021 
CX: Building a customer engagement framework 
May 27, 2021 
Data-Driven with Data Mesh 
May 13, 2021 
Green cloud optimization: Reduce your digital footprint, increase your bottom line 
April 21, 2021 
Looking Glass report: Tech trends and advice for your enterprise 
April 06, 2021 
The journey to enterprise modernization starts with value 
March 17, 2021 
Driving innovation with connected devices 
March 09, 2021 
Evolving the culture for an agile workforce 
March 02, 2021 
Moving the needle in technology leadership: Focusing on customer success 
February 15, 2021 
No-code platforms and the art of the possible 
February 03, 2021 
Resilience, curiosity and belonging: The drivers of successful change. 
January 12, 2021 
Building a strong data foundation to power tomorrow’s public healthcare services 
December 10, 2020 
Tech Concepts Every Exec Should Know 
November 19, 2020 
Building Business Resilience in the Cloud Era 
August 28, 2020 
Bridging the Gap: Bringing Technology into the Boardroom 
July 08, 2020 
Risk Management for Building Robust Organizations 
May 22, 2020 
Solving the Legacy Dilemma 
May 07, 2020 
Reimagining Value Delivery with Blockchain 
February 14, 2020 
Creating a Product Organization Within Your Business 
January 17, 2020 
The Collaboration Blind Spot 
December 13, 2019 
Creating an Online to Offline Mindset 
November 22, 2019 
Small Changes, Big Effects 
November 08, 2019 
Unlocking the Power of Customer Experience Data 
October 25, 2019 
Edge: Value-Driven Digital Transformation 
October 11, 2019 
Digital Fluency: Becoming a Modern Digital Business 
September 26, 2019 
Building Products with Purpose 
September 12, 2019 
Learning to Unlearn: Changing the Behaviors That Hold You Back 
August 29, 2019 
Harnessing Uncertainty to Survive Disruption 
August 22, 2019 
Digital Transformation: Disrupting the World of Fitness 
August 01, 2019 
Your Data Science Journey 
August 01, 2019 
The Future of Artificial Intelligence 
July 26, 2019 
## Don't miss out on the latest episodes. Subscribe today
[ Subscribe ](https://podcasts.apple.com/us/podcast/pragmatism-in-practice/id1474372829)
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