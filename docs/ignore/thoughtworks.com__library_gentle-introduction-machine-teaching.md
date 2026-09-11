<!-- Source: https://research.thoughtworks.com/library/gentle-introduction-machine-teaching | Title: A gentle introduction to machine teaching | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# A gentle introduction to machine teaching
By 
Published: September 01, 2021  | Last updated: September 25, 2024
### What is machine teaching?
Despite its widespread popularity, AI still has [yet to pay off for more than 10% of companies that have adopted it](https://sloanreview.mit.edu/projects/expanding-ais-impact-with-organizational-learning/). According to the MIT Sloan study, to properly reap benefits from AI - organizations must find ways to bring humans and machines closer together, a concept they call "organizational learning." Concretely, when most enterprises start adopting AI strategies, the first set of use cases targeted are the lowest hanging fruits. These are typically problems where the data is readily available and in a form where a model can be easily trained (e.g. customer support triage, social media sentiment analysis, customer segmentation for marketing), but are rarely the highest value use case in the organization. When thinking about where AI can provide the most value, typically [the most successful enterprises focus on augmenting subject matter experts](https://hbr.org/2019/04/using-ai-to-make-knowledge-workers-more-effective).
This poses a problem for most organizations, as applying AI to augment domain experts requires those very same experts to be involved in training those models. For example, a large healthcare organization might target one of their highest value use cases: building an AI to help diagnose a few specific cancer strains. For the AI to be able to complete the task, it must be trained on hundreds of thousands of well-labeled examples produced by experts like oncologists and radiologists. This process is cost-prohibitive for most organizations, as experts are scarce resources and can't be diverted to labeling data full time for months on end. "Organizational learning" makes room for experts and machines to not only work together but also learn from each other over time, and the team at MIT that conducted the survey indicate that this mutual learning between human and machine is essential to success with AI. Doing this right, however, is difficult as it increases the demand on already scarce subject matter experts without ever addressing the core issue: there are not enough experts in an organization to have them both label data and perform their typical day to day tasks. 
Machine Teaching, a field of study that has [been gaining popularity recently](https://blogs.microsoft.com/ai/machine-teaching/), is focused on addressing the bottleneck of domain expertise in AI. While classical Machine Learning (ML) research focuses on optimizing the learning algorithm or network architecture, Machine Teaching (MT) focuses on making the human more effective at teaching the model. While a "smarter student" (new innovation in model architectures) could learn the expert's context faster and with fewer examples than the "average student", these types of innovations are rare and unpredictable. On the other hand, a more effective "teacher" (a single domain expert doing the work of hundreds) can have an outsized impact in practically any AI/ML context regardless of how sophisticated the "student" is. 
While the expertise bottleneck is by far the biggest limiting factor currently facing AI/ML implementations today, there are other major obstacles in the current ML workflow that prevent organizations from seeing value come back from their investments. Productivity for ML scientists is lower than it could be as [the ML workflow is inherently disjointed and often rife with debt](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf). It is near impossible to stay agile in the face of model drift, as drifting models require fresh data for retraining - constantly draining time from expert labelers to maintain legacy pipelines. Finally, current ML processes don't lend themselves naturally to explainability - what happens when your training set is biased but you can't ask your labelers  _why_ their labels were biased (because there are too many labelers, no record of which labelers produced a set of labels, or they are no longer part of the organization)?
### Productivity
Software engineers have long touted the importance of “flow state” when programming, but this concept is missing in data science workflows. For instance, before you’re even able to start building a model, you first need labeled data to dig into. Once a project is defined, you may have to wait weeks for data to be annotated. This labeling process is the slowest part of the workflow, yet you can do nothing until it’s completed. 
“You’re never done labeling” is a common expression muttered angrily by ML experts. Even after your model is built and deployed, the labeling never ends. Models don’t stay static forever - their performance degrades over time due to changes in the environment (which is called drift). Typically, models are retrained periodically to counteract the effects of drift - but how do you measure the model drift itself? You could track statistical measures (e.g. [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence), [Jensen-Shannon divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence), or the [Kolmogorov-Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)) for your input and output spaces, but these statistics are difficult to interpret without having concrete labeled data to reference. Ideally, you would assess model performance in production the same way you would during development - by looking at metrics like precision, accuracy, recall, etc. but all of these measures are comparisons between predictions of the model and a labeled baseline. In your development environment you would use your validation set as the baseline, but in production the only way you can generate a baseline is by labeling a sample of your production traffic periodically. This process is difficult to scale, as each production model would require a constant ongoing investment of human effort for maintenance.
Simply put, labeling is the most frequently re-visited step in the workflow and causes compounding slowdowns throughout the process. Since labeling takes time when performed manually, the current ML workflow is discontinuous and doesn’t lend itself well to flow states.
### Agility
What happens when the concept of what you are trying to predict changes? For example, if you’re building a classifier for personally identifiable information (PII) based on rules or regulations, what happens when those regulations change and include a brand new type of PII? 
What about when the input space shifts? For example, let’s imagine you work in the data science team of a popular email service, and your team manages a model that detects spam for all of your users. Your team worked diligently to build a model that takes many features into consideration, and it did a great job of finding spammers. Over time, however, you notice that the model’s performance degrades and false positives/negatives start piling up. It’s possible that your users’ behaviors have changed - maybe your users like your email client so much that they’re emailing much more frequently than they did before. Maybe spammers are making changes to their tactics to make prediction much harder. 
To overcome both of these issues, you would need to relabel data and retrain your models, but how often should that be done? How early do you need to start creating training data? The relabeling and retraining process takes weeks of work, delaying the speed with which organizations can adapt to changes. For acute changes in the world (like when COVID-19 became widespread), being able to react quickly is key and is not currently something that ML workflows are currently well adapted for.
### Explainability
Explainability in model development pipelines is something that most Machine Learning practitioners can likely appreciate. There are various ways to provide explainability at the model level - for instance, by using Shapley Values or by using an inherently interpretable model to begin with, but bias is typically introduced in the training data itself. If labelers hold biases or if the way the data was sampled introduces some skew, models tend to pick these up. Using the plethora of methods to achieve model explainability, we can diagnose model biases and find issues in the training data - but how do we explain the labels in the data?
As useful as it is to point to bias and skew in the data, it's more helpful to be able to get to the why - why did the labelers indicate that this particularly hateful tweet isn't toxic? Why did the labelers mislabel this credit application from a minority? Currently, the only way to get this level of explainability is to physically ask the labelers why they applied a particular label - but it's impossible to do this well. Labeling teams see churn, labelers may not be paying full attention because they're trying to get through the task quickly, and labelers sometimes just make mistakes. All of these factors make it difficult to nail down the root causes of poor labels, and ultimately prevent data teams from quickly fixing problems with their models.
### Use case coverage
As mentioned earlier, the biggest reason why most enterprises don't see value come back from their investments in AI is that their highest value use cases are massive time sinks for their subject matter experts. Today, the most impactful ML/AI solutions are typically considered too difficult or expensive to even attempt due to labeling the data. For example, if you wanted to build a model to detect a specific type of cancer in MRI images - you would need an army of radiologists and oncologists on staff to provide their expertise in the form of labeled data. There's no doubt that this model would be incredibly valuable if built, so the argument for building the model is straightforward from an impact standpoint. However, an organization might only have a handful of these experts, and their time is too valuable to spend on data labeling. As a result, the business case is dead in the water despite the apparent value the project would bring to the table should it be successful.
Every vertical suffers from this issue - subject matter expertise is expensive, therefore the most valuable models are difficult or impossible to justify building. The easiest to build models are rarely the most helpful, and so many organizations end up spinning their wheels trying to get AI to provide meaningful impact.
### Properties of machine teaching solutions
By shifting the focus to making machine teachers more effective, we can more effectively target the human bottleneck in the workflow and solve for all four of the above problems. An effective machine-teaching solution requires the following attributes to lower the costs introduced by human effort significantly:
  1. **Simple data exploration**


Domain experts should easily traverse their data to help them discover patterns and elicit their knowledge.
**2. Expressive interfaces to capture knowledge and context**
As the domain experts interact with the data, they should capture patterns and context that they may have come across. For example, a user might want to define a regex or another function that roughly approximates the shape of data that a particular label belongs to.
**3. Tight feedback loops**
While working, the domain experts should be getting guidance from the platform on how they can be using their time most effectively. This guidance may come as feedback about the patterns they've come across so far, or as recommendations from the platform about where they can be spending more time to maximize their impact.
**4. Automation as a core pillar**
Ultimately, the labelers should only be necessary until the point where the system can take over. The ongoing cost of maintaining a pipeline should be near zero.
**5. Explanations and interpretations**
Since automation is being leaned upon heavily, a useful machine teaching platform must be entirely explainable. These systems are used to bootstrap and train models that live in production environments, so being able to diagnose "why a label is Y1 instead of Y2" and act on it is vital.
**6. Separation of duties between ML experts and domain experts**
Sometimes the "Domain Expert" in this case is a machine learning practitioner, but many times it's not. It's essential to separate the two concerns - subject matter experts should focus on providing their subject matter expertise. At the same time, ML practitioners should focus on the actual ML work necessary to learn from that subject matter expertise. 
Applying this framework to the problem statements above paints us a good picture of the impact Machine Teaching can have on our existing workflow.
**Productivity**
  * Instead of having an army of labelers, have one or two subject matter experts available as labelers.


  * Instead of labeling taking weeks, it can take hours or days, leaning heavily on automation.


**Agility**
  * As environments shift, the cost of adjusting the distilled context in the platform should be negligible. If the definition of a class changes, or if the input space drifts, it should be trivial to adjust the platform to reconcile.


**Use case coverage**
  * Since large numbers of domain experts aren't necessary in a Machine Teaching workflow, it's easy to unlock otherwise cost-prohibitive use cases. Have a single expert spend a few hours bootstrapping the system until the automation starts kicking in. At that point, only spot-checking is necessary to deal with production model drift over time. 


**Explainability**
  * Since explainability is a required core feature of Machine teaching platforms, we can get more in-depth explanations than just at the model level. We should easily find incorrect labels and quickly figure out  _why_ they are wrong (did someone distill a concept incorrectly? Did the environment shift? Does the platform need more signal to understand the class better?)


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
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://research.thoughtworks.com/about-us/privacy-policy)
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