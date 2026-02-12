"""
Test Voice Module
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from voice.tts import VoiceAssistant

def test_voice_assistant():
    print("Testing Voice Assistant...")
    
    voice = VoiceAssistant()
    
    # Test basic speech
    voice.speak("Test message", "info")
    
    # Test obstacle alert
    voice.obstacle_alert("CHAIR", "left", "CLOSE")
    
    # Test navigation
    voice.navigation_guide("RIGHT", " in 5 meters")
    
    print("✅ Voice test completed")
    return True

if __name__ == "__main__":
    test_voice_assistant()