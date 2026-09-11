<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/data-driven-with-data-mesh | Title: Data-Driven with Data Mesh | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Data-Driven with Data Mesh 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Tania Salarvand | Podcast guest  Zhamak Dehghani, Director of Emerging Technologies, NA
May 13, 2021 | 36 min 31 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/data-driven-with-data-mesh#transcript)
Listen on these platforms
## Brief summary
Modern companies have audacious goals and initiatives to become data-driven, but many still suffer a data disconnect. Despite increased investment, expanded commitment and more tools at their disposal, how can companies translate gathering tons of data into becoming a data-driven business? In this episode, Zhamak Dehghani, Director of Emerging Technologies, North America explains how Data Mesh brings people closer to data and insights.
_Learn more about the topic in Perspectives:_[_Data strategies to drive business value at scale_](https://www.thoughtworks.com/perspectives/edition15-data-strategies-article)
**Highlights**
  * Companies with a rich ecosystem can't operate on “gut-driven” insights so you have to be “data driven.” This involves a spectrum of solutions, from traditional reporting to machine learning, fueled by reliable, high-quality data that is gathered from every touch point within the ecosystem of your organization.
  * Turning data into actionable intelligence: It's not about how many megabytes of data you have stored that nobody understands. But, what percentage of the domains in your business are providing data in a meaningful, usable, trustworthy way for the rest of the organization to tap into.
  * Organizationally and technology-wise, there is a gap where business happens, and real actions happen – and where goals get formed. Bring the data closer to the source and closer to the people who understand it, and then empower those business units with data capabilities so they can easily access and share their data with the rest of the organization.
  * When your business goes from a single function and into multidimensional - the failure modes are typically around scale, and having access to diverse data sets with quality and reliability.
  * In the "next pandemic phase" model - change is eminent and it's continuous. You will need to have data to have your finger on the pulse of your business. 
  * Successful transformation journeys require a top-down vision to mobilize people. And then bottom up support and ownership; new roles to be defined. 
  * Data Mesh as an approach: If you are experiencing pain points around the scale, or you have bottlenecks, and you're thinking about breaking this monolith down – you may need to commit to a decentralized mode of operating around data.


**Podcast Transcript**
**Tania Salarvand**
Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. Today's modern digital businesses have created audacious goals around data, to collect it, manage it, access it, visualize it, all to drive decisions. Yet, despite expanded commitments and investments, there's still a gap in measurable business outcomes from data. In fact, a recent report shows that over 50% of big companies are spending more than $50 million on data and AI, yet only 30% have a well-developed data strategy. Why are corporations still suffering from this disconnect?
I'm Tania Salarvand and I'm here today with Zhamak Dehghani, Director of an Emerging Technologies North America, to help answer the questions for executives. How to think about data to become a data-driven organization. Welcome, Zhamak, nice to have you.
**Zhamak Dehghani (**[00:57](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=57.27)**):**
Hi, Tania. It's wonderful to be here talking to you about everything data.
**Tania Salarvand (**[01:01](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=61.94)**):**
So many are probably going to recognize your name for coining the popular term, Data Mesh. But before we get into that specifically, can you tell us a little bit about yourself, your role as Director of Emerging Technologies and what that means?
**Zhamak Dehghani (**[01:14](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=74.76)**):**
Sure. So I'm a technologist at heart, I'm a problem solver, and look for corners of our industry that is prime for innovation. And that's essentially this job is. Thoughtworks has a wonderful vantage points working with many companies globally, solving difficult, hairy problems. So we can see what are the challenges that organizations still have and still face today. What are the technological solutions that exist today, and what's the gap between that? What is missing and where we can still innovate, where we can push the boundaries of how we imagine our solutions forward. And my job is identifying those opportunities and encouraging innovators within Thoughtworks in our other core systems with our clients to come up with the next big technologies, and Data Mesh was a brain child of basically applying this discipline.
**Tania Salarvand** ([02:17](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=137.8)):
So how would you actually define a company that wants to be data-driven? We hear this all the time, "We are data-driven." Sometimes true, sometimes not, or, "We have an ambition to be data-driven." What does that look like for an organization, but also an end user?
**Zhamak Dehghani**([02:34](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=154.17)):
Yeah, that's a fantastic question. I think maybe we can say what it's not to be data-driven, like you're gut driven, you're intuition driven, and that's maybe okay when the landscape and the complexity of organization is rather simple. As a person, as a human being, you have a good understanding of all the signals that, through the interaction with your clients, your company is generating, it can understand the customer. But we've passed that world now quite a bit. Now, for decades, our organizations becoming more skilled, they're not single operational, they operate in many different domains, they have a rich ecosystem of partners, B2B, B2C offerings. So we can't be gut driven, so we have to be data driven.
And what does that mean? That means different things for different organizations. But one lens we can apply is that you try to embed intelligence and machine intelligence into every decision, every touch point with your customers, every service and product that you provide so you can improve those decisions, and streamline your operation, and improve the experience of your customers with now a new found point of view, a new intelligence that the machine is telling you about the data that goes beyond just your intuition and what your gut tells you.
What does that look like? That means, well, applying a range of technologies in terms of training, machine learning, models that can make predictions, or they can look at your customers and identify patterns, apply machine learning to understand what the customer is actually telling you, the sentiment of conversations that you have from your customers. And traditionally, we've always had reports, and dashboards, and metrics to look retrospectively at different KPIs and different, I guess, performance measurements that we have in our business. So it's a spectrum of solutions from traditional reporting to more modern machine learning that is fueled by reliable high quality data that is gathered from every single touch point and every single interaction within the ecosystem of your organization.
**Tania Salarvand** ([04:57](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=297.88)):
And that just drives me to think, how do you then measure how a company, their goals or performance around data, how do you measure what good looks like? And then how do you then turn that into something actionable? You talked about intelligence being embedded and built into everything that you do, how do you turn that data into actionable intelligence?
**Zhamak Dehghani** ([05:17](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=317.25)):
Yeah, that's a really good question. And I think there will be a set of complimentary measures and metrics. When we think about metrics and when you try to be metric driven, usually you look at your early indicators, "What are the activities that I can do so that I can move towards this intelligent driven, data driven operation of my business?" And then the lagging indicator is, "What are the outcomes I'm actually now getting, and I'm measuring, applying those activities?"
So you have this range from activity oriented measures to outcome oriented measures. So we can talk about all those classes of measures that you can put in place, but I would say you can start with thinking about those audacious goals that you have. I love the phrase that you use at the beginning of this, is audacious goals, because they are truly audacious and think about, "Okay, what functions of my business are being optimized, are being streamlined? What offerings to my clients are actually driven by the data that indicates what they want and the experience that they're having?" And let's think about those functions and see which one of those and how many of those, what's the coverage of those functions that has some sort of machine intelligence augmenting what we're doing manually with our people.
So, as an example, we have this great healthcare provider and payer client in North America, and they have this, again, audacious goal that every year they improve 20% of their touch points with their members using the data that they have with them, and with some sort of a machine intelligence. As an example, they want to move to where it's a care system that, by understanding the unique needs of every member, they can provide it specialized, personalized care team for that member. So you can just imagine how many of services that need to be now augmented with machine learning to segment those patients, to understand their needs, to do pattern matching of what are the care team capabilities need to be?
So as a starting point, you can work backwards from those audacious goals, and then see the coverage of having machine learning, and intelligence, and insights embedded into every function, and then work backward to see, "Okay, if I have these goals, what's the state of data that needs to actually feed this machine learning?" So without it, it doesn't matter how many of these audacious goals we have, if we can't train the machine learning with reliable data, we're stuck on the first step.
So then the measurement around that, which is something Data Mesh introduces, is that the coverage of accessibility of data as a product. So it's not about how many megabytes of data you have stored on this that nobody understands and can use. But what coverage of what percentage of your domains in your business are providing analytical data, historical data, in a meaningful, usable, trustworthy way to the rest of the organization to tap into that? What's that network of these data nodes on your mesh look like, and what's the coverage of that? So I think we can just then start working backwards and say, "Okay, how do I measure? I have data products." And this is just, turns it all the way down to finding a good set of complimentary measures to be data driven.
**Tania Salarvand (**[08:51](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=531.29)**):**
That brings up a thought in my head around how there's a big gap between what business leaders think they know and want because I think there was another recent report in Harvard Business Review that said 80% of business leaders do believe that data and analytics investments are important and that they should be making them, probably are making them. However, less than a quarter actually effectively measure and report on those business values. So they want them, they're investing in them, they don't know exactly what they're doing with them, or how they're achieving any kind of value outcomes.
So you mentioned how important that is from an analytics and analytics management perspective, but based on the experience you've had and the clients that you've been working with, how would you, or what would you contribute to that gap between what the business leaders know that they need to make those decisions, where they're investing their funds and money to do so, and then how adequate that data is, and what they're actually getting?
**Zhamak Dehghani (**[09:48](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=588.84)**):**
Yeah, well, you've got to close that gap. Right now, organizationally and technology-wise, there is a huge gap where business happens, and real actions happens, real interactions with the customers and those goals get formed and dreamed of. And there was a big gap between the responsibility of data, ownership of the data, and there is centralized, often a data team, and this diverse set of business units that making decisions and require that data.
So one way to bridge that gap, in fact, is to bring those two elements together. I mean, if you look at the evolution of digital businesses over the past decades, we have moved away from this centralized, monolithic IT to more distributed microservices, technology aligned with business goals and business domains. And we have to continue that evolution to data and accessibility, to analytical data as well. Bring the data closer to the source and closer to the people who understand it, and then empower those people, those business units, with data capabilities so that they can easily access and share their data with the rest of the organization, give that data responsibility to them and then empower them with your data platform technologies.
And with that, now the knowledge around the data, people who really need it and want to use it are the closest to people who would be creating it and sharing it. And I think that's one way to start bridging that gap. I mean, there are other issues around data literacy and people will be kind of aware, but I think we need to bring data to people who most intimately understand it and understand how to use it and kind of break apart that monolithic data view of the world and empower those teams.
**Tania Salarvand (**[11:54](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=714.36)**):**
I think you're right, making a commitment to being data-driven and data-driven transformation and decisions is one thing, but executing on that and having the right variables in place, whether it's people, resources, capability, it's a whole nother thing. Which leads me to something that you say quite often in a lot of the talks that you give around the inconvenient truth around data and corporate data agendas. Can you tell us a little bit about what that is, what you mean by that, and how that drives, or in some cases inhibits, executives from getting to that ideal state?
**Zhamak Dehghani (**[12:24](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=744.8)**):**
Yeah, I think the inconvenient truth points to the metrics that you mentioned, that despite the accelerated pace and amount of investment in big data and AI, the executives are reporting failure on transformational metrics. "Have my cultural and technology changed to be data-driven? Has my business changed to compete using data?"
So those transformational metrics still remain to be satisfied. And then if we scratch the surface, and I'm a technologist, so I would scratch the part of the surface that points at the technology and architecture sitting under it. When we scratched that surface, we will find out this great divide that exists between where the business runs, and the systems that are supporting that business, and where the data sits, and the responsibility of curating, and cleansing, and getting that data already in a way that perhaps you can use it.
And that great divide has been created with technologies that centered around monolithic and centralization of the data, they build so that we can have the data in one place. And that has led to this kind of centralized teams that are disconnected from the business, they really don't understand. It's very hard to understand it, the business is constantly moving, how to deal with the data and even cleanse it, and what's the need for it. They're disconnected from the actual domains.
So underneath that inconvenient truth of failed measures sits a great divide of data with really fragile architectures that don't lend themselves to a modern world that we're constantly changing, we're constantly finding new use cases, we're constantly finding new sources of the data, and we need to kind of close that gap.
**Tania Salarvand (**[14:19](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=859.11)**):**
And speaking of closing the gap, what are some of the things that I know you've talked about and definitely done a lot of deep dives on in terms of the observations of those failure modes, what are those failure modes that you've seen, and what are some thoughts you have on getting past those?
**Zhamak Dehghani (**[14:35](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=875.41)**):**
Yeah. The signals that we see, the symptoms that we see really evolve, I think, at core around the scale. The moment your business goes from a single function and turns into a large operation, you're in retail, you're in healthcare, you're a provider, I mean today's businesses are very multi-domain, multidimensional.
So the moment you start having that scale, and the moment you have an innovation agenda that requires now embedding intelligence in every single function of that business, multidimensional business, you have a bottleneck. Sitting in the middle, you have a data lake, or a data warehouse, or multiple of them sitting in the middle. So the failure modes are really around scale of having access to diverse set of data sets with quality, with reliability, no matter where those data sets come from in the business. And also being able to satisfy an ever growing list of use cases and business needs that require access to that data.
The growth and scale of the two pressure points of users, number of users, the number of use cases, the number of business needs as well as the number of sources are what we are seeing as the main failure modes. And then the answer to those often is, "Well, our data platform doesn't work so we have to move to our next generation data platform. We had Hadoop, now we go into cloud, we had data warehouse, now we have data lake, now we have lake house." Or whatever the next big tech is. And then you find yourself in this ever moving cycle of the investment for the next one, and the next one, and chasing these goalposts of having the answer.
And ultimately, instead of investing in really competing using data and getting value, you're just investing on bootstrapping yourself to get there. And those were the symptoms that we saw that led us to really question why, what are the underlying assumptions that we haven't challenged for half a century? And we started kind of challenging those assumptions and arrived at a different architecture, different organizational structure that we call Data Mesh.
**Tania Salarvand (**[16:52](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1012.16)**):**
And so I imagine a lot of what you just mentioned really can drive a business case for Data Mesh within an organization, and all the things around silos, scale, lack of integration or understanding of what it is that they're trying to look for. What is your thoughts, or opinion, or observations around how Data Mesh can push executives to imagine data very differently, and then mobilize their entire organization to get on board with this as a concept?
**Zhamak Dehghani (**[17:18](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1038.83)**):**
Yeah. I mean, the executives care about the outcomes that they get, the bottom line that this new paradigm that would give them. I think it requires the same shift in thinking and approach that we saw from monolithic big applications and big single solutions to microservices. And executives who have gone through that journey in their career, they have seen that they can really create agility and scale, if done right, with that sort of distribution of ownership. So they can now apply the same learnings to data and analytics and say, "Okay, how can I remove these bottlenecks that I have today?"
So I think where they can get started is with kind of connecting the dots between the goals that they have, the pain points they feel today, and how a decentralized distributed model that mirrors their business today can get them kind of bridge the gap and get closer to those outcomes.
**Tania Salarvand (**[18:31](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1111.78)**):**
And along those lines, what are the factors that have made the case for getting a handle on data and data policies, even more urgent today? We're talking about a "next pandemic phase" model, we're talking about cloud and the urgency of getting to cloud, we're talking about digital transformation and why everyone's jumping on it. What is that driver? How has that driven the urgency around data?
**Zhamak Dehghani (**[18:57](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1137)**):**
I think one thing that was evident with pandemic was respond to change. A changing landscape, a shifting landscape that none of us expected, and suddenly we went through this world that services were manual required people in intervention, and moving around, and socializing, and all of those things that our business was built around, and move to a very different world, almost a digital only world for within a very short span of time.
So if you take that as a lesson, that change is eminent and it's continuous, and the moment we think we have a handle of how the world works, something would get thrown in whether it's a competitor, or a new comer in the business that would disrupt our goals and strategy, we have to respond fast. That's when you need to have data and have your finger on the pulse of your business and your changing landscape within which your business operates.
So I think the continuous change and unpredictability of the future, and moving to this model that nothing is constant, and I have to have a probabilistic view of the world, like the world is not a black or white binary, it's a probability of all of these scenarios that might happen, then, as an executive, you really need to have those real time intelligence. I mean, simple, simple example, one of our clients who, as a retailer. They had their quarterly or monthly kind of reports and dashboards. And when COVID happened, they need a real time understanding of which neighborhood they could next open their stores, or which ones they have to immediately close, and what was the response on the website, how things were changing, what products people were ordering? This near real time view of the world that really changed the way they had to think about their infrastructure. So I think that's the main driver, the change, the response to change, agility of... Reconfiguration of your business, if it's needed, and really have an understanding of what's really going on.
**Tania Salarvand (**[21:13](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1273.94)**):**
It's probably fair to say that data has always been critical to running a business and/or making smart decisions. However, what I'm hearing from you is that now more than ever it's real time, almost two seconds before it happens, and that ability to have access to it, but more than just access, knowing what it means, what the insights are, and what to do with it is something that's creating even more urgency today than it probably has ever before.
So obviously there's something there around flexibility, there's also something there around, outside of the tech, the organization itself, the culture, the way that you think about this, the way that you behave, the mindset. Can you talk a little bit about what organizations need to either do differently, behave differently in order to really get into this culture and DNA about embracing data differently?
**Zhamak Dehghani (**[22:01](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1321.5)**):**
Absolutely. I can point to one or two things that I have seen in transformation journeys. However, this is a, I think, white space for innovation as well around the organizational change to become data-driven. What I see with successful transformation. So first and foremost, we need a top-down vision and support from the top, from the CEO, that we are going to be data-driven, whatever that means for your organization, to really mobilize people.
And then bottom up, we need the support. If the CEO says, "We are going to be data-driven and we're going to change every function of the business and introduce a new service or a product with ML." It's not going to go anywhere if the teams are still struggling to get access to data, still struggling to easily build those... Train those machine learning models, deploy them, monitor them. So the bottom up support is the right foundation and infrastructure to enable those teams.
And then the ownership, I think we need new roles to be defined. So Data Mesh introduces a few new roles. One of them is data product owner. This shift of perspective, shift of language and mindset that data is not an asset that we're going to hoard and collect and value. In fact, data is a product that is useful only when it's used and delight at the experience of the consumer of that data. So then if data is a product, you need people whose responsibility is maintaining and serving that product.
So data product owners, data product developers, I think we need to, again, move away from this centralized, a specialization of data engineers, around the tooling, and by elevation of new platforms and abstraction of complexity, create a new generation of data people that don't need to have super specialized skills because the platform gives them generic tools that they need so that they can produce this data products, they can produce or engineer a machine learning model, but they don't necessarily need to be the scientist who defines the mathematical model behind it. So data science in a box, as a product that other general engineers can use it.
So I think we need to both have those top-down supports, new roles in the organizations, definitely those ambitious data-driven initiatives to mobilize people, and enablement by kind of the platform teams and roles within the platform teams to really look at their platform also as a product that delights the experience of these domains that need to find a data, and use the data, and create solutions on top of it.
**Tania Salarvand (**[25:11](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1511.69)**):**
That's wonderful. Thank you. Yes. It's clearly the hardest part of any transformation is the people side and getting people to change the way that they think, or how they approach a problem. So I can imagine that that's more difficult in some instances than the technology. But speaking about the technology specifically, as you think about Data Mesh as an approach or a way of thinking about how to really solve for some of the data issues, what are the things that you've seen work in an environment where Data Mesh has been the right solution, and are there times where maybe that's not the right solution so don't waste your time on this, focus on something else? How would you kind of navigate or help someone navigate that answer?
**Zhamak Dehghani (**[25:52](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1552.67)**):**
Yeah, we can look at it from multiple dimensions. One is Data Mesh is a new approach. The technology and tools we have today are powerful tools, but they've been at heart designed for pretty much a centralized model, and to change them and reconfigure them so that they can be used in a mesh model, in a distributed model, requires quite a bit of an engineering commitment.
So if you think about an adoption of a new innovation adoption curve, you usually have your innovator adopters that just go riding, head in and take the risk and commit the engineering kind of capacity that is needed. And then you have lead adopters and laggers and so on. So if your organization is not a take out core organization, you just want to buy things and plug them in, perhaps we're not yet there.
And then the other dimension we can look at it is that how big and complex and rich the domains within your business are. If your business is still quite small or focuses on single function, and one team is managing your data and your getting value out of it, well, maybe you don't need Data Mesh, Data Mesh will sound like a whole lot of over-engineering to use. But if you are experiencing those pain points that we mentioned earlier around the scale, and you have those bottlenecks, and you're thinking about, "I need to break this monolith somehow down so I can paralyze work and move faster." Then Data Mesh is perhaps suitable for you to kind of have a look and say, "Okay, now I've reached a level of complexity and scale that I need to commit to a decentralized mode of operating around data."
**Tania Salarvand (**[27:54](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1674.9)**):**
And as you mentioned, this is essentially new, but new because there's some things that you've learned from previous experiences that haven't worked from what we used to have, and then how do we kind of converge or evolve that into something that works for today? And I'm sure it will continuously evolve.
But I'd love to hear from you, what are some of the emerging technologies in the data space that you're starting to see, or you're starting to hear about that you think is important to keep an eye on, or is there an area that you think is really going to start peaking soon, and those that are in this space should start to investigate a little bit earlier?
**Zhamak Dehghani (**[28:28](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1708.96)**):**
Yes. I think one of the areas that I would kind of pay close attention to is anything around automation and continuous delivery of data or a machine learning model because at core we need to really rely on a lot of things done in an automated fashion and streamline the experience of data product developers, or data product consumers who are building your reports and who are building your machine learning models.
So there are a lot of good technologies around automation and continuous delivery of that Also think about a new way of exposing data so we go back to the conversation around APIs again as a way of encapsulating complexity around data products, and then hiding that complexity and exposing that data through easily consumable APIs. But in new generation of APIs, a generation of APIs that allow you to run SQL queries, that allow you to Traverse files, allow you to consume large volume of data. So I think there was data APIs around your data products are important, and there are technologies that exist that can be configured that way.
And then on the surrounding of the mesh, I think, try to find new technologies that allow you to now look at this mesh. So tools around data discoverability and exploration of existing now newly created mesh to give you a window into the mesh. So there is technology around data cataloging that exists, but they need to morph and mutate to actually think about it in a distributed fashion or the centralized catalog. So I think that discoverability is... Tools around discoverability of the data become important.
These are some of the spaces. I think the rest of the utilities, how do we run our data processing jobs, or where do we store our data? I call those utility layer technologies that already exist, and whatever cloud provider your using, or on-prem solutions you're using, you probably have access to those utility technologies like the data processing, and orchestration, and storage, and access that you can use. The challenges that those technologies, again, need to be reconfigured in a distributed fashion and you can work closely with your providers to go to the next generation of existing technologies for a distributed configuration.
**Tania Salarvand (**[31:12](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1872.11)**):**
Thank you for sharing those thoughts and definitely things for folks to keep an eye on. But as we wrap up this conversation, we talked a lot about the intent versus reality, obviously, and the gap between that. How do we close that gap? How do we get people to start thinking, or organizations to start thinking about their data journey, what it means, what it doesn't mean? Some of those failure modes and points and how to kind of avoid them?
Just thinking through what's next, from your point of view, for companies who are at a point where they need to, it's urgent now, they need to reimagine their data philosophy, their strategy, their agenda, what it means to their organization. What are some of the things that you think they need to keep in mind today, some of the things that are happening today that they should just be apprised of, and also keep in mind as they start to embark on this journey?
**Zhamak Dehghani (**[32:00](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=1920.69)**):**
I mean, every journey starts with a destination and a vision. Even though that destination will keep changing. So I think even if you're starting today or you're somewhere on that journey today, I think there is a visioning exercise that needs to happen for you to reimagine the organization and get inspired what that future could look like, what are the products that you will be providing to your customers?
And we see that with our clients, that the beginning of a lot of our conversations is around, "This is our strategy in terms of the initiatives and that we want to enable using data." And then work backward to see what are the pieces we need to gradually unlock to reach that destination? What is the team structure that we need to start reconfiguring so if we are moving from a centralized governance team, or a centralized data team, what are the best domains, what are good to get started with, and started giving those domains autonomy?
And if you need to do that, what is the commitment to the underlying platform technologies to give them autonomy and empower them? And start really in an iterative fashion, attempt to unlock one use case at a time, one initiative at a time, but keeping that big picture, whether it's a Data Mesh, or it's something else, keep that big vision in mind as a target state, and use your business initiatives and use cases as an execution vehicle, and define your incentive models and fitness functions, or objective measures to guide your journey to know whether I'm actually moving towards that target state or I am I moving away? So define those objective measures also early on, just use that as a compass, as a guide, use your use cases as a vehicle for execution, and use that big picture, beautiful, ambitious kind of target state as a driver.
**Tania Salarvand (**[34:02](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=2042.29)**):**
Back to those audacious goals, which I think are important to have, but to your point, having the path to get there. And maybe one last thing, if I can ask, clearly the term data in itself is all encompassing, and depending on who you ask and what they need from it, it means something different, and obviously expectations are different. So I'd love to hear from you, are there one to two myths around data that you think are worth busting? What would those one or two things that just bubble up to the top that you think, "This is what happens every time." Or, "I hear this so much." That you think is important for our audience to know?
**Zhamak Dehghani (**[34:35](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=2075.88)**):**
I love this question, in fact. I think maybe there's also a slant in this question that what's the evolution of the term data, what it meant and what does it mean today? So by definition, it's pieces of facts. So people think about them as bits and bytes that are stored or they're streaming somewhere on their architecture. But I think the myths, some of the transformational thinking that needs to happen is that data is not the byproduct of running your business. I have any e-commerce system, the job of e-commerce system is selling convergence and selling wonderful products to my customers [inaudible 00:35:19] their needs. Of course, to run this function I need to have data in this database that keeps the current state, but I'm also generating all these touch points and events from the customer behavior as a by-product.
And then I will give that to somebody else to curate and cleanse and then turn it to a data is usable. So I think that notion needs to change. That e-commerce system should be exposing a form of its data that is consumable, understandable, usable, right there. So data is a product and not a byproduct. And I think once we move to these more that data is now more than just bits and bytes and facts, in fact, it has a heartbeat, it has a behavior, it has all of those affordances and capabilities around it that makes it usable, it has documentations, it has SLOs and guarantees of its quality, then we arrive at a new creature that never existed before. It's the data and the code and the policies around it that actually make it useful, make it alive.
It's like for decades and decades we separated the soul from the body, the code from the data. I think we would need to bring them back together and turn it into an alive lively data that is always trustworthy and is easy to find and discover. So I think that's the transformation that needs to happen. That data is not just this dead bits and bytes for somebody to come and discover it, and get the dust off it, and then clean it, and give it to someone down to track. And that's the evolution I'm personally going through in understanding what data in future looks like when we talk about data.
**Tania Salarvand (**[37:01](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=2221.97)**):**
Zhamak, thank you so much, every time I have a conversation with you, I feel like I walk away with so much, not to just think about, but also to research. So this has been very helpful for me, I really appreciate the time with you today.
**Zhamak Dehghani (**[37:12](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=2232.5)**):**
Thank you, Tania. Thank you for the conversation.
**Tania Salarvand (**[37:15](https://www.rev.com/transcript-editor/shared/ig1KqlmLscLTsSCEYn6Hu4lXx3hmbQIEJasPp-dxdmgLhClvWrUX9-iEIofqGEjfr1NpdXOjsYYe86Kle5Uxhk34og0?loadFrom=DocumentDeeplink&ts=2235.43)**):**
And thank you for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcasts. And if you enjoyed the show, please spread the word by rating us on your preferred podcast platform. Thank you.
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