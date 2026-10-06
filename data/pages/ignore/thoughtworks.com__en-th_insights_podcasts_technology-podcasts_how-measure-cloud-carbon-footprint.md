<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-measure-cloud-carbon-footprint | Title: How to measure your cloud carbon footprint | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  How to measure your cloud carbon footprint 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Ken Mugrage | Podcast guest  Arik Smith and Cameron Casher
April 04, 2024 | 38 min 44 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-measure-cloud-carbon-footprint#Transcript)
Listen on these platforms
## Brief summary
If you've ever wondered how to measure your cloud carbon footprint, you can — thanks to a tool that's called, somewhat unsurprisingly, Cloud Carbon Footprint. Launched in March 2021 by Thoughtworks as an open-source project, it allows users to monitor and measure carbon emissions and energy use from cloud services. 
On this episode of the Technology Podcast, senior software engineers Cameron Casher and Arik Smith join Alexey Boas and Ken Mugrage to talk about Cloud Carbon Footprint in depth. They explain why CCF is different from the measurement tools offered by established cloud vendors, how it actually works and how you can get started with it yourself. 
  * CCF on [GitHub](https://github.com/cloud-carbon-footprint)
  * Learn more on the [project site](https://www.cloudcarbonfootprint.org/)


## Episode transcript
**Alexey:** Hello and welcome to the Thoughtworks Technology Podcast. My name is Alexey. I'm speaking to you from Santiago in Chile, and I'm going to be one of your hosts this time together with Ken Mugrage. Hello, Ken.
**Ken Mugrage:** How are you? I'm good. Thanks. Hi, I'm Ken Mugrage. I'm in Seattle, Washington, one of your regular hosts.
**Alexey:** This time we're going to talk a little bit about the cloud carbon footprint, and we have two guests with us this time. Eric Smith and Cameron Casher. Maybe you two could introduce yourselves to the hosts. Eric, how about you? Can you tell us a little bit about yourself?
**AriK Smith:** Yes, for sure. My name is Arik Smith, currently based out of Cleveland, Ohio. I've been at Thoughtworks for three years, anniversary recently. During that time, I've been primarily working as a developer and consultant on our sustainability solutions team, where I was able to help develop and currently maintain the Cloud Carbon Footprint project. As of now, I am still doing sustainability stuff, but also on our enterprise modernization and platforms and cloud team, where I essentially serve as a cloud specialist and sustainability SME on that team. Thanks for having me.
**Alexey:** Thanks a lot, Eric. Great pleasure to have you with us this time. How about you, Cameron?
**Cameron Casher:** Hi, my name is Cameron Casher. I've been at Thoughtworks for almost five years. I live in Denver, Colorado, and I've worked pretty closely with Eric for at least two or three of those years, I'd say, doing sustainability work and maintaining cloud carbon footprint. I think that I objectively have the worst podcast voice out of the four of us here, I'll just say that!
**Alexey:** That's great. That's great. Thank you so much. It's a great pleasure to have both of you this time with us. Maybe we can get started telling the listeners, what is the Cloud Carbon Footprint? Can you talk a little bit about what it is, what it does, and where it came from?
**Arik:** Yes, for sure. The Cloud Carbon Footprint is essentially an open source project that we launched back in March of 2021. It's essentially a tool that allows you to measure and monitor your carbon emissions and energy usage from services in the cloud. It currently supports three major public cloud providers. Your Google Cloud, AWS, and Microsoft Azure. I always say three, but we also recently added support for Alibaba Cloud as well. That's our fourth one that's brewing and catching up with the others, so to speak.
Essentially, we have a dashboard that allows you to visualize these estimations. It's very modular and you can customize it as well. Even though we have that dashboard, you're also able to stand up and consume an API implementation of it as well or a command line interface for it. I would say it's similar as far as running and deploying it to Spotify's backstage tool, where you stand it up within your own environment and we'll get into the methodology, but essentially connected to your cloud provider accounts and are able to view estimations for a given time range that way. I think the origin of it and why we created it is a fun story. Maybe I'll kick it off to Cam to speak more to that point.
**Cameron:** Maintaining Cloud Carbon Footprint has been really awesome. We have a really great microsite that contains well thought out documentation and blog posts and basically how you can understand the ins and outs of how Cloud Carbon Footprint works from both the calculations and to the methodology. It's getting iterated upon for the last few years now so that's one of the awesome things that we'd like to say to the contributors is it's always open for feedback and anybody can help contribute to it.
**Alexey:** That's amazing. That's amazing. Cameron, you touched on something that I would really like to ask you. It's as much a framework, a methodology, or a way to do the calculations as it is a tool. Maybe you can talk a little bit about that. How does it come with the estimates and where did it come from? How did you develop that as well? Because that's an important and complex part of that as far as I know, right?
**Cameron:** Yes. Basically, when we open source launched Cloud Carbon Footprint or even before that really when we were trying to decide what to build and how to build it, we decided to come up with a tool that could measure your Cloud Carbon Footprint and there wasn't really much out there. We had been referencing Etsy's Cloud Jewels, which is actually a very foundational piece of the Cloud Carbon Footprint methodology.
We refer to that on the website and basically just built on top of that. The idea of why there needs to be a methodology is because at the time the cloud providers or the major three did not provide the details for Cloud Carbon Footprint. We had to essentially get data from billing and usage reports and convert certain metrics that we're able to grab into energy and then from there convert that into carbon emissions.
Needless to say, there needs to be some sort of calculation or methodology in place and there needs to be different calculations for different basically usage resources. I know we might dive into more technical details but that's a pretty high level of how we need to go about making these estimations.
**Ken:** You mentioned that there weren't really other things out when the idea came about and we first started creating this tool. Since then, most of the major cloud providers have done something. I remember very early on, at least, the numbers really always didn't add up. Different providers look different ways and so forth. How did that shake out? What's it look like versus the other tools? Why would you use this over, if you're using AWS, why not just use AWS tools or should you now?
**Arik:** Yes, I can tackle that one. Essentially, I think there's a lot of fundamental differences. Of course, as you mentioned, every single cloud provider essentially has its own methodology that's out there and its own way of doing these estimations. One major thing is the way we source our data. Cam mentioned that we have to go about gathering usage details to convert to energy, then to convert into carbon emissions.
The way we source those usage details are directly from your cloud provider billing data since a lot of setups are essentially monitoring your usage or pay-as-you-go setups that we're able to get that granular level information pertaining to, one, how much hardware you use or how much resources you use, such as if you're running a virtual machine, the amount of compute hours you're using, and then the type of configuration that you have, which is the machine specifications in this case of what microarchitecture for the processor, how much memory you have configured, how much storage, all of that fun stuff.
That's like the one major fundamental piece is how we source it, and that goes into the major difference of how frequent you can get these estimations. A lot of the cloud provider tools essentially show you at least a month or sometimes even a few months back as far as your estimations for your usage versus with CCF, we can do it as frequently as we have usage data available through the billing data, so we can show you estimations from that same day or from the prior day.
We also offer different levels of grouping or granularity, so you can view your estimations at a daily level, or a weekly level, monthly, quarterly, or yearly, and a lot of cloud provider tools essentially default to that monthly granularity as well. We also provide energy alongside emissions because sometimes you may want to see your usage in terms of kilowatt hours. Some cloud provider tools default to just the emissions and metric tons or kilograms that you're emitting.
There's fundamental differences there, and of course with our methodology being open source and transparent, that transparency and the methodologies can differ as well, but as far as recommendations go as to where we see our usage comparing to those cloud provider tools, we actually recommend you use them in tandem because at the end of the day, our goal was to give you the most holistic transparency in your usage and emissions, and we have done work, to your point, Ken, of getting our numbers as close to theirs as possible.
As they iterate on their methodology, we try to iterate on ours. It's a good feedback loop of confirming whether we're too far off the mark and what makes sense, especially as we dive into the way they go about it, but of course, if you want the most holistic view, it's good to have CCF to show you that multi-cloud level usage in one dashboard, which we found that a lot of organizations, they don't tend to stick to one cloud provider so it's nice to have an apples-to-apples comparison, single methodology application across your entire infrastructure, no matter what CSP you're using but iIf you want to dive into granularity with a specific cloud provider of maybe using CCF to see estimations for one, and also using a second cloud provider to confirm those numbers.
It's up to you based on your use case, but we never recommend one over the other. The more, the merrier in this case, especially since at least we hope the setup doesn't warrant too much work that would stray you away from it but there's also tons of other differences I can go into as far as the tool itself, which I mentioned how customizable it is, how the level of configurability you get with it, and a few other things that stand out as well. Those are like the main things that we like to call out.
**Alexey:** Yes, amazing. The multi-cloud aspect and being able to compare that across the board under the same method is a great thing to me. I'm sold just on that one. Then, can you talk a little bit about examples? Who's using it or in which ways have you seen companies use CCF and what are they use? Any examples to share?
**Cameron:** I can start that and then I'll throw it over to Eric because I think probably I have like a couple ones we could call out. We have a public case study actually with a company called Holaluz from Europe. They were actually one of the very first, I guess clients we had with CCF, where we were able to help them implement that into their own basically organization in AWS.
It was a really great experience. It was the first time we were able to understand what sorts of specific user requirements might be needed, what problems we might run into as we're trying to get this app deployed, scalability issues that we could iterate over as we went to improve the application. Really for Holaluz, I think the idea was just to get something up and running just at a very base level so that they could have some measurement in place. I think as we grew with CCF, part of our thinking shifted to, how do we implement CCF for our clients, but then also help drive them and steer them in a direction where they can really make use of the data they're seeing.
This really gets into this concept of green ops where you can work with sustainability data and use it and bring it into your cross-functional data to have metrics that actually matter and, generate reports, do visualizations and charts and make sense of them and a whole lot of other stuff. That was our first example really. I know that Arik actually was involved in the publishing of a new case study. Maybe I'll let you speak to that one.
**Arik:** Yes, for sure. Thanks, Cam. We actually had a case study for a recent client that we've worked with, which is Ivan. They're essentially a data platform company that provisions a range of different cloud-based services to their customers. We have a case study that went live with them earlier this week actually. Essentially what we did with them is a testament to the question that you asked earlier, Alexey, which isn't the bread and butter of CCF the methodology, which we think it is.
A lot of people mistake CCF as a SaaS product, but we emphasize that it's a tool, whether you're using the methodology to help accomplish your own goals or you're using any entry points to the tool itself like the API, CLI, to embed it in your current systems or to use those as is based on what we have set up out of the box. A good example of this is what Ivan wanted to do is they wanted to bring carbon emissions data and calculations to their customers as a way of displaying or making that data available through invoices or through their internal platform whenever they bill and show their usage information to their customers.
What Ivan went is that we served as SMEs and advisors on that engagement where they were actually able to take CCF methodology and build a new Python-based tool that would essentially serve as an integration of CCF within their system. That way, whenever customers get billed or sent a report of their usage from the previous month, that they can also see their carbon estimates and their impact based on that usage within that same type of dashboard or report.
I love telling this story because I think it's just, again, a testament to how customizable and flexible CCF is to where we really tried to hone in on the methodology just to make this type of work possible. We'll be speaking some more about this. We plan on releasing a white paper about it and have an upcoming webinar that we'll be sending invites out for soon and communications as well. If you're listening, feel free to keep an eye out for that and if timelines overlap, then definitely maybe rewatch the recordings or go back and view that.
I think that's just another awesome example of just, again, ways that companies are using CCF, as Cam mentioned, from different spectrums of standing it up as is inside of your current environment and using CCS dashboard out of the box to building something completely new just based on the methodology of the tool itself.
**Ken:** That actually brings up something that I think one of you brought up earlier, a little bit about how it's deployed. A lot of times these types of things are SaaS tools and you get what they gave you. You get whatever your dashboard looks like and you can do what they predicted and nothing else. I know that's not the deployment model for this. What is the deployment model? How does somebody get and use CCF? Do they have to write their own Python or can they download something?
**Arik:** Yes, for sure. One thing going in and that we've emphasized throughout its entire development is that we wanted to give options. I mentioned Backstage as an example because if you ever stood up and maintained your own Backstage instance, the idea of CCF is the same in which you would clone the repository of CCF or create a new instance of the app via NPM script that we've made available. Then you would set up your environment variables and configurations to connect it to your appropriate accounts and point it to the correct billing table so it knows where to actually get your usage data from. Then how you go to deploy it is totally up to you.
We have Helm charts and different configurations to allow you to stand up a Kubernetes cluster if you want to deploy it that way and scale it through that method. We have AWS CloudFormation templates if you want to easily deploy it to EC2 instances that way. We also have write-ups and blogs on how to stand it up manually in a virtual machine. We have, if you want to stand it up in a serverless option, such as like Google App Engine, we have templates and configurations already ready to go for that so all you have to do is download the gcloud CLI and just run the appropriate commands. It's pretty flexible.
We also have Terraform scripts ready to go as well as a starting point for you to customize and deploy it that way. It's again, a combination from ways that we've deployed our own CCF instance through smaller sandbox or different organizations within Thoughtworks, things that community members have contributed and actually opened up PRs for that they've said, "Hey, I actually prefer to deploy CCF this way, so here's like an example script of how I did it and we make it available to the rest of our users or just things we've done with clients that we found was best for their environments, and with permission, of course, we were able to build back into the tool as another option.
We try to take a very unopinionated approach in that regards because again you never know if someone is standing up a full CCF React dashboard and API in tandem with each other or just using CCF's API to connect it to their existing dashboard that they use for monitoring costs or usage or whatever they may have going on within their organization. We try to take a hands-off approach and hopefully offer as many options and resources to get you started in the way that you want.
**Alexey:** Yes, it's interesting. you've been mentioning customization in several different ways. It's not just options in which we need to deploy, you can also use parts of the Office TCF in different ways and integrate that to an existing ecosystem. Maybe we can shift gears a little bit and then start getting into some of the more technical details. Can you talk a little bit about the overall architecture and then how does that lend to customization and to different users of TCF?
**Arik:** Yes. Cam, maybe you want to tackle this?
**Cameron:** Yes, I can now. I can start. basically we've got CCF obviously living in a GitHub repository. It's a mono repo where we have, React front end dashboard, and then we're also using a node and express on the backend, and we have a number of different packages or basically different services trying to make it fairly modular where we have our core logic separated from logic where you need like specifically for connecting to AWS or GCP or Azure. We have different packages for different cloud providers. We also have different packages for connecting via the CLI or the API. We have different ways that users can interact with CCF and get the data.
We basically have our front end or our UI so the dashboard that you can load up. Then we also actually have a demo that'll be connected to the API that CCF has exposed. There's a number of other ways you can get the data as well. Another package we added more recently was our on-prem package. We had data separated or logic separated rather to help calculate for on-prem estimations that we wanted to start trialing out as well.
Hopefully, that helps from a high level architecture but basically another visual I can try and give you. I actually have a visual in my mind. It's an architecture diagram that Arik had created where it's sort of understanding the flow of the data. Basically when you use CCF, you're connecting all your cloud providers that you'd want and you hit the API that tells you what cloud provider you want to connect to, what time frame of data you want.
You can even add even more filters than that but then you'll essentially grab that data from the usage or billing data from the cloud providers and then that data gets returned, and we essentially do the core logic that separates out the usage data into various categories, like compute, networking, storage, and memory. Then from there we go about creating our estimations that are returned in our API format. That's the pretty standard way that we use a CCF, but there's a number of other ways, like I mentioned, CLI which is very useful for some folks. Arik, feel free to chime in if you think I missed anything blaringly.
**Arik:** No, I think you awesomely called out something that I wish I would have pointed out earlier, which is that on-premise piece and how we were able to leverage, CCS methodology to, essentially make estimating on-premise data centers and even anything granular, such as, laptops and desktop usage as well.
As far as the data outputs, it's unique in the way which works and which essentially given our data model which we have added on our microsite and detailed documentation on, what information is needed for that, as well as a cool article on our blog, as far as how to, go about gathering the data for that, but you essentially use a CLI to provide a CSV input of all of the different on-premise machines that you wish to estimate, and then we use the same methodology and same data and coefficients that we use to see CCF to output a usage for each of those line items as a CSV output.
I want to call that out because we mentioned dashboards, we mentioned API, but we support CSV outputs as well. In terminal tables. Even if you're using a dashboard, we support being able to export the data within a dashboard to PDFs or CSV files to share around your organization. Another cool piece I wanted to mention as well, which again is a testament to the customization and extensibility of the tool is that we've also added support in partnership with electricity maps as well to add support for marginal and real-time carbon intensity data, which is great because electricity maps has tons of cool data for carbon intensity of regions across the world.
It offloads a lot of that work that we've been trying to keep them updated to the awesome work that they've already done, but also adds, again, some of that marginal carbon intensity data that we talked about in which you can include carbon-free energy percentages and incorporate renewable energy metrics relative to that region. You can also go ahead and of course get real-time data for a specific timestamp in that region. What the carbon intensity, number may be at this moment in time in New Zealand may be different than what you have two or three years ago for that same region.
We're able to get the actual, accurate number for that as well which is really cool and something that we've been finding has been valuable for people that not only want that real-time monitoring, but also want that historical data collection and care about the accuracy for that. I just wanted to shout that out as well because I felt like that's an important part of the nitty gritty technical details and again, of how extensible CCF is, but that's pretty much hits it on the head.
**Alexey:** Yes, that's really cool. Nice, nice, thanks for sharing. Maybe you mentioned the architecture diagram, we can link that to the show notes so people can have access to that and have a look at it if it helps as well. How about, the maintainer's life? What were the main challenges? From a technical perspective, there's a lot of innovation and I imagine lots of hard problems on the way. What were some of the challenges in doing and evolving CCF? Maybe some of the problems you have right now from a more of a technical perspective, would you care to share some of that?
**Cameron:** A couple of things that come to mind for me are, I guess there's different levels of problems. There's problems that arise from working onour Thoughtworks team, like developing CCF and there's just problems that we face just trying to keep improving upon CCF. A problem just like on a team level is, we had some dedicated folks on Thoughtworks working pretty full time and we always tried to promote any other ThoughtWorkers to join and help out when they wanted to, but not necessarily in a dedicated manner, so usually a lot of folks on the beach.
We had to really learn how to effectively onboard some people. Then also off board the same people, a couple of weeks later, if they got staffed and really keep that context going and make sure we were doing it effectively where we didn't feel like we were wasting time in that way. That was a little difficult to navigate, but we did get some really awesome contributions from some ThoughtWorkers who were interested to join.
Something else that came to mind was, as we're developing CCF, we're very limited to Thoughtworks data. As we're trying to implement different cloud providers, we need Thoughtworks to use those cloud providers so that we can connect and see what the data looks like, see what scalability problems we might face. Scalability was especially difficult to work with because Thoughtworks doesn't have that much cloud usage. We're primarily consulting and not doing our own stuff, so we had to rely on contributors or partners to really understand scalability issues and also other cloud providers that might want to be implemented that Thoughtworks doesn't use.
Those are just a couple to name a few, but I'm sure if I thought about it for a little bit longer, could have some more, but Arik, I'm sure you have some good stuff too.
**Arik:** No, I'll piggyback off of that and definitely say scalability was one of the larger things. It goes in just when you're relating to Cam's first point about the difficulties of onboarding and offboarding, that this is just such a complex and relatively new type of domain that it took a lot of upscaling and learning and things that we are still learning every day as developers of the tool.
When we're talking about whether it's getting contributors or engaging with the clients, we're trying to ramp them up on the amount of necessary knowledge needed for this tool because now you've got to learn micro architectures of processors and to all the different type of services across cloud providers and the nuances across all of the different. CSPs of how a virtual machine and ways you go about gathering usage on Azure may not be the same way that you go about doing it on Google Cloud and et cetera. Those are definitely one of the main challenges. Since we're taking this multi-cloud approach, we try to practice keeping all the different-- I guess the proper term is feature parity across all the different cloud providers. Just out of fairness, we don't want to give edge to the other one to be able to support that multi-cloud model that we talked about. If we're developing a feature, we want to make sure that it works the same way or at least has its own implementation with the same result or similar result across all the cloud providers that we support.
That's a challenge within itself because there's, again, so many different ways that a lot of the different cloud providers operate that there's a lot of gotchas when we're implementing one thing for a cloud provider and then trying to implement the same thing for another but the scalability is also a big thing as well because as Cam mentioned, we don't have as cloud workers, a lot of internal cloud usage outside of the few internal tools we have because we typically go to a client and work within their space.
We've discovered that a lot of the problems like CCF has to work for the individual that is maybe building their first startup and wants to get ahead of their cloud usage as they're beginning, and also, for the large enterprise customer that has multiple applications with millions of users, if not billions, and is trying to make sure that they are getting ahold of their footprint for these apps that already work. Again, that could also go into the use case of a user that is trying to just get real-time feedback who only cares about seeing their carbon emissions for the same day, so that way they can remediate it versus someone that wants to actually track their historical usage for across a few years.
That can range anywhere from, again, dealing with just a small subset of a small few rows of data to millions of rows of data that the tool now has to support. That was one of the big challenges we've come across and have been trying to tackle just in terms of adding support for MongoDB and their robust database and making sure that we're building out those flexible database options and supporting different deployment options as well that enables not only that individual user or that startup or that small to mid-sized company, but also the enterprise customer.
Again, making sure our deployment options aren't just the naive one-and-done virtual machine approach, but also, again, can support Kubernetes clusters and more robust infrastructure and making sure again that we're flexible to all of those different use cases and thinking about the different spectrum of users that we may come across. I think those are like the main challenges we've been dealing with and have been adding hopefully cool new features to support.
**Ken:** Especially like you mentioned, the people using it run such a gamut. What's the open source model like? A lot of times companies will open source something and they say, "Here's the source code," but they don't actually take any pull requests or that sort of thing. What's the model like? Do you take pull requests? How's the project managed? How do people get help with the code base? That sort of thing.
**Arik:** Yes, for sure. We go off an Apache 2.0 License. By nature, anybody can of course clone and build off of CCF. Of course, there are some tools that have already done that, so some third-party tools that are out there that utilize CCS methodology as a way, or even build on top of one of the implementations of CCF within itself. We're pretty open. We take pull requests. As Cam mentioned, we're hosted on GitHub. CCF wouldn't be possible without the community of contributors and people who have provided feedback and have contributed to the tool over the years. We encourage issues on GitHub, whether it be bugs or feature improvements, or just even general praise, if you would like to do that as well.
We're pretty flexible. We've had organizations come and as they're standing up, CCF may contribute back a pull request that has helped them out in their implementation that they want to build back into the tool. I would say pretty much just standard open source model, but we definitely welcome contributors that can be anywhere from making methodology changes to actually building out a full feature for CCF, which is where Alibaba Cloud came from, was the actual contribution to the code base itself.
**Alexey:** We're getting to the end of the episode. Maybe, perhaps if you have any final comments or any final thoughts you want to share, I don't know, maybe a personal learning that you had contributing to CCF and helping build it, something cool you have learned personally, or some other thoughts that you want to share with our listeners.
**Arik:** I'm so sorry. I did have a comment I wanted to add to the last question because I left off two very important points. Our project and overall issues and roadmap are all public within GitHub as a project board. You're welcome to view that and comment and add support for those roadmaps. We tend to prioritize our work based on what we see from the community. If we see there's a feature that the community really, really wants, we adjust it to our roadmap accordingly. If it's something new, we'll add it to it. If it's something that the community deems is not important versus another, like we're always flexible and try to accommodate that.
We try to make ourselves available as well. Just as far as getting help or asking questions and maybe wanting to get involved and become a contributor. Again, we're on GitHub through the discussion board or through conversations via issues, but we also have a Google Group that you're able to join, which you can view on our microsite and we'll provide a link for hopefully people to join where it's pretty active. You can ask questions and get help from not only the team itself, but also other users as well.
We mentioned that we're partnering with organizations that wish to be regular contributors to CCF and so we're trying to build a more immediate way of communicating with us that isn't through the Google Group or GitHub. Currently we're working on a Slack that people can hopefully join and get even more direct access to us and more community conversations as well. Sorry, I just wanted to throw that in there because I didn't want that to go left unsaid. As far as your last question for last thoughts, I'll pass it to Cam.
**Cameron:** I'll kind of echo Arik said one of the things about maintaining is having the visibility into who's really using it so we don't really know unless people reach out and let us know or at their name, the ADOPTERS.md. It really gives us a good sense of things. Even a lot of the questions you were asking us, what are some examples of people using it? What problems are they facing? These are all questions we really would love to know so that's always a plug I like to give.
I just like calling out the fact that being an open source software maintainer is just a really cool experience too. It's afforded Arik and I opportunities to speak about it like this in a lot of different ways, get to meet really awesome people, get to face unique problems dealing with the community and have a sense for just other general open source software too and look upon it in a different perspective as a maintainer, like Backstage, for example, "Oh, I wonder how these maintainers work on a day-to-day basis and what challenges they face. It's a really awesome art about being a developer for us so that's what I'd say.
**Alexey:** Cool, cool, thank you. I guess this takes us to the end of the episode. Cameron, Arik, thank you so much for joining. It's been a pleasure. Thank you all so much for listening. See you next time, bye.
**Ken:** Thank you.
**Arik:** Thank you.
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
## We can help make your cloud greener
[ Learn more ](https://www.thoughtworks.com/en-th/what-we-do/enterprise-modernization-platforms-cloud/green-cloud)
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