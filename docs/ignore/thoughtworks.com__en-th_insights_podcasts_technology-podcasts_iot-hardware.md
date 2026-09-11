<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/iot-hardware | Title: IoT Hardware | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  IoT Hardware 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Zhamak Dehghani and Alexey Boas | Podcast guest  Charlie Gerard and Desiree Santos
October 18, 2018 | 34 min 7 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/iot-hardware#transcript)
Listen on these platforms
## Brief summary
The Internet of Things promises radical change in how we interact with the world around — whether it’s coffee makers that turn on when our alarm clocks go off or using brain control to actuate objects. Join Thoughtworks Principal consultant, Zhamak Dehghani and Principal Associate, Alexey Boas as they explore the practical implications of building IoT software and hardware with Software Developer, Charlie Gerard and Consultant Software Engineer Desiree Santos.
**Podcast Transcript**
Zhamak Dehghani:
Hello. My name is Zhamak Dehghani, and I'm recording a session of our podcasts on hardware development with my cohost.
Alexey Boas:
Hello, my name is Alexey Boas. I'm the head of technology for Brazil, and I'm speaking from San Paolo right now.
Zhamak Dehghani:
Great. And I am in San Francisco. We have two of our passionate developers who've been working on hardware for quite a few years with us today from Brazil. We have!
Desiree Santos:
Hi, I'm Desiree, consulting developer.
Zhamak Dehghani:
And from Sydney, we have!
Charlie Gerard:
Hello, I'm Charlie, I'm a software developer, and I'm really excited to be talking about IOT today, so thanks for having me.
Zhamak Dehghani:
Thanks for coming. Yes. Desiree Santos has been a software developer for quite a while, but she has been quite passionately involved in hardware development since 2011, and she's been playing around with different tech stacks and different types of projects.
Zhamak Dehghani:
Anything from C++ and Rust and Raspberry Pi and different kind of hardware boards.
Zhamak Dehghani:
Charlie Gerard has an interesting perspective on IoT development because she's been kind of playing in the intersection of IoT design and art.
Zhamak Dehghani:
So we're super excited to talk to you guys about your experience today.
Alexey Boas:
And we are here at this time to talk a little bit about hardware development and internet of things. And so, there are a couple of different definitions, and there's also some confusion.
Alexey Boas:
So, internet of things. Hardware development, smart ecosystems.
Alexey Boas:
Desiree Santos, what's your view on what IOT is, and then what's involved when you talk about all these things?
Desiree Santos:
First of all, I love your question, right. But, I think that we have a few different terms of IOT definition, right?
Desiree Santos:
In my vision, and also understanding is we'll align it with... I can say we are garnered for being conceptualized definition.
Desiree Santos:
Imagine that the drink that you like, coffee or beer, it's over, right? And the refrigerators send a notification to your supermarket.
Desiree Santos:
That sends a box in delivery, your drink to your house, and debiting your account automatically. Right?
Desiree Santos:
It sounds like a dream. In the [inaudible 00:02:21] future. But it's not. It's real, and we're talking about the internet of things, right?
Desiree Santos:
And it's very interesting because when you're talking about the definition of internet of things, for me it means like a network of physical objects.
Desiree Santos:
So when you're talking about your drink, it's the physical. It's going to be like also your pet, your clothes, your refrigerator.
Desiree Santos:
These physical objects contain embedded technology, right? That could communicate and sense. It means get all information, getting the information from the environment, temperature, image.
Desiree Santos:
A lot of information and sends to somewhere. It could be local or in the cloud. And also interacting with the environment. The internal state or external environment.
Desiree Santos:
I think that it's a very important because when we are talking about internet of things, we have a different relation. It's not only people communicate with people. Like we have the internet today, right?
Desiree Santos:
But, we are talking about the people interact with things and things talk with things, also.
Desiree Santos:
So for me, the conception of internet of things, it's a mix of network, physical objects, communication, and sensor and exchange this data. To improve our life, increase the precision. For us to make decision.
Desiree Santos:
We want a good and better life. And I think that IoT really helps in part to improve this.
Alexey Boas:
That's great to hear, and thanks, Desiree Santos. That's a very good explanation. It definitely helps understand what this all means.
Alexey Boas:
And Charlie Gerard, what's your view? You've worked closely in the intersection of hardware and software and design. So what's your take on that? What does that mean in general?
Charlie Gerard:
Well, to me, IoT is to put it in a really small definition, I like to just say that it's like a giant network of connected things.
Charlie Gerard:
So, anything that can be connected to the internet via Bluetooth or WiFi can communicate together, and you can create new experiences either in, as Desiree would say, the kind of like automation of your life. Where you could have, I don't know, when you stop your alarm in the morning, your alarm is connected to your coffee machine and it starts your coffee straight away.
Charlie Gerard:
So, you have like a lot of different fields where IoT is present. But yes, where I like to actually... What I'm interested in is more in trying to create new interactions and new ways for people to interact with devices.
Charlie Gerard:
You have examples of, for example, dancers wearing certain sensors, and it interacts with the visualization in real-time. So depending on their movement, you have different colors or things like that.
Charlie Gerard:
So IoT can be used in really like a lot of different fields. I kind of like to try and explore, try to push the boundaries and really see where it can go.
Alexey Boas:
Oh, that's great. And what's some cool things you've been seeing lately, Charlie, you're working on and what's been exciting you related to that?
Charlie Gerard:
So what I've been working on for since I started being interested in that space actually is around motion sensors.
Charlie Gerard:
Either sensors that you wear on your body and you try to understand the natural movements of the body and apply that to certain actions.
Charlie Gerard:
For example, I was playing with an armband sensor called the Myo armband that senses the activity of the muscle in your arm, and you can detect if you're doing a swiping right movement or left.
Charlie Gerard:
So you can swipe your slides when you're talking about something, and you're doing a presentation, or I've been more recently playing with a brain sensor.
Charlie Gerard:
You wear the headset, and you can train it using machine learning to recognize certain mental commands, certain thoughts like pushing something.
Charlie Gerard:
And I was working around trying to build an interface where you could navigate using certain thoughts, which were still very early stages, but you also have facial recognition. When I'm looking right or looking left, I see different things in an interface. That's what I like to play with, really.
Alexey Boas:
And how about you, Desiree. What have you been playing with or seeing that's cool and excites you?
Desiree Santos:
Yeah, so I have a lot of projects to share and talk, but I think that I will start to talk with a project. Drone talk, IoT project from Thoughtworks, that is a silent [inaudible 00:07:00].
Desiree Santos:
It's amazing project because, since I'm from Brazil, I think the IoT market in Brazil is more regarding like the farming.
Desiree Santos:
And because of this, this project is calling so much of my attention, and I like to share. Right!
Desiree Santos:
The idea of this project is something like around the technology solution. Take the guesswork out of the milk production for farmers in UK. Right?
Desiree Santos:
And how it works, a cow wear a collar that contains a 3D solar meter, right, which transmits this data to a base station inside the farm.
Desiree Santos:
It's very interesting. It was called to my attention because sometimes you're talking about internet of things, always say the information to internet, but internet is, I think, instead of thinking internet, start to thinking the network. And sometimes like MESH. Because of a lot of constraints.
Desiree Santos:
Also, the security. Okay. But coming back to the project, it's interesting.
Desiree Santos:
The idea of this typical event, the cow, right, is the head. She moves a lot. Right? And also we have their fault.
Desiree Santos:
You can understand how much is moving and this movement. And all this movement are monitored to let the farmer know the right time, the best time to start the process.
Desiree Santos:
And also to improve the quantity of milk in the end, of course.
Desiree Santos:
The collar has the benefit of giving the farmers inside the hardware and maximize the amount of milk being produced.
Desiree Santos:
And I think it's very interesting because we have from the bottle, right? The 3D solar meter inside of the collar and sending this information to a base station.
Desiree Santos:
Of course, the main part is the data. Of course, the hardware is very interesting, but the data is the best part. Is the main part. Because of the data, we can increase our precision, and of course, when you're talking about the farmer, increase the amount of milk.
Desiree Santos:
It's a very interesting technology. And also it's a project from Thoughtworks, right?
Desiree Santos:
But, also, I have a personal project. Sometimes I like to create, build some projects. But sometimes I like to understand more, how can I bring some conception, from software development, and improve the internet of things process to the development process.
Desiree Santos:
And when you're talking about the continuous delivery, the continuous deployment in my day, I would like to do the same in internet of things project.
Desiree Santos:
And because of this, I'm starting to study some, "How can I improve this, how can I make sure that I could apply in a safe way?"
Desiree Santos:
And I decided to start some system operational that we call snappy, and this snappy is very interesting because you can start on the ground.
Desiree Santos:
I can talk about also using some [inaudible 00:10:39] board or another microprocessor, right?
Desiree Santos:
This operational system is very interesting because you can use this app, and this app is responsible to wrap and isolate your project. In the inside of this is embedded, right? An embedded system.
Desiree Santos:
And the other part is interesting. It's because this system. This Board, I actually brought, is connected with Apple store, not Apple store, but Apple application store on the cloud. Right?
Desiree Santos:
And every time that you have... You apply a new release. You automatically update all the projects.
Desiree Santos:
For me, it's interesting because I can move and apply and test how we can deliver in a fast and secure way when you're talking about 1000 hardware.
Zhamak Dehghani:
I like to kind of double click on some of these stories you shared and maybe talk about the technology behind them.
Zhamak Dehghani:
Charlie Gerard, you mentioned brain sensors and controlling the world with our brain.
Zhamak Dehghani:
That's scary and fun at the same time. Can you tell us a little bit more as how the brain sensor works? Especially, that calibration process that you mentioned and the tech stack behind it?
Desiree Santos:
Yes. So the brain... Since I've played around with two brain sensors. The first one was called Neurosky, but it doesn't have a lot of channels. So it doesn't really track. I wasn't really happy with the way it was tracking things.
Desiree Santos:
So I moved on to using another device called the Emotiv, and the Emotiv has 14 different sensors all around the head to be able to track different things.
Desiree Santos:
So the facial expressions and also some mental comments. And, when I started working with it a few years ago, the SDK was only in C++ and Java. So I wasn't really familiar with those technologies, cause when I learned to program, I learned Ruby and JavaScript.
Desiree Santos:
But I wanted to work on something that would allow more developers to play with that. So I built a framework in [inaudible 00:12:49] to be able to let JavaScript developers use the data and build JavaScript applications as well.
Desiree Santos:
So, yes, now in terms of tech stack, I think the Emotiv team has been working also on like a Python SDK, but at the time, it wasn't there.
Desiree Santos:
So, now there is C++, Java, Python and JavaScript. So the thing that I've been building, it's still like a work in progress.
Desiree Santos:
But it's really interesting to be able to get the data in nodes now, and either send it to the browser via whip circuits or interact with other devices or things like Arduino and Raspberry PI, all in JavaScript as well. Yeah, this is how it works.
Zhamak Dehghani:
Do you have a particular application in mind or a particular use case in mind for this brain sensor?
Charlie Gerard:
I built two little prototypes when I'm working with the device, and one of them is to have an interface with a keyboard. So you just have the letters of a keyboard but on a webpage.
Charlie Gerard:
And I'm using the movement of my eyes to be able to select letters and be able to write a message on a webpage just by using the movement of my eyes.
Charlie Gerard:
I actually started working with that because, well, that's a little bit of a personal story.
Charlie Gerard:
But, when my grandfather passed away, he actually was in a state where he couldn't move at all. And when I started playing with that brain sensor, I really realized that it could help people communicate with just the movement of the eyes.
Charlie Gerard:
Maybe not me, but it could help other people. And so that's also why I like to make it open sources.
Charlie Gerard:
If anybody is in the situation, they could actually buy the sensor and potentially use the framework that I built and let a member of the family of someone they know, be able to communicate with other people just by using the movement of their eyes, which is something that I think is really exciting.
Charlie Gerard:
But, otherwise, if we keep it to hardware, being able to just move things just by thinking about pushing something. So, you think about the action of pushing, and I can make a little robotic ball move forward, or a drone take off.
Charlie Gerard:
And it's not really useful. It's very much like experimentation, but it's quite extraordinary that now you can buy consumer products online that allows you to play with your brainwaves.
Charlie Gerard:
I mean, that sounds crazy to me, but it's just getting more and more accessible to a lot of people.
Zhamak Dehghani:
Yeah, I think that's such an important point because we often forget that hardware's been around for a long time. Connectivity to internet from hardware has been around for a really long time.
Zhamak Dehghani:
Suddenly, IOT becomes the thing, but it's that accessibility and the maker movement.
Zhamak Dehghani:
And, accessible hardware, schematics, prototypes, the whole maker movement pivoted, I think the industry and the ecosystem. So, that is super inspiring.
Desiree Santos:
But, one thing that you said is very interesting also, because I think that also become more popular because of the low cost of hardware.
Desiree Santos:
And also, when you're talking about the prototyping area, you can say the Arduino change drive it completely because it's open, easy to use, and very accessible.
Desiree Santos:
Even in Brazil or even different part of the world.
Charlie Gerard:
Yeah, I agree. I think that I probably wouldn't have been able to start experimenting with hardware if I didn't learn about Arduino.
Charlie Gerard:
I think it was... They made it look kind of so easy to get started with. Because I think at first it wasn't even developed for developers. It was actually created to help designers get into hardware and build, or artists and build art installations.
Charlie Gerard:
And I think that really made it look so accessible to me. Then I started looking into this space, and then I go into more complex boards or sensors. But I definitely did start with Arduino as well.
Desiree Santos:
Yeah. Every computer. And when [inaudible 00:16:56] created Arduino, the main idea was, "So I really like to empower people that really don't know programming and have any idea about electronic."
Desiree Santos:
I think that it's the magic. It's the magic.
Zhamak Dehghani:
Yes. It's a level of abstractions that just didn't exist in the past in an accessible way. They'll do better. I think in terms of... We've played a lot in the prototyping phase, but for commercial production-ready systems, we can still share more layer of abstractions, open libraries, open hardware, open schematics.
Zhamak Dehghani:
Desiree Santos, on the internet of cows project that you just shared with us, that was really fascinating because if I understood correctly, the farmers were using this hardware accelerators in the collar of the cows and then tracking their movement, and from the movements, they could then predict when the cow has most milk and be able to kind of utilize that information. Is that a correct understanding of that project?
Desiree Santos:
Exactly, You got the idea. Exactly. I think this project is amazing because also you can improve, maximize the production of milk, and now also detect some disease.
Desiree Santos:
Only because of a specific known movement from the collar. You can define this.
Desiree Santos:
And all this information I can say is data. Right? Data has a strong, strong power, and we really need to take care of it and increase our knowledge around this.
Desiree Santos:
Embedded data and all the data science. I think it's here. Yeah. This is the time. This is the era.
Zhamak Dehghani:
The interesting fact I had heard about that project in terms of the diseases was the cows actually get depressed.
Zhamak Dehghani:
And when they get depressed, they go far away from their herds and wander off, and maybe die.
Zhamak Dehghani:
So we can kind of get them back to life.
Desiree Santos:
Yeah. It's amazing because imagine a farm is very, very big and a lot of cows. But you know exactly the cow X and B has a disease or doing some more movements that you can improve for that cow. Internet of Things, it's fantastic.
Alexey Boas:
And this again, Charlie Gerard, you both have experience developing commercial software products, and working software consultants. What would be similarities and differences that you would highlight when you develop commercial software versus working in an IoT or hardware project?
Alexey Boas:
What are some of the main things that are different?
Alexey Boas:
Desiree Santos, you mentioned some of the deployment challenges and doing a distribution of binary's and then doing continuous delivery in that context. Are there other aspects that you think are relevant?
Desiree Santos:
Yeah, I think, of course, there are a lot of difference between one and the other, but I think that looking this perspective, when it's time to think about internet of things projects in more complex.
Desiree Santos:
Because you also need to understand where these projects will be. It's inside the house. It's outside the house, is a farm. And it's also the kind of sensor you need to use. You need to understand the best connectivity to use.
Desiree Santos:
It will be online/offline. Also, we have a different variety of states when you're talking about connective the machines, right?
Desiree Santos:
If the machine is WiFi off, it's on. If it's busy, it's sleeping.
Desiree Santos:
You need a lot of things to take care.
Desiree Santos:
But, when you're talking about also the software development, I think the main part, and a lot of the mistakes that I saw a lot, is when you're talking about some protocols, right?
Desiree Santos:
When you're talking about the interrupted ability. Because we are dealing with a lot of, and different kinds of hardware and sometimes hardware means we have some relation with the fabric.
Desiree Santos:
That you need to use a specific protocol and your application should deal with different and multiple protocols.
Desiree Santos:
And of course, for IoT, we need to take care about the size, about the restriction of the band, about the restriction of the hardware, and it guides us.
Desiree Santos:
Instead of using HTTP we usually use, we need to take care and think more about messaging.
Desiree Santos:
We can say protocol like MQTT or COOP or if we talking about MESH, maybe Zeeb or Telehealth.
Desiree Santos:
Something like this, but it's a different perspective. We need to take care of much more than regular or normal software development.
Alexey Boas:
And Charlie Gerard, I know you use a lot of creation process when working with hardware. So could you tell us a little bit about this prototyping cycle in that context, and then how it works and some of the highlights and pitfalls of doing this kind of stuff?
Charlie Gerard:
Yeah, so every time I come up with a new idea... So, for example, in Sydney, we moved offices a few months ago, and we wanted to start and build kind of our installation in the office that would involve using voice recognition to display words on a matrix of LEDs.
Charlie Gerard:
So that sounded really exciting, and I had an idea in mind, in theory, about how everything would work.
Charlie Gerard:
But then, when I started prototyping, I realized that it was not at all what I thought.
Charlie Gerard:
And that's what I really like about prototyping. It's you kind of think you have it all covered, but then as soon as you start, you realize that you're going to probably have to change everything.
Charlie Gerard:
And you iterate, and you start with boards like Arduino or Raspberry PI and you kind of attach sensors one by one, and you see what doesn't work.
Charlie Gerard:
And also, in terms of the amount of power that things are going to need.
Charlie Gerard:
For example, if you just prototype with an LED at first, you probably just need three or five volt or not even.
Charlie Gerard:
But for our matrix of LEDs, we started... We had to actually calculate how much one LED would need multiplied by, probably 1000, and then you actually deal with real power.
Charlie Gerard:
I haven't had the time to really keep working on that. But it was really interesting to start with Arduino for a very basic prototype. And then I realized, "Well, the Arduino can't drive that many LED strips."
Charlie Gerard:
So we moved to a raspberry PI, and then I was following a tutorial, and they were talking about having a FadeCandy driver between the Raspberry PI and the LED strips.
Charlie Gerard:
And then same again. I actually realized later on that the strips were too long to be driven by the FadeCandy driver.
Charlie Gerard:
So it was having all these different steps made me realize that prototyping is a very important stage. You learn so much about things, and then you start changing how the whole installation is going to work.
Charlie Gerard:
And yeah, so that's, that's my process really. Starting little by little, I haven't had the chance to put anything to production yet. So I don't exactly know what is involved later on.
Charlie Gerard:
But at least in terms of prototyping, that's definitely a stage that is important, and that you shouldn't forget.
Zhamak Dehghani:
I think that's what's really changed in kind of hardware development. Because even doing prototyping was such an expensive step. So you would normally traditionally have these very concrete schematics upfront and every iteration to produce the boards. And then every iteration of that will go through some sort of different hardware verifications, and it would be yet another multi-month expensive projects.
Zhamak Dehghani:
But, having an open hardware that you can just plug things to it and then at least get an idea if the idea you had in your head is doable at the prototype level.
Zhamak Dehghani:
Yes, production might have different restrictions and foreign factor restrictions, but even to be able to just touch and feel and get some feedback from the idea, that's super empowering. That we didn't have prior to open hardware movement.
Desiree Santos:
Yeah, I think it's the best benefit of a prototype, because during the prototype cycle, you can forget the best products.
Desiree Santos:
You can also focus the minimal of the product, like the MVP, the value to validate some things that are in your mind.
Desiree Santos:
When you're talking about this, the prototype for IOT, we can, of course, talking about Arduino. Because it's easy to use, and everyone can start from zero to hero.
Desiree Santos:
Doing your project. Yeah. And see things really happen. And no matter if it's the best products, the best sensor, the minimal you can do. And also it's very, very, cheap.
Alexey Boas:
Yeah. That takes us back to the things you were mentioning that made IOT and hardware development popular despite some of the things being available for so long.
Alexey Boas:
And, and Zhamak Dehghani, I think it was you that mentioned the maker movement as something quite important to make that happen. What's that? What's the big movement?
Zhamak Dehghani:
I think the [inaudible 00:26:48] for me is the accessibility and availability of the hardware to tinker.
Zhamak Dehghani:
Everybody who wanted to just tinker and build their own things. I think a few technical development made it possible. One is open hardware like Arduino and the libraries and their simple firmware that may not be production-ready, but it's good enough for prototyping, became available.
Zhamak Dehghani:
3D printer became kind of widely accessible, so people started making their own things, physical things much more easily. And there were businesses actually built and commercial offerings built to workshops to build workshops and allow people to go in and use different machinery to produce the physical objects and create the boards and so on.
Zhamak Dehghani:
I think what's interesting is how to replicate that within an enterprise and within an organization to create innovation. And through creating space for innovation at Thoughtworks, about five years ago, we started with a little global competition called 100 days of hardware, which was basically a global initiative for any developer who is interested in building something with hardware, to get his or her hands dirty to build the project.
Zhamak Dehghani:
We got support, financial support from the local offices, and we started investing in creating a makerspace or an innovation lab within every office. And I think at the end we had some sort of a prize for the winners.
Zhamak Dehghani:
But it just... That little nudge and that little support that we got from Thoughtworks internationally and across all the regions have created this wonderful spaces.
Zhamak Dehghani:
Now, every office has a maker space, has a passionate community around it that build things and also build capability to explore more commercially developed applications.
Zhamak Dehghani:
And I'm curious actually because I know more both Desiree Santos and Charlie Gerard are active members of their community. Maybe you can share your experience about the maker space and innovation lab in your office and what it offers.
Desiree Santos:
Sure. I love it. So when you talk about the makerspace, for me it's a magic word, right?
Desiree Santos:
Because if I'm interested about IoT, I learn in sign from the space.
Desiree Santos:
Makerspace and hackerspace, for me, it's like collaborative work, and we can build things together, and no matter if the person is from technology or not.
Desiree Santos:
Because sometimes inside the right hackerspace in Porto Alegre, we start coding in Rust or Go.
Desiree Santos:
And in the end of the day, we start to talk about the life, how life is.
Desiree Santos:
This is the point. As I reach a space to share, create and build the things together. And no matter what you know or don't know. I think it's amazing space.
Desiree Santos:
But the point is, this kind of space has tools that make you empower you to build and create the things.
Desiree Santos:
Like, do yourself, you can do. You can build and sometimes you can use learning to choose a 3D printer or help someone to build a smart plan, connect things.
Desiree Santos:
And I think this is a different mindset when you have it inside the office.
Charlie Gerard:
Yeah, no, I agree. I think it's actually really important to have like a makerspace. Because having a dedicated space makes you more likely to actually experiment.
Charlie Gerard:
Because you have this space where you have access to a 3D printer or different sensors, LED strips, anything that you want.
Charlie Gerard:
And this space is kind of only to build whatever you want and to experiment. And if the 3D printer makes a bit of noise, you're not bothering anybody else because you have this space where you can build.
Charlie Gerard:
And, also if you start building something, you can just leave it outside in this room, and people get curious, and they ask you a little bit about what you do, and maybe they even contribute with their own ideas.
Charlie Gerard:
And it's kind of creates a different dynamic where you can just let your creativity go, and you build whatever you want, and you actually have the space to do it.
Charlie Gerard:
You don't feel like you have to share a desk on a normal table where a lot of hardware can actually bother quiet people. Where it can get a bit messy. You can actually have this room where you can just borrow things whenever you want and experiment with it.
Desiree Santos:
Yeah. And because of this, I think the maker culture is very strong inside of this collaborative space, right?
Desiree Santos:
Because sometimes, every time they want you to start a project, the first thing is, "Okay, I need to learn A, B, C, D." And after it starts to work.
Desiree Santos:
In the makerspace, it's completely different. It's change this mindset.
Desiree Santos:
Instead of listing all things, it's changed, "Let's try to start with the minimum that we have."
Desiree Santos:
And it's a lesson for life., Not only to build things but for life.
Desiree Santos:
And it also changed a lot of my daily work because every time you're assigned a project is the same mindset.
Desiree Santos:
Or okay, "What's the minimum that we need."
Desiree Santos:
Not necessarily to have, the sandbox and the AWS or in different place. But, let's start doing a little bit in spite.
Desiree Santos:
I think this kind of mindset. It's changed a lot of our day.
Zhamak Dehghani:
That, I think, was quite evident when I went back to Sydney last week.
Zhamak Dehghani:
After a while, I noticed the difference between makerspace in Sydney when we first started.
Zhamak Dehghani:
When I first started setting it up five years ago, it was out of a few drawers in the middle of the office. So we had a few Arduino boxes and some sensors and other things in a drawer, and we will bring them out, put them in the kitchen and use the kitchen temporarily as a makerspace.
Zhamak Dehghani:
But, now, as Charlie said, we have a dedicated space with a lot of gadgets and goodies. Really creating an environment for learning, for experimenting. As you Desiree mentioned as well, just providing the conditions for learning, and this grass-root movement just blossomed itself.
Alexey Boas:
Yeah, it's cool. And on top of that, every Thoughtworks office is always hosting events and many things open for the community.
Alexey Boas:
If you listened to this and happened to be in Porto Alegre or Sydney, check it out. You might be able to get to know one of these spaces.
Alexey Boas:
So that's really awesome.
Alexey Boas:
Okay, so I guess we're coming to the end of this episode. It was a great conversation. It was great to have you with us. Thank you very much for joining. Bye.
Rebecca Parsons:
And next time, we will be joined by Camilla Crispim and Marco Valtas, both from Brazil, who will talk along with Neil and myself on how we make the Radar twice a year. So please join us.
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