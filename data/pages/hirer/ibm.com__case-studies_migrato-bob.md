<!-- Source: https://www.ibm.com/case-studies/migrato-bob | Title: Breaking a Java 8 deadlock to open up the way forward | Seed: https://www.ibm.com/consulting (IBM Consulting) -->

Support
  * [OverviewResolve product issues with self-service tools](https://www.ibm.com/mysupport/s/?language=en_US&lnk=flathl)
  * [CommunityShare knowledge in a collaborative environment to unlock innovation](https://community.ibm.com/community/user/community?lnk=flathl)
  * [DeveloperAccess digital resources, code samples and code trials](https://developer.ibm.com/?lnk=flathl)
  * [DocumentationUnderstand, develop and deploy our products with comprehensive technical resources](https://www.ibm.com/docs/en?lnk=flathl)
  * [IBM Cloud platformAccess subject matter experts and content to address questions and issues about IBM Cloud](https://www.ibm.com/products/cloud/support?lnk=flathl)
  * [ImplementationDrive better business outcomes with an experienced team of IBM product experts](https://www.ibm.com/products/expertlabs?lnk=flatitem)
  * [TrainingDevelop your skills with premiere educational offerings and credentials](https://www.ibm.com/training/?lnk=flathl)
  * [Technology Lifecycle ServicesElevate your support experience with a holistic approach to data center management across your IT environment](https://www.ibm.com/services/technology-lifecycle-services?lnk=flathl)


My IBM  Log in 
#  Breaking a Java 8 deadlock to open up the way forward 
When a legacy installer blocked modernization, Migrato used IBM Bob to carve a cleaner path to future Java upgrades.
When the upgrade path became the problem 
##  When the upgrade path became the problem 
For many organizations, modernization challenges emerge in unexpected places. For Migrato, a Netherlands-based software company that helps organizations analyze, inventory, cleanse and migrate unstructured content, the obstacle was not a major application or business process. It was a software installer.
Migrato’s MICC (Migrato Intelligent Content Classifier) software suite relied on a decade-old installer written in Java 8. The installer performed a narrow but critical role, installing and updating applications across the MICC suite. But because it depended on Java 8, Migrato could not use it to replace the Java runtime cleanly. The mechanism designed to deliver upgrades had become the first blocker in Migrato’s broader effort to modernize its Java-based platform.
The MICC Manager and installer worked together to manage licensing, server connections, application access and software updates. Updating customer environments manually would add operational work and make upgrades harder to coordinate. With a six-person development team whose expertise was concentrated in Java and Python, Migrato wanted to remove the runtime dependency while preserving the installer’s existing behavior and customer experience. It was looking for a practical way to create a path for future modernization without disrupting the experience customers already knew.
[ Dive into the architecture and technical details  Read the blog ](https://www.ibm.com/new/product-blog/how-migrato-used-ibm-bob-to-turn-a-java-8-roadblock-into-a-three-day-c-plus-plus-migration)
0 days 
to complete a Java 8-to-C++ installer migration that was expected to take several weeks
< 0
to plan the conversion and generate the initial C++ implementation with IBM Bob
Java Virtual Machine 
required for the installer to operate, creating an independent deployment path for future Java upgrades
IBM Bob helped us accelerate a complex migration while keeping validation and engineering oversight at the center of the process. By creating an independent deployment path, we removed a key modernization barrier and established a practical foundation for future upgrades. 
Oscar Dubbeldam  Migrato 
Creating an independent upgrade path 
##  Creating an independent upgrade path 
Rather than treating the installer as a reason to rewrite the entire MICC suite, Migrato focused on removing the first obstacle standing in the way of future Java upgrades. By rebuilding the installer in C++, the company created a native application that no longer required a Java virtual machine to start, while allowing the rest of the MICC codebase to remain in Java. This approach preserved the existing user experience while establishing a practical foundation for broader platform modernization; customers could continue managing updates through the familiar MICC Manager experience while Migrato modernized the underlying installer.
Working with [IBM® Bob](https://bob.ibm.com/), the team followed a plan-implement-validate approach. The existing installer served as the reference point for the migration, helping developers preserve established behaviors while rebuilding the application in C++. IBM Bob analyzed the Java code, proposed a C++ project structure, mapped dependencies and generated the new implementation after developers reviewed and approved the design approach.
The team then validated the new installer against the behavior of the original application. Developers reviewed the generated implementation, examined security-sensitive functionality and reused existing tests to verify compatibility. When testing uncovered a timing issue between the installer and the MICC Manager, the team used IBM Bob to help trace the problem, adjust the implementation and confirm that interface tests continued to pass. Throughout the effort, developers retained responsibility for architecture decisions, dependency selection and validation.
Making future upgrades easier to deliver 
##  Making future upgrades easier to deliver 
Migrato transformed an effort expected to take several weeks into a three-day project. Using IBM Bob, one developer completed planning and code generation in less than a day, while review, testing and integration validation brought the total migration effort to three days. The approach enabled Migrato’s six-person development team to complete an unfamiliar C++ migration while maintaining ownership of architecture, security review and final validation.
The result was a functional installer that preserved the behavior of the original Java application while operating independently of the Java runtime. Because the installer no longer depends on the environment it is designed to update, it can deploy Java-based components and packaged runtime updates without first requiring a separate runtime upgrade. Customers can continue managing updates through the familiar MICC Manager experience while the installer handles the underlying deployment work.
What began as a challenge with a legacy installer became an opportunity to accelerate future modernization. With the deployment bottleneck removed, Migrato now has a practical path to advance its Java modernization strategy while maintaining the experience its customers already know.
About Migrato 
##  About Migrato 
Founded in 2014 and headquartered in Strijen, the Netherlands, [Migrato](https://migrato.site/) helps organizations analyze, inventory, cleanse and migrate unstructured content, including documents, PDFs, scanned records, emails and chat messages. Using custom-built solutions, the company transforms unstructured information into actionable insights that add value to employees and business processes.
Solution component  IBM® Bob® 
Build a practical upgrade path with IBM Bob
Discover how IBM can help your organization remove modernization barriers and create a practical path to future upgrades. 
  1. [ Learn more ](https://www.ibm.com/products/ai-coding-agent)
  2. [ Start your 30-day free trial  ](https://bob.ibm.com/trial)


#####  Legal 
© Copyright IBM Corporation. August, 2026. IBM, the IBM logo, and IBM® Bob are trademarks of IBM Corp., registered in many jurisdictions worldwide. Examples presented as illustrative only. Actual results will vary based on client configurations and conditions and, therefore, generally expected results cannot be provided. 
Products Consulting services Industries Case studies Financing Research LinkedIn X Instagram YouTube Podcasts Business partners Documentation Events Newsletters Support TechXchange community Overview Careers Investor relations Leadership Newsroom Security, privacy and trust United States — English Contact IBM Privacy Terms of use Accessibility