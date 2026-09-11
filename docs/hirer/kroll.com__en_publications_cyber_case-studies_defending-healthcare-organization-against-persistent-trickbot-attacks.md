<!-- Source: https://www.kroll.com/en/publications/cyber/case-studies/defending-healthcare-organization-against-persistent-trickbot-attacks | Title: Defending Against Trickbot Attacks - MDR Case Study | Kroll | Seed: https://www.kroll.com/en (Kroll (Duff & Phelps)) -->

Managed Detection and Response
# Defending Healthcare Organization Against Persistent Trickbot Attacks
After being infected by an aggressive and persistent form of malware, a highly-modular trojan known as Trickbot, a private healthcare organisation leveraged support from Kroll’s managed detection and response (MDR) service to help eliminate it quickly and effectively.
## Overview
##### Industry
  * Healthcare


##### Challenges
  * Large volumes of sensitive patient data
  * Targeted by sophisticated malware
  * Vulnerable because of a lack of round-the-clock monitoring


##### Kroll Services
  * Managed Detection and Response


##### Impact
  * Proactive defence against malware
  * Greater event visibility
  * Swifter incident response


## The Incident
As a private health care organization, Kroll’s client processes large volumes of patient data, including highly sensitive medical records.
To improve the protection of this information beyond the level of security offered by traditional perimeter solutions, the organization uses Kroll Responder—a specialist MDR service supplying the people, technology and intelligence needed to swiftly identify and help address a wide range of threats.
When Kroll’s client was targeted by a sophisticated type of malware that sought to harvest employee credentials and exfiltrate data, Kroll’s experts were on hand to quickly identify, investigate and respond to the attack to minimize operational disruption and prevent patient details from being stolen.
## The Investigation
Proactive Intrusion Detection System and Security Information and Event Management monitoring are key features of the Kroll’s Responder MDR service that helps to identify attacks targeting on-premises, cloud and hybrid IT environments.
Having first become aware of some suspicious port-scanning activity on the client’s infrastructure, Kroll’s global security operations centre (SOC) analysts were aware that an attack could be imminent.
Endpoint detection and response is an optional but increasingly valuable part of the Kroll Responder service. In this case, a leading Endpoint Detection and Response (EDR) tool, Carbon Black, was deployed across a series of the organization's endpoints deemed to be high risk, enabling Kroll’s global SOC analysts to achieve greater event visibility, enhance threat hunting and perform swifter incident response.
On this occasion, it was Carbon Black Response that first alerted the Kroll team to the presence of malware on two of the client’s host machines. A Kroll analyst set about quickly investigating the alarm and within several minutes was able to establish that the alert was a true positive. Malware with an unknown signature had been detected and was attempting to terminate and delete the host’s Windows Defender Service, as well as connect to a series of known malicious IP addresses.
A priority two incident was promptly raised to the client by Kroll’s global security operations centres (SOCs) via Kroll’s Redscan threat management platform, included as part of Kroll Responder. By accessing the Redscan platform, the client was able to obtain a full overview of the incident and the remediation guidance needed to respond accordingly. On this occasion, the advice was to isolate the infected hosts from the environment, perform a full malware scan and block the observed malicious IPs at the perimeter firewall.
That wasn’t the end of the incident, however.
### Increasing Incident Severity
Almost immediately after notifying the client of the incident, the Kroll team detected the same malware on two additional hosts, prompting the incident to be escalated to a P1—a level of classification reserved for critical incidents which pose an extremely high degree of risk.
Kroll’s [incident response playbook](https://www.kroll.com/en/services/cyber/reactive-services/incident-response-plan-development) for malware infections was in full execution at this point. To prevent additional infections, the SOC teams used Carbon Black (CB) Response to ban the signature of the identified malware binaries and, with the client’s authorization, used the same tool’s incident response capabilities to quickly isolate all infected hosts from the network.
### Investigating the Kill Chain
Upon containing the malware, the Kroll team set about analyzing the kill chain of the attack—how it was able to obtain a foothold on the client’s network and spread so quickly. By recording each and every file execution and modification, registry change, network connection and binary execution across all installed hosts, CB Response is an important tool that helps the Kroll SOC teams perform more detailed digital forensics to inspect deeper into IT networks for signs of malicious activity.
One of the binaries that CB Response identified was attached to the roaming Windows profile of one particular employee who had logged into multiple endpoints, thus spreading the infection.
The malware detected, Trickbot, was a Trojan designed to harvest user credentials, exfiltrate data and add infected hosts to a botnet of devices.
While forensic investigation of network and endpoint log files revealed no evidence of data loss, the malware was observed to have conducted an internal network IP scan—designed to obtain DNS information about the network which could be used to help attackers spoof network addresses for social engineering scams.
Owing to the advanced, persistent nature of the malware, identifying the source of the attack proved harder. Previous variations of the Trickbot malware are known to be widely distributed by spam emails as well as infected attachments and URLs. The team had no reason to suspect that the source of this infection was anything different.
### A Highly Persistent Threat
In the week that followed detection of the original four malware infections, Kroll’s SOC teams observed 12 additional malware binaries resident on hosts, each with a different signature and attempting to communicate with malicious IP addresses in locations including Russia, Germany, France and Canada. The new infections were linked to the roaming profiles of a number of employees, including a system administrator.
Whenever a new infected host was identified, it was quickly isolated from the network for a minimum of 12 hours and scanned to remove the infection. As an additional precaution, particularly given the evidence that a system administrator had been compromised, all the client’s employees were encouraged to reset their Windows login credentials.
Further forensic investigation by the Kroll team revealed references, within the malware’s code, to Remote Desktop Protocolrelated registry keys. The team recommended disabling Remote Desktop in Windows to mitigate the risk of any unauthorized connections.
### Preventing Future Incidents
After receiving confirmation that all infected machines had been successfully cleaned, and with no new infections reported, the Kroll team finally closed the incident. Given the severity of the incident, a detailed report was prepared for the client. This included a full event timeline, detailing all actions taken, and a list of recommendations to help mitigate the risk of future attacks.
The advanced persistent nature of [Trickbot](https://www.kroll.com/en/insights/publications/cyber/monitor/fighting-against-banking-trojans), and other forms of malware, means that future attacks cannot be discounted. With Kroll Responder for network and EDR , however, the client can be sure that it will be ready to respond quickly and effectively should any anomalous activity present itself.
Learn more about Kroll Responder, our [Managed Detection and Response solution](https://www.kroll.com/en/services/cyber/kroll-responder), and our [Incident Response services](https://www.kroll.com/en/services/cyber/reactive-services/incident-response).
[Stay Ahead with Kroll](https://www.kroll.com/en/services)
[24x7 Incident Response](https://www.kroll.com/en/services/cyber/reactive-services/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.
[Cyber Litigation Support](https://www.kroll.com/en/services/cyber/data-risk-discovery-litigation/cyber-litigation-support)
Whether responding to an investigatory matter, forensic discovery demand, or information security incident, Kroll’s forensic engineers have extensive experience providing litigation support and global eDiscovery services to help clients win cases and mitigate losses. 
[Cyber Risk Retainer](https://www.kroll.com/en/services/cyber/enterprise-risk-retainer/cyber-incident-response-retainer)
Kroll delivers more than a typical incident response retainer—secure a true cyber risk retainer with elite digital forensics and incident response capabilities and maximum flexibility for proactive and notification services.
[Computer Forensics](https://www.kroll.com/en/services/cyber/reactive-services/computer-forensics)
Kroll's computer forensics experts ensure that no digital evidence is overlooked and assist at any stage of an investigation or litigation, regardless of the number or location of data sources.
[Kroll Responder MDR](https://www.kroll.com/en/services/cyber/kroll-responder)
Stop cyberattacks. Kroll Responder managed detection and response is fueled by seasoned IR experts and frontline threat intelligence to deliver unrivaled response.