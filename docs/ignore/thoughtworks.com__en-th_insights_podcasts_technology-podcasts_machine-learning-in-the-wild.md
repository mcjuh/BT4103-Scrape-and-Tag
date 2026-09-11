<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/machine-learning-in-the-wild | Title: Machine learning in the wild | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Data science and analytics ](https://www.thoughtworks.com/insights/topic/data-science-analytics)


Podcast host  Zhamak Dehghani and Mike Mason | Podcast guest  Max Pagels and Jarno Kartela
September 24, 2021 | 46 min 49 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/machine-learning-in-the-wild#transcript)
## Brief summary
From creating novel solutions for parking airplanes or identifying the winning formula for single malt whiskeys, our colleagues at Fourkind have extensive experience in building machine learning systems. Here, Max Pagels and Jarno Kartela highlight why deploying ML is different, how edge cases can confound well-trained models and the unexpected areas where ML can deliver better than human-levels of performance.
### **Full transcript**
**Zhamak Dehghani** : Hi, everyone. Welcome to another episode of Thoughtworks technology podcast. I'm Zhamak, one of your co-hosts, and I'm here with my co-host Mike. Hi Mike. 
**Mike Mason** : Hi, Zhamak. I'm Mike Mason who you might also know from other podcasts. I'm one of the regular hosts here.
**Zhamak** : We have a great episode for you. We are going to talk about deploying and running machine learning models in the wild. I'm really excited to talk to two of our colleagues, Max Pagels and Jarno Kartela from Finland. Max, would introduce yourself?
**Max Pagels** : Yes. Hi. Thanks for having me on. My name's Max Pagels. I'm currently the Head of Technology for a company called Fourkind which has offices in Helsinki in Amsterdam. Fourkind is a recent Thoughtworks acquisition. Now, I'm part of Thoughtworks working from the Helsinki office with all things machine learning and trying to figure out where technology might be in the future, and helping everyone in that area.
**Zhamak** : Thanks, Max. Jarno, would you say hi to the audience and introduce yourself?
**Jarno Kartela** : Yes. Hi, I'm Jarno. I'm a Principal Consultant at Fourkind and my day-to-day is trying to figure out how organizations could be more intelligent and how to apply data science and data to their day-to-day work.
**Zhamak** : Glad to have you both here. The reason we thought it's a good idea to get together for this podcast was a conversation we had in our last Technology Radar meetings. There was a conversation that why deploying machine learning model should be any different from deploying any other old microservices or executable or application. What are the differences in runtime configuration, runtime behavior, architecture that we should be aware of? Are there any? I guess just to start the conversation, can we think about machine learning models like any other old application that we deploy, or are there differences?
**Max** : I think there are several ways of looking at what machine learning is and what traditional software engineering is. One way to think about it is in traditional programming, you have some input, some data, you have some program that's written by a software engineer, and then you do some computation. Input comes in, the program does something and you get some end results. Whereas in machine learning, I think it's useful to think of the paradigm such that you have input data, then you have some results you want to achieve and you have data for that as well, and you use a learning algorithm to produce a program.
This is fundamentally different because you didn't write the program. It's a bit more of a black box to you. That's one thing. The rule set is completely automated effectively. It's not something you explicitly write. It's also inextricably linked to the data that's available. When you make a model and train it on some data and you produce a program, similar type of information needs to be available when you actually make a prediction and try to use this program, so that's a fundamental difference.
There are also, obviously, similarities. Just like any other piece of software, a machine learning model, any type of optimization model runs on a computer and therefore is a program. A lot of the best practices when it comes to deploying and monitoring a machine learning model, a lot of the things you've learned from software engineering also apply in this instance, but more heavily focused on data and this link, and where we see machine learning programs in the while go a bit wrong is when there are subtle differences in data you use to make a model and the data you use to make a prediction. I think that's where it can fall down and that's where it's a bit tricky to get right.
**Zhamak** : Jarno, from your perspective, what are the similarities and differences between any other executable and a serialized machine learning model that's now being deployed and running as an executable?
**Jarno** : I think you can frame it as a question of if you take machine learning out of what we do today in software engineering programming, how do autonomous cause without machine learning? If you start thinking about how to program a driving vehicle that's totally autonomous, I think it's problematic if you can't use data as the basic input of the program and something that you don't need to explicitly code. I think the total paradigm is different and that lays the groundwork of why do we speak about machine learning and I think what's great about it's because you can solve totally different problems than with traditional software engineering.
I agree totally with Max that I think the best practices are strictly the same. I don't think there's much differences in doing testing. You should basically go by the same rules of architecture and so on, especially if you're doing production systems. I think there's a lot of similarities in how we want to deploy and how we want to run them but they solve completely different problems.
**Mike** : Can you give any more specific examples of where machine learning has potentially gone wrong because people were not treating the software in the right way? Like both of you have alluded to it around the model, the data used to build a model and the data used to make predictions diverging. I think maybe some other examples of where things go wrong could be helpful for people to anchor that.
**Max** : Yes, there are several types of failure modes in machine learning and many of them have to do with this difference in data distribution when you make a model and train on it and what you actually see in the world. This is largely an unsolved problem, it's quite tricky. You can imagine, let's take autonomous vehicles, I actually saw this was going on the rounds on social media a couple of weeks ago, where someone was in a vehicle with semi-autonomous capabilities and they were driving behind a truck with traffic lights on top of the truck.
I think this is a perfect example of where things can go wrong. When you make a model to try and navigate your car in a world, you see traffic lights at particular junctions but what you don't expect to see in your data or may not have in your data is this edge case where something happens in the real world that's perfectly natural and you know how to act when you see a truck full of traffic lights but a machine can't distinguish what's happening. That's one clear case of the distribution you trained on is not exactly the same as you see in the real world and there's a really long tail of these edge cases that you need to be aware of.
Other very clear issues you might see is if you take let's say data from a database and you train your model on it and you want to deploy it in the real world and you need that similar type of information to make a prediction in the real world, you may have some different operational database with different latencies, data might arrive there in a different fashion, so you won't get precisely the same type of information you're interested in. There may be some ETL pipeline, some other technical reason why the data isn't as fresh or as stale as when you saw it, to begin with. That can lead to quite unpredictable results really.
**Jarno** : I think the unpredictability is one of the keys here. I think it was some years ago that Netflix was accused of being racist yet they don't ask for race when you subscribe to the service, which means that from the implicit data and the behavior of the users, the machine learning models can learn ways of doing personalization and doing recommendations in a way that might be perceived as racist yet it is unknown to the actual system beneath. I think the unpredictability is certainly key. How do you actually design tests for something that is not deterministic? I think it's a good question and yet to be solved in machine learning.
**Zhamak** : In fact, I think Mike and I both have recorded previous episodes on this podcast where we've talked about addressing the first problem, Max, that you were mentioning, the disparity between the data that you had access to at the time that trained your model and the data in real-world that's being fed at the time that you're inferring using the model. What are the architectural models that we can put in place to make sure the data that you have access to at the time of modeling is reflective of reality, is truthful, is relevant, and all of good things. We have episodes on data mission and other conversations to cover that.
I think, Jarno, to your point about testing how testing and continuous delivery change where you are in this non-deterministic world, how do you test unknown unknowns? We've talked about I think in the past episodes around continuous delivery and different types of probabilistic, I guess, based oriented testing of the models, which I think is a fascinating space.
I want to shift our focus a little bit on, let's assume that we've done a good job in terms of having access to the right data to model. Yes, there will be some corner cases and we've done a good job in testing, and now we're deploying them into the wild. I want to pick your brain about what are the different ways that we can actually see these models running in the wild, serving over APIs, or where would they go? How would they get embedded into the execution ecosystem? If you can talk about different types of models and different architectural challenges perhaps around the deployment of those.
**Max** : There are several ways. I like to think there are three or four general setups you might have for deploying machine learning models. One is probably the most widely used still, which is batch recommendations. You make your model and you validate it offline and you use that model offline to make predictions. What you end up with is obviously predictions, you may associate that with some metadata. Then the problem of actually serving these predictions is more traditional software engineering. You have a piece of data that needs to be stored somewhere and you need to serve it. If it needs to be served over an API in real-time to customers, there's obviously speed and all sorts of other requirements.
That's a common setting. It's also a setting that I probably recommend if you're not familiar with machine learning is to do that first because you can obviously run batch predictions at a relatively good pace so you don't have those hugely stale predictions. Another way of deploying these types of models is to do online predictions. Again, traditionally, you train your model offline, you have a model, an artifact which you load into some API, and then when you need to make a prediction, you fetch fresh data to make that prediction. That data can come from a client's side, from a web browser, for example, it can come from some other database, but it needs to be accurate to the data distribution that we talked about earlier and needs to be available quickly.
Then there are these types of hybrid deployments where you may do one of both, so you may take some data that's sent to you or fetch from somewhere really quickly to make a prediction, but you may tie that together with some other batch prediction that you have. These can require quite a lot of care as do online models because if you have even a portion of data that you can't see before you make a prediction, you have to be quite certain that that data is amenable to making a good prediction, and you have to be able to deal with missing data. You have to be able to deal with the data not necessarily being missing, but being in the wrong format, the ranges being off. Online serving of predictions is generally speaking, more tricky.
You have these three different types of learning. Then you have some emerging trends, which we can probably talk about later, which include things like not training your model in advance. Doing so-called incremental learning or continuous learning where you have an effective set of parameters settings. You put a model in production that hasn't learned anything or has been warm started with some data, and it continues to learn, it continues to update itself autonomously all of the time, possibly several times a second.
**Mike** : Maybe I could try to give some examples in my understanding of what those things might be and you can tell me how wrong I am. Bulk prediction, for example, maybe you have a model of customer churn and you compute a churn likelihood for all of your customers and store that in a database. Then when someone phones your call center and they're a high churn customer, you flag it in the UI for the person receiving the call that this is likely to be an annoyed customer and they should treat them with extra care or something like that. That would be the first style and I guess the second one is where you are doing online predictions is, I don't know, have you got an example of that?
**Max** : You could conceivably do recommendations. One thing that's quite normal to do is anything to do with images. For example, if a customer is on a website and uploads an image and there's some image recognition going on, the only data you really need in order to make a prediction there is the image itself, the raw pixel data. That's something that's quite good for online prediction serving use cases. There's no reason to first store that information somewhere and then, later on, make a prediction. You want that prediction to be reflecting what the actual thing that was sensing you want that prediction to happen quickly and you don't want it to be old.
**Zhamak** : Can you give an example of the hybrid model you were mentioning that you do access some pre-trained data and then also live online. You have some API, sorry.
**Max** : These can get a bit more tricky but if we continue this example of, let's say you have pre-calculated churn risk scores, and let's say you have some other piece of information that is calculated or prediction that's calculated online, let's leave that open for now, you may want to do something like you may want to sum up these prediction values. You may want to weigh them by something in order to make a business decision or return something to the user.
If you have a model that for whatever reason is batch, there may be a very good reason for it, it may be really hard expensive to compute these predictions, and then you have some online prediction, then you can still make an aggregate result to return to the customer. These are typically quite proprietary and they're quite business case-specific but I hope that gives you a general idea of when you might want to use this type of information.
**Zhamak** : Jarno, do you have any examples of these emerging trends that Max alluding to with reinforcing learning and just learning with minimal pre-training?
Jarno: Yes, absolutely. I think, again, if we continue with the business case of modeling churn because it's one of my favorite topics because it's 100% wrong or maybe 99%, but the problem is that if you take churn predictions, you are usually predicting states as you said, Mike. I have a churn rate of 90% and you may have 80%. Problem is companies are weird places. You don't take deterministic action based on that state prediction. The actions can be pretty varied, they can be really biased. They can be respective of whatever it is this business silo approach of that specific company and so on, which means that only part of the states get acted on. It also means that only a part of the states that were acted on are acted in similar fashion.
Now, this creates a problem for actually making the models learn because obviously, you don't necessarily see what were the actions taken, you only see the end result. Meaning that if you built the model yesterday, if you changed the model yesterday and I got 90% and you get 80%, but for some reason, they decided to send you an email with a discount for whatever service, that may or may not change your behavior towards the company. It may or may not change the state prediction of your churn rates. What will this mean as this carries on by time? What will happen if we train the model anew day after day for years and years? What has it actually learned?
It's a problem and a question which brings us to, and I think Max can continue on the topic that, what if instead of states, we would predict actions and we would actually be rewarded if those actions were true? Instead of saying that my churn rate is 80%, let's suggest what is the best action to take, call me up, send me an email, give me a discount, do nothing, take that action every single time. Take that action, even it being do nothing, but take that action, and based on the result, if I do something that we wanted, or if I don't, give a reward, negative or positive. This brings us to the topic of reinforcement learning. What if instead of trying to predict states, we would predict actions, and we would actually learn from that as an agent, instead of a machine learning model that's trying to learn only from past data.
**Max** : Risking, going a bit off-topic because this is interesting, just in general is. I think, one of the mistakes we make in machine learning to date, partially because we're a bit stuck in our ways and partially because we don't know how to solve everything yet, is continuing on this churn example is that we end up with a prediction of who might be churning when we could just as well predict what we should do about it, which is the actual problem at hand. There's usually a huge gap between making a model and actually doing something based on it. If we only train on historical data on how things have been done before, we may be missing some course of action that might actually be better.
That's what reinforcement learning is all about. It's trying to predict what to do, and it's giving a machine also the autonomy to choose something you might not agree with, in order to learn more about the world. I think that's an emerging trend that's really interesting and that also has implications in how these types of models are served. Because we don't have only predictions, we have a piece of feedback that happens later on. That feedback is directly tied to the prediction I made. In order for us to learn from that, we need to tie these two pieces of information together, and we can't really make mistakes in that stage.
This is, even, it's larger than just the machine learning problem. It's an organizational problem because you can imagine that when you try to move to this type of way of working, the gap between a data scientist making a model and something happening needs to be as small as possible.
**Jarno** : Exactly. I'm just going to quickly because I think this is really profound currently in the market. It is really difficult to go from the strict state predictions and go from the traditional way of doing machine learning to reinforcement learning. Something else that forces you to say that this is better than that, this is the reward that you get if you take this action, and this is what happens because it forces the organization to say that this is the value of the actions that we take. That is not true, that is actually pretty hard. What is the value of me selling this gray t-shirt versus Max selling the black one? Is there a difference? If it is, how should we calculate it?
What should we do about some rewards or something where the feedback is not immediate, and the feedback is not necessarily explicit in a way, such as total customer lifetime value, or something else? That's actually what we are trying to achieve, which brings a whole new set of problems on how do we want to actually reward these autonomous systems of the actions that they take. It's a fun challenge for organizations and businesses to actually say that these are the actions that we take, this is how we value them. It also makes them learn about their own internal processes and how they see the world, which I think is golden.
**Mike** : Just for the listeners to expand on that reinforcement thing a bit. I know we've had a conversation about this in the past, and I thought it was fascinating, not as a machine learning professional. My impression of reinforcement learning was actually there was a lot of game playing style models where you can have multiple versions of an agent that plays a game and then you play it against itself at huge scale and then it learns to get better. When we talked about it, you guys also talked about reinforcement learning for dynamic pricing, which I thought was really interesting because I was under the impression that you needed thousands or millions of events or attempts for the system to try a course of action and to reward or not to reward.
Actually, you are able to use reinforcement learning for dynamic pricing where the system could explore what level to price something at and then get a reward based on not just, did the customer buy the thing based on the price, but also even intermediate things like, did they put the item into their basket? Maybe you get something of a reward for that or you get a bigger reward for them actually purchasing the thing. I don't know. I thought that was a good example of making reinforcement learning a bit more concrete in people's minds.
**Max** : Yes, absolutely. I think not to go on and on about reinforcement learning is one piece of a larger puzzle was quite promising though. The reason it's mostly applied in games nowadays is because to do reinforcement learning, there's a classical problem where if I take a hundred different actions and I see something really good at the end of it, I need to know which actions led to that really good reward. That's something that adds to the amount of data you need.
The second is that the easiest way to do reinforcement learning is to have access to a simulator, which you do if you do games, but you can play against yourself, you can play against the computer and become iteratively better, whereas for real-world problems, let's say pricing, you don't have a simulator. If you knew what people would buy at what price you wouldn't need machine learning, to begin with. What typically is done for these types of settings in the real world is that we use relaxation of reinforcement learning where the reward has to come relatively quickly and it's only assigned to the previous action you made. This makes it tractable, something that you can learn, and it's also possible to do without a simulator which is quite exciting.
**Zhamak** : I guess going back to the original question of what's the difference between the good old microservices running with some a restful API and this particular model that it is probably deployed as a microservice within API. As you were describing this, I was putting my architect hat on and thinking about, okay, all of these now new links and connection points that I have to make to actually get that way down the line feedback into my system is something that I don't necessarily have with my microservice.
I call an API and the microservice actually decides whether this API you called was successful or a failure and all the information is available within the context of that transaction, either as part of the data available or environmental context, or the parameters sent to me.
In this particular case, the job is not done. Once you've called that API, you've just started a bigger transaction that needs to happen, actions will happen, and the feedback needs to come back and that link architecturally needs to be made. Are there any other differences around architectural deployments and integration models and links that people need to think about that we don't normally think about in just good old applications?
**Max** : I think it's useful to think about these types of systems as event-driven systems. First, you make a prediction, and ideally, at the point of prediction, you want to store the data that was made to make that prediction. That's very important that you store it's at the point of prediction. You also crucially in practical applications, you want a unique identifier for this prediction, and that is returned then to whatever end-user you have. It is the end-user or caller's responsibility when they give feedback that they give feedback with this original ID you gave.
That gives you the possibility to link these things together. It also gives you the possibility to deal with things like rewards never happening, adding default rewards. All of these can be consumed in some form of an event stream. You can even join these pieces of data together in an event stream. When you link these things up, you have then training data that you know or if it's properly implemented, you know that this prediction led to this reward either now or in the future. You also have the data that was made or used to make the prediction so you can be certain that there's no weirdness going on with time or something else.
I think that's an abstract recipe for success is that you need an additional piece of information, a unique identifier through this whole loop, and you have to be very careful that it actually goes through the whole life cycle. The life cycle begins with a machine suggesting something to do, and that piece of metadata has to go through every single piece of feedback you want to associate with this entire system.
**Zhamak** : I really like the idea of event-driven choreographed systems because as you were saying a minute ago, sometimes you have multiple predictions made led to a final action. How do you know which of these steps and which of these predictions have led into that? If you have multiple machine learning model, let's say I called the call center and there was one model that said I'm a customer that might have a high score of churning, then I will get some treatment. Then another model says, give her this type of price or offering, and that led to a different action. All of these can be sitting and listening for the final action event that what did I do, and then they can learn from that. It's not just a single model that might be learning from that final event that happens.
**Max** : I think ideally you want to make systems that are governed by one model if you can. One model can make several predictions, that's not a problem. Obviously, across all domains that won't work, but I also suggest people to try and keep it as simple as possible. You can see really good results with a relatively simple reward calculation and not trying to tie it to something that's very far in the future. In a business sense, what you probably really want to do is you want to optimize profits or revenue but it doesn't really make sense for a single let's say, recommendation engine to wait for quarterly results and feed that back into the system. There are so many moving bits in the middle that that will lead to trouble.
Usually, what you want is to take a feedback that you know correlates well with a longer-term reward and something you can calculate quickly. That is something that you can do quite successfully nowadays but you should spend time validating whatever metrics you use. Feedback is the lifeblood of machine learning, be it supervised learning, reinforcement learning, or anything else. If the signal's wrong, then you're doing the wrong thing.
**Zhamak** : All right. We talked about sales and marketing use cases. Let's have a bit more fun about where machine learning can actually be used. Jarno, I'm curious if you can share some of the work you've been involved in deploying machine learning models in the wild that might be interesting for our audience, and it may not be the default use cases that they think of in terms of image recognition or, I don't know, recommendations to buy the gray t-shirt or the black t-shirt. Can you share some of those?
**Jarno** : Absolutely. We've been fortunate enough to work on multiple cases and a bunch of different problems, but the one that's I think is interesting is the one that we did on computer-made whiskey. Not that that specific case is the most interesting one. It is. We took like hundreds or thousands of years old industry and we said that, okay, can we actually make whiskey recipes with computers? Can we use this computational creativity, generative modeling, whatever you want to call it, can we use it to augment the creative experts? I think that's the interesting bit here.
For multiple years and even a decade, I think we've been mostly using machine learning to automate stuff. We use it to automate marketing, we use it to automate personalization, direct pricing, we want to do autonomous vehicles, and so on. What is interesting is what's to happen when machine learning becomes this coworker for experts and even creative experts, and whiskey is just an example because it's an example of an industry where the process is hundreds or thousands of years old, and we want to be able to show that we can actually create something meaningful with computers in that setting.
If we can do so, what does it mean for other industries that are highly respective of humans as the main driver of value? What does it mean for architecture? What does it mean for design? What does it mean for healthcare? What does it mean for all of these things where we still want the human in charge, but we could augment them with something a bit more emerging? That's why I think generative modeling is interesting because it's a whole new, different paradigm. You're not trying to make the best possible prediction anymore. You're trying to create something that's creative in a way that we, as humans are creative. It can come up with solutions in which all of the solutions are good, but something that you would've not thought about yourself.
I think that's interesting, because what does that mean for entire industries from media to retail to what have you, and that's what I'm personally-- one of the things that I'm most interested in is that how will generative modeling actually, change entire industries? What does it mean if computers become coworkers?
**Zhamak** : I remember a long time ago I was reading on Lateral Thinking with Edward de Bono. These exercises that you can do to get away from this linear thinking and rational thinking that we all very much used to and just come up with random ideas that seem wrong, but maybe they finally take you down a creative path. I'm curious in this whiskey building or making a generative AI solution that you had, what was it doing? What was it suggesting?
**Jarno** : Yes. Basically, the problem that we had was a blending problem. The company, Mackmyra, they make whiskies and they mostly make blends, meaning that it's a single malt whisky, but you have different casks where the liquid is sitting. It can sit for 6 years, 10 years, 12 years, 20 years. The problem is you have a hundred different cask types. The question is, how can you make the perfect liquid out of a specific combination?
From a hundred different cask types, and you can choose the amount that you want to use and mix. The problem space is infinite. You cannot just brute force all of the solutions and try to come up with the best one. You need to create a system that will intelligently explore the space around it and somehow be able to do discrimination on the things that it finds.
It has to be generative on one part and it has to be discriminative on the other. That's basically the architecture around which I think most generative models nowadays work.
That's what we also did. We fed in all of the previous recipes, all of the previous products that they've done, which are basically mixes, which are basically blends of these ingredients. Then we created basically a tailored algorithm around the generator and discriminator architecture, through which we created a system that's able to create new recipe ideas, so new ideas for different blends, and can do that in a way that they are interesting, they are new, they are tasty, but they are not something that they have done before.
**Zhamak** : I don't know if I should feel envious or sorry for the human in the loop that was testing the result of that model you had.
**Jarno** : I would go for envious. I think it was a good one. I highly recommend.
**Max** : As a side note, I can say, during this project, they sent testing samples in the post that were just handwritten. I suspect the finished customs had some issues with those. It was fun times all around
**Jarno** : Yes, truly. I highly recommend end to end testing for computer made whisky
**Mike** : Just on that, is tastiness of whiskey an objective function that you can evaluate? Because the distiller, I guess the master distiller or whoever it was who's supervising this thing, they're the ultimate arbiter of, yes, this tastes good or, no, it doesn't. Because I don't know, it's a little bit like art, right?
**Jarno** : Yes, it is, certainly. I think what is interesting is that what we did was that we wanted to give, we basically took two rounds of creating samples, and then we went with a product. We used information from customer ratings, you had rating sites all around the web. We used ratings or basically rankings out of sales, we used expert reviews, we used information that what of these different products have actually won some prizes and so on, which gives us an idea on how can we build a score for all of the previous recipes but doesn't solve the problem of how do we actually teach that to the discriminative model in a way that it will not lead the generative part to just do the same recipes? That's one problem.
What I think is more interesting is exactly what you said. What if in the future, this is not what we're doing. We're not asking a computer to create a product and then it does, but rather, we actually work as the intermediary, as the main source of feedback, and we actually interact with the model day-to-day so that it produces something, we test it, we say it's better or worse or something else than we've done before. Then this goes on and this creates actually this co-worker loop if you want. That you're actually interplaying with a machine learning model to produce a product. This is, in fact, true currently at one of the other customers that we have. I hope we're going to go live with the story soon.
**Max** : I think the key thing to know in these types of computational creativity cases is you don't need to be perfect and you don't need to be able to scientifically define what taste is because that's near impossible. What you want is something that's close enough such that you have an ideation machine that can help you think outside the box because you are the final arbiter of the decision. Not just whiskey and in other creative industries as well, you can see this being deployed already. It's not just something that's done for fun. There are also cases where, objectively, these things have been done better in the market than others. I think that's exciting stuff.
If we think about work that other people have done, one thing that caught my eye is that you can use machine learning and optimization in general also in IT. In software and in hardware, and this is perhaps not as exciting as whiskey-making but, for example, chip design. Last year, Google published a preprint of a paper that uses reinforcement learning to do floor plans for chips. Which components are placed where? This is a very, very difficult problem. They were able to achieve better than human-level performance in about six hours. Now that algorithm is used to make the floor plans for their machine learning acceleration chips, funnily enough. I think that's unexpected.
The second is database systems. Instead of having a database system where information retrieval is thought about really, really carefully, like what kind of B3 setup do I have, what kind of index is where, you can do it data-driven. You can have your own data and you can use machine learning to try and find the best way of indexing and retrieving data that fits your use case. These are things I wouldn't have thought of first when it comes to what machine learning can be used for.
Then just to plug our own case of aircraft parking, we did a case where we generated automatically parking plans for an airport such that robustness is maximized. If there are delays, it doesn't necessarily mean we need to do a whole new plan but that used the different optimization technique, but there's a lot of unknown variables that you want to know when you do this type of optimization and predicting the unknown is what machine learning is all about. I think that's a really interesting avenue is combining all the types of optimization routines such that the decision variables you use, if you don't have them, you can predict them quite accurately with machine learning. It's kind of a hybrid model. Those come to mind.
**Zhamak** : Max, Jarno, thank you so much for this episode. I think this was a wonderful conversation. We could have gone going for another couple of hours here. Is there anything you want to share with I guess our audience last? Anywhere they can follow your work or any pointers on your talks or writings you want to share?
**Max** : What I'd encourage everyone to do is go have a look at the Thoughtworks blog. We've moved some of our write-ups over there. I'm also semi-active on Twitter, you can always reach me. It's @maxpagels. Also, feel free to say hi on LinkedIn. I think you can find some of my writings in the area of reinforcement learning and incremental learning scattered over the internet, but I think via thoughtworks.com, you'll probably find a path to them.
**Jarno** : Yes, plus one on what Max said. I've also written quite a bit about how to do applied data science for business initiatives. You can also learn that I think, scattered around the internet. Also, feel free to contact on social media.
[END OF AUDIO]
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