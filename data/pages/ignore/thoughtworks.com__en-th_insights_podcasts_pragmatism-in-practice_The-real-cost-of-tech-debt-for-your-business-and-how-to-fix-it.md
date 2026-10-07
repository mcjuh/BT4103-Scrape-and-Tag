<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/The-real-cost-of-tech-debt-for-your-business-and-how-to-fix-it | Title: The real cost of tech debt for your business- and how to fix it | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The real cost of tech debt for your business- and how to fix it. 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Mike Mason and Rachel Laycock
April 05, 2023 | 35 min 53 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/The-real-cost-of-tech-debt-for-your-business-and-how-to-fix-it#transcript)
Listen on these platforms
## Brief summary
Technical debt has bounced into the spotlight after major system failures hit US aviation hard, forcing executive leaders to consider their own risk. Mike Mason and Rachel Laycock, Thoughtworks’ Global Heads of Technology and Enterprise Modernization, explore why addressing tech debt matters and how doing so can benefit your bottom line. If you are a business leader seeking practical ways to strategically manage your tech debt risk, this is the podcast for you.
**Episode Highlights**
  * It's hard to see, in a very straightforward way, the impact of poor design decisions in the code.


  * There's different kinds of tech debt. Sometimes there's a deliberate decision to just do something quickly, for today, but sometimes things sneak up on you, because you could build stuff well with all the information that you have today, but then tomorrow, the business landscape could change.


  * The most critical thing, I believe, is creating visibility. To translate tech debt into the impact on the business. Metrics, both qualitative and quantitative, can help with that. 


  * You can also do value stream mapping as a technique there, where you look at the entire process of going from an idea or a business requirement all the way through to having something running in production and creating value. You can look at all of the steps there and say, "Hey, does this step really need to take this long? Why is it taking this long?" 


  * People don't intend to get into a situation where they're stuck and going slower than they want to be. Sometimes you can almost use the emotions that people are feeling as a clue.


  * look out for what I call conflicting metrics, or a metric but where two teams might disagree on how they want to improve that metric.


  * Developer experience comes from trying to enable the development teams to move faster. I also think it's a lens of bringing product thinking to the development team. Treating those teams who are building features for your business as customers.


  * Applying a product thinking approach, even for internal pieces of software, means you can think of the technical health of such a thing as part of the creation of a long-term asset.


  * There is a specific outcome, a negative outcome of not paying down that technical debt. That's what we need to get to, or it's what we need to create visibility for, and we need to do it in a way that business leaders have enough information to make a decision on


  * One of the fundamental problems we have is this huge separation between a business strategy and a technology strategy. It should be a close feedback loop.


**Podcast Transcript**
**[00:00:01] Kimberly Boyd:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. I'm your host, Kimberly Boyd, and I'm here with Rachel Laycock, Thoughtworks' Global Head of Enterprise Modernization, and Mike Mason, Thoughtworks' Global Head of Technology, to talk about one of the topics on all executives' minds today. Technical debt. Rachel, Mike, thanks so much for joining us today.
**[00:00:26] Mike Mason:** Happy to be here.
**[00:00:27] Rachel Laycock:** Yes, thank you for having us.
**[00:00:29] Kimberly** : Technical debt. I feel like it's been dominating in the news here for the past couple of months. Maybe just to get us started, both of you are experienced technology leaders, have worked with a variety of client organizations over your careers. Why is tech debt something that all business leaders, not just technology leaders, the CEOs, the CFOs of the world should care about today?
**[00:01:01] Rachel:** Sure. Tech debt, it's ultimately a metaphor. Why do we need a metaphor? It's because software is really abstract. It's hard to see, in a very straightforward way, the impact of poor design decisions in the code. Whether those decisions are somehow intentional because you were trying to get things out of the door faster, it's quite well known that startups and scaleups have a lot of technical debt, or you're moving towards tight deadlines, or-- [chuckles] Hopefully not, but maybe there's just people who are like, "It's fine, but we'll just push it. It'll be okay for now." That's not my experience of software engineers. They usually want to do the best possible job.
Sometimes it's just the software is no longer fit for purpose. The original ideas of why you designed something the way that you designed it, may have changed. Your user interactions may have changed, you may have added so many different features onto something that require different load or that have different security requirements. That now you've got this debt that doesn't necessarily, in a very obvious way, show itself to be a product feature.
That's where the challenge comes, because if you're just measuring teams or product people or even business people on the number of features or that they get out and the value that those features create for the business, what you're missing is what we call these cross-functional requirements which in the past I've called non-functional requirements around things like scalability, the performance of the system, how part of our system is. There's a whole host of them. I've lost count of how many of these cross-functional requirements there are.
10 years ago, we weren't very good at measuring that, and showing that to business leaders and saying, "Hey, if we make this decision, we're going to have issues with load. We're going to have potential security issues. We'll only be able to handle this many transactions in this time frame." Now, we have all of these measures. We call them fitness functions at Thoughtworks, which you can build into your system, and they should become part of your product measures.
Not just the features, but how resilient, basically, your product is, within the environment that it has to run. I think sometimes people almost get lost in the tech debt metaphor or analogy in that, "Okay, we'll just pay it off later." That isn't always the case. A, you might [crosstalk]-
**[00:03:37] Kimberly:** Treat it like your credit card, right? Don't just--
**[00:03:40] Rachel:** Exactly. I think it's a good metaphor, but some people are a little more reckless with their credit cards than others, and it matters who's accountable. If somebody else is paying off your credit card, choose the example of-- Say you're lucky enough to have your parents pay off your credit card, you're probably going to continue to be pretty careless. I map that to, are you holding your business and product leaders accountable for ensuring that the system continues to run in the most effective way for your business?
You don't have the catastrophic failures that we've seen quite a few of lately, and I'm sure we'll continue to see over time, because there's an incredible amount of software in the world now, and not all of it is in great condition. On top of that, there's also other metrics that you can look at. Such as, how quickly can you onboard your teams, and the attrition. We've been talking for years about how hard it is to hire great talent, and to keep great talent.
If you bring that great talent, and we've seen this many times at Thoughtworks, you bring that great talent onto a creaking system with loads of problems, and they can't do their jobs to the best of their ability, they don't want to stay. There's lots of different things that you can measure, like business metrics, basically, that you make more than just the technology team accountable for. That way, you can both create visibility of what the problems that the tech debt is or isn't causing, and collaboratively solve them.
**[00:05:10] Mike** : I think something that you said there is worth emphasizing, which is, there's different kinds of tech debt. Sometimes there's a deliberate decision to just do something quickly, for today, but sometimes things sneak up on you, because you could build stuff well with all the information that you have today, but then tomorrow, the business landscape could change. Your business strategy could change, the things that you're trying to do could change, and those changes might mean the thing that you have, the software asset, is no longer exactly what it should be or what it would have been if you had known how the future was going to pan out.
That's not anybody's fault, actually. I think that's one of the mysterious things about software, is because you can change it and use it for lots of different things, people get a bit frustrated that they have to continue to invest in it. Why is it that I have to keep pumping money into this thing? I think it's because the environment in which that software finds itself changes so often as well. If you have a changing business strategy, you need to have a changing technology strategy to keep up with that, and when you change your tech strategy, that can often mean that you have some implied technical debt there as well.
**[00:06:28] Kimberly** : What I've heard from both of you is really that best intentions when software is being built, but over time, it really can become this invisible drag on the business. What organizations need to be thinking about doing is, how do we remove that invisibility and shine a light on it? I heard you speak a bit and allude to metrics. Is that the way to really bring this problem to light and have everyone have a little bit more awareness of what potential tech debt or tech drag exist in their organizations?
**[00:07:12] Rachel** : Yes, I think it's one of the important parts of it. Obviously, it's not the only answer, and you're right. The most critical thing, I believe, is creating visibility. That's what we've missed in the past. Technical teams would be like, "Oh, we have all these problems," but they weren't able to easily translate that into the impact that that has on the business, and so they might get shooed away or [unintelligible 00:07:34] we've got to get features out of the door, we've got to do X, Y, Z. I think metrics, both qualitative and quantitative, can help with that. There's a lot of great tools and systems out there that can help you do that.
There's also metrics, like I said earlier, looking at the attrition and retention of your best talent and understanding why people leave, why people stay. I think that those are the kinds of things that it's not necessarily measurable, it's more qualitative, but you have to look across all the different axes of, sure, there's all these cross-functional requirements, there's the development teams, there's downtime of your systems, and how long it takes for them to recover. I think the DORA metrics covers some of that.
There's been a lot of advancements in the last 10 years in terms of ways that we can create visibility into the impact of the technical debt that might be in the system and how things might need to be changed not just, okay, we want to build this new feature, we want to onboard this many new customers, or what does that mean from a cross-functional requirement perspective, what does that mean from a security perspective? Not just do the absolute bare minimum, but do what's needed to be done to really continue to not only get that feature out the door, but keep that feature running long term.
**[00:09:00] Mike:** You can also do stuff like value stream mapping as a technique there, where you look at the entire process of going from an idea or a business requirement all the way through to actually having something running in production and creating value. You can look at all of the steps there and say, "Hey, does this step really need to take this long? Why is it taking this long?" Asking that question usually unearths quite a lot of tech debt, but can also unearth situations where, for example, different parts of the organization are waiting on each other the whole time, or there's some kind of bottleneck to go through a test environment.
We see that often. That you have to get into the one magical environment before you can go into production, that kind of thing. Value stream mapping can be a useful, generalized technique to look at all of those things and figure out what's the slow part.
**[00:09:53] Kimberly:** Does that work? We're talking a little bit ideal state. Like, "Here are things you should be asking and measuring." Maybe let's assume organizations haven't done that. Does it work just as well to do it retroactively as it does from setting that up from the get-go when you're creating new software? Asking those questions, establishing those metrics, and doing some sleuthing to find out the answers to them retroactively?
**[00:10:20] Mike:** Yes, I think sleuthing is a great word to describe that actually, because if I was coming into a situation as a technology leader, one of the things that I would want to figure out is what's working well, and what's not working so well in this new situation in which I find myself. Value stream mapping is a great way of doing that, and you don't have to use a big fancy name. Just poking around and asking good questions often achieves the same outcomes. Yes, you do have to keep an open mind. I think a lot of people go in with a preconceived notion of what the problem is.
You actually really need to keep more of an open mind and get the situation and also the people involved in it to tell you what the problem is. I think a lot of the time, folks have an intuitive understanding of what's not ideal about their situation. People don't intend to get into a situation where they're stuck and going slower than they want to be. Sometimes you can almost use the emotions that people are feeling as a clue.
If people are feeling frustrated, that probably means they're also feeling not very productive, which means something's getting in their way from going faster. Frustration, I think, is an emotion that we should all pay close attention to, because it means someone's trying to do a good job but things are getting in their way.
**[00:11:53] Rachel:** Yes, and also that they maybe not getting heard. It's come up so often when I've done that value stream exercises. When you get to a certain point where something, it takes a long time, and it has to go for an approval here, an approval there, and everything's manual, you start to hear that frustration in people's voices. Someone will say something like, "I've been saying this for ages and no one listens," or they might be very despondent. If you dig into that, it's because like, "I've been raising this for six months, I've been raising this for a year, I've been raising this for two years, like nothing has been done about it."
Again, like Mike said, those are things to dig into and look out for. Of course, it's definitely better to start with having great intentions, but I think we all start with great intentions, and a lot of the software is older. We've come a long way in the industry, over the last 5 to 10 years, in terms of how we can measure these things. I will say that the baselining effort is often very hard, and it can have diminishing returns, trying to get really, really accurate numbers.
I think it's good enough to have a ballpark of like, "This thing takes three days, or this thing takes three weeks. That's a long time, let's try and get that down to two days, or one day, or two weeks, or one week," because I think once you start measuring, what matters is trends over time. Are things improving in the way that you want them to for your business? I think that's another important thing. Getting that first snapshot is difficult, retroactively. You just do the best you can, with what you have, because that's really your starting baseline, and from there, you're looking at how things evolve.
**[00:13:43] Kimberly:** There's really no magic metrics formula, it's better just to get started and see what you can uncover than focusing on perhaps if it's the perfect mix. Is that fair to say?
**[00:13:57] Rachel:** I think one thing that I often use is a magic quadrant sometimes with these, of like, the impact of something versus the feasibility or ease of making a change to it. There can be things that are very high impacts, that are just going to be so difficult to improve on. We call that looking for the low hanging fruit of like something that's high impact that you can start to baseline fairly quickly or improve fairly quickly, because the other thing is, is if some of these challenges have been going on for a long time, and your technical teams are frustrated, or they're despondent, you also need to try and find some quick wins of like, "Look, we've improved this."
This testing thing that used to take three days to run now only takes two hours. That's going to help people a lot, because that's a faster feedback cycle of like, "Okay, now the test has gone through, two hours later, I can go back and see what's come up in terms of challenges or bugs or issues within the system."
**[00:14:53] Mike:** I think also you want to look out for what I call conflicting metrics, or a metric but where two teams might disagree on how they want to improve that metric. I was working with a large retail chain, and they had some metrics around conversion of shopping carts into orders. Obviously, to get the most orders through that kind of a system, you want a streamlined process, you want to make it easy for everybody to pay for their order and go from their shopping intention to actually getting revenue from them as a business.
One of the other departments was producing a company branded credit card. They wanted to put the credit card signup into the checkout process, because they wanted to get more signups. Their particular bit of the business was looking for this metric around credit card signups, but the other piece of business was looking at metrics around cart conversions. As soon as you put the credit card thing into the cart flow, you reduce the conversion rate, because it's extra friction for the customer. It doesn't matter how well you do it, it's always going to cause a little bit of a drop off.
You've got a situation there where you have two different parts of the organization disagreeing on what the right metric is, or even having conflicting metrics there. I think that's something to look out for when you start trying to measure stuff, because you get what you measure, so you got to be careful what you measure because otherwise, you can set people up against each other, or even get into situations where people are gaming metrics and stuff like that.
**[00:16:38] Kimberly:** Well, don't leave us hanging on that story. How did they resolve the conflicting metrics? [laughs] What was the resolution there?
**[00:16:46] Mike:** I don't think there was a solution, only a resolution. An agreement that this is the way that we will work together, and this is how both departments can be successful on this. There were a ton of-- I think that's another thing certainly within IT. Everybody is looking for a solution all the time, when in fact, things are not as easy as that. Sometimes you just have to create a good path forward that everybody can live with, that's not actually optimal for any one individual [crosstalk].
**[00:17:14] Kimberly** : Compromise. [laughs]
**[00:17:15] Mike:** Compromise. Exactly.
**[00:17:17] Rachel:** I think the critical thing there is that these are compromises that won't necessarily have been made in the past. Is that the issues that the technical teams were raising were not being raised in a way where it was obvious the business impact, right? There wasn't a compromise, it was always what seemed like the best business decision. As in, get this feature out this door, hit that deadline, make that change.
All of those, all their challenges, those cross-functional needs, those scalability needs, those were like second class citizens that were really not in the conversation. Then you bring all of that together, and sure, the decisions might get harder, because you've got more variables, but hopefully, you're making better decisions even if they're not perfect all round, because most decisions aren't.
**[00:18:05] Kimberly:** Amen to that. I want to bring up the topic of developer experience. I actually know we're chatting tech debt today, but in hearing you talk about just the happiness and the mood of your technical talent, your engineering teams, and how that can help you get to the source of frustration and what's creating some of this technical debt.
With developer experience exploding as such a popular topic and opportunity space in the past few years, it seems to me that tech debt should probably be a part of that discussion, or your developer experience, what you're hearing from that should feed into how you're treating your technical debt problem. Is that fair to say? Is that how you're thinking about it when you're talking about the two topics today?
**[00:18:59] Rachel:** I think developer experience, in my mind, comes from trying to enable the development teams to move faster, to achieve some of the DORA metrics that are out there, in terms of like faster time to value and faster development time. I also think it's a lens of bringing product thinking to the development team. Treating those teams who are building features for your business as customers.
In doing so, starting to create tools for them whereby they don't have to continuously rebuild the same things over and over when really, it's a cross-functional requirement that they could just build as part of the system. Then I think there's tools that have come out of that, like backstage and others. The challenge is, is it doesn't cover the full breadth of what I would say, non-value add time [chuckles] of what developers do. Just because I have a great tool for building and deploying my software faster, it's not magically going to fix the cruft in the code, and if there's a certain-- We used to call them God classes.
There'll be a class or an object in there that's hundreds and hundreds and hundreds of lines long, which is suddenly, everything's ended up in there. It's got 20 to 30 different purposes, and when you make one change to it, everybody is terrified that you updated that one file. Those developer experience tools, they're not going to solve that problem. I think there's a lot more to developer experience than the tools. The tools are never a panacea. They help a lot, they remove a lot of friction, but there is a whole host of other friction that's in there, that's associated with the technical debt that those tools are not going to solve for. You need to think about both.
**[00:20:56] Mike:** When we started talking about this years ago, I think we made some mistakes by talking about developer happiness, because in the cutthroat world of being in corporate business, corporate IT, happiness is not actually the right word to use there, but developers are actually happier when they feel productive and effective. I guess the word is useful, but really, effectiveness reducing friction, reducing frustration. The reason that people are annoyed about something is it's taking longer than they think it should. The accidental complexity of solving the task is more than the inherent complexity of it.
I'm spending 20% of my time actually solving business problems, and 80% of my time jumping through hoops, or trying to get the pieces to talk to each other, or whatever else. All these other things that, as Rachel said, were non-value add. To me, that's another reason that you should pay attention to that kind of emotional state of someone, so when they're feeling frustrated, they're not productive, that's a big warning siren that you should be trying to figure out, how can I make these people more productive, because they will be more effective, they will be happier in their jobs.
**[00:22:21] Kimberly:** Although developer less frustrated-ness is less of a catchy term than-- [laughs]
**[00:22:25] Mike:** Less pithy. Yes.
**[00:22:28] Rachel:** We used to talk a lot about clean code as well. I remember when I used to help coach and onboard new graduate developers, I used to always remind them that most code gets read way more times than it gets written. That means that that's another, not necessarily value add activity, if it's not easy to read. That's where there'll be cruft within a code base of, somebody's written it with some idiosyncrasies, or some style of coding from way back, and then somebody new comes on, never seen it before, doesn't have the context of why decisions were made. 5 to 10 years later, they look at it and they're like, "I don't understand what this is supposed to be."
Trying to understand it, trying to find out information, identifying different dependencies, maybe there's other teams involved. There is this whole host of other things, that are developers doing, that isn't just about producing that feature. To me, it's a smart business decision to remove as much friction as possible so they can increase the value add activities that they're actually doing. That's one of the things that we've been really working with our clients lately, is just, what are some of these non-value add activities, how can we measure them, and where would we get the most benefit from reducing the time spent on these non-value add activities?
**[00:23:51] Kimberly** : Speaking of the non-value add activities, for someone who is in the business and not necessarily in the technology arm of an organization, how can they be thinking about managing tech debt? Well, is it thinking about those non-value add activities? Is it something else? What levers are available for them to pull to help address this issue?
**[00:24:15] Mike:** I think one of the major things that we need to do is start thinking about things as products rather than as projects that we're working on. Something that Rachel was talking about just now reminded me of this, which is that if you have this revolving door of people who are working on a software system in a project-based mentality, they're going to do what they need to do to get that thing out the door for the project, but not be thinking about the long-term.
Whereas if you can apply more of a product thinking approach to it, even for internal pieces of software, and saying to yourself, "This is an asset that we are going to do a good job of building product features, building the product in a sustainable way for the long-term." To me, the technical health of such a thing is part of the creation of a long-term asset. We have product managers who are worrying about what features should go in this product, and who is my customer base, and how do I make this competitive in the marketplace of products?
One approach is to couple that product management person with a technical product manager, who can represent the technical health of the system and help make good trade-offs, because I think a lot of people hear us talking about tech debt, and I think folks are-- They get a bit tired of paying all this money to IT to continually fix stuff, and they don't really understand what that is. Like, "Why am I paying a million bucks for yet another database upgrade? I don't really understand what I'm getting for that money."
If you can elevate the discussion about the investments you need to do for the continued long-term technical health of a product to the same level as the product feature discussions, not that it's the same priority, just that it's in the same conversation, that can go a long way actually, to being able to make good trade-offs and say, "Hey, look, for this particular release, it's more important for us to hit the date and get the thing out the door than it is for us to be looking at this more long-term technical situation."
I know, after we've got this release out, we will have a bit more breathing room. We'll be able to prioritize this other stuff. It allows you to have this give and take within it, rather than just, from my perspective, you end up with a situation where it's always about features and never about the technical quality.
**[00:26:58] Rachel:** I think that's why people are maybe tired of the tech debt term, is that that's basically what development teams have been saying for years, is like, "We need this iteration to pay down the technical debt." That's not actually what the iteration is for. There is a specific outcome, a negative outcome of not paying down that technical debt. That's what we need to get to, or it's what we need to create visibility for, and we need to do it in a way that business leaders have enough information to make a decision on that. I like Jim Highsmith's analogy of a car, but you can use it for so many things.
If you don't take care of your house, [chuckles] a lot of other things start to go wrong. If you don't take care of your car, you don't do the oil change, a lot of things start to go wrong. In the past, 20 years ago, you might not have had the signals inside of the car to tell you that these things need doing. Now, in modern cars, you're driving around and it's almost telling you too much information. [chuckles] Like, "You need to do this, you need to do that." You're like, "Ah, okay." It's reminding you that it's been one year, and you need to take the car back to the garage.
I think that changes people's behavior, in terms of how they might look after their vehicle better. Even maybe with some of the modern technology that people are putting in their house, how they might take care of their house better. Without that, you know those things need to get done, but then there's nothing nagging you. There's nothing reminding you of the value of doing it. I think that's really what this is about, is let's stop talking about technical debt, and talking about what is the problem that this debt is creating?
Is it, A, people have to take two or three times longer to get anything done in this area of the code base because of the technical debt? Or is it that we'll only be able to handle so much load, and in order to scale even further, we're going to have to pay this much more money versus if we broke up the system better, in a way that was less monolithic, it would be a lot cheaper to create scale and really make the use of the hyperscalers? Really get the benefits that the cloud providers have been telling us you would get.
You only really get those when you modularize your system. A lot of people didn't do the modularizing of the system, you just migrate the system straight onto the cloud, and guess what? It isn't magically cheaper because you've put something huge. [chuckles] Full of debt into the cloud. That's, again, not a panacea. I think it's about, how do we really elevate what these challenges are, and maybe we are doing ourselves a disservice even talking about tech debt anymore, and saying like, "Here are some of the core problems that tech debt causes, which of one of those core problems is our first concern right now?"
**[00:29:51] Kimberly:** Can we come up with a new phrase on this podcast today for tech debt? Is it essentially elevating it to, do you want speed? Do you want performance? Do you want whatever X and Y is, and take technical debt off the table entirely?
**[00:30:11] Rachel:** I wish it was that easy. A, any developer will tell you naming things is hard, because it is. Especially when it's a global thing, and people have slightly different words for things. The other thing is that cross-functional climates alone, I think there's more than 40 of them, and that doesn't include some of the things we talked about around the frustration of your developers, how much non-value add time they're spending on work.
It's a tough one to come up with a single name for. I think tech debt is a fine proxy, but when it comes to talking to your business leaders about what actions or decisions they need to make on it, it's not the tech debt. It's the thing, or it's the challenge, the problem, the impact of that tech debt that we need to be talking about. That is a bit more-- It's going to be specific to the business, to the product. In our case, to that client.
**[00:31:08] Kimberly:** I think it comes back to what we were talking about earlier. The tech debt is the metaphor, and it's really thinking about what is causing the drag on your business, and elevating that up to what those drag levers are, and what that's impacting in terms of your ability to create the business value you desire. If there's one thing for a CEO or a CFO who has maybe perked their ear up to this problem more in the past few months than they may have lately, what's the one thing they should take away? The one thing they should be asking their technology leaders, their executive teams about technical debt?
**[00:31:57] Mike** : I would probably ask, how do we know we are investing the right amount in tackling technical debt? Not, tell me what the technical debt is, or exactly how long it's going to take to fix, but how do we know we are spending enough time and investment and effort on it so that it's not going to become one of these problems where a single system melts down and then causes some kind of cascading failure. How do I know that we, as an organization, are handling this in the right way?
**[00:32:36] Rachel:** I would build on that and say that I think sometimes organizations still see a technology strategy as an execution plan for technology. Things we need to build, things we need to buy. It goes against the definition of a strategy, which is something that you make decisions on, and that you continue to learn from. A roadmap is not a project plan. You need to hit those quarter-by-quarter points and say like, "Are we getting the results that we want? What are the challenges that are in our way?"
Elevating technical debt into that conversation of, "We haven't solved this problem from before, now it's worse, and this is the projected outcome if we continue to go down this route. Are we okay with that for now? When are we going to revisit that?" To me, this is where that harmonious business and technology strategy should really be working together. Instead of it being a business strategy and then there's a separate technology strategy, which is really just a technology execution plan that just goes ahead, and then changes are made to the business strategy, and then we just tell the technology leaders, "Hey, you need to change your strategy."
There's not a nice feedback loop that really should be in there, because for most modern businesses now, most of them are digital businesses. That technology strategy really matters. It has a huge impact on your business. You've got to make it part of the conversation, whether that's having those technology leaders in those decision-making conversations around the business strategy, whether it's rethinking how the technology strategy is presented, and when you revisit it at different milestones, who's in those conversations about how we should continue executing on this?
To me, I think that's still one of the fundamental problems, is we have this huge separation between a business strategy and a technology strategy. That's, to me, it should be a really close feedback loop.
**[00:34:35] Kimberly:** Need to get rid of those adjectives, and just have it be the strategy, and it includes both business and technology.
**[00:34:41] Rachel:** Yes, maybe that's the answer. The one word, Kim. Is, do away with business strategy, do away with technology strategy, we should all just have a business and technology strategy, put it all on one roadmap and let's see if we can have a conversation about what the different milestones mean together.
**[00:34:56] Kimberly:** Well, Rachel and Mike, thank you so much for this conversation today. I know I was educated on technical debt, and I think for those listening, don't be discouraged if you feel like you have a lot of that drag on your business, because you just need to do some sleuthing, to understand where the frustration is in your organization, to help you begin remediating that. If you get stuck, give us a call. We have got lots of folks who are familiar with how to help you sift through that.
Thanks so much for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcast, or if you enjoyed the show, help spread the word by rating us on your preferred podcast platform.
[music]
[00:35:59] [END OF AUDIO]
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
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
## Check out Thoughtworks managed services 
[ Learn more ](https://www.thoughtworks.com/en-th/what-we-do/managed-services)
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