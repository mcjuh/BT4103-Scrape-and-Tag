<!-- Source: https://research.thoughtworks.com/library/beyond-linear-steering-unified-multi-attribute-control-for-language-models | Title: Beyond linear steering: Unified multi-attribute control for language models | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Beyond linear steering: Unified multi-attribute control for language models
By 
Narmeen Oozeer , 
Luke Marks and
Fazl Barez
Published: May 30, 2025  | Last updated: April 04, 2026
Controlling multiple behaviors in large language models (LLMs) is a challenging problem because different attributes can interfere with each other. Current linear steering methods are limited as they assume that behaviors can be simply added together in the model's activation space, which is often not the case. Additionally, these methods are inefficient, requiring a separate, dedicated tuning for each individual attribute, making them difficult to manage and scale for complex, multi-faceted control.
To solve this, a new approach called K-Steering has been developed. It uses a single, non-linear classifier trained on the model's internal states to dynamically compute new intervention directions via gradients. This approach is more flexible and powerful because it avoids the restrictive assumption of linearity and removes the need for storing and tuning separate attribute vectors. K-Steering allows for the dynamic and flexible composition of multiple behaviors without any additional training, providing a unified and efficient solution for controlling LLM outputs
**Research submission[here](https://arxiv.org/abs/2505.24535).**
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
Thoughtworks.com stores and retrieves information on your browser in the form of cookies. This information might be about you, your preferences or your device and is used to make the site function properly. We also use cookies to give you a more personalized web experience. For additional detail on our cookie categories, you can review them here and reference our privacy policy. [More information](https://research.thoughtworks.com/about-us/privacy-policy)
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