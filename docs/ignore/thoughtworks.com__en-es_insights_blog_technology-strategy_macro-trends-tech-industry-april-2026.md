<!-- Source: https://www.thoughtworks.com/en-es/insights/blog/technology-strategy/macro-trends-tech-industry-april-2026 | Title: Macro trends in the tech industry | April 2026 | Thoughtworks Spain | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Macro trends in the tech industry | April 2026 
[ Blogs Back ](https://www.thoughtworks.com/en-es/insights/blog)
Close


By 
Published: April 15, 2026 
The last few editions of the [Technology Radar](https://www.thoughtworks.com/radar) have captured relentless AI-accelerated change in the industry. However, while recent volumes have reflected the astounding energy of the field, from the proliferation of new tools to the almost monthly emergence of new terms and concepts, volume 34 is different: it highlights a level of maturity, a moving away from endless experimentation to a desire for repeatability and stability and something cognitively manageable.
However, this isn’t to say things are stabilizing: the macro trends in the tech industry reflected in volume 34 all speak to unresolved tensions — reliability and AI’s unpredictability, AI-acceleration and developer experience and past and future practices. 
## Searching for consistency and reliability
Consistency and reliability have always been significant concerns in AI. However, in the early part of 2026 they appear to have shifted from one of many issues to one of the most critical. Perhaps driven by increasing adoption and the step change in capabilities we witnessed at the end of 2025, the best evidence of this is the emergence of the term ‘harness engineering’ in recent months. 
### Harness engineering
Broadly speaking, [harness engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html) refers to the infrastructure, constraints and feedback loops that wrap around AI agents to improve their reliability. Part of this is an extension or evolution of spec-driven development (SDD); one of the ways in which we can harness agents is by using SDD frameworks such as [OpenSpec](http://www.thoughtworks.com/radar/tools/openspec) and [GitHub SpecKit](http://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit) to provide guardrails and structured workflows. 
However, it also goes beyond this to consider the ways in which agents ‘learn’ and self-correct. In this edition we featured something called the ‘[feedback flywheel](http://www.thoughtworks.com/radar/techniques/feedback-flywheel)’, which essentially adds a further step to the spec → plan → implement flow typical in SDD aimed at iteratively improving the coding agent. It’s worth flagging a number of techniques here including [feedback sensors for coding agents](http://www.thoughtworks.com/radar/techniques/feedback-sensors-for-coding-agents) to reduce the manual review burden and provide agentic systems with the capacity to improve themselves.
### Sandboxing
This apparent desire for increased reliability arguably suggests a growing awareness of the many risks associated with AI and agent assistants in software engineering. However, while we welcome the expansion of risk-aware practices like [sandboxing coding agents](http://www.thoughtworks.com/radar/techniques/sandboxed-execution-for-coding-agents), demonstrated in blips on this Radar including [Dev Containers](http://www.thoughtworks.com/radar/tools/dev-containers) and [Sprites](http://www.thoughtworks.com/radar/platforms/sprites), it would be wrong to think there’s been an industry about-face. There’s certainly lots of high-risk experimentation happening, including [agent coding swarm](http://www.thoughtworks.com/radar/techniques/coding-agent-swarms) projects like Steve Yegge’s Gastown. While these are intriguing and may offer insight for the future of software engineering, as we note in this volume, these need to be approached with caution.
It’s also worth noting the importance of agent durability in the context of reliability. We’ve noticed that [ignoring agent durability](http://www.thoughtworks.com/radar/techniques/ignoring-durability-in-agent-workflows) is a bit of an antipattern, with teams successfully developing agent workflows only to find they fail when deployed to production in complex distributed systems. Bringing durable computing approaches and tools such as Golem and Temporal to bear on these use cases can help minimize the risks of execution failures.
## Rethinking developer experience and productivity
Many of the practices that grapple with AI reliability are closely related to the question of the role of the developer in the software development process: where should the humans have control? What needs to be reviewed? What needs to be iterated manually and what can be automated? 
One of the things that’s becoming clear is that ‘agentic’ coding poses challenges for developer experience. This is something we’ve been thinking about a lot at Thoughtworks; indeed, even before we began putting this volume of the Radar together, the potential for AI workflows to degrade developer experiences, leading to a divergence between productivity and personal flow and satisfaction, was a significant topic of discussion at Martin Fowler’s [Future of Software Development Retreat](https://www.thoughtworks.com/about-us/events/the-future-of-software-development).
### Measuring the right things
Undoubtedly some of the challenges are cultural, informed by misunderstandings of what AI can and cannot do. For instance, despite long-running discussion on this topic, we thought it was still important to caution against using [coding throughput as a measure of productivity](http://www.thoughtworks.com/radar/techniques/coding-throughput-as-a-measure-of-productivity). As an alternative we suggest [measuring collaboration quality with coding agents](http://www.thoughtworks.com/radar/techniques/measuring-collaboration-quality-with-coding-agents) using metrics such as iteration cycles per task, post-merge rework and failed builds. This shifts the focus in a way that ensures developers are focusing on the right things and should ultimately lead to higher quality software being delivered.
### MCP scepticism and the return to the command line
One of the major shifts in the experience of developing with AI is the shift away from MCP. While it was hailed as a game-changer 12 months ago, in many instances it isn’t necessary, which is why we’ve cautioned against [MCP by default](http://www.thoughtworks.com/radar/techniques/mcp-by-default). This isn’t to say it shouldn’t ever be used but instead that there are often more appropriate approaches that avoid what Justin Poehnelt calls ‘[the abstraction tax](https://justin.poehnelt.com/posts/mcp-abstraction-tax/)’.
Interestingly, it appears reservations around MCP have led to a return to the command line. One of the reasons for this is [Agent Skills](http://www.thoughtworks.com/radar/techniques/agent-skills), an open standard that packages instructions, executable scripts and other associated resources to modularize and progressively disclose context to coding agents. This means that rather than interfacing with an MCP server, a given skill can be called in the command line. In addition to Agent Skills is the [Claude Code plugin marketplace](http://www.thoughtworks.com/radar/tools/claude-code-plugin-marketplace) which we’ve found is significantly improving the developer experience and collaboration; workflows and other resources can be easily synced with the CLI.
## The importance of older and established practices
The return to the command line points to another trend we noticed during Radar discussions: persistence or re-emergence of older and established technologies and practices.
To a certain extent this is a corrective to the period of novelty and experimentation we’ve been living through; when things are constantly changing, ensuring there are robust and even familiar foundations takes on even greater importance. Measuring the right things is something we’ve already discussed; we wanted to emphasize how critical this is by placing the [DORA metrics](http://www.thoughtworks.com/radar/techniques/dora-metrics) on this edition of the Radar. Yes, they’re almost as old as the Technology Radar itself (introduced more than a decade ago), but they have a vital role to play in helping teams ensure they’re focusing on what’s most critical even when practices and technology shapes are continually evolving. We even noted in the write up for that particular blip that using the DORA metrics effectively doesn’t require sophisticated and complex tracking and dashboards; if anything these can be a distraction, and, as we write, “simple mechanisms, such as check-ins during retrospectives” can be much more powerful.
Another established technique that we’ve featured in this volume of the Radar is zero trust architecture. First appearing on the Radar in May 2020 and moved to Adopt in October 2021, we wanted to bring attention to it half a decade later. “Principles such as ‘never trust, always verify,’ along with identity-based security and least-privilege access, should be treated as foundational for any agent deployment,” we write. 
We also talked a lot about testing too, this time discussing [mutation testing](http://www.thoughtworks.com/radar/techniques/mutation-testing) and building on last edition’s mention of [fuzz testing](http://www.thoughtworks.com/radar/techniques/fuzz-testing) by featuring [WuppieFuzz](http://www.thoughtworks.com/radar/tools/wuppiefuzz). These techniques certainly aren’t new, but recent developments in AI are both lowering the barrier to entry and making it more important to test for a wider range of unpredictable behaviors.
## Cognitive debt
What ties this all together is the issue of cognitive debt. Yes, AI can accelerate many parts of the software development process — far beyond just writing code — but in doing so it does two things: first, it creates greater distance between developers and the software they’re responsible for and, second it increases the range of tasks and problems they may be working on. 
We caution against [codebase cognitive debt](http://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt) on this edition of the Radar, but it’s also important to think beyond day-to-day work to recognize how we may individually incur cognitive debt as professionals. If you offload everything to a coding assistant, what are you avoiding learning? And what might the impact be in the future? Of course, this is always a question of trade-offs; an important part of a developer’s skillset is knowing what to pay attention to. However, given the speed of AI-accelerated change, consistent self-reflection is important as a reminder of our agency.
For all the novelty in the industry at the moment, much of the most interesting work in this area is exploring exactly how we can manage cognitive debt, whether that’s at an individual, project or organization level. We’re excited to continue monitoring this work in future volumes and contributing to ideas and practices that help technologists everywhere.
  * [ Generative AI The cognitive demands of AI novelty  Learn more ](https://www.thoughtworks.com/en-es/insights/blog/generative-ai/cognitive-demands-ai-novelty)
  * [ Technology strategy Key themes in Technology Radar Vol.34  Learn more ](https://www.thoughtworks.com/en-es/insights/podcasts/technology-podcasts/themes-technology-radar-34)
  * [ AI and ML From vibe coding to context engineering: 2025 in software development  Learn more ](https://www.thoughtworks.com/en-es/insights/blog/machine-learning-and-ai/vibe-coding-context-engineering-2025-software-development)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Gain a fresh perspective on tech today with the Technology Podcast
[ Listen now ](https://www.thoughtworks.com/en-es/insights/podcasts/technology-podcasts)
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