<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/Agentwashing-and-how-AI-agents-fail-us | Title: The dangers of AI agentwashing | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The dangers of AI "agentwashing" 
How AI agents can fail us or lead us astray
[ Engineering Stack Back ](https://www.thoughtworks.com/en-gb/engineering)
Close


By 
Published: July 17, 2025 
Since the launch of ChatGPT in 2022, the AI world has grown increasingly optimistic. Today, following the rise of generative AI, interest has turned to [AI agents](https://www.thoughtworks.com/insights/decoder/a/ai-agents).
However, while the term “agent” is gaining popularity and attention, it’s also beginning to lose meaning. What started as a technical distinction quickly turned into a marketing catch-all term — applied to everything from simple scripts to chatbots. 
We’ve entered the era of **agentwashing** , where the term “AI agent” is being overused, overhyped and often misapplied.
Figure 1. Definition of Agentwashing  Figure 1. Definition of Agentwashing 
To make matters worse, the concepts of agentic AI, AI agents and agentic workflows are now being mixed interchangeably — with few tangible outcomes delivered. Yet capital markets continue to fuel the narrative: Salesforce is pushing Agentforce, Glean’s remarkable IPO.
Yet, [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) that over 40% of agentic AI projects will be canceled by 2027, citing escalating costs and unclear business value.
## What is an AI agent — really?
This isn't a debate about definitions. We have no intention of getting into semantic arguments over “AI agent” versus “agentic AI.” Defining the concept perfectly won’t stop your AI initiatives failing.
Instead, we need to ensure a stronger shared understanding to structure this conversation. Regardless of the UX form factor — whether it’s a chat interface, background process or embedded system — an effective AI agent is built around a focused task and demonstrates the following core traits:
  * **It’s autonomous** — able to operate without constant human prompting.
  * **It’s goal-driven** — designed to pursue and adapt to objectives.
  * **It’s context-aware** — able to reason over state, memory and feedback.
  * **It’s interactive** — able to take action, collaborate, negotiate and delegate.


Agentic AI, on the other hand, is the broader system architecture that enables and governs those agents. It’s more than a single interface or workflow. It includes:
  * Multiple collaborating agents.
  * AI evaluation frameworks (evals) for monitoring and feedback.
  * Communication protocols that orchestrate decisions across agents and systems.
  * Observability layers to trace, debug and optimize agent behavior.
  * Governance and safety mechanisms to ensure alignment and trust.


Any use case that combines agents with tools like AI evals, observability or protocols qualifies as an AI agent or agentic AI initiative — whether it's a research chatbot for drug discovery or a customer success platform for selling agricultural machines.
## Seven ways AI agents can fail us
AI agents are still software — and classic software failure patterns still apply. Through firsthand experience leading and contributing to these initiatives, we've identified recurring failure modes worth watching. Use them to re-evaluate your current use cases or ongoing agentic AI efforts.
### Using a probabilistic tool for a deterministic problem
The root of the “LLM revolution” is still a guessing game — from predicting the next letter to estimating the statistical relevance between concepts. An LLM-driven solution remains a probabilistic tool at its core.
Applying it to a deterministic problem is like rolling a die and hoping for the right outcome. LLMs excel at generating plausible responses, not guaranteeing correctness. And if you find yourself wrapping it in a complex evals framework just to make it behave deterministically, you're likely misapplying the solution to the problem.
Do we really need an LLM to translate: “Create a Terraform config to provision a secure S3 bucket with versioning and encryption” into code?
If the output — a Terraform script — is already deterministic and well-structured, why introduce a probabilistic model to guess what we already know?
And if doing so requires layers of guardrails, validations and evals just to make the result behave deterministically, we have to ask why we took the probabilistic approach in the first place.
### Underestimating chain effects
AI agents aren’t limited to isolated, standalone tasks — and that’s the point. To be meaningful to business stakeholders, they must be integrated into real business workflows, solving more complex, interconnected problems.
But when we link probabilistic tools together, we introduce a chain of uncertainty (Figure 1). A single misstep — like a misunderstood input or misclassified context — can cascade through the system, leading to compounding, confident failures.
Figure 2: An example of chained AI agents in clinical trial management, where compounding errors across agents can lead to unauditable and high-risk outcomes.  Figure 2: An example of chained AI agents in clinical trial management, where compounding errors across agents can lead to unauditable and high-risk outcomes. 
In traditional digital products, a product owner could afford to focus on the “happy path.” The “sad path” — edge cases, input validation, failure modes — was someone else’s job: an analyst to define it, a developer to implement it.
But with AI agents, especially when chaining multiple probabilistic components, that model breaks down. Product designers and owners now face a new kind of ambiguity: How do you define a “sad path” when every step is a guess?
While we celebrate the “art of the possible,” what’s often overlooked is the “disaster of the possible.” The hidden risk isn’t just in what the system can’t do — it’s in what it thinks it can do, but gets wrong.
These underestimated chain effects are where many agentic AI initiatives falter — especially in enterprise environments where workflows have real consequences.
### Paving cow paths and entrenching dysfunction
In his seminal 1990 HBR piece [Reengineering Work: Don’t Automate, Obliterate](https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate), Michael Hammer warned:
“It is time to stop paving the cow paths. Instead of embedding outdated processes in silicon and software, we should obliterate them and start over.”
That quote is just as relevant in the age of AI.
Using AI Agents to automate a broken process doesn’t make it better; it makes the dysfunction faster, harder to detect and harder to audit, especially when it's painted over with a layer of AI
Take the classic layered escalation model in IT operations — a structure built in the 1990s. Designing an AI agent to automate escalation may seem helpful at first, but it often reinforces the very inefficiencies we should be eliminating. If escalation causes delays and rework, automating that step doesn’t solve the root problem — it entrenches it. The better question isn’t “How can an AI escalate this ticket faster?”It’s “Why do we need to escalate it at all?”
Escalation is often a symptom of skillset silos or rigid support hierarchies. The real opportunity is to use AI to resolve issues before escalation becomes necessary, not to optimize a workaround born from structural compromise.
### Using AI as a vanity amplifier
Using AI to decorate trivial outputs won’t make them meaningful. AI agents that amplify the byproducts of a process — rather than the outcomes — simply scale the noise.
Whether it’s generating flashy dashboards, auto-polishing slide decks, or writing process reports no one reads, these agents contribute nothing to the core value. Vanity metric augmentation and artifact generation may look impressive, but they often obscure the absence of real progress.
The right AI product strategy must serve the outcomes, not embellishing the process around them. The goal should be to skip unnecessary artifacts altogether and move closer to the point where value is actually created.
In other words: don’t automate the output if the output didn’t matter in the first place.
### Useless agent loop
The vanity amplifier often sets the stage for an even worse failure: the useless agent loop.
It starts when agent #1 generates or amplifies some in-process artifact — a meeting summary, a dashboard or a performance report. But the output is messy, verbose or unclear; so, we introduce Agent #2 to simplify, summarize or reformat it.
Now you’ve got two AI agents in a feedback loop. One is creating complexity, while the other is trying to clean it up — all centered around an artifact that didn’t even need to exist in the first place.
What emerges isn’t intelligence — it's an infinite loop. A recursive waste of compute and attention.
If the loop exists to manage its own byproducts, you’re not solving a problem — you’ve just automated the mess.
### Cognitive overload
AI agents are meant to reduce cognitive load — not increase it. Yet their creative, guessing nature often leads users into long, polished, but unstructured conversations, where the path feels productive until the user realizes they’ve lost the thread entirely.
While we can extend an AI’s context window, we shouldn't forget that humans have one too. After a few rounds of prompting, corrections and re-prompts, users often lose track of what’s been said, what’s been done and what they’re even trying to achieve.
A typical AI agent–driven RCA tool with an extended context window — but no UX support to help humans process and navigate that context.  A typical AI agent–driven RCA tool with an extended context window — but no UX support to help humans process and navigate that context. 
Conversational UI isn’t efficient for high-load cognitive tasks. This demands a rethink in agent design. Product teams must consider new UX patterns for:
  * **Context anchoring** : show users where they are in the flow.
  * **Short-term memory aids** : recap decisions, show history, clarify current task.
  * **Escape hatches** : let users reset, rewind, or exit loops.


When users must constantly manage, verify or course-correct the agent, it stops being an assistant and becomes a cognitive liability.
### Solutionism
The classic trap of solutionism is alive and well in the AI era. [Jian-Yang’s smart fridge](https://www.youtube.com/watch?v=K3pYZwol6Dc) from Silicon Valley just got an upgrade — it’s now powered by a large language model and a friendly AI voice, telling you what to cook with leftover Coke.
Yes, an LLM can tell you what to do with the contents of your fridge. Yes, it can order a pizza on your behalf. That doesn’t mean those are legitimate problems to solve.
Just because something is technically possible doesn’t make it desirable or valuable. Customers don’t buy AI; they buy outcomes, just as they did 15 years ago with a smart phone, 30 years ago with the internet and 50 years ago with a computer.
## Focusing on what matters
A hyped technology is always a mix of excitement, partial understanding, FOMO and genuine ambition. The rise of AI agents is no exception.
We don’t write this to criticize experimentation or dampen innovation — both are vital to any paradigm shift. But if we want to move from hype to real, durable value, we need to proceed with clear eyes.
The failure patterns we’ve outlined aren’t hypothetical; they’re having real-world consequences. Some come from our own missteps. They emerge when teams misapply probabilistic tools, amplify what doesn’t matter or automate processes they should have reimagined. They reinforce an age-old truth: technology doesn’t fix bad design; it scales it.
The good news is that the old lessons still apply:
  * Start with real problems — never build Jian-Yang another smart fridge.
  * Don’t pave the cow paths.
  * Don’t solve deterministic problems with probabilistic tools.
  * Always simplify.


Yes, AI agents are powerful, but they’re still software. And success, as ever, depends not on what we call them, but on how we design, integrate and govern them.
**Let’s build carefully and let’s build things that matter.**
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
## Related content
  * [ AI and ML Agentic AI | Perspectives  Learn more ](https://www.thoughtworks.com/en-gb/perspectives/edition35-agentic-ai)
  * [ AI and ML Agentic AI at work  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/machine-learning-and-ai/agentic-AI-at-work)
  * [ Generative AI AI agents don't have to be a security nightmare  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/ai-agents-dont-security-nightmare)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Discover fresh perspectives and new ideas on the Technology Podcast
[ Listen now ](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts)