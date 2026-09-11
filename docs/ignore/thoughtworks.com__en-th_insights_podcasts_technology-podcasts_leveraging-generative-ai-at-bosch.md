<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/leveraging-generative-ai-at-bosch | Title: Leveraging generative AI at Bosch | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Leveraging generative AI at Bosch 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons  and Birgitta Böckeler | Podcast guest  Andreas Nauerz
December 14, 2023 | 43 min 16 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/leveraging-generative-ai-at-bosch#Transcript)
Listen on these platforms
## Brief summary
Generative AI has, unsurprisingly, been a major topic of conversation within Thoughtworks in 2023. However, as enjoyable as it is to get sucked into discussions about the reality, the risks and the benefits of this new technology, what's really interesting — and most important — is understanding how organizations can actually leverage generative AI in a way that's both safe and effective. 
For this episode of the Technology Podcast, Rebecca Parsons and Birgitta Böckeler spoke to Andreas Nauerz, CTO and Executive Vice President of Bosch Digital, who explained how he and his team have been thinking about generative AI and exploring the ways it can be leveraged across a huge multinational organization. He discusses where generative AI has already been effective, managing risk and the challenges of bring a large organization with you as you seek to implement something new. 
## Episode transcript
**Rebecca Parsons:** Hello, everyone. My name is Rebecca Parsons. I'm one of your co-hosts for the Thoughtworks Technology podcast, and I'm here today with my colleague Birgitta. 
**Birgitta Böckeler:** Hi, everybody, I'm Birgitta Böckeler. I'm a Technical Principal with Thoughtworks in Berlin, Germany.
**Rebecca:** We are joined today by Andreas, who's the CTO and Executive Vice President of Bosch Digital. Andreas, can you tell us a little bit about yourself and about Bosch?
**Andreas Nauerz:** Yes, absolutely. First of all, thanks for having me. Maybe, I'll tell you a little bit about my short history in Bosch because it's quite untypical. Normally, when you're talking to someone being the CTO or EVP of Bosch, they all have this typical Bosch leader, like being 20 years with Bosch. I can't offer you that. I joined Bosch in 2019 at corporate research and then, one and a half years later, I was then appointed the CEO and CTO of Bosch.IO, where we have been looking into Bosch AIoT strategy and where we developed AIoT and IoT-related products and solutions.
Then exactly as you have said, at the beginning of this year, I became the CTO of Bosch Digital, which is, at least as we call it, which is the digital powerhouse of the Bosch Group on its mission to drive forward the digital transformation. Before I joined Bosch, I worked for different software companies worldwide. I think the longest time for IBM, and there as a program director and a senior technical staff member primarily responsible for IBM serverless compute solutions. Yes, I studied computer science, by the way. Yes, that's me.
**Birgitta:** I'm from Germany as you are, so I am aware of Bosch who are based in Stuttgart but can you tell the audience who are not immediately aware of what Bosch does, a little bit more about the many things that you do?
**Andreas:** Oh, yes, and that was really hard for me when I joined. It's not an IT company, it's a company that is so diverse. I would call it a conglomerate if that translates well. We do a lot of crazy things and that makes life exciting. What is Bosch? The Bosch Group is an engineering and technology company. It's headquartered in Stuttgart, Germany — the Southwest — close to the Black Forest, some might know that, and close to Lake Constance, which is, in summer, wonderful.
Our strategic objective is to facilitate connected living with products and solutions, exploiting the power of different technologies like IoT, AI, and so forth. Our overarching goal is to improve the quality of life worldwide with products and services that are innovative and spark enthusiasm. And that's why we have our slogan: “We create technology that is invented for life.” This is our mission, right?
We operate in multiple sectors, so now we come to this conglomerate aspect. We are active in mobility, mobility solutions, industrial technologies, consumer goods. That's where most people know us from, right? You may have seen a fridge or a washing machine or whatever, or a trailer from Bosch already, and we are also active in energy and building technology. A lot of different things. And this broad spectrum is what, for me at least, what makes Bosch super exciting because every single day you can learn something new regarding to one of these sectors that I've just mentioned.
Of course, all these sectors and business rely more and more on IT and digital technologies, especially on software. I can bring in my background to drive all these different topics forward, especially now being in Bosch Digital when just the world of Bosch Digital, so that's an 11,000 people organization on acting around the globe. As I've said, we are on our mission to help the rest of the Bosch universe to drive forward the digital transformation. We develop and operate products, services and solutions so that all our internal customers can run their existing business and build up new digital business all based on our digital solutions.
Our portfolio ranges from infrastructure, workplace solutions, software development tooling so that the rest of the Bosch group can develop the software they need in their domain, even consulting services and products that we are trying to develop.
**Rebecca:** What we wanted to talk about today, actually, there is, of course, so much hype around generative AI, and we've got the apocalyptic vision of the end of the universe or the end of the earth as we know it, to, "Oh nobody's going to have to work anymore because everything's going to be AI and everything in between". What we'd like to talk about here is let's ground that hype in an organization that has the breadth of offerings and requirements and use cases that Bosch does.
Tell us a little bit about how this whole Gen AI revolution is playing out. Where are you looking at using it? Why might those use cases make sense? How are you approaching it? I know that that's broad, but let's just start with the basics of where you're looking at applying it now.
**Andreas:** You phrased it absolutely correctly. Due to the fact that we are such a big conglomerate, we have many, many different use cases that we have to find a mechanism, what to really go after and what not, right? Maybe I start with a short description, how we identify the use cases we want to pursue. We go, I would call it a four-step approach, with the team that we have built, and by the way, we have built a team or set up a team that is cross-business units. That's something that Bosch is not doing all day or every day.
We have to break the silos between these different business units that we have, I would call it, a center of excellence has been set up. This team, comprised of people that come from corporate research, comprised of people that come from Bosch Digital, they usually follow by working together with our business units, our internal business units, which are our customers, they follow a four-step approach I would call it.
First, we talk to all of them and we collect all the use cases, all the ideas that they have, no matter if I talk to the power tools guys, or if I talk to the consumer goods people, we collect all the use cases. Then we analyze all these use cases. Because what we want to do is we want to go for those solutions that seem to be low effort, but cause max impact for a plurality of our customers.
If there's one use case where we say, "Oh, if we build that, and if we build it in a very generic way, then we can help not only the what customers, not only the guys that are working on fridges, we can help a plurality of our internal customers at once." We cause max impact with low effort, so to say. Once we have that clear, we cluster these things a little bit because when you talk to all these customers, what you find out very quickly is the needs they have, even though they are in different domains, there are clusters of things that they all need, and that is something that you can then build a generic foundation for to then implement their specific needs that they have on top.
**Birgitta:** As a consultant, I now have to bring up the word synergies, yes? You're looking for synergies across your business units. [laughs]
**Andreas:** Yes, that was the word I've been looking for. Exactly, that's what we want to do. We listen carefully, we try to detect the pattern that we see, and then once we have seen the pattern, reassess what is causing max impact and what is leading to max synergies to make sure that we help this organization the best way we can.
Then, of course, we check the technical feasibilities, or some of the use cases, we might find out, "Oh, actually generative AI is not the right thing to use here". We can talk about that maybe later because, currently, I also see this trend or more problem that everybody's trying to solve the traditional problems now with generative AI, that's something I would not recommend to do. There's this third step that we do. We look at all these use cases and then we try to check for technical feasibility, and if it really makes sense to tackle the problem with Gen AI.
Last but not least, we also have to do, I would call it a legal status check. We also check, if we do that with generative AI, that we do not violate laws, that we take care of data protection regulations, and that we do not harm individuals' personal rights, something like that. This is how we tackle the problem. Use case collection, clustering, assessing the impact, making sure that generative AI is the right tool to be used, and then checking that we do not violate any rules that we better do not violate—four steps.
There are also four clusters. We have been asking for, "What are you using it for?" I keep it first on a more abstract level, and if you want, we can go into more detail what concretely we are doing. The four clusters, and feel free to ask in between, of course. The first one is what I would call the search and summarization scenario. This is all about searching or allowing people to search in natural language, to analyze and understand large volumes of data in order to ease and fasten and consolidate access to information. That could be the headline for this.
In this scenario, generative AI enhances enterprise search and data summarization by allowing to search a natural language and keywords. We all probably have this internal search engine in our companies. I'm not sure how yours works, but the most internal search engines that I've seen are not the best ones I've ever seen on this planet earth. I think many people know what I mean.
Now we have a new tool here where we do not have to come up with the right keywords, and even better, we are not being presented with this list of links that we all have to open in a new tab and see if the information behind is really what we are looking for. Now, we get not only the opportunity to ask our question in natural language, we also get a concise summary of relevant information rather than that list of links that you have to go through manually and that makes it so much easier and faster to extract valuable insights and to make, at the end, an informed decision. That's the first cluster.
**Birgitta:** Maybe a question about that first cluster. It's a very common use case that we also see with a lot of our clients. What are your experiences so far with the correctness of results and also data quality? I think a lot of people are almost having this hope, there's this magical data lake now of unstructured information that we can ask questions about, but the data quality still matters. What are your first experiences there about preparing your data in a way that gives you added value?
**Andreas:** That's a good one. I want to be honest here. We have just started that, and due to that, I think it's more like a gut feeling what I'm answering now. I think people are, with the experiments we have been doing, quite okay, but we also see and not only we, we see some of the problems that are quite surprising. I'm not sure if you've read about that Stanford paper recently. That's very interesting. You see, for example, even in systems like ChatGPT, that they can even derogate, if that is the right English term. You see that, even so, an answer has been correct back in March, for example, if you ask the system again, it's wrong now because they use reinforcement learning and stuff like that. That means the system changes its behavior over time based on the feedback it's getting from the users.
In March, maybe there was a different population, only a small group experimenting with this technology. Now it's the entire world. I'm bored. I do not want to touch on the IQ of all people on this planet Earth, but obviously, systems are, for whatever reason, derogating to some extent because they get the wrong feedback.
**Birgitta:** Yes, or also not necessarily wrong feedback, but an answer might be useful to one person and not to another person, the same kind of answer. Then, was this useful to you, thumbs up or down? For one person might be thumbs up, the other person wanted something else. Correctness is also subjective sometimes. [chuckles]
**Andreas:** Absolutely. That's a very valuable addition that you just made. I think the important thing that you need to consider when using generative AI and that links a little bit to what I was already teasering a couple of minutes ago, it's a very unstable technology.
Due to the fact that it's using reinforcement learning, if you need something-- let's say you are working on a use case that is safety critical, I wouldn't use that because it's an instable technology and you might run into problems that you do not want to have and that then you better use one of the more traditional concepts that give you more security or certainty about the results to expect.
The second cluster I would call it the chat voice bot scenario. This is about adding natural language to chats to facilitate human-like understanding and responding in natural language to improve interactions. In this scenario, generative AI is enhancing chat and voice bots by improving the natural language processing abilities of these systems so that they better understand and respond to consumer or customer inquiries and requests.
It could be internal employees, so maybe we equip our internal IT support with such technology, but it could also be that we apply this in our service centers, for example, where our external customers are calling. This is, of course, leading to a better user experience, no matter if it's an associate or an external customer, and to making people way more happy. This is something we are really looking at at the moment. We are looking at how can we improve our internal IT ticketing system. We are looking at our customer supports and their agents, or how we can be a system.
It's actually funny. If you look at how our service centers work, some people think there's only a human sitting there and that human gets the call coming in. That's not the case, actually. That's nothing new, but now we have a new technology to make it even better. The voice is being split in two parts. Of course, the person you're calling hears what you're saying, but at the same time, there is an AI analyzing in real time what you're saying.
Of course, now you can put a model behind a large language model that has been trained on all the manuals, on all the problem tickets that you had before. While they are talking to each other, the agent sitting there gets in context in real-time hints what the problem may actually be. That's an assisting technology. That's something very concrete that we are currently-- not only we, you find that all over the internet. It's a very, very common use case currently, and that'll be very, very helpful.
**Rebecca:** The nice thing too about using these capabilities, one of the real frustrations with many of those voice systems as well is, no, you can't use the word speak to a representative, you need to say, speak to the pharmacy, or, what is exactly the word that is being looked for, and yet with these large language models, I can quite naturally say, I want to speak to a person, and they'll route me to a person, because whether they want you to say pharmacist or representative or whatever, all of those things can now-- It becomes much more natural to be able to correspond with these systems. Even if that's all you use it for is to improve that interface, from a customer service perspective, that makes a huge difference to--
**Birgitta:** Makes it fuzzier.
**Andreas:** Absolutely. I think we all remember these funny systems where they are telling you, if you want to X, Y, Z, please say one. If you want to do A, B, C, please say two. Oh, I didn't understand. Can you please repeat? This is a story of the past then, right?
**Birgitta:** Yes.
**Andreas:** The third cluster, and now we get more into the creation of content, I would call it. I think this is very powerful, and very powerful, not only what you may think of immediately like engineering and software development, but channel the content creation. I think using generative AI to support content creators, like for example, marketing specialists by assisting with the creation of high quality and maybe even personalized content at scale, this is a super powerful thing to improve efficiency and to reduce costs while allowing the creators that originally have been responsible for doing so can focus more on the strategic tasks.
One project where we see this currently is, we have a little tool currently in the PLC where we generate our texts for websites in different languages and so people are being relieved from doing that manually. We can do that in 47 languages. We can just let it be generated for what previously people have been doing by hand. For example, if you are in HR-- we are discussing with our HR colleagues, if you want to generate a job offer, a job advert, why do you want to write that by hand any longer? Why do you want to write that manually? Let it be generated by generative AI.
Of course, you need to be careful because we know there might be hallucinations in and also the system has not an ethical understanding. Be careful, there might be, I don't know, violent language, harmful language, whatsoever, in there. Please have a human being have a review on that. Still, it's better to start on this 80% as a basis than writing something on your own from scratch. That's the third cluster, the content creation cluster. Marketing is just one example, right?
**Rebecca:** Yes. In fact, one of our colleagues, I was talking to him about how he's used it for content creation. One advantage of course is you immediately get past the terror of the blank sheet of paper because you've at least got something and it's always easier to edit something that exists than it is to create from the whole cloth. What he also told me was there was one thing that he just never liked anything, and he tried two or three different prompts and never liked anything that he got back, but he got so irritated with the fact that why can't this model come up with something sensible that that got him over the terror of the blank sheet of paper and motivated him to go write something.
I do think that that's interesting but there are so many stories of when people haven't taken your caution into account. Please keep the human in the loop! We have lawyers being fined by judges because they put together case law that chatGPT made up out of whole cloth and nobody checked it, nobody went back to say, oh, does this case actually exist?
I do think, even as the technology gets better, we're still going to need the human in the loop for a lot of that, just to make sure that the tone is right. Although I do know of somebody, and I thought this was an interesting use case as well. He writes a lot of blogs. What he did was he instantiated one of the large language models with his writings. Now it basically answers in the same way that this individual would answer, and of course, that can apply to organizations as well, where you can get that tone of voice, if you will, by saying hone in on this aspect of the corpus.
**Andreas:** That's an interesting addition, to make sure that you fine-tune the model to make it even harder to distinguish that this is coming from an AI. It's not only coming from human, but it even sounds like you. It starts to mimic you.
**Birgitta:** I've been using GitHub Copilot actually for writing because it's like I get suggestions as I type. None of the other tools for writing assistance do that at the moment, at least not that I know of. I've been using it, for example, when I wrote some of the blips for the last technology radar, just getting suggestions and then editing always and double checking, of course.
**Andreas:** Wow, you're saying you're not using it for coding, you're using it for writing normal text?
**Birgitta:** Yes, for both. In a markdown file. For articles, blips, and so on.
**Andreas:** Wonderful. I liked the saying that Rebecca just made on the terror of the blank sheet. That reminds me so much of when I've been a student and I've been sitting in front of my diploma thesis, there's this blank sheet of paper. I know this feeling very well. Coming to the last cluster, and I think that's something that is very, very known already so probably doesn't need a lot of explanation. This is all about engineering and software development.
It's about automating the creation of documentation, or even code, or writing tools, or developing tools that help to detect box or security vulnerabilities that allows developers to focus on the higher level design and on problem-solving tasks, and accelerates the entire development process. Of course, we being Bosch Digital and we, as I've said before, in all our sectors that we are active in relying more and more on software, that's a very, very powerful thing.
We all know these studies that are being out there. There's this one study from GitHub that has been quoted very often saying, hey, if you use GitHub Copilot, you can increase our productivity I think by 55%. That's the number they've been using. What I found very funny is, when you look at a study in more detail, what they measured is 55% on productivity increase, but when they ask people what they think how more productive they were, they said a number that was way beyond that—80% or 88%, which shows that people are not only more productive they are also happier because they do not need to waste so much time searching for the information that they need to do the actual job they are supposed to do. That is something that I found way more interesting when reading through the study.
**Birgitta:** By the way, this 55% that was in their study that they did, there was one task they gave to people which was to create an HTTP server in JavaScript, and this is what that is based on as one example. It depends on the situation, like how much faster you get, or on lots of factors.
**Andreas:** Yes, thanks for adding that, Birgitta. I just want to make a similar comment. It's just that there are not so many studies out there, and I would be a little bit careful with this 55%. If you start Googling around and trying to find a number for a real-world project that is running since a while already, with really a diverse set of tasks and not this one example like you've just explained, you don't find a lot. We have been looking for that the last few weeks. Let's see if we do another podcast in two years, maybe we will know a little bit more what do we hear about that you can expect actually is right.
**Birgitta:** We just talked a lot about exploring the problem space, like collecting the use cases, and what types of use cases are there and so on. What about the solution? How do you, at Bosch, approach that? Buy versus build, how to roll things out, what are your experiences there in the space at this point?
**Andreas:** I think I touched a little bit on that. We have the center of excellence, I called it. We really have this interdisciplinary staff team where people from legal, we have people from purchasing but also the IT guys are in.
We bring together people with the digital knowledge and that are experts in fields of AI and software development with the people from the business units that are our customers that have the domain knowledge, they know everything about the fridges, the cars and so forth. Then we bring them together and the to-do things.
First we as Bosch Digital provide the right technology. That can go into two directions. It can be that we onboard tooling that they need. For example, maybe it's a very simple problem — they want to use generative AI to generate video material, for example. Maybe we then just onboard a tool like Synthesia, for example, because this is able to do that. Then, of course, we need Purchasing and Legal to see how to do that the best possible way.
We try to do that in a very coordinated way. What we do not want to end up with is 1 million tools for the very same problem. We do not want to end up with a slew of tools for the same use case. That's the one thing that could happen if we just onboard tools. The second thing that can happen is that we provide them with a technology stack, where we, in-house, in our own data center provide the entire stack that you need maybe up to the point where we have our own foundation model or large language model or whatsoever.
This is not the standard case. This is something we usually do. If the data we need to train is IP-sensitive, then we go that path. If not, we usually use the technology being out there being provided by the big players. At the very end, so onboarding tooling, providing the right tech stack be it on the public cloud or be it in a private cloud environment, and the last thing that we do is we assist them during development. We really have our people with their software experience coming in, and jointly with the domain experts, we really coach the problem and try to come jointly to a solution. That's how we work.
**Rebecca:** We've talked a lot about the interdisciplinary, cross-functional nature of the teams, but how is this all being received within Bosch? Are people excited to use it because it's going to make their job easier? Are they scared of it? What's your sense, so far, in how the people within your organization are responding to the potential of GenAI?
**Andreas:** We see a lot of excitement. We see that the interest is really super high. Almost everybody in all the different parts of the company is starting to do something. Even trying to take over or claim ownership for the topic, even that happens here and there. That has a risk, of course. That has the risk of doing a lot of duplicate work, and even things a little bit quite risky, because it's being done maybe without Purchasing or Legal being part of what is going on.
What we think or what I think is very important, and that people are enthusiastic and want to try things out it's something I like very much but still, we need to be careful because of all the risks that are associated with the technology, like the legal risks, the ethical risks, the commercial risks, and all of that. Some governance is being required to get everything that is currently happening under control.
The point here is that we need to find a good middle pass so that you allow individuals to have some freedom, while at the same time, not ending up with a slew of developments and with a lot of redundant work and with a lot of duplicate work being done. Then the risk is that things are reinvented over, over again leading to massive inefficiencies. The goal must be really to allow for a reasonable degree of, I would say standardization and homogenization, and especially reuse without ignoring the individual needs of different units and forcing them into borders. Maybe that just describes it.
**Birgitta:** I also think this is a space that requires a lot of exploration, and so you also need to keep the barrier to experimentation low so that you can actually get people to play around with this in their context, but in a safe way and in a way that doesn't create too much waste. The typical challenge of innovation and experimentation in a good way.
**Andreas:** Absolutely. Now you're touching on what I wanted to mention as well. The Center of Excellence has, on the one-hand side, the task they already explained. Helping all our business units to develop the solutions that are Gen AI-powered, but they also have some additional tasks. One is about really identifying the risks, really identifying the potential mitigation options, and really informing the rest of the organization, so there's also the educational task behind, about these risks and providing the rest of the organization also with training material and with guardrails and giving them, or providing them with a kind of certainty and security what to do and what not to do.
This is something very, very important because, especially we at Bosch, we are 420,000 people, I think, but not all of the 420,000 people are IT experts. We need to make sure that everybody being part of our organization understands the potential, but also the risks, and is being assisted a little bit and not left alone to understand what to do and what not to do. We are really working hard on developing training material. We do a lot of publishing of articles in our internet.
We have so-called sofa sessions, which is our internal YouTube where I'm sitting on the sofa, that's why it's called sofa session, and try to explain things to everybody being part of our Bosch family. That also helps to address something else, namely fears.
Even so, there are people that are quite enthusiastic, and I think that's maturity. There are also people having fears. I think most of them, they have understood that this year is not about the launch of Skynet, and it's not about achieving technical singularity, but some are, for example, worried about, "Is this replacing my job?" We know it's affecting more than just IT. We have talked about the examples. That it's affecting people in marketing, it's affecting people in HR.
I think the important message, and that's also part of this educational thing that we are after, is generative AI should be seen as an enabling technology or commending human capabilities rather than displacing them. We have always experienced human history. We have always seen new technologies automating tasks to free up time for other higher-value mental work, let's call it like this. What is key, in my opinion, is that people learn to exploit the power of this technology in a meaningful and responsible way because if you don't do this, you will fall behind from a competition point of view.
The analogy I use very often is think of two doctors-- when I'm asked this question. There might be one doctor that is not using, in the future, anything related to AI, and it might be one that is using this technology. The second one might be able to find the best diagnosis and the best treatment much quicker because he can use the technology and search through all these databases the way I've described it with our internal search a couple of minutes back. He will be more competitive. He has an advantage, a competitive advantage over the first doctor.
It's essential, if you want to survive with your business, that you really learn how to deal with this technology in a responsible way. That means, for Bosch, for example, we are working on our AI codex where we really define the rules of the game, what to do, what not to do. We even provide our employees with protection mechanisms.
We have a tool that is called AI Shield that really checks the prompt before it's being routed to an external system, to see if we really want to let that go out. Not to control our employees, but to protect them from ending up with a case that we have all seen on the press from another company a couple of months back where some engineers thought it's a good idea to have IP-sensitive data in the prompt. That's things that we do.
We see that even on the political level currently. Out of Brussels, we see all these thoughts around the AI Act being driven forward because we all see that there are risks associated, for instance.
**Rebecca:** At the beginning, I mentioned the range of opinions between the world ends tomorrow and the tech utopian dream. Where do you personally sit on that? You've mentioned that you don't think Skynet's going to happen tomorrow. What you just said tells me that you are seeing this as a valuable way that we can enhance the human experience as opposed to degrade it. Is that a fair characterization?
**Andreas:** Yes, absolutely. If we use it responsibly and if we use it right. I already touched on that a couple of minutes back. They are also use cases where I really would encourage people to not use it. For example, if you think of a traditional classification task, there you wouldn't use generative AI, or when you think of non-generative task, where it's not about generating new content based on existing one, there you better use our reinforcement learning or traditional machine learning. Generative models do not make sense.
Maybe you want to look at these things from a cost point of view. Training these models and running them, at the moment, this requires a lot of computational power, so it's quite expensive. If you want to have real-time or low-latency applications, well then again, it's probably better to use one of the more traditional technologies. Maybe you don't have a lot of data.
Generative AI requires a lot of data. Look at ChatGPT and large language models, it has been drained on the entire text corpus of the internet, actually. If you don't have enough data, you can't use this technology.
We already touched on things like trading instability. The system can change the behavior, and if it's changing behavior, it's also not suited for safety-critical systems. Still, I think generative AI will continue to accelerate in the context and in the scenarios and in the examples that we touched on a couple of minutes back. I think it'll accelerate even more because I see what I call the democratization of AI will continue.
What do I mean by that? Democratization of AI, for me, refers to that the AI technology becomes accessible and affordable to a wide range of people, not necessarily being experts. This happens because there's a simplification of AI tooling and everything you need. A couple of years back, you really needed to know everything about the algorithms behind and so forth. Meanwhile, you can download a model from Hugging Face. You can deploy it on some AI platform. That's it.
The second thing is, which will even make it accelerate is, I'm very convinced that the compute power being required to train and run will significantly decrease over the next years. Then even more and more open source models will come up, which currently is, due to the associated cost, not happening so much. I think it will be interesting, and probably we won't find the answer to that one today, is I'm very curious what will happen the next months and years when looking at this ongoing war between the really large channel purpose and the specialized small models. Who will win? That's a very interesting question, in my opinion. Let's see in one or two years from now.
The second thing that I'm very convinced of here, which also needs to be proven, is from an end-user perspective, I am totally convinced that generative AI will change IT systems as we know them today. I'm totally convinced that every system or tool will come with a natural language interface that allows you to verbally describe your problem or the task to be performed. This is what we already see in GitHub Copilot, but I'm talking about every tool.
Think of Adobe Photoshop. You will just write, "Can you please edit the photo that I've currently loaded like the following? Can you please exchange the sky and make it a blue sky instead of the gray sky I'm currently seeing?" The tool will understand what you're talking about and will do it. This will happen when you use PowerPoint. You just write some text and say, "Can you create me some slides that deal with the following topic?" Even though it might not be perfect, you don't have the terror of the blank sheet as you call it before. You have something to start with and that will help.
These trends, I think, will continue. The democratization, the less compute power being needed will accelerate this technology, and we will see this war between the large language models, the small ones, and we will see how, at the very end, this will cause a huge change for how IT systems work and how they are being made accessible for non-IT experts by using this technology.
**Birgitta:** This democratization and having this natural language interface and all applications, that will mean great power for the users. With great power, comes great responsibility, right? Technology is not just happening to us, we can decide as users and as people how we're going to put up guardrails and what we're using it for and whatnot. We'll have to see how well we will deal with this responsibility for the good effects or the bad ones or somewhere in between.
**Andreas:** Yes, absolutely. What I think is not a good idea because this has never worked out in human history is this-- I'm not sure what you think about that but this idea of stop research, right? Let's not continue with that. Someone will do it. It's super naive, right? When I've been asked what I think about that, I usually use an analogy saying, it's like the Tour de France, like the big cycling event taking place in France every year. Everybody uses stuff he or she not yet should better not use because they're all afraid somebody will use it so I also need to use it right because otherwise, I'm not competitive anymore.
The same thinking will probably happen when you look at this technology. Somebody will do it because somebody will think "If I don't do it, the others may do it so I better do it. Maybe I do it in my garage. Nobody finding out." I think it's very naive to say, "Okay, let's better stop research on that until we exactly know how it works, how we can control it, and for what is allowed to be used or not to be used." This is the idea I personally find very naive.
**Rebecca:** Well, that answers the next question I was going to ask you, which was what your position on that is, so thank you. Well, Andreas, this has been a fascinating conversation. It's great to hear how this is actually playing out with people trying to run a business and take advantage of this technology. Thank you so much for joining us today. We'll make a note to come back in a year or so and say, "Okay, how did these things turn out?" Because I do think we are going to see a lot of advances.
We're going to see a lot of uses that we haven't really even thought of yet because the barrier to interacting with this AI is so low that democratization, I think, is going to be a source of tremendous innovation as people who are not traditional technologists, traditional computer scientists, are looking at this technology and, "I would see. This is what I can do with it." Thank you, Andreas. Thank you, Birgitta. I hope our audience has enjoyed this exploration of generative AI within a context.
**Andreas:** Thanks a lot for the invitation.
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
[ Explore Tech Radar ](https://www.thoughtworks.com/en-th/radar)