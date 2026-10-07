<!-- Source: https://www.ibm.com/case-studies/fnz-uk | Title: FNZ (UK) Ltd. | IBM | Seed: https://www.ibm.com/consulting (IBM Consulting) -->

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
#  A series of successes 
IBM Power Systems Virtual Server helps FNZ upgrade its approach to testing—and more 
Sometimes a single, successful change can bring about a series of related victories. Just ask John Cullen, Chief Technical Architect in the Asset Management Infrastructure Division of FNZ (UK) Ltd., a financial services company based in Edinburgh, Scotland.
Several years ago, Cullen and his team began to automate software testing with the goal of improving the speed with which they could roll out new releases of their core digital wealth management platform, Figaro. It worked—they were able to shave days off their test cycles.
But the testing team was sharing a logical partition (LPAR) with the development team, and over time their successful testing strategy started to slow down important software development. Cullen and team tried to address this by running their tests after business hours, but that proved to be less than ideal.
“We would make a change, wait for the test to run overnight, find out we’d introduced a bug, fix it, wait for the test to run overnight … over and over, to the point where we were starting to slow down our own processes—the opposite direction from where we wanted to go,” explains Cullen.
## **Server set-up**
FNZ can spin up a new virtual server in as little as 10minutes
## **Faster testing**
With the new platform, FNZ can complete tests at least 15xmore quickly
All we have to do is find the right image, spin it up, run the tests and we’re done. 
John Cullen  Chief Technical Architect, Asset Management Infrastructure Division  FNZ (UK) Ltd. 
Next, the team considered creating a separate, dedicated LPAR for running tests. “That would no doubt have solved our problem, but it wouldn’t have been cost effective and it wouldn’t have been scalable,” says Cullen. “We want to keep adding more tests, so we needed a proper, cost-effective solution that would address the scalability problem.”
Cullen found that solution with IBM Business Partner CSI Limited’s test-as-a-service platform, which runs on [IBM® Power® Systems Virtual Server](https://www.ibm.com/products/power-virtual-server).
A powerful, scalable solution 
##  A powerful, scalable solution 
Figaro is a very large system, with millions of lines of code, thousands of tables and about 25,000 program objects. Historically, it has run on IBM i on Power servers, so the move to IBM Power Systems Virtual Server was natural. But there’s more to Cullen’s choice than finding the right combination of server and operating system.
With IBM Power Systems Virtual Server and CSI’s test-as-a-service offering, Cullen and team have as much compute power as they need, when they need it. “With this setup, we can request a virtual server with the required version of Figaro and the appropriate data set, run our tests against it, then delete the virtual server,” Cullen says.
The ability to access the right version of Figaro is key. FNZ’s current release schedule calls for new versions of the software every quarter, with patches every two weeks. For testing to be efficient and cost-effective, Cullen’s team needs to be able to spin up an accurate, up-to-date version of the software on an as-needed basis. “We don’t want a situation that in order to run a test, which might only take 15 minutes to execute, we have to install reams and reams of patches to get a working environment—it all has to be prebuilt,” he says.
To accomplish this, the team relies on a Docker-style approach, which use layers to build images. “You have a known starting point, and you add layers on top. We took the stock IBM Power images and gradually layered on more and more configuration software until we had a fully working environment,” explains Cullen.
Now, Cullen’s team has automated the entire image building process to keep everything up to date, using a watcher program to identify newly published artifacts. “Say we want to upgrade from version 1.2 to 1.3 of our system. When we push the version 1.3 patch to the artifact repository, the watcher sees that, then spins up the previous version on a virtual machine, installs the version 1.3 patch, saves the results and deletes the virtual machine.” 
As a result of this process, FNZ always has a test-ready environment. “All we have to do is find the right image, spin it up, run the tests and we’re done,” says Cullen.
Plus, with the Docker-based approach, if anything in the intermediary layers changes, they don’t have to rebuild any of the surrounding layers. “It’s quite efficient,” notes Cullen.
The CSI solution also takes advantage of the [IBM Cloud Pak®](https://www.ibm.com/products/cloud-paks) multicloud management technology, which runs on [Red Hat® OpenShift®](https://www.redhat.com/en/technologies/cloud-computing/openshift). Specifically, the offering’s cloud automation management capabilities help FNZ organize, templatize and parameterize Terraform system definitions, while [Red Hat Ansible®](https://www.redhat.com/en/technologies/management/ansible) automation scripts fully deploy the application.
One of the main reasons we wanted to look at an IBM Cloud solution rather than something that would just fix our short-term problem was to be able to stand up new instances of our software for different purposes. IBM Power Systems Virtual Server is going to enable us to do that. 
John Cullen  Chief Technical Architect, Asset Management Infrastructure Division  FNZ (UK) Ltd. 
Plenty of possibilities 
##  Plenty of possibilities 
Today, Cullen and his team have accomplished more than their original objective of increasing the rate at which FNZ releases new versions of Figaro. They’ve created a robust automated testing environment that allows them to spin up new machines in as little as 10 minutes and then run multiple tests in parallel or in sequence. As a result, FNZ can carry out tests in the new environment at least 15 times faster than it could previously. 
The environment also provides them with easy access to up-to-date software and the right amount of computing power without having to pay for anything they don’t need. In fact, the IBM Power Systems Virtual Server can cost as little as GBP 100 per day.
Cullen confirms that FNZ is well on its way to a future in the cloud. “Now that we’ve got a solution that works for our testing group to automatically spin up Figaro environments on demand, we can use that for our development teams. They need their own dedicated environments for doing testing, particularly if they’re doing performance testing where they need an environment that’s separated off and not affected by other activity that’s happening within the system,” he explains.
Cullen has other uses for the IBM solution in mind, including the possibility of offering a similar solution to FNZ customers. “One of the main reasons we wanted to look at an IBM Cloud solution rather than something that would just fix our short-term problem was to be able to stand up new instances of our software for different purposes. IBM Power Systems Virtual Server is going to enable us to do that.”
About FNZ (UK) Ltd. 
##  About FNZ (UK) Ltd. 
is a global financial services company founded in 2004 and headquartered in Edinburgh, Scotland. Financial institutions use FNZ’s solutions and services to help customers manage and grow their wealth. FNZ employs approximately 3,000 people and has operations in 12 countries. In 2019, FNZ acquired JHC Finance, a wealth management software firm. Its assets under management exceed GBP 700 billion.
### CSI Limited
Founded in 1983, is an IT managed services provider based in Birmingham, England. It provides infrastructure, data protection and cybersecurity solutions to various clients throughout Europe. CSI has been an IBM Business Partner since its founding.
Solution components  IBM Cloud Pak®  Red Hat® OpenShift®  IBM® Power® Systems Virtual Server  Red Hat Ansible® 
Take the next step
To learn more about the IBM solutions featured in this story, please contact your IBM representative or IBM Business Partner.
  1. [ View more case stories ](https://www.ibm.com/case-studies)
  2. [ Contact IBM ](https://www.ibm.com/contact/global)


University of the Arts London 
The show must go on
[ Read the case study ](https://www.ibm.com/case-studies/university-arts-london)
#####  Legal 
© Copyright IBM Corporation 2021. IBM Corporation, IBM Cloud, New Orchard Road, Armonk, NY 10504
Produced in the United States of America, July 2021.
IBM, the IBM logo, ibm.com, IBM Cloud, IBM Cloud Pak, and Power are trademarks of International Business Machines Corp., registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on the web at “Copyright and trademark information” at [ibm.com/trademark](https://www.ibm.com/legal/copyright-trademark).
Red Hat®, OpenShift®, and Ansible® are trademarks or registered trademarks of Red Hat, Inc. or its subsidiaries in the United States and other countries.
This document is current as of the initial date of publication and may be changed by IBM at any time. Not all offerings are available in every country in which IBM operates.
The performance data and client examples cited are presented for illustrative purposes only. Actual performance results may vary depending on specific configurations and operating conditions. THE INFORMATION IN THIS DOCUMENT IS PROVIDED “AS IS” WITHOUT ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING WITHOUT ANY WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND ANY WARRANTY OR CONDITION OF NON-INFRINGEMENT. IBM products are warranted according to the terms and conditions of the agreements under which they are provided.
Products Consulting services Industries Case studies Financing Research LinkedIn X Instagram YouTube Podcasts Business partners Documentation Events Newsletters Support TechXchange community Overview Careers Investor relations Leadership Newsroom Security, privacy and trust United States — English Contact IBM Privacy Terms of use Accessibility
IBM web domains
ibm.com, ibm.org, ibm-zcouncil.com, insights-on-business.com, jazz.net, mobilebusinessinsights.com, promontory.com, proveit.com, ptech.org, s81c.com, securityintelligence.com, skillsbuild.org, softlayer.com, storagecommunity.org, think-exchange.com, thoughtsoncloud.com, alphaevents.webcasts.com, ibm-cloud.github.io, ibmbigdatahub.com, bluemix.net, mybluemix.net, ibm.net, ibmcloud.com, galasa.dev, blueworkslive.com, swiss-quantum.ch, blueworkslive.com, cloudant.com, ibm.ie, ibm.fr, ibm.com.br, ibm.co, ibm.ca, community.watsonanalytics.com, datapower.com, skills.yourlearning.ibm.com, bluewolf.com, carbondesignsystem.com, openliberty.io 
About cookies on this site Our websites require some cookies to function properly (required). In addition, other cookies may be used with your consent to analyze site usage, improve the user experience and for advertising. For more information, please review your [cookie preferences](javascript:void\(0\)) options. By visiting our website, you agree to our processing of information as described in IBM’s  [privacy statement](https://www.ibm.com/privacy).  To provide a smooth navigation, your cookie preferences will be shared across the IBM web domains listed [here](https://www.ibm.com/case-studies/fnz-uk#truste_domain_list). 
Accept All More options