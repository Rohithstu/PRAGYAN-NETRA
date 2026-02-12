"""
PRAGYAN-NETRA - Speech-to-Text Module
Voice commands input
"""

import speech_recognition as sr

class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
    def listen_command(self, timeout=5):
        """Listen for voice command"""
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=timeout)
                
                command = self.recognizer.recognize_google(audio)
                print(f"✅ Heard: {command}")
                return command.lower()
                
        except sr.WaitTimeoutError:
            print("⏰ No speech detected")
            return None
        except sr.UnknownValueError:
            print("🔇 Could not understand audio")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def get_voice_commands(self):
        """Get available voice commands"""
        return {
            "start navigation": "Begin navigation assistance",
            "stop": "Stop current operation",
            "where am i": "Get current location",
            "help": "Get available commands",
            "emergency": "Trigger emergency alert"
        }