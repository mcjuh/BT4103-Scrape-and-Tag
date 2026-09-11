<!-- Source: https://www.capgemini.com/insights/expert-perspectives/from-exposure-management-to-agentic-security-the-next-step-in-cyber-resilience/ | Title: From exposure management to agentic security: The next step in cyber resilience - Capgemini | Seed: https://www.capgemini.com/service/capgemini-invent/ (Capgemini Invent) -->

[Skip to content](https://www.capgemini.com/insights/expert-perspectives/from-exposure-management-to-agentic-security-the-next-step-in-cyber-resilience/#main-content)
## Turning Project Perception’s north star into a continuous vigilance model for exposure management and cyber resilience  
|  **Bottom line:** Microsoft Project Perception signals a broader shift from AI-assisted security tools to agentic security systems. For organizations already moving toward exposure management, the next step is a continuous vigilance model that connects exposure intelligence, control validation, detection and response, remediation, and governance into one operating loop. |  
| --- |  
As organizations face increasingly dynamic attack surfaces and AI-powered threats, security teams are under pressure to move faster from identifying exposure to reducing risk. Microsoft’s newly announced Project Perception offers a view into how agentic security systems may help achieve that shift, bringing together specialized security agents, AI models, security signals, and human oversight in a continuously learning security system. The update is important because it points to a practical question for security leaders: how can AI help organizations move from understanding exposure to reducing risk faster, without losing control of decisions, evidence, and accountability?
At its core, Project Perception reflects a closed-loop security model that connects exposure intelligence, validation, detection, response, remediation, and governance. It begins with understanding which assets, identities, applications, data stores, and vulnerabilities create the most material risk. Those insights are then moved through offensive testing, control checks, and attack path analysis to confirm what is actually exploitable. From there, the model connects to detection and response, so the Security Operations Center can improve telemetry, triage, threat hunting, and playbooks based on validated risk. Finally, remediation and governance close the loop by routing work to accountable owners, tracking exceptions, validating closure, and feeding lessons learned back into the next exposure cycle.
Microsoft is also advancing the model and engineering layer behind agentic vulnerability discovery, including MAI-Cyber-1-Flash and MDASH, Microsoft’s multi-agent vulnerability discovery harness. For security leaders, the practical takeaway is that AI can help analyze more of the software and infrastructure estate, including binaries where source code may not be available, while keeping humans accountable for prioritization, guardrails, and approval.
### The exposure problem security leaders already know
Most organizations do not lack security data. They lack a unified way to turn that data into sustained risk reduction.
  * Vulnerability management identifies technical weaknesses but often struggles to prioritize what matters most to the business.
  * Security Operations Centers detect and investigate threats but are often disconnected from upstream exposure and remediation workflows.
  * Red and purple team exercises validate controls but are typically periodic rather than continuous.
  * Cloud, identity, endpoint, and application teams each manage part of the attack surface, but not always through one risk-based operating model.


Exposure management helps address this by shifting the conversation from counting vulnerabilities to understanding business-relevant risk. Instead of asking, “How many vulnerabilities do we have?” organizations start asking, “Which exposures create the greatest risk today, and what should we fix first?”
### Why agentic security is the logical next step
Exposure management creates the foundation. Agentic security changes the operating speed.
The value of Project Perception is not simply that AI agents can analyze more data. The real shift is the closed-loop model: agents identify potential paths to compromise, reason over context, recommend or execute corrective action within guardrails, and continuously improve the organization’s security posture.
MDASH also expands the conversation beyond traditional source-code review. The ability to analyze binaries was added in the latest release. This matters because many enterprises rely on commercial software, firmware, third-party components, and legacy applications where source code may be incomplete, unavailable, or difficult to assess at speed. In practical terms, agentic vulnerability discovery becomes more useful when it can reason across the software artifacts organizations run, not only the code they directly own.
A second shift is how the tool encourages collaboration. Exposure reduction is rarely owned by one team. Security operations, vulnerability management, application teams, infrastructure teams, and risk leaders all need shared evidence, clear decisions, and traceable handoffs. In practice, the value of agentic security increases when these workflows are integrated into a shared operating model that spans validation, detection, response, remediation, and governance rather than creating another isolated security workflow.  
|  **So what:** If exposure management helps organizations see risk, agentic security helps them act on it faster, with humans still setting strategy, guardrails, and accountability. |  
| --- |  
### Capgemini perspective: Continuous vigilance as the operating model
For clients, this points to a broader shift toward continuous vigilance: an operating model that connects prevention, validation, detection, response, remediation, and governance into repeatable loops. The aim is to help security teams keep pace with changing exposure, not simply produce more findings.  
| **Understand exposure**  | **Validate controls**  | **Monitor and respond**  | **Continuously improve**  |  
| --- | --- | --- | --- |  
| Asset and attack surface visibility  | Security control validation  | Managed detection and response  | Risk-based prioritization  |  
| Identity, cloud, endpoint, and data exposure  | Adversary emulation and purple teaming  | Threat hunting and incident response  | Remediation orchestration  |  
| Vulnerability and configuration intelligence  | Attack path analysis  | SOC feedback loops  | Executive reporting and governance  |  
The goal is not to add another tool or dashboard. The goal is to create a security operating model that continuously learns which risks matter, validates whether controls are working, and improves faster than the adversary can adapt.
### Exposure Management operating model: closing the loop from insight to action
_A practical model for turning exposure insight into validated response, remediation, and continuous risk reduction._
**Bottom line:** Agentic security delivers value when it helps security teams close the loop between exposure insight, validation, response, remediation, and governance. In this context, red, blue, and green agents are not separate personas for separate teams. They represent operating roles that help clarify how work moves from finding risk to reducing it.
How this works in practice:  
| Red agents  | Blue agents  | Green agents  |  
| --- | --- | --- |  
| Offensive and validation agents identify attack paths, test reachable exposure, analyze binaries, and produce evidence of exploitable risk.  | Defensive and response agents that assess telemetry, validate detections, support triage, recommend containment, and improve playbooks.  | Remediation and governance agents that route work to owners, manage exceptions, validate closure, and report risk reduction.  |  
### Example agent tasks in the exposure management phase  
| Exposure phase  | Red agent tasks  | Blue agent tasks  | Green agent tasks  |  
| --- | --- | --- | --- |  
| **1. Understand exposure**  | Map likely attack paths from internet-facing assets, identity misconfigurations, cloud permissions, vulnerable binaries, and exposed data stores.  | Compare exposure data against telemetry coverage, detection rules, log sources, and known blind spots.  | Identify asset owners, remediation constraints, business criticality, exception history, and change windows.  |  
| **2. Validate risk**  | Test whether an exposure is reachable, exploitable, or chainable into a realistic compromise path.  | Confirm whether detections are triggered, alerts contain useful context, and response playbooks match the validated scenario.  | Assess business impact, remediation feasibility, compensating controls, and whether temporary risk acceptance is justified.  |  
| **3. Act on priority findings**  | Provide evidence, steps to reproduce tests, affected assets, likely adversary techniques, and confidence level.  | Prioritize triage, enrich the case, recommend containment if needed, and tune detections for the active exposure.  | Create remediation tickets, route to accountable owners, track exceptions, and confirm change approval requirements.  |  
| **4. Improve continuously**  | Retest closed findings, look for variant paths, and identify recurring exposure patterns.  | Update detection logic, hunting hypotheses, playbooks, escalation paths, and analyst guidance.  | Validate closure evidence, update risk reporting, improve remediation playbooks, and feed lessons into governance forums.  |  
### Putting these tasks into practice
### What this means for clients
#### 1. Exposure management must become operational, not just analytical
  * Security leaders need a single view of exposure across assets, identities, cloud, endpoints, applications, and data.
  * Prioritization should be based on exploitability, business impact, compensating controls, and active threat context.
  * Findings must flow into remediation owners, ticketing, governance, and SOC feedback loops.


#### 2. Security validation must become continuous
  * Organizations need recurring validation of whether controls are deployed, configured correctly, and producing the expected outcomes.
  * Security validation should connect to detection engineering, control testing, and incident response readiness.
  * Point-in-time assessments should evolve into continuous testing and improvement.


#### 3. AI must be governed before it is scaled
  * Agentic security introduces speed, but speed without governance can create operational risk.
  * Human oversight, explainability, approvals for high-impact actions, and clear accountability must be designed into the operating model.
  * Security teams should define where AI can recommend, where it can automate, and where humans must approve.
  * Agentic workflows should support shared review and decision-making so multiple security, application, and risk stakeholders can participate in the same investigation and remediation loop without losing context.


### Now what: practical next steps  
| **Step**  | **Leadership question**  | **Action**  |  
| --- | --- | --- |  
| 1. Establish the exposure baseline  | Do we know our most material exposures today?  | Map assets, identities, vulnerabilities, cloud posture, and external attack surface into one exposure view.  |  
| 2. Prioritize by risk  | Are we fixing what matters most?  | Connect exposure findings to business criticality, exploitability, active threat context, and compensating controls.  |  
| 3. Validate controls continuously  | Do our controls work as intended?  | Use attack path analysis, purple teaming, and security validation to test whether defenses reduce real risk.  |  
| 4. Connect to SOC and remediation  | Can insight become action?  | Create closed-loop workflows between exposure management, detection engineering, MDR, ticketing, and remediation owners.  |  
| 5. Govern agentic security  | Where should AI act, and where must humans approve?  | Define guardrails, approval thresholds, auditability, and accountability for AI-enabled security workflows.  |  
| 6. Design for team-based agentic workflows  | Can multiple stakeholders work in the same loop with clear accountability?  | Enable shared context, role-based approvals, evidence review, and remediation tracking across security, application, and risk teams.  |  
**Agentic security is not a replacement for exposure management. It is the next stage of maturity.**
Organizations that build a strong exposure foundation, validate control effectiveness continuously, and connect AI-enabled workflows into governed operations will be better positioned to defend at the speed of AI. The future of cybersecurity will not be defined by more alerts. It will be defined by how quickly organizations can understand risk, take action, and improve resilience with confidence.
### Reference notes
  * Microsoft Project Perception page, published July 27, 2026.
  * Microsoft Official Blog, “Rethinking security for the age of AI,” published July 27, 2026.


## About the author
### Mona Ghadiri
Vice President, Global Offer Lead for Cybersecurity Defense
Mona is a four-time Microsoft Security MVP, recognized for expertise in SIEM, XDR, and Security Copilot. She has led development of Microsoft-based cyber services and now focuses on SOC transformation, pragmatic AI in security, and talent development. A global speaker and advocate for women in AI and cybersecurity, she serves on multiple Microsoft community boards. Mona holds a BA and MBA and brings a unique blend of product leadership, engineering, and industry recognition.
Slider. Slide 1.
Capgemini cares about your privacy and enables you to choose the types of cookies we can use when you visit our website. You may use the “Manage Cookie Settings” functionality in the banner and/or footer of the website to change our default settings. We use cookies to enhance your experience on our website. They also assist us in improving the website's performance, delivering relevant content to you, and enabling you to share content on social networks. Choosing not to allow the use of certain cookies may consequently affect your browsing experience and limit the availability of some services.Your choices will be recorded by Capgemini and TrustArc for a duration of 3 months, after which you will be required to provide your preferences again.If you wish to know the detailed list of cookies under each category used on the website, you may find it in the [Cookie Policy](https://www.capgemini.com/cookie-policy). 
Accept Manage Settings Decline All