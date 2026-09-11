<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/AI-evals-for-MCP-in-AIOps | Title: AI evals for MCP in AIOps | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  AI evals for MCP in AIOps 
[ Engineering Stack Back ](https://www.thoughtworks.com/en-gb/engineering)
Close


By 
[Larissa Dornelles](https://www.thoughtworks.com/en-gb/profiles/l/larissa-dornelles) and
Published: July 31, 2025 
## A case for evaluating MCP
AI agents in ops hold clear promise: more adaptive, context-aware and autonomous operations. Powered by the Model Context Protocol (MCP), these agents can retrieve real-time data — logs, metrics, traces and runbooks — and take action.
But as agent deployments scale, so do the risks: hallucinated outputs, compliance gaps, security vulnerabilities, performance issues and untraceable decision-making.
This blog post introduces a solution: embedding AI evaluations (evals) into MCP-driven AIOps workflows. We’ll explore the limitations of federated context retrieval, where AI agents access and synthesize information across distributed sources, share insights from real-world agent deployments and show how evals can bring trust, safety and accountability to AI-powered operations.
## The rise of context-aware AI agents in operations
The use of AI agents in operations (ops) is evolving from automation scripts to autonomous decision engines. This shift is driven by access to live context, made possible through the Model Context Protocol (MCP).
Traditional ops automation relies on static rules, preset API calls and pre-indexed data. But real-world incidents require up-to-date information, like logs, metrics, traces and tickets, pulled as events unfold. MCP allows AI to query systems in real time, correlate signals and suggest or trigger further actions.
These context-aware agents can now investigate incidents, recommend resolutions and assist humans.
## MCP: Powerful, but risky
MCP allows AI agents to access live operational data so they can make real-time, context-aware decisions.
However, this capability comes with trade-offs.
Unlike static or pre-indexed data, federated retrieval through MCP is unpredictable. The accuracy and usefulness of results depend on many factors: network conditions, system availability, permissions and how well the agent interprets the request. This often leads to inconsistent or irrelevant responses — especially when scaled across complex environments.
These inconsistencies increase the risk of **hallucinations** — when agents generate incorrect or misleading outputs. And because agentic workflows often chain decisions together, a single error early in the retrieval process can cascade into larger failures. This makes root causes harder to trace. In ops, this could mean false alerts, misdiagnosed incidents or unsafe automation.
  * **Latency** is another issue confounded by live context injection. Real-time queries take time, especially under system load, which can delay responses and reduce the agent’s effectiveness in time-sensitive situations.
  * **Security** is also a growing concern. A Backslash Security [report](https://www.backslash.security/blog/hundreds-of-mcp-servers-vulnerable-to-abuse) found hundreds of exposed MCP servers at risk of abuse. Without proper controls, agents or attackers may be able to access sensitive data or trigger unintended actions.


In short, MCP is a powerful enabler. However, without real-time evaluation and strong governance, it introduces significant risks in accuracy, performance and security.
## AI evals are a critical layer
As AI agents take on more responsibility in operations, continuous evaluation becomes essential.
Without it, agents operate as black boxes. Verifying if their outputs are grounded, if their actions are safe or if performance is degrading over time is inherently difficult. This lack of visibility creates a new layer of operational risk which can undermine trust, traceability and control.
Ensuring scalable and trustworthy AI agent performance, evaluation should occur on three levels:
  * Automated metrics for real-time performance, such as success rates, latency and hallucination frequency.
  * LLM-as-a-Judge to assess reasoning at scale.
  * Expert review to ensure domain relevancy. 


In a recent banking AIOps project, we embedded an Eval component by working with AI eval platform [Weights & Biases](https://wandb.ai) into our agent architecture to measure grounding quality, decision accuracy and response performance in real time. This allowed us to detect hallucinations early, track behavioral drift and improve agent reliability before incidents reached production.
## A real-world case
At a leading LATAM-based bank, we’re building an AI-powered solution to transform traditional operations into a more proactive and autonomous model. The solution consists of two integrated components (Figure.1):
  * **Intelligent alerting with DavisAI** which automatically classifies and suppresses non-actionable alerts. This reduces noise and alert fatigue while enabling the team to focus on high-impact issues.
  * **An AI agent for actionable alerts**. For alerts that require attention, an AI agent (Cline) performs automatic triage and recommends context-aware resolutions by retrieving log context via Dynatrace MCP and enriched insights through retrieval-augmented generation (RAG) from indexed knowledge sources.


Fig 1. An AI-powered solution focuses on incident triggering, responding, and resolving.  Fig 1. An AI-powered solution focuses on incident triggering, responding, and resolving. 
To evaluate the agent’s performance in triage and resolution tasks, we apply a three-layer evaluation framework that measures:  
Three layer evaluation framework  
| Layer  |  What it checks   | Field example   |  
| --- | --- | --- |  
| Functional effectiveness  |  Did the agent complete the task and produce useful results?  |  mcp_calls_successful Indicates whether the agent can reliably interact with real-time systems via MCP.  |  
| Reasoning quality  |  How did the agent think through the problem? Was the process transparent and sound?  |  ai_thinking_pattern Helps us audit and understand the decision-making process.  |  
| Trustworthy output  |  Was the output grounded, explainable, and secure? Did the agent avoid hallucinations and expose limitations?  |  hallucination_type Detects ungrounded or fabricated responses — critical in high-stakes environments.  |  
Three layer evaluation framework  
| Layer |  
| --- |  
| Functional effectiveness |  
| Reasoning quality |  
| Trustworthy output |  
|  What it checks  |  
| --- |  
|  Did the agent complete the task and produce useful results?  |  
|  How did the agent think through the problem? Was the process transparent and sound?  |  
|  Was the output grounded, explainable, and secure? Did the agent avoid hallucinations and expose limitations?  |  
| Field example  |  
| --- |  
|  mcp_calls_successful Indicates whether the agent can reliably interact with real-time systems via MCP.  |  
|  ai_thinking_pattern Helps us audit and understand the decision-making process.  |  
|  hallucination_type Detects ungrounded or fabricated responses — critical in high-stakes environments.  |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
To support this continuous and structured evaluation, we use W&B Weave, the AI evaluation platform by Weights & Biases (W&B). [W&B Weave](https://wandb.ai/site/weave/) allows us to log, visualize and analyze agent performance. By using Weave, we gain deep insight into how our AI agents behave in production — where they excel, where they struggle and how to improve them in mission-critical AIOps environments.
## Technical deep dive: How the eval framework works
To ground our evaluation in a real-world context, our framework begins with four troubleshooting conversations exported from an infrastructure engineer's interactions with our AI agent, Cline. Using our custom tool, [cline_eval.py](https://github.com/ldrmqs/eval-ai-mcp-aiops), we implemented a pipeline to log each of these conversations as a complete **session** with **W &B Weave**. Each session focuses on a distinct **task** , like root cause analysis, and is structured as our primary measurement tool: the **eval unit**. 
Note: The screenshots in the technical deep dive section are taken directly from W&B Weave. 
Every eval unit is designed to assess the agent’s performance across our three core layers: **effectiveness, reasoning, and trust**. To illustrate how this framework provides deep, actionable insights, below is a sample eval unit generated from one of the sessions:
**Example eval unit** : cline_task_2
**Summary** :  
Sample eval unit generated from one of the sessions  
| Task type  | Root cause analysis  |  
| --- | --- |  
| Session ID  | cline_task_2  |  
| Eval unit result  | Functional effectiveness  | Reasoning quality  | Trustworthy output  |  
| **Passed**  | **Passed**  | **Passed**  |  
Sample eval unit generated from one of the sessions  
| Task type |  
| --- |  
| Session ID |  
| Eval unit result |  
| Root cause analysis |  
| --- |  
| cline_task_2 |  
| Functional effectiveness |  
| **Passed** |  
| Reasoning quality |  
| --- |  
| **Passed** |  
| Trustworthy output |  
| --- |  
| **Passed** |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
1.**Functional effectiveness**
**Goal** : Did the agent solve the problem?
**Key task** : The user asked the agent to analyze a "failure rate increase" for a specific problem ID, identify the error type (service, infrastructure or external), find the failing component and assign team responsibility.
**Outcome** : Root cause found.
**Metrics** : The agent successfully used **three** MCP tool calls to diagnose the issue. The **mcp_calls_successful** metric helps us verify the agent can reliably interact with real-time systems.
2. **Reasoning quality**
**Goal** : Did the agent reason correctly and coherently?
  * **Thinking pattern captured** : For the "reasoning quality" layer, we logged a structured **ai_thinking_pattern object** , which shows the agent followed an "evidence-based diagnosis" approach.
  * **Key reasoning steps** : This object allows us to audit the agent's decision-making process by capturing its logical flow:
    1. It first retrieved the high-level problem details.
    2. It correctly identified the likely root cause service from the initial data.
    3. It then attempted to gather deeper data by analyzing the root cause entity's details and searching for logs.


3. **Trustworthy output**
**Goal** : Was the output reliable and transparent?
  * **Hallucination check** : To ensure a trustworthy output, we logged a **hallucination_type flag** , which detected **no** fabricated information in this case.


  * **Transparency and limitations** : This was a critical test. The agent explicitly and correctly reported its limitations, stating that **logs_access_denied_and_trace_data_unavailable**. This demonstrates the agent does not invent information when it hits a data wall, which is crucial for building operator trust.


This granular, session-level view allows us to see not just what the agent did, but how it ‘thought’ and where it hit roadblocks. By structuring our evaluations this way for all four tasks, we can build a comprehensive and data-driven picture of the agent's real-world capabilities.
## Looking ahead: Eval-first AI agents in ops
As MCP-powered AI agents become more embedded in operational workflows, their ability to act in real time — and with autonomy — marks a major shift in how we manage systems. But with that power comes a new class of risks: hallucinations, inconsistent decisions, security gaps and unpredictable behaviors.
Without evaluation, these agents remain unpredictable and unaccountable. We can’t scale trust if we can’t measure how agents behave.
An eval-first approach changes that. By embedding evaluation directly into the agent lifecycle — monitoring grounding quality, latency, accuracy and safety — we move from passive observation to active governance. Eval-first agents are measurable, explainable and trustworthy.
As adoption grows, agent evals must become a core design principle like observability or security. It’s not just about making agents smarter; it’s about making them safe, reliable partners in real-world operations.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
## Related content
  * [ Generative AI The dangers of AI agentwashing  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/Agentwashing-and-how-AI-agents-fail-us)
  * [ Generative AI Deep Kernel-level AI RCA with MCP  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/deep-kernel-level-AI-RCA-with-MCP)
  * [ Generative AI The Model Context Protocol: Getting beneath the hype  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/model-context-protocol-beneath-hype)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Explore more insights
[ Read now ](https://www.thoughtworks.com/en-gb/insights)
Thoughtworks respects your privacy and only uses cookies that are essential for this site to function. If you enjoy our content and would like a personalized experience please ‘’accept optional cookies’’. See our [Privacy policy](https://www.thoughtworks.com/about-us/privacy-policy) for more.
Manage preferences Decline cookies Accept optional cookies
## Privacy Preference Center
## Privacy Preference Center
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Functional Cookies
  * ### Targeting Cookies


#### Your Privacy
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://www.thoughtworks.com/about-us/privacy-policy)
#### Strictly Necessary Cookies
Always Active
These cookies are essential in enabling you to move around our site and use our features. Without them, services you ask for can't be provided. Registered Visitor Cookie: a unique identifier given to each registered user that recognizes you anonymously during site access.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies collect information so we can analyze how our visitors use our site but they don't collect information that identifies you. All information is anonymous and is only used to improve how our site works.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies allow websites and applications to remember choices you make and provide more enhanced, personal features. We may use information collected from functional cookies to identify user behavior and to serve content based on the user profile. These cookies can't track your browsing activity on other websites and don't gather any information about you for advertising usage or to record where you’ve been on the internet, outside our site.
Cookies Details
#### Targeting Cookies
Targeting Cookies
In order to keep our website services relevant, easy to use and up-to-date, we use web analytics services to help us understand how people use the site. Cookies allow us to recognize your browser or device and identify whether you've visited our website before, what you've previously viewed or clicked on and how you found us. The information is anonymous and only used for statistical purposes.
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
Save Settings
Allow All