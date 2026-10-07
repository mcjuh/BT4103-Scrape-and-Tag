<!-- Source: https://www.publicissapient.com/resources/blog/time-to-ship-metric-ai-software-delivery | Title: Why “Time-to-Ship” Is the Wrong Metric in AI Software Delivery | Publicis Sapient | Seed: https://www.publicissapient.com/ (Publicis Sapient) -->

[Skip to main content](https://www.publicissapient.com/resources/blog/time-to-ship-metric-ai-software-delivery#main)
  * Sapient Slingshot wins Technology Breakthrough of the Year. 
[ Explore Slingshot  ](https://www.publicissapient.com/platforms/slingshot)
  * Sapient Bodhi ranked #1 for deep research. 
[ Explore Bodhi  ](https://www.publicissapient.com/platforms/bodhi)
  * Meet Sapient Sustain: context-aware AI for complex IT operations. 
[ Explore Sustain  ](https://www.publicissapient.com/platforms/sustain)
  * 3M lines of COBOL → clear specs in 8 weeks. 
[ Get the details  ](https://www.publicissapient.com/customers/stories/financial-services-slingshot-legacy-modernization)


#  “Time-to-Ship” Has Lost Its Meaning 
How to rethink vanity metrics in an AI-native world.
April 29, 2026 
Share
Generate AI Summary
## Why “time-to-ship” is the wrong debate 
When it comes to AI coding tools, enterprise leaders are asking the wrong questions:
“How do we ship faster?” “How do we use AI to increase developer productivity?” "How do we accelerate code review?”
Questions about output make for great points in a board deck. But behind the scenes, speed has never been universally accepted measure of engineering within the [DevOps Research and Assessment (DORA) framework](https://dora.dev/guides/dora-metrics/). It’s never been an effective way for serious engineering teams to show success.
As an engineering leader, you already knew this. But in the age of AI, developer productivity is back on the executive agenda. More and more CEOs are competing on what percentage of their code is written by AI, and [there’s no agreed-upon](https://www.thepragmaticcto.com/p/lines-of-code-are-back-and-its-worse), [powerful replacement](https://www.thepragmaticcto.com/p/lines-of-code-are-back-and-its-worse) metric.
We’re measuring AI-assisted engineering with metrics that miss the most important variable: how well developers steer, or maintain control of, complex systems and architectural integrity while accelerating change.
The reason speed is dominating the conversation is because time-based estimates are easy to present, compare and defend with non-technical audiences. Executives need evidence to allocate capital and prioritize initiatives, but too often, that evidence is little more than inflated vanity metrics.
In the short-term, the board-level “we’re too slow to production” problem and its “autonomous coding agents” solution is somewhat harmless. In the long term, this oversimplification will create chaos. To protect the organization’s technical future, engineering leaders must shift the AI investment conversation from how fast teams produce code to how well they can manage the complexity, risk and architectural integrity that come with it.
## How faster code can slow the business
Imagine you’re deploying a new back-end platform feature with the help of an AI coding tool, and the release cycle is faster than predicted. But that feature feeds multiple downstream systems:
  * Reporting pipelines
  * Financial models
  * Allocation engines
  * Operational workflows


Each has their own dependencies and assumptions. That, right there, is millions of lines of code that no single person knows the implications of. The problem with optimizing “time-to-ship" is that you don’t know if you’re accelerating impact on other system dependencies in the process.
That faster release cycle tells you nothing about how these implications will erode revenue metrics, like:
  * Forecast accuracy
  * Inventory balance
  * Allocation quality
  * Margin stability
  * Downstream operational friction


When visibility into these dependencies is low—and for leadership it often is—AI coding assistants can improve time estimations on paper while larger, systemic risk increases underneath, and that gap will eventually surface down the line as development rework.
A common example of how rework shows up, invisible to non-technical leadership teams:
  1. An error appears in production.
  2. An engineer pastes the stack trace into the LLM.
  3. The model suggests a patch.
  4. The patch resolves the immediate exception but introduces a subtle change in how a downstream function interprets data.
  5. A day later, a different team flags inconsistent reporting behavior.
  6. The team patches again.


This pattern, sometimes called “prompt thrashing,” creates local fixes that amplify system instability. If you can articulate how this pattern drastically influences business outcomes long-term, you can guide the AI funding conversation.
## The metric that matters more than speed
“Time-to-ship” was already a blunt instrument before AI-assisted coding, and now it’s almost misleading. But it still needs a simple replacement. This is where the conversation about AI-assisted software development gets quiet. Vendors and executives talk confidently about productivity and speed but stop before getting to a shared, portfolio-grade definition of risk. AI reduces the time it takes to produce code, but it does not reduce the time it takes to understand a system.
DORA’s model is useful here, because it separates “how fast you move” from “how much damage you cause while moving.” Think of throughput as horsepower and instability metrics as how well you steer.
A rising deployment rework rate is the clearest penalty for poor steering: It shows AI is accelerating output faster than the team can validate assumptions across the system. It’s the executive lie detector that points out that if speed improves but rework increases, you haven’t modernized; you’ve redistributed risk. FINRA, the self-regulatory organization overseeing U.S. broker-dealers, adopted the DORA framework, including rework among its delivery metrics. Making that hidden rework measurable is exactly the shift engineering leaders need.
## DORA’s software delivery performance metrics 
**Software delivery throughput (i.e., “horsepower”)**
  * Change lead time
  * Deployment frequency
  * Failed deployment recovery time


**Software delivery instability (“steer”)**
  * Change fail rate
  * NEW: Deployment rework rate


Increased failed deployment recovery time, or time to restore service after a change to production caused an impairment, indicates a potential loss of cognitive ownership. Prompt thrashing, as an example, shifts engineers from owners of logic to orchestrators of prompts. If something truly breaks, recovery slows because no one fully understands the embedded assumptions surrounding the change.
Both deployment rework rate and failed deployment recovery time give engineering leaders a concrete replacement for time-to-ship and developer productivity in the executive AI conversation. These new metrics create a shared understanding of what “good enough” means for developers and the business.
## The problem with metrics and decision-making 
So, why aren’t more engineering teams using it? There are a few reasons. The main being, at most companies, application layers are fragmented and measuring feedback is equally as disjointed There are probably multiple versions, hidden versions, or in some cases, no version of “the truth” when it comes to measurement data that informs metrics like deployment rework rate and mean time to resolution (MTTR). Documenting these metrics can become a matter of human reconciliation, and measurement becomes manual.
Another reason teams struggle to utilize metrics is the fallacy of engineering project estimates due to the nature of software engineering work itself.
[A quote from a software engineer at Github](https://www.seangoedecke.com/how-i-estimate-work/) puts it plainly:
“Software engineering projects are not dominated by the known work, but by the unknown work, which always takes 90% of the time. However, only the known work can be accurately estimated. It’s therefore impossible to accurately estimate software projects in advance.”
AI accelerates the known work but doesn't illuminate unknown work where 90 percent of the time estimate and the risk lives: undocumented dependencies, hidden assumptions and downstream interactions. If you’re managing a developer team or product that affects business portfolios with uneven digital maturity, you need a measurement model that acknowledges this asymmetry.
That means standardizing signals like deployment rework rate and recovery time while still:
  1. Not forcing identical architecture
  2. Creating comparable safety signals across domains
  3. Making business impact specific and clear
  4. Avoiding incentives for developers to game the system


##  How to change the conversation 
**1) Set a portfolio safety baseline using paired metrics** For each domain you manage (example: checkout vs. supply chain vs. merchandising):
  * Prioritize tracking instability (change fail rate + rework rate)
  * Add failed deployment recovery time as the executive reality check
  * Make sure your data sources and reasoning, even if muddy, are part of a visible trade space
  * The proof is in the paired metrics: If stability improves (lower change fail rate, lower rework rate, faster recovery), operating expenses will decline, and the organization has achieved necessary baseline safety to accelerate.


**2) Treat “rework rate” as the executive lie detector**
If AI “speeds you up” but rework rate rises, you didn’t modernize; you just shifted cost into instability. So before answering, “will it ship faster?” ask:
  1. What is our “good enough” across domains?
  2. Which instability metrics (DORA) must improve alongside throughput?
  3. What evidence is produced continuously, before we trust the speed?
  4. Can we run a constrained pilot that increases confidence without committing to sunk cost?


If a leader, teammate or AI vendor can't answer those questions, your project or investment might be headed toward tech debt.
**3) No speed claims without proof artifacts**
Increasing speed without proof just increases long-term risk and decreases long-term speed. Defining “good enough” quality for production with an anecdotal opinion and optimism is not a strategy. The debate over AI should be based on:
  * Explicit specs extracted from current system behavior
  * Mapped dependencies (system + data) i.e., the architectural context required to effectively steer AI-generated change
  * regression tied traceability from requirement → code → test → release evidence


If speeding up means slowing down or stopping later to hunt down documents, use the rework rate metric to re-think how much speed with AI you’re actually gaining. Steering without visibility is impossible, and context is the fuel that allows engineers to direct AI safely across interconnected systems.
Unless context is made visible and traceable across the lifecycle, instability will compound faster than throughput improves. Context continuity is the prerequisite for good steering.
##  A different way to think about AI-assisted legacy modernization 
Modernization decisions compound. The discipline you apply to stability today determines your portfolio’s resilience tomorrow. [Most AI coding platforms](https://www.publicissapient.com/resources/blog/ai-software-development-platforms) optimize for local speed through generating specs, code or tests in isolation. But instability doesn’t happen inside a file. It happens at a system level, where business rules, regulatory logic, upstream dependencies and production data flows intersect.
Platforms like [Sapient Slingshot](https://www.publicissapient.com/platforms/slingshot) are built around a persistent [enterprise context graph](https://www.publicissapient.com/resources/blog/enterprise-context-graph) that maps those relationships across discovery, specification, build, test and release. That continuity is what makes rework measurable, regression enforceable and recovery time reducible. The goal isn’t faster commits. It’s safer change.
If you’re forecasting how AI can accelerate complex legacy modernization, download [How Regulated Enterprises Modernize Legacy Systems Safely](https://www.publicissapient.com/resources/research/ai-legacy-modernization-regulated-industries). It includes
  * Seven modernization case studies with measurable business outcomes
  * A structured pilot model to validate stability before production
  * A proven enterprise modernization roadmap
  * Quantified proof of AI’s impact on system stability


Like this article?
Your browser does not support the video tag.
## 
Ready to learn more?
  * Discuss your unique business challenges
  * Explore AI solutions built for your industry
  * Get proven delivery guidance
  * Identify the next step that fits your goals


Trusted by leading organizations in every industry.
### 
Get in touch
Submit the form below and one of our experts will reach out.