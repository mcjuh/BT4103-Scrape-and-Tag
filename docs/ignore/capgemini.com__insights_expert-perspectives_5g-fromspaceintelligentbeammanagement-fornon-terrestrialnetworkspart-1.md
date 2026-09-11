<!-- Source: https://www.capgemini.com/insights/expert-perspectives/5g-fromspaceintelligentbeammanagement-fornon-terrestrialnetworkspart-1/ | Title: 5G from Space: Intelligent Beam Management for Non-Terrestrial Networks (Part-1) - Capgemini | Seed: https://www.capgemini.com/service/capgemini-invent/ (Capgemini Invent) -->

[Skip to content](https://www.capgemini.com/insights/expert-perspectives/5g-from-space-intelligent-beam-management-for-non-terrestrial-networks-part-1/#main-content)
The convergence of terrestrial and non-terrestrial networks is no longer optional; it is a strategic imperative on the path to truly ubiquitous connectivity. But the more we rely on satellites, the more demands we place on them. Beam management is one area slated for change, with many satellite companies actively planning upgrades. This paper outlines a new approach to beam-hopping that will enable satellites to serve multiple areas fairly and efficiently. 
When [3GPP Release-17](https://www.3gpp.org/specifications-technologies/releases/release-17) defined the specifications for satellite-based connectivity as part of 3GPP specifications, it enabled the path to integrated architecture for NB-IOT/5G NR and Non-Terrestrial Networks (NTN). Capgemini took up the challenge and started to explore the evolution of satellite networks based on 3GPP specifications. Our innovation accelerates the business case by unlocking new use cases in IoT, mobility, logistics, and rural broadband – where connectivity gaps traditionally hinder adoption. For satellite companies that need ever greater efficiency from their fleets, it could be a significant step forward. 
### **The industry challenge: Capacity from space**
Non‑Terrestrial Networks include satellite constellations in Geostationary Earth Orbit (GEO), Medium Earth Orbit (MEO) and Low Earth Orbit (LEO). LEO satellites offer advantages such as reduced latency, better link-budget and path-loss compared to GEO and MEO satellites, and are thus increasingly seen as the key to extending 5G beyond traditional coverage boundaries. [Multiple LEO constellations are currently being planned](https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/non-terrestrial-networks-opportunities-and-challenges/), with use cases such as: 
  * Maritime and aviation connectivity 


  * Rural and underserved areas 


  * Public safety and disaster management 


  * Remote industrial sites (energy, mining, logistics) 


As the industry moves toward truly ubiquitous connectivity, LEO satellite systems are becoming a core pillar of 5G evolution, and are even laying a foundation for 6G. However, delivering coverage from space also introduces unique challenges. 
### **The need for beam management**
How do you get maximum coverage from each satellite? First, satellites today deploy multiple beams – you can picture a honeycomb pattern on the ground, with each cell corresponding to one beam. But modern 5G satellites take this one step further. In order to optimize satellite payload weight and limit the amount of energy consumption, the number of beams deployed on a satellite are typically much smaller than number of cells covered by it, meaning that one beam is responsible for multiple cells. 
This strategy requires an elaborate scheduling framework that dynamically maps cells to beams, such that a particular beam illuminates multiple cell clusters on a time-sharing basis. Furthermore, the traffic load across cells may fluctuate, and beam allocation must adapt to these dynamic changes. 
Figure 1: Overview of Beam-hopping in NTN 
Satellite payloads must remain lightweight and power-efficient, even as they serve thousands of dynamically changing ground cells. This makes intelligent beam management essential: satellite beams must be allocated, adapted, and optimized in real time to match varying traffic patterns and ensure seamless service continuity. 
### **Capgemini’s experience in beam management**
At Capgemini, we have been working to make this a reality within the 3GPP 5G standards and the O‑RAN ecosystem. Our recent IEEE paper, “ _Beam Management for 5G FR1 LEO-based Non-Terrestrial Networks”_ at the IEEE Future Networks World Forum (FNWF) 2025, addresses one of the most critical challenges in satellite‑based 5G: **how to intelligently manage satellite beams to deliver capacity where and when it is needed.**
Our paper presents a novel beam-hopping and resource allocation framework designed specifically for 5G NTN. Using an O-RAN-based architecture and an intelligent Beam Allocation Module (BAM), the approach dynamically assigns satellite beams to ground cells while complying with 3GPP standards. Simulation results demonstrate how this technique significantly improves capacity utilization and enables more efficient use of spectrum and satellite resources. 
In practice, operators face three intertwined challenges, as shown in Table 1:   
|  **Challenge**  |  **Description**  |  
| --- | --- |  
|  **Limited satellite payload and beam resources**  | A single LEO satellite must cover a very large footprint on the ground. To keep SWaP (Size, Weight and Power) under control: – The number of satellite beams and Payload Total Power (dBW) is fixed – The number of ground cells that need to be served is much higher than the number of beams This means a beam must be shared in time across multiple cells – a concept known as  _beam hopping._  |  
|  **5G NR scheduling and timing constraints**  | Beam hopping needs comply to 5G NR standards such as: – Transmission of mandatory signals such as Synchronization Signal Blocks (SSB), System Information Blocks (SIBs) and Random Access (PRACH) – Transmission of Control channel (PDCCH), Data channel (PDSCH) and HARQ acknowledgements Each cell must be illuminated by a satellite beam at those specific time instants. If different cells sharing the same beam need mandatory signalling at the same time, the system risks: – Coverage holes (user can’t find or access the cell) – Protocol violations (non‑compliant behaviour vs 3GPP spec) – Unpredictable performance   |  
|  **Highly dynamic and uneven traffic**  | NTN networks cover vast geographical areas and are characterized by: – Uneven traffic demand: some cells could be highly loaded while others may not have any traffic – Dynamic traffic variations: high demand for a particular period followed by long periods of inactivityStatic or semi-static beam allocation strategies fail to adapt to demand and waste precious satellite resources, leading to: – Underutilized satellite spectrum and payload – Poor user experience during peak demand – Difficulty in meeting SLAs for enterprise customers   |  
Table1: Challenges in NTN networks
In summary, there is a need to dynamically share satellite beams across many cells, comply all 5G scheduling and timing constraints and maximize capacity based on traffic demand. 
#### In [part 2](https://www.capgemini.com/insights/expert-perspectives/5g-from-spaceintelligent-beam-management-fornon-terrestrialnetworkspart-2/) of this blog, we’ll demonstrate how we did just that. 
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