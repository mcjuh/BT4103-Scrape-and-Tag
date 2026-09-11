<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/from-crisis-to-confidence-building-reliable-IT-systems | Title: From crisis to confidence: Building reliable IT systems | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  From crisis to confidence: Building reliable IT systems 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Sarah Taraporewalla and Max Griffiths
October 04, 2024 | 46 min 07 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/from-crisis-to-confidence-building-reliable-IT-systems#transcript)
Listen on these platforms
## Brief summary
Recent events, like the CrowdStrike incident, highlight the critical need for business leaders to understand and strengthen their IT infrastructure. Sarah Taraporewalla and Max Griffiths explore strategies for balancing rapid software delivery with system resilience. If you are a business leader interested in fortifying your organization’s defenses against technology crises, this podcast is for you.
### **Episode highlights**
  * **The Challenge of Software Supply Chains** : The discussion highlights how vulnerabilities in software supply chains can lead to catastrophic failures. Leaders need to better understand their entire software supply chain, ensure proper testing, and recognize the risks inherent in third-party updates.


  * **Importance of Simulation and Practice** : Both speakers advocate for regular "game days" or team exercises to simulate system failures and responses. These disaster drills, help teams prepare for real incidents by identifying weak points and ensuring that responses are well-rehearsed and calm during actual crises.


  * **Cross-Disciplinary Involvement** : For robust resilience and preparedness, the conversation stresses that it is crucial to involve teams across security, testing, engineering, and business functions in planning and recovery simulations


  * Sarah points out the need for **clear communication channels** during an outage to minimize panic and ensure a coordinated response


  * **Trade-offs Between Speed and Thorough Testing** : Delivering software quickly can compromise testing depth. The general consensus is that in some cases, more testing could be done.


  * ThoughtWorks advocates for a **"sensible default"** approach to software testing and development practices, which ensures that quality is embedded early and throughout the lifecycle, from design to deployment.


  * **Cloud-Native vs. On-Premise Systems** : Max contrasts cloud-native systems, which allow quick, programmatic recovery, with on-premise setups that often require manual intervention, highlighting the importance of automation for resilience.


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
### **Transcript**
**[00:00:00] Kimberly Boyd:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks, where we share stories of practical approaches to becoming a modern digital business. I'm Kimberly Boyd, and I'm here with Sarah Taraporewalla and Max Griffiths to explore critical lessons from the recent CrowdStrike incident. Today we'll delve into the importance of understanding and strengthening your IT infrastructure, balancing rapid software delivery with system reliability, and uncovering strategies to fortify your organization's defenses against IT crises. Whew, sounds like a lot that we'll cover, but welcome, Sarah and Max. Thanks for joining us on Pragmatism in Practice today.
**[00:00:39] Max Griffiths:** Thanks. Good to be here.
**[00:00:41] Sarah Taraporewalla:** Thank you so much.
**[00:00:42] Kimberly:** Sarah, Max, maybe before we dive in, you could both introduce yourselves to our listeners and tell them a little bit about both of your backgrounds.
**[00:00:53] Sarah:** Yes. Sure. G'day. Hi, everyone. I am Sarah Taraporewalla. I live in Australia. I'd like to begin by acknowledging the traditional owners of the land on which I'm sitting on at the moment, the Jagera and the Turrbal peoples, and pay my respects to the elders past, present, and emerging.
If you haven't heard this before, this is something that we do within Australia at the opening of important meetings and important discussions because paying that respect back to the elders and people of the land grounds us with what we're doing, why we're here, and the purpose, which is more than just technology, and it's more than just this conversation. We live in a bigger world that's around us, and all of these pieces play an important and crucial part.
Now, I've been at Thoughtworks for quite some time. I started as a developer, and I've grown into a business-focused technology leader. I work with clients across APAC, so Australia and the Pacific, usually to advise them on technology, AI, or modernization strategies. A common thread throughout all my work has been taking a complicated subject that only a few in the business can explain and getting them to help me understand what it is, but then making these connections, simplifying it down, and democratizing this knowledge to the masses.
I'm regularly looking out across industries, across disciplines, even in non-tech traditional industries, and really studying a lot of case studies and examples that we can learn lessons from to find ways to simplify some complex topics, make them relevant, and most importantly, actionable to our clients and the industry at large.
**[00:02:43] Max:** Thanks, Sarah. Max Griffiths here. I have been at Thoughtworks for about 11 years, but I've been in the industry about 20. Started off as, I would say, a Unix scripter, an automator. I didn't think about it back then, but now I do, that developers or application developers have always been my customers. I've always sat in this DevOps land, now called platform engineering, but building efficiency and automation tools to help application developers get on with their day faster, more securely, more efficiently.
Rolling forwards, joining Thoughtworks, got into cloud engineering and architecture and always doing that with programmatic code-driven approaches. Then got into production operations and the whole cyber reliability engineering movement that went with that. More recently, coming up to present day, I tend to help our C-suite, CTOs, CIOs, strategize about how low-level technical concepts like platforms and infrastructure platforms, cloud platforms, can actually yield business value and try to help them articulate return on investment for that.
Right now I'm the head of platform engineering for Europe, which covers leading our platform engineers and helping them get on the right projects, but also strategizing and building go-to-market products that our customers can consume.
**[00:04:08] Kimberly:** Wonderful. I think both of your backgrounds and experiences will bring a lot of color and context to our discussion today around the CrowdStrike incident. Before we dive in and do that, I think it would be great if one of you could just reframe that to us. Things move quickly today and it's perhaps not top of mind for everyone, or they only know it as the thing that messed up some airline travel for me or my family or friends. Maybe you can break it down for us a little bit and give a little synopsis of what happened with the recent CrowdStrike incident.
**[00:04:45] Max:** It's incredibly technical when you get down into the detail of it, but I'll give a breadth, and then I'm sure, as we go into the podcast, we might pick out some of those more specifics. Ultimately, CrowdStrike is a security software vendor that many, many, many companies and systems use and they purchase the software and they subscribe to its updates.
When we think about security software, in order to apply certain levels of security all the way down a system or an ecosystem, you're really getting into some of the nuts and bolts of how computers work. This particular, I guess, change that was pushed out by CrowdStrike-- This is common for security software to be pushing out regular updates. Actually, it can be quite important that they get pushed out very, very quickly because vulnerabilities in software are being discovered all of the time. Quite often, the speed to patching that can be the difference between you having a business in the morning and not having a business in the morning.
Part of the event that happened is CrowdStrike in their Falcon software pushed out a change to all of those people who subscribe and pay for these updates. That change propagated across pretty much all of their systems or all of their subscribers. This software update had a bug in it. There are multiple layers. How was that bug released into the wild? Why wasn't that prevented? Why did it take so long to detect? The specific nature of this change got right into a part of the Windows kernel. The kernel is almost the lowest-level foundational building block to a computer operating system.
Again, we can get into some of the details, but the way that this was able to be pushed in with very little change to the overall system made it very sneaky almost, or very difficult for, let's say, a consumer of this update to detect exactly what happened. Because this bug was inserted at that low level, essentially, the whole system collapsed. Not only did it collapse, it made it very difficult then to restore. Everybody was trying to restart, and because that low-level kernel system was essentially damaged, these systems couldn't boot up. Until some of the information came out to the market about how and the steps that you need to take with all of these systems, it was really impossible to detect what was going on.
Moreover, I think a lot of these systems that were affected are, like you mentioned, I think airport terminals. The way that we've got with how we deploy systems, we don't just have computers on people's desks where we can just maybe stick in a CD drive or plug in a USB stick. There are millions and millions of servers that are sitting on the back of TV screens at airport terminals or hidden away in server rooms, thousands and thousands buzzing in a particular server room. Applying a fix to this change at scale, there is then another layer of complexity on that as well.
**[00:07:58] Sarah:** Yes. I think the scale is the thing that has taken us all by surprise. There's certainly been lots of incidents that have caused outages in the past. If I think about just this wide scale, it's just crazy numbers of computers that were blue-screened. It wasn't just in IT departments that this was happening. It wasn't just in places where there was a phone call to the IT department that was ringing off the line. It was moms and dads, families, and schools.
A lot of this affected a large part of the population that had no real means to work through the complicated manual steps, which were released quite quickly, but they were still quite complicated to go through to restore your home PC so that your kids could do that study for that weekend. I've been looking at a couple of the other outages that have happened in the last five years, this one, I think, has taken the cake in terms of the number of machines that were actually impacted. I think we're still trying to understand what the economic impact of that is. Definitely, from a number of machines affected, it was huge.
**[00:09:31] Kimberly** : I want to put a pin in the scale point because I want to come back to that because it's really interesting and I think complex and something worth diving into. First and foremost, folks who were impacted by this or who even just observe it from the outside probably both had the thought of, "I don't want this to happen to me or I don't want this to happen to me again. How can I avoid this? How can I ensure that my business is resilient in the way it needs to be in order to not be impacted when something like this inevitably happens again in the future?"
Sarah, Max, can you talk a little bit more about just the concept of business resilience in general and why it's crucial for organizations to really have an understanding of what that means for their business and how they can go about starting to assess and build a plan?
**[00:10:29] Sarah:** Business resilience, this isn't an uncommon term. This isn't anything new, really. We know about disaster planning. We know about the preventative things that we need to do for business continuity plans. Why this is different is because in the past, we've been working in industries where we've been able to work workshop floors, and we've actually been able to eyeball where the problems are.
On a factory floor, the factory foreman and the managers and the higher-ups, they can literally walk through the building and have a look at where threats could happen, know what could catch on fire, what could go wrong, which machines could break down, which would break their business continuity. All of the things that they're making are actually visible to them.
Fast forward into this digital age, where digital has become such a key component on many, many organizations, and it doesn't matter if you're a digital pure play or an asset-heavy organization, or somewhere in between, digital is now a very, very core part of most organizations and the way that we work and live. Digital gives us different challenges in the sense that we can't see it. We can't see the ones and the zeros that are making up this.
The factory floor is in a hidden black box now. As non-experts of what's actually happening in the black box, it's really difficult to come in and eyeball and have a gut feeling about where the vulnerabilities are lying in the business. That's a really interesting note to take right now. The reason why we're in this state is actually that we haven't matured enough to build up this gut sense as business leaders to ask the right questions of technology.
We're so used to asking the questions around speed and "When am I going to get my project delivered?" We're starting to learn a little bit more about security, but this wasn't even a security issue. This was a software supply chain issue and understanding all of those components in the software supply chain that actually hang together to make our business run. In a lot of the cases, people don't really understand what all those different components and parts are. Business resiliency and business planning for these outages is going to become the new normal where we will need to start doing disaster recovery in the same way as we run fire drills throughout our businesses.
**[00:13:27] Kimberly:** You mentioned the concept of understanding your software supply chain, and that was a bit of where the breakdown happened with this. What can organizations or leaders do to begin to understand that supply chain and where there might be risk or points of breakage within it?
**[00:13:48] Max:** I've been working in this software supply chain for pretty much my whole career. You're in this constant battle with shifting bottlenecks. Like you say, everybody is trying to do things faster. I think one of the causes of why these problems are starting to happen is because the computational aspects of our business are almost speeding up far beyond, to Sarah's point, I think, than what people and process can catch up to.
A lot of the need for this business resilience has come from almost technology in a way because previously we used to have a server that was running our system, and then maybe a backup server that we would somehow switch over to in a certain amount of time should a problem occur. Now we have very complex cluster-type service systems that this idea of disaster recovery is still a concept, but how that's implemented is very different. Now it's more about having ultimate resiliency. If an event happens and you lose 10% of your capability to serve customers, then you can hopefully restore that later and you haven't lost your whole business.
Coming back to the question, I think understanding that software supply chain, which tends to involve multiple teams in your organization-- Actually, modernizing some of these aspects requires you to modernize your organizational structures. Most of us are familiar with Conway's law and also the inverse of Conway's law, where you start to change your architecture based on your people architecture, if you like. Zooming into exactly what's happening in this, again, like the SolarWinds outage of a few years ago really opened up some of the problems about how attackers can come inside that supply chain and start to manipulate things.
I think one of the popular concepts that's come up for technologists is this idea of game days or red-blue teaming, which is where you take a day or a number of hours or a number of days and you are intentionally testing the resilience of your system, whether that's receiving a whole bunch of production load, or indeed, whether you're practicing your ability to respond to an event or an incident. If a system goes down, how quickly can we get a change or a fix through that supply chain? What does it look like?
Broadly speaking, you're trying to simulate these events, but in a very real way, using the people and the teams that would actually be responding in a real situation. Now, obviously, once you play around with these simulations, you still need to be running your production system. That can sometimes cause a bit of mayhem in the organization, so these days need to be planned and thought through.
I think this idea of getting different people from different disciplines, from security, from testing, from engineering, even from the business, to gather around this idea of simulating a few different events, it exposes very quickly, very shockingly, in most cases, where some of these maybe oversights have appeared and immediately gives you this backlog of like, "Okay, we can't really go live with this next because we need to fix these things." That's one of the ways that I've seen.
**[00:17:18] Kimberly:** Max, how many organizations would you say engage in something like that on a regular basis? Is that a pretty common practice or something only a handful of organizations do on a regular basis?
I certainly don't see it everywhere. I think this is another one of those uptick curves as we start to catch up with what's happening in technology that is becoming more and more common. I started introducing it as mandatory on any teams that I work on as of about five or six years ago, and I think it was only really invented or popularized, I would say, maybe a few years beyond that as well.
I think the catch-up is faster, but I still certainly see organizations who don't do it. They talk about it. It's one of those things where everybody likes the idea of it. They understand the benefits, but actually maneuvering your organization to take it seriously is difficult. I think events like CrowdStrike suddenly summon some of that energy for people to finally get around to doing it.
**[00:18:35] Kimberly:** Bring it to the forefront. When you said red teams and blue teams too, it made me immediately think of a technology capture-the-flag. That's--
**[00:18:45] Max:** It's pretty much like that. You'd have one team who are essentially defending the system or trying to respond to the outage, and you have another team who are a sinister threat. They might know the code and they'll say, "I'm just going to go and exploit this area of it and then see how the team responds." There's a huge amount of learning that can happen in a short amount of time on both sides.
**[00:19:09] Sarah** : I think practice runs are really, really important here. We do fire drill planning in most buildings. I always think about the story from 9/11 where prior to that a person within one of the companies that worked in the towers mandated that the company would do disaster planning and they would have to do all of the steps, go up and down all the steps and actually exercise their disaster planning. People weren't allowed to skip out on the fire drill day. That became really, really important on September 11 because they got all of their workforce out of that building in a very safe manner for everybody.
I think about that in terms of these disasters. I think it's a fallacy to think that your organization will not be impacted by any significant outage like this. The question isn't if, but when, and more importantly, what are you going to do? Does your team know what the chain of command is, what the communications line is? How are you going to stop the noise of the fire from actually going in and problem-solving? This is not only something happening within your software supply chain, but this is you yourself taking down your website or your product or your business.
Are there well-established lines of communication if something goes wrong within the business to both shield the team that is looking after fixing it but also giving enough information to the external leaders that they can then turn around and tell their customers and their shareholders about what is happening and keep the panic out of the conversation and just focus on solving for the problem and getting the problem done?
I think that we've got the exercising of what the supply chain going down and where that could go wrong with these game days. As important is let's exercise what these communication plans are. Let's make sure that when we are in disaster mode, we are actually cool and calm going through it and we're not panicking. We get that by simulating and training ourselves not to go into panic.
**[00:21:44] Kimberly:** Yes. That's a great point, right? Because you talk about practicing the defense of this happening, but I think we all acknowledge it is an inevitability, so also practicing the after you've defended and the incident has still occurred so you can retain that calm. I think that's a really fantastic point. One thing I did want to circle back to is you talked about, at the beginning of the conversation, how part of the problem with this CrowdStrike incident was the bug got into the kernel o into the foundation, which really prompted and made this such a challenging issue.
Could you talk a little bit about how organizations can identify potential points of failure or vulnerability in the core of their IT infrastructure?
**[00:22:46] Max:** Typically that doesn't receive many changes. When it's changed, it's usually being changed by the operating system software vendor. If you're on a Mac, it'll be your Apple macOS. If you're on a Windows machine, it'll be coming from Microsoft. If you're on a Linux machine, whatever Linux distribution you're on. These are typically very trusted sources and they've gone through a lot of testing. For a third party, if you like, to be changing some of these kernel parameters, for them to go through a lot of testing for every single configuration, ultimately slows down the time it takes to then deliver the change.
In this particular event-- I know you're speaking more generally and I'll comment on that in a second. In this one specifically, there is a trade-off between how much testing they do and how quickly they want to ship it because if they take longer to ship it, maybe an hour, maybe a day, if you're really testing kernel parameters and you want to test all the different types of machines that you could be pushing out to, that might take months or years.
There's always this trade-off or slider to say, how is it there? Now, I don't believe, and I think the community doesn't believe that enough was done and that maybe the slider does need to move. I think they've acknowledged that with testing practices. I think that the concept of this trade-off is relevant for everybody. You cannot spend infinite amounts of money getting to 100% protection.
One of the things that you can do is create a testing funnel, or sometimes we call it a testing cone, which is from the origin of your first lines of code, all the way through to deploying to a production system where your customers are interacting. This software supply chain, as we now know it to be called. There are multiple testing gates. As you get further, always talk about a left-to-right thing, we talk it as a software delivery pipeline or lifecycle.
As you start with code on the left and you start to push forward towards your customers on the right, the testing gets more expensive because typically the environments are getting bigger and more complex because you want to be testing an environment that is like a production environment. Then when you're looking at the code on someone's laptop, the testing is said to be cheap because the feedback is very quick and the way that you're writing the tests and how the infrastructure that it's running on is just your laptop, so it's very cheap.
This kind of testing strategy, something that Thoughtworks has been specializing in for a long, long time, is really important. It enables you to dial in or dial-up where you need to be doing that testing. Is it in performance and resiliency? Is it in unit testing different chunks of your code? There are different scenarios where you might want to expand or invest in more testing in one particular area than the other. The recommendation is looking at that whole system, understanding what the fundamentals are of your application and how that responds, and then the considerations you need to make as it gets closer towards a real customer.
**[00:26:08] Sarah:** I think there's two things here at play. The first one is, do you know your vendors, and do you know how your vendors actually produce the software? We've always been thinking about software in terms of buggy software, and we just accept that bugs that they're just part of the norm. Facebook really popularized the break-fast, fix-fast mentality, but I think that doesn't hold up anymore. What we have to do is we have to go fast but with confidence. Go fast, but don't break things.
That's really where as Thoughtworks, we've been hitting that tin can for such a long time and introducing some tools and techniques that people use throughout the world to improve that software delivery lifecycle so that we don't end up continuously producing code that hasn't been tested, that hasn't had that engineering rigor put around it. Understanding how your vendors are writing the code and whether they are following the good practices that you might also be in making sure that your engineering teams are following, are your vendors following it? That's the first thing.
The second thing, a lesson that we can learn from it, specifically around where we were caught out with the specific CrowdStrike thing, is that that can happen. That is actually happening on a very daily basis in most organizations that we're talking with, this go-fast, fix-fast mentality, just push things out the door, don't do a lot of testing around it, or wait to testing at the end of the delivery phase. This is happening in a lot of organizations, maybe not the newer organizations, but this is where having a look at the engineering practices that your teams are using on the ground and learning from the lesson of CrowdStrike, not just how to protect yourself from a supply chain problem, but how to take the post-mortem that CrowdStrike are doing and take those lessons and ask the technology teams, "Do we have a really good software delivery lifecycle? Are we having the right and adequate testing? How many times do defects escape into production from our own systems?"
Because we are probably part of somebody else's supply chain, so we can build up the confidence with our clients by showing them just how good our engineering processes are and expecting the same great engineering practices from the vendors that we work with as well.
**[00:29:32] Kimberly:** I think what you've both shared about testing being a continual thing in the lifecycle and not waiting until you get to the end, it's almost like tasting your food as you're cooking something. You don't wait till the very end. You might have to throw the whole dish out. Let's taste as we go and also know where you're buying your ingredients from, who your vendor is up front, so you know it's quality. You know how they make it. You know how they test it.
Sarah, you were just talking about some of the practices, making sure they're testing in different stages, is there value in almost having a resilient or testing practices checklist of sorts for folks to say, "Look, these are practices we're doing today or we're doing 60% of this list so that there's some risk to us, and if we want to tighten up even more, maybe we can think about getting to 80 or 90% of this list"? Is that something you'd recommend organizations think about or is it something that you've worked with organizations to get them to adopt and practice on a regular basis?
**[00:30:42] Sarah:** Yes to both. Within Thoughtworks, we call them our sensible default practices. We've published them. They're on our website. You can take a look. They span engineering, QA, infrastructure, and project management and design and analysis, sensible defaults. I recently came off an engagement with a client where I was looking at their QA strategy. They came in and said, "We've got a large number of QAs here. We spent a long time in our QA step. Tell me what I need to do to improve that."
We applied not just looking at it through that sensible default lens, we actually started to look at it from a systemic lens and system lens. We didn't just look at the QA practices that were at play, which is the work that the QAs were doing, we also looked to see how quality was baked in from the very start.
That was looking at how the BAs and the product and the QA and the devs all looked from the requirements perspective and really try to understand where these edge cases typically lie, having a look at the defects that are coming through and doing root cause analysis of the defects that are coming through to really shore up the system and having that quality built and baked in from a software code and design perspective, from an architecture perspective, from an analysis perspective, and finally, from the QA practices and testing perspective.
If you want a list of line items to go through to see whether your teams are following good, sensible defaults for quality assurance, design, and infrastructure, take a look at our sensible defaults that our teams across the world adopt.
**[00:32:44] Max:** I'll just add on there that this is where this concept of pair programming tends to be a typical one. We have debates about how much pair programming is useful, as an engineering practice, this is another one where if you are pair programming, where you have two people working on the same problem, same computer, there's a person always there to converse about how you might approach the problem, and you've got someone there who isn't concerned about typing code thinking about the problem and thinking about, "Well, do you think that is a good test? Do you think we should be adding another test there?" Actually having a human debate on how this system is intended to function.
The other aspect, which I've mentioned, is this concept of threat modeling. As you're going through this process, rather than having checklists per se-- We have go-live checklists, especially if you're launching a new service. Is it resilient? Is it performant? How much so? What are the SLAs or the service level agreements that we're going to have around the availability of this service?
There's lots of really good checklist items you can build. Actually, it's more about the principles and practices that you would like to have amongst your teams so that the world can ultimately change, the technology can change, and the service that you're talking about specifically can change, but the principles and practices that you're applying create resilient technology, just like using the sensible defaults that Sarah mentioned.
**[00:34:19] Sarah:** I think now more than ever, we can start to see how some of these metrics that we look at within engineering teams, mean time to recover, defect escape rate, code coverage, test coverage, we can start to show to business people how these metrics roll up to business outcomes. This is where I'm spending a lot of my time at the moment working with engineering teams. A lot of teams have heard about the DORA metrics or the four key metrics, and then measuring the teams, measuring progress of improvements to it, but it's getting stuck at the engineering layer because it's not being translated into something that's actually meaningful to the business.
I think incidents like this, whilst they are unfortunate that they occur, actually give us really good opportunity, learning moments, so we can start to use these to educate some of the non-tech executives and the board members alike into how the way that we build our software is also so impactful to our business outcomes. How moving the needle on some of these low-level engineering metrics will affect things like customer success, will affect things like ultimately ARR. It will impact the quality of the product. Not only that, but also have a bearing of the total cost of ownership over the software that we're building.
We can start to paint that picture from engineering effectiveness measures and metrics, all the way up to business outcomes that we're talking about at the exec table and boardroom.
**[00:36:16] Kimberly:** It's a great point, Sarah. I think when these instances happen and they grab the attention of people that perhaps wouldn't necessarily be paying attention to more of the details of engineering practices, seize that moment and use that opportunity to help provide that connective tissue of here's why these things matter, and here's what we're doing about them. It's a really great point.
I did want to come back to the point of scale and not lose that thread that we had mentioned a little bit earlier. This was fundamentally a software issue. Obviously a digital footprint of it, but given the nature of how interconnected and so many different industries and businesses were using CrowdStrike, there's also very much a large physical footprint that was impacted by this. What's an organization to do when you have this incident at scale but it's also impacting you on both the physical and digital sides of your business?
**[00:37:28] Sarah:** It's funny the timing of the CrowdStrike one. I had a bit of a chuckle. In Australia, it happened at about three o'clock on a Friday afternoon. The blue screens happened, we all looked at each other. We're like, "Argh." Close our machines. Luckily we weren't responsible for repairing this damage. Now, that played out differently in Europe, Max, where you are. It was right in the middle of the day. In America, people were waking up to the fact. It was over a weekend as well. It impacted people's holiday plans and people's travel plans, but it impacted for like a day as well.
It wasn't a really long and ongoing outage like we have had in the past where-- I recall the Atlassian incident, which whilst it didn't affect everyone on a global scale like this, it definitely impacted a lot of software companies. Then I think about the Delta Airlines outage where it impacted at the peak winter holiday season. That failure that took down all their systems with 2,000 flight cancellations or something led to such a huge economic problem for the organization. It wasn't just the bill of the recovery, it was the reputational damage and the reputational outpay that they had to have as well.
The scale of this was impressive, but it doesn't negate. Every incident like this really impacts-- Even if it impacts a core number of people, there are definitely steps that we can take to apply to it. Thinking about what practices we've already put in place that we can start exercising from a disaster recovery perspective, start analyzing to see, who is solving it? What is going on? Are you adding to the noise? Can you sit back and actually just wait to find that fix that goes through?
Thirdly, what's our manual workaround for this? How do we get humans to where they need to be? I'm thinking more specifically around some of our critical systems like healthcare, our police departments, our fire departments. If everyone who wants to shop can just sit back and relax for a little while and we can get the emergent departments and the critical services up and running.
**[00:40:20] Kimberly:** You need good incident response so incident response businesses can get back up and running.
**[00:40:27] Sarah:** Yes. Exactly. I don't know, my perspective was a little bit, especially because it was a Friday afternoon, a little bit of a chill pill. "Hey, guys, it doesn't really matter at the moment for the large number of people. Let's just wait to see how this plays out and let's not panic." I think that's an important part. Don't panic through this.
**[00:40:45] Max** : It's cascading effects. Not only does the update push out in a cascading way, but then how that actually impacts the systems around our society starts to have this wave that ripples through your life essentially and through each country in its own different ways. Everybody is familiar with cloud computing, but I think people are quite quick to say, "Oh, I'm in the cloud," or "I'm running a cloud," without thinking about are you cloud-native or are you operating with the intended way of cloud computing?
What I mean by that is your ability to programmatically or automatically orchestrate and control aspects of this. I think even if you're on an on-premise data center and you're managing effectively your own private cloud, there's technology and there are practices and processes that you can put in place to respond to something like this better. I think it's going to be a serious wake-up call when this happens.
For those that are very cloud-native, it might just be a few commands, ditch a whole bunch of broken Windows virtual machines, and start a whole wave again. Then, before you know it, service is restored. All the way on the other end of the spectrum where you've got people managing their own servers, they're not doing it in a programmatic way, so swathes of humans have to run down to a physical data center with a bunch of USB sticks and keyboards, start plugging in and actually start manually resetting things.
I believe both of those extremes and everywhere in between happened as part of CrowdStrike. Again, to Sarah's point, those that were on the worse end of that are going to be having a very stark wake-up call in terms of how they need to redirect some investment towards the operational aspects of their systems.
**[00:42:58] Kimberly:** When this inevitably, as we've said, happens again, my takeaway is going to be to tell people, "You should have been playing your capture-the-flag and tasting your food beforehand so you wouldn't have that impact." I think just, to wrap up, one more point. I've heard both of you talk about, but I think it's good to reemphasize to close this conversation today, is it probably feels like there's trade-offs between rapidly delivering software and having a well-tested, reliable system. Listening to you both, it doesn't need to be like an either-or. It can be an and. There can be a balance. Final thoughts for how organizations can thoughtfully achieve that balance?
**[00:43:55] Sarah:** My mother always said, "Less haste, more speed." That's definitely what I see in this case. It's not about one or the other, it's about you can run really, really fast when you're smoothly operating and you're baking this in from the get-go. If you're not doing that today, it doesn't take a lot of effort to actually get to a point where you're running safely again.
**[00:44:22] Max:** Yes. I was just going to slightly augment your tasting the food comment there, Kimberly, because I think the tasting the food analogy or metaphor is around testing and doing as much as you can upfront. I think a lot of what we've talked about here today as well is around your response and ability to respond and how resilient you can be around that. I think there's a balance there. There's only so much you will really be willing to invest in preparing for possible inevitabilities, but you won't be able to think of everything. Why not then invest in how quickly you can respond and safely you can respond all the way?
I love that Sarah talked there about this idea of, in that incident management frenzy, there's a lot of work being done by large companies now really meticulously. As an engineer, I just wake up in the morning, how do I then step into this incident manage where someone else can go back and get sleep? Because if you roll back the clock 10 or 15 years, people would spend two days without any sleep, knocking back the coffee, and that created even more problems. Thinking about these two sides of the problems, investing for preventative, but then investing in responsiveness, I think is really key.
**[00:45:40] Kimberly:** Thinking about what we can do pre, but also being really prepared for what you need to do in post. Sarah and Max, thank you so much for today's conversation. I learned more about why my family was stuck in the airport and what organizations can do so they can avoid that in the future. Hopefully, our listeners found some practical tips and takeaways so they can pressure-test and challenge their organizations for how they can respond to this a little bit better next time it comes around.
**[00:46:14] Sarah:** Thank you for having us on, Kimberly.
**[00:46:16] Max:** Yes. Thanks, Kim.
**[00:46:17] Kimberly:** Anytime.
**[00:46:18] Max:** Bye-bye.
**[00:46:20] Kimberly:** Thanks so much for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcast. If you enjoyed the show, help spread the word by rating us on your preferred podcast platform.
[music]
[00:46:47] [END OF AUDIO]
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