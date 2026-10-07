<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/backstage-spotify-developer-effectiveness | Title: Backstage: Spotify's secret to developer effectiveness  | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Backstage: Spotify's secret to developer effectiveness 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Austin Lamon, Spotify
June 13, 2022 | 25 min 11 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/backstage-spotify-developer-effectiveness#transcript)
Listen on these platforms
## Brief summary
Software professionals and their skills are in high demand and organizations are constantly thinking about how to invest in capability development. In this podcast, we speak with Austin Lamon, about how Spotify created the Backstage platform to empower happy developers. Listen to learn more about creating an environment where development teams can thrive.
**Episode Highlights**
This episode is presented to you from our executive conference [ParadigmShift – learn more](https://www.thoughtworks.com/paradigmshift/exec-summary-2022).
  * Developers are spending 30%-40% of their time actually writing code. The rest of their time is troubleshooting incidents, sitting in meetings, interviewing, dealing with security issues, and other areas that may be seen as a burden. What developers want to be doing is building products. 
  * Backstage was born out of the need to onboard effectively as Spotify was quickly growing. Fast forward, the tool is enabling engineers to do their job day in and day out, but also creating these reusable patterns and these sets of tools and really almost codified culture that allows teams to build products. 
  * The technologies developers depend on are constantly changing and evolving, so if we look at one lagging metric, it's all about satisfaction. It's all about, "Are developers happy" and broadly, "What's helpful?" That's where satisfaction comes in.
  * Focusing on developer satisfaction enabled Spotify as an organization to retain top people.
  * Start by just asking people how they're doing, and then, two, start putting metrics on those things that are the biggest problems. Once you're measuring them, it makes it a lot easier for organizations or teams, or individuals to feel empowered to test ways to move them.


**Transcript**
**[00:00:01] Kimberly Boyd:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks, where we share stories of practical approaches to becoming a modern digital business. Today's episode is brought to you live from New York at our executive conference, ParadigmShift.
In a roomful of enterprises from various industries, a common theme has emerged. To succeed, we need to create an environment where our development teams can thrive. Our guest today took to the stage to share how his organization created the right mechanisms for developer effectiveness.
I'm your host, Kimberly Boyd, and I'm here with Austin Lamon, Head of Backstage at Spotify. Welcome, Austin. Thanks so much for joining us at ParadigmShift. We're excited to have you here with us. To get started, why don't you share a brief intro, tell us a bit about you, and why this topic of developer effectiveness is important to you and to Spotify.
**[00:00:48] Austin Lamon:** Awesome. Thank you so much, Kimberly. I can't understate how much of a delight it is to actually be in person. I've recorded a few of these podcasts over the last few months, here's what have you, and none of them have been in the same room. Definitely looking forward to the conversation.
To start with, my name's Austin. I've been at Spotify for the last few years now, but always and even before Spotify, working in the world of building platforms and building tools for developers. I almost think of it as what is it that's needed to build a car? What is it that's needed to build a plane? There's all these different aspects and components that we think of in a factory or what have you.
As an engineer, there's all those tools and componentry as well, and they all live in software. My career, my time at Spotify has all really been focused on how can we create these reusable building blocks, how can we create this machinery that enables organizations and developers to build software and products effectively? I'm a software engineer turned product manager, now working at Spotify, leading a platform called Backstage.
Really, the story behind Backstage starts four or five, six years ago before I was even at Spotify. Essentially, Spotify was growing really quickly. We were in this state of every new engineer was actually least productive than the one before them. It was really, really hard to figure out how do you actually contribute at Spotify?
It started really with engineers, but it was also through product managers, designers, other functions. There was all this tribal knowledge you really needed to be effective. Backstage was born out of this need to onboard effectively and it was on both sides. We had both people joining, wanting to be productive, struggling, a little bit disappointed in that onboarding experience.
Then we also had the existing population of people who were saying, "I'm spending all of this time onboarding new people. I'm not doing anything productive." There just wasn't the mechanisms or tools that allowed new joiners to be effective. Backstage started with this metric of how can we really measure and make onboarding more effective, and now fast forward, became this tool for really enabling engineers to do their job day in and day out, but also creating these reusable patterns and these sets of tools and really almost codified culture that allows teams to build products.
Backstage is an open platform for building developer portals now. Within Spotify, it's our developer portal, 91% of people in product engineering and design at Spotify use it every day.
**[00:03:20] Kimberly:** Who is that other 9%? What are they doing? [laughs]
**[00:03:21] Austin** : [chuckles] They're the ones who are taking their own vacation is what I like to think. It's like, "We only measure it Monday to Friday." There's, obviously, a stiff drop-off on the weekend. That other 9%, I don't know what they're doing.
It's tried and true within Spotify. It's how we contribute code. It pulls all of our tools into one consistent UI so developers can really be more effective and now having open-sourced it just over two years ago, we have hundreds of companies using it as well. Really, really excited to continue to export as much as we can all of this learning and really try and elevate productivity and effectiveness for developers outside of our four walls.
**[00:04:00] Kimberly:** I'm always curious-- I don't know if you know this or not, but I love the name. Do you know how the name came about?
**[00:04:06] Austin:** Yes. The name, I was not there at the time but like all things at Spotify, Spotify is known for this autonomous culture and really trying to, at the highest level, define what are the problems we're trying to solve? What are the businesses we're trying to go after? Then enabling these units and individuals to really make their own decisions, figure out the solutions, figure out the path to getting from A to B.
Backstage and really naming anything starts with the team that's solving the problem. There was a small team, four or five engineers, a designer, a product manager in a room, brainstorming what they should call the thing and Backstage won on the day.
It sort of, I think, make sense. The first real use case we had within Spotify was this idea of provisioning capacity. Essentially, we'd move from the data center into the cloud. Even in the data center days, we needed to be able to spin up resources somewhere to execute some software to do some job. Backstage was sort of the thing behind the scenes that was controlling the puppet, if you will, and allowing us to create new resources.
I think the name grew out of that first use case, but like anything, it was some engineer who had an idea who brought it up at the right moment and time. Now, here we are, probably four or five years from that moment.
**[00:05:28] Kimberly:** As a marketer, I love it and appreciate it. I'm very impressed that an engineer came up with that. I think it's a fantastic fit. Austin, you talked a bit about the creation of Backstage, was born out of really trying to up and turn around that trend on developer productivity that you were noticing in the onboarding cycle. Can you talk a little bit about what came next in that journey as the tool, obviously, expanded and helped do things other than just accelerating your onboarding capability?
**[00:06:00] Austin:** Yes, for sure. For us, there was this moment of, "Okay, what are we actually building here?" We weren't building a developer portal. I would say, at the time, even now, to a certain extent, the definition of a developer portal is almost a fleeting thing. It's something we've spent a lot of time trying to work with the industry to understand like, "What does that actually mean?" Those two words that people often put back to back, but what do they actually mean?
For us, candidly, we stumbled on what became our definition of a developer portal. It started with onboarding and then there were other metrics that we cared about. Sort of like any product-driven company, we have metrics, we measure them, and then we find ways to improve them, whether that's increasing MAU or increasing the effectiveness of our teams.
It started with onboarding and then it went to how can we accelerate the deployment frequency of back-end engineers, or how can we make the cycle time of shipping a feature just a little bit faster? Over time, with Backstage, you can almost think of it as this stacking on of new metrics and new problems that we wanted to solve and we wanted to pull together in this experience. Then, I guess, talking to a marketer, inverting it.
What it turned out to do was just create a place where developers within Spotify, whether their job was to build tools for other internal users or not, it became a place where they could go to market. They could take some piece-- Something they hated about their day-to-day, they could literally build something pretty quickly, and then they could use it the next day to solve that problem. Then they could allow others to do the same.
They could see analytics and metrics on how that thing they built was performing. It really became this way where, "Sure, we'll start with onboarding and we'll start with cycle time and these other metrics that we care about." Sort of a more organizational or company level, but then it became about controlling your own experience in your own day-to-day as a developer, regardless of where you were within the organization or what your focus was. I would say we started with onboarding, we added on a few more metrics, then we got really, really broad. Then we saw, "Okay, this is madness."
[00:08:08] Kimberly: [crosstalk]
**[00:08:08] Austin:** Yes, no, it was total madness. It was like, "Okay, we need to figure out what are these core jobs to be done that developers need to accomplish?" It really started with that, yes, that total broad flaring, if you will, and now we've really tried to bring focus to it. That's where this definition of developer portal comes from.
Now, it's all about three things, being able to create software consistently and effectively, being able to manage all the software that you and your team own and depend on, and being able to explore the ecosystem of your company or of Spotify and understand what's out there. Find documentation as you’re onboarding or find the capability that maybe you're the first one who needs it, but probably not. We can make those things discoverable and reusable through Backstage and everyone's more effective.
**[00:08:55] Kimberly:** You talked a little bit about metrics and now those three things that you kind of narrow the focus back in on. How are you quantifying and measuring that you are delivering on those three primary objectives? What does good look like for each of those?
**[00:09:11] Austin Lamon:** Totally. I guess I would separate the metrics question a little bit then from what good looks like for those things. We certainly have metrics tied to them, so from a creative perspective, we'll look at what is the consistency across our fleet? Of all the components that are out there, if I'm a developer working somewhere in our mobile app, and I'm dependent on a system, or if I'm a developer working on a Spotify web app or something else, what's the consistency of the components such that I could contribute to something that's outside of my team and be able to control my own fate or make a change quickly?
Consistency and the time it takes to create something new or what we care about from a creative perspective. From a manager and an explorer perspective, it gets a little murkier because then it's really about this sort of product of a developer portal, and we're almost looking at very specific metrics of how quickly do you find the thing that you're looking for, or how can we better personalize the home experience?
I think when we zoom out and think about Backstage holistically, really where we're focused now is around what is the broader satisfaction with the tool itself because all of those use cases are changing day to day. What developers are trying to do, the technologies they depend on are constantly changing and evolving, so if we look at one lagging metric, it's all about satisfaction.
It's all about, "Are developers happy and do they--" They don't have to use this tool. They don't have to use any of these tools. They can build something new. That's the power of being a developer whose job it is to both write code that helps you be more effective but also builds that end experience from a product perspective.
For us, it's really all about satisfaction at the end of the day. We have very targeted and specific metrics, but I think that gets tied to our ways of working more than, broadly, like, "What's helpful?" I think that's where satisfaction comes in.
**[00:10:59] Kimberly:** Well, also, when you have that 91%, that's telling you there's satisfaction when people are opting in and choosing to use it and then be a part of it. That's a pretty clear indicator that you're hitting the mark at least when it comes to having folks engage with it.
I know you talked a little bit about, obviously, building that consistency, having people have more control over managing, improving effectiveness in the onboarding times, what else has the focus on developer satisfaction really enabled Spotify as an organization to do that they couldn't do before this all started?
**[00:11:39] Austin:** I think the biggest thing it's enabled us to do is actually retain top people, to be totally honest. I think it would be grandiose for me to say that Backstage is the reason that people stay and work at Spotify. I don't think that's true at all. I think it's the culture of our engineering group, the culture of what we call R&D as a very Swedish company. It's the culture and the ability to own and control your own experience.
For Backstage and what is the bigger impact, I think it's all about finding ways to retain and empower people to be happier day in and day out. We have this cheeky tagline that comes along with Backstage which is happy developers make happy code.
**[00:12:28] Kimberly:** Happy code makes happy customers. It's all connected.
**[00:12:31] Austin:** It was honestly part of the open-source journey. When we open-sourced it, it was just a small team of engineers who had a hack week project and they were like, "People have asked us over and over to open source this thing, let's just try it." The response was nuts. It took a lot of effort for Spotify, for all of us across functions, product engineering, design, marketing to figure out like, "What is the right positioning for this thing? What is Backstage?" Because what it really is I think is a representation of our culture and our beliefs and there's a lot of powerful functionality there that can be used for a lot of people.
Specifically tied to Spotify, I think what we're doing is really trying to create mechanisms for our culture to persist into our ways of working and really empower people to work in the ways that they find most effective and build the experiences that are the reflection of that creative passion that brings them the Spotify in the first place.
**[00:13:29] Kimberly:** I think every company's feeling the talent crunch, especially the technical talent and autonomy and having the ability to have the tools and work in the way you need to and want to is so critical regardless of where you work. The fact that you guys have cracked the code [crosstalk]. Cracked the code to make it a little easier and a little more satisfying for developers I think is a big win for everyone beyond just Spotify.
**[00:13:58] Austin:** I hope so. I think one of the-- I don't know, to maybe bring the cloud back over all the happiness of the conversation, I think one of the things that we do is try and really frequently ask people how they're doing and obviously, that's through very specific surveys.
There's a team of incredible data scientists and user researchers that are just focused on our engineering satisfaction at Spotify. They're really trying to measure that for our tools, for our processes, everything. One of the things that I think was almost flooring to me the first time we came across it is that really developers aren't spending that higher percentage of their time writing code.
I mean there's these across the industry even within Spotify, it's developers are spending 30%, 40% of their time actually writing code. The rest of their time is troubleshooting incidents, sitting in meetings, interviewing new potential employees, dealing with security issues, all sorts of things. I think what we've tried to do is really push that percentage. What developers want to do is be building and shipping products and I think it's what can we do to remove the burden of those other things, not to say it will never be 100%. I think people like to think of software engineering as just this exercise and sitting down with a really dark screen [crosstalk] in a dark room, writing code. The reality is, I think of engineering as a far more-- it's a very, very creative exercise and it requires a lot of back and forth and engagement with other individuals of other diverse disciplines and backgrounds and domains and being able to break down problems to their smallest scale, and then build up these amazing solutions.
I think it's much more creative or artistic than people often give it credit. I think the more you can, one, enable people to spend time doing what they want to do, which in that moment might be writing code, it might be finding other prior arts within the company that they can lean on or use. It might just be finding a way to connect with another individual in the company who's working on similar problems, even things-- One of the most heavily used features in Backstage is search and it's not just people searching for other code that they can pick up and use, it's people searching for other people who have the same skills.
**[00:16:19] Kimberly:** Who is doing the same thing?
**[00:16:20] Austin:** Yes, exactly. I think it's-- I don't know, I'm rambling at this point because I'm very passionate about the idea that I think we don't think about, one, the creative aspect of engineering enough, and two, I think developers are just spending a lot of time doing a lot of other things that even if you look at it from a top-down business perspective, that's not good for anyone, they're not doing what they want to be doing.
**[00:16:46] Kimberly:** The core thing.
**[00:16:47] Austin:** Yes, they're not delivering the impact that you think or through the mechanism that you think they are by writing code. It's so much more than that and if you can take away or strip away as much of the negative stuff as possible, I think that's where you get happy developers and happier code.
**[00:17:05] Kimberly:** Is it also fair to say too, you're talking about 30%, 40% of the time is spent writing code, delivering code, and then the remainder is on all these other things. Backstage kind of helps aggregate some of the other things, right? You may have to be doing them, but you're not also going out to these independent various places, so you get a little kind of, I guess, bundling effects via that?
**[00:17:31] Austin:** Yes. I think when you think about it, even if you were to look at any company that's building and shipping software as part of what they provide from a B2B or B2C perspective, they probably have 100 companies that they're paying for software, for cloud tools. It's probably a bit of an exaggeration, but there's so many different components there and each of those pieces is valuable, who's on call for this piece of software? What within our organization is dependent here? How is this rollout going? How many people are using it in this part of the world? Where should we scale up or scale down?
Each of those things I'm labeling, there's four or five SaaS companies who are providing amazing functionality to do that. As a company who's building cars or building airplanes or whatever you're doing, you don't want to rebuild all those things. What you do is you then pull in these amazing tools that have no real focus or awareness on one another necessarily.
What happens as a developer is-- everyone's familiar with an internet browser at this point, you end up with a million tabs, in the simplest sense. You end up with this place you're writing code, you have a code editor, you have somewhere that the code is stored and shared across your team, but then you have 15, 20 other tabs across the development life cycle that allow you to see, again, how are rollouts going, who's on call? All sorts of things.
What Backstage does is helps you aggregate all of those things. It's not trying to be the best tool for any of those, it's trying to give you a really consistent developer-focused view where you can pull all those tools together and you can work with them side by side, and then you can go through to them if you're trying to do sort of a power piece of functionality. At the highest level, you don't have to know every tool, or you don't have to know all the previous decisions that have been made. It's just, if you're trying to create something or manage something existing, or find something within the ecosystem, you know where to go and then that will pass you through to the place where you can update whatever it is you need to.
**[00:19:31] Kimberly:** Backstage, "We will help you decrease the number of tabs you have."
**[00:19:34] Austin:** Literally. Yes. In the simplest sense, that's how I explain it to my grandparents or my parents.
**[00:19:41] Kimberly:** Honestly, sometimes that's the best way to distill it. We got to think about how to explain it to grandma. One thing, Austin, when you mentioned we're like we'll bring the cloud back, that there's still quite a bit of work to be done, I think it is very interesting that Spotify is an organization that a lot of other companies look to as a gold standard for developer practices and just as a kind of leading tech at core organization. I think it is telling how much time and effort that you as an organization are putting into developer effectiveness. It's not something you can just kind of one and done, set it, and forget it type of thing that to have that great talent, to have that engine filling your organization, you're constantly looking at how you can improve it and enhance it, provide those tools, provide that platform.
I think it's, hopefully, not daunting for folks listening who are maybe early in that journey, but just a good reminder that everyone has to look after it and think about continually improving and growing it because it's always evolving and talent is, I think, probably the most challenging landscape we're dealing with today right now.
**[00:20:52] Austin:** Yes. I guess just to quickly build on it, I think one of the things that people ask over and over-- We've met with now, I don't know, hundreds of companies that are considering or in later stages of adopting or using Backstage at scale internally. The thing that comes up, time and time again, is like, "We can't drive adoption of this tool, that people aren't using it, or we have it and it's super valuable."
I think one of the things that I've realized that I even take for granted is people think about, oh, to be this great technology company, you have to just have great engineers building great stuff. The reality is, I think, we have such diverse teams of people that are not engineers necessarily, that are building tools for our engineers. It's not just about engineering. It's not about having great engineers. It's very important, but it's also about design and product marketing and all these different things even for these internal tools.
I think people often overlook that or they often think like, "We don't need data scientists digging through and understanding the effectiveness of our teams, or we don't need marketing campaigns internally for new tools that we want to roll out or changes we want to make to our ways of working."
**[00:21:58] Kimberly:** You do if you want people to adopt them.
**[00:21:59] Austin:** You do or at least we do. I don't know. Maybe someone else is able to do it without, but I think it's often overlooked. It's not just about investing in engineers and engineering experience. It's about bringing together diverse backgrounds and experiences to do just that.
**[00:22:17] Kimberly:** Maybe one more question for you. If the organization who is here at ParadigmShift for us this week, or taking a listen to our chat today is at the beginning of this journey about diving into really getting serious about cultivating developer effectiveness and improving developer satisfaction, what advice would you have for them?
**[00:22:42] Austin:** I would say the first place to start is go talk to them. Go, or you don't have to do it yourself if you don't want to, but fund a user research project into your internal developer experience and just go ask 10 developers across varying levels of seniority, maybe in different geographies, depending on your company set up. Go ask them what it's like. Go ask them what the worst parts and the best parts of their experience are day in and day out.
Go ask them why they might quit. What makes them frustrated with the tools that they're using. What's hard? Is it processes? Is it manual things that they need to do that are blocking them? Is it actually that there's tools that need to be built, or is it that there's too many tools? Is it just that there's this massive, we call it chaos control? Is there this massive entropy in the number of tools that are entering your ecosystem? What are those problems?
Because a lot of people come to us or come to the Backstage team and say, "Hey, we want what you have." Well, your problems, [crosstalk] good or bad, are different than ours. I think it's important. That's I think the place to start, and then that's candidly probably the most important thing to keep doing, to keep understanding what it is that you're improving.
Then if you're already past, you already have some of those problems, then start measuring them. Start finding ways to put blended quantitative and qualitative metrics in place, they'll let you understand if you're making an impact. Because otherwise, it's very hard, it's very frustrating to know if the work or the effort that you or the team is putting in is bearing any fruit.
I think start by just asking people how they're doing, and then, two, start putting metrics on those things that are the biggest problems. Once you're measuring them, it makes it a lot easier for organizations or teams, or individuals to feel empowered to test ways to move them.
**[00:24:38] Kimberly:** Austin, thank you so much for joining us. It's been great to have you here with us live in-person in New York at ParadigmShift. Hope this has inspired folks to perhaps dive a little further into developer effectiveness than they have before. Thanks so much for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcast, or if you enjoy the show, help spread the word by rating us on your preferred podcast platform.
**[00:25:11] [END OF AUDIO]**
[ View more ](javascript:void\(0\))
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
## Don't miss out on the latest episodes. Subscribe today
[ Subscribe ](https://podcasts.apple.com/us/podcast/pragmatism-in-practice/id1474372829)