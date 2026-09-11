<!-- Source: https://research.thoughtworks.com/library/distribution-aware-feature-selection-for-saes | Title: Distribution-aware feature selection for SAEs | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Insights
# Distribution-aware feature selection for SAEs
By 
Narmeen Oozeer , 
Nirmalendu Prakash , 
Michael Lan and
Alice Rigg 
Published: August 29, 2025 
TopK Sparse Autoencoders (SAEs) break down neural activations into understandable features, but they're inefficient because they reconstruct each token using a fixed number of the most active features. A more advanced version, BatchTopK, improves this by selecting the most active features across an entire batch of tokens. However, this can lead to an "activation lottery," where a few very high-magnitude features dominate the selection process, potentially at the expense of other more informative features that have a lower magnitude.
We have developed a new approach called Sampled-SAE. This technique works by first scoring all the potential features in a batch of data. It then creates a smaller, curated "candidate pool" of the best features, which it selects from. The size of this pool is controlled by a new parameter, l. By adjusting l, researchers can find a balance between using globally important features and using more specific, rare ones. For example, a small l forces the model to use only the most globally consistent features, while a large l allows for a wider variety of fine-grained features. This makes BatchTopK a more flexible, tunable approach that can be adjusted based on the specific trade-offs needed for a given task, such as prioritizing a model's performance over its interpretability.
**Research submission[here](https://arxiv.org/abs/2508.21324).**
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