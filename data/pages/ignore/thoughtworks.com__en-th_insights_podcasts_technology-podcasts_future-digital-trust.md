<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/future-digital-trust | Title: The future of digital trust | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The future of digital trust 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Zhamak Dehghani and Mike Mason | Podcast guest  Ken Adler and Shangqi Liu
November 27, 2020 | 49 min 17 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/future-digital-trust#transcript)
Listen on these platforms
## Brief summary
Establishing who someone is and how much they can be trusted is hard — even more so on the Internet. Here, our podcast team explores some new concepts in digital trust, such as decentralized identity, privacy protection and identity ownership.
**Podcast transcript**
Mike Mason:
Hello and welcome to the Thoughtworks Technology Podcast. My name is Mike Mason. I am one of your regular hosts and I'm here today with Zhamak, who is also one of your regular co-hosts. Hello Zhamak.
Zhamak Dehghani:
Hi Mike. Great to have another episode together.
Mike Mason:
Yeah, it is great. So today, we are going to be talking about trust and the challenges of establishing trust between things and entities and people, especially on the internet. With the current design of the internet, we're going to be talking about various initiatives and efforts that are in place to progress how we deal with trust. Today, we've got two guests on the podcast. I'm going to ask them each to introduce themselves briefly here. So we've got Ken Adler. Hello Ken?
Ken Adler:
Hey there. How's it going? I'm Ken. I've been working on the OpenNet and then later the internet since the late '80s and I've been involved with identity-related technologies pretty much that whole time. I ran a publicly signed PKI in the early 2000's which got me all ready to read Satoshi’s white paper in 2009. And I have been a CISO in a previous life. I joined Thoughtworks about four years ago with the DPS group, where I was the security pillar owner of DPS. And over time, just because of how Thoughtworks and our clients and the needs, I've increasingly been focused on identity and the related authorization type of engagements. And I am an early member of the Trust over IP Foundation, where I serve both on the enterprise and the patient ID ecosystem task force.
Mike Mason:
Awesome. Thank you, Ken. And we will be getting to some of those topics in much more detail. We're also joined by Shangqi Liu. Shangqi, do you want to introduce yourself, as well?
Shangqi Liu:
Hi everyone. I'm Shangqi from China. Currently, I'm the head of Blockchain at Thoughtworks China. And also, I pair with Mike and Zhamak working in the Thoughtworks group creating those off the radar. I think there's been quite a big trend on the digital identity recently. So also, my work has a lot of engagement in into that. So I'm so glad to be here to share some thoughts and experience around this decentralized identity.
Mike Mason:
And although I kicked off the podcast today, I would say I'm the least knowledgeable person on the podcast. So I'll be asking, hopefully not too dumb, but entry level questions when everybody else gets a bit too technical here. So Zhamak, why don't I hand over to you to kind of introduce the topic and kick off.
Zhamak Dehghani:
Sure. We could start in so many different places. I think it's such a rich domain. But I wanted to kind of go a little bit further kind of backed away from technology, maybe start at a more philosophical place as, what is trust and how do we trust each other, at least in this scope of digital world, right? On internet. How as people or users of services with trust services, how the services trust us and reflect on that a little bit and how we've established it. Because, as Shangqi you've mentioned, we are at such a pivotal moment to redefine some of those fundamental assumptions that we have made about establishing trust.
Zhamak Dehghani:
And to be honest, I think the internet is a little bit broken when it comes to trust protocols and approaches. If you think about it, the way we establish trust is protecting a bunch of person we identify of attributes behind a password and trusting that those personally identifiable information that I share with service providers to prove who I am, I'm not sure I'm uniquely the only person I know, that information has been breached probably multiple times. And a lot of people know about my, I am assuming, about my social security number and so on. So, assuming identity based on a password protect, that set of attributes, that identity controlled by central or a federated set of services, I think it's rather flawed and should be challenged.
Zhamak Dehghani:
So maybe we start with a little bit of definition of kind of trust. What do we mean by, a service trusting a user, or a user trusting a service. What does that mean to each of us?
Ken Adler:
Trust is really, it's both an emotional and a logical act. And trust is the belief in the truth, the reliability and the ability of others. And belief, we get really philosophical about this. What is the definition of belief, and it can be confidence based on something, it can be faith, and it can be just hope. So again, it's really the belief in the truth and the reliability and the strength and the ability of others. And I think, in sort of this scope that we're talking about, it's helpful to think about trust outcomes. What is it that we're chasing here, and I think if you take it at the highest level, to be a bit mercantile with it, trusted eCommerce interactions. And underneath that, you sort of have trusted ecosystems. And then underneath that, each individual organization, within the ecosystem, you want to believe that there's a trusted governance structure, something that you can trust, you can look at, that one way or the other, you have defined this trust in this other organization, hopefully as a logical act. But certainly a lot of trusts, especially these days is more on an emotional level of brand trust, things like that.
Shangqi Liu:
Yeah, I remember, there's a book called the Liars and Outliers, it's quite famous in the information security space. And it's interesting, because it’s Chinese, translated into the title is, our trust. So basically, that's a book talk about trust. It discuss different angles around the trust, like how do you steal trust from the social perspective, from the moral perspective, the reputation perspective, and then the system and mechanism perspective. But all of this is not as simple. Yearly, technology is the way we are really trying to establish trust with certain set of technologies to do that. But the answer is not that simple.
Shangqi Liu:
Yearly we see trust is more than a simple mechanism. We need more collaboration. So we need to consider different parties, different roles in your ecosystem. And based on this assumption, to do our assess on the trust. That's my understanding on the trust.
Zhamak Dehghani:
Yeah. One of the, I guess, find definitions of trust that I found, it's very hard to actually define it, is from this author, Rachel Botsman that does a lot of work on trust, and who you can trust, using one of her books. And she says, "Trust quite simply is confident relationship to the unknown, establishing relationship transaction with uncertainty." And the way I think we have traditionally try to, I guess, get established that relationship with unknown is by turning that unknown to known by defining this concept of digital identity, right? Authentication is such a foundational pillar in any transaction we do, is that you say, you are who you say you are.
Zhamak Dehghani:
So if we pick then identity as a way of, kind of making the unknown a little bit more known, I like to kind of walk down, the historical landscape of how we have defined identity or digital identity traditionally, and perhaps what your thoughts are, where it's broken, and how we can address some of the gaps or the broken bits. And Ken you've been around this topic for a long time. And you can maybe bring some of that historical perspective for us.
Ken Adler:
So first identity, let's define identity, right? So identity in the biggest scope is really sort of the oneness of a person, right? It's everything that the person conceives and union belief is that there's sort of two aspects to your identity. There's a sort of the inwardly focusing identity anima, and then there is the outward focus aspects of identity persona. And as we know, what we're talking about here is really about the persona, the way that you project yourself in different environments and contexts.
Ken Adler:
And historically, the identity and the trust tying them together, historically if you go way back, it's really very social based. And the mechanisms that you use to establish both the identity and the trust, are physical things. Your face, the way your face looks, for your identity, and for the trust the expressions that you may put out. And then over time, guess both your identity and your trust has changed to be more sort of institutional based, where, certainly trust you trust in the church, and somebody else is a member of the church, and so trust is done that way, and then you can get into identity politics and all of that-
Zhamak Dehghani:
You really went far back, Ken. You went from the face to church. Come forward, come to the digital world.
Ken Adler:
Absolutely. The digital world is really where you're relying much more on knowledge, where you're dealing with both physics and math. And what we're talking about today is really about programmable trust and programmable identity. And one of the things that's interesting about this, is that it does allow you to become less centralized. But I still might, I would caveat that you would, there's still a heavy institutionalized aspect of the crust and the identity there. As far as actual technologies, techniques, obviously there's a variety of things, when you're talking about the identity of a person or identity of a service. So username passwords, services, their certificates, certificate authorities, and in modern times, in more modern times, there's a heavy reliance on cryptography, to identify individuals and services and such like that.
Mike Mason:
So Ken, just as the outside guy here asking you a random question, I have no idea how you're going to answer this one. But I remember back in the day, you could get Unix systems to talk to other Unix systems using basically completely unencrypted protocols, where if you were able to open a port on this particular socket from your machine to another machine, it would trust you, because it had been told to do that. So I could log in over there as me because some network service somewhere was doing that. To me today, that seems hopelessly naive and it obviously is because we're now talking about all the crypto and stuff that was layered on. I'm curious, was that ever thought of as not hopelessly naive? Or all the unencrypted stuff that existed on internet version one, was there a notion that this is not going to be good enough?
Ken Adler:
Well, you know what they say, this is why we can't have nice things, there's a lot of jerks out there. And certainly there's a saying about the internet was built without an identity layer. And because really, the technologies really weren't there at the early days. And thank God it wasn't built with an identity layer that we didn't get stuck into something that was not ready for today. But now, we've got to right that wrong and build an identity layer.
Zhamak Dehghani:
Shangqi on the identity story, I wonder what your thoughts are on the advancing from kind of centralized way of establishing this identity to federated an application of that and where you see that that's going?
Shangqi Liu:
For me I think we have been in the age of federated identity, because previously I ran into issues when I had to create another one email address, trying to have siloed user accounts and to remember different password. I still think it's very hard to remember different passwords. And now, like federated identity, I can use my Gmail or WeChat ID in China to log in different systems. I think it's much better than others. However, I still feel like even I can use one logging account but my information still stay siloed in different commercial internet companies. I cannot easily extract my information and to do some information share. I just feel it’s hard with the current setup.
Zhamak Dehghani:
Yeah, I think just so many things are gaps that exist within, even with a federated way of establishing identity as in relying one identity holder to give access to that identity on my behalf, to a variety of services. Of course, that's removed a lot of friction but still, there are a lot of challenges. And one of those challenges, as you mentioned, is sharing information across the boundary trust boundaries, right? How do you know that now, this information that you've shared across this trust boundary with another organization, how that's going to be used, and consent management, and that whole category of not having visibility to the information that you've shared and how it's being used, and being able to not only, I guess, give consent, but also reveal consent in some situations.
Zhamak Dehghani:
What are the, and I know we're kind of building up to this decentralized identity story. And so self sovereign identity. But I want to pause here for a minute, on some of the kind of challenges that exists with federated or centralized identity.
Ken Adler:
Yeah. I agree with you. There's a number of challenges that we've had throughout this sort of whole progression from centralized identity where identities in a single database in the monolith to federated where we're getting a little bit better, to hopefully, the future of decentralized. But main problems on the first two is, first is the most obvious thing that there's an intermediary involved, there's an institution involved, and that institution can change the rules of the game on. And it can take away your access, can change how it uses that information, you give it to them, how they share it, how they sell it, or whatever. So you've got that issue, you've got an issue that ultimately, it's a scaling problem.
Ken Adler:
And it's not only a scaling problem, because it's not going to be as big as Google is, it's not going to cover every place, everybody. But it's also the more you get stuck into one and you as an individual, there's a switching problem. So, the cost to switching and giving up one becomes larger. The other thing is typically using the technologies that we use for centralized and federated, which is username passwords as your credentials, they're not independently verifiable. They're not cryptographically verifiable. And as you mentioned, there's other things like to use federated identity, of your verifier of your website, and you want to start using it. You already are using Google and Facebook, but now you want to use Amazon's. Now you've got to integrate and do Federation, with Amazon and there's a barrier to allow more players in there. And of course, it allows for tracking so that central entity can tell where you've been and all the different places that are requesting authentication.
Zhamak Dehghani:
Yeah, I think the last one I've been particularly annoyed. Recently, I think I've clicked on maybe one or two ads recently working from home, buying things to make myself happy and now internet is unreadable for me. Every page is just littered with related ads that on a different platform maybe on Instagram, I clicked on one ad and now they're all popping up on, I don't know my YouTube and I have to change my browser, like move to brave browser because I just can't read the internet anymore without seeing stretchy pants all over it.
Mike Mason:
Here's a question. You mentioned usernames and passwords, right? Password seem like a bit of a rubbish idea given that it's 2020. But what do we replace them with? What is the post password will look like?
Ken Adler:
I was going to say the same thing, great segue. It's all the stuff that we're talking about in the rest. So certainly there's been a long history of security professionals, screaming, kill the password. And basically in one form or another, a lot of it comes down to this asymmetric cryptography where you have two sides, two related keys. And as long as you protect your private key or whoever is in control of that private key is the assumed identity in this particular case.
Ken Adler:
So I always think, when we talk about decentralized, I think one of the existing technologies that we're familiar that sort of give a hint towards decentralized identity, I think about SSH access. People are very familiar with SSH, right? SSH into a Unix server, and you've put your public key up there in your Unix server, but their private key normally, or in the canonical case, you're generating yourself. And you're holding on to that. So that sort of hints at where we're going with this centralized identity.
Zhamak Dehghani:
I heard this interesting, kind of metric on passwords, it takes from Christopher Allen, who's the co author of TLS SSL, and he's a big advocate since 2016 and maybe before on self sovereign identity. He mentioned that if you have an 18 character password, which is probably a good secure password right now, it takes 25 dollars on Amazon to break it. So it's just that level of protection is just the bar is coming lower and lower, with more compute power.
Mike Mason:
Is that true, really?
﻿Zhamak Dehghani:
That's what I heard.
Mike Mason:
25 bucks for an 18 character password, wow that's incredible.
Zhamak Dehghani:
I have to double check, hopefully everything is coded before publishing this.
Ken Adler:
I think you can buy it if someone's gotten it already. If they fished it from you, you can buy it. I'm not quite sure of that study there.
Zhamak Dehghani:
Shangqi sorry, I interrupted you there. Take us there, we want to jump into decentralized identity and self sovereign identity. Tell us more.
Shangqi Liu:
Yeah. I think for most of us, the decentralized identity, we learn this could be adopted first from the crypto space and if you see, like Bitcoin, easier the recruiter of currencies people regard their simple wallet address or public key, in some format of public key as their identity. That's interesting because that's quite different from how people usually looks like identity. People think of identity as some profile in my Facebook with some information, but actually all you need is a unique ID that could identify yourself, plus a lot of other profile information like you can make this ID as your Bitcoin address and to transfer money in.
Shangqi Liu:
The key difference I would say, between the centralized identity and the decentralized identities is the wallet address is purely generated a bios. So like Tencent, you could generate your private key locally without connecting to the network, without connecting to any commercial internet company. You can even try to use your brain trying to figure out one, two, five, six lines of numbers to calculate your private key. That's quite a powerful thing. That means you don't need any sort of hideout circuitry to generate your identity. You only need some mechanism of mass to do such. I think that's quite a disruption to people's mind that you actually could own your own identity without third party.
Zhamak Dehghani:
Interesting. You used the language ‘own’ there. One of the things, I really like that now that you as an organization, or as an entity, as a person, you control the generation of that identity and you're not at the mercy of some other organization, whether tomorrow you will have that identity or not. But there is a warning around the language of ownership as identity becomes a property, and if you're a property, then you're subjected to kind of a state, federal, whatever property management. So there's a little bit of a warning around, kind of using the ownership. But I do completely agree that's one of the foundational principles of this essentialize identities that is under your control.
Mike Mason:
But then surely the trade off, like on blockchain, the point of it was to enable decentralized, not under government control, exchange of funds. And if all I'm doing is generating a key pair, and my public key becomes my wallet address, that's great if all I'm trying to do is store funds in there. But if we then say that's my identity, it doesn't mean anything, because I just made it up. And I could have 10 of them. So where does the identifying portion start to actually come in?
Zhamak Dehghani:
That's a really good point. I think that's a good segue to maybe talk about kind of this different layers of this protocol, that together all of those layers considered together, would give you that sense of identity or sense of verifiable attributes or characteristics that as a person or organization you have. Just on the definition, maybe just pause for a minute as the definition of, I've googled this before, so for disclaimer, the definition of a decentralized identity from Drummond Reed, who Ken Adler knows, the founder of Sovereign and big evangelists, I guess in this space, is lifetime, portable identity for any person, organization or thing that does not depend on any centralized authority, and can never be taken away. So I think that's just kind of sums up what decentralized identity is. And if the readers or listeners haven't read Christopher Allen's 10 principles of self-sovereign identity, you should go and read it. It's just beautifully put 10 principles to just define what this thing is, and why.
Zhamak Dehghani:
And then I think that now that the question is, how does this generated long number digit character thing would actually turn into representation of me as a person or organization? Ken, do you want to have a go at that?
Ken Adler:
So I think there's a couple things here. Maybe one way to think about it is let's just zoom out a little bit. So first thing is that, yes you're going to, let's start with connections. So first thing to understand is that in this scenario, when you're talking about self sovereign, decentralized identifiers, there's a lot of peer-to-peer stuff going on. So first of all, the DID itself is not a public key, per se. In fact, the DID standard doesn't even say how you generate that key. But the thing is that, it is globally unique, and that it's associated with a dead document, which contains the metadata. And they don't say where you got to put the document, there's a couple different ways you can do it. But generally, you don't try to put it on the blockchain or on the public ledger.
Ken Adler:
So the relationships between me and you, for example, or there's four of us on this call, so there's three other people, the idea that I use for my communication with you and Mike is going to be a different did than I use with my connection with Zhamak and with Shangqi as well. So as an individual, you don't have just one digital identifier. You have large numbers of them, many of them and they're pairwise and your keys and your public keys, all of that stuff is off chain. It's not on any kind of blockchain or public place or semi public place where people can see it. The only things that goes on the public chain are the identifiers of an issuer of a credential. With someone that is like the government that wants to issue your driver's license using this stuff, has something that other people have to verify that this person, that this organization is who they say they are.
Ken Adler:
So you zoom a little bit more in and you say, Well, what do I need with decentralized identity? I need protocols for the secure connection, how do I establish these secure connections between me and Mike? And then I want to exchange data over that connection. And so I need some protocols and some standards around sort of watermarking that data, so that data can also be verified cryptographically, that I was really the person that actually sent that, this data to you, and that it wasn't messed around in transit. So you need these protocols around the data itself. And then if you want it to be useful outside of just you two, and especially you're using public issuers, you want to have some kind of public key registry, or public registry, which we typically talk about as being either blockchain or some other distributed ledger technology, or it could be other things. It could be other peer-to-peer kind of networks.
Ken Adler:
But the trick is that, it shouldn't be a central identity, anybody who's commissioned on to that should be able to verify things independent of a centralized identity. So maybe that's a good first shot at it.
Zhamak Dehghani:
Yeah, and maybe to just put that in context, Shengsi, I know you guys are working on a digital wallet implementation. I know COVID was a big driver for establishing some of this infrastructure, do you want to share maybe some of the work that you're doing to put this kind of stack of technology that gives us this decentralized identifier and a set of attributes that can be verified about us into context?
Shangqi Liu:
Yeah, for sure. Actually, recently we are working on the digital wallet, which is one of the key features is decentralized identity. We are following up very famous initiative, which is the COVID-19 credentialing initiative in this space, trying to use decentralized, I would say now decentralized identity, but the verifiable credential is very important part of the decentralized identity. Using the verifiable credential to provide a format of health certificate for normal people or for healthy people, because in China, you go everywhere, you'll need to provide your certificate to prove that you are healthy, you're safe. Otherwise, you cannot go to a shopping mall, you cannot go to your office.
Shangqi Liu:
So currently, we're still using a very traditional technology trying to extract data from your service provider and to extract your traffic information to know you haven't been to the dangerous area or like the dangerous area that has a lot of COVID patients. So it's important to provide such kind of claim to prove that you are safe, you will not infected anyone else. However, we need a better way, which could build up a better privacy if you wanted to leak less personal information. I think verifiable credential is such a technique. So basically, it is established on decentralized identity. And like for individuals, you could have your own identity. But also you'll need the collaboration of some health authorization like CDC, which can give you the claim you'll need to request the third parties help to issue you a claim in a format of verifiable credential.
Shangqi Liu:
This verifiable credential is a digital format with certain fields and there are ways to do the cryptographic verification. Third party could verify that this credential is signed by the Health Care Center and this verifiable credential could be transferred And installed at your mobile wallets, basically, you can carry it everywhere. So from now we have these different solutions of digital certificates, but none of them can be verified cryptographically cause basically, they are just a digital paper, you still need to link back to your authorities to do the check. By the way, this verifiable credential actually, we can just use the, like the authorities public key to do the verification, to verify if this certificate is still valid.
Shangqi Liu:
And another amazing thing about this verifiable credential is that it allows you to leak the least information that you require. Like if I want to prove I'm healthy, all I need to prove is I'm healthy, I haven't been to the dangerous area, dangerous place. But I don't need to provide every place that I've been to, which is a I believe is a covenant status. So I think the verifiable credential could help to leak the least information that that we need.
Zhamak Dehghani:
Interesting. If I summarize, it looks like we're moving away from establishing trust by providing a whole lot of information overly unnecessarily maybe, and then protect those with password and really move back to the physical world, right? We have a wallet, I have a wallet, and I carry my driver's license, and maybe the certificate that I've done the tests. And I know my bank cards, there's a whole lot of certificates that are claimed about myself that I carry my wallet today. And we're talking about the super wallet now that carries that, and a whole other set of certificates that I have been given by issuers or institutes. But the fun part about is that, in different places, like I go to a mall, and they need to verify that I am healthy and I'm trustworthy and I don't have COVID, and I didn't go to dangerous places, I can only provide the bits of information that is relevant to that verification and not more.
Zhamak Dehghani:
So it's a privacy respecting way of kind of sharing information by cryptographically, verifying that the actual issuer that gave me, there is a trust with that issuer. That's kind of like a super wallet that I now carry all of that information in.
Shangqi Liu:
Yeah, exactly. I think when it comes to the trust, we do not need to exchange error data, we just need to exchange the information, we need to prove that we are trustable.
Zhamak Dehghani:
Which makes me wonder, so what is missing to have this really as a widespread implementation and get that widespread adoption. I love this kind of idea of narrow waist of internet or narrow waist of protocols, right? This hourglass kind of shape of technologies. We're in the middle of the hourglass and narrow waist, you have technologies that are enablers, right? IP was there and on top of it like TCP and an HTTP and all of these applications and maybe today's like the HTTP in that narrow waist on top of it, having that kind of standard, you can build so many tools and applications on top and so many technologies to support it.
Zhamak Dehghani:
I wonder what is in that narrow waist of new trust stack that would enable the wider adoption of verifiable credentials and digital wallets as a way of establishing trust?
Ken Adler:
Well, I think you can look at it, sort of in two stacks here. First of all, there is the technology stack, and that is emerging now. Man, it's sort of like the early days of the internet when, yes, there were a number of standards or standards were coming out. But there's a lot of proprietary stuff floating around stuff that hasn't become standard yet. So therefore, it's proprietary or non standard. So there is a lot of motion in the industry. However, having said that, if you wanted to get something and up and running and demonstrating, you could do it today with the standards and they semi standards and other hacks that are around to demonstrate the thing and that's going to continue to progress over time.
Ken Adler:
I think the interesting thing is that at the end of the day, it's not just about the machines. It's not just about cryptographic trust, but there's this human trust aspect of it. That Shangqi was talking about, also about, hey you trust the government, the health care providers stamp that, hey, you passed your test and stuff like that. So there's a whole bunch of governance that has to take place and has to be widespread and accepted in order for these different ecosystems to be created. And that's one of the exciting things around the trust over IP foundation. Is that the trust over IP Foundation, which is highly associated with a number of the other sort of main organizations, and we can talk about the, do a quick rundown of the different organizations involved in this industry.
Ken Adler:
But the trust over IP Foundation has a dual stack, they have a technical stack, and they have a governance stack. And the stacks are divided in four layers. And it's very nice, just like the IP stack is in four layers, it allows you to swap things in and out that each layer. But generally speaking at the first two layers of the stack, you're dealing with cryptographic trust, and to higher level, you're dealing with human trust. So one interesting analogy I heard was the analogy of roads, cars, passengers and cities, I thought that was a really neat analogy. So the roads is layer one, and there's regulations about how the roads are constructed, or how the railroads are constructed. And so that would be your public utilities, and all the regulation, not regulation, but if you wanted to belong in this ecosystem that you would follow, you would use an Indie blockchain, or you would use an Ethereum blockchain or whatever.
Ken Adler:
Then the next one up would be the cars. And as you can imagine, there's a whole bunch of regulations around car manufacturers, the safety, regulations, and in different places, those things are different. So, somehow you'll need governance, if you want to perform or want to interact within an ecosystem of people, you'll need to make sure that you're using the right cars. And then you go up higher, and you think about the passengers. Here's what the analogy is a little bit thin, but I guess, to me it would be like, okay, you don't drink on this subway. So there's regulations around how the passengers and then finally, at the highest level is your city's right? Is how, is your city regulated?
Ken Adler:
So this environment, you're dealing with your public utilities, sort of your server to server, your DID. The third level would be around your VCs and how you encode your data, what kind of schema you use within your VCs, your verifiable credentials. And the highest level is sort of the ecosystem governance of, if you want to belong to the local ecosystem put together by the local Chamber of Commerce, that you agree to behave in certain ways, all up and down the stack. So maybe that's helpful. So the short answer is the governance. Integrating both the human trust and the machine trust to me, in a unified governance stack is pretty interesting.
Zhamak Dehghani:
You're probably one of the very unique individuals that would consider governance, interesting and exciting, but I can't imagine how necessary it is in this space.
Ken Adler:
With emphasis on necessity. As opposed to necessarily interesting.
Mike Mason:
Okay, well I think we are running towards the end of time on the podcast. What I will ask, first of all, where can people go to find out more about this stuff, if they're interested?
Ken Adler:
Well, the way I look at the organizations, there's a whole bunch of different organizations involved, so let me try it this way. So if you're for just community around identity and where ideas sort of bubble up and come, there's a great thing called the internet identity workshop IIW, it's been going on for 15 years. That's where OpenID connect came from, and a lot of this stuff came from their self sovereign. So IIW, there is around technical specifications, there is the decentralized identity foundation DIF, and so those are working groups coming up with specifications. And then generally speaking, those specifications, then to become standards, they push it through the, they go to the W3C. So there's standards in W3C, there's the verifiable credential standard already out, and the DID, soon to be out through W3C.
Ken Adler:
If you're interested in actual software, open source software, and implementations around here, a really good place to go hang out is hyper ledger, which is with the Linux Foundation, and they have a variety of software there. And if you're looking for a public utility, that's out there that you can connect into a network that you can connect in and start using today. There's the Sovereign Foundation and the Sovereign Network. And the last place are reserved for really being the first place, the trust over IP Foundation. I found that a very useful place to get a hold on it, because again, on the technical side, the trust over IP foundation doesn't try to create new tech, it really is an accumulator, and a curator of technology coming from all of these other entities and others, including the IETF and so on.
Ken Adler:
Plus, that's where all, even though there's governance activities happening in different places, like in sovereign and DIF, but really where the winds in the sail around establishing governance frameworks and templates for them, that people can go off and create their own governance frameworks around, that's trust over IP. So those are sort of the main places that are, there's a lot of information around this topic.
Zhamak Dehghani:
Shangqi, if I understand correctly, I think your team, the blockchain group in China has put a fair bit of open source software out there as well. Is there anything that worth for folks to look at?
Shangqi Liu:
Yeah, recently we just released our mobile wallet, which is called the T Wallet, shortfall servers as well as trustworthy. And we do follow the W3C DID standard, as Ken mentioned. So basically, there's a bunch of things here. And another thing I think I need to point out is that, recently in our tech radar, we have blips that mention decentralized identity, trust over IP, and we gave out a reference. So for anyone that hasn’t subscribed to the Technology Radar, please go to see the radar.
Mike Mason:
Okay, awesome. Well, I'd like to thank very much, my co-host Zhamak for having all the actual information here because I just asked some questions. And to Ken and to Shangqi for being on the podcast today. Thank you.
Zhamak Dehghani:
Thanks everyone, it was wonderful.
Ken Adler:
Thank you.
Rebecca Parsons:
And on the next episode of the Thoughtworks Technology Podcast, Neal Ford and I will be joined by Stuart Holloway, who is very active in the Clojure ecosystem, is a member of CogniTech, which was recently acquired by NewBank and we'll be talking with a story about the state of the Clojure ecosystem, how the languages evolved and some interesting developments in that ecosystem. So please join Neal and I next time on the Thoughtworks Technology Podcast.
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