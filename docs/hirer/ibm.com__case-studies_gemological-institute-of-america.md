<!-- Source: https://www.ibm.com/case-studies/gemological-institute-of-america | Title: Gemological Institute of America | IBM | Seed: https://www.ibm.com/consulting (IBM Consulting) -->

Support
  * [OverviewResolve product issues with self-service tools](https://www.ibm.com/mysupport/s/?language=en_US&lnk=flathl)
  * [CommunityShare knowledge in a collaborative environment to unlock innovation](https://community.ibm.com/community/user/community?lnk=flathl)
  * [DeveloperAccess digital resources, code samples and code trials](https://developer.ibm.com/?lnk=flathl)
  * [DocumentationUnderstand, develop and deploy our products with comprehensive technical resources](https://www.ibm.com/docs/en?lnk=flathl)
  * [IBM Cloud platformAccess subject matter experts and content to address questions and issues about IBM Cloud](https://www.ibm.com/products/cloud/support?lnk=flathl)
  * [ImplementationDrive better business outcomes with an experienced team of IBM product experts](https://www.ibm.com/products/expertlabs?lnk=flatitem)
  * [TrainingDevelop your skills with premiere educational offerings and credentials](https://www.ibm.com/training/?lnk=flathl)
  * [Technology Lifecycle ServicesElevate your support experience with a holistic approach to data center management across your IT environment](https://www.ibm.com/services/technology-lifecycle-services?lnk=flathl)


My IBM  Log in 
#  A new way to sparkle 
GIA and IBM team up to revolutionize the diamond industry 
The Gemological Institute of America (GIA) introduced the first high-quality jeweler’s loupe in the 1930s. Small enough to be held in one hand, the loupe magnifies stones 10x, allowing jewelers and gemologists to inspect them for color and clarity. The loupe revolutionized gemology, and it is still widely used today.
A spirit of discovery and innovation continues to drive GIA, so it’s no surprise that the organization embraced the idea of artificial intelligence (AI) as an ideal way to optimize the diamond grading process. Pritesh Patel, Chief Operating Officer at GIA, explains: “We’ve brought a lot of different instruments into this industry over the years, and we solved the problems of cut, carat weight and color a long time ago. Clarity was the last frontier, and AI was the key to conquering it.”
## **High capacity**
4Million diamonds analyzed by GIA per year
## **Extensive AI usage**
Stones expected to be analyzed using the AI-based solution 70%–80%of all diamonds
We’ve brought a lot of different instruments into this industry over the years, and we solved the problem of automating cut, carat weight and color a long time ago. Clarity was the last frontier, and AI was the key to conquering it. 
Pritesh Patel  Chief Operating Officer  Gemological Institute of America 
With that in mind, Patel approached [IBM Research®](https://www.research.ibm.com/) with a vision: with the right skills and technology, Patel believed it was possible to harness the power of AI on the cloud to grade the clarity of diamonds.
IBM Research agreed, and the two organizations began developing a strategic partnership: GIA provides the specialized imagery along with data from tens of millions of diamonds examined by its diamond experts; IBM provides the AI capabilities and the computing power. The result of that partnership is GIA’s cloud-based AI approach to diamond grading.
Rethinking the process 
##  Rethinking the process 
Evaluating the clarity of a diamond is a complex process. Using a loupe, a microscope or an image, gemologists meticulously examine each diamond for inclusions—tiny characteristics trapped in the stone’s structure. Inclusions can be miniscule internal spots or cracks penetrating into the stone from the surface.
Flawless diamonds—those without any inclusions—are exceedingly rare. Less than half a percent of all diamonds graded by GIA in the world fall into this category. The vast majority of diamonds have one or more inclusions that, taken together, make each stone unique.
After IBM Research developed a successful proof of concept (POC) showing that AI can indeed help automate the diamond grading process, the [IBM Global Cloud Acceleration Team](https://www.ibm.com/consulting/cloud) (GCAT) stepped in and shepherded the project along to the next stage. The GCAT team partnered with the GIA Engineering DevOps team to guide the solution from the POC into a production-ready environment with separate development, testing, production and disaster recovery clusters.
Today, the solution is well into its testing phase and on the way to full production. GIA labs upload specialized images of each diamond to an [IBM Cloudant®](https://www.ibm.com/products/cloudant) database housed on the [IBM Cloud®](https://www.ibm.com/cloud). The system’s middleware layer is made of an [IBM Cloud Kubernetes Services](https://www.ibm.com/products/kubernetes-service) cluster. Says Patel, “we decided to use IBM Kubernetes Services because it gives us the flexibility and the computing powers to process a very high volume of data.”
GIA’s cluster is composed of three NVIDIA K80 GPUs, each of which has one shared virtual node and one bare metal node in a serverless architecture. NVIDIA GPUs are uniquely suited to GIA’s needs because of their ability to process high-resolution imagery quickly, helping speed up the entire process. They can also reduce the time required to validate AI algorithms.
The new solution analyzes each diamond using two custom algorithmic models. The autoplot AI model creates a visual representation of the diamond’s inclusions, and the grading model assesses the diamond’s overall grade. This information is then sent to GIA’s gemologists on an iPad application, where they can evaluate the autoplot and, if necessary, make changes. Those changes are then fed back into the system to re-evaluate the grade and can be used to retrain the AI model to improve accuracy.
Protecting the process 
##  Protecting the process 
GIA’s mission to protect consumers is the driving force behind the idea for their innovation. But GIA had another goal for the project: to achieve the highest levels of data security to protect the integrity of diamond grading. Diamonds are a high-value commodity, and protecting the grading process was of paramount importance. [IBM Cloud App ID](https://www.ibm.com/products/app-id) helps ensure that uploading and processing the diamond images are done with advanced security capabilities, including multifactor authentication, single sign-on and user-defined password policies. 
“The transmission of the data from our premises to the cloud is very secure,” says Patel. “The algorithm that does the work in the cloud needs to be protected like the formula for Coca-Cola. Everything that we have built in our architecture is designed to ensure the security and integrity of the entire end-to-end process.”
The images are stored using [IBM Cloud Object Storage](https://www.ibm.com/products/cloud-object-storage), a cost-effective storage solution that meets all of GIA’s requirements for scalability and accessibility. IBM Cloud Object Storage also offers built-in encryption and policy-enabled, lockable, write once read many (WORM) storage.
Throughout the engagement, the [IBM Strategic Embedded Partnerships](https://www.ibm.com/partnerplus) (ESA) team has been on hand to develop a mutually beneficial strategic partnership between the two companies. Not only does the ESA team provide continuity and support from a business perspective; it also helped establish the legal and business structure that serves as the bedrock for this type of partnership.
A brilliant future 
##  A brilliant future 
GIA grades millions of diamonds per year. Patel expects the new solution to handle 70–80% of those evaluations, primarily focused on the smaller sizes of diamonds submitted, allowing human graders to focus on the more complicated cases where a human evaluation is critical to determining the grade.
But getting to that point will take time. Right now, GIA is using the solution in 2 of its 11 labs, performing AI and human evaluations in parallel as the team refines the algorithms. Eventually, thanks to continued support from the GCAT team, GIA intends to make the new solution available in all of its labs.
Although the solution is still in its early stages, Patel can see several major benefits on the horizon. The first, he says, is efficiency. “As we automate the many steps that each diamond goes through, we will significantly improve turnaround time for our customers.”
The solution will also bolster both accuracy and repeatability. Even though human diamond graders go through a training course of rigorous instruction, they work within the limits of their physical senses. When two graders look at the same diamond, their evaluations might differ in some very small way. With AI, those slight differences will be virtually eliminated, helping to ensure that diamonds are valued accurately when they reach the marketplace.
GIA is staking its reputation on the integrity and accuracy of the new solution. Just as introducing the jeweler’s loupe into the diamond grading process transformed the industry in the 1930s, this project will introduce a whole new level of precision to the process.
“IBM has the expertise in AI and cloud computing to really bring this whole project together,” says Patel. “That’s why GIA chose to work with IBM in this particular space: we are both leaders in our respective fields and it was imperative to collaborate with IBM to ensure the best possible results on this very important strategic initiative for GIA.”
**[Learn more](https://www.linkedin.com/posts/gia_how-is-ai-technology-transforming-diamond-activity-6697607005172973568-IYqh/) (link resides outside of ibm.com) as GIA CMO Mark Buntz interviews GIA COO Pritesh Patel on how this cutting-edge collaboration with IBM benefits consumers, graders, and the industry.**
All images and video © GIA
About the Gemological Institute of America 
##  About the Gemological Institute of America 
Founded in 1931, the [Gemological Institute of America](https://www.gia.edu/) (link resides outside of ibm.com) is a non-profit institute dedicated to the study and evaluation of precious gems and pearls. In addition to providing world-class analysis and grading, GIA educates aspiring gemologists and is considered a world leader in gemological research. GIA is based in Carlsbad, California, and employs 2,500 gemologists. 
Solution components  IBM Cloud®  IBM® Cloudant®  IBM Cloud App ID  IBM Cloud Kubernetes Services  IBM Cloud Object Storage  IBM Global Cloud Acceleration Team  IBM Research®  IBM Strategic Embedded Partnerships Team 
Take the next step
To learn more about the IBM solutions featured in this story, please contact your IBM representative or IBM Business Partner.
  1. [ View more case studies ](https://www.ibm.com/case-studies/search)
  2. [ Contact IBM ](https://www.ibm.com/contact)


Abu Dhabi National Oil Company 
Enhancing accuracy, consistency and speed of rock analysis
[ Read the case study ](https://www.ibm.com/case-studies/abu-dhabi-national-oil-company-adnoc)
IBM Blog 
8 Kubernetes Tips and Tricks
[ Read the blog ](https://www.ibm.com/blog/8-kubernetes-tips-and-tricks/)
#####  Legal 
© Copyright IBM Corporation 2021. IBM Corporation, IBM Cloud, New Orchard Road, Armonk, NY 10504
Produced in the United States of America, March 2021.
IBM, the IBM logo, ibm.com, IBM Cloud, IBM Cloudant, and IBM Research are trademarks of International Business Machines Corp., registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on the web at [ibm.com/legal/copyright-trademark](https://www.ibm.com/legal/copyright-trademark).
The performance data and client examples cited are presented for illustrative purposes only. Actual performance results may vary depending on specific configurations and operating conditions. THE INFORMATION IN THIS DOCUMENT IS PROVIDED “AS IS” WITHOUT ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING WITHOUT ANY WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND ANY WARRANTY OR CONDITION OF NON-INFRINGEMENT. IBM products are warranted according to the terms and conditions of the agreements under which they are provided.
Statement of Good Security Practices: IT system security involves protecting systems and information through prevention, detection and response to improper access from within and outside your enterprise. Improper access can result in information being altered, destroyed, misappropriated or misused or can result in damage to or misuse of your systems, including for use in attacks on others. No IT system or product should be considered completely secure and no single product, service or security measure can be completely effective in preventing improper use or access. IBM systems, products and services are designed to be part of a lawful, comprehensive security approach, which will necessarily involve additional operational procedures, and may require other systems, products or services to be most effective. IBM DOES NOT WARRANT THAT ANY SYSTEMS, PRODUCTS OR SERVICES ARE IMMUNE FROM, OR WILL MAKE YOUR ENTERPRISE IMMUNE FROM, THE MALICIOUS OR ILLEGAL CONDUCT OF ANY PARTY.
Products Consulting services Industries Case studies Financing Research LinkedIn X Instagram YouTube Podcasts Business partners Documentation Events Newsletters Support TechXchange community Overview Careers Investor relations Leadership Newsroom Security, privacy and trust United States — English Contact IBM Privacy Terms of use Accessibility
IBM web domains
ibm.com, ibm.org, ibm-zcouncil.com, insights-on-business.com, jazz.net, mobilebusinessinsights.com, promontory.com, proveit.com, ptech.org, s81c.com, securityintelligence.com, skillsbuild.org, softlayer.com, storagecommunity.org, think-exchange.com, thoughtsoncloud.com, alphaevents.webcasts.com, ibm-cloud.github.io, ibmbigdatahub.com, bluemix.net, mybluemix.net, ibm.net, ibmcloud.com, galasa.dev, blueworkslive.com, swiss-quantum.ch, blueworkslive.com, cloudant.com, ibm.ie, ibm.fr, ibm.com.br, ibm.co, ibm.ca, community.watsonanalytics.com, datapower.com, skills.yourlearning.ibm.com, bluewolf.com, carbondesignsystem.com, openliberty.io 
About cookies on this site Our websites require some cookies to function properly (required). In addition, other cookies may be used with your consent to analyze site usage, improve the user experience and for advertising. For more information, please review your [cookie preferences](javascript:void\(0\)) options. By visiting our website, you agree to our processing of information as described in IBM’s  [privacy statement](https://www.ibm.com/privacy).  To provide a smooth navigation, your cookie preferences will be shared across the IBM web domains listed [here](https://www.ibm.com/case-studies/gemological-institute-of-america#truste_domain_list). 
Accept All More options