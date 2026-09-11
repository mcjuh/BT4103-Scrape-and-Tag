<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/user-journey-testing | Title: Testing the user journey | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Testing the user journey 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Alexey Boas and Ashok Subramanian | Podcast guest  Scott Davis and Zabil Cheriya Maliackal
June 12, 2020 | 36 min 58 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/user-journey-testing#transcript)
Listen on these platforms
## Brief summary
Great web development isn’t just about the front and backends: the experience the user has is critical to success. In this episode, our hosts Alexey Boas and Ashok Subramanian talk to Scott Davis and Zabil Cheriya Maliackal about the principles of user journey testing and the tools such as Gauge and Taiko that can help.
**Podcast transcript**
Alexey:
Hello and welcome to the Thoughtworks Technology podcast. My name is Alexey, I'm the head of technology for Thoughtworks Brazil and I will be one of your hosts this time together with Ashok who's head of technology for the UK. Hello, Ashok.
Ashok:
Hello, Alexey. Good to be on the call again. Look forward to discussing the topic of the day.
Alexey:
Oh, great. And well, we're delighted to have Scott Davis and Zabil with us today. Hello, Scott. Hello, Zabil.
Scott:
Hello, hello. Thanks for having us this morning.
Zabil:
Hey, Alexey. Hey, Ashok.
Alexey:
And Scott, would you mind introducing yourself, telling us a little bit about your background?
Scott:
Absolutely. I'm a principal engineer and a web architect here at Thoughtworks. I've spent a considerable amount of time doing web development, both on the backend and the front end, but this is a topic that is really especially near and dear to my heart, the user journey and capturing the user experience. I firmly believe that we can apply the same engineering rigor to front end technologies that we historically and traditionally have to the backend. So, as I said, I'm really excited to be talking about user journey testing with Taiko this morning.
Alexey:
Great. And how about you, Zabil?
Zabil:
So I'm a product manager and for the past five years I've been working with a few products. Two of the recent ones being Gauge and Taiko and I've been a developer for most part of my experience. I'm quite passionate about testing and building quality software products that I've been working on is around that.
Alexey:
Okay, thank you. And well, you did mention Gauge and Taiko, so those are two open source projects that were born inside of Thoughtworks. I know we're going to talk a little bit about them during our conversation, but would you mind telling us just a little bit what they are?
Zabil:
Yeah, sure. So both Gauge and Taiko are test automation tools and to keep it short, Gauge is a tool for writing acceptance tests and Taiko is a node-JS library for automating web browsers. So we can put both of them together and use them to test web applications.
Alexey:
Okay, wonderful. Looking forward to understanding better how that would work out. So Scott, you mentioned user journey testing, and I guess that's the main topic for today. So why don't you start there? What is user journey testing?
Scott:
Oh, absolutely. So I think many people are probably familiar with this idea of user acceptance testing and language is powerful and it's important. We definitely want the users to accept the code that we're writing. As software engineers, we're not writing this for ourselves, we're writing this for our users. But I really like user journey testing, this phrase, because it captures perfectly what we're trying to accomplish here. A user journey is something like, "Hey, I have to log into this website, add three items to my shopping cart and checkout." That's my user journey right there in a nutshell.
Scott:
And so what a browser automation tool like Taiko allows us to do is write that user journey, capture it in this really nice high level DSL, or domain specific language. And so if you go to a URL and you click on a login button and you write your username in a field, these are things that we can capture and automate in Taiko. And so this focus on the user journey through your application is very much focusing on the user experience, much like a developer might focus on the developer experience and write unit tests and integration tests to kind of experience the code journey through the application, a user journey test allows us to capture the user's journey through your website, as I said, in this really lovely high level DSL.
Alexey:
Okay, great. Thank you. So you mentioned unit testing and I would expect some listeners to be familiar with the concept of testing pyramids. Is it fair to say that user journey testing is a part of testing that will sit at the very top of the pyramid and connect and integrate with the other types of testing as a testing strategy?
Scott:
So the testing pyramid is something that I'm sure many developers who've read up on unit testing at all have seen. The testing pyramid is very broad at the base and that represents unit tests and then as the pyramid gets narrower and narrower, we go through integration testing and finally at the peak is user acceptance testing. The visual metaphor of this testing pyramid is very powerful and it really does a great job of describing the developer experience. The developer's experience is unit testing. They want to make sure that their code is bug free and their APIs are friendly and things like that. So the testing pyramid does a wonderful job of visualizing the developer experience.
Scott:
What I like thinking of is less of a pyramid and more of a spectrum, one that goes from the DX on one side, the developer experience, to the UX, the user experience, on the other. And by thinking of it as a spectrum, we want to make sure that we are well represented across that spectrum and user journey tests will feel familiar to developers if they're familiar with unit testing. But again, the focus is not on the developer experience and the soundness of code, the bug free nature of code, but it really is focused on the user experience and how they interact with the website rather than how a developer might interact with an API.
Ashok:
Okay. That's really interesting. So the mindset you would say that needs to be applied when you're thinking of tests in this shape or format towards, as you're describing the spectrum, towards the user experience side of the spectrum. Have you seen a difference in mindset that needs to be applied as you think about either writing unit tests versus writing user journey tests.
Zabil:
Yeah. That's a very interesting question and I'll try to answer that in terms of the tools and how we've designed Gauge and Taiko. So while the pyramid, like Scott mentioned, talks about developer experience, the existing automation tools are also heavily developer focused, where there is this kind of the concept of a gray box testing, where we need to know the structure of the application that we want to test. So for example, testing an HTML page means knowing what XPath I need to use to click on a specific element or exactly how that element was built in code. And we came to this point because we were looking at testing from a developer perspective. So flipping that and saying that, okay, we need to take a look at the user journey testing perspective will also influence the design of the tools and how they are used according to the user. So that's the difference. So how we code and write those tests are totally different.
Ashok:
Do you almost have, like try to address who the intended user audience of the test-
Zabil:
Yes.
Ashok:
Focus it from their perspective and then use that to drive the design of the tools that you have spoken about.
Zabil:
Exactly. So it's a very clear separation. So it's not very associated with the test pyramid, but, like Scott mentioned, it's like a spectrum. It's a very different universe altogether.
Scott:
I think another interesting angle on this. Part of the reason why the test pyramid came to a pointy tip around user journey testing or user acceptance testing is that historically these tools have been amazing in what they were able to accomplish, but they did tend to be fragile, they did tend to be brittle. Many of them were written in a time when we didn't have evergreen browsers that were constantly upgrading. So if you have a third party tool that's trying to wrap a browser that doesn't update out from under you, you can have some stability. But in this era of evergreen browsers that are constantly upgrading, having third party tools try to wrap and encapsulate them did lead to brutal tests and that was frustrating. That frustrated me as a web architect, having these tests that fail, not because our code has changed, but because the underlying assumptions like the browser has changed. That was one of the top considerations when Taiko was being written, was to address this fragility.
Scott:
And they accomplished it in kind of a very simple, obvious way. If the browser is ever changing, well then not ship Taiko with the browser that doesn't change. So in fact, Taiko ships with Chromium, which is the core of not only the Google Chrome web browser, but also the core of the Opera browser and now even Microsoft Edge. So when you NPM install Taiko, what you end up with is a known good browser that works with Taiko that represents well over two thirds of the market. Now we can point Taiko at other browsers as well, but having this known good stable browser that ships with Taiko really helps address one of the primary reasons why user acceptance testing was kind of worried about and kind of put off to the last, because why put a lot of effort into tests that are going to break for reasons beyond your control?
Scott:
So even just the nature of the tools we use as developers can change our relationship with these tests. Taiko and Gauge are quite fast and quite stable. And the high level DSL makes it very easy to represent the user journey. So when you put all of these things together, it should make user journey testing appealing to the developer as well.
Alexey:
Yeah, I was going to ask, so it's interesting because you talk about how the technology has evolved and has enabled brand new things for us to do. On one hand it does sound like the promise of behavior-driven development coming true, because now technology enables that. Is that true to an extent? Because the concepts, they seem to be related. So BDD was trying to approach testing and the interaction with the system from a user's perspective, using the language of the user and things like that. So now it looks like the technology has enabled us to take this to the next level and remove some of the brittleness and the flakiness of the tests and et cetera. Is that what's happening here?
Zabil:
Maybe, maybe not. So the thing about BDD is, and this is from the people who created BDD and the blogs they have written, they always make it a point to say that it's not about testing. So BDD is about capturing business behavior, the requirements, and managing the requirements and communication within the team. And they consider BDD to be a communication tool, not a testing tool. But Gauge and Taiko take a different perspective. It, again, puts the user into the forefront. And it is focused on testing. And it so happened that specifications are written using markdown because It's plain English (or any spoken language), it's much easier to write tests that way. So although there is no relation to the BDD process, there is, let's say, a kind of an evolution of parts of BDD, but heavily focused on testing.
Scott:
Yeah, I think that idea of evolution is really important to focus on in these kinds of conversations. Thoughtworks has a long history in this space. BDD was kind of coined and popularized by a Thoughtworker named Dan North back in 2003. And so over the course of almost two decades now we've seen this idea expand and involve, as you would hope, but knowing that applications like JBehave and later RBehave, JBehave was implemented in Java, Rbehave implemented in Ruby, and then RSpec. and then Cucumber and Gherkin. All of these are open source projects that came out of Thoughtworks and came out of the result of Thoughtworkers working on projects with clients and wanting to have tools that better represented what they were trying to test. Similarly, Jason Huggins was a Thoughtworker who developed a tool named Selenium back in 2004. And Selenium evolved to include WebDriver, written by another Thoughtworker, Simon Stewart.
Scott:
And so all of these represent 20 years, almost nearly 20 years of industry experience trying to run and evoke tests that take the user's perspective into mind. So even though I affectionately say Gauge and Taiko are BDD Selenium plus plus, I mean that affectionately. Because they aren't an extension of those. What I mean is they're an extension of our experience as an organization trying to write user focused tests. And so when Selenium was faced with the flakiness of evergreen browsers, no blame on Selenium at all, just the nature as the technology evolves, Taiko has evolved to address that. And as Zabil mentioned, Cucumber is great, but it is almost like writing haiku. There's a very formalized structure of this "given when, then" kind of mentality. And while I love the intellectual rigor of "given when, then," no users think that way.
Scott:
Maybe business analysts do, right? Maybe product owners do, but no user is going to say, "Given I have a credit card in my hand and I need groceries in my house, when I drive to the ..." That just doesn't happen that way. And so what Gauge has managed to tap into is this use of markdown, plain English, being able to express the tests in the language of the user. And then Taiko as a browser automation DSL being able to represent the actions of the user. These two technologies, even though they can be used separately, when you use them together, expressing the tests and the language of the user and then being able to automate and represent the actions of the user, make a really compelling combination of two different technologies that work incredibly well together.
Ashok:
I know you were mentioning the reference through Gauge and Taiko a little bit. You mentioned in Gauge you use the tool to express the user journey in an easy to understand language. You also made a reference that Taiko's actually something that could be run by itself, or it can be adopted separately. What's the relationship and the value that we see, if someone's actually going to adopt these, to start thinking about this mindset of moving towards user journey testing? Is there a bump? Do you think about using one over the other to start with? Or do you say you use both together? What's your vote or recommendation for people thinking about adopting or moving down the path of user journey testing?
Scott:
So one of the powers of Gauge is that we're expressing these tests in the language of the user, again, in markdown, in plain English. But Gauge is not opinionated as to how you actually execute these tests. Gauge has first-class support for Java as a back end, or Ruby, or C-sharp, or Python, or in fact JavaScript in the form of Taiko. So the power of Gauge is that we can capture these user journey tests in plain English, in markdown, and implement them in the language of your choice. Now, Taiko is very tightly tied to JavaScript. It actually is a Node.js project and it uses the Chrome dev tools protocol, the CDP, the same low-level protocol that the actual Chrome dev tools use in Lighthouse and things like that. So whereas Gauge is more focused on capturing the language of the user and implementing it in the programming language of your choice, Taiko is very firmly rooted in modern JavaScript idioms.
Scott:
Every action in Taiko is asynchronous. And so these are async functions and you await, await, await each one of these Taiko actions. So another real anti-pattern I see in a lot of these user acceptance user journey testings is, go to URL and sleep for three seconds. And type in a username and password and sleep for another five seconds. And this was a very synchronous, maybe old school first attempt at solving these kinds of problems. But now that we have modern JavaScript that embraces this asynchronous await paradigm, the fact that Taiko embraces this and you do each action and each action takes exactly as long as it needs to take and no longer.
Scott:
And of course we have timeouts and other things to deal with these kinds of things, but as a web developer and a web architect, being able to express this in JavaScript feels very natural to me. That's the natural language that I think a lot of developers are going to gravitate to. So it makes a lot of sense that Taiko was implemented in JavaScript. Also, arguably the most popular programming language on the planet as well, 10 million JavaScript programmers can't be wrong, right?
Zabil:
Yes. And the way to think about how they are different and independent is, Taiko is focused on driving the browser, but testing involves other stuff, like having a runner that will run on your scripts that will report what passed and what failed. So that's where Gauge comes in. Gauge is, after writing the specifications in a specific language, it can run those specifications. Now, Taiko can be used with other runners, like Jest or Mocha. But then the thing that we would miss out here is the topic of this podcast, which is the user journey testing part of it.
Scott:
Absolutely. And I think that's a really important thing to amplify as that thinking of Taiko as a testing library is one particular use case, but not the only use case, it is truly a browser automation tool. So if you need to automate visiting a website, downloading a bunch of images, any of these kinds of things that you might want to do, you can certainly express that in Taiko. But some of the testing aspects of Taiko, being able to intercept network calls, that just lends itself so perfectly to testing. And here's a great example of that. Let's say that you've got your website out there and you've got Google Analytics wired up, and you want to run a series of user journey tests against your production website, but you don't want your Google analytics kind of gummed up with these kinds of testing artifacts.
Scott:
So Taiko gives you the ability to intercept literally any HTTP call that you make. And in the case of Google Analytics, since this is run client side, you might want to intercept that call to the Google Analytics and just kind of dove null it. Just kind of push it aside and not doing anything interesting with it. But if intercept did only that I'd still be interested, it'd be worth the price of admission, but wait, there's more, you could also intercept and supply your own particular payload. So this all of a sudden becomes a very powerful mocking and stubbing tool as well. And then it's got even kind of the best of both worlds, where it can intercept that request, grab the payload that came from the actual website and just tweak it and in a very simple way, tweak that payload and then pay it on.
Scott:
So again, in terms of browser automation, there are broad, broad uses, but boy, the use cases for testing and mocking and stubbing make it an especially compelling tool. But when we say it's a testing tool, Taiko doesn't come with its own assertion libraries at all. So it really is meant to be incorporated with your testing library of choice. It really is meant to be incorporated with Jest or with Mocha or with any of these other kinds of libraries. It's meant to automate the browser in a testing scenario, not just test the browser in and of itself.
Alexey:
Well, that's certainly impressive, the capability of intercepting. So that goes back to what we were talking about, the flakiness and fragility of these user journey testing, and then I have seen situations in which I know small changes to the application would break a large number of tests and then require a lot of work. So could you give me one example of how Taiko provides the sort of resilience to the tests? I don't know, one thing that comes to mind is I have lately had lots of problems using selectors to find elements in a page and that changes all the time. So for example, how does the title DSL deal with those things and provide resilience to the test?
Zabil:
So like you mentioned selectors, that's a big thing. And some history around how Taiko came about is while we were building Gauge, we were trying to solve problems that users face when they were testing and flaky tests were the biggest problem that people noted. And there were two top reasons why tests fail. One was changing selectors, and I'll talk more about changing selectors. And the other one was wait times, people not knowing what time to wait for a particular element to appear on the page, or when people click something, there's an Ajax call and then something happens. These are the two biggest problems that were there. Now, when we looked at selectors, changing selectors was the biggest problem. And that is because the current tools use XPath selectors, which needs to know about the structure of the page.
Zabil:
And that's where we figured out that a change in functionality does not mean a change in the structure of the page. A button can remain a button with two different code styles. But that doesn't mean that the functionalities change which means your tests shouldn't fail either. So that can only happen if we actually go back to the roots of testing, treating the browser as a black box and not knowing how that box is built and the tests being written that way.
Scott:
So Taiko Selectors does not use XPath. It has an option for using XPath in some extreme cases, but the selectors over there are something we call Smart Selectors, which depends on the visual elements of the page. For example, if there's a button over there with a label add to shopping cart, you can just say click add to shopping cart without even saying that it's a button, it's just going to click something on the screen with add to shopping cart. And that holds true for other elements. So that in itself removes a lot of flakiness, because most of the projects when tests are plugged in earlier on in the development cycle, the application constantly evolves and things change, the pay structure changes.
Zabil:
Now, developers need not worry about that to go back and update the tests because of some page change. The other thing that we have is something called Proximity Selectors, where we can say, click a button near a specific text, and Taiko can automatically figure that out. So with this approach, treating the browser like a black box and having APIs to do that, it solves the first problem around selectors. And that is, let's say a major part of flakiness.
Zabil:
The other problem it solves is because Taiko uses or interacts directly with the browser or uses Chrome dev tools protocol, it knows how a browser page loads or how elements are loading in the browser page. So it just automatically, or intelligently figures out that the page is loading and elements are not loaded yet. Let's wait for the page to finish loading before clicking something. So that eliminates a lot of waits in the code, because I think already how people use waits is based on guesswork and you can never predict how much to wait for the page. And then the test ends up all becoming about tweaking the wait times, increasing your testing, and a lot of flakiness around this thing. So again, Taiko eliminates that by intelligently waiting.
Alexey:
Plus you have to be pessimistic, right? And that makes your test take much, much longer to run.
Zabil:
Exactly.
Scott:
Every page will take 20 seconds to load.
Ashok:
I do remember this where the natural instinct, once you start seeing the sort of behavior of a test failure that isn't necessarily indicative of change in anything like the journey. It starts promoting this thing that can just read on the best part and slowly, over time, you start losing confidence in anything . That could be seen as being very powerful for the future.
Zabil:
Yeah, exactly. I think long before, when we were building our products out, a colleague of mine actually came up with the term, I think it's very popular, “there's no such thing as flaky tests”. There are tests that break and we just ignore them and call them flaky. But those are actually unreliable tests.
Scott:
Well, and I think it goes back to something I said earlier about how we can apply the same engineering rigor to the front end that we have historically applied to backend development. When Zabil is talking about this selector logic, not only does it capture the user experience, the user is going to say, "I want to click on the search field." Not, "I want to click on the ID of this or this deeply nested kind of XPath selector logic." So not only does Taiko allow us to kind of get in the mind of the user that says, "Click on the search field, write this in it, click submit." These kinds of user experience kind of things. 
Scott:
It also allows us to address something that came out of very sound engineering principles, but simply aren't needed anymore. And that's the page object. The page object was a great pattern at the time. If you were doing your writing in say Java, and this webpage that's written by someone else is constantly changing, they're changing CSS classes, they're changing IDs, they're changing all these things and inadvertently breaking your tests, well, what you did is you wrote your own adapter pattern. You wrote your own page object and you said, "I'm going to program to the page object. I'm going to say, 'click the select field, write this in, click the submit button'," and then it gets wired up to whatever the code is behind the scenes. That was almost a firewall, a protection between you, the non-fronted developer and this kind of scary, unknown front end that seems to be changing in arbitrary and capricious ways.
Scott:
The selectors just completely deprecates the need for a page object altogether. It's actually kind of an anti-pattern now. When you're using these tools, we want to select. And so if I say, "click search" and there's something obviously on the page that's labeled search, well, it's just going to be clicked. But if you need more, there are these really wonderful fuzzy selectors like near. You could say, "Click search near the search button," or, "Click purchase near the invoice," or these kinds of things. And you can do above and below and to the left of, and to the right of, and so it really is about kind of more naturally interacting with the Dom and the way you'd be expecting rather than adding yet another layer of indirection.
Scott:
But another thing that I want to come back to once again, these sound engineering principles. When we come to unit tests, these unit tests are meant to be run in isolation. We want to isolate ourselves from file systems. We want to isolate ourselves from database calls and network calls and things like that, again, to add stability to these unit tests. Much of the flakiness that we've talked about, isn't a flakiness in the test. It's a flakiness on the network connection or the database connection or the file system not being in the state it needs to be in or anything else.
Scott:
What Taiko allows us to do is remove a lot of those sources of flakiness, a lot of those sources of instability. In Taiko, you can set your GPS location so you don't have to physically be in Bangalore in order to test this app as if you were in India. You can set that location and then run your Taiko tests. You can set cookies so you can be in a logged in state, or you can be in whatever state you need to be in. You can emulate individual devices, you can emulate an iPhone or a Galaxy, or these kinds of things. You can emulate networks to emulate a slow 2G network or a fast 4G network or things like that.
Scott:
By applying the same engineering rigor that we've historically applied to the backend, to the fronted, we can do these same kinds of things. We can put Taiko in a known good state every time. Known good state in that it ships with a known good browser, but also a known good state in terms of location and screen geometry and network conditions and through the intercept we talked about. We could completely isolate our tests and only be dealing with mock stubbed responses. And that feels like unit testing to me, but this is frontend user journey testing, but I'm using all the same skills that I have as a backend developer to test my frontend.
Ashok:
Well, I think what you describe Scott, about the capabilities that are now available, this opens up a whole world of richness in terms of my imagination. You don't need to be limited by imagination or what you can do with functional testing while continuing to retain all the power that you have, oftentimes that you describe there. That people will do with you in a test run. That's bringing that same engineering curve as you've been describing. I think that's fascinating. And seeing that applied, improving the design of the tool itself, I'm sure that users of Gauge and Taiko there's definitely a lot of power waiting to be unleashed. Fascinating.
Alexey:
And just to make sure, again, Zabil, open source projects, anyone can look at how it was done and contribute to that back and then of course use that.
Scott:
Yes. And both are long past 1.0 as well. Again, Thoughtworks has a 20 year history of this. And so these tools are really thoughtful tools and they are advanced tools, but they're based on our 20 years of experience and the pain that you all have been feeling about testing at the tip of that pyramid is pain that we felt as well. And we've lived in. Being able to actively address that, there's something to be said for eating your own dog food. And certainly these are tools that we use internally on our projects. These are tools that we use with our clients and based on our experience, anytime we find a particular pattern or technique, that's popular, what we try to do, popular and successful. What we try to do is encapsulate that in software and then open source it. And that's just the nature of iterative software development. But when you look at iterative development over the course of decades, you really do end up getting a richness and sophistication that sometimes it's just missing from newer tools.
Alexey:
Yeah, that's great. Maybe we should have a conversation on that longer journey and how we got there. All right, so I guess this takes us to the end of the episode. Zabil and Scott, it was a great conversation. Amazing to have you with us. Thank you very much for joining.
Scott:
Thank you so much. It was a treat.
Zabil:
Thanks Alexey.
Alexey:
Thank you. And on the next episode, Rebecca Parsons and I will be joined by Ken Mugrabe, Arvind, and Scott Davis to talk about realizing the full potential of continuous delivery. Please join us for that conversation. And if you have any feedback for us, don't hesitate to reach out or to leave a rating or comments on your preferred platform. Thank you so much for listening. Bye.
[ View full transcript ](javascript:void\(0\))
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
## Check out the latest edition of the Technology Radar
[ Explore now ](https://www.thoughtworks.com/radar)
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