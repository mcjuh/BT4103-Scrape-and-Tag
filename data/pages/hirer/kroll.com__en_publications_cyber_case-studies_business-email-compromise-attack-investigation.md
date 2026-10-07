<!-- Source: https://www.kroll.com/en/publications/cyber/case-studies/business-email-compromise-attack-investigation | Title: Insurance Broker BEC Investigation Case Study | Kroll | Seed: https://www.kroll.com/en (Kroll (Duff & Phelps)) -->

Digital Forensics and Incident Response
# Business Email Compromise Attack Investigation and Remediation for Insurance Broker
Concerned about the impact of a business email compromise (BEC) attack, which resulted in an attempt to defraud one of its customers out of nearly £300K, a leading independent insurance broker approached Kroll to investigate the source and scope of the attack.
## Overview
##### Industry
  * Finance


##### Challenges
  * High volumes of sensitive data
  * Compromised by cybercriminals
  * Business email compromise


##### Kroll Services
  * Digital Forensics and Incident Response


##### Impact
  * Comprehensive incident insight
  * Securing against business disruption
  * Better protection against potential attacks


## The Incident
As a specialist firm providing insurance advice for high-value business mergers and acquisitions, Kroll’s client processes a wealth of sensitive data.
Despite maintaining a high level of security, the firm discovered that it had been compromised by a cybercriminal and used as a platform to launch a BEC attack designed to trick one of its clients into paying two open invoices, with a total value close to £300K, into an alternate bank account.
Fortunately, on this occasion, the attack was detected by the firm before any payment was made by the client—a vigilant staff member from the client company had insisted on verbal verification of the financial details supplied, leading to an alarm being raised.
Nevertheless, the firm was keen to understand the extent of the compromise and how to safeguard against similar threats.
In need of support from an expert cyber security company to help shed light on events surrounding the attack, the firm turned to Kroll to conduct a full Office 365 forensic investigation.
## The Investigation
The initial focus of Kroll’s assessment was analysis of email logs relating to the Microsoft Office 365 accounts suspected as being used to instigate the fraud.
The team quickly identified that six weeks prior to the BEC attack, one of the Office accounts belonging to a senior-level employee had received a phishing email.
Purporting to be from Microsoft, the email claimed that the user’s account may have been accessed and requested that the user sign in to review activity for security reasons.
Working on the basis that the phishing attempt had been successful, leading to the harvesting of the user’s Office credentials, Kroll set about reviewing audit logs relating to the account in question.
It soon became clear that an attacker had successfully accessed the account from an unidentified IP address.
The attacker promptly introduced mailbox rules designed to scan all incoming emails for keywords, move them to the user’s RSS Subscriptions folder within Outlook®, and mark them as unread. This course of action would help the attacker quickly identify emails of interest and prevent the compromised user from viewing and responding to them.
### Important Client of Firm Targeted
One email thread to capture the attention of the attacker was related to the billing of two high-value invoices, which had been raised by the insurance firm for one of its clients.
Kroll’s analysis of the firm’s email logs reveals that the attackers had used the information gathered in reconnaissance to create a chain of spoof email communications designed to imitate the compromised user and request payment of the outstanding invoices to a substitute bank account.
The source of the spoofed emails was a domain set up to closely resemble that of the insurance firm, so that the difference would not be easily discernible.
Additional attempts by the attacker to conceal the fraud were uncovered by later analysis, which showed that any incoming emails from the firm’s client to the compromised Office account were promptly deleted.
The attacker also created additional fake email accounts pertaining to colleagues of the compromised user and suggested that one of these colleagues would call the client to provide verbal verification of the bank payment details supplied, increasing the likelihood of the BEC succeeding.
Even at the point where the attack was close to being foiled, the attacker did not relent. Further analysis of event logs revealed that an email rule had been set within the compromised account to auto-forward all incoming and outgoing emails to an external Gmail address.
Over the course of a week following detection of the attack, the email forward had delivered over 280 emails to this fraudulent account, resulting in the continued disclosure of highly confidential client details and payment information to the attacker.
### Tracing the Source of the Attack
Having established the means of attack, Kroll’s cyber incident response team set about identifying how the compromise was able to occur. Analysis of audit logs reveals that, following the original phishing attack which led to Office 365 credentials being harvested, hundreds of account login attempts were initiated from a range of malicious IP addresses.
These attempts originated from IPs in Nigeria, China and, later, UAE, from which a number of successful logins were eventually made.
While it’s possible that the failed authentication attempts may be unrelated to the BEC attack, they are unlikely to be a coincidence. One theory is that the compromised user may have, in falling foul of the phishing attempt, entered incorrect account credentials. This led to brute force attempts to identify the genuine password.
Upon detection of the BEC attack, the insurance firm’s IT staff made the decision to lock down the compromised account and enforce multi-factor authentication for all Office 365 users. While this course of action was effective at preventing subsequent malicious login attempts, it was not until the Kroll team identified and disabled email forwarding that the attack was safely contained.
Having concluded its investigation, the Kroll team produced a formal incident report outlining a full timeline of events. The document also included recommendations to help the firm prevent and detect future attacks.
Learn more about Kroll’s [Digital Forensics](https://www.kroll.com/en/services/cyber/reactive-services/computer-forensics) and [Incident Response services](https://www.kroll.com/en/services/cyber/reactive-services/incident-response).
[Stay Ahead with Kroll](https://www.kroll.com/en/services)
[24x7 Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.
[Computer Forensics](https://www.kroll.com/en/services/cyber/reactive-services/computer-forensics)
Kroll's computer forensics experts ensure that no digital evidence is overlooked and assist at any stage of an investigation or litigation, regardless of the number or location of data sources.
[Cyber Risk Retainer](https://www.kroll.com/en/services/cyber/enterprise-risk-retainer/cyber-incident-response-retainer)
Kroll delivers more than a typical incident response retainer—secure a true cyber risk retainer with elite digital forensics and incident response capabilities and maximum flexibility for proactive and notification services.
[Kroll Responder MDR](https://www.kroll.com/en/services/cyber/kroll-responder)
Stop cyberattacks. Kroll Responder managed detection and response is fueled by seasoned IR experts and frontline threat intelligence to deliver unrivaled response.
[Cyber Litigation Support](https://www.kroll.com/en/services/cyber/data-risk-discovery-litigation/cyber-litigation-support)
Whether responding to an investigatory matter, forensic discovery demand, or information security incident, Kroll’s forensic engineers have extensive experience providing litigation support and global eDiscovery services to help clients win cases and mitigate losses. 
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