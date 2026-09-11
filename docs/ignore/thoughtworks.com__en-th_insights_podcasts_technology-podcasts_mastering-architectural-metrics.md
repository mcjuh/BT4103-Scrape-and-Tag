<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/mastering-architectural-metrics | Title: Mastering architectural metrics | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Mastering architectural metrics 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Ashok Subramanian and Rebecca Parsons | Podcast guest  Andrew Harmel-Law
August 12, 2022 | 48 min 09 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/mastering-architectural-metrics#Transcript)
Listen on these platforms
## Brief summary
Given the variety of architectural styles — and the unique technology landscapes at every organization — how can you develop a set of metrics that can reliably guide your organization to improve? Andrew Harmel-Law has been grappling with this question for some time. We catch up with him to hear how he thinks DORA’s Four Key Metrics provide invaluable guardrails that can empower teams and improve the software delivery process.
#### Full transcript
**Ashok** : Hello, everyone. Welcome to the Thoughtworks Technology Podcasts. I'm Ashok Subramanian, one of your regular co-hosts. I'm joined today by another one of your regular co-hosts, Dr. Rebecca Parsons.
**Rebecca** : Hello, everybody, Rebecca Parsons, Chief Technology Officer for Thoughtworks.
**Ashok** : Great. Today, Rebecca and I are joined by Andrew Harmel-Law. Andrew, do you want to introduce yourself to our listeners?
**Andrew** : Yes, hello, thanks, Ashok. Hi, Rebecca. I'm Andrew Harmel-Law. I'm a tech principal with Thoughtworks, based out of the London office in the UK.
**Ashok** : Great. Andrew's specialty is architecture metrics. In fact, he's actually written a chapter on the O'Reilly book on architecture metrics. That's the topic of our podcast today, maybe when we start, why don't we actually start by trying to get your definition of architecture metrics. What is it that you mean?
**Andrew** : That's a very good question, actually. I think because architectures themselves, there's a great variety and at Thoughtworks, we see lots of them, I'm sure everybody listening has got-- the individual manifestation of anyone's architecture is probably not what everyone wants it to be or aspires for it to be but it's probably what it is. It's also probably very different from any other architecture. Maybe the styles or the aspirations of them could be fitted into various buckets, but there's a wide variety.
Also, in my experience in IT, which has been quite a few years, these days, there's always a fashion or a trend or a new way of doing things. That means there's older ways of doing things and then new ways of doing things and there's even newer ways which are coming. Given that variety, the concept or the question of architecture metrics is interesting. It's like, what do you measure if there's that much variety to make sure that you're giving yourself-- because what you want from a metric is something to guide where you're going and let you know if you're doing the right thing, or going in a positive direction.
What would you count? Like you said, Ashok, we got challenged by this, myself and the other authors of the chapters by O'Reilly, to write down what we thought, all of the other authors came up with very different things and I realized that, from my perspective, because when I architect, the style that I think's most effective for the projects and the clients I work for, is to have autonomous teams with a supporting architecture and a supporting organization structure and everything to make teams empowered and autonomous and to be able to flow and deliver software.
What I did was, I actually picked the accelerate door at for key metrics because when I've set those up, I've seen to be super productive, to let teams see if they are autonomous. If they're not, then they can either change their team structures, whatever, but frequently it comes down to architecture. I was able to deliver a stable product efficiently. Those metrics are really nice. They're a good broad brush way of understanding if you're in the right direction or if you're not in the right direction, maybe with whether you want to architect for testability or decoupling or stability or continuous deployment and all these kind of things. There's other flavors that are available, but that's my--
**Ashok** : You mentioned a few things in there. One was around autonomous teams and enabling and you also touched about most organizations either end up having a collection of different systems over multiple eras if you like, and they all have their own particular architectural style. In effect, what you're saying is really for organizations to work well, you found that autonomous teams are useful and then these four key metrics are a good way of trying to measure them. How do you almost come to this realization? It'd be good to get-- tell our listeners a little bit about your journey into the space?
**Andrew** : Yes, sure. It's the classic-- one of those benefits of being at Thoughtworks is, we get to do different things for different clients. A few three years ago, four years ago, Accelerate, the book had been released and lots of people were reading it, the client CTO had read it, they were buying it from all of their staff. Luckily I just finished reading it before they started asking all of their people to read it.
We looked at the four key metrics but didn't really do anything with it, but it was a really interesting lens to look through, to the extent that when I started on my next client project, the last one before lockdown, we realized that we could start to hand gather, kind of hand raise our four key metrics and we use that to not really to measure things but more as a decision making aid so that if we did this thing, and if we improve this or did this refactoring, whatever, do we think it would have a positive impact on the four key metrics?
The project after that, which was during lockdown was where actually, I'd seen the benefit and we've been trying these things and we tried, so it's all right, let's actually invest time and effort in setting things up. That's actually the story behind the chapter and I thank the client at the time. Luckily, we can talk about the client. The client was Open GI in the UK. Myself and my client pair, who was their tech director, I think he was called, Pete, we basically hand rolled, we hand created our own four key metrics and then we built dashboards.
Fundamentally, and this, I think, is the most important thing. We built dashboards which teams could consume and teams could look at and teams could see, we reported the big picture of four key metrics but the teams could then drill into that and say, "What are the four key metrics for my team, what are the four key metrics for this pipeline," and ask questions and get answers. The power of being, they could do that they could see where tight coupling or difficulty of testing or things like test data make their lives difficult or environments, progression for environments or releasing, all of these things, which, some point come back to our architecture. They could see that these were problematic. The teams themselves, were driving these initiatives.
Up to that point, as a Thoughtworker, I would be the person driving the initiatives. I'd be like, "You're paying me to be here, I have this vision, this is where we should go, this is what we should be doing," but the four key metrics, given to the teams, they could see this, and they're like, "Cool, we all agree that we would like to deliver more frequently, we'd like smaller increments and have more stable observable systems."
Then they took that back and went, "Let's look at our code and see if it's the architecture or see if it's the release process." When we cleared out the easy stuff, like adding more tests or whatever, all of it became about architecture. That's where I was confident to submit this chapter to O'Reilly, because we changed the organizational staff, we just decided to release more frequently. As soon as you've done that, the marginal gains, the real gains are in refactoring your code, making sure that teams really are independent, that one story can be delivered by a single team and released via a set of one or more microservices.
You could see it, you could step back, and you could see the teams speed up, and they gained more empowerment. Their autonomy rose and the engagement rose and the satisfaction rose. In the midst of COVID, that was cool to see. We didn't sit in the same office as anyone else but we could see this shared understanding coming. That's when I saw the power of it. Since then I've just kind of, it's my go-to default for setting stuff up and showing teams where they are and where they want to be, what they might do to fix it.
**Ashok** : I realize we've been talking about or we've been referencing the four key metrics. Not all fan listeners, might necessarily be aware of what they are. Perhaps if you could quickly give an overview of what the four key metrics are and maybe why, ultimately, this were distilled out to those four for what?
**Andrew** : That's a very good point. The four key metrics come originally comes from DevOps community. 2016, I think, maybe, Dr. Nicole Forsgren, and Gene Kim, and Jez Humble, started writing something called The State of DevOps Report or The DORA State of DevOps Report. They wanted to do something statistical and really look in detail, at all of these practices, whichever one kept. The DevOps community had started to talk about more of advocating, and they seemed to be having positive impacts, but nobody had actually gone in and really had a look and prove things.
They did a load of work statistical deep, hardcore statistical work to prove this. They did surveys, I think it's about 23,000 respondents and staff, they gathered loads of data, and every year they will update this thing. They realized that these practices did have a positive impact on not just commercial performance of companies but non-commercial performance, so employee satisfaction, quality of product, et cetera. They realized that the ways to find out how good you were at these things, they could distill down to four metrics and those metrics were the four key metrics which are deployment frequency, lead time for changes, mean time to recovery, and change failure rate.
They proved statistically that if you improve these, across the board-- you can't just improve one but you need to improve all. I can make my lead time for changes a lot better by just turning off all my test, but then I'll obviously impact the stability of my service. I've got to keep my service stable, but I want to deliver more frequently and deliver more rapidly. If I keep them all balanced and I do that-- do those things, and I optimize for the lower four key metrics, then I should be moving towards being efficient at delivering a stable product.
It doesn't say that I'm delivering a product that customers want, those are entirely different metrics, but the metrics for the machine of-- not machine, the craft room of the teams building and shipping this software, it's a very good indication of all of those things. As a consultant, it's a gift, it's a proven set of methodologies and practices with strong statistical work behind the scenes that Dr. Forsgren's done. It's super useful.
**Rebecca** : One thing that occurs to me though, and you alluded to it when you mention those would be other metrics, like whether or not what you're building is actually what people want, the four key metrics assume nothing about what the actual requirements of the system are. It really is all about just, "Are you able to efficiently and effectively deliver a product into production and getting it into the hands of your users?"
How do you go about thinking about other kinds of metrics that might be more tailored to the particular application? Perhaps it's something that requires low latency or something that requires five nineths of reliability, or do you just start with the four key metrics and they then say, "Now let's move on, we've got a stable platform and we've got a working organization, now I can start worrying about these other architectural concerns."
**Andrew** : That's a very good question. Typically in my experience, but this caveat, maybe this is just the clients that I've worked with and the work that comes to us as Thoughtworks. Typically the work and the organization, and the kind of focusing that would have the biggest impact at the start is around about just getting software out the door, but maybe that's the projects-- I guessed after-- maybe that's because Thoughtworks UK think that I can advocate for this stuff quite well. Then when we're getting stuff out the door, then we can focus on other stuff.
For example, at Open GI, there was also parallel pieces of work where they were focusing on, because they were an insurance broker and they were moving to a multitenant cloud version of their application, they knew, from their business model and from their existing customer base, they knew, for example, that performance of quotes and availability of the quoting system would be a big deal. There was a parallel piece of work to set things up around that and to set up, some performance testing and availability testing, and also to set that up kind of continuously, they didn't just want to do one and done.
They knew that they were moving to a product mindset, they knew they wouldn't build something and leave it, they would build it and iterate on it and keep going. Maybe they'd build something that's fast and they test it and it's fast, but then they add three years' worth of features, which slowly degrade the performance or degrade the availability. They wanted to build capabilities to test those kind of things. There's probably a US equivalent or other country equivalents, there's a person in the UK who, called Martin Lewis, who has a TV show every now and then on the TV, basically, he tells you how to save money. He will tell you, "If you go to this insurance broker, they will give you a really good deal." This is effectively, he would DDoS their servers, every time he would do a show.
Explicitly, when they were on prem, they would spec out more servers when they saw his TV show coming up in the schedules, because they knew it would be bad. We did look at that, and they looked at that in far more detail and spent a lot of time worrying about it. That was a product metric and another technical metric. They knew that throughput, within some certain response time was going to be key for clients, but also that it could cope with the load also being elastic because provisioning that much-- if they're moving to the cloud, they don't want to pay for that much infrastructure underneath the quoting engine all the time, they just want it to be there and be able to scale up plastically when Martin Lewis does one of his TV shows.
We still had the four key metrics, but what was nice was, and at the start, it was clear that lots of stuff around about the quoting engine was tightly coupled because of the old architectural decisions which weren't wrong, they just were. They would scale up a lot of things because they couldn't individually scale just this individual piece. Part of the four key metrics was to be able to get that team, to be able to slice out their piece of the infrastructure, and to then work to be able to continue to deliver that piece, and then they could deliver it. We weren't so worried about them being able to put that kind of stuff into production, but we did want to get them to be able to rapidly do experiments and then deliver something to a test environment, then they could soak test it, see what really happened to it, and do that stuff.
Again, building for things where you can ship multiple increments very rapidly, on demand, and be able to have something that's stable and that you're confident in with good observability, and all these other things, that enabled lots of the other things that they were doing, and that was key so they could see-- to be fair as well, Rebecca, I think the exec on the tech side probably cared about the four key metrics, but I think the rest of the execs, like chief product owner, CEO probably didn't-- they shouldn't care. They should care if it sucks. Like, "Why are tech in the way, why can't my product people come up with ideas and then ship it rapidly," but as soon as we got out of their way, then they're just like, "Good, now I need to make sure the product people have found the right market fit and have found the right business model and have found all of these things."
It was nice, and again, the final thought is, it was nice to get things set up in a way that they could start shipping stuff. When we left, we were just there for a specific period of time, but they kept going and they've recently released, they were definitely able to keep delivering all of this stuff, to the extent that I spoke to the CTO, I'm sorry, I can't remember if that's their title. Spoke to one of the senior exec members of Open GI recently, and they'd actually slowed down on some of their four key metrics because it turned out that that was not the blocker, it was the product, "We're doing nice," went to find product market fit and all of these things. They were de-investing in this stuff because it had paid off and now they were investing in other things. That's nice, to be able to get IT to respond to the needs of the business as opposed to not get in the way of the business was quite a refreshing place to be.
**Ashok** : Maybe that's something we can dive into a bit more detail a bit later. You mentioned product metrics, maybe that's something I'll keep aside to to come back a bit later as we discuss. What you described, there are a few things in there you spoke about almost as a positive benefit or side effect or some of these things will happen. One of the things you spoke about was scaling, and you mentioned both scaling the technology, but using these four key metrics almost like see whether you're making progress. You mentioned earlier on, I think when you were describing, you mentioned about autonomy of teams and so on.
I think one of the things that we see quite often is, the approach to architecture can sometimes be seen as almost adversarial sometimes depending on how organizations are set up between architectural-- teams that have more responsibility of focus on architecture and teams that are you just go and deliver stuff. Are there any other benefits that you've seen where actually everyone starts caring ? The way you described, it almost felt like you were saying, "This is the only thing you measure, and then everybody somehow magically sort of falls in line." Is that what happened?
**Andrew** : You're right, it doesn't magically fall in line. There's an awesome-- which exercised my brain for years, there's an Alberto Brandolini quote, Alberto Brandolini, the person behind EventStorming. I think it's something like, although I'm going to get it wrong, what ships to production is the developer's assumption of what they're supposed to be shipping to production. The person who writes the code, that's what gets into prod. It's not the architect's picture of what's there or whatever.
Maybe the architect's picture has been effectively-- they've co-designed with the developer or the developer is the architect or all these kind of things, but what goes into prod, the architecture that's manifested and various store workers have talked about this as well, that's what ends up in production. I was talking to another colleague about this yesterday, setting up the four key metrics alone, won't get you there.
I think the thing that we did most was every week we would sit down with all the-- It was an open invitation so not every member of every team came so that be the most expensive meeting in the universe. People from all the teams, plus people from key representatives from like infosec, from product, used to come along, sometimes the exec and tech would come and we would do things. We would look at ADRs that were moving through the system to get them to understand architecture. Also, we would look at our four key metrics and our cloud spend and we would discuss what was going on openly with the team.
It wasn't like the architects were having a discussion, or the people who were blessed with seniority. It was an open conversation around about, "Where are we, what could we improve, is this the right amount of money to spend, is this the wrong amount of money spend, is this an acceptable level of four key metrics? You don't want to over-optimize, or would we benefit from trying a new practice, like trying trunk-based delivery?"
Some teams realized that trunk-based delivery was for them so they could pick up their practice. Other teams realized-- because some testing, the shape of data in insurance, but also in banking and other industries is complicated and can have significant impacts on performance, so some teams invested in big pieces of work to build realistic test data and do test proper test data management. All of these things led us to look at things. For example, if we were wanted to do nice testing with a stable predictable product, we would say, "For this team that was doing all of this performance testing, it makes sense for them to invest in some test data setup stuff," they built some services to do all of these things. Other teams, it was very simple. They just had crowd-type stuff so they didn't bother.
What was nice, because we centered the conversation, was we were getting the concerns and the fears and the broader, bigger picture from the architects or the people who had the cross view, but you also got an equal weight of the conversation from people who are just trying to ship code, and they're like, "It's taking me too long to do this. This architecture is stopping me. If I thin slice a story, I've still got to wait for two other teams to deliver two pieces." We could look at re-architecting, we could get that feedback loop. Even before we deployed stuff we could hear from people and hear what it was like and that was a really powerful conversation.
Then we get the engagement and therefore people want to understand. In my opinion, my impression was that what ended up in prod, because it was co-designed, it was a lot closer to what everyone was hoping would be there as opposed to some aspirational PowerPoint slide deck that someone produced three years ago at the start of the program.
**Ashok** : Almost the beneficial side effect of actually having collective ownership of that.
**Andrew** : The metrics almost fade into the background. At some point, the big thing is everyone, and this is what I spend half of my chapter doing and half of the talk, when I talk about this, there's a mental model behind the four key metrics, which is the lean, the pipeline, the single piece flow. In the four key metrics, it starts from check-in or development complete down to running in production, but not necessarily released.
It's easy to forget as a consultant, not everybody has that mindset. Lots of people have the, "I've been given a story so I write it and I write some tests and then I stop and I'm done and then a QA picks it up and then they do, and then they're done. Then the release team releases it and then a support team supports it." By having an end-to-end model, lots of stuff, conversations that would be segregated and siloed suddenly become cross conversations and people are aware of it and care about it, and that has a big impact, in my experience.
Not everybody's used to that. Some people are like, "That's obvious, that's such a default, why are you even telling me this?" I never fail to be surprised, because I didn't start off my career with that mindset, I started off with, you're given a requirement, you implement the requirement and then you're done. At some point, people go through this change, and I think getting that and mapping that onto your lived experience and then figuring out how to improve that mental model is key because that's the power.
We can build and release software to the cloud, very cheaply and very rapidly these days, so we should optimize for that to help discover products and to help evolve products and to help to right-size our systems and all those kind of things. If we're not taking advantage of that, then that's a big problem.
**Ashok** : I think when you were describing this journey and you were talking about how all the things the teams have to do to make sure you can deliver this fast, you also touched on, there's a number of other practices that are almost necessary or underpinning this that are going to end up supporting whatever you define as the specials you want to achieve in the four key metrics, but you need those enabling practices, right?
**Andrew** : You don't need them, just your four key metrics won't be very good. Then if you adopt them-- there's things like lean product management is one of the big boxes in groups of practices, the other one is lean project management, lean product management, then there's all the agile DevOps practices which Thoughtworkers, given 15 seconds will start telling you about whether you ask for it or not. In later iterations of the DORA State of DevOps Report and in the book Accelerate, they also realized, I think, there's something to do with leadership. Again, if you have all of these things in place, but people don't feel like they have the permission to improve things, they won't improve things, they'll sit and wait to be told to do it.
Because I firmly believe in autonomous teams, I think about half the time I just crash in and build. Autonomy isn't just like, "You have few dependencies and this bit belongs to you and this bit belongs to someone else," autonomy is the ability and the desire to pick that up and use that to improve your piece and improve your metrics, your product metrics, not your four key metrics, and to understand the empathy for the customer, which as a Thoughtworker once impressed on me. The two things about microservices are, you can release independently and you should have empathy for the consumer of your service. I was like, "Oh, that's a quite nice summary."
If you have that, then you've got this feedback loop from the consumer, whether that's another team or an end customer or whatever, then you've got this build measure, learn loop, and you've got the empathy and you're right sizing your product and your care and all these things.
**Ashok** : Really, the way you describe it, it's great it’s like everybody would want to be there, but we know effectively, you said at the start, yourself, you've got systems across multiple eras and so on. You've got different styles, potentially different approaches to solving problems as well. If you want to actually start on trying to go down this journey, when or how do you start? You've seen this across a few different organizations, what works and what doesn't work?
**Andrew** : I've thought about this a lot. I've thought about this a real lot, actually. It's very easy to do things that make things change and change positively, but it's harder to find the thing that will have the biggest positive impact in the biggest direction and set up and enable future changes. This may just be because I've been very lucky to work with some awesome BAPO of product manager type people, but I think identifying your first valuable thinly sliced stories, and then using that to drive to find the things which are blocking you being able to deliver in this way and architect in this way and organize your teams in this way and observe your running system in this way and to build this feedback loop with your end customer.
If you don't have a valuable story, everything else feels a bit secondary. The key thing is a really nice and really small story, but with known or at least a hypothesis of value, then you can push that through, and you will have to push it through because like you say, the world of IT is not-- we're not all living in this glorious future which we imagine Silicon Valley to look like but which isn't, because it's as messy there as is anywhere else. We all think it's amazing. People at Twitter can ship in 30 seconds after they've got their foot in the door.
You have to convince people and you have to change minds and you have to change mindsets and stuff. If you have a valuable story, you can say, if this one thing gets in, or even this hypothesis, this experiment, if we prove we can release this little thing, you can take product with you, you can take tech with you, you can bring all these things through and you drive that through. You probably make compromises and you probably have to go slower than you want to, you probably have to cut corners and cheat-- there's few bits in the chapter in the book as well where-- like at Open GI, we weren't actually releasing to production. We were going to do a big bang release at the end so we faked it.
We weren't even in production, technically our lead time was infinite as one person joked, but we were confident we were doing the right thing because we were treating our highest environment as prod. If it failed or if testers couldn't test something or if there was a defect, we treated it like it was a defect in production. We stopped the line, all of the and-on, core type stuff, and we went around and fixed it. We kept ourselves honest even though we knew we were cutting corners. That's the thing. I've spoken to other people, other clients, we've done things like with, where you release a mobile app, my client before my current one, they had a mobile app and they pointed out, "I can go as fast as I want, but the Apple Store is not going to release my code any faster than they choose to", which is true so you can't.
We were like, "Cool, your prod is when you've submitted something to Apple. A change failure is if Apple give you a knock back because you're using too much CPU or you've used the volume button as a camera to take a photograph, or any of the rules that you might have broken, that Apple will push back on. Because we're taking it to the point where you think you're done, that's the end, the deployment point is, "I should have no more recourse to do anything else," if you do, it's a change fail, then you've failed.
I think it comes back to value. If you can say this one thing, which is hard to find and I end up spending quite a lot of my time at the start of projects these days, peeling stuff back to find a little thing that's useful and then you can push it through in any case, "Let's do that," and then there's some stuff we compromised on let's push through another one, and you can incrementally build it up. That's how I do it. There's probably other ways of doing it, but it helps to have a debate with someone if you've got a valuable business thing to argue about because if it's just some random thing that nobody cares about then the skin's not in the game.
**Ashok** : Try and take some thin slices through the system all the way through or as far down the--
**Andrew** : Yes, like classic agile terminology, like aspirin use cases or tracer bullets or something a bit less military. Aspirin use cases is a nice one. The first one I got told about was, if I'm building a hyper complicated system, which prescribes drugs to people, what's the simplest thing I can prescribe, which will bring value to end users? Lots of people take aspirin and prescribing aspirin to a person who has had no other drugs, that's a useful thing.
Pushing that through, it's not build the label printing service and then build the mobile front end for the blah, blah, blah, it's like prescribe an aspirin, simple. Then you can get people behind it. The mindset is beginning to be value and customer and things like that. Maybe I've been brainwashed by BAs. Maybe I should be, maybe I'm saying the wrong thing, maybe I should be like, we should build awesome Kafka-based microservices.
**Ashok** : I think maybe it's a good time to circle back into and talk about the product metrics that we're talking about. I think that's something that we have spoken about as well. I know discussions on things like, when do you know you're done with this, are these architecture metrics a useful tool or are they like a stepping stone. I think there was a reference you made about, well, actually we don't want to be pushing to production at one of our clients. We don't want to push to production too often because, counterintuitively, maybe that's bad. Is this a stepping stone to getting better and when you realize that actually maybe that's-- you stop focusing on this a bit more and focus on the product metric?
**Andrew** : Exactly, I think so. It's a tool and I think the tool's most powerful when everybody knows how to use the tool. That's how I use it, I don't use it as a-- which as a consultant, I've got to be careful when I come in, because some people are like, "He's setting up metrics and that feels like he's going to use it to judge us and mark us," that couldn't be further from the truth, but I'm aware of that and again, Accelerate the book is branded on Amazon as management book, which it isn't, it's a practical book for people to adopt a mindset and some tools and practices and ways of working, but it is a tool. When you don't need the tool, then you get rid of the tool.
It's interesting. I've read a blog post, because I spoke about these four key metrics at Excon last week. Someone came up to me at the end, [clears throat] they shared with me an article that someone had written and it was critiquing the four key metrics. I've read a few other ones as well. Fundamentally, most of them that critique them say, "Yes, but all of this stuff is obvious, why do I have to optimize for this, why am I measuring? It seems like a lot of effort for very little gain." Those articles, in my opinion, are written from the perspective of someone who doesn't need the four key metrics because they're already doing most of the stuff that the four key metrics would help them get to.
If they're already doing it, it's overhead, why are they doing it? Where you want to get to and when are you done with the four key metrics depends on your product, it depends on your customers, it depends on where you are in your life cycle. Very interestingly, I think I mentioned a minute ago, I caught up recently with John and Pete who are at Open GI. They've realized, number one, that different parts of their legacy product suite have different sweet spots for the four key metrics, and some of them, because some of the stuff they produce is like thick clients, which they need to release to customers and customers install it, every time they release a new version of something, a customer has to go off and install a bunch of stuff on a bunch of Windows 95 desktops, probably not Windows 95, but something like that.
The customer doesn't want them to install some fancy whizbang auto-update, they just don't need it. Therefore they get to the point where they can have what they want and then they keep it there. Other teams, they want to go super-fast, they can release behind-release toggles, it's go crazy. When I left, some of the teams were deploying Easter eggs because they were so comfortable. They were at Christmas, this wasn't Thoughtworkers, this was the client, if you hit a certain URL, you would get Christmas lights on your web UI.
Because they've got full control and they could do this stuff and everywhere in between and this was the kind of thing, what was interesting-- John's was the exec, the more senior to Pete, his big point was when you get to that point, you can't lump all of your four key metrics into four numbers because you'll obscure things, you'll hide the variation, which is important. You'll make some people think they need to optimize beyond where they should optimize, you give some people permission to slow down when they maybe shouldn't slow down and they could still speed up.
That's not in the book, the implementation of the four key metrics, Open GI is now really mature and again, they're using it as a tool. The teams are happy, are comfortable with it and they're using that as a way to right size and focus their engineering organization to be in the right place for the products that they're doing at whichever point they are in the life cycle. That was exciting. I was like, "I hadn't even thought about that before." They were like, "What are our metrics, what do we care about? We care about customers being able to request quotes or upload new products to the platform," and all this stuff. They could do that without having to release 20 times a day, awesome, don't release 20 times a day.
**Ashok** : It's almost like this is, in some ways, a useful tool metric like most metrics. Then, once you reach, like I think the data metrics are reports called them elite organizations. I suppose once you become elite, then you know when you're--
**Andrew** : You've gone beyond elite when you become elite you're so elite, you don't even know you're elite anymore, you forget about the four key metrics ever existing. I'm sure they didn't do this on purpose, but elite feels like something aspirational. Maybe not these days in this world actually, but it feels like, "Oh crikey, I've reached the top," but then, I think when you get to the top, you're like, "Cool, maybe I should actually take my foot off the gas a little bit and focus."
I say Open GI and other clients focus on the product metrics well before they get to elite, you can get out of the way of product delivery well before elite but at that point, the practices are embedded, the culture is set up the build measure, learn the single piece flow, all of the lean mindset type things, which are fundamentally, basically moving towards the culture of learning, the culture of sharing and all the DevOps stuff breaking down boundaries and safety and all of those kind of things.
I think by this point, you get to that then hopefully you're coming up with your own stuff. Because it's interesting. The book isn't prescriptive, it just goes, "These things are proven to improve these things." In 20 years’ time-- half of them are about the current fashion. In 20 years’ time, we'll have come up with some other thing, quantum computing will be here and all of the rules will have changed. I think things like shipping valuable product to customers and getting their feedback from that product and using that to iterate, I don't think that'll change. Maybe the tools, maybe the languages we use and where we run stuff will change, but that feels like a function.
**Rebecca** : I do think though, there is value in continuing to track these. Perhaps not continuing to try to improve them,. I'm definitely with you on that in part, just to provide that reassurance, that backsliding isn't occurring. Like any change, it takes a while to get that bedded in and if you have new people coming in and new requirements coming in and you might see some of those things degrade. It's helpful to know that they're there.
I like the emphasis on deciding what is the right level for these metrics, for these individual circumstances. I too find the elite wording, it does seem to set that up as aspirational and in some instances, it's more important that you can do something, not that you do it. I remember having a conversation with an internet service provider who said, "I don't need to worry about continuous delivery, I'm not delivering any functionality. I'm providing systems," I said, "Wouldn't you like to know how long it would take you to roll out a security patch to the operating system on a zero day?" He said, oh yes.
I do think there is something, even if you're not going to aspire to the elite level of doing it, knowing that you could, that you do have the infrastructure in place to make it happen, to me, that's very important.
**Andrew** : That's exactly it. This is what's interesting, that's very important, Rebecca, because if you look at elite and you get to deployment frequency, it doesn't keep going up. It goes, blah, blah, blah, or slash on demand. It's like, we're only deploying three times a year, but like you say, it's like some zero, Log4J has another gigantic security hole in it, they want to go [gasps] and rapidly do deploy it. Meantime to recovery again, the key thing is knowing that something is broken so you can fix it.
There's something that's always weird. It's like change failure rate, elite is 15%, which still confuse. I understand, I've read the book, but the point is-- sorry, it's 0-15%. I think for medium, high end elite or something. People always go, "That's insane, why is it not getting any better?" The point is, they've realized that by doing any analysis, there's a lot of variations. We see it, when you hit your web service provider or something, if you use Google enough, you'll get the broken arm robot. Or if you use Gmail enough, something will break. Or if you use Netflix sometimes the stream will break and then it'll come back and all this stuff.
Obviously, because they've made a tradeoff between being too careful-- Netflix talks about antifragility and all this stuff, failures will happen. They don't want to over optimize for zero failures, because that's a false economy. They do want to optimize for, "Crikey, we broke it, we need to get this thing fixed fast," and that's key, like you say. Then you get to that point and that's where you want to be. That's your business value and that's predictability and all those things. It's like avoiding control, but giving you the possibility to do things that you want. I think that's the--
**Ashok** : I think with what described as the interrelationship, almost between some of them between how fast can you deploy versus how quickly can it recover. Also, these are all, I suppose, guidelines or thresholds that you set and then you go and reevaluate that time. Maybe there's the other aspect of any guidance if at all is, you said these ones, as we're saying, you also look at-- I suppose the trend is a lot more valuable to look at than the absolute number at a point time.
**Andrew** : We talked about it a little bit in the book, but after I wrote the chapter, I read working backwards, the book about how Amazon work. There's a really interesting bit in there, which I've shared with Pete, because Pete's still, obviously working at Open GI and they were talking about how they visualize their data, because they have metrics all over the place at Amazon, how they visualize their data. One of the things they shadow plot, and Pete now has the ability to do this. They plot, this time last year against, right now. Pete and I would plot the last 30 days for lead time. Pete now has enough data, I don't know if he's done it, but we were talking about it. We said it maybe not as important as for Amazon, but it like to shadow plot this time, this month, last year or this 31 days last year to show the improvement or to show that it's the same or to show that, before Christmas we do lots more deploys.
If you have all of this data, you can do some super smart stuff. Another reason why I advocated in the chapter and in the talk for building your own, you can get loads of things like Thoughtworks have metric, which we provide to do four key metrics is Google four keys, there's a million plugins for Azure DevOps and Jenkins and all this stuff-- not Jenkins are JIRA. The benefit Pete and I got from rolling our own was we could collect the data in our own format and then we could interrogate it for tons and tons of stuff. When we had these discussions on a weekly basis, questions would come up from developers and they were good questions. We were like, "We don't know." Then it was like an RFI to the dashboard and we'd go away and add extra things to the dashboard.
Again, like product development, they're like, "Oh, I've got a question. I've got a need, I want to know, what's the 95th percentile for this, I don't know, we'll find out because we have the raw data and we could put it up." The other interesting thing, that Rebecca's question made me think, the thing I liked most about the Simian Army and Netflix and the Chaos Monkey and all these things, which nobody ever talks about. It goes back to meantime to recovery and there's a blog post again, that someone's-- they're like, meantime to recovery is nothing because it's basically the time it takes to deploy 99.9% of clients. I think customers, the time taken and meantime to recovery is not writing the code to fix it, delivering it to production.
It's noticing it's broken, it's turning panic into action, it's finding the right person to do the right thing at the right time and arranging it and deploying stuff. Again, that's what Simian-- the reason I believe they do most of the Simian Army stuff and the Chaos engineering at Netflix is to normalize failure. That's what you want that's to remove the panic time in the meantime to recovery, to just shrink the human being carnage down to like, "Oh problem fixed, dah, dah, dah." That's the thing. I think that's what you want to optimize for.
**Ashok** : It made me smile, just reminded of the time that I think Rebecca and I were on a fairly large program work where, I think it was for a large retailer, there was an outage and we were trying to figure that out. Actually the figuring out what was causing the outage was the thing that took the time actually fixing was fairly trivial. It was almost like, "You just need to switch off the till." Actually, it was trying to bring some more clarity to that is quite-- yes.
**Andrew** : I've got a lightning talk called, "Turning a Crisis into a Drama." The theory was like, nobody likes an escalation, but if you treat it-- instead of turning a drama into a crisis, if you make it fun, then at least people will have-- I use disaster movies, everyone likes going to the cinema to watch disaster movies. What if we treated, escalations like disaster. It's tongue in cheek. Obviously you shouldn't treat any escalation like a disaster movie, but it's the drama that gets in the way. It's the emotions and the lack of clarity and the confusion and stuff. It's not the change in the code and pushing it to source control and watching the build run, it's everything else.
**Ashok** : That's brilliant. It was really entertaining. I think we started with the four key metrics and ended with disaster movies. I'm sure it's going to make an interesting episode for our listeners. Thank you so much, Andrew. Really great having you and chatting about architecture metrics.
**Andrew** : Thanks for having me.
**Ashok** : Thank you, Rebecca.
**Rebecca** : Thanks Ashok, thanks Andrew. On the next episode of the Thoughtworks technology podcast, I will be joined by Prem, one of our co-hosts and Gautam and Jayanta who are going to talk to us about EpiRust and BharatSim, both are agent based simulators used primarily in epidemiology. You'll hear a whole lot more about it on the next episode. Thank you.
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
More eipsides 
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
## Find out more about software architecture metrics
[ Learn more ](https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/)
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