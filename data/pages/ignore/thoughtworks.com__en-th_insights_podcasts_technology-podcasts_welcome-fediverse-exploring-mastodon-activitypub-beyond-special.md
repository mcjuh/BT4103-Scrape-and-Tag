<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/welcome-fediverse-exploring-mastodon-activitypub-beyond-special | Title: Welcome to the fediverse: Exploring Mastodon, ActivityPub and beyond [Special] | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Welcome to the fediverse: Exploring Mastodon, ActivityPub and beyond 
[Special]
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


#### Follow Thoughtworks on Mastadon [@thoughtworks@toot.thoughtworks.com](https://toot.thoughtworks.com/explore)
Podcast host  Birgitta Böckeler | Podcast guest  Effy Elden , Moritz Heiber  and Julien Deswaef
November 24, 2022 | 44 min 32 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/welcome-fediverse-exploring-mastodon-activitypub-beyond-special#Transcript)
Listen on these platforms
## Brief summary
For many who have been part of the recent migration of users from Twitter to Mastodon, their first encounters with the "fediverse" have been puzzling, even disorienting. Given a decade in which we've all grown accustomed to the affordances of corporate social media, it's not surprising people have questions: _How does it work, exactly? How am I supposed to use it?_
With so much current interest in the platform — and the wider ecosystem of which it is a part — in this special bonus episode of the Technology Podcast, Birgitta Böckeler digs into the technology and culture of Mastodon with the help of Effy Elden, Moritz Heiber and Julien Deswaef, three Thoughtworkers that have been long-time residents of the fediverse. They discuss how Mastodon works, how it sits within the broader decentralized social media landscape and whether this move to Mastodon marks the start of a new chapter in how the world views social media.
## Episode transcript
**Birgitta Böckeler:** Hi, and welcome everybody to a new episode of the Thoughtworks Technology Podcast. I'm your host for this episode, Birgitta Böckeler. I'm a technical principal with Thoughtworks based out of Berlin. Today, we want to talk about Mastodon, or the fediverse, and we'll talk about what the difference between those two things is. For this conversation I have here today the three main initiators of the Thoughtworks Mastodon instance that was set up about four years ago. If you maybe introduce yourselves, Effy Elden, do you want to go first?
**Effy Elden:** Hi, my name is Effy. I'm a lead infrastructure consultant with Thoughtworks Melbourne. I've been at Thoughtworks for about five years now. I tend to do DevOps duct tape, cloud infrastructure. All that fun stuff.
**Birgitta:** Thanks. Julien?
**Julien Deswaef:** Hello — Julien. I'm based in Barcelona; I was hired as a designer, but now I'm head of social change for Thoughtworks, Spain.
**Birgitta:** Then finally, we have Moritz.
**Moritz Heiber:** Yes, hello! My name is Moritz. I've been at Thoughtworks for almost eight years. I'm a Principal Infrastructure _Wrangler_ , I would say. I've been administrating the Thoughtworks Mastodon instance since its inception.
**Birgitta:** With some additional effort recently, I think.
**Moritz:** It did take a little bit of a head scratching initially, yes. I think once you figure out the metrics, then it was pretty straightforward.
**Birgitta:** That's exactly what we want to talk about. We want to talk a bit about how does it actually work technically, and all those aspects that we're interested in as software practitioners. How does it work technically? What are the UX implications? Does one of you maybe want to start just describing what is it? What is Mastodon? What is the fediverse?
**Julien:** The fediverse is an ecosystem on application services, of which Mastodon is maybe its most known piece of software. Mastodon is an open-source software that is often compared to Twitter because it is inspired by Twitter. It's a social media software that allows its users to post pieces of text or video or sound and connect with other users. The magic of it is that it's not confined to its own website, like Facebook or Twitter, it's just the users of Twitter or Facebook only can talk to users there. Everyone that installs Mastodon or every administrator that installs Mastodon on their server, their user can talk to each other across servers.
That's what we call the federation; it's social media software that federates. Then the fediverse is an even larger network than that, even larger network than Mastodon itself. Because we use Mastodon to describe the software, but also the network and so on and the social media platform. The fediverse is a connection between multiple software that federate through a protocol that is called ActivityPub. That allows to connect these different pieces of work together. For example, the ActivityPub protocol allows me to follow someone from another application, like their comments, reply, etc., etc.. All the usual things we do with social media but across many different services across a large network.
**Birgitta:** The way I understand, technically, Mastodon is the server software. The open source, one server software you can use to set up an instance in the fediverse, even though there are apps as well that are called Mastodon, I think, but it is the server software.
**Julien:** Yes. I think that's a little bit of the confusion because there's Mastodon as the software, which is free software released under AGPL license that anybody can install on any server. There's some forks of it already because it's open source. But then there's mastodon.social, which is the most well-known instance where hundreds of thousand people go by default to create an account. Then there are applications like Mastodon for iOS or Mastodon for Android you can install on your phone which can connect to any instance. They don't have to solely connect to mastodon.social.
**Birgitta:** In the media right now, Mastodon is often compared to email to explain to people how it's maybe different from Twitter. What do you all think about that analogy?
**Effy:** I'd say it's definitely the most commonly understood analogy. Everyone has to interact with email so it's quite a good baseline analogy. There's some ways it doesn't quite fit but the core concept of federation, the core concept of multiple different servers at different domains but that can communicate with each other, I think email encapsulates that quite well. I have a Gmail address, but I can email someone's thoughtworks.com address, and that means the servers that are running my Gmail address talk to the servers running thoughtworks.com. I think at a baseline level, it's not bad as an analogy.
**Birgitta:** Moritz, can you maybe talk a bit about the experience of maintaining this instance? What are, actually, the implications of the setup then of people following each other on different instances? What actually happens in the infrastructure if somebody toots, I think it's currently called, or “Tröten” in German, which I find even more funny.
**Moritz:** We had the luxury of having a very slow grind from the start. I think, initially, it was literally just the three of us on that instance. We only, I think, gathered a couple of tens of users over a couple of years, and only the recent surge really has put the server under a lot of stress and some more strain. I think it has unearthed some of the inefficiencies in the way that the service itself or the software itself actually communicates with other services or with other servers, as in that if you have a single user who's really popular, which in this case, for Thoughtworks, it's Martin Fowler.
Then it might actually be that a single toot, as you call it, can have a substantial impact on your service performance or the service quality at large. Then again, I think this is mainly just a question of how you design the server and service infrastructure. For us, as I said, it's been basically quiet, and the server has been non-existent in everybody's mind for the larger part of its existence. Now that we've seen some ramp up, I think the relevant scale up has been as first expected. Now, I think we're in safe waters again, and I don't believe it'll be much of an issue to scale further up should it be required. The initial onset was really for us to get the server running.
What we did really was to have a keen eye on how can we make this work with as little budget as possible and as little impact on the surroundings. We didn't ask for any help from our internal IT tech ops, we didn't really ask for help from the greater community. We basically just went around and said, "Hey, if you're interested, just join us, but we don't really want to bother you." If you want to operate it, we want to operate it on a budget, which you would otherwise consider something which is minuscule, I would have to say, compared to the value that it actually adds. Factoring all of these different things into the equation, I think it's been a fairly pleasant experience.
We've had plenty of time to get this set up into state where it's well automated and you can easily manage it with a couple people. I think just from a perspective of managing our own server, it has actually been a pleasant experience. But I believe if you look at other servers out there in the fediverse, which have now gained thousand of users, if not even tens of thousands, or hundreds of thousand of users, there in a much more dire state because it's not just about scaling the software, which was never meant to scale to the extent that it's now being used. At the same time, also the money for financing all this has to come from something.
The way that the software is intended to be used implies that to our local moderation teams on each of these instances, but also has an implication, quality over quantity whenever you are using these services. All of that basically something that we, at Thoughtworks, aren't necessarily exposed to because we already are in our own world to say, and we only have to care for the employees on the server and not necessarily but all of the other quarrels that other people have to put up with.
**Birgitta:** What does it mean technically, when somebody like Martin Fowler joins on our instance? Or there was the story that got some attention about Stephen Fry joining mastodon.social, and then things exploding a little bit. What actually happens there? I see the word “Sidekiq”, for example, in the discussions and articles about how it technically works.
**Effy:** Sure. Mastodon, there's actually several different open source protocols that power different parts of it. As mentioned, one of the big ones is ActivityPub. ActivityPub largely operates on a push model. When someone from another instance follows Martin Fowler, essentially what's happening is that the server that they're on is reaching out to the Thoughtworks server and saying, "I would like to subscribe. I would like to receive new toots, new posts from this user." Once that subscription's in place, whenever Martin Fowler makes a new post, our server, the Thoughtworks server, is responsible for delivering that post out to every server that's subscribed to it.
What that means is for someone like Martin Fowler, who has a bit less than 6,000 followers last time I checked — but has been going up quite rapidly — those 6,000 users are probably spread across over a thousand servers. Every time he posts, that essentially creates a thousand jobs, a thousand tasks for our server, which is to go out and push that out to actually make a web connection to each of those remote servers and deliver that, post that status. All of that is done asynchronously, or that's done using Sidekiq, which is a popular Ruby-based worker, so that it doesn't take more than 30 seconds to actually be able to get back to his homepage after he makes a post.
What we are seeing a lot of — as things scale as the fediverse rapidly expands and lots and lots of people onboard to Mastodon is that where you see the biggest impact is that Sidekiq, that queue of tasks that need to be done. If a server is underprovisioned or not set up correctly for that scale, then your queue is going to go up and up and up, and you end up with a big backlog of all the things that you have to be doing, which is where you start to see those delays. It's all quite easy to overcome, but that's the core mechanics, and there are other bits and pieces, too. As I said, it's primarily a push model, but there are cases where things are pulled. If I go on to the Thoughtworks Mastodon and I try to look up a remote user, I try to find someone else so I can follow them, that's a pull because that's my server going out and getting information from the remote to show to me.
**Birgitta:** Yes. Just reminded me a bit of this then probably also different users see a toot at different times. Just reminds me of watching a soccer game during the World Cup in Germany, and you hear people cheering for a goal somewhere far away because maybe your streaming is behind [chuckles] or something, right?
**Effy:** Yeah, absolutely. One of the interesting things about Mastodon is that it offers these timeline views by default. In addition to your feed, your home, which is all of these statuses from the people you follow or statuses that have been boosted by the people you follow, which is like a retweet on Twitter. In addition to that feed, you have a local timeline, which is just a list of every status posted by other people on your instance. 
For Thoughtworkers, that means that we can just see all the posts in chronological order made by other Thoughtworkers, even if we're not following them, but then you have the federated timeline. That's basically seeing every status across the fediverse that your server knows about. If your server knows about it, that's because either someone on the server is following that user, or someone on your server is following a user that has boosted that has essentially retweeted that piece of content. 
It's a fascinating way to get a glimpse into the very wide ecosystem that's out there beyond those small pockets that you have. Definitely, you do get those delays, and you do get things starting to weigh up. You do get cases where things can be considered to be delayed. Another case of those queues growing with scaling can lead to things like people signing up for a new account on an instance and not getting the email for six or 12 hours later, because that's stuck in a big queue behind all the posts being sent out.
**Birgitta:** Yes. I only just really made that connection, I think, with the federated timeline. If I wanted to think about, "Yes, but what does my instance actually store in its database or in its cache?" That's actually a view of the database, the federated timeline. That helps me think about it. Yes.
**Effy:** It also means that you end up with a lot of… not duplication, but you end up with a lot of local copies of remote content because your server essentially stores everything that someone on your server wants to see. So you've got a copy of a status, in the case of the Martin Fowler one. He posts something, a thousand different servers are now storing a copy of that information. If you, say, tooted a photo, that photo gets copied and downloaded by a thousand different servers. Which is great in terms of that kind of reliability and resilience and distribution, but can have some downsides in terms of storage costs and bandwidth costs because it means that you are essentially saving a copy of every image that someone else has posted.
**Birgitta:** Then there's like a storage scaling and archiving challenge there when you have a really large instance — at which point do you maybe decide to purge some older toots just to save storage, yes?
**Effy:** Yeah, absolutely. There's different ways you can go about this, but I think one important thing that I've seen a lot of people on the fediverse note over recent weeks is that it's good not to consider Mastodon a long-term archive. It's good to actually save important content, archive that content, whether that's just archiving the toots themselves using free online services like archive.org's way-back machine or saving things locally, saving images. Mastodon isn't designed as an archive and really neither is, say, Twitter. We tend to post things and think they're going to be around forever.
Especially in the case of these distributed open source networks being run by volunteers in many cases, it's good not to make that assumption. Certainly there's that trade-off between speed and storage. It's definitely a good idea to purge some of that older content because it can always be re-downloaded if and when a user needs it.
**Moritz:** As any software that's exposed to a large amount of users, it's under constant pressure from the usual typical things: CPU or compute-bound network I/O storage bound and networking itself. Outbound and inbound bandwidth is something that needs consideration whenever you are trying to scale at a magnitude that some of these server instances require. I would also like to add that I don't believe that you'll ever come to a point where you would actually have to delete most of the content that's coming in or out of your instance because compared to what else you are actually accumulating on the server side, it's quite negligible.
I have a funny story just from yesterday where I basically deleted, I think, 450 gigabytes of media data that was still stored in our instance from years and years ago. Because that is definitely something which makes quite a dent, so we had a run rate now, I think, of 500 gigabytes after five years —or four years — on the instance. Those are all just pictures, videos, audio files. I think most of them were GIFs accumulated over the years and stored on our server because it is fetching all of this content as well, and it doesn't just contain text.
The text itself will still be available, but whenever you're revisiting those toots now from, let's say, three or four years ago, which were in our federated timeline, it will re-fetch the media again to present this toot to you instead of just fetching it from your local cache. I think from a scaling perspective that is a much more important metric than the actual textual content that's being displayed.
**Birgitta:** It's "just text," which these days is not that big of a deal anymore. [chuckles]
**Moritz:** I think it changes over time as the fediverse changes. I think at beginning it was mainly text, and then people kept adding metadata and kept adding other media content as well. Now, you have large instances, for example, which are solely dedicated to posting pictures or posting videos, not necessarily based upon Mastodon, the software, but rather on other software. That there's Pixelfed, for example, which people associate with Instagram or it's interfaced with Instagram. Then there are other instances like Funkwhale, for example, which are in and of itself linked to services like SoundCloud or Spotify. You have implications depending on what the software actually supports and what type of media content you'll be serving, which have an impact on how you design your server or your service infrastructure.
**Birgitta:** One other thing that I've been wondering about technically recently is how do these instances in the fediverse actually get to know each other? When you set up a new instance, it doesn't know any other, right? Is this all about people joining the instance and starting to follow others?
**Julien:** Yes, but actually it's a connection with which you said before, is that you mentioned that the federated timeline is the view of everything that reaches your instance, but that's a very important aspect is that there's no global view of the whole fediverse. There's only the view from your instance, where you are. If you search, for example, for a hashtag, for an instance that already exists, if you look for a hashtag or a user or whatever, you will only see what has already reached your instance. It's not going to go and fetch in all the instances whatever's out there. Yes, when you start an instance, it's empty.
I like to say that actually when you start on your own account, it's empty. That's the magic of social media. It's becoming this thing everybody keeps checking all the time, but it's empty at the beginning. It's only what you bring there that starts to become interesting. It's because you bring something that basically you come back. You have to start connecting to people, but then where do you find them? If there's no one on your instance, if you're the first user, you're going to have to go and find those other users somewhere else. You're going to have to use a different network. Already your email and where people have shared their Mastodon handle with you, or use a web search, or whatever, or Twitter.
Now people use Twitter to find people they're already connected with and to connect with them on Mastodon. That's how you start populating your feed, but then you will get access to more because they boost other content, they link to other people, they mention other people, and that's how the network... [crosstalk]
**Birgitta:** Oh, sorry, go ahead.
**Effy:** I was going to say there is also the concept of ActivityPub relays, which are becoming more and more common. There are servers set up that don't have any users, but they're designed to let small servers get a bigger view, so you can connect a small new empty Mastodon server to a relay, and because several large servers are in there, that suddenly means that your federated timeline has all yellow posts, which you are seeing now, not because anyone on your server is following them, but because they are being relayed through the relay. That's another kind of discoverability. [crosstalk]
**Birgitta:** That means that if I look for user, ideally I have the, let's say, direct link that includes their instance domain already. If I search for a hashtag, my server will only search for that hashtag on the instances that it already knows? Not in its local storage, but on all the instances that it knows.
**Julien:** Maybe — Effy can confirm — but if you look for your hashtag, you will only see the cache of your instance that mentions that hashtag. For example, I run my own instance in my personal account. When I type my hashtag, now it's different, but at the beginning I can only see my posts that have it. Now it's getting a little bit more because I'm getting more and more posts from other instances where the hashtag might be mentioned, but you only see what your instance knows about.
**Effy:** That is something that's being tweaked a little bit in the latest version of Mastodon that came out quite recently, Mastodon 4.0. Mastodon 4.0 provided the ability to follow or subscribe to a hashtag as opposed to a user as a way to promote that ability to subscribe to topics that you are interested in and get more content related to them. Again, ultimately, it is always going to be limited by the servers that your server communicates with. That depends on what it knows about, and that's where those relays can also…
**Birgitta:** Including filter the things that the server decided to not know about, like blocked instances. 
Let's maybe move on a little bit from the technical implementation to how to design a user experience in a decentralized federated environment like this and in an open-source environment as well. Julien, you said in your introduction already you're a designer. What are your thoughts on this?
**Julien:** Actually, it's something I haven't fully wrapped my head around, but I'm really interested in the challenges that it brings. Especially, for example, the one we just mentioned, which is discoverability. How do you discover new people and so on? That's a big challenge. If we step out a little bit maybe from just Mastodon and think about the fediverse and ActivityPub, here we have Mastodon's account, and that's what we mostly use, but we also connected with people who are using Pleroma, or Misskey, or PeerTube, or Pixelfed that was mentioned, or Funkwhale, or Lemmy, which is an equivalent to Reddit, and so on. They all interconnect with ActivityPub.
That means I could potentially follow someone with an account on Lemmy, on this equivalent of Reddit, follow someone on Pixelfed, and all their posts will show in my Mastodon timeline within my Mastodon interface. There's an expectation or a habit with regular social media — the big silos like Facebook and Instagram and so on — is that everybody sees the content in the same interface if you exclude maybe some weird clients that exist when the API is open. Normally, everybody has the same experience. I think that was one of the reasons that Twitter closed its API, is that it wanted to make sure every tweet was delivered in a consistent way.
**Birgitta:** It's almost like Apple locking down their ecosystem to have more control over the user experience versus Android where it's all a bit more messy.
**Julien:** Exactly. Here with Mastodon, it gets even more mind boggling because someone who would be posting on Pixelfed to have creative feed of very carefully crafted pictures that they're posting, will appear in a completely different way on a Mastodon feed or Pleroma feed and so on. There are also some features that are maybe designed a little bit differently. Actually, we mentioned when you're on an instance, Mastodon or else, you already have only a certain view of the fediverse. Then, you layer that on top that, what you're probably seeing is your own experience of that content because it might not have been posted in a way like that by the initial person.
The intent or the experience of the posts on Pixelfed is very different than the experience of someone on Mastodon. I think we haven't grasped yet the implication of that in terms of what that means as a social network where everybody has a different experience.
**Effy:** I think also seeing the evolution of more types of open source websites on the fediverse, the fact, as you mentioned, that you have a Reddit-like, you have a YouTube-like, you have an Instagram-like. I think as we see that expand further, it's going to be more and more interesting. Wait until there's an open-source eBay equivalent with ActivityPub, then the challenges of _how do you stop your feed containing user statuses from containing listings for items for sale_ is going to be a fascinating one.
**Birgitta:** It will be interesting to see in into how many things that ActivityPub data model can be shoehorned. We all know this probably from applications we've worked on how existing data models have to shoehorned to mean something else in a different context to avoid changing the data model.
**Julien:** There is a good example of research right now I think — and I don't know what's the state of it — but GitHub is a very particular social media software for developers. The social aspect is around issues and setting up everything that is not handled by Git but all the other services that make GitHub a central place. There's quite a few people working on trying to add that ActivityPub layer to some Git hosting software. What's that coming to, how is that-
**Birgitta:** Interesting.
**Julien:** -going to be used, I'm very curious.
**Birgitta:** Also in terms of user experience, users might all have different access to features. Maybe because their instant software hasn't been upgraded to the latest version, or I was initially using an app that didn't actually give me the bookmark feature, so I was using favoriting of toots as my bookmark functionality.
**Effy:** It can be from completely workflow altering ways. People can have completely different workflows or use Mastodon and other fediverse-compatible platforms in completely different ways depending on features or just through to minor things. A great minor example is on one of my Mastodon accounts, I follow a friend who has Pleroma. Now, Mastodon and Pleroma both have support for custom emoji. Little emoji icons can be uploaded to a Mastodon instance with a custom code to represent them, and they can be embedded in toots, and that correctly flows through. If, on the Thoughtworks instance I post something with a custom Thoughtworks emoji, when it's downloaded by the remote mastodon server, it downloads the emoji as well, and I can see that in the toot.
However, Mastodon doesn't support emoji in names; the account name that you have that displays above your toots can't contain emoji. If you try and put an emoji code in there, it'll just be plain text. Pleroma, on the other hand, _does_. And so my friend's name when viewed from a Mastodon instance just contains this code for the emoji, whereas in Pleroma instance, you can actually see the emoji inline. That's just one small way that there's all these challenges around compatibility and interoperability.
**Birgitta:** I've had that on Twitter though as well, not seeing emojis and not understanding why. [laughs]
**Moritz:** I was about to say, I think you rarely ever see this in corporate social media or in these walled gardens that the other social media giants actually have built over the years, because they're usually at the helm of the user experience and how people perceive their existence. Twitter was once — famously — a very open and very developer-friendly company and used to empower and enable a lot of developers to do whatever they pleased with the data that Twitter was producing, be that just the raw content or the metrics that came out of users participating in the network.
Then, over the years, I think this directive, this paradigm had changed, and Twitter became very restrictive and even shut off a lot of the APIs the developers were very fond of using and didn't replace them with, I think, feasible alternatives. So I think a lot of the behavior that people associate with other social media, or especially the corporate social media they're used to, is much more focused on consumption and therefore the owners of that social media empire have to be in charge of what it's like to consume the content because otherwise, you wouldn't be able to present a coherent experience.
I think that's one of the main and key differentiators really is with this decentralized approach to social media to just connecting over a large network, is that there is no single entity who's in charge of the experience because, precisely, it is not meant to replicate the same experience. It's not meant to be the next Twitter. It's not meant to basically repeat the same mistakes people have made in the past in trying to monetize on that particular scheme, but rather it's meant to offer an alternative — that comes with a lot of pitfalls and people are used to other experiences — then again, I think it offers a compelling alternative that people just have to get used to over time.
I see this as the main gripe with a lot of folks that are migrating over from Twitter, for example, is that it does not represent the same level of coherence, user experience — it doesn't satisfy the same expectations that people have from an environment where it's mostly just about chasing the next big thing. Whereas here, it's mostly just about following other people and enjoying each other and enjoying their content.
**Birgitta:** For what it's worth, I found Twitter very confusing when I first started using it. 
**Julien:** No, I agree. There's an interesting aspect about the fact that the experience is not the same and we have multiple software — right now, all open source might not be in the future — let me phrase it like some power dynamic at play. Because Mastodon being the most popular of it, it is driving the implementation of the ActivityPub protocol in a certain direction, which some people have complained. Mastodon developers have decided, "Oh, all right, we understand the activity protocol like this, and we're going to shape an experience like this."
Because it is the most popular software being used on the fediverse, and if you want to have a career and experience where emojis are shared and you still have communication between people, then now other software that want to connect with the fediverse are a bit constrained to follow how Mastodon has implemented certain aspect. It's a discussion in the community of developers around ActivityPub. That's very interesting also to see happening because, as Moritz said, there is no consensus; there's nobody ruling saying how it should be. There is a group that defines what the ActivityPub protocol is. It's a W3C group, and it's been very active long before Mastodon, I think, existed, but they're not defining how you should implement it, that's left to the software creators.
**Birgitta:** I think this whole thing is so fascinating to me. There's so many aspects to it, and we could probably talk about it for hours. Before we wrap up, I just want to ask one more question. Julien, do you actually have any experience in the open-source context to contribute from a design perspective? Because a lot of the clients are also open source — or all of them. Do you have experience with that as a designer contributing user experience [chuckles] designs and stuff like that to open source?
**Julien:** Yes and no. I would say the experience I have and which I think is the most profitable one is I'm part of a community called Libre Graphics, which, until the pandemic, had a yearly gathering in different parts of the world. It was the only gathering of developers and users and designers of free software for graphics use. I think this was really the best opportunity to actually have that conversation between designers and developers of free software and open-source software and the users of it to start actually getting to that because GitHub is great, a great interface and so on. It's great for developers; it's not that friendly for bringing a design experience there.
It's really an adaptation from the designer to the developer language. The experience I've seen from the designers wanting to contribute to open source software was more to find areas where they could actually meet and discuss. That would be for me, in my experience, the best approach.
**Birgitta:** Discuss with developers as well to find opportunities to pair, let's say. Let's try to wrap up then. Maybe I would be interested that each of you, where do you see this going? Do you think this momentum will keep up? What other things are popping up? Are you hopeful about it or worried about it? [crosstalk]
**Effy:** I think the concepts at the core of the fediverse are definitely not going anywhere in a hurry. We're seeing such mass adoption, and we're seeing such an ecosystem evolve. As mentioned, we're seeing big players start to buy into that as well. Something quite interesting that happened relatively recently was an announcement from some of the people who run Tumblr about looking at bringing Tumblr into the fediverse and making it ActivityPub compatible. Seeing — I don't want to say traditional — but one of those big centralized corporate social networks look at how they can become interoperable with this big community is fascinating. I really hope we see more along those lines.
How long Mastodon is around for I couldn't really say — I wouldn't want to speculate. I think if there is going to be a Mastodon killer in the future, it's very likely to be something that is, to a degree at least, federated and able to work with these protocols. Because it actually offers the ability to entice users towards your product and your experience without sacrificing the communities and networks that you have. That's been the big reason that platforms like Facebook and Twitter have endured for so long. Someone might start something new and better, but if all the people that you follow and interact with, all your friends and family and colleagues aren't there, then you're only going to hang around there for so long.
Getting a critical mass has been the big barrier to so many failed social networks out there. What we see with the fediverse from ActivityPub is that you can build something new. You can make it easier for users to come and dabble and see if they like it or not while keeping their networks, their communities, their follows, their friends, the people they need to interact with. I think that power means that you're not locked in. There's no lock-in to nearly the same extent with any of these new tools like Mastodon, Pleroma that you see with proprietary locked-down ecosystems like Twitter, Facebook.
**Moritz:** I think it's pretty much in the same lines as Effy has already said. I just hope that people will start discovering more alternatives to what they perceive now the fediverse is, which is largely just this Twitter replacement thing, but also discover things like PeerTube, for example, where you can upload your own videos and still share them on the fediverse. Or even alternatives like Mobilizon, which offer you all of what you get with other proprietary services like Doodle, for example, or Google groups, or, I think, Facebook groups as well. I think there's a lot of potential in the idea behind making things more interoperable.
I think the protocol itself, which is the underlying current of this movement, has enough flexibility to really bring a lot more ideas into this network than what we've seen so far. I like this idea of replacing Twitter or finding an alternative to Twitter is driving adoption right now, but I don't think it'll sustain this movement until eternity. People will likely want or wish to discover other things as well. I think there are a lot of opportunities out there right now, and there will only be more opportunities as time progresses. I think I'm actually quite positive on the future concerning that.
**Birgitta:** Julien?
**Julien:** I agree with both views there. Especially I think on the current wave of Twitter users, unless as Martin says, Twitter goes MySpace, it's probably going to slow down. Less people are going to switch over and probably out of the million that switched in the last couple of weeks, three-quarters are going to go back to Twitter if Twitter is still there. There's a large proportion who's going to stay, and it's going to come back to this steady growth it had for the past five years. 
I think, though, in terms of what I'm really hopeful is that ActivityPub as a protocol is here to stay. It's still going to be here in 10 years because we're still using IRC, we're still using email, they're still in newsgroups; every open standard, it's still in use today.
Maybe not by large population but they're still people using those open standards. Especially on Mastodon, you see people running Gopher servers and other things of that nature. I think we've only scratched the surface with ActivityPub. There's so much more to happen. It's going to be really interesting to see how it's going to shift and shake the network when a large corporation or large social media platform is going to implement that. I'm curious to see how the network is going to react. Looking forward to the future.
**Moritz:** Sorry for barging in. I think one of the most important aspects of this growth and also of the future of everyone who participates in this network is that I strongly believe that we have to rid ourselves of these growth metrics that are applied to these processes. How many likes did you get? How many followers do you have? How many? users does this instance have? How many users or user growth or active users a month this instance or the network itself have? Really? Because finally, the network allows you to get rid of them. I think that’s the key differentiator for me really. On Twitter, this what drives the bottom line — this is how Twitter makes money. This is why they have to put this center stage. That's not the same case for Mastodon or any other software in the fediverse, really. Because the metric doesn't matter. 
What matters is, where the people are and who the people are, and what they want to say, what they don't want to say or what content they produce and actually put out there. Which is not to say that people aren't looking at these metrics; I just think that really, whenever you speak or talk or see other pieces or content pieces on this migration, people always try to zone in on this X amount of users migrated recently. I'm usually inclined to say it doesn't really matter for me, and it shouldn't matter for anybody else because this isn't Twitter anymore or this isn't Facebook anymore.
That's also one of the things that I still enjoy about this surge of new users right now is that you can finally see that although this is no longer a factor, people still enjoy what they see and what they experience. It's not something that has to be a part of social media. It's just something that people imposed on social media because otherwise, it wouldn't have been profitable.
**Birgitta:** For me, the key is also — I think you've all touched on that — interoperability, because it opens up options. There could be a corner office that is still, what you just described, Moritz, what you do not like. Then there are also corners where you can freely go where it's not like that, and you can choose to do that. 
Cory Doctorow, he's been writing and talking about interoperability a lot over the past few years. He's always talked about adversarial interoperability. Forcing this through regulation on tech giants, let's say. I recently saw somebody tweet or toot [laughs] that it's nice to see some momentum for non-adversarial interoperability finally. I think all four of us are very excited about that. Let's see where this goes in the next few weeks and months. 
Thanks a lot for the conversation.
**Moritz:** Thank you.
**Julien:** Thank you.
**[Music]**
**[END OF AUDIO]**
Follow Thoughtworks on Mastadon [@thoughtworks@toot.thoughtworks.com](https://toot.thoughtworks.com/explore)
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
## Find out what's happening at the frontiers of tech
[ Explore Technology Radar ](https://www.thoughtworks.com/en-th/radar)