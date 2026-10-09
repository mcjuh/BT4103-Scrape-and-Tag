<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/tinyml-bringing-machine-learning-to-the-edge | Title: TinyML: Bringing machine learning to the edge | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  TinyML: Bringing machine learning to the edge 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Scott Shaw and Rebecca Parsons  | Podcast guest  Andy Nolan and Matt Kelcey
May 04, 2023 | 45 min 45 sec 
[Read Transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/tinyml-bringing-machine-learning-to-the-edge#Transcript)
Listen on these platforms
## Brief summary
When we think about machine learning today we often think in terms of immense scale — large language models that require huge amounts of computational power, for example. But one of the most interesting innovations in machine learning right now is actually happening on a really small scale. 
Thanks to TinyML, models can now be run on small devices at the edge of a network. This has significant implications for the future of many different fields, from automated vehicles to security and privacy. 
In this episode of the Technology Podcast, hosts Scott Shaw and Rebecca Parsons are joined by Andy Nolan, Director of Emerging Technology at Thoughtworks Australia, and Matt Kelcey of Edge Impulse, to discuss what TinyML means for our understanding of machine learning as a discipline and how it could help drive innovation in the years to come. 
## Episode transcript
**Scott Shaw:** Welcome everybody. My name is Scott Shaw. I'm one of the hosts of the Thoughtworks Technology podcast here. The topic today is going to be TinyML. We'll find out what that is in a second. There are three other people here that would like to introduce themselves. Rebecca, do you want to go first?
**Rebecca Parsons:** Sure. This is Rebecca Parsons. I'm another one of the recurring hosts for the Thoughtworks Technology podcast, and I'm here to be the peanut gallery. [chuckles] Andy, do you want to go next?
**Andy Nolan:** Yes, I'll go next. I'm Andy Nolan, Director of Emerging Technologies at Thoughtworks, Australia. I'm really excited to talk about TinyML today. Matt, would you like to go next?
**Matt:** Yes. Hello. My name is Matt. I'm a software engineer, machine learning person at a TinyML startup called Edge Impulse. Long-term ML person, and more recently focused on the smallest of small ML.
**Scott:** Matt, you used to work with us at Thoughtworks. We were sorry to lose him, but we're also excited about his new venture. Before that, he was at Google, doing some of the work there that's gotten somewhere now. Let's start out with some definitions. Andy, you're the first person that brought this to my awareness, I guess. I wonder if you could give us a bit of an overview of what are we talking about with TinyML?
**Andy:** Yes, for sure. TinyML, the name says a lot. It's a very small version of what we typically know as machine learning. It focuses on deploying models to sometimes the smallest device as possible. Think microcontrollers, Raspberry Pis, those types of devices. It does have its constraints around what you can do with it, but it also has a whole bunch of opportunities that opens up.
Because it does run on small devices, means it can often be battery-powered devices, latency is a lot lower because the data source and the model are really close together. It also gives us the ability to scale these things into places where we probably don't typically consider locations for machine learning. Because of their disconnected nature, we could deploy them into harsh environments at the top of a mountain or at the bottom of the ocean. They don't need that connection with the cloud compute to actually do the inference around the model.
**Scott:** Is that the only place when we don't have access to cloud computing? Even in the presence of cloud, is there still a place for the small devices?
**Andy:** Yes, absolutely. I think if we think about our cars or even our phones as devices that merge the worlds between cloud compute and edge compute. Often when you're using your phone, there'll be many models running to do face recognition on photos or even voice detection and things like that. As an end user, you don't actually know where that model's running. Sometimes you don't even really care where that model's running. As long as you're getting that user experience.
We are seeing more and more developers embedding machine learning into the edge compute component of their software systems and enhancing the user experience like you would on your phone or something like that. We're also seeing it deployed into cars. We can think about a car as a software-defined vehicle that has a whole collection of sensors running. Ideally, the compute would be happening as close as possible to where the data's occurring just because you don't want latency in a car. However, there's other attributes within a car sometimes around the user experience that could occur in the cloud. The navigation and these types of things could be occurring in both of those locations.
As an end user, you don't really mind where that's happening as long as you're getting the best of both worlds.
**Matt:** A lot of privacy-related stuff as well there. There's no reason why you can't use something very tiny to basically protect the user's core data and just basically ship up the minimum requirement to do something useful. Even if you are the aggressive person on the other side capturing the data, you can't reverse engineer any other information about the person, so that's a big one.
Many times they do exist next to each other in what we call cascades where you've got some first model whose only responsibility really is to very cheaply and quickly decide whether it needs to "wake up" a later model somewhere where it might be on a bigger device or it might be all the way to the cloud. You see that with a text transcription or wake words on a phone.
They often have three pieces. There's a tiny super low-power chip in a phone whose only job it is to decide whether the last bit of audio sounds like something that might be worth waking the CPU up. Then the CPU might go, "Oh, actually that's a bit hard, oh, I might send that one off to the cloud because I need to cascade it along." Often, it's not just about one or the other, it's about how these things decide to poke the next one down the chain.
**Rebecca:** That was going to be one of my questions as well. How cooperative are these various models both in the cascade that you're talking about as well as potentially across peers. Is that something that we're starting to see more where maybe you've got a lot of sensors and they're sharing data with their nearest neighbors or something so that everybody's got a sense of the neighborhood? Is that so something that occurs in this as well?
**Matt:** Yes, absolutely. In industry there's cases. They're pretty rare a lot of the times, especially because it's early nascent fieldwork. We can get a lot of really low-hanging fruit with just this dumb sensor that's sitting on one device and doing something useful. In those cases, it's like the absolute nightmare in terms of cloud scenario because you expect this device to be burnt into something that's read-only. It's going to be attached to this big vibrating, greasy machine for the next five years and you're never going to see it again.
It's the exact opposite of what you might get with the cloud. Totally, there's this idea about mesh-related network stuff. The analogies with networks is very common. You can think about these machine learning models as only being really responsible for packaging up some really high-frequency data that might be coming along in a useful form to then add to the mesh.
It really starts to blur the lines about what these things are really responsible for. Because when you've got something that is now working with bigger models down the chain, or it's working with peers that are sometimes nearby, whatever that means, it's no longer this really simple input in, prediction out. It can be very flexible with what these things are aiming to do. The constraints are often around things that Andy alluded to that are really unusual and they're not really something that a web dev or someone who's a classic MLOps engineer is really thinking about.
It's, how much does it cost in terms of power usage to access this bit of memory? I would've never thought about that with a big fat GPU that's burning my house down effectively, but this starts to become really important. Again, it's that cadence of the deployment cycle. All the things that we know about MLOps that have really taken off in the last five years are almost completely relevant when it comes to the idea that you're going to be deploying this thing and it's a one-shot. It's really interesting to see how do you carry the lessons learned about building models when they're so differently in terms of how you actually operate them.
**Scott:** Are there different kinds of models? Are they the same models that you would use in a large system or do you have to constrain them in some way?
**Matt:** Constrained is the underlying word there. It's a funny thing about neural networks particularly that their biggest win, their biggest win in terms of the class of models they represent is they have this free parameter idea where you can scale a model independently to what the input or what the output is. This has been the growth of neural-- the success of neural networks over the last 20 years has been around let's make really big data sets and we can scale the networks accordingly even though we're not changing what we put in and out.
That works the other way too in terms of edge stuff. It touches on one of the reasons why I left very, very large computing because of neural networks, it's because we were building models that were just so big. It was becoming vulgar displays of power on how many GPUs you could throw at it. I feel like a lot of the art and the beautifulness of building these things was lost. I know that sounds a bit ridiculous artistic, but anyway. The other flip side now is how small can you make them? These models are tiny and it's that constraint idea. How do you now take away from the types of models we've built these days? How do you strip them back to their core based on these constraints to make them useful?
There's lots and lots of things to do around the ways we approach this, and a lot of still low-hanging fruit. It's very early days for this field.
**Scott:** I love that we can talk about the aesthetics of our technical solution on here. I think about that as well. I tend to think of, and you alluded to this, of machine learning as requiring massive amounts of data, not something like that one individual could even collect and train for a specific application. Is that the case? Where do you get all the data to train these real-world devices?
**Matt:** There's a really old rule of thumb that is all rule of thumbs a little bit wrong in that, if you have a neural network that has 10 parameters, then you need 10 training instances. This is something that's been in my head since day one. It's never one-to-one, but it talks about the fact that as you make models bigger, you have to make data sets bigger.
If you go the other way and you got a really small model, you can argue then, "Oh, I don't need much data." It really then starts to talk about what is the complexity of the question you are now asking of the model. If you have this some huge complicated vision model that you know is doing really fine discrimination between breeds of dogs, whatever, then it's fair to not really expect that to do terribly well on a TinyML model, whether model is a millionth of the size of a big one, but that doesn't mean that you can't frame your problem as something that is very, very, very simple, in which case it doesn't need much data.
Say, for example, day or night detector or something, something that's really, really simple that could work on a very low-resolution image. We can build something that is useful. It's a lot around the times about the scaling of this class of problems. Now, the other thing that's really interesting is when you talk about data for feeding a supervised model, we often think about--
Say I'm doing image classification, my data is a bunch of images and a bunch of labels for that. The TinyML has an interesting scenario that we as siblings of these tiny models are these absolutely enormous models that have already been pre-trained. When we talk about supervision and ingredient dissent for building these models, it doesn't have to be the raw inputs and outputs.
It can be what other models think about these things. There's a whole class of these ways of training we call distillation, where the input to the TinyML training isn't data sets. It's what this other big model think about things. That's really interesting because, if you are building one of these models out and you're trying to build some pipeline about how you train these models, you often have the use of other models as the primary source of input data.
The point I'm getting to is if you've trained a huge model or someone else has trained a big model for you, like ImageNet, which has hundreds of millions of examples, and you have access to a model, which we certainly do now, you don't need as much data anymore because you're using this big model as a bootstrap to direct the small model in the right direction.
You can get quite a way. In a concrete example, this is a ridiculous experiment I did recently. There's a generative vision model called stable diffusion, where you can give it a text prompt and you can basically just sample and generate images. I ran up stable diffusion on my huge big fat desktop here and said, generate me, I can't remember, 100,000 images of a screw on a workbench. Now generate me 100,000 images of a bolt on a workbench. I use those images downscaled to train a TinyML model, and it works okay, because the constraint now of what we're trying to decide is quite small.
In terms of what did I use as a user? I just gave two textual descriptions of what I wanted the thing to do. Then behind the scenes there's this big CPU burn, which is basically materializing information from this large model to just really narrow down to then train that small model. It's a really interesting question, how much data do you need? Because we have access to things now that we maybe didn't have before.
**Scott:** You shrink the solution space down for the small models from what the large model is, and you can do it with a lot less resources then, I guess.
**Matt:** Yes, absolutely.
**Scott:** One of the things that I've noticed about when people are talking about these applications is that it's usually working on streaming data. There's that it's a continuous process. I wonder if that presents any particular challenges that would be different from one of the big cloud solutions that we see?
**Matt:** Yes, that latency thing that I think Andy alluded to. A lot of industry problems are around streaming data. It's classic sensor data. You've got some machine that's vibrating and you want to know, does that vibrating mean that you're about to fail in the next day? In which case, I should tighten your bolts now before you fail. Some streaming data, audio-related stuff, wake words, those things very much are around that very, very short roundtrip, which definitely doesn't work well with cloud-related stuff. It's one of the main motivations they had to put things on a phone was because the roundtrip lengthy was too slow to go to a cloud to do wake word detection.
No one wants to wait 50 milliseconds or something. It's a big one. Streaming data as well. Often the ways that it's funny, it's been embarrassing. The classic, the best ML is no ML, but a lot of the streaming related things we do with say very high frequency data vibration, that stuff. It's solved primarily using very, very old classic digital signal processing stuff and the actual "neural networks" we put on the device to do something are just very flat linear regression-type stuff even.
Again, the beauty of neural networks, if you take a neural network and you keep turning things off, you get to something like logistic regression, which is this super old technique that is fundamental. The practical side of things is that in the TinyML space, again, based on the modality of the data and the low-hanging fruit, the ML part is sometimes a little bit embarrassingly small. [chuckles]
**Rebecca:** Well, and thinking about a lot of the examples that we've been talking about so far, are this real, okay, you flash it and then you forget it with the sensors and such. Are there applications other than okay, I've trained my iPhone to recognize my face so I don't have to type in a PIN except every two weeks. Can you think of more out-in-the-wild applications where maybe you are using some tiny reinforcement learning or there's interactions that would modify that model over time?
**Matt:** Yes, anomaly detection's a really big one. The idea that you don't really know what's anomalous on a particular device until you get to it. It's a huge, huge market in terms of predictive maintenance. It's a mammoth one. The staging usually is that three steps. One step is how do you set the model up to do its best in terms of before it leaves the nest? Then the second stage is what can you do on device to do training on the fly, which might get some phenomenal detection-type stuff? Then how do you, if at all, get stuff back to base in terms of training data?
Because one thing that really surprised me, and it's obviously in hindsight, but I hadn't really thought about it at the time, is that if you're doing something on a microcontroller, you don't have much working space, you really have enough memory to do something interesting in the next 10 milliseconds, and then you throw it away to get the next bit of streaming data in. If you want to do long-term collection of data, it's often with an attached device that's very particularly there just for the point of providing storage. Though we can do things on the device that's often around this fine-tuning type of stuff, it's definitely difficult.
That's not to say that not lots of cases where there are things in a mesh and that are talking to each other. It's just the extreme you always have to think about is this idea of the single shot of the model. More and more as infrastructure gets better and tooling across a network of industrial plant, you can do on-the-fly updating of models. The actual device is getting big enough to handle the idea of an over-the-wire update and stuff. It progresses and progresses and gets better and better in terms of these updates, but we're still in a lot of regime of one-off.
**Scott:** At the start, Matt, you mentioned that TinyML challenges a lot of the MLOps approaches that we use today. Machine learning engineers will train a model, deploy it, and slowly refine that and monitor its accuracy over time until they finally get something that works. It gives them the ability to adjust that model to its environment, so it's as realistic and as close as possible.
In contrast, TinyML doesn't give you that ability sometimes. How does that change the development process? Does it push a lot of the iteration right back to the lab so you need to maybe simulate more or change the way you do things because you've really got that in a lot of cases just one shot to burn it to a sensor and then it's off in the wild for however long? How have you seen that challenge that MLOps idea?
**Matt:** Yes, it's really about that embarrassing waterfall-type approach of saying, "I've got to collect a bunch of data up front." There's a whole industry around the idea of how do you collect that data. There's what we call bricks, which are these devices that you might say to someone, I'm going to have to have put this brick on your industrial devices for the next month or whatever to collect fundamental data. Then we'll take that data away and then we'll do the model development and then we'll deploy.
It can be iterated, but it's just the things that we assume are really cheap in online web-type stuff, like parallel models or just logging every bit of inference that goes through a model, they're just really difficult to do. It's much more traditional. Collect a bunch of data, train a model, deploy that model. Even the monitoring is really difficult. Once you've got this thing that's running on a microcontroller and the only reason you could really deploy it in the field was you knew it was only going to cost $4 per device to send across this manufacturing plant of a thousand devices. How are you going to monitor them? How do you even know they're working properly? What's the operational version of this? It's really difficult and certainly unsolved.
**Scott:** What is the workflow, the typical workflow for somebody who's building one of these models and getting it on a device?
**Matt:** It's funny that there's two real key personas that I've seen in this area. There's one where there's an ML person who's a bit more like me, who comes from the ML side of the things and is interested in the embedded. Then the other one's the embedded engineer who's the person who knows how to actually write some bizarre C++ code to get this working on a bizarre bespoke toolchain they're using because it's a complete wild west. When you think about the silicon side of things, everyone's got their own compilers and you have to use this SDK on this chip and are you using this other chip or this other thing?
It's all over the place Those embedded engineers who are very specialized in that type of area don't know much about machine learning. The flow is really interesting at the moment. There's a lot of, not conflict, but there's a lot of budding of heads when you try to go from the idea about how do I train a model to how do I actually deploy the model. It's funny as well.
The one thing I've really noticed, and it's the elegance often in the tech industry of us, we build layers on things, which build layers on things, which build layers on things. It's easy to take a model nowadays. Even if I don't know much about ML, I can Google search for a while and find some, "Oh, here's a model that does something in the mobile network. That's cool. I'll just download. Oh, here's a colab, I'll grab that Jupyter notebook. Oh cool. I'm trying to model." It's so easy to do and to build something valuable but have absolutely no idea how it works under the hood.
It's funny to see a lot of people we work with that are embedded that they're running these ridiculously large models that are a hundred times bigger than they need to be, just because it was the simplest thing for them to do. I feel like that's happening a lot, that we've got people who are embedded that don't really know the machine learning, but are able to get something working because again, they're in that low-hanging fruit.
They get something simple, but they're going to experience pain pretty soon when they try to do something more complicated. The tooling, there's a real mismatch cadence between the tooling. I might train in TensorFlow, for example. TensorFlow has a part of its sort of library ecosystem called TensorFlow Lite, which was developed for phones.
Then there's another part of it, which is TensorFlow Lite for micro, which was developed, for the microcontroller type stuff. It's all still quite weird. I have to run this command over here. If you look at a bit of code to do this, you can really see the sort of levels of distraction and where they break. This is real elegance and beauty around these abstract methods to call, "Oh, get a data set, train a CARES model. It looks really nice." Then there's this horrific, bizarre bit of code where I make some converter to convert TF, I don't know what's going on.
You can really see, whenever I see a bit of code that's like that, it really illustrates the fact that these bits that have these really bizarre bits of code that aren't at the same level as the abstractions around it, mean that these haven't been unified yet, it's frameworks. They're very cobbled together. It's certainly not solved. [laughs] There's a lot of hard work you need to do to make things work.
**Rebecca:** I'm a programming languages geek. I have to ask since you mentioned C++ and I know in other contexts, like autonomous vehicle technology there is a move to adopt Rust as opposed to C++. Is there any of that going on in the TinyML world, or is it still very firmly in the C++ world?
**Matt:** I think it's very firmly in the C++ because there's no agreement between silicon manufacturers to have a real standard for how you write a bit of code except for C++, so it really is still the canonical thing. Yes goes back to that wild west comment of if you want to actually deploy something on a microcontroller you get to this point where you've got a bit of C code or whatever it might be C++ running inference.
Or even if you have maybe a TensorFlow graph, so you've trained a TensorFlow model, you want to run this on a microcontroller, the TensorFlow graph becomes the symbolic representation of the compute which then goes through these compilers to get it converted to different bits and pieces. You end up having to find for this particular silicon provider a bespoke toolchain that I have to download and, "Oh, it only runs in windows. I have to run in a VM or something."
Now, I've got some weird XCI have to run that takes a TF lite graph and spits out some dump BIN file that I flash. The fact that it's all this wild west and this certainly not standardized means that we're forced as the common denominator to stick with something like C++. To be honest, and again it's an interesting thing, I haven't learned as much embedded as I would've liked. I was talking to someone about this the other day. I'm still an ML person, not an embedded engineer but one day maybe.
**Rebecca:** Sorry for the detour but like I say, I'm a languages geek.
**Matt:** No, no, no. No, I'm fascinated with it. There's a language that we've been using more and more that's called JAX that I've jumped on the bandwagon quite a while ago. There's this whole compiler technology called XLA that Google has provided. It's nothing really to do directly with TinyML, except it is. Here's a random diversion. Google had these huge farms of GPUs from NVIDIA. They realized they can't be stuck with it forever.
When you get to a large enough scale, it's worth building your own ASICs for doing compute so there's development of the TPU. If you're developing your own ASIC like this, you need to put hard software abstractions between what you are doing and the way you're deploying which turn into this series of compiler technologies called XLA which is this accelerated linear algebra toolchain. It's more formally under these open things like MLIR now but it gives us this level of abstraction in the software that we write things in, this symbolic graph that get spit out so to speak to GPU kernels or to CPU code.
The reason I bring it up is because more and more there will be targets from this compiler language which is a particular sub-microcontroller. One thing that we've been playing with a lot is this idea that a language like JAX gives us this intermediate representation which means I can pull in NumPy and I can go through JAX. Underneath TensorFlow now, if you start to dig a little bit, you get to XLA because it's what they're using under the hood.
It all becomes this muddy one thing under the hood. No longer is TensorFlow just TensorFlow. It's something that sits on top of XLA, which means that I can approach it from different angles. The reason I bring this up is because the language becomes more and more free and these intermediate compiler languages mean that I'll be able to write Rust, pass it to this XLA.
The XLA compiler will just spit out some binary microcontroller code in optimized, in insane ways. It's changing. If we were to do this podcast in three months, it'll probably quite different again. It's really under churn at the moment. It's really interesting stuff.
**Scott:** Is there trends in the hardware space? I don't know what the popular deployment platforms or microcontrollers or embedded devices, but is that changing? Are there any big trends there now?
**Matt:** I feel like the whole supply chain stuff that's been happening the last couple of years has had some interesting directions about things. I feel like the more and more and more as useful applications are demonstrated through the use of a microcontroller, the more microcontroller silicon providers want to get on the bandwagon and sell people stuff. The most interesting general thing I think is around sensor fusion. Because at the moment you have an idea that you might have a sensor, especially a very high dimensional sensor like a camera that is very different to vibration sensor in terms of its acquisition.
The complexity of the information it gathers and how much memory it takes and stuff. At the moment, architectures are still hardware-wise very separated. You have a camera that acquires something and then you pass it off to a machine-learning model running on a chip. If we are talking about more and more this idea of not disposable, but one-off built things, then they start to merge a little bit in what they are. Why not start to put things around the sensing actually more directly in the memory that the devices are using.
In some ways, it's the most interesting trend. I think the idea that the sensor and the compute for it become almost the same thing in a sense. There's these ridiculous examples of my most interesting one, I think it's from about a year ago where someone-- and I'm going to get this totally wrong because it's been a while, but someone in developed this idea of a memory layout on a chip, an actual piece of memory that you write and read from this bit of memory at the lowest level. They worked out a way to express the read from the memory to have as a side effect, the calculation of dot products.
Now dot products are like this fundamental part of linear algebra that is used in all of machine learning. Everything we do in machine learning these days is just lots and lots of matrix multipliers, which are lots and lots of dot products. They'd worked out through this really bizarre scheme, a way of doing these types of calculations as a side effect of the memory read, which is just ridiculous because suddenly it's insanely fast. We're going to have the idea that maybe CCDs, and the idea of the way we acquire information from a visual sensor, gets more and more connected to the memory as well.
In five years, we might have this idea that your sensor is actually doing the compute as well. Why not burn into the actual CCD the way we laid out a feature extractor that says that this little camera module I'm giving you isn't a camera module in the sense that it's spitting out RGB, it's spitting out some learnt interesting representation, lower the dimensional representation, that is then useful for a neural network downstream without you having to have this 10 million parameter convolution neural network. That's just a really rambling answer to your question, Scott, but I think--
**Scott:** It was a rambling question, so that's okay.
**Matt:** To this idea of fusion, I think that's the most interesting thing. How do you find two bits of hardware that are close to each other that are serving a common goal and actually make them the same bit of hardware?
**Scott:** Hey, Andy, part of your job is to be a bit of a futurist and look at what are the potential industrial uses or where are these things being done now and what are the potential business implications for that? I guess the first thing, is this a future, you think? Is this something, or is this a practical reality now?
**Andy:** Yes — and Matt mentioned this earlier — I think the most common application for TinyML today is around wake word detection. For our smartphones, all of our voice assistants, they're using TinyML to listen to the audio stream and detect very, very few words, simple words. We all know what they are. I won't say them because all your phones will probably go off but that is an example of TinyML. It's embedded, there's dedicated hardware in our phones these days to do specific tasks like that. We're already seeing it. When we talk to people about TinyML, they're like, "I've never heard of that before."
When you explain how it's already part of their everyday lives, they all of a sudden realize it's something that's here today. It's not a futuristic thing. That's one example. Matt has been mentioning a few other examples that are starting to come out in industrial IoT applications for preventative maintenance and anomaly detection and these types of things. I think we'll begin to see more and more of this in the future where it's embedded in smartwatches and activity monitors and you can buy pillows that detect your sleep patterns and all of these sorts of things.
That's where we'll start to see more and more of these machine-learning models being deployed at the edge. It has its challenges, but it also has its advantages around privacy, latency, and all of these sorts of things. Imagine you can start to use models now to detect things that you probably wouldn't be comfortable sending to a third party or a cloud provider. Maybe it's health data or something about you that's inherently personal that you wouldn't want to share. All of a sudden we can start to use these very narrow specific devices to service those applications that maybe otherwise we wouldn't have a way of dealing with. I think we'll begin to see it more and more.
I think machine learning engineers will start to develop the skills that are appropriate for these types of applications. What I'm hopeful is that machine learning engineers don't always default to just deploying things into the cloud, and start to look for opportunities to deploy things closer to the edge. If it's on a microcontroller, fantastic. If it's on a phone, that's also really good as well because there's these unique user experiences that we can create with these models that otherwise wouldn't be possible because of latency and privacy and things like that.
**Matt:** Yes, as tooling gets better you just get more and more people thinking they've got a problem and the tooling's easy they'll just solve it. We have a really common use case which makes me laugh but if it works, it works. Where if you are retrofitting a large old industrial system that uses water pipes, for example, or gas pipes and you've got analog dials that are just literally sitting some old gauge, why not sticker vision model on it that literally reads the dial and then pings off as a digital thing, what the dial is reading? It sounds ridiculous but if it's trivial to do then [chuckles] why the hell not retrofit things if it cost $100 or something.
These things, I love them in the sense that if you put your formal academic hat on, you're like, "That's ridiculous overkill. Why would you bother using a convolution net to do this?" It's like, "Well, actually, if it's really easy to do and really cheap and it adds value immediately, then why would you not do it?" I feel like the better tooling gets and the better the easier things become, then the more ridiculous ways people will work out to stick this stuff everywhere.
**Scott:** One of the things that we alluded to before was what you can accomplish with lots of these devices working together. It's fascinating to think about lots of these tiny smart devices working together to create some emergent behavior that is smarter than the sum of them put together. I know, Andy, you've talked about composable AI. Is that a similar concept?
**Andy:** Yes, for sure. The idea is that we have these small devices that do one very specific task well. If we can combine different types of devices together, we end up with these systems that are composed of small AI devices that create this more intelligent or more interesting thing. Again, cars are a great example of that. How we can have a sensor that detects whether it's dark outside or not to turn on the lights, we combine that with proximity sensors and all of these other sensors. All of a sudden we can start to create these eventually self-driving cars or even driver-assist features that together are really, really interesting.
Another great example is VR and VR headsets. If you think about a VR headset, it's all about the user experience. The latency in processing the visual information, the gesture information, the movement of the head, the sound, audio, all of these things need to come together for this device to be successful. I can see a future where TinyML is playing a really key role in at least pre-processing some of that information so that it can enrich it for further processing maybe later on.
Together with all of those TinyML systems embedded in that headset, we get this greater user experience that hopefully is more immersive and realistic than it otherwise would've been. I really like that idea of taking these very simple dumb devices, adding them together to create these really intelligent systems like cars and VR headsets and things like that.
**Scott:** In my layman's understanding, that's how the brain works. Lots of modules, smart modules, but working together, competing, and cooperating in different ways to create some larger behavior.
**Matt:** It definitely fits very well with how neural networks work. They have this beautiful decomposition where you can break them into what we call this idea of layers or blocks, depending on how you want to structure things. Where the only job of the network is to take some information and transform it. Then transform it again, and then transform it again, transform it again to the same output.
Usually, it's a lot around the time the idea of compression. If you have a vision model, you have this very high dimensional data coming in. If you're classifying, is this a cat or dog, you can think of the neural network as just incrementally compressing that very, very high dimensional image down to something that is just literally zero, one. The beautiful thing about it is that if you train a model that does this, you can literally chop them in half, and you get the first part of the model whose job is to learn interesting features from the high-dimensional data that is only really used for the second half of the model.
That ability to chop them up means that you can do some of the stuff that you talk about in terms of composability, where the job of the edge model, the thing that's in the factory where there's 1,000 of them, its only job is to learn some distilled version of what it's seen from this high dimensional very high-frequency data in the last five minutes to ping off with a little Bluetooth ping after some central box like a big raspberry pie sitting in the corner, or something that then collates that then turns it into a useful decision in terms of monitoring the overall structure of the factory.
This idea that a lot of the common ways of the most successful formulation of machine learning in the last 10 years for supervised stuff is neural networks, which have this great ability to be decomposed. You can literally think of it as run the first bit of the neural network on the edge and then run the second part of the neural network back to base, so to speak. A lot of flexibility in how you decompose and run bits in different places.
**Scott:** Our audience would probably like to know, how they can get started with this. There's a lot of practitioners out there that might be interested in experimenting with themselves. I wonder what would your advice be to a developer who wants to get started?
**Matt:** Yes, it's hard not to plug my own company, but there's platform at Edge Impulse that does this thing. We have a lot of competitors, Neutron.AI, for example. Neutron. There's a number of platforms available, a number of frameworks that are made for either the embedded person or the ML person that are coming at it in different ways. They all frame the problem as this three-step of curate the data bits, build some machine learning model, deploy it to a device.
You can go a long way with those-- Most use cases can be started with that general idea of I have a data set, I train a model, I want to deploy it. Then as you go further and further and get more mature, you might decide, "Oh, I don't want the platform to do the first part, I just want the second and the third part." Or, "I've got the third part handled, but not the first and the second."
More and more it is being approached, at least from a first phase for a lot of people as using one of these platforms. Then as they get more mature, picking and choosing parts of the platform that they might want to integrate into a bigger part of their system. Yes, it's still very early days and it's very illustrative, I can tell you firsthand experience, to try to build it from scratch in terms of first principles, like take a SDK from Arduino Library or something, take TensorFlow and the way it exports TF lite graphs and the TensorFlow experimental conversion to some of these things and to stitch it all together. It's very interesting in early days and I think a lot of the platform plays have come out of that pain.
**Scott:** Matt, given your background at Google and your long history with this field, I can't pass up the chance to ask you what you think of the topic nobody's discussing about generative AI, large language models. Are chatbots going to take over the world and ruin literature or what's happening here?
**Matt:** It's the singularity here? This is one of the questions I get. When is AI taking over? No, it's funny. Maybe I would've been more interested in this 10 years ago when I was really deep in NLP large models. To be honest, given some tiny problems, I've been working on ChatGPT, which is far from tiny, has been on my radar to deeply look at. I do like all people have opinions that I'm happy to talk about.
I feel like the biggest thing with NLP and it goes all the way back to classic natural language processing. There'a two fundamental pillars in NLP. There's syntax and semantics. When you think about a model like a ChatGPT or all the models I ever worked with in NLP, they're very much trained on textual data, which is very much on the syntax side of things.
They're very, very good at being syntactically correct. Very good grammar, being able to write in the style of a person, all the sort of things you think out of syntax, the actual surface forms, and the way it's written. A prose gets longer and it's more coherent in terms of syntax, that can be quite convincing. I think these models are very good at convincing people they're right. The other pillar, which is really important with text and a lot of the ways we use it is semantics. What does it mean? Is it correct? Is it factually correct? I feel like more and more we have these models, which make it trivial to generate text because text is the ubiquitous modality of knowledge we have on the internet.
The ability to have a model that generates a bit of text that I can then cut and paste into a YouTube comment or a Facebook thing or make a bot to do is very interesting what the large-scale ramifications for that will be. It's just text. There's nothing about it being correct in any way. It's convincing, but it doesn't mean it's factually correct. Now, for a lot of cases, who cares if it's factually correct? I want to write a Harry Potter alternate history or something. Sure, spit out a bunch of very coherent syntactically correct stuff. If you start to now talk about it in terms of weaponization for political stuff and the fact that people would be reading this stuff, thinking it's factual, it worries me, that stuff worries me.
That's just an opinion. It's certainly very interesting.
**Scott:** It's an opinion that might be more informed than a lot of the others that I'm listening to these days. Thank you.
**Matt:** It's fascinating. We used to work on knowledge graph completion, so the idea of building semantically correct knowledge that then is then used in textual generation, and it's really hard. It's really hard. There's so many things when you start to talk about truth, what does truth mean? Did Harry Potter go to Hogwarts? Well, yes, he did, but no he didn't because that's fiction. It's not actually real, is it? You can't say he did or can you say he did? If you think about something like what's the capital of France? Oh, it's Paris.
What about a thousand years ago? It wasn't Paris anymore. What's the fashion capital of France? Is that Paris? Hang on we're talking about opinion now. Is it objective? Is it subjective? As soon as you start to even think about any of these concepts, they get way muddier than you think they're going to be. It's a fascinating problem space to deal with.
**Scott:** Okay. Well, thank you. This has been really interesting. It's always good to talk with the three of you. I've had many separate conversations with you so this has been really good to get everyone together. Thank you.
**Rebecca:** Thanks.
**Matt:** Thank you.
**Andy:** Thank you.
**[music]**
**[END OF AUDIO]**
[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
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
[ Explore Technology Radar ](https://www.thoughtworks.com/radar)