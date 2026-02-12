"""
PRAGYAN-NETRA - Text-to-Speech Module
Voice guidance and alerts
"""

import pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.setup_voice()
    
    def setup_voice(self, rate=160, volume=1.0):
        """Configure voice settings"""
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Try to set female voice
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
    
    def speak(self, text, priority="info"):
        """Speak text with priority-based styling"""
        priorities = {
            "emergency": "🚨",
            "warning": "⚠️",
            "info": "ℹ️",
            "success": "✅"
        }
        
        icon = priorities.get(priority, "🗣️")
        print(f"{icon} {text}")
        
        self.engine.say(text)
        self.engine.runAndWait()
    
    def obstacle_alert(self, obj_name, position, distance):
        """Generate obstacle alert"""
        if distance in ["VERY_CLOSE", "CLOSE"]:
            self.speak(f"Emergency! {obj_name} very close on your {position}!", "emergency")
        elif distance == "MODERATE":
            self.speak(f"Warning: {obj_name} ahead on your {position}", "warning")
        else:
            self.speak(f"{obj_name} detected {distance} on your {position}", "info")
    
    def navigation_guide(self, direction, distance=""):
        """Give navigation instructions"""
        if direction == "STRAIGHT":
            msg = f"Continue straight{distance}"
        elif direction == "LEFT":
            msg = f"Turn left{distance}"
        elif direction == "RIGHT":
            msg = f"Turn right{distance}"
        elif direction == "STOP":
            msg = f"Stop! {distance}"
        else:
            msg = direction
        
        self.speak(msg, "info")