<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/looking-key-themes-across-technology-2023 | Title: Looking back at key themes across technology in 2023 | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Looking back at key themes across technology in 2023 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Rebecca Parsons  | Podcast guest  Scott Shaw and Erik Doernenberg
December 28, 2023 | 36 min 43 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/looking-key-themes-across-technology-2023#Transcript)
## Brief summary
With each edition of the Thoughtworks Technology Radar, we identify a number of key themes that we see as significant in the industry. In the most recent edition — volume 29, published in September — we picked out AI-assisted software development, the challenges of measuring productivity, the rapid growth of LLMs and remote delivery workarounds beginning to mature in a post-pandemic world.
For this, the final Technology Podcast episode of 2023, a few members of the team involved in putting the Technology Radar together — Neal Ford, Rebecca Parsons, Scott Shaw and Erik Doernenberg — got together to discuss these themes in more detail and offer their perspectives. As we leave the year behind, it's a great way to review some of the key issues and stories that shaped the way the world builds software.
## Episode transcript
**Neal:** Hello, everyone, and welcome to the Thoughtworks Technology Radar. I am one of your regular guests, Neal Ford, and I'm joined by another regular co-host today, Rebecca Parsons.
**Rebecca:** Hello, everybody.
**Neal:** We're joined today by two of the members of the Doppler group who helped to put together the Thoughtworks Technology Radar, the report that we put together twice a year that's crowdsourced from our projects. One voice that you will definitely be familiar with because he's also one of our podcast hosts, but he's sitting in the much more comfy guest chair today, we're joined by Scott Shaw, and then Erik Doernenburg. I'll let each of them introduce themselves.
**Scott:** Hi. I'm Scott Shaw. Yes. Thanks for driving today, Neal. I'm going to be the guest. You can ask me questions. I'm in Australia, and I sometimes host this podcast as well.
**Erik:** Hi, I'm Erik. I'm based in Hamburg, Germany, in Europe. I'm normally a guest on this podcast, and I'm really happy to be here today.
**Neal:** Today, we are talking about the Thoughtworks Technology Radar. As I mentioned, we put out twice a year, and it's very much crowdsourced from things that have worked well on our projects. That's very much generated from real project work. The only thing that we really generate as a group are the themes. As we are discussing all of the various things to make it on our Radar over the course of the week, at the end of the week, we try to take a step back and say, did we see any sort of connective tissue between all the individual, very discreet blips on our Radar? Is there something that holistically ties them together?
That's what leads to the themes. We generally have three to five themes on each Radar. What we're going to do today is talk a little bit about the themes on our most recent Radar, which was Volume 29, which came out in September 2023, and talk a little deeper about each one and a little bit about how that theme came about and some of the discussions around it. We can start with AI-assisted software development, which was our first theme, and definitely, probably the biggest topic of conversation for the whole week this time.
**Scott:** Yes, we get asked about it a lot. This is obviously squarely in what we do and the value that we bring to our customers. Of course, our customers ask us what our experience is all the time. I think we do have some experiences to share now. There's been quite a bit of experimentation that's taken place.
I think one thing that I've noticed is that people go immediately to coding assistants. There were a few coding assistants on The Radar, Copilot being by far the most best known and widely used, but there are a few others on there. There are some open-source ones too, which I think is really interesting. There's some open-source coding models. We find that people may be overly optimistic in the productivity gains. That's another word we should talk about later, but the efficiency gains that they might get from using coding assistants alone.
**Erik:** Yes, I was personally really surprised. I'd certainly played with Copilot and I'd seen a lot of the hype around it, and I was surprised to see some of the other tools. While I have not personally used them, in the group when we discussed them, it became clear that these are really serious alternatives to consider. Some of them really having areas in which they work better than Copilot, so definitely worth checking out.
As Scott said already, open source was interesting for me also to see that there are. They're not really foundational models, but there are pieces that allow you to string together tools. What was also maybe not a surprise, but I didn't know what would happen, but something to do with security in that space already again. Of course, the moment you introduce new technologies, there is always the possibility to exploit it in a way that was unintended by the authors and just taking old patterns. The one that we had then in the end highlighted on The Radar are these hallucinated dependencies.
Basically, what is happening, I guess everybody's familiar with the idea of the large language models making up things with great confidence. Of course, if you're generating code, almost all the code you generate today includes other packages that you depend on. If you get that wrong, you're trying to include or import a package that doesn't exist. Here it is exactly where the people, the malicious actors spotted an opportunity. They thought, if this doesn't exist, but it is commonly recommended by an LLM, why don't I register that import?
Then, of course, the bunch of developers would use it. The hallucinated package is no longer hallucinated because now it does exist. The hackers have found a new way, the hackers in the malicious sense, have found a new way of actually getting onto the developer machines. It was, as far as we were concerned, only one of them, but it was really interesting to see how that wave of new tools immediately brought a new attack vector.
**Neal:** It's even worse than that because of the way the LLMs work, if that hallucination starts getting pulled into a lot of projects, it'll start being not just a hallucinated dependency, but a real dependency that shows up all over the place and grows sort of organically. It's always fascinating the second-order effect of some of these things that look beneficial but then you start following implications and it goes to interesting places.
**Scott:** One of the things that was interesting to me is most of us, because we manage The Radar while we're writing it in Git, a lot of us use VS Code to write Markdown when we're writing The Radar. Unbeknownst to me, Birgitta had enabled the GitHub Copilot for Markdown while we were doing that writing. I all of a sudden started getting paragraphs of text suggested to me by Copilot. Sometimes the next sentence was uncannily accurate in what I was thinking about writing. I have to admit to having accepted those once they were inspected.
**Erik:** Yes, what I noticed was, for me, my workflow is often, I don't know whether everybody on the podcast knows this, but we have meeting minutes from The Radar meeting, from the Doppler meeting captured. I usually paste them into the Markdown file to remind myself of what was discussed in the session when I write the blip. Then further, of course, helped the large language model because now I was providing context, almost in a rack style. I was providing content about what I was going to write, and in that case, exactly as Scott described, I never took a single sentence entirely that was suggested to me, but I did find it, even for writing text, a helpful tool in that regard then.
**Neal:** It's a great way to solve the blank canvas problem in writing because some people hate starting something but love revising it. Even if it's not great, it's a starting place and you can start revising it towards something that's much better.
**Scott:** It also produced paragraphs of gibberish half the time, but the next sentence was often really good.
**Erik:** Yes. One last thing I remember from the session that also came up is that we also immediately saw a blurring of different tool categories. We had tools like Sourcegraph and Kodi on The Radar before which were analyzing code, and we were now seeing but also at this stage speculating how these two categories would not necessarily merge but how they would learn from each other. That is, I guess, something that we will see when we, in a few months' time, build the next Technology Radar. I'm looking forward to that already.
**Rebecca:** I want to comment because I know lots of people are very interested in how the sausage gets made. One of the things that we had to do just because of the sheer volume of Gen AI-related blips was we used a separate way of visualizing them and came up with broader categories that allowed us to hone in on specific things like the coding models or other tools supporting different aspects of the software development, software delivery lifecycle. That helped us simply manage just the volume of the blips that we were dealing with.
This is something that we have not experienced in the entire history of The Radar. Even when we've had a lot of blips, because they were just so dispersed, we didn't need something like this. We did actually separate out all of these blips and used a different process to go through and winnow them down, which is a big part of what we have to do at The Radar meeting, is just decrease the number of blips.
**Neal:** Famously, on our Radar, one of the most chaotic periods that a lot of us lived through was the JavaScript explosion and how much chaos there was. In fact, we had a theme many years ago that the JavaScript ecosystem settles down to merely chaotic. We've never seen so much, and at least for me, it was extremely beneficial to take the vast number of blips we had and do some extra categorization and sub-categorization to understand how they related to one another because it's easy just to lump them all into AI. They're very different things, different levels of abstraction.
In fact, that's a nice lead-in to one of our other themes, which was about a specific part of that categorization that we did, which are LLMs or the large language models themselves. Another one of our themes was a large number of LLMs which talk about the use of the big public ones but also the use of people building their own for a variety of reasons.
**Erik:** Are they guestimates, experimentation? Because that is what it was in the one year that OpenAI has now published GPT, or ChatGPT I should better say. That amount of experimentation also then followed with the release of Facebook's LLaMA and so on that came so quickly that that resulted in the amount of blips that Neal was just talking about. LLMs in particular I think really, at the heart of it, caught all the geeks' attention and really invited people to experiment more with the tooling than with actually the solutions. That was something that we also remarked on when we did this.
When we were faced with that large number of different blips, one way of cutting back to a manageable number was really to say, how much is really just people playing around with just wanting to make it work? I think we also discussed some of the variants of LLMs that run on hardware as lightweight as a Raspberry Pi and said, that is maybe interesting from a pure perspective. You do it because you can do it, but this is maybe not-- This is probably the weakest one that is probably the ones that we would not necessarily put on The Radar and would focus on the ones that actually help us solve real problems.
We just managed to get back to a sensible number, but yes, there was a large number, not only of LLMs, but only the related technologies like quantization and so on to actually let the LLMs run on a number of different hardware architectures.
**Scott:** I'm sure we're going to have another crop when we get together in a couple of months to do the next Radar because this is, as with all things LLM, everything we say today is probably going to be invalidated and out of date tomorrow. There is a whole new crop of LLMs now that we're going to have to talk about and assess, which is great.
I think the big well-known models like Anthropics or OpenAI seem to take all of the attention when-- I actually do see there are a number of organizations, particularly those with particularly sensitive information or those who might be in regions where they can't be assured of the sovereignty of their data, that want to do self-hosted models. There are a lot of people asking about self-hosting and using the open-source models.
I was in our Bangalore office last week and sat next to a giant gaming machine that's running a 40-billion parameter LLaMA-2 model on the desk there. It is capable of a lot of things. It's not going to give you the wizardry that from GPT-4, but it solves a lot of problems too.
**Neal:** I think there's an interesting split between the general use or the very general purpose and very surprisingly useful, but also hyper-specific context and training an LLM around a very specific context, either because language is hyper-precise like in a legal or medical realm or in gaming or something like that where you want a narrow way to look at that. That's one interesting aspect. The other interesting aspect is, as technologists, we love to peel back abstraction layers and see how things work. That's, you get into LLMs and then start looking at the individual pieces and how they fit together, which is always fascinating.
**Rebecca:** One of the interesting use cases that I've heard about, and we actually have, internally, a system that will allow you to do this, is you can basically upload a specific document, maybe it's a manual or a tutorial or something, and then you can use the chat interface to query that document. Rather than having to page through or page through on the screen, you simply ask, what is the interface for this function? It will return it to you.
That's one of those very specific contexts where you're using the foundational model as your effectively interface mechanism, but the content itself is very specific to, and this is the document I want you to retrieve from. These are the things I want to know about. From a knowledge management perspective, that can be incredibly powerful.
**Scott:** One of the things that I found amazing was the explosion of vector databases. Retrieval augmented generation, RAG, is probably the most common application that we're building of LLMs. To be able to do your own embeddings, you need a vector database, and there is a huge list of those. Pinecone is one that we called out, but there are a number of others on there. I think it's great that there's a renaissance in that area.
**Neal:** For those of us who are not steeped in the AI acronyms, can you describe a little bit of what a RAG is and retrieval augmented generation, what that means?
**Scott:** I'm not an expert, but we all have to become familiar with these things. Retrieval augmented generation would be where you use some additional information. Whether it's looking something up on the web, but more commonly, you have a corpus of documents that you tokenize and then embed in your own embedding space. Then when you do a query, it's first put into that embedding space, and relevant information, similar information from that embedding space, is used to augment the prompt in the LLM response.
**Neal:** It's a way to refine the results that come out of something to make it more specific and more--
**Scott:** More specific to your documents and to some specific documents that you might be asking questions about, yes.
**Neal:** That's a great example of where all these tools are available for ingestion or at the beginning of the pipeline or the end of the pipeline. We also talked about a bunch of tools that let you do prompt engineering and say prompts and let you tweak them, et cetera. That's the input side, and then you can do things in the output side as well, so a rich ecosystem.
**Erik:** It is also partly my hope as well that we're not going to see that many new LLMs because, in the end, I think the trend-- As a regional CTO, I do talk to a lot of the teams that work at ThoughtWorks, what we're really seeing is that people are moving away because training LLM is expensive and there's still the problem with the LLM making something up even if the right information is in the training data set. What we're actually seeing more is that teams are using these foundational models and then have patterns around it, like ReAct or ReAct prompting and others.
I'm actually curious to see whether there are any new patterns that I haven't heard so far because these two are the ones already listed on this Radar. It's going to be interesting to see whether something else was built on top of it. My hope really is that we've gotten over the first wave where people were like, "Oh, LLMs are cool. Let me do my own LLM." Then they realize, "Ah, I need this really expensive professional NVIDIA card. I don't have that. Let's make it run on a gaming graphic card or let's make it work on a computer that doesn't have a GPU." It was just this tinkering.
I personally love tinkering, but this is not what the Tech Radar really is about. I'm hopeful that we got over that first wave of just trying to replicate, and then, as you said, trying to understand, look under the hood, how did it work? That curiosity is now filled and we can now move on to the next step where we're saying we accept the technology that is there and see what we can build on top of it, what patterns we find, what other technologies we can use, how we can approach this. That, I think, is what we'll be seeing for, I don't know, my prediction is at least a number of issues of volumes of the Technology Radar to come.
**Scott:** I do think we tend to take a North American Eurocentric view of these things and forget that not every region has a ready availability of ChatGPT or the Anthropic model. Some places are compelled to use a self-hosted model or one that's perhaps less known.
**Neal:** Another theme that is sort of very peripherally related to the AI things that we've been talking about up until now is an age-old topic. I have to admit that when these blips first came up on our Radar, my first reaction was to roll my eyes because the theme in question is, how productive is measuring productivity? In fact, our chief scientist, Martin Fowler, in 2003 wrote a part of his blog, Wiki, about how futile it is trying to measure developer productivity because it's this unique combination of creativity, engineering, and there have been all these attempts in the past.
There's this new wave of tools, and I'm usually immediately skeptical, but then as we started digging into them, they actually look more promising because they're trying to measure actual things that touch on productivity, for example, measuring how long a developer can get and stay in a flow state, which is an actual measure of productivity versus some specious metric like lines of code or something like that. There's a bit of a resurgence of tools in this area.
**Scott:** There's been a lot of-- Everywhere I go and I speak at conferences and things, people ask me about the McKinsey article. There was a McKinsey article that said, yes, you can measure developer productivity. That, along with the coding assistance, I think has got people thinking about developer productivity. We prefer to say it's-- efficiency. It's really difficult to measure as you said.
That was one of the first things I did when I joined ThoughtWorks, by the way, was help Martin in trying to analyze our collection of coding samples that we had to see if there was any correlation between what was in there and assessing quality. What we find is that it's really hard to measure. We've tried it over and over again, but what we can do is eliminate waste. Most places that are worried about developer productivity actually have environments that the environments themselves stand as an impediment to developers achieving that state of flow. It's much more productive to look at the system in which the developers operate and start eliminating waste piece by piece.
**Erik:** I would say from a personal perspective as I also work as a developer in ThoughtWorks for a long time, for us, it is okay to be slightly uncomfortable with not knowing, if you could even measure it, the precise gain in productivity we've had. I've personally had numerous conversations about the practice of pair programming, which we follow on many of our engagements. People are then saying, "Oh, there's two people in front of one keyboard. You must be twice as fast," and so on. It was always hard. Again, on that level, you couldn't quantify the productivity gains either way.
Similar things happened a lot. For those of you who remember Java 10 years ago, there used to be two major IDEs, Eclipse and IntelliJ. IntelliJ, of course, is not free. It's commercial software and it's well worth it, I would say, but then, again, we had those questions. If IntelliJ costs X amount of dollars, how much more productive are you? How much time are you saving? Show me the return on investment. I guess in that case, at least, it was so obvious that even a small productivity gain that you couldn't precisely quantify would easily make up for the cost of an IDE.
We're reminded of this, and it is that need in some areas of the business to say, I must absolutely quantify everything, even a creative process that software engineering in the end is in order to think about it in any meaningful way. That is what we are really struggling with. For us, it is not for me, I should say. It's not a contradiction to say, I can tell you that there are benefits of using an AI powered coding assistant, but I cannot tell you whether it's a 10% increase or 20% increase in productivity. It may actually change from one day to another. It will definitely, as I've written about in a blog post, definitely change depending on programming language and the area you're working in.
Again, the question is, how important is it? Would you really make it contingent on knowing precisely what the productivity gain is to actually trust the team of developers to say, "We feel we are more productive. We can work better with that tool"?
**Rebecca:** One of the things that I noticed, particularly in the earlier studies on productivity, was they all focused on speed and completion. Scott said the magic word earlier, which is quality. Only recently have I started to hear people talking about whether or not these AI-assisted tools are, in fact, generating good code, or are they just generating lots of code? I do think that this is going to be something that we need to consider over time, particularly when you think about somebody who is an inexperienced programmer and how they might work with an AI code assistant.
I have heard of studies which showed that more senior developers did get a productivity increase. Less senior developers, in fact, took a hit because if there is, for example, a subtle bug, a more experienced developer is going to spot it relatively quickly. A less experienced developer is going to have to spend time figuring out, why doesn't this thing do what I want it to do? I do think, although I know Erik is quite familiar with the problem of, how do you actually measure code quality? I believe we have to get this into the conversation around the use of these tools as well.
**Erik:** Rebecca, in that case, it's not only the productivity, it is also because we often hear that these tools are good for teaching a language. That is really dangerous because a lot of the examples that are then being used is code on the web. That is example code. One of the classic ones that I've observed multiple times now is, in languages that have exceptions, you do catch an exception. Then normally when you're writing a real piece of software, you know what to do in the case of an exception. In an example, that's often the case that you're not really talking about. You just say, catch exception. The next time you either put a comment, say, should do something, or you say through exception.
I've seen multiple times that a coding assistant was then putting these things in. If it is meant to teach somebody to program, it is actually teaching them quite bad practices in the end.
**Scott:** We have to remember that the length of time that it takes to find or to assess quality has a big impact on how effective and how productive your developers are going to be. Those long feedback cycles is one of the things that we actually can measure and that we know has a direct impact. We want to provide that quality feedback, but we want to provide it in an immediate way while the developer is working instead of having to wait for an environment to get provisioned and for a QA to run some tests and so on. That's one of the things that people can do to actually improve the effectiveness of their developer.
**Erik:** Maybe, and Rebecca made an interesting comment, when we bumped into each other at our XConf conference. Because he knows that I, 10 years ago or so, spent a lot of time looking at code quality and she posed the question to me and said, "Erik, could you maybe do better code quality metrics with an LLM?" That is something I've begun to talk about. I don't have any good answers, but I just wanted to say just because the LLMs, when prompted to solve a problem may produce certain undesirable patterns as a byproduct, we can.
I think there is a path in there. I agree with Rebecca's suspicion, but did you feel that there should be something in there that we can use them in a way that would allow them to assess them whether a piece of code has certain characteristics that experienced developers would consider desirable?
One thing that is also interesting in that whole debate about productivity is that there is one set of metrics that we've featured on The Radar that I think almost everybody at Thoughtworks understands that they are sensible metrics, which are the four key metrics. Oftentimes, I've heard people say, "Why don't you just use the four key metrics then if you believe that they are and there's the scientific background and everything? If you are convinced that they are sensible and plausible metrics, why don't you use those to measure developer productivity?"
The problem here is that there's one massive misunderstanding because the cycle time or lead time as it is used in the four key metrics is the time from checking in the code to deploying to production. The entire phase, the AI coding system is used mainly and the programming is not captured by the four key metrics. Therefore, they are of little help to really quantify the improvements you could get by using such tool.
**Scott:** That's one of my triggers. I feel like the four key metrics have been used way beyond what they were ever intended or what they empirically were shown to predict. It was about business performance and operations. It was never meant to assess team performance. Yet I see team after team automatically measuring their four key metrics and holding them up proudly. That concerns me.
**Neal:** That's something else that Martin Fowler wrote about on his blog, semantic diffusion, that once a term becomes popular, the meaning starts diffusing because it becomes just the, oh, we capture metrics and these and these are all we need. That's something we always have to battle to make sure that technical things still have technical meanings.
Let's talk about the last one of our themes, which is around remote delivery workarounds and their maturity. We were all forced to get better at remote work during the pandemic, but then things eased up and now it's much more of a hybrid model. We try to pay attention to our ecosystem and what makes it better and worse. We're seeing a lot of the remote delivery workarounds mature by way of fixing broken feedback loops that exist live that got broken with remote. We're seeing tools and approaches that are helping us build a nice, effective hybrid model.
**Rebecca:** One of the things too, I think, is quite interesting in this space is how we are re-evaluating what it is that makes particular collaboration styles more or less effective for particular types of interactions. When we did the remote Radars, for example, overall, I think the blip stuff worked pretty well where I really felt, actually, given the subject of this podcast, where I really felt that we didn't get the richness of discussion was, in fact, in the themes.
When we are face-to-face with the themes, everybody gets in front of the board and moves stickies around and adds new stickies. The level of interaction that we have in that is at a different kind of level. I think more broadly, as we look at the various workshop formats and facilitated exercises, we are starting to get that meta-analysis, if you will, of what style really, really benefits from face-to-face versus other interactions where it may not be as important.
**Scott:** We should point out that we're all doing this from our home offices in opposite corners of the world. I was amazed when we did get together face-to-face for the first time after the COVID, and we had been doing The Radar remotely for some time, how efficient it was and how much more satisfying it was. I felt like we had a better quality product in the end for having been in the same room together.
**Erik:** There was one controversial point, though. At some point, we realized we're getting almost everything. There was a practice of how to develop software with the word remote stuck in front of it as a proposal to include on The Radar, like remote event storming, and I can't remember them all, but they were almost everything that you could just got a remote in front of it. Then we thought, what does it really mean? What is noteworthy?
We had a not too long a discussion in the Doppler group, if I remember correctly, to put our perspective and direction on it. The theme as it stands now on The Radar is remote delivery workarounds mature. We still would consider those as workarounds, making an implicit statement that the in-person format is the default format and the other one is merely a workaround. That got, for the listeners who don't know this, when we write the Technology Radar, it's the people who are in the group who write the entries, but it gets reviewed by anybody within ThoughtWorks who wants to.
That actually was one of the points that triggered a robust debate, I would say, in the margins of the Google Doc where we do the review of people saying, why are you saying it this way? Why aren't you saying we are switching to remote or the new normal has shifted or something like that? Are you just too old as a group that you have to hold to what you've done? I assure you, it was a discussion that we had, and yet we do feel many of the formats actually do work better in person.
If it is possible, we would encourage teams to get together for some of those formats because they are more productive. As Scott was saying, we're recording this podcast, which is relatively easy, from homes on I think three continents at least. At the same time, we also know because we have gone back and forth a little bit with it, creating The Radar itself, for example, is much, much easier when we all physically in the same room, despite all the technology we have in our hands.
**Scott:** As I said, I was in our Indian offices last week, where many people are still working remotely. There were some teams who were deliberately working in a co-located way, the old fashioned way. In that room, you could feel there was energy and creativity happening that you just don't get on a remotely distributed team. People were learning from each other, and they were excited about the things that they were learning and excited about the roles that they're playing on the project in a way that I don't think you can really achieve when people are disparate and sitting in their own homes.
**Neal:** I think what we've done with our Radars is a good call to action to people listening to this because it's not that you should go the pendulum swing completely to remote or to completely non-remote because we've kept some of the artifacts that we created during the remote time. The way we keep track of things, our blips in a spreadsheet now, we do that when we meet in person now instead of the way that we did before.
We're trying to be sort of meta-analytical ourselves about, okay, what is the real effectiveness of this practice, whether it's in person or remote? Let's try to measure what's effective for us as a group versus trying to make blanket statements about whether you should do one thing or the other and look at the trade-offs for each one case by case.
**Scott:** I think one of the things we've found is that simply translating the things we do when we're co-located in person into a remote format is not the way to do it. If you're going to work remotely and distributed, there are ways of working that are different and that are probably more effective. I think bringing in this asynchronicity, being able to work so that you don't have to be face-to-face and you have a collaborative space that you work in, I think that's a key aspect of it.
**Neal:** Okay. Well, that wraps up our observations for Volume 29 of our Technology Radar. This is always a snapshot in time, so there's no telling what Volume 30's themes will bring, but I'm sure there'll be some AI-related stuff on it, but who knows? We'll see. We'll do another podcast highlighting some of the thought process and a little deeper dive into some of our themes. Thanks very much to my co-host, Rebecca, and our two guests today, Erik and Scott. Thanks for joining me remotely today in all the scattered time zones we're in.
**Rebecca:** Thank you, Neal.
**Scott:** Thanks, Neal.
**Erik:** Thank you. Go ahead.
**Neal:** Thanks, and we'll catch you next time on the Thoughtworks Technology Podcast.
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
[ Explore Tech Radar ](https://www.thoughtworks.com/radar)
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