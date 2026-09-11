<!-- Source: https://www.kroll.com/en/insights/publications/cyber/monitor/business-email-compromise-trends | Title: Business Email Compromise Trends and Mitigation – The Monitor, Issue 1 | Seed: https://www.kroll.com/en (Kroll (Duff & Phelps)) -->

The Monitor
February 1, 2019
# Business Email Compromise Trends and Mitigation - The Monitor, Issue 1
Share
[https://www.linkedin.com/sharing/share-offsite/url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fmonitor%2Fbusiness-email-compromise-trends](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fmonitor%2Fbusiness-email-compromise-trends "Linkedin")mailto:?subject=Business%20Email%20Compromise%20Trends%20and%20Mitigation%20-%20The%20Monitor%2C%20Issue%201&body=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fmonitor%2Fbusiness-email-compromise-trends
Kroll identified 25 business email compromise (BEC) incidents via its cyber intake process during the month of January 2019. Among the BEC incidents that Kroll reviewed, representative attacks led to unauthorized changes to direct deposit information, unauthorized mail forwarding and fraudulent wire transfers of up to $5 million.
BEC incidents most commonly involved an actor compromising an Office 365 Outlook account. For example, Kroll reviewed an incident where a human resources employee complained to her payroll department that her banking information had been changed. Payroll investigated and found an email record from the employee requesting the change. Upon further investigation, the company discovered unauthorized logins to the employee’s Office 365 account from an external IP address. A malicious actor had likely obtained her Office 365 credentials and was able to use her email account to request a change in banking information.
Corporate executives are under particular assault by BEC attackers. Managing Director Jonathan Fairtlough explains, “Criminals are focusing their efforts on executives not only because of their access to high-value data, but also their reach throughout the entire enterprise. Companies should back up executive training with technology that provides early detection of problems to reduce the opportunity for lateral movement once a hacker breaches their systems.” 
Jonathan continues: “While senior executive accounts are commonly targeted, it is important to note that any employee routinely accessing customer account data or treasury functions is at risk.”
BEC attacks also continue to be highly lucrative for cybercriminals in the form of wire transfer fraud. According to the FBI, in 2018 nearly [21,000 victims lost close to $1.3 billion](https://www.securityweek.com/bec-fraud-losses-grew-13-billion-2018-fbi). “Wire fraud highlights a persistent security weakness — our human nature. In the cases we’ve seen, when employees receive requests from senior executives, the motivation to assist the person higher in rank outweighs the need to stop and validate that the request is legitimate” says Peter McFarlane, Managing Director and Toronto Office Head.
According to Peter, tone from the top is critical for combating this crime: “A company’s most senior managers need to make it absolutely clear to everyone involved in approving wire transfers that no one, no matter their rank, can override policies or proper procedures.”
##### Technically Speaking
The growing adoption of [Microsoft Office 365 requires specialist skills](https://www.kroll.com/en/services/cyber/reactive-services/office-365-security-forensics) in securing and/or investigating the environment in the event of BEC and insider threats. Check out these Kroll resources for insights to help you better meet the challenges ahead: 
A Planned Methodology for Forensically Sound IR in Office 365. First presented at SANS DFIR Summit 2018, this talk by Managing Director Devon Ackerman discusses numerous forensic, incident response and evidentiary aspects of Office 365. Based on two years of forensics and incident response data collection in Microsoft’s Office 365 and Azure environment, it also encompasses more than a hundred Office 365 investigations, primarily BEC and rel="noopener noreferrer" insider threat cases. [View now](https://www.youtube.com/watch?v=CubGixACC4E).
Penetration Testing for Active Directory Forests: Exploring Trust Relationships. Active Directory (AD) is a critical software for most organizations in that it serves as the single centralized point for handling authentication and authorization control access to all critical resources within an organization. As Kroll’s security penetration testing lead Carlos Garcia discusses in this article, compromise of just one domain admin account in the AD forest could give an attacker unrestricted access to all resources managed by all domains, users, servers, workstations and data. [Read more and download slides here](https://www.kroll.com/en/insights/publications/cyber/penetration-testing-active-directory-forests). 
##### Case Studies
As these recent Kroll cases demonstrate, BEC incidents are not going away and warrant ongoing vigilance. 
  * Hackers sent a legitimate-looking phishing email from an account belonging to one large company’s Director of Corporate Services to approximately 900 external recipients and 400 internal recipients at that company. In this case, any of those emails could have been used to initiate unauthorized BEC transactions.
  * A supervisor at a financial services company received an email request from a business associate at another financial institution. Despite recognizing the request was somewhat out of character, the supervisor – who routinely works with financial information – opened the attachment expecting an invoice. The document was in fact a maliciously crafted document which triggered a chain of events on the endpoint that were invisible to the user.


##### BEC Red Flags for Wire Fraud
: 
  * **Unusual or Vague Transaction Details** The transaction is described in vague terms (e.g., “strategic marketing advice”) or referenced as a confidential matter known to senior management (e.g., “confidential joint venture investment”). Instructions regarding recording of the transaction are also vague (e.g., “corporate marketing”). 
  * **Unknown Beneficiary and Round-Sum Amounts** The beneficiary is typically a person/entity unknown to the organization and may reference a jurisdiction in which the organization typically does not conduct business. Round-sum amounts, such as “$200,000,” should raise suspicions, although many fraudsters are aware of this and often avoid them. 
  * **Absence of Required Supporting Documents** Normal wire transfer requests should be supported by appropriate documentation available to both those preparing and approving the transfer. Fraudulent requests often state supporting documents will be provided later or were provided to the CEO or other senior executives. 
  * **Non-standard Email Format** Any irregularity in email headers, footers and content such as John.Doe@acme.com rather than the standard format jdoe@acme.com or use of an atypical font or email footer suggest that it could be a fraudulent communication (in addition to a false email domain). 
  * **Requirement to Circumvent Normal Protocols** A pretext is often presented to justify the need and urgency to circumvent normal protocols. These include reasons such as the funds must be received before end of business the next day to close a confidential transaction, avoid penalties or avoid seizure of product.


##### Kroll Experts Corner – Mitigating Business Email Compromise
Following are some insights from Kroll experts on how to prevent or mitigate the harms from business email compromise. 
  * **Implement Multifactor Authentication** Requiring that all users- especially senior and treasury staff use a multi factor authentication system to access email is the most effective mitigation step to take. A phishing attempt or credential theft can be effective, but without the additional token or access method, the attacker cannot access the mailbox. 
  * **Review Email system Configuration** Email systems need to be properly configured and regularly reviewed. There are many modern security processes to securely configure an email system like Office 365 to enforce trusted relationships with common clients and partners, and to track and block misuse. A security professional needs to review email configurations, regularly log and review the use of forwarding rules, domain trust settings, and external exchange access.
  * **Phishing Training** Implement regular phishing awareness training and consider implementing testing to review how many users within the organization are clicking on phishing links. Phishing emails can be used to compromise network credentials and carry out BEC attacks against your organization. 
  * **Beware of Social Media Links** Recent open source reporting highlights an increase in phishing emails designed to look like LinkedIn updates with titles like “profile views” and “InMail message”. These emails can be used to harvest credentials for use in BEC scams. Train employees to use caution when opening these types of messages in their corporate mail accounts. 
  * **Raise Awareness of Spoofed Domains** Hackers will often buy a domain that is similar to a vendor or client’s name but will change one letter or spell the name differently. Employees in payroll and other finance departments should receive training on how to recognize spoofed domains or emails; additionally, create protocols for double-checking domain names and email accounts to ensure the accounts match up to the legitimate company name and domain. 
  * **Implement Dual Verification Procedures for Financial Transactions, Including Wire Transfer Requests** Many BEC attempts rely on creating a sense of urgency or presenting a business case that pressures the targeted individual to quickly transfer funds or edit banking information, so the attacker can swiftly carry out fraudulent activities. Ensure mechanisms are in place to validate requests before action is taken, such as predefined escalation protocols. Also, build a corporate culture that stresses defined channels and protocols cannot be circumvented by anyone, no matter how senior.


The article above was extracted from [The Monitor newsletter](https://www.kroll.com/en/publications/cyber/monitor), a monthly digest of Kroll’s global cyber risk case intake. The Monitor also includes an analysis of the month’s most popular threat types investigated by our cyber experts. Subscription is available below.
[Stay Ahead with Kroll](https://www.kroll.com/en/services)
[Cyber and Data Resilience](https://www.kroll.com/en/services/cyber)
Kroll merges elite security and data risk expertise with frontline intelligence from thousands of incident responses and regulatory compliance, financial crime and due diligence engagements to make our clients more cyber- resilient.
[24x7 Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.
[Office 365 Security, Forensics and Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/office-365-security-forensics)
Digital forensic experts investigate hundreds of Office 365 incidents per year and help strengthen your security.
We use cookies to remember users and provide the best possible experience. Some cookies are essential, others help us improve your experience through insights on how the site is used. Please visit our [cookie notice](https://www.kroll.com/en/cookies-policy) for more information.
Manage Preferences Decline Accept All
## Cookies Preference Center
## Cookies Preference Center
  * ### Your Privacy
  * ### Essential Cookies
  * ### Functional Cookies
  * ### Analytics Cookies
  * ### Advertising Cookies


#### Your Privacy
We use cookies to remember users and give you the best possible experience. Some cookies are essential, others help us improve your experience through insights on how the site is used. Please visit our cookie notice for [more information](https://www.kroll.com/cookies-policy).
#### Essential Cookies
Always Active
These cookies are essential in order to enable you to move around the site and use its features. Without these cookies, services you have asked for cannot be provided.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to function. Certain functional cookies also allow us to respond to service or other inquiries received through a form.
Cookies Details
#### Analytics Cookies
Analytics Cookies
Analytics cookies track aggregate site performance, web speed, traffic sources, video plays and other aggregate data across the site. These cookies allow us to personalize web experience by type of visitor and, upon certain circumstances, by individual user. Individual user information is recognized through form completions or response to other marketing campaigns.
Cookies Details
#### Advertising Cookies
Advertising Cookies
Upon occasion, our firm advertises on certain media sites and these cookies track campaign performance. Cookies may be set by our firm or by our advertising partners. The cookies may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
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
Confirm
Allow All