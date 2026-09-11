<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/casper-helping-developers-work-effectively-with-coding-assistants | Title: Casper: Helping developers work effectively with coding assistants | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Casper: helping developers work effectively with coding assistants 
[ Engineering Stack Back ](https://www.thoughtworks.com/en-gb/engineering)
Close


By 
Published: March 24, 2026 
When a team of software delivery specialists set out to improve how developers use AI coding assistants, they weren’t looking to build a new tool from scratch. Instead, they wanted to shape a repeatable, adaptable workflow that helps people get the best out of AI coding assistants while avoiding common pitfalls.
The result was Casper — a simple but powerful, rule-based framework designed to work inside any coding assistant. Casper guides developers through a structured three-phase approach to producing high-quality code with AI: explore, craft and polish.
## The problem we were trying to solve
When developers start using AI coding assistants, they often go through what we call the “honeymoon phase” — productivity seems to skyrocket, tasks that took hours are done in minutes. But delight at that boost in productivity can quickly sour, as developers work with code being generated: each new fix is breaking something else, and the code base is becoming a mess; on occasion, the assistant might declare that it's done, but nothing is working. 
Your team will then hit the "disillusionment phase” hits. You might find that the coding assistant has generated hundreds of lines of code, when a dozen would have sufficed. Code becomes overly complex, best practices are ignored and AI makes incorrect assumptions (hallucinations).
Casper was created to provide a structured workflow that gets developers past that frustration phase and keeps AI contributions aligned with good engineering practice.
## How does Casper work?
Casper runs entirely on natural-language rule files rather than custom code, making it portable across different AI coding assistants.
It follows three phases:
  1. Explore. Before writing any code, Casper prompts the developer with targeted questions about edge cases, technical approaches and functional requirements. This mirrors how a human would conduct thorough analysis before starting work, reducing the risk of unspoken assumptions. The result is a set of exploration notes capturing agreed-upon functionality and technical direction. 
  2. Craft. Using those notes, Casper encourages a test-driven development (TDD) approach. It generates an initial list of test cases, which the developer reviews and refines. The story is then implemented one test case at a time, producing small, readable code changes. This prevents AI from generating overly long or complex code blocks that are hard to review. 
  3. Polish. Independently from the implementation phase, Casper runs validation checks: does the code meet acceptance criteria? Were all edge cases handled? Is the coding style consistent? This final pass can uncover missing test cases, error handling or refactoring opportunities.


## What makes this different from just using an AI coding assistant?
Without guidance, AI assistants tend to generate large chunks of code quickly — which is impressive but risky. Casper introduces process discipline — what Thoughtworks refers to as sensible defaults — into AI-assisted coding, so road-tested practices like TDD, building for production and security-first thinking are part of every story.
Because Casper is rule-based and written in plain language, teams can easily adapt it for different project contexts — for example, focusing more on refactoring in a brownfield project or integrating extra checks for security-sensitive systems.
## What challenges did you encounter while implementing Casper?
Like any workflow, Casper evolved through trial and error.
Early on, the team noticed that the AI sometimes deleted existing test files when adding new tests. This was traced to a misused internal function in the coding assistant. The fix was simple once identified — another benefit of using a flexible, rule-based approach.
More broadly, adoption was gradual. In the initial rollout, about 30 out of 80 developers in the project used Casper regularly; that number was expected to grow to around 50 within weeks. Each team’s feedback helped refine the rules and improve reliability.
## How clients have responded
While clients were not directly involved in Casper’s design, they did have early questions about security and risk when introducing AI tools. The team addressed these by running workshops, demonstrating the workflow, and working with platform providers (e.g., AWS Bedrock) to ensure data security guarantees were clear and contractually covered.
## What are the key lessons learned?
  * Structure beats spontaneity. AI works best when it follows a process designed for human-AI collaboration.
  * Natural-language rules are powerful. They make the workflow tool-agnostic and easy to adapt. Human review remains essential. AI can do much of the heavy lifting but final judgment on quality still comes from people.
  * Gradual adoption works best. Expanding usage in phases allows teams to refine the approach without overwhelming developers. 


## What’s next for Casper?
The team is exploring how to let AI take over parts of the workflow autonomously when a developer is unavailable. For example, if a developer has completed four out of ten test cases before being pulled into a meeting, Casper could delegate the remaining six to AI agents — one to write the code, another to review it — and present a pull request for human review upon return.
This vision of multi-agent collaboration could extend Casper’s reach even further, turning it from a guided workflow into an active coding partner.
## Augmenting coding assistants
Casper shows that the real opportunity in AI-assisted coding isn’t just about having a smarter AI — it’s about having smarter ways for AI to help humans. By embedding good practices into a flexible, tool-agnostic workflow, teams can harness the speed of AI without sacrificing quality, maintainability or security.
The experiment demonstrates a core truth about AI in software delivery: productivity gains are only sustainable when they’re built on strong engineering discipline — and sometimes, the best way to teach AI discipline is to give it a friendly ghost in the IDE.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
## Related content
  * [ Generative AI The future of software development: AI speed, human judgment  Learn more ](https://www.thoughtworks.com/en-gb/insights/articles/the-future-of-software-development-AI-speed-human-judgment)
  * [ Generative AI Inside AI/works™: An agentic development platform  Learn more ](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/inside-ai-works-agentic-development-platform)
  * [ AI and ML AI-first software engineering | Perspectives  Learn more ](https://www.thoughtworks.com/en-gb/perspectives/edition36-ai-first-software-engineering)


## We're helping organizations successfully leverage AI 
[ Find out how ](https://www.thoughtworks.com/en-gb/ai)
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