<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/experiment-github-copilot-practical-guide | Title: Our experiment with GitHub Copilot: A practical guide for development teams | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Our experiment with GitHub Copilot 
A Practical Guide for Development Teams
[ Engineering Stack Back ](https://www.thoughtworks.com/en-gb/engineering)
Close


By 
Published: April 03, 2025 
AI is transforming industries, and software development is no exception. From automated code generation to intelligent debugging, AI is reshaping how developers write and maintain code. Among the many AI-driven tools available today, GitHub Copilot stands out as one of the most discussed and widely adopted solutions. But does it truly enhance productivity, or does it introduce more overhead?
## A real-world Copilot experiment
When we first introduced GitHub Copilot into our team, we had two big questions:
  1. **Would it actually make us faster?**
  2. **Or would we spend more time fixing AI-generated mistakes than writing code ourselves?**


After 10 weeks, we found clear answers. To be clear: this isn’t another generic Copilot review — it’s a firsthand account of what worked, what didn’t, and what teams should consider before rolling it out.
## Where could we leverage AI?
When we first discussed AI adoption with our stakeholders, they were genuinely interested but cautious. They saw the potential but weren’t willing to invest millions without a clear, guaranteed outcome. They wanted to see the impact without massive investment. After careful consideration, we identified AI-assisted software delivery as our starting point.
Here’s why this approach made sense:
  * No infrastructure changes were needed
  * No disruption to development teams
  * Clear focus on augmenting, not replacing, engineers
  * Measurable ROI through existing delivery metrics
  * Low initial investment (just licensing costs)


## Setting up the experiment
With this approach in mind, we swiftly secured approval, assembled a small team, and initiated our experiment. The table below outlines the structure of our experiment.
Copilot integration roadmap: 10-Week implementation journey  Copilot integration roadmap: 10-Week implementation journey 
## Approval with a condition: Proving real impact
We got the green light, but with a key condition — we needed clear metrics on the outcomes. It wasn’t enough to say, “Copilot improved productivity.” 
Our stakeholders wanted quantifiable proof:
  1. Whether it actually helped — and if yes, to what extent?
  2. Did it improve developer experience but slow down delivery?
  3. Did code quality suffer in the process?


## The gap in AI metrics
As we engaged with colleagues and the developer community, we noticed a pattern. Most existing Copilot evaluations focused on technical accuracy, things like:
  1. How often were AI suggestions correct?
  2. How well Copilot understood context.
  3. How frequently developers accepted its recommendations.


But what was missing was a real-world assessment of how Copilot impacted team delivery: Did AI-assisted development actually make teams faster?
## Our measurement framework
To bridge this gap, We implemented a comprehensive measurement framework focusing on four key areas beyond just code suggestions:
  * **Velocity impact**
    * Short-term velocity: Did Copilot help close more user stories?
    * Long-term velocity: Were these improvements sustained over multiple sprints?


  * **Code quality**
    * Did AI-generated code introduce technical debt?
    * Were there more code smells, duplicate code, or cyclomatic complexity issues?


  * **Developer experience and productivity**
    * Time saved per developer: Did Copilot reduce time spent on tasks?
    * Cognitive load: Did developers feel more focused or distracted by AI suggestions?
    * Adoption rate: How many developers actively used Copilot after the initial phase?


  * **Delivery throughput**
    * Did the overall story cycle time improve?
    * Were we closing more features and bug fixes per sprint?


With these metrics in place, we had a structured way to objectively measure Copilot’s impact.
## Enforcing metrics through CI/CD
Defining our approach was just the first step. The real challenge was tracking Copilot’s impact consistently. Manual measurement wasn’t enough, we needed automated safeguards to maintain code quality and security.
To tackle this, we reinforced critical safeguards within our CI/CD pipelines.
  * Code Coverage — 90% minimum to prevent AI-generated code from reducing test quality.
  * Automated checks for code smells, redundancy and cyclomatic complexity etc.
  * Security checks, including dependency scanning and security linting.
  * Architecture fitness functions, which ensured structural integrity.


## Experiment: The two faces of Copilot
With the right framework in place, we conducted our experiment. Through this process, we thoroughly explored two core features of GitHub Copilot: Inline Assistance and Chat Assistance. Below are the key focus areas where we ran our experiment.
Our AI-powered development lifecycle  Our AI-powered development lifecycle 
One clear pattern emerged — both Copilot and the developers improved over time. As our team used Copilot more, it began understanding the context better, and developers discovered techniques to maximize its usefulness.
However, an unexpected challenge arose — we realized we were gradually drifting away from [test-driven development (TDD)](https://www.thoughtworks.com/insights/blog/generative-ai/tdd-and-pair-programming-the-perfect-companions-for-copilot).
## The TDD shift: A challenge we had to fix
Our teams traditionally followed TDD principles — writing tests first, code second. But with Copilot in the mix, we noticed a shift — developers started solving problems first, then writing tests.
Recognizing this drift, we took corrective measures to realign with TDD.
  * We trained developers on how to prompt Copilot for test cases first, before asking for solutions.
  * Additionally, we leveraged the framework to ensure test coverage was maintained through CI/CD gates.


At first, this shift was difficult, but over time, the team adapted and got back on track.
One way to enhance these suggestions is by using predefined prompts. These can be particularly useful for small, repetitive tasks. For example, [this](https://github.com/PatrickJS/awesome-cursorrules/tree/main) repository contains prompts for various use cases. Similarly, you can create customised prompts for your team based on your project’s standards.
## Some observations on software development with Copilot
By the end of the assessment, here’s what we observed at a high level:
When we first introduced Copilot, productivity gains weren’t immediate. In fact, during the initial stages, we often spent more time using Copilot than we would have without it, as developers adjusted to AI-assisted workflows. However, once we overcame this learning curve, the benefits became clear.
Before Copilot, our team completed 20 user stories per sprint. Now, we complete 23 user stories per sprint, three more stories per sprint, a whopping 15% increase in velocity without any extra effort. 
For a team of four developers, this efficiency gain is equivalent to adding a full developer’s worth of output without hiring. At the organization level (10 teams), this translates to 30 additional user stories per sprint — the equivalent of six full-time developers’ output, delivering 6 additional features without increasing headcount.
That said, Copilot's impact wasn't uniform across all tasks. While some stories showed a 40% improvement, others saw only 10%, and in some cases, productivity even declined by 5%. This demonstrates the varying effectiveness of Copilot across different development scenarios.
The effectiveness of Copilot depended on several factors like task complexity, domain knowledge, code isolation and other factors.
### Where did Copilot work well?
Here's where we found Copilot to be effective:
  * Projects using well-known tech stacks
  * General rather than specialized domains
  * Simple, isolated problems with well-defined boundaries
  * Environments with strong IDE support
  * Small to medium-sized code generation


### Where did Copilot struggle?
Here are the areas where Copilot wasn't that effective:
  * Projects using unfamilar or niche technologies
  * Highly specialized or domain-specific problems
  * Complex and interconnected problems
  * Problems that can't be easily isolated
  * Environments with limited IDE support
  * Large-scale code generation


But wait — it’s not quite that simple! These factors actually interact with each other in interesting ways. 
For example:
  * A complex problem might be manageable if you have strong tech stack knowledge
  * A large codebase might be less challenging with good IDE support
  * Even domain-specific problems can be handled well if they’re properly isolated


On average, we observed a 15% reduction in development time, which was significant enough to justify a full rollout of Copilot across teams. By the end of the experiment, our team’s velocity had improved by 15%, demonstrating that AI-assisted development, when used correctly, can be a valuable accelerator.
### Alternative coding assistance options
For organizations with specific concerns about GitHub Copilot, we did some initial exploration of alternatives:
  * Open-source LLMs like Ollama for local deployment
  * Custom-trained models for specific domains
  * Hybrid approaches combining multiple tools


While we’ve done only preliminary testing of these options, they show promise but require thorough evaluation based on organizational needs.
### Looking ahead...
The AI-assisted development landscape is evolving at a remarkable pace, with exciting new tools like Cursor AI, Amazon CodeWhisperer, and Codeium revolutionising the way we think about AI pair programming. Each of these innovations offers unique possibilities making it an excellent and challenging time for teams and organisations to explore and experiment with these emerging solutions.
## Final thoughts on experimenting with GitHub Copilot
For our team, Copilot proved to be a valuable accelerator — but only when used strategically. These metrics are specific to our experience, and your results may vary. The key isn’t just adopting AI, it’s adopting it thoughtfully, with clear goals and framework in place.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
  * [ Generative AI Claude Code saved us 97% of the work on the first try. Then it failed utterly.  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/claude-code-codeconcise-experiment)
  * [ Generative AI Demystifying DeepSeek  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/demystifying-deepseek)
  * [ Generative AI How much faster can coding assistants really make software delivery?  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/how-faster-coding-assistants-software-delivery)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## We help engineering teams successfully leverage AI
[ Learn more ](https://www.thoughtworks.com/en-gb/what-we-do/ai-first-software-engineering-transformation)
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