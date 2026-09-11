<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-sql-etl | Title: Exploring SQL and ETL | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring SQL and ETL 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Data science and analytics ](https://www.thoughtworks.com/insights/topic/data-science-analytics)


Podcast host  Neal Ford and Rebecca Parsons  | Podcast guest  Bharani Subramaniam and Madhu Podila
September 21, 2023 | 31 min 57 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-sql-etl#Transcript)
Listen on these platforms
## Brief summary
The evolution of SQL and the ease of access to ever larger sizes of computational power has made SQL and ETL a useful pairing for practitioners in the data space. But how do they work together exactly? And what challenges can it pose?
Bharani Subramaniam and Madhu Podila discuss these issues and much more with hosts Neal Ford and Rebecca Parsons on the latest episode of the Thoughtworks Technology Podcast. 
## Episode transcript
**[MUSIC PLAYING]**
**Neal Ford:** Hello, and welcome to the Thoughtworks Technology Podcast. I'm one of your regular hosts, Neal Ford. And I'm joined today by another of our regular hosts, Rebecca.
**Rebecca Parsons:** Good morning, everybody. Rebecca Parsons, one of your other regular hosts. And we are joined by two colleagues today. So Bharani, would you like to introduce yourself first?
**Bharani Subramaniam:** Yes. Thanks for having me here. I'm Bharani Subramaniam, one of the heads of tech in India.
**Rebecca:** And Madhu?
**Madhu Podila:** Hi, this is Madhu. I'm a data strategist based out of India.
**Neal:** Great. Well, thank you for joining us today. And today, we're — our industry is rife with acronyms. And today, the entire title of our podcast is just two acronyms together: SQL ETL. So let's talk about — this is actually something that came up as a too complex to blip topic, I believe, on our previous radar meeting, which was the seed for talking about this subject. So let's talk about SQL ETL and start by defining what these acronyms mean and what are we actually talking about in this podcast?
**Bharani:** We all know SQL. I don't think I need to introduce SQL to our listeners. So I think someone told me that SQL is probably one of the best or the most widely adopted DSLs in the world right now because it is — you don't realize it's a DSL, but it's actually — you can do quite a lot with SQL nowadays. So what's interesting is the usage of SQL in ETL has gone up, right? ETL stands for extract, transform, and load: So you basically, if you have two systems, and you need to connect them together, these two systems have been built over time, they have different internal representations of the data, so you would take a dump and then transform it, usually outside your database, and then load it back into the structure that you expect to have in your system. But SQL is not used in ETL mostly. You would use some other tool like Talend, Informatica, or other, even Excel, to do the transformation, and then finally load them with the SQL script. So ETL was mostly in the load of the ELT than the transformation.
**Neal:** So two quick things, first, you used another acronym when you were defining our acronym, which is DSL, which is domain-specific language, which you're contending that SQL is, in fact, a domain-specific language, and it certainly can be. So, that's the first one. And the second is, can you give us an example of the kind of transform you're talking about here? So you extract data, you transform it, and then load it back in. So what's the purpose of this transformation? What's an example of some reason to do a transformation like that?
**Bharani:** Yeah, so I did talk about two systems. Usually, the first system is a transactional system, so this can be your order entry or an online shopping cart service. So those are transactional systems. And then, you might have a data warehouse or an analytical system where you want to make some BI reports and do some intelligence on your transaction data. If you are connecting these two systems, the internal structure of your data, you've organized it for a transactional use case. So if you have to — if I take a step back, you need to change the shape of the data so that you can do efficient analytics on top of it. And that's the part of transformation. So people traditionally had a star schema in the warehouses whereas more normalized schema or something different on their transactional systems and hence transform as you can think of shifting the shape of data to fit for your purpose. And that's traditionally done outside SQL, is what we're starting this conversation with.
**Rebecca:** Well, and one question I have always had about ETL is when you listen to your description of what that transform phase is, the term that always comes to my mind is data migration. And data migration is — it's very easy to define and incredibly hard to do. So I know this is a little bit of a tangent, but can you talk a little bit about why this is something that you can do over and over and over again, which is what you have to do as you — is it because the data is current, and therefore, you don't have those little landmines that we always have with data migration? But that's always the thing that pops into my mind when we talk about ETL, is, why doesn't this break all of the time?
**Bharani:** Of course. Madhu, you wanted to add something?
**Madhu:** Yeah, I think what Bharani talked about is right. You have operational data, end of the day, you need to make sense of that to make business decisions. And you cannot put a lot more queries on the operational system; it's not inefficient to have analytical queries. This is where you take out the data from an operational system and try to shape it in a form where you can have run analytical queries so that you can effectively make business decisions. And this is not a one-time. So there are — transactions keep coming. Your business is continuously operating. You need to continuously capture the new transactions and analytical queries and continuously run on the newer and latest data on historical data. I think that is the reason you need to continuously do this process all the way.
**Bharani:** So I'm going to respond to what Rebecca said. So when you have some kind of migration, you have well-defined data in your database in some schema version A or structure version A, and then you have a well-defined version B that you need to migrate to. So you know upfront the shape of data that you're going to transform. And you can write a migration script in increments, you can up-migrate, you can down-migrate, see if everything is OK, and then you're good to go. So this ambiguity of the shape of data is very less when you're migrating, typically, in a typical setup, as opposed to in the pipeline that we talk about in ETL, it's, in most of the cases, you may or may not know the shape of the data because you would be integrating with third-party systems that you don't control, and they change the schema without informing you. And that's the part where the transform in the ETL or ELT is flaky, if I can put it that way. Because, unlike your migration scenario, you don't see the data upfront or the shape of the data upfront, and it tends to be a little unstable at times.
**Neal:** Well, and one of the destinations that used to be a popular destination for this kind of data is a star schema, which is a schema that's optimized for doing queries for this kind of analytical behavior. But it seems to me that that's also very fragile because if you change your operational schema, that has to feed into the star schema, which is fundamentally different. And so I think that's part of the traditional resistance we've seen from database administrators in enterprise environments from changing schemas because you're liable to break that downstream operation that relies on this kind of known certain known quantity on the other side.
**Bharani:** Exactly, yeah.
**Neal:** OK, so why is this interesting now? So I think we've defined terms. Extract, transform, and load, we understand what that is. We understand what SQL is. So let's talk about why this was a subject that came up in our TAB meeting because this has obviously been around for a long time. So why is this an interesting topic now?
**Madhu:** So I think there is a history to it. OK, so if you traditionally start with the traditional data warehouses, there is limited by the computing power and a tight coupling between the storage and the compute together. And I think people started with the SQL and PL/SQL to do the ETL's part. And there is always competing workloads with analytical versus transformation workloads. That is the time ETL tools come into picture. OK, you can offload the transformations and database prime or warehouse primarily used for analytical queries. So over a period of time, again, big data came in, and people did not have a chance to leverage SQL. People moved towards MapReduce then spark and those things. And there is cloud computing, I think, more and more power being added to the processing. Again, this is the time, especially if I talk about the cloud data warehouse, BigQuery, or Snowflake. These are game changers. The first thing is separation of compute and storage, and also there is a dynamic compute loads. Snowflake says I have a virtual warehouse, I can use certain virtual warehouses for integration workloads, certain warehouses for analytical queries. So there is no compete in the compute power. Similarly, there is a BigQuery. You can say burst computing or dynamic computing is always available. OK, so one side you have great SQL skills by the data professionals earlier limited by the computing power. Now, there is abundant compute power. And you can leverage the same SQL to do these kind of transformations. OK, we have scalability coming into picture so that people naturally tries to move towards that. Other thing which I wanted to talk about is there is continuous innovation is happening. Even in big data worlds, also like MapReduce moved to Hive, then Spark also started supporting SQL. Even Databricks started giving the SQL endpoints. What I wanted to talk about is further new innovations like DBT tools came into picture, which is more and more encouraging the engineering practices bring into the SQL world. That is one of the, I think, drawback, I would say, SQL deploying as ETL pipelines, and those things. DBT actually bring those —a lot more engineering practices, version control, modularity. Then, you can survey promotion easily from one end and another environment, testability by expectations. OK, all these kinds of features bring into the SQL —which makes SQL more powerful. I think that is the reason I think I can leverage MySQL skills and also bring a lot more transparency to the transformations. So even business users can look at this: oh, this is looks good to go for my business rules.
**Bharani:** Yeah, I was just going to say plus one. Over the years, SQL got a little bit more interesting because we've got more and more analytical functions got added to the language. I know different databases support different levels of SQL, but you've got things like windowing functions. You've got common table expressions. There is even a group that argues SQL is now Turing complete! We can agree or disagree to that, but they've implemented cyclic tag systems, which is a Turing machine. So SQL got a lot more analytical power and a lot more expressive, though as not expressive as your common programming language. But it has got better over time. So the fact that SQL has this new capability together with Turing, like what Madhu mentioned about things like DBT, those are the enablers, I would say, that makes SQL a very attractive option if you want to do the transformations inside the data warehouse.
**Rebecca:** So we've often talked about things like stored procedures on hold and all of the different ways people try to use SQL too much. How would you respond to someone who says, aren't you being inconsistent by saying, oh, SQL is now this wonderful, powerful language, but you shouldn't use SQL this way, but you should use SQL that way? How do you respond to something like that?
**Bharani:** I think a part of that advice is still true. We don't want engineers to write their business logic inside a database and hence — because it makes it difficult to version, difficult to test, and it makes our life much more complicated. You would rather use a full-fledged programming language for that. But in this case, what makes SQL interesting is that you get all the goodness of a proper programming language, like what Madhu was talking about earlier. You can write modular code because tools like DBT leverage a templating engine. So you can write small reusable functions in SQL. And then, with the templating engine, it will kind of compile it to a complete SQL in the end. So you get that modularity in SQL now. You can check it into your source control and version like a normal programming language. You can write unit tests for this piece of functionality, which makes it great. So you get all this goodness minus the negative effects of having a store proc. So that's why it's interesting. So it is not one advice to say that do everything in SQL. That's not something you're saying. But if you have — it always depends on what is a simple transformation. But if you have that level of capability of SQL in your team and you think this is straightforward to implement and model in SQL, I think SQL is still an attractive action, attractive option, sorry, for transformation.
**Madhu:** Yeah, I think if you can model your business rules as SQL logic, as long as it's not too complex, OK, I see the code, having a 10 self-joins, as long as you're not getting into that zone, I think still SQL is still a better choice.
**Neal:** So that brings us to the inevitable, which I think is why this ended up as too complex to blip on our radar, which is the context. So we're not saying that you should always only use SQL as ETL. So let's talk about what are some of the contexts where you would or some of the situations where you would and would still continue to use a specialized tool for this kind of stuff. So this is — what is this better for and what are alternatives or case studies that would still lean you toward some of the more traditional tools? 
**Bharani:** I'm going to introduce another acronym. So we talked about ETL. Now, there is another acronym which is very similar to it called ELT. So it's basically as if you are swapping L and T, the order of L and T. So you basically extract the data, you first load it in your data warehouse without doing any transformation, and then use the SQL engine of the data warehouse to do the transformation. And this way, you can use SQL power. And since the data is already in the data warehouse, it can manipulate it much faster. So just to answer your first question, when you should embrace using SQL for transformation, most likely, you are you are embracing ELT instead of ETL. So you have data already loaded. It's far easier to just use the existing DB engine to do transformation instead of going out of the database. So that's the first option. And the second one, for which the real answer is it depends, what Madhu also said. If your transformation logic is straightforward to implement, and you're not doing excessive joins, and it's — you would know that it's in a mess. Unless you're not in that state, I think it's still OK to do that transformation in SQL. 
**Madhu:** Just to add, I think another point to where you don't use in SQL as a first choice is when you're dealing with unstructured data or semi-structured data. SQL is not competent enough to handle that. This is where you use other programming paradigms to handle the unstructured data, structurize it, then hand it over to SQL for the transformations.
**Bharani:** Yeah, that's a good point. Yes. Yeah, SQL, by its very definition, works on structured relational data. Yeah, so you have that limitation. Though, more and more, with support for JSON, you can do semi-structured, but it also depends. If you are working with a really dense JSON that you think you're better off with a third-party library, then just pick a programming language to model the transformations.
**Rebecca:** So this is definitely one of those cases where we need to be cautious of, oh, gee, 80% of this is easy, and 10% of this is a little squirrely and the last 10% of it is a mess. So we need to be cognizant of when we are falling off the cliff of, gee, I really shouldn't be trying to do this with SQL. I should be using a more powerful tool.
**Neal:** Yeah, I think part of what — so the elephant in the room in all these conversations, and the reason you have to think so much about where things run is because we're talking about such huge volumes of data. And to Madhu's point earlier, the entire ecosystem that we're dealing with has changed recently because of cloud environments where you can, in fact, run these massive queries against your data. So that would lead you to some ELT environment where you do have enough resources, where a lot of the battle. And a lot of the need for the tools before was to offload the actual workload of this data because there was so much of it, and you didn't want to bog down your existing system so much.
So being able to separate things cleanly operationally like that with cloud environments, I think, makes this a more attractive option, coupled with the fact that SQL has gotten more powerful. So it seems like this is one of those places where a lot of people started rejecting SQL to do this because it wasn't powerful enough and because of resource constraints. And then, slowly, the ecosystem has evolved and changed to the point where now it’s time to reevaluate this for some situations where you might be currently using some sort of specialized tool. Is that a good summation of what we've been talking about so far?
**Bharani:** Yeah.
**Neal:** So Bharani started talking about some of the things that you should do with SQL. So how do we have some advice, some best practices, and some good approaches to take if you're going to do this because we realize, too, that SQL is a golden hammer in some organizations and ends up getting misused, as Rebecca was alluding to before, getting you closer to that last 10% trap. So what are some of the ways to some of the best practices that we've figured out if we're going to use SQL for this purpose?
**Madhu:** Maybe I would say one of the things is yeah, bring the engineering practices. Make sure that you version control the SQL files and try to modularize. OK, breaks the complex transformation of multiple SQL transformations so that you're able to manage easily and you can make necessary enhancements in those things.
**Bharani:** Yeah, I was going to add that this whole — okay, I'm going to add yet another acronym! It's called DAG, directed acyclic graph. If you are familiar with SQL, this term does not come up often. But if you have built a data pipeline, this comes up again and again because what you're doing in a data pipeline is basically you're building a DAG along. There is some kind of a graph because you have to break the problem into small chunks and then stitch them together, and that forms a task execution graph. So when you start using SQL to do transformation, like what Rebecca was saying, there would be parts that are easy to model, that are parts that may be difficult to model. There are parts where you're better off spinning up another programming language or a JVM or another spark engine to do the compute and then combine and then join back with SQL. You need to be aware of how the structure of your DAG looks like for you. And that's something that's critical because there are tools that make it easier. But if you're not familiar with that, then there could be rough edges when you start modeling it in SQL. So I think the knowledge of the tools in the ecosystem that make it easy to build a DAG with SQL is really, really critical. The familiar tool that we have spoken about in the radar is DBT, which stands for data build tool. So that's the tool that we have used often that makes it easy to just do this with SQL. Everything that Madhu talked about, reusable small pieces of functionality modeled as a template and SQL, those would be the proven best practices, things that we have borrowed from the traditional software engineering, right, like write small piece of code, write unit tests, version them, manage dependency, that, I think, that's the most critical part where if you start building reusable components, you need the tool to manage the dependencies because, otherwise, it gets tricky. So yeah, all of that.
**Rebecca:** So basically, treat this whole process as if it was just another part of the software development life cycle — which it is.
**Bharani:** Yes! [Laughs]
**Rebecca:** It's amazing how often our advice comes down to just treat this as it, which is — this is code that contributes to your overall ability to deliver business value. I like it.
**Neal:** So let's talk about the negative trade-offs since this was/became too complex to blip, so there had to be some. So what are places where you absolutely should not try to use SQL as either ETL or ELT tool? What kind of scenarios would you say not?
**Bharani:** I think the first one is like, Neal, you were talking about, if you are not — if you do not have a massively parallel processing data warehouse, then using SQL for transformation is a bad choice because you need to have that elastic compute power if you are doing transformation at scale. So that's the obvious one. The not-so-obvious, that kind of hits you hard, is if you do the ELT, which is extract, and then load it first and then do the transformation, you are directly coupled with your transactional systems or your upstream systems.
So that could be a surprise. There are ways to mitigate it. You can make the loading structure schema very flexible on demand, but that is a coupling. That is a tight coupling between your transformation logic and the structure of your upstream data, which otherwise you would not have. You would let the pipeline handle all the changes of the upstream, and you just have a very well-defined format in which you can just load it in your DB. So I would say be aware of that limitation.
**Bharani:** And then the very nature of SQL, right? There are newer syntax, there are newer functions to make SQL look like a full programming language, but you still have the inflexibility of expressing logic in SQL. If you make a small change in business logic, the structure of SQL might change significantly. So if you are in that paradigm, it's bad advice. It's a bad choice to use SQL for the transformation.
**Madhu:** Yeah, I think this comes to the complexity of transformation. If you're not able to… yeah, I think there are transformations, you need to have a procedural language or a complex programming language. If you try to model that SQL, it's very difficult to do that. I think you have to be cautious what can be modeled in SQL. Avoid it if you… it is not easy to model in SQL.
**Rebecca:** The classic just because you can doesn't mean you should! [Laughter]. Yeah, as we've been talking about this, I keep going back to the definition that Martin has in his Domain-Specific Languages book about how you actually don't want your DSL to be Turing complete because that's what programming languages are for, that this whole — the whole purpose is to model something simpler. And it seems like SQL has gotten to that wobbly stage where you want to be careful you don't lead yourself too far down that garden path.
**Neal:** Well, yeah, when you see people starting to try to implement Towers of Hanoi in SQL just to prove that they can, just like they did in XSLT because it was Turing complete. You can find online Towers of Hanoi implemented in XSLT. And I'm sure someone's done it in SQL now, too, so that's definitely a cautionary tale.And I think you have to always be cautious, even when using a more enhanced tool is to take a step back. We get into this golden hammer mentality of, oh, I'm using this tool for this, so I should keep using this no matter how really ridiculously complex it gets when you can take a step back and say, wait a minute, this is getting really, really complicated, could I use and offload this to another tool, another, like you say, an imperative programming language instead of a set-based programming language? So I think it's wise to be always paying attention to the trade-offs when you're looking at something like that and not just blindly follow, oh, we're doing it this way, so we should just keep doing it this way no matter how far in the weeds you get. I think it's good to always keep that in mind.
**Rebecca:** Well, it also sounds like that — the DAG structure that Bharani was talking about. You do have the option of saying, okay, all of this stuff can is relatively simple, and it can flow along this SQL path. And then we've got this one part of it, which is really hairy, and we'll branch that off, treat that differently, and then bring it back into the fold. And I think that having that ability within the tool chain allows for you to do the simple thing for the simple stuff and only have to use the more powerful tool for the thing that really needs it. And that's always that trade-off: well, gee, I've got this one thing that is really hard to do, so I have to use something really hard and powerful on everything. And that's technical debt. You're making things far more complicated for things that don't need it. But by having this more powerful tool chain, we can carve off that piece that's more complex.
**Neal:** OK, so that's — let's wrap up. I think this may be the episode that has had the most three-letter acronyms of any of our episodes so far! And that's a pretty high bar to hit! [Laughter] So congratulations to coming up with all the acronyms. Of course, in the data world, you end up with all those things… So any last bits of advice you want to leave our listeners with about SQL and ETL or ELT?
**Madhu:** I would say follow the best practices. Yeah, apply engineering practices while leveraging SQL, otherwise, you will be compromising in the deployability and other aspects of it.
**Bharani:** Yeah, I would echo Madhu on this. Use SQL as a domain-specific language. It has a lot of strength, but there are rough edges. So don't shy away in acknowledging that. And I would say plus one to Rebecca, is use the right tool for the job. So if there are parts of the pipeline that make sense to use and model as a relational algebra, go for SQL. If not, don't shy away from branching out and you can always come back. And there are a number of data pipeline tools that let you do this mix and match, or rather polyglot in this data processing. So yeah, use the right tool for the right job.
**Neal:** Well, like many things on our radar, there are some things that cannot be summed up in a single paragraph that take about 30 minutes of discussion. So this is a great example of one of those. So thank you so much for adding some nuance and context to this nuanced subject. Thanks for joining us today on the podcast.
**Madhu:** Thank you.
**Bharani:** Thank you.
**Madhu:** Thanks for having us.
**[MUSIC PLAYING]**
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