<!-- Source: https://www.capgemini.com/insights/expert-perspectives/5g-from-space-intelligent-beam-management-for-non-terrestrial-networks-part-2/ | Title: 5G from Space: Intelligent Beam Management for Non-Terrestrial Networks (Part-2)  - Capgemini | Seed: https://www.capgemini.com/service/capgemini-invent/ (Capgemini Invent) -->

[Skip to content](https://www.capgemini.com/insights/expert-perspectives/5g-from-space-intelligent-beam-management-for-non-terrestrial-networks-part-2/#main-content)
In [Part-1](https://www.capgemini.com/insights/expert-perspectives/5g-fromspaceintelligentbeammanagement-fornon-terrestrialnetworkspart-1/) of the blog titled “5G from Space: Intelligent beam management for Non-Terrestrial Networks,” we introduced the need for beam management in LEO constellations. In this half, we’ll explore an intriguing solution to intelligent beam management. 
### **Intelligent, O‑RAN‑native beam management**
To recap: in modern satellite deployments, one beam often illuminates multiple regions (cells) on the ground. Beam management controls which cells are illuminated, and when. The specific time-instance is determined by the Beam Allocation Management algorithm. 
In this scenario, radio resources on the satellite beam must be time-partitioned among cells to meet the following requirements: 
  1. The beam hopping pattern must align with time-domain allocation of mandatory signalling across cells – i.e., a cell must always be illuminated at time instances where mandatory cell-defining signals (like Synchronization Signal Block, system information and random-access preamble) are to be transmitted or received 


  1. The beam hopping pattern must be able to serve the traffic needs across cells 


  1. The beam hopping pattern should be able to adapt to variations in traffic requirements, i.e. to be able to provide the coverage to cells that addresses the dynamic traffic requirements.


**In summary, beam hopping is a capacity maximization problem within given constraints of cell configuration and traffic partitioning.**
Capgemini Engineering’s research proposes a  _multi‑tier_ ,  _intelligent beam management_ and  _resource allocation framework,_ specifically designed for 5G FR1 LEO NTN networks and fully aligned with 3GPP and O‑RAN principles as shown in Figure 1. Key benefits of the architecture are as follows: 
Multi-level resource allocation 
  * Step-1: A beam allocator module performs beam‑to‑cell allocation and decides which ground cell a satellite beam should illuminate at each time slot. This ensures that all cells receive the mandatory downlink and uplink signalling opportunities required by 5G NR standards. 


  * Step-2: O-DU performs the UE-level frequency domain scheduling within a cell. NTN resource allocation logic within O-DU takes the Beam Allocation Matrix (BAM) as an input, and schedules individual users according to QoS and SLA requirements. 


Figure 1: Capgemini’s intelligent beam management framework for 5G NTN FR1 LEO 
####  **Leveraging O‑RAN RIC and xApps**
Beam management functionality can be onboarded as a xApp on Near-RT RIC inline with O-RAN architecture principles. SatRRM‑xApp (Satellite Radio Resource Management xApp): 
  * Computes a Beam Allocation Matrix describing, for each beam and each time slot, which cell is illuminated and for what purpose (signalling or data) 


  * Ensures compliance with 3GPP constraints on signalling and data channels 


  * Maximizes allocation of remaining time slots to data, based on each cell’s traffic demand 


  * Continuously adapts BAM as traffic changes, based on KPIs from RAN nodes 


Alternatively, depending on the type of deployment (Regenerative, Semi-regenerative or Transparent mode) and the acceptable latency for updating the Beam Allocation Matrix, the Beam Allocation Module can be flexibly placed either on the ground or on the payload. 
####  **Beam allocation algorithm**
A highlight of this architecture are the beam allocation algorithms which includes the following steps: 
  * Signalling allocation logic determines when each cell must transmit/receive mandatory signalling channels and reserves the time slots in BAM ensuring that there are no conflicts between cells sharing the same beam. 


  * Data allocation logic allocates remaining timeslots for data channels in proportion to the cell’s traffic demand. Allocations are adjusted to avoid overlap with the signalling and data of other cells to maintain conflict‑free operation. 


This architecture enables the satellite‑specific constraints (beam hopping, coverage, payload limits) to be managed by beam allocator module while user‑level scheduling is managed within O‑DU. The result is a  _demand‑aware_ ,  _conflict‑free beam-hopping pattern_ that adapts to the dynamic needs of NTN networks. 
#### **Benefits of Capgemini’s intelligent beam management architecture**
From an operator, vendor, or enterprise ecosystem perspective, this architecture delivers tangible benefits. Instead of illuminating idle cells, satellite resources are focused on carrying actual data, which improves overall capacity by avoiding signaling conflicts and rigid, static beamhopping patterns. As a result, the network can naturally support asymmetric and realworld traffic profiles without the need for manual reconfiguration, making it both more flexible and operationally efficient.
####  **Fully compliant O-RAN ready architecture**
Our approach is explicitly designed to comply with 3GPP NTN specifications and native integration with O-RAN architecture. This enables: 
  * Integration with multi‑vendor RAN deployments 


  * Deployment as a software feature on their existing O‑RAN infrastructure rather than requiring tightly‑coupled satellite‑RAN implementations 


  * Support for the long‑term vision of converged terrestrial and non‑terrestrial 5G/6G networks 


### **Flexibility for operators and service providers**
The intelligent beam management approach leverages the flexibility of the ORAN framework to allow operators and satellite service providers to customize policies – such as SLA weighting, latency preferences, and traffic prioritization – and deploy different beam allocation strategies without requiring changes to baseband software. By building on an open, standardsbased platform, it also enables ecosystem partners to innovate and add value on top of the solution. For operators, this results in a softwaredefined, policydriven satellite RAN and the ability to continuously evolve beam management strategies as usage patterns and business models change. 
###  **Capgemini’s differentiator**
Beam management for satellite networks is an active research area and most existing studies focus on multi-beam resource allocation using frequency reuse and power control. Most existing studies do not address time‑multiplexed beam hopping combined with strict 5G signalling timing, and rarely consider realization in a standardized O‑RAN environment. 
Capgemini’s research paper bridges this gap by advancing a standards‑aligned NTN beam management that explicitly focuses on beam hopping in LEO NTN networks, with detailed consideration of 3GPP‑defined scheduling and timing constraints. 
Additionally, multi‑tier resource allocation architecture provides clear separation between satellite beam‑to‑cell allocation and UE‑level scheduling. The result is a realistic simulation of capacity and coverage usage under 5G NTN configurations. 
### **Summary**
Our research is a step towards making satellite‑based 5G deployments efficient and reliable. For operators and ecosystem players looking to integrate LEO satellites into their 5G networks today, the key takeaway is this: beam management is a critical part of NTN networks and ideally implemented as a programmable function in RAN with options to deploy it flexibly. 
Capgemini is actively working with clients and partners to bring these concepts from research into pilots and real‑world deployments. If you are exploring NTN, LEO constellations or O‑RAN‑based satellite integration, we would be pleased to discuss how this architecture and our reference implementations can support your roadmap.
#### To understand **why beam hopping is essential in 5G NTN and the engineering constraints that shape its design** , we recommend starting with **[P](http://insights/expert-perspectives/5g-fromspaceintelligentbeammanagement-fornon-terrestrialnetworkspart-1)[art‑1](https://www.capgemini.com/insights/expert-perspectives/5g-fromspaceintelligentbeammanagement-fornon-terrestrialnetworkspart-1/)of this blog series**
## Authors
### RaviKanth Pasumarthy
Vice-President, Capgemini Engineering
RaviKanth is working as Chief Architect at Capgemini Engineering with experience in developing Wireless and Satellite based systems. His area of expertise involves Solution Engineering, System Architecture and realization for 5G/5G-Advanced systems and RIC/Apps based on O-RAN architecture, application of AI/ML concepts to RAN and System design and solutioning of NTN systems. Ravi is IEEE Senior Member and is also active speaker at various workshops/conferences.
### Sachin Gupta
Senior Director, Capgemini Engineering
Sachin Gupta is a seasoned Wireless Architect with over two decades of experience architecting high-performance cellular wireless solutions across networks and devices. At Capgemini, he focuses on end-to-end architectures spanning multiple generations of wireless standards. He is also a Machine Learning practitioner with expertise in Federated Machine Learning.
### Dhanmeet Singh
Principal Systems Engineer, Capgemini Engineering
Dhanmeet Singh is a seasoned Wireless System Engineer with 20 years of experience developing high-performance Layer 1 (PHY) solutions across GSM, LTE/4G, and 5G NR technologies. At Capgemini, he specializes in physical-layer procedures, HW and SW partitioning and L1 system architecture for cellular wireless systems
Slider. Slide 1.
Capgemini cares about your privacy and enables you to choose the types of cookies we can use when you visit our website. You may use the “Manage Cookie Settings” functionality in the banner and/or footer of the website to change our default settings. We use cookies to enhance your experience on our website. They also assist us in improving the website's performance, delivering relevant content to you, and enabling you to share content on social networks. Choosing not to allow the use of certain cookies may consequently affect your browsing experience and limit the availability of some services.Your choices will be recorded by Capgemini and TrustArc for a duration of 3 months, after which you will be required to provide your preferences again.If you wish to know the detailed list of cookies under each category used on the website, you may find it in the [Cookie Policy](https://www.capgemini.com/cookie-policy). 
Accept Manage Settings Decline All