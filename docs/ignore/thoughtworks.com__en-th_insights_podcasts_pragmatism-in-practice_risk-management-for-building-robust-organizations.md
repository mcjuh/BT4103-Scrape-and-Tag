<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/risk-management-for-building-robust-organizations | Title: Risk Management for Building Robust Organizations | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Risk Management for Building Robust Organizations 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Sam Massey | Podcast guest  Anthony O'Connell
May 22, 2020 | 32 min 11 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/risk-management-for-building-robust-organizations#transcript)
Listen on these platforms
## Brief summary
As many leaders have discovered the hard way, having the right risk management strategies in place can be the difference between success and disaster. Anthony O'Connell, Principal Consultant at Thoughtworks, discusses how risk identification and mitigation allows organizations to build resilience into their business. If you are a digital leader, wanting to create more robust services for your customers, this is the podcast for you.
**Highlights**
**We need to take a risk-based approach to failures**. There are some good tools that force you to think about or create these artificial failures. And then we ask engineers who are really good at problem-solving to think about the mechanisms by which these failures can happen? And then we can say, "How should we build more resilience along those pathways? What controls should be put in place? 
**if you can educate or train people who make the decisions on the consequences of the decisions they make and therefore the risk management processes and procedures** , then hopefully they will make better decisions.
**I think risk and risk of and security can sometimes be treated as a compliance exercise** and they don't really give much value back to the business.
**A common mistake is simply reporting risks and doing nothing with them, not actively using them to make changes** to the services or the way in which an organization does business so that we can reduce the chance of those things becoming failures and impacting people.
**There's huge opportunity. I see this and it's not just let's build a bigger system because that's not the answer.** It's not what we're trying to do. It's like saying, "Look, the car isn't fast, let's stick another engine in it." It's not like that. It’s thinking about it from a resilience point of view.
**You could also take this approach to building rapidly connecting modules or rapidly connecting systems to build new services really fast.** If you can design these systems with a risk-based approach and they can automatically scale, you can plug them end to end and just increase your capacity as required and produce a very resilient service in a very short space of time.
**I think you'll find a lot of governments, progressive ones, will do a bit of a stocktake of what systems we have and what ones didn't hold up really well in this crisis and why.** I'm hoping that's going to be one of the good outcomes of this. It's going to force us to think that way.
**The point of risk management is not to eliminate risk because you can't.** It's not possible to eliminate all risk. The point is to understand what risks you're introducing into a system by the decisions that you make such that you make the best decision you can at the time and you avoid those decisions that present an unacceptable risk that you can't back out later on.
**It's important that we move the risk based approach as far up into the design phase** so that when we're making early decisions, whether it be architectural decisions, whether they be accessibility decisions, whether they be user experience decisions, all those design decisions are the ones that are going to benefit most from a risk based approach.
**Podcast Transcript**
**Sam:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. I'm Sam Massey and I'm here with Anthony O'Connell, principal consultant at Thoughtworks. We'll be discussing risk management and how a risk based approach allows us to build more robust services.
Welcome, Anthony. Thank you so much for joining us on the Pragmatism in Practice podcast.
**Anthony:** Thank you.
**Sam:** Today we're going to be talking about risk management. Quite big topic, especially in the current climate that we're living in. But before we do that, why don't you just tell us a little bit about what you do at Thoughtworks and the types of businesses and the sectors that you work in.
**Anthony:** Sure. I might give you a little bit of background too, which might give you a bit more information about where I'm coming from with regard to risk. My position at Thoughtworks in Australia is as a principal consultant working in the advisory space. Usually what happens is I get plunked down in front of a client who says, "Stuff's not working. Business not working, please help. We have a problem here." And so it's usually fairly open ended and usually it's helping clients define the problems while understand the reasons why the problem exist. And then coming up with potential solutions we can test and learn using, good agile, lean practices. It's not really in the delivery space, but it does then overlap in the space if some of the solutions happen to be build a new process that needs a new system or needs a new tool that we need to develop moves off a legacy system. 
My background though comes from, it's an automotive, it's an engineering background. I guess when you think about automotive, you think about reliability. You think about going out in the morning, get in your car, the car starts 9.999 times out of 10 or 999 tenths out of a hundred, the car is going to start for you. There's a lot of risk analysis or risk assessment that goes into the design of the components in a car. We have very little tolerance for much less than we would have with a computer system or even a TV. We have zero tolerance for a car not working. It's an expensive thing. It is a safety thing and we expect it to start when we want to use it and we expect you to get us to where we wanted to go.
And so I spent roughly two decades, yeah, this was 20 something years in the auto industry working as an engineer, designing electronics components, electrical components, software systems for those components. And part of that was to look at the risks of failure of these systems in adverse conditions. And I mean adverse conditions, I mean when you give a car or a person buys a car, it's now in an adverse situation. You can't control how someone drives it or whether they service it or not. But as an engineer, you need to consider these things. And what you're essentially doing when you're designing components in that situation is you're looking at the risks of failure given the situation that the vehicle is out of your control and now in someone else's control. And so that's where I guess I started the conversation in Australia about how might we look at risk management a little differently than we have and a little differently maybe than the software industry currently does.
**Sam:** Very interesting. And it's great to hear about your background. If my car didn't start in the morning, I can point the finger to an engineer such as you,. And it's even more interesting now that you're now working within Thoughtworks, within a software consultancy. Let's talk about risk itself as quite a big subject and how would you define it? And why is it important?
**Anthony:** Yeah, let's think about two things. The first one is if we have a problem, we have a situation where something has failed and we have a definite situation that we can analyze. If we're in a situation where we have a service or a system that's failed, we can apply good problem solving tools to that situation. And we can identify the problem, the causes, and we can recover from that. Risk is related to that, but it's a little different. Risk has a certain uncertainty to it. It is the potential or the possibility of failure. And if you think about a problem that's actually occurred, we need to use convergent thinking. We're looking for a root cause or a number of root causes that we can fix.
With risk, we actually go the opposite way. We try to consider possibilities. What are possible ways in which systems can fail? And we need to employ more imaginative thinking when we think about risk. While it has its roots in the same thinking and the same kind of tools, one thinking is focusing on what happens, the other one is focusing on what might happen. And if you have the basics and problem solving tools, you're on your way to thinking about risk. But you need to think about it a little bit differently than actually solving the problem.
**Sam:** I'll give you the example that I've realized recently around risk. I'm a fan of motor racing and I'm a fan of Formula 1 and I was watching a really good documentary about one of the teams and in it, it explained how they mitigate risk within a racing scenario. And essentially what they said was they come up with around 1,000 possibilities of what could happen in a race so that therefore when you get to the race and said problem or outcome happens, they've planned for it. And therefore they can manage the risk as best they can within the circumstances that they're in.
And for me that was a huge surprise because I been a fan of Formula 1 since I was a kid. And all the while you're constantly fascinated by the engineering side of things and by how the drivers think and everything like that. But behind the team is this, basically a bunch of problem solvers throwing every single problem at the team and figuring out how do we get to this outcome, which is the win? Obviously that's the ultimate outcome. But in those scenarios, how do we manage it? Is it much the same? Is that how you would approach within the software industry, is that how you would manage the risk or manage or mitigate the risk that you might find within the problem?
**Anthony:** Yeah, it's certainly how we should do it. And it's interesting that you say Formula 1 because they would have learned a lot of that from the other way round, from the manufacturing industry, the producers, the cars that go on the road. They would have adopted a lot of the practices that that industry uses. Because if you think of Formula 1, you have a single car doing a single race and they rebuild the car after every race. They will have improvements to make and they will change designs and they will have learned something from each race. If you buy a car tomorrow, the expectation is that car will work for 10 years, with servicing of course, and all the things that you should do to prevent preventative maintenance on the car.
The potential for failure in a Formula 1 car is for a single race on a number of days, let's say a trial and then the race day. They would have learned and adopted the practices used by the manufacturing industry, manufacturing vehicles that have to work for a period of 10 years. They have a use of a life for 10 years, so it's probably while the technology has gone one way for Formula 1 to the production vehicles, production vehicle approach to things like risk management has gone the other way I think.
**Sam:** So within the software industry as well obviously, that as a consumer, as a user. We have a much higher intolerance I think sometimes when something doesn't work properly. How does that work on the back end? How do you make sure that the user or the person that ends up wanting to use the service or wanting to, I don't know, book a flight or carry out a transaction for example, how do we make sure that doesn't happen?
**Anthony:** Yeah, it's in a similar way. We need to take that risk based approach to failures. We need to think about ways in which the system can fail. Now having a 1,000 possible failures, that may be where we end up, but the approach can be the same. If we think about the way a system needs to function, so you're buying a ticket, there's a system, there's a infrastructure, there's software that runs, there's databases that run and talk to those. We can think about how the system should function and everything outside of that function is a failure. Interestingly enough, human behavior is very interesting when it comes to think about failures and think about catastrophes. We're really bad at it. We're really bad at it.
If someone says to you "How bad could things be tomorrow? What failures could happen? Or what things could be go wrong tomorrow?" You'd go, "Well, it could rain or yeah." You really find it really hard to think of these catastrophes. Yeah, an asteroid could hit the Earth, but you don't really talk about those sort of things. When you want to take a risk based approach, there is some good tools and good techniques you can use to describe the failures as you see. For example, you want to buy a ticket, you can't buy the ticket, do you buy the wrong ticket, the ticket is given the wrong price, the wrong information ends up on the ticket. There's some good tools that force you to think about or create these artificial failures. And then we ask engineers who are really good at problem solving to think about the mechanisms by which these failures can happen?
Rather than ask people to think about the failures and then they kind of get lost and maybe after two or three, we define all the failures and say now assume all those failures have happened, a bit like the Formula 1 team. Assume all these failures have happened. Now tell me, based on the way you're designing the system, hopefully we're doing it before we've actually built it, based on the way you're designing the system. What are the mechanisms by which these failures can happen? And there may be more than one for each of those failures. And then suddenly we have dozens and dozens of pathways that lead to that failure that we can look at and say, "How should we build more resilience along those pathways? What controls should be put in place? And more importantly, what prevention controls should be put in place so that these failures don't occur?" Does it make sense?
**Sam:** Yeah, it does makes sense. It's an incredibly complex thing and quite fascinating. Which business sectors do you think are doing a good job of managing risk at the moment?
**Anthony:** The ones for which consequences really matter are the ones that probably are doing it quite well. I think the health industry probably does it quite well. Although I've heard some pretty significant failures. Ones where you'd look at it from an engineering perspective and say, "How could you allow the situation where you mix up gases connecting to hospital supply lines?" For example, I've heard one, this happened in a case happened in Australia I think a couple years ago, but by and large I think the industries and industry segments that are doing it well are ones where it's safety related. They have to, they really have to because if they don't do it well, people get hurt and so there are big consequences. I think more and more there are calls to up the level of managing risk. Actively managing risk, not just documenting it, not just being compliant with a set of rules that we define, but actively managing those things in industries like banking and industries like insurance and in service industries, ones that are purely providing services.
My experience in being more in the financial sector that I have been in the insurance sector is there's a gap between what they're currently doing, which is looking at risk more as a compliance and as a central function of the banker. Not an obstacle but certainly a thing to achieve and get approval on and report on of course. Compliance drives those things. And actively and deliberately using risk to make different decisions about the processes and services that they build. And so the idea is if you can educate or train people who make the decisions on the consequences of the decisions they make and therefore, and that's the risk management processes and procedures, then hopefully they will understand the consequence decisions they make and therefore will make better decisions themselves and doesn't have to go through a risk group where I see that that's still that old style approach to compliance still being done.
**Sam:** Let's talk about from the leader's perspective. When people get it wrong, what are the common mistakes that you find that leaders make when they're thinking about risk?
**Anthony:** The first one I can think of is the one we've talked about before. It's failing to identify the risks effectively. Failing to actually acknowledge that these, identify and acknowledge these risks are risks that could eventuate and have significant consequences either on the business itself or its customers. And so the risks are confined to things like financial risk or confined to things like operational risk and they don't go broad enough to look at what are all the potential risks that could it happen to all the customers or all of the people or entities that experience the services or products that we build?
The second one is treating risk as a routine compliance exercise, ticking it off and then security falls into this space as well. If you're ever been in a situation where we have a security group and they have a set of rules and you got to meet these rules and therefore if you meet them you're fine. If you don't meet them, you're not. And so it's more black and white thing. I think risk and risk of and security can sometimes be treated as compliance exercise and they don't really give much value back to the business.
And the last, the third thing I can think of as I'm thinking on my feet here is not doing anything with risk. Let's say you do identify good risks, you identify well, risks of potential failures to the organization and the consequences, but then simply reporting them out and doing nothing with them, not actively using them to make changes to the services or the way in which an organization does business so that we can reduce the chance of those things becoming failures and impacting people.
**Sam:** Let's talk about governance.
**Anthony:** Let's talk about governance.
**Sam:** We're in a very, I keep calling it a strange time. I think it is a bit of a strange time, but for some it actually might not be as strange as the rest of the world perceives it because someone somewhere has had this notion that we would go through some kind of global pandemic or global health crisis. And I think what's been really interesting for me over the last few weeks, and I'm sure everyone's attached different chat groups and different groups where you can receive this information on a daily basis. And what I've been quite taken back by is that there have been so many talks, things on YouTube and all over the place where people have been predicting this for quite some time and yet governments and the more or less the rest of the world didn't have it as one of their risk factors to how we would operate.
And what are we seeing now is that we are seeing a huge knock on effect of the being unprepared or not being ready for the risk. I had a really funny conversation with my wife about a year ago and she said to me, she said, "We should have in our back garden shed some food and some things that if things go wrong, we've got some backup just in case." And I said, "In what world would we need? We're not living in the dark ages. This isn't going to happen." Of course now she can say, "I told you so." She'd actually watched a really good political talk where I think it was actually Angela Merkel had said something similar, like we should all be ready for something quite terrible to happen within the world where you can't go out. And I, and I'm happy to hold my hand up and say, "Well, wasn't I wrong." But it's really interesting because what everyone is seeing now, and obviously humans are fantastically adaptable but also not brilliant actually thinking before the adaptation has to come.
In terms of particularly in terms of government services, how can taking that risk based approach allow us to build tougher services and we're talking more particularly in terms of the government services and where you've worked as well.
**Anthony:** Yeah. Before I answer that one, I just want to make a point that you've just shown a good example of what could go wrong and how we make a decision about whether we should do something about that. We tend to confuse or conflate the severity of something like this particular health crisis, with the probability of it happening. Sure the probability is quite low, but if it does happen, probability's now got nothing to do with this. The severity is now what matters. It's how serious this thing is to the world. Angela Merkel, that's an interesting point she made that we should all think about what we should do to be able to be resilient in the face of something. Not untenable, but something catastrophic that could hit the world. We hope it never happens, but we should be thinking about these things and planning for these. I think your wife has a very good approach. I think I like her thinking.
**Sam:** Well she's a very smart woman.
**Anthony** : She is.
**Sam:** Smarter than me it might seem, which is probably quite true. 
But going back to that in terms of government services and how we're thinking about this and how governments have probably going to have to shift the way that they manage risk. What we're seeing in terms of this particular health crisis is going to probably shift the way that governments operate. How government services are delivered. How, there's examples that we have where we are working within certain government sectors, which I can't mention, but we know we've been drafted in at this moment right now because some of those services are failing because of the amount of demand that's been put on them. Have you seen, in terms of government services, have you seen that before? Or are we going to see more of a risk based approach to government services?
**Anthony:** We didn't need to see this crisis to see that the approach that some government services or at least the approach that's taken by the departments who provide the services is probably not taking a risk based approach. We had a census debacle. You might've heard this last year. There was for some reason, the system was rebuilt. In time, it had four years to be built from the last census till this one. And as the census was launched, there was encouragement for everybody to go online and to fill out their census application rather than fill out the paper one. That's where we're going and people would rather not sit down with a pen and paper now, rather get on a laptop and just fill it out and get it all done with. What did they actually expect to happen if they encouraged people on that one night that everybody was going to fill out the census, what did they expect to happen as it got to about 5:00 and 6:00 and 7:00 and 8:00 o'clock in the evening?
Well, of course what happened is hundreds of thousands of people started logging into the system and the whole system fell over. Now the initial story from what we heard was, oh, it was a distributed denial of service attack that took down the system. And you could see a lot of people looking at each other going, "No, what you've done is you've created a demand. You made a service, and you've told people to all hit that service at the one time and you haven't designed the service to accommodate that. And so what looks like a distributed denial of service attack is simply hundreds of thousands of people trying to access the servers at once. And you actually look at the number of requests, times number of people and it's in the millions." Clearly when you're building a system like that, there's a huge opportunity to look at what are the potential ways in which the system will be used?
And we knew that if it was going to be a single day that people were going to log into the system and we knew it was going to be around a certain time people get home in the evening and they go to log in, there's going to be a massive peak. Then what are the possible failures in which way the system can fail? And then think about and how can we mitigate against that? There's an absolute case study you could take in complete isolation to the systems that are now being hit in a real crisis and we're talking about a crisis that it's weeks and months long rather than a single night.
But that was a light bulb moment for me, that there are opportunities and this is not just in governments, in other services too, where we can take a risk based approach. We can start thinking about the ways in which you can fail and the ways in which it might be used that will lead to the failure and therefore we can design the system to be automatically scalable. Perhaps throttling, perhaps we can put controls in place that allows the service to continue to operate but doesn't allow the service to fail.
Now fast forward to the current crisis and you have a huge number of people losing their jobs or being put off for the time being and being told you can get, UK is the same. You can get access to a wage subsidy. Now, however that gets paid, people need to register on the existing system. Instead of going, instead of a system having roughly 6,000 or so, I think I remember numbers, I might be wrong, but roughly 6,000 requests a day or 6,000 applications or changes. It's in the hundred thousands of applications and changes in the system a day. Significantly scaling the capacity the services need. And it's not surprising those systems are falling over because they were built according to what people thought they needed at the time and not according to how the system might have to respond to a crisis.
Again, there's a lack of risk based thinking and if we would broaden that to beyond just health services and looking at tax services and looking at any digital government service, you could apply the same thinking and say, "Okay, it needs to do certain functions. A health service needs to be able to take applications. It needs to provide information to citizens about their application status. It needs to give them information about how it links to other information and also needs to make payments, let's say to them through, the health payments for example." All the ways in which they can fail and all the reasons for a failure can be considered as at the time when we start building the service so that we can start building in some of the mitigating actions and prevention controls so when the service does get hit or if it ever does get hit with this significant increase in incapacity or demand, we don't have a system that fails. It's more resilient. It bends to the demand. It isn't brittle and it doesn't fail.
There's huge opportunity. I see this and it's not just let's build a bigger system because that's not the answer. It's not what we're trying to do. It's like saying, "Look, the car isn't fast, let's stick another engine in it." It's not like that. It's think about it from a resilience point of view. Think about the mechanisms in an engineering way and consider how you might build in some shock absorbing systems or shock absorbance into the infrastructure, into the databases, into the applications and services that we build.
The other thing I'm thinking about is you could also take this approach to building rapidly connecting modules or rapidly connecting systems to build new services really fast. If you can design these systems with a risk based approach and they can automatically scale, you can plug them end to end and just increase your capacity as required and produce a very resilient service in a very short space of time. Rather than, oh, we have a new crisis. We now need to spend six months building a new system or changing the current systems. We need to be thinking about how do we respond in a much shorter space of time in the matter of hours and days rather than weeks or months.
**Sam:** It's really interesting you're talking about this now. We really just weren't prepared and I think the thing we weren't prepared for was the circumstances in which humans would be asked to live in. And it's an extreme circumstance and it's probably extreme because although pandemics have been around for hundreds and thousands of years and in modern society we haven't seen it very often, but we have seen it. But what's being asked of humans and the way that we operate is completely different to how we would operate before. Therefore, every touch point that you have from buying your groceries to visiting the doctor, to something that you might do online, to traveling is completely different because if you're being asked to operate in a completely different way.
And what's been surprising, quite surprising to me, is how some companies and services have responded really well to it, probably because they've managed to think about the risk before it happened.
But when you're talking about this almost baking in the system and putting these shock absorbers within the software, within the platform, whatever it is, as we're building it, how much harder is it if you haven't done that? If you haven't thought about building some shock absorbers in, how much more difficult is it to go back into the system that the engine as it were, and go, okay, we're failing over here. This thing over here is more is at breaking point. Presumably, I'm not a software developer and I'm not a risk manager. Presumably it's much harder to do that in the midst of an extreme circumstance like we're in at the moment.
**Anthony:** Yeah, there's been some talk about that over here and I think the right decision at this point in time is you shouldn't be going and fiddling with systems while they're at breaking point. We can't do that. We can't change critical systems. There's a recognition that, I'm not sure if there's a recognition that we need to be doing more scenario planning, more risk assessments, but I think you'll find a lot of governments, progressive ones, will realize that, and there's going to be opportunities to maybe do a bit of a stock take of what systems we have and what ones didn't hold up really well and why. And do some really good analysis on why we actually end up with these systems and why we don't have good resilient systems. I'm hoping that's going to be one of the good outcomes of this. It's going to force us to think that way.
As to changing systems once you build them in, see the thing with risk is, and this happens with whether you build a digital product or a physical product, but usually it's more expensive with a digital product. If you build an aircraft and it has a fundamental design flaw, that's pretty expensive. You could imagine the Boeings and the Airbuses, you've seen Boeing of course in the last 18 months or so suffer with what is effectively a systemic problem. I won't say it's a software problem because it is more than that. It's a, and I've been following it really closely because I'm really interested in how that sort of managed to move into production and bypass what are normally pretty good safety controls in aerospace. A lot of the techniques actually that I talk about come from the aerospace industry because of the significant consequences if something goes wrong.
But there, obviously something went wrong in the Boeing case and it's more of a systemic failure rather than you'll point at a component or a particular piece of software. But if you imagine that all systems, all software products that we build, form part of a system, people use the system. The system sits on infrastructure, a process sits around that system and it plugs into or the system plugs into that. If you haven't built it with a risk based approach, it's like baking a cake. It's very hard to unbake it. You often have to go and bake another cake. Very hard to pull the ingredients. Even when you start mixing, it's hard to pull the ingredients out. And what happens with risk is, when you're faced with critical decisions, and these can be significant major decisions you make early on in a project, they could be incremental decisions that you make throughout a project. When you make a decision, it's usually a choice between, well it is a choice between two things. Otherwise there's no decision. It's at least two options or maybe more.
Each of those decisions comes with a risk. And here's the thing about risk assessment or understanding risk. The risk exists whether you know it or not. And as engineers and technologists, it's our responsibility to start to, not start to, maybe better understand the risks that we're creating in the systems when we make those decisions. The point of risk management is not to eliminate risk because you can't. It's not possible to eliminate all risk. The point is to understand what risks you're introducing into a system by the decisions that you make such that you make the best decision you can at the time and you avoid those decisions that present an unacceptable risk that you can't back out later on. If you have a major decision to make early on in a project on let's say the infrastructure that we choose or the architecture that we choose of a particular product, it probably will benefit from more analysis and more catastrophic thinking. What are the catastrophes that could face us? Rather as opposed to a smaller decision that could be reversed or changed at some point in the future.
You can, and I'll go back to the physical world. You can change the components out on a particular, on a physical device, whether it's an iPad, an iPhone, a laptop, a car, whatever it might be. Even a house you can change components. But try changing your foundations out on a house. Try just jacking the house up and sliding out the foundations when you realize the decisions that you made early on when you were building your house are faulty and you've built in an unacceptable failure, potential for failure in there for the house falling down.
There's no one size fits all but I think hopefully with, if we are looking for some good out of this crisis, it's to think about risk a little bit more pragmatically. Use some good tools that exist in engineering disciplines where safety matters and we can adopt a lot of those tools and practices and apply them where it matters most and it's not a broad brush approach. Apply them when it matters when we're choosing solid foundations versus the color of the paint we put on the walls.
**Sam:** Very, very great messages to take away. Is there anything else that you'd like to give to our audience when they listen to this? Any key messages that you think would be useful to them before we wrap up?
**Anthony:** Yeah. One message and this talks to, and this is not because my partner is a designer working at Thoughtworks, not just because of that. There was a maxim that came from the auto industry and we were working in a space where we were designing electronics hardware and so embedded systems, electronics hardware and software and user interfaces and electrical systems in the vehicle. More than just the mechanical components, but there's a maxim in automotive that says, "Design influences 70% of a system's performance, it's reliability. And the application of that or the application of a design so when you manufacture it, when you produce something, it only has 30% of the influence."
It's important that we move the risk based approach as far up into the design phase so that when we're making early decisions, whether it be architectural decisions, whether they be accessibility decisions, whether they be user experience decisions, all those design decisions are the ones that are going to benefit most from a risk based approach. If we leave it too far down, we've lost most of the opportunity to make changes. We kind of baked half the cake. We've mixed all the ingredients together and we can simply make some adjustments to it, but to get the most benefit, we want to be thinking about these things as early as possible in the design phase.
**Sam:** Fantastic. Great advice. Thank you so much, Anthony, for joining us on the podcast today.
**Anthony:** Thank you very much.
**Speaker 3:** Thank you for listening. If you enjoyed this episode, help spread the word by giving us a rating on iTunes, Spotify, or wherever you listen to your podcasts.
[ View full transcript ](javascript:void\(0\))
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
## Don't miss out on the latest episodes; subscribe today
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