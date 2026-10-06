<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/xr-in-practice-engineering-challenges-extending-reality | Title: XR in practice: the engineering challenges of extending reality | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  XR in practice: the engineering challenges of extending reality 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Scott Shaw and Birgitta Boeckeler | Podcast guest  Cam Jackson and Kuldeep Singh
September 08, 2022 | 39 min 01 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/xr-in-practice-engineering-challenges-extending-reality#Transcript)
Listen on these platforms
## Brief summary
Extended Reality technology — XR — has had a lot of hype in recent years thanks to the concept of the metaverse. But bold visions of the future can obscure the reality of what engineers and organizations are doing today. 
In this episode of the Technology Podcast, Scott Shaw and Birgitta Boeckeler are joined by Cam Jackson and Kuldeep Singh to discuss the XR work Thoughtworks has been doing with clients. Together they explore what it means for engineers and how the future of the technology might evolve.
## Transcript
[music]
**Scott Shaw:** Hello everybody and welcome to the Thoughtworks technology podcast. My name is Scott Shaw and I'll be your host along with Birgitta Boeckeler. We have with us today Cam Jackson and Kuldeep Singh who will be discussing the topic of XR and hopefully we'll find out a little about what that actually means in a minute. Brigita, would you like to introduce yourself?
**Birgitta Boeckeler:** Hi everybody, my name is Birgitta. I'm the second host for this podcast episode today, and I'm a technical principal based out of the Thoughtworks Berlin Office in Germany.
**Scott:** Cam, how about introducing yourself?
**Cam Jackson:** Hi everyone, my name's Cam Jackson. I'm a Lead Developer with Thoughtworks in our Melbourne Office. I've been spending some time looking into XR for Thoughtworks, figuring out where the industry is at, and what it means for us and what it means for our clients.
**Scott:** Kuldeep?
**Kuldeep Singh:** Yes, so my name is Kuldeep Singh, and I am leading some of the XR initiatives at Thoughtworks India and a couple of XR projects we have experienced with and we have been sharing the learning around it and this is a time we should share with a wider audience.
**Scott:** Maybe we could start out with some definitions. I thought X in the XR was a variable, but that's my math background, I guess, but I've heard it referred to differently. Cam, can you give us a little tutorial on what XR means?
**Cam:** It definitely can be a bit of a placeholder, XR just being — The R is definitely reality. XR can be something reality. It can also be extended reality but it's an umbrella term, which refers to augmented reality, virtual reality and mixed reality. Maybe some other new ones might come up as well, but those are generally the three that we think of.
**Scott:** I think we have to get this out of the way whenever this topic comes up, are we going to be talking about the metaverse at all?
**Cam:** I think we have to talk about it at least a little bit today. It would be an omission if we didn't at least mention the metaverse. It might not be the main focus of the discussion. It's obviously become a pretty big topic over the last, however long it's been since Facebook decided to rebrand themselves as a metaverse company.
**Scott:** It does seem to me like there's a lot to talk about even without the metaverse, so maybe we'll just focus on the XR aspects of the problem for now. Perhaps we ought to talk about the different types of XR and the different ways it can present itself. Kuldeep, maybe you could give us a rundown on that.
**Kuldeep:** Yes, sure. As Cam talks about this XR gets hype when this meta word gets together and the center of the metaverse is still XR because we are talking about changing the reality, extending the reality, which XR word more being used. When we talk about types of reality — for example, augmenting the reality — you overlay digital content on top of the real world environment. That's the augmented reality AR stands for. VR is when you don't see the real world; the whole environment is also computer generated and you overlay content on that computer generated environment and program that digital content — that's what's your reality.
Mixed reality is the term which combines both the worlds together. We have devices that can smartly understand the environment, that can understand the lighting condition, that can understand the depth of the wall in front of you, and you can design a better experience using those devices. That's a mixed reality experience. Then there are a number of other definitions that are coming, like assisted reality where Google glass projected a display just near to your eye; that was assisted reality because it helps your working, it assists you. That is assisted reality’s definition. There are now more of these with this X word, that's why we are putting a lot of X words here and anything which we are changing reality is XR.
**Scott:** Do I need to have a headset? Do I need to have some specialized device to take advantage of it? Cam, you've talked about different modes of programming XR.
**Cam:** It's an interesting one. For virtual reality, yes, you're going to need a headset because as Kuldeep said, we're creating an entirely fictitious environment or taking you to a different place than where you currently are. You will need a headset and they're still quite expensive. There are consumer level ones, the meta devices or the Oculus devices cost around on par with a gaming console. They're within reach for some people.
Augmented reality is a little bit different. There are certainly augmented reality and mixed reality headsets, like the HoloLens and the Magic Leap, for example. Those are very much industry-grade devices that cost several thousand dollars and people aren't going into shops and buying them.
Where augmented reality really becomes in reach for people is mobile phones. There are already a lot of augmented reality applications out there that can run on phones — not every phone, it does need to be a relatively high powered device — but I think that is going to be for 90+ percent of people, their first experience of any XR is going to be on their phone, so it's really interesting seeing people get into the space, get into XR through AR on their phone.
At the same time, though, there probably will be a lot of people whose first real serious use of it will be in the workplace because companies will be the ones who do have the money to be able to afford to invest in purchasing expensive high level hardware as an investment for their business and making their employees more effective or unlocking new ways of working for their employees. Just like we had with the internet and with personal computers, a lot of people's first exposure to using it seriously is probably going to be through the workplace.
**Birgitta:** Then when it comes to phones, is it still mostly augmented reality? Like you hold up your phone and you see with your camera what's around you and it's augmented, or is it also still a thing like there used to be this Google — what was it called? — Google Cardboard or something like that. Like have something on your face and you put your phone into that. Is that still a thing that is also being pursued or...?
**Cam:** Yes, those still exist and a lot of people have tried those. I would say it's a completely different experience. I had played around with the Google Cardboard and I was like, "Oh, this is pretty cool. It's VR with my phone." The first time you put on a proper VR headset, it's mind blowing. It's a really completely different experience. The smartphones, I think, are for doing real useful things. Augmented reality is probably where they're going to be useful for. They'll continue to be useful for it because even once the AR or mixed reality headsets come down in price, it's probably still going to be a niche product for the foreseeable future. Whereas everyone, well, most people have a smartphone.
**Scott:** I know I've used the measuring app on my iPhone and I wonder if it'll come into our lives in subtle ways like that, where it's just a really useful thing to be able to see both the digital world and the physical world and overlay it.
**Birgitta:** Interesting. I hadn't even thought of that as an augmented reality thing.
**Cam:** It's interesting; I think in some ways the sign of a technology really being mature is when not all of its applications are really mind blowing. That's when it really has arrived is when it's just one of really simple things that you can use it for.
**Scott:** Speaking of industrial applications, I think Kuldeep has been working on something like that. Do you want to tell us about your project?
**Kuldeep:** Yes, of course. We are really building an enterprise-ready XR product shoot for one of our customers, Lenovo. We are building their ThinkReality XR Platform. That comes with out of the box solutions — for example, Remote Expert. We are experts sitting remotely and you are wearing the smart glass, which always has a camera at the center. You can share your environment while working with your hands. Your hands are free to work, and you can share your environment with the expert sitting remotely where the expert can guide the person sitting in the field and can guide step-by-step and not just that, there are a lot of other use cases like auditing.
You can build an audit application automatically. Your camera is always there while you are working — it can guide you, it can improve your efficiency and it can give you all the additional information you need. You want to run a video, it'll be available on your voice call; you just say to the device and it will bring that video or bring the PDF document in front of you where you don't need to really open a manual, which is a multipage manual. You don't need to switch the context of your work. These are the use cases which are out of the box on the solution, which we are building.
**Scott:** They're counting on there being an enterprise market. This isn't a consumer device. This is something that all businesses would buy.
**Kuldeep:** Right. This is actually an enterprise XR solution and there is a slight difference between enterprise and consumer, because on the enterprise side, you still have a controlled environment. You can provide the right training, you can provide how the devices are to be managed, what permissions are to be given, all the existing mobile device solutions like MDM solutions. The organization’s policies can apply to these devices, but content needs to be displayed, but not all these things can be maintained well in an enterprise setup. That is the immediate need. That is not a very important factor on the consumer side.
That's where a lot of concern is also in XR; like how all this thing will be maintained — how the content will be maintained. In the controlled environment enterprise side, it is still the same set of standards that we have built in years. Similar standards of software can continue working on the XR side as well. That's where organizations like Lenovo are pitching heavily. Qualcomm is pitching heavily in this area.
**Birgitta:** This example you just described, that's about the person in the field is wearing some smart glasses or — 
**Kuldeep:** Right. The product which we are talking, ThinkReality here, that is a smart glass. Part of it is a smart glass. Then there is a cloud solution which can provide all the provisioning services, what could be needed. Then there is an SDK component, which is for developers to build applications for these devices.
This is a similar setup for any smart or HMD glasses, head mounted glasses, be it Microsoft HoloLens, be it Oculus; every device comes with their own software development kit for developers to build solutions for these devices. There are some common programming environments which can be used by developers to build their solutions. This is how this whole ThinkReality program works. I am part of that project.
**Scott:** That's a lot of specialized hardware for a developer to get started with. Are there ways to get started that are cheaper or easier?
**Kuldeep:** Yes, if you look at these devices, not just this Lenovo device, I have explored around 200 plus devices in XR, around 70% of them are still on Android devices. All of your skills coming from Android development will continue here. All of the development, for example, Unity, the gaming side development gaming — Unity is being used for game development for ages now.
All that experience and skill can continue working here. This is just another Android or similar device. We can build software on top of that. The same knowledge can continue, but of course, there is a lot of other things people need to acquire to build solutions. Because it's an Android, there are simulators available. You can try those things directly in the simulator. If you don't have a device still, you can build applications and once you access the device, you can, of course… 
**Scott:** Can I get started just on the web? Can people just access the web through these devices?
**Cam:** Yes, you can. As someone who spent most of their career doing web development, that's really appealing to me. I've written a lot of JavaScript and a lot of React and it turns out there actually is a way that you can transfer a lot of those skills. There is a thing called WebXR. It's still pretty bleeding edge stuff, but it is out there and you can use it and it's fantastic to be able to get into a whole new space and bring along those transferable skills.
As Kuldeep said, you've still got Unity there, for example, as a really good cross-platform solution. Unity is fantastic, but it is an extremely different programming environment for someone who has mostly done JavaScript or web applications or even Java backends, for example. Even simple things like how do you do source control in Unity? for example; How do you hook it up to your Editor?
There's just a lot of problems that are solved problems in a lot of other programming, which you have to reinvent some solutions to. WebXR is a really good way of being able to get started in the XR world as a developer who hasn't played in that space very much.
**Scott:** If I was just a React developer and I wanted to start working in 3D, is there a migration path for me?
**Cam:** Yes. That's one of the coolest things; there's a project called React to XR, which allows you to build a React application, create React components, just like you normally would.
**Birgitta:** Of course there is a project like that.
**Cam:** Yes, you can do anything with React — I've even seen you can create your infrastructure using React if you really want to. It's become the hammer that people want to use on every single nail, but you can create regular looking React components that function as normal React components do. The only difference is instead of spitting out HTML, they spit out 3D elements.
Instead of a div or an H1, or a table, it's creating a light or a camera or a mesh — and it's a really approachable way to take all the skills that we already have and start doing XR. It's still not that easy, and as Kuldeep said, there will be a lot of extra skills that you will need to pick up along the way, but it's a great way to get started.
**Birgitta:** I can also imagine, okay, I know React, I know JavaScript, but it's probably not that one-on-one transferable. There are probably different challenges to consider and maybe different things to think about when you build these types of applications, right?
**Cam:** Yes, and the biggest one that you'll run into fairly quickly is needing to make updates to things in real time. When you're building a web application or even if you're building an API on the backend, usually your code only ever runs in response to something having happened. A user has clicked on a button or an event has come off a stream or NGTP request has come into an API, like your code is responding to a thing that happened, it runs, it executes, it gives the response and then it finishes and it's done.
As soon as you get into XR, and this is true of game development as well, you're operating in real time. You've got code that needs to run continuously. It needs to be able to run 60 times every single second in order for the experience to be good enough for the user. It sounds like a small thing, but it's a really significant shift going from my code just runs and then it finishes to my code is running constantly over and over and over again, many times per second. You'll run into that fairly quickly as soon as you start trying to create an interactive 3D or immersive app and it definitely takes a different mode of thinking to be able to operate in that way.
**Birgitta:** JavaScript and the browser don't immediately make me think suitable for real time, right?
**Cam:** It's not known as a high performance environment, and that's, I guess, where you have to make some of the trade-offs depending on what you are building — single threaded operating in a sandbox JavaScript may well be fast enough for what you're trying to do, and there are real advantages to building on the web. You don't have to deal with an in-store barrier. You don't have to deal with getting your code into an app store. You can push updates out many times per day, constantly, and your users always get the latest version.
The web is fantastic for that, but JavaScript is not known for super high performance. You still get the power of WebGL. All of the rendering can still be hardware accelerated, but if you're doing something more complicated, you may find that the web is just not fast enough. That's where you get into more native solutions that give you a bit more power, a bit more control over the underlying hardware. Then you have to think about all those other problems, app stores, installation processes as well. There's definitely a trade-off between the two.
**Scott:** On the Lenovo project, you must have had to address continuous delivery issues like how do you deploy to a device like that?
**Kuldeep:** Very interesting. We had a lot of challenges when you really build a solution, and especially in pandemic, we started this project almost at the peak of pandemic and everyone was not having those devices, even how to test this whole thing. Forget about the continuous delivery. How to test our regular XP practices, how can we do test-driven development when people can't see other people's what they are seeing.
The first product we need to actually introduce in the product is how we can share the mixed reality experience on a browser. That person who is not wearing the device, that person can also see what is happening in the device. That helped us a lot in our development and not just development, of course — sales demonstration and everywhere the product is helping. That gives us how the whole product can be developed. That helped us or in test driven development.
Then it was about automation testing in XR or Unity development. It was not very well defined how to do it, as Cam said, it's not the JavaScript development, which is very standard for years now. Here we need to devise new ways of automation, how a gaze click can be automated, how a sensor input can be automated, how the gyroscope inputs can be automated. All these things we need to think through and simulate in our environment. For that — [crosstalk]
**Birgitta:** Sorry. Just a quick understanding. A gaze click would be: I look at something and then something happens in the glasses, yes?
**Kuldeep:** Right. It's like a laser beam coming from your head, but you don't see the laser beam — it's like that. That is clicking all the virtual elements. To simulate this, we actually introduced, in fact, developed Arium platform which we open-sourced also. That's an automation testing platform for Unity applications and it's a general platform. We open-sourced it.
We have been using this heavily in other projects also to simulate all the mobile interactions, all the device-based interactions and plugin can be written on that platform. It's an extendable just like Selenium and other open-source products do. This helped us to do automation testing and once the product is out, then it can follow the standard mobile development based practices, because eventually this is a mobile device which runs on certain Android devices and software can be posted the same way as any mobile app can be posted.
**Scott:** I suppose it's a lot easier on the web. Is that right, Cam? You probably had a breeze testing. I know Cam just also delivered some work, 3D bathroom planner and experimented with putting that on a VR headset. Was testing easier there?
**Cam:** It's definitely easier. At a high level, you can bring a lot of the same tools, especially because we were using React-based tools using React Three Fiber for that. You can still use the React testing library for a lot of it. You can use Jest as a testing framework on a lot of the same tools that we usually use. You definitely still run into lots of unknown problems. As Kuldeep said, you've still got the… what does TDD mean for something which is moving in a 3D space and how do you simulate basic things like clicks? I'd say it's probably easier in a web-based environment than with Unity because it's closer to the tools that we usually use, but there's definitely still unsolved problems there.
**Scott:** Suppose I was a developer and I wanted to get started doing this, what skills should I learn? Do I have to learn Unity or what's the basics?
**Cam:** I think it depends on what you already know. My advice to people when they want to get into something is often, find something which is at least a little bit familiar so you're not starting from scratch. If you're a web developer, I would say you can get started pretty easily with WebXR. If you've played around with game development before, I know a lot of developers think it would be cool to make a game one day and they download Unity and have a play with it. If you're already familiar with Unity, then that's probably a great way to get started with XR as well.
I would say the best way to start learning it is to just start making stuff. Go ahead and start playing around with it. You'll definitely find pretty quickly there are extra skills that you might not necessarily have. You're probably going to need to start brushing up on your maths skills, learning some linear algebra, auto matrix, autovector, how do I transform something in 3D space? A lot of problems that most developers, unless you're in games, don't have to deal with on a daily basis. It can be tricky stuff, but there's a lot of great tutorials out there and it can be really fun to pick up once you get the hang of it.
**Scott:** Do the frameworks shield you from some of that? I would have thought that would have been worked out already?
**Cam:** The frameworks shield you from having to implement the maths yourself. All of the functions are there. There's great libraries and APIs for multiplying two matrices together. The hard part is still knowing which function to call. There are a lot of different operations you can do on a matrix, there are a lot of different ways you can combine two vectors together. Knowing which one to call is probably the hardest part. Once you know what operation you're trying to do, yes, the libraries have solved a lot of the lower level maths for you.
**Kuldeep:** To be a true XR developer or a gaming developer also, I would say you need to be an artist, you need to be a scientist, you need to know maths, you need to know geography, you need to know physics, the complete and you need to be a movie director who can work on scene actions. This is how any XR project is defined. It is not defined in terms of screens, like traditional 2D development is defined, this screen and on clicking on a certain button, another screen comes…
Here it is all about scenes just like movie making. You define a scene, you define actors, you define what will happen after that, who will do what dialogue and what action will happen, same way the XR project is defined.
Eventually, the person who is driving needs to know all these things. Yes, the tools will help us. For example, any gaming engine, if we rely on that, can solve a lot of things from maths, a lot of things from physics, gravity and all those calculations, at least everything will come in the gaming engine and that can be the backing of any application which we are building. Yes, tools can help, but of course you need to gain gradually on those skills where you can get better at this.
**Cam:** I think it's a great point. It really speaks to not just the new skills that developers will need, but the new capabilities that organizations are going to need. If you're a company who's really getting into this stuff seriously, there might be new roles and new capabilities that you didn't have before in your organization that you're going to need to bring in. A lot of companies, they might not have used to afforded themselves as a technology company and they realize how important technology is to them. They need to hire a lot of developers.
If you're now getting into XR, do you need to hire directors and artists and producers and storytellers and all these extra roles that you didn't use to have in order to take advantage of the technology to its fullest?
**Scott:** It seems like it's almost like an architecture problem, as opposed to design like visual design. You're designing spaces, aren't you? It's the whole thing of moving around and what's an ergonomic way to do that. I'm not sure we know how to do that yet.
**Cam:** Yes, it's very multidisciplinary, and you're right. There is a lot that we can probably learn from architecture and interior design in terms of designing spaces.
**Kuldeep:** We are talking about extending reality. We are talking about changing the belief. Now the biggest challenge we have faced in — of course we learned with time that in XR, when we talk about design, the product design, if people do not believe in the product you have designed, if the virtual content which we are showing a person cannot believe it is a real product, then it's not a great immersive experience people will want to. This is all about changing the belief. Changing beliefs is not easy. It's lot of things you need to do when the design comes in.
For example, if I'm throwing a metal ball virtually, now wherever the ball touches the floor, the sound needs to be exactly like a metal ball. If the sound is not coming at that moment and that sound is also, if it is afar, the sound should be a special sound. If that is not coming in that proportion, I would not believe that a virtual ball is a real ball I'm throwing. If I am not believing, I'll not use that experience. That's how these designs and the different skills are really important.
**Birgitta:** It also sounds like yet another one of those things where like, let's say, us in this call, we're like, let's say application developers, web application developers, whatever. We're now moving into yet another like different area like you're starting with Ops, right, and then it turned into this whole DevOps movement and then it's happening right now with things like data mesh where we are always like the elephant in the China shop going into the data space saying oh, why don't you automate these things and how do you test this? Now it's like this area as well, where there are actually lots of experts who can do 3D modeling and all of those things and now we are coming in and discovering all these things and talking about testing.
I always find that fascinating how as application developers seem to move through all of these areas and try to see how we can make them better, but also often approach them naively as if nobody has done this before, but actually people have been doing 3D modeling and stuff like that and perfecting it for years, right?
**Cam:** Absolutely. I've spoken to a few game developers in part of my investigation. One of the things that they say is you can tell really quickly just from little basic language things about whether someone is coming to XR from a web application or a "corporate environment" or whether they're coming to it as a web developer. It's a place where I think we're going to be meeting in the middle for a lot of — two industries, game development and then all other development that seem to not really overlap that much, I think they're about to be thrown together in new ways that they haven't before and there's probably going to be some culture clash.
Like you said, Birgitta, we've seen it before with DevOps and with all of the other spaces that developers have a habit of infiltrating and acting like they just invented it. It's going to be interesting to see how we learn from each other.
**Scott:** This seems like it’s something that's been talked about for years because I'm old; I remember when Jaron Lanier first started talking about virtual reality. What is it that's stopping it from more general adoption?
**Cam:** I'm not as old as you, Scott, but even I remember in the '90s going to a little Nintendo exhibit in a shopping center and I think the Super Nintendo was about to come out. The guy at the store was talking about how VR is going to be the next thing — the next Nintendo console is going to have VR. Here we are 25 years later and it's still a fledgling thing which has barely been invented. I think it has come along a lot more slowly than people might have expected or wanted it to. I think it's just a really hard problem. In fact, it's not one, it's lots and lots of really hard problems.
If you look at the marketing material from Meta when they launched their big Metaverse pitch, even they were really open about the fact that to create the Metaverse that they envision, they'll need huge breakthrough innovations in at least 10 different technology areas. You're talking about graphics, you're talking about computer vision, you're talking about all these really advanced computing areas that need a hell of a lot of research to get them to a point where this stuff is more usable. It's taken a long time I think just because they're really hard problems.
I do think we've seen big advances in the last few years like having the Oculus devices come down in price to the point where a lot more people can afford one, looking at the new things that get added into the iOS and the Android SDKs for their AR abilities. I think the pace of invention is really picking up, which is probably just a function of the amount of money that's being invested in it. It's coming along slowly, but I think we're at a pretty exciting point where things are really starting to pick up.
**Scott:** You think the hype is becoming reality?
**Cam:** Well we want it — It's impossible to know and definitely some things the hype might be a bit outpaced. Metaverse is one thing where the hype is at a pretty ridiculous level. None of us has a crystal ball. We can't really know what it's going to be. I think the hype for Metaverse, for example, is probably beyond where it's at today, maybe the Metaverse will be the huge world changing thing that is predicted in 5 years, 10 years.
Right now, the Metaverse doesn't really exist and so a lot of the hype about “you need to be in the Metaverse”, well, there isn't really a Metaverse, you can't really be in it just yet. I think the hype around XR and where XR is going and maybe that leads to the creation of the Metaverse in the future, I think there's a good reason to be pretty excited about it.
**Scott:** I read an article in Wired that about Metaverse is like cyberspace; we're living in cyberspace, but we don't call it cyberspace. Maybe when there is actually a three-dimensional world that we can enter, we're going to call it something different by the time it actually becomes a reality.
**Kuldeep:** If I share a few of the bottlenecks in XR adoption is from the industrial side, the biggest thing that we found is the content. If you look at any industrial setup, content designing, CAD/CAM is a standard 3D content development which has been there for ages. There is a complete separate department which is building content and that content is not usable in the devices which we are talking about today, the head mounted devices where these are not capable to run that high quality content.
We need a lot of transformation from one form to other form of that content that is still not yet mature enough to really make it a real photo-realistic content. You still need a 3D designer to convert that content in a photo realistic fashion. If we are talking about content for a really big product like a car or an airplane, maybe still it makes sense to design 3D content and invest there. If I'm talking about a $1 retail product, it doesn't make sense to build a 3D design for that content, for that product.
There are so many use cases of XR in retail, for example, but if the content process is not automated, it's hard to catch there and that's where, as Cam talked about, there is a lot of innovation happening. For example, you talked about you are able to use an iPhone to scan your room, it can give you the size of your room. That's the innovation we are talking about. Your devices need to automatically scan to fit the content where it should be and automatically, if I need to bring a 3D content, I can scan the content at just a moment of time, it will bring in 3D.
A lot of development is happening, Google, Meta and Facebook earlier, if you look at their recent patents or recent research, all talking about this type of research where single image, a 2D image and converting into a 3D model automatically through a content pipeline. That's where the industry now needs to focus on. Once that problem is solved, there is a huge content available. You can just bring in these devices as tools to visualize, but they're not useful until there is the right content to show.
**Cam:** Interestingly, that's one of the things that we can learn from the game development industry, because it's not true for all games, but for a lot of big AAA games, the bottleneck for them is actually in content creation. These companies employ armies of artists and 3D modelers and texture artists and they also employ a lot of developers to do the transformation of those, to get those into a format where they can actually be useful in an engine. Again, this is a problem that the games development industry has been wrestling with for a while.
**Scott:** Okay. Maybe we'll leave it there. This sounds like there's a lot of opportunities and new job descriptions that are going to get created. Thank you and we'll see you next time.
**[music]**
**[END OF AUDIO]**
[ View full transcript ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
More episodes 
Episode name 
Published 
Series 
Open-weight models: What are they and when should you use them? 
September 03, 2026  Technology podcasts 
AI-generated code: What has to be true for us to trust it without looking at it? 
August 20, 2026  Technology podcasts 
Scaling the enterprise harness: How to achieve AI agent controllability across an organization 
August 06, 2026  Technology podcasts 
Embracing hybrid AI: How Lenovo is leveraging local, on-device AI 
July 23, 2026  Technology podcasts 
What does the future of software engineering look like? 
July 09, 2026  Technology podcasts 
What does code mean in 2026? 
June 25, 2026  Technology podcasts 
Database branching: Overcoming the bottlenecks of shared database environments 
June 11, 2026  Technology podcasts 
What is spec-driven development? 
May 28, 2026  Technology podcasts 
What is harness engineering? 
May 14, 2026  Technology podcasts 
Anthropic Mythos: Hype, reality and the actual security implications 
April 30, 2026  Technology podcasts 
Key themes in Technology Radar Vol.34 
April 15, 2026  Technology podcasts 
How it feels to be a software engineer when AI is changing our relationship with code 
April 02, 2026  Technology podcasts 
Be brilliant at the basics: Inside Looking Glass 2026 
March 19, 2026  Technology podcasts 
Durable computing: What is it and why now? 
March 05, 2026  Technology podcasts 
Inside AI/works™: An agentic development platform 
February 19, 2026  Technology podcasts 
Unlearning, experimentation and engineering rigor in an agentic world 
February 05, 2026  Technology podcasts 
Exploring AI agent platforms 
January 22, 2026  Technology podcasts 
Architecture antipatterns and pitfalls: Good intentions, bad habits and ugly consequences 
January 08, 2026  Technology podcasts 
Are we entering the 'age of intent' in digital interaction? 
December 23, 2025  Technology podcasts 
AI-assisted software development in 2025: Inside this year's DORA report 
December 11, 2025  Technology podcasts 
We still need to talk about vibe coding 
November 27, 2025  Technology podcasts 
How developers can get the most from new AI coding workflows 
November 13, 2025  Technology podcasts 
Themes from Technology Radar Vol.33 
October 30, 2025  Technology podcasts 
What does an AI strategy with humans at the center look like? 
October 16, 2025  Technology podcasts 
What we're talking about when we talk about context engineering 
October 02, 2025  Technology podcasts 
Mean time to shared understanding: Bridging the gap between citizen developers and developers 
September 18, 2025  Technology podcasts 
Organizational design and Team Topologies after AI 
September 04, 2025  Technology podcasts 
Context engineering: Tackling legacy systems with generative AI 
August 21, 2025  Technology podcasts 
Navigating AI opportunities at MYOB 
August 07, 2025  Technology podcasts 
Caring about documentation in the LLM era 
July 24, 2025  Technology podcasts 
Why the tech industry needs Expert Generalists 
July 10, 2025  Technology podcasts 
The three new fallacies of distributed computing 
June 26, 2025  Technology podcasts 
MCP and SRE: Why the future of IT operations is agent-driven 
June 12, 2025  Technology podcasts 
Unpacking Google I/O 2025 
May 29, 2025  Technology podcasts 
Accelerating mainframe modernization using generative AI 
May 15, 2025  Technology podcasts 
Exploring the fundamentals of software engineering 
May 01, 2025  Technology podcasts 
Themes in Technology Radar Vol.32 
April 17, 2025  Technology podcasts 
We need to talk about vibe coding 
April 02, 2025  Technology podcasts 
Infrastructure as code in 2025 
March 20, 2025  Technology podcasts 
How fitness functions can help us govern and measure AI 
March 06, 2025  Technology podcasts 
Architecture as code 
February 19, 2025  Technology podcasts 
Decoding DeepSeek 
February 06, 2025  Technology podcasts 
AI testing, benchmarks and evals 
January 23, 2025  Technology podcasts 
Exploring the intersections of software architecture 
January 09, 2025  Technology podcasts 
Who should make software architecture decisions? 
December 26, 2024  Technology podcasts 
Generative AI's uncanny valley: Problem or opportunity? 
December 12, 2024  Technology podcasts 
Using generative AI for legacy modernization 
November 28, 2024  Technology podcasts 
Data contracts: What are they and why do they matter? 
November 14, 2024  Technology podcasts 
Themes from Technology Radar Vol.31 
October 17, 2024  Technology podcasts 
Build Your Own Radar: Using the Technology Radar as a governance tool 
October 03, 2024  Technology podcasts 
Exploring DuckDB: A relational database built for online analytical processing 
September 19, 2024  Technology podcasts 
Software service granularity: Getting it right 
September 05, 2024  Technology podcasts 
Measuring developer experience 
August 22, 2024  Technology podcasts 
How can AI support designers? 
August 08, 2024  Technology podcasts 
Sensible defaults: A way to think about our technology practices 
July 25, 2024  Technology podcasts 
Tracking technology stacks, practices and experiences across teams 
July 11, 2024  Technology podcasts 
Inside Bahmni: An open-source digital public good 
June 27, 2024  Technology podcasts 
How to assess your organization's security maturity 
June 13, 2024  Technology podcasts 
Continuous delivery vs. continuous deployment: What should be the default? 
May 30, 2024  Technology podcasts 
Themes from Technology Radar Vol.30 
May 16, 2024  Technology podcasts 
Building at the intersection of machine learning and software engineering 
May 02, 2024  Technology podcasts 
Refactoring with AI 
April 18, 2024  Technology podcasts 
How to measure your cloud carbon footprint 
April 04, 2024  Technology podcasts 
Technology through the Looking Glass: Preparing for 2024 and beyond 
March 21, 2024  Technology podcasts 
Diving head first into software architecture 
March 07, 2024  Technology podcasts 
Exploring the building blocks of distributed systems 
February 22, 2024  Technology podcasts 
Software-defined vehicles: The future of the automotive industry? 
February 08, 2024  Technology podcasts 
Beyond the DORA metrics: Measuring engineering excellence 
January 25, 2024  Technology podcasts 
Asynchronous collaboration: Getting it right 
January 11, 2024  Technology podcasts 
Looking back at key themes across technology in 2023 
December 28, 2023  Technology podcasts 
Leveraging generative AI at Bosch 
December 14, 2023  Technology podcasts 
Jugalbandi: Building with AI for social impact 
November 30, 2023  Technology podcasts 
AI-assisted coding: Experiences and perspectives 
November 16, 2023  Technology podcasts 
What's it like to maintain an award-winning open source tool? 
November 02, 2023  Technology podcasts 
Engineering platforms and golden paths: Building better developer experiences 
October 19, 2023  Technology podcasts 
Managing cost efficiency at scale-ups 
October 03, 2023  Technology podcasts 
Exploring SQL and ETL 
September 21, 2023  Technology podcasts 
Driving innovation in radio astronomy 
September 07, 2023  Technology podcasts 
XR with impact: Building experiences that drive business value 
August 24, 2023  Technology podcasts 
Leadership styles in technology teams 
August 10, 2023  Technology podcasts 
Making design matter in technology organizations 
July 27, 2023  Technology podcasts 
Generative AI and the future of knowledge work 
July 13, 2023  Technology podcasts 
Scaling mobile delivery 
June 29, 2023  Technology podcasts 
Making privacy a first-class citizen in data science 
June 15, 2023  Technology podcasts 
Multi-cloud: Exploring the challenges and opportunities 
June 01, 2023  Technology podcasts 
Scaling up at Etsy 
May 18, 2023  Technology podcasts 
TinyML: Bringing machine learning to the edge 
May 04, 2023  Technology podcasts 
The weaponization of complexity 
April 20, 2023  Technology podcasts 
How we put together the Technology Radar 
April 06, 2023  Technology podcasts 
Inside India's Drug Discovery Hackathon 
March 23, 2023  Technology podcasts 
Serverless in 2023 
March 09, 2023  Technology podcasts 
My Thoughtworks journey: Rebecca Parsons 
February 23, 2023  Technology podcasts 
How to tackle friction between product and engineering in scale-ups 
February 09, 2023  Technology podcasts 
6 key technology trends for 2023 
January 26, 2023  Technology podcasts 
Tackling system complexity with domain-driven design 
January 12, 2023  Technology podcasts 
Shifting left on accessibility 
December 29, 2022  Technology podcasts 
Data Mesh revisited 
December 15, 2022  Technology podcasts 
Low-code/no-code platforms: The 10% trap and the limits of abstractions 
December 01, 2022  Technology podcasts 
Welcome to the fediverse: Exploring Mastodon, ActivityPub and beyond [Special] 
November 24, 2022  Technology podcasts 
Rethinking software governance: Reflecting on the second edition of Building Evolutionary Architectures 
November 17, 2022  Technology podcasts 
Reckoning with the force of Conway's Law 
November 03, 2022  Technology podcasts 
Exploring the Basal Cost of software 
October 20, 2022  Technology podcasts 
Why full-stack testing matters 
October 05, 2022  Technology podcasts 
Acknowledging and addressing technical debt in startups and scale-ups 
September 22, 2022  Technology podcasts 
XR in practice: the engineering challenges of extending reality 
September 08, 2022  Technology podcasts 
Agent-based modelling for epidemiology: EpiRust and BharatSim 
August 19, 2022  Technology podcasts 
Mastering architectural metrics 
August 12, 2022  Technology podcasts 
Building a culture of innovation 
July 28, 2022  Technology podcasts 
Starting out with sensible default practices 
July 14, 2022  Technology podcasts 
Better testing through mutations 
June 30, 2022  Technology podcasts 
Patterns of legacy displacement — Part two 
June 16, 2022  Technology podcasts 
Patterns of legacy displacement — Part one 
June 02, 2022  Technology podcasts 
Mitigating cognitive bias when coding 
May 19, 2022  Technology podcasts 
Following an usual career path: from dev to CEO 
May 05, 2022  Technology podcasts 
Software engineering with Dave Farley 
April 21, 2022  Technology podcasts 
Tackling bottlenecks at scale-ups 
April 07, 2022  Technology podcasts 
Coding lessons from the pandemic 
March 24, 2022  Technology podcasts 
Is there ever a good time for a code freeze? 
March 10, 2022  Technology podcasts 
Navigating the perils of multicloud 
February 25, 2022  Technology podcasts 
Compliance as a product 
February 10, 2022  Technology podcasts 
The big five tech trends for 2022 
January 27, 2022  Technology podcasts 
Fluent Python revisited 
January 13, 2022  Technology podcasts 
Creating a developer platform for a networked-enabled organization 
December 30, 2021  Technology podcasts 
The art of Lean inceptions 
December 16, 2021  Technology podcasts 
The hard parts of data architecture 
December 02, 2021  Technology podcasts 
TDD for today 
November 18, 2021  Technology podcasts 
You can't buy integration 
November 04, 2021  Technology podcasts 
The rise of NoSQL 
October 21, 2021  Technology podcasts 
The hard parts of software architecture 
October 07, 2021  Technology podcasts 
Machine learning in the wild 
September 24, 2021  Technology podcasts 
Delivering innovation at scale 
September 09, 2021  Technology podcasts 
Jim Highsmith: a 54-year agile journey 
August 26, 2021  Technology podcasts 
Securing the software supply chain 
August 12, 2021  Technology podcasts 
Making retrospectives effective — and fun 
July 22, 2021  Technology podcasts 
Patterns of distributed systems 
July 08, 2021  Technology podcasts 
Refactoring databases — or evolutionary database design 
June 24, 2021  Technology podcasts 
Making developer effectiveness a reality 
June 10, 2021  Technology podcasts 
Team topologies and effective software delivery 
May 20, 2021  Technology podcasts 
How green is your cloud? 
May 07, 2021  Technology podcasts 
Green software engineering 
April 22, 2021  Technology podcasts 
Twenty years of agile 
April 08, 2021  Technology podcasts 
Talking with tech leads with Pat Kua 
March 25, 2021  Technology podcasts 
My Thoughtworks Journey: Patricia Mandarino 
March 11, 2021  Technology podcasts 
Exploring infrastructure as code 
February 25, 2021  Technology podcasts 
XR in the enterprise 
February 11, 2021  Technology podcasts 
Getting to grips with data visualization 
January 21, 2021  Technology podcasts 
Computational notebooks: the benefits and pitfalls 
January 07, 2021  Technology podcasts 
The architect elevator 
December 24, 2020  Technology podcasts 
The future of Clojure 
December 10, 2020  Technology podcasts 
The future of digital trust 
November 27, 2020  Technology podcasts 
Integration challenges in an ERP-heavy world — Pt 2 
November 12, 2020  Technology podcasts 
Democratizing programming 
October 28, 2020  Technology podcasts 
Integration challenges in an ERP-heavy world 
October 16, 2020  Technology podcasts 
Models of open sourcing software 
October 01, 2020  Technology podcasts 
Applying software engineering practices to data science 
September 17, 2020  Technology podcasts 
Using visualization tools to understand large polyglot code bases 
September 03, 2020  Technology podcasts 
Machine learning in astrophysics 
August 20, 2020  Technology podcasts 
Programming languages geek out 
August 06, 2020  Technology podcasts 
Observability does not equal monitoring 
July 23, 2020  Technology podcasts 
Working with 50% of code in the browser 
July 09, 2020  Technology podcasts 
Realising the full potential of CD 
June 25, 2020  Technology podcasts 
Testing the user journey 
June 12, 2020  Technology podcasts 
Continuous delivery in the wild 
June 01, 2020  Technology podcasts 
Lessons from a remote Tech Radar 
May 13, 2020  Technology podcasts 
The future of Python 
April 30, 2020  Technology podcasts 
A sensible approach to multi-cloud 
April 17, 2020  Technology podcasts 
Digital transformation: a tech perspective 
April 02, 2020  Technology podcasts 
IT delivery in unusual circumstances 
March 20, 2020  Technology podcasts 
Continuous delivery for today's enterprise 
March 06, 2020  Technology podcasts 
Fundamentals of Software Architecture 
February 21, 2020  Technology podcasts 
Cloud migration — part two 
February 10, 2020  Technology podcasts 
The price of reuse 
January 24, 2020  Technology podcasts 
Towards self-serve infrastructure 
January 13, 2020  Technology podcasts 
Martin Fowler: my Thoughtworks journey 
December 27, 2019  Technology podcasts 
Building an autonomous drone 
December 13, 2019  Technology podcasts 
Cloud migration is a journey not a destination 
November 28, 2019  Technology podcasts 
Getting to grips with functional programming 
November 14, 2019  Technology podcasts 
Compliance as code 
November 01, 2019  Technology podcasts 
Data meshes: a distributed domain-oriented data platform 
October 18, 2019  Technology podcasts 
Edge — a guide to value-driven digital transformation 
October 04, 2019  Technology podcasts 
Tech choices: CIO or CTO? 
September 20, 2019  Technology podcasts 
Microservices as complex adaptive systems 
September 05, 2019  Technology podcasts 
Supporting the Citizen Developer 
August 22, 2019  Technology podcasts 
Getting hands-on with RESTful web services 
August 08, 2019  Technology podcasts 
Zhong Tai: innovation in enterprise platforms from China 
July 25, 2019  Technology podcasts 
What’s so cool about micro frontends? 
July 11, 2019  Technology podcasts 
Unravelling the monoglot monopoly 
June 27, 2019  Technology podcasts 
Breaking down the barriers to innovation 
June 13, 2019  Technology podcasts 
Delivering strategic architectural transformation 
May 30, 2019  Technology podcasts 
Exploring programming languages via paradigms vs labels 
May 16, 2019  Technology podcasts 
Multicloud in a regulated environment 
May 03, 2019  Technology podcasts 
Can DevSecOps help secure the enterprise? 
April 18, 2019  Technology podcasts 
A11Y — Making web accessibility easier 
April 04, 2019  Technology podcasts 
Continuous delivery for modern architectures 
March 21, 2019  Technology podcasts 
Delivering developer value through platform thinking 
March 07, 2019  Technology podcasts 
Architectural governance: rethinking the Department of ‘No’ 
February 21, 2019  Technology podcasts 
Serendipitous Events 
February 08, 2019  Technology podcasts 
Diving into serverless architecture 
January 24, 2019  Technology podcasts 
Seismic Shifts 
January 10, 2019  Technology podcasts 
Understanding bias in algorithmic systems 
December 28, 2018  Technology podcasts 
Microservices: The State of the Art 
December 14, 2018  Technology podcasts 
Evolving Interactions 
November 29, 2018  Technology podcasts 
The state of API design 
November 15, 2018  Technology podcasts 
How we build the Tech Radar 
November 01, 2018  Technology podcasts 
IoT Hardware 
October 18, 2018  Technology podcasts 
Continuous Intelligence 
October 04, 2018  Technology podcasts 
Distributed systems antipatterns 
September 13, 2018  Technology podcasts 
Agile Data Science 
August 23, 2018  Technology podcasts 
## Take a look at what's happening at the frontiers of technology
[ Explore Technology Radar ](https://www.thoughtworks.com/en-th/radar)