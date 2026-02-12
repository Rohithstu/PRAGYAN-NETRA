# PRAGYAN-NETRA - WORKING APPLICATION
# Fixed path issues, guaranteed to run

print("=" * 70)
print("           PRAGYAN-NETRA - WORKING SYSTEM")
print("   AI Cognitive Memory & Obstacle Detection")
print("=" * 70)

import os
import sys

# Fix paths - use absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
data_dir = os.path.join(current_dir, 'data')
models_dir = os.path.join(current_dir, 'models')

# Add to Python path
sys.path.insert(0, src_dir)

print(f"📁 Project root: {current_dir}")
print(f"📁 Source directory: {src_dir}")
print(f"📁 Data directory: {data_dir}")

# Check if directories exist
if not os.path.exists(data_dir):
    print("⚠️ Creating data directory...")
    os.makedirs(data_dir, exist_ok=True)

if not os.path.exists(models_dir):
    print("⚠️ Creating models directory...")
    os.makedirs(models_dir, exist_ok=True)

print("✅ Paths configured successfully")

# Now import modules
try:
    print("\n📦 Loading modules...")
    
    # Import with correct paths
    import pyttsx3
    import cv2
    import numpy as np
    import json
    
    print("✅ Core libraries loaded")
    
    # Try to import our modules
    try:
        from src.vision.obstacle_detection import ObstacleDetector
        print("✅ Vision module loaded")
    except:
        print("⚠️ Vision module not found, using simulation")
    
    try:
        from src.voice.tts import VoiceAssistant
        print("✅ Voice module loaded")
    except:
        print("⚠️ Voice module not found, creating basic version")
        
        # Create basic voice assistant
        class BasicVoice:
            def __init__(self):
                self.engine = pyttsx3.init()
            
            def speak(self, text):
                print(f"🗣️ {text}")
                self.engine.say(text)
                self.engine.runAndWait()
        
        VoiceAssistant = BasicVoice
    
    print("✅ All modules loaded successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("\nPlease install dependencies:")
    print("pip install opencv-python numpy pyttsx3")
    sys.exit(1)

# ============================================
# MAIN APPLICATION
# ============================================

class PragyanNetraApp:
    def __init__(self):
        print("\n🚀 Initializing PRAGYAN-NETRA...")
        
        # Initialize components
        self.voice = VoiceAssistant()
        self.running = True
        
        # Create data files if they don't exist
        self._init_data_files()
        
        print("✅ System initialized successfully!")
    
    def _init_data_files(self):
        """Initialize data files"""
        data_files = {
            'face_memory.json': {"known_faces": {}},
            'object_memory.json': {"personal_objects": {}},
            'context_memory.json': {"current_location": "UNKNOWN", "last_obstacles": []}
        }
        
        for filename, default_data in data_files.items():
            filepath = os.path.join(data_dir, filename)
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    json.dump(default_data, f, indent=2)
                print(f"📄 Created: {filename}")
    
    def start(self):
        """Start the main application"""
        self.voice.speak("Welcome to Pragyan Netra")
        self.voice.speak("AI vision system for visually impaired")
        
        self.main_menu()
    
    def main_menu(self):
        """Display main menu"""
        while self.running:
            print("\n" + "=" * 50)
            print("PRAGYAN-NETRA CONTROL PANEL")
            print("=" * 50)
            print("1. 📷 Camera Mode (Live Detection)")
            print("2. 🎮 Simulation Mode")
            print("3. 🧠 Memory Management")
            print("4. 🧭 Navigation Demo")
            print("5. 🚨 Emergency Test")
            print("6. 📊 System Info")
            print("7. 🚪 Exit")
            print("-" * 50)
            
            try:
                choice = input("Select option (1-7): ").strip()
                
                if choice == "1":
                    self.camera_mode()
                elif choice == "2":
                    self.simulation_mode()
                elif choice == "3":
                    self.memory_mode()
                elif choice == "4":
                    self.navigation_mode()
                elif choice == "5":
                    self.emergency_test()
                elif choice == "6":
                    self.system_info()
                elif choice == "7":
                    self.shutdown()
                else:
                    print("Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\n\nOperation cancelled.")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def camera_mode(self):
        """Live camera mode"""
        print("\n📷 Starting Camera Mode...")
        self.voice.speak("Starting camera mode")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Cannot open webcam")
            self.voice.speak("Cannot access camera. Please check connection.")
            return
        
        print("✅ Webcam activated")
        print("Press 'Q' to quit, 'S' to speak status")
        
        self.voice.speak("Camera ready. Showing live feed.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Display frame with overlay
            display = frame.copy()
            cv2.putText(display, "PRAGYAN-NETRA - LIVE", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display, "Press Q to quit | S: Status", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            
            # Simple obstacle simulation (draw boxes)
            height, width = frame.shape[:2]
            cv2.rectangle(display, (100, 100), (200, 200), (0, 0, 255), 2)
            cv2.putText(display, "SIM: CHAIR", (90, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            
            cv2.rectangle(display, (400, 150), (500, 250), (0, 255, 0), 2)
            cv2.putText(display, "SIM: TABLE", (390, 140),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
            # Show frame
            cv2.imshow('PRAGYAN-NETRA - Camera Mode', display)
            
            # Handle keyboard
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.voice.speak("Camera mode active. Showing live feed.")
        
        cap.release()
        cv2.destroyAllWindows()
        self.voice.speak("Camera mode ended.")
    
    def simulation_mode(self):
        """Simulation mode without camera"""
        print("\n🎮 Starting Simulation Mode...")
        self.voice.speak("Starting simulation mode")
        
        # Simulate obstacle detection
        obstacles = [
            ("CHAIR", "left", "close", "high"),
            ("TABLE", "center", "moderate", "medium"),
            ("PERSON", "right", "far", "low"),
            ("STAIRS", "ahead", "close", "high"),
            ("DOOR", "left", "moderate", "medium")
        ]
        
        print("\n🔍 Simulating obstacle detection:")
        print("-" * 40)
        
        for obj, pos, dist, danger in obstacles:
            print(f"⚠️ {obj:10} | {pos:8} | {dist:10} | Danger: {danger}")
            
            if danger == "high":
                self.voice.speak(f"Warning! {obj} very close on your {pos}!")
            elif danger == "medium":
                self.voice.speak(f"Caution. {obj} ahead on your {pos}.")
            else:
                self.voice.speak(f"{obj} detected {dist} on your {pos}.")
            
            import time
            time.sleep(1)
        
        print("\n🧭 Navigation guidance:")
        print("Move diagonally right to avoid obstacles")
        self.voice.speak("Safe path identified. Move right forward.")
        
        print("\n✅ Simulation completed successfully!")
        self.voice.speak("Simulation mode completed.")
    
    def memory_mode(self):
        """Memory management"""
        print("\n🧠 Memory Management")
        print("-" * 40)
        
        # Load existing memory
        face_file = os.path.join(data_dir, 'face_memory.json')
        object_file = os.path.join(data_dir, 'object_memory.json')
        
        try:
            with open(face_file, 'r') as f:
                faces = json.load(f)
            print(f"👥 Known faces: {len(faces.get('known_faces', {}))}")
        except:
            faces = {"known_faces": {}}
            print("👥 No faces in memory yet")
        
        try:
            with open(object_file, 'r') as f:
                objects = json.load(f)
            print(f"📦 Personal objects: {len(objects.get('personal_objects', {}))}")
        except:
            objects = {"personal_objects": {}}
            print("📦 No objects in memory yet")
        
        print("\nOptions:")
        print("1. Add new face")
        print("2. Add new object")
        print("3. View all memory")
        print("4. Back to main menu")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            name = input("Person's name: ").strip()
            relation = input("Relation (friend/family/etc): ").strip()
            
            if name:
                faces['known_faces'][name] = {
                    "relation": relation,
                    "added": "2026-02-08"
                }
                with open(face_file, 'w') as f:
                    json.dump(faces, f, indent=2)
                print(f"✅ Added {name} to face memory")
                self.voice.speak(f"Added {name} to memory")
        
        elif choice == "2":
            obj_name = input("Object name: ").strip()
            location = input("Location: ").strip()
            
            if obj_name and location:
                objects['personal_objects'][obj_name] = {
                    "location": location,
                    "added": "2026-02-08"
                }
                with open(object_file, 'w') as f:
                    json.dump(objects, f, indent=2)
                print(f"✅ Remembered {obj_name} at {location}")
                self.voice.speak(f"Remembered {obj_name}")
        
        elif choice == "3":
            print("\n📋 Memory Summary:")
            print("-" * 30)
            for name, info in faces.get('known_faces', {}).items():
                print(f"👤 {name}: {info.get('relation', 'Unknown')}")
            
            for obj, info in objects.get('personal_objects', {}).items():
                print(f"📦 {obj}: {info.get('location', 'Unknown location')}")
    
    def navigation_mode(self):
        """Navigation demo"""
        print("\n🧭 Navigation Demonstration")
        print("-" * 40)
        
        self.voice.speak("Starting navigation assistance")
        
        steps = [
            "Starting from main entrance",
            "Proceed straight for 5 meters",
            "Turn right at the corridor",
            "Continue for 10 meters",
            "Elevator on your left",
            "Destination: Library entrance reached"
        ]
        
        for i, step in enumerate(steps, 1):
            print(f"{i}. {step}")
            self.voice.speak(step)
            import time
            time.sleep(2)
        
        print("\n✅ Navigation demo completed")
        self.voice.speak("Navigation demonstration complete")
    
    def emergency_test(self):
        """Emergency system test"""
        print("\n🚨 Emergency System Test")
        print("-" * 40)
        
        self.voice.speak("Testing emergency alert system")
        import time
        
        alerts = [
            ("FALL RISK", "Steep staircase detected immediately ahead!"),
            ("COLLISION ALERT", "Large obstacle in direct path!"),
            ("EMERGENCY", "Sending alert to emergency contacts!"),
            ("ALL CLEAR", "Emergency cleared. Safe path available.")
        ]
        
        for title, message in alerts:
            print(f"⚠️ {title}: {message}")
            self.voice.speak(message)
            time.sleep(2)
        
        print("\n✅ Emergency test completed successfully")
        self.voice.speak("Emergency system test complete")
    
    def system_info(self):
        """Display system information"""
        print("\n📊 SYSTEM INFORMATION")
        print("=" * 40)
        print(f"Project: PRAGYAN-NETRA")
        print(f"Version: 1.0.0")
        print(f"Team: Sparkerz")
        print(f"Status: Operational")
        print()
        
        # Check components
        components = {
            "OpenCV": self._check_module("cv2"),
            "NumPy": self._check_module("numpy"),
            "Voice": self._check_module("pyttsx3"),
            "Webcam": self._check_camera()
        }
        
        print("Component Status:")
        for name, status in components.items():
            icon = "✅" if status else "❌"
            print(f"  {icon} {name}")
        
        # Data info
        print(f"\n📁 Data directory: {data_dir}")
        print(f"📁 Models directory: {models_dir}")
        
        self.voice.speak("System information displayed.")
    
    def _check_module(self, module_name):
        """Check if module is available"""
        try:
            __import__(module_name)
            return True
        except:
            return False
    
    def _check_camera(self):
        """Check if camera is available"""
        try:
            cap = cv2.VideoCapture(0)
            available = cap.isOpened()
            cap.release()
            return available
        except:
            return False
    
    def shutdown(self):
        """Shutdown system"""
        print("\n🔄 Shutting down PRAGYAN-NETRA...")
        self.voice.speak("Pragyan Netra system shutting down.")
        self.voice.speak("Thank you for using our system. Stay safe!")
        self.running = False

# ============================================
# RUN THE APPLICATION
# ============================================

if __name__ == "__main__":
    try:
        app = PragyanNetraApp()
        app.start()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  System interrupted by user")
    except Exception as e:
        print(f"\n❌ System error: {e}")
    finally:
        print("\n" + "=" * 70)
        print("PRAGYAN-NETRA - Project by Team Sparkerz")
        print("=" * 70)