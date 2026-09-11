<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/patterns-legacy-displacement-pt1 | Title: Patterns of legacy displacement — Part one | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Patterns of legacy displacement - Part one 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Rebecca Parsons | Podcast guest  Ian Cartwright , James Lewis and Rob Horn
June 02, 2022 | 45 min 02 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/patterns-legacy-displacement-pt1#Transcript)
Listen on these platforms
## Brief summary
Updating legacy systems has been a common feature of enterprise IT. But — strangler-fig pattern aside — there’s little written about how to do it effectively. We explore the ideas of legacy replacement — and even legacy displacement — with a group of colleagues that are writing an article series on the topic for martinfowler.com. In the first episode of this two-part series, we look how they’ve come up with patterns for legacy displacement.
**Rebecca Parsons** : Hello, everyone. Welcome to another edition of the Thoughtworks Technology Podcast. My name is Rebecca Parsons, I'm one of the co-hosts of the podcast. I'm joined today by three colleagues, Rob Horn, Ian Cartwright, and James Lewis, and we're going to be talking today about some work that they're doing, documenting legacy displacement patterns. Welcome, Ian, Rob, and James.
**Rob Horn** : Hi, Rebecca.
**Ian Cartwright** : Hello.
**James Lewis** : Hello.
**Rebecca** : I'd like you to start by introducing yourself with a story about how you got interested in spending so much time on this topic or your favorite story of when something like this either went terribly well or horribly wrong? Ian, let's start with you.
**Ian** : Hi, yes. I can think of quite a lot of stories, and a lot of those I think we're capturing is examples in the writing we're doing, but I think one of my favorites are around legacy was I'd see quite a few programs where things hadn't gone wrong, and that culminated with some work I did for a client who's a grocery business here in the UK. They were two years into a 10-year program to replace a set of legacy systems. As we got talking to them, they would say things like, "Well, at the end of 10 years, we'll have feature parity with what our competitors have today." I just started to realize that, "Hold on, your competitors aren't going to sit still for the remaining eight years of your program." It was very puzzling.
Then we were talking to parts of the business who were saying, "We really need to fix these things now. We need these things sorted out." We would go back and talk to the legacy replacement program, and they said, "That's scheduled for year six."
Then the final thing that, again, I'd seen this before, but the tech they were using was already out of date. As part of the program, they had to do a massive update of-- I'm not going to mention the company involved, but the company systems that they've bought, all the customizations they were using, were not valid in the new version of that product. In the end, the net result was they canceled. They had to cancel it. It wasn't delivering for the business, the tech wasn't right, and the timescales didn't make sense for anybody. That's one example, but I guess, where all of the things came together, but I've definitely seen a lot of that over organizations over the years.
**Rebecca** : Rob, how about you?
**Rob** : As we're reflecting on projects, getting on about 12 or 15 years ago now, which is I think one of my favorite projects because of both learning and the bonds and friendships that have stuck with me from shared adversity. I'm going to call it project 647, and maybe we'll come back to why 647 at one point.
Essentially, it was talking about started off as a feature parity outcome legacy modernization project. Turned into a lift and shift because how could you possibly rewrite six million lines of code in a super short period of time? We need to start moving the code, as well as moving the features into this new platform. It was a monumental failure, but it was also a fantastic-- Commercially, it was a failure, but from a learning perspective, it was a massive success and a time when the team involved really got to understand what it meant operating at scale and distributed teams, and using some really good engineering practices in that kind of a legacy modernization context. Unfortunately, the project say, commercially was a failure, and we never made it to the end.
**Rebecca** : James?
**James** : It's funny you ask why we're interested in spending so much time getting this stuff down because I think we can all probably argue, it's probably not the most exciting part maybe on the bleeding edge of what we do as software engineers in Thoughtworks I think it's also it's one of these problems we come across so often, so regularly is very, very quick. Any software becomes legacy very, very quickly. You can always argue after six to eight months, any project is a legacy replacement project in a sense or displacement project.
I think for me it was the case of coming across lots and lots of different asks around displacing legacy. Then realizing that even though, while I can talk to my colleagues like Ian, like Rob, like yourself Rebecca, we've got all these ideas about how we've done it in the past and we can share with each other, but really, the only thing that was really written down seems to be the strangler fig pattern. There isn't much more out there in terms of a catalog of how to go about doing some of these things that we do fairly regularly for our clients, apart from quite sparse amounts of writing a marketing sign.
I guess, that's one reason, it's because there is a lot of learning. We have learned a lot over the years in how to do this successfully, in how to do it in a least risky way as possible, but also around how to take advantage of the moment in time that you have. When you have the focus of the business in terms of money to go ahead and replace something, the ability to do it better than you've done before or to leapfrog, as opposed to in the story, let's hope our competitors don't do anything and we'll catch up to them. Or, maybe get out in front and leapfrog is better.
In terms of an example, my favorite example, we had a case study on it a long time ago, it was a insurance comparison website where they had a fairly creaky Microsoft, Visual Basic, and VB6, I think it was, and so SQL Server Backend with data services, the classic three-tier Microsoft architecture. In this thing, they were trying to service all the different lines of business in the organization, so the home insurance business, the motor insurance business, so cars, and vans and things. Pet insurance, apparently pet insurance is a thing. All the different lines of business within the same codebase, and it was just becoming impossible for them to get any changes out the door.
They were into wholly a branching hell trying to get people to work on the same codebase at the same time and different products. We were involved over a period of probably over four years in the end, helping them on a journey away from this big monolithic, three-tier Microsoft stack towards a more modern C# based stack organized around events and event-driven architecture, and the individual product lines. We helped them split out into home insurance, merger insurance, et cetera, and organized teams around that, which meant they were able to go an awful lot faster, get changes out the door much, much, much quicker, and got a whole bunch of other benefits as well around things that observability. That's probably my favorite example of where we're successful. We can probably also talk about things when we aren't successful, but I appreciate I've being chatty a little while, so I'll hand it back.
[laughter]
**Rebecca** : How would you characterize this project that you're on? We call it patterns of legacy displacement, but how are you deciding things like what's in and what's out? Do you have particular criteria that you're using to select the individual ideas that you're putting out in this series?
**Rob** : I'd say we're approaching it somewhat organically. The things that we are writing about are things that they're tending to use in conversation when we're trying to talk about the legacy displacement. If something sticks as we're trying to describe how we're going about solving a problem, then it becomes more likely to be added into the catalog of patterns, if you like.
**Ian** : Also, the thing that's driving it is, in terms of trying to think of the problem in terms of how to break the problem up, that might be one category. Then once we say, "Oh, you could break it up this way?" Or, "That's how we did it on some past projects," I say, "What patterns did we then use to solve the problem once we've broken it up into smaller pieces?" I think what we're doing is feeling through different ways of solving the problem, and then documenting the things on that path. Then, sort of going back to the start, I say, "If you broke it up in this other way or you had this other situation, you might take a different path." "Oh, okay," "In which case, you might use this additional pattern along the way."
I think the challenge at the moment we have is we have an ever-growing backlog of things we want to put in, and a limited amount of time. At the moment, it's more around prioritization. I think at some point, we are going to have to say, "That's out. We're just going to have to roll some stuff out," but we've not reached that point yet.
**James** : No, sorry, I was probably going to make a joke about it. Also, it helps that Martin tells us off every week if we haven't done something.
[laughter]
I think the example-driven thing is quite important there though. The fact that all three of us and all of our colleagues do this a lot, so we're able to say, "Oh, what about this example from this client?" Or, "What about this example from another staff, another type of architecture and different topology?" Do the things that we're talking about makes sense in each of those cases? Sometimes they do, sometimes they don't. I think taking that concrete example, I think, Ian, you talked about tracer bullets a lot. What are the tracer bullets that we can use to test out whether these things work in real life or not.
**Rebecca** : I've heard you each use legacy replacement and then legacy displacement, so tell me a little bit about the name. Why did you land on legacy displacement?
**James** : Good question. I'm jumping Rob and Ian, obviously. Thinking back, I think there's a subtle distinction between where you've got something that's in place and you want to replace the whole thing. Actually, a lot of the patterns we're talking about is where we're incrementally either leaving bits of the old system there for a long period of time and displacing parts of it, and shoving slightly moving bits to the side, if you like, and the new system becomes more a priority. That, for me, was the difference. I don't know about you two.
**Ian** : I think that the change would be legacy replacement, I think, in the industry, has got a lot of folks think that means feature parity. In order to get a legacy system with a set of functionality, we're going to replace it from a tech perspective. As far as a business person is concerned, they'll see the same functionality, but somehow, the tech behind the covers is better. That's become a prevalent way of thinking about legacy replacement.
Displacement is nice because we're sort of saying, "We're going to push some of that old stuff out the way, and that includes the business processes." Maybe we'll come back to this, but what we found is in when you've got a legacy system for like 10 or five or 20 years or however long, the business processes people follow when using that system are shaped as much by the system as they are by the way people work, because maybe there's a workaround or maybe there's a constraint in their legacy system that meant they couldn't work the way they wanted to.
You want to displace that also, otherwise, you take a workaround that was put into the mainframe 10 years ago and it becomes a must-have requirement for your brand new system. That was one of the things we’re trying to get at, was it's not just replacement of the tech, we're trying to do something subtly different.
**Rebecca** : Yes, it reminds me of an internal discussion we had on our Hivemind Software dev mailing list about whether replacement of the tech should actually be the goal, and the utility of actually thinking what is the outcome that we're hoping to achieve by replacing the legacy. Very often, changing that mindset away from just, "I need to dump this tech," to "This is the outcome I'm trying to achieve," can help in fact shape what the new system actually looks like and help with the prioritization as well. I always thought that that was an interesting distinction when I heard in the early days of what you all were trying to do.
Are you finding this pattern's formulation to be useful? There's patterns in everything, enterprise architecture, integration architecture. We had an earlier episode in this series from Unmesh on his patterns of distributed systems. Are you finding this pattern formulation to be useful in this context, or is it just a nice convenient name for these are the kinds of things we see sometimes?
**Ian** : I think it is useful because, especially when Martin approaches it, it is in terms of saying what it is and then saying when it's applicable and how you might go about doing it. I think sometimes without that two-pronged attack, you can just say, "Here's some clever technical stuff." As to when is it the right time to use it and when is the wrong time to use it, can get missed. I think there's other reasons, but I think one of the reasons that patterns are nice is because they bring some contexts with you. They say, "In these sorts of situations, this might well be useful. However, in these other circumstances, this probably isn't the right approach for you."
**Rob** : I think as we're, I say, writing more, we're finding, certainly, there's some things that aren't going to fit into that shape either, like certain tools or techniques or things that we use to maybe help break a problem up. Those things, we'll just have to write about in their own way. Not everything is going to fit the formula, but it has been really helpful.
One of the things I've enjoyed working with Martin on is his approach of avoiding antipatterns as well in that no one may take decisions lightly. No one sets out to do something maybe suboptimal with hindsight. There's this thing of not writing something as an antipattern, but rather maybe a pattern with now limited applicability or applicability that applied at the time with the given context.
**James** : My first-ever conference talk I did was at Agile Vancouver. I did a talk on antipatterns of agile adoption. Mary Poppendieck was absolutely scathing about the fact that I chose to talk about antipatterns that I think, rightly so, looking back with it.
[chuckles]
Obviously, it was very embarrassing, but I think that's really important, the point you made, Rob, Ian, no one sets out to do the wrong thing. Everyone sets out in the best intentions. If we can capture that rather than the failure modes, it's much more useful, I think, for people to do that. For me, it's being useful as a collaboration tool as well to use the pattern structure because it means we each know to an extent how we're going to fit our own thoughts into this structure and we can coordinate across it. I feel I can coordinate with others with the two of you more easily.
I guess there's one final thing on the patterns. The patterns point I think you touched on, Rob. We're coming across a lot of examples and a lot of stories that we all have about individual displacement activities or individual clients and programs at work, whatever it is. I suspect they might fit into a different type of format in the book, in the collection as we go forwards. Whereas, it's more of a story, more of a business parable almost with a set of patterns to back them up, but I'm not sure about that yet.
**Rebecca** : In talking about structure, and you alluded to this earlier as we were talking, there are clusters. Do you want to talk about how these different patterns might cluster and what kind of flow there is to--? If you were going to approach this from, "I need to do a legacy displacement," so how do I go about doing it? I'm assuming that's your end goal is, here's a playbook for someone who's going to actually do it now. How do I start my way through this? Can you talk to me through those clusters a little bit?
**Ian** : Yes, I can talk about one of the first clusters, I think is around how to break the problem up. What we found as well is there's often-- The challenge of legacy replacement, I'm choosing my words carefully there, is it can pull in a huge amount of scope, and you get to this situation where people say, "It's too hard to break the problem up."
When we reflected on where we have seen legacy replacement done well, people did manage to break it up. It was difficult and it was challenging to do, but they did break the problem into smaller parts.
The first set of things, if you like, at the beginning of the journey, is a set of the techniques and approaches you can use to try and find ways, find the seams is how we've been referring to it is where are the seams in how the business works where I can start to break up this system that's become all things to all people? How can I carve on part of that off The exact right way to do it might depend upon how the organization works, how the business is organized and so on. There are a set of patterns and techniques there, right at the beginning, which is first, find a way to break it into smaller parts, before you then move on to try to think how I'm going to then do each of those steps, each of those slices that I've made, how am I going to tackle each of them in turn.
**Rob** : Another one of the clusters as well is, and you touched on this earlier, Rebecca, is about that outcome. Why are we doing or needing to do this legacy displacement in business terms? Like you said, the replacement of the technology itself is not always the, or it shouldn't really be the outcome, the end game. It could be like you want to be doing it because of cost of change. Maybe your business is no longer able to respond to competitive threat or to just make the simplest changes on a customer-facing website or service. Maybe it's you want to improve business processes. You want to be able to optimize something or to try and experiment, do something new.
If it is about replacing the tech, that's likely to be because of spiraling support costs or a business carrying a significant amount of risk because of systems were going end of life. It could also be because there's impending disruption. Maybe your industry you're working in is about to undergo some significant change, and the systems supporting your business now are not going to be fit for purpose for the future. We also talk about, yes, how can you get agreement across all of your stakeholders around how are we going to even measure success, and how do we even know when we're finished this exercise at all?
**Rebecca** : I'll just remind you all, there's one more.
**Rob** : There's two more.
[laughter]
**Ian** : I think then there's the implementation part. It's there now. Okay, that's great, so we've agreed what our measures of success will be with the business. We've sliced the problem up. We've found a way to tackle it in terms of being able to deliver things to the business in an incremental way, but then how do we actually go about doing that? That's where, if you like, the very much pattern-focused bit comes in where we've got patterns like revert to source, divert the flow. Patterns which are around, how can I take one part of legacy, build something new, but I've also got to have plumbing back into the existing systems or maybe into the data warehouse because we've got to keep the reporting going and so on? That's the implementation patterns. Okay, how do I actually do it now? How do I actually get to being able to deliver something?
**James** : Yes, and then I think there's finally the fact that often, the journey or mostly the journey can't end even when you've displaced something. Often the journey needs to keep going. I think Ian mentioned the start, as you mean to go on, that behind this idea of incrementally displacing something is the idea of continuing then to deliver incrementally changes over time. Often, the organizational structure will need to change in order to accommodate that change in delivery processes.
One thing I quite liked, so Elyiahu Goldratt, the famous management consultant who wrote The Goal, he talked about what's the questions you should ask if you're adopting new technology. He said, "Most organizations will see this new technology, maybe we've displaced this new legacy system that's really shiny. What were the old limitations that we had before adopting the technology? Now, what were the old business processes? Now what were the things that we couldn't do previously?"
Then he says, "You should look then for the old rules that you had in place to manage those limitations. Did you have lots of governance in place, because change was hard or testing was difficult? All that sort of thing." Then he says, "The final piece is that most organizations don't ask is, what are the new rules that we need when we're managing this new technology? When we've got this shiny new thing, how do we actually use this in a way that's not constrained by an old set of rules that we can use going forward with a new set of rules?"
This is this idea of change the organization to allow this to happen on an ongoing basis. We need to look at actually the organizational structure, the rules that are hiding in plain sight, and actually adapt them as well, in an ongoing way.
**Ian** : I think when we've been comparing notes and talking to colleagues about where things have gone well or gone badly, we often see organizations, they're stuck in this cycle of having repeated attempts. I don't think this is uncommon at all, that they've had many attempts to get off legacy. What is always interesting is, usually what happens is they say, "We just chose the wrong technology. If we take the same organizational structures, the same leadership, and the same teams, but just change the tech, then we'll get a different outcome." They don't. They got the same outcome as they got last time.
This is why we think it's so important to call out organizational change because actually, maybe it's your org structure, maybe it's your leadership that mean that you keep failing to get off of legacy. Maybe it's got nothing-- Tech isn't the most important factor after all. That's also one of the things we want to call attention to is if you keep failing, just changing the tech is unlikely to break you out of that cycle.
**Rebecca** : It has that pesky people problem. We just can't get away from it. It would be nice if it was only a technology problem. [chuckles] Let's start to delve a little deeper into some of these. Why don't we start with understanding the outcomes? What kinds of patterns or what kinds of techniques or strategies? How are we actually talking to people about let's do that drill down into why are you really doing this?
**Ian** : Yes, I think the key first step is to say we can't just have the tech people in the room, and that sounds incredibly obvious. It's often the case because folks sort of get into this feature parity, look-what-we've-got-today mindset, right at the very beginning. They say, "There's no need to ask the business stakeholders into the room because they're going to see the same as they see today."
The problem, you're off on the wrong foot from the very beginning so one of the things I think is before you decide it's going to be feature parity or before you decide how to split the problem up, get other folks from the business in the room. When we talk to clients about this, we often say, "Can we talk to someone from the finance team?" People are often like, "Why? You're here to look at replacing the mainframe, why do you want to talk to the finance team?" It's because you want to understand where is the value generated in the system, because what we could do is move a whole bunch of functionality that loses money for the business. I've seen that happen. Somebody spent a lot of time and effort migrating something that didn't make any money for the business because no one ever had that conversation.
That coming up with a shared set of measures, shared definition of success for not just the tech people but for the business stakeholders as well, be they end users of the system inside of an organization, or the managers of a department, or even the head of a global part of the business. What are the outcomes you're trying to achieve?
The other part of that is if you're building something new, you need to think about where the company's heading in terms of their strategy, where are they heading in the next three or four years because the other thing that can happen is if you do this feature parity approach and build what you have today, then often, what happens is you do that, you deliver it, and then someone says, "Yes, but that doesn't line up with the strategy we've defined for the next five years." Now we've got a come back to it and retrofit all the things that give us strategic alignment. I guess it's not so surprising that to have shared measures of success, you've get the right people in the room.
**Rob** : Additionally, I've seen quite often that the drivers that different stakeholders have might appear to be intention as well, so for example, wanting to be able to decommission a legacy database or some legacy middleware that's no longer in support, versus the need to improve some business processes. A technology stakeholder might think, "Surely I need to do the absolute bare minimum in order to be able to switch off that database." How is doing top-down user-driven development and improving business processes going to help me achieve getting off of a database quicker?
It's not in the scope, it needs to be driven by what we do now, that's surely the simplest possible thing we could do to turn the database off. Then, probably not the case. As like Ian said a bit earlier, there might be a whole load of features in the system now that aren't used. Let alone the fact that the business user doesn't actually even want the system to behave how it does now. They don't want a like-for-like. They'd probably much rather be engaged and have something delivered that does meet their business needs, and would probably settle for something maybe a little bit scrappy around the edges in order to get something new and something done quicker. While it might appear to be intention and not aligned, just getting the stakeholders in the room and talking is you can potentially find these win-win scenarios for everyone.
**James** : I remember there was a fun example, I guess, with Ian and I were on a project, on a client together where we were, I'm trying to understand how to displace quite a lot of legacy infrastructure, tens and tens of older line of business applications. I've talked to old Db2 back ends and things. When we actually looked and talked to the business users about how they used the current software, actually their usage pattern was to open it up in the morning, wait for your spinning wheel of death to finish because that took ages to load all the data from Db2.
They then dump all that into an Excel spreadsheet, but pretty much forget about the line of business apps for the rest of the day. They'd work in Excel or passing that data around in a shared access database on their team. Then, at the end of the day, they'd upload the data back into the line of business application. Of course, the line of business application had all this incredible functionality that could do X, Y, and Z, and was really whizzy and things, but it was so slow and old that they never used it.
The approach that was looking to be taken was to replace like-for-like those line of business applications, which would've meant those users fundamentally got nothing from the whole project at all, nothing from that process and would've been left-- It's a quote that I like using. One of the business users said, "I feel totally alone when it comes to IT and their support for what I do in my job."
I think what that highlights is another aspect of this, which is user research, which is user experience, which is service design in the UX sense of service design, going and finding and sitting with the real users of the software that we're displacing to understand how they do their jobs. This is not rocket science, it's how we've been, hopefully, trying to build software for years. It seems to be missed quite a lot when we talk about feature parity and legacy displacement, so yes, that would be my tip.
**Rebecca** : Are those difficult conversations to facilitate? James, you alluded to this. These aren't parts of the organization typically that talk to each other very often, so are there tips to facilitating that conversation and helping get over those bumps so that there isn't the feeling like you have two gladiators that are going to battle to the death because they don't like each other anymore? It's how you can get past that. Are there some tips that you've used to help smooth over those conversations?
**James** : I've got one very important tip I always try and use. I'm not sure how scalable this is, but I always try to have Ian to have those conversations. That's what--
**Rebecca** : [laughs]
**Ian** : Oh, I probably have to respond to that, but I think there's definitely applying some techniques, like event storming or business model canvas can be very useful, but initially, not to define what the new system is, but rather to get a shared understanding of objectives. It's back to that measures success and finding the common ground between the two different groups, because you're right, there's often frustrations. I can think of organizations where the business were like, they'd pretty much given up on IT. Smaller changes were taking six months, costing hundreds of thousands of dollars.
IT had got frustrated with the business because they blamed them for years of budget cuts. The reason they haven't been able to replace all these old systems was the money had never been available, and that was the business's fault. Just getting them in the room and cutting straight to the chase of what should we do next, isn't the right first step. I think first you've got to get them in the room, get some shared understanding, maybe even have some sessions where people can vent a little bit, get some of those frustrations out on the table, but to say, "Hey, we all made the best decisions we could, given the information and resources we had at that time. That's the history. Now we've got that out the way, let's move on to starting to think about how we break this problem down together."
I think the other thing as well in terms of, and it is a trust-building, because there's often trust is broken down, is if you can show there's a plan where they start to see things early, and this is jumping ahead a little bit to some of the other things we talk about in the articles, but if you can show you're going to get something early and there's a way that you're going to be able to respond to the feedback of end users and from business stakeholders, you can start to demonstrate that, that can really change people's attitudes.
Because the fear they've often got is, "Oh, here we go again. There's a bunch of consultants. They're going to write some huge document with everything we do right now. They're going to disappear for four years or whatever, however long it is, and then we're going to get a system that looks like what we've got now and doesn't solve any of my problems that I see in my business day-to-day." It's those two things, it's building up, it's clearing the air a little bit, but working in a way where feedback can happen often, and that's the way to build trust.
**Rebecca** : Let's talk through a bit of that final stage, the changing of the organization and the processes. Give me a little more color on some of the strategies that we use there.
**Ian** : I have a favorite one which is quite radical, if you like. At the far end, if we had a spectrum of what our options might be, one is, we call it NewCo It's not like we invented that, but the idea is basically saying, "Look, in a large organization, there's this idea of organizational antibodies." I can't remember who came up with that, but it's a brilliant analogy, where, oh, it doesn't look like the rest of the organization, and so the structures and the meetings and everything will get rid of that new thing.
What we can do is almost start a brand new company. You say, "Right, we're going to have a new building, a new organization, new reporting lines. We're going to go off away from the mothership and we're going to do something different. We're going to build this new thing." Then, what you might do is start to migrate folks from the old organization into the new organization.
I still describe, if you like, the most radical way to crack that particular nut. There are less radical ways of doing it, but I always think it's interesting, almost as a thought experiment to say, "What if we did do that? What would it look like?" We might not end up doing it, but we might learn some interesting lessons by just considering it as a possible option. That's one way to come at it.
**Rob** : I was thinking about maybe when your outcome conversations haven't quite gone as well as you'd have hoped. You have your IT organization who are heading off down a, let's say, a feature parity path. Don't worry when you get your new system, we'll then be able to start iterating on it and putting in new releases every couple of weeks. "Okay, that sounds good," says our person from the business, "When is that going to happen?" "That's going to happen in three years' time." "Okay."
Now, what's happening in that three years is you're learning or reinforcing your ability to not release software every two weeks. What we need to do, we need to help organizations to change that and to be able to release incrementally. That's really at the heart of what we are proposing around start as you mean to go on and either deliver value early, mitigate risk by doing things in smaller pieces. By doing that from the start, hopefully, you can continue in that vein and continue to respond to change as you need to.
**James** : I guess another thing I've seen is a misunderstanding that when you move away from say one big monolithic, big mainframe that's doing all the things that's got your ledger, that's got payment process, and that's got the whole works in it or something, and you're starting to move away and break some of these capabilities out into their own, into their separate capabilities, which are implemented maybe by a set of microservices or whatever it is.
Then, once that's been delivered, you expect to have the same support structure in place managing the operationalizing this now what, 50 set of 50 microservices split between these different capabilities. Then unless you are, I think as an organization, understand that you also need to start thinking about your organizational boundaries around what our product teams look like, what capabilities are the product teams going to be looking after on a long-term basis? Are we going to have product teams?
The product team isn't just to build the thing and then hand it over to your service management group in the IT operations, the product team is there to build it and run the thing long term. These are all quite subtle shifts in how, I think, we've come to learn about rightly, about software engineering. Dave Farley talks about these days is as some modern software engineering, but if you're not set up for that, and I think you can fall into the trap of just doing the same old thing and trying to manage a hundred services in the same old way that you managed the one big monolith.
There's actually a signal, I see quite a few signals quite often where you have questions like, "Oh, we need a set of architects because someone needs to understand what these hundred services do. If you're thinking about capabilities and you're thinking about product teams, you only ever need to understand what three or four services do. Then you've got a boundary to another capability when someone else understands what those three or four services do. No one really needs to have the understanding of everything, which is a fairly radical change. I think for a lot of organizations.
**Ian** : In terms of, I mentioned organizational antibodies and organizational change, I think a great example of where you do need change is things like a change board. Many organizations, especially when you've got a very large legacy system, because it's running the whole business, there's a lot of processes that has grown up around that. We don't want people just being able to go in there and make changes because we're running the whole business on that. That will have a certain cadence, and there'll be certain release cycles. That's often could be a month or three months, or you might only have a release once or twice a year.
The organization in terms of its processes, and those change boards, and how they run, how responsive they are, they're setup for like a month or every three months. Then, if you then come along and say, "We want to be doing test release, we want to get fast feedback, we want to do stuff every week, we want to release," that isn't going to work. All of that has to get batched up into the three-month chunks to go into the change board.
That is definitely something we've seen with organizations where they start trying to do something new in terms of how they're approaching the software engineering and the deployment side of things, but they don't make the corresponding organizational changes. Then these existing organizational structures and processes slowly caused the program as a whole to revert back to these three-month or six-month-long releases.
If you like, that's an example of these organizational antibodies in action. It's not that anybody's setting out to sabotage or make the program fail, they just say, "My job is every three months, I go to this big meeting. We spend two days going through all the change requests, so we decide which ones are going to get to be approved. Everybody has to write a big document saying why they're doing that change, and then we do that again, in three months' time. If you don't get in this time, you should apply to the change board three months from now."
They're not setting out to cause folks to be unsuccessful, but you've got to be very aware, if those things are in place, you've either got to agree you're going to not use them or they have to change how they work.
**Rebecca** : Okay, I think that's enough for today. I hope our audience will join us for part two of this discussion where we will go through the other two clusters of these patterns, which is how do you actually decompose this? Then how do you actually deliver this in the ways that we've been talking about? I'd like to thank you, Rob, Ian, and James, and we'll reconvene and talk about the rest of the story. Thank you.
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
## Explore the latest Technology Radar
[ Explore ](https://www.thoughtworks.com/radar)
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