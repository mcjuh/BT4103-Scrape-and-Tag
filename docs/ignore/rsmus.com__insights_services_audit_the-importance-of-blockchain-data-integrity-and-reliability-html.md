<!-- Source: https://rsmus.com/insights/services/audit/the-importance-of-blockchain-data-integrity-and-reliability.html | Title: The importance of blockchain data integrity and reliability | Seed: https://rsmus.com/ (RSM) -->

High Contrast
Dropdown language Selected region:
United States
  * Region


  * Countries
  * [Hong Kong SAR, China](https://www.rsm.global/hongkong/en)
  * [Ireland (Republic of)](https://www.rsm.global/ireland)
  * [Macedonia (Republic of North)](https://www.rsm.global/macedonia/en)


[ Contact RSM ](https://rsmus.com/contact.html "Contact RSM")
Search 
Share this
#### Video
# How to maintain blockchain data integrity and reliability
### Financial reporting on digital assets requires a robust data validation framework
April 15, 2025
##  Key takeaways 
A data validation framework with regular reconciliations can improve blockchain data accuracy.
Consider costs and technical complexities when evaluating options for accessing blockchain data.
Establish a stringent third-party vendor management program to evaluate blockchain data vendors.
Financial services Blockchain Audit Digital transformation
Blockchain data is becoming a crucial source of information for financial reporting and audits, especially for companies who are either interacting with customers, counterparties and vendors on-chain, or are interacting with tokenized real-world assets.
So how can organizations maintain the integrity and reliability of data they're pulling from any blockchain in this landscape? Start by implementing a data validation framework, says Bennett Moore, RSM US LLP’s blockchain and digital asset innovation team leader, and Todd Briggs, RSM US’s national digital asset audit leader.
Moore and Briggs joined RSM’s “The Audit Statement” and discussed various considerations for maintaining blockchain data integrity, including the following (with timestamp noted in parentheses):
  * Data retrieval and storage (1:06)


  * Data conversion and indexing (1:51)
  * Data validation framework (3:17)
  * Third-party vendor management (4:32)
  * Independent verification and data integrity (6:00)
  * Cost, technical complexities and risks (7:04)


Below is a transcript of their conversation, which has been edited for clarity and length.
**Todd Briggs:_I want to talk a little bit about integrity and reliability of blockchain data._ _What is the initial step in the process of data retrieval from raw node data on a blockchain, and how is this data stored?_**
**Bennett Moore:** Initially, when we think about raw blockchain data, this data is actually stored within a node. The node maintains different amounts of data or history archival data, depending upon the type of node, as there exists multiple different types, as well as the different types of blockchains that exist out there.
This raw data is stored in a machine-readable format, such as bytecode. This is primarily for the purposes of security and particular blockchain operations as it relates to interacting with a given virtual machine, depending upon the blockchain, rather than for the purposes of human-readable queries on activities and transactions such as a structured query language (SQL) database, let's say.
**TB:** **_And how is this raw blockchain data made suitable for further analysis?_**
**BM:** To enable further analysis, raw blockchain data is first exported from that raw node into a traditional database or data lake and first converted into a human-readable format. This data then goes through a computational, complex process called indexing. It has a few different names. You could also call it transformation. Indexing really is about organizing the unstructured blockchain data into a human-readable format so that it can serve specific data use cases.
This could be activities such as everything for a given address, such as every single transaction it has performed since the onset of the blockchain or since the wallet's creation. It could also be for more aggregate structured data, such as looking to understand how many different transactions a given application has had, or how many different interactions a given contract address has been interacted with by particular types of wallets.
And it can also include indexing more complex types of data beyond transaction records such as metadata, event data and call data, which are more associated with things like smart contracts. And these are all really important to support a more in-depth analysis and documentation of exactly what's happening on-chain.
**TB:_What is the first step an organization should take to mitigate challenges in blockchain data retrieval for financial reporting?_**
**BM:** Organizations really should be focused on implementing a data validation framework, starting with establishing a reconciliation process that cross-verifies data obtained from each respective blockchain and third-party vendors against internal transaction logs and ledger entries.
These regular reconciliations help identify and fix discrepancies, ensuring that your financial statements are based on accurate and complete data. Because—coming back to the process of how raw blockchain data exists and moves into databases—that raw blockchain data, based on how it's stored in a node, is immutable. It's unalterable based on how the consensus algorithm of a blockchain works.
But once you put that data into a database to query and to structure it, it becomes subject to all the traditional forms of controls we need to consider within databases today. So these reconciliation processes, these data validation frameworks that businesses need to build, are very important for validating that the data you are recording is actually what occurred on the blockchain or on a given blockchain.
"Organizations should be focused on implementing a data validation framework, starting with establishing a reconciliation process that cross-verifies data obtained from each respective blockchain and third-party vendors against internal transaction logs and ledger entries."
**Bennett Moore,** Blockchain and Digital Asset Innovation Leader, RSM US LLP 
**_TB: You mentioned third-party vendors, and I was just curious about what internal controls should companies establish to get comfortable with their third-party vendors? How do they manage the risks of dealing with those third parties when thinking about data processing and using this information?_**
**BM:** A stringent third-party vendor management system is focused on ensuring data integrity by verifying a vendor's data acquisition, indexing and error-handling processes, as well as node operation processes.
Companies that are working with different third-party vendor management systems and third-party vendors that are providing blockchain data, for especially financial reporting, should be establishing things such as:
  * Performing regular validation checks
  * Maintaining a detailed audit trail
  * Reconciling data from multiple different sources, including many of the open-source locations you can find blockchain data to corroborate information you're receiving from third parties
  * Enforcing, most importantly, role-based permissions to ensure accountability and reduce unauthorized data manipulation


Because—as we've said before, coming back to the fact that we are moving this raw blockchain data into data lakes, which are technically manipulable—ensuring that there are proper segregation of duties and role-based permission controls that are reviewed in the context of that data lake is important for understanding the integrity, completeness and accuracy of that data in the data lake.
**TB:_Beyond the controls at a third-party vendor and getting an understanding of those controls, what can a company do in addition to that to get comfortable with the assets that are theirs on-chain and ensure that there's appropriate data flows into their financial reporting system?_**
**BM:** When we think about getting that comfort, it comes down to independent verification that ensures the assets are reflected accurately on-chain. It is about maintaining data integrity and reliability, and that is especially when third-party vendors lack system and organizational controls (SOC) reports and certain types of certifications over that data.
A deep understanding of on-chain data flows can help organizations evaluate their options for accessing blockchain data, considering the different types of models and costs you can approach for accessing that data, different types of technical complexities depending upon the types of data you need to obtain, as well as the risks, which can ultimately help ensure accurate financial reporting as a whole.
**_TB: What should organizations consider when evaluating their options for accessing blockchain data?_**
**BM:** Overall, organizations should be thinking about a few, three or four main components. So first and foremost is the costs.
Overarchingly, the cost to operate a node on each individual blockchain can vary widely. Certain blockchains can cost $50 a month, others can cost upwards of $20,000, $30,000 or $40,000 a month just to maintain the raw node.
So the first thing organizations should consider is the approach to cost. Are they running the node? Is a third-party vendor that they are going to perform due diligence over running the node? So on and so forth.
Other areas that businesses need to consider are the technical complexities. Are you able to actually operate that node? Do you have the appropriate personnel? Do you have individuals experienced with cloud and other components related to manipulating data, even within a data lake separate from the node operation?
Lastly is considering the risks involved to choose the most suitable method for the needs. Because when it comes from a risk standpoint, if it's really important for you to have this data being delivered 99.999% of the time via a service level agreement (SLA), running that node yourself if you don't have the right experience could present a very high risk to the business compared to outsourcing it.
Overarchingly, organizations also need to ensure that the completeness and the accuracy of their financial data is in place by implementing robust processes and controls as we've been talking about, including through vendor management and internal reconciliation processes.
**TB:_Finally, as this landscape continues to evolve in the blockchain space, what is essential for management to maintain, and stay on top of their data integrity and compliance with financial reporting?_**
**BM:** Most importantly, as many of us in this space are aware, blockchain and digital assets is a constantly evolving space. There are constantly new types of technology, new types of applications and protocols and platforms that are being built.
Really staying informed and adapting to these new technologies and methods is essential for understanding how to maintain data integrity and compliance in financial reporting as this blockchain landscape continues to evolve very rapidly.
**TB:_One last thought here. As a financial statement auditor, in our risk assessment process, we like to ask the questions: What could go wrong? What controls are in place to mitigate these risks? So, what could go wrong?_**
**BM:** There are a number of different things that can potentially go wrong. I think most importantly, understanding that you have and can demonstrate complete and accurate blockchain data is important for financial reporting, even from a potential fraud standpoint as well. Because, ultimately, if you aren't getting complete and accurate information, you might not understand that there are potentially employees or external actors who have compromised your assets and you are missing certain types of digital assets.
Or if we think about the accuracy in terms of what you might anticipate earning in terms of revenue or interest on different types of lending activities, if this information that you're retaining from blockchains is not complete and accurate, you may not be adequately representing the financial position, financial health of the business to your investors, and the overarching public if a public company. So, understanding how you can demonstrate the completeness and accuracy of your blockchain data for financial reporting is extremely important, both internally and externally.
#### RSM contributors
  * Bennett Moore
Blockchain and Digital Asset Innovation Leader 


## Related insights
Showing 0 results.
[ Article January 28, 2025 Principal market price for crypto-assets: An accounting perspective Accounting for crypto-assets presents unique challenges. We highlight what practitioners need to know about principal market price. Learn more # Digital assets Digital assets ](https://rsmus.com/insights/industries/financial-services/principal-market-price-for-crypto-assets.html)
[ e-book April 30, 2023 Driving a sustainable digital assets strategy RSM's professionals weigh in on how companies involved with digital assets need to navigate an ever-changing landscape for a sustainable digital assets strategy. Read more ](https://rsmus.com/insights/industries/financial-services/driving-a-sustainable-digital-assets-strategy.html)
[ Resource center Digital assets: Latest insights and resources for financial services The digital assets space is complex and evolving. RSM professionals can provide insights that help financial services companies stay up to speed. Learn more # Digital assets Digital assets ](https://rsmus.com/insights/industries/financial-services/latest-insights-and-resources-for-financial-services.html)
[ Article January 28, 2025 Principal market price for crypto-assets: An accounting perspective Accounting for crypto-assets presents unique challenges. We highlight what practitioners need to know about principal market price. Learn more # Digital assets Digital assets ](https://rsmus.com/insights/industries/financial-services/principal-market-price-for-crypto-assets.html)
[ e-book April 30, 2023 Driving a sustainable digital assets strategy RSM's professionals weigh in on how companies involved with digital assets need to navigate an ever-changing landscape for a sustainable digital assets strategy. Read more ](https://rsmus.com/insights/industries/financial-services/driving-a-sustainable-digital-assets-strategy.html)
[ Resource center Digital assets: Latest insights and resources for financial services The digital assets space is complex and evolving. RSM professionals can provide insights that help financial services companies stay up to speed. Learn more # Digital assets Digital assets ](https://rsmus.com/insights/industries/financial-services/latest-insights-and-resources-for-financial-services.html)
[ View all audit and assurance insights ](https://rsmus.com/insights/services/audit.html "View all audit and assurance insights")
## Resources and guidance
### Board and audit committee insights
Views and perspectives for board members and audit committees serving public and private companies.
  * [ Learn more ](https://rsmus.com/insights/critical-issues-for-boards-and-audit-committees.html "Learn more")


### Financial Reporting Resource Center
Follow changes to technical and financial reporting with help from our accounting thought leaders.
  * [ Access here ](https://rsmus.com/insights/financial-reporting.html "Access here")


### Quarterly accounting update webinars
Stay informed with our quarterly webinars, delivering key accounting and financial insights.
  * [ Click to watch ](https://rsmus.com/events/2026-events/quarterly-accounting-update-q2-2026.html "Click to watch")


Follow RSM:
###  THE POWER OF BEING UNDERSTOOD 
ASSURANCE | TAX | CONSULTING
Follow RSM:
RSM US 


Worldwide locations 
  * [ Africa ](https://www.rsm.global/africa "Africa")
  * [ Asia Pacific ](https://www.rsm.global/asiapacific "Asia Pacific")
  * [ Europe ](https://www.rsm.global/europe "Europe")
  * [ Latin America ](https://www.rsm.global/latinamerica/en/region/latin-america "Latin America")
  * [ MENA ](https://www.rsm.global/mena "MENA")
  * [ North America ](https://www.rsm.global/northamerica "North America")


RSM blogs 
  * [ Economy ](https://realeconomy.rsmus.com/ "Economy")
  * [ Technology  ](https://technologyblog.rsmus.com/ "Technology ")


RSM US LLP is a limited liability partnership and the U.S. member firm of RSM International, a global network of independent assurance, tax and consulting firms. The member firms of RSM International collaborate to provide services to global clients, but are separate and distinct legal entities that cannot obligate each other. Each member firm is responsible only for its own acts and omissions, and not those of any other party. Visit [rsmus.com/about](https://rsmus.com/about.html) for more information regarding RSM US LLP and RSM International.
© 2026 RSM US LLP. All rights reserved.
  * [ Terms of Use ](https://rsmus.com/pages/terms-of-use.html "Terms of Use")
  * [ Privacy ](https://rsmus.com/pages/rsm-us-privacy-policy.html "Privacy")
  * [ Sitemap ](https://rsmus.com/sitemap.html "Sitemap")
  * [ Cookies ](https://rsmus.com/pages/rsm-us-privacy-policy.html#cookies "Cookies")
  * [ Do Not Sell or Share My Personal Information ](https://rsmus.com/pages/california-consumer-data-request.html "Do Not Sell or Share My Personal Information")
  * Cookie Settings


By clicking “Allow Cookies,” you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.
Cookie Settings Allow Cookies
Your opt-out cookie preference has been applied
## Cookie policy settings
When you visit our website, we store cookies on your browser to collect information. You can choose not to allow certain types of cookies, which may impact your experience of the site and the services we are able to offer. Click on the category headings to find out more and change the default settings according to your preference. You cannot opt-out of our first-party Essential Cookies as they are deployed in order to ensure the proper functioning of our website (such as prompting the cookie banner and remembering your settings). [View our cookie policy.](https://rsmus.com/pages/rsm-us-privacy-policy.html#cookies)
Allow All
###  Manage Consent Preferences
#### Essential Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services – such as setting your privacy preferences or filling in a form. You can set your browser to block these cookies, but doing so may cause some parts of the site to stop working.
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalization. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies, then some or all of those services may not function properly.
#### Performance Cookies
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular, and to see how visitors move around the site.
#### Marketing Cookies
Marketing Cookies
These cookies may be set through our site by our marketing partners. They may be used by those companies to build a profile of your interests and show you relevant messages on other sites. If you do not allow these cookies, then you may experience less relevant content.
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