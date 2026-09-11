<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/navigating-ai-opportunities-myob | Title: Navigating AI opportunities at MYOB | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Navigating AI opportunities at MYOB 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Nigel Dalton | Podcast guest  May Xu and Simon Noonan
August 07, 2025 | 57 min 23 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/navigating-ai-opportunities-myob#Transcript)
Listen on these platforms
## Brief summary
How should businesses go about actually navigating AI? It's one thing to strategize and generate new ideas, but what needs to be done to put it into practice in a way that's effective and commercially impactful? 
In this episode of the Technology Podcast, new host Nigel Dalton is joined by his Thoughtworks colleague May Xu — Head of Tech for Thoughtworks APAC — and Simon Noonan, CTO at Australian business software company MYOB. Thoughtworks has been working closely with MYOB for a number of years now; May and Simon explain how they collaborate and offer their perspectives on everything from leadership to architecture in a world where AI has become imperative. 
**Learn more about[Thoughtworks' partnership with MYOB](https://www.thoughtworks.com/clients/myob).**
## Episode transcript
**Nigel Dalton:** Hi, and welcome to the Thoughtworks Technology Podcast. My name's Nigel Dalton. I'm guest-hosting the podcast today. I'm a social scientist, not an engineer, so that'll bring a different perspective, and that's useful because we're going to take a different perspective on a very popular topic today. It's July 2025, and today's exam question is, "So, I'm exhausted by all this media hype about artificial intelligence for software delivery. What are the real people in real companies actually doing?"
To answer that question, we have, in the studio today, two very real people armed with data and experience earned by making AI work for a very well-known Australian company, MYOB. Today, we get no AI slop, no vibe-coding, no marrying your robot-- thanks, Gary V., for frightening us all, just real-world experience. Welcome to MYOB's Simon Noonan, Thoughtworks' very own May Xu. Seat-backs upright, tray tables folded away, let's get going, and let's start with some introductions. Who are we, and how are we using AI? Let's cross to you, May.
**May Xu:** Thanks, Nigel. Very glad to be here. I'm May Xu, Regional Head of Tech for Thoughtworks APAC, and I'm also a consultant. I'm actually very cautious in adopting AI myself. I definitely believe AI has a transformational impact across all, but it is not a silver bullet. Actually, at home, I used to call some of my kids' questions, used to call them "Google questions." Now I call them, actually, "ChatGPT questions." When the kids are asking those, I redirect them that way.
On work, actually, Gemini Deep Research has become my new favorite. Like, say, as a consultant, we do a lot of work regarding analysis. It's I used to spend days actually to research all these materials across different sources. Now I got the initial draft, like, say, with Deep Research in 30 minutes, so very satisfying. Just sometimes, it's the way you look deep in, to say, "Oh, okay." I could say it's good in structure, but you need to be very careful because sometimes, it does make up things.
**Nigel Dalton:** Deep Research is a great AI to be useful and adept at using because we've got clients like MYOB who demand references, and facts, and all those kinds of things. Leading the charge for them today, Simon, welcome to the show. What have you been up to? What do you do? What's the job title? And how do you use AI?
**Simon Noonan:** Yes, Simon Noonan. I'm the Chief Technology Officer here at MYOB. I've been lucky enough to be in technology for over 25 years, be that in banking, consulting, but mostly, in digital businesses, in digital-first organizations, so I have deep experience there. From an MYOB perspective, we often describe ourselves as a 30-year-old startup. For those who don't know, we provide cloud-based business management solutions to small and medium-sized businesses across both Australia and New Zealand.
Our purpose is really dear to our hearts. Our purpose is simple, but it's very powerful. We are here to help more businesses start, survive, and succeed, and, as you would imagine, technology plays a big role in that. The technology team at MYOB think very deeply around the technology solutions that we can provide our customers, and as the world has evolved in the last number of years, AI is now part of that conversation. AI is something that we talk about internally around how we operate, but also what AI we can provide to our customers.
It's going back to May's points, where I'm using AI? I'm not a fancy user by any means. I use some of the generic tools and AI in some of the generic tools like Glean, Teams, Miro, Confluence. I've just used that naturally, but I've been stretching myself as well. I've started using Cursor, started using Google Notebook, and started to write a few apps. They are not flash, and my prompting skills are improving by the day.
**Nigel Dalton:** Thanks, Simon. Then we'll get into this later, but of course, you're at the leadership level of a very large technology group, and one of the things we'll talk about is. I'm pretty sure you're seeing the bills from paying for all this AI and making the business case accordingly. It's great to have the two generations of execs. I've got 40 years of scars from managing technology over that time, so two generations. We've faced different kinds of monsters during that time. I think we crossed over at about the mobile revolution and the arrival of smartphones and those kinds of things, but so much, for me, resonates around the web arriving in the '90s.
The hype, the expectations, the transformation required in the way we worked. We got agile of all the things, and Thoughtworks grew out of a lot of that. Leading in the current environment with the last few years have just been security, data, and artificial intelligence. It's beyond my pay grade. I'm delighted to have someone on the show who's doing that. The best I can do is, mid-journey, to animate my grandparents and frighten the old people. That's what I'm engaged in with artificial intelligence.
Let's get on. Let's talk about the context. Let's anchor ourselves in 2025, not the least of which it's early July 2025. Simon, your business has just exploded, so thank you so much for making time for us today, because it's the beginning of a new financial year in Australia. The rollover of the old one. Everyone's in their MYOB reconciling the year and attempting to get as much tax advantage as possible. It really does feel like the movie Everything Everywhere All at Once. We've got ChatGPT-5 coming this month, apparently. We've got America and all of its nuances. We've got wars, tariffs, a climate crisis, aging population, 16 billion password leaks, of which I think 15 billion are mine, according to my password manager. In that real world, talk about MYOB and the challenges and the opportunities as you're facing into another year, Simon.
**Simon:** Yes, and great introduction once again there, Nigel. As I mentioned a little bit earlier, we're a software business, and our goal is to provide great experiences for our customers, and that translates to really providing and delivering unrivaled software experiences. With that, myself and the technology team have developed, recently, a three-year technology strategy. It's got four main pillars that I might touch on, and it gives you a bit of color around where we're going and how we're looking to support our customers.
The first pillar is around Future-Ready Teams, and how do we create the capabilities of the future? How do we create the capabilities of the next generation of requirements for our customers? The second pillar is around Flow. How do we get the flow of work working so that you--? What I imagine is, think about those times in your career where you've just been in that flow state; how do we create that flow state just naturally, in the system of MYOB? Be it ways of working, be it tools, be it techniques.
The third pillar is Intelligence Everywhere. Intelligence Everywhere, it's got two dimensions. It's got, how do we create human intelligence and really empower our people with greater insights, great data, and great intelligence? Also, it's about customer intelligence. How do we provide solutions and products so our customers, these small businesses that use our software, have a greater insight around their financial progress and their financial situations? In intelligence everywhere, you've got Human Intelligence, let's call it "HI." We've got Customer Intelligence, let's call it "CI." It will be powered by our old mate, AI.
For me, I think about artificial intelligence and how it helps human intelligence and customer intelligence. The fourth pillar we have is Platforms, and platformers being our bedrock. It's all very well having great teams and a wonderful flow of work, and having these new innovations for our customers, but if our platforms aren't performant, if our platforms aren't thinking about the next-generation experiences for our customers, yes, they will slow us down. My role is to think about, "How do we explore technology? How do we take in the insights around the way the world's moving and think about how we can enhance what we're doing in MYOB, so that, ultimately, we can enhance human intelligence and customer intelligence?" We've learned a lot with AI in the last little while, and we've made some mistakes.
Those mistakes have been that, yes, in the past, we'd thought to ourselves, "Let's get some AI tools into the organization and enable our teams to use those tools." That was a classic fail. It was literally like throwing mud at a brick wall and seeing what sticks. Yes, it didn't stick, so we've taken a step back, and we've gotten a lot more deliberate approach around how we're thinking about AI and AI within MYOB. We focus on three components. It's an approach that is embedded into what we do. It's about mindsets, really going through and helping out people around understanding the opportunities of AI and busting some myths around what AI does and doesn't do, and how we want to use it internally. It's mindsets.
Once we've got the mindsets right, we start thinking about, "How do we help our teams and support our teams with the right skillsets?" With those skillsets supported by the mindsets, we then think about, "What are the toolsets that we create that we enable for our teams to be using AI in a safe and really effective way?" What that does is it creates a little bit of a flywheel effect, if you like, because once you have the mindsets, the skillsets, and the toolsets, you actually start lifting the capability in the organization.
Then our teams get curious and they think about, "What are the mindsets I need to have for the future? What's the next set of mindsets or opportunities that we have?" Then we're thinking about the skill sets to further empower our people, and that flywheel is occurring internally. The beauty of that flywheel is, people can go at different speeds, teams can go at different speeds, but we're doing it in a joined-up, consistent way. For me, that is supported by what we have across the organization, an OKR, or goal that everyone has, which is we are asking people, myself included-- leaders and people from across the organization, to use AI every day in their working practices.
I'm really happy to say that where we stand today is 80% of people at MYOB want to use AI more in their daily work. That survey was taken two weeks ago. I suspect if we took that survey 6 months ago, it would have been down in the low 10s, so we are really seeing an uplift. This is not just top-down, it's bottom-up. It's us as an organization thinking about, "How do we embrace AI for the right use cases to really enhance our people, make them more effective, and then enhance that human intelligence?"
**Nigel:** Thanks, Simon. Now, May, it would be typical for a Thoughtworks consultant to get put into a box of just being about toolsets. Tell us a bit about how you've been fitting into that threesome with the mindsets and the toolsets in terms of what you've brought to the table at MYOB with the Thoughtworks approach?
**May:** Yes, I think what Simon shared has been a great way regarding, really, from, "Would we get stuck?" To, "Will we be able to create momentum with the teams?" I think that is really the key. One of the common things I see across many clients is what I call "20% disappointment." This is actually something related to what Simon talked about the tools. When organizations just treat AI or software delivery as, "This is a tool, thing," they will just like to say, "I paid the money, I should be able to get the value, whatever the vendors told me around productivity, late engagement," and, after a year, most organizations find out they're actually getting stuck with this 20% adoption rate and 20% acceptance rate.
They now just start to wonder what goes wrong and, "How do I actually be able to make this, really, skill engage?" Because it's surprising. Everyone should be interested in, say, AI, why it doesn't work? I think this is actually one of the things, just by working closely with the amazing MYOB team there, Simon and the tech leadership team have been really, really amazing because we're basically just partners, collaborate in just the ways, "How do we do this?"
One of the learnings we have kept using this-- following the toolset, mindset, skillset is actually extract this into five dimensions of AI adoption. For here, one of the key things that we talk about is around, definitely AI literacy. When we talk about the first thing around AI literacy, it's not about training the team on how to use certain tools. We'll actually go one step further, thinking about, "What is the underlying core capability we need to build here?" Rather than just train people to use GitHub, Copilot, or different tools. We take a step back and we actually say, "Hey, proper engineering is the key." We actually focus on training people on proper engineering rather than just on the tools, because the other things-- I think the reality we're facing in this space, is around the entire ecosystem is still evolving, the tools landscape changing very fast.
Unlike previously, you can use an ID for 10 years without changing, and here, what we need to be prepared is that we need to be prepared to change these code assistant tools maybe three months. For example, like to say, "We have been using Copilot, but now, we start try using Cursor," in that-- As well, it's, organizationally, we're ready to change at a faster pace, how do we prepare our people to change at a fast pace as well?
The second dimension we're talking about is really around campaigns and community because I think that we have been creating AI campaigns, in my opinion, in that space, because we definitely believe, say, for these kinds of changes, the key is around, like you say, it needs to be valuable for our people. It can't just be a top-down change to say, "We want to become AI-enabled."
One of the key messages I think we're having-- talking to, for example, our development team in this space is around to say, "Hey, we want you to use AI to reduce the waste, the friction points of the system to create a better developer experience so you actually can shift your cognitive load to AI rather than keeping all of them with you." That's actually what we focus on, so we didn't actually focus around tools adoption. That's actually moving on to the next case is around-- say, as we're building up this capability, one of the cases is around, of course, people are going to try different things, I think a very passionate group of people, but as an organization, how do we ensure we have structured experiments?
Repeated experiment does not have this increased learning across the organization. Just make sure we have a focused experiment, and we will be able to build on top of the learnings we learned from one experiment to another, rather than repeating. It's actually coming into a user case-driven experiment. We're actually mapping out to the entire value stream and working with the team to say, "Hey, what's the biggest pain points of delivery today?" Then, focusing on this one. Then let's think about, "How can we use AI to solve that?"
The ones we have actually are really exciting because we have so many different experiments across different roles happening there. It covers, actually, from user requirement to testing, to code, of course, to architecture, as well as instant response. We'll basically consider this across the entire software-delivery lifecycle.
One of the key things, we're definitely saying, "Hey, how do we ensure this is knowledge well-known?" This is actually one of the things we're thinking about, to, say, create an AI playbook so we'll be able to-- using that as the single source of choice around the organization's knowledge or around AI adoption, not only about success. Not only about, "Well, it works," but also about, "Well, it doesn't work because the tools actually move in very quickly."
How to capture our most recent experience of working with certain tools is really important, so we can avoid people keep trying-- the failing cases, in a very short time. The next one, I think, we definitely wanted to highlight is actually around AI governance. Yes, that, really, we're thinking around, say, the team has built an amazing AI Tech Radar in this case, because with so many different tools flying away, so organizations, do we allow everyone to use everyone's everything? Because it will be really hard to support, and also a brand's risk regarding security compliance.
How do we keep up of that as well? I think AI Tech Radar is becoming a really good example around using that, and I think the team also-- yes, I think that's an amazing name. Every time I think of the name, I would smile. [chuckles] I think I'll have to-- Tracey Banks and Dave did an amazing effort to call this "Daisy." Basically, Daisy is a design authority to go through all of the AI-related decisions, as an organization, around that. That was really amazing to ensure we both allow innovations in the organization without slowing down the pace of change, but in the meantime, also minimize the risk to the organization.
**Nigel:** Next question time. Simon, you're just back from some travel. I don't envy you at all, having to do the air miles that you do. My challenge to you is, can you link Silicon Valley to the Hunter Valley in terms of AI playing out? Because MYOB is a pretty humble package used by a lot of down-to-earth Australian businesses. You've had the challenge of drinking from the fire hose of the United States just recently. I'd love to know-- so two parts to the question. How's AI turning up for that humble vendor in Hunter Valley, and what have you been hearing? Let's start with, what have you been hearing in Silicon Valley?
**Simon:** Yes, cool. Nigel, I might contrast the two valleys to the Napa Valley and the Yarra Valley because they've very much got some similarities there, clearly. Yes, you're right, I just returned from the US, where you're met with over a dozen organizations, and I think it's fair to say the conversations very, very quickly centered and focused on Agentic AI. Yes, a number of takeaways from those conversations, but I can say it was unanimous that every organization, in their own way, describe the rate of change we're going through right now as staggering and genuinely nothing they've ever seen before.
Some of the hyperscalers said they didn't have a product in this space six months ago, and now, the adoption of the products they've got in this space is one of their fastest-growth products in their suite. One of the things I'd take away was, as you speak to all these organizations, they all have their own examples as to the type of change we're going through right now. The way I've brought it together in my head is, Nigel, you spoke about a little bit earlier, your experience in the late 1990s with the dot-com boom.
If you think about the dot-com booms of the late '90s, early 2000s, you think about the adoption and the explosion of smartphones in 2010 and beyond, and then we think about cloud computing and how that really came to life and has scaled since 2015, and you say, "Well, dot-com booms, smartphones, cloud, that all occurred big, significant change individually, but collectively, massive change over 15 years." What I'm taking away from my conversations in the US is, you put all that change together, those big moments, and what's happening right now is going to happen in three years.
That same amount of change is going to happen in three years. It's just amazing just seeing these organizations think about the bets they're placing, but also, frankly, just some of the uncertainty around, "Where to next?" I think, be it how agents communicate, be it MCP or agent-to-agent, there's a whole lot of debate out there, and I think the open-source community is going to have a really important role to play to influence the pathway for the future for AI. One of the things that we spoke about is how we think about AI within MYOB, and tested some of that thinking with the hyperscalers and organizations we spoke to, and we look at AI with three different lenses.
One of the lenses is, yes, AI for our people. For human intelligence, as I referred to earlier. Then we've got AI for our customers and our existing product offering. They're two different and distinct-- different opportunities for AI. Then the third element or third lens we think about is AI for disruption, and what we were able to articulate to the organizations we spoke with is, we see these three things, albeit being different. There are some similarities, but I guess the beauty of thinking about it in three different dimensions is that they can go to different speeds, but everything needs to be going together, simultaneous.
For me, having those three different speeds allows us to think about, "What is the risk appetite we have for each of those dimensions?" Some things never change. Security, responsible use of AI, and user experience need to be at the forefront of whatever dimension we're thinking about using AI. My takeaway from those conversations is, as these big organizations are thinking about the next evolution of AI in their worlds, the one thing that really holds true is, AI must be intuitive, it's got to be human-centered, and the user experience needs to be fit-for-purpose. I think that was just a really important takeaway. I think, at the moment, we can get dazzled by LLMs and platforms, those things, but actually, we've got to think about the end customer, be that people in our teams or be it our customers.
**Nigel:** Simon, I think the agentic thing is really fascinating and particularly linking it back to your comment about flow being one of your core principles, because what we want to do for people is create a lot less friction in their business flows, those kinds of things. I'm curious as to how you balance that up against a sense of creating security, because MYOB, probably one of the most trusted pieces of software and relied-upon pieces of software in Australia and New Zealand.
How have you blended that into your thinking around making AI a part of the customer offering as well?
**Simon:** Yes, and I think it's still early days, Nigel. I think what you heard from May a little bit earlier is, we are very much a curious workforce and we're curious around how AI comes to life. With that, we pulled together really contained experiments that we can test out because we have a really important responsibility, and we are trusted with a whole lot of important information and data from our customers, and we don't want to jeopardize and lose their trust. That's a cornerstone of everything we do. We've got a really great Cybersecurity team who help us think about the guardrails we need to put in place and, what are those non-negotiables?
As I also mentioned, the risk appetite for doing things internally is a little bit higher, the risk appetite that would do with our customers, because we need to provide our customers a seamless, accurate, correct, unambiguous solution so they can do their jobs. Our job is, ultimately, allowing small businesses to work on their business, not in their business. If they can think about where their business is going and think about, strategically, how they grow their business, we're doing our job because we're empowering them to get out of the day-to-day admin work of their business.
**Nigel:** Now, May, one of the things, as a social scientist, I talk about a lot with our clients is navigating complexity and complex environments, which the simple principles are you need great scaffolding and you need a really coherent narrative. Now, one of the things I love is the scaffolding you talk about for engineering thinking, particularly around the loops of AI, the three loops. I can't draw them in a podcast, but how would you go explaining those three loops?
**May:** Yes, I think for that, three loops is a very interesting one because if you try to visualize this from the path between the organization and the customers, one of the key things you're probably looking into is actually very similar to what Simon talked about. The first loop you're actually thinking about is the inner loop about Build Productivity. It's actually around the technologies, how do we build things in the way that we're leveraging AI?
The second loop we're looking into is, say-- it's actually a middle loop. What does that actually focus on? We're focusing on Business Process Optimization. Basically, it's really around, how do we run our business leveraging AI? The third loop, if we look into it, is exactly just more-- it's almost like this disruptive around the customer experience side. It's actually the third loop called "Outer Loop." It basically focuses on customer experience. I think that is really just a clearly real-world indicator, is around the three loops we all need to focus on. I think that's one of the things you probably feel like it's about. We have to do it all, but I think that's probably around there's no choice.
[laughs]
You have to focus on them all, but I think according to the priorities, and definitely, those are prioritizations. How much you want to invest, how much you want to progress, is still this decision you need to make.
**Nigel:** Simon, I'm curious as to who's left holding the baby at MYOB? Who owns AI at your place? Is it one person? Is it many people? Is it a guiding committee? How are you managing that level of governance?
**Simon:** Look, the governance is one thing. I think ownership is-- actually, it's shared accountability across the whole of MYOB. We all have an OKR or a goal that we use AI every day, and that's a catchphrase that we all have. That's actually a responsibility that everyone has. My job and the executive team's job is, how do we empower our people to use AI and drive innovation with AI? If I didn't even think about the adoption of AI, there's a shared accountability between our people experience team and technology where we are co-sponsoring an AI-enablement capability, which is us thinking about, "How do we support our teams to do AI effectively for their roles, but also safely within the right guardrails?"
May touched on, before, that we've got a number of tools that we've rolled out across the organization. One tool, we call the AI Everyday Hub. That's a place where people can go to understand the tools that are available to them, provide some guidance as to how they can use AI, but importantly, it's a resource which talks about the stories of learnings we've had around AI; the good ones and the bad ones.
Naturally, people think to themselves, "Actually, AI is probably something for the tech team, or AI is something for another team over here," but we have stories from every department across the organization around how they're using AI. What that does is it goes back to those points made a little bit earlier around the "us" myths. The mindset becomes not, "It's not relevant for me," but actually, the mindset is, "What is possible for me? What is possible for my team? What is possible for my department?" We really open up that curiosity and that growth mindset around, "How do we use it?" Then, May also touched upon some of the governance processes we've put in place.
Daisy, which is our design authority for AI. We've got an AI radar, which tracks the use of AI tools, and that's used in a couple of dimensions. Its use is, what tools are being adopted right now and are readily available across the organization? It talks about the tools which we're evaluating, but also talks about the AI tools we're retiring. The cycle time of AI evolution is really short and sharp, and my job as a technologist is to make sure that we create a technology architecture and environment where we've got flexibility. Because this space is moving so quickly, we need to plug and play different AI capabilities at different times.
I think my last check was, there's 1.8 million LLMs now on Hugging Face. That's nearly 2,000 LLMs that have been written every day since the invention of ChatGPT. We can't keep up with that. All we can do is make sure they've got an architecture and a framework that allows us to plug and play the right things at the right time. We've also spoken about things like training and communities of practice, and I really liked the reference that May made towards prompt engineering.
We believe that with better prompts, you get better outcomes. We've done a number of lunch-and-learns with our teams around a framework called CoStar. That's really helped me personally around, "How do I think about the prompting that I'm doing, be it in Google Notebook or Cursor, or wherever it might be?" For those who aren't aware, "CoStar" is an acronym. 'C' stands for "context." You provide background to the prompt as to what you're asking for and the information, and the context around your prompt. The 'O' is around the "objective," so this is an opportunity for you to define, in your prompt, clearly, the outcome you're looking to achieve.
'S' is the style of the prompt. Do you want the prompt to come back with a style which is professional, personal, advice, consultative? Then you've got the tone; is it polished, funny? Is it casual? Whatever tone you think is right. Then you'd really think about, and really importantly, "Who is the audience? Am I an engineer? Am I an executive? Am I somebody who talks to customers?" You provide the audience into the prompt as well. Then, finally, you define, to the prompt, the response you're after. Is it an email? Is it a Slack message? Is it a code? Is it a generated image? That gives you the best outcomes. The more and more you play with the prompting framework, the more natural it becomes. As I mentioned earlier, with the better prompts, you get better results.
That's just one example with just some knowledge, going back to your comment, "Who owns AI?" It's owned across the organization. We've got some of these capabilities that really help to empower it across the organization. When there's big items to go after, we will partner very closely with our colleagues within the lines of business to think about, "How do we create this outcome together for our customers?" But we always think about doing it safely and responsibly, but also, just going back to one of your prompts a little bit earlier, in a cost-effective way. We do think about FinOps and how FinOps plays out into an ML/AI environment as well.
**Nigel:** I was going to say, I think CTOs and heads of technology will never escape from, one, accountability for it, which is it's going to turn up on your budget. We're all hearing from CTOs the world over about the AI tariff that's appearing on the daily tools that we use from Copilot, document management, HR systems, Salesforce, all those things have now got an AI tariff embedded in them. How do you manage that? Is it just the same ROI thing where you're weighing up the value of those pieces of software versus the returns from them? Because, ultimately, in 2025, not a lot of people have got a big room for extending their budgets to taking on a lot of new tools.
**Simon:** Yes. Look, we're still early days, so we don't have that solved. We have uplifted our FinOps practices. It does look at AI, so we consciously have an approach around looking at AI. A good example is we've just recently launched what we're calling an AI innovation lab. That's got the right controls from a governance point of view, from a security perspective, and it also helps us think about, "How do we contain the blast radius of any costs?" As well.
In this AI innovation lab, we've got some rules of the road, if you like, that guide us, but we're adapting those as we learn more. I think that's probably the piece that I would really urge people to think about, is it's not one size fits all. This is not set-and-forget. You need to be flexible. You need to be nimble. You need to be thinking about, "How do I continually evolve the architecture and our practices and processes to be able to control and to really engage with AI the right way?" Otherwise, you'll constrain it, but you don't want to let it loose into the wild.
There's really this balancing act between constraints as well as going too wild, and going back to that comment I made a little bit earlier, we are very, very mindful about the responsibility we have to our customers, and that is paramount in terms of how we think about safety.
**Nigel:** May, earlier on, you promised real-world and data, and I'm very curious as to what you've got. Simon alluded to some research from a couple of weeks ago about adoption rates. I think there's a lot of people very curious as to what that's playing out like. In a big tech community like MYOB's, what are you seeing? What are the numbers? Are you making progress?
**May:** I'll start with this, but first of all, I think the adoption rate is a really interesting metric, and we're still evolving it because one of the things we learned is, actually, there's no one metric ruling it all. It needs dimensional. That's one of the things, is around, say, we definitely started with a tools-adoption rate and code-acceptance rate because we get that 30% disappointment. We actually want to make it better because we want to understand why. It's not ironic we want to make that number high. It's because we actually understand. We try to understand the "why." Why people do not use the tool, and actually, how can we make the tools more useful? How can we make sure the tools actually deliver value? That's one. Is there any support we can provide in there? I think that's the reason we look into the metrics, not we just want to make the metrics high.
I think we started with that. I think we actually moved to quite a bit of a higher number regarding to adoption rate. I think it moved from 30% to almost 80%. I think a good acceptance rate is to above 30%, around there. I think that's reasonable. One of the things we actually found out is to say, "Yes, it's good." Now, all that remains is the team using it, interacted with it daily as part of their day-to-day, but that actually, even with that number, that does not answer the question about, "What does this mean? What does this mean, actually, for our overall outcome from a business point of view, for our developer experience?"
We still can't actually answer that question. One of the pivot points we're driving is, actually, we're following the adoption rate, and now, we're actually moving to use cases. That's one of the things, is really around addressing the friction points and waste of the entire process. I think, actually, it's what Danni has said regarding the system can decide up to a 90 to 95 performance. It's not just one tool. One of the things I think we're looking to is, really, definitely looking into this way from the system point of view. Looking across the entire system and around to say, "Let's address the pain points," because, in that way, you will be able to have a clear answer around, "How does this impact the business? How does this impact each of the individual teams around the whole developer experience?"
One example I want to call out is actually regarding the team have been using AI to improve, say, how do they do incident management? As you all understand, every time when those incidents happen, it normally-- actually, that it takes the team around, at least, 30 minutes to go through everywhere, checking the monitoring, alerting, the logs, and checking the health and everything. Try to understand what's going on to say, "What's the action I need to take?"
Actually, the team has built a solution using AI in that case. Right now, when those incidents are triggered, it's basically just a summary is done by AI. You basically get a summary around the incident and the action points you need to do in two minutes. If you're thinking about this, 30 minutes to 2 minutes, 96% of improvement. That's actually, how do we look into the-- Then, if you're thinking about how many incidents we have across the entire organization, I think the impact to business is actually very clear.
It's not just the dollar value. It's also about, say, the response speed to a customer, to minimize the impact to customer, actually improve-- provide a better customer experience.
**Nigel:** Simon, question for you. We get a lot of architect-level people listening to the Thoughtworks Podcast over time. Thinking about the architecture of MYOB, and your team structures and the structure of your code, it's a very long-running business, so I'm sure there's some legacy hiding in there somewhere. How are you tackling that holistic problem that May just talked about, that, "It's the system here, it's the people and the process, and the existing code." You've got software architecture. You've got org structure. You've got processes. How are you juggling all of those to optimize for this adoption of AI?
**Simon:** Yes, and it's an opportunity still to be solved. I would say that we're doing it quite mindfully and taking the approach that we can't fix everything simultaneous. Therefore, what do we go after? And, what's the sequence of events that we think is the best sequence? You're right, Nigel. Like any 30-year-old business, there's a level of legacy in the system, but what we're seeing is that, actually, with some of the legacy comes opportunity as well, and I might use the example of the engineering tools that we've rolled out recently.
Originally, we rolled out GitHub, Copilot, and that was just using OpenAI as the LLM. Our uptake was pretty poor. The adoption, as May mentioned, wasn't that flash. What we've realized is that just from speaking to the engineers and what's important to them, we opened up GitHub, Copilot, not just to OpenAI, but to Claude Sonnet as well. What that did was it allowed us to really unleash the power of two models, simultaneous, to teams to say, "Okay, how do you use this? How do you use it with a new code base, an old code base, with a frontend code base, and a backend code base?" And again, I've talked about adoption; we saw adoption rise.
The next evolution of that was-- again, going back to a comment I made earlier, that there's no one-size-fits-all here. We, also, have decided that, actually, alongside GitHub, Copilot, we're going to roll out Cursor. We're going to offer people the choice between the tools, depending upon the domain and the architecture they work within, because it's a fit-for-purpose kind of conversation. This is not saying you've got one email service that you provide. It's Outlook 365 or it's Gmail. This is actually allowing our teams to choose what is fit-for-purpose in their domains.
What we're seeing now is, we've got over 90% of our engineers using one of GitHub, Copilot, or Cursor. We're seeing, as May mentioned, on average, just over 30% acceptance of the-- or code acceptances that have been made, but what we're seeing is, depending upon where you are in the architecture, the acceptance rate can increase to over 40% in some areas, and clearly drop down in others. I think, going back to your question, we will still think about the flexibility of the tools we provide our people. We'll think about, what are the models that we enable into Cursor or GitHub, Copilot?
Another example is going from Claude Sonnet 3.5 to Claude Sonnet 4.0 is a hockey-stick, nearly, increase in terms of the code acceptance we've seen, and that's because just the blast radius of what it was able to do for us has increased. We'll continue to look at that. I think there's still some work for us to do to think about, how do we define the domains and have more fit-for-purpose tools across all domains? I think we're still constrained in some domains, but I think as the tools become more effective, we'll have the right ecosystem that'll allow us to plug and play tools at the right time.
That might be staying with GitHub, Copilot, and Cursor, but just thinking about, what are the backend LLMs we think are more appropriate for the different domains? Hopefully, that gives you a bit of color, how we think about it, but it's a work in progress, I think it's fair to say.
**Nigel:** Look, I think it's really important because a lot of the hype that is being generated is very theoretical cases or wonderful cases of a greenfield's development of a tooling set. Of course, you've got a generational issue coming in here, too, I think, where there's a new generation of people who are just going, "Yes, I'm going to knock MYOB off their number one position by vibe-coding something that--," and we all know. We're all grownups here.
We know 80% of the cost of code occurs after that first deployment. It's about maintaining, and it's about tracking. We certainly see a big growth in our practice around understanding code and helping it mature and change generations and go forward. That's the challenge of any enterprise, I think, and certainly something of your scale.
Now, thinking of generational transitions, as we're moving into a world where we'll get a whole generation for whom this is not a big challenge to them, where do you go? Where are the best resources? How do you keep up with this, Simon? What's your secret sauces of tracking what's good, what's not? And, what do you recommend for people? Because people come to this podcast thinking about, "Well, where should I take my career? Which direction?" Have you got any great sauces and things that you're following today?
**Simon:** There's those go-to sources of information, but also, I just keep reminding myself, "Don't be stale. Don't get into habit. Be open-minded." A couple of just places I go; I subscribe to the Superhuman Newsletter, and that comes out a couple of times a week. That gives you really great insight around updates to AI, tech, and tech trends, and that's across the globe. It's not US-focused, it's across the globe, and it goes all the way through to robotics as well, which I think is pretty cool. Seeing AI in a physical sense as well is neat.
There's another newsletter I subscribe to called The Summary AI. It's a short and sharp three-minute summary about AI news, tools, techniques, what's happening, and there's a couple of podcasts. I've been subscribing to a16z, which is Andreessen Horowitz, now for over 10 years. They've got a couple of branches off now.
There's a a16z for AI, would you believe? And that's quite a neat program. I go down the coast pretty often. I love to surf. That's my hobby outside of work. I just chuck on a podcast and immerse myself in that. When the kids are in the car, they're like, "Dad, do you mind if I put the headphones on, listen to music while you listen to your AI stuff?" That happens, but I think really importantly, Nigel, I'm blessed to be working with a really highly-skilled and qualified team. The MOYB team are constantly coming up with great ideas or areas of insight.
We've got a channel in Slack where people post a lot of the insights they have, and I'm forever just troweling through that just to get some insights. For me, it's a great learning because I don't claim to have the answers, but as we all are, we're going on this journey together. For me, it's helped me refine my thinking around AI and my thinking around how AI is here for HI. I think the human intelligence piece is going to evolve and be elevated the more and more we use AI.
**Nigel:** Now, May, I'll put you on the spot here because you're actually the author or the co-author of some of the things I rely on to keep up with artificial intelligence. What is someone at your level, so deeply immersed in leading adoption for Thoughtworks-- how do you keep up? I guess you've got a hotline to Martin Fowler?
**May:** I think that's just a privilege, is definitely around this. I think that one of the things, I definitely feel like I'm really lucky because I think that it's around the Thoughtworkers. We are such a big community. One of the key things is around, I could say, I think "living" is just a general world. For me, it's "real." Even though I work on it every day, I think that it's still very real for me, is around giving to the limited time, and is around, "How do I ensure I spend things on the right things?" One of the primary channels I have to admit I use is actually our internal Thoughtworker community.
We got a community around AI for software delivery. The reason I focus on that? Because those are other information from other Thoughtworkers, I trust it. It's to actually be able to share the comments. This is actually the things we need to watch out for and some of the things we need to be cautious, as well. I think that's one. I really enjoy, say, being part of the community. I think that is really one of my primary channels around this. The other is actually that I also benefit from the MYOB channel around that. I like that MYOB has a wonderful AI community as well.
I think the teams from different backgrounds, from business, from tech, all sharing different insights, I think that's really, really helpful as well because I think it's more like, say, Thoughtworkers as much as a technology community. This is actually what I was saying. What I actually learn from MYOB community is a bit of a business lens. It's from the impact, to the industry, like, "What does this mean?" I think that is really crucial. One of the things is around, say, I just want to highlight one side that I, especially, have been following on, is around, we all know-- with GenAI, I think we know it's still fast evolving.
We don't know everything. It's still changing every day. I did have a conversation with Martin Fowler around this. We've been talking about the only way to success, to influence the future, is actually to experiment, to share. I think Thoughtworks, we keep sharing our learnings with real experiments from Martin Fowler's website around the GenAI series. I definitely read every one of them as they come up, because they are actually talking about the real-time experiments, how do we try around this? I think we have been talking a lot regarding vibe-coding and some of the interesting experiences. We talk about vibe-coding, how does that impact? And people are just, "Hey," because we have Thoughtworkers experimenting different things on this one, and report back. It's more from experience around-- as someone who have been experiencing building production-grade software.
This is, how do we think? Rather than, say, yes, just using this as a hobby. I think that we're really, really thinking around, "How do we actually turn this into production-grade software?"
**Nigel:** On the bombshell that neither of our two guests today rely on TikTok to keep themselves up-to-date with what is going on with this new generation of technology entering the workforce, I reckon we can wrap this up. There's a lot more information to be had, and we'll put in the shownotes a whole bunch of links from thoughtworks.com and from MYOB as well. I absolutely want to point out a very, very cool customer video where they're introducing what AI might mean to those folks running a small vineyard in Hunter Valley.
Accordingly, I think we'll end on Simon's wisdom; use AI every day, build the muscle, and have the conversations accordingly. I'm duty-bound to say, if you enjoyed this episode, please help spread the word. Give us a rating, a thumbs up, and ding the bell, all those sorts of things, on iTunes, Spotify, or wherever you get your podcasts. You could hear a lot more conversations like this on thoughtworks.com/podcast. Thanks, team. Thanks for taking the time out today and giving us those real-world stories, and I look forward to-- I don't think we're going to wait a year before we hear about revolutionary progress and what's going on at MYOB, so we might have you back in six months, Simon.
**Simon:** Yes. Thank you, Nigel. Thank you, May. Really enjoyed the time. Thank you.
**May:** Thank you, Nigel. Thank you, Simon.
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
[ Read Technology Radar ](https://www.thoughtworks.com/en-th/radar)
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