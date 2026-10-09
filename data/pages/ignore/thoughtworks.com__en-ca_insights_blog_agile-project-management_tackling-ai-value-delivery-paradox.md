<!-- Source: https://www.thoughtworks.com/en-ca/insights/blog/agile-project-management/tackling-ai-value-delivery-paradox | Title: Tackling the AI value delivery paradox | Thoughtworks Canada | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Tackling the AI value delivery paradox 
[ Blogs Back ](https://www.thoughtworks.com/en-ca/insights/blog)
Close


By 
Published: May 19, 2026 
We’re witnessing the AI value delivery paradox: while AI tools allow engineers to generate code at unprecedented speeds, many CTOs have yet to see a corresponding impact on time-to-market, as highlighted in the [recent Harvard and Jellyfish study](https://jellyfish.co/blog/harvard-jellyfish-ai-is-making-developers-faster/). The reason is simple: deploying agentic AI on its own doesn’t accelerate the software value chain but often stresses it.
Think of your organization as a dam. The infrastructure was built for a certain throughput of water. If you force 10x more water (code and new functionality) through the same pipes, you don’t get 10x more electricity; instead, you risk structural failure. It’s only if your architecture, organizational structure and processes can effectively channel a 10x faster coding phase will you see a positive effect. The question is no longer will AI help us write code? It’s  _how must our tech estate and organizations evolve to safely absorb and sustain this new velocity?_
## Strategic starting points for transformation
The answer depends on your organization's starting point. Typically, they fall into two categories:
  * AI-first digital transformation. If your digital transformation is ongoing or hasn't truly taken root, you face a foundational challenge. This requires rethinking digital architecture, moving from projects to products and shifting from functional to cross-functional teams. Upskilling in TDD, CI/CD and removing technical debt via the "[inverse-Conway maneuver](https://www.thoughtworks.com/en-de/insights/blog/customer-experience/inverse-conway-maneuver-product-development-teams)" is essential. An AI-first approach can compress this change so rapidly that catching up becomes highly worthwhile.
  * AI transformation. If you already have a mature digital estate, your challenge is [unlearning](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/unlearning-experimentation-engineering-rigor-agentic-world). You’re faced with the sunk cost fallacy and change fatigue while needing to disrupt established architectures and practices.


Realizing the return on AI investments requires leaders to be honest about their current capabilities. AI assistants are powerful but expensive and smart, AI-powered product features are expensive to run. Getting the foundation right is critical to avoid speed at the cost of EBITDA, employee satisfaction and customer experience.
## Think of living, adaptive systems: Tissue vs. cell
To prevent the organizational dam from breaking with agentic AI, we must think systemically. A lot of moving parts are in play during transformations. Borrowing terms from biology can help us differentiate the core components of a modern tech organization: the "cell" and the "tissue".
  * **The cell.** This is where products are developed. Thanks to generative AI, the inner loop of development (coding, testing and CI/CD) can be an agentic single, high-speed flow. This is the organ that does the primary work. 
  * **The tissue.** This is the connective substance that wraps around the cells. It handles cross-cutting concerns like identity, customer channels, security and common data. The goal of the tissue isn’t to introduce new bottlenecks but to provide a collection of smart value chain interfaces and automated guardrails that adapt to cell needs. 


The challenge is to design and run a tissue which is increasingly machine-readable. An AI agent in a cell might generate a perfect feature, but it cannot push until it satisfies the gated surface of the tissue (e.g., MFA or SOC2 compliance) in real-time, without human gatekeepers.
## Governing 'tissue': Scaling through adaptable machine-readable guidance
In an AI-first transformation, the tissue makes the organization accessible to AI agents, who cannot wait in manual approval queues. Each capability represents a team or group boundary with which the rest of the organization communicates in an automated, self-service manner.  
Tissue capabilities  
|  **Tissue capability**  |  Highlight  | Examples  |  
| --- | --- | --- |  
| Gated surface  | The engagement block acts as a buffer zone for secure, consistent interaction with the outside world.  | App/web shells using MFEs, conversational surfaces for intent registry and machine-readable gateways.  |  
| Machine-ready supervision  | Encoded guided autonomy where value chain interfaces provide guardrails and sensible defaults in machine format.  | Policy-as-code baked into CI/CD, restricted identity/access for agents and FinOps for token monitoring.  |  
| Common memory  | Ensures systemic intelligence maintains coherence across expanding cells rather than fragmenting.  | "Golden record" data (e.g., customer entities) enabling cross-segment agent comprehension.  |  
| Crucial foundations  | Product-agnostic base software and XaaS capabilities that enable the rest of the tissue and cells to jumpstart.  | IaC provisioning, CI pipeline templates and centralized cloud power for unit economics.  |  
Tissue capabilities  
|  **Tissue capability**  |  
| --- |  
| Gated surface |  
| Machine-ready supervision |  
| Common memory |  
| Crucial foundations |  
|  Highlight  |  
| --- |  
| The engagement block acts as a buffer zone for secure, consistent interaction with the outside world. |  
| Encoded guided autonomy where value chain interfaces provide guardrails and sensible defaults in machine format. |  
| Ensures systemic intelligence maintains coherence across expanding cells rather than fragmenting. |  
| Product-agnostic base software and XaaS capabilities that enable the rest of the tissue and cells to jumpstart. |  
| Examples |  
| --- |  
| App/web shells using MFEs, conversational surfaces for intent registry and machine-readable gateways. |  
| Policy-as-code baked into CI/CD, restricted identity/access for agents and FinOps for token monitoring. |  
| "Golden record" data (e.g., customer entities) enabling cross-segment agent comprehension. |  
| IaC provisioning, CI pipeline templates and centralized cloud power for unit economics. |  
[ Expand table ](javascript:void\(0\))
[ Collapse table ](javascript:void\(0\))
## Empowered 'cells': Guided autonomous value delivery
The heart of each organization is the ‘cell,’ where autonomous, high-speed teams own outcomes through vertical, end-to-end scope slices, here called ‘product groups.’ By cutting the organization into these slices rather than horizontal layers, we eliminate the hand-off delays that typically break the software value chain. To enable high speed teams it’s important to consider the role of legacy tech, too.
### Legacy modernization and sundowning
Most companies operate in a messy middle between target architecture and legacy debt. To enable guided autonomy, core modernization must involve the AI-enabled decoupling of legacy systems. Using "facade" tactics like the [strangler fig pattern](https://www.thoughtworks.com/insights/articles/embracing-strangler-fig-pattern-legacy-modernization-part-one), agents can rapidly create modern API wrappers around legacy services. This allows high-velocity cells to interact with the old world without being slowed down, eventually dismantling legacy layers through automated synchronization pipelines.
### Product group
Product groups [represent clearly delineated scope for maximizing speed of value delivery while making sure to reach best product market fit](https://www.thoughtworks.com/en-de/insights/blog/digital-transformation/how-to-create-and-leverage-a-product-map-in-your-organization). The scope is a vertical, end-to-end cut through the product landscape. To discuss agentic AI in this context, let’s have a look at proven ways for product development.
Effective tech organizations have mastered [dual-track value delivery](https://www.thoughtworks.com/en-de/insights/decoder/d/dual-track-development). This is when discovery and engineering work run in parallel and both feed back to each other constantly to build the best possible product. They manage different types of risk, so our interaction with AI across these tracks must be designed intentionally:
  * **Track 1: Discovery (figuring out WHAT to build).** This is human-in-the-loop (HITL). Discovery deals with ambiguity, psychology and nuance. AI synthesizes feedback and generates prototypes, but the human Product Owner makes the final empathic and strategic leap.
  * **Track 2: Engineering (figuring out HOW to build it).** This is human-on-the-loop(HOTL). Software execution is supposed to be deterministic. The product engineer evolves into an orchestrator who defines constraints (context/[harness engineering](https://martinfowler.com/articles/harness-engineering.html), TDD, deployment pipelines etc.) and allows coding agents to iterate on coding tasks until the code passes the tests. The human intervenes only when, for example, policy-as-code gates are challenged.


## Role evolution: From doers to orchestrators
The most fragile component of the "AI-volution" is the psychological shift. Highly skilled "doers" must become "value delivery orchestrators." While not everyone will bridge this gap, there are possible development pathways:
  * **Pathways toward discovery:** Roles with strong stakeholder alignment skills could pivot to become data-driven product owners or UX architects.
  * **Pathways toward engineering:** QA testers and release engineers move toward the system's "breaking points," upskilling into product engineers or infrastructure specialists who build the CI/CD gates that make autonomy possible.


Enabling this transition requires building the right orchestration muscle. Training must focus on guiding and critiquing machine-generated output while establishing a feedback loop around the cognitive load paradox: if reviewing agentic AI output creates more toil than manual execution, “tissue” and “cells” must improve on the fundamental capabilities as described above.
## Steering for guided autonomy
Moving fast in the wrong direction is a significant risk. Autonomy through coding agents is only scalable when paired with strategic guardrails and actions:
  1. **Define the right scope:** Use a [product map](https://www.thoughtworks.com/en-de/insights/blog/digital-transformation/how-to-create-and-leverage-a-product-map-in-your-organization) and domain modeling to establish properly bounded end-to-end product groups.
  2. **Establish organization-wide guardrails:** Set sensible defaults (e.g. policy-as-code), FinOps and API standards — as well as relevant feedback loops.
  3. **Define clear accountability and incentives:** Distribute accountability where teams are measured by lagging business metrics (such as revenue, EBITDA) and leading product metrics (adoption, NPS), [not lines of code written](https://www.thoughtworks.com/radar/techniques/coding-throughput-as-a-measure-of-productivity).


In practice, this looks like lightweight governance bodies: a **product forum** ensuring alignment across the portfolio, and an **architecture forum** where technical leaders codify sensible defaults as policy-as-code for deployment pipelines.
## It’s about architecture and people
The AI value delivery paradox is solvable. By deliberately designing the "tissue," the "cells," and evolving talent to navigate paradigm shifts, you stop bolting AI onto broken processes. Instead, you build a fundamentally faster, safer and more resilient tech value chain where humans and AI agents interact seamlessly to drive business value.
  * [ Digital transformation How value slices can fix your digital transformation  Learn more ](https://www.thoughtworks.com/en-ca/insights/blog/digital-transformation/how-value-slices-can-fix-your-digital-transformation)
  * [ Digital transformation Effective steering structures for your digital engineering at scale  Learn more ](https://www.thoughtworks.com/en-ca/insights/blog/digital-transformation/effective-steering-structures-for-your-digital-engineering-at-scale)
  * [ Product innovation Beyond the prototype: The reality of delivering generative AI products  Learn more ](https://www.thoughtworks.com/en-ca/insights/blog/product-innovation/beyond-prototype-reality-delivering-generative-ai-products)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Explore a snapshot of today's tech landscape
[ Read Technology Radar ](https://www.thoughtworks.com/en-ca/radar)