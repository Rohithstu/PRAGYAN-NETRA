# PRAGYAN-NETRA
An AI-based cognitive memory management and obstacle detection system for visually impaired individuals.
# Pragyan-Netra OS
**An Edge-AI Cognitive Assistant for Enhanced Spatial Awareness**

Pragyan-Netra is a real-time assistive technology framework designed to provide high-fidelity environmental awareness for the visually impaired. By integrating computer vision, spatialized audio, and offline speech recognition, the system converts complex visual scenes into an intuitive auditory landscape.

## (Core Architecture)

### 1. Computer Vision Pipeline

* **Object Detection:** Leveraging **YOLOv10** for low-latency detection of environmental obstacles and structural hazards.

* **Biometric Recognition:** Localized face-recognition engine for social identity persistence.

* **Depth Heuristics:** Geometric analysis of the ground plane to identify structural barriers (walls) through edge density monitoring.



### 2. Auditory Interface

* **Spatialized Feedback:** Audio cues are mapped to the azimuth and distance of detected objects, reducing cognitive load through natural sound localization.

* **Proactive Alerting:** Differentiated audio frequencies distinguish between social entities (speech) and structural hazards (haptic-tone beeps).



### 3. Voice Interaction Engine

* **Neural Speech-to-Text:** Powered by **Vosk** for fully offline, privacy-compliant command processing.

* **Wake-Word Activation:** Asynchronous listening architecture that activates system feedback upon the "Netra" trigger.



## Technical Specifications

* **Inference Engine:** Ultralytics YOLOv10

* **Audio Processing:** PyAudio / Pyttsx3 / Binaural Simulation

* **Language Model:** Vosk-Kaldi (Offline)

* **Identity Management:** Dlib-based 128D face embeddings
* 
## Installation

```bash

# Clone the repository

git clone [https://github.com/yourusername/PRAGYAN-NETRA.git](https://github.com/yourusername/PRAGYAN-NETRA.git)



# Install core dependencies

pip install -r requirements.txt



# Download required model weights (YOLOv10n.pt / Vosk-model) 

# and place them in the models directory.
