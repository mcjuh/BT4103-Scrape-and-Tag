<!-- Source: https://research.thoughtworks.com/library/multifeature-graph-convolutional-network-ocr | Title: MultiFeature graph convolutional network for OCR verification | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# MultiFeature graph convolutional network for OCR verification 
By 
Shikhar Dubey , 
Krish Mittal , 
Sourava Kumar Behera , 
Nitin Kumar , 
Saurabh Shigwan and
Rohit Saluja
Published: December 10, 2025 
his paper presents a novel Graph Convolutional Network (GCN) based framework for verifying OCR predictions on real Hindi document images, specifically addressing the challenges of complex conjuncts and character segmentation. Our approach first segments Hindi characters in real book images at different levels of granularity, while also synthetically generating word images from OCR predictions. Both real and synthetic images are processed through ResNet-50 to extract feature representations, which are then segmented using multiple patching strategies (uniform, akshara, random, and letter patches). The bounding boxes created using segmentation masks are scaled proportionally to the feature space while extracting features for GCN. We construct a line graph where each node represents a real-synthetic character pair (in feature space). Each node of the line graph captures semantic and geometric features including i) cross-entropy between original and synthetic features, ii) Hu moments difference for shape properties, and iii) and pixel count difference for size variation. The GCN with three convolutional layers (and ELU activation) processes these graph-structured features to verify the correctness of OCR predictions. Experimental evaluation on 1000 images from diverse Hindi books demonstrates the effectiveness of our graph-based verification approach in detecting OCR errors, particularly for challenging conjunct characters where traditional methods struggle.
**Read the complete research paper here:**[AACL](https://aclanthology.org/2025.bhasha-1.1/)