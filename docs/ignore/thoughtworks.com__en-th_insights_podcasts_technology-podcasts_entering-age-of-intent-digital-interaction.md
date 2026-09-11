<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/entering-age-of-intent-digital-interaction | Title: Are we entering the 'age of intent' in digital interaction? | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Are we entering the 'age of intent' in digital interaction? 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Lilly Ryan | Podcast guest  Sara Taraporewalla
December 23, 2025 | 45 min 24 sec 
Listen on these platforms
## Brief summary
The 'age of intent' is a phrase that's been around for a number of years. However, with the rise of AI agents in 2025 it has the potential to become a key trend for 2026. It describes a new way of thinking about digital interaction in which the gap between human intention and output are reduced even further through AI assistance.
Thoughtworks' APAC CTO Sarah Taraporewalla has been exploring the age of intent in recent months; she's written a series of blog posts that tackle what this new phase of digital interaction means for businesses and how they can prepare themselves.
On the latest episode of the Technology Podcast, Sarah joins host Lilly Ryan to discuss the concept the age of intent and its implications for the future of digital experiences. 
**Read Sara Taraporewalla's series on the age of intent:**
  * [The interface is dead. Time for the age of intent](https://www.thoughtworks.com/insights/blog/generative-ai/the-interface-is-dead-time-for-the-age-of-intent):
  * [From prototype to transformation](https://www.thoughtworks.com/insights/blog/generative-ai/the-age-of-intent-from-prototype-to-transformation)
  * [What it takes to become an intent-ready organization](https://www.thoughtworks.com/insights/blog/generative-ai/the-age-of-intent-from-prototype-to-transformation)
  * [Rethinking value in the AI economy](https://www.thoughtworks.com/insights/blog/generative-ai/the-age-of-intent-rethinking-value-in-AI-economy)


**Lilly Ryan:** Hello, welcome to the Thoughtworks Technology Podcast. I'm Lilly Ryan. I'm one of your regular hosts, and with me today is Sarah Taraporewalla, the CTO of APAC here at Thoughtworks. Sarah's written an article series recently over the last couple of months exploring what happens to businesses when users stop navigating interfaces and simply express what they want to AI systems. She's calling this the Age of Intent. I'm really interested to hear more about it. Sarah, welcome. Please tell us what is the 'age of intent?' Is that the one we're in now?
**Sarah Taraporewalla:** Thanks, Lilly, for having me. I don't think I'm the only one calling it the age of intent. It's definitely the phase that we're moving into. I think you can really classify what we have been doing in digital business today as much more like website and mobile driven, where people have to fill in web forms with complete sense of data in order to get responses from the servers.
We're rapidly moving to this intent-based world where we're instead of saying what a specific thing that we need to do, we just, say, describe the intent that we're trying to have, and describe that context that we need. We're ending up more fuzzy with our interactions, and as a result, there's some changes that we need to do and think about as we build out our digital products.
**Lilly:** This is a five-part piece, that series that you've put together for Thoughtworks Insights. I've read through it, and there are quite a few of these little avenues that you've gone down in terms of what businesses, users, everyone needs to think about as these things are evolving. The one thing I appreciated about the way that you framed it is that, in addition to being the age of intent, perhaps, it's more about the age of experimentation that we're not quite at that point yet, where this is actually what's happening, but we are at a point that it's becoming possible.
People are trying it, and you've provided a bit of guidance for the way that people could try it, the way that businesses might want to approach it. What do you feel about the way that it's actually expressing itself in the world right now, you seeing businesses use it or starting to use it, or are you more hopeful that we could get more of that and see what actually becomes possible?
**Sarah:** I think we're still in the really early days at the moment. I started to write the article series when ChatGPT announced first the buying experience, and then their apps at SDK in ChatGPT, because that was really the unlock that I was waiting for to really start to understand how organizations could actually be participants in this new ecosystem that I could see emerging. It's been something that's been coming out for the last year at least, but not really understanding the shape and the form that it's going to take until that announcement.
Now, following that announcement, we've been trying to play with this idea a little bit more now that we've got much more tangible and concrete APIs and SDKs that we can work with so that we can really start bringing to life some early-stage prototypes to get teams to reimagine and rethink about what this might look like. I think it's really interesting and fascinating time. You've heard it from lots of people before, just the speed, that this is changing is crazy.
It's not too long ago, and I can still remember, and Lilly, I'm sure you can still remember when mobile phones came about, and the first stage apps that we had. I remember one where you could pretend to drink a beer with your phone, and as you tipped it, it would look like it was being poured out of the glass. That was really us experimenting with this new technology and tilting, and the motion that the phone could give to an app, but that was meaningless. People bought it for the joke, not to do anything.
It took another revolution of apps and rethinking to actually start doing experiences on the mobile that we're expecting today, but that felt like it happened over a couple of years and organizations having the time to actually think about what that first mobile experience might look like for them, having their customers be a lot more accustomed to having mobile phones that were smart phones, and then moving into the applications, and pace of change felt slower.
Now we're seeing a rapid pace of change. Why that's important is that in this space, I think much more than the mobile app space, it does feel like you get an early intranet advantage if you are one of the first participants in this ecosystem. Zillow's there as one of its launch partners. Expedia is there as one of its launch partners. You can see what advantage they can have from a discoverability, from a searching perspective, by being early-stage adopters there.
I think right now, we're in this flux of, it's worth having active conversations in organizations about what this might do to change the customer experiences, the customer interaction, but more importantly, what they need to do within their own organization to enable and prepare themselves for it. The actual SDK is easy to work with, I found, but it's like anything. It's productionized in a system that's going to take a lot of effort in most organizations.
**Lilly:** I've got a lot of questions about what you think this could look like once we are in a space where it's more widely used. Before we get there, I wanted to know more about what you learn from working with the ADK, with the SDK, and with building out an application. Could you step listeners through what your view was for that particular application and the way that you were thinking about how it might work in an intent-driven interface, what that looked like in practice?
**Sarah:** Yes. The first prototype that I created with it, just to play around with it, is something close to my heart, and it's all about travel. I like to travel, and I'm the family travel agent. I set about trying to create just a flight exploration discovery. Not really booking system, but something that would surface flights. I used dummy data. I found it was easiest to explore the tool with just coming up with a set of good, structured dummy dataset.
Then I just played with creating a simple MCP and then simple UI components. I used Codex to help me. I had a working prototype within half a day of doing that. It was actually really easy and really quick for me to set it up. It just relied on my knowledge on React and how React works, and knowledge about Java or Python of two different versions. The code was clean. It was easy and simple to play with. Once I had that first prototype version of it just working in, first, MCPJam, and then actually within ChatGPT Dev environment.
I then started to explore the different conversations that I could have with it. The first version was really recreating that web form experience, and booking the departure and arrival city, the dates, the number of people traveling, and then having flights returned as a result. Then I started to have some fun and experiment with the type of conversation that we could have, and much more loss of information or buildup of information through that conversation that we had.
**Lilly:** The core thing here, I suppose, if it's not already coming through for folks who are listening along, is that the interface that we're talking about here, there is still an interface, but you are having conversation with a large language model, with a service provider, with a chat bot kind of thing in order to get the information back that you want rather than clicking through a website in order to get that information and driving it yourself, is essentially the idea.
That you can either connect your own servers to that, or you say that you are an airline and you're trying to expose that information, you can then connect your server to ChatGPT directly. Also, that information about your flightsmight also end up in that conversation because of search-related tooling that ChatGPT already has, that kind of thing. Both of those things, as I understand it, are in the mix for what we're talking about with this intent-based interface. Is that right?
**Sarah:** Yes. Importantly for me, it's more than just text that you get back, which is if you use ChatGPT or any of the other chat LLMs. You're very familiar with that. You write a message, and then you get text as a response. This takes it one step further, and you can actually get HTML as part of the response. You can get a lot of the visual elements coming back, which means that you, as an organization, can actually start to own that branding as well.
**Lilly:** That's a good avenue, I think, for us to look at at the moment. We've talked about what that user experience looks like in terms of getting the information that you might want. You've got this chat-driven, intent-driven, "I want to find a flight that goes from A to Z, and here is my budget. What can we do?" From a business point of view, that control is an interesting one as well.
This is where I think we do start to get a bit more hypothetical and where it is a bit more experimental, because we know that traditionally, the way that businesses have been able to be found online is by search engine optimization, by using SEO in order to make sure that whatever somebody puts in, if they're searching, and it's usually via Google, that your results come up at the top.
Ideally, that would be the most relevant things, but because Google, being a search engine provider, has the control over the algorithms and how those decisions are weighted, search engine optimization has always been a bit of a game of cat and mouse or whack-a-mole or whatever analogy you want to use. In general, there has only ever been one SE2O for like, no one's doing search engine optimization for Yandex quite so much outside of certain parts of the world, for example.
In this case, we have multiple different search engines in the form of multiple different large language model providers, and we also don't have the control over what comes up. If you have a snippet that comes up as a result in a search engine, you know what that's going to look like. It's either going to be first, second, third, or it could be a sponsored place or whatever.
If it's being pulled back as a result of a large language model's thing, you can, as you say, have HTML, and that's one thing I want to discuss more about what that experience is like, but also synthesized text results in general so that the words that you are putting out there are not necessarily precisely the words that are going to come back and land in front of the user. It may not even be the language that the user is talking with you in. That presents a couple of different challenges.
One for the branding, two also for the context in which your results would appear, and three, I suppose, for how you keep track of that, some of which you've discussed in the articles. Because you've started with the HTML snippet, I'd like to hear more about how that works. I then would also like to talk more about how and when you can actually develop some understanding as a brand of how that information is being delivered to people. How are people finding it if there's no click-through to track, which is traditionally how it's been done?
**Sarah:** Let's caveat this completely by saying this is a podcast reported in a point of time. This is moving at such a pace. Advice that we give today--
**Lilly:** It's hypothetical.
**Sarah:** It's hypothetical. With that under our belt, I'm seeing a couple of different things coming out. SEO, when it first was introduced, was considered a black magic in a black art. Some people understood how to take advantage of it, and over time, a lot of people seem to suggest to add lots of keywords in a robot's file. That was one way to help improve your SEO ranking. GEO, which is the term that I've seen used most effectively for the generative optimization, again, seems like a very much of a black art and is still being figured out.
It looks to me, although OpenAI hasn't been completely clear and transparent yet, we're still waiting for more information. We still don't know yet how you can be discovered through that experience. What do you need to do to boost your brand's presence in those results? We don't know that yet. What we do know by just generic usage of ChatGPT, not only will they use the information that's available to them through web searches of your website, it's also sourcing a whole bunch of different information.
I'll give you another example, Lilly. Imagine if you are searching for a house and you go to ChatGPT and say, "I want a three-bedroom house in specific suburb area." They will then be able to find, based on the websites, a whole bunch of different houses that might be for sale based on web property information that's out there. Then you can also say, "Oh, I don't want to be in a flood zone and I want to be close to schools, or I want to be close to good coffee shots."
It will then go to another level of searching across flood data, across schools, ranking data off maybe Yelp results for good coffee shops. It will consolidate that information together and then show you the properties that meet those requests that's available today. That's available today without anyone participating in that value exchange or the ecosystem. There is a little bit around be careful what's out there about you because everything will be surfaced on the same level. There is a sense that brands are losing that control of the marketing messaging because we are pulling together external review searches with curated content.
**Lilly:** There's also the enduring issue with hallucination as well, which is something that a lot of effort and energy has been poured into, but which is going to continue to occur regardless because it is a property of how large language models function. Even if you are returning search results, one, you don't really have that much control over the context.
It's also been a problem in cases of traditional online advertising where certain businesses have directed companies such as Meta and Google, and so on, who are advertising providers, to make sure that their ads don't appear on Facebook pages for things they consider to be objectionable or in certain contexts. That vice versa, their websites, if they have advertising space, are not going to be showing ads for things that they find objectionable or for competitor brands and that kind of thing. Those contexts are always a bit of a mishmash.
Also, there have been at time of speaking a couple of different types of lawsuits around the world because of people who have had incorrect information about them surface. Not because it was written online anyway, but because came out of that latent space and is put in front of a user. While that is improving, that is still a part of the risk. The other part of it is also how to make sure that the information that you actually do have is returning in the way that it should and that it is part of the conversation if you want it to be.
**Sarah:** That is why I'm actually quite interested in this app's version in ChatGPT. It is no longer the LLMs who have sourced information off the open web, surfacing up what is most likely to be the right results. Once a specific brand like organizations MCP is being used, then that organization has much more control all over that information flow. I think to counterbalance the hallucinations, we're going to start to see brand trust coming back.
If you do create your own app and it's the thing that's gets surfaced, having your brand design elements within that UI, within that results that you search I think we'll offer that sense of trust and such to build that trust, and the results that are coming back are from an authored and curated owner. Again, we're in speculation land right now, but I am very interested and curious to see whether that apps model actually helps with people's trust of the data that comes out and then distrust of other data that it gets surfaced.
**Lilly:** What do you see as the first cab off the rank, so to speak, for things that people could be experimenting with, knowing that this is really experimental, that the established kind of SEO ecosystem is definitely undergoing a change, but that you can't afford not to participate in it if you want to be found, and that this is going to require experimental effort? As you mentioned earlier, if you're not experimenting with it now, then you are also not picking up on advantages in terms of figuring out how it could work.
Where should people begin if they're looking at this, and whether that is a big business or a small business. I noticed that part of the marketplace integration included, I think, Etsy, which meant that people who were small businesses operating with Etsy could also use this if they wanted to.
It's a different discussion there about arts and creativity, but as a discussion about how people find your business, that's always been part of the discussion, is how do you surface yourself in search results, which requires participating in some kind of exchange in this way? I want to be clear that I'm limiting my discussion to that, not to the content of the artistic stuff, which is a topic for a different conversation. What can you do? Big businesses, small businesses? What's worth experimenting with in your view?
**Sarah:** My bet is being placed right now on B2C as the first cab of the rank. We already seeing it with Shopify. If you have Shopify as part of your storefront, then you'll have the option to participate. It looks quite seamlessly. That's good news for Shopify fronts. I think it's really in that B2C. Retail and travel are the two likely candidates that I see as really good cabs off the rank. The reason is I'm seeing in customer data a lot of people turning to the likes of ChatGPT to help them doing the research planning phases of that.
I'll give you an example, Lilly. I was looking to book a holiday for my family, and I thought to myself, "Let me see how far I can push the envelope on this." I was able to get it to give me a very good itinerary for Tasmania for a family of five between certain dates, taking into consideration things that we wanted to do, things that we wanted to see, and recommended hotels to go for, and also the flights to have.
Just through conversation, I was able to build up a very good itinerary in a short amount of time. Things that would've taken me a long time of Googling or YouTube videos or just putting together the itinerary. The one thing that I wasn't able to do in that experience was book the hotels, book the flights. By the time my inertia got into gear and I went to book it, they'd sold out. The accommodation wasn't available, so I had to pivot. It brings me back to intent-based and what intent-based really means.
I don't think anyone really wants to book a flight, in reality, but we want to go on holiday, and we want to have great experiences, or I want to go to a meeting at 10:00 AM on Pitt Street. The intent-based is looking beyond the customer's interaction with an organization or with a brand to say what part of that job to be done is being serviced through that organization, is to look at that holistic picture and then stitching together all of the different components seamlessly for that customer so that they can not only book that holiday, they have that experience. They can have it.
The itinerary built up the experiences, the activities created the hotels that accommodate a family of five and the flights, and have the administration side handled through that agentic commerce experience. We move from you booking a flight, and then you booking a hotel, and then you booking an experience to you booking a holiday or you booking a business meeting that you have to go to. You get your taxi, you get your Uber, you get your flight times figured out for you and the waiting time included in the whole itinerary.
**Lilly:** I think this presents a really interesting challenge because, on the one hand, you're talking about things that are quite transactional, very straightforward, because you've got a specific goal that you're aiming toward. There are a lot of different reasons people might be looking for information about a product, and some of it is just research, and some people really enjoy doing research, or it depends about what. That is also occasionally part of the process.
It also means that the folks providing this information need to be really clear about what it is. I think flights are a pretty decent example because we have third party flight aggregators, and we have had for quite some time. Airlines are fairly used to publishing information about flights, and that sort of data is already structured and quite clear. That's not necessarily the case for something like an insurance policy, or like a bank account type policy in all cases.
There are also a lot of cases where things are put into the fine print and never really surfaced but do tend to be relevant, and that has been contentious over time. An interface like this requires of a business that you make it really clear what you're about so that people can make effective comparisons. I'm wondering what things people might need if they are looking at how a business might participate in this, what a business would need to make discoverable that is not yet discoverable in these ways to handle these kinds of use cases that's not already this, we have an existing structured API?
**Sarah:** Just taking their existing APIs and trying to create MCP services. I still think there's a significant amount of heavy lifting that's still to be done before we prepare to the next stage of conversations that is just waiting once that first unlock happens. Our APIs think in black and white. They have the data, or they don't have the data. There's mandatory fields that need to be filled in, and from a booking experience, you have to have a destination, you have to have a departure city, you have to have a date to search up, and you need to know the number of people that you're searching for.
We've hardwired into API mandatory fields that are no longer mandatory when you start having a conversation. There is still, I think, a significant amount of rethink that we need to do from an architectural perspective to get our APIs ready to handle conversations. Building up intent. What does fuzzy logic look like in them? How do we have different endpoints surface different amount of data? Maybe when I'm searching for flights from New York to San Francisco, I don't care initially about the price of it.
Maybe I'm just actually looking to see if the flight times are any way shape satisfactory. Is it a decent option to take a flight? Is it crazy morning, crazy night, or is it a good middle of the day flight? A lot of the data that we have is assuming that what you're looking for, ultimately, is the price of that flight. I think we've got to do a bit of work to rethink and reshape some of the APIs that we have that expose the data because we want to just build this up.
The second part is something that I'm thinking about right now, which is how isolated should we have this as data? If we're creating an external MCP that can participate in either Google or OpenAI's ecosystem or any other frontiers models ecosystem that they're developing, how much access do we want to the rest of our systems? How much do we want to give? Do we need to create an isolated air-gapped environment that that MCP has data replicas for?
For which case, we minimize that harm. We isolate it, we can update the data as we need, but we really minimize the harm that it could do to the rest of our system because we've almost air-gapped that experience. I think APIs need to evolve. We need to rethink about what our architecture patterns look like, and how they fit in with the wider ecosystem, and what those design patterns look like as well. There are three elements that are still emerging that we need to rethink about.
**Lilly:** I have mixed feelings about how MCP works at the moment as a protocol, as somebody who works in cybersecurity, because there are quite a few things that come along with any emerging protocol that just take time to get hammered out. We've repeated this pattern over and over with a lot of different technologies over the last few decades. I think that some of this is early issues with the technology that's not quite yet mature, particularly when it comes to the issues of trust that you were talking about, and where we can do most of the least harm, like information discovery is one thing, and making sure we have access to that straight away.
Read-only actions tend to be less of a concern, provided that the source you're allowed to read is the source that you're allowed to read. Also, I am cautiously optimistic about the intent-based part of what you're talking about and the way that relates to MCP, because I feel that with APIs and other kinds of interfaces that are better at describing what they are and what they do to a variety of different users, both machine interfaces, which APIs are predominantly built for, but also for human users and that conversational-based stuff to handle the nuances of a natural language human conversation, which is tricky enough for humans to do a lot of the time.
Machines with rule-based things are very different. I do feel that MCP is in some ways getting us a bit closer to the kind of semantic web that Tim Berners-Lee and folks were thinking about when they were describing web ontologies in the early 2000s, in a way that I think we haven't seen realized before, because SEO sort of took its place in terms of information discovery. My hope is that, at least with the way that MCP is going, because it is intended to be this kind of semantic discovery in a way, that it will enable more natural types of things.
We're talking in the context here about business-related discovery, but in order to surface anything based on user intent, you need to think broader than just the transactional part of this. You need to think about the problem someone's trying to solve, which good UI and good UX has always done, but which is really doing it in a very natural language kind of way. That's the part where I feel hopeful that this is a technology with the potential to do some really decent things for being able to find things online, ultimately, and as it matures.
I wonder, from your point of view, what are the side benefits you're seeing or you would anticipate, I suppose, with this hypothetical that we're talking about? If it continues down this path, more businesses are trying this kind of age of intent-based discovery stuff. What advantages do you see that that could have for the ecosystem in general in terms of the way that we share information with each other?
**Sarah:** Up till now, our marketplaces have been very much one-sided. There's a very strong player in that value exchange who owns and controls the share, and we haven't really led to that world of true ecosystem where everyone is a participant, and you get value from it, and you add value to that ecosystem. If I think about taking a step back and organisations no longer owning and controlling that digital front door, that digital front door experience is happening within that intent interface, which is a version, I think, of the super apps on mobile phones, that multiple things that you do underneath it.
Grab is an example, and Uber with lots of the different things that you can do. I think it's an interesting world and it's tied to research around customer, customer loyalty, customer personalisation, and what customers are expecting of how they interact with their purchases.
**Lilly:** That makes sense. I feel like we've been pretty clear with the conversation that we've had to this point that a lot of this is really experimental. We're talking about projected hypothetical futures that may or may not come to pass, but that in this current moment. There are things in here that are worth experimenting with if you want to get a sense of what you might need to adapt and change as a business moving into what might be happening next. Where do you see the most important actions that businesses can take about how they experiment right now?
**Sarah:** I am having lots of conversations with a bunch of clients about what experimentation might look like for them and they might get from it. In my perspective, I'm seeing a couple of different things coming out. The first one is that by experimenting, they're actually staying on the forefront of what is happening. They can talk with firsthand experience as to what this is doing, what shape this is taking.
Secondly, even if they're experimenting not to create yet another failed prototype or POC that never lands into production, I'd actually urge clients to experiment not with the purpose of taking something production, but the experiment to learn. There is a couple of different things that they can learn about. I'd like them to get them to consider how to experiment with a very strong focus on the engineering skills that we've learned to date.
What I mean by that is it's very easy for them to create an MCP prototype using the apps SDK. I did it within the course of a day, but what I uncovered was what we might need to do from a data side and from the MCP down into our layers, down into our stacks, and really uncover and unearth what the APIs might look like, what the data might need to look like, what some of these architectural concerns that we might need to have, and create a plan for how we are going to incorporate that into our existing technology roadmaps.
At the same time as we are really, really starting to have new design emerge and conversational experiences emerge. By starting to think about what are different interactions and interaction patterns that customers might have with us, and I think there's going to be an evolution here. Once you start doing version one of your prototype and your experiment, that seems to lead to aha moments that get to the next level of conversation.
You start building out a set of patterns and thinking about the way that a human might interact with this new experience in a slightly different way. By having that hands-on prototype, you can actually start to put it into our hands to think about and to run those thought experiments. The experimentation not to build something in production, the experimentation to learn and think differently and be curious gives us valuable insights as to what we might need to do next in our roadmaps for our product, for our customer, and for our technology.
**Lilly:** We've spoken a lot about what the customer gets out of an interaction like this. It's intent-driven. What does a business get out of this same exchange apart from making sure that the business ends up in front of the customer as one of the options?
**Sarah:** That's a great question. I actually think these details are still fuzzy, and they're emerging. We can start experimenting and playing around with what that customer experience and the conversation and the intent-based will look like. What's still to be revealed is the value exchange in participating in this ecosystem. Marketplaces that have gone before, we can suspect it'll be very lucrative for you to join as one of the first players in this ecosystem.
Over time, that value will shift back. As we are looking to think about participating, we also need to be thinking about what's the value that we need to hold onto and retain. What do we give away as part of that participation, and what do we keep? Now, from where I stand at the moment, even within that value exchange question, having your great answer right now or still to be revealed, I think that there is something around market share. I don't necessarily see that this is going to exclude or mean that you take away a particular channel.
I think this is an extension on your channels that you have to look after. As a CTO, one of the things that I'm concerned about is every new channel experience that we maintain and that we support, costs us money. It costs us because even if we have a fantastic platform underneath, we still have a component that is very specific for the channel, and we've got to make sure that all of our channels are returning the right data and ideally have an omnichannel experience.
The thing that I've seen most organizations getting the value out of that omnichannel experience is where they combine it with a business capability platform. Where they start to think about their organization in terms of capabilities, that contain all of the business logic, the business data, the business rule sets, and the integration that you need, and then just expose that as a capability for your digital channels to consume, or your internal UIs to consume.
I think that there is a way that we can minimize the technology investment by rethinking about how we've architected our platforms themselves. What I'm seeing at the moment from organization is that this might actually be another channel that we have to support where at least initially, the revenue isn't flowing directly to counterbalance the investment. Even if it does, it probably just spreads the wallet share across all the channels rather than necessarily having a completely separate and new revenue stream.
I think it's a really great question for businesses to ask, "What's in it for me and what value do I get out of it beyond just customer acquisition and retention?" Although customer acquisition and retention is an important revenue strategy. I think it's a good moment to start thinking about, is this an investment that we're willing to have as one of the loss leaders as long as that can he help increase our market share overall?
**Lilly:** The biggest thing that I took away from reading this series overall was that this isn't really about making another chatbot. This is about making a way for your business to be found in the ecosystem that's emerging. It could look like a chatbot, there could be chatbot-based expressions of that, but that this is not necessarily put a chatbot on the front page of the website and we're done, it's good. My hope is that for anyone listening or anyone who's gone to read these pieces, that if you are deciding to experiment, that you're looking beyond just the chatbot paradigm and talking more about the actual user experience, the user interface.
It brings it back, in my view, to a really core user experience question, and to draw on that user experience expertise that you hopefully have in the organization and that exists in bucketfuls out there, to really understand what users want, do that research, and spend that time looking at it, because I think that however it gets expressed, this is the type of future that we could be unlocking with intent-based interfaces. That's my hope and what I took away from it all. In putting it all together, Sarah, what was the main thing that stood out to you and what are you hoping to carry forth into the work that you're doing next?
**Sarah:** The main thing I think is that we're standing at the point of large change where we're at that cusp, we've been at cusp for a while, and there is, I think, a significant moment that's about to happen in the way that customers interact with us as organization, with brands, customers expectations about what to expect, and how we can respond in a way rapidly that keeps on innovating, keeps on reinventing ourselves so that we can continue to add value to that customer experience.
**Lilly:** Sarah Taraporewalla, thank you so much for coming to talk to us about the age of intent, about your article series on Thoughtworks insights, and about what you learned through putting it all together. If you enjoyed this episode, please help us spread the word about the podcast. Give us a rating, thumbs up, whatever it is on iTunes, wherever you get your podcasts, and you can always get more conversations like this on thoughtworks.com/podcast. Sarah, thank you so much for joining me today.
**Sarah:** Thank you for having me on, Lilly.
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
## Explore a snapshot of today's tech landscape
[ Read Technology Radar ](https://www.thoughtworks.com/radar)