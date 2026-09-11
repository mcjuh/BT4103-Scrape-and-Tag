<!-- Source: https://rsmus.com/insights/services/risk-fraud-cybersecurity/identity-crisis-digital-identity-attackers-path-resistance.html | Title: The identity crisis: Why digital identity is attackers’ path of least resistance | RSM US | Seed: https://rsmus.com/ (RSM) -->

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
#### Article
# The identity crisis: Why digital identity is attackers' path of least resistance
### What you can do differently to defend against identity-based attacks
April 07, 2026
#### [Contact our risk team ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/identity-crisis-digital-identity-attackers-path-resistance.html#contact)
Risk consulting Cybersecurity consulting  Cybersecurity
Digital identity has become the crown jewel for cyberattackers—and for good reason. In RSM's [2026 Attack Vectors Report](https://rsmus.com/insights/services/risk-fraud-cybersecurity/rsm-attack-vector-report.html "2026 Attack Vectors Report"), which analyzed more than 650 offensive security engagements conducted throughout 2025, identity-related weaknesses provided successful access in more than 80% of cases.
Even more concerning, these attacks succeeded in mature enterprise environments that had invested significantly in zero-trust initiatives and multifactor authentication (MFA). The message is clear: Digital identity isn't just another attack vector—it's become _the_ attack vector.
## The scope of the problem
The numbers from our 2025 testing paint a stark picture:
  * **2,047 total vulnerabilities:** Roughly one-third were rated high or critical severity, directly enabling privileged access or data theft.
  * **Primary targets:** Active Directory security, excessive privileges and insufficient authentication were the most common vulnerabilities.
  * **The outcome:** These weaknesses provided a repeatable path from initial access to high-impact control of enterprise systems, including domain compromise.


**Key insight:** A single compromised identity rarely stays contained; it becomes the launching point for broader organizational compromise.
## The identity security gap: Vulnerable vs. resilient organizations
Based on our 2025 testing, here's what separates organizations that were compromised in hours from those that successfully contained or prevented identity-based attacks:  
| Security domain  | Vulnerable organizations  | Resilient organizations  |  
| --- | --- | --- |  
| **MFA implementation**  | Push notifications, SMS codes, inconsistent enforcement, legacy protocol exceptions  | FIDO2 tokens, passwordless authentication, conditional access policies, no legacy protocol access  |  
| **AD CS management**  | Default configurations, no ownership, unmonitored certificate issuance  | Continuous validation, quarterly audits, certificate lifecycle monitoring, defined ownership  |  
| **Service accounts**  | Static passwords, shared credentials, domain admin privileges, no rotation schedule  | gMSAs where possible, PAM with session recording, least privilege, automated rotation  |  
| **Detection**  | Periodic log reviews, signature-based alerts, manual investigation  | SIEM/XDR with identity-specific detections, AI-assisted analysis, automated response playbooks  |  
**Key insight:** The gap isn't about budget—it's about treating identity as infrastructure requiring the same rigor as network architecture and application security.
## The MFA illusion
Our teams identified practical bypasses in nearly 75% of organizations using MFA. MFA is not ineffective, but implementation gaps are creating a false sense of security. Common bypass techniques observed include:  
| Bypass technique  | Effectiveness  | Impact  |  
| --- | --- | --- |  
| **Push fatigue**  | High  | Users approve prompts just to stop the “notification spam.”  |  
| **BitB phishing**  | Extreme  | Capture rates are 65% higher than rates for traditional email phishing.  |  
| **Legacy protocols**  | Consistent  | IMAP/SMTP exposure allows bypass with just a username/password.  |  
RSM's offensive security team documented a financial services case where a browser-in-the-browser (BitB) attack captured credentials from 35% of targeted users. By combining this attack with a voice phishing (vishing) call to the help desk, our team achieved full access within just four hours.
## The AD CS vulnerability cascade
If a single technology vulnerability defined 2025 for our offensive teams, it was Active Directory Certificate Services (AD CS). Our analysis found misconfigurations in 42% of tested environments.
Misconfigurations (specifically, domain escalation scenarios ESC1, ESC4, ESC8 and ESC11) enabled certificate forgery and stealthy persistence. Because certificate-based abuse blends into legitimate authentication activity, it consistently bypassed many conventional detection tools. As noted in the Attack Vectors Report, "in multiple engagements, testers achieved lateral movement and domain dominance within hours, even in environments with mature monitoring."
## Kerberoasting: The old reliable
Some attack techniques never go out of style. Our 2025 testing revealed that Kerberoasting attacks—a method used to extract service account credentials from Active Directory—succeeded in 73% of environments with improperly secured service principal names (SPNs).
RSM identified a consistent pattern: "Weak, crackable passwords and excessive service account privileges frequently converted Kerberos ticket access into rapid escalation."
When combined with privilege sprawl and flat internal architectures, a single compromised service account often enabled unrestricted access across the enterprise.
## The vishing and AI revolution
As email security strengthens, attackers have pivoted to voice-based attacks. Our offensive security engagement team documented a sharp increase in vishing efficiency in late 2025 and early 2026. This rise is due to several factors, including:
Multicolor icon
**Voice cloning:** AI-driven impersonation over phone and conferencing platforms has proven devastatingly effective.
**Procedural exploitation:** Our teams regularly bypassed technical controls by convincing help desk staff to reset MFA for "users" experiencing an "urgent business need."
**Speed to compromise:** By late 2025, AI-enabled scripting allowed our testers to automate nearly 100% of techniques that previously required extensive manual iteration, shrinking the attack window from days to minutes.
The RSM report warned, "Many security programs still assume they have hours or days to identify, investigate, contain and remove an active threat. In practice, AI-enabled offensive techniques are rapidly shrinking that window toward hours or minutes."
## Privilege sprawl: The force multiplier
Privilege sprawl amplifies the impact of every identity compromise. Our testing identified several consistent patterns:
  * **Excessive permissions:** Compromising a standard employee account often provided access to sensitive systems far beyond that employee’s role.
  * **Shared credentials:** Common local admin passwords enabled unrestricted lateral movement.
  * **Flat architectures:** In 83% of cases, inadequate segmentation allowed a single-system compromise to escalate into enterprise-wide access.


Our cloud-focused assessments found that "in 71% of assessments, users and service accounts had broad permissions with wild-card actions that enabled privilege escalation, resource manipulation or data exfiltration."
## The nonhuman identity problem
As organizations embrace automation, RSM's findings highlight how "service accounts and other nonhuman identities with excessive and poorly governed privileges frequently converted initial footholds into rapid domain or cloud control."
During our engagements, credentials were discovered in Lambda environment variables, JavaScript files, GitHub repositories and infrastructure as code (IaC) templates. The data shows these credentials were "frequently long-lived, reused across environments and lacked rotation."
Testing also revealed that in 73% of AI-integrated applications tested, “prompt injection attacks succeeded, enabling filter bypass, exposure of sensitive data or actions outside intended agent boundaries."
## The uncomfortable truth: Zero trust failed (or did it?)
Here's a statement that will make some security leaders uncomfortable: Organizations that proudly announced "zero-trust implementation" in 2023−24 still suffered identity-based compromise in over 80% of our 2025 offensive security engagements.
But before we declare zero trust dead, we need to acknowledge the real problem: **Most organizations implemented zero-trust architecture without zero-trust identity.**
They bought the software-defined perimeter. They implemented microsegmentation. They deployed endpoint verification. They configured conditional access policies. But they left the front door wide open by:
  * Allowing MFA bypass through legacy protocols
  * Never auditing AD CS configurations that enable certificate forgery
  * Operating critical systems with service accounts using five-year-old static passwords
  * Training help desk staff to reset MFA based on a convincing phone call
  * Deploying “zero trust” while 70% of users still use push notification MFA that can be fatigued


**The result?** Attackers stopped trying to break through the sophisticated network controls and started walking through the identity layer with valid credentials. Microsegmentation means nothing when the attacker has legitimate credentials for the target system.
The uncomfortable truth isn't that zero trust failed—it's that organizations' efforts were incomplete. They implemented 30% of the zero-trust framework and wondered why they didn't get 100% of the benefit.
## What actually works: Recommendations from the report
Based on what successfully stopped our teams during 2025 testing, RSM recommends:
**Phishing-resistant MFA**
Prioritize passwordless or phishing-resistant MFA such as Fast IDentity Online 2 (FIDO2) for administrators, help desk and remote access. Reduce reliance on push approvals, short message service (SMS) and voice-based factors.
**Hardened AD CS**
Audit and remediate AD CS misconfigurations, including ESC1–ESC11. Treat AD CS as critical infrastructure, define ownership, enforce change control and validate configuration regularly.
**Privileged access management**
Implement privileged access management (PAM) with session control and auditability and migrate service accounts to group managed service accounts (gMSAs) where feasible.
**Rigorous help desk verification**
Require multistep verification for password resets and MFA changes, particularly for high-risk roles. Implement out-of-band confirmation (or call-back procedures), approvals for privileged resets, and monitoring for anomalous reset behavior.
**Improved detection**
Use SIEM/XDR detections for abnormal certificate issuance, suspicious Kerberos service ticket activity, privilege escalation patterns and MFA fatigue indicators. Validate monitoring effectiveness through routine internal simulations.
## Looking ahead: 2026 identity security predictions
Based on attack trends observed in our 2025 testing and conversations with security leaders across industries, here's what we expect in 2026:
### **Q1−Q2 2026: The tipping point for AI agents**
By mid-2026, we predict artificial intelligence agents will outnumber human identities in most enterprise environments. Organizations deploying autonomous agents for customer service, data analysis and workflow automation will discover they've created a sprawling shadow identity infrastructure with inadequate governance.
### **Q3 2026: Insurance policy shifts**
Cyber insurance carriers will begin requiring phishing-resistant MFA for privileged access as a standard policy condition. Organizations unable to demonstrate mature identity practices will see 40%−60% premium increases or face nonrenewal.
### **Throughout 2026: Identity becomes a C-suite priority**
Chief information security officers will increasingly report identity security metrics directly to boards, such as: percentage of privileged accounts using phishing-resistant MFA, time to detect credential compromise, service account password age, and mean time to revoke compromised credentials.
## What you can do this week: Identity security quick wins
Feeling overwhelmed? Start here. These five actions require minimal investment but can provide immediate visibility into your identity security posture:
### **Day 1: Run an AD CS configuration scan**
If you have AD CS deployed, use free tools like Certify or PSPKIAudit to scan for common misconfigurations (ESC1, ESC4, ESC8, ESC11). This 30-minute scan can reveal critical vulnerabilities that enable certificate forgery and privilege escalation.
**Time investment:** 30 minutes | **Potential impact:** Identify critical vulnerabilities present in 42% of environments in our report.
### **Day 2: Audit service accounts for password age**
Query Active Directory for all service accounts and sort by password last-changed date. Any service account with a password older than 90 days (or worse, set to never expire) represents a persistent risk for attacks.
**Time investment:** 15 minutes | **Potential impact:** Identify stale credentials, used in 73% of the Kerberoasting attacks in our study.
### **Day 3: Review help desk MFA reset procedures**
Pull the last 30 days of MFA resets and password changes executed by your help desk. Look for patterns: Are resets happening outside business hours? Are the same users repeatedly resetting MFA? Are verification steps documented?
**Time investment:** 45 minutes | **Potential impact:** Close the gap exploited in device code phishing and vishing attacks.
### **Day 4: Scan your top five repositories for hardcoded credentials**
Use tools like TruffleHog or GitHub's built-in secret scanning to check your most active code repositories for exposed credentials, application programming interface (API) keys and access tokens.
**Time investment:** 1 hour | **Potential impact:** Find credentials in Lambda, IaC and scripts, as we did in 71% of our cloud assessments.
### **Day 5: Enable and review conditional access policies**
If you're using Microsoft 365 or Azure AD, review your conditional access policies. Are legacy authentication protocols blocked? Is MFA enforced for all admin access? Are sign-ins from unusual locations flagged?
**Time investment:** 1 hour | **Potential impact:** Close legacy protocol bypass used in 75% of the MFA evasions identified in our testing.
## The takeaway
The 2026 RSM Attack Vectors Report makes it clear: Digital identity is no longer a supporting actor—it’s the main character of the security story. As RSM's research concludes, "Organizations that made the most progress treated identity, application security, cloud and API protection, architecture, and user awareness as an integrated program supported by continuous custom-designed testing, automated monitoring and policy-driven governance."
Organizations that treat identity as a compliance checkbox will continue to be compromised. Solving the crisis requires treating identity as critical infrastructure, accepting that perfect prevention isn't achievable, and building resilience through the practices RSM's offensive security team validated across more than 650 engagements.
And as we move into 2026, that infrastructure must extend to govern not just human users and service accounts, but the autonomous AI agents that are rapidly becoming part of every enterprise environment.
_Read the complete_[ _2026 RSM Attack Vectors Report_](https://rsmus.com/insights/services/risk-fraud-cybersecurity/rsm-attack-vector-report.html "2026 RSM Attack Vectors Report") _for detailed findings and analysis on application security, cloud and API security, architecture and network segmentation, and user awareness._
## Related insights
Showing 0 results.
[ e-book April 13, 2026 Security alert: Using IAM to safeguard your organization’s data How identity and access management reduces identity risk Read more # Cybersecurity consulting  Cybersecurity consulting  ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/security-alert-using-iam-to-safeguard-your-organizations-data.html)
[ Research February 26, 2026 2026 RSM Attack Vectors Report Several emerging trends have challenged organizations to sustain a robust cybersecurity posture. Read more # CybersecurityRisk consulting CybersecurityRisk consulting ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/rsm-attack-vector-report.html)
[ Video September 05, 2025 Identity at the Center podcast (IDAC) IDAC podcast providing digital identity security and IAM strategy and insights Listen now # Cybersecurity consulting Risk consulting Cybersecurity consulting Risk consulting ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/IDAC-podcast-featuring-RSMs-digital-identity-team.html)
[ e-book April 13, 2026 Security alert: Using IAM to safeguard your organization’s data How identity and access management reduces identity risk Read more # Cybersecurity consulting  Cybersecurity consulting  ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/security-alert-using-iam-to-safeguard-your-organizations-data.html)
[ Research February 26, 2026 2026 RSM Attack Vectors Report Several emerging trends have challenged organizations to sustain a robust cybersecurity posture. Read more # CybersecurityRisk consulting CybersecurityRisk consulting ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/rsm-attack-vector-report.html)
[ Video September 05, 2025 Identity at the Center podcast (IDAC) IDAC podcast providing digital identity security and IAM strategy and insights Listen now # Cybersecurity consulting Risk consulting Cybersecurity consulting Risk consulting ](https://rsmus.com/insights/services/risk-fraud-cybersecurity/IDAC-podcast-featuring-RSMs-digital-identity-team.html)
## Contact our cybersecurity professionals
### Complete this form and an RSM representative will be in touch shortly.
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