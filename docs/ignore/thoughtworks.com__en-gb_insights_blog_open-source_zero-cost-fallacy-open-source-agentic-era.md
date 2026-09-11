<!-- Source: https://www.thoughtworks.com/en-gb/insights/blog/open-source/zero-cost-fallacy-open-source-agentic-era | Title: The zero-cost fallacy: Open source software in the agentic era | Thoughtworks United Kingdom | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  The zero-cost fallacy: Open source software in the agentic era 
[ Engineering Stack Back ](https://www.thoughtworks.com/en-gb/engineering)
Close


By 
Published: July 09, 2026 
We’re currently living through the friction points of a shift that's been decades in the making, but has unfortunately accelerated sharply under the pressure of generative AI. For years, industry has operated on a comfortable and lazy, myth: that open source software is an infinite, self-renewing public good that costs nothing to consume and requires nothing to sustain.
Discussions at the [Future of Software Engineering Retreat](https://www.thoughtworks.com/about-us/events/the-future-of-software-development-europe-2026) in Switzerland at the end of June 2026 painted a much more fractured and urgent picture. The reality we must face is that open source isn’t simply undergoing an evolution; it's being ground down by structural exhaustion and the industrialization of code generation.
## The economics of exhaustion and the zero cost fallacy
At the heart of the current crisis is a fundamental misunderstanding of asset pricing versus human cost. There’s an economic argument you hear a lot that says the price of a digital asset should gravitate toward the marginal cost of its distribution, which is effectively zero. So, if copying a library costs nothing, the software, theoretically, should be free.
But this elegant theory hides the human labor at the heart of all this. While distribution costs nothing, maintenance is incredibly expensive. Maintainers of critical open-source packages, those invisible pillars holding up modern digital banking, cloud infrastructure and enterprise platforms, are burning out and facing psychological harassment from multi billion dollar entities that consume their labor without contributing a single cent back.
We’ve collectively confused permissive licensing with a license to exploit. Since the rise of cloud, open source advocates championed MIT and Apache licenses as the ultimate victory for software adoption. However, this permissive regime became the bedrock that massive corporations built proprietary empires on, wrapping open-source code in light orchestration and capturing economic value while returning little to the ecosystem. It’s a system of patronage for the lucky few, and a welfare state of charity for the rest. This is fundamentally unsustainable.
## Twin pressures: Slop pull requests and declining trust
If the structural economics of open source were already fragile, the introduction of automated tools has made a chronic condition acute. 
Maintainers are now facing an assault on two fronts.
### The industrialization of slop
The barrier to entry for generating code has dropped to zero. While this empowers individuals, it has also flooded repository gates with an alarming volume of low-quality, AI-generated pull requests. Maintainers who once spent their time writing code are now forced to become full-time, unpaid code reviewers, sifting through automated contributions from individuals seeking to gamify their portfolios. 
This creates a vicious cycle. The psychological, and even emotional, burden sometimes forces maintainers to close their projects to public contributions entirely. This inadvertently cuts off the next generation of legitimate maintainers who would eventually inherit and sustain the project.
### The radical shifts in the trust landscape
The traditional metrics of open-source credibility can no longer be trusted. The timeline for project maturity has collapsed; libraries are skyrocketing to tens of thousands of GitHub stars within weeks, driven by viral AI-agent hype, despite having only a three-week commit history. 
It’s now also incredibly cheap to raise malicious PRs. Agents are finding new attack vectors every day, which makes it challenging for maintainers to do the work that makes trust possible. Taken together, open source’s trust model has been severely degraded and there are no easy routes out of this conundrum.
## The licensing paradox: From freedom to exploitation
The structural fragility of modern software engineering is intimately bound to the legal frameworks we designed to protect it. Our current licensing models have inadvertently created an extraction economy, forcing a critical re-evaluation of the foundational philosophies separating "permissive" open-source licenses (such as MIT and Apache) from copyleft agreements (like the GPL).
The historical consensus championed permissive licensing as the ultimate catalyst for widespread software adoption. By reducing friction and stripping away compliance barriers, licenses like MIT and Apache allowed code to propagate globally. 
Yet friction-free distribution became a double-edged sword. One participant at the retreat noted that permissive licensing was a profound collective mistake, serving as a legal mechanism that enabled the world’s largest corporations to cannibalize volunteer labor, transforming independent maintainers into unpaid supporters of pillars of multi-billion-dollar enterprise infrastructures.
The alternative is restrictive or dual-licensing models. These introduce an entirely different set of operational failures:
  * **The procurement bottleneck.** Attempting to protect code via non-commercial or "free for hobbyists" clauses often serves as a death sentence for project adoption. One practitioner shared that restricting a project to non-monetized use completely paralyzed its growth. Corporate developers abandoned the tool entirely, not due to a lack of utility, but because the licensing shift triggered complex enterprise procurement reviews and administrative paperwork that engineers simply refused to navigate.
  * **The corporate boycott.** Even when dual-licensing thresholds are calibrated carefully, such as Akka’s transition to a license targeting organizations with over $100 million in revenue, enterprises routinely choose boycott over compliance. In one cited case, an enterprise explicitly chose to abandon a critical dependency it could easily afford, purely to avoid setting a precedent of paying the open-source community.
  * **The enforcement burden.** For some purists, any license restriction introduces an administrative liability. From this perspective, adding commercial restrictions forces the maintainer to become an enforcer, transforming an act of creative expression into a legal chore.
  * **Bypassing by reimplementing software.** Not only is this ethically dubious (although some may disagree), there are also practical issues here: reimplementing requires time and money and may also introduce new security or reliability issues. 


The industry has largely collapsed the distinction between software that’s free to change and software that’s free at the point of consumption, or what’s often described as the difference between ‘free beer’ and ‘free speech’.
The open-source definition originally emerged precisely because traditional free software was not deemed business-friendly enough. By optimizing entirely for business friendliness, we’ve arrived at a landscape where corporate patronage is treated as an optional charity rather than a fundamental structural obligation.
Compounding this crisis is the emotional and psychological toll levied on maintainers who attempt to correct course. When an important project undergoes a defensive licensing shift, the community response is frequently hostile. Maintainers face severe reputational and psychological backlash from the very ecosystems they supported for years. We're then left with an environment where changing the license is viewed as an act of aggression, while exploiting it is just standard business practice.
## Ecosystem collapse and the crisis of maintainer incentives
We're at the point where the ecosystem may collapse. The incentives to maintain projects are disappearing and broader industry pressures on jobs are making it difficult for even the most motivated and enthusiastic software developers to participate in open source. 
The ‘[tragedy of the commons](https://online.hbs.edu/blog/post/tragedy-of-the-commons-impact-on-sustainability-issues)’, which describes the phenomenon of a public resource being depleted because of self-interested actors drawing from it, is a concept often cited in these discussions. At first glance this is a great example of the idea in practice. 
Yet while it’s helpful, applied here the concept doesn’t account for or illustrate the asymmetry at play. First, if open source software _is_ some kind of commons, it isn’t a naturally occurring resource anyone can dip into and take from; it’s something that’s built and maintained by people acting purely in the spirit of community. Second, the process of extraction is happening on an astonishing scale by actors with _immediate_ commercial incentives. 
Whereas earlier eras of open source were by and large sustained by a sense of there being a developer community and a system of mutual benefit, the economics of software today are such that value is being rapidly extracted and then captured with no way of it being released back into the ecosystem that initially brought it into being.
## The spec vs. the code: Where do we go from here?
As a consequence of all these pressures, we’re seeing the emergence of a radical thesis: is the future of open source the specification, rather than the code?
With LLMs capable of generating specialized code on demand, enterprise engineering teams are beginning to question the utility of pulling in massive, multi-thousand-line external dependencies. If using an external library introduces an unmanageable supply chain risk and an endless cycle of patching, it becomes economically logical to use AI to re-implement only the precise functional fragments needed, wrapped in a local 'safety bubble'.
  * The 'traditional' model -> consume external code library -> inherit supply chain risk and maintenance
  * The emerging model -> study open specification/idea -> AI-generated local re-implementation


However, this 're-implementation' thesis has its limits. It’s worth noting, for starters, that many impressive stories of generative AI use here were based on things that had a very clear and detailed test harness or very clear specifications.
And while a simple static site generator can be spun up by an AI in an hour, complex engineering tasks, such as cryptographic libraries or browser-agnostic UI frameworks, require an extraordinary depth of engineering rigor that automated models cannot reliably replicate without collapsing into an utter disaster. 
What’s more, it also denies the originator of the reference library their credit. That might not be a priority for organizations with commercial goals, but if that recognition is the maintainer's motivation, what happens when that disappears?
Completely abandoning shared code libraries in favor of local, fragmented codebases risks creating an elite divide: those with the hardware and financial capital to run sophisticated local AI architectures, and those left with no software at all.
## Questions for software engineers and architects 
To navigate this landscape, engineering teams must move past passive consumption and start asking harder, more deliberate questions:
  * **What’s our dependency footprint?** Are we importing a 20,000-line third-party library to solve a problem that requires only 200 lines of logic? If so, are we prepared to own the security and maintenance lifecycle of that dependency?
  * **How do we define our relationship with maintainers?** If our production systems rely on an open-source tool maintained by a volunteer or a tiny team, what is our mechanism for material return? Are we actively participating via corporate patronage, or are we acting as consumers expecting free enterprise-grade support?
  * **Where do we draw the line between specification and execution?** For upcoming projects, should we look to open source for its architectural patterns and specs, or for its literal binaries?


## Guidance for the months ahead
As we move deeper into this agentic era, engineering organizations should adopt a defensive yet highly intentional posture regarding open source:
  1. **Shift from passive consumption to active ownership.** Treat every open-source dependency not as a free gift, but as code you have effectively hired into your organization. If the maintainer steps away or closes pull requests tomorrow, your team must be capable of auditing, patching, or forking that codebase internally.
  2. **Implement rigid supply chain auditing.** Given the [400% increase in supply chain threats in the first few years of the 2020s](https://www.insurancebusinessmag.com/us/news/cyber/supply-chain-cyber-attacks-surge-over-400-expected-to-continue-rising--cowbell-report-525369.aspx) and the reality of long-term social engineering attacks, rely less on "star counts" or recency. Implement automated sandboxing, verify package origins and establish strict internal registries rather than pulling directly from unvetted public mirrors.
  3. **Formalize an open source contribution and patronage budget.** If your business leverages open software to drive revenue, establish a formal pipeline to fund those projects. This isn't corporate charity; it is basic risk mitigation to prevent the burnout of the individuals keeping your underlying infrastructure alive.


Open source isn’t going to vanish, but the era of the unvetted, un-patronized, completely permissive free lunch is coming to an end. 
**The teams that survive and thrive in the coming years will be those that treat open source with the[respect, critique and material support](https://earthbound.report/2018/01/15/elinor-ostroms-8-rules-for-managing-the-commons/) that a true structural bedrock demands.**
  * [ Technology strategy Caught between ephemerality and materiality  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/technology-strategy/caught-between-ephemerality-materiality-reflections-fose-europe)
  * [ Generative AI Cognitive debt is a real organizational risk: Don’t ignore it  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/cognitive-debt-real-organizational-risk)
  * [ Generative AI Your agent skill is not an anti-corruption layer  Learn more ](https://www.thoughtworks.com/en-gb/insights/blog/generative-ai/your-agent-skill-not-anti-corruption-layer)


[ View more ](javascript:void\(0\))
[ View less ](javascript:void\(0\))
## Explore a snapshot of today's tech landscape
[ Read Technology Radar ](https://www.thoughtworks.com/en-gb/radar)
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