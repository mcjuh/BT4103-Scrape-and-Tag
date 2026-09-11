<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/measuring-what-matters-in-the-age-of-ai | Title: Measuring what matters in the age of AI | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Measuring what matters in the age of AI 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Abi Noda and Chris Westerhold
September 16, 2025 | 27 min 34 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/measuring-what-matters-in-the-age-of-ai#transcript)
Listen on these platforms
## Brief summary
Many engineering leaders are eager to embrace AI, but few have a clear way to measure what’s working. In this episode, we dig into how teams can track AI adoption, assess the real impact of AI tools and agents, and make smarter decisions about where to invest. You’ll hear from Abi Noda, CEO and Co-founder at DX, and Chris Westerhold, Global Practice Director at Thoughtworks, as they share how leading engineering orgs are turning AI hype into measurable value.
### **Episode highlights**
  * Abi emphasizes that measuring developer productivity is challenging and requires a combination of perceptual metrics (e.g., how developers feel about their work) and objective metrics (e.g., throughput and output). This more balanced approach provides a fuller picture of productivity and avoids over-reliance on vanity metrics.
  * Abi highlights the importance of using a "basket" of metrics that capture different dimensions of productivity. This ensures that optimizing one aspect, such as speed, does not come at the expense of another, like quality.
  * Chris explains the need for both leading indicators and lagging indicators. He describes leading indicators as the "why" behind productivity issues, while lagging indicators act as a report card. Both are essential for driving meaningful change.
  * Abi noted that while AI is a promising accelerator for software development, its benefits are often outweighed by inefficiencies and bottlenecks in the software development lifecycle (SDLC). Organizations need to focus on deploying AI tools effectively and ensuring developers have the AI literacy to use them meaningfully.
  * Chris points out that many organizations mistakenly focus on technology solutions when addressing productivity issues, rather than addressing people and process challenges. He argues that better processes and treating people well often have a greater impact than introducing new tools.
  * Both Abi and Chris stressed the importance of implementing metrics collaboratively with teams, rather than imposing them. 
  * Chris highlighted tools like Value Stream Mapping and Lean Value Trees as powerful methods for identifying inefficiencies and aligning metrics with long-term strategic goals. 
  * On the topic of AI, Abi and Chris discussed how the introduction of AI tools is changing the art of software development. Abi noted that new metrics are needed to measure AI’s impact, such as how much work is offloaded to AI and how quality is assessed in the AI paradigm. Chris added that metrics like incident response time and meantime to recovery are becoming increasingly important as organizations adopt AI.


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
### Transcript 
[00:00:00] Kimberly Boyd: Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. I'm Kimberly Boyd, and I'm joined by Abi Noda, CEO and co-founder at DX, and Chris Westerhold, Global Practice Director at Thoughtworks. We know that many organizations struggle to define which engineering metrics actually matter. In this episode, we'll explore what to measure and why, and also discuss how you can go beyond vanity metrics to discover what drives meaningful change within your engineering teams.
This is also a timely episode as DX has just launched their new AI measurement framework, which measures agents and coding assistants. I'm very excited to learn more about that later on. Welcome, Abi and Chris, to Pragmatism in Practice. Great to have you here today. First, it'd be great if you could both introduce yourselves and tell us a bit more about your background and roles for our listeners.
[00:00:49] Chris Westerhold: Thank you, Abi. I appreciate it. Thank you for having us, Kimberly. I really appreciate it. Chris Westerhold, Global Practice Director here at Thoughtworks. I am our global offering owner for our AI-first Software Engineering Transformation offering, which includes engineering insights and good platform engineering, and developer platforms. Just like how do you start to get all of that going?
To me, one of the biggest pieces of that is the metrics behind it. If you can't understand where you are and where you're trying to get to, it's really hard to be able to truly make meaningful and realizable change. At Thoughtworks for four and a half years or so. Been in the industry for over 15 years, something like that now. Again, thank you for having me.
[00:01:28] Kimberly: Great. Thank you, Chris. Abi?
[00:01:30] Abi Noda: Kimberly, Chris, thanks for having me on this discussion. Abi Noda, co-founder and CEO of DX. DX is a platform for helping companies measure and optimize their developer productivity today in a world where the landscape of software development is radically changing with the introduction and advent of AI. We really sit front row to hundreds of organizations that are navigating this shift and using data to help make better decisions on how to leverage and deploy AI across their businesses. I'm sure we'll talk about that and much more today, but thanks again for having me.
[00:02:02] Kimberly: Great. Thank you both. Like you just said, Abi, I think there's plenty we can get stuck into in today's conversation, but maybe we can start here first. Metrics. Everyone's measuring a multitude of things. It feels like they're increasing every day. People often say, "What gets measured is what matters." We also know, on the flip side of anything that is data-driven, that there can be a lot of vanity and not a lot of meaning behind those metrics.
What's your advice as someone who's thinking, believing, breathing this on a regular basis for identifying and shifting focus to metrics that really do matter when it comes to software development, especially when you're starting to think about the impact of AI tools and agents that are coming into play?
[00:02:47] Abi: First of all, we have to acknowledge that measuring developer productivity, really measuring knowledge worker productivity in general, is a really hard problem. Folks have been trying to do this for many years, since the advent of software development, and most efforts that try to do this often fail because it's really difficult to do. At DX, we've done a lot of research into the problem over the years, partnered with a lot of companies on how do we tackle this problem. Some of the things that we've learned along the way are really principles.
Not so much here the specific metrics you need to use, but what are the key principles for how to think about this problem? A few I would share today would be, one, this idea that productivity can't be boiled down to just a single number. It's not just lines of code. It's not just number of pull requests. It's not just even developer satisfaction. It's really important to use a basket of different metrics that capture different dimensions of productivity, and ultimately counterbalance one another so that you're not optimizing one aspect of productivity, like speed, at the expense of another, like quality.
The other really important principle is combining both perceptual and objective data. For a long time in our industry, efforts to measure productivity have principally focused on measuring development activity. How fast are developers typing? How much code are they producing? How many changes are we shipping? That sort of data is really important for understanding the throughput and output of the software delivery process.
Over the past few years, there's been a lot of research and increased attention on also the perceptual side. How do developers feel about the development process? Do developers feel productive? How much time do developers spend in a state of flow? By again, balancing these perceptual metrics with objective metrics, you ultimately get a much more fuller picture of how productivity is going in your organization.
[00:04:37] Kimberly: I think two questions I had, listening to what you were just sharing, is that basket that you talked about, and there's multiple dimensions to consider, as well as the perceptual and the objective-based, does that mix differ and look different company to company, or are you advocating that everyone should have a very similar dimension mix and a similar balance between perceptual and objective?
[00:05:00] Abi: I think, DX, we've put out research-based frameworks to help organizations, at least, have a starting point. We published a framework called the DX Core 4, which focuses on overall engineering productivity measurement. Then, more recently, as you mentioned, the AI measurement framework. These aren't meant to be necessarily applied wholesale at organizations.
I think productivity is particular, based on the type of software development and the type of work you're doing, and the context, and really what you're trying to focus on and improve in your organization. I will say that organizations don't necessarily need to reinvent the wheel, start from scratch when they're trying to tackle this problem. Organizations do need to be also adapting the research and best practices out there to their own context and not just taking things off the shelf wholesale.
[00:05:46] Chris: I think there's a couple of interesting things to layer in there. There's leading indicators and there's lagging indicators. I think the Core 4 is a really good lagging indicator, and it's your report card at the end of the day. Whether you have an A, a B, or a C, or a D, that's interesting. It's going to help you understand where you are, but it's not going to tell you what the problem is. One of the things I see people struggle with is they're like, "Yes, I want my scorecard to be better." And like, "You just need you to be faster," or whatever.
Really, those leading indicators that waste and friction, and all the things that people deal with, that's the reason why you have to have both of them to really be successful. If you're just looking at waste and friction, it's like, yes, they're dealing with some of these problems, but then what does it look like? It's the combination of those that's really where the power comes in to be able to truly move your organization forward.
[00:06:36] Kimberly: You both are working with organizations on this exact topic all the time. Where do you see engineering teams most often fall down on the balance of those leading and lagging? Is it folks are mainly focused on the lagging today and forget about the leading or vice versa?
[00:06:52] Abi: I think it's both. This really is a hard problem. I think we see organizations have trouble just at the beginning, coming to a shared definition of what even is productivity, and high level, how do we think about measuring it? That's one of the problems we aim to solve with the Core 4 was at least here's a conceptual model for how to think about this problem to get your journey started.
To your question, Kimberly, I think, again, we see both problems. Sometimes, it's very tactically focused on, "Hey, what are the metrics that teams should be using every day?" Then it's disconnected from the business, and what are we really trying to accomplish? What does productivity really mean for the business? Then, we definitely see the opposite problem where the business and leadership is spending a lot of time zeroing in on how they're going to score and benchmark the organization. Then, when it gets time to, "Okay. Then, how do we operationalize this with teams?" it's a whole nother problem, and organizations don't always have the answer to that. I see it happen both ways.
[00:07:47] Chris: I think a lot of it has to do with their maturity overall. The less mature an engineering organization is, the more valuable some of the lagging indicators can be of like, "Hey, just tell me where I am." I have plenty of leaders, just like, "I want to benchmark. Where am I across these different aspects of software engineering?" If you're at a pretty low level of maturity, that can be really valuable.
One of the clients told me the other day, he's like, "I know my organization is a train wreck. I don't need you to come tell me that this is a train wreck. I just need to understand where am I so that I can even begin to think about how do I actually make this better?" That's where the balance comes in that Abi was talking about. You have to have both, and you have to really understand when to focus on one and when to bring in the other, so that you can truly drive then the change in a meaningful way that doesn't have a serious impact on your culture or the other negative things that can come from doing metrics wrong.
[00:08:42] Kimberly: To that point, say you're an organization and you know you're that train wreck that you just mentioned, but where do folks then begin on setting the train car right and trying to put it back on the track in this process?
[00:08:55] Chris: You can always break these down into people problems, process problems, and technology problems. We as technologists tend to always want to focus on the technology problems. "Oh, if I just went and got this other tool, if I just made another framework to replace all of these frameworks, we would just be better off." Very rarely is it that you ever actually need more technology. It's almost you need less technology, and you need better process, and you need to treat your people well.
If I were to show up tomorrow with a pure AI agentic developer platform, just with the best of everything, do your people actually have the AI literacy to be able to leverage that platform in a meaningful way, or is it going to grind your organization to a halt? Depending on who you are, both of those possibilities might happen. Bringing in all of those aspects of good metric strategy is going to help you figure out what is the thing that I need to do next. "Oh, maybe I shouldn't focus on bringing in an agentic platform. Maybe I should just do better testing. Maybe I need better CACD pipelines." A good metric strategy is the light that's going to show you the way to that, where you're not just taking swings in the dark.
[00:09:59] Abi: So many investments in technology are not data-driven. It's the hot trend of the moment. Right now, it's definitely AI. I think what we find is that data really illuminates, like Chris was saying, where the real bottlenecks are. What we're seeing across a lot of organizations right now is that AI is a really promising accelerator, but AI gains are largely still being outweighed by other inefficiencies and bottlenecks in the SDLC.
We're also seeing that, as Chris mentioned, the AI technology is not so much the limiting factor as is the ability for organizations to actually deploy these new tools to developers and get developers using them in effective ways. There's a lot you uncover when you look under the hood at the real data that ultimately provides guidance on how do we accelerate as an organization.
[00:10:47] Kimberly: Since you brought it up, I'm going to go there with the AI increasingly coming into the equation here for software development. As you see greater adoption and additional AI technologies come into this space, do you have a point of view on how you think that will impact or evolve the metrics you're looking at today?
[00:11:09] Abi: Yes. My answer to that is always some things are going to change, some things are not. What's the same is that just like before AI, we need ways of tracking and benchmarking overall organizational engineering productivity, and largely looking at how quickly can we get ideas to the customer through the SDLC and how much friction is there for our developers in the SDLC. Those things aren't changing, and in fact, we want stability in those measures so that we can actually compare pre-AI to post-AI, whether those metrics are actually improving.
What is changing, however, is that the art of software development is evolving. The way we build software is changing, and inherently, there's different things we need to be measuring and looking at to optimize these new working patterns. With the introduction of AI assistance and agents, there are new metrics, for example, understanding how much code, how much work are we actually offloading to AI, or how do we understand quality and the AI paradigm. It's different than how we think about quality of human-produced software. Again, some things are changing, some things are not, but largely, how we think about productivity holistically is the same.
[00:12:20] Kimberly: Is the bar lower or higher for quality when you're comparing the metrics for AI versus human?
[00:12:26] Abi: Should be higher, right?
[00:12:28] Kimberly: It should be. [laughs]
[00:12:28] Abi: I think that's a debate that's happening. It should be higher, but organizations are-- I think, an interesting one, for example, is code quality because we see in the data a lot of organizations are finding that the code produced by AI, while it's produced much more rapidly and efficiently, sometimes the code itself is more verbose or not as good as a human's code.
Then there's an argument to be had of whether is that a problem or not? Because ultimately, if it's going to be AI that's going to be iterating on that code, does it matter that it's more difficult for a human to understand? There's open questions still around questions like that, Kimberly, of should the bar be higher or lower? It really depends how you look at the problem.
[00:13:10] Chris: It's changed. Quality is an interesting thing, to Abi's point. There's some other interesting metrics that you need to throw into here, and this is where the metrics stuff is really evolving. If you're going to move to prompt-based software engineering, there's a lot of value to some of that. How often are you cycling back and forth with your AI chatbot? Are you going back and forth 5, 10, 15 times, writing page-long prompts to get it to do what you want it to do until you get so frustrated that you just give up? Then you just handwrite it yourself.
There's some interesting metrics you can wrap around. If you think about the incident response time, you can make a case that I think less human-readable code isn't necessarily a problem as long as it's performant. What happens when you have an incident and now you're going back 15, 20 times with an LLM to be able to get that to answer for you? Now, all of a sudden, you've extended out your incident time. Studies have shown that the more you remove yourself from that code base, you very quickly start to lose context.
Now, all of a sudden, if you have to step in, that's becoming more and more of a problem. What is the incident management? What's the meantime to recover? What are the other things that are going to indicate future tech debt problems and things that you may want to, or need to, address to make sure that you're not struggling as an organization, especially for mission-critical systems?
[00:14:36] Kimberly: Sounds like that opens a whole other can of worms for folks to consider as adoption of all this starts to really ramp up in a more meaningful way. Say I'm an engineering leader and I want to bring a more holistic basket of metrics to my team, to my organization. Where's the right place to start with that? Is it with a new team kicking off on a new piece of work? Is it possible to implement this approach on an existing team where things are already in flight? Practically speaking, where do folks start with this?
[00:15:08] Abi: Where we see it typically start is within leadership, typically at every organization, every company. Someone reporting to the CTO or closely to the CTO is tasked with figuring out productivity. That individual or that team oftentimes it's platform organization because platform organization is thinking about productivity today. It could even be someone in charge of AI transformation. Previously, it was Agile or DevOps transformation.
That individual team is often tasked with figuring this problem out. It's this individual or team that has to navigate this murky problem of, "Okay, first, how do we choose or come up with the definition, and then how do we choose the metrics? Then how do we take these metrics, implement them, and roll them out to the organization in a way where they're actually going to make a difference?" That's roughly the progression I see. Chris, what have you seen in your experience?
[00:16:00] Chris: This is where a lot of people get paralyzed, to be honest about it, because this is a really multidimensional problem, because you have business metrics and business outcome metrics. You have engineering, organization CTO-level metrics. You have team-level continuous development metrics. You have your waste and friction, the leading metrics. You have initiative-based metrics. When you think about that as a whole, how do you operationalize all of that? It becomes incredibly daunting.
You're like, "Okay, as a platform leader, I can do some of that. Oh, maybe I'll start with the DORA metrics. Maybe I'll start trying to gather some feedback from the teams of waste and friction and those kinds of things." It very quickly becomes problematic because if you're talking about business-level metrics, now you have to bring in product people. You're starting to talk about portfolio management if you're talking about initiative-based metrics, and how do you track all of those? It is a very complex problem. What you see or what I've tended to see is that people, they'll just focus on the engineering team, the continuous delivery metrics, and then the waste and friction, and the rest of it gets pushed to the side.
The problem is, the board and the C-suite is saying, "Hey, I want you to drive better productivity numbers across the organization." That's missing. I think the Core 4 has done a really great job of helping to bring some of that to light, but you have different OKRs, you have different goals, you have all of these different initiatives that are happening. It's really hard to become a data-driven organization. Where I've seen it be successful is where people have a dedicated team to make it happen, because it won't just happen by itself. I'm sure you've seen a lot of that, too, Abi.
[00:17:40] Kimberly: Yes. Just listening to all those metrics you just rattled off, Chris, it definitely sounds like there needs to be someone with a dedicated focus on that. Otherwise, I'm not sure how that would ever happen. Also thinking about Core 4, the marketer in me just wants to turn each of those metrics into superheroes and give them a personification. [laughs] Random aside, idea for your DX marketing team to think about.
One thing I do want to hone in on a little bit is, Chris, you talked about it's tech, it's people, it's process, and particularly the people piece. When you're implementing a lot of metrics, you're measuring things, that has a tremendous impact on human behavior. I guess what are some things to keep in mind when thinking about bringing these metrics into an organization, so you're promoting and encouraging the behaviors you want to see versus perhaps more negative ones?
[00:18:31] Chris: Yes, that's a great question. I can try to wrap this up into one statement. You have to do metrics with your organization, not to your organization. If you just follow that one principle, you're probably going to be okay, but you can get a lot of really bad outcomes through poor incentives. If you want me to go faster and you're going to measure me by how many PRs I put out, guess what? You're going to see an awful lot of PRs come out, and they're not going to be very useful PRs. Then what downstream impact does that have?
Now you're running more pipelines, you're running more tests, putting more pressure on all of the rest of the system. Then you're going to break a lot of other things downstream from that pressure. It's not going to be positive, like we're moving faster as an organization. What you'll actually end up seeing is you're moving slower as an organization because a lot of the stuff you're putting out is not complete, it's not well thought through, it's being done because that's what you've told me to do. It can have a very negative impact on people. We want to self-preserve.
If that's the thing you tell me to do, that's the thing I'm going to do. It's how a lot of people are going to react. If you follow that principle of doing it with you, not to you, I think you're going to be fine. One of the things I love about DX is the fact that it's an open platform. You gather lots of qualitative and quantitative information. All of that stuff is open for all to see. If you set the right culture, you're going to be able to say, "We are trying to make this better for everyone. It's not this black box, I don't know what's going on, I don't know what I'm being held to until the end of the year, when I get my performance review." That's just a very different way of looking at it.
[00:20:04] Abi: I would add to what Chris said. I think one of the most important things is how you show up to developers because when you're rolling out these types of metrics, understandably, a lot of developers and even frontline managers have concerns about how this type of data is going to be used or abused, or weaponized against them. The advice we always give is to be really deliberate about how you're communicating and positioning these types of efforts. Show up as an ally to your developers.
Ultimately, this data is there to help make the developers' lives better. It's to reduce friction and toil and enable developers to do their jobs better and ship more software to customers. Showing up as an ally to developers, positioning the metrics and the data as being in service of the developer, really important to do that proactively. Otherwise, folks get the wrong idea about what this data is for. Then that can lead to all kinds of problems that are infamous in the industry.
[00:21:01] Kimberly: Speaking of using the data for a purpose, it's not just for the sake of gathering data and gathering metrics, but maybe that you both can talk a little bit about how you can just go from data metric collection into insight, improvement, change. Are there tools? Are there practices? Maybe, Abi, you can talk a little bit about DX's AI framework and how that can really help transition from just data to improvement and insight.
[00:21:26] Abi: This is what we try to focus on with our platform. In DX, it's about not just collecting the data and displaying the data, but synthesizing the data and combining it with recommendations and insights so that everyone from executive leadership down to the frontline team and even developers have actionability from this data. The way to think about this data when synthesized in a useful way is not too dissimilar from getting an MRI or even a full-body MRI, or having Apple Health or a Fitbit and getting insights every day.
Data is ultimately informing you on how you are tracking against your goals or reference ranges and benchmarks on what is good, what is bad, and it's directing you to where you need to invest, where you need to make changes, and how you're working, where you're spending time, processes you need to improve. Again, it's ultimately up to the individual, up to leaders, up to the team, on whether or not to do anything about that insight and recommendation. The work of actually improving productivity is guided by data, but the real work happens apart from the data. It's about actually taking those recommendations and insights and doing something about it.
[00:22:33] Chris: There's two really powerful tools that I love to use in this space, and Lean Value Trees and Value Stream Mapping. Those are both very time and energy-intensive to put together. Putting together a good Value Stream Map of a path to production or team onboarding, or if you're going to be serious about it, those can take hours or days to really put together. By having the right set of data, it makes a lot of that significantly easier. It provides you with the insights to be able to ask the right questions.
If I'm doing a path to production Value Stream, and I understand the waste and friction that a lot of the organization is feeling, when you're starting to map out what that process can look like, you have the data that says, "Oh, are you struggling with this? Is this a problem? Is that a problem?" You can get to that next layer down, which is really where the efficiencies can be gained. Because you can spend a lot of time and go, "Oh, look, hey, there's this rosy point of view on how this process looks." When you have that other data, it really starts to be able to fill that in.
On the Lean Value Tree side, you have these longer-term strategic initiatives, like, what does a good developer platform look like? Am I going to bring in new AI tools? How am I thinking about technology strategy from the long run? Then on the other side, you need these developer experience initiatives. That's the other part that you can get out of there. Both of those are really important. I see a lot of organizations struggle to choose between the two of them. It's like, "Yes, that's just tech debt. I can worry about that later. Here's this shiny new strategic thing that we want to do as an organization. That looks way cooler. I want to do that."
If you think about it, you can start to put these things together and say, "Great, here's the vision and the goals and the bets and everything that I want to put together and the metrics that I want to wrap around that" to say, "Hey, this is the impact of this thing from a tech debt perspective. We just can't ignore it." You can shape it up and you can present it in a way that makes it really powerful for everybody and also helps enable autonomous teams because they now understand what are the things that they want. I think this is the anti-Goodhart's Law.
If you're going to incentivize people to do PRs, they're going to do a bunch of PRs. If you say, "Hey, these are the goals we want to hit and this is the value that I think they can provide," people are going to start to navigate towards that North Star. Holistically, when you wrap all of that together, it can really be a huge impact to your organization. That's people in process and has nothing to do with the technology side.
[00:24:56] Kimberly: Now, if I've learned anything from these podcast episodes, tech debt always works its way into a conversation, so don't ignore it, people.
[00:25:02] Chris: It has to.
[00:25:03] Kimberly: It will come back and haunt you. [laughs] I know we just have a few minutes left, and you had mentioned DORA a little earlier, so I'm just curious to pick both your brains on the upcoming DORA Report is going to be out soon for 2025. I'm curious what trends or findings you're most excited to explore in that report when it comes out.
[00:25:23] Chris: Yes, I know this year is going to be focused on AI, as most things are. There's been a lot of reports and studies and everything that have come out. This is a report that comes from the people, for the people, is what it feels like. To get a good understanding of how people are seeing this, there's this weird dichotomy right now, of there's a whole group of people saying, "Oh, my gosh, there's 10x productivity gains."
Then there's other people saying, "No, there's nothing actually." I think the answer's somewhere there in the middle, and I think the DORA Report's going to do a good job of describing what the problem is and how do we want to frame that up? Coding has never been the problem. Okay. We all know that, I think. What is the problem? I think it's going to hopefully shine a lot of light onto what that looks like.
[00:26:04] Abi: Yes, I don't really have any predictions on what's going to be in their report. In their last report, which focused a lot on AI, they had some really interesting findings around even negative impact of AI on some of the throughput and delivery metrics we would intuitively expect to be benefiting from AI. From my understanding is that this upcoming report is going to be a longitudinal study on the same core findings that they uncovered in the last report, with a lot more new findings introduced.
It'll really be interesting since so much has changed in the industry just in the past four to six months, especially around AI. It'll be really interesting to see what shows up in the report to see the state of the union as far as how is AI impacting organizations.
[00:26:47] Kimberly: Yes, absolutely. You're right, so much has changed. From year to year here, it'll be interesting to see what they have to say. Abi, Chris, thank you so much for joining us today. It was really great conversation. I think focusing on that balanced set of metrics, not doing metrics to your organization, but really making it a collaborative process, are some of the key things I'm going to take away from our conversation today.
Really fantastic having both of you here. Appreciate it. Thanks so much for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcast, or if you enjoyed the show, let us know. Share a post on LinkedIn or X and tag Thoughtworks.
[music]
[00:27:34] [END OF AUDIO]
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