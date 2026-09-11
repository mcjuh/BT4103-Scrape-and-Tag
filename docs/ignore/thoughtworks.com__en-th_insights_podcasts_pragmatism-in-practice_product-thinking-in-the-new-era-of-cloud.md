<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/product-thinking-in-the-new-era-of-cloud | Title: Product thinking in the new era of cloud | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Product thinking in the new era of cloud 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Max Griffiths
October 27, 2021 | 41 min 27 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/product-thinking-in-the-new-era-of-cloud#transcript)
Listen on these platforms
## Brief summary
Cloud infrastructure has been universally praised for its simplicity, an intuitive, scalable, and cost-effective alternative that promised to transform how we approach IT infrastructure. But as offerings from the major public cloud providers have become more sophisticated, cloud is becoming increasingly complex. Listen to this episode with Max Griffiths, Principal Infrastructure Consultant, to learn more about productizing this part of the business, preparing teams for the skills shift to this new paradigm, ensuring cost savings and enabling the business with product thinking.
**Episode highlights:**
  * **Always tie back to the business strategy** or what you’re trying to do as a holistic organization. Set markers to optimize when you’re in the middle of the journey and have a plan, but avoid being too rigid or getting lost on the journey. Have key indicators of the benefits you're hoping to get to measure success along the way.
  * **Software engineering within an infrastructure context.** The infrastructure world is moving, everything in the cloud is software-defined. Understand what the application teams are doing and then supply enough infrastructure to make the application work, but make it evolutionary as possible and make decisions on the architecture that is driven by the business.
  * **Creating self-service infrastructure.** To create this self-service aspect, the developer team should be able to get what they need without depending on too many teams; it needs to tie into that application-driven infrastructure. 
  * **There's lots of shiny objects on the cloud journey that can distract attention.** There's over 2 million products offered right now from vendors who are building more specific capabilities to help their customers. It brings about different challenges, complexities and it creates a harder space to remain disciplined.
  * **Product thinking on the team.** Factor your application around the business capabilities that make sense to customers. It creates a clear understanding of where the value is being connected. Think about your developers and other teams within the company as internal customers. Have someone on the team who has the business acumen and understands broadly what the organization that you're working in is doing, be able to work with the platform engineering team so they can help make sure that those two things are always tied together.
  * **Future-proofing cloud strategies.** Focus on how to financially model the benefits of building internal platform services. Try to package up your platform products in a way that can be monetized, whether it's real money or whether it's just estimated costs in terms of the balance sheet, really weigh up these expenditures and business value that they're providing.


Learn more about this topic _Infrastructure as Product_[here](https://www.thoughtworks.com/insights/articles/infrastructure-as-product).
**Transcript**
**Kimberly:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks, where we share stories of practical approaches to becoming a modern digital business. Not too long ago, cloud infrastructure was being universally praised for its simplicity, an intuitive, scalable, and cost-effective alternative that promised to transform how we approach IT infrastructure. But as offerings from the major public cloud providers have become more sophisticated, cloud is becoming increasingly complex and harder for engineering teams to keep pace with.
What are the complications that companies need to be aware of and what are some of the helpful approaches businesses can put in place to realize the true promise of the cloud? I'm Kimberly Boyd, and today, we're speaking with Max Griffiths, principal infrastructure consultant in our Thoughtworks, UK office, about this new era of cloud. Max, thanks so much for joining us on Pragmatism in Practice today. I'm excited to dive in and learn a little bit more about cloud and all things cloud infrastructure.
**Max:** My pleasure, thanks for inviting me.
**Kimberly:** We're talking about cloud. It's not something that's new though. It's been around for a while, even though there are still a number of organizations that need to move to the cloud. There's known practices of the best way and why you should make the move, but a lot of people still struggle and fail to realize the value and the promise that they thought cloud would provide. Can you talk a little bit about why we are still seeing so many failed attempts when it comes to cloud?
**Max:** Yes. I think there are, as you say, a lot of people on this journey, a lot of people very far through the journey, and a lot of people would say that they have completed that journey, but whether they are reaching the goals, business or otherwise, yes, sometimes remains to be seen. I think one of the things I see most commonly is people get a little bit lost on the journey.
Due to the technology being so appealing, there are so many different options for people to choose. They are so excited to get the cloud or so excited to look at X new product that's available on the cloud, that tying that back to what the business strategy is or what are they trying to do as a holistic organization sometimes gets lost in the weeds.
You can be 6 months or 12 months through, having spent however many millions of pounds or dollars, and then be sitting there wondering exactly where are you. It's the same with a lot of digital transformation pieces, I think. You have to try and optimize and set these markers for when you're in the middle of it when you're really trudging through the difficult times. Some of those indicators, they're on why you're there and which direction you're going, can really help.
**Kimberly:** Is there anything that you've seen work particularly well, or anything you'd recommend organizations to do so they don't get distracted by all those bells and whistles, and they can stay true to their original purpose for the journey in the first place?
**Max:** I think having a plan, obviously, to begin with always helps, but also being realistic that what you find may have to change that plan. I think one of the first things or one of the most common mistakes I do see people make is it becomes very much about a technology change or re-platforming, moving a whole bunch of workloads that we have running, maybe perhaps in an on-premise data center, moving that to the cloud, when actually it can be so much more than that and should be so much more than that.
One of the bits of advice or one of the things that I look for when I go on and work with some of our clients is see how tethered the technology strategy is to the business strategy because cloud or transition to the cloud or yielding the most out of cloud should really be about what parts of the business are you trying to accelerate or enhance.
**Kimberly:** It's never just moving to cloud for cloud sake. I wonder if we should just not even call it moving to cloud. We should call it moving to get X, Y, Z business capability. Maybe that would help.
**Max:** I agree. I think as the novelty of cloud is probably, depending on what industry you are in and varies depending on the size of the organization as well, but I think the novelty of cloud is now starting to fade. I think that the industry is getting on board with that, similar to how DevOps was this big, shiny word and everybody overused it, and now most people are fed up with using it. We've now got to the next level of conversation, which is what does it mean behind the scenes? I think the same will happen with cloud. If for nothing else, just because of how many different things it means. Cloud in itself now, it doesn't really mean anything.
**Kimberly:** Like the word digital, right?
**Max:** Exactly.
**Kimberly:** Is there anything that you're seeing, in particular, from clients who are deploying the cloud platforms that really trips them up the most or a common pattern of struggle?
**Max:** Yes. Apart from having a plan and maybe staying a bit too rigid to that or maybe getting lost on that journey, as I mentioned, not having some of the key indicators there of whatever benefits you're hoping to get. If we start from the beginning, let's say you have it connected to the business strategy, you have your plan in place, but if you don't have some of those leading indicators, some measures of success along the way just to let you know that you're heading in the right direction, that can really cause you to trip up.
Having to think about when you have your plan and having to think about what 6 months through, 12 months through, what should we be able to see and try to hold yourselves accountable to that because I'm sure the business if they're investing in this, they're going to want to see some of those KPIs, whether it's KPIs or OKRs that you're doing, but some sort of measures. Some of these things, it doesn't have to be very elaborate dashboards or elaborate hardcore metrics.
It can really just be some hypothesis that you're starting to measure up against. But I would also say there are some clients out there, some of our clients that I've worked with, you can go in and there's an expectation that it's going to be a cost-saving exercise or that is going to be a much more efficient in a certain way. I think there is this transition that companies are making from cloud being-- rather from infrastructure being in a data center and it being this huge amount of machinery that runs your business. I think with the transition to cloud, it's really being used as a business accelerator. Actually how the financials work in organizations can be quite tricky because traditionally the things that are an operational cost versus the capital expenditure are quite different parts of the organization. That's been quite a difficult thing for a lot of companies to figure out.
**Kimberly:** Yes. I think that's a great point too, and then as the business, you're the CFO, you're looking at data center costs versus, like you said, the business accelerator, those are very different types of fees and the way you spread them over your business and when you expect to see return or just anticipate them being that sunk costs, it's a very different way of thinking about it.
**Max:** Absolutely. It's very interesting going into an organization like we do at Thoughtworks. The first thing I tend to want to look at is an organizational chart and to see who is making decisions in those various parts of the business. It's very interesting if they do still have some on-premise infrastructure or some of the more traditional infrastructures outside of the cloud, and then they have their journey going into the cloud, stepping back and having a look at an organizational chart and actually seeing how far across the organization those two opposites exist, and then actually working your way up the organizational tree to see who actually can make decisions out of both of those, and then actually see how much of the cloud strategy does that person actually have influence over. It's quite a good and quite a cheap exercise to do.
**Kimberly:** This is where your infrastructure consultant mind is coming into play. You're like, let me see that organizational infrastructure before we get started here. I do want to go back to one thing you had mentioned at the beginning around thinking about what are those measures and making sure you're tracking them over the course of the effort. This is infrastructure, this is a migration effort. Does it help to maybe bring in some of the agile principles that you would apply to software development and think about doing things in the smaller chunks slices, having the faster feedback cycles to see how your migration and how the move is progressing, if you're able to see some of those wins? Is that a way that organizations do approach it, or if they don't, maybe they should consider approaching it that way?
**Max: I** think that is actually where the modern side of the community now, the community that is pushing the boundaries on that, is trying to take software engineering within an infrastructure context. Typically, if you think about the idea of the data center and that long procurement process that used to happen, they used to have to make large highly risky predictions on how much compute power they were going to need for the next year, several years potentially. That in itself is very, very waterfall, a lot of upfront guesswork, and then 12 months down the line, and whoops, we haven't got enough.
I think the whole of infrastructure world is moving. It's all software-defined now, everything in the cloud is software-defined. You've got less of these long lead times now, and it becomes much more about this incremental approach. You're absolutely right on that. I think still though, I am seeing people take on the infrastructure as this is all separate to the applications that have been built and deployed on top of it. Actually, it's one of the things our friend, Kief Morris, who wrote the book on Infrastructure as Code, is very focused on now as people are now reading his book and taking it into practice this idea of application-driven infrastructure.
I'll just give Kief a quick cheap plug there. It's this idea of understanding what the application teams are doing and then supplying just enough infrastructure to make the application work, but not with the blinkers on so that when the next application comes along, that infrastructure is no good for it. Making it evolutionary as possible and making good decisions early on in the architecture, but it being very much driven by the business so that you don't just have this all-singing, all-dancing infrastructure platform there and no one to actually use it. The idea of composing this infrastructure piece by piece in a scalable evolutionary way is very difficult. I think it's something that we're just starting to see trends in now.
**Kimberly:** I think that parallels to what you were saying. You shouldn't move to the cloud for cloud's sake, you shouldn't build the infrastructure in the cloud just for the infrastructure's sake. It's everything having the purpose, which I know probably sounds common sense, but the common sense things are typically the hard ones to make sure we always get right. Speaking of that, so we talked about the importance of having a plan, making sure you're having those checkpoints to understand what the KPIs are and see whether or not you're appropriately tracking to those over the journey. Is there anything else for people saying, "I want to make sure I do this right," or, = "I want to do this the best way possible for what we're trying to achieve"? Any other advice you would give individuals in that spot?
**Max:** Yes. It's hard to be prescriptive without seeing a specific problem in place for some of the common things that I've seen. Looking at what the problem is that you're trying to solve, you could use cloud orchestration to take your business to a new region across the other side of the world. You could use it to automatically scale really quickly to unknown loads that's going to come to your website. There are lots of different reasons why you might want to start using the bells and whistles that cloud is offering. When you're sitting down and looking at the problem space and putting your strategy together in terms of how you're hoping to take the business forward, usually around that point you should start to have a good feel for when this is going well, I'm going to know what this looks like.
I was working for a client last year, and one of the intents was to try and get teams using the cloud and actually deploying their workloads to the cloud. One of our key metrics was to see how many teams we could have onboard onto this new platform. That was something that was quite easy to measure. You don't need a fancy measurement tool. You can just start marking this stuff down and track.
**Kimberly** : Are people on there? Yes or no.
**Max:** One of the other things we're trying to do is create the infrastructure to be self-service as possible. This is one of the big challenges that companies have today is if we're going to have a platform team that's helping land the cloud and some of the concepts and technologies with the business, let's have this platform engineering team there. But you need developers to be able to come and self-serve because if you put a platform team in the middle or an infrastructure team in the middle, that's going to slow you down a lot unless these tools are self-serve.
One of the things that we put in place was let's have a look at the application team's backlogs. Every time they have a story that is dependent on this team, that's almost like a negative point. It's not always negative because they may need something from that team, from the platform team, but for the most case, if we're trying to create this self-service aspect, then the developers team should be able to just get whatever they need to get done without depending on too many teams, too many other teams. We were using a project management tracking tool, lots of people use it, Jira, and we just kept an eye out for anything that had dependencies on the platform team at that time, and then just start to track that.
Over time, as we start to factor these self-service tools, then that number went down. Every time a new team came on board, they had fewer and fewer dependencies outside the team, which made them go faster, made them deliver quicker, and made the platform engineering team a lot happier. That's just one example of a very specific case because of what we were trying to do. It earmarks the point of setting these things, even if they might change down the line and making sure that they're aligned to what the business, I suppose, for what you're trying to do are.
**Kimberly:** That sounds like too setting that self-service as one of your guiding principles upfront isn't to say that there's no dependencies right away, but you're setting yourself up in a way that it's going to evolve and get smarter as the initiative progresses so you will reduce that number. Probably tying back to importance of the plan, importance of those guiding principles just to help set you up for continued success. It sounds like the theme here to me. [chuckles]
**Max:** Yes, and I would say that the idea of self-service is for these two parties not to talk to each other because, like I said before, it needs to tie into that application-driven infrastructure. If this is the first team that's coming on to your cloud platform, you're going to have to work very closely with that team to understand what is it that they need, but then be abstracting it away enough so that if team two comes along and they need a similar thing but slightly different, that you might be able to mold and shape it so it can work for both teams. The more teams you have, the more use cases you have. There is slightly different factoring you might need to do or you might need to create a whole other service that's self-service as well. The conversation is always happening. The intent is that you're not spinning multiple wheels for multiple teams, in the same sense.
**Kimberly** : Not spinning them or recreating them over and over. [chuckles] We talked about, too, at the beginning of our chat, about how people can easily get distracted when they're like, "Wow, we're on the cloud journey." There's lots of shiny objects that can distract attention. and saw that there's research that shows there's over 2 million products offered right now from the 5 largest cloud providers, which blows the mind, because also who's just cataloging all those? That's an insane number. Do you really need 2 million? Why did this get so big and why is this something we should be concerned about?
**Max:** Yes, this is a really philosophical one; are some of these cloud providers good or bad? I think people have to make their own minds up on that one. I think if you're a technologist, it's very exciting times, just because of how much is going on and how much innovation is happening. If you take one example, so AWS, Amazon Web Services is the largest and continues to be the largest. They were the first to the post, really, with some of the most basic cloud compute options years and years ago. I think once they started to explore what their customers were doing, and what their needs were, what their individual user journeys were, they started to break down some of the very fundamental basics into now getting into some fairly more specific building blocks that would help their customers.
I think it's providing a lot of different options, but whether it's good or bad, like I said, it brings about different challenges, different complexities, and it certainly creates a harder space to remain disciplined and really focus on-- I said before about focusing on the business, it makes it harder when there's a lot of these shiny objects about.
**Kimberly:** Sometimes the infinite choice makes it more challenging. I know when I go to a restaurant, and there's a massive menu, I'm almost like, "No, I rather have fewer options." [chuckles] It makes it a little easier to ensure I'm going to have a good meal.
**Max:** That's a funny one, actually, because you see Gordon Ramsay go and slash all of people's menus and they've got 50 things on the menu, and they really just need 7, and for that business, that does better. I don't think the cloud model would work the same way. I think there's definitely a business goal here, which is trying to offer more than the next person but I think one of the nice things that I've certainly seen from some of the big cloud providers is a real honesty around not having customers just spend incessant amounts of money through negligence.
Its actually one of the nice things I've seen as a result of just so many things happening, so the cloud providers are now offering really good cost-optimization tools that will analyze and actually offer you advice for free on how you can spend less with them, which you think from a business perspective is crazy. How many businesses are out there spending lots of money building tools so that your customers can then spend less with you? I think that there's a certain amount, and maybe I'm naïve, but there's a certain amount of good honesty there and good technology being built for the customer.
**Kimberly:** Well, we're in the business of consulting as well, showing you're that trusted partner and you're willing to actually help them spend less for a better return. In the long run, you're going to continue with them as a partner in all likelihood. Make sense too. Plus they have their catalogs of millions or hundreds of thousands of products. They probably need all the help they can get too in doing optimizing. Makes a lot of sense.
Coming back to, since I know everyone's interested, we're talking cost optimization, we're talking value, the reasons people say that they want to move to cloud. You talked about the importance of having hypotheses, testing those. KPIs don't always have to be something super sophisticated. They can be yes or no. Are the developers deploying the workloads? What are some of the other signals? What are the types of ROI folks should be looking for in these scenarios?
**Max:** Like I said, if the team that is responsible for the infrastructure has its strategy tied into the business, then really, the infrastructure is there to enable the application teams that are using that infrastructure. I think the four key metrics or the DORA metrics have been around now for a while around deployment capability, how many failed deployments you have, mean time to recovery, lead time to change.
These are real software delivery metrics that all teams should hopefully be measuring in some shape or another. It helps inform when to play that bit of tech depth versus new feature, et cetera. The tricky bit that I don't see a lot of people measuring right now is, if you have an application team, let's say they're pushing changes to a website, and if they have to wait on a piece of infrastructure because it's not ready, that they're asking the infrastructure team to, I don't know, open up a network port or something like that, how long is that taking?
Of their whole lead time of that particular change that they wanted to make a new website change, how much of that was delayed due to that call going out to a different team? I think it's that bit that's going to create some exciting evidence, and that then really gives a value proposition to that self-service nature of the platform. Because if the developers were able to flip a switch or had a port number that would then unblock that port automatically for them, then the change would be a matter of minutes versus potentially a matter of days, if not weeks, waiting for another team to do it.
I think if you're able to measure some of the software delivery metrics in your developer teams, in your application teams sitting on top of the cloud platform, and then it's just about working out how much of that is currently being spent waiting on that infrastructure team. Like I said before, cloud should be there to enable the business. In order to feel good about that actually working, you need to have some of those key measures in place.
**Kimberly:** Ways of seeing if the business is being enabled or not. Well, right, when we were also talking about the self-service with those teams, you would think that the third or fourth team who was self-serving should have that-- The time should reduce by each team who was adopting and using the platform.
**Max:** I was able to show that for a particular client actually. I think if you show a graph like that in a room full of businesspeople, there's no other reaction than a happy face, really, if they can actually see because that conversion of technology into time saved for people really resonates with businesspeople. It was a very rudimentary measure that I took, plotted it over six months, and then you could see by team five, teams six, the reduced time to market, if you like, was much, much smaller.
**Kimberly:** Any time you can show that business side against that red line swooping down from left to right for cost or time and sweeping up for revenue or growth, I think you'll have a happy audience.
**Max:** I was just going to say that's a good point, actually, because one of the things that I have been talking about recently is around having some sort of product thinking around that. I think one of the key wins is being able to have somebody who has a little bit of the business acumen, business savviness, understands broadly what the business and organization that you're working in is doing, be able to work with that cloud infrastructure team or platform engineering team or whatever it is that you have in charge of that low-level infrastructure so that they can help make sure that those two things are tied together at all times and represent quite a very technical team.
Typically the lower down the stack you get, the more and more technical it becomes, and the more and more disconnected your average business person might become. Making sure you've got the people in place to really bring that business vision back down all the way down the stack, all the way down to the people who are building the infrastructure really, really helped in that place.
**Kimberly:** Absolutely. Reminding everyone the ultimate reason why we're doing this, then connecting it at each stage of the chain of everyone involved. Again, one of those things that sounds like common sense that can be incredibly hard to do, so a good reminder. We've talked about some of these guiding principles of getting this right. Are these one size fits all? Should there be any differences in the strategy when it comes to size of organization, the scope of their cloud effort, what industries they're in, or is everything applicable to everyone, or are there other nuances that are good for a larger organization versus a smaller one?
**Max:** Definitely. I had the opportunity to work for a scaler, really just out of the startup blocks, about 50 people in total in the technology part of the organization, and so you have a lot of generalists there. You have strong developers who can do a lot of different things and, of course, their goals are usually to try and be as autonomous as possible, go as fast as possible, have as few barriers as possible. That usually means everybody else getting out of the way. Even though there was a platform engineering team, a very, very small platform engineering team, there's a lot of flexibility that the more senior developers on the various teams are going to want-- They want a little bit more control, they're a little bit more capable because they've been reading up on all of the latest cloud widgets. Really understanding your internal customers, as I would call them, because I'm always working on a platform team, so my customers are developers, and so really trying to understand them is important.
It doesn't make sense to go from a company like that to a huge, I don't know, investment banking organization that has thousands of developers across multiple geographies to then give all of the developers access to them, just orchestrate things from the cloud directly. That's where you need to build really good regulatory practices. There are a lot of sharp tools out there, as I call them. If you're allowing every developer to then have access to the cloud, you're probably going to have a lot of problems very quickly. Also understanding that push-pull. If you just stop everybody from using anything in the cloud, then you're likely inhibiting a lot of the benefits cloud is supposed to bring. That balance, again, is where a product owner, a very technical product owner, can come in and really try and understand developers as a customer, understand what they need, give them just enough so they can get their jobs done, and they enjoy their jobs, and they can be successful in their own right, but not too much so that it's bringing about security risk or it's going to bring about a lot of snowflake patterns that become very difficult to manage overtime.
**Kimberly:** As an infrastructure consultant who's worked across multiple organizations, and you have the developers that's your core constituency, your core customer base, what are your key takeaways or ahas to share with maybe other infrastructure folks listening on this call to make sure you keep your customer population of developers happy?
**Max:** This one goes for people on the teams and also the people who are managing the teams and the business is that all infrastructure is software now, so there's no need to treat the infrastructure team or teams, there are large organizations now that have multiple platform teams and infrastructure teams, there's no need to treat them as these special fish as they used to be because they're a software team now. Test-driven development, project management, using all of the latest project management tools that are designed for software, having a product owner, having a delivery manager or a project manager, having a QA.
QA for infrastructure is a very different thing to think about. We're used to seeing QAs in developer teams. What does it mean to have a QA in an infrastructure team? There's absolutely a test surface there that's really important, whether it demands a QA person on the team full time or not, but the concept of how do we test the software-driven infrastructure is paramount. I think the first crystal clear thing that came to me a few years ago was that there's no excuse really for treating infrastructure team any differently to any other software team. To try and elevate that team that's been pretty stuck in the corner and no one really talks to them because their answer is often no, which is that historical, I guess, stereotype, and then actually elevating them as a dev team like any other can actually be quite a big deal for an organization in itself.
**Kimberly:** It probably speaks to you wanting to get those teams working together really in an integrated and fluid way saying, "Hey, we're all engineers. We're all developing software here." It goes a long way to doing that. I'm glad you brought up talent and teams as well. Obviously, there's a lot of work to be done. You've talked about a lot of it in the course of our conversation, but it comes down to there's actual people creating all of this. For leaders who were on these journeys of building their cloud infrastructure, besides maybe making sure you're treating everyone as software developers as equal teams, what else should they be thinking about when it comes to the talent they have in this space and how they organize their teams?
**Max:** That's a good question. I think that certainly has been a pattern I've seen of the existing infrastructure team just being handed that cloud transformation journey. If you look at the skills that the existing infrastructure team have, they may have even been the people going into the data center and racking and stacking this hardware and cabling up the networks and then installing [unintelligible 00:31:35] operating systems and layering everything up until you can run an application on it. Larger organizations maybe that's a data center ops team, but you still have another infrastructure team that's responsible for some of the networking and security patching and things like that.
To ask a team that has a lot of these very useful sysadmin low-level skills to then suddenly take on some modern software-driven infrastructure approaches is a little bit like asking a history major to come in and then suddenly start coding some Java or something. It can be a very different way of thinking about it, very different practices, different pace, and working a lot closer with application developers. With that, I think that just needs to be taken into consideration, and setting that expectation upfront, providing some supplementary training, bringing in some cloud experts who can help supplement that team, help level up that team, but also not having these expectations that these folks are going to turn into these cloud wizards just if they go and do this one course and spend six months looking at some infrastructure as code.
**Kimberly:** Any big program like that it's a huge change management element, but I think that it's a good reminder that there's change management for the talent experience on that too. What you talked about there is a wide variety of skills and capabilities, so definitely not losing sight of that for folks that are on that journey. 
Max, you work with a wide variety of clients and have seen these cloud infrastructure challenges in a number of places. Can you give us a sneak preview of what's coming down the road so people are in the midst of these journeys and these programs now? If you're looking three, five years out, are there things they can be doing to future-proof their cloud strategies?
**Max:** I think there's a lot of focus now on how to convince the people who are financing a lot of the projects or deciding on the financing for a lot of these projects how to invest in cloud or how to invest in platform engineering at least this adoption. I think, on one hand, there's one direction that companies are going which is starting to try and financially model the benefits of building these internal platform services. You could get down to the level of if dev team A wants to use platform service B, should there be a cost associated with that?
You can imagine if, again I'll use the concept of a website, there's a new payments processing engine on a shopping website that we want to add and let's say there's a team that's responsible for designing that bit of the application. In order to do that, they need to plug into some identity platform, let's say that the platform engineering team are providing. If the project is spun off and they said, "We think this is going to cost X amount of dollars in order to ship this new feature," it would be nice for the platform-- Let's assume it's all self-service, so they've achieved all of those goals, it would be nice for it to be almost a utility or a subscription process.
How to do that internal financing, you're almost building your own facade to the cloud, these 2 million products that we talked about earlier, you need to build this facade in terms of how you're engineering the next layer of that platform to then expose that to your developer team A. I think trying to package up your platform products in a way that can be consumed for a certain amount of money, whether it's real money or whether it's just estimated costs in terms of the balance sheet, I think I'm starting to see clients now who have large platform teams who have their own P&L or balance sheet to really weigh up these expenditures and business value that they're providing.
**Kimberly:** Really bringing product thinking to some degree to the cloud infrastructure platform, is that my inelegant way of summing up what you're trying to share there?
**Max:** Yes. I think that's the way that people always talk about AWS in this context around how they're just a huge number of services that are just all wide up as an organization, but I think that is one way to view the business capabilities within your organization. If you've managed to factor your application around these business capabilities that make sense to customers, and then actually your entire business platform is just these business capabilities talking to each other, and that includes the infrastructure platform as well, it creates quite a clear understanding of where the value is being connected.
**Kimberly:** Yes. You took the words right out of my mouth. I was going to say if you're thinking about them, you're talking about them as products, it probably just helps to reinforce why are we doing this to begin with? It's to create these types of products that enable speed or value or whatever the dimension is. I think all things come back to product thinking for me, or at least it seems that way. 
**Max:** The interesting thing there is this role or this set of skills that's required around that technical product thinking. I feel it's still emerging and you can see some of the big tech companies out there who have done a good job of recruiting for this role. I think a lot of other companies are still catching up a little bit who can bring in that balance of the business, balance of the technology, and then really make that work. Even at ThoughtWorks here, we are very excited about this. We've got a number of people who are moving into these roles, but I think as an industry, it's still starting to piece together so it's quite exciting.
**Kimberly:** Now, do you think that's a role that's just taking shape? Could you describe what the ideal profile looks like for someone who has that full package that we're just talking about, or is it you'll come to the table with these skill sets and learn the others on the fly?
**Max:** Yes. I don't think I can. I think that's part of the problem as well, but I'll probably get told off by some of my peers, but there are multiple paths into this role, that's the thing, is that you can have come up through as an engineer and then be taking a bit more of an interest in the business and then start to leverage your technical skills, but learning more on the business side.
Then you see product managers and some business analysts also coming into this. I quite commonly might have a BA who's on a team saying, "Oh, I'm a BA on a platform team, how do I get more technical?" I had an interesting conversation with a colleague the other day about does that BA really need to understand how much do they really need to understand of this low-level infrastructure detail versus just know enough to be able to talk with the tech lead and be able to convey to the rest of the business what the value proposition is.
I think it's still being formed as far as I feel. I don't think it's a very clear bullet point list of what this person needs to do which makes it a little bit tricky to hire for, which may mean that we're doing it wrong or it may mean that we just need to work out it a little bit harder. It's a little bit like that DevOps role that started getting advertised years and years ago that used to be quite frustrating because it was this all-singing, all-dancing, not quite sure what this person actually does. We need to be careful not to fall into that trap.
**Kimberly:** Yes. Go find all these DevOps unicorns or all these infrastructure unicorns. Well, I think probably an important thing too, like you mentioned, there's no perfect bullet point list of things, but also the aptitude of someone to be able to come in and pick up the more technical elements or pick up the more business elements. I think if they have the openness to wanting to connect the dots between those two, that can go a long way into facilitating the connection there. 
If you could sum it up for us, Max, because I know we've talked about a number of things in particular, but if someone were to ask you, what are the handful of things that are key to successfully executing a cloud infrastructure platform strategy, what would be the top three or four items on that list for you?
**Max:** Yes. Just to summarize, I think, thinking about your developers and other teams within the company as internal customers, and nothing can do that better than assigning a product thinking person on that team, as well as a couple of other roles as well. You need a solid project manager or delivery manager there as well, but I always feel like if you assigned somebody in that role, it creates a certain amount of ceremony around it, give that person the remit. That would be my first piece of advice.
The other pieces that we talked about are some of those early indicators or early leading indicators that you are heading in the direction that you intended, being open about those changing as time goes on, you always have to be factoring in what are you learning, what needs to change, but to be able to at least narrate that journey to somebody who wants to know what you've been doing for the last six months, and being able to hopefully show at least a little bit of trend in the right direction, even if it's not hardcore metrics, is really valuable.
**Kimberly:** I think this is probably lots of food for thought for everyone on their cloud journeys. Thank you so much, Max, for joining us today. I learned a lot. I hope our listeners learned a lot too and really appreciate your time.
**Max** My pleasure.
**Kimberly:** If you'd like to learn more about this topic, you can download the ebook Infrastructure as Product on thoughtworks.com. Thanks so much for joining us for this episode of Pragmatism in Practice. You can listen to similar podcasts at thoughtworks.com/podcasts. If you enjoyed the show, help spread the word by rating us on your podcast platform.
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
## Don't miss out on the latest episodes.
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