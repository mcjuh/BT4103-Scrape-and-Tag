<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/unleashing-the-power-of-technology-and-business-transformation | Title: From stagnation to success: Unleashing the power of technology and business transformation | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  From stagnation to success 
Unleashing the power of technology and business transformation
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Knut Talman and Matthias Wlaka
November 27, 2023 | 25 min 49 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/unleashing-the-power-of-technology-and-business-transformation#transcript)
Listen on these platforms
## Brief summary
How does an industry titan like OTTO, spanning retail, logistics, and online marketplaces, embark on a transformation journey that ensures relentless competitiveness? Knut Talman and Matthias Wlaka, share the strategies that empowered OTTO to pivot with agility, craft innovative business models, and leverage technology to achieve seamless, uninterrupted growth. If you are a leader embarking on a transformation journey, this is the podcast for you.
### Episode Highlights
Knut and Matthias shared their learnings from leading OTTO through a large scale transformation:
  * **Start Small, Iterate Quickly:** Begin with Minimum Viable Products (MVPs) to rapidly roll out basic functionalities. Gather feedback early and often to refine and improve offerings based on real-world usage.
  * **Embrace Agile Methods:** Move away from traditional, lengthy planning phases towards agile methodologies. This shift allows for flexibility, quick adjustments, and iterative development, crucial for adapting to changing market demands.
  * **Involve Senior Leadership:** Secure buy-in and active participation from senior leadership and board members. Their support is critical for providing resources, guidance, and ensuring alignment with the overall vision.
  * **Customer-Centric Approach:** Continuously engage and involve customers in the transformation process. Collect feedback, iterate on designs, and focus on creating a seamless and satisfying customer experience.
  * **Bridge Business and Tech:** Ensure a strong collaboration between business and technology teams. Having business-oriented product owners who understand existing processes while being open to innovation is essential.
  * **Transform Mindset** : Encourage a cultural shift towards a more adaptive and open mindset. Embrace change, encourage risk-taking, and foster a culture of continuous learning and improvement.
  * **Utilize Cloud Services:** Leverage the benefits of cloud platforms for scalability, flexibility, and enhanced technological capabilities. Consider a multi-cloud approach to diversify and optimize services.
  * **Endurance and Patience:** Understand that transformation is a challenging and continuous process. It requires patience, endurance, and the ability to learn from setbacks and challenges.
  * **Feedback Is Key:** Establish mechanisms to collect and act upon feedback regularly. Customer, partner, and internal team feedback is invaluable in shaping and refining products and services.
  * **Collaborate and Learn:** Collaborate with partners, learn from their experiences, and be open to adapting your strategies based on market dynamics. Continuous learning and adaptation are vital for long-term success.


## Transcript
[music]
**[00:00:00] Kimberly Boyd:** Welcome to Pragmatism in Practice, a podcast from Thoughtworks where we share stories of practical approaches to becoming a modern digital business. I'm your host, Kimberly Boyd, and I'm here live at ParadigmShift with Matthias Wlaka, vice president of IT at Otto Marketplace and CTO of Otto Payments, and Knut Talman, vice president of IT Logistics & Services at Otto to explore a topic that they are very passionate about, transformation at scale.
Matthias and Knut, welcome. Thanks for joining us here in LA at ParadigmShift. We're very excited to have you. As a longtime partner of Thoughtworks, I'm familiar with who Otto is, but our listeners might not be familiar with them. Maybe you could start by telling us a little bit about who Otto is.
**[00:00:45] Matthias Wlaka:** Of course. Thank you for having us. Excited to be here at ParadigmShift. Otto is a German online retail firm and has a quite long history. After the Second World War, Dr. Werner Otto had pictures of shoes and then he glued them to a little catalog. That was a first--
**[00:01:12] Kimberly** : Oh, he glued them. [laughs]
**[00:01:14] Matthias:** Yes, so it's a long history and this is when it started. He sold shoes online. The trick to not have fraud at something, he only sent one shoe out, then you could try the shoe. If the shoe fit, then if you paid, then he sent out the second shoe. This was how the business started. Of course, now, many, many years later, it's a completely different business model. What I think we want to speak about is the last pivot of this business model.
**[00:01:47] Kimberly** : I'm assuming there was probably a need for transformation if you're moving from the pasted-on, very physical mail catalog to where we are today, but maybe you could talk a bit about what prompted the need for this transformation.
**[00:02:00] Knut Talman:** Otto was always transforming itself. There was never any period in time where they stood still and say, "Okay, we are making some revenue. That's great." In the mid-'90s, Otto started sending out CD-ROMs. The older listeners may remember what that was.
**[00:02:20] Kimberly:**[chuckles] Netflix used to do that too, so you're in good company. [chuckles]
**[00:02:23] Knut:** Indeed. Then later on, followed by an online shop, so that's when the age of the internet dawned also on Otto. Actually, I think they were the first in Germany and that's why also the only mail-order company, which is still there globally. Then we saw that even though Otto was still growing, it was losing market share. The other competitors mainly from US and nowadays also China grew much, much faster. To overcome that, there was that vision, "Okay, let's create a marketplace." Now, it feels like an ages ago, but it's only six, seven years ago where we actually started working on that, and here we are.
**[00:03:07] Kimberly** : That is ages ago in transformation years though, right?
**[00:03:09] Knut:** Exactly, yes. In transformation years, yes. Listeners cannot see me, but I had the longer and less gray hair before we started, but all jokes aside. We were looking for a partner we could trust and who was fitting our culture. We found that partner in Thoughtworks and that's why we're here.
**[00:03:29] Kimberly:** Well, maybe if I can ask you both to think back six years or so when you were just going into this transformation effort. What was it that you were perhaps most worried or concerned about as you headed into that and did that end up being the most challenging thing now that you're at the tail end of this transformation?
**[00:03:50] Matthias:** It started out a bit of a technical transformation. The legacy of Otto technic-wise is like a host mainframe system with 40-year-old catalog processes as it's a catalog business. We transformed this into a still monolithic but a bit more modern Java-based solution. When we planned that we want to become a marketplace, it was very early in the process clear that with the 40-year-old catalog process system, it will not work. We had too many limitations and we said, "We need to completely redo the system." That was a big challenge stakeholder-wise because it costs a lot of money. It's a risky undertake.
At the same time, we were not really sure how to start with it. We wanted to have something in the cloud. We want to do agile product management and all these fancy things and we had only little experience. The first big challenge was, how can we start with it? How do you shape the solution in a way that you can then do product development and how would you do this in the cloud? We needed help to really understand how this works. How can you start? How can you shape the solution and start the first teams? It was the biggest challenge at the beginning.
**[00:05:21] Kimberly:** Where did you start? Where did you determine was the place that made the most sense to dig in and get this kicked off?
**[00:05:29] Matthias:** Well, what we did is we wanted to do something new and one cultural elements where, for example, we decided we want to create something new, so we need a new location. We left our Otto campus, rented an office building down the road to create a little startup thing. We decided we want to create something new, greenfield next to our legacy system, and we started small with three teams and really tried to create this startup here.
How we created the teams was, I think, quite specific. We wanted to bridge the gap to the business. We wanted to have the product owner from the business side. That took some time to find the right candidates with a good business mindset and understanding of the current processes, but at the same time with an open mind so that they could really think about something new. We started small with three teams, so we needed three product owners from the business.
We were then identifying cool tech people from our legacy tech community, which were willing to really learn something completely new. With this, we started small teams, then established them. We asked Thoughtworks to help us with inception to help us with understanding how agile product management works, how cloud works. We had Thoughtworks in this process, more or less, from day one to really get these initial three teams going. That worked pretty well. That was a very good approach.
**[00:07:17] Kimberly:** Great. I love that you were talking about finding some space down the road to help you really embody that startup mentality because I think all the big startups started in garages, right? This is Otto's version of doing that. Knut, maybe a question for you. Matthias was just talking about finding product people and having them work with the technology side of the business.
Since we're reflecting on transformation today, I know that's often a challenge for a lot of organizations is successfully bringing product or business and tech together to the table. Could you share what some of your learnings were in doing that like what worked well, what you might have changed knowing what you know now?
**[00:08:00] Knut:** Yes, absolutely. I think one of the key elements was that, as Matthias just described, it started small. We went away from the traditional approach. Most of the companies do. They look at a waterfall model. They try to figure out everything before even starting. That's impossible as we know. We have seen many, many projects fail also within the Otto Group. Doing it that way, we said, "Okay, let's start with these three teams. Once they are ready and live and up and running, let's grow."
We're now at 150 teams. Most of them working very closely with the business, so that's another element. What we thought is essential to doing that so that you have immediately the buy-in from the business because they're part of the transformation. We're not only doing a tech transformation. We are doing six transformations in one go.
It's tech, it's business, it's capabilities, it's how we make money, it's cultural, and it's the way we work. Every one of those transformations we did starting with baby steps. Just have a few people starting to learn English, starting to speak English within the business on a day-to-day basis, so have your standups in English and all that. Wherever you look, we started small.
Also, the buy-in from the business, as I said, we moved away from the demand-and-supply model, which usually companies do. Make decisions together, make them fast, and then, obviously, also fail fast if it was not the right approach but realize it immediately, and then take the next step. Learn from it and grow from it. I think also that we separated from them at the beginning was very good.
Later on, we brought them back on campus. They integrated with the rest of the team so that they all could benefit from it. Also, Matthias' organization started first. My organization followed two years later. We learned a lot from what they have gone through. All the things we should be doing and we should not be doing, we knew already, but also we did some other things.
When we came on board, we developed a multi-cloud concept. Now, we are even more attractive, even more agile, even more scalable because we're using multiple clouds and so on. It's a long process, but I think you must not be afraid to jump into it to do the first step obviously. We had enough people willing to do the first step. That helped us massively to grow that product and be where we are now.
**[00:10:46] Kimberly:** Great. It definitely sounds like starting small and then looking to embed that in the rest of the organization helped be a key to scaling it successfully.
**[00:10:54] Knut:** Yes, it doesn't work any other way. That's what we are convinced of.
**[00:10:58] Kimberly:** You mentioned a multi-cloud approach was a way into the transformation. It was something that you adopted and it's given you more flexibility. Is there any other technology that you've adopted as part of the transformation that you feel has been really pivotal to the success and scale you've been able to achieve?
**[00:11:16] Matthias** : I think from a technical perspective, we do what everybody does today with AWS and GCP. We have the main two hyperscalers online. I think from the methodology next to the start small, what we did was a lot of MVPs really, so minimum viable products, to get something out there fast and then try. That was, for our organization, something new. Otto loves to do long analysis, loves to do design phases, and create big piles of paper where everything is described.
**[00:12:00] Kimberly:**[laughs] The legacy paper in the business.
**[00:12:04] Matthias:** That's where our heritage is and this is how many people are somehow used to work. We really did not do that at all. What we did for the partner site as marketplace, we needed to somehow have a partner site to attract onboard partners. It's a component we call Otto Partner Connect. The first MVP of Otto Partner Connect was extremely minimal, so the very basic, basic functions. People were concerned to really go to market with such a minimal, minimal product, but we found partners who knew us well.
We had two partners helping us on the way. We asked them to try this very basic functionality. What they did is they used it. They used it really in real life. It was not a mockup, but it was a real life. They gave us immediate feedback, what they would expect, what they would like to see compared to their experience with other marketplaces. We directly used this feedback and created a product that really suits these partners very well. I think we couldn't have done this if we would've thought through with our limited knowledge about marketplaces.
How would you build a marketplace that does not work that way? With MVP, we put something out, got immediate feedback. Some things we got right, some things we got wrong. We fixed it. Step by step, we created an environment that really works pretty well for the partners. Even today, the feedback that we get from our partners is very positive on this interface. I think this iterative approach to bring something alive fast, get the feedback, and then optimize it work very well for us.
**[00:14:00] Kimberly** : I know you said it was very minimal, but it sounds like even though what you initially rolled out was maybe basic and functionality, it ultimately enabled you to move a lot faster than spending forever trying to get it perfect and then learning that it's something your partners didn't even want. In talking about the partners in that process you just talked about sounds very similar to also how you approach customers and understanding what matters to them.
Obviously, you were transforming for Otto but with the intention of it ultimately resulting, I'm assuming, in a better experience for your customers. Can you talk about the role the customer played in your transformation journey and how you really brought them into the center of everything that you were doing?
**[00:14:43] Knut:** Obviously, as a retail company, the customers and the partners who are also a customer of our marketplace play the most vital role in every process, even though we took some risks in the transformation that we say, "Okay, there are certain transformation steps where we need to implement something, where we know the customer will not be very happy at the very beginning."
Right now, when we're moving customers from our legacy system to the new world, there are certain elements, certain functionalities, which do not work right from the beginning, but they will be coming in two weeks, four weeks, six weeks because that's how we roll now with the continuous integration, continuous delivery. Even though in all the process when we think, "Okay, how do we want to do this like that onboarding of a partner," it needs to be self-service obviously. We want to reduce any frictions a partner could stumble into.
We worked also there with some pilot partners. They were an essential part of that process design. There were multiple iterations, "Okay, how do we want to do that? Okay, that doesn't work, so let's do it better." We wanted it to be a very precise, very short with very few steps for the partners, for the customer who's actually buying them, those products we sell and the partners are selling. We have multiple also, how do you call that, engagement groups. They're testing the customer journey.
They're making proposals how that could work better. To be honest, after almost 75 years of being in the business, we know pretty well what the customer wants and needs. We are trying to embed that into every process we do now. Just one more thing. Obviously, mobile is extremely relevant. Before we started the transformation, we had, I think, 9% of our customers coming through mobile applications. It's now half. We developed also the mobile applications as part of the transformation.
**[00:16:52] Matthias:** Maybe to add some more numbers to make this a bit more tangible. When we started the transformation, we had about six million regular customers. Now, we are up to 13 million. We more than doubled. I think it looks like we do some things right. Customers appreciate. I think the thing that they appreciate the most is that they find the products they're looking for in our shop now.
If you are a retailer and if you purchase all the goods on your own, it is impossible to have the variety the customer is looking for. We have so many competitors out there and they have millions of millions of products. When we started the transformation, we had several hundred thousand products online. People did not find what they were looking for. They were frustrated of the fact that, "I want to shop at Otto, but I can't find it. I go to someone else, and there I can find what I'm looking for."
With the marketplace now, we have so many partners online. We started with zero partners. We now have more than 6,000 partners online. We have close to 17 million products online. It's a massive change in how the customers can search for the products they're looking for and what they find at Otto. Now, we are relevant again. That was an important element of this business transformation. How can we make Otto relevant again in the market? I think this was a marketplace that worked out pretty well.
**[00:18:29] Kimberly:** I would say it sounds like you're quite successful in making Otto relevant again. Double the amount of customers from 0 to 6,000 partners, that's really a fantastic value story.
[00:18:40] Knut: We wanted to have also a very seamless checkout process. That was a hurdle before we did the transformation. Because if you would go through a checkout and you would have a mixed basket, so a partner selling and Otto selling, you had to go through the payment process twice. We were not allowed to collect money for our partners. That's why Matthias' team, they founded a bank. Otto now has a separate company, Otto Payments, which is actually a bank.
**[00:19:10] Kimberly:** You thought you were a retailer, but you're actually a banker. [laughs]
**[00:19:12] Matthias:** Yes. What Knut described shows a bit of the downside of this MVP approach. During the process, you have times where the solution is not ideal. We created a greenfield new system. At the same time, we had to operate our legacy system. The traditional retailer run on the legacy system and the marketplace run on the new system. The customers experienced this through two checkouts, which is, it's annoying and it's bad for the conversion.
That had technical reasons, process reasons. One was, as Knut described, our business model provides customers with "buy now, pay later" features. As we sell furniture, TV sets, all these things, customers appreciate the "buy now, pay later." In Germany, for regulatory reasons, if you touch third-party money, you need to have a bank license. That's why we, pretty early in the process, realized that we need to have a dedicated payment solution with a bank.
We created Otto Payments and we reused all the experience that we made in our transformation with the agile and the product development. We copy-pasted that all to Otto Payments. The thing was when we started Otto Payments, it was at the same time as COVID hit us. We had to do this all in remote, which was an additional challenge to set up a complete new company.
I think it also shows the quality of the people, of the processes because we were able to really, in three years' time, get the company up and running, get the core banking solution up and running, obtain the license of the regulator, and had the first customers then on Otto payment. Now, with the migration, we are now in the step where we migrate all the legacy to our new solution and migrate 22 million customers to Otto Payments as we need to migrate the historical ones as well. We think we will be done with this in three weeks or so. I think the fact that we sit here and make a podcast with you shows that it works quite smoothly. [laughs]
**[00:21:35] Kimberly:** Yes, you seem very calm and collected moving 22 million customers over to a new system.
**[00:21:40] Knut:** I wanted to add one more thing about your question. How do we engage with the customer and how do we involve the customer in that whole process? Obviously, we collect customer feedback and we have a whole team looking for and looking at customer feedback. They build reports and distribute that amongst the senior management. We do look at it. It's part of the business routine. If any of the Otto customers are listening, please continue to provide feedback. We need that.
**[00:22:07] Kimberly** : I love the feedback plug.
**[00:22:08] Knut** : It adds another perspective to help us becoming better every day.
**[00:22:13] Kimberly:** Well, I'm guessing they're going to give very favorable feedback now that they have the single-payment solution and don't have to pay multiple baskets. I think that's a big home run right there. If you had to reflect back on the past six years, what advice would you both give to other digital leaders that are looking to go on a similar transformation journey in their organizations?
**[00:22:51] Matthias:** I think the first thing is it is possible even for a pretty large, historically long-grown company with old processes. Our process were really old, 40-year-old catalog-based processes. Transforming into a modern marketplace is tough, but it is possible. I think when I speak to other CEOs, leaders, the first step seems to be pretty hard to convince the board, to convince the key stakeholders that it is possible to take this journey. It is possible. Give it a try, but do it properly.
What we did from the beginning was we involved all senior stakeholders and board members extremely direct. In many, many meetings, we had full buy-in of the board. Of course, they provide us with funding, but it's way more than that. With the shareholders, to make sure that we get all the support needed in this transformation, especially over such a long time, it is so important to have the senior leaders on board. That, I think, is really important.
I spoke to another colleague and he said, "Oh, you managed to do that?" I just have a quarterly report and tell him how it's going. I think that's not sufficient. You really need to have a very in-depth involvement off the board with a business transformation like that because it changes the whole company, right? It changes the way of working for so many people, so many colleagues, way more than just the tech people because it's a business transformation.
**[00:24:38] Kimberly:** I call that getting everyone in the boat with you. Y'all have to all be in there together to be able to sail to where you want to go. Knut, anything you'd want to add?
**[00:24:57] Knut:** It is a painful process. You need endurance. You need stamina and a lot of patience to go through that process. If the wind blows hard into your face, turn around and use that to help you push you forward. You need people with the right mindset. All the things, we now said multiple times with that MVP approach, not waterfall.
I'm 100% sure that if we would've done it the traditional way, we would not be sitting here in that relaxed way we are now. Thoughtworks helped us also along the way to find the right measurements to write with OKR and KPIs. How do you do that anyway? I think that's part of the process. Again, that mindset is crucial on all the levels.
**[00:25:51] Kimberly:** Well, it's very much been our pleasure to be a partner with you on this and see what you've all built and accomplished together. I think it's been very exciting and you shared some of the results you've experienced to date have been so impressive to see. From going from one shoe you would get in the mail to 70 million different products in your marketplace, it's definitely impressive. Thanks so much for spending time with us today and sharing a bit about the transformation journey.
**[00:26:15] Matthias:** Thank you.
**[00:26:16] Knut:** Thanks for having us.
**[00:26:17] Kimberly** : Thanks so much for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcast, or if you enjoyed the show, help spread the word by rating us on your preferred podcast platform.
[music]
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