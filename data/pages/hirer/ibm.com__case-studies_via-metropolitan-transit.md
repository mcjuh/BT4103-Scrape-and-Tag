<!-- Source: https://www.ibm.com/case-studies/via-metropolitan-transit | Title: VIA Metropolitan Transit | IBM | Seed: https://www.ibm.com/consulting (IBM Consulting) -->

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
#  Digital agent Ava guides San Antonio transit riders 
Applying AI to answer customer questions and predict bus arrival times 
VIA Metropolitan Transit is the primary public transportation provider in the San Antonio, Texas region. VIA is an essential resource for the community’s residents, making some 36 million passenger trips annually with its bus, van and on-demand service.
VIA supports customers through two call centers, one for paratransit riders and one for general information, with live agents available during most hours of the work week. To improve service, the Technology and Innovation and Customer Care teams added a service that reports wait times, and a callback feature designed to alleviate long hold times.
Given VIA’s focus on continuous improvement through innovation, the team sought to further enhance the customer experience by applying digital technology. “Our culture is to be really customer centric and rider friendly, and part of that is offering cutting-edge tools to provide better information,” says Steve Young, Vice President of Technology and Innovation at VIA.
Several informational issues were ripe for digital innovation. First was the need to offer customer support 24x7, not just during call center hours. In addition, the growing percentage of transit riders who rely on smartphones, tablets and PCs would welcome a digital channel. Plus, in reviewing call center data, the executive team noted the repetitive nature of basic customer queries that could be addressed with digital information tools, allowing agents to focus on value-added services.
“When is my bus coming? Can I bring my dog? What is the fare for my child? There are so many recurrent questions that are easy to answer,” explains Young. “We wanted to be able to answer them automatically even when the call center was closed.”
The solution was an automated digital agent, a virtual assistant that would draw on call center data to answer FAQs. It would also need to interact with third-party APIs to provide real-time transit information and directions. To support San Antonio’s diverse community, it had to converse in both English and Spanish. Operational analytics were a must. And it had to be based on cloud computing.
The VIA team began development with a local startup, but when the partnership faltered, VIA put the project on hold. Fortuitously, around this time IBM® was offering an AI-powered agent for municipalities to answer questions about the pandemic. Though Young wasn’t looking for a COVID agent, it piqued his interest, and he shared his on-hold project with the IBM team. The result was that VIA engaged IBM to co-develop the customer service assistant.
Why IBM? “We wanted stability and we wanted a market leader in the AI space,” says Young. “We found that in IBM, but we also found a partner that would collaborate with us, that was willing to sit down with us and help us grow.
## **AI conversations**
Ava, VIA’s digital assistant, has conducted more than 41,000conversations since it went live
## **AI capability**
Using AI and integration with third-party APIs, Ava has assisted almost 28,000unique users
## **AI efficiency**
Each month, Ava conducts around 3,000conversations with VIA customers
We wanted stability and we wanted a market leader in the AI space. We found that in IBM, but we also found a partner that would collaborate with us, that was willing to sit down with us and help us grow. 
Steve Young  Vice President of Technology and Innovation  VIA Metropolitan Transit 
Developing Ava, the automated digital agent 
##  Developing Ava, the automated digital agent 
Consultants from [IBM® Expert Labs](https://www.ibm.com/products/expertlabs) collaborated with a team of VIA developers who were working on their first AI project. “There were weekly planning calls about things the IBM team was working on and things our team handled,” says Young. “We had assigned some junior developers and we wanted them to grow. The IBM experts were really great about sharing, saying, ‘Hey, if you get stuck or need help, please reach out to us.’”
After agreeing on the requirements and architecture, the team analyzed call center data to categorize it and pinpoint common queries the assistant would need to answer. The intelligence was provided by [IBM watsonx Assistant](https://www.ibm.com/products/watsonx-orchestrate) software, a multilingual conversational agent from [IBM Cloud®](https://www.ibm.com/solutions/cloud) that can understand questions texted in natural language and answer in kind.
The team next turned to the most common question, “When is the next bus arriving at my stop?” VIA had already created a service that assigns each stop a five-digit code, which riders can text to Swiftly Systems Inc., a VIA partner. Then, Swiftly uses AI to analyze real-time bus sensor and traffic data to predict the next arrival. The developers integrated the Swiftly service into the assistant. They also integrated the API of VIA partner HERE.com, a mapping service that offers location and point-to-point directions.
In addition, there was a need for operational intelligence. VIA managers would profit from understanding the digital customer interactions, including the number of users and conversations and the content of questions. The developers created a dashboard report that is automatically sent to stakeholders, without them having to query the system.
The analytics are powered by the [IBM Watson Studio](https://www.ibm.com/products/watson-studio) development environment, [IBM Cognos® Dashboard Embedded](https://www.ibm.com/products/cognos-dashboard-embedded) analytics and the [IBM Db2®](https://www.ibm.com/products/db2) database, all from IBM Cloud. These technologies extract the conversation history from IBM watsonx Assistant and analyze it to determine how well the agent has responded to users. They then present results in a dashboard display that shows business KPIs—demonstrating to executive stakeholders the assistant’s value.
The VIA team named the tool “Ava,” for Automated Virtual Assistant, and after a period of testing and review deployed it in late 2020 on VIA’s website. Ava also is available from VIA’s mobile app, goMobile+. It can answer more than 150 common questions 24x7 in English and Spanish and predicts next-bus arrivals in real time. Ava has become quite popular, conducting thousands of conversations each month.
After releasing the first version of Ava, the developers continue to add to and refine its features. As an example, initially Ava referred users back to the call center when it was unsure of an answer. But this might lose the customer if the call center were closed. Now, through a digital handshake, Ava turns such engagements over to SPS DGTL, a social media management company, which queries users for contact information and communication preferences.
“The assistant kind of knows when it didn’t answer a question correctly,” says Young. “SPS collects user information, including the conversation itself, and turns it over to the SPS DGTL team, so we have a sure way to reach these people.”
Another tweak came on the analytical side. After realizing the power of IBM tools, a VIA developer on her own created a second analytical dashboard, this one for the Customer Care team. It provides a daily accounting of the questions Ava missed or was unsure of. As Young says, “It’s really helpful that the Customer Care team can see what’s being asked and where the gaps are, and then go back and train Ava to become more intelligent.”
Ava has made it more convenient for people to get information, and ultimately, that improves the customer experience. 
Steve Young  Vice President of Technology and Innovation  VIA Metropolitan Transit 
Continuously improving customer care 
##  Continuously improving customer care 
Since going live, Ava has conducted more than 41,000 conversations with almost 28,000 unique users, and currently averages nearly 3,000 conversations per month. And Ava provides a response to 96% of users. “I’m thrilled that we’re seeing so many conversations and such strong performance,” says Young.
VIA personnel are pleased with the agent’s impact. “Ava has made it more convenient for people to get information, and ultimately, that improves the customer experience,” says Young. “And the people that use the assistant instead of the call center free up phone lines, lessen queue times and relieve our live agents, which helps us provide better service.”
Young also notes that the project was cost effective, in part because it relied on cloud computing. “We didn’t have to put in any dedicated infrastructure,” he says. “We just capitalized on really smart cloud technology.”
Bigger picture, a key benefit is the knowledge IBM transferred to VIA during the project—knowledge that will serve the organization well over time. In fact, developers are already working through a long list of enhancements.
Richer location and directional services are a priority, using the APIs to answer questions like “How can I get from my home to Walmart?” Or perhaps predicting bus arrivals when users aren’t at a stop, or graphically showing a user’s location and nearby stops. For those who prefer to call, developers are adding a voice interface. The solution will likely be an option in the future for customers calling VIA’s call center. And the system may switch users to a live agent if Ava is stumped during call center hours.
“AI and digital agents were new to our team and to our developers,” says Young. “We wanted to create something that our whole team could support, sustain and grow, and have a partner that would do it along with us. That’s exactly what we gained with IBM.”
About VIA Metropolitan Transit 
##  About VIA Metropolitan Transit 
Founded in 1978, provides multimodal transportation to San Antonio, Texas, and 13 member cities throughout Bexar County. VIA makes around 36 million passenger trips each year through bus, paratransit, and VIA Link ride-share services. It also operates vanpool, park and ride, and special event services. Employing around 2,200 people, VIA’s operating region covers seven transit centers, nearly 7,000 bus stops and eight park-and-ride centers over 1,208 square miles.
Solution components  IBM® Cognos® Dashboard Embedded  IBM Db2®  IBM Expert Labs  IBM watsonx Assistant  IBM Watson Studio 
Take the next step
To learn more about the IBM solutions featured in this story, please contact your IBM representative or IBM Business Partner.
  1. [ View more case stories ](https://www.ibm.com/case-studies)


Natwest Group 
Taking the pain out of purchasing a home 
[ Read the case study ](https://www.ibm.com/case-studies/natwest-group-watson)
State of Rhode Island 
Modernizing in the time of COVID-19 
[ Read the case study ](https://www.ibm.com/case-studies/state-of-rhode-island)
#####  Legal 
© Copyright IBM Corporation 2022. IBM Corporation, IBM Hybrid Cloud, New Orchard Road, Armonk, NY 10504
Produced in the United States of America, April 2022.
IBM, the IBM logo, ibm.com, Cognos, Db2, IBM Cloud, and IBM Watson are trademarks of International Business Machines Corp., registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on the web at “Copyright and trademark information” at [ibm.com/legal/copyright-trademark](https://www.ibm.com/legal/copyright-trademark).
This document is current as of the initial date of publication and may be changed by IBM at any time. Not all offerings are available in every country in which IBM operates.
The performance data and client examples cited are presented for illustrative purposes only. Actual performance results may vary depending on specific configurations and operating conditions. THE INFORMATION IN THIS DOCUMENT IS PROVIDED “AS IS” WITHOUT ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING WITHOUT ANY WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND ANY WARRANTY OR CONDITION OF NON-INFRINGEMENT. IBM products are warranted according to the terms and conditions of the agreements under which they are provided.
Products Consulting services Industries Case studies Financing Research LinkedIn X Instagram YouTube Podcasts Business partners Documentation Events Newsletters Support TechXchange community Overview Careers Investor relations Leadership Newsroom Security, privacy and trust United States — English Contact IBM Privacy Terms of use Accessibility
IBM web domains
ibm.com, ibm.org, ibm-zcouncil.com, insights-on-business.com, jazz.net, mobilebusinessinsights.com, promontory.com, proveit.com, ptech.org, s81c.com, securityintelligence.com, skillsbuild.org, softlayer.com, storagecommunity.org, think-exchange.com, thoughtsoncloud.com, alphaevents.webcasts.com, ibm-cloud.github.io, ibmbigdatahub.com, bluemix.net, mybluemix.net, ibm.net, ibmcloud.com, galasa.dev, blueworkslive.com, swiss-quantum.ch, blueworkslive.com, cloudant.com, ibm.ie, ibm.fr, ibm.com.br, ibm.co, ibm.ca, community.watsonanalytics.com, datapower.com, skills.yourlearning.ibm.com, bluewolf.com, carbondesignsystem.com, openliberty.io 
About cookies on this site Our websites require some cookies to function properly (required). In addition, other cookies may be used with your consent to analyze site usage, improve the user experience and for advertising. For more information, please review your [cookie preferences](javascript:void\(0\)) options. By visiting our website, you agree to our processing of information as described in IBM’s  [privacy statement](https://www.ibm.com/privacy).  To provide a smooth navigation, your cookie preferences will be shared across the IBM web domains listed [here](https://www.ibm.com/case-studies/via-metropolitan-transit#truste_domain_list). 
Accept All More options