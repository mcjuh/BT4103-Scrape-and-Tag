<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/who-make-software-architecture-decisions | Title: Who should make software architecture decisions? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Who should make software architecture decisions? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Neal Ford and Prem Chandrasekaran | Podcast guest  Andrew Harmel-Law
December 26, 2024 | 35 min 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/who-make-software-architecture-decisions#Transcript)
Listen on these platforms
## Brief summary
Who should be involved in the process of making decisions about software architecture? That's a question that's been puzzling Thoughtworker Andrew Harmel-Law for some time — so much so that he decided to write a book about it. The result is Facilitating Software Architecture. Published by O'Reilly in December 2024, it's both an argument for and a guide to involving more people in the architecture decision process.
To discuss the topic and the book, Andrew joined hosts Neal Ford and Prem Chandrasekaran on the Technology Podcast. They explore why including more roles in software architecture matters today, some of the common objections to and risks of such an approach, alongside techniques and practices that can make doing it in fast-paced and dynamic organizations easier.
_"It's quite magical when you see this blossoming of understanding of what it is that architects do... It's not less architecture, it's more. It's just happening in a broader sphere."_ — Andrew Harmel-Law
You can find Andrew's book on the [O'Reilly website](https://www.oreilly.com/library/view/facilitating-software-architecture/9781098151850/).
## Episode transcript
**Prem Chandrasekaran:** Welcome everyone to another episode of the Thoughtworks Technology Podcast. My name is Prem. I'm one of the regular co-hosts of this podcast. Along with me, I've got Neal Ford and Andrew Harmel-Law. Neal, do you want to quickly introduce yourself?
**Neal Ford:** Indeed. Thanks, Prem. Hello, everyone. My name is Neal Ford. I'm another of your regular hosts and our guest today. I keep bumping into in person over and over again because I was traveling in Europe, some in the fall. Welcome our guest today, Andrew Harmel-Law.
**Andrew Harmel-Law:** Thanks, Neal. Thanks, Prem. Thanks for having me. I could introduce so quickly as well. That's why I'm a colleague of Prem and Neal. I'm a tech principal based out of London in the UK. I'm usually the senior technical person working with a client. I get to do architecture, but I get to do a bunch of other stuff too. That's typically what I do.
**Neal:** The reason we keep bumping into each other most recently is that Andrew has just published a book with O'Reilly, and that's what we're here to talk about today. What is the name of said book? Andrew, what's it about?
**Andrew:** The book is called _Facilitating Software Architecture_. It's based on the premise that we need more architecture, not less, as the software systems that we're building are tending to continually evolve and change all over the time. We're trying to get more teams wrapped around those architectures and more teams flowing and delivering their changes to production, but as a consequence of that, what I was seeing more and more in my day job was me being an architect was, I was a blocking thing in the flow of all of these changes.
I'd started experimenting with different approaches to making sure that the right architecture happened in the right way at the right place and got down to the code, but without me being a blocker. Fast forward four in a bit years, and you end up where you are now, or where I end up now with a book.
**Prem:** Awesome. I was going to ask you about what inspired you to write the book and call it Facilitating Software Architecture. Maybe you've answered some of that, but are there other things that inspired you to write a book?
**Andrew:** This isn't a book that I thought I was going to write. There were other books which I pitched to O'Reilly, all of which the ideas were deemed terrible, but this one came about. This one came about because I mentioned the fact that there's typically we experience, or I experience anyway, we come in and help clients build softwares, typically important, complicated software. I was becoming more and more stressed, and I talk about this in some of the talks. I do that, introduce it.
I was realizing that I'd come along, and all my thought was colleagues would come along, and we would modernize how you did architecture, how you delivered and ran software. I was realizing that the more my ThoughtWorker colleagues optimize for flow and continuous deployment and evolutionary architecture and all of the continuous quality and things, I was rapidly becoming the bottleneck. I was the part-- I'd be like, "Well, we need to make sure this is a good decision, and we need to make sure that this gets implemented and pushed down to prod," and typically, my client pairs or my client peers.
I tried to come up with a way that would approach this. I tried lots of different things in various places, but then when COVID happened, I was really lucky to have a really willing client and a really supportive ThoughtWorks team. We tried and experiment to see if everyone thought there was-- because with COVID, they thought there was a big opportunity to do this really big refactoring of an architecture for one of the clients who are named in the book, actually. We tried a lot of stuff; we learned a lot of things. Like I said, the client is actually explicitly named in the book.
It's because we didn't always succeed. I learned a lot. They learned a lot, but lots of things came out which worked around about this process, which we can talk about maybe in a minute. Since then, I've been doing that with multiple different clients, trying out different things. What I've realized is there's a very simple core to the approach, but then there's a lot of extra things which you can bring in if you need. That's how it turned into from a blog post into a book because there's a lot of lessons learned. There's a lot of sociotechnical stuff around about the core technical practices.
That's how it turned from a, I don't know, an 18-page blog post because Martin Fowler likes you to write quite detailed blog post or articles into, I think, a 520-page books. It got pretty, or in forms, it's quite a lot of pages that got quite big.
**Neal:** This is often one of the things I state as the superpower of consultants because we get to see a lot of different projects and approaches and get-- If you're a good pattern matcher, you can see patterns, and of course, with superpowers from Kryptonite. One of the problems we often have is we don't see projects from beginning through the middle and through the end, but it's great for this kind of process. It sounds really promising, but how does this work? How do you get the architect out of the ivory tower and stop him from being the sole arbiter of important decisions on projects?
**Andrew:** It's a great question. It's basically I've been playing with a concept called trust organizations for a long time in my previous employer and then at ThoughtWorks. One of the core practices in trust organizations is the idea of this thing called an advice process, which is a decision-making process. The advice process is very simple, and it's quite good for talks because it fits on a slide. The process is anyone can make any decision. In our case, it's the architectural advice process, so anyone can make an architectural decision as long as they seek advice from two parties or two areas.
One area are people or teams who will be impacted by the decision. Therefore, you need to think about dependencies and whoever's going to have consequences placed on them based on your decision. The other one is people with expertise. Again, it helps you and drives you to go and seek out those things. What I didn't realize until I wrote the book was that that's effectively a social contract. I expect people to trust me to do this well and do it properly and seek the right advice as long as I trust them and they trust me, so this thing builds up.
That is the fundamental advice process. Correctly, that would then in the fast-moving, evolving complex world of software delivery, that would lead to complete chaos. The thing that I really liked with lots of experimentation was the key thing you need is some transparent form of capturing those decisions, but also capturing the advice. ADRs is one way, and that's the way I've written up in the book, but what's cool is I've spoken to other people who've ended up at lots of good ideas. Other people have said, "Oh, we've ended up at a similar approach."
We've also tried the advice process, but we've used RFCs or whatever, but some transparent, semi-synchronous, maybe asynchronous written way of communicating, so you can have a record and an immutable record of what's going on. That's the core. Around about that, you can decorate lots of other processes. The idea is you do build trust, learn as a collective, et cetera, et cetera, and make sure that you maximize involvement and make failure safe, et cetera, et cetera. All of those things happen, but what was interesting was, I've done this with some clients where you end up putting in place lots of things.
I've done this with other clients where you think you need to put in place lots of formal measures, but it turns out the teams already have a pretty good idea of what their architectural principles are and they've got a pretty-- I've even been to clients, which was terrifying, but I have seen it where they had a pretty good implicit understanding of their cross-functional requirements. They knew what the overall performance and availability, et cetera, things of their services should be.
Maybe I've written them down to make them clear, but they've always been there, but you needed these aligning forces to make sure everyone heads off in the right direction, because otherwise, everyone will scatter and you'll end up with chaos. That's the fundamental core of it, and then, like I say, you add lots of extra bits to make sure stuff works.
**Prem:** Is the premise then that anybody can make architecture decisions, and as you said, as long as those two groups of people you seek advice from, but that presumes that the folks that you're seeking advice from are at a level of experience, competence, and other humanities-
**Andrew:** Yes.
**Prem:** -for this tool to scale, right? Doesn't this become very chaotic very quickly if you don't have the right kind of people?
**Andrew:** It's interesting. Like you mentioned a minute ago, one of the blessings is we get to go everywhere and one of the curses is we leave. What's really cool is Pete, who is my pair at the client, I've stayed in touch with Pete so he gets mentioned quite a lot in the book. Hopefully, rounding up Pete and one of the team lead architects from that client to do a talk at a conference coming up that I'm building or putting together a track on. They were a really good case study. There were a few people who had the architectural expertise.
Pete's recently published an article which he calls The Autonomy Rollercoaster. Pete and I had a big question at the start, have we unleashed chaos because of this autonomy? What's very interesting, and it does depend on the client and the level of skills and the level of trust, but typically, when you roll this out-- and it's definitely good to roll it out small. There's bits in the book that say do it with one team, or if you're an architect, do it individually as a practice.
Then you can show that you're modeling the process because there's a learning about the process and there's a learning about how to engage the right people and have the right conversations. If you do that very rapidly, the appropriate for your architecture, your code base, your client, and your context that surrounds it, you'll rapidly find that kind of thing. In some places where it's-- This is a case study that's written up in Martin's site as well, Xapo Bank.
They were a Bitcoin bank, so decentralization was in their DNA. That's how they expected the world to be, not just their software. They already had a high level of architectural maturity. They're the ones who already had like implicit CFRs, et cetera, et cetera. Lots of the stuff was there, so we were just trying to help them be more efficient because they liked to have a nice debate. Most of my coaching there was like, "You don't need to agree." It doesn't say everyone needs to agree, you just need to consult and listen and understand.
Other clients where I've done this, it typically tends, you think it could be everyone deciding, but it starts off typically with the people who decide anyway. We'll still keep deciding, but you'll start engaging people in a way that you and Neal recommend, but there's an explicitness in that engagement. I'm speaking to you because I believe you have an expert role, or I'm speaking to you because you have an advisor, an affected team role. Then you model that behavior and then slowly people will start saying, "Oh, there's another thing."
I've seen, for example, a client we were going along doing stuff and most of the architects were doing most of the system architecture work, but individual teams would see an opportunity to refactor some of their architecture. It's nice and tightly scoped. They don't want to have to seek advice from lots of other teams, so they specifically scope their decisions, so that they can do whatever this thing is without having a big impact because they don't want to cause impact that is responsibility of a system architect or someone with a broader view.
They'll scope it to that level. They'll come seek the advice. They'll seek lots of advice from people who have got a broader architectural view, so it'll help them shape those things. Then they'll put those things into practice and get all of the learning because it's more within their field of control which is nice. It self modulates, it self-select. The key thing you do need to do, and this is where most 50% of pages of the book came from. Architecture becomes like Ruth Mallon says very much about conversations. It always is conversations, but you're broadening out the circle of who are having those conversations.
What's nice is you start watching because obviously you've got the ADRs, which you can see these conversations happening. Sometimes you realize the conversation's happening and you can see the advice and there's nothing you can add, so you just leave it alone and you keep an eye on it. Other times, you're like, "That's going in a terrible direction. Let's add a pretty detailed comment about why we think this isn't going to work." Other times, my kind of chaperoning will be, "I don't know the thing, but I know you should speak to operations because they definitely have an opinion."
Or in banks, "Please speak to regulatory because I know that this is something--" I'm not the domain expert in regulation about cryptocurrencies, but I definitely know you should speak to this person because they know. It's more about conversation curation and explicitness and all the skills that Neal and I have talked about before about clarity through writing and clarity through communication. All of these things slowly grow.
There is a learning curve, but what you'll see is and the key thing, which is again in the book, the accountability typically in more traditional approaches, the accountability and responsibility for decision making sits with the architect, the person with the architect and the job title. That spreading round, making that clear to everyone is key because some people think, "Oh, I can decide but I'm not accountable for it." If your name's on the ADR, then your responsible — and that checks the reckless people because they're like, "Oh, okay. Right."
It's my backside that's going to get kicked if this goes wrong. Then you'll see people, they'll fall back from deciding to advice giving and then they'll slowly build their skills up and move into that space. It's a transformation thing and that's why I've been very interested to speak to lots of other people who've tried this approach because it's a definitely an organizational learning type thing.
**Neal:** It changes the role of architect from sole decision maker to curator of the garden of decisions that are growing underneath your feet, which I guess is the best guard against I think Prem was touching on the subject of what happens if you have people who shop for a yes. This is a controversial decision, but I know those two people agree with me, so I'll get an advice from those two but then, yes, the curation that comes in to-- Maybe the corollary to the advice or get advice from experts is at least one of them needs to be a contrary opinion.
**Andrew:** Oh, totally. There's a whole thing about-- Yes, it is 100%. Again, this is where many of the words come from because it's very simple to state this stuff and then the practice of it is where you get it. Explicitly engaging people who you know will disagree with you. Explicitly — there's a big chunk on advice isn't opinion. Should I do this? No. That's not advice. That's an opinion. Why should I not do it? Well, 300 years ago when… days of COBOL and when dinosaurs ruled the earth, we tried this, this didn't work for these seven reasons.
Five of those reasons might be out of date, but three of those reasons might be complete zingers. That's the kind of stuff you want to separate out. Then the learning, and like Diana Montalion talks about, like the knowledge stocks, which are typically-- a few people know everything about a set of problems or the architecture or whatever. You begin to flow that.
Because this is happening in the open in ADRs, and this is what I've seen, which is amazing, people who don't feel confident enough yet to start stepping up to the space can see architectural peers, people with more experience asking the right questions, even digging into stuff like, there'll be a request for comment. Someone will provide advice. Then the original requester will say, "Oh, can you tell me more about this?" The practice of architecture, which frequently is never done behind closed doors, but you know what I mean? It's not explicitly open.
Suddenly, lots of that can happen and it's quite magical when you see, although Martin Fowler advised me not to put the word magical in the blog post, but it is quite magical when you see this blossoming of understanding of what it is that architects do. That's my point. It's not less architecture, it's more. It's just happening in a broader sphere.
**Prem:** Does this sounds fair to say? Let's say, I'm not doing the things that you're advocating for, but I'm curious and I want to get started. Are there any formal methods that I can do to pivot to using the approach that you're advising for?
**Andrew:** Yes. There's two-- Again, I outline this in the book. Either you're someone who already has the authority and the responsibility to make decisions, so then you could keep doing that, but write them down as you might already be doing in architectural decision records. You identify the individual decision, you write the context, you identify the options, and then you go and identify the people to seek advice from and seek advice. You tell them you're following the advice process. You say, "It's still me, I'm still responsible, but I'm seeking your advice because I want to incorporate it into the decision."
Then you make sure they write the advice down because typically it works best if-- If you've recorded the advice which others have given you, it's not as transparent because you might misinterpret it or whatever. It's better if the person who's giving the advice writes it down. Then another nice clean discipline is to say, you can bring all of that and acknowledge all of that advice in the body of the ADR.
You can even, and this to Neal's point earlier, it's really nice practice to say, "Despite this advice from so and so, Person X, who knows exactly what they're talking about, I've chosen to not do this because product management or someone. We believe that it's acceptable to do this or we believe we'll get a benefit that will outweigh the downside." That's if you already have that authority. Alternatively, you're a team that would normally go to an architect to seek input advice with an architect who's responsible for multiple teams.
You can still do the same process, but acknowledge the opposite that you still have no responsibility or accountability to do this. Here's an ADR. We've prepared. We'd love your advice. We'd like to get to the position where we can understand your thinking about architecture to such an extent that you are reading it and going, 'Yes, yes, yes, I completely agree. I've got nothing to add." If the architect has things to add, then you can add that and then you're openly learning and teaching.
The goal in… it would still follow the same process. We're currently doing that and my client. They still have a centralized signoff process but the goal is to get so boring that that's almost like a rubber stamp exercise because we're like, the teams are better, the CFRs are more explicit, the principles and the overarching architecture are clear because of continued teams trying to consume this architecture and make their decisions at their level. There's been a feedback loop between these higher, more overarching architectural aspects.
Because you could say, "Oh, the team doesn't know what they're doing," because they've taking a decision that's wrong or in the wrong direction but then what we're trying to encourage is the overall architecture to bring that back up and say, "Okay, we need to make this clear. Or this is an implicit CFR or an implicit principle, which isn't stated." That can tune things. Then at some point, people get more and more comfortable, so therefore, you let go. It works pretty well. Not as well as it could with the centralized sign-off, but it can get really close. My current client, it's what we're doing.
**Neal:** It also occurs to me that a side benefit of this approach is that you very effectively grow your next generation of architects because software architecture is not something that you're a developer one day and then you go to a three-day seminar and then you're certified and you're an architect. It's more apprentice-based, and this is a way to basically, force people who bump into decisions to apprentice for the length of that decision to look at some of the issues.
**Andrew:** Yes, totally. It's nice. Some hate the experience and never want to do it again. The titles of most of the subjections in my book didn't come from me. They came from read to my editor, but there's a thing which is something like just because you can decide doesn't mean you're obliged to decide. It's nice. People can think they want to try it on. They try it on. They turn out they don't like it. They're like, "I'm quite happy having someone else make decisions, but I've realized I could."
Other people just like you said, Neal, they like taking, but also there's this transparency as they can see what's going on. It's a superpower. It's really good. Actually, the two kinds of people that we've been talking about, architects who have not enough time and feel like they're blockers and people who are straining at the leash, wanting to move. This is maybe to the meta question that we might ask at the end, but one of the things which was hard, but I'm glad I tried to do and we'll find out from feedback whether I succeeded. There are two audiences for the book.
The architect who's got not enough time, but wants to make sure that their architecture is evolving and coherent, and someone who wishes that they had the ability or the responsibility and accountability to take these decisions. They know they don't have the experience. They know they don't have everything, but they don't know where that path is. That's trying to bring those people together to say, "Right, this is where you might be able to overlap. This is where you can benefit from each other. We'll find out if I succeeded."
**Prem:** Yes, here's a question I have. I completely appreciate the whole advice process that you are looking folks to adopt, but how does one prevent that from becoming a command scenario? It's not advice. It's basically, I'm telling you, this is what it needs to be. How does one prevent that situation where it's all top-down?
**Andrew:** It's a very good question. Basically, there's spread, there's a talk that I do called A Commune in the Ivory Tower, where I explicitly identified four failure patterns. I tried to put those failure patterns in the book, but they ended up spread around a bit. That is completely a failure pattern that you've seen, Prem, like you can imagine. I might have even been that architect. There's a story where I was like, "We're doing the advice process up to the point where someone makes a decision I disagree with."
Then there's a story I tell where there's a conversation between me and Pete because it was ThoughtWorkers who were planning to do the thing contrary to our advice. I said to Pete, "This is bad. They shouldn't do it. We should tell them not to." I can, because I'm a ThoughtWorker, so I'm senior and I can tell them not to do it. Pete was like, "If you do that, you've crushed the whole thing immediately." He was right. That's why it's in the book because we stepped back and we trusted them. It totally can.
The things that I do, and-- if all of the people with the authority don't want to give the power up, and if there's no trust, because this doesn't work everywhere, to be very clear, like Eric Evans once got asked. Domain-driven design, does it work? It sounds like it's the universal panacea. It'll work everywhere. Eric was like, "Here are the 17 places where it doesn't work. There are places where this is not appropriate." The place where I think this is most inappropriate is where people don't feel the need to give up that centralized control. People don't feel the need to share this power around.
Maybe that different places which don't evolve as fast, which aren't shipping software as quick as everyone else, that's fine or where the trust doesn't feel like he'll ever build. In my experience, it builds a lot more than anyone would ever think. That's why if you start small, you can see that the trust comes up. If you do it, there are things you can look out for. It's basically the four-- you know it's succeeding or failing. If you look out for the four key metrics of decisions.
Number of decisions per month or whatever, how long it takes a decision to go from draft or proposed to adopted, number of superseded decisions, which is like a change failure. Is a decision and then it turned out to not be true or whatever and we changed our decision and the time it takes to go from a decision which has proven to be not perfect or not suitable to something that is suitable? Those are metrics you can look at.
On top of that, if you look at who's doing the deciding and who's offering advice, if it's the same three old men doing all of the work, you're like, "We've created the illusion of this being inclusive, but it's not really." That's what I'll do, although it's very infrequently required, is having lots of conversations with people and saying, they'll be having opinions where you are affected or you are an expert, you have some experience of this, so please submit this stuff. It's usually very interesting to watch people go, I didn't think that they would care.
Most people in software are typically trying to do a good job and just stay afloat and make it evolve in the best way that possible. Yes. There are saboteurs, I think chapter 16. There's the CIA saboteur manual, which is how to sabotage decentralized decision processes. Quite a lot of that is appropriate. If you wanted to sabotage that, I address all of those things. The biggest thing is the transparency and the writing down of things and hopefully the pressure from product or the users of the system that you want to see us evolve.
That's the thing that should hopefully ungum the machine and make it work.
**Neal:** What about something that I would view as inadvertent sabotage? Like somebody falls in love with some golden hammer technology, like an XML database or something that's clearly inappropriate, but--
**Andrew:** That shouldn't happen in real world.
**Neal:** Yes. They love it and think it's the solution to every problem on earth. I guess you just have to keep saying no to them until they stop or pick another toy.
**Andrew:** Yes, exactly. You'll see it. You'll see it in the advice, it'll keep coming up. There's an example in the book where the DBA, the answer to everything is a database. For some reason, if we need distributed Caching, we could just deploy Oracle all over the place. We need this and the DBA will do it. It's good. You won't seek their advice and you want to-- especially if you think it's relevant seek their advice, but you don't need to follow their advice.
Again, the trick of acknowledging it, but saying yes, but, an XML thing is suitable for other things. In our specific circumstances, and this is nice because if you're right, I can't pick between this option, this option or this option, even though we all gut feel know that the XML database is wrong. Typically, there might be implicit CFRs, which nobody is talking about, and you're like, "Right, there is a reason why to do this versus that, but it's in the CFR, which everyone is assuming was explicit but isn't," or there'll be a principle which is implicit or not fully understood.
I've had some really nice experiences where the old architect who's got a strong opinion will give you a gigantic quote and you're like, "Oh, there's two principles, or lessons learned or war stories, which are in this, which we should pull out as principles." Constantly feeding those back into the broader shaping and guiding landscape, which is what architects typically have in our heads, but we don't always make sure it's consumable ad developers, pulling all of those things out is key.
Again, I spent quite a lot of time looking at the open agile architecture framework from the TOGAF, The Open Group. A lot of this is in there. It's just they haven't really said how. My book in some way is an answer to like, if you want, there are other ways, but this is a good way to try and approach this stuff.
**Neal:** Let's talk about a slightly different architecture because you clearly have the entire book in your head right now, having just finished it. One of the things that we typically do for authors is ask them a little bit about the writing process, about what they liked, what they didn't like, what was unexpected, which is usually how long it takes to write the stupid thing. What'd you think about the writing process?
**Andrew:** Lesson learned number one, I thought I could write, but I couldn't write, but so O’Reilly and I don't know if other publishers do this, they had an editor who I would write a chapter. I'd draft a chapter, I would send it over Rita, she's happy that I mentioned her name. Rita would read the chapter, completely gut it. I had this annoying thing, which took me about 16 of the 17 chapters to unlearn.
In talks, you can bury the lead and you can do the big reveal at the end, and it's like, "Oh, you can describe the problems in the horrible world that everyone is living in and lead them on an emotional journey." O’Reilly Books did not want an emotional journey. The big reveal at the end of each chapter would be the end of each chapter. Many times Rita would go, she'd start sending me meta documents, which would say where everything had moved to because all the words would be the same, but they'd completely shifted around.
Diana Montalion calls this the architecture of the book. You write the book and then you re-architect it and refactor it. That was very hard to learn, but it's such a power move. I've really, really having properly written a big book now, the structure of knowledge and how you present it and who you're thinking about, like your audience and all this kind of stuff, which is important in software architecture, super key. It was very interesting to do that. That was cool. Again, because the book was early access, pre-released, there were people reading the book and giving me feedback.
There's quite, and lots of people gave me lots of little bits of feedback, but some people were really, really waiting for the next chapter, really using the book, really doing stuff. They gave me incredibly detailed feedback. That was super advice. Some stuff I acknowledged and then said-- but I choose to ignore it. That was amazingly powerful.
I don't know how I could write a book in a black hole and just go into a cave and write the book, and then come out and assume everyone liked it because there's tons of stuff in later chapters that are like, "Yes, but what about--?" "Oh, God, I hadn't thought about that." Another chapter appears to cover off these circumstances.
**Neal:** Just like in software, having faster feedback gives you better adaptive direction. I've never written a book yet where I didn't write the first chapter first and then write the entire book and then rewrite the first chapter from scratch because it's completely changed. Because you think you know what it's going to be about and then you write the thing and then you realize what it's actually about and it's very often-
**Andrew:** It's hilarious.
**Neal:** -quite a bit different.
**Andrew:** Yes, 100%. That's exactly what-- The preface was like, I think I completely binned the preface and rewrote it actually because it bore no resemblance to what I thought this book was going to be.
**Neal:** Well, and the other thing that a lot of people shockingly discover when they encounter a professional copy editor for their first time is that what you think is a first draft is really like a third of a first draft. That is where the adage of writing is rewriting comes from. That's mostly what it is.
**Andrew:** Yes, it was amazing. I owe a great deal to Rita. In fact, Rita is in the book as a young developer because she's not a software. She's a professional, say, copy editor. Not an architect, but the quality of the questions that Rita would ask-- She just leaves these comments, I'll be like, "Oh my God, she's done it again." Things like social contract, all of the framing and the positioning and just the naming of things, a lot of it comes from Rita because she's like, "I'm trying to do this."
Therefore, there's a little homage to Rita in the book, which is a junior developer asks a very personate question, which flips the whole decision on its head. That's kind of the point of the book. It's like, if people have some skin in the game and they might, you can ignore if it's a useless suggestion, but if it's a good one, it doesn't matter if they started writing code three weeks ago or if they've been an architect for 20 years. If it's something worth bringing bearing in mind, then it's important to do that. It's a humbling experience, but it's good.
**Neal:** One of my colleagues at one point said that there are one-and-done authors or they're serial authors. Are you going to do it again or are you a one-and-done or is it too early? Early to--? [chuckles]
**Andrew:** I'm still trying to relax because it was two, maybe nearly two years. I think I've figured out the book that I pitched, which O'Reilly said wasn't the right kind of thing. I think I'm figuring out, having written this, like you said, my thinking has changed a lot. There's bits where the book drifts at the end into organizational. Not organizational design, but the last chapter is like, "How does this coexist?" Because This could be like, again, to your questions, Prem, between the lines, "This is a big cultural shift. How does this work?"
You're not refactoring the culture of the whole organization, you're just doing it within the technical organization. There's a bunch of stuff which is considering organizations from an architectural perspective. Something that was very interesting. One of my reviewers, who spends a lot of time thinking about sociotechnical systems and has done lots of research into where they came from originally in studies in the 1940s and '50s, there's a lot of stuff there, which I think is very interesting.
This book was gestating for five years. I don't know how you then write a book without having another five-year gestation period, but it's interesting. It's bubbling away, but I don't know yet what to do with it.
**Prem:** Thank you very much, Andrew. This was really, really insightful. Any parting thoughts for our listeners or those bidding architects?
**Andrew:** The big thing that I'm hoping will come out of this is, like I said, there are other people who have already done this and they're like, "Oh, I've done it. You just described it in a slightly longer long-winded way." O'Reilly, obviously, wants you to write a book which tells people how to do things. A lot of it was like, I'm not going to tell you how to do it because I don't want to be someone who's accused of creating Scrum, which is now destroying Agile later on 20 years down the line. There's a lot of don't do this because I'm telling you, but read what's going on and see.
There's so much scope for alternative extra different ways of doing this. What I'd love to hear is other people, because there's already some-- Neal and I know Sonya Natanzon, so she does loads of talks about decision making. It doesn't fully follow what I propose because I'm only one approach. That kind of stuff is super interesting to me. People are in the same space addressing the same forces, but coming up with different solutions. That's my parting thought would be like, just because I wrote a book doesn't mean it's the only way to do it.
Technology changes all the time as we all know. As the dynamics change, I'm super interested to watch and see what works, what doesn't work, and all extra things, bits that don't need to be there. That's what's most interesting to me. Using it, but using it in a creative way and remixing it and stuff is what I'm hoping will happen.
**Neal:** Thank you so much, Andrew. It's a fascinating topic. It's a great idea of democratizing decisions and getting rid of bottlenecks. Thanks for joining us today.
**Andrew:** Cool. Thanks for having me.
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
[ Read the latest Tech Radar ](https://www.thoughtworks.com/radar)