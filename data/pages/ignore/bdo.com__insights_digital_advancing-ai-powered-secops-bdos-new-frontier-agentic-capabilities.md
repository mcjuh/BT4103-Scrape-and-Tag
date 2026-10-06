<!-- Source: https://www.bdo.com/insights/digital/advancing-ai-powered-secops-bdos-new-frontier-agentic-capabilities | Title: Advancing AI-Powered SecOps with New Agentic Capabilities | BDO | Seed: https://www.bdo.com/ (BDO) -->

# Advancing AI Powered SecOps: BDO's New Frontier Agentic Capabilities
Article 7 min read
  * PRINT 
  * 

In identity-based attacks, the first few minutes can shape the outcome. A suspicious sign-in, risky OAuth consent, token misuse, or mailbox rule change can quickly point to a larger compromise. But too often, SOC teams are forced to piece together fragmented alerts and manually gather evidence before they can understand the scope of the threat and decide how to contain it.
As identity-driven attacks become more sophisticated, many organizations are reevaluating how their security operations teams investigate and respond to threats. Security analysts are often challenged by fragmented data spread across identity systems, endpoints, cloud platforms, email environments, and third-party applications. The result is a growing gap between detecting suspicious activity and developing the context needed to understand its potential impact and determine the appropriate response. To address this challenge, organizations are increasingly exploring AI-powered security operations (SecOps) capabilities that can help accelerate investigation and response workflows. Rather than replacing human expertise, these capabilities are designed to help analysts assemble evidence faster, identify relationships across complex environments, and gain a clearer understanding of potential attack paths. The goal is to enable more informed decisions, reduce response times, and allow security teams to focus on higher-value analysis and risk management activities.
## What Is AI Powered SecOps, and Where Is Time Actually Lost in the SOC?
Alert volume is rarely the constraint. Evidence assembly is the mechanical work that drains the analyst team. A single identity-led incident can pull an analyst across sign-in logs, token grants, mailbox rules, endpoint telemetry, cloud audit events, and third-party SaaS activity before scope is established. Dwell time compounds. So does the risk that the attacker moves laterally, escalates privilege, or exfiltrates data before containment is approved and deployed.
As organizations explore AI-powered approaches to improve investigation and response, the focus is increasingly shifting from simply generating more alerts to helping analysts gain context faster, understand potential impact, and make more informed response decisions. BDO's Active Protect service applies these principles through a human-led security operations model designed to accelerate investigation, enrichment, and containment workflows while maintaining analyst oversight.
BDO's Active Protect managed security service helps organizations detect, investigate, and respond to threats across XDR and SIEM environments. Recent enhancements focus on applying AI-powered capabilities to areas where security teams often experience the greatest operational burden, including investigation, enrichment, scoping, and containment. By helping analysts assemble context more quickly, these capabilities can support faster and more informed response decisions while preserving human judgment and governance. 
> “AI driven attacks are compressing decision windows. BDO’s Active Protect service now uses analyst run agents and predictive capabilities to help teams investigate, contain, and communicate faster, while keeping analysts in control of response decisions.” – Wally Seliga, Principal, Cyber Defense and Resilience
## How Do Analyst-Run Agents Support SOC Investigations?
BDO’s analyst-run agents support the front end of the investigation loop. The Emerging Threat Detection Agent helps classify newly disclosed CVE activity and zero-day patterns against a client’s asset and telemetry graph. The Triage Agent then helps assess potential exposure and organize remediation work, so analysts can open the ticket with scope, likely blast radius, and a proposed response path already assembled.
Microsoft capabilities expand the investigation surface beneath BDO’s custom agents. The Phishing Triage Agent in Microsoft Defender XDR can operate under a least-privilege scope tied to alert-linked email content rather than broad mailbox access. That gives analysts a way to use the agent’s triage support while reducing unnecessary access to sensitive mailboxes.
For analyst-led investigations, Microsoft’s Threat Hunting Agent can support natural-language hunts, generate KQL, interpret results, and help analysts collect relevant evidence. The Threat Intelligence Briefing Agent can quickly produce threat actor and vulnerability briefings. Defender Chat also lets analysts ask investigation questions in plain language without leaving the incident view.[3]
Combined, our custom agents and Microsoft’s advances enable hunting that is deeper and more identity aware. With AI-powered visualizations, analysts have new entity enrichment for Kerberoast, AS REP roast, domain compromise paths, OAuth application risk, and guest access to cloud resources. Entity pages for IP, domain, URL, and file now include a Threat Intelligence Insights tab with reputation, attributed threat reports, infrastructure relationships, and sandbox analysis, cutting the pivot cost during triage.
The analyst still owns the decision. Agents classify, enrich, and recommend. Active Protect analysts validate, scope, and authorize response actions against the client's change control, business calendar, and risk tolerance.
## How Do Predictive Containment and Blast Radius Analysis Reduce Attack Impact?
Containment is where the new agentic capabilities are most visible. Proactive user containment can help disrupt attacks before they escalate by using activity data and exposure data to identify credentials with clear indicators of misuse. Once triggered, predictive shielding can disrupt likely attack paths based on Microsoft’s risk analysis by isolating entities that appear next in the attack chain. The action is time-limited, scoped, and reversible by operators.
Blast-radius analysis helps analysts understand scope faster. Graphs from the Sentinel data lake can show propagation paths from a selected node to predefined critical targets, within the analyst’s permissions. That gives responders a clearer view of the reachable identities, workloads, and data sets associated with a potential foothold. After BDO’s Emerging Threat Detection and Triage Agents prepare an investigation, analysts can use Microsoft’s identity-focused platform capabilities to move from one suspicious sign-in to domain-compromise paths, OAuth risk, and guest access exposure without manually building every query.
In highly regulated industries, agent assisted investigation can help sharpen containment, evidence collection, and reporting. Financial services organizations may benefit from more complete incident records for SOX, GLBA, FFIEC, SEC cyber disclosure, and NYDFS review while working to close token theft and wire fraud paths. Healthcare organizations may be able to disrupt ransomware activity and contain PHI exposure earlier in the kill chain while operating within HIPAA and HHS 405(d) considerations. Manufacturers can gain a more unified view across IT and OT signals for supplier compromise and ICS exposure, aligned to NIST 800-82 and CISA ICS guidance.
Early research also points to the potential impact of AI-assisted, human-led security operations. One Microsoft Research study reported an approximately 30% MTTR reduction across more than 95,000 incidents[1]. Gartner has also reported that mature AI SOC agent deployments may move MTTR from 3 to 4 hours to under 10 minutes[2].
**How AI Powered SecOps Supports Regulated Industries**
  * **Financial services:** AI powered SecOps can help security teams document identity driven incidents, close token theft paths, and support incident records tied to SOX, GLBA, FFIEC, SEC cyber disclosure, and NYDFS review.
  * **Healthcare:** Agent assisted investigation can help responders identify ransomware activity, understand PHI exposure, and contain threats earlier while operating within HIPAA and HHS 405(d) considerations.
  * **Manufacturing:** Expanded visibility across IT and OT signals can help teams assess supplier compromise, ICS exposure, and operational disruption risk in alignment with NIST 800-82 and CISA ICS guidance.


## How Should Organizations Govern AI Agents as New Attack Surfaces?
AI agents are both a new layer of defense and a new attack surface. BDO now has agentic security visibility through Microsoft Agent 365 in Defender. Together with enhanced agentic security playbooks, Defender can support discovery, posture management, threat detection, investigation, and real-time protection for first-party and third-party AI agents, including custom, open-source, Microsoft Foundry, and Copilot Studio agents.
With agent telemetry from Agent 365 in Defender, agents are folded into the control plane alongside users and machines. BDO SecOps now has centralized inventory of AI components, models, apps, and agents. That enables better, more comprehensive exposure mappings and advanced hunting visualizations. Blocked and audited events fire alerts that correlate into incident workflows, so prompt injection, unsafe tool use, and coerced agent actions receive the same treatment as any other malicious user or code.
New least-privilege scoping on custom and first-party agents restricts them to alert-linked email content instead of the broader mailbox. Active Protect kill-switch controls and human-in-the-loop approval points ensure oversight and curtail excessive access. Agents can classify, recommend, and confirm. Analysts, and where required client owners, authorize response and hold the control.
As Active Protect evolves, BDO continues to help clients build confidence in an increasingly complex digital world.
**Lessons Learned From Our AI-Powered SOC**
  * To understand the value of agents, baseline mean time to detect and mean time to respond by kill chain phase, not just by tool.
  * Enable predictive shields and define escalation rules for containing detonation and for device isolation.
  * Add hunting visualizations for identity scenarios to your regular hunt rotation.
  * Plan to extend AI detection and response (AIDR) coverage to third-party, Copilot Studio, Microsoft Foundry, and local endpoint agents.
  * Pressure test kill switches, rollback, and human in the loop approval workflows in a red team exercise.


For BDO Cyber analysts, the first hour of an incident can look different. Instead of manually stitching together sign-in logs, token grants, endpoint queries, and incident narratives, analysts can start with more context already assembled.
Scope is assembled when the ticket opens. Containment options are researched and staged for the team with context. The incident briefing that used to take half a day writes itself while the analyst is still on the call with the client.
That shift matters because it gives analysts more time for the work that requires judgment: reading the adversary, weighing containment options, and giving client owners a clear answer to a hard question. Clients get faster, more confident support from defenders who are focused on decisions, not repetitive evidence assembly.
That is how security teams can move through a complex digital world with stronger context, clearer decisions, and more control over the response. With Active Protect, BDO is helping security teams bring more clarity, speed, and control to the moments that matter most in cyber response. To learn more visit: <https://www.bdo.com/services/bdo-digital/digital-managed-services/cybersecurity-solutions>.
1. Bono, S., Grana, J., Xu, J., et al., "Generative AI Adoption in Security Operations: A Large-Scale Empirical Study," Microsoft Research / arXiv, November 2024.
2. Gartner, "Innovation Insight: AI SOC Agents," October 2025.
3. Microsoft, "What's new in Microsoft Defender XDR," Microsoft Learn, accessed July 2026.
Select your preferences and stay current with our latest insights  [ SUBSCRIBE ](https://www.bdo.com/create-account)
## Related Resources
[ Blog PostBuilding a Safer Nonprofit Data Landscape July 16, 2026 Blog PostBuilding a Safer Nonprofit Data Landscape July 16, 2026Nonprofits face growing data risks in a digital environment. Learn how stronger data practices can help protect sensitive information and support operational resilience. Read Morechevron_right ](https://www.bdo.com/insights/blogs/nonprofit-standard/building-a-safer-nonprofit-data-landscape)
[ Case StudyALA Turns 150 and Goes Cloud-First to Drive Member Benefits July 7, 2026 Case StudyALA Turns 150 and Goes Cloud-First to Drive Member Benefits July 7, 2026As ALA marks 150 years, the organization is embracing a cloud-first approach to support its mission and future growth. See how BDO helped build a new Azure-based foundation tied to ALA’s strategic plan. Read Morechevron_right ](https://www.bdo.com/insights/case-studies/ala-turns-150-and-goes-cloud-first-to-drive-member-benefits)
[ ArticleTurn ERP Uncertainty Into a Clear Path Forward June 30, 2026 ArticleTurn ERP Uncertainty Into a Clear Path Forward June 30, 2026AI is changing what SOC 1 and SOC 2 examinations require—learn how its use can affect scope, controls, timing, and cost. Read Morechevron_right ](https://insights.bdo.com/Turn-ERP-Uncertainty-Into-a-Clear-Path-Forward.html)
[ ArticleMicrosoft Copilot Cowork: Combining Human Judgment with AI-Powered Execution June 26, 2026 ArticleMicrosoft Copilot Cowork: Combining Human Judgment with AI-Powered Execution June 26, 2026Microsoft Copilot can help teams pair human judgment with AI-powered execution. Explore how this approach may improve productivity, decision-making, and workflow support. Read Morechevron_right ](https://www.bdo.com/insights/digital/microsoft-copilot-cowork-combining-human-judgment-with-ai-powered-execution)
## Cookies Help Us Improve Your Experience
BDO USA uses third-party cookies and other tracking technologies (“Cookies”) on this website. We require the use of certain Cookies (“Mandatory Cookies”) that may collect and receive your information, including information relating to your usage of the website and content you submit or share during your visit, for website functionality, performance, analytics, and other business purposes. You may choose whether to accept our use of certain other Cookies (“Optional Cookies”) to conduct targeted advertising or for other purposes considered data “sharing” or “selling” under applicable privacy laws. To accept these Optional Cookies, please select “Accept All” below, or to opt out, select “Accept Only Mandatory Cookies.”[Privacy Policy](https://www.bdo.com/privacy-policy)
Customize Cookies
Accept Only Mandatory Cookies Accept All
Opt-Out Request Honored
## Opt-out of Targeted Advertising/Do Not Sell or Share My Personal Information
BDO USA uses third-party cookies and similar tracking technologies (“Cookies”) to conduct targeted advertising and for other purposes considered data “sharing” and/or “selling” under privacy laws, as further detailed in our Privacy Policy. In accordance with applicable law, we provide you with the ability to opt out of our use of Cookies for these purposes. If you visit this website from a different browser or device, or if you “clear” your cookies or otherwise reset your browser settings, you may need to re-submit your opt-out preference. Cookies may collect and receive your information, including information relating to your usage of the website and content you submit or share during your visit. Please note that we require the use of certain Cookies for analytics and other business purposes, as described in the “Mandatory Cookies” section below. By selecting “Confirm” below, you acknowledge and accept that we may use Cookies for these purposes. [Privacy Policy](https://www.bdo.com/legal-privacy/legal/privacy-policy%20)
Allow All
### Opt-out
#### Mandatory Cookies
Always Active
Some cookies and tracking technologies are necessary for our website to function, or used for monitoring, performance, analytics and other business purposes.
  * ##### Strictly Necessary Cookies
Always Active


  * ##### Performance Cookies
Always Active


  * ##### Functional Cookies
Always Active


#### Optional Cookies
Optional Cookies Active
Please use the toggle to opt out of our use of Cookies to conduct targeted advertising or for other purposes considered data “sharing” or “selling” under privacy laws. These Cookies are ON when the toggle is moved to the right, and will be turned OFF when the toggle is moved to the left.
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
Confirm