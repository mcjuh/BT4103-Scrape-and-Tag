<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/jugalbandi-building-ai-social-impact | Title: Jugalbandi: Building with AI for social impact | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Jugalbandi: Building with AI for social impact 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons  and Ken Mugrage | Podcast guest  Vinod Sankaranarayanan and Prathamesh Kalamkar
November 30, 2023 | 35 min 52 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/jugalbandi-building-ai-social-impact#Transcript)
Listen on these platforms
## Brief summary
It's easy for key industry players to talk up AI's potential positive social impact, but what does building for social impact actually look like? At Thoughtworks, a small team has been working on a project called "Jugalbandi," designing AI-driven systems and tools for civil society initiatives, such as a chatbot that helps Indian citizens find information about government programs and schemes in their native language. Earlier this year, Jugalbandi caught the attention of Microsoft CEO Satya Nadella, who saw it as evidence of AI's power to drive transformative change to every single part of the world. 
In this episode of the Technology Podcast, Jugalbandi team members Vinod Sankaranarayanan and Prathamesh Kalamkar offer an inside look at the project, talking in detail about the work they've done, some of the challenges they've faced and how they're looking to expand and increase its impact in the months and years to come.
**[Music]**
**Rebecca Parsons:** Hello, everyone. My name is Rebecca Parsons. I'm one of your co-hosts for the Thoughtworks Technology Podcast, and I'm joined today by my colleague, Ken.
**Ken Mugrage:** Hi, I'm Ken Mugrage. I'm one of the other regular hosts of the podcast.
**Rebecca:** We're joined by two of our colleagues who have been involved in a fascinating project that we'll be talking about. The first one is Vinod.
**Vinod Sankaranarayanan:** Hi. Good to be here. I'm Vinod. I lead our Digital Public Goods and Infrastructure work out of Thoughtworks, India.
**Rebecca:** And Prathamesh.
**Prathamesh Kalamkar:** Hi, I am Prathamesh Kalamkar. I'm a Lead Data Scientist at Thoughtworks India. Glad to be here. Thank you.
**Rebecca:** The project that we want to talk about is an umbrella project called Jugalbandi. First, I want to congratulate you all on the fact that this has been accepted into the Digital Public Goods Alliance. That's something that we are quite excited about. Can you tell us what Jugalbandi is about, where the name came from, and how this piece of work has come about?
**Prathamesh:** The name is very interesting. The name originates from, actually, Indian classical music. Indian classical music, we have this concept that two artists are playing together and they're lead artists, not one on the percussion, but there are two artists, and then they're playing some thoughts. That's what you call Khayal Gayaki. If you take that concept that if you're two artists are talking to each other, it's similarly in Jugalbandi, we have multiple AI systems talking to each other. You have a lot of speech models coming in from speech-to-text translation and from text-to-speech again. Again, you have elements on the other side and you have multiple search engines.
There are multiple AI components that are talking to each other. That's the real meaning of Jugalbandi — that there are multiple AI systems talking together, creating a beautiful symphony out of it. That's where the name came in from. When this project started, this was initially conceptualized to be an Indian government welfare schemes chatbot. That means that ordinary citizens can just talk to this bot in their own native language and can get their responses back so that even illiterate people can get access to this information. That's the central theme behind Jugalbandi. It's a suite of solutions, which breaks up one important thing, that is breaking barriers to information access, and that it does leveraging state of art AI systems. That's where the name and the concept comes from.
**Rebecca:** Excellent. Let's take those pieces and talk about them separately. Tell me a little bit more about this speech-to-text translation, because I understand that it's one of the very few systems that exist supporting many of the non-English languages on the Indian subcontinent.
**Prathamesh:** This whole project started actually at Thoughtworks itself. We started with this project called Vakrangee, where we tried to develop models in an initial few Indian languages, which can do speech-to-text conversion, and then doing a translation from one Indian language to multiple others. After that, the Ministry of Electronics and IT of the government of India came over and then took over that project and then made it into an offering, which is called Bhashini.
They are hosting some of these models that we are currently consuming, which can do lots of these things, starting from speech to text, text to speech, translation. They are hosting these models and making it available in the form of APIs, which we are consuming. Bhashini is currently hosted at the government of India, and we are the main users or advocating users of Bhashini through a lot of building these applications.
**Vinod:** Prathamesh, the advent of Vakrangee itself is actually a fascinating story. When we started Vakrangee, we did not know that in two and a half years we will have 22 languages with the level of precision that can rival anything across the world. When we started, the going standard was for someone to get a speech-to-text with a level of precision that is acceptable, it would take one and a half years.
Our team was able to bring that down to one week. Now, our team can actually create a new speech-to-text for any language within one week, given, of course, the data is made available. There were so many breakthroughs that happened through that journey. That's probably for another discussion, but that itself is a fascinating story. Vakrangee also is a Digital Public Good.
**Rebecca:** What percentage of the Indian population do you think is currently covered now by the 22 languages that you do support?
**Vinod:** The 22 languages are definitely the major languages that all of India uses. Of course, India has about 800 dialects, but these 22 languages I would think they should be covering more than 80% of the Indian population today. I can put it the other way. I would say most of the people in India would know at least one of these 22 languages.
**Ken:** If I may, a question. Can you give me just, like, a person in India wants to discover a government scheme: what does the interaction look like? Describe to folks what they're actually doing with the government chatbot.
**Prathamesh:** Earlier, it was mainly happening through an offline medium of communications, that is through printed media or maybe something in the newspaper, on television, or through the service center, that isn’t a very effective way of propagating this information. Again, that had issues in terms of sometimes they used to get inadequate information, they couldn't have ability to say that, "Okay, this is fine, but how would I make sure that, in my case, whether I'm eligible or for my need, how do I go and make sure that this information is actually relevant to me?" There used to be even these intermediaries who used to charge money just to give this information.
There is a recent news article that was published, and the title said that here is a chatbot that doesn't take money to give you the right information. It's that value proposition that you actually have a chatbot that you can talk to in your own language, describe your need in your own language, because if you go to a government office or a service center, they'll ask you very technical questions and people get scared. "I don't understand what is this, even. I don't understand these terminologies, so how do I get the right information?"
We try to break that using-- you ask your question in your natural language, the way you use it in daily life, and then it'll do all the translation at the backend. It will search for the right keywords and come up with the right kind of schemes that are available and even explain to you some of these keywords that people struggle to understand. If some people understand it, then it can use those contexts. For certain people who don't understand those terms at all, it can even simplify: ‘okay, this is the meaning of it.’ As you keep on asking it more and more clarification, it give you that and then bring it back to the original flow that they're supposed to have. It's that way that you can talk to it and in your own language.
**Ken:** If I may, just to be explicit for listeners that aren't maybe aware of Jugalbandi, it's doing this in audio, it's speaking to the person. It's not defining it on their phone in a literacy they can't read it anyway.
**Prathamesh:** Correct. It's actually a WhatsApp chatbot. One of the interesting things in India is that the penetration of WhatsApp is surprisingly high, right? Even if you go to the villages, with the advent of smartphones and as well as the connectivity in 4G and 5G networks, you'll be surprised to see that people are using WhatsApp as primary mode of communication. The simplicity-- they're used to it because if you want to talk to someone, I will just go on to WhatsApp, record a voice note and send it to you. It's so much easier than just typing in there and doing something in English or maybe in their own language because typing is difficult. They're very much used to conversing in this format of sending voice notes. We thought that the most effective way of reaching the bottom of the pyramid is through this channel.
**Rebecca:** Excellent. Can you tell me a little bit more about that backend piece. We've talked so far mostly about the speech-to-text and text-to-speech and such. You alluded to, yes, we find the keyword and we look things up. Can you tell me a little bit more about how that backend works for this government scheme and in terms of getting the right information to them and following on that flow that you were talking about?
**Prathamesh:** This whole flow is orchestrated using something that we call a finite state machine, that means we track the user state using multiple finite states. As the conversation moves on, the user conversation moves from one state to another. These transitions from one state to another is where we are actually using OpenAI large language models. That is one thing. The other one is also for doing the right search, that means given the information that you're looking for, how do you make sure that you're searching for the right schemes.
For there, what we had done is we scraped the information from the Indian government website, and they keep on updating this website on a regular basis. We scraped that information, we take that, we pass them through something which is known as embedding models, and then store those vectors. When the user query comes, we try to do a semantic search, that means it's not a keyword based search, it's a meaning based because many a times the words that are used maybe in a government website versus what people are using can be very, very different, but semantically, they mean the same thing.
It's important to do this semantic search. Nowadays embedding models are getting better at embedding the meanings or encoding the meaning. We do that search and then fetch the right information that, okay, based on your thing, this looks like, okay, we believe that these schemes look relevant to you, or even ask a probing question that it looks like your search is too wide — maybe can you narrow down that, what kind of information you're looking for. It does that clarification. And then it gives you the user, we believe that these are maybe five most interesting government welfare schemes as per your need.
Gives us a one line summary of each one of them, and then tells you, which one you want to know more about. That's when the state transition happened, that from a searching you're moving now to the detailing, that you're going into specifics of one particular welfare scheme. Then that's where this transition happens in the finite state machine. It gets more details about, now what is your eligibility criteria? What benefits does it provide? What documents are needed, et cetera. There's that back and forth conversation and then gives back replies in the native language. This is how the flow is structured.
**Rebecca:** We hear a lot about large language models and hallucinations. Obviously, given your target audience, the level of frustration that might come from, "Wait a minute. Why are you telling me this bizarre thing?" How have you handled that hallucination problem?
**Prathamesh:** Basically, to answer your question, hallucinations is definitely a very important problem and the most practical hindrance in terms of adoption of LLMs. Literature has shown that using retriever augmented generation is an effective way to control hallucinations. What we do is we tell LLM that, hey, there are two sources for knowledge for an LLM. One is the parametric knowledge. That means whatever it has learned from internet during the pre-training plan. That's one knowledge source, and the other knowledge source is what you give it as an information in the input prompt.
People think that prompts are only supposed to be meant for asking questions. That's not correct. Actually, you can also give it a lot of information into that which fits in that window, and then ask that using this particular information, can you answer me the question? That's the crux of RAG. Post-RAG, what we have done is we have created six layers in which each of these concepts are formalized. It starts from UI layer, then speech handling layer, then how do you plan for what information is needed to answer a query, actually getting that information, putting it into the LLM and getting the answer back.
There are these six layers that we have formalized in post-RAG architecture. Essentially, how do you control hallucinations is two, three things. First is using RAGs, and second one is using write prompt engineering, saying that you should draw the knowledge boundary very clearly, because for most of the practical applications, you would want LLMs to focus on certain types of problem. You don't want answer for anything under the sun.
Let's say you are working in retail and you see your-- just your domain, if you are working in, for example, in fashion, where it just about what's the latest trends, et cetera. Every like chatbot or customer facing application will have that boundary. It's very important to draw that boundary using prompt engineering so that if anything outside that comes, you should politely say that, "Hey, I don't know this instead of trying to answer that." Those are the two, three things that effectively reduce hallucinations.
**Rebecca:** Excellent.
**Vinod:** If I may, Rebecca, it's also interesting in terms of the risks that you perceive with regards to hallucination and the use cases that you start adopting. While Jugalbandi for schemes and benefits is one, we also got a request from one of the law enforcement personnel of a state to adopt this technology for helping women and girls who are undergoing harassment. The risk associated of hallucination on the second is much, much larger.
If you give the wrong answer about a government scheme, they go check, they got the wrong scheme, they come back. It's perhaps a few hours wasted. In the second case, the case of harassment, if you give the wrong answer, it could be a matter of life and death. We are navigating through those aspects as well in terms of what is acceptable in this type of use case and what is not acceptable in a different type of use case.
**Rebecca:** That actually leads nicely to my next question, which is what are some of the other applications other than the government schemes application that you have already implemented or are looking to implement under this Jugalbandi architecture?
**Prathamesh:** We started off with this government scheme chatbot, but we soon realized that it has potential to be used elsewhere. One of the things that we felt immediately was that, hey, now that you have a chatbot working on the schemes, is it possible that I can swap schemes? Let's say I put my own documents, can I swap out that scraped information about schemes and then plug it back with my own information, which could be anything that's specific to my domain? Then you have a chatbot working on top of it.
That's where we created a solution called as Generic Question and Answering which says that talk to your own documents. The concept is essentially the same, that you upload a corpus of your own documents. Then basically you, again, index it, store it somewhere, and then you can do a conversation on those documents. This, while on top level, it looks very simple, but I think it breaks barrier to innovation for a lot of players, especially in social sector because they don't have a technical capacity in-house to build such things. That while at a high level everyone is talking about chat GPT, et cetera, but they were under constant questioning that, how can you make the answers more authentic or make them conditioning or condition those answers based on certain type of data that I wanted to look at?
Then that's where it helped them. It immediately acted as a starting point, as an innovation trigger for a lot of people to just quickly come and then put those documents, and we created an API on top of it. Everything was self-hosted and it acted as a starting kit for anyone who wants to create a chatbot. Then this become an instant hit. We tried this in multiple places. A lot of NGOs showed interest, actually. Bandhu is one of-- a great example of that, that they have created a chatbot using this starter kit. Basically, their problem statement was how do you help migrant workers in India who migrate from the villages to the cities to find the right shelter, because many of time these shelters for blue-collar workers are not listed.
They have created something which acts as a listing for such blue-collar workers. This became an instant application of such thing wherein they took Jugalbandi question and answering as a starting kit, uploaded their own data into it and then built a chatbot for them in a matter of couple of weeks. Then now they have taken it forward and then built more sophistication on top of it. These offerings really act as a starting point for a lot of such innovation use cases. That was one.
Then we took it to even courts, Indian courts. They had very specific requirements in terms of they wanted to search for the right information but they didn't want any paraphrasing aspect. That means I just want to get the answer as is. We did some changes to them. How do you make sure that the right information reaches and at the same time it's traced back to the original source? While an ordinary citizen is-- or he wants paraphrasing, on the other side of the spectrum are judges who says that, "Okay, I just don't want to answer, I want to trace it back to the original source from which it came."
We built something for them where you can actually trace back the answer to the original thing and that it doesn't paraphrase too much, and use that actual language that was used in the original documents. A lot of this spectrum was quite large on this. Even though we have a lot of adapters from social sectors, NGOs, but also now we are working very closely with UMANG that is one of the app that we have under government ministry.
Wherein they have a lot of APIs that are integrated into the UMANG, and now they're adding one more feature to UMANG which says that talk to government. Talk to government, not just government schemes, but talk to a lot of other government offerings that are there. One of those things that we are seeing is push this, all of government towards citizen using technologies like this to make it more accessible.
**Vinod:** Just to explain, UMANG is almost like the super app of the government of India where they try to bring all features that citizens need to interact with the government. It could be about your driving license, it could be about your power, it could be about your school, hospital. It could be about any of those things. This is supposed to be a portal from where you can go and get all those benefits, and they're now looking to integrate this chatbot into that, which I think is incredible.
**Ken:** That's great. I'm curious, of course, the AI space and generative AI, et cetera, is fast moving. I think you probably have noticed. Also, you've talked about the demand here. Are there strategies you've taken from an architecture perspective or from a rollout perspective to make up for that, that, "Okay, it's a very, very fast-moving technology, demand is very fast moving, next week's not going to be the same as last week?" Are there strategies or are you just rolling with it, or what are you thinking about there?
**Prathamesh:** When we started, we just were following the trend, like, "New models are coming up every week. Maybe new methods are being discovered of writing prompts. How do you cope up with this?" I think initially when we started, we were just following the trend, keeping an eye on what's happening, integrating that into what we can build. I think then later on we felt a need that there is a need to formalize some of the learnings that are coming up consistently.
That's where we came up with this post-RAG architecture where some of the very common needs are being actually documented. The common patterns that we saw across. For example, people constantly were struggling with having leaking of sensitive information outside organization boundaries. That's one of a very common example. The data privacy layer in post-RAG tries to handle that.
Just like we try to create guardrails in terms of what information should go in, go out, or go where. Not just that. A common pattern that we have seen is that you need to understand that LLM can't do everything on their own. They need to pick and choose tools for right set of tasks. Obviously, they're good at certain things like reasoning, having conversations, et cetera, et cetera, but let's say you want to do something else, then there are specialized tool. If they can do it, then there should be a provision that it should be-- You should call that tool rather than doing that thing on your own. We provision that using the data planning layer wherein it's plug and play. We try to formalize our learnings in that architecture. Yes, and as you said, it's a constantly moving space and we are trying to--
**Vinod:** If I may add, I just wanted to, Prathamesh, take you back to maybe about 10 months when OpenAI suddenly became big. Prathamesh and I were having this discussion, and Prathamesh you were saying, "I don't know what I'm going to do because over the last 12 years, I've been specializing in something and suddenly this has come." We discussed and we said, "Hey, if you can't fight it, join it."
We pivoted and we said, "Hey, rather than saying everything that we've done so far is perhaps irrelevant, let's see what we can do by adopting LLM." It's actually interesting because I think OpenAI became more visible last November, and by March, Jugalbandi was out and perhaps one of the most visible application that used LLM out there. I think we were pretty good with moving with the flow. Of course, it's evolving, but it's rapidly evolving. I think we are just trying to stay along with it.
**Rebecca:** Excellent. I mentioned at the beginning that this was accepted into the Digital Public Goods Alliance. Can you tell me a little bit about what that means and some other activities we have surrounding that alliance?
**Vinod:** Digital Public Goods are essentially software content protocols that are aimed at supporting the 17 sustainable development goals that United Nations has. That's the broad theme, but one very key aspect of a Digital Public Good is that it is open source. This alliance is a body of several organizations including United Nations and other foundations, even countries today, India, for example, is one of the alliance members, et cetera. Thoughtworks is the only IT services company who's been invited to be part of the alliance.
We are very proud and privileged to be in that group. The reason why we were invited was because out of about 150 certified Digital Public Goods out there, when we counted, we realized that we have contributed to about 14 of those. About 9% of the entire Digital Public Goods that are out there, we have had a role to play. Of course, we've been nurturing two, which is Bahmni and Cloud Carbon Footprint. That's ThoughtWorks' association with the Digital Public Goods Alliance.
I think Vakrangee, Bahmni, Cloud Carbon Footprint, there are a number of Digital Public Goods that we work with. It's humbling as well and matter of privilege because some of these solutions that we work on help people at scale and make benefit the last person standing on the in a matter of speaking. For example, Bahmi is very focused on health, and so you can look at it from that domain, but something like Vakrangee or something like even Jugalbandi in this case, so they're domain agnostic.
I can now use Vakrangee for health, for justice, for finance, for education. I can use any of these tools across the board. That's where we are also seeing a lot of innovation. There is this concept called combinatorial innovation. Prathamesh spoke about Jugalbandi from the concept of saying, "Hey, we've got different AI models talking to each other and providing this." That's the technology space.
You can also look at innovation happening where you have Vakrangee or a Bhashini that you can then combine with something like Bahmni. Bahmni is a health product, where doctors, rather than having to type and give notes for patients can just speak, and then the notes are taken automatically. You just increase the productivity of doctors that much more. This concept of combinatory innovation is starting to really take off, and we are very happy that we are behind in the midst of all that exciting work.
**Rebecca:** What comes next? Are you just mostly waiting for requests to come in? I think this whole concept of talk to your documents, for example, has such potential for knowledge management and many other things, but I'm interested in where you two see this going.
**Prathamesh:** First, I think we get many requests for this every week. Actually, we are getting so many requests that the current Jugalbandi team is no longer able to address all of those. We thought of there should be another Jugalbandi, that how do you use Jugalbandi, something like that? The essential thing is that Jugalbandi is already open source and people can use it. The main pain points that we see is they don't have technology capacity to implement those.
How do you move from the current point where you need to have some technical capacity in-house, to more like a local or one click deployment solution. That's what we are working, one area. The other one is looking at some very big implementations, which are citizen scale. One that I spoke about is UMANG. The other one is Department of Justice. These are two very big implementations that we currently have in place, which will use Jugalbandi as a starting point, and then they really take them to the citizen scale. Those are the areas. Apart from that, we are also continuously changing how Jugalbandi is implemented, because now with all these latest changes, strengths that we see, the architecture behind Jugalbandi needs a lot of changes. How do you keep up with those? How do you make it work better? That's something that we are continuously improving on.
**Vinod:** Could you also talk about the G20 session and what was being demonstrated there in G20?
**Prathamesh:** We were invited at G20 to talk about, "Hey, why don't you talk about what we have already built and show it to people across the globe?" This year, G20 happened in India, New Delhi. Basically, the objective was, can you create a chatbot around G20 thing, or like all the information or all the things that are happening at G20? What had really happened was just all the input document-- ingested documents where all the tracks that are there in G20, what are the conclusions that were drawn or what are the discussion points, et cetera, what are the trends, et cetera.
Then we ingested those documents, and in just less than three days, we were up with a running bot on which you could talk to in your own language about what's happening at G20, et cetera, and all the information related to that. That was seen as a big success. We had international media, and then even Bangladesh Prime Minister, Sheikh Hasina, showed a keen interest in implementing this in Bangladesh. The team have contacted us, and then we are following up with them. Bangladesh government is really keen to implement this at their own level, similar to what we have done. They want to implement a schemes bot in Bangladesh. That was a key takeaway for us.
**Vinod:** It's very interesting to see that in places when people are not digital natives, the government or the tech community there are actually making rapid strides, use some of these technologies like AI so that the non-digital natives, so to speak, are now able to start accessing a lot of these digital capabilities. It's a bit like, people in the [unclear] countries, they never had a wired phone. They just directly went to the mobile phone because it was much easier to just set up mobile phone towers and then get everyone a phone rather than put all these wire. I definitely see that deep tech is starting to get utilized a lot more in the global south now.
This sophistication of technologies that are occurring here are definitely something that I think the entire world should watch out. We've had conversations with several other-- some of our colleagues in other countries as well about some of these technologies including Jugalbandi and Vakrangee, and they're definitely keen to see how some of these can be adopted. The good thing is these are all open source, and so there is really no barriers to adoption. I think it'll be really interesting for people across the world, the international population, to start looking at some of these technical tools that are being put out as open source and see how that can be adopted and utilized.
**Prathamesh:** I just want to summarize this. Someone said this to me, which is very-- that 2023 was year where prototypes were being built, and the next year, '24, is the year when it'll actually be deployed on ground. That's what we see even for us, that there will be so many implementations and then the rubber hitting the road, and then lots of things happening. We are excited to see all of that happening.
**Rebecca:** Excellent. Well, thank you, Vinod. Thank you Prathamesh, and thank you, Ken. As I said, again, congratulations on the Digital Public Goods Alliance. That's somewhat old news, but I think it's still worthwhile highlighting that. I look forward to a bright future of knowledge management and talking to my documents. Maybe we can sort out some of the speech-to-text features of some products that we all know and love. Thank you, everybody.
**Prathamesh:** Thank you.
**Vinod:** Thank you.
**[Music]**
**[END OF AUDIO]**
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