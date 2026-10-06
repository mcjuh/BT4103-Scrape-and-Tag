<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/building-intersection-machine-learning-software-engineering | Title: Building at the intersection of machine learning and software engineering | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Building at the intersection of machine learning and software engineering 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Agile engineering practices ](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)


Podcast host  Scott Shaw and Ken Mugrage | Podcast guest  David Tan , Ada Leung and Dave Colls
May 02, 2024 | 48 min 30 sec 
Listen on these platforms
## Brief summary
Bringing machine learning models into production is challenging. This is why, as demand for machine learning capabilities in products and services increases, new kinds of teams and new ways of working are emerging to bridge the gap between data science and software engineering. _Effective Machine Learning Teams_ — written by Thoughtworkers David Tan, Ada Leung and Dave Colls — was created to help practitioners get to grips with these challenges and master everything needed to deliver exceptional machine learning-backed products.
In this episode of the Technology Podcast, the authors join Scott Shaw and Ken Mugrage to discuss their book. They explain how it addresses current issues in the field, taking in everything from the technical challenges of testing and deployment to the cultural work of building teams that span different disciplines and areas of expertise. 
  * Learn more about [Effective Machine Learning Teams](https://www.thoughtworks.com/insights/books/effective-machine-learning-teams)
  * Read a [Q&A with the authors](https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/author-q-and-a-effective-machine-learning-teams)


## Episode transcript
**Scott Shaw:** Welcome, everybody, to the Thoughtworks Technology podcast. My name is Scott Shaw. I'm one of the hosts of the podcast, and today, we are going to talk to some friends of mine here in Melbourne, where we all live. The topic is going to be their new book, which is called _Effective Machine Learning Teams —_ I think that's particularly relevant in today's technology landscape.
I'd like to have each of the participants introduce themselves and tell us a little bit about themselves and the perspective they bring to the book, but first of all, I want to introduce my co-host, Ken Mugrage. Do you want to introduce yourself? Do you want to tell us a little bit about yourself, Ken?
**Ken Mugrage:** Yes, sure. Hi, everybody. I'm one of your other regular hosts and the only person on this team that's not only not in Melbourne but not even on the same continent, actually, not even the same day. Welcome.
**Scott:** We're greeting you from the future. If you all would start — David Tan, why don't you go first?
**David Tan:** Cool. Thanks for having us, Scott and Ken. I'm David Tan. For deduplication purposes between David Colls and David Tan, I'm David. Yes, Dave has generously become Dave [laughs] for our collective-- to reduce the confusion. I'm a lead machine learning engineer with Thoughtworks.
I've been with Thoughtworks for seven years and, through this time, have been fortunate to be able to work on data and AI systems, help clients build various machine learning models, and in one time, building an ML platform, and really happy to be here to chat about _Effective Machine Learning Teams_.
**Scott:** What unique perspective do you think you bring to the book amongst the three authors, David?
**David:** I love engineering. It's something I can touch and feel and deploy and write and commit. I think in this book, I bring a lot of that ML engineering perspective in the intersection between software engineering and ML systems.
**Scott:** Great, thanks. Ada, why don't you introduce yourself next?
**Ada Leung:** Hello, my name is Ada, and no, I'm not named after Ada Lovelace! I think that's a random fact about myself. [Laughs] I've been at Thoughtworks just over six years. My role is a senior business analyst or product owner or scrum master, the type of roles that we go on and work with clients where we bring people together. I think that's where my specialty is, bringing people together, building that shared language, but also delivering value and showing that we can deliver quickly as well, so de-risking delivery.
**Scott:** Thanks. Dave Colls, why don't you go now?
**Dave Colls:** Thanks, Scott. Yes, nearly a palindromic triad for the three authors, but I'm going by Dave, for disambiguation. I've been at Thoughtworks about 13 years, and in that time, I've worked in almost every aspect of the business and every service we offer to clients, from project management to business analysis to infrastructure to data science.
In the last seven years, I've been building the data practice in Australia. In that regard, my focus has been on not necessarily the detail of technical practices or data but creating environments for teams to be successful. I think that that's the perspective I bring to this book. What can we do in the wider organization to create a successful environment for ML teams?
**Scott:** This is the first time I've heard the phrase "palindromic triad" used on one of the technology podcasts, so thank you for that! I'll be looking it up later... Let's get started. How did you come to write this book? It's a big endeavor. Writing a book is a big job, one that I would be daunted to undertake. I wonder, how did you come to write this, and why a book?
**David:** I think it was a series of events. It started all with a blog post in 2019, just finishing off a project. It was a blog post I wrote about refactoring Jupyter Notebooks from that project back then. Then that blew up on Twitter. Someone in our community shared it, and there was, I don't know, 800 hearts, which to me was a lot. Most I ever got on Twitter or X. Then it became a repo that had 600, 700 stars.
Once or twice we ran it as a workshop in Thoughtworks Singapore with AI Singapore, and the feedback we got from folks who attended was like, "Oh, yes, this intersection between ML and software engineering wasn't talked about enough." How do you test models? How do you refactor Notebooks? We got those feedback points and said, "Okay, we're onto something here."
Then we eventually put together a book proposal and O'Reilly accepted it. It's been a journey of fleshing out those points about, "How do you build reliable ML systems?" How do you get feedback? How do you apply product thinking? How do you test your ideas with users? That's how it came to be a book there.
**Scott:** Ada and Dave, how did you get involved?
**Ada:** David reached out to me and said, "Hey, would you be interested?" and I said, "Yes, why not?" I think that's always my default if I haven't done something before. The previous writing experience I've had was publishing a Thoughtworks blog on slicing data stories. It was a big jump, but at the same time, it's been such a hell of a ride, distilling my thoughts and moving from implicit knowledge to something that is shareable. I think the journey has been quite rewarding as well.
**Scott:** There's been so much written about machine learning technology, and in my experience, I guess the things don't get actually done unless you have an effective team to put it together. I'm really happy to see that perspective represented in here.
**Dave:** Yes, and I think that was exactly how I got involved in the book. Having had the good fortune to work with David and Ada in the past and seen the reception that David's coding habits for data scientists and other resources had generated, I really wanted to highlight that it wasn't just about an individual contributor perspective, that the practices and tools that he was advocating for were really there to enable whole teams to deliver effectively.
**Ken:** I'm curious if I could. You each had a lot of experience in your own particular roles. How different was what you thought you knew versus what you learned you knew during the writing process? Sometimes, you, "Oh, I got a good handle on this." Then you start researching and, "Oh my gosh." Was that a big leap, or was it incremental? Did it just bounce off each other? What was that like?
**David:** I think that's a great point. The story I've been telling people is that I started writing this book with Ada and Dave going in thinking, "Wow, I know so much about machine learning from past projects. I want to tell the world about it." Through writing, I was like, "Oh, there's so much I don't know." [Laughs]
I think through the literature review, through testing ideas whether on a project or through our technical reviewers, and we have a panel of other reviewers with experience in other domains and ML technologies, through that, it's been a lot of growth, a lot of learning. Even through literature review, one of the books that I read was _Atlas of AI_ by Kate Crawford, which was like a whirlwind tour about responsible AI in application.
There's just so much in any of those sub-topics or branches in the domain of ML. I think writing definitely helped to make, at least personally, my knowledge more robust. Ada?
**Ada:** I was thinking about how we've collectively been on different engagements, client engagements, and we've been on ones together, and was it a big leap? It felt like it was in the sense that the book was one engagement, and do we have the experience from end to end? Equally, it wasn't because we've collectively been on different types of client engagements, like fast experimentation with ML, productionizing an ML PoC that was just thrown into production. In some ways, it wasn't. It was just collecting and rehashing our memories, and it was fun going down memory lane together.
**David:** I think there's an aspect of it that is like testing and extending what we know. We had an idea for a chapter about automated testing for ML systems through writing that we were like, "Okay, yes, you can write an automated test for an ML model using a global metrics test," but then through that we discovered, "Okay, there's the hidden stratification problem where maybe the model is 70% accurate but actually for a particular subclass is totally rubbish." Like maybe 40% accurate.
Through testing and through checkpointing our knowledge with a working example in the book, a code repository, then we refined, "How do you fully test ML systems and monitor it?" I would recommend-- Blogging or checkpointing has been a really helpful exercise to consolidate that knowledge.
**Scott:** Can we assume that the fictional scenarios that are depicted in the book are actually things that happened to you, that really happened, and that you've observed on real projects?
**Dave:** Often, they're amalgams of different things as well. Yes, they're based on a true story, as it might be said.
**David:** Yes. In our book, we followed the arc of this fictional character called Dana who's a data scientist or ML engineer. Somewhere in the book, we say the character is fictional, but the pain is real. We follow her. Throughout, it's basically versions of Ada, Dave, or myself in various scenarios where there's a story in there about deployment day, release day.
We have a launch party organized. We're going to celebrate the release of this new ML model. As she is there with the infra engineer to try to deploy this thing, deployment fails, and then before you know it, it's the troubleshooting. It's 7:00 PM, and they have to go to this lunch party feeling guilty like, "Actually, the ML model's deployment failed." We try to bring our experience to life in this book through these story snippets that hopefully people can relate with.
**Scott:** Is there an overall message? Are there a few key takeaways that people are going to get from the book?
**Dave:** I think for me, it's about great ML products require effective teams to build. When you look at team effectiveness and the way we've broken down the book in broad terms, we've broken it down into sections that focus on building the right thing, so understanding the right business problems to solve, where you have access to the required data and where an appropriate ML paradigm exists for a successful product to be built.
Then we focused on building the thing right, so the practices that will enable you to manage complexity and to maintain responsiveness in delivery. Then the third element has been building it in a way that's right for people, as we've described. A lot of those stories indicate the pressure and difficulty that the teams can have working in these highly complex environments with many different demands, so we're looking at, "What can we do to relieve the cognitive load on teams to create safety nets for delivery and also to align their work with value streams within the organizations so that they're not blocked on getting value to customers?"
**Scott:** I know I've seen, especially in the early days when organizations first started embracing machine learning, if you were talking about a machine learning team, you were talking about a team of data scientists, and they always sat separately from the main engineering department and the product people.
I'm assuming you're talking about cross-functional teams here and teams where data science is embedded into a larger product stream. Do you see that changing in the industry?
**Ada:** Yes, absolutely. I think data scientists in nature are very curious creatures as well. People like to understand the bigger picture of why, not just how, a model is put together, and the answer to why is usually sitting with product owners or business analysts or business-shaped folks with that context and who are close to the end consumer or customer. That can be an internal one or an external user as well.
I think that contextualizes it and makes it human in terms of how usable and then therefore how valuable what we're producing is. We do see the added increasing pressure of return on investment, for example. There's a lot of investment going into these spaces, in organizations, and being able to demonstrate it in a showcase where you can see the impact, not just showing a feedback loop and the data being collected and how it's being retrieved, I think that is what gets everyone else in the organization interested and then on board with ML-driven products.
**Ken:** Question. 2023 was the year of the hype around generative AI and so forth and not going away anytime soon. That aside, is some sort of machine learning a part of what percentage of projects would you say? My impression is very, very high, but I'm curious what your real-world experience is.
**Dave:** Yes. Without putting an exact figure on it, very, very high from our experience as well, in different aspects in that ML might be incorporated purely as a service into a digital product from a third party or from another part of the organization as a starting point. It's still useful for teams to understand what goes into building ML services in that regard as well and how they might fail and how to properly test products that incorporate ML services right through to in-house built ML products where proprietary data training processes and deployment of the models are all taken care of in-house.
We're seeing a very high proportion of products, especially as organizations move to provide more convenience features in digital products, so a lot of those convenience features are driven by ML. Again, if we look at digital marketplaces, often, we're looking to provide insights to both sides of the marketplaces, and a lot of those are driven by machine learning as well, but yes, we're seeing the application spreading.
Then we've also got the generative AI wave now currently as well, so in those cases, mainly integrated in that first mode as a service, but we'll probably see as the tooling improves and we're able to build smaller, more dedicated models, we'll probably see more of that coming in-house as well.
**David:** Yes. My read of the ML landscape today post the 2023 hype or boom of generative AI, as you mentioned, Ken, is I see a long tail of if we plot a Y-axis of number of ML practitioners like ML engineers or data scientists if you do a count of data, I think it's a long tail where you have a long tail of orgs with perhaps one or two, maybe three data scientists or ML engineers, and then there's the chunky middle path where perhaps you've evolved and become more mature.
You have a full data science team that's servicing multiple varied needs. As Dave mentioned, maybe it's insights. Maybe it's language models. Maybe it's personalization, but then there's the third part, which is the very few, but deep organizations with multiple data science teams could be-- I've heard numbers of 100-plus data scientists. It could be ranging a bit from 20 to 100.
I think all the more, it makes it important in order to reduce the frustration of these practitioners of people who have hopes on these ML products going to the market, that these product and engineering and team topology practices, they become more important to help these teams to be able to move towards a goal.
Let's say, it's about building a recommender system or building an insights report using advanced analytics. It's very common to see some teams cycling around PoCs after PoCs that just are not maybe good enough or don't have a market for it. PoCs are good. It's a great way to test ideas. They also over time make practitioners frustrated over time when you don't see things going out into the market.
We talk a lot about practices to test these ideas early so that when you start to really build and productionize something, it is something that's fit for market, is product-market-fit, is problem-solution-fit, and how do you build that rapidly using engineering best practices?
**Ada:** You mentioned something, David, that I wanted to go back on and that is a shared goal. Ken, you asked the question how much of gen AI are we seeing out there? We see a lot, but also, the risk is also high in terms of are we really getting a return on investment because you have a lot of the tools there, but what is that saying?
If you have a hammer, everything looks like a nail. If we're not clear on that shared goal and we're not clear on what customer problem or value we're trying to create or get back because of market competition, then we are seeing what David mentioned is lots of PoCs just cycling through. Forever being in discovery is not always a bad thing.
I think statistics with the big tech is what? 95% of PoCs do fail. It is important to keep on going, but it's also equally important to have a shared goal and vision and also a clear idea of what kind of problem or value we're trying to solve.
**Dave:** If I may, I'll come back to the question on team shapes as well. Is it a multidisciplinary team, or is it a group of data scientists? I think that in the early days of data science and machine learning exploration in organizations, they saw data science as the key problem to solve. It certainly is one of the key problems to solve in many ML teams, but while it's necessary, it's not sufficient. We also need to have a business problem, a product lens.
That's another element. We do need to be able to connect insider intelligence to action in organizations as well. We might be working with teams of data scientists who could build great predictive models, but it wasn't possible for that to actually influence a customer experience in deployment in the organization so that there wasn't an opportunity to deploy it into production, or production systems were unreliable to the extent that, say, offers weren't being fulfilled, so the value of those better-targeted offers wasn't being realized.
Then the question can factor, "How do we solve these with the team construct?" and that's where we see-- and I think Thoughtworks' heritage has been around delivering value end to end in short cycles, especially, there's established literature around the innovation potential of multidisciplinary teams as well. If you're looking to do something new, then that's where a multidisciplinary team really shines.
That's been our default unit, but one of the great things that came out from the book was some time and space to explore the various team shapes for machine learning and what role they might play in a larger enterprise. We've still been able to articulate "What's that team shape that's mainly composed of data scientists? Where might that play a role in a larger enterprise, and how might do you make that team effective?"
**Scott:** You mentioned product thinking and building products and the importance of understanding the customer. What else? What does it take to make a great machine-learning product?
**David:** What does it take to make a great product? Product development is hard. I think it was Henrik Kniberg from Spotify that says, "Product development is hard. Most products fail," and that's the reality of it. In ML, I suppose we are reminding people that shiny hammers looking for problems don't always-- most of the time, if it's not solving a real problem, then the return rate of your users are not going to be great.
You may get a high hit rate at the start, but it's not a solid or defensible product. One aspect that we talk about is just that lean discovery approach, so just to focus on what that problem is, and it may turn out that it's not ML, or it may turn out that it is. Regardless, once we have a clear understanding of who our customers are, what is their pain points, we talk about some techniques like user journey mapping, customer research, just maybe plain simple fact of talking to our users, which sometimes the bureaucracy of product delivery sometimes just stands in the way.
All the times in my career where we've had the chance to actually go talk to users or have one of our teammates go understand the user's needs, that has just always been very rewarding in terms of what their pains are and how our efforts align to that. To the question of "What does it take to build a great product?" the short answer is that it's a hard problem, and we just got to trust the process in a way and go talk to customers and talk to users and speak to that rather than to find ways to use our shiny hammer of AI.
**Ada:** I think about what makes a great product or ML-driven product. One is that the team, and hopefully it's a cross-functional team, we see ourselves as a customer as well. I think that's really making it close to building the mindset of the customer. If the product is being used, I think early indicators maybe could be like we're discovering new things about our customer that we didn't know before or we didn't anticipate.
I think those would be really cool indicators of what makes a great product because your ML-driven aspect of that is automating something really quickly or learning something really quickly and then being able to suggest another decision or assist the end user with something that they may not have been able to do before. I think that is where great product innovation comes through. We're just discovering something new and unexpected, and I think that is a great success indicator.
**Scott:** It seems like experimentation is a bigger deal with these data-driven machine learning sorts of projects. I know experiment tracking and being able to do experimenting in a methodical way is part of it. Do you cover that in the book?
**David:** Yes, absolutely. In the context of continuous delivery and the path to production, experiment tracking is absolutely a critical part of that. There was one project that we were on and when the builds were green, we had high test coverage, we had model quality tests, and we had an experiment tracking dashboard.
Imagine a data scientist has a pull request with multiple commits, being able to just go to their experiment tracking dashboard and say, "Oh, yes, commit 698" was better than the one in production. That gave us that confidence to deploy the production knowing that it's a better quality model than before. Yes, it's absolutely a part of path to production for any ML model.
**Scott:** To be honest, I think ordinary non machine learning software engineering teams ought to do more experimentation. I've seen examples where that led to really effective outcomes, and maybe we could take some of these concepts and apply them back to software delivery in general.
**Dave:** Yes. We have borrowed I guess a term we call "dual-track delivery" from simultaneous user experience research and product development as well. The data science research looks similar from a delivery perspective to that user experience research. Yes, you'd start with hypotheses and then you go and test them, and you're either successful, or you're not.
In the process, you need to learn something and keep track of that learning, and exploit the upside of that learning in the delivery track where you're producing stuff rather than knowledge. Yes, I think it's a really effective model anywhere you're dealing with unknowns, or ambiguity, or uncertainty in delivery.
**Ada:** I couldn't agree more. I'm currently doing dual-track at the moment, and it's kind of nice as well as a team that you're not just doing your BAU or you're doing a long-term strategic feature, but you've got this other track of test and learn, and by the time you get to that near end of "Do we know enough and have enough confidence that the following investment to do the implementation is there?"
I don't know. Obviously, there's only so much context switching one likes to do in a day, but I think it gives a breath of fresh air in the terms of portfolio of work a team can do.
**David:** Just on top of that, on the topic of experimentation, I think it's also a function of the level of trust and safety within the team as well. Sometimes it's awkward or hard to say, "This experiment didn't pan out." In a high-trust or high-safety team, we can kill ideas very quickly. We say, "We try this. It's not giving us the results we want. We can bin it, and that's okay."
We are still learning rapidly. It's about how fast we can kill bad ideas, how fast we can learn from those. I remember moving to my first apartment years back before I had a kid. We used a new place, and we didn't have a rubbish bin. Then, two weeks in, it was like, "Oh, man, there's so much trash everywhere." [laughs] Not to say ideas are trash or products are trash.
I'm saying in the analogy of this house or this apartment, that the inability to chuck things away led to maybe that in my home, things lying around. Yes, I think that experimentation, as you mentioned, Scott is spot on in how quickly we can experiment how safely we can say that "This PR didn't pan out. Let's just shelf it." That's okay.
**Ada:** David, it's almost like it's a discipline as well. We say experimentation can be fun, but it can be a hard discipline for some people because we can go down to technical components and a Lambda versus an AKS versus a Databricks, and what do we want to use? The hypothesis is the overarching thing of like, "Well, what's our first end-to-end? What's our thin slice that we're trying to achieve?"
Really, that conversation in the team of prioritizing which test or technical spike we want to play first does matter because we're trying to be smart with our time as well.
**Dave:** Yes, this is exactly what David said. In terms of trusting in the process when the outcome is uncertain, you need to look at the leading measures such as, "Do we have a good set of experiments? Are we able to conduct them quickly, and can we exploit the upside quickly as well?"
**Ken:** Then what I'm sure is a very easy question is, how do you build a great ML team because that's harder to experiment with, right? People don't have feature flags, and it takes a little longer to roll on and roll off and that sort of thing. How do you build that team that's going to build the product?
**Dave:** Yes, we look at building blocks of teams as well as products, so this is the third section of the book focused on building things in a way that's right for people. We ask what's important for teams, in general, to be effective, but then we also add the lens of the fact that ML is technically complex and requires a lot of different disciplines in a modern product development context.
Then we look at elements like trust as foundational. In this section, we do refer to a lot of existing literature that was perhaps one of the challenges of writing the book, where to leave some of our insights at a paragraph and point readers to further information rather than have chapters proliferate endlessly.
In Chapter 10 in the book, we look at a range of things like trust. We look at communication. We look at the shared purpose and progress, as we've discussed previously. We look at diversity. We look at all the things that make teams effective in complex, ambiguous environments.
**David:** Yes, I think that's an engineering aspect to your question as well, Ken. How do we as a team experiment quickly? I think it's quite common in the ML engineering or data science world to be caught up in toil of, say, manual testing of a model's output. I think there was a Tekton Research from 2023 that said 30% of a data scientist's time is used on deployment rather than experimentation.
What we ended up doing for one of the projects we talk about in the book was that when a data scientist has an idea, if I add this feature, it might improve the model quality by X%. They can cut a branch and in their path to production do execute the idea, see the results on the experiment tracking dashboard. Don't have to worry about breaking stuff because tests will tell them that.
That fast feedback afforded from these engineering practices could help them experiment more quickly. If it doesn't pan out, adding this new feature actually makes things worse, fine, just throw that away and try the next thing.
**Scott:** Test-driven development is just as applicable to machine learning projects, I assume, as it is to everything else. What other engineering practices? I know, David, that's one of your areas. What other practices do you think are important in these contexts?
**David:** Yes. In the book, we talk a lot about testing. There's two chapters on it, and we take a nuanced view about TDD itself, which I can come back to later. We flesh out this kind of typology of tests of an ML system. We first start to think about "What is the subjects under test?" In any ML system, there are pure functions, right? Just data transformations, feature engineering, those lend themselves to unit-test very nicely.
Then the next part of it is the model itself, which are hard to unit-test because even the training of that artifact could be hours, could be 20 minutes, what have you. Then we bring on the lens of model quality tests, and most, I would think all, data scientists are very familiar with model evaluation, metrics precision-recall, and what have you.
Then we take it a step further, and there was an interesting example or exercise in the book where the model was 80% accurate. Then we explored the hidden stratification problem where "What if for some subclasses, actually, the model wasn't 80% accurate?" Then we wrote a test, we ran it, and it was like a loan default prediction example, and it did turn out that for some occupations, the model, yes, was 80%-plus above the threshold, but for laborers, it was 50% accurate.
We discovered this type of errors that was happening to a sub-segment of that data so that model quality tests and stratified metric tests brought that in. Yes, in an ML system, there's only so much you can test, and there's a part of it that's also just production monitoring. As this thing is operating in the production or as a shadow model in production, then being able to collect real-world data, say the model said, "Yes, this loan application is likely to default," and then collecting data on whether it did default or what's the risk profile over time.
Being able to monitor that in production was important. It's not monitoring as we know it, like real-time monitoring. Sometimes, the batch or latency depends on how quickly we can label those ground truths, but still, it's going to give you that feedback about the quality of that model. Yes, so a lot of engineering fun in ML systems, and it was just quite striking to us how--
I think we have the fortune of sitting in the intersection of software engineering and machine learning, so we could take practices from both worlds. Actually, there were some parts where we found that some engineering practices didn't always pan out, and maybe this is where I'll circle back to TDD. There were some cases where TDD wasn't going to give us-- or test-driven development doesn't give us that fast feedback.
Then at that point, it's like, "It's fine. If it's not, give us the feedback. We don't have to be dogmatic about practicing it." Actually, it's dogmatic in both ways. It's either dogmatic in that "Yes, I have the TDD," or the other dogma is, "No, it's machine learning. You can't TDD, and the truth is more nuanced." It's like being able to know when you cannot get that fast feedback.
It's interesting to really stretch the limits of these software engineering practices and see when it breaks down and add on some angle-specific engineering practices.
**Ken:** Perhaps more than any other area, I see practices that are common, but they're slightly renamed such like DevOps is now MLOps and continuous delivery is continuous delivery for ML is the process inside Thoughtworks. Is that positioning, frankly, is that to say to data scientists, "Hey, don't worry we're thinking about you"?
Are they radically different engineering practices? Is there a crossover? How much do people need to know? If I'm an infrastructure engineer and I'm now going to be on an ML team, do I need to go study MLOps, or am I going to apply most of my DevOps?
**David:** Yes, that's a great question, Ken. I think there are ML-specific extensions in the MLOps space. It builds on top of DevOps things like Infrastructure as Code, deployment automation, scaling infrastructure essentially for training or for inference. MLOps then brings in those ML-specific components like being able to have a metadata or model registry for every deployable because it's no longer just code; it's also this really gigantic model sometimes.
Then also things like a features store, so it's not just compute or logic at runtime but also what features need to be available at more latency in production. I think being a DevOps engineer gives us a really good background and starting point to understand a lot of this. It needs to be augmented with ML-specific or MLOps-specific practices.
**Ada:** I also see those namings is to be, one, inclusive and inviting. I think it's a really exciting space, and lots of people may be coming from career-changing and straight into this space and not from the traditional software delivery. I think being able to extend the name with MLOps, for example, it's to say that there is a whole body of knowledge that is tried and tested, lots of experienced practitioners with the points of view.
You don't need to go through the one-track pathway of having a PhD or go through tertiary studies, for example, to be an ML engineer. There are building blocks on the software delivery landscape that can lend you to being in this space and be part of this community. I think we do need to keep growing this community with different perspectives and different-shaped people because that's when our models are going to be richer and less biased as well.
**Scott:** I know you started this book back in the dim past before gen AI became the central feature in all of our lives, but I wonder. I know it's applicable, and we're still doing a lot of that more traditional, if you can call it that, machine learning. Do these techniques and this approach also apply when we're talking about generative AI?
**Dave:** Yes, they do. As I said earlier, even if you're consuming a gen AI service, such as an embedding service from OpenAI, it really helps us the team to understand what's gone into training that service, how it actually performs, and what its failure modes are because any ML service will have some degree of unpredictable behavior or some less-than-perfect performance.
Yes, being able to design products with those failure modes in mind is very important, but they offer a lot of advantages for solving otherwise difficult problems with complex data as well. It's not to say that the failure mode should drive your thinking. Another aspect, and I think we've touched on it a little bit about successful products is that a lot of conversations we're seeing, gen AI is a great trigger.
Really, the right intuition is there that this is a problem that can be solved with AI, but it's not necessarily the most effective technique, the most efficient, or the most architecturally ideal technique to use to solve a particular class of problem. This product development approach of testing and learning teams being able to potentially prototype with gen AI first but then if they identify there's a better solution for a digital product when it goes into production when it moves out of that realm, that you can handhold the solution, so then teams being able to identify the most appropriate traditional ML or AI technique as we might describe it to support that feature in a production environment. It's very important for teams to be able to make that pivot as well.
**David:** On that question of, "Do any of these apply to gen AI?" In addition to what Dave has shared, I think there's a whole swath of things to say about product testing and all of that. To zoom into engineering for a little bit, we were lucky in the timing of this, one of the chapters on automated testing that we were on a project to develop an LLM prototype.
We were actually able to TDD or apply test-driven development in the prompt engineering of one of the LLMs. That was really fun and low-cognitive load to be able to say, "These are the scenarios that I need my LLM to handle or LLM plus my prompts from design to handle and be able to just iteratively refine our prompt design to pass one scenario at a time."
That fast feedback was really good. Then sometimes the stakeholders would say, "Oh, I need to add this new thing," or "Can you make this chatbot more polite or something like that?" The ability to change that prompt and then run a test suite of 10 to 20 tests or scenarios and say, "Oh, everything's still green," that really helped us move really quickly.
I can imagine if somebody one day needs to deprecate GPT-40615 to support a newer version, the ability to just run the whole suite of tests to say, "Yes, it was still as good as before," or "It starts to fail in these scenarios," I think this engineering practice definitely will help those LLM application areas.
**Scott:** I have so many more questions I would like to ask, but we're going to run out of time. In wrapping up, I'd like to give each of you an opportunity to tell me, tell the audience, what is the most important takeaway from your perspective? Dave Colls, let's start with you.
**Dave:** I would say that when it comes to building ML products, there's a role for everybody in a modern digital organization. This book tries to articulate how each person, regardless of their background and experience, can play a role in delivering great ML products.
**Scott:** David Tan, how about you?
**David:** I would say my key takeaway in building effective machine learning teams is just to be able to reflect on your past week. What has worked for you? What hasn't worked? Just to be able to be sensitive to those smells and signs that there may be a problem underneath. For example, if I spend three days manually testing something before I release, I don't like that feeling. It was tedious. Then that's a signal to us that something could be improved. Just to look back at your week as an ML engineer, as a data scientist, what frustrates you? Be it in the product space, user space, engineering space, or data science space, what's annoying you? Then just to seek out other ways or better ways of handling those scenarios.
**Scott:** Ada?
**Ada:** Thinking of a succinct way to answer this, and I'll try my best. I'll start with it's all about the bigger picture. It's all about the problem and the value we're trying to solve and deliver. Our principles and practices in software delivery and engineering is all applicable to this. That is what will help us make ML products successful.
**Scott:** Thank you. I think that was a really good answer. Where can we find the book?
**David:** Yes. We'll add it in the show notes, and you can go to your favorite search engine and type in "Effective Machine Learning Teams." They will bring you to O'Reilly, or you can order on Amazon, Booktopia. We've heard from a publisher that in North America, it's also in Target and Barnes & Noble. That's, to me, very cool. Yes, you can find it in your nearest search engine.
**Scott:** There's a hard copy floating around the office, I noticed, which was very exciting, I'm sure, to have it in your hands.
**David:** Yes. That was courtesy of Dave for the Melbourne office.
**Ken:** Well, and for what it's worth, I can tell you that the technology section in the Barnes & Noble's here in North America is very small. That is high flattery for you as authors.
**Ada:** We hear you.
**Scott:** You need to do a tour now, obviously.
**Ada:** I'll be up for it.
**Scott:** Okay, thanks. Thanks, everybody. This has been a great conversation. I hope everyone will go and read the book and consider applying some of these techniques in their own work.
**Dave:** Yes. Thank you so much, Scott and Ken.
**Ada:** Thank you.
**David:** Thank you, everyone. Thanks, Scott and Ken.
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
## Start your software engineering transformation
[ Learn more ](https://www.thoughtworks.com/en-th/what-we-do/software-engineering)
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