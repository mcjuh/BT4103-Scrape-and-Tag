<!-- Source: https://www.kroll.com/en/publications/cyber/case-studies/kroll-swift-system-cyber-fraud-middle-eastern-bank | Title: Kroll Contains, Remediates SWIFT System Cyber Fraud for Middle Eastern Bank | Seed: https://www.kroll.com/en (Kroll (Duff & Phelps)) -->

Digital Forensics and Incident Response
# Kroll Contains, Remediates SWIFT System Cyber Fraud for Middle Eastern Bank
Share
[https://www.linkedin.com/sharing/share-offsite/url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fcase-studies%2Fkroll-swift-system-cyber-fraud-middle-eastern-bank](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fcase-studies%2Fkroll-swift-system-cyber-fraud-middle-eastern-bank "Linkedin")mailto:?subject=Kroll%20Contains%2C%20Remediates%20SWIFT%20System%20Cyber%20Fraud%20for%20Middle%20Eastern%20Bank&body=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Fcase-studies%2Fkroll-swift-system-cyber-fraud-middle-eastern-bank
In early 2019, a Middle Eastern bank was alerted to numerous fraudulent SWIFT transactions that amassed to over $10 million. The bank soon determined that several of its critical servers and workstations had been sabotaged. Kroll was engaged to investigate how the fraudulent transactions occurred and to identify, contain and remediate the threats attacking the bank’s network.
##### How Kroll Helped
Kroll examined logs during the timeframe when the fraudulent transactions occurred. Our analysis determined that various servers and workstations, three SWIFT user accounts and several administrator accounts had been used suspiciously throughout the time of the transactions. 
We established that some of the suspect servers and workstations had been sabotaged with a master boot record modification tool that rendered the systems inoperable. We repaired the servers and workstations and conducted a forensic analysis, which enabled us to discover valuable artifacts that the attacker was trying to hide.
Our team quickly deployed Kroll’s [CyberDetectER® Endpoint](https://www.kroll.com/en/services/cyber/kroll-responder/managed-edr) across nearly 3,000 endpoints to identify any malicious activity and binaries. Analysis of the collected artifacts identified several suspicious command and control (C&C) IP addresses and URLs from where malicious tools were being downloaded by the attacker. Network device logs were analyzed, and they revealed that many servers and workstations had been in communication with the C&C servers from late 2018.
Our forensic analysis of infected machines identified the presence of two malware variants: PowerShell Empire and Mimikatz. PowerShell Empire enables full remote access to a system, while Mimikatz is used to capture authentication credentials. 
The attackers had rendered several exchange servers inoperable. After Kroll recovered these mail servers, we identified that rules had been implemented which blocked emails containing the words “swift” and “case” to hide detection of the fraud. 
##### Kroll Key Deliverables
  * Identified and contained the various malware infecting the bank’s network and restored the environment to a clean state, preventing continued fraudulent SWIFT transactions.
  * Provided specific security recommendations to help prevent further attacks and related financial losses.
  * Conducted a skills gap assessment and provided training for the bank’s security and infrastructure teams.


[Stay Ahead with Kroll](https://www.kroll.com/en/services)
[Cyber and Data Resilience](https://www.kroll.com/en/services/cyber)
Kroll merges elite security and data risk expertise with frontline intelligence from thousands of incident responses and regulatory compliance, financial crime and due diligence engagements to make our clients more cyber- resilient.
[24x7 Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.
[Penetration Testing Services](https://www.kroll.com/en/services/cyber/threat-exposure-management/penetration-testing)
Validate your cyber defenses against real-world threats.