<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/the-human-side-of-data | Title: Humanizing data strategy: The human side of data | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Humanizing data strategy: The human side of data 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Markus Buhmann | Podcast guest  Tiankai Feng and Sebastian Kaus
February 25, 2025 | 40 min 27 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/the-human-side-of-data#transcript)
Listen on these platforms
## Brief summary
When we think of data, we think about numbers and statistics, but we don’t often think about people. In the second episode of our [Humanizing Data Strategy](https://www.thoughtworks.com/insights/books/humanizing-data-strategy) series, we discuss why storytelling, empathy, and creativity are all crucial parts of a successful data strategy. This podcast is for you if you’re a data leader looking to communicate and influence data strategy more effectively in your own organization. You can explore more about data gamification [here](https://www.sigs.de/artikel/der-einsatz-von-gamification-elementen-fuer-das-data-management-bei-vattenfall/). 
### **Episode highlights**
  * Tiankai says that data governance used to be all about customer data, or master data, but thanks to increasingly digitalized processes, more and more data is available, and more sensors are available in different industries like in manufacturing, which is creating a lot of information.


  * With data governance, focusing on a lot more data that is a lot more granular and having a much higher quantity than we see in customer records, requires organizations to rely a lot more on defined processes, guidelines, and automation as much as possible, because it isn't possible to manually actually check all of these data sets anymore.


  * Sebastian explains that at Vattenfall, the moment they uncover something that's difficult or annoying to people, they take that as a first step to improve because it gives them an intrinsic motivation to improve. 


  * Tiankai says when you follow a use case-based approach, you have a very clearly mapped business context. If you want to do something with data, then it's for a specific business purpose, and that means you actually know what the value of the data is.


  * Sebastian suggests that gamifying data governance is a great way to get people on board. For Vattenfall, rewarding people was a huge game-changer. People are now actively reaching out to do data governance, which was unheard of previously.


  * Tiankai says that allowing people to experiment, make mistakes, and fail is important when fostering a culture of data innovation.


  * Sebastian shares some useful info for listeners, including this [gamification case study](https://www.sigs.de/artikel/der-einsatz-von-gamification-elementen-fuer-das-data-management-bei-vattenfall/).


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
### **Transcript**
[00:00:00] Kimberly Boyd: Welcome to an exclusive Pragmatism in Practice podcast takeover, Humanizing Data Strategy, guest hosted by Markus Buhmann, Data Strategy Principal at Thoughtworks. In this series, we'll speak to leaders who have successfully bridged the gap between analytics and real-world human needs. We'll explore some of the ideas and strategies they've leveraged, equipping you with insights you need to create a sustainable and impactful data strategy in your own organization.
[00:00:26] Markus Buhmann: Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories or practical approaches to becoming a modern digital business. I'm Markus Buhmann, your guest host for the second episode of our Humanizing Data Strategy podcast takeover. I'm joined by the author of the book, my colleague, Tiankai Feng, the Head of Data Strategy and Governance at Thoughtworks. Hi, Tiankai.
[00:00:46] Tiankai Feng: Hello.
[00:00:48] Markus: Today we're joined by Sebastian Kaus, the Head of Data Governance at Vattenfall, a company at the heart of getting the world to net zero.
[00:00:57] Sebastian Kaus: Thanks for having me.
[00:00:58] Markus: It's great to have you here. I guess we just want to first dive in. Tell us a bit about yourself, Sebastian, and tell us a bit about your role at Vattenfall. What does the Head of Data Governance do for a fossil fuel elimination company?
[00:01:16] Sebastian: Yes, I'm Sebastian Kaus, living in Hamburg, working for Vattenfall since six years. My actual profession is engineering, actually, so I'm an electrical engineer. That's also how I basically got into this whole topic. I started off as an analyst for wind turbine data. All of us know that typical analysts' daily schedule is 80% finding, cleaning, preparing data, and then 20% fun, in a good case. That wasn't appealing after some time at least.
I started off studying again business informatics with a focus on data science to also tackle this whole data challenge a bit more strategically. Basically, I grew from being an analyst into more strategic tasks in terms of data engineering, so building the pipelines. That's how I also interpret the role as Head of Data Governance in Vattenfall to set the boundaries, the guidelines to exactly build those pipelines. A bit like creating traffic rules for data, so that more or less flows smoothly without too much interruption between different systems.
Yes, if things go wrong, that we have something at hand to remediate basically what happened. Yes, that's also what I'm doing in the end. It's a role in the, let's say, more central IT. It's a bit like a moderating coaching role almost in that sense. We have many different businesses from our hydropower plants in northern Sweden, which operate for 100 years. It's actually quite difficult to tell them that now they need data when they have operated successfully for 100 years. We also have, of course, now the, let's say, smart grid and smart home and you name it, basically.
The most recent developments when it comes to electricity and the electricity market, and where we want to have live insight into consumption and production and trading and so on, and bringing those together is the holy grail, basically, of the energy industry to have supply and demand always in balance. The more we are able to control it and to have insights to control it, the more efficient we get. Actually, what I'm doing is, in my opinion, of course, everybody says it about their job, and very much at the core of what we're doing, because I'm dealing with the information that helps us to make the right decision to reduce our carbon footprint, to reduce CO2 emissions, and make us efficient and successful as a company.
[00:04:05] Markus: I wanted to pick up on something you said there, and Tiankai, please jump in. I guess one of the bigger challenges that you would find in an organization where you are thinking about things like smart grids, wind turbines, sensors, batteries, all of those sorts of things, is the sheer volume and variety of data. Now, big data is something which people roll their eyes at a bit nowadays and think is a bit passe, but I imagine that's going to be right at the heart of the challenges that you face.
[00:04:35] Tiankai: No, I think definitely what I've also noticed with generally data governance, that while it was focused more on the, let's say, commercial processes in the past, it was all about customer data, master data, and all these kinds of things, that with increasingly more digitalized processes, more and more data is available, and there's also, in return, more sensors available in different industries like in manufacturing as well, for example, where all of these sensor data is creating a huge load of information.
With data governance, then focusing actually on a lot more data that is a lot more granular and having a much higher quantity than we see in customer records, for example, you can actually have to rely a lot more on defined processes, guidelines, and automation as much as you can, because there's no way that you can manually actually check all of these data sets anymore. The shift actually from being this authoritative manual process of governance shifts more towards more automated and, let's say, human-driven, but technology-enabled way of governance. It's a really exciting time to be here right now, especially with all the hype around AI and stuff. That is all part of the game now.
[00:05:49] Sebastian: Yes, it's a lot of data. It's a lot of different and large variety of data that we have, not just documents, but also time series and in all forms and shapes, and sometimes even screenshots with whatever data on them, and then they are being used for whatever. The format even is as many as you can think of. That's why I think it's actually not so much a technical challenge because it's all there more or less, but it's really about understanding the context of the data and understanding what other people mean when they provide you data and what they were basically using this for or how it should be used for. That's maybe even the bigger challenge, not the variety of data, but the variety of context of data and then use it properly. That requires a lot of alignment and communication and sitting together and providing that context.
[00:06:48] Markus: It's really interesting you say that. The American novelist Thomas Wolfe, he said the United States and the United Kingdom were two countries separated by a common language. I see that is what you're getting at in that point. I imagine different parts of your organization with different focuses, so your hydro and your smart grid and everything, they might have terms and definitions in terms of art, which are the same, which clash, which are subtly different. How do you navigate that in your role and how do you bring those people along to a sensible consensus, if at all?
[00:07:26] Sebastian: Yes. If I had a simple solution, that would be great. It's certainly not simple. In Vattenfall, we follow a use case-based approach. We figured out it's not advised at all to create a big governance program and tell everybody to do governance by whatever, 2020 something, and then hope it will magically happen because it's on the agenda. Yes, it might create some certain attention to the topic and people might even do stuff, but it's then not, let's say, intrinsically motivated.
We usually go by use cases and what people, interestingly enough, do across the board through different cultures. They like to, let's say, complain or bring up challenges in that sense. The moment we figure out something is difficult or annoying to people, then we take that as a first step to improve because then they also have an intrinsic motivation to improve. Based on whatever problem they are bringing up, we start basically finding solutions for that.
For example, if somebody says, "I always have to send that email to that one colleague to explain the latest changes in that data set, or if there's something not clarified or properly documented, I spend hours and hours in meetings or whatever to express myself or to clarify the situation." Then we basically start with that and we agree that we should maybe have a common definition or a common documentation where everybody can access that. For us, that's data catalog. It's a no-regret topic, basically, and sometimes takes a bit of time, certainly that people understand that.
I have a lot of analogies from real life, so to say, and I always compare it a bit to, let's say, the catalog of a large Swedish furniture company that you would usually consult before you go to the actual warehouse to not get lost on a Saturday afternoon. It's the same with data catalog is it simply helps us navigate through that vast amount of data and provide and put context to it. That's how we try to overcome it. Again, use case-based. It's an incremental step-by-step approach and providing context based on the biggest pain.
[00:09:46] Markus: Tiankai, I think there's a couple of things in there that were really interesting. We wrote an article about thin slicing, which sort of pushes that use case-based approach to the forefront. There's something in there about communication and empathy, I guess, which I think, we were talking about before. Do you want to maybe expand on that?
[00:10:08] Tiankai: Absolutely. I think, especially when you follow a use case-based approach, at least you have a very clearly mapped business context around the tool. That if you want to do something with data, then it's for a specific business purpose, and that means you actually know what the value is of the data. Going for a use case-based approach makes it actually easier to then find and define the value of data because, behind each use case, you ideally have a business case to either it's connected to a business process, or it's connected to a licensing, something commercial where you actually can get to a quantified way of actually estimating how much the value is, which then in return actually helps to prioritize certain use cases over others.
On the other side, and this is also part of the book, in terms of the communication part, just going for commercial or organizational value is not enough. It's the rational side of things that everyone should actually agree that those commercial goals of an organization is important, but people individually and personally might not actually care that much. They convince themselves to care about it, but it doesn't really have a lot to do with a day-to-day.
Actually, focusing a lot more on the personal aspect and the personal reward of people helping with data quality issues or any data issues and data governance is really key there. Also one of my basically learnings is if you can fit in both narratives in one to say the organizational goal is this, it's undeniable, but for you personally, as a group, you will get this out of it, then you actually have a very nice narrative that everyone can get behind too. It moves from this rational and motivation to a more intrinsic emotional motivation to actually support the cause.
[00:11:49] Markus: I think there's something very important there as well to add. The motivation is driven by people's incentives and they can be extrinsic, you're going to get a bonus, or intrinsic, the desire to do a good job or even to have fun with it. This is something that I was really fascinated by, Sebastian. You've taken the really, really novel approach of gamifying data governance. Now, Tiankai and I have been in this lark a while, and you tend to find similar stories.
People would buy access to a framework, a DCAM or a DAMA, and then they go through and check things off one at a time. With your use case approach and your targeted and personalized, I'll use that word advisedly, approach to generating value, you've taken that one step further and put gamification around your data governance processes. Can you tell us a bit about that and tell us how gamification makes some people a little suspicious, how you overcame that, and how that's working?
[00:12:51] Sebastian: Yes, it's definitely a very interesting topic. It was born almost out of desperation because when I started in this position, I had really difficulties to motivate people because, who am I from somewhere in Germany telling someone in Northern Sweden or the Netherlands or whatever that they should work better now with data and get their act together and document stuff and whatever? It's actually the image of data governance, but it's the most unthankful task to do. That's how you get basically asked to leave the room in no time if you do it incorrect.
I was trying to flip it around and I was trying to understand what is the motivation of the people working in their job, basically. I'm an engineer myself, usually, especially engineers, so to say, they have profound knowledge about their assets and how they should be run and how they work and how they don't work. They don't like to be told how or what to do basically. They also like to share sometimes stuff and usually, it's more about how to make it easy to share your experience. If we reward basically sharing and trigger, let's say those very human, let's say, attributes or behaviors, and then maybe we get a bit closer.
We first started off by not forcing people to put stuff in the data catalog, but really leave it a bit to them to put stuff in. The first step was really making use of, let's say, Cunningham's Law, which is basically saying, if you want to have a correct answer on the internet, post something wrong. That same story basically holds for the data catalog that we allow people to make mistakes and people learn through mistakes playfully. That was the key, let's say, ambition at the beginning to invite people to play and make mistakes, and to not make it a scary topic.
Eventually, we grew further in this thinking and started to collaborate also with a startup from Munich actually. They listened to some other podcasts where I was presenting this idea and they said, "We want some feedback on this." Eventually, we collaborated and developed that system that basically integrates, very important, into existing tools, shouldn't be a new one. The backend is basically connecting based on quality rules for the database of governance tasks, connecting information and sends out small tasks, small teams messages, directly to the people they can fix it.
They would for each and every interaction, which is usually quite tiny to just correct the value or write a short description for each and every one of that, they would get points, they would collect them, and they would be then aggregated, summed up. There are leaderboards with, of course, anonymized. It triggers really this people want to collect stuff and get some tangible result after they've done something. We've been deep into human behavior basically. I should have studied psychology maybe a lot more than data science in that sense because that's what we try to achieve here.
It's really about, and it's maybe also some important analogy here, this reward mechanism for people like, what do I have from doing something? Is it some empty promise at the end of the year? Is it something I have right now today as a reward from what I'm doing? That basically was a huge game-changer. People now actively reaching out to do data governance, which was unheard of when I started this. They ran away and it's sadly still the image of data governance. Even within Vattenfall, that it's something bureaucratic, something on top.
I hope that this will change more and more. The good thing is also if other people have made good experiences, they will share the story out as well. Then the whole train basically gets traction and speed. That's in a nutshell basically what we did and how we do data governance by keeping it as simple as possible and rewarding even the smallest activity, making it therefore somehow beneficial for the people actually doing it.
[00:17:28] Markus: What's the shape of the rewards look like? I'm sure everybody is wanting to know how that works.
[00:17:33] Sebastian: Yes. In the end, it's basically, simply creating or giving out points and that's like some sort of, let's say, fake currency in that sense. You can then trade in those points into whatever you like. We can have the standard pizza party at the end of a data quality project initiative, you name it. The leaderboard, maybe you tie the points to your yearly performance review that you say, okay, you should be, at least in the top X percent of people active in this field. It doesn't matter. I don't even care.
That's why I don't have too much examples anyway. The good thing is that people don't feel left out anymore. They don't feel that the activity they are doing is basically worthless because that's what it feels when you need to go into, let's say, SAP somewhere fixing that one field of an important entry, but nobody recognizes it. Even if it's at the end of the week team meeting and nobody would say, "Oh yes, thank you for fixing that one value. Now we can finally avoid that million-dollar mistake." Doesn't happen.
The small incentive of saying, "Okay, it's not wasted," so to say, or a batch that you get, you single-handedly fix SAP or you are the search dog for data arrows in that database, whatever. You can even have a lot of jokes and fun around that basically that people are recognized in the end. That's very important. It can be whatever they personally like. A small gift from the gift shop.
[00:19:16] Markus: That's so cool. This wouldn't be a data and data governance discussion without a data question. With the increase of points in the tracking of that information, what is the relationship you see now between those increases and data issues? Are you nailing that really easy data issues first and covering some really gnarly ones or what's going on there inside your estate?
[00:19:42] Sebastian: In Germany, we have the workers council and they are very attentive on all those things. We had a lot of red flags here. Cloud Microsoft Teams in that particular case, gamification, chatbots. They were like trigger words all over the place and how do we basically made it happen in the end. It's not like it's not even made up in that sense. It actually is at the core of the idea. We make it easy for people to get the job in the end done.
It is also for them a useful tool that helps them to overcome the struggles they have with the vast amount of data and the vast amount of context they see every day. It's a useful tool that basically makes them more efficient and ensures they can actually do their job properly. It's very important here. It's not just about gaming and having fun, so to say, but also about making people work in a more convenient way again and basically working also as it should be in today's day and age.
[00:20:51] Tiankai: Everything as Sebastian just said is actually very interesting. I think there are some other learnings in there. That, for example, recognition is so important to people on a personal level. I feel like the bigger an organization is, the more people are actually craving for recognition because you can seem like such a small cog in a huge machine, and that you actually get the deserved recognition of having done something important. Also, with the gamification part, making it easy to fix problems. That if you get the right interface, and usually people, they want to help with solving problems, but it's too complicated to solve it, and they give up on the way. If you give them just a simple interface to solve it, the threshold was so little to just do it. Just it's in front of you to start doing it. I think those are really two other nice learnings about it.
[00:21:40] Sebastian: What we also saw, now it's just came back, we saw people collaborating a lot more and a lot better because it was tangible. The data quality problem or that the governance task they had to do was all of a sudden so tangible that they could easily talk about just that. Maybe some people who work in this field know that discussions about an issue usually explodes and you will find all kinds of issues and potential or obvious or maybe related root causes that you get lost.
You will never have a meaningful discussion for longer than half an hour in this field because it will be so distracted and basically the finger-pointing starts and yes, but IT, the business and whoever in between. That was all of a sudden not that present anymore because we had a very concrete error that we saw and the people who were basically affected could directly interact because you can also forward the issue, basically put an envelope on it, and send it to someone else and say, "Oh, please have a look." We saw that people even started to discuss the actual root cause.
One time we figured out that there was an error in some API integration, which was pushing data from one system to another, and they figured out there was a pattern in the errors. They, "Oh, it's another one of those errors here in this data set. I've had those. I will reach out to the person in charge of the API to have a look." Then we fixed basically that integration and all of a sudden we fixed a thousand or whatever, a lot more data issues. This efficiency, very concrete on a particular error, I've never seen that before for sure. That was also really mind-blowing for me to see that people are very efficient at fixing those things and not start pointing fingers.
[00:23:40] Markus: There's something I wanted to pick up on that: the classical formulation of data governance. This is something that I'll put words in Tiankai's mouth as well, is that we don't agree is a good pattern, is that there is a data steward and it's their job to make sure that the data is of the highest quality. Then there's a data owner and then all those names and roles. For your process, are you empowering the end users as well to work through this and collaborate with one another? Those classical data governance roles are almost like coaches and referees if you want to stretch an analogy.
[00:24:17] Sebastian: I was referring earlier to the engineers who have profound knowledge about their work and they have it. They also sometimes, let's say, like to brag about it because yes, it's a good, let's say, knowledge as well what they have and addressing them as experts who also correct, let's say, or make sure that the power plant is running properly in a particular case. They know what information is needed. Engineers, they work with data all day, basically, maybe not in a database in that sense, but they know what correct and incorrect means and then how the settings of a power plant should be and so on.
They are the best data stewards in that sense that you can wish for. They just don't like to be called like that, because they are engineers, and they are experts. That, again, basically addressing them as what they actually are, instead of giving them, let's say, another hat or some title they don't really know what it means, rather creates friction. We avoid that as much as possible. Simply ask those people to share their knowledge. That works wonders by recognizing what they actually are and how they can contribute.
Usually, that's quite easy for them to then start documenting stuff, or fixing some incorrect data. Later down the road, we can say, "You are now by the way so called data stewards." You can forget that again because it doesn't matter. That's more important those people do the work of a data steward. That's way more important than any title we could give or whatever training we could provide to them, because they already know how it should be done and how it is done. Why not simply keep it pragmatic here and just let people do their job?
[00:26:01] Tiankai: Absolutely. I think what is also interesting about that, because you basically are democratizing that role. It's based on people wanting to do it and doing it already, instead of first giving it a name and then appointing someone. You get it from there that they bring their own creativity with them too. They actually have their own unique experiences. They know how to think differently than any central data governance lead could ever do. They bring all their different experiences with them. I feel like also with having different perspectives and data governance can really help innovate data governance in a way and also innovate data practices generally.
[00:26:41] Sebastian: Yes, absolutely. I think this approach of having a theoretical-- It's good to have the theory basically and understanding definitely it's important. When it comes to rolling it out to make it happen, it's best to follow the people who should be doing it and follow their individual interests, and then you will be much, much more successful than shoving some framework over them and then try to put them in the box, which they don't think they fit in.
[00:27:13] Tiankai: Absolutely. You said also before that, because of how you allow people to make mistakes. That is how I would always call it as part of an experimental culture that you can only create innovation if you let people experiment and not all experiments always work. Failure has to be an option and has to be acceptable too. Have you felt like that there was a real cultural change that through in your initiative, allowing mistakes that people generally got looser, and they all got more creative and had more ideas all of a sudden?
[00:27:44] Sebastian: It's difficult to speak for the whole of Vattenfall or for everyone because we are quite diverse. There is many different areas who are adopting data governance with their own company culture. Again, we have parts of the company in Northern Sweden, and then some in the Netherlands, and in Germany as well, and of all day age, and you name it. It's very much also about the people you're interacting with. There is no general answer. A culture change is what I noticed when people are successful.
When they see, "Oh, this, it does something positive to what I'm doing." Then they are also very eager to do more because they see it helps them personally as well, because they don't need to explain themselves so much anymore. They can share or collaborate easier with other colleagues. That's definitely nice to see when people write the first description, and they can share it and get traction, and then also inspire others, so to say.
I may be quite present, and I'm of course, advocating the topic, but I have not the level as someone from the business, let's say, within the same organizational unit who would say, "Oh, by the way, I've documented my tables here on my attributes now. I save a lot of time, or the collaboration with the other departments, all of a sudden, super easy, because we don't need to meet every week to discuss the latest errors in our data set." That is basically the biggest change. I always do a little dance of joy, so to say, when I see that people actually are successful when they have such an achievement.
It's difficult to measure that cultural shift, so to say, or that change, because it's also something natural that people are happy. Measuring it would be a bit weird. It's always great to see that individuals change. A lot of individuals who are changing eventually also change then the company. That, of course, takes time. It's also a process that's never done. There will be no final level to achieve, so to say. The small changes are actually what makes it enjoyable actually.
[00:30:06] Tiankai: Since we talk about culture, culture famously needs both the people on the ground to bottom up, change the culture, as well as leadership, changing a top-down. Would you say that you had at the very beginning already a lot of support from your leadership to gamify data governance in your case, or has that slowly been adopted and then been endorsed by leadership? How was your journey in getting buy in from leadership basically on this one?
[00:30:31] Sebastian: I'm very thankful for that sponsor who was allowing me to do something crazy. It must've been looking crazy from the outside. Maybe if it was so super obvious what would happen in that sense, there might or would have been second thoughts? I don't know. Like, "Oh, should we really do it?" There was a lot of trust, and that's what I'm very thankful for. I think in the grand scope of things, it's still an early stage.
A lot of misunderstandings that governance because of a term has to be something rigid or something where you are about correct or incorrect, where you follow up and then where you make people do it, so to say, and that changes only slowly. Hypothesis of mine, I sometimes have the feeling that from a certain level in higher management, the bad news, so to say, are not that transparently communicated anymore. For example, the data quality in certain data sets or the data which is used to make an important decision on.
I think some of those people in senior management would be thinking twice if they knew actually where some data and decision is based on or on what data some decision is based on and how it basically is created. That's, I think, true for every company in the world anyway. I'm hoping also that when people understand and see, because we have also dashboards, of course, that indicate the quality, and show how improvable it is here and there, that they will be more aware and then also show more support because usually data quality is measured and communicated, but not so much fixed because it's so difficult to fix it.
We have the unique and very comfortable position now that we can say, "Yes, it looks quite bad. Yes, only 50% is whatever credible, but we have a way to fix it. It might take a couple of months, but we can do it." Then when the realization is there that this is the case, that they will also support this on a much higher and broader level, so to say, as of today, because I think today, the awareness is sometimes not even there that I will have to change latest now with the rise of AI, where you can't blame it anymore that your report is not good enough. Also, the people putting in the prompts for some analysis or whatever. They also, of course, don't do mistakes, so data is left. It must be the bad data, which is actually very often true. We are slowly, but steady getting to the source of the issue that the data should be in good shape and that this is universally understood is happening, I think, rather sooner than later. Then also the support starts.
[00:33:27] Markus: How does that support look like with the venerable engineers in the hydro plants and the dams in the North of Sweden? How are they coming around to this? Are they coming around to the fact that maybe having data and up-to-date data and good quality data is going to help them, or are they still obstinately pushing back on you?
[00:33:50] Sebastian: They are an example, first of all, like a prototype of a typical person that you could meet potentially in Vattenfall. I'm not blaming them at all, but just to show the diversity of Vattenfall basically. What I really see is, and that was interesting actually from our IT department, we put up this platform now, and we have our IT systems, of course, where you can order them the services, you name it. Of course, they need to be put into those systems.
After I had an initial call with the colleague who was in charge of that, the colleague reached out again and sent me a message and said, "Our data for our tools and software, and that are putting in the system also doesn't look too good. Can we use that platform also to fix our own stuff?" That's definitely happening. That's maybe the most enjoyable part when people now come back and say, "Yes, I admit there is something to be fixed, but we can fix it." That's maybe the biggest changer here as well, or the biggest change that we can fix it now. We having means to fix it and not just pointing fingers.
[00:35:00] Markus: That's really at the heart of all of this. This is something that Tiankai talks a great deal about in his book, is that data governance, the stereotype is this distant, bureaucratic, grey, machine. What you've done now is that you've really underscored one of the themes in the book, that there's people at the heart of this, and there's people who have to collaborate, and there's people who have to talk, and it's messy. It's tricky, and people have their agendas and things, but they're starting to come together on this. This is a tremendous story. Tiankai, do you want to add anything to that?
[00:35:38] Tiankai: It very well fits to the emphasis of this episode of communication and creativity. I think Sebastian shared a lot of how he not only changed the way of communication around it, but how not only he and everyone else actually got creative, and how they actually combined these skills and traits into making data governance more successful and impactful. Yes, all very good.
[00:36:04] Markus: Do you have some case studies, or do you maybe even have some other sort of conversations that you've had, lectures, and things that you've given? Because I think this is a really, really powerful, powerful story about how communication and creativity can make what people sometimes think is a very dry topic vital and important and, dare I say it, fun. Is that something that you can share with people?
[00:36:33] Sebastian: Yes, links to other podcasts. We even have some articles written. There is quite some material that can be shared, and I'm also happy to share it. Basically, what we did in a nutshell is that we put the business and the purpose of what we're doing at the center again, and of course, the humans working on that at the center. What can be more fun than working with great people and interacting with them and sorting out things? That's what we just tried to put in the center and make it as big and as enjoyable as possible and basically take out all the dry, gray, theoretical stuff that's not so enjoyable. Flipping basically the whole thing upside down was maybe what we did in a nutshell. It's great to see it turns out that great in the end.
[00:37:30] Markus: I've got to say it must have been a big sigh of relief from your sponsor to see this on the face of it, let's say novel approach to data governance, take root and succeed.
[00:37:42] Sebastian: Yes. There was a lot of trust, as I said at the beginning, but I think there is some relief. Not that there was a lot of doubt in that sense, but also quite a relief to see that it turns out so great, because, yes, you never know. We are just starting, actually. We are a large company. Things take an awful amount of time sometimes, and we are just getting started. I can't wait to see where we are in two years and then looking back, actually, what we did in the past, how we've been working in the past, how people were dealing with those things in the past, and how they do it today. Definitely great times.
[00:38:20] Markus: I guess the one thing will be at the end of it, the true proof of it is how much time do your data scientists spend wrangling data? Is it the 80% that everyone talks about now? What is that percentage of their time going to be in two years' time? I guess we'd love to hear back from how that's panned out, how it's gone. Tiankai, I just want to say, do you want to add any thoughts before we close the podcast for today?
[00:38:48] Tiankai: No, not really. This might be actually a great transition to our next episode when we do it again about competence and conscience. Now that we talked also about people having the right skills to do it, it's about how we grow competence in a more equal way across data and business professionals and experts and how we can also apply critical thinking on a human level, actually, to the right things, which is also in the heart of data governance. Yes, I'd say to the listeners, they can stay tuned also for the next episode.
[00:39:22] Markus: Sebastian, do you have any final thoughts before we wrap up for today?
[00:39:27] Sebastian: Thanks for having me. It's always great for me to share the story and to have people also listening to it. I'm very thankful to be able to make a small change, so to say, in this big topic and to actually make it tangible and see the positive outcome eventually. Thank you for having me.
[00:39:50] Markus: No, thank you, Sebastian. Thank you as ever, Tiankai. Thanks, everyone else, for joining us for this episode of Pragmatism in Practice. If you enjoyed this episode or have any questions, please feel free to reach out to us on LinkedIn. My and Tiankai's and Sebastian's details will be in the show notes. Don't forget to tune in to our next episode, where we'll dive into the topic of competence and conscience, and data ethics with our VP of Data and AI, Emily Gorcenski. Thanks very much, and see you next time.
[music]
[00:40:35] [END OF AUDIO]
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