<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-we-put-together-technology-radar | Title: How we put together the Technology Radar | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  How we put together the Technology Radar 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford | Podcast guest  Marisa Hoenig , Perla Villareal and Camilla Crispim
April 06, 2023 | 35 min 55 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/how-we-put-together-technology-radar#Transcript)
Listen on these platforms
## Brief summary
The Thoughtworks Technology Radar is a snapshot of technologies and practices that the company believes the industry should be interested in, based on the actual experiences of Thoughtworkers working with clients. With its first edition launched in January 2010, it is now a fixture of the Thoughtworks calendar, released twice a year in the spring and fall. 
Although it has been around for more than a decade, we're well aware that people have lots of questions about it. One comes up more than others: how do you actually put it together? Giving a good, short answer is difficult — for those involved, it's a long process involving various stages of writing, debate and deliberation. However, with the next edition of the Radar — volume 28 — just weeks away, we wanted to give the world an insight into how we put Technology Radar together. 
In this episode of the Technology Podcast, Marisa Hoenig, Perla Villareal and Camilla Crispim join host Neal Ford to discuss the work that goes into producing it and what the experience is like.
## Episode transcript
**Neal Ford:** Hello everyone and welcome to the Thoughtworks Technology Podcast. My name is Neal Ford, I am one of your regular hosts, and we normally have a co-host, but we don't today because we have three guests all with a very particular unique perspective on our topic today. Today we're going a little bit meta and behind the scenes on the Thoughtworks Technology Radar, which if you're listening to this podcast, you are no doubt familiar with, if you're not, take a moment to go to thoughtworks.com/radar and you will see what it looks like.
What we're going to be talking about today is how that thing is created and talk to several of the people who have been very intensely involved in the creation, behind the scenes of this radar. I'll get them to introduce themselves and a little bit about themselves and where they fit within the era of the Thoughtworks radar. We'll start with you Marisa because you're the current TA and going to be present for the next radar.
**Marisa Hoenig:** Hi, my name is Marisa Hoenig, I am the current Technical Assistant for the CTO at Thoughtworks, which means I'm also the product owner for the Tech Radar. I started last year back in 2022. I've done one radar, our volume 27, and I'll be doing the next, I don't know, three or four or so. It's a really cool thing to be a part of from coordinating all the writing to the translations and copy edits and seeing it finally go live. I'm really excited to be here and to be in this role.
**Perla Villarreal:** Awesome. I'm Perla Villarreal, I'm a lead consultant at Thoughtworks. I was in Marisa's role as the Technical Assistant of the CTO and the product owner of the radar not too long ago, for about two [chuckles] and a half years. I joined in 2020 and stepped out late last year, late 2022 joining right at the epitome of the pandemic and all the changes that were coming with that and moving into a remote world. It was great, and I miss it already. Looking forward to the chat.
**Camilla Crispim:** Hi, I'm Camilla Crispim. I work at Thoughtworks Brazil. This end of the month is actually my 10-year investor here at Thoughtworks. I've done many roles but lately, I am the Technical Director for the nearshore market in Brazil. I'm also part of the TAB group who is responsible for creating the Tech Radar. I was Technical Assistant for the CTO back from 2016 to 2018. I have both sides of how we create the radar, let's say.
**Neal:** Yes, indeed. Camilla has the unique position of having sat in both seats of a content creator and also the TA role. All of these folks who have joined me today have played the role of assistant to Rebecca Parsons, who is our CTO. That's job is not only the radar, it's got a lot of stuff in it, but it includes the ownership and other aspects of the radar that Marisa was talking about. Let's talk a little bit about where this thing started.
The Technology Radar was a purely accidental artifact because Rebecca has this group, the Technology Advisory Board that gets together and advises her about technology. It's a well-named board since she is the CTO. One of the things that group started talking about were interested technologies that we were playing with or had seen at client sites. We thought it was really interesting that we were curating this list in the entire world because this group encompassed all the offices that we had and the very first visualization of radar as we mentioned, volume 28 is coming up, there have been 28, 27 of these up until now.
Volume one was actually created by another technical assistant Darren Smith who created it in Keynote because that was the best drawing tool that he had. It has evolved into a very, very complex process. Camilla is the earliest one in the creation process. She got handed over a process that it consisted of-- Thoughtworks used to make this project tracking tool called Mingle where a lot of the materials captured, but then it was-- Let's let Camilla describe some of the process that you inherited as a TA for creating a radar.
**Camilla:** Oh, my God. We used Mingle to track the progress of the writing. You have to import all the blips that actually got to the radar in that specific edition. There's a lot of export-import spreadsheets and a little bit of hacking as well. The first time that I saw that Anne Simmons was the former TA and was handing over the radar to me, she had this very step-by-step process very specific.
I was looking at it for the first time like, "Oh my God, I'm never going to be able to reproduce this [chuckles] I'm going to fail so much at helping this group build the radar." Turns out she was actually able to support me in the first radar that I was doing by myself. We had that for quite a while. The Mingle was the source of truth for the whole history of the blips that made to the radar. Then the TA Ni Wang, she was after my time, she actually was the one responsible for the transition because we were sunsetting Mingle, if I recall correctly. We had to find something else [chuckles] to help track the process.
**Neal:** Let's catch up on some terminology for those who may not be familiar, the blips. The way that this thing comes about is that the members of this group bring a lot of candidates to this meeting and those are known as blips. Then we go through in a very intense face-to-face session put in asterisks around the face-to-face part of that, we'll get back to that in just a second [chuckles] to discuss the things that should be there, the things that shouldn't, are they appropriate, et cetera.
What Camilla's talking about is the output of that intense face-to-face session, which has been captured. Then after that meeting, each person who has nominated one of those things has to write up the context that shows up on the radar, and then the TA has to take all the blips and all the content and the positioning, et cetera, and create some cohesive whole. Mingle was basically, as Camilla said, our source of truth. We're using it like we're using Git now, we're using GitHub repositories now to store that. It was Mingle plus some spreadsheets and a little bit of voodoo magic and some other stuff to transform all of these things from one part to another.
Then Camilla turned that over to me, and she was the first one who had to, at the last minute, accommodate the pandemic, which is in the early 2020s. Now, we had always claimed that it was absolutely impossible to do a radar if we couldn't gather face-to-face because it's such an intensely collaborative meeting. Then we were, of course, proved wrong by the global pandemic. Ni did some magic with a shared Google spreadsheet.
That's what we've been using to track the radar when we did it remotely. Let's let Perla talk a little bit about this spreadsheet that she suddenly inherited, which is one of the more complex spreadsheets I've ever seen. It gets updated by a global group of 25 people in real time constantly. Let's let her describe that a little bit.
**Perla:** Absolutely. That spreadsheet, I think I've had several different people reach out, interested in how the radar's put together or interested in creating their own mini radar. They always want to see the spreadsheet and I always know it's a mistake to show [chuckles] the spreadsheet. It's very intimidating, just the amount of information that it holds. I also think it's interesting how well the team works together to make that all-- That's all information that was being held in a lot of team members' heads throughout the whole conversation that we now have a space for.
This spreadsheet essentially is our documentation and momentary source of truth during the face-to-face meeting, virtual meeting, during the discussion meeting that this group has. Eventually, all of that is moved into a much more stable environment. It is a spreadsheet that really works through all of the proposed blips that we have across our many countries within Thoughtworks. I've seen a spreadsheet start with over 300 blips that are proposed and it's speaks to all the technology that people are interested in speaking to. It has descriptions of them, conflictive information about them as well.
One of the things that's most fascinating to see all of that in one space at once because with the spreadsheet, while we were remote, we spent a lot of time anticipating the discussion. We have all of this to go through, how do we make sure we prioritize the right conversations? It's always interesting to see that the spreadsheet really shows where we're having similar conversations across the world or very different conversations [chuckles] across the world about the same technologies.
The spreadsheet is a really interesting visual that I don't think we had previously. It's all I knew during my time as a technical assistant but there's so much value in that. It holds space for that conversation. A lot of times I also found myself going back to understanding that progression of information. We start with so many blips, we bring them down to a much smaller amount about 100 and sometimes we end up with blips that weren't even in that original listing. That transformation of information and decision-making, it really comes alive through that spreadsheet.
**Neal:** There are at least two super interesting things that you mentioned there. One of them was the visualization that we used live that we ended up recreating in the spreadsheet because one of the things that we learned early on in these meetings when you have such a group of people and they're all, of course, opinionated, you want to try to reach consensus as quickly as possible and Rebecca does a brilliant job of steering this group of unruly cats to get them and herd them in the right direction.
One of the things that we implemented early on was this system where everybody is issued when we're in person three index cards, a red one, a yellow one, and a green one. When a topic comes up, there'll be a broad vote which is, "What do you think about this?" Green means I agree, red means I disagree, and yellow means let's have a discussion about it.
That was recreated in the spreadsheet in a brilliant way because every person has a column and it has three values, which is red, green, or yellow. You can just flip those when topics come up and we've actually adopted that now for the in-person meetings because the visualization is so nice and we still use the cards for the visual effect. It's a really nice way of capturing something that started out very much as an in-person thing and moved into the real world or the virtual world, the anti-real world, or virtual world.
Camilla can probably say something about just the volume of information that gradually has been collected about this. It started literally as just a little bit of text and rings but now there's all this metadata and other stuff that has been captured in the various pieces of software. It's a little bit of a tribute to Mingle that it did what we are using three different pieces of software to do now because it used to manage a lot of this and now we're using GitHub and Trello and several other things to do the same work. What about the information we're gathering here?
**Camilla:** If I can be honest, now we are using the right tools to the write [chuckles] things. I don't think Mingle was [chuckles] actually the place to hold the blip history and all that stuff. It was very easy to get it wrong as well and Perla was talking about the virtual meeting, It was my first meeting as a TAB member. It was my first meeting as a third member and it was very impressive how the process, how we got to that point of so many fancy things.
By my time, I had and I was the first non-English native speaker who had the TA role. I had to write notes, record the decisions of, is this blip making it to the radar or not? I was so nervous because I was sitting by Rebecca's side that I was like, "Oh, my God, I'm going to get all this wrong." It's a lot of people. They speak very fast and the conversation flows, it can go very quickly. It was a challenge to me by that time. My English improved a little bit [chuckles] during this period but having all this right tools now it makes the process more verifiable, let's say.
It's easier to double-check things. It's not only like you and the Google Docs that you are literally trying to write every single word. You have a better way to track it. We are also, as folks who are going to write the blips later on, have something to go back to and say, "Okay, this is--" We call the conversations in a much easier way and get the context and write better blips and texts to the radar. Which I think it's very important.
**Neal:** It's even more doubly important because this is not just a recording of the events that you can take all the time you want to think about later. There has to be instantaneous results while we're all there face-to-face. One of the things that Rebecca tries to herd us toward is a reasonable number of blips on the eventual radar and so there's this real need to have pretty much real-time information about how many are there, how many are in each place, et cetera. That has been a real struggle because there have been so many manual pieces of the process.
That's something that the automation has gotten more and more impressive over time. It's such an intensely manual process and there's a lot of coordination, et cetera. It was always done in a formal handoff where two TAs would be at the same meeting so they could see all the processes, et cetera. Then we had the grand plans to do that for the handoff between Perla and Marisa but then this global pandemic thing sorted itself. Marisa got the interesting experience of getting to do it for the first time live without having an in-person handoff. Let's hear a little bit about what that was like.
[chuckling]
**Marisa:** I was lucky enough to get to do a face-to-face in-person in Barcelona back in October. That was really awesome and while, yes, Perla wasn't there in person. She was still whispering in my ear the whole time, she was chatting with me while things were going on. It felt like I had her there with me but it was a different experience because Perla had never gotten the chance to do the in-person one. I was going of what she knew of the radar, what I gathered from different resources and so a lot of it I was asking Rebecca, "How does this work? What do you do in this session? Should I be taking notes? What's going on?"
It's crazy, like Camilla was saying, how fast everyone talks and I have to sit there almost like a zombie, just typing notes and trying to remember who's speaking. I would look up and be like, "Oh, yes, that's Neal speaking, Neal." Then I'm typing exactly what you're saying just to keep a record of the conversation and you don't even know how crazy the radar is until you experience it.
I feel Perla kept telling me that. [chuckles] When we were onboarding, she was like, "Trust me, it's going to be rough," and I was like, "No, I feel good, everything's fine," and I was like, "Oh, my God, wow, this is intense." I feel a lot better about it now that I've done one even though she couldn't be there in person.
**Neal:** Perla, did you ever get to do a face-to-face one even when you got handed over from Ni, or was everything you did remote?
**Perla:** All of the radars I helped produce were remote first. There was one radar volume February of 2022 where we had smaller pods. I had the opportunity to work with a few folks in North America. We all met in New York City. We also had Scott come from Australia, which was great in terms of time zones, [chuckles] but otherwise, no, and even that face-to-face in person, we were really trying to be remote first, not make it feel like anyone is being left out.
My duties in person were very different than the ones Marisa had because I was chasing down monitors, making sure everyone had more than one monitor to feel comfortable in their space and making sure that we were still all up and ready at the office at 6:00 in the morning, which is usually not when the office is open. The logistics were very different for that, but for the most part, I was the remote only TA throughout the five radars that I helped produce.
**Neal:** It's an amazing bit of work to be able to create one of those things remote, and especially given that you basically did it all of your times remote, which is really tough. When we were face-to-face in February, there were still COVID protocols and a bunch of other circles. It was still February 2022 so it was the variants were very, very complicated.
The only person on our call that's actually sat on both sides of the table is Camilla, who was Rebecca's TA for a while and then spent some time working on projects, et cetera, and then has made it back onto the advisory group. What's the difference between those two? What's the perspective shift from one seat to the other?
**Camilla:** Oh, my God. I think the first difference is as a TAB member, like non-TA, you can actually sleep.
[chuckling]
**Camilla:** Because when you're the TA, it's very hard to sleep because you are always thinking about, is everything set up? Do I have everything right? I need to do the import to Mingle so tomorrow I can double check and see. Sometimes the Post-It will fall from the wall and all that.
I would have to go very early in the morning to double check and make sure everything was right. Also as the TA, I was desperate to get the recordings of which blips made to reach each place and the notes as well. My notes was pretty bad, but now, [chuckles] being the one who's going to write the blips, the notes are so important to get the context to reach out to the right people because during my time, I was like, "They're going to figure it out."
You don't have much time actually to think about, "Oh, my God, I got nothing from this discussion." It was such a consensus that we moved very, very quick, but now, I actually need the notes to write the blips. The pressure of having someone saying, "We have this many blips left, we have this many blips left." When I was that one couple years ago actually saying, "Oh, you're going to miss the opportunity to talk about this. Are you not going to write it? Are you going to sleep because we need this too? Is this done?
It's a shift but then, having both perspectives, you'll realize that every single part of the process and every single person, they are equally important in order to get the radar out so that's very cool.
**Neal:** I'll ask each of you in turn something that was unexpected when you started doing this or something that would surprise someone about the creation of the radar or something that people might not understand about it, et cetera. Some insight that you would get from your unique role. What about you, Marisa? You're the one who's done them the least so I'll pick on you first. [chuckles]
**Marisa:** Wow. I don't know if that sounds good or bad. [chuckles] I feel like one of the most surprising things, at least during the meeting, was just how fast we go through each blip, and so when thought workers around the globe are proposing blips and they have, I don't know, a two sentence paragraph or five sentence, whatever, the more information we get really helps the case by the TAB member to say, ''Actually, we should really put this in adopt, or we should put this in trial.''
If we don't have a lot of information, often it just gets shot down and it's done. Sometimes it's like, if you really want to blip on the radar, you should put a lot of evidence in there and explain how it got used, put the pros and cons of it. That will help have a better discussion and have a better chance of getting on the radar.
**Neal:** I think Perla and Camilla both alluded to that. I think that's one of the things that the remoteness has forced us to do is better preparation and a little more detail in those, whereas a little more seat of the pants in Camilla's day when everything was face-to-face and it's a little more formal now so that's actually one of the improvements. Perla, what unusual thing would you think about this role?
**Perla:** I don't know if unusual, but I think shortly after producing five radars with the TAB at Thoughtworks, I actually had the opportunity to also jump in and try to do this with a client. That's when, I think, in terms of insight, what really hit me is how important the community aspect that the TAB has, the respect they have for one another, the room for all voices, every voice on that group is loud, yet there is room for every single voice. The way Rebecca facilitates, it's magical.
I watched it for two and a half years and I still don't know how to put it in writing, what she does, but it's also, I think, the group and the respect they have for one another, for the work that they do, for the experiences that they have, and when you see the client opportunity that I had, it was a very-- A lot of the people hadn't interacted with each other before.
It was their first radar that they were trying to put forth and it's stepping stones. You really first want to make sure we can all talk about this, disagree about it, that's okay as well, and understand where those disagreements are coming from. I think that's what I walked away super impressed with and surprised by just how important, that seems like very minor thing, but I'm sure the in-person aspect helped a lot as that group has transitioned, but then there are also people who have been on this group for years and the way we talk internally and culture within Thoughtworks, I think also helps mitigate a lot of that.
Of course, the facilitation that comes from making sure we all have a room for conversation, we all get a vote. Sometimes it's a tight vote, sometimes we come back to it, we get second opportunities. I think that is the insight I would share to anyone trying to put a radar together for themselves or for their organizations. Make sure you build that community, that team of people who really want to work and grow together because that's what will make the reflection valuable.
**Neal:** I also have a theory exactly to your point, that part of why that group functions so well is because it is a group of fairly senior technologists and we are very used to pitching ideas that get shot down and not get mad about it when it happens because it happens so much and you're just happy when it actually gets accepted.
I think that actually helps because I've seen other groups within Thoughtworks struggle with some of the large group dynamics that group doesn't seem to struggle from. I attribute it to being mostly a group of technologists and being accustomed to disappointment. [chuckles]
**Camilla:** To your point, Neal, when I got home back from the face-to-face scene in Barcelona, I was actually sharing some thoughts around this. I pitched some blips and it was challenged and people were just pretty much saying it's a bad idea or this doesn't sound right but it was not personal. I didn't take it personally, and they were not intended to be something to me. It was to the idea. That was pretty clear in the conversation. I think it's not even that we are mature, it's just very respectful the way that we disagree as well. This is something unusual. You don't always get this [chuckles] in all places or discussions, especially about technology.
**Neal:** I think there's a strong desire to get it right, as right as we can as a group, and that overrides a lot of the other interpersonal stuff that might cloud judgment that may. That's just an aspirational goal if nothing else. Marisa, you're about to launch into the next radar. Any ideas you have for improvements or any behind-the-scenes stuff you're thinking about implementing for the next round?
**Marisa:** Very interesting question. I feel like we've had a lot of conversations recently about, can we add other features? Can we get other people involved? How can we really continue making it better? None of it is really confirmed yet. Nothing is really figured out, but on my side, I'm trying to just improve some of the processes that I have to go through.
As you heard from the other two, also, it's a crazy process. I feel like every day you're working a lot of hours just to make sure it gets through the door and it's as perfect as much as it can be and so I want to just make it easier on myself so I'm not so stressed out during that time so that's going to be fixing up some of those scripts that we have that move things between Trello and Google Docs and back to Trello and back to Google Docs and the whole process.
**Camilla:** The hacks are still there.
[chuckling]
**Marisa:** They're still scripts, [chuckles] trying to improve some of those before we jump into the next one.
**Neal:** I think it's a tribute to Rebecca's skill in choosing TAs that no TA has ever just taken the previous process as a cargo cult and decided not to touch it and just try to leave it as magic. They've always dug into it and figured out ways to improve it and it's markedly improved. Camilla can attest to that, the difference between the era that she was dealing with it and the era that we see now.
One last question for each of you. If you could give yourself, and Marisa can't really answer this one yet, at the end of your tenure as a TA, if you could have given yourself a piece of advice from the beginning of your tenure, what would that piece of advice be? For the thing that you unexpectedly learned during your time and that tenure usually lasts for about two and a half or three years per person. What do you think, Perla? Any advice you would give to your slightly younger self about that role?
**Perla:** Absolutely, and I gave Marisa this advice too, and I received it multiple times early on, but it's chaos, but I think it would be to take a moment to really take it in. Camilla was saying, when you're a TA you're really listening to everything, taking notes, double-checking, making sure the right decisions were made and documented. There are very just rich technical conversations that you're documenting. You're acting like a robot to some extent, early on, especially. I'll also say that too, Marisa, it gets easier, even without process changes, it gets easier. You start acting like a process yourself.
That's what I would say, really, you're amongst such rich conversation. You're amongst rich times. Technology continues to evolve drastically month by month, I would say, and we're having different conversations. That's part of the reason we try to get the radar out the door as soon as we can because these conversations continue to evolve.
What I would say is that I would tell myself to also, as you're documenting all these blips, I read them 20 times before they're published, but really taking in like what's there. I think now as I'm coming back into professional services, going back and understanding that the radar tells a story across volumes even during one set volume.
As you see all the information, take it in as an asset and take advantage of your experience as you're doing it and understanding your perspective. Like Neal said, there are different perspectives throughout the room and you're bringing one as well. That's what I would tell my younger self.
**Neal:** What about you, Camilla?
**Camilla:** I was going to say something similar that you as TA, even though you are in the operational side of it, you are a contributor as well. It took me some time to figure that out. Even when Rebecca invited me back to the group as a contributor, I was like, "Am I a contributor?" [chuckles] It looks like I am and I'm taking that place, that space, but I think that is also the networking that you do so take advantage of it.
There are a lot of luminaries from the industry in that room, in that group, getting to know them, their perspectives as well, them besides technology, which is also important, that's something important. It also took me some time to have the sense of belonging, I guess. It was like, "No, I'm just like this young lady here and they have my age of experience. They don't want to talk to me, but actually, you have more recent experience than they do in terms of hands-on project context. It's always an exchange of experiences and knowledge as well.
**Neal:** Fantastic. Thank you so much for your terrific insight and hope all of our listeners enjoyed getting a little behind-the-scenes, details behind how the radar is created, and you'll get to see the next one crafted by Marisa and a bunch of others coming up before too long. Thank you very much for joining us today on the podcast.
**Perla:** Thank you.
**Marisa:** Thank you for having us.
**Camilla:** Thank you.
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
## Find out what's happening at the frontiers of tech
[ Explore Technology Radar ](https://www.thoughtworks.com/en-th/radar)