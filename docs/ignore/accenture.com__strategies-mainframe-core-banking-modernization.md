<!-- Source: https://bankingblog.accenture.com/strategies-mainframe-core-banking-modernization | Title: Key strategies and approaches for mainframe and core banking modernization | Accenture Banking Blog | Seed: https://www.accenture.com/us-en/services/technology-transformation (Accenture) -->

###### Popular
######  [3 efficient ways to win the payments innovation race](https://bankingblog.accenture.com/win-payments-innovation-race)
######  [The ultimate guide to banking in the cloud](https://bankingblog.accenture.com/the-ultimate-guide-to-banking-in-the-cloud)
######  [Scaling AI for business transformation in financial services](https://bankingblog.accenture.com/scaling-ai-business-transformation)
######  [AI implications for leadership, culture and operating models in financial services](https://bankingblog.accenture.com/ai-implications-financial-services)
######  [The ultimate guide to banking in the metaverse](https://bankingblog.accenture.com/ultimate-guide-to-banking-in-the-metaverse)
##### Accenture Banking Blog 
Other Blogs
[Banking Blog](https://bankingblog.accenture.com "Banking Blog")[Capital Markets Blog](https://capitalmarketsblog.accenture.com "Capital Markets Blog")[Insurance Blog](https://insuranceblog.accenture.com "Insurance Blog")




  * English US


# Key strategies and approaches for mainframe and core banking modernization
15 Nov 2024
The financial services sector, like many industries, is undergoing a transformation to drive new revenue streams and profitability. This shift is fueled by evolved and new business models based on advanced technologies and aimed at meeting client expectations. Similar to other industries, financial services organizations are focused on streamlining cost-to-serve mechanisms and enhancing productivity. However, unlike others, financial services companies are under strict regulations, with increasing scrutiny on IT risk and third-party dependencies.
AI, data, and cloud technologies hold great promise for addressing some of these challenges. However, their adoption is often hindered by legacy systems—a situation I call the “banking technology trap.” Many banks rely on outdated, complex mainframe systems that obstruct transformation. While many have successfully moved peripheral workloads to the cloud, there’s a critical need to modernize core systems. This step has been delayed for too long, causing financial services to lag behind other sectors in cloud adoption.
The combination of legacy systems, outdated technologies, limited expertise, new business capability demands, and increased regulatory focus has created a perfect storm. This is driving long-overdue decisions and actions, breaking the status quo.
There’s no single approach to core modernization. Successful transformations require a tailored, fit-for-purpose mix of strategies based on each organization’s starting point, context, and goals to maximize value.
In this blog, I will discuss the main strategies, archetypes and patterns for modernization that can be combined in parallel and sequential steps to create a successful roadmap:
  1. #### **In-place optimization to enhance efficiency, reliability, and service quality**


For those domains where there is no immediate business need, a clear business case, or pressing obsolescence issues, but where opportunities to enhance efficiency, reliability, scalability, and service quality are still seen, the solution might lie within their existing technology framework. Some options here include:
  *     * Optimizing current technology, such as configuration fine-tuning, on-line and batch workloads rationalization and data access enhancements.
    * Revisiting and renegotiating vendor contracts to unlock cost savings or consolidation opportunities.
    * Partial outsourcing of specific services or components to specialized providers.
    * Adopting mainframe as a service (MFaaS) solutions.


  1. #### **Iso-functional technology modernization to leverage new technologies**


For many business functions, products, and platforms, simply upgrading the underlying technology without altering functionality can yield significant benefits in cost, service, scalability, and productivity. Here are some options:
  *     * **Read off-loading:** Migrating database read workloads to the cloud can offload high-volume queries while keeping critical write functions on the legacy system. This reduces processing loads on high-cost systems and provides scalability and access to more productive software development environments, in areas where speed and innovation are crucial. Maintaining write functions in the current technology minimizes risk, especially for critical financial functions that require less innovation. Key considerations under this approach include methods for data access and replication, as well as the requirements for real-time data synchronization.
    * **Re-platforming (lift and shift):** Migrating existing legacy code to cloud-based emulated mainframe environments. This approach offers access to low-cost, scalable computing, enhanced data access and event capabilities, along with DevSecOps and higher-productivity development frameworks. There is no need to change the source code, which reduces risk and minimizes the need for specialized knowledge and resources. The main considerations in this case are the focus and effort required for establishing technical foundations, parallel run capabilities, and batch scheduling. 
    * **Re-factoring:****Rewriting** legacy code in a modern language, such as converting Cobol to Java or Python, for deployment in a cloud-based architecture. Once the Development Environments (IDEs), landing architecture, and configuration are established, the source code rewriting process can be either manual or automated. New gen AI capabilities are transforming both the manual process, with ‘co-pilot’-like tools, and the automated process, improving the quality, maintainability, and performance of the new automatically generated code.


  1. #### **Functional transformation and legacy exit for business reinvention**


When legacy systems and functions fall short of meeting strategic objectives, re-engineering or re-imagining functionality becomes essential. Options for this include:
  *     * **Custom-built solution:** Developing business and technology capabilities in-house to enable market differentiation. A custom-built solution isn’t about reinventing the wheel; it’s about creating enablers to deliver personalized, differentiated products, services, and experiences. Harnessing gen AI can significantly boost software development creativity, quality, and productivity in this space.
    * **Packaged solution:** Upgrading or replacing current core systems with a market vendor’s packaged solution, either fully or partially. Most banking software vendors embrace interoperability/composability and offer atomized capabilities that can be integrated, consumed, or implemented for specific business needs, rather than requiring a full end-to-end solution. However, when considering an end-to-end core banking package version upgrade, it’s crucial to assess the number of versions to bridge, the technological evolution between versions, and the level of customization in the installed version.
    * **Greenfield:** Launching a new digital brand with a modern technology stack to deliver innovative products and experiences. This can be a standalone offering, a testbed for future migration of the customer base, or a way to penetrate new markets.
    * **Side core:** Implementing a new core system alongside the legacy system to support new products and services with greater speed, flexibility, and improved capabilities. In some cases, the new core becomes the target for gradually migrating the full range of products and services, eventually exiting legacy platforms. In other cases, it is just one component in a broader overall systems strategy. Key considerations in this approach include, functional coverage of the target platform, carving out cross-product functions from the legacy system and addressing technical integration, orchestration, and coexistence.
    * **Core as a service** : Traditionally suited for smaller institutions, this approach is now evolving to support larger players through a composable model that integrates core functions as services. Although this approach is not yet fully mature, it is expected to grow strongly in the near future.


**Systematic decommissioning** is vital for phasing out legacy systems when progressing along the modernization path. This process requires thorough planning to ensure that legacy components are efficiently retired as new systems become operational.
### **Interoperability and composability ensure a fit-for-purpose approach**
The “secret sauce” that brings together all these short-, medium- and long-term applicable patterns is a robust interoperability/composability landing architecture. This architecture will serve as the structural glue for coexistence and the main enabler for some key concepts. These include de-coupling and isolating different layers, integrating various technologies and hosting models, orchestrating and choreographing services, ensuring technical coexistence, and achieving logical coexistence through cross-product abstractions and standardized micro-services frameworks.
Adopting this interoperability/composability approach and architecture will de-risk legacy modernization programs. It allows for the coexistence of legacy and next-gen systems, both on-premises and in the cloud. This enables entities to design a fit-for-purpose transformation roadmap aligned with their desired pace, selected transformation patterns and investment capabilities, while ensuring timely business outcomes. Learn more about the interoperability/composability in core banking modernization 
_Click / tap on image to enlarge._
### **How to start core banking modernization: Think big and start small**
Crafting a successful transformation strategy requires a thorough understanding of your current state and future aspirations (beyond IT). This vision will guide a gradual transformation roadmap towards the north star goal. Start by defining a high-level vision (think big) and identifying the optimal modernization option for each domain, application or platform. Then, develop a roadmap that starts small, reducing risks, balancing investments, and ensuring timely business outcomes.
You can read about how to build a compelling business case for core modernization If you’re interested in exploring core modernization options and creating a tailored strategy, feel free to reach out to me **.**
#####  Disclaimer: This content is provided for general information purposes and is not intended to be used in place of consultation with our professional advisors. Copyright© 2024 Accenture. All rights reserved. Accenture and its logo are registered trademarks of Accenture.
##### Disclaimer: This content is provided for general information purposes and is not intended to be used in place of consultation with our professional advisors. Copyright© 2025 Accenture. All rights reserved. Accenture and its logo are registered trademarks of Accenture.
# Related Posts
25 September 2025
###### By [Frederic Brunier](https://bankingblog.accenture.com/author/fbrunier10 "Frederic Brunier")
### [Why cloud and AI are the keys to banking’s long-term growth](https://bankingblog.accenture.com/cloud-ai-banking-growth "Why cloud and AI are the keys to banking’s long-term growth")
[Read more](https://bankingblog.accenture.com/cloud-ai-banking-growth) 4067 Views
20 September 2024
###### By [Accenture Banking](https://bankingblog.accenture.com/author/alvaro-ruiz "Accenture Banking")
### [Core banking transformation: strategies for modernization and value creation ](https://bankingblog.accenture.com/core-banking-transformation-strategies-for-modernization-and-value-creation "Core banking transformation: strategies for modernization and value creation ")
[Read more](https://bankingblog.accenture.com/core-banking-transformation-strategies-for-modernization-and-value-creation) 5898 Views
18 June 2024
###### By [Accenture Banking](https://bankingblog.accenture.com/author/alvaro-ruiz "Accenture Banking")
### [Solving the puzzle: How interoperability eases banks’ core modernization dilemma](https://bankingblog.accenture.com/solving-puzzle-how-interoperability-eases-banks-core-modernization-dilemma "Solving the puzzle: How interoperability eases banks’ core modernization dilemma")
[Read more](https://bankingblog.accenture.com/solving-puzzle-how-interoperability-eases-banks-core-modernization-dilemma) 6024 Views
29 April 2024
###### By [Accenture Banking](https://bankingblog.accenture.com/author/alvaro-ruiz "Accenture Banking")
### [Core banking modernization: Unlocking legacy code with generative AI](https://bankingblog.accenture.com/core-banking-modernization-unlocking-legacy-code-with-generative-ai "Core banking modernization: Unlocking legacy code with generative AI")
[Read more](https://bankingblog.accenture.com/core-banking-modernization-unlocking-legacy-code-with-generative-ai) 7391 Views
9 May 2022
###### By [Accenture Banking](https://bankingblog.accenture.com/author/cameron-w-krueger "Accenture Banking")
### [Got legacy tech debt? 5 reasons to modernize now](https://bankingblog.accenture.com/got-legacy-tech-debt-5-reasons-to-modernize-now "Got legacy tech debt? 5 reasons to modernize now")
[Read more](https://bankingblog.accenture.com/got-legacy-tech-debt-5-reasons-to-modernize-now) 3178 Views
5 May 2022
###### By [Accenture Banking](https://bankingblog.accenture.com/author/nicole_lanza "Accenture Banking")
### [3 ways banks can get great ROI from the cloud](https://bankingblog.accenture.com/3-ways-banks-can-get-great-roi-from-the-cloud "3 ways banks can get great ROI from the cloud")
[Read more](https://bankingblog.accenture.com/3-ways-banks-can-get-great-roi-from-the-cloud) 5326 Views
28 April 2022
###### By [Accenture Banking](https://bankingblog.accenture.com/author/nicole_lanza "Accenture Banking")
### [Smart banks will move their core to cloud now](https://bankingblog.accenture.com/smart-banks-will-move-their-core-to-cloud-now "Smart banks will move their core to cloud now")
[Read more](https://bankingblog.accenture.com/smart-banks-will-move-their-core-to-cloud-now) 3830 Views
24 June 2020
###### By [Accenture Banking](https://bankingblog.accenture.com/author/accenturebanking "Accenture Banking")& [Emily Heffelman](https://bankingblog.accenture.com/author/emily-g-heffelman "Emily Heffelman")
### [Transforming core banking with the right technology](https://bankingblog.accenture.com/transforming-core-banking-with-right-technology "Transforming core banking with the right technology")
[Read more](https://bankingblog.accenture.com/transforming-core-banking-with-right-technology) 4264 Views
15 August 2019
###### By [Accenture Banking](https://bankingblog.accenture.com/author/accenturebanking "Accenture Banking")& [Ben Lopez](https://bankingblog.accenture.com/author/ben-lopez "Ben Lopez") & [Charlie Arthy](https://bankingblog.accenture.com/author/charlie-arthy "Charlie Arthy")
### [The back-office revolution: powered by the agile workforce](https://bankingblog.accenture.com/back-office-revolution-powered-by-agile-workforce "The back-office revolution: powered by the agile workforce")
[Read more](https://bankingblog.accenture.com/back-office-revolution-powered-by-agile-workforce) 4700 Views
# Get the latest blogs delivered straight to your inbox.
[SUBSCRIBE NOW](https://bankingblog.accenture.com/strategies-mainframe-core-banking-modernization) Close
Next Post -  [Challenges shaping North American banks' payments tech investments ](https://bankingblog.accenture.com/challenges-shaping-north-american-banks-payments-tech-investments "Challenges shaping North American banks' payments tech investments")
Suggested Post - [Challenges shaping North American banks' payments tech investments](https://bankingblog.accenture.com/challenges-shaping-north-american-banks-payments-tech-investments "Challenges shaping North American banks' payments tech investments")
[Subscribe](https://info.accenture.com/fs-blog-subscription-center) Get the latest blogs delivered straight to your inbox.
Share 
Welcome to accenture.com! In order to provide a more relevant experience for you, we use cookies to enable some website functionality. Cookies help us see which articles most interest you; allow you to easily share articles on social media; permit us to deliver content, jobs and ads tailored to your interests and locations; and provide many other site benefits. For more information, please review our [Cookies Policy](https://www.accenture.com/us-en/support/company-cookies-similar-technology) and [Privacy Statement](https://www.accenture.com/us-en/support/privacy-policy).
Cookies Settings Reject All Accept All Cookies
## Privacy Preference Center
Any web site that you visit may store or retrieve personal information, mostly through the use of cookies. The stored or retrieved information might be about you, your preferences or your device and is used for the purposes specified per cookies category below. The data controller of your data processed through our cookies is Accenture PLC. In addition, some cookies we use are from (and controlled by) third-party companies, such as, Facebook, Microsoft, Google, Marketo Munchkin Tracking, X (formerly Twitter), Knotch, Youtube, Instagram, Yoptima and Linkedin Analytics to provide us with web analytics and intelligence about our sites. You can accept the cookies as per your preferences by activating the sliders per cookies category. By accepting cookies, the functionalities described per cookies category will be activated and by not accepting cookies, such functionalities will not be activated. Because we respect your right to privacy, you can choose not to allow some types of cookies and you have the right to withdraw your consent by adapting your preferences in our cookie consent manager. Click on the different category headings to find out more and change our default settings. Please read our [Cookies Policy](https://www.accenture.com/gb-en/support/company-cookies-similar-technology) for more information.
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
These cookies are essential in order to enable you to move around the site and use its features, such as accessing secure areas of the site. Without these cookies, services you have asked for cannot be provided.
Cookie Details
#### Analytics Cookies
Analytics Cookies
These cookies enable us to employ data analytics so we can measure and improve the performance of our site and to personalize and enhance your profile-based experience on our site. They help us test and deliver content that is more relevant to you by analyzing how you interact with our site. These cookies don't collect information that identifies a website visitor at an individual level. Non-identifiable region-based data is leveraged by service providers acting on our behalf, including Adobe Analytics, Adobe Target (including using AI for website performance improvement), Audience Manager, Contentsquare, and Demandbase. These service providers are unable to use this data for their own purposes.
Cookie Details
#### Performance Cookies and Functional Cookies
Performance Cookies and Functional Cookies
_Performance cookies_ are generally third-party cookies from vendors we work with or who work on our behalf that collect information about your visit and use of the Accenture website, for instance which pages you visit the most often, and if you get error messages from web pages. These cookies don't collect information that identifies a visitor. All information these cookies collect is anonymous and is only used to improve how the website works. Third party vendors may have access to this data and may use it to improve their overall services and offerings. _Functionality cookies_ allow a site to remember choices you make (such as your username, language or the region you are in) and provide more enhanced, personal features. These cookies cannot track your browsing activity on other websites. They don’t gather any information about you that could be used for advertising or remembering where you’ve been on the Internet outside our site. 
Cookie Details
#### Advertising and Social Media Cookies
Advertising and Social Media Cookies
Advertising and social media cookies (including web beacons and other tracking and storage technologies) are used to (1) deliver advertisements more relevant to you and your interests; (2) limit the number of times you see an advertisement; (3) help measure the effectiveness of the advertising campaign; (4) retargeting to Accenture websites/information and (5) understand people’s behavior after they view an advertisement. They are usually placed on behalf of advertising networks with the site operator’s permission. They remember that you have visited a site and quite often they will be linked to site functionality provided by the other organization. This may impact the content and messages you see on other websites you visit. If you do not allow these cookies you may not be able to use or see these sharing tools or play certain videos on our site.
Cookie Details
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
  * checkbox label label


Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Reject All Confirm My Choices