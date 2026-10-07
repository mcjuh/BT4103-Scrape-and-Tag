<!-- Source: https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/machine-learning-astrophysics | Title: Machine learning in astrophysics | Thoughtworks Thailand | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Machine learning in astrophysics 
[ Technology podcasts Back ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts)
Close


Podcast host  Neal Ford and Rebecca Parsons | Podcast guest  Yogesh Wadadekar, Divya Oberoi, Shraddha Surana and Ujjaini Alam
August 20, 2020 | 59 min 50 sec 
[Read transcript ](https://www.thoughtworks.com/en-th/insights/podcasts/technology-podcasts/machine-learning-astrophysics#transcript)
Listen on these platforms
## Brief summary
Astronomers are increasingly turning to machine learning as a means to understand more about our universe — whether that’s the formation of galaxies or the Sun’s activity. Here, our co-hosts Neal Ford and Rebecca Parsons catch up with our special guest from the National Center for Radio Astrophysics in Pune, along with a couple of Thoughtworkers to hear more about this intersection of data science and astrophysics.
**Podcast transcript**
Neal Ford:
Welcome, everyone, to the Thoughtworks technology podcast. I'm one of your regular hosts, Neal Ford. And I'm joined today with one of our other regular hosts…
Rebecca Parsons:
Rebecca Parsons. I'm happy to be here. Thoughtworks' Chief Technology Officer and one of your regular hosts as well.
Neal Ford:
And we have a large, varied group of people today, with a wide variety of recording qualities, because we're scattered literally all over the globe, and we're all trapped at home, because of the current geopolitical circumstances. But today, we're going to be talking about quite a fascinating subject, which is about machine learning and astronomy.
Neal Ford:
I want to get some folks to introduce themselves. We have a number of people here from the National Center for Radio Astrophysics, which is part of the Tata Institute of Fundamental Research based in Pune, India. And so let's get people to give an introduction to yourself.
Neal Ford:
I'm also going to ask our guests to specify whether they are talking about galaxies or the sun. Because we have two broad topics here.
Yogesh Wadadekar:
My name is Yogesh Wadadekar, and I'm an astronomer at the National Center for Radio Astrophysics, located in Pune, in India. Pune is a town with an urban population of about 6.5 million, and we are located about 200 kilometers southeast of Mumbai. So we are close to the western coast of India.
Yogesh Wadadekar:
We run and operate a very large radio telescope known as the Giant Metrewave Radio Telescope. This telescope is a radio interferometer, which is located about 80 kilometers north of Pune. Within our institution, we have researchers exploring a wide variety of areas in current astrophysical research. There's people who research pulsars, radio galaxies, they do cosmology with high redshift hydrogen detections and so on.
Yogesh Wadadekar:
So we cover a very large area, field of research in radio astrophysics, but we also do research, some of us also do research in fields of astronomy that are outside of the radio astronomy domain.
Rebecca Parsons:
And Divya, would you please introduce yourself?
Divya Oberoi:
Sure. Hi, everyone. My name is Divya Oberoi. I'm also one of the astronomers at the National Center for Radio Astrophysics. And like Yogesh said, we have a variety of different science areas in which we work. My own personal area of research is to do with the sun. I study the sun primarily at low radio wavelengths, which basically means that you're studying not so much the sun itself, but the very hot gas surrounding it, which we call the corona.
Shraddha Surana:
Hey, so I'm Shraddha Surana. I'm a lead data scientist at Thoughtworks. Been with Thoughtworks for quite a bit, but have been working specifically with the engineering for research team for more than a year. I think one of my first projects, I have been collaborating with the NCRA along with Dr. Yogesh and Dr. Divya in both their fields of specialty.
Ujjaini Alam:
Hi, I'm Ujjaini Alam. So I did my PhD in cosmology from the Inter-University Center for Astronomy and Astrophysics. And then for the last 15 years or so, I've been working in data science and machine learning algorithms as applied to cosmology.
Ujjaini Alam:
I joined Thoughtworks last year as a data scientist. One of the first projects that I've taken up here is the radio solar project with Dr. Divya Oberoi.
Neal Ford:
Okay, great. So we have two scientists and two Thoughtworkers, as our guests today to talk about two general problems in astronomy. So if we could have our specialists describe the two general problems that we're utilizing machine learning, to learn more about. So let's start with the galaxy’s problem, please.
Yogesh Wadadekar:
So what we are trying to understand is the star formation history of a galaxy. What that means is, whenever a galaxy forms over a period of time, it forms stars. Now, this star formation may happen all at once, or it could happen over a very long period of time. Or it could happen in bursts, which means there's star formation and it shuts off for a little while and it restarts again. And then there is a third burst or a fourth burst of star formation.
Yogesh Wadadekar:
So what we are trying to use machine learning is to predict what the star formation history of a given galaxy is. And how do we do this? We do this by measuring the fluxes of the galaxy, meaning how bright a particular galaxy is at different wavelengths or at different frequencies. And trying to use that to build a model of what the star formation history of a galaxy actually was.
Yogesh Wadadekar:
For different star formation histories, you expect to see different fluxes in the different wave bands. So that's exactly what we are trying to do.
Yogesh Wadadekar:
Traditionally, this is done using a very, very sophisticated technique called stellar population synthesis, wherein you actually try and model the star formation. You also try and model the kind of spectrum that stars of different masses and ages have, and how these stars evolve throughout their lifetimes.
Yogesh Wadadekar:
You also try to model how the spectrum of a galaxy gets modified by absorption and re-emission by dust. The dust itself could be very close to the star, in which case, it will be very hot. In some cases, the dust could be very far away from the stars as they form, and therefore, it's going to be quite cold.
Yogesh Wadadekar:
So, therefore, modeling this in a completely physical way, is an extremely difficult and complicated process. But this has been done very efficiently and very well, using all the known laws of physics and all the understanding of astrophysics that we have developed over the last century or so.
Yogesh Wadadekar:
What we've tried to do in our work is to try to see if one can take a physics free approach to this and just give a machine a very large number of examples, where we have measured the fluxes, and we've built, have the physics predict the star formation properties of these galaxies. And then we try to see whether the machine learning can build, without knowing the underlying physics at all, can build a model, which is equivalent to the physical model itself.
Yogesh Wadadekar:
Of course, here, we are trying to basically, the ultimate goal is to model the underlying physics based model and not the real universe. So, if the physics based model is an incorrect or incomplete representation of what we see, what the real universe is like, in that case, our model, our machine learning model will also be an incorrect and incomplete representation.
Yogesh Wadadekar:
But assuming that the physical model is a correct model of the underlying reality, what we try to do was trying to train a machine to understand, comprehend that model and make predictions. Of course, the physics based model is very compute intensive. It takes a fairly long time for it to model even a single galaxy, whereas a well trained machine learning model can do, one strain can make predictions in fractions of a second.
Neal Ford:
Can you give us a sense of what that data looks like? Is this all numeric data or is it imagery and the size we're talking about?
Yogesh Wadadekar:
Yes. So what we've done is, we've used data collected as part of a very large survey known as gamma. It's a survey that aims to understand galaxy assembly over different cosmic epochs.
Yogesh Wadadekar:
As part of the gamma survey, a sample of galaxies was first selected, for which spectroscopic observations were obtained with the Anglo-Australian Telescope in Australia. And following that, there were a lot of multi-wavelength observations that were obtained for the gamma fields.
Yogesh Wadadekar:
So for example, the gamma survey team went out and used an ultraviolet telescope to get ultraviolet fluxes for all the galaxies in their sample. Then they went and used infrared telescope to go to get infrared fluxes and then they used optical telescopes to get optical fluxes.
Yogesh Wadadekar:
Then what they did was they combined all the data that they had gathered on each galaxy and constructed a catalog. So in the catalog, basically, every line represents a galaxy and all the columns are numbers representing the fluxes in the various wave bands, going all the way from ultraviolet to the infrared, going through the optical wave band as well.
Yogesh Wadadekar:
So, what we are working with is a catalog of galaxies, that contains flux measurements in 21 different bands. This is not work that we've done, this is a very large community effort that was done over the last 10 years or so, wherein they obtained data on all of these galaxies.
Neal Ford:
And this is publicly domain data?
Yogesh Wadadekar:
Yes, this is absolutely public domain data. It has been released as a panchromatic catalog, wherein all the data have been combined. So they've done all the hard work of obtaining the data, processing the data and collating and collecting it together and making a public catalog.
Yogesh Wadadekar:
So all we had to do was to go to the gamma survey website, and simply download that catalog and that was our starting point.
Neal Ford:
Okay, I want to talk about the machine learning approach you took. But let's talk about the other problem first, which is the solar problem that we're applying machine learning to.
Divya Oberoi:
Okay, so let me try to put the solar problem in context. So it may seem like a bit of a surprise. But even though the sun is really the brightest object we see in the sky, there's plenty about it which we don't really understand yet. And a lot of that relates to the magnetic fields and the very hot gas which surrounds the sun.
Divya Oberoi:
Now, it has so happened that people have known for a long time that the sun as seen in the radio frequencies, especially at low radio frequencies, is much more dynamic, much more variable as compared to the boring sun which we see in optical. But we had never really had an instrument which was capable of being able to capture all that detail.
Divya Oberoi:
So sometime around 2013, a new instrument became available in Western Australia, it was called the Murchison Widefield Array. And this instrument is the best we have on the planet for capturing in great detail how things are changing on the sun, over very short intervals of times, over a fraction of a second. And over very small spectral spans, you move 100 kilohertz in the frequency which you're observing, and the sun looks completely different from what it was at the neighboring frequency.
Divya Oberoi:
So we had been working on building a robust, unsupervised pipeline, which would make these images in an automated manner. And just about the time Thoughtworks approached us for this, we had basically come up with a fairly good pipeline which would deliver these images. Now, we can in principle make something like 100,000 images a minute.
Divya Oberoi:
Having solved the problem of imaging, we immediately came across the next problem, which is how to understand what all these images are telling us. It was really impossible to look at them image by image and to imbibe for the human brain to wrap one's head around what all these thousands or hundreds of thousands of images are telling us.
Divya Oberoi:
So we wanted to, or started to look for a machine learning based approach, which would help us synthesize the information content of all these very large number of images. That's how we got started here.
Neal Ford:
Okay, great. So let's talk, now let's go back to the galaxy problem and talk about the data science machine learning aspect of that problem and a dataset that looks like that.
Shraddha Surana:
So for the star formation histories problem that we were trying to solve, the data that we used for it was from the gamma survey. So, this is a pretty standard data and the kind of data that we would use for most machine learning models.
Shraddha Surana:
So, there are some input records, which are the flux values in different frequency bands. But along with that, we also have the output free parameters that we are trying to estimate over here, which is namely the star formation rate, the dust luminosity and the stellar mass of the galaxies. So, these have already been estimated by the MACFES model and we have those values.
Shraddha Surana:
So the idea over here was to implement a machine learning model that will be able to mimic the current MACFES model that is present. We used several machine learning algorithms to see and the one that we zeroed down on was deep learning. We got pretty good accuracy for the deep learning model that we implemented and we created three models to predict each of those parameters.
Shraddha Surana:
Now, the main advantage that we had with this was that while the current MACFES model tends to take more of a brute force approach, in the sense that it has millions of templates that it tries to fit through each reading of the galaxy, which takes about 10 minutes per galaxy. Now, once we train a deep learning model for each of these parameters, and the training takes a maximum of 30 minutes for one of the parameters, we can now predict the same parameters for millions of galaxies in just a couple of seconds. So there is a huge savings in terms of time, which will help expedite the research project and the inferences that can be made from these estimations.
Shraddha Surana:
So one of the challenges that we had was to understand why most of the results, so we got pretty good accuracy, the estimates that the deep learning model was predicting, were pretty close to the MACFES model. However, there were some results that were not very similar, that had a stark difference. Now, machine learning models tend to generalize the results or at least that is the way that we try to implement the machine learning model.
Shraddha Surana:
For example, take ohm's law. So if the readings are taken of the resistance, current and voltage and we create a machine learning model, a regression model, it will essentially be able to give us that particular formula. It will generalize, even though some of the readings may not match or adhere completely to the formula, it is a similar thing that we are trying to do over here with the deep learning model, as well that we have implemented.
Shraddha Surana:
So, in such cases where there is a stark difference between the deep learning estimates and the MACFES model estimates, these give us very interesting cases to actually go further and investigate as to why the difference is. Is it something that can be improved in the deep learning model? Or can it enhance our assumptions and modeling of the MACFES model, which in turn might lead us better understanding of these galaxies?
Shraddha Surana:
Yogesh, do you want to add anything?
Yogesh Wadadekar:
Yes. I'd like to add a couple of points to what Shraddha has just said. First of all, I'd like to say how and why we chose the output parameters. So what we are trying to do here is to use machine learning to predict three numbers that characterize the star formation history of the galaxy.
Yogesh Wadadekar:
The first number is the stellar mass, which represents how much mass is contained in the stars that have formed within the galaxy. Obviously, if the star, if the galaxy has formed a lot of stars over its history, the stellar mass will be high. And therefore, the stellar mass is a measure of the integrated star formation history of the galaxy.
Yogesh Wadadekar:
The second number that we'd like to predict is, what is the current star formation rate? Which means how many stars are being formed in this galaxy at the current time? Now, this is completely different, because it's unlike the stellar mass. This is not an integrated quantity. It's a differential quantity, we are trying to measure how many stars are being formed per year in a particular galaxy.
Yogesh Wadadekar:
The third parameter that we are trying to predict is the dust luminosity of each galaxy. The dust luminosity is a number, which depends on how much star formation has happened in the galaxy. Because if you go back before to a time when no stars were formed, there is little or no dust in the galaxy. Galaxies increase the quantity of dust within them. Because dust gets formed, dust which is basically silicates, get formed inside of stars. So it's only when stars evolve and the first generations of stars return their materials to the interstellar medium, do we get dust within galaxies.
Yogesh Wadadekar:
And the dust luminosity naturally depends both on how much dust there is, and how hot it is. If there is a lot of dust and if it's at a high temperature, then the dust luminosity tends to be very high.
Yogesh Wadadekar:
So these are three independent quantities that together helps us understand how and when stars form within a particular galaxy.
Neal Ford:
You're basically saying the more crowded the house is the dustier it is.
Yogesh Wadadekar:
Yes, in some sense, yes. If there are a lot of stars that have been formed already, then it does get more dust here, because those stars evolve, some of them may explode as supernovae, and then they throw out a lot of material into the space between the stars. And then the dust begins to increase.
Yogesh Wadadekar:
The second point I wanted to make was regarding the extremely non-linear dependence between the fluxes that we measure and these output parameters. Unlike the Ohm's law example, that Shraddha mentioned, which is a linear relationship between voltage and current, this one is a very non-linear relationship. So, tweaking one parameter by a small amount can change the output by a very large amount.
Neal Ford:
So this is sensitivity to initial conditions.
Yogesh Wadadekar:
There's a fairly large sensitivity to initial conditions. So it's very important to measure these fluxes as accurately as possible.
Neal Ford:
This is a problem where you decided to use a technique called supervised machine learning, correct? Could you describe what that is and why that approach was chosen?
Shraddha Surana:
Yes. So in this particular case, so actually, broadly speaking, machine learning techniques can be classified into supervised techniques and unsupervised techniques. Supervised techniques is when we have a data where the inputs are matched to outputs.
Shraddha Surana:
So to take a simpler example of common house prices, based on certain factors, such as the number of bedrooms, the carpet area, et cetera, and the price of the house is available to us, that's when we would go for a supervised machine learning approach, where we are telling the model that these are the inputs, and this is the output for it. And hence, in this particular case, where we have to predict these three star formation properties, it was clear from the beginning that we have to use, that supervised learning techniques would be most suitable.
Shraddha Surana:
Because we had the input flux values and we had the corresponding free parameter estimates given by the MACFES models.
Neal Ford:
Okay, so let's talk about the solution to the solar problem. And it actually utilizes a different kind of machine learning. So if you could describe the approach there and how that approach was different than the galaxy problem.
Ujjaini Alam:
Of what outcome we desired, we had all this data, we knew that there must be a lot of physical information in it. But we didn't know what question we were asking. Therefore, in this case, unsupervised learning seemed to be the obvious way to go.
Ujjaini Alam:
And that's when you have a machine learning algorithm, which is trying to draw inferences from a dataset, which has input data, but two labeled responses. The commonest way of doing this is to do some sort of clustering, which means it takes all the data and it tries to find patterns, hidden patterns of groups in the data. And then the expectation is, once you find those patterns, you should be able to look at those patterns and draw some inference.
Ujjaini Alam:
So in this case we had, I'll take a minute to describe the data, again. What we started with was a four minute data cube, which had data every half a second in time and 48 frequency bands. And this was over a 200 by 200 pixel image.
Ujjaini Alam:
So we decided to start off with treating each image as a data point. So we have 22,000 data points over different frequencies and different time slices. Each data point then contained 40,000 pixel intensities and these were the features of the data points. And then we tried to use unsupervised clustering algorithms on these data points.
Ujjaini Alam:
What we found was, firstly, that when you have such a large number of features in the data, that in itself causes a problem. Most unsupervised learning algorithms do not scale up to this kind of large number of dimensions. We used self-organizing maps, we used density based clustering algorithms, and in each case, we found that having so many features was a problem.
Ujjaini Alam:
So we had to take two approaches to that. One was to do some sort of feature selection, find out the feature importances. The other was a more data engineering approach, which was to figure out if we could speed up the processes by using say a different language, C++ instead of Python, or if we used GPUs, whether this would improve the results, speed of the results, et cetera.
Ujjaini Alam:
But then the problem with this was, since the pixels are the features, if you do feature importance, and if it tells you that say pixel number 125 is important to the clustering, that does not necessarily lend itself to a physical interpretation. Because pixel number 125, you're not very clear what that means. So we did have problems. We got very consistent results from various clustering algorithms.
Ujjaini Alam:
But once we had these results, we could not really, physically interpret those results. We couldn't quite figure out why those clusters had formed. We knew that they were forming over and over again, with different methods, but we didn't know what was causing them to form. So then we had to take a step back, and we had to think of how to represent the data in a better way.
Ujjaini Alam:
What we decided was to concentrate on the peaks within the images. So rather than considering the entire image, we considered the peaks in each image. We tried to fit those with Gaussians. We tried to see what information those peaks could give us. And we found that if we took the peaks and followed their time series, and then we tried to cluster those time series, we were getting better results.
Ujjaini Alam:
So, in the end, we ended up using clustering, but in a very different way than we had initially envisaged. And that is something that I think happens a lot with unsupervised learning, because you don't know what question you are asking. You have to often step back and modify your question and keep modifying your methods, based on the results that you get.
Ujjaini Alam:
So this is a work in progress. At the moment where we are is that we are trying to cluster the various peaks in the images into different classes. And we are hoping by doing this, to isolate a specific type of physical process, which are the nano flares. And Divya we would be the better person to talk about what nano flares are. Why are they important in physics?
Neal Ford:
Before we go there, a couple of questions for you. So, there's a famous quote by the artist Picasso that said computers are useless. They can only give you answers, but not questions. But it sounds like you figured out a way to get a computer to give you questions as well, which is really, really useful.
Neal Ford:
And the other thing and this is a broad generalization that I want to, that's translated into layman's terms, and I want to make sure that I'm understanding the difference between these two. So is it fair to say that you would typically use supervised learning if you have a known, unknown problem, and use unsupervised learning if you have an unknown, unknown problem?
Shraddha Surana:
Just to add to that, for our unknown, unknown problem, we would typically go for unsupervised machine learning problems. But you could also use it for known, unknowns as well or unknown, knowns, known, unknowns rather. Because at the end, what unsupervised machine learning algorithms do is to figure out groupings, clusterings and patterns that are present in the data and that can be useful in both the scenarios.
Rebecca Parsons:
It's definitely applicable in many places. We've been using methods like this literally for decades. For example, credit card fraud detection, if you have a particular spending pattern and you aggregate those spending patterns, and then when some anomalous spending arises, it gets flagged. So there are numerous applications for this outside of the world of science and in terms of price predictions, recommendations, et cetera.
Rebecca Parsons:
But I want to get back to the sun. So, Divya, what can you tell me about some of the impacts on your way of thinking about the sun have arisen from some of the results that have come so far?
Divya Oberoi:
Before I go there, let me make some comments about the solar app, the machine learning applications to the solar work. And something which I did not mention before is that not only we have an enormous number of images, individually, these images are very deep. Their dynamic ranges can be as high as 100,000. So the contrast between the brightest and the faintest reliably detected feature could be as high as 100,000.
Divya Oberoi:
And that is about two or sometimes even three orders of magnitude better than what has ever gone before. So that is an enormous part of the phase space, which has never been explored before. We also know that the sun hides many secrets, in terms of what Ujjaini had mentioned as nano flares, which is a very large number of very small events, like small smatterings, or a large number of individual fireworks going on, on the night of Fourth of July. So many, so that you can hear only the rumble and you can't make out the individual firework.
Divya Oberoi:
So, here also, on the surface of the sun, there is this general idea that there is a very large number of individually very small events, which are taking place all the time. And they have just been beneath our sensitivity limit for thus far.
Divya Oberoi:
And there has been a regular attempt or a long standing attempt to go to fainter and fainter events, more and more sensitive instruments, which would allow us to detect them. And now for the first time, we have evidence for having detected some of these in the solar data. And so those tiny Gaussians which Ujjaini was referring to, we believe those are coming from the sites where these very tiny explosions, if you will, are happening and we are just trying to characterize them, to see if they are consistent with our expectations based on the theory.
Divya Oberoi:
And then to get back to the question which Rebecca had asked, that how has this changed or influenced my perspective about solar physics in some ways, I think what it is telling me is that, well, okay, when we started down this path, another reason for me to go for unsupervised learning was to make sure that we were not biasing what we were looking for, just based on our prior knowledge. Because we are in completely uncharted waters, in terms of how faint features can we see. I wanted an algorithm to find for me whatever relationships exist in these data, rather than me directing the algorithm to look for specific relations, which I know must exist.
Divya Oberoi:
In the process of looking at these data, what we have ourselves discovered, not quite using machine learning, but just by staring at these images long enough that there are many, many faint relationships which exist. Relationships between the size of something and its brightness, which vary in some sort of a quasi periodic manner. Things with periodicity is ranging from a few seconds to a few minutes, none of which we knew about earlier.
Divya Oberoi:
Now, we happened to find them, because we happened to be staring at some particular four minutes of data for a long enough time and noticed it. But what it tells me now is that these data are really rich, in terms of what must exist in these data, the various correlated variations, in terms of what is happening to the morphology of that emission, to where it is located, to maybe a small jitter in its motion and to the variation of its amplitude.
Divya Oberoi:
There are good reasons to believe that there is a large number of relationships which exist between various parameters in the emission, which is sitting in these images. And that is what I would love these machine learning algorithms to discover for us.
Rebecca Parsons:
Great, thank you. So, let's talk a little bit about how in both of these instances, you address more unexpected results. I know Ujjaini talked a little bit about how the focus was shifted from all of the data to the peaks. Shraddha was actually talking about some of the ways that we're learning something when the machine learning predictions seem to be off from the model.
Rebecca Parsons:
I wonder if you can talk a little bit about what kind of feedback loop you see between the insights you're getting from the models, and what that is telling you about the physical system. Professor Divya, you were going there a little bit towards the end. But Dr. Yogesh, could you talk a little bit about what we are learning from the perspective of our understanding of the underlying physics of galaxy formation? Has that work been informed by some of the things that you've discovered as you were working to try to increase the effectiveness of the model?
Yogesh Wadadekar:
Yes. So for me, one of the most interesting things are as you pointed out, the failure cases where the machine learning model made a prediction that was way off from what the physics based stellar populations synthesis model gave us. We have only a handful of such objects, wherein the prediction is way off. But the most surprising thing which I found was, when we used the machine learning model, what I had expected was that when you made a joint prediction of stellar mass, star formation rate and dust luminosity together all in one go, one should get a smaller scatter than if you tried to predict each one individually.
Yogesh Wadadekar:
The reason for that is that these are not completely independent parameters. They're coupled to each other in complex ways. So if you try to predict one without trying to predict the other simultaneously, you should get a higher scatter.
Yogesh Wadadekar:
But surprisingly, what we found was that if you predicted each of these parameters separately, the scatter was actually lower than when you tried to do them all together. And this was significantly lower in a statistical sense. So this is something that I still don't understand. That's something I would like to investigate further, why this is happening.
Yogesh Wadadekar:
The other things that I would like to investigate are these outliers and whether they can help us inform the physics. So there are clearly objects where the prediction from the machine learning model doesn't match up with the physical prediction. And we've tried to take a quick look at these objects, but we haven't found anything completely different in these objects.
Yogesh Wadadekar:
So this is something that is very interesting, needs to be done. But we were focused on writing up our work as a research paper and getting it accepted and so on. So we haven't yet looked at these objects, but these are potentially the most interesting.
Yogesh Wadadekar:
Even if it turns out that we cannot understand why there is such a discrepancy, these objects are potentially very interesting. Because they're fundamentally different from the average population in that region of parameter space. So what we've done is, the machine learning tries to get things right on the average, and therefore, it could miss out unusual objects of which it has not seen an example of in its training set.
Yogesh Wadadekar:
So it's very likely that these objects that are outliers in the predictions are actually very unique galaxies whose star formation properties are very different from other galaxies of similar mass and similar star formation properties. So we'd have to look at these objects individually. We haven't done that yet, but that is on our immediate agenda.
Neal Ford:
So could we get the two scientists to remark on how much machine learning and computation in general has changed your fields over the last few years, in the last decade or so?
Yogesh Wadadekar:
I can comment on that. In astronomy, as you know, we study the whole universe. When we study the whole universe, there's a lot of objects to study because it's a very vast universe.
Yogesh Wadadekar:
Also, over the last 80 years or so, new windows on the universe have opened up. So radio astronomy started in the 1930s and '40s. Later on, we had X-ray astronomy, and gamma ray astronomy, and so on. So different kinds of telescopes could be built. Some of them needed to be located in space. And they gathered data, the amount of data that we gathered began to increase.
Yogesh Wadadekar:
So we had innovations in a telescope technology, but that was matched with the continuous growth in the capabilities of computers, in the amount of data that we could gather, the amount of data that we could store, the amount of data that we could process, and so on. Everything has been growing exponentially over the last, not just the last decade, but over many decades.
Yogesh Wadadekar:
The kind of work that we are doing now, as was already pointed out by Divya, depends on data that could not have been gathered in the past. So Divya talked about the MWA, which is a very unique telescope. The kind of data that it gathers was not available a decade ago.
Yogesh Wadadekar:
Similarly, the kind of large catalogs of galaxies on which my work with Thoughtworks depended, requires you to have telescopes that are capable of carrying out large area surveys in different wave bands. And this is a capability that we've only had over the last decade or two. And therefore, this is something that could not have been done before.
Yogesh Wadadekar:
And of course, with the large availability of data, we are facing a very unique constraint in the past, as compared to the past. In the past, when I started my astronomy career 25 years ago, we actually put in a lot of effort to gather data for our research. Now, because of the explosion of technology, both the computer technology and the telescope technology, the data are there for the asking.
Yogesh Wadadekar:
So when we started working on this research project, the gathering of the data, which used to be an effort, which used to take years, is now a five minute job. Basically, you head off to the website, you figure out what dataset you need to download, and you download it.
Yogesh Wadadekar:
Another thing that I wanted to mention, which is unique to astronomy, is that astronomers are possibly the only scientists who have very large amounts of data and are willing and able to share it openly with everyone else. In many other domains, for example, in medical studies and so on, for various reasons, including that there is a lot of money to be made in that profession, it's very hard to get access to data without signing various non-disclosure agreements and so on.
Yogesh Wadadekar:
In astronomy, it's like, oh, you want data? Here's the website. So astronomers not only have a lot of data, they're willing to share it with people. And they go to great lengths to make that data available in a form that people can simply download and use.
Neal Ford:
Okay, we're near about the time limit of what we normally have for length. Does anybody want any last questions or last observations?
Rebecca Parsons:
I just saw Dr. Divya come off of mute and then whoever else was just saying that, so maybe we can give them each a chance to weigh in.
Divya Oberoi:
Sure. Thanks, Rebecca. So what I wanted to say was that the way I got started on machine learning or looking at machine learning for answers to this was that I was working with a student. We picked up a fairly run of the mill kind of an event which takes place on the sun and said that, okay, we'll put it under a microscope. And by under a microscope, I really mean put it, observe it using our telescope in such excruciating detail that nobody has ever done it before.
Divya Oberoi:
And what we found there surprised us, in the sense that we found relationships between various aspects of this burst, which we never knew existed. And then as we were working on it, we found that, hey, there is something else which is going on, not so far away from this one. Let's look at that as well.
Divya Oberoi:
And when we did that, we found a completely different zoo of animals there, where again, there existed relationships, which were very different from what we found in the original event. And the process of really figuring all of this out and understanding them took us better a part of two years. And all of this is happening in just four minutes of data.
Divya Oberoi:
So it really struck me that there is so much richness in these data. So many things are happening in these data, that it is probably going to be very hard for the human mind to appreciate all of them, to wrap one's head around all of them, and then figure out what these are telling us.
Divya Oberoi:
So it became imperative to me to look for things from the machine learning, AI sort of world to at least help us identify what relationships exist. And then we use our existing knowledge of physics to figure out what it is telling us about the sun.
Shraddha Surana:
I had two points that I wanted to highlight. Having worked in some of the business problem statements earlier and now working specifically for research.
Shraddha Surana:
I felt there were two things that were starkly different. I think the first that I want to highlight is the explainability and the reasonability of the problem statement. I think this is very important when we are approaching research problem statements, because the idea in this particular case is not only to build a model to do something well, but also be able to understand what is happening behind the scenes.
Shraddha Surana:
So, for example, understand the relation between the input values and the output values like in star formation histories and when they are different from the current model, to really be able to understand and explain why that is. This is very different from some of the business problem statements where, for example, if there is a phase detection problem statement.
Shraddha Surana:
In those cases, we are mostly interested in optimizing the model, and not very much bothered with why the model is behaving the way it is. So this is one thing that I wanted to highlight. And of course, this is also important in the unsupervised learning problem statement that we are doing for the solar images, which is to be able to explain what is happening in the data. Needless to say, I feel once we master this in the research aspect, it has direct usefulness for any business problem statements as well.
Shraddha Surana:
The second thing that I wanted to highlight was the vagueness of the problem statement. So, for example, for the radio solar imaging problem that we have, which is an unknown, unknown problem statement, and it's quite vague actually. So, which is very different from most business problem statements that I have worked with, which was, for example, optimize my product prices or create chatbots or identify customer churns, which have a concrete problem statement or at least a direction that I want to be able to optimize my supply chain or something.
Shraddha Surana:
So this is very different, which is here is data. We know from past experience that this sort of data has something useful in it. We want to be able to bring out that usefulness faster than usual. Because many humans looking at it takes that much more time and that much more humans. And that is where we want to be able to bring in machine learning models, which can at least dig into the data and give some direction where we can explore further. Explore with other statistical methods or with machine learning itself.
Shraddha Surana:
It's more like finding a needle in the haystack, and I'm pretty optimized that we will be able to find something. And that's where the excitement lies for me. So these are the two things I wanted to highlight, the explainability and reasonability that is required and the vagueness that we have to deal with.
Shraddha Surana:
And I think this also has direct business implications, because I do hear colleagues mentioning that we have clients saying that this is the data, figure something out. I think if you master that here, we'll be able to implement it in many places.
Yogesh Wadadekar:
I just wanted to say that astronomers have now started to look at machine learning seriously, not because they like machine learning, but because they simply have no choice. The amount of data that we are generating from the present generation telescopes, as well as the data that we will generate over the last decade is so huge, that it's simply impossible for a human to delve into these data and gather all the scientific insights. There's simply no choice but for us to automate these things in various ways.
Yogesh Wadadekar:
And machine learning is one of the ways in which we can look for the most interesting, physically most interesting objects in the vast datasets that we collect. So unlike many other fields, we are not just interested in the needles in the haystack, but we are also interested in the haystack as a whole. We're interested in doing statistics with all the objects that we observe. We're also interested in individual, unusual objects that we never looked at before.
Neal Ford:
It seems like astronomy is the latest scientific discipline who's realized that they eventually become a data driven discipline, at least in part. Biology went through that and your observation about the amount of data that's available, essentially forces astronomy to start becoming a data intensive and a compute intensive field, at least partially.
Yogesh Wadadekar:
Yes. It's even more severe in astronomy, because in fields like biology, the data are growing fast. But the number of people looking at the data is also growing very rapidly. The number of astronomers in the world is relatively stagnant.
Rebecca Parsons:
Well, hopefully we can change that and get more people interested in astronomy, or at least computational astronomy.
Yogesh Wadadekar:
Absolutely. Sure, sure. Because astronomy is such an open field, there is a lot of room for people who are not professional astronomers to come and look at astronomical data and look for things that we are not geared to look for, especially for the unknown, unknowns, there's a lot of room to make serendipitous discoveries that us professional astronomers will not make because they're simply not looking... They know what they're looking for and they're only looking in a particular direction, in a particular way. But somebody who's completely unbiased, might be able to make discoveries that would have been missed by professional astronomers.
Neal Ford:
So instead of burgeoning astronomers making their own telescope at home, maybe they should be learning machine learning and algorithms and making scientific discoveries in astronomy that way.
Yogesh Wadadekar:
Absolutely, absolutely. And this is something now that can be done by anyone, sitting anywhere. You don't have to worry about the weather, because so long as your internet connection is up, there's a lot of science that can be done by mature data scientists in the field of astronomy.
Rebecca Parsons:
So in the chat, Prasana has raised the question of data engineering, so Shraddha, Ujjaini, is there anything in particular from a data engineering perspective? Yogesh just talked a great deal about the sheer volume of data. But are there things just from an engineering perspective and dealing with the data?
Rebecca Parsons:
I know Divya, you referenced that when you were talking about focusing initially on all of the data, and then just looking at the peaks. Anything interesting from a data engineering perspective that we should mention?
Ujjaini Alam:
I talked a little bit about this when I talked about the problem. So when you have a large amount of data, and a large amount of features in that data, there's two ways to deal with that problem. One is from a data science perspective, you try to reduce the number of features, you try to just look at only part of the information that is important. Feature selection, feature importance, calculation, those kinds of things.
Ujjaini Alam:
But there is also, as your dataset becomes larger and larger, it becomes a data engineering problem. At the moment, we are looking at four minutes of data for a particular dataset. The full dataset is 70 minutes, which we have not looked at as of now. But if and when we have to look at that 70 minutes of data, and we have to apply the algorithms we are applying right now, then we have to do some major refactoring to our algorithms. And that would be from a data engineering perspective, where you look at a different language to speed up the process, when you look at GPUs.
Ujjaini Alam:
So, that is something we have partially worked on. We wrote a self-organizing map algorithm in C++ in order to speed it up when we initially had problems. It is something that as the dataset gets bigger and bigger, we have to deal with it from a data engineering perspective, not just a data science perspective. We have to think of it in terms of creating pipelines to deal with these huge amounts of data, rather than just the data science part.
Shraddha Surana:
For the star formation histories problem statement, although the data did have lacks of records, we didn't have a requirement of having a computation intensive processor or having any pipelines. So this can be treated as like a total data science problem.
Yogesh Wadadekar:
One more thing I wanted to add, these two problems, I believe, are just the beginning. When we started working with Thoughtworks, we astronomers at NCRA came up with about a dozen different problems where a machine learning approach could be applied in the astronomy domain. And we asked our partners in Thoughtworks to select one or two of these problems to get started with, and they happened to choose these two problems.
Yogesh Wadadekar:
But we have many more problems on which such an industry academic partnership could be usefully employed, in order to tackle those.
Neal Ford:
Okay, well, I want to thank all of our guests today, both Thoughtworks and our scientists for giving us this great insight into machine learning, and how it is being utilized in the real world, including a great example I think of the difference between supervised and supervised machine learning.
Neal Ford:
I wanted to mention Thoughtworks Engineering for Research is organizing 2020 symposium on the theme of the role of artificial intelligence in scientific discovery, will AI ever win its own Nobel prize? That will be in Pune, India. It was originally scheduled for June of 2020, but is going to be rescheduled for a date yet to be announced. So, keep an eye out for that. That should be fascinating.
Neal Ford:
So thanks very much for our guests and for Rebecca.
Rebecca Parsons:
I would like to add my thanks to Dr. Yogesh, Dr. Divya, and Shraddha and Ujjaini from Thoughtworks for this fascinating discussion.
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