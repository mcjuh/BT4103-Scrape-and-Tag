<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/inside-bahmni-open-source-digital-public-good | Title: Inside Bahmni: An open-source digital public good | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Inside Bahmni: An open-source digital public good 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons  and Ken Mugrage | Podcast guest  Satish Viswanathan and Angshuman Sarkar
June 27, 2024 | 52 min 11 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/inside-bahmni-open-source-digital-public-good#Transcript)
Listen on these platforms
## Brief summary
Bahmni started life as an open-source hospital information management system and electronic medical record for a single hospital in rural India. Today, it has more than 500 implementations in 50 countries across Africa and Asia, and is recognized as one of only 165 digital public goods by the [Digital Public Goods Alliance](https://digitalpublicgoods.net/).
Thoughtworks played a key part in bringing Bahmni into the world back in 2012. And although today it’s run and supported by a coalition of organizations, Thoughtworks continues to have a leading role in the project as a member of its Governing Committee.
To tell Bahmni’s unique story, Rebecca Parsons and Ken Mugrage speak with Satish Viswanathan and Angshuman Sarkar, two Thoughtworkers actively participating and contributing to the project. They discuss Bahmni’s origins and how it grew from a small, local tool to become a vital component in healthcare infrastructure in parts of the world that have long faced resource challenges. 
  * Learn more about [Bahmni](https://www.bahmni.org/)


## Episode transcript
**Rebecca Parsons:** Hello, everyone. My name is Rebecca Parsons. I'm one of your recurring co-hosts for the Thoughtworks Technology podcast. I'm joined by another one of my co-hosts, Ken. 
**Ken Mugrage:** Good morning. I'm Ken Mugrage. I guess, good evening, depending on where you are. Another one of your regular podcast hosts.
**Rebecca:** We are joined today by two of our folks from Thoughtworks India, who have been working for various periods of time on a product called Bahmni. We'll get into what Bahmni is, but I'd like to introduce Satish.
**Satish Viswanathan:** My name is Satish Viswanathan. I lead social change and sustainability for Thoughtworks in India and the Middle East. I also represent Bahmni on the governing committee of the Bahmni Polishing.
**Rebecca:** And Angshuman.
**Angshuman Sarkar:** Hi, everyone, my name is Angshuman. I work for Thoughtworks India. I usually work in health-related projects, and I have been a long-term contributor and also one of the architects for Bahmni.
**Rebecca:** Let's start with a little bit of history. What is Bahmni?
**Angshuman:** Bahmni, as we say, is a HIMS. A hospital information management system. It integrates and brings in various capabilities of a typical hospital together. Starting from registration to clinical information management, to doing, say, laboratory test, managing radiology test, as well as all the pharmacy inventory, billing, et cetera.
**Rebecca:** How did we get started with Bahmni? Where did it come from?
**Angshuman:** Probably requires a little bit of context as well. Back in 2009, Thoughtworks had this social impact program going on, and under which we were doing various health-related projects. Often, we would be wondering that what is the impact that we are causing. Many Thoughtworker's were part of this and came because they wanted to contribute to the social caucus were dissatisfied.
Now, all that changed in 2012, 1st October when our then chairman, Neville Roy Singham, and five of us traveled to a place called Ganiyari where one organization called Jan Swasthya Sahyog or People Support Group, a not-for-profit organization, had a remote hospital set up for care for the rural and underserved people. That really inspired us seeing them there, how they're doing, how they're working, what they're contributing to society. They asked us some very pertinent questions. For example, why is software so expensive?
Because from their perspective, they would rather use the money for buying medications or buying other provisions. They obviously couldn't maintain. We came back totally inspired, determined to help them out. Over the next few months, we deliberated, we debated, we reached out to networks, et cetera, and then started this project. It was not a product. That point of time we didn't think about as a product, and started this project just to help this particular hospital. That's the genesis of Bahmni and how we started.
**Rebecca:** Can you tell us a little bit about how it's evolved since then? Then we'll talk a little bit more about what it is and how it's built and such. How has it grown and changed since then?
**Angshuman:** That's quite a story. As I said, initially we just started as a project to help this particular hospital. Now these were doctors, practitioners for whom the quality of service, quality of care was supreme. That is the first time actually we decided we're going to build a system, being with them, working alongside them, learning from them from the daily usages. That's how sort of Bahmni drew based on their needs and demands. Now over time, word of mouth spread and other organizations.
These are initially all not-for-profit organizations. They like Bahmni and they wanted to add on. Another iconic organization called SEARCH, Society for Education and Research in Community Health they took it up. Another remote hospital run by Dr. Prakash Shanti in rural Maharashtra, they also took it up. We were getting loads of feedbacks, a lot of queries that, "Can you implement it in our hospitals? We like it. It is appropriate for our usage." That was the time we started thinking about it as a product.
We were also lucky that point of time, the worldwide EndTB Initiative was being launched. The EndTB Initiative was for clinical trials of these two specific drugs on the treatment of tuberculosis, multi-drug resistant tuberculosis. Médecins Sans Frontières, so Doctors Without Borders, they were working with us along with IRD, as well. They contextualize it for tuberculosis, and that gave us more confidence that, yes, potentially, this can be a generic product, which is widely applicable to different usage context.
In 2015, we decided we had to launch it as a product. Now, soon after that there was a major expansion in Bangladesh and Africa. Later on, obviously, in 2017, the Bahmni Coalition was formed rather to expand the supporting ecosystem. Since 2017, '18, there has been large-scale adoptions in many Asian and African countries, namely, Bangladesh, Lesotho, Nepal, Cameroon, as such.
We realized that this was not possible for Thoughtworks to do alone, and that's one of the reasons also to create the Bahmni Coalition. That's where we are right now, it is probably one of the most popular open-source, EMR, EHR, or HMI solutions, and ever-growing with this ecosystem, and even independent organizations have taken it up as their business models.
**Ken Mugrage:** Angshu, I'm curious, creating it as a product with multiple users, how does that differ in your management of features and that kind of thing from a project that's got one user base and a direct feedback? How did you manage feature requests and that sort of thing? Does that change your whole mindset, or what was the impact of that?
**Angshuman:** Initially, we didn't have to bother about it because probably for one and half years we were only working for DSS. Then as others who came in, arrive and we saw the variances in their systems, we decided to make the solution more and more generic. Now, it was still two or three such organizations working together. Probably it was more easier, we had to look into the technical aspect of how to make it generic.
We had to take into consideration of how do we actually build this product to be applicable in an extremely low-resource setting, where you can find reliable hardware, reliable, say, internet, or infrastructure, people capacity. Many things that we decided were done from the angle of how will it be serviced, how will it be operationalized in such context. Now, in terms of the actual product governance part, I think we started thinking about it, as I said, around 2015, when we had implemented a bunch of, say, hospitals as such.
That was the real pressure that came in. That is the time we realized that the governance must be open as well. That was while Bahmni was open source right from the beginning. It was largely managed by Thoughtworks. Retrospectively, I do think it also benefited from the initial patronage of Thoughtworks and guidance. As the needs came in, more global demands came in, we realized we needed to really open up the governance part. Today, I am glad to say that everything starting from the roadmap, to designs, to features is done along with the community.
We get a lot of contributions from projects. Now, we do have a product management team, which engages early, and that was probably one of the issues also we faced back in 2015/2016 with changing about, how do we get in the feedbacks? How do we build a generic feature that is applicable, not just for one but for global needs? Now, I think we have matured a lot. We have the established community processes to guide us through this.
**Satish:** I would also add here that I think it's helped that since Bahmni is built on top of OpenMRS, which is again another by being in open source EMR, it helped that we were part of the community. We had a chance to observe the community processes. When we formally set up the Coalition in 2017, I think one of the focus areas in addition to completely making the code available for contributors from upside, it's always been open source.
One key aspect which the movement to create the Coalition did was to strongly establish the community and governance processes, and essentially develop out into the open and still continues to this day. I'm sure they used to anchor the weekly product architecture calls, which is wide participation from volunteers and community members from across the globe. We have other forums as well and generally are-- run with a very strong open source project with good community contributions.
**Rebecca:** You've both mentioned the Coalition and the community. Can you talk a little bit more about the foundation or the establishment of the Coalition, Satish, and how it relates to the community? I think most people are at least familiar with the concept of an open-source community, but how does that work when you also have the Coalition as well as Thoughtworks involved?
**Satish:** Angshu mentioned Bahmni is obviously an open source from day one. Thoughtworks was, I guess, the only contributor for about four or five years, and in 2017 we actually moved to set up the Bahmni Coalition. This is driven by a couple of factors. One is, as a technology organization that's primarily an engineering organization, we've not built anything like Bahmni before. We had done other products that eventually became really important open-source projects like CruiseControl or Selenium, but those are all software engineering adjacent.
Bahmni was really the first thing that we did that was a domain product that you see open source, so it was a little different one for us. I think the other peculiarity of this was while Bahmni is not a B2C product, this is used by hospital teams, this is used by health organizations. While it is fairly modular and doesn't need too much once you set it up, in order to actually do the initial setup, you would definitely benefit from the services of an implementation partner.
The first few implementations are all being done by Thoughtworks, but that's not something that we naturally had the muscle to do at that point. We try to hire people to do implementations and so on and so forth. For various reasons, we expect that it was probably limiting Bahmni if Thoughtworks were the only organization that was doing implementation. With a view to expanding the ecosystem around the product, we felt that it would be better to involve other organizations and create a larger community around the product itself.
That's when, with advice, we set up the Bahmni Coalition, and this brought together implementation partners who, by the time, were very interested in Bahmni through word of mouth and hearing about it in various forums. Other large organizations like Médecins Sans Frontières, MSF, which were already using Bahmni across many installations and many projects by that point. Also, the OpenMRS foundation which Bahmni was a part of. We back all of these organizations together to form the Coalition. I think you asked what is the difference between this Coalition and the broader open-source community.
I think the coalition was essentially an effort for us to build a more tightly knit governance structure of organizations that were really invested in Bahmni. We still had a lot of organizations in the science community that continued to be users that continued to contribute code. For example, there were organizations that took Bahmni and customized it for all the public health centers in lesser code, for example.
Those organizations still continue to be part of the larger community, but the Coalition is a more tightly knit group that has a slightly larger say in terms of governance of the product and so on and so forth. The purpose at with which these organizations come together to be part of the Coalition is to essentially vandalize Bahmni and do everything to make sure that Bahmni grows and so on and so forth. In return, they also contribute either monetarily or non-monetarily to growing Bahmni.
For example, some organizations contribute manpower to, say, take care of incoming contact requests and responding to people on forums, for example. Other organizations might say, "We're using Bahmni, we need this particular feature built in, so can someone build it for us as paid or commercial engagement." They contribute to building features on the product that benefits the entire community. That's the broad distinction between the community and the Coalition.
**Angshuman:** I also want to add or define the community a little bit more and how it shaped. Now typically in open source, we typically mean the communities in terms of development or people who are directly involved on the development process. An analyst, QAs, product managers, et cetera. While we had all this, the people who actually run the operation often are not the ones who are actually modifying the codebase. Now, as I said, it deliberated long.
When the idea initially came to us, we found that in all the implementations, the developers were involved as in they knew the code, the inside, the models, the flaws. They were the people who were actually implementing this right on the ground. Looking it in the different low resource environments that we were getting the demands for and people are asking us to implement. We realized this is going to be an extremely tough one, so we focused on building the community more on the implementers.
Now, it's not that they are not technical, but they don't know inherently the behavior of the code or the details of the code as such. They knew about, okay, this is how I take the product, this is how I can configure it. So we chose configuration over customizations. Well, that means extremely customizable, extensible, but that's our favored way of going off enabling configurations, so you could change a few configuration files, JSN files and you could bring in different sorts of behavior.
Now you could say this is-- probably we deemphasize the developers aside of it, but initially that also made Bahmni extremely easy that somebody can just take it, follow our Wiki, and self-implement and this is what we targeted. Even today I would say a large part of the community actually is by the implementers. Increasingly obviously, we're focusing more on the developer community side, but that focus didn't come in I would say till about 2016, '17 on the developer side.
**Ken:** I'm curious, you've both mentioned low resource environments in the places that you're working. What are some of the architectural things at a high level-- don't need the exact JavaScript libraries. What are some of the architectural things you have to think about when a system like this in a low-resource environment?
**Angshuman:** A lot of resilience and reliability is probably the first because you need to realize that in such environments they don't have a server grade machines as such what you typically think about. Many places are devoid of internet or have absolutely unreliable internet connectivity. Can't even think about the cloud solutions. There are places where people would prefer cloud. We need to make both cloud native as well as support for on-premise. That had to be there from the beginning. Since they didn't have capacity or capability of typical things like--
Think about patient and data safety or security aspect. You will find there is lots of data, but there is no security often in such places, no backups, probably people are now aware of the privacy. We need to make sure that when the system is set up and it's a few steps that we were actually setting up the firewalls, we're setting up the security policies. We are putting in the specific rules in terms of the data sharing, et cetera. Another aspect is that many places that doctors are working, say, with their gloves on, even the user interface, for example, we want it to be absolutely touch-friendly.
If you look into Bahmni and lots of people say, is this, "Oh, why are there such big buttons? Why are all the templates or the forms mostly this," and it is designed because it needs to be touch responsive. Doctors are not sitting in front of their laptops all the time. They are moving about, they have their gloves on, they needed to select something. Many of the user interface design were reflections of how it is being actually being used. Now, it is not to say that throughout the system, the behavior need to be the same. Think about people who are handling the billing.
They don't need to select clinical information. People who are at the registration, for example, they were using desktops, in some cases, like obviously mobile devices as well. We also had to design for cheap devices. Although, those are the early days of rich client and more of a single-page applications, but we didn't try to put all the behavior into one big, no single-page app. We went by them more by the function. For registration people, they have only limited all the registration-related module. Maybe that is self-pay, the single-page app. That's our thinking.
People who are doing the more outpatient consultant, all the clinical aspects are bundled together into another single page app. Even in terms of the typical packaging, or in terms of assembling of all these diverse components together, we need to really think about what would be the most appropriate. Would latency kill it? Would that be a big problem? We also had to think about that, especially when people are going outside. I couldn't make 10 different calls in a transaction context because what if the second call fails.
You have to create these coarse grain services, for example, because the idea is like, to do the entire consultation, and you just click one button, say save, it'll be saved, and everything will be saved at once. Now, although we did have those smaller granular 10 APIs to do this, but we could not do that. Many of these reflections of where we're working, the environments, how lean it had to be, as well as appropriate for the users.
**Rebecca:** You alluded to this earlier, both of you, Angshu and Satish, about the fact that were built on top of OpenMRS being a medical record system, but this is actually a hospital management system. I'm sure you talked about labs and all of that. Can you talk a little bit about the challenges of bringing in these various open-source projects together, it had to be an interesting integration problem.
**Angshuman:** Absolutely. We were working with OpenMRS. Even before the Bahmni started, we had a relationship with OpenMRS. Many of us were contributing to OpenMRS. I contributed as early as 2008. When we looked into this, we obviously didn't find that something that seamlessly integrates the major functions of the hospital. We went about looking what is the most appropriate solution. We didn't want to reinvent the wheel. We wanted to leverage the community power.
Thoughtworks being so raw open source, I think it was also in our nature that we were looking for well-supported community-established products as such. We took OpenMRS, which was probably natural because we had also worked with OpenMRS interoperability teaching hospital context. University of Washington had built this lab system, a lab information management system called OpenELIS. DCM4CHE, for example, is a renowned radiology system. It's a fax server.
The last part was around pharmacy billing, which we realized that Odoo — and at that point of time, it is known as an OpenERP — would fit our needs. Integrating them was tough. Look at it, all the trigger points are from the main system, which is reconsidered as the EMR. You register something, the patient needs to be recognized as a customer in the ERP. That way. If you prescribe a new drug, for example, that needs to be going for billing to the pharmacy. If you ordered a test, that needs to flow to the lab system.
What we decided was this-- and it's not that all the environments needed all these four components. Some would say, I just want the clinical part. Our lab functions are outsourced. We get reports, we just want to upload the reports. Each system is pluggable. Each component as such. Each system essentially raises events. We leverage the typical event stream. We follow the event-driven architecture. We follow the event notification, more like a state transfer pattern asset. You follow them onto even notification pattern.
Naturally, people would think about that, why don't you put some sort of a message broker to handle these needs? That's probably the first thing that comes to somebody's mind. We again went back and said, "We can't ensure that there is a reliable internet backups capability. Do you want to introduce another middleware for somebody to manage?" He said, "Maybe that's not the best option. We have already decided each system is responsible for its own data, own API, own access.
It is just like raising events. Others could just subscribe to these events, and if they're interested if they have the right access, they could access the data. I think a few years before that, Jim Webber, who was our Director at Thoughtworks, had released this book called REST in Practice. It is interesting that we liked some of the patterns over there. One was like event notification through feed. We leveraged at them as a specification, and we build a protocol called simple feed, and we leveraged that.
Now, obviously, over time, and we know we can also support other JMS brokers now, but we were able to sustain that and leverage that very well. I remember the first time we employed this for synchronizing the information between the lab system and the medical record system at JSS, there were close to about 120,000 tests that were already done. We're wondering, will it work? We waited for some time. We saw lots of failed events coming in and we said, "Okay, let it all go through and come back so."
We came back after three, four hours and we found everything had resolved beautifully. That gave us confidence that this works. We don't need a middleware. We are still independent of any, say, specific middleware as such. Yet we are open. We are built or still leveraging, say, specific standard like say atom. The APIs that are export were also standardized.
The rest API now increasingly we are moving to HL7 FHIR. That's sort of the way, for example, that we have handled. Even till date, I think that's a broadcasting of even which others can subscribe to is still the pattern that you follow for a system integration. We don't use it easily. As I said, we were just following the event-driven architecture.
**Rebecca:** Let's skip ahead a little bit and tell me a bit more about some of both benefits and challenges of the open-source nature. As we've discussed, you don't just have a traditional software development community in your open-source community. You also have implementers. There are the unique aspects of the architecture. Tell me a little bit about how this is working now. The foundation was 2017, that's seven years ago. How has this community been growing over time, and what are the things that you think have contributed to the success of the Bahmni Coalition and the broader open-source community around it?
**Satish:** I think I can talk over, Angshu, feel free to jump in. These are the key element that helped in the Coalition was that all of the organizations that came together to be part of the Coalition were very committed to growing and evangelizing Bahmni in their different roles. Either as implementers or users or in the case Thoughtworks as the primary maintainer. Over time, I think the Coalition membership has changed where some organizations priorities have changed and they're no longer part of the Coalition. Others have come in because of their commitment to Bahmni.
One thing that has helped I think is the need-- and I think the fact that Thoughtworks has essentially played a little bit of a role of an anchor in the Coalition ecosystem. We still continue to be the primary maintainer and probably still contribute most of the code. The support from the other Coalition members that is invaluable. Either to monetary funding, to building projects or to non-monetary support. Keep in mind that the Coalition is actually fairly diverse in terms of its composition.
We have small organizations who built their entire business around Bahmni. We have large NGOs that use Bahmni in many, many places. So getting all of these organizations together and working jointly on the agenda and evangelizing Bahmni in each of the ways that each of us can contribute I think has been a growing organic process. Of course, there are challenges as any open-source community does. We always take time to talk about it in the community and try and resolve those.
I think one thing that we've seen in terms of challenges adding — and I think this is possibly true of pretty much any open source community or product — is how do you keep the sustainability of the product in mind? How do you keep it sustainable and growing, while at the same time continuing to keep it free for users as a digital public cloud. Our experiences, I think, there's no easy answer to this problem. Over the period of time, I think largely it's been supported by investments from organizations like the Thoughtworks investments from organizations like MSF who contribute monetary to build new features. CURE International is another organization. Also voluntary contributions from members. We've also been fortunate at some point to get grant funding to make some changes.
For example, a couple of years ago, we got grant funding from Digital Square, which is an organization that encourages global goods, as they call it, which are digital public goods for health to essentially implement a performance testing suite in the Bahmni product. Of course, these grants are few in property. The smaller organizations in the Coalition, I think they have built a business around Bahmni.
They make money from implementing Bahmni for hospitals, which actually has been good because we get at least a few inbound requests a week, I would say, where some organization or the other reaches out to us and say, "Hey, I need Bahmni and I'm looking at this. Can you or somebody in the Coalition help me with implementing it?" There's a steady stream of inbound business that is coming through the Bahmni site, and these organizations make money on that.
Individual organization is kind of benefiting from Bahmni. The sustenance of Bahmni, overall, I think are-- there's some overlap, but I think the Coalition was larger and the community was larger and the broader adoption was larger. I think we'd start seeing a lot more traction.
**Rebecca:** You mentioned sustainability a fair amount in there in terms of sustaining this project over time. It's been going for quite some time. It's even been under the auspices of the Coalition for quite some time. Given the rate of technology change that has happened over that time period, Angshu, how do you feel the code and the architecture is holding up given all of the changes that we've seen? You mentioned that you migrated from just on-premises to the ability to run it cloud-native as well. How's it holding up and how difficult has it been to keep this viable as an open-source project over this extended period of time?
**Angshuman:** One is obviously the changing nature of how people are looking at this. Before they were just looking at a system of record. Obviously, they are not anymore. They are looking to improve quality of care, provide continuum of care. This is one aspect of it. Even in terms of technology, things have changed. Initially, as I said, 2012, '13, we had to make something that was installable on-premise, and it evolved through.
Even in terms of deployment and provisioning, from Puppet to Ansible, Vagrant, we had to support multiple ways of standing up the system. We wanted to leverage, obviously, the more the cloud, because that's where the more demands were coming in, internet was more accessible and reliable for people. About three, four years back, we said, "Hey, we think container-based deployment has reached its maturity. We need to reorganize in terms of how we package, how we deploy."
Obviously, cloud-native support over Kubernetes came along with this. Even still today, for example, we support on-premise deployment, mostly on Docker Compose, Docker Swarm, as such. Right now, if somebody wants to set up on, say, AWS Cloud. Once you have the necessary infrastructure, it's a matter of, say, half an hour or so to set this up. We also started emphasizing more on standards. Now we started looking into this sometime back. Now, interoperability in health is a big thing because we don't work in isolation. No system these days are working in isolation. Somebody needs to integrate like, say, lab analysis, or somebody wants to bring in like, say, a care coordination tool as such. We are increasingly leaning over this sort of a standardized interface. HL7 FHIR, for example, has been a great boon because it's also built with extensibility in mind. That has helped us a lot.
We're increasingly trying to model even our applications over HL7 FHIR. Initially, we focused it just on the integration part, but we are looking even in terms of the application interactions within a particular feature over FHIR. Even on the cloud, we still have challenges, for example, in terms of the deployment-- actually I'll just give some examples. Infrastructure as a service or platform with service, I think are right now de factos.
People even in the Bahmni Coalition have started offering these services on the cloud. Many cases we are not ready yet. For example, think about two different hospitals, two different entity. You probably for the data security governance part, probably it's best to go with segregated data, which I mean databases, volumes, indexes, logs, all are separate. Now, if you try to put this in a smaller clinic, so single doctor clinics as such, just infrastructure cost becomes prohibitive for them.
Now, if it is within the same entity but multiple different, say centers, we can very well support it. For all different entities, legal entities, and especially such smaller clinics, we are looking how we can provide a more like an appropriate multi-tenant system while keeping the data aspect pretty much in mind. Many cases we have to be absolutely careful of the country's specific laws and privacy laws. Although Bahmni doesn't take it onto themself to be certified in a particular country's operating context, but we need to be aware, we need to provide them options.
These are some of the changing, I think patterns. The cloud has totally changed, I think, in terms of how we have thought about or used to think about this. At the same time, I would say about 50% of the queries that we get are from people who still probably can't go with cloud option. There are also other challenges. Think about in the community health worker scenario. These are single user, but they are operating areas probably there is no internet.
They probably come to their office, synchronize data, and go to their catchment areas. They need to be able to capture all this data and feedback, push it back. Again, follow-up comes onto them. They must know, "Oh, these are the patients that we need to follow up," et cetera. For that also the system needs to be different designed to be capable of having the appropriate data. If you put it alongside that who has access and visibility to what sort of a data, it becomes more complicated.
**Rebecca:** We're getting close to the end here, but I do want to recognize that recently Bahmni was awarded a Future of Government Award from the Digital Public Goods Alliance. First of all, of course, congratulations. Satish, you want to tell me a little bit about what it means to be a digital public good? You've referenced it a few times, but this might be a concept that people really aren't familiar with.
**Satish:** Thank you, Rebecca. Digital public good is defined as any software, data content, or framework that helps in the achievement of one of the UN sustainable development goals. That's the official definition of a digital public good. This is something that is put forward by an organization called the Digital Public Goods Alliance of which, say, Thoughtworks is a member. The other founding members are the University of Oslo, which anchors one of the largest open source software in the health world called DHIS2.
It has the USAID, Gates Foundation, and so on, so a bunch of country governments as well. The need for defining something like this emerged from the fact that it's undeniable that for achievement of UN sustainable development goals, digitization and technology have a huge role to play, but the funding doesn't necessarily work in the same way. Any large donor, in fact, any donor is essentially looking at, okay, what's the impact that I am creating through my dollars?
A lot of time it is possible for you to say, get $2 million to implement a digital public good. Bahmni in a country or for a hospital and so on then it is to get maybe $100,000 to make, say, important security fixes, or to add a new feature that will benefit the entire community. These organizations recognized the fact that not only do you need to support projects, which have a direct quantifiable beneficiary benefit, but also things that are used in the background like software that amplify the impact that you're having.
They formed this Digital Public Goods Alliance. As it turns out, we were doing a lot of the criteria that are part of the DPG standard are things that Bahmni was already doing because of its origins, our philosophy of working out the open or have some commitment to open source. When we filled out the questionnaire to nominate ourselves for Bahmni to be a digital public good, I think we straight away met most of the criteria. That's been the history. I think increasingly there is a lot of discussion around use of DPGs as an important tool to accelerate the achievement of UN SDGs.
It's gotten a lot of commitment and push from the office of the United Nations Secretary General. There are many other governments, including the government of India that's offered strong commitments to use of DPGs. In fact, there have been several DPGs and DTIs, the infrastructure equivalent of DPGs coming out of India. I think as from our own social impact side as part of the setting, we're also looking to do more in this particular area because we believe that can be a very powerful tool for creating much wider social impact.
**Angshuman:** I think particularly in health context, if you see the trends over the last four or five years, we are seeing that healthcare is becoming extremely collaborative. From how it used to be that big infrastructure-based healthcare service providers to now it is like-- even if you go to a hospital your lab records might be managed by somebody else. The followers maybe done some other organizations as such. Each of this are bringing in probably their own set of toolings as such.
I think it is very, very important that systems are designed for this collaborations. Wy build it again and again and again if you can ensure that there are interoperability, if you follow the plus one. Say, if I already have something, if I need something I'm going to build on top of it or integrate along with this. Then you don't need to start from the scratch again. I think even the institutional donors and funders over the years, they have learned that so much money has been spent in health tech.
I'm obviously talking more in terms of the health tech perspective, not across all sustainable development goals. So much money has been spent that we should probably already have the toolings that if put together, if they collaborate together, they interoperate together can do much more than probably what a Thoughtworks or a Bahmni can do.
I think that's the genesis or I say a sense of the DPG that you unbundle things to something that does one thing well and always think about the plus one approach. I already have this. What can I do next that augment this? I think the cool part is easy, we are increasingly finding that. Actually in the health domain, there is a lot to do with the other aspect in terms of the content, in terms of the metadata, in terms of the rules. I think we need to do a lot more in that space as well.
**Satish:** Now, saying that, and I think this is why the DPG standard, I think is certainly one part of it. The standard just to touch on the areas that covers broadly, I think is one, is that it needs to be open source with the credible open-source license. There needs to be clear ownership. There are also other factors that are important, which is the presence of a community around it, the commitment to do no harm, and so on, so forth. A lot of these go beyond just the code aspects of the DPG standard, which is what makes it really powerful.
**Ken:** Excellent. Well, I think it's time for us to wrap up. I'd like to thank you two again, Angshu and Satish for joining me and Ken to discuss Bahmni. Again, congratulations on the award and keep up the good work. It's clearly a critical area for the wellbeing of the world, and there aren't too many people who can say that they're supporting the wellbeing of the world, so thank you both.
**Ken:** Congratulations. Thank you.
**Satish:** Thank you, Rebecca. Thank you, Ken. It's been a pleasure.
**Angshuman:** Thank you so much.
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
## Discover a snapshot of today's technology landscape
[ Explore Tech Radar ](https://www.thoughtworks.com/insights/podcasts/technology-podcasts)
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