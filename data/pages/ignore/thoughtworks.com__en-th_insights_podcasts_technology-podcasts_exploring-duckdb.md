<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-duckdb | Title: Exploring DuckDB: A relational database built for online analytical processing | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Exploring DuckDB 
A relational database built for online analytical processing
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close
  * [ Data science and analytics ](https://www.thoughtworks.com/insights/topic/data-science-analytics)


Podcast host  Ken Mugrage and Lilly Ryan | Podcast guest  Simon Aubury and Ned Letcher
September 19, 2024 | 35 min 26 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/exploring-duckdb#Transcript)
Listen on these platforms
## Brief summary
Like every other kind of technology, when it comes to databases there's no one-size-fits-all solution that's going to be the best thing for the job every time. That's what drives innovation and new solutions. It's ultimately also the story behind DuckDB, an open source relational database specifically designed for the demands of online analytical processing (OLAP), and particularly useful for data analysts, scientists and engineers. 
To get a deeper understanding of DuckDB and how the product has developed, on this episode of the Technology Podcast hosts Ken Mugrage and Lilly Ryan are joined by Thoughtworker Ned Letcher and Thoughtworks alumnus Simon Aubury. Ned and Simon explain the thinking behind DuckDB, the design decisions made by the project and how its being used by data practitioners in the wild. 
  * Learn more about [DuckDB](https://duckdb.org/why_duckdb.html)


## Episode transcript
**Ken Mugrage:** Hello and welcome to the Thoughtworks podcast. My name is Ken Mugrage. I'm one of your regular hosts. With me today as a co-host is Lilly Ryan. Lilly, why don't you introduce yourself? 
**Lilly Ryan:** Hi, I'm Lilly Ryan and I'm another one of the hosts of the Thoughtworks technology podcast.
**Ken:** We have a couple of guests with us today to talk about a cool new product, Simon Aubury and Ned Letcher. Simon, you want to say hi?
**Simon Aubury:** G'day. I'm Simon Aubury. I'm a director of Data Platforms and I'm based out of Sydney, Australia. It's great to meet you this morning.
**Ken:** Welcome. Ned, how about yourself?
**Ned Letcher:** Hey. Yes, I'm Ned. I'm a data scientist in Thoughtworks Australia, Melbourne.
**Ken:** Welcome. Astute listeners may notice that only one of us this time has a North American accent. Thanks the three of you for joining from Australia. Today we're going to be talking about a product called DuckDB, which is a cool new database or a newer database that Simon and Ned wrote a book about, a little bit of a departure for our podcast to focus on a specific product, but this is pretty unique and new and exciting and open source and free and all the right things. With that, I want to turn it over to Lilly to run us through some questions and we'll have a good conversation.
**Lilly:** Absolutely. Yes. A lot of the questions that most folks have around DuckDB are about, what database is it? There are plenty of database types out there and all different kinds of software that's used for different purposes. What about DuckDB? What makes it special beyond a cute name?
**Simon:** I think we need to start off by maybe almost the Wikipedia definition. Then I think if you were to look at the cereal box description, DuckDB is free. It's open source. It's extremely fast and it's extremely extensible. If you're trying to do the mind map of where DuckDB sits within the data ecosystem, it's very much that OLAP, transactional analytics space. It's really helpful for overlapping the needs of data engineers and data scientists. One of the things that I really appreciate about DuckDB is it's super efficient at getting jobs done. Ned, what would you say were the highlights or the sticker for DuckDB?
**Ned:** Yes, for sure. This is a bit different to, when we think about databases, we might think about things like MySQL or Postgres. These are sort of, we've got lots of rows and records and things like applications where you're storing user data for web apps. We're in the analytical world here. Like you said, this is useful for data scientists, data analysts, and data engineers. We're doing lots of large-scale transformations. I think one of the interesting characteristics is you sort of think about this as columnar operations where we're going vertically.
We're interested in getting big statistics of big data. Maybe I want to crunch and get the average or the median. When you need to do that over large sets of data, we can't do that using these row-based approaches. That's where we're sitting. Then I guess why might you be interested in this as a data scientist, data engineer, even software engineer? If you have that sort of a workload, but you just want to spin up this on your local machine or in a small lightweight instance, it's in process.
It runs within the process that if you import DuckDB in Python, there's no external server you have to set up, no config. It just makes it sort of that lightweight, easy to access. You don't have to install and run anything. I think that accessibility, it's the sort of thing where you can just, once you learn about it, if you haven't come across it, you can jump in and get started with it super easily. We can get further into some of the more interesting and exciting benefits that it has to offer.
**Ken:** You both said data scientists and data engineers, like these are two different kinds of people, aren't all data people the same? I know that they're not, I'm being a little tongue in cheek, but from your perspective, for our listeners' sake, how do you separate those out?
**Simon:** That is a super good question, Ken. I think at the end of the day, you're right in that everyone is a data practitioner. Maybe there's sort of an anchor around skillset and a focus to where people's strengths are. I might identify myself as a data engineer. I might spend more of my working day thinking about data storage, data transformation, some of the nuts and bolts around presenting data, ownership of data, lifecycle of data.
Then I work alongside folks who might identify themselves as data scientists or data analysts, and they might be lifting up insights and actually doing exploratory work with the data. You're spot on that. I think we're all data practitioners, but we might spend maybe the majority of our day thinking about different concerns of the data. One of the things I really like about DuckDB is it's sort of ergonomic to the needs of multiple personas.
**Lilly:** How did you both find your way into this particular space? It's cool when you're talking about a database like this, you're talking a lot about its utility. Not many people would like it enough to write a whole book about it. What is it about this that's specifically compelling to each of you being data scientists, data engineers, and how did you find your way to this particular place?
**Ned:** For me, it was suddenly everyone was talking about it. This was maybe a bit over a year ago, back then it was Twitter, not X. It was just all of the buzz and people were saying, "Hey, I've been giving this DuckDB for a spin and it actually allows me to do a whole bunch of common workloads." I was hearing this from both data scientists and data engineers. That convinced me that I should take it for a spin. I picked it up and I actually was doing some scraping of Twitter data using the API before it all got too hard and expensive to use and trying to see who I followed.
I had I think something 70 million records of JSON lines data that needed to be wrangled into a consumable format. This is one good use case for DuckDB is just transformation cleaning of interestingly shaped data. For me, this was JSON, like row-by-row records of JSON data. It just transformed it in blazing fast speed. I was like, "Okay, this is interesting. People are onto something here." Simon approached me with the idea of pairing on writing a book. I said, well, that's certainly one way to get on top of this and make sure that I can bring this into my toolchain and then hopefully if that is a cool thing, share with other people and it turns out it was. Yes, how about you Simon?
**Simon:** I probably stumbled across DuckDB via a different path. I found a lot of my day job working on client sites where I had to deal with a lot of disparate data sources, data in Parquet files on top of Hadoop systems, maybe data persisted on object stores. There's a lot of very unexciting ways of lifting that data in and processing it. I found that DuckDB was smoothing away a lot of those paper cuts and just making my life easier. That was just one of the revelations I had. There was a lot of things I was getting for free by using DuckDB and by free, I mean, just reducing some of the day-to-day paper cuts of processing data.
Probably a more meaningful example of this is I had a side project where I wanted to do some analysis on my own fitness. I have an activity tracker that I wear pretty much daily. I've had essentially accumulated 10 years worth of data. One day I decided I was going to download the large archive provided a bit of a history of every time my heart beat or every time I took a step or every time I went for a run. When I pulled down this archive of data, it was something 70 gigs worth of data.
There were close to 85,000 files and I believe 27 different file formats. This just felt like, "Oh, this is going to be a bit of a Herculean task to think, 'how am I going to process all this data and do some data analysis?"' What I found with DuckDB was it was actually really straightforward to interrogate some strange JSON files, parse a whole bunch of fairly esoteric delimited files and just lift it up very quickly into a notebook so I could do some analysis.
Again, it was one of those revelations of this was not a technically difficult task, but maybe a time-consuming task. I got to that point of being able to do something quite useful with the data much faster than I had anticipated. It was essentially just smoothing away some of the day-to-day ergonomics of working with data and getting to the important and meaningful stuff. That was why I appreciated the jobs that I didn't need to do with a framework like DuckDB.
**Simon:** While we're talking about the data scientists and data engineer personas, I think it's an interesting observation that actually, originally DuckDB was intended with data scientists in mind. It was originally created by the two founders from a computer science research institute in the Netherlands. It's sitting on the top of a whole bunch of decades of database research. The observation was, hey, data scientists have jobs to be done that could benefit from a lot of database management technology that we have.
Not only things like performance, which Dr. B is great for but having nice curated tables and data catalogs and things like transactional consistency so that when you submit a query and something goes wrong, it rolls back to the previous state, which is not necessarily something you get out of data processing tools. All that ability to have nice curated data stores to help you not have piles of CSV 1 and CSV 2 renamed and things like that cluttering around.
What was interesting is that it turns out that all of these properties that it was being designed for, it turns out that data engineers went, "Hang on, this is an amazing lightweight tool for doing data transformation, data management for analytical data. Not only is it useful for ergonomic accelerated workflows for data wrangling analysis, it's also useful as a lightweight building block for lean, fast analytical processing and querying. We can actually use it for lightweight versions of things like data warehouses and data engines for applications that software engineers might be interested in." It's an interesting quirk of how things worked out, that yes, all of these different personas, it's an awesome tool for them.
**Lilly:** When you've been speaking there about a lot of the different use cases that you've personally come up with, you've spoken a lot about your personal projects and things that you've done for fun around the sides, that kind of thing. What kinds of use cases have you seen it be used for in a professional environment? You're talking about things that are in process that are lightweight, it flies under the radar a little bit. Is it capable of doing this work at scale in an enterprise environment?
**Simon:** It's a good question. I think so far, Ned and I have been describing what might be considered personal data analytics or that life cycle of an individual working with a bunch of data, maybe in a notebook or a data science or data analytics capacity. That's definitely one solid use case for DuckDB. Where I've been super interested is seeing where DuckDB is actually being used in other capacities. One place where I've used it is in tooling pipelines where we've needed to do essentially CICD on development workflows. That integration with build pipelines, integration with modern data. Tech such as DBT.
DuckDB can sit seamlessly in some of those release processes, which means that the evaluation, the coding, the schema checks are all being handled locally or as part of a build pipeline. This is great for working across teams where you obviously want to integrate your code quickly and test some of the richness and validity of schemas. It means that you're not hitting some of the more expensive cloud services.
That's a small example of what I think is a larger movement of maybe cost offset where you're using very capable, free extensible tooling to mimic some of the behaviors that are also supported by some of the commercial offerings. I've been using it in build pipelines, but I've also seen a number of clients who are essentially doing what might be considered endpoint simplification, where instead of taking huge amounts of data that might be acquired by an endpoint, such as a sensor or a network sensor or a telco collection thing.
Instead of slurping terabytes or petabytes of data into your cloud data warehouse, which can be quite an expensive thing, being able to essentially do some endpoint simplification of that data and maybe take some of the signals of the data and put that into a warehouse means that you're still achieving the outcome, but you're doing it as a lower price point, which is again, another interesting place where DuckDB seems to really straddle having competent data processing, but doing it at a lower price point or localized processing.
**Ken:** I'm curious, these are problems that are not new, right? Sometimes we see new products or technologies coming out, and we touched on this at the very beginning, like there's lots of databases and so forth, but if somebody wasn't doing this today or before you all found it, what are the other options? Is this really like leaps and bounds better? Is it incrementally better? What are the alternatives here?
**Ned:** Yes, great question. I think it's helpful to think about-- yes, this is where you want to start thinking about what's your workload type? Hey, if it's analytical, we've got lots of high cardinality, large datasets where you're doing these vertical column, the group buy-in and summarization and joins, cool, okay, this is the thing we want to be thinking about. A lot of times if you weren't using something like DuckDB, you would be looking at a large, distributed cloud situation. Whether it's BigQuery, Snowflake, Redshift, or perhaps you're using a bit more of, something like Spark, if it's a bit more of that ETL data crunching jobs to be done.
There are also really low latency analytical engines like Clickhouse and Pino and Druid, which were some of the ones a bit newer to me. I think the observation there is that, "Hey, a data warehouse is a bit slower. You wouldn't want to plug your dashboard directly into the curated metrics in a data warehouse. You'd want to put it into these more low latency analytical engines. In some ways, yes, you're right. We had options for these things before. I guess it's about the nuance. At this scale, it's like, well, the observation is if your data is not absolutely humongous.
If you're not talking about petabyte scale, maybe we don't need these massive, large, complicated systems that take time to configure, install, run and tune and are expensive. I think one of the observations is that a lot of these workloads, there's big-ish data, but it's not as big as maybe you need for these big systems. When you think about what DuckDB, it sort of, in a way redefines what big data is, big data isn't so big anymore because you can actually get quite large, several terabyte, data crunching operations on your local machine, on a laptop, or maybe it's on a virtual machine in the cloud and you can scale that.
It allows you to kick that can down the road before you need to start thinking about those bigger options is one thing. Then of course, as we're mentioning, there's the personal workflows and the ergonomics and things. That does feel like a bit of a game, perhaps in some ways from the data scientist perspective, maybe that is a bit more game changing in that we just didn't really have a tool like that, sort of a nice database management approach to analytical data when we compare it to what we would have been using.
Before it was Pandas, Dataframe processing, or DataFrames in R. Polars is the other, Python one, as well as Pandas. These are really cool tools. Polars is doing awesome things for processing speeds, but it's just a data frame tool. It doesn't give you these data management solutions. Organization and transactional consistency. There's definitely a bit of a step change in capabilities that data scientists have there.
**Simon:** Yes. It's a super good question, Ken, and just adding on to what Ned was saying, all of these problems were solvable. DuckDB is not solving an insolvable problem. I think one of the things that I've really appreciated is you're not learning anything particularly new, and this is building on extensible frameworks that already exist. A lot of data out there can be classified as data that really can fit within memory, really can be processed in situ, and you really can talk about processing things locally. Yes, you can solve a lot of these processing things with existing tools or new tools, or you can write a lot of bespoke Pandas or R, and there's some great frameworks out there.
I think one of the things that really sets DuckDB apart is it just embraces a lot of these existing concepts. It exposes everything in both elegant and ergonomic way. At the end of the day, it just makes jobs to be done much easier, and it just cements everything together in a much more straightforward approach. Both data scientists can extend tools that they're already familiar with, and data engineers or data analysts can continue working in quite a familiar way, but get a lot of benefits of the extensible frameworks under the covers.
**Lilly:** One thing that I think stands out to me as you're talking about this, is that this touches a huge number of parts of the lifecycle where you're talking about ingesting and cleaning information that you're pulling in from a lot of different sources and connecting to those sources in the first place.
You're talking about transforming it. You're talking about all of the output as well and the different ways that you can work with it. It feels like it touches all of these different parts of that process. It could be quite difficult to find a way to start using it if it's so broad. When you've approached it and when you've recommended people approach it, how do you recommend people begin? What's a way in for folks who are looking to get started?
**Ned:** I feel like it's a leading question. There is a book we can recommend you to, which is Getting Started with DuckDB. Seriously, I think with all these things, finding a dataset that interests you, whether you're a data scientist or a data engineer, and maybe you have problems at work that's relevant. Find a problem you can sink your teeth into. There's plenty of public open datasets out there. In the same way that if you're picking up a tool, if you're coming up from this analytics perspective, you'd go find a dataset as a data scientist.
I want to get some insights, I need to clean this. You could use DuckDB for that, like going through all of the cleaning preparation. When it comes time to consuming, maybe you do need to do some converting into Pandas or Polars, which is very good integration in both the Python and similarly in the R, and then jump in and start doing your visualization. There would be that. I don't know, Simon, do you have any thoughts around, from a data engineering perspective, what good inroads might be?
**Simon:** Yes, it's a good question. Maybe I'll take a slightly spicier answer here. I think DuckDB pretty much sells itself because it's the things that you're not doing. I don't think anyone should go and learn a technology just because they heard about it or it has a couple of sparks on Twitter or whatever. I think I appreciate DuckDB because it smoothed away a lot of the things I didn't need to use in my day job. I wasn't writing Python code to pulling files from object store. I wasn't having to interrogate a lot of Parquet files. I wasn't writing reams of transformational logic to transform CSV files.
One of the things I really appreciated about DuckDB was essentially that it stopped me from having to learn the nuances of a bunch of different frameworks and tools. I guess one of the approaches I would take for DuckDB is do you have a problem that you're attempting to solve with maybe three or four frameworks that you're familiar with? My challenge would be, can you solve it with one tool instead of three?
Absolutely agree with everything that Ned was talking about. It's great to get familiar with frameworks through examples or buying wonderful books. I think my challenge to listeners is if you're attempting to solve a problem and you think that path ahead needs three or four frameworks, maybe just simplify it down and see whether DuckDB would also get you to that solution faster.
**Ned:** If you're going to throw out a spicy take, I feel like I have to add to that. Definitely, there are opportunities to rationalize and simplify your tool stack where DuckDB can help you do things that different tools might've used. That doesn't necessarily mean that we're saying, "Hey, throw away your other tools." Don't necessarily replace Pandas or even in R, this doesn't replace dPlayer over DataFrames, which is a really nice interface for wrangling data within R. The nice thing is because there's some really great interoperability connectivity with libraries in the analytical data system.
In R, it's a very good chance you like dPlayer, which is a wonderful interface for describing analytical transformations. It turns out that you can plug that into DuckDB, use DuckDB as the backend, which means that I don't think we've said it explicitly, but as a database, DuckDB uses SQL as its primary language. Some people prefer to use dPlayer. You can actually just swap that out and then continue to use the same queries under the hood. There's some interesting stories along the same in Python.
In Python, there's a really great library called Ibis, which is quite like dPlayer in that it allows you to do elegant transformations and querying, but with pluggable composable backends. More recently, which includes DuckDB. Then more recently, there's actually a Spark, interface.
You can write, PySpark queries that would be the same as you'd be targeting a Spark backend, which is a distributed cluster-based processing tool, but using DuckDB as the backend, which opens up some interesting opportunities for having simple, testing out your Spark queries, in continuous integration environments and things like that.
**Lilly:** It'll work within whatever you've got going on, as in, you don't have to swap out everything, you don't have to throw it all away, but it could integrate at different points.
**Ned:** Yes, that's right. There's opportunities to shift some of the things into DuckDB. I'd say use the right tool for what its capabilities are. If you're already using something like Pandas, maybe some of the processing that you're relying on Pandas, bring that into DuckDB because DuckDB with its more lazy operations where data doesn't have to, the transformations doesn't have to be materialized at each step of the pipeline, it actually creates these nice, lazy, representations that can be optimized end to end for the query to bring your transformation operation into DuckDB.
Then turns out that next thing you might want to do is visualization using a data frame from Pandas. That export to Pandas is the last step. Not necessarily replacing things, but working out what the right tool for the right job is, or if, as Simon said, if it turns out actually maybe, yes, you don't need one of those tools, then you have rationalized your tech stack and made things a bit simpler.
**Lilly:** What are you folks excited about coming down the pipeline next for this entire ecosystem? It feels like it's not just DuckDB, it's expanding fairly rapidly. The more people realize the value to be had in managing data effectively, wherever you are with whatever you're doing. I think that the both of you in the work you're doing are seeing a lot of very interesting trends that are coming up. What are you most excited about here and where do you think it's going?
**Simon:** I think there's two things that get me very excited about both DuckDB and the ecosystem more generally. The first one is probably what's possible when you don't actually unencumbered by price. An awful lot of really great processing is now possible, locally exploiting some great technology that you have possibly within arm's reach. We're talking about the power of your laptop, the power of your browser. DuckDB runs pretty much everywhere. It can run in memory. It can run through Wasm in a browser. It really increases the surface area of places where you can do processing and essentially processing for free using existing hardware.
**Ken:** If I'm honest, that scares me a little. We're talking about a very extensible system that can connect to lots of things that can run anywhere and so forth. How do you protect that? How do you secure that? How do you make sure that no one's, I'll put on my Lilly hat here who runs InfoSec for us in Australia and New Zealand. Scary, make me safe, please.
**Simon:** Yes. I think nothing's ever perfect, but I think possibly one of the most battle-tested bits of code working in one of the most hostile environments would be a web browser. The fact that we're talking about WebAssembly as possibly an execution environment for untrusted code with a lot of sandboxing and a lot of compartmentalization. If you wanted to do some rich processing in a hostile environment, I think one of the places that you might want to consider as one of the most battle-tested bits of code would be some of the code paths that are already available and battle-tested within your web browser.
The idea that the memory space is separate, the virtual file system is separate. I do like to think that it's a better place to be rather than building code from scratch that you're building from some of the frameworks that already exist.
**Ned:** I think the other dimension to add to that is maybe the other way to respond to the question you're asking, Ken, is, well, hang on, if anyone can just install it, anyone can do whatever they want. This is almost like the shadow engineering. It's sort of like, well, I've got problems to solve and I can use this tool. I'm going to go and install it. It's true, but that is also true for things like Pandas, which is, it's hard to answer the question how many people use DuckDB for the same reason with Pandas because anyone can pip install and start using it.
I think, what I'd say is, well, this is a tool that is actually going to help people bring cleaner and more organized patterns. You're actually giving them access to a better, depending on the use case, oftentimes a more appropriate tool to help you do things closer to a nicer sort of best practice, cleaner ways.
I think, all of the problems around that governance and what you can and can't do, they still exist. A lot of that does lie in, well, can you access the data? Those governance and data access and lineage things, that's all still there. We must think about how to build that into how we do things. It's still a relevant concern, but I don't know that it necessarily changes the surface area of them.
**Lilly:** You folks have just written this book about getting started with DuckDB. I think it was the first book that was written about DuckDB ever. There are a few more now, which is really great. We've also talked a lot about the way that this can touch different parts of the ecosystem, different parts of the environment. I think, for me listening to it can be a fairly overwhelming thing to contemplate in the whole.
If you were going to point people to a place where they could look to get started, not just with DuckDB, but with also thinking about how to work with their data in a better way, or how to maybe even connect to DuckDB in different parts of their stack, where would you go? What would you recommend that people look at?
**Ned:** There's a few really good online resources. Duckdb.org, the homepage of the project is a great place to go. The documentation is really awesome. In addition to that, there's also a Discord community. That's a great place to go and chat to community members and contributors to the project. Jumping online whether it's on X, previously Twitter, LinkedIn, and, Mastodon, there are people talking about DuckDB. Lots of community things going on. DuckDB project has a regular DuckCon conference. Then maybe, I guess the other part to your question, I don't know, Simon, did you have any thoughts around getting started with analytical endeavors more generally?
**Simon:** Everything that you said, I did actually just wanted to emphasize the wonderful community that has both made core DuckDB very solid. I know I had a problem a while ago where I was trying to process something ridiculous, like a JSON file with over 700 million rows and I hit a small processing error. It was a completely infeasible problem to solve. One of the developers within 24 hours submitted a PR and essentially fixed the processing problem I was having. More generally, I love the community that's spawned around DuckDB.
There's a wonderful and vibrant ecosystem for extensions, everything from geospatial vector processing. There's all sorts of communities that have cross-compiled some very specific frameworks and they've all been expressed and imported as extensions into DuckDB. The way to get sort of both inspired and familiar with that, as Ned said, is either the online documentation, which is fantastic and open source, and the Discord community that have also been very flourishing and growing quickly. I find that really both inspiring and supportive environment to ask questions and get inspired by potential.
**Ned:** There's also the awesome DuckDB GitHub repo, which has an amazing collection of resources. If you're interested in looking and getting insider and analytical data more generally, I think that there's plenty of resources out there, blog posts and books, and it's getting started with data analysis and diving in. I think it's a good question, Lilly , because it can be hard to know how to get started because there's so many different ways to do this. Some books will be using a tool like Pandas if you're a data scientist, some will be using SQL. A lot of these are the same concepts.
I think look for, if you're going to be using SQL with DuckDB, then other resources that involve SQL are relevant. Of course, it's interesting that DuckDB has its own nice ergonomic flavor of SQL, which we didn't mention, but brings a whole lot of niceties to it. I think that, yes, there is a really rich array of resources out there to mine from. Once you get where does DuckDB sit in the landscape, I think you can work out, okay, this is the relevant jumping into analytical resources to dive into.
**Lilly:** Speaking of a rich array of things to dive into, we didn't get into the rich array of Duck-related puns that this affords us, which I'm going to leave as an exercise for the listener. Thank you both for joining us today to come and talk a bit more about this ecosystem, about the tool, about the ways that it can be used in so many different places. Hopefully, we've inspired a few more people to play around with some of these things or to read up more.
**Simon:** Thank you for your time, Lilly, and good talking to you as well, Ken.
**Ned:** Yes, thank you very much, everyone. Thanks a bunch.
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
## Explore a snapshot of today's technology landscape
[ Read Tech Radar ](https://www.thoughtworks.com/radar)
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