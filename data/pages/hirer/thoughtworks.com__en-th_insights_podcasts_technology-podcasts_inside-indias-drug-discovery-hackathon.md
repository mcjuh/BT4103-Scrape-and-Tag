<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/inside-indias-drug-discovery-hackathon | Title: Inside India's Drug Discovery Hackathon | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Inside India's Drug Discovery Hackathon 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Rebecca Parsons  and Ashok Subramanian | Podcast guest  Pooja Arora and Justin Jose
March 23, 2023 | 38 min 56 sec 
Listen on these platforms
## Brief summary
Covid-19 unleashed a wave of medical and pharmaceutical research and innovation across the world. In India, the government launched the Drug Discovery Hackathon, an initiative designed to bring together expertise in fields ranging from biotechnology, pharmaceuticals, machine learning and virology to discover new drugs that could help thwart the pandemic. 
One team that took part was from Thoughtworks India. In this episode of the Technology Podcast, two of the members — Pooja Arora and Justin Jose — talk to Rebecca Parsons and Ashok Subramanian about a number of projects they worked on during the hackathon. Among other things, they explain how they used reinforcement learning to improve the efficacy of potential drugs in tackling what was, at the time, a virus that was only partially understood.
## Episode transcript
**[Music]**
**Rebecca Parsons:** Hello, everyone. Welcome to the Thoughtworks Technology podcast. My name is Rebecca Parsons, I'm one of your recurring co-hosts, and I'm with my colleague Ashok. Ashok, you want to introduce yourself?
**Ashok Subramanian:** Hello. Hello everyone. I am Ashok, one of your regular co-hosts of this podcast, and I'm delighted to be joining and discussing a very, very interesting topic today.
**Rebecca:** We are joined by two of our colleagues from Thoughtworks India, Pooja Arora, and Justin Jose, and we're here to talk about using reinforcement learning for drug design. Welcome, Pooja. Welcome, Justin.
**Pooja Arora:** Thanks Rebecca.
**Rebecca:** This project came about as a result of a hackathon, if I understand. Can you tell me a little bit about the hackathon.
**Pooja:** Sure, so this hackathon came up right in the middle of the COVID-19 crisis in 2020, where the world was fighting COVID and the scientific world was figuring out ways how to control COVID. That is the time where Government of India launched the drug discovery hackathon. As a part of it, there were three tracks to it. One was fighting a few of the COVID aspects. Another track was to build tools and algorithms that will help in the current COVID-19 crisis, was also thinking from a future pandemic perspective. Another track was for any other moon shots. We participated majorly in track two, to build tools and algorithms frameworks for fighting such pandemics.
**Ashok:** I think my understanding of this was an open competition for many people to explore different or novel approaches to trying to solve this problem, right?
**Pooja:** Yes. We participated in three problem areas. One was to generate antiviral molecules, peptides, which is in itself a different world, and very different to find naturally using generative methods. Second was, if you've heard of drug toxicity, can we early on identify the toxicity of potential drug molecules? The third one, which essentially is the major one that we're going to talk about here, is can we utilize reinforcement learning methods for identifying the drug pose? With all the three problems, we got into the final phase-- it was divided into multiple phases in the final interviews or selection process. However, this particular problem got through the phase one and we got a one year project in phase two.
**Ashok:** Maybe I think that given that there's probably quite a few different things in there, if we focus maybe a little bit on the last one you said, using reinforcement learning for drug pose, what is drug pose really?
**Pooja:** Maybe setting a few synonyms or acronyms here. Look at when COVID-19 came in, it was something different. People were not reacting to the regular medicines. There were tests conducted, there were x-rays done, and a lot of lab tests done, which took us to identify that this is not a usual fever. This virus is attacking somewhere else. That's what you call as the target. For the identified target, I need something that will either help me stop that virus from spreading, it will attach itself, it will make some impact, so that it does not spread further.
That is where the drug came into the picture. Now, taking the biology out of it, take an example of a lock and key. The lock here is the target, and key here is the drug. Unless you have the key in the right position, with the right touch points, right orientation, the lock will not open. That is the importance of the drug pose. The drug will come and bind-- the potential drug. I'll cautiously use potential drug, unless it is really identified. Potential drug will bind to the target, given both of them are the chemical entities at the bottom, can bind in multiple ways. Binding in the right pose with the right interactions, will only make it biologically relevant and it will have its desired impact. Does that make sense?
**Ashok:** Yes. Yes it does. Oh yes, definitely. It does clarify what you were trying to solve for.
**Rebecca:** How did you go about solving it?
**Pooja:** Go ahead, Justin.
**Justin Jose:** The problem required us to come up with a mechanism, specifically in reinforcement learning. This problem has been tried to be solved in machine learning approaches, where you have data, you used data generator model, try to predict where that drug would bind to the target. The problem was presented to us as a reinforcement learning problem, and we have seen reinforcement learning being used in, let's say, robotics, or gameplays mostly. There, the expected outcome is finding a path.
We have the agent, who would try to navigate and reach a destination. For us, the binding pose, where the drug would finally attach becomes the destination, and a randomized starting position for that drug becomes a starting pose. We would want to train the reinforcement learning agent to navigate it, or push that drug to that final pose. That is the overall idea of using an RL, or reinforcement learning in solving the problem.
Now, how did we visualize the problem? Visualization was a bit tricky. This is a three-dimensional structure chemical, complex three-dimensional structure. The analogy of lock and key, yes it fits to make it understandable, but can we model it into a reinforcement learning problem? We had to look at other areas which we can quickly understand how to formulate it as a reinforcement learning problem. In that case, parking lot came as a good analogy for us, but it doesn't capture the entire complexity, it just gives an idea how the drug and the target would work.
Here the target is a parking lot. There is a free parking space where I would want to park my car. The car becomes the drug. I would want to train an agent, RL reinforcement agent here, which can drive the car into that parking space, making that problem map to a more robotic or gameplay kind of approach. That was understanding the problem. Once we have understood the problem, the second aspect is identifying what will contribute to identifying that position. Now, we have to look at chemical structures, atoms. The proteins are chemical structures in general, they're molecules, large molecules, so atoms come into play. How do I represent an atom?
The drug, again, is a molecule which attaches to the protein. How do I capture the idea of two molecules interacting with each other? These would then come into the representational idea. Then one aspect of reinforcement learning is defining a reward function. The reinforcement agent learns an action by repeating it, and the reward tells the agent whether the action is good or bad. Designing that reward function becomes a third problem, or a third challenge in entire formulation of the problem.
**Ashok:** You mentioned the parking lot as an analogy in there. Clearly, I think in the lock and key, or even the parking lot, part of it is almost like-- does it describe the initial part of the problem they're trying to solve? Which is actually, where do you fit in or finding the space, but then maybe I think around, do you park the car facing forward or reverse? That is the kind of analogy you're talking about?
**Justin:** Yes, that is the kind of analogy now. You would want to park the car in the right orientation, you can't just park the car. It has to be right orientation. Parking lot analogy slightly makes the problem less complex. There are many complications which comes in when you look at it from a chemical space, you have molecules interacting with each other. Some atoms cannot be next to another atom because of repulsion. Some atoms would just attract and be there. Such complications come into play. Parking lot analogy was to help us formulate the problem in a way which we can understand, we can relate to, so that we can find a path from robotics, gameplay, and then finally apply it to a chemical space.
**Ashok:** It reminds me of sometimes when you go into parking lot and you park a car, and you realize after you parked it, there's a pillar right next to it. While you can park the car, you can't really get out. It's not really very helpful. I can see where that instance —
**Pooja:** I was just going to say I will multifold that. When you have structures that they may look similar as a sequence of letters. There is an A, after that a G comes, at some point a L comes. When that defines it final confirmation as a 3D structure, those similar looking may give you a very different binding pocket is where we go. Actually, the drug goes and bind, then ultimately the interactions that they form the structure of the drug itself. They give very unique setup. You may get similar-looking parking lots, but it's a tough job to get similar-looking binding cavities or the binding pockets. That adds another level of complexity that the diversity that the agent needs to look at and to learn from is quite a lot.
**Rebecca:** Is there a simple explanation to the reward function on how you conceptualize that?
**Justin:** The reward function here should help the agent navigate this complexity while being able to capture the ideas around what atom should be next to it, what interactions should be there. The reward function should enable the agent to find a pose which gives precedence to all of these. To start off with training, you would take some data which exists. In this case, it is complexes which are similar for which we would want to train the agent to, in this case, the SARS being the target for which we want to train. We would take similar complexes.
Now, these complexes, they have an experimentally attached drug which experimentally has been proven that it works. We would want our agent to mimic at least that to begin with. Once we are sure that the agent is capable of mimicking it, because of the similarity between the SARS and this particular training complex, it can find the optimal pose for whatever complex we give. With this as the premise, what we would want to do, the agent-- when we design the reward function, what we would want to focus on is how do I tell the agent that where you have reached and where you are, the action which you have taken to reach there, is it a good action or a bad action? For this, what we take is a difference between where it has to reach. It's practically a positional difference.
The drug would have to reach at coordinates-- For simplicity's sake, let's take coordinates as an example. Drug has to reach at a coordinate of 10,9, that is experimentally available position. The current action which the agent has taken has pushed the drug to 8,7. Basic Euclidean distance between these two positions would give me a sense whether is the action good or bad. Has it moved it closer or has it pushed it further away from there? If I use it as an absolute value, the changes between these individual actions would be really small. Now for the RL agent, I would want to tell that once you reach very close, I would want you to push it further closer.
Because once it has reached close enough, the changes in that distance is very small, the agent would be like, I'm not getting enough reward to do that. I would want to shape my reward in such a way that the closer it gets, it gets a higher reward versus when it is very far off. That would come under reward shaping in the reinforcement learning problem.
**Ashok:** Almost like when children play, they're trying to find something and then play hot or cold or you say freezing as to how far away you are. Similar concept analogy in there, right?
**Justin:** Yes.
**Pooja:** Excellent analogy, Ashok. You always talk in terms of parenting. That's how the reward function works.
**Ashok:** I can see that in this case. Does that mean where you also described that, just following on from what Rebecca was asking around the reward function, this basic concept, is that the same? Would that basic concept apply across different types of these drug poses? Or would you have to tailor the reward function? Say you look at SARS, COVID as a thing, if you look at a different type of problem, would you also have to tweak the reward function and its principles? Are the principles that remain the same?
**Justin:** We have to look at the current problem in two separate lenses. The first one is, do I want to generate a model which can be then reused across multiple drug complexes, or do I want to do a one-step optimization? One-step optimization would be across multiple iterations the same drug and the protein complex are played around and they eventually converged to an optimal position. That would be one-step optimization.
Reinforcement learning can be used there. In that case, I can use a tailor-made reward function which very specifically can work for that particular drug complex. On the other hand, if I'm trying to generate a model which after being trained on a large data set can be applied back to any complex, then I can't use that individual complex-based tailor-made reward. I'll have to use a single reward which in a way applies to all of the drug complexes which we are working with. In this case, the distance based is the most general way to look at it. What I'm telling the agent is all you have to do is reach to the target and I'll tell you, have you reached the target?
While you reach there, learn why the action which you took was good. That would come under the neural net or the machine learning part of it. Underneath it, we have a neural net which takes in a state of features. The input drug and the protein or the complex will have certain features which would be dependent on the molecule, the atom, the interactions between them, the number of edges, et cetera. This entire input representation would be converted into action space which would say, given this, what action should I take? This neural net would be trained based on the reward.
This neural net would be responsible for capturing the relationship between features, interactions, which atom should come next to which residue or atom for that matter. Since we were trying to develop a model, we had to go with a single reward function which would apply across a collection of complexes.
**Pooja:** Also, if I can add there, it may not be the only reward function thing, but we look at it underlying the exposure that the agent needs to have, the differences in the complexes in terms of their structure, interactions, and many more. What exposure that the agent needs to have? At some point, we were in a position that there were too many variables for our model to learn on. There's a changing reward, there are features, the data is too diverse. At that point, we said, let's look at it in a fashion that we reduce the diversity for the agent. We give it some similar structures. That will also help us understand its learning patterns.
Identifying that right data set, which will give it enough exposures, which will give it enough opportunities to experiment and learn on the type of interactions or the structural aspects will eventually help it get to the right pose. Eventually, the goal was to have, probably a very difficult task in the biological world, was for us to have a generalized model as much as we can. We wanted to move towards a generalized model that could cater to multiple protein or target families. When I say families, they're literally in terms of-- think of it as different viruses, for an example. A type of virus may belong to a family and they will have their own structural dynamics.
Another type of virus will belong to another family. We want to have a generalized model that might be able to cater to a large extent to multiple families. Then eventually there could be further training onto it. That was the larger goal.
**Rebecca:** What were the results? I know you've published a paper on this, but how well did it do?
**Pooja:** Sure. Like I shared that we said that, "Okay, there is a lot of diversity. Let's reduce the diversity for the model, understand what reinforcement learning can achieve, what learning capabilities the agent has." We reduced the data set to looking at only SARS 1, a particular type of protein, our target, M protease, collected some data around it, and then we started looking at-- And then we trained our model. The final results that we got which we have also published was to that, as a reward function, we used like Justin shared, RMSE, Root Mean Square Error, to identify how good our pose is to the experimentally available pose. Our model was able to reach to an experimentally available pose starting from something like 6.5 angstrom.
Angstrom is the distance in which the distance is measured 2, 3, 3.2 angstrom, which was fair. Then we also looked at that, "Okay, it has reached here, but what kind of interactions is it forming? Is it connecting any hydrogen to any oxygen, or is it making the right connections?" There are experimentally available tools. One of them is LIGPLOT which tells you the actual interacting amino acids or residues. We compared with that, and we observed that our model had similar interacting residues to a great extent, which gives a lot of promise in its biological relevance. If it is interacting with the right residues, it may be close to the biological relevance, which we have not tested in the experimental lab, but it gives us that promise.
Also, there is a series of work that we did after that which we are yet to publish, but we have been able to improve our model performance to go to an extent of-- for us, how do I say? For starting from 0.5 angstrom, as close as 0.5 angstrom to 4 angstrom. That's the journey that our model has covered, but yes, the published results that are available are till somewhere close to three angstroms.
**Ashok:** That's great. I think some of the things that you were mentioning in terms of this-- clearly where you started off with you trained the RN models to, again, some training data sets, which had some outcomes which were experimentally sort of-- How do you see this taken forward? The way these models would then be potentially used, is there about reducing the universe of options available so that then can be targeted to try out a fewer set of-- yes in a more limited set of options that can then be tried out experimentally? Is that the direction of travel for us?
**Pooja:** Yes. Eventually, as a larger goal, it should be able to help a structural biologist to take a drug and a target pair and say that, "I have this pocket, I have these couple of drug molecules, which I feel could be a good potential for these, and I need to know the optimized pose for them." There are a lot of methods available today. Some of them are traditional, some of them are deep learning methods. After that as well, there is a good amount of work that a structural biologist will do or experimentalist would do. Some of the traditional method, what they would give them is how good a binding is they calculate by atom's binding energy by calculating the binding free energy.
"Hey, here are the 10 poses, which are good, ranked 1 to 10. Now you can choose from them." That is the outcome of that tool. Now, the experimentalist will use a lot of their acquired knowledge to identify, "Okay, even the binding energy is less, this pose is not right." Maybe because it doesn't form the right bonds. They can clearly see a structural hindrance that is there available and many more. We believe that reinforcement learning could be path-breaking there, where one, it will give you one optimized pose. With my learning, this is the optimized pose for you.
That's the larger goal, that eventually it is able to acquire that knowledge that is either available publicly or available in the way experimentalists interacts with tools or utilizes their knowledge. The agent being able to learn those nuances of scientific domains and being able to apply them to predict or to get the right optimized pose. This is one of the aspect. There are many more aspects in the entire drug discovery cycle where these could be used. To answer your question in very short, we hope that utilizing this model, one, it will reduce their overhead to look at 10 different things, utilize and then come up with one.
Two, it will also help them to try out for the unknown targets, the unknown drug target pair. A lot of training has been done on the known drug target pair. Eventually, when there is a new virus or a new microbe or any other target is available for which we need to identify, based on the knowledge that it has acquired, they should be able to apply that. The agent being able to learn that this is the right pose and this is the right drug that fits in.
**Justin:** Adding on because we are using reinforcement learning here, we can also introduce the idea of live learning. Going ahead, the agent makes a prediction for known-unknown kind of boundary-based complex target, which is not part of its data set, and based on the outcome, it can be reintroduced into the learned model. Also since the reward function can now be tweaked, right now we are just using distance as a reward function. That is where Pooja mentioned that the knowledge aspect of it can be introduced along with the distance. Now, I can tell the agent, "As per my scientific knowledge, you have done good."
Rather than just saying, "Based on the experimental data you have done good." I can say, "Based on the experiment data plus my scientific knowledge, you have done good." So that is how you can now redesign the reward function in the reinforcement learning itself.
**Rebecca:** Are you continuing work on this model or are you branching out into other things?
**Pooja:** Yes. Like I said, now we have a working model. We want to package it and give it to a couple of scientists in our vicinity and known scientists to test it out, see how it performs. We have a set of things that we want to eventually do, but based on what they test, how did they feel? Did it help, how much of help it was. Getting that feedback from them, and then getting back to it is the goal right now.
**Ashok:** Pooja and Justin, what you've described is quite fascinating. I think it opens up lots of possibilities and clearly about how technology can be used to accelerate drug discovery. If you think of it, I actually have to try and get this to-- can you talk a little bit about the kind of technology stack that you used and the amount of effort that actually goes into training the model and the kind of data sets that are maybe available today. Do we need to get better at collecting them as well?
**Justin:** The initial first phase, when we presented it to the committee, before that we started with a 3DCNN approach. Where now since the drug and the target are three-dimensional structures, it made complete sense to just put them into a cube surrounding them as a three-dimensional entity. Soon we hit the performance problem because 3DCNN the cube is a densely packed information where actually the drug and molecule data is very sparse. If I take a 10-by-10 cube angstrom, it would hardly have 200 dots inside them, which needs to be captured. We had to then think of what is a better way to represent it. Graph Convolution Networks felt like a right approach there, but the only downside to it is we lose the three-dimensional information in Graph Convolution Network. It's a two-dimensional representation.
The challenge here comes like, how do I capture the idea of a atom being in space in a three-dimensional coordinate and another atom being its neighbor? That neighborhood information is something which we need to capture now. The three-dimensional idea can be captured as the coordinate itself, as one of the node features, node here being the atom of the molecule. Three-dimensional coordinate captures the spatial information.
Now, the neighborhood information. If you look at how a drug attaches to the complex, it comes pretty close and then there are these chemical interactions which happen, and we would want the agent to know that such an interaction is happening. If you look at 3DCNN, it is purely proximity. The agent can understand proximity there and it can deduce that, "Okay, fine, these two atoms are close, hence I'm getting a reward for bringing them close."
Now, when it comes to graph, I have two separate molecule structures. One is for the protein, which is an independent graph, another is the drug or the ligand, which is another independent graph. These two are not connected in any way, just purely from the chemical structure perspective. These have weak interactions between them. The spatial proximity is now captured as graph edges which represent these interactions. Whenever two atoms, one from a ligand, and a protein, come close enough so that certain rules are satisfied, which says that, "Okay, fine, these atoms are close, now, they can form an interaction," they form an interaction because of the rule. We introduce an edge, and that enables the agent to understand that these two atoms are next to each other.
Also, we are using message passing. It's a convolution network. CNN, it would create a grids and it would convolute the entire information across multiple grids, create a representation in one grid. Similarly, in graph CNN, what it will do is it will take the information of one node, convolute it with the neighbor, and based on the number of layers we add, it can accumulate, or one node can represent the information of n-hop neighbors. Hop is the number.
In this way, the spatial proximity idea also gets captured as edge is being added to the graph. What graph would generate is a representation on which now the RL agent can take a decision. The entire thing would be trained while the RL agent is training, based on the reward it tells-- There are two parts to it. One is it has to correct its action, which helps it do better in optimization. Second, is it has to correct its understanding of the representation itself. Based on the reward, it has to do two things now.
It would be exactly the same when we do RL with any machine learning approaches. It has to learn the neural net representation, output of the neural net, and using that output, what action is best suited for that. For this we use DQN. DQN takes a state-- DQN would be Deep Q-Networks, Q-based learning network based on neural nets. It takes a state, generates intermediate representation within the neural net, and the output of the neural net is the Q values, or quality, or goodness values, across multiple actions.
For us, the actions were, translation, delta translations in three-dimensional space. I would tell the agent, "Move the ligand by delta-X upwards, downwards, left, right," like that, in three dimension. For a given input molecule representation, the intermediate network would churn out the value which says which action would be the best suited, and this would be reinforced using the reward function.
**Ashok:** Combination of graph-based as well as DQN? Cool. Thank you.
**Justin:** One major challenge was graph in DQN, back then when we started, the literature was very sparse on this. Graph CNNs back then were used mostly for classification task. They were rarely used in combination with DQN. That was one of the challenges, trying to build was one challenge. Again, RL in drug also was one of the challenge. There was very little literature around it.
**Pooja:** Yes, there's hardly any literature in RL. Like us, there are a couple of papers which expand the potential, but very smaller experiments are available. There were a lot of things that we had to experiment from scratch, and then do a lot of test. One of the example of test we want to share on the-- where we were stuck on-- There is some problem, but we didn't know what it is. We broke down the problem in terms of data, in terms of graph, and then we did some experiments to see that, is that graph working right? Is it able to do a basic classification also?
**Justin:** The representation, converting the representation to the right learning in the graph, and then transferring, then attaching the reinforcement learning part to it. First, we formulated it as purely a classification problem. We would randomly spawn the drug left, right of the protein, and we would ask the classification to classify it as left or right. By tuning it, we understood that, fine, we have a graph model which learns now, now we can use it with the DQN approach to do the reinforcement learning part.
The same went for the reward functions also. Coming to RMSE, it might sound simple, like one step, we take the distance, we minimize it, it's a good idea, but identifying the way you would shape the reward was a very difficult task to start with. How do I tell the agent that, "You're pretty close, you have to go further closer."? Reward is in itself, it's a complex space in reinforcement learning.
**Ashok:** It sounds like there are quite a few different areas where you've had to either come up with new, novel techniques to try and actually solve for the end goal, as well as both in terms of solving the problem around it for discovery, but also in terms of the building blocks that are necessary, both around RLs and getting graph CNNs going. Well done, I think. For people who would be interested in diving a lot deeper into this, I think you had mention the paper. The paper is published at the moment, right? Okay, great. Yes.
**Rebecca:** Well, I think everybody understands the critical nature of the problem that you're trying to solve. We're hearing in the news about a new strand of bird flu that is going through the population, and we know that sometimes those things do jump to humans as well, so anything that can help in identifying a good target and a drug pair is clearly critical. Congratulations on the success that you've had so far. Thank you very much for talking us through this and putting it in terms that mere mortals can understand. [chuckles]
Thank you, Pooja. Thank you, Justin. Thank you, Ashok, and thanks, everybody, for joining us on this edition of the Thoughtworks Technology podcast.
**Pooja:** Thanks, Rebecca and Ashok, thanks for having us.
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