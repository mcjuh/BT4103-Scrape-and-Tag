<!-- Source: https://www.thoughtworks.com/insights/articles/infrastructure-as-product | Title: Infrastructure as Product | Thoughtworks | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

#  Infrastructure as Product: Accelerating time to market through platform engineering 
[ Articles Back ](https://www.thoughtworks.com/insights/articles)
Close


By 
Published: January 26, 2021 
Not too long ago, cloud infrastructure was being widely praised for its incredible simplicity and manageability. For companies and teams burdened by complex on-premises infrastructure, it presented an intuitive, scalable, and cost-effective alternative that promised to transform how we approach IT infrastructure as a whole.
But, as offerings from the major public cloud providers have grown and become more sophisticated, that simplicity has fallen by the wayside. Today, cloud infrastructure service portfolios are incredibly large, increasingly complex, and harder than ever for engineering teams to keep pace with. 
Today, Amazon Web Services alone offers 175 different cloud infrastructure services across its portfolio. We’re no longer dealing with a short, simple selection of intuitive services that can quickly be provisioned with just a few clicks.
Instead of relieving pressure from businesses and simplifying their infrastructure approach, cloud is now pushing in the opposite direction — creating new management challenges, demanding new (virtual) data center skills, and increasing average time to market.
###### **Why rising cloud complexity is a business problem**
When cloud-based infrastructure first emerged, businesses and their IT teams were eager to embrace it and gain the flexibility, scalability, and management simplicity benefits it offered.
It enabled developers and infrastructure teams to provision new services in minutes — dramatically improving time to market, and enabling organizations to gain an all-important competitive edge in crowded markets.
But, as the complexity of cloud infrastructure offerings has increased, those benefits have shrunk for many organizations. More complex services and decisions mean the teams managing cloud infrastructure need greater skills, and developers need deep expertise just to be able to self-serve — pushing the definition of ‘full-stack’ to the point that it becomes disadvantageous.
Put simply, rising cloud complexity is putting many organizations and their infrastructure teams right back to where they were 15 years ago — struggling to keep up with demand for new services and instances, and stay on top of an increasingly unmanageable infrastructure footprint.
###### **The solution? Start viewing and managing infrastructure as a set of internal platform products**
Major [cloud service](https://www.thoughtworks.com/what-we-do/cloud) providers may have moved away from providing simple and intuitive infrastructure options that anyone can provision themselves. But, that doesn’t mean that you can’t create internal platforms and processes to do it yourself.
That’s the essence of a [Platform Engineering](https://www.thoughtworks.com/what-we-do/platforms/developer-platform-engineering) approach. Rather than having your cloud infrastructure team spend all of their time constantly configuring and deploying new instances, environments, and services as developers need them, instead you have the team create a platform that offers self-service components that developers can easily choose and deploy themselves.
It’s an approach that’s started to see widespread adoption in 2020, featuring significantly in [Puppet’s State of DevOps](https://puppet.com/resources/report/2020-state-of-devops-report/) report. According to the report, 63 percent of organizations have at least one internal self service platform in place. 
With re-usable, self-service solutions available on a platform that’s easy to understand and engage with, cloud infrastructure teams can spend less time configuring individual solutions, and give the business a rapid path to market for new digital services and capabilities.
The diagram above shows how speed to value and speed to market both exponentially increase through this approach. As the platform offering matures by creating more reusable elements, these can be easily combined to create new product experiences for the product teams, and by extension the business.
As each re-usable product or component is created, the build-measure-learn cycle gets smaller and quicker, delivering value for everyone faster. However, careful management of the platform is required as it evolves, to ensure that it remains composable and cohesive. Or in other words it doesn't become complex to engage with, or restrictive in the product choice it offers.
###### **Why the approach works**
This platform-based approach to cloud infrastructure management works because it considers everyone’s needs, and gives every group the time and capabilities they need to focus on the things they do best:
﻿
  * **Development teams and other internal customers** don’t need to become masters of new languages or develop specialist cloud infrastructure skills to help themselves to the services they need.
  * **The platform team** has visibility of all cloud infrastructure requests, and can broaden its expertise as cloud offerings and the infrastructure landscape advances, ensuring that products are both relevant and highly valuable to the organization as a whole


However, it’s important to note that it can only deliver these results when planned, implemented, and managed correctly.
###### **What can go wrong?**
Thoughtworks recently worked with a fintech enterprise that had attempted to implement a platform-based infrastructure approach, but faced many challenges that limited its effectiveness.
The company had built a team called Platform Engineering, seeded with some new cloud engineer hires, and a few of the existing data center team who had demonstrated an ability to code and an appetite to stretch out of their comfort zone.
The team worked for 18 months to build a platform that enabled developers to provision their own cloud components by submitting [infrastructure-as-code](https://www.thoughtworks.com/books/infrastructure-as-code-2nd-edition) via pull requests to the Platform Engineering team. The platform team would then coordinate and deploy the applications to a load balanced set of VMs, via a continuous delivery (CD) pipeline. 
But, after a year and a half of coding, only 2% of the company’s production workloads were flowing through the new platform. Why?
The diagram above shows the cross-backlog dependencies that this approach created. It wasn’t a true self-service approach, because in many cases, other teams and individuals had to contribute to and edit a request before it was given the go-ahead. Ownership of the final product was unclear.
As new dev teams submitted more code, that inefficiency began to scale (shown in the bottom half of the diagram). There were more requests to review, but still only one platform team to review it all, creating a major bottleneck that slowed deployment speed further.
The end result was a platform that struggled to deliver the business value it initially promised. Backlogs and bottlenecks slowed time to market, new languages and processes made the internal platform hard to engage with, and ultimately, it didn’t meet developers' needs.
###### **Keys to success**
To ensure the success of this approach in your organization, there are three key factors you must consider as you create and execute your cloud infrastructure platform strategy:
###### **#1) Understand your customers (and their experience expectations)**
**﻿**
This approach treats infrastructure as a suite of internal products, and views development — among others — as the customers. Like any other product, one of the biggest keys to success is properly understanding and responding to the needs of those customers.
Just as product and marketing teams maintain a laser focus on delivering seamless, intuitive customer experiences, cloud infrastructure teams must do the same for internal customers. They must put developers at the heart of every decision to ensure high uptake and long-term success.
If, for example, engaging with a platform requires a developer to learn a new language just to continue doing the same work they’re already doing, that doesn’t represent a good developer experience. And, just like a customer who is being asked to jump through too many hoops to buy a product on an ecommerce platform, they’ll simply walk away and revert to however they were doing their job previously.
###### **#2) Assign a product owner**
One of the biggest issues with true cloud infrastructure self-service is that no customer team or leader is incentivized to configure solutions that can be reused across the organization. Each team simply creates what it needs at that moment. That’s fine for them, but it leads to a lot of duplicated effort across the organization.
By appointing a product owner, you can overcome that challenge and configure cloud infrastructure products with your entire organization in mind. This team-agnostic leader will ensure that everything created delivers as much value as possible for everyone.
There’s enough work involved to warrant a person full-time in the role, so don’t give in to the temptation to share the responsibilities across a team. Dedicating a person to the role creates a stronger sense of accountability than simply assigning additional tasks to existing team members. 
It will help draw attention, and at the same time send a message of intent to change, commitment to improve, and ultimately, your intention to start viewing and treating infrastructure as a product.
###### **#3) Reconsider how you measure infrastructure success**
One of the biggest barriers to this product-based infrastructure approach is an outdated view of what a successful infrastructure team looks like. In the past, teams have naturally strived to drive down costs and keep systems as stable as possible, rather than aiming for change or enablement across the enterprise.
This Platform Engineering approach, on the other hand, is all about supporting and enabling developers to turn their applications into market and business-ready services quickly and easily.
You’re not going to see short-term cost reductions. But, what you should see are long-term improvements in metrics like time to market, developer throughput, and consistency in provisioning and deployment, leading to reduced [Mean Time to Restore (MTTR)](https://www.thoughtworks.com/radar/techniques/four-key-metrics). Those are the measures by which you’ll need to define success, and it’s critical that this is understood by stakeholders and decision-makers at every level of the enterprise.
###### **In summary**
Cloud infrastructure management has become an extremely complex task. If you want to continue empowering developers and IT teams with the fast, self-service access to infrastructure services that the cloud used to deliver, you’ll need to take matters into your own hands.
By adopting a Platform Engineering approach and building infrastructure ‘products’, you can restore the simplicity offered by early-generation infrastructure-as-a-service (IaaS) offerings, while still making the most of the advanced capabilities and choices available today.
﻿
This approach demands dedicated ownership and accountability. It requires a deep understanding of the internal customers these products will serve. And it must be based on a new definition of data center success that’s better aligned with the value a modern infrastructure approach can deliver.
But, if you can tackle all of that, what awaits is a faster, leaner, more consistent approach to infrastructure management. An approach that empowers everyone involved in the software delivery process, helps developers launch new services and solutions faster, and can significantly improve both time to market and time to value.
As a final note, it’s important to recognize in all of this that cloud infrastructure provides the foundation for your entire business. Cutting corners, accepting fragility, and not giving this process the strategic attention it deserves will all add risk and escalate costs later down the line.
## How can you achieve faster growth?
[ Get in touch ](https://www.thoughtworks.com/contact-us)
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