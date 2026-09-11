<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/measuring-developer-experience | Title: Measuring developer experience | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Measuring developer experience 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Scott Shaw and Prem Chandrasekaran | Podcast guest  Abi Noda
August 22, 2024 | 41 min 46 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/measuring-developer-experience#Transcript)
Listen on these platforms
## Brief summary
Trying to measure developer effectiveness or productivity isn't a new problem. However, with the rise of fields like platform engineering and a new wave of potential opportunities from generative AI, the issue has come into greater focus in recent years. 
In this episode of the Technology Podcast, hosts Scott Shaw and Prem Chandrasekaran speak to Abi Noda, CEO of software engineering intelligence platform DX, about measuring developer experience using the DevEx Framework — which Abi developed alongside Nicole Forsgren, Margaret-Anne Storey and Michaela Greiler.
Taking in everything from the origins of the DevEx framework in SPACE metrics, to how technologists can better 'sell' the importance of developer experience to business stakeholders, listen for a fresh perspective on a topic that's likely to remain at the top of the industry's agenda for the forseeable future. 
  * Read the [DevEx Framework paper](https://queue.acm.org/detail.cfm?id=3595878)
  * Read Abi's article (co-authored with Tim Cochran) on [martinfowler.com](https://martinfowler.com/articles/measuring-developer-productivity-humans.html)
  * Listen to Abi's [Engineering Enablement podcast](https://getdx.com/podcast/)


## Episode transcript
**Scott Shaw:** Hello and welcome to the Thoughtworks Technology podcast. My name is Scott Shaw and I'm one of the regular rotating hosts on the podcast. I'm joined with by my co-host, Prem. I'll let him introduce himself.
**Prem Chandrasekaran:** Hey, folks, I'm also one of the other regular podcast hosts here. Very glad to be here.
**Scott:** We are lucky to be joined today by Abi Noda. Abi is one of the authors of an influential paper on developer experience metrics, and we'll let him talk about that. He's also the founder of a company called DevEx, which is, it's a unique product, I think, that assists with surveying developers and displaying and analyzing metrics from the delivery process. Again, I'll let Abi talk about that. Abi, do you want to introduce yourself and give us a little background?
**Abi Noda:** Sure, yes. Thanks for having me on the show. Excited to be here. My name's Abi. I'm a programmer, researcher. I'm currently the founder and CEO of DevEx, where we help organizations measure, improve, understand productivity. I spent about seven years in this developer productivity Space ever since I first became a manager and then started a former company focused on developer analytics, which was acquired by GitHub and then at GitHub focused on this problem internally for a number of years. Spent a lot of time in this whole developer productivity problem Space. Too long, I'd say. Excited to unpack some of that today with you guys.
**Scott:** Some of this came out of the work done at the Microsoft research lab with the Space framework. You've worked with Nicole Forsgren on some of this.
**Abi:** There's been a story arc to all the developer productivity stuff, with Dora being, of course, something Nicole created almost a decade ago now, and then while Nicole and I both worked at GitHub, part of Microsoft at the time, the Space paper or framework was published right around when COVID had begun. Then Nicole and I still work together today, she's at Microsoft, but is also part of the research team here at DevEx.
Nicole and I have published a couple papers recently, one of which is the DevEx framework, which I'm sure we'll talk about today, as well as a more recent study looking at the impact of developer experience, which was a joint study with GitHub and Microsoft. Nicole's been the continuing thread across all these different things. She's obviously a brilliant researcher and thinker in this Space, so it's been an honor to be able to work with her.
**Scott:** I think bringing this, the rigor to research in this area, I think, has been really important. I'd like to get into that a little bit later, but let's dive right in because I get asked all the time. I visit a lot of businesses. I talk to a lot of CIOs and CTOs and engineering managers. There seems to be, have been for the last couple of years an enormous interest in measuring developer productivity. That's a term that always makes us a bit apprehensive when we start talking about developer productivity. In your opinion, why shouldn't we or should we be measuring developer productivity?
**Abi:** I would argue it's always been a big area of focus. Every now and then it becomes spikes, with COVID for example, then now with GenAI. It's always been this elusive problem that we've all, I think, collectively as an industry and as business leaders, been trying to solve. It still feels unsolved, although I think we're getting closer. Why should you measure productivity? If you spend millions or tens of millions or hundreds of millions or even billions on R&D at your organization, you want to maximize that investment. How are you going to maximize that investment without getting an understanding of, A, how you're doing and, B, how to get better?
I think that's ultimately where this problem always stems from. Whether it's a CEO asking that question or the board asking that question, or if you're a platform engineering leader or developer experience team that's trying to define your own charter and determine your investments, you need to be able to answer those questions as well. It's an important problem. As a result, it's no surprise that there's a lot of tension around it.
**Scott:** I think there's a lot of misunderstanding, though, around productivity and that we use that word in a lot of different ways. We use it, economists use it in a very rigorous, specific measurement way. I feel like people are trying to take that and apply it to the field of software delivery, where we use it in a much more like we feel productive. It's a loose concept.
**Abi:** Space, for example, the whole thesis of that paper was productivity is complex and it's multidimensional, and we can't just boil it down to lines of code or commits or whatever the output measure of the day is. A lot of organizations that we work with and I talk to are spending years, sometimes years, trying to come to an answer around how do we measure productivity? What even is productivity? Of course, we've published research on this and, to some extent, I think that's really advanced the discussion. At the same time, I also recognize that now there's just more perspectives and more angles to this problem, it only grows more complex. It's a fascinating problem.
You mentioned the conundrum around how do we measure knowledge work and development work that's so different than other types of work, labor and even business functions? Peter Drucker wrote a paper in the 90s about this called, Knowledge-Worker Productivity: Our Biggest Challenge. I only recently came across that paper, but it blew my mind because all this frustration, all the dialog around whether you should or shouldn't or can or can't measure productivity, Peter Drucker was talking about this 20 years ago, this exact problem. It's encouraging in some sense validating to know that even this really is a difficult problem.
**Scott:** I'm going to read that now.
**Abi:** Great paper.
**Prem:** I do have a question related to that. Our foundational beliefs came from Martin Fowler, definitely influenced a lot of it. He very famously wrote an article on his Bliki saying that you cannot measure productivity. What is your take on that? Is it possible to measure it? Is it not possible? Is it a good idea? Is it a bad idea?
**Abi:** It's funny. Martin gave me the great privilege of publishing an article on his blog recently about measuring productivity. He seemed accepting of my perspective on it. I've often shared that article by Martin. I think he captured-- that was written 15 years ago or something, which is really funny to think. We're still having the same debates, 20, 15 years later. I agreed with everything he wrote in that article he talked about. Inevitably, every business tries to measure productivity and lines of code and function points and this doesn't work, it feels impossible. I agree with his observation of what doesn't work.
I wouldn't agree with Martin from a standpoint that there isn't an answer to that question or that there shouldn't be. I think there needs to be and there is. I think there's some discomfort in that. It's not a simple answer and even today it's not a clear answer. I do believe there's a way forward, and that's why I've spent the last seven years of my life and we're publishing all these papers and trying to figure this out with the best researchers and best companies in the world that are trying to also solve this problem.
**Prem:** What you're saying is there is light at the end of that tunnel where we can measure the right things and you actually drive the right insights is what I'm hearing from you.
**Abi:** Absolutely. That's the business I'm in. I'm biased, but we'll talk more about some of the newer approaches that we're leveraging to do that. Today, I think we are closer than ever to having a clear point of view that both developers, managers, CEOs, boards, investors, that everyone can be aligned around to have a clear view on that question.
**Scott:** We should probably get into what is the DevEx framework and what are the metrics that you're advocating people use.
**Abi:** I want to set a little bit of context on how the whole DevEx framework and paper and research, where that originated. If you were to go back and read the Space paper, the Space framework, The Space of Developer Productivity is the title, it talks about how productivity is multidimensional. In particular, if you read through the paper, there's a lot of emphasis on the importance of self-reported and perceptual data in our understanding of developer productivity. It talks about things like developer satisfaction, or developer's perspectives and observations on how things are going.
One of the things that happened after Space was published was everyone started asking, "Well, how do we do that? What does this mean? How do we put this into use?" The authors of the DevEx framework were myself, and both the two lead authors of Space, Nicole Forsgren, as well as Dr. Margaret-Anne Storey, who's at University of Victoria, amazing researcher, I think the most prolific, most published researcher in developer productivity.
What we were trying to do is put forth a practical approach to this perceptual measure thing. Our research into that really took us in a number of different directions, but ultimately, took us to this concept of developer experience, which was already a little bit of a research concept, but in 2020, we actually published, I think, really the first paper that put forth a framework in conceptual model around what even is a developer experience, and what does it consist of.
The most recent DevEx framework is really a practical approach to defining developer experience, which is something that a lot of the organizations we work with struggle with, is defining, just like productivity is difficult to get aligned around, how do we even think about developer experience? Then, of course, how do we measure it? In our framework, we provide a multidimensional framework that looks at perceptual sentiment measures, as well as objective workflow measures, combined with North Star metrics to get a complete view into developer experience.
I should also add that measuring developer experience isn't the end all be all. Developer experience is a component of how we should think about and look at developer productivity as a whole. I think developer experience is a critical piece to it, and of course, the title of that paper was DevEx: What Actually Drives Productivity. If you're looking to improve productivity, and understand how to do that, developer experience data and measurement is key to that, but there's more to the story if you're just trying to understand the impact of the R&D organization, or the efficiency, or the quality of the work. There's, of course, other types of measurements and understanding that you need around those types of questions.
**Scott:** I know that when the Space paper was first published, I'm one of the people that does the tech radar, and we discussed that, so we proposed that as a blip, but we talked about it, and we came to a conclusion we're not really sure what we're blipping here. Are we giving some advice to people? It's an interesting way to look at it. When the DevEx framework came out, that was really helpful, I think, because it put some better, more shape to it.
**Abi:** Yes. That was part of the intention. It just so happened that between the time Space was published, and the DevEx framework was published, developer experience came into its own. Back in 20, I would say, what was it, '19, people weren't really talking about developer experience, a little bit they were, but by the time we published this paper a year and a half ago, it was unbelievable to see how much attention. Gardner was talking about developer experience, everyone was talking about, the Stack Overflow was talking about. GitHub is all about developer experience in AI, of course. It was good timing, and really resonated, I think, with practitioners and industry leaders.
**Scott:** That brings up an interesting point that I was thinking about after I listened to your podcast, that I never put together this interest, this resurgence of interest in developer experience with the COVID-19 epidemic, and remote work, the rise of remote work. Do you think that those-- are people worried about what-- are there people actually working when they're at home? Is that what it's about?
**Abi:** The COVID-19 impact was really that suddenly companies shifted from co-located, in-person teams in work, to hybrid and remote work overnight. That is when Space was published, and it was really an answer to a spike of questions around, and business is trying to understand the impact of that. Hey, everyone just went remote. Are we more productive? Are we less productive? That was the question being asked.
I think developer experience trailed that. I think developer experience, I think there's a number of reasons why we've seen such a rise and focus and attention on developer experience. I think when I talk to companies, a lot of them, it's capped off, or finished off their continuous delivery transformations, if you will, DevOps transformation. Had moved to continuous delivery. A lot of the previous ways in which organizations were measuring, like the Dora 4 Key metrics, started to no longer really be applicable. It started to no longer give the answer to how do we get better.
I think that's actually really what has driven the interest in developer experiences. As we've moved, as organizations have moved beyond adaption of continuous delivery, the next problem becomes, well, now that we've done this whole DevOps thing, however you want to define it, that's a whole thing, but now, how do we actually make it effective for developers?
We've given them all these tools, and more responsibilities, and we have all these microservices, and who knows what else, how do we manage all this stuff, and make the daily work of developers streamlined? I think that's how developer experience has organically risen to be a focus area for organizations.
**Prem:** Are you saying here that there are these specific metrics that we can actually look at and draw some good insights? Is that what you seem to be suggesting?
**Abi:** Absolutely. As we start entering our discussion about metrics, there's a lot more to it than just that, but certainly, measuring developer experience is something we found to be incredibly valuable as a source of insight to organizations that are trying to improve productivity, or have investments in productivity platform engineering developer experience initiatives, and are trying to understand the impact of that to our lives.
I think it's table stakes for that, and more broadly, if you're a business leader trying to understand the competitiveness and the agility of your R&D organization, gauging the developer experience needs to be part of how you get insight into that question.
**Prem:** Are there good metrics, and are there bad metrics? Can you give us some examples so that our listeners understand what is good versus what is bad, if there is something like that?
**Abi:** I wouldn't say that there's universally good or bad metrics. I think there's good or bad metrics for different purposes. To give you an example, if you're trying to understand and measure, or even incentivize your organization to ship faster, measuring story points would be a bad metric to incentivize that improvement and behavior for, I think, reasons that are pretty well understood.
Now, if you're trying to understand the predictability of your organization at delivering on time or against the estimate, then story points are the metric you should be using to get visibly into that. I can't give a universal good or bad metrics. I can give context-specific point of view on what metrics work for what types of problems.
**Prem:** What you're seeing here looks like the intent and the context matter quite a bit. A good metric in one context can be a bad metric in another. Is this what I'm concluding from what you just said?
**Abi:** Correct. Even within a context, there's different levels of-- I have a little framework I share. I say, "Hey, are you using this data to understand, to align, or to assess?" If you're using, for example, Microsoft, they look at, pull request for developer. They heavily rely on that as an input into how they understand productivity, do research around productivity, to understand productivity, but if Microsoft were to use that to assess developers, we can all picture some of the bad things that could happen from that.
Again, even within the context of a purpose, there's that intent, from which you mentioned, what's the intent, and what's communicated? If you don't communicate your intent clearly, there could be consequences as well.
**Prem:** Right. Here is a thing that we recently did as well. There is this debate on the kinds of metrics, qualitative versus quantitative. I know that your article on martinfowler.com also talks about that, right? A couple of scenarios, in this example that you were-- this campaign that you were doing, consulting work with, they had and asked, tell us what kinds of metrics, and so on and so forth.
Now, they didn't have a lot of quantitative information. Then we had to get started, and we said, "Okay, let's look at qualitative information, gather data through surveys and questionnaires, and so on and so forth, interviews, and so on and so forth." Now, one thing that happened was which was interesting, we got a bunch of data. It was all over the place, and then when we actually dug in to see under the covers, a lot of it didn't actually quite match up with what people actually answered.
I was like, "Huh, I read your article as well, and I saw that there was a huge emphasis on qualitative information." I was almost like, "No, I don't know if this really works." I'd rather believe the quantitative data than qualitative information. I wasn't quite sure how to move forward with that qualitative information, especially because it seemed to give us the wrong indicators.
**Abi:** Yes. That's interesting. That's not uncommon for people to have that experience. My personal recommendation, and our recommendation of our company, is to use both. You want as much data as you possibly can have. If you look at how organizations like Google, that are heavily instrumented, they have the IDE to every part of the developer environment instrumented. They have metrics on everything. They talk about how they still use self-reported data as a way of complementing that and even double-checking the metrics they collect.
Prem, based on the experience you described, I think partly it could just boil down to the design of the survey itself because getting reliable and accurate information is really difficult without really rigorously designed questions. The process for designing one question is a lot more QA than we do for our software releases, I can tell you that. Also, the fact that you found divergent information from what people were telling you and what the systems and objective data were telling you, I see that as an opportunity.
That's an opportunity either to realize that only one of these things could be true, either the people misinterpreted the question, the people lied, [laughs] or your objective metrics aren't telling you the full story. Whatever the reason may be, that's probably valuable to know. Again, it boils back down to it's about having the most data possible, so double-checking your qualitative data with the quantitative and vice versa is really bad. I'm sure, Prem, you've come across instances where the objective metrics are misleading as well.
Google talks about their famous example is they were trying to measure build times. They were seeing some data that had them really concerned about developers getting blocked waiting on CI, and then once they talked to the developers, they realized, "Oh, those are actually programmatic bot builds." They weren't actually holding developers back. Again, I think the opportunity is to collect as much data as possible from people and from systems and then triangulate it and leverage it together to give you the fullest possible picture.
**Prem:** Absolutely. I think, again, it boils down to the thing that you previously said, which was about intent and communicating the intent. It wasn't that people were lying, but I think they naturally became defensive because they weren't sure, or rather, they probably were speculating that this would be misused. If they self-reported bad things, then it would have adverse consequences for them, and what's the natural thing humans do? They become very defensive, right?
**Abi:** Yes. That's where, in our approach, things like anonymity and the communication and the design of it, it all goes together to hopefully produce reliable as possible measurements and then cross-cultural concern. We have to translate things into multiple languages. It gets pretty deep and complex. Yes, it's not easy to do. I always tell people, doing a SQL query on your GitHub data is a lot easier than designing, getting good developer experience data, a lot, lot easier. Again, by leveraging both, I think you're able to get the insights you need as quickly as you can and in a cost-effective way.
**Scott:** I'm really curious about the methodology and how the methodology might have led to the conclusions that the papers describe. I'm guilty of having sent surveys to developers many times to try and track what's going on in our business and the things we're delivering in. Social scientists have been doing this for a long time. This is a really well-established field, how you ask questions, how the questions are worded, how do you statistically interpret the results? I wonder, how much of that went into the development of these frameworks?
**Abi:** Funny thing about Nicole, I think she's a real pioneer because she's a computer scientist who ventured into psychometrics, which is the social sciences. That's one of the things that's inspired me and inspired a lot of the folks in our team. At DevEx, we have folks who actually come from the social sciences, so industrial-organizational psychology, for example, is this is what they do, is develop questionnaires and assessments, psychometrics to assess, make really mission-critical assessments about people's health, mental state, performance. It's a fascinating field.
Our approach has been heavily driven by the social sciences and best practices. The methodology of the development of our measurement instrument, or survey instrument, if you will, adheres to an industry standard that comes from the social sciences. That is a standard in any sort of psychometrics assessment. There's a rigorous standard for how that has to be developed, tested, and validated in order to be considered even a valid data source.
Then, of course, we have had to solve challenges that are unique to R&D organizations and software developers, and there are many, let me tell you that. [laughs] Then find how to apply this approach of self-reported data and psychometrics, how do we apply that in a way that's most useful for business, and that's, of course, an ongoing journey as well. A lot I could share, but it's definitely been a really exciting opportunity to blend these fields together and be a pioneer in that.
**Scott:** One of the things that's really challenging is survey fatigue, and that people are just so reluctant, even if it only takes 5 minutes to fill out a form. We get response rates when we do that kind of stuff, we get really poor response rates from well-intentioned people because they've got a lot of other stuff going on. How do you avoid that?
**Abi:** Well, at Thoughtworks you all covered, did a little blip on our survey platform. I think you covered the response rates you saw at Thoughtworks. We at DevEx sustain on average over 90% participation rates on the self-reported surveys that our customers run. People don't believe us when we bring that up, but it's true. You can talk to our customers to verify that.
Then the second question we get asked is, "How do you do that?" There's a lot of things that go into it. I could share a couple of examples of, I think, some of the strategies that we leverage. One thing we do is that the results of the survey are transparent to the entire organization down to the developers themselves. If you think about what it's like to typically take a survey, you get an archaic-looking form, probably sent to your email.
You fill it out reluctantly because, out of the kindness of your heart, you want to be helpful, and then you never hear about it again. Maybe you see a bullet point about it in the next all-hands, but you never see the results, you never get any benefit from it, there's nothing that data does for you. Then, the next quarter, you get that same link in your email, and you decide, "I'm not going to participate in that."
One thing we do with DevEx is that the data is open to everyone, and it's compiled in a week, so it's not like you see the results three months later, you see the results within days of submitting your feedback. Again, there's a lot of things that go into the response rates, but that's one I would call out as an example of a very stark difference between, I think, how organizations traditionally run surveys and our approach with the customers we work with.
**Scott:** I think that's really important, the transparency and seeing that there is a consequence, or that there are actions that are taken in response to those. It takes a certain amount of courage, I would think, on the part of the leaders to be that transparent, vulnerable.
**Abi:** Absolutely. It's funny sometimes I wonder if they don't realize it [laughs] till the data becomes available. I will say, if you had to ask me what's one thing that really surprises me about what we're seeing with the organizations that use our platform, I think that would actually be one of them. It is surprising to me that so many of these organizations are comfortable capturing the voice of the developer, and revealing it to everybody. Because developers, they voice their opinions, and they're direct about the concerns and opportunities they see.
I'll also tell you that these leaders find that data to be incredibly valuable and insightful. There's some risk associated with that, but ultimately, I think keeping it open benefits all parties and solves, or helps solve the participation rate problem, which pretty much kills a lot of these survey programs before they even really get any traction typically.
**Scott:** I see a lot of organizations that are really embracing this, because they understand the benefits that it's going to bring to them. I still encounter a lot of businesses who-- When you talk about developer experience as a critical thing to improve, they see that as maybe narcissistic on behalf of the developers. Like, why do I care about their happiness? My business is at stake here, and I wonder, what do I tell those people? Maybe you can help me out.
**Abi:** This is a problem I'm really focused on personally right now, because as you both know, I've spent the last few years championing developer experience, and getting a lot of organizations to adopt and invest in developer experience. I think a lot of organizations run into the exact challenge, Scott, that you're bringing up, which is they get this data, they want to make investments, so then the rubber meets the road, and executives are asking why? This is about making developers happy, that's not our highest priority at the moment.
We have to be profitable. We have to ship this feature, this product, get it to market. I think developer experience is a positioning problem, because, as you said, Scott, you said the leaders you talk about seems almost narcissistic. Why is developers' feelings the priority for our business? That's a problem of misunderstanding, and mispositioning on the people championing developer experience, because developer experience is not about making developers happy. Developer experience is about understanding the friction, what's slowing you down, and costing you money in your business.
Today, I think my recommendation, and what I'm advocating for, and the guidance I give to leaders is to think about developer experience as just one pillar in how you're thinking about productivity. You can think about productivity maybe across four dimensions, speed, effectiveness, quality, impact. I see developer experience as fitting in under that effectiveness pillar. I know that's something at ThoughtWorks you all have published quite a bit about as well, so that's all it is.
Developer experience is your best signal into effectiveness. It's not the whole pie. The developer productivity is bigger than that, but it's a critical piece, and in particular it's about understanding improving effectiveness so that you can also improve speed, quality, and impact of your R&D organization.
**Scott:** I think one of the things about DORA and the DORA metrics is that they showed that those metrics are predictive of business success. I think that gets lost a lot. It's one of my pet peeves is people measuring Dora metrics without really understanding why, or what they're—
**Abi:** Me too, Scott.
**Scott:** —getting out of it, and dying to use that to define team performance and things like that. Anyway, is this something you've looked at? Like, how can we predict business performance based on developer experience? Is there any correlation there?
**Abi:** We are about to publish something just on it. Earlier this year, we published a paper with Microsoft and GitHub, a very quick study looking at the impact of developer experience. Following that study, we've invested in a much larger study around developer experience, and predictive modeling around our measure of developer experience, we've developed DevEx, which is called the Developer Experience Index, and it is predictive. We've looked at business outcomes like profitability and growth.
We've looked at other outcomes like rate of delivery, time waste, or regrettable attrition. I can't go into detail here, but I can tell you that one of the things we found was a very strong correlation between developer experience and time waste. To the point where you can pretty much say, "Hey, X a number of point increase in your developer experience index score translates to X percentage point decrease in time waste, which translates to X amount of dollars per engineer and recapature efficiency savings."
That data's coming, and that data is there. I still don't think that will solve the whole problem we were talking about, Scott. I still think executives will just at face value misunderstand developer experience. Again, that's why I think developer experience needs to be spoken about and positioned as part of a larger focus on developer productivity rather than as its own singular thing.
**Prem:** Wonderful. Oh, it's 2024, so thanks to ChatGPT. This is where AI finally has maybe become mainstream. Are there any AI and generative AI techniques that we can use to make this process of understanding developer productivity a lot more easier?
**Abi:** Yes. At DevEx one maybe obvious application of this, we have organizations that on a given survey will collect upwards of 20,000 comments from their developers. If you think about an organization with 8,000 developers, and each developer maybe writes two or three comments that adds up to tens of thousands. We've been able to leverage GenAI as a fantastic tool for synthesizing that information, and deriving actionable insights from it quickly without manually sifting through tons of data.
Of course, more broadly I think GenAI has a lot of potential to help with developer experience, and developer productivity. One of the examples I'd like to share is one of the most common things, opportunities, challenges we see with the organizations around developer productivity is knowledge sharing, and documentation, and technical debt. Well, GenAI has huge potential to help with quickly understanding a code base, or automating, documenting thoughts and processes of a developer.
That's a use case in particular I'm really excited about. Of course, the code gen copilot stuff, I think, is, of course, pretty intuitive and exciting, and we do see data on the impact of that. That's very positive. At the same time I think it only tackles the code writing aspect of the developer day, and developer experience, which is really not where I think the most friction actually exists if you look at the SDLC.
**Scott:** We've found the same thing, and in that developers really like copilot. They don't want to give it up, and they find it useful, but it's been much more difficult to find any impact on the overall cycle time, and there's a lot of reasons for that. I think that's another podcast. One of the things we always try to do when we wrap up the podcast is try to get some call to action, and how to help people get started. Like if you have a development organization, an engineering organization, and you want to start understanding developer experience, where's a good place to start with that?
**Abi:** Sure. I'll give two calls to action. One is, if you're in the scenario you just described, Scott, you're a leader, or you're in charge of a platform organization, productivity organization, and you want data, and you want data fast, then a survey is the fastest way you're going to get holistic baselines about productivity and experience. On that Martin Fowler article that we referenced today, we did provide a starter template for a survey you could use as well as other examples of different types of questions and insights you can capture.
I'd recommend, folks, you go-- It comes with a Google form template, you can make a copy of it, get started with it right away. The other recommendation I have is, whatever company you're at right now, if you don't have an aligned way of thinking about and measuring productivity today, then I would recommend you get that into place, because every organization I talk to at some point has to answer that question.
If you can get ahead of that problem now, not only is that going to save you a lot of pain down the road, but it's going to give you value today to get a baseline and start tracking how your organization is changing and where the opportunities are. If you don't have an answer to how do we measure productivity at your organization, yes, I would invite folks to try to figure out that question.
**Scott:** Yes. I know that's one thing that we run into a lot, is the absence of a baseline, where people want to know right away how they're doing. It's like, well, what do you have to compare against? I think we'll wrap it up here. I wanted to remind everybody that you also have a podcast, and they should go check that out. There's a lot more information and in-depth discussion these things as well as, I think, the practical experiences of a lot of businesses who are putting this into practice. Where would people go to find that podcast?
**Abi:** It's called Engineering Enablement podcast. It's on Apple, Spotify. I think anywhere where you listen to podcasts, I think, it's published there. As you mentioned, we're fortunate to have folks like Nicole Forsgren, leaders from companies like Google, Airbnb, frequently come on the show to talk about how they're thinking about productivity, how they're measuring it, and all the challenges that come along with that. I would invite folks to check that out. Thanks for the shout-out.
**Scott:** Great. Well, thanks a lot. I could talk about this for a lot longer, and I have lots more questions, but we need to wrap it up. Thank you so much for taking the time to do this. I really appreciate it.
**Abi:** Yes. Thanks, Scott. It's a pleasure to be here.
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
## Explore a snapshot of today's technology landscape
[ Read the Tech Radar ](https://www.thoughtworks.com/en-th/radar)