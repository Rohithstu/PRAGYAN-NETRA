# PRAGYAN-NETRA - SIMPLE VOICE DEMO
print("="*50)
print("PRAGYAN-NETRA VOICE SYSTEM")
print("="*50)

import pyttsx3
import time

print("\nInitializing voice engine...")

# Create TTS engine
engine = pyttsx3.init()

# Test voice
print("Testing voice... You should hear audio!")
engine.say("Hello! Welcome to Pragyan Netra")
engine.say("AI vision system for visually impaired")
engine.runAndWait()

print("\nVoice test successful!")

# Obstacle alerts with voice
print("\n" + "-"*50)
print("SIMULATING OBSTACLE ALERTS")
print("-"*50)

alerts = [
    "Warning! Chair detected on your left",
    "Caution! Stairs ahead",
    "Person detected 3 meters ahead",
    "Clear path on right side",
    "Destination reached"
]

for i, alert in enumerate(alerts, 1):
    print(f"{i}. {alert}")
    engine.say(alert)
    engine.runAndWait()
    time.sleep(1)

print("\n" + "="*50)
print("VOICE SYSTEM READY!")
print("="*50)
print("\nNext: Combine with camera for real-time detection")