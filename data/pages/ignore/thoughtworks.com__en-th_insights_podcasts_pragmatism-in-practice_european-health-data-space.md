<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/european-health-data-space | Title: European Health Data Space: The future of healthcare | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  European Health Data Space: The future of healthcare 
[ Pragmatism in practice podcast Back ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice)
Close


Podcast host  Kimberly Boyd | Podcast guest  Khrystyna Shlyakhtovska and Alexandra Lovin
January 28, 2025 | 41 min 39 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/pragmatism-in-practice/european-health-data-space#transcript)
Listen on these platforms
## Brief summary
The European Health Data Space launches this year, promising huge opportunities, as well as challenges, for healthcare organizations. This podcast episode is essential listening for healthcare tech leaders, researchers and policymakers not just in Europe, but globally, who want to understand how to effectively leverage data to build resilient health systems, and foster long-term competitiveness and innovation.
### **Transcript**
[00:00:00] Kimberly Boyd: Welcome to Pragmatism in Practice, a podcast from Thoughtworks, where we share stories of practical approaches to becoming a modern digital business. I'm Kimberly Boyd, and I'm here with Khrystyna Shlyakhtovska, Data Ecosystems Program Manager at AWS, and Alexandra Lovin, Technical Director for Healthcare and Life Sciences at Thoughtworks. Today we're going to discuss the European Health Data Space and what it means for healthcare across the European Union and beyond, including looking at how to approach use cases for the primary and secondary use of data, the challenges, opportunities, technical perspective, and the patient aspects of this new 2025 regulation.
Before we dive in, Khrystyna and Alexandra, maybe we could kick off with you just taking a few minutes to each introduce yourselves to our listeners and tell us a little bit about your roles. Khrystyna, can you kick us off?
[00:00:52] Khrystyna Shlyakhtovska: Yes. Thank you, Kimberly and Alexandra. Thank you so much for inviting me to your Pragmatism in Practice podcast. I'm honored to be here. During 2024, I have been working with different European customers on implementing their projects related to European Health Data Space because while the regulation has not been adopted yet, there have been already many pilot projects in this regard. Our main task for me and our European teams was to help customers to build secure, scalable, and cost-effective infrastructure, which will be aligned with European Health Data Space.
Which will allow them to innovate in healthcare and also to make use of their health data. This topic is very exciting to me, and I'm very happy to be here. Alexandra?
[00:01:42] Alexandra Lovin: Thank you, Khrystyna. Nice to have you on this podcast. My name is Alexandra Lovin. I'm joining from Bucharest, Romania. As a senior technologist at Thoughtworks, I'm working with various clients, including healthcare and life science organizations to help them stay on top of any regulatory halters that are coming in the domain, as well as making sure that they take advantage of any technology and innovation that can further help them in any of their data or AI and analytics use cases.
[00:02:17] Kimberly: Great. Thank you both. Maybe you can start by helping this American understand exactly what is the European Health Data Space and why does it matter so much for European healthcare organizations right now as they're embarking on adhering to this new regulation at the beginning of 2025.
[00:02:38] Khrystyna: Yes. Happy to do so, Kimberly. European Health Data Space is a unified framework for health data sharing across European Union for cross-border health data sharing. It has two aspects, primary usage of health data, where a patient should have full control over their data and should be able to share their health data across European Union's borders. Another aspect is secondary usage of our data where research institutions and political institutions can request and get access to European-wide anonymized health data sets for research, policymaking, and innovation purposes.
It's a big transformation for European Union. It will affect 470 million of European citizens. Why does it matter so much now? Pandemic was, I guess, the biggest reason to start this project for European Commission because it has shown that there are critical situations where research institutions need to have access to big data sets in order to improve patients' health very fast and to create solutions to urgent problems. I also would like to mention a personal story because while being very personal and maybe far from cloud and regulation, it depicts the European health data space goal very good.
A year ago, I supported my mother in a clinic. She needed to have a very small surgery and we spent full day from 7:00 AM to 7:00 PM filling in different medical forms in different cabinets of doctors in the clinic. On the next day, she had a surgery which lasted 30 minutes long, and she went home directly after that. This is a situation where nobody of the participants of the process wanted to be in because we spent all the day, my mom was very nervous. The medical personnel spent time coordinating us between these cabinets and also after that, digitalizing the data.
Also, an interesting fact, there is a study which shows that 97% of the data generated in clinics is not used. That being said, that means that this all day was important for my mom to get the surgery, but it is very possible that 97% of the data will not be used. At the same time, my mom has given the consent to use this data for research purposes, but it was only for research purposes in a research institution related to that clinic. Hence, any other research institution in Germany, where we live, in any other European country will not be able to access this data, which limits the data being available to improve patients' health a lot.
[00:05:32] Kimberly: That's insane that the paperwork took longer than the procedure and that only about 3% of the data actually gets used. I think that really brings to life why regulation like this is going to be valuable moving forward. Maybe we can dive in a little bit to that point exactly. Alexandra, Khrystyna, what new opportunities does EHDS present for healthcare organizations in the EU?
[00:05:58] Khrystyna: Coming back to this example, taking the clinic, the clinic being able to use electronic health records which is included into the provisions of European Health Data Space. The clinics will be able to have digitalized data, and also to make use of that data, and also to get the patients' data from other doctors in a digital way. Maybe some of the process will be eliminated, hopefully the main part of it. Talking about the research institution, the research institution would be able to get the data of my mother immediately.
For instance, if databases are updated live and there is data streaming, so there will be no pause and no need to digitalize manually given data. As for research institutions, they will be able to get access to big data sets from the whole European Union, so I think the benefits are obvious.
[00:07:04] Alexandra: Another interesting aspect of EHDS that I want to add is that, it actually doesn't mandate anything related to digitalization, which we know it is at times even a global-wide concern issue. There's quite different levels of maturity when it comes to digitalization of electronic health records even in Europe. Some countries have a very low maturity on this. However, EHDS does come with a lot of benefits that can be built on top after the digitization has happened.
Consider there's definitely a lot of opportunities for the patients themselves as this may lead to more improved treatments that they would have more rapid access than they do right now. Also ties to what you have told us, Khrystyna. There is also an opportunity to perhaps expand some of the telemedicine services, and ultimately for the healthcare providers themselves, hospitals, clinics, et cetera. It is definitely an opportunity for them to actually start improving their care coordination, making sure that they are more efficient, making sure that they actually free a lot of their time to actually focus on what matters most for them.
Which is obviously offering high-quality services to their patients. Indeed, as you have said for the secondary use cases, the access to the data sets themselves should be more streamlined in a controlled environment with patient consent, with granularity of the access for patient data, and through the healthcare body authorities. This will also be done in a ethical and secure manner. Ultimately, all of this combined effort, where we talk about primary or secondary use case of data will all converge into better research, better treatments.
For example, some of the, let's say, targeted users could be patients that are suffering from a rare disease or oncology patients where research at times may move too slow because of the clinical trials' access to data sets, et cetera.
[00:09:33] Kimberly: It's amazing to me that digitization, a tough one for me to get out of the mouth here the first week of the new year, is not a required element of this regulation. Some people can be providing and adhering to the regulation digitally, it sounds like, but some might be still relying on physical copies of the data. Is that accurate?
[00:09:57] Alexandra: To some extent, I think there is quite a tight coupling and dependency between the digitalization and the scope of EHDS, which is ultimately electronic healthcare records, which are supposed to be digitalized. Indeed, you have a good observation. In a lot of facilities, countries, we do use paper records, and it's going to be quite a problem for the scalability. One of the corner milestones for the incubation of EHDS is indeed for the data holders to start digitalizing their records.
[00:10:38] Kimberly: We're here in the first week of 2025. This regulation is now in place. What are some of the challenges for EU healthcare organizations that are going to need to start abiding by the regulations? How does that look like? Where do they begin? How do they start navigating to make sure they're following the intent of this new policy?
[00:11:01] Alexandra: That's a great question. I want to go into digitalization once again. Let's assume that once this major challenge has been addressed, there will be definitely other challenges. One would definitely be around the fact that there are a lot of different standards on how data is being stored and exchanged. Even for countries that have a better digitalization, there are definitely data quality issues. Where perhaps data is not captured in the right format. It might have some issues, some misinformation.
There are also challenges on how to actually obtain the data for the use cases. Definitely, there's quite an uneven implementation even when it comes to GDPR, because there is a connection between EHDS and GDPR. There are definitely some strategies and barriers here towards how the electronic health data can be exposed in a way that it is also compatible to GDPR. Right now there is quite a limited control for the individuals, so the patients themselves.
This would need to be further addressed to work in the framework offered by EHDS, which is within having a joint controllership between the patient as well as the health body authorities in the access of the data and better granularity. It is a lot about balancing the access and the privacy. Obviously, there are also concerns from the patient community towards how my data is going to be utilized. They would definitely have the last call in exposing that data. Right now when it comes to data altruism, I believe that this is something that still needs to be worked on, but this was a little bit around the data.
Let's also focus a little bit on the technical aspect of things and the current status of the IT departments within various data holders. This is also quite uneven. Most of these are operating other aging infrastructure. They are heavily operating using older systems spreadsheet. They are definitely understaffed. We are seeing situations where healthcare professionals even doctors are needed to act as business analysts and to input the data. There are also concerns towards, is this secure enough in this format to actually store and process the data.
There's also a challenge towards some implementation costs. Let's also call this out, because with aging infrastructure, this would need to be updated. The integration with EHR systems would need to change. Some of the EHR systems would need to be updated on their end because they are currently not compatible with all of the new, for example, the health data at EU platform, the European Union is promoting as part of this. There is definitely a lot of things to address, but I guess a good part is that you can actually address these with EHDS.
Obviously, you need to do them from EHDS, but it's also an opportunity to basically clear and improve all of these longstanding challenges that are happening in the healthcare system.
[00:14:34] Khrystyna: I completely agree with you, Alexandra, and I would also like to refer to an article which you have recently published at the end of 2024, where you go deeper into the EHDS. You've said there that EHDS gives us a chance to do that step back and think about the data strategy, because for healthcare and life science institutions nowadays, financial and organizational constraints are probably the biggest challenges. They are so big that usually business and technical decision-makers don't have the time to do that step back and analyze, "Do we have a sound data strategy? Do we make use of data which we have? Which data actually do we have, and what benefits would we have out of using this data?"
The EGS gives those entities need, but also a great opportunity to do that step back and to deal with their data strategy and to finally start using their data.
[00:15:40] Kimberly: That's exactly what stuck out to me, Khrystyna and Alexandra, that EHDS, obviously, it sounds like there's a lot of complexity and a lot of scale to this new regulation. It really can serve as a catalyst for change that's probably been desired, but because it wasn't required, wasn't necessarily taking place in the healthcare landscape. A complex, but I think exciting opportunity for that space. One thing, Alexandra, that you mentioned, and I'd love to get both of your perspectives on this is, say I'm an EU citizen, with this new regulation, what does it look like?
What do I get? Do I have my accessible portable healthcare data? What does it look like from the consumer aspect of this?
[00:16:28] Khrystyna: The answer to that question in terms of how does your app look like or what exactly program would you use is still open, and it might be even different from country to country, but functionally as, for example, a German citizen speaking only German language, you should be able to go on a vacation to Spain. If you would need to visit a general practitioner there, you will be able to share all medical information you want to with the doctor there and get the diagnosis there in Spanish, but get it in also in German.
You will also have medicine prescribed, go with that prescription to pharmacy, and buy what you need. Coming back to Germany, you should be also able to withdraw that consent so that data, which can be withdrawn, will be withdrawn and not be shown to the doctor anymore. 
[00:18:08] Alexandra: While there will be definitely different digital touchpoints, let's put it like this, for patients to actually access data, configure the consent on the data granularity, the idea would be to actually take advantage of the concept behind the federated data sharing, where this obviously goes towards decentralization. It's definitely not going to be one central location where all the data is being stored. The data holders which are, let's say, the individual clinics, healthcare facilities, et cetera, are going to be the ones that will be ultimately storing the data in the different formats, potentially in the same systems that they are currently doing.
However, the sharing of the data will be done towards a more EU-wide platform or through a EU-wide platform. Through this platform, the data will be then shared to any other authorities, or life science companies, or research institution that they would want to get access to the data. There are still a lot of things to be factored in and determine how they are going to look. Like, for example, what would be the proper data exchange format?
There are discussions to have a single standardized data exchange format for EHRs at EU level, but this will definitely require a lot of integration and interoperability work. There's also the question of authentication authorization system. How would this work at an EU level? Does it need to be a single one or something different? A lot of things to still see how they do evolve as part of the overall picture.
[00:19:55] Khrystyna: I also wanted to give you example of how one of the European healthcare national systems that we are collaborating with is currently addressing the patient records transfer between various physicians. Here, we started by actually attacking a problem related to efficiency, especially when it comes to patient records, fragmentation, and transfer between different healthcare providers and the various systems utilized by them. Obviously, one way you could go about this would be looking at standardization.
However, in practice, standardization would be very difficult to achieve. Instead, we worked on exposing the healthcare data in a secure manner, making sure that it is accessed with the proper controls, policies in place between the holders and the appropriate requested systems. We've also looked at it from a product and value perspective. This work has actually resulted in a reduction in the technical issues as numerous opportunities for improvements of the processes have been identified and further resulted in a reduction of the staff hours that were being spent on anything that was operational or data transfer activities that were being handled manually.
Additionally, this has also helped to lay the foundations for the future data strategy as well as healthcare data platform. To further expand on this, at the core of a health data system, that should be compatible with EHDS, which is basically a digital infrastructure for sharing data, there needs to be a source of data platform or multiple sources of data platform. This would need to be replicated both at the place of the healthcare public authorities as well as potentially at the individual data holders, depending on the size and the ability to take over such scale projects such as data platforms.
Therefore, the registration of the various data products can also be as well as handling of data sharing requests, with proper rules and policies in place, can also be handled through the data platforms. One example to do this would also be to introduce data mesh, as data mesh also has a lot of similarities to the federated approach of EHDS. For example, the source of data platform that is envisioned in a data mesh ecosystem is where the consumers can access data without requiring any central IT involvement for every single request.
EHDS actually aims to make it easier for researchers to be able to access necessary data with standard application processes and a EU-wide dataset catalog. This will allow them to create streamlined application processes for accessing data from multiple member states.
[00:22:54] Kimberly: Khrystyna and Alexandra, I know you both are speaking with a number of healthcare organizations on a regular basis and helping them think about this particular challenge that this new regulation poses as well as their day-to-day goals and strategies. Where are EU healthcare organizations today when they're thinking about EHDS? What's step one in terms of what they're addressing to help ensure that their organizations are in compliance?
[00:23:32] Alexandra: That's actually a great question. It depends a lot. There's a lot of variance on the current state of things for healthcare in Europe. There are definitely countries that are a little bit more advanced on how they handle health data right now. Not just from a digitalization, but also, from a storage, from a collaboration perspective, either within the country or across countries, between different institutions. It depends a lot where you start to where you are also at. The first wave of EHDS that would need to be ultimately addressed is around the primary usage of data.
How are the EHRs record being stored as well as being synced within the data platform. As you can imagine, for everyone, this first step or this first wave does mean relooking at their data strategy, at the data platforms or the way that the patient data is being handled, processed, secured, et cetera. There will be also a lot of integration work and inter-variability work when to expose this data. Now, when I look at the next wave towards secondary usage or how some of these use cases could evolve, it would make sense to look at it from a data platform perspective.
Exposing data is usually a lot easier when you, let's say, invest in creating a self-serve data platform with a proper granularity, proper access control and at others. This is going to help the data holders interact and integrate with different use cases systems, both for primary as well as secondary usage of data. Maybe also important to take a look at, let's say, the cloud and on-prem setup and how these could potentially also influence the future. Relook at your cloud strategy, at your health data strategy to determine where to first invest.
I think it's also important to-- again, it's about challenges and opportunities. When you address the challenges, also do it in a more valuable use case context. If you are able to identify a particular use case, like for example, let's help a certain department within healthcare to better expose their data because they also want to collaborate with another department on a research paper or on a clinical research setup. It's important to also tie it to a business and data value as well, and not just do it because it's mandatory and you basically need to do it.
[00:26:37] Khrystyna: Kimberly, I would like to elaborate on that. Also, you have asked about the EHDS compliance, however, we need to remember that EHDS has two aspects. It has legislative aspect and it has also a technological aspect. We had already compared EHDS to GDPR and to some extent, the comparison is fair. At the same time, EHDS will include technological implementation standards and some infrastructure implemented on European Union's level as well on the national level, and this is a big difference to GDPR.
EHDS has a big technological component. If we speak about technological alignment with EHDS, on one hand, it is difficult to speak about it directly today because the regulation has been adopted, but there are still no technical standards for the implementation of technological infrastructure, for example, on European or on national level. At the same time, I need to say that the main idea of EHDS is to build a federated system as Alexandra has already mentioned, federated health data sharing and collaboration infrastructure across European Union.
As it needs to be federated, it also needs to be interoperable, and it needs to be technologically agnostic. That being said, it should be able to combine a technological stack of different types. Speaking about the readiness of different entities to align with EHDS, for sure, those entities who have developed a data strategy, who have progressed on their cloud journey are more ready to align with EHDS because having a data-driven culture and having a scalable infrastructure, they will be able to first understand the importance of data and benefit from the access to big data sets.
Second, they would already have an infrastructure and expertise which allows them to scale where needed and analyze big data sets, and scale down where needed in order to effectively use their IT resources. Coming back to the question of cloud usage, there are studies which show that on average, those entities who move their workloads from on-premises to AWS cloud save up to 20% cost and the time to market for the new features is 43% shorter for them.
Such entities, for example, will be much more ready to embrace the change, integrate to the European Health Data Space, and make use of data faster than all others because they have been already practicing data-driven decision-making before.
[00:29:52] Kimberly: Yes, makes sense. Folks who are already invested in their infrastructure modernization and transition to the cloud journey will have that flexibility and agility as an organization to ingest and also respond to what the requirements are. I did think it was interesting that you mentioned that it's two-pronged. It's regulation, so legislation, but also the technical aspect. There's not currently a common set of technical standards. Is that something that's coming as part of EHDS, or is that something that isn't really going to take shape because it's so federated in nature?
[00:30:35] Alexandra: From a EU perspective, there are some things that are going to be standardized. What we know so far is that the MyHealth@EU central platform is getting created. This would represent the core infrastructure that is going to facilitate the cross-border data exchange. There will definitely be a standardized data exchange format for EHDR. They will definitely need to build a data set catalog at EU level. This is just from the top vision. Now, from the bottom approach, there is a lot of independence in how the local standards are going to be set up by the countries or by clusters of countries.
Here, we are expecting, within this federated data sharing and collaboration framework, to have either centralized country or multiple decentralized country setups, including polyglot data architecture with a mix of technical stack, a mix of cloud providers, et cetera. I would say, probably that the bulk of the work initially is going to happen on how to potentially harmonize all of these decentralized country implementation to be able to properly work with the high-level vision from the EU approach.
[00:32:03] Kimberly: Speaking of vision, and I think I heard another V word a little earlier in the conversation, value, what are the expected outcomes? How will we know that EHDS is delivering on what it's intended to deliver with this new regulation, or is it too soon to tell? Is that an unfair question to ask? I know we're week 1 in 2025.
[00:32:30] Khrystyna: I definitely will see the difference because I live in Germany, and unfortunately, the digitalization level in healthcare sector is very low here. I am having big hopes for EHDS change to come. This is the same for every citizen of European states, where digitalization in healthcare is not so progressed until now. On the level of healthcare institutions, like clinics or research institutions, professionals like doctors will see the change when they have more time for their medical activities and they need to less spend time for paperwork.
The heads of departments in clinics and in research institutions will see the change when they experience their personnel having more time for patients or for research work, and spending less time with burdensome work like digitalizing papers. The heads of clinics and research institutions will see the change when they are able to be creative and think about strategy for their organization, instead of thinking about how to save costs. I think this is in a perfect future. I still hope this will come and member states will see the change.
For instance, in critical situations, like a pandemic or some crisis, they will be able to make data-driven decision very fast, and will be also able to get the most current data from big datasets. For example, if the next pandemic comes, which I hope will not happen,-
[00:34:24] Kimberly: You and me both.
[00:34:28] Khrystyna: -it doesn't take months or even years to find the vaccine. It doesn't take months to implement an app, which helps to have an overview on European level of available medical support, but these things can be tracked immediately. Alexandra, what do you think on this matter?
[00:34:52] Alexandra: I think these are definitely ways that we can tell that this works. This is me maybe coming from a technical perspective of how we actually can observe and measure that these are working. I think as part of EHDS, there's definitely some KPIs that are measured on how to actually determine whether it works. The European Union will definitely start monitoring some of these KPIs, which could be around, are the healthcare providers more connected right now, which could be, I don't know, which are the ones that are connected on the MyHealth EU infrastructure.
Whether these are the provider themselves or the natural personnels. What's the volumes of data shared? What's the percentage of response towards data sharing versus requests, the number of data sets published. When it comes to the EHR systems themselves, I think these would also undergo certification or self-certification to see whether they are compatible with, let's say, EHDS. There's a lot of measures of success and points and things that can be measured to actually determine what's the progress, because the progress itself will need to be tracked as well. Then also, the impact of EHDS.
[00:36:18] Kimberly: I think one other measure of success would be, Khrystyna, that your mother doesn't have to spend 12 hours completing paperwork in the future. Hopefully, that can then-
[00:36:28] Khrystyna: Yes, definitely.
[00:36:29] Kimberly: -be whittled down to 15 minutes as a real practical measure of value. One more question for you both before we wrap here today, what advice would you give to healthcare leaders in the EU who are embarking on the EHDS initiative?
[00:36:48] Khrystyna: First of all, I would like to emphasize that while we have been speaking here about European-wide initiative, this problem missing digitalization and health data sharing and missing availability of data for analytics and AI usage, for example, this challenge is not only present on European level. Almost every European country faces this challenge on national level. Almost every regional healthcare system experiences this challenge inside them too.
Almost every healthcare entity have this challenge too, because even if you have a healthcare entity which merged from two, usually you would have two different technological stacks and maybe even two different systems of storing the data. Hence, this challenge is applicable. Everything, what we've discussed today is applicable not only on the European level, it's applicable to each and every healthcare institution in European Union. Starting to address these challenges, which we discussed at the beginning, I think the easiest way would be to start with small steps with low-hanging fruits.
Many entities hesitate to start implementing data strategy because it's a long process. However, if you select one small problem, which can be solved with digitalization and solve this one very small challenge, you will see success quite fast. It'll motivate you and bring you resources to solve another one and another one. The first one is start with small steps with low-hanging fruits. Another one is bring technological business and operational teams together. It will ensure that you identify the most urgent problems, and that you have also commitment from every stakeholder in the entity to contribute solving this challenge.
For example, in my case, I imagine that a clinic could benefit from having a department lead and IT department lead or any member, and any nurse or doctor who struggle to translate paper forms to digital formats together, describe what is the biggest problem here, and what would be the easiest step to solve it just right now, that could help to progress. The last one is, having seen successful projects implemented on AWS, for instance, those with Thoughtworks, an implementation partner, we would recommend leaders to start with data strategy diagnostic.
For example, Thoughtworks and Alexandra's colleagues have great offering where they help customers understand where does the organization stands just right now in terms of data usage, which goals would the organization like to perceive on the long term? It could be, for example, EHDS alignment, but it could also be cost-saving. It could also be more time for staff to deal with patients and less time for staff to deal with organizational work, something like that. Then moving step by step to how to implement these changes.
[00:40:28] Kimberly: Yes. You got to know what your starting position is and where you want to go to determine what it is you do next.
[00:40:34] Khrystyna: Yes. Exactly.
[00:40:36] Kimberly: Alexandra, any final thoughts on advice for leaders embarking on this?
[00:40:43] Alexandra: I think just to maybe emphasize a little bit, see this as definitely an opportunity. Make sure that you approach it from a value-driven standpoint as well. Even if it means that you would need to adapt along the way, make sure you start, even right now in perhaps relooking, assessing where you are from a data strategy, data platform perspective. Looking at what are your technical impediments, and building a value use case out of this, in an incremental and lean mode.
[00:41:26] Kimberly: Khrystyna and Alexandra, thank you so much for your time today chatting about all things EHDS. It definitely sounds like there's lots of work to be done, but also tremendous opportunity as healthcare organizations begin to implement this, not just for the organizations, but for the patients and for the systems as a whole. Really appreciate your time and sharing your thoughts today.
[00:41:49] Khrystyna: Thank you also for having us today, Kimberly. It has been a pleasure.
[00:41:52] Alexandra: Of course. Thank you, Kimberly.
[00:41:54] Kimberly: Thanks so much for joining us for this episode of Pragmatism in Practice. If you'd like to listen to similar podcasts, please visit us at thoughtworks.com/podcasts, or if you enjoyed the show, help spread the word by rating us on your preferred podcast platform.
[music]
[00:42:18] [END OF AUDIO]
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
### **Episode highlights**
  * Khrystyna introduces the European Health Data Space (EHDS) as a unified framework for health data sharing across the European Union. 


  * The EHDS has two aspects: Primary usage of health data, where a patient should have full control over their data and should be able to share their health data across European Union's borders. And secondary usage of data where research institutions and political institutions can request and get access to European-wide anonymized health data sets for research, policymaking, and innovation purposes.


  * Alexandra suggests that EHDS presents opportunities for patients to receive more improved treatments with quicker access. It also presents an opportunity to expand telemedicine services, and for healthcare providers themselves to start improving care coordination and efficiency.


  * Digitalization, GDPR concerns, and implementation costs all pose challenges for organizations that need to comply with EHDS.


  * Khrystyna suggests that a sound data strategy should be adopted for organizations that want to get the most out of their data.


  * Alexandra suggests organizations should think about their most valuable use cases to get the most value out of their data, not just thinking about EHDS because it's now mandatory.


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