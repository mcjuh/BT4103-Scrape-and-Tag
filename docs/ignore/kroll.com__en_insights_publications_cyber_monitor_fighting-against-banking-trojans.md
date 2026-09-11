<!-- Source: https://www.kroll.com/en/insights/publications/cyber/monitor/fighting-against-banking-trojans | Title: Understanding and Fighting Against Banking Trojans – The Monitor, Issue 4 | Seed: https://www.kroll.com/en (Kroll (Duff & Phelps)) -->

The Monitor
May 1, 2019
# Understanding and Fighting Against Banking Trojans - The Monitor, Issue 4
Share
[https://www.linkedin.com/sharing/share-offsite/url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fmonitor%2Ffighting-against-banking-trojans](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fmonitor%2Ffighting-against-banking-trojans "Linkedin")mailto:?subject=Understanding%20and%20Fighting%20Against%20Banking%20Trojans%20-%20The%20Monitor%2C%20Issue%204&body=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fmonitor%2Ffighting-against-banking-trojans
Kroll identified eight banking trojan incidents via its cyber intake process during the month of April 2019, including cases that involved Emotet, Trickbot and Qakbot. Much of the insight and guidance in this month’s newsletter comes from a recent [article on banking trojans](https://www.kroll.com/en/insights/publications/cyber/cybercrime-banking-trojans-ransomware) by Managing Director Devon Ackerman. Banking trojans primarily aim to steal the banking credentials of an organization or individual, usually moving silently in the background leveraging several propagation methods, waiting until victims go to access their personal or corporate financial accounts. At that point, credentials are captured through a variety of means and ultimately funds are drained, paychecks are diverted, fraudulent transactions occur, etc.
According to Devon, banking trojans are most commonly introduced into networks by users at all levels of the organization. Many of the strategies used by fraudsters are not new and include:
  * Social engineering attacks, including phishing (email), vishing (voicemail) and smishing (mobile messaging), where victims most often click on infected links
  * Email attachments that contain macro viruses (i.e., maldocs)
  * Compromised internet ad campaigns
  * “Drive-by” attacks: users visit a website infected by malware that in turn infects users’ computers
  * Visiting contractors or clients with infected laptops


Devon says that two characteristics make banking trojans like Emotet particularly insidious. First, they are polymorphic in nature, such that actors can rotate code and signatures virtually every day, enabling them to evade standard antivirus detection. Second, beyond aiming to capture banking credentials, this malware is able to scrape or steal the contents of locally stored emails on infected endpoints. “Imagine how much more believable a new phishing campaign is when an attacker has a technically valid email and an entire conversation thread to build on,” explains Devon. “Messages that leverage conversation threads from spoofed senders not only have an easier time getting through email filters, they are typically recent enough that recipients will likely have lowered their “mental” defenses from annual cyber awareness training. The ‘clickability’ of these well-disguised emails jumps astronomically, and so the attacker gains a continuous stream of new victims.” 
Statistically, Kroll usually sees less than a 24-hour turnaround between fraudulent domain registrations for spoofing campaigns and actors leveraging those domains for email fraud.
Additionally, Devon warns that in recent months, the newest strains of banking trojans don’t stop at bank-related fraud. “Some join with other malware as secondary and tertiary payload drops into infected networks, which aim to saturate victims with unauthorized remote access looking for additional information to steal. Some infected victims become part of a larger botnet. Kroll has also observed actor groups moving to [deploy ransomware post network saturation](https://www.kroll.com/en/insights/publications/cyber/monitor/ryuk-ransomware-cyber-hygiene) as a means to cover their tracks and to further monetize their intrusion through ransomware payments,” says Devon.
##### Emotet banking on Eternal Blue
Emotet is known for its ability to maintain persistence and spread across networks thanks to its use of the now infamous [Eternal Blue exploit](https://www.wired.co.uk/article/what-is-eternal-blue-exploit-vulnerability-patch). Eternal Blue is an exploit that capitalizes on a vulnerability within the SMB (Server Message Block) protocol. If Emotet finds an unpatched instance of this vulnerability, it can enable the installation of malware without human interaction. Microsoft issued an emergency patch for the Eternal Blue vulnerability in March 2018, but many systems cannot or do not install updates. Consequently, threat actors have continued to capitalize on SMB vulnerabilities for ransomware and trojan attacks.
##### Technically Speaking
While each banking trojan is unique in the mechanisms it employs to inflict harm and further spread malware, the following is a simplified overview of the way Kroll typically handles common banking trojans such as Emotet or Trickbot and provides a glimpse into the steps of an effective response:
  * Deploy [Kroll’s endpoint detection and response](https://www.kroll.com/en/services/cyber/kroll-responder/managed-edr) (“EDR”) solution to combine forensic and incident response tools, threat intelligence feeds, human analysts and client feedback about their own networks to identify and ban identified malware hashes (i.e., unique fingerprints of malicious processes or binaries). This allows for containment and banning of running processes and prevents subsequent execution. When deployed at an enterprise level, this gives us the ability to block the execution of malware network-wide, sometimes within minutes of sensor deployment and initial data analysis
  * When necessary, Kroll is able to isolate infected systems to prevent data acquisition or exfiltration from client networks due to unauthorized access and network intrusions.
  * Identify and block actor command and control (“C2”) IPs at the network perimeter.
  * Pull selected events to generate a timeline of infections and determine user accounts being utilized by malware for installation and/or spreading.
  * Reset domain and local user account credentials for all accounts known to have been used by the malware to spread (or at the appropriate time, perform an enterprise-wide password reset); also ensure all local administrator user account passwords are unique.
  * Ultimately, create and deploy a custom remediation script to purge remaining malware artifacts.


##### Case Study
Kroll recently worked an investigation where a comptroller for a large engineering firm received an email request from a known, legitimate business associate. Despite recognizing that the request was somewhat out of character, the comptroller—who routinely works with financial information and invoice for payment—opened the attachment expecting an invoice. The document was in fact a maliciously crafted document disguised as an older legitimate invoice, which triggered a chain of events on the endpoint that were invisible to the user. The user, upon interview, stated that they discounted the invoice as having been sent in error since it was dated months earlier and was known to have been paid.
The employee’s manager soon received a call from one of the company’s major clients saying they had received a strange email from this employee and it could be malicious. Upon being engaged by the client’s counsel, a Kroll forensics specialist immediately began analyzing the supervisor’s email account remotely. Kroll confirmed the account had suffered unauthorized access but with no signs of the password to the account having been brute forced. Kroll then worked backwards and identified the suspicious email and malicious document and turned their investigation to the user’s computer.
##### Kroll Experts Corner: Mitigating Banking Trojan Risks
Following are insights on how to better defend against banking trojan malware.
Devon Ackerman says because of the persistent, polymorphic nature of banking trojans, organizations should be prepared with a diversified defense that blends “back to the basics” security with advanced threat monitoring and response capabilities.
  * **Employee Education and Awareness Still Key for Defense** Devon recommends conducting more frequent training with staff at all levels, including executive leadership and boards of directors. 


  1. Issuing regular bulletins that share examples of deceptive emails can prove enlightening to employees. 
  2. To gauge the effectiveness of their training programs, many enterprises are proactively making social engineering exercises part of their technical penetration testing programs. 
  3. Annual training should be conducted along with tabletop exercises that involve IT security teams, corporate staff, internal and external legal counsel and a third-party incident response firm like Kroll.


  * **Be Prepared With Threat Intelligence, Endpoint Monitoring and Expert Response** Traditional anti-virus solutions have historically proved ineffective against polymorphic, bit-shifting and process-hollowing techniques characteristic of today’s banking trojans. 


  1. A sophisticated endpoint detection and response solution will continuously search for known bad and unusual behaviors and alert the organization to potential intrusions. 
  2. Kroll’s [CyberDetectER® Endpoint](https://www.kroll.com/en/services/cyber/kroll-responder/managed-edr) leverages multiple threat intelligence sources and IOCs, including Kroll’s learnings from real-world intrusions. 


The article above was extracted from [The Monitor newsletter](https://www.kroll.com/en/publications/cyber/monitor), a monthly digest of Kroll’s global cyber risk case intake. The Monitor also includes an analysis of the month’s most popular threat types investigated by our cyber experts. Subscription is available below.
[Stay Ahead with Kroll](https://www.kroll.com/en/services)
[Cyber and Data Resilience](https://www.kroll.com/en/services/cyber)
Kroll merges elite security and data risk expertise with frontline intelligence from thousands of incident responses and regulatory compliance, financial crime and due diligence engagements to make our clients more cyber- resilient.
[24x7 Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.
[Malware and Advanced Persistent Threat Detection](https://www.kroll.com/en/services/cyber/reactive-services/malware-advanced-persistent-threat-detection)
Our expertise allows us to identify and analyze the scope and intent of advanced persistent threats to launch a targeted and effective response.