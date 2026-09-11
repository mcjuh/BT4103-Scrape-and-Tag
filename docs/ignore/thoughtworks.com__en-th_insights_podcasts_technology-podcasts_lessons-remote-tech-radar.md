<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/lessons-remote-tech-radar | Title: Lessons from a remote Tech Radar | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Lessons from a remote Tech Radar 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford | Podcast guest  Zhamak Dehghani, Mike Mason and Evan Bottcher
May 13, 2020 | 47 min 42 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/lessons-remote-tech-radar#transcript)
Listen on these platforms
## Brief summary
The COVID-19 pandemic meant that for the first time in 10 years, the next volume of Thoughtworks Technology Radar had to be created via a virtual meeting, instead of face-to-face. Our podcast team share their experiences of working on this complex and highly interactive project. They discuss how the tech held up, what was missing and what worked well.
**Podcast transcript**
Neal Ford:
Welcome to the Thoughtworks Technology Podcast. I'm Neal Ford, one of your regular hosts, but you can't see me. I'm doing air quotes around host because we don't really have hosts and guests for this episode. Rather, what we have are four regular members of Doppler, who's the group who puts together the Technology Radar, and we're here to talk about what it was like to put together the Technology Radar during the midst of a global pandemic. So I'm one of your regular hosts, Neal Ford, and I'll let the other folks introduce themselves. Zhamak, you can start.
Zhamak Dehghani:
Sure. Hi everyone. I'm Zhamak. I'm also a member of Doppler, putting the Radar together as well as being your host in this podcast. And I joined the Tech Radar sessions as well as joining this session from San Francisco.
Mike Mason:
And I'm Mike Mason also one of the regular hosts of the podcast. You might remember me from a previous podcasts such as the one in which James Lewis absolutely blows my mind talking about complexities theory and microservices. I'm happy to be on the podcast.
Evan Bottcher:
Hi. I'm Evan Bottcher. I'm the head of engineering for Thoughtworks in Australia. And I've been part of the Doppler group since about 2010. So it's been an interesting experience.
Neal Ford:
Yeah. So one of the things that we always swore was impossible, absolutely irrevocably impossible, was to put together a Technology Radar not face-to-face. In fact, even during terrible financial times, at Thoughtworks we fought the battle so that we could get face-to-face to put together the Radar because it is an intensely collaborative, interactive kind of exercise. And yet necessity is the mother of invention. For the last Radar, we were scheduled to all meet in Singapore in April, but of course for obvious reasons we could not do that. And so by a lot of really great innovation and reliance on some technology, we managed to do it. And this is what that podcast is about, is what our Radar normally looks like and in how we had to adapt to it for the modern world.
Neal Ford:
So well, just talk first about what our Radar is normally like. So we gather a group of about 30 people from literally all over the globe. Poor Evan is often the victim of time zone horribleness unless we go to Australia because he's having to come from Australia. And we meet face-to-face in one of the folks locations twice a year. And it's a very intense week of putting together the Radars. Anybody want to give a feel for what that's like?
Mike Mason:
Well, I mean one of the aspects of the Radar is the sheer amount of proposed technologies to go onto it. That we as a group have to sift through and figure out which of these are worthy of being on the Radar and actually us wanting to make some noise about and tell all of our readers about. So one of the big things is that decision making for usually around 200 proposed blips, I think just to get a scale of it. 200 proposed blips, probably 100 or 110 existing blips from a previous Radar that we still need to figure out what to do with. Do they survive onto this new addition or do we do something else?
Mike Mason:
So there's the blips themselves, there's the themes. So we'll include some themes at the beginning of the Radar, which tries to give people a sense of the discussions that we had, the important trends that are happening because of course looking at hundreds of individual technology blips can be a little bit bewildering and difficult to follow that. So we put together trends. And then actually there's a whole bunch of other stuff that we'll do at the meeting, which is also about us as Thoughtworks technologists.
Mike Mason:
Rebecca Parsons runs the meeting, she's the Thoughtworks CTO. And so she'll use us as a sounding board for various things that are going on within the company as well, which are not necessarily strictly Radar related. But we'll spend time on those during the meeting too.
Zhamak Dehghani:
Yeah. And I think for me an additional flavor of being at the Radar usually involves carrying, now a three and a half year old child with me. So I started joining since she was six months. So long days of having conversations and arguing over the blips and which one should be in and which ones shouldn't be in and then dealing with the jet lag few months or now three year old baby. So this was actually a nice change to be honest.
Evan Bottcher:
I think one of the reasons why I've always felt that remote would be very difficult or doing this in a distributed way would be difficult, is that there's this richness of storytelling that comes with each of the discussions. And so we tend to, Rebecca runs the meeting in a really interesting way allowing space for people to share the experiences they've heard from their regions and to expand and let the important conversations run on and then for us to swim in that conversation. But then when you're ultimately getting down to a decision, because we have a lot of material from all over the globe to get through in order to produce this information to publish out to the world. So I was really skeptical that it would work or that we would get the same value. And I was pleasantly surprised at just how good it actually was.
Neal Ford:
So there, I think at least two distinct things there. One of the things that we've developed over the years, we've been doing the Radar for 10 years now. In fact, this coincides with the 10 year anniversary for the Radar campaign, which is also interesting. But we've worked out an all sorts of interesting analog techniques over the past decade. We always nominate blips by using yellow sticky notes on a big huge white board that has been prepared by someone coming in. And we've also, if you've read the really terrific article by Camilla Crispin about how we create our Radar, she talks about several of the conventions that we created. For example, every member is given a green, a yellow and a red index card as we come into the meeting as a quick way to judge the temperature of the room. So for example, when Rebecca talks about a particular technology item, if everybody holds up green, then there's wide agreement. Everybody holds up red otherwise, and yellow means let's talk about it.
Neal Ford:
So a lot of these face-to-face analog things that we've really inspired by agile software development of course, which is where the roots of our company come from. We ended up having to recreate, and we'll talk a little bit about that in a second. But the other thing I want to talk about briefly as something that Evan mentioned was the actual experience of being at the face-to-face meeting. The meetings themselves are very intense, but I equate it to visiting a submarine for a while because it's not just the nine hour meeting during the day, because before the meeting, you've all been at breakfast together. And then at lunch you all have lunch together. And then in the evening there's an office event with a bunch of other Thoughtworks people or you go out to dinner and you frequently go out to drinks.
Neal Ford:
And so it's very much like being trapped on a submarine, in a very good way trapped on a submarine. But it's like being trapped on a submarine with a group of people and there are a lot of side conversations that happened that actually contribute to a lot of the texture of the Radar, particularly things like the themes, which is really the thing that you can't do preparation for before the week happens, because the intent of the themes is really the culmination of the conversations that happened over the week. So we'll talk about how that came about.
Neal Ford:
So Ni, Ni Wang is now the Rebecca's assistant. She's the one who runs and does all the admin stuff for the Radar. And so it was discovered that we're not going to do the face-to-face. We're going to try to do it remotely. And so Ni ended up creating some magnificent stuff.
Mike Mason:
Well, actually just to tell the full story, Ni is located in China. So in actual fact, even while we thought we were going to still have the meeting in Singapore, China had locked down. So we knew that she was not going to be able to make it to the meeting. So we actually had an inkling that we would need to do something different because the technical assistant who runs all this stuff was not going to be there and we were going to need to do some sort of filling in for her. And then as the situation globally changed, we actually were planning to go to Madrid instead, which also would have turned out to be not a great idea.
Neal Ford:
For about a week we were planning to go to Madrid.
Mike Mason:
About a week. [crosstalk 00:09:36] No. Then we weren't going anywhere at all. So we had a little bit of a warning that we'd need to do something different, but I think it was only maybe a month before the meeting that we really realized that it was going to be fully removed.
Zhamak Dehghani:
And I think Mike, you were involved in some of those decision makings as how to move the face-to-face experience with fully digital experience. And I know generally attending Radar meetings are super considerate and inclusive of everybody regardless of where you come from. And we always really try to find a middle ground that works for everyone. And this time around, we had to have a digital remote experience with 10 different times zones. So that was, I guess one of the, maybe if we can talk about like different factors that went to making a decision around the digital first experience that is inclusive of everyone, regardless of where they come from.
Mike Mason:
And actually I should also mention that two of our regular Doppler members were also from China, so we were actually going to be losing three people from China. And then as the situation evolved, it became clear we were going fully remote. And I think one of the things that people are starting to realize in this emergency remote world, it's not exactly planned. All of this stuff is that everybody's individual situation is different. Not everybody has a home office that they can work from. Some people are managing living with their family and pets and all that kind of stuff. Everybody's situation is different. And we had to be careful about making assumptions about what people would have access to, even in terms of things like the number of devices that they might have in order to be able to connect digitally with the meeting.
Mike Mason:
A few of us actually, I think tweeted and sent LinkedIn pictures of our set ups. One of the things that people who were sending those were sending was giant gaming rigs with huge monitors and massive, we'll talk about it in more detail, but it was a big, dense spreadsheet of blip data that we were using to work through all this stuff. But being able to have enough screens literally to show the people's faces as well as the digital artifact that we're working on. And we thought about it, but there wasn't a lot that we could do. So we tried to design the experience so that it would work if you only had your Thoughtworks laptop, if that was the only thing that you had.
Mike Mason:
But we were encouraging people, if you've got an iPad as well, maybe get that out and try to multi-device to increase the amount of ability to join. I wasn't actually involved directly in the discussions but we ended up doing six hours a day and asking people to shift their schedules to align with those hours. So for me that was getting up early to do that, which wasn't really a big deal. For some people it was actually almost like they were working the night shift. Our friends in Australia were doing that. And what we tried to do was, because we know how important and how valuable that face time is because of everything that Neal was saying about the richness of the conversation, we really valued that together time, even though it was virtual together time.
Mike Mason:
So certainly the first two hours of that six hour chunk, you really had everyone's full attention and nobody was even showing any signs of fatigue or anything like that. It was only towards the end of that big block of time that the reality of it being in the middle of the night for some people kind of crept up on them. So something that was great was how willing everybody was to do that, to make it work and to really make the most of the time that we had.
Mike Mason:
The other technique that we did from an organizational perspective was we had two times owner line subgroups who could do work outside of that core chunk of hours and we could figure out is there a sensible chunk of Radar something that we can carve off for those groups and then work that back in when we all got back together.
Neal Ford:
So let's give a direct sense of that. So I'm on the East coast of the US. So for me it was 8:00 AM to 2:00 PM every day. So what about Zhamak Dehghani? What was it for you everyday?
Zhamak Dehghani:
I woke up at 4:30 to show up with my eyes open at 5:00 AM.
Neal Ford:
5:00 AM?
Zhamak Dehghani:
Mm-hmm (affirmative)
Neal Ford:
Mike.
Mike Mason:
6:00 AM for me.
Neal Ford:
And Evan.
Evan Bottcher:
Yeah. The meeting for me and Scott Shaw, the other person who's here from Australia, that's part of the Doppler was from 10:00 PM until around 4:00 AM, the official time but I wasn't quite making it through all the way until 4:00 AM. It's an interesting experience for me of all of the sessions that I've been to, all of the Doppler meetings and Tech meetings that I've been to, they've almost always been significantly out of my home time zone. And so I'm actually quite used to spending time with this group of people in a state of delirium.
Evan Bottcher:
So staying up a bit later wasn't actually that hard. And it was actually almost a bit of a relief to not have to go out for dinner afterwards, which is always a little bit hard when you're absolutely ruined. Most of you will know from some kind of time zone shift as part of these meetings. Obviously the cost of that was quite hard because we got a lot less of the time to expand on stories from the day or to share those social times together or with the local Thoughtworkers wherever we would be. But yeah, the actual time zone shift worked reasonably well for me.
﻿Neal Ford:
Yeah. But to Mike's earlier point, it's just if you've got to get everybody in a global company together, you got to make some major sacrifices. So we try to pick a sweet spot to get the most people but there were always going to be outlier. So I think one of the really smart innovations was to create the sub-working group that did in fact encompass a reasonable working time for people at Asia. And they actually did a huge amount of very useful work and going through some of the lower priority things and sifting through them so that the larger group could move through them more quickly. So it turned out to be quite an effective way. A use of time.
Mike Mason:
Yeah. One of the things that we did. I mentioned we've got 200 proposed blips to wade through and figure out what they are. One of the things we did was give everybody homework beforehand, which actually was not 100% successful because everyone's dealing with this weird situation and work from home and all that kind of stuff. But quite a lot of folks were able to wade through the blips and give an initial thumbs up, thumbs down on that. And by looking at those, we could see which ones were the most controversial. And so therefore, which ones are we going to need to discuss when everybody's the most awake, when we've got the most attention from everybody, which ones do we need to discuss early in the week as opposed to maybe later in the week when we're running out of time. One of the things that the sub-group did was they did these low priority or low controversialness, uncontroversial proposals went through those and then were able to bring those back to the group.
Zhamak Dehghani:
I really actually liked that innovation because we had a constraint. We didn't have nine hours together, we had a shorter number of hours together. And usually we don't prioritize, we basically go through all of the blips. We start with the quadrants that has most number of blips. That's the only prioritization we did in the past. But now this time we prioritize based on let's get the heart conversations out, make sure we cover those and then take a different approach for the others. And I wonder if he wouldn't take some of these methods that makes creation of Radar a bit more effective forward even if we do it face-to-face.
Neal Ford:
Well, let's talk about some of the innovations, because I'd like to get to some new innovations, things like the scary tab, but we need to talk about tabs on the spreadsheet first. So let's talk about Ni's magnificent spreadsheet for just a bit.
Mike Mason:
Okay. So I could describe this a little bit. Unfortunately she was unable to be on the podcast today, so I'm trying to fill in, doing a poor job I'm sure. So Ni is a technical assistant for Doppler and for Rebecca. And when we say technical, we really mean that. This is somebody who is an awesome developer in her own right. And once she's spent a year or a year and a half, whatever it is helping us do technology stuff and Radar type things, she's going to go back to being a professional consultant. And so she brings a huge amount of technical capability to what she does for us as a group. And I think this was a really good example of that shining through because we've been slowly increasing the amount of tech and automation that helps the Radar from... I think the first one was PDF only. Recent ones, the PDF is also if you really need a PDF you can get one. But the primary way of consuming the Radar is the interactive website version of the Radar.
Mike Mason:
And that's actually backed by a bunch of stuff, including blips written in markdown and GitHub and a Trello board and all this other stuff. So what Ni had done was really amp up the full level of automation for what we had and providing unified tracking across this giant spreadsheet. So it had all of the proposed blips. So it was a Google sheet, so it was live. Anyone could look at it. A Google sheet for each of the phases of what we do. So in the initial discussion about each proposed blip as well as did it make it? Okay. So it's made it from an initial discussion where we then have an existing blip review that was an entire tab in this spreadsheet.
Mike Mason:
There's this final call process that we do where we realize we have 150 things that everybody likes and we actually need to cull the weak ones from the group. It's called cull for a specific reason. We have a lifeboat activity where anyone who is feeling like something they proposed or their region proposal or something that they heard during the week got the short end of the stick and they would like to give that technology another chance to be on the Radar. There's a lifeboat activity. So each of those had a tab in the spreadsheet with some Google spreadsheet automation magic to copy things back and forth and do filtering and all this kind of thing.
Mike Mason:
The thing that I think worked really well, that has been a huge innovation was the real time voting. So Neal mentioned earlier on that we would all vote in person with an index card that we'd hold up and wave around and all that kind of thing. We actually had lines in the spreadsheet per technology where each person as the discussion was happening could give it a thumbs up or a thumbs down or say they want to put their hand up and actually discuss something.
Mike Mason:
And that was incredible. You were able to watch somebody on video making an argument in one direction or another and actually see the mood of the room changing because we had a little counter tally for the number of blips and you could see things flipped from red to green as someone made an eloquent argument for why this thing is important and we should include it on the Radar.
Mike Mason:
The other thing I'll mention, I think we did, we've always done a good job of this in person, which is to raise a yellow card when we wanted to discuss. And Rebecca would keep track of who wanted to make a point and we'd go around the room. And actually for some people it's a bit of a weird experience because we don't have a discussion straight back and forth. You take turns to say things that actually we continued to do that and I think it worked really well. But that's a great way of allowing everybody involved in the discussion to be able to have a voice and not worry that there's a more quiet person in the corner who hasn't had their say.
Neal Ford:
Yeah, I will double that. I was really shocked at how well the spreadsheet managed to replicate the in-person flipping cards. Because one of the things you see very often in the live meeting is that the initial vote for something, there'll be a few red cards and then someone will make a really good point and then you'll see the tide start turning and then it'll eventually turn to the other direction. We saw the exact same thing happened over and over again in real time on the spreadsheet. And part of that, and this is one of the points that we wanted to bring up and this was a good time, how well the underlying tech held up.
Neal Ford:
We were 30 people globally distributed, we were hammering on the spreadsheet and the spreadsheet was very clever because it was basically one sheet with all the data on it and then multiple tabs with all these really clever filterings and sortings and all this other stuff.
Neal Ford:
And we were all hammering on this thing in real time. Plus we were all watching each other in Zoom, so we're all logged into a Zoom meeting and so we could pretty much see each other in real time and interact in real time. And just a half of second latency added to that recipe would have been a disaster because a lot of that real time interaction would have been lost. And so we were actually, I think, fortunate, I was quite trepidatious coming into the meeting about how well the tech would actually hold up, especially given that everybody else in the world is having to do the same stuff. And I was pleasantly surprised as an architect at how well things didn't break.
Evan Bottcher:
I think this is where for some of us in the antiquities down here at Australia that only I'm on the end of the longest span of internet distance and also due to the crisis. So we were isolating in our country property equivalent of a log cabin in the backwoods. And so I was on satellite internet, which introduces latency. But even then I felt that I was able to participate both through the digital tools, that the spreadsheets and other things that we were using. And the Zoom actually held up really well, so I was impressed with that.
Evan Bottcher:
Often, I just want to make the point. Often in my consulting and talking to clients, we talk about the Doppler meeting as an example of how to get 20 people in a room and or more now and have an effective run of conversation. It evolved over time, I think being there for nearly 10 years. And to the system using the cards and Rebecca essentially drives the traffic of the conversation in the room through and does it very, very skillfully.
Evan Bottcher:
And I've talked to people who need to, facilitated sessions where you really need to get to an outcome and you really need to allow people to speak, but you need to narrow in on outcomes in a reasonably quick amount of time about doing this. And I've yet to have anyone try to replicate it because it requires such a high degree of trust and it requires such a high degree of respectful disagreement within the room. That's then allowed to go on. And it's really quite hard to do. And it's one thing that I think really allowed us to have this meeting remotely was that almost everybody is the same. It's the same team with some very, very small changes. So almost everybody was there in the last few meetings and is familiar with the way the meeting runs. And so I'd be very interested to know whether we could replicate this from a cold start as a remote meeting or whether it actually relied on the face-to-face interaction to get it started.
Neal Ford:
Well, I think to Evan's point, one of the observations we've made in the past, and it was only an observation we made after the fact, was that as a group, as people of Thoughtwork we typically are very opinionated. As a company we're known to be quite opinionated and reaching consensus in that room of very opinionated people we're actually very good at it. And I think in hindsight we've realized that if you're a tech lead or an architect on a Thoughtworks project, you get accustomed to making your best argument. And then if you don't win it, then you can't be mad and sore and hold a grudge. You just got to move on and make a better argument next time. And I think all of us bring that into the meeting. And I think we discovered this when there were several other similar size groups that tried to spit up at Thoughtworks and they had trouble doing things like deciding which room to meet in for hour long discussions.
Neal Ford:
They just couldn't reach consensus on anything. And we realized after the fact just like, well we exercise that consensus muscle on a regular basis. And that added with the mutual respect, that Evan was talking about, because we know no one in the room is bringing bad intent because we're very serious about doing this. So there's a level of respect and respect that is certainly I think facilitated this and it would be extremely hard to do this from a cold start because you wouldn't know all the things about the group of people. And it would be hard to pick those things up.
Zhamak Dehghani:
And I think one of the things we know about the individuals is that the perspective that every individual brings, we all bring a slightly different perspective and we have different tendencies or different biases and we cancel each other's biases out. And that combination of the group we have different experiences, we have different areas of focus on people, our data. I'm all focused on people, our infrastructure, platform focus. I think one of the first things that I noticed when I joined the first Radar was this global perspective. That the blips don't come from one country with the biases that countries have. And we are very cognizant of not picking things that are very localized and relevant to one area of the world and not relevant to the other area. So I think that complimentary factor makes us comfortable with our ideas, not make it to the final round because we know that there's a holistic view that is filtering what's relevant, what's not relevant to the Radar.
Mike Mason:
I think the other thing I would offer is that I would not expect any anyone to magically develop a process overnight. Whether that's in person or remote, whether that's from a cold start or a lukewarm start or even a warm starts. Part of the reason that we were able to do this was because we had a very solid process. There are other groups within the company that I'm working with where we are frankly still figuring out what our process is for the group and both trying to do work as well as have that meta discussion about our process and what are the expectations and what should we change, what should we do differently?
Mike Mason:
And so I think if something isn't perfect the first time through, that's natural in this remote first world. And people need to expect to have to put in effort of their process, of their digital tools, all that kind of stuff to get better at doing it and to look for things that were a problem and try to fix them, to make it better the next time that you do it and it's really a process and you're going to get better over time.
Neal Ford:
So to that point of making changes as you go along and being flexible, Mike, can you describe to us what the scary tab was and how it changed over time?
Mike Mason:
So when Ni had originally put this things together, we had all the separate tabs with all the proposed blips. But then actually we realized there's all this other work that we have to do is not just the, how many proposed blips where there? Was it 293 blips or so?
Zhamak Dehghani:
It was about 300.
Neal Ford:
It was almost 300.
Mike Mason:
Okay.
Neal Ford:
Higher than usual, which is even more terrifying.
Mike Mason:
Exactly. So usually we have 200 proposed blips. We had nearly 300 this time. I still don't understand why we had more.
Zhamak Dehghani:
We had time to do homework.
Mike Mason:
Everyone had time to do, okay.
Zhamak Dehghani:
We didn't have time to do homework, but we were asked to do homework.
Neal Ford:
Actually the suspicion too that people were paranoid that other people wouldn't bring in as many. So people brought in more.
Mike Mason:
Everyone did extra effort. Yeah. So we had tons of these things to work through. And not only did we have all the new proposed blips, we had all of the old ones as well because we have to decide what's going to happen. Whether we have switched to fading stuff by default, but we still need to go look at all the things on a previous Radar and say, are any of these important enough to still talk about them on this edition? And then on top of that we had the analysis from people's initial thumbs up, thumbs down votes, which ones are controversial. And we had tons of controversial ones where we knew there was going to be a lot of disagreement. It was going to require a significant conversation. And Rebecca wanted to quantify what that was.
Mike Mason:
And so she said, "Ni, can you make a new tab on this spreadsheet that just details some of that stuff." And so we made a new thing and it was called scary tab to begin with, which had just the horrific numbers of blips that we still had to go through and 0% complete across the board. And what was funny after two days of going through it, someone renamed scary tab on the spreadsheet to, I think it was vaguely reassuring tab. And then the next-
Neal Ford:
Yeah. There was a legitimate concern going in that we would not finish all this Radar stuff.
Mike Mason:
Absolutely. I think all of us are amazed that we got through it frankly. I think it's a pretty good Radar. I'm happy with the result. I think it's going to be really interesting to see the response from the community, would people have known that we used a completely different process to create this thing? Is it up to our usual level of quality? I have a good feeling about it. I think the external response to that is going to be interesting.
Zhamak Dehghani:
So just on that dashboard that we had, the scary tab and then evolving to give us better news over time. I think this is an interesting one because with COVID and outside of Tech Radar, things are changing day by day. So a lot of our clients are actually asking to have a data driven executive dashboard so they can keep track of things day by day. So I see this as a trend that is going to go beyond Radar and will become more data driven because things won't change over long period of time. And we wouldn't know how things would change based on our gut feeling. We have to rely on data more and more. And this was a good example of a little executive dashboard that you had built into our spreadsheet.
Evan Bottcher:
So I have experience, I do some consulting with a client who builds their own Technology Radar and almost immediately at the time where we were putting this together or almost coinciding with, they needed to produce the next issue of their own internal Technology Radar with their own technology leaders and they are fully remote because of the crisis. And so I was able to immediately just show screenshots and examples from what we were doing. And they've made a big effort to try to replicate some of the same techniques. Now particularly being able to provide that live information back to their group on what progress that we're making through it to essentially hold them accountable, and get them focused on delivering an outcome, delivering some value at the end of the process. So I was really, really pleased with that, that we could share that lesson straight away.
Neal Ford:
So I think for me, the thing that changed the most in this Radar was the themes and how we came up with those was different. Because I think more than anything else, that's really the result of the bar, the restaurant, the breakfast and the lunchtime conversations. And I think we ended up at the same place we would have before. But I think we had to bootstrap the conversation almost from nothing when we started talking about themes and then get to a place, whereas normally that conversation organically bootstraps as soon as we, actually before the meeting starts because people bump into each other in the airport and it's like, hey, how are you? Like I said, I think we ended up at the same place, but I think it was much harder to do just because we didn't have all that face-to-face time.
Neal Ford:
And that makes sense because the themes really are meant to be the invisible things between all the blips. And of course we didn't have time to really speculate and ponder on all the things around the blips as much face-to-face because unlike regular meetings. And one of the ways this is vastly different, we would take a 20 or 30 minute break, where we would all disappear to our own homes, to our own coffee makers and rather than go to the boutique coffee maker down the street, that's just out of too far away, but if you walk fast with a conversation, you can get to it, which is more traditional than our meetings.
Neal Ford:
So that's when a lot of those conversations happen. So that to me I think was the toughest thing. And the thing I worry most about, like I say, I think we got to the same place. So how do you think this has changed this forever? What things do you think we're going to pull in when we start doing this face-to-face again, which I anticipate that we will at some point. What things we're going to bring with us that it's like, hey, we'd like that. I'd like to keep doing that or are we going to go back to face-to-face?
Mike Mason:
So unquestionably I think some of the digital tools that, particularly the live voting thing I think worked really, really well. I think it actually sped the process for us because there is a certain amount of counting, can you hold up your cards again? It introduces some friction and delay, that's actually just wasteful, it doesn't actually add anything to the meeting. So I think those tools would be really, really useful. It also gives us quick access to links and to read some of the background story and get some of the data, which is important for some of the smaller and the more interesting small tools which may be not everybody is familiar with, particularly in the tools quadrant. So I for one will be definitely wanting to keep some of that electronic tooling in the spreadsheet or whatever, other thing it evolves into over time.
Neal Ford:
I agree. So one comment about that. I agree wholeheartedly with that. It's really nice to see the realtime count and see it shift. But one of the things that's prevented us from doing this in the past is the convention that we've always adopted at the face-to-face meeting is everyone's laptop is closed so that you don't get distracted by shiny things when discussions are going on. And so there's definitely a trade off there between access to the fancy digital tools on your laptop and all the other shiny distracting things also on your laptop.
Zhamak Dehghani:
Yeah. And some tools or some approaches makes this a little bit more effective. I liked some of the async work that we did before coming to the Radar or having the blip that we had collected available to the larger group for people. We'll have time to do a bit of research or reading in advance and have a little bit more informed discussions. I liked that asynchronous that worked with it in advance. I know some people would hate me for saying this because that means more work. But if you have the time as an optional item, I would add it.
Evan Bottcher:
I think that that's definitely been the async nature. Being able to do some preparatory work is really quite difficult. If you look at the group of people in our team, they're all playing very senior technology leadership, either operational leadership or client facing consulting leadership roles in a very, very busy weeks. But the investment very clearly paid off in terms of being able to get a quicker understanding in the group of what the items were that we were discussing. And then what we can then focus on is adding the richness of the conversation around it and the experience that we've maybe had with these things globally or finding where it's been used in this particular approach or technique or the platform is being used across multiple regions. And in that lends the importance.
Evan Bottcher:
I think are the clients I work with who do build their own Radar, almost all of them are using some kind of async process in advance of any face-to-face meeting to gather some stuff. And I think that works really well. So hopefully we can keep an emphasis on that.
Mike Mason:
I think for me what's interesting is that we put the digital tooling together fairly quickly. And user experience was not exactly at the top of our list. It was very functional, but it was also you were appearing at a small screen trying to figure out which row of the spreadsheet you should click on. Everybody had a column for their votes so people could accidentally vote for each other's things or sorry, make a vote on behalf of someone else accidentally. There were a number of things in there where it's like, this is Lo Fi, it's a first attempt. I am actually really excited about working with some of the folks at Thoughtworks who really know how to design these kinds of user experiences and to get them to work with us on what a version two might look like.
Mike Mason:
Because I could imagine there are bits and pieces of this that we just want to bring into the in person meeting regardless. And maybe everybody has a little voting app on their phone with big buttons on it. And then it's getting lost on your laptop situation, but you can still do some of the voting. Maybe there's simple ways to also re-track who's doing the voting so you can't accidentally do somebody else's vote, all those kinds of things. And I also think there's potential here for us being more inclusive of people who couldn't make it to the meeting. So in the past, if you couldn't make it, basically, unfortunately you were out, whereas with this, I still think if we had 20 people in person and two people who were remote, I think it would be a significant disadvantage for those people who were remote. But I think they could still contribute if we were using some of this tooling.
Mike Mason:
So I'm excited about that kind of thing going forward, making it more accessible. I don't know what Evan's position is on this today. I'd be interested to find out, but I know in the past he has said, I'd rather stay up all night than sit on a plane for 24 hours to get somewhere. Evan, I don't dunno how you feel about the trade off. If you were given the option to stay home but do weird hours or travel and be jet lagged and effectively do weird hours, what would you pick?
Evan Bottcher:
I have got a couple of points here I think. I definitely felt that the meeting lacked some timber to me. The extra value, the extra stories that you bring home to share with Thoughtworkers and unanimously with clients and a lot of that happens in the gaps. A lot of that happens over dinner. A lot of that happens in the times where we definitely could not make time for, in fact, I felt like the meeting itself, we were also frightened that we wouldn't produce result, we actually accelerated through the material faster than we would have face-to-face. And so yeah, there's definitely I think the richness of the material to bring back from the meeting isn't there. And I think that not being face-to-face degrades a lot of that. So I would probably vote to travel given the value of what we get.
Evan Bottcher:
I also think we need to be very careful to make a distinction between fully remote where every member of the team is subject to the same disadvantage from satellite team members. I've dialed into things before as the one person whose time shifted to be in a meeting. And you really do, you miss out on a lot of the little bits of nuance and little bits of conversation, the coffee walks and so you get a six out of 10 experience compared to a 10 out of 10 experience for other people. That may be worth it but you need to really factor that in. And what we did was not the same as having a face-to-face meeting with satellite participants. So on net, I'm keen that we at least for one of the meetings a year perhaps have it face-to-face.
Neal Ford:
Leftover advice for anybody?
Mike Mason:
Well, I think everybody's being bombarded with advice about how to do remote stuff these days. So I would probably go and try and think about the best advice you're getting there. I think the major problem is that everybody's focused on the technology of remote collaboration and not of the human aspects. So I would advise everybody to think strongly about that. Who are the human beings that you're trying to connect with and what is their situation and how can you make it most accessible and fairest to everybody and try not to make assumptions about people's situations and connectivity and all of that stuff.
Mike Mason:
I think as time goes on maybe people will get better internet at home and fix their crummy home Wi-Fi and all the other problems that people have. But certainly in the short term, this kind of stuff you have to put up with and empathize with the person at the other end.
Zhamak Dehghani:
And I think be frugal with the technology we have and how much impact it can make. We had a spreadsheet and zoom, and we got quite creative about it and it took us a long way.
Neal Ford:
It did indeed. And it's enough to make you think, well, could we with enough tech really replicate that? But I think the experience for me are the two things you can't replicate. One, you can't do anything about time zones. So if you try and do something remote, it's always going to suck for somebody that's going to stay up all night, at least if we fly somewhere. It's formal and the sun's up and so it feels less like you're up all night. So that's a big deal. And the other is we're fundamentally social creatures. We pick up things from body language and doing meals. There's a richness of communication there that you cannot replicate no matter how good the technology is and I think we're just wired that way.
Neal Ford:
So I think there's still some value in face-to-face stuff that you can't get away from. But exactly to Evan's point, for people who can't make it, I think a six to 10 experience is better than a zero of 10 experience. So I think there's definitely accommodations we can make. And I think the tech helps a lot toward bridging that gap, toward making it from a six to an eight out of 10 or maybe even a nine out of 10 versus a 10 out of 10. So I think there's a good opportunity there for some innovation to happen. And there's a great forcing function in place right now to encourage that innovation to happen.
Zhamak Dehghani:
And technology is still quite a few years away from replicating hugs for huggers like me.
Neal Ford:
Indeed. So we hope you enjoy our Radar. We thought it could never happen remotely, and yet it did. And we're actually quite proud of the result and believe that it looks like all of our other Radars. And we hope you enjoy it as much as you have the previous ones. And maybe we'll do it face-to-face next time and maybe we won't, but stay tuned and we'll find out.
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