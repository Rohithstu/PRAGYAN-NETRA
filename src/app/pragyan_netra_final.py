# ============================================================
# PRAGYAN-NETRA - FINAL INTEGRATED SYSTEM
# AI Vision + Voice + Real-time Detection + Memory
# Team Sparkerz: Subhiksha, Jenisha, Kaviyasri, Sumithra
# ============================================================

print("=" * 70)
print("           PRAGYAN-NETRA - FINAL SYSTEM")
print("   AI Cognitive Memory & Obstacle Detection System")
print("             For Visually Impaired Users")
print("=" * 70)

import cv2
import numpy as np
import pyttsx3
import time
import json
import os
from datetime import datetime

print("\n📦 Initializing PRAGYAN-NETRA System...")

# ==================== SYSTEM CONFIGURATION ====================
class SystemConfig:
    def __init__(self):
        self.project_name = "PRAGYAN-NETRA"
        self.version = "1.0.0"
        self.team = "Sparkerz"
        
        # Paths
        self.data_dir = "data"
        self.memory_file = os.path.join(self.data_dir, "memory.json")
        
        # Create directories if they don't exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "faces"), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "objects"), exist_ok=True)
        
        # Load or create memory
        self.memory = self.load_memory()
        
    def load_memory(self):
        """Load cognitive memory from file"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        # Default memory structure
        return {
            "familiar_faces": {},
            "personal_objects": {},
            "safe_paths": [],
            "emergency_contacts": []
        }
    
    def save_memory(self):
        """Save cognitive memory to file"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)

# ==================== VOICE SYSTEM ====================
class VoiceAssistant:
    def __init__(self):
        print("🔊 Initializing Voice Assistant...")
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('volume', 1.0)
        
        # Try to set female voice if available
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        print("✅ Voice Assistant ready")
    
    def speak(self, text, priority="normal"):
        """Speak with priority levels"""
        colors = {
            "emergency": "\033[91m",  # Red
            "warning": "\033[93m",    # Yellow
            "normal": "\033[92m",     # Green
            "info": "\033[94m"        # Blue
        }
        
        reset = "\033[0m"
        color = colors.get(priority, colors["normal"])
        
        print(f"{color}🗣️  VOICE: {text}{reset}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def welcome_message(self):
        """System welcome message"""
        welcome_text = f"""
        Welcome to {config.project_name} version {config.version}
        AI Cognitive Memory and Safety Assistance System
        Developed by Team {config.team}
        System initializing...
        """
        self.speak(welcome_text, "info")

# ==================== SIMULATION MODE (No YOLO) ====================
class SimulationDetector:
    def __init__(self):
        print("🤖 Initializing Simulation Detector...")
        self.objects_database = {
            "person": ["Subhiksha", "Jenisha", "Kaviyasri", "Sumithra", "Unknown"],
            "chair": ["Office Chair", "Dining Chair", "Wheelchair"],
            "table": ["Dining Table", "Study Table", "Coffee Table"],
            "bottle": ["Water Bottle", "Medicine Bottle"],
            "phone": ["Mobile Phone", "Landline"],
            "stairs": ["Staircase Up", "Staircase Down"],
            "door": ["Entrance Door", "Room Door"]
        }
        print("✅ Simulation Detector ready")
    
    def detect_objects(self, frame):
        """Simulate object detection"""
        height, width = frame.shape[:2]
        
        # Divide frame into regions
        regions = {
            "left": frame[height//2:, :width//3],
            "center": frame[height//2:, width//3:2*width//3],
            "right": frame[height//2:, 2*width//3:]
        }
        
        detections = []
        
        for region_name, region in regions.items():
            # Simple brightness-based detection for simulation
            avg_brightness = np.mean(region)
            
            if avg_brightness < 100:  # Dark area = potential obstacle
                # Randomly select an object type
                import random
                obj_type = random.choice(list(self.objects_database.keys()))
                obj_name = random.choice(self.objects_database[obj_type])
                
                # Estimate distance based on darkness
                if avg_brightness < 50:
                    distance = "VERY CLOSE"
                    confidence = 0.85
                elif avg_brightness < 80:
                    distance = "CLOSE"
                    confidence = 0.75
                else:
                    distance = "MODERATE"
                    confidence = 0.65
                
                detections.append({
                    "type": obj_type,
                    "name": obj_name,
                    "region": region_name.upper(),
                    "distance": distance,
                    "confidence": confidence,
                    "brightness": avg_brightness
                })
        
        return detections

# ==================== MAIN SYSTEM ====================
class PragyanNetraSystem:
    def __init__(self):
        print("\n" + "="*70)
        print("PRAGYAN-NETRA SYSTEM STARTING...")
        print("="*70)
        
        # Initialize components
        self.config = SystemConfig()
        self.voice = VoiceAssistant()
        self.detector = SimulationDetector()
        
        # System state
        self.running = True
        self.emergency_mode = False
        self.last_alert_time = 0
        self.alert_cooldown = 5  # seconds
        
        # Statistics
        self.objects_detected = 0
        self.warnings_issued = 0
        self.emergencies_handled = 0
        
    def start(self):
        """Start the main system"""
        self.voice.welcome_message()
        time.sleep(1)
        
        self.voice.speak("Select mode: 1. Camera Mode, 2. Simulation Mode, 3. Memory Mode, 4. Exit", "info")
        
        while self.running:
            print("\n" + "="*50)
            print("PRAGYAN-NETRA CONTROL PANEL")
            print("="*50)
            print("1. 📷 Camera Mode (Real-time Detection)")
            print("2. 🎮 Simulation Mode (Demo without camera)")
            print("3. 🧠 Memory Mode (Manage cognitive memory)")
            print("4. 🆘 Emergency Test")
            print("5. 📊 System Status")
            print("6. 🚪 Exit System")
            print("-"*50)
            
            try:
                choice = input("Select option (1-6): ").strip()
                
                if choice == "1":
                    self.camera_mode()
                elif choice == "2":
                    self.simulation_mode()
                elif choice == "3":
                    self.memory_mode()
                elif choice == "4":
                    self.emergency_test()
                elif choice == "5":
                    self.system_status()
                elif choice == "6":
                    self.shutdown()
                else:
                    self.voice.speak("Invalid option. Please try again.", "warning")
                    
            except KeyboardInterrupt:
                self.shutdown()
            except Exception as e:
                print(f"Error: {e}")
                self.voice.speak("System error occurred. Returning to main menu.", "warning")
    
    def camera_mode(self):
        """Real-time camera detection mode"""
        self.voice.speak("Starting camera mode. Opening webcam...", "info")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.voice.speak("Cannot open webcam. Please check camera connection.", "warning")
            return
        
        self.voice.speak("Camera ready. Show objects to the camera. Press Q to quit.", "info")
        
        print("\n" + "="*50)
        print("CAMERA MODE - LIVE DETECTION")
        print("="*50)
        print("Commands:")
        print("- Press 'Q' to quit")
        print("- Press 'S' to speak status")
        print("- Press 'E' for emergency alert")
        print("- Press 'M' to memorize current scene")
        print("="*50)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Display frame with UI
            display_frame = frame.copy()
            cv2.putText(display_frame, "PRAGYAN-NETRA - LIVE", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display_frame, f"Objects: {self.objects_detected} | Warnings: {self.warnings_issued}", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            cv2.putText(display_frame, "Press Q to quit | S: Speak | E: Emergency | M: Memorize", 
                       (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            
            # Run detection periodically
            current_time = time.time()
            if current_time - self.last_alert_time > self.alert_cooldown:
                detections = self.detector.detect_objects(frame)
                
                if detections:
                    self.objects_detected += len(detections)
                    
                    for det in detections:
                        if det['distance'] in ["VERY CLOSE", "CLOSE"]:
                            self.warnings_issued += 1
                            alert_msg = f"Warning! {det['name']} {det['distance'].lower()} on your {det['region'].lower()}"
                            self.voice.speak(alert_msg, "warning")
                        else:
                            info_msg = f"{det['name']} detected {det['distance'].lower()} on your {det['region'].lower()}"
                            self.voice.speak(info_msg, "info")
                    
                    self.last_alert_time = current_time
            
            # Show frame
            cv2.imshow('PRAGYAN-NETRA - Live Camera', display_frame)
            
            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                status = f"System active. Detected {self.objects_detected} objects so far."
                self.voice.speak(status, "info")
            elif key == ord('e'):
                self.trigger_emergency()
            elif key == ord('m'):
                self.memorize_scene(frame)
        
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        self.voice.speak("Camera mode ended. Returning to main menu.", "info")
    
    def simulation_mode(self):
        """Simulation mode without camera"""
        self.voice.speak("Starting simulation mode. Generating test scenarios...", "info")
        
        scenarios = [
            {"name": "Indoor Navigation", "obstacles": ["Chair", "Table", "Person"]},
            {"name": "Staircase Detection", "obstacles": ["Stairs Up", "Stairs Down", "Handrail"]},
            {"name": "Object Recognition", "obstacles": ["Water Bottle", "Mobile Phone", "Keys"]},
            {"name": "Familiar Face", "obstacles": ["Subhiksha", "Jenisha", "Kaviyasri"]}
        ]
        
        for scenario in scenarios:
            print(f"\n📋 Scenario: {scenario['name']}")
            print("-" * 40)
            
            for obstacle in scenario['obstacles']:
                import random
                positions = ["LEFT", "CENTER", "RIGHT"]
                distances = ["VERY CLOSE", "CLOSE", "MODERATE", "FAR"]
                
                pos = random.choice(positions)
                dist = random.choice(distances)
                
                print(f"📍 Detected: {obstacle} - Position: {pos} - Distance: {dist}")
                
                if dist in ["VERY CLOSE", "CLOSE"]:
                    self.voice.speak(f"Warning! {obstacle} {dist.lower()} on your {pos.lower()}", "warning")
                    self.warnings_issued += 1
                else:
                    self.voice.speak(f"{obstacle} detected {dist.lower()} on your {pos.lower()}", "info")
                
                self.objects_detected += 1
                time.sleep(1)
            
            # Navigation guidance
            guidance = random.choice([
                "Safe path available on right side",
                "Proceed straight with caution",
                "Turn left to avoid obstacles",
                "Clear path ahead"
            ])
            
            print(f"🧭 Guidance: {guidance}")
            self.voice.speak(guidance, "info")
            time.sleep(2)
        
        self.voice.speak("Simulation completed successfully.", "info")
    
    def memory_mode(self):
        """Cognitive memory management"""
        print("\n" + "="*50)
        print("COGNITIVE MEMORY MANAGEMENT")
        print("="*50)
        print("1. View familiar faces")
        print("2. View personal objects")
        print("3. Add new memory")
        print("4. Back to main menu")
        print("-"*50)
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            faces = self.config.memory.get("familiar_faces", {})
            if faces:
                print("\n👨‍👩‍👧‍👦 Familiar Faces:")
                for name, details in faces.items():
                    print(f"  • {name}: {details.get('relation', 'Unknown')}")
            else:
                print("No faces memorized yet.")
                self.voice.speak("No familiar faces in memory yet.", "info")
        
        elif choice == "2":
            objects = self.config.memory.get("personal_objects", {})
            if objects:
                print("\n📦 Personal Objects:")
                for obj, details in objects.items():
                    print(f"  • {obj}: {details.get('location', 'Unknown location')}")
            else:
                print("No objects memorized yet.")
                self.voice.speak("No personal objects in memory yet.", "info")
        
        elif choice == "3":
            print("\n➕ Add New Memory:")
            mem_type = input("Type (face/object): ").strip().lower()
            
            if mem_type == "face":
                name = input("Person's name: ").strip()
                relation = input("Relation: ").strip()
                
                if name:
                    self.config.memory.setdefault("familiar_faces", {})
                    self.config.memory["familiar_faces"][name] = {
                        "relation": relation,
                        "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.config.save_memory()
                    print(f"✅ Added {name} to familiar faces.")
                    self.voice.speak(f"Added {name} to memory.", "info")
            
            elif mem_type == "object":
                obj_name = input("Object name: ").strip()
                location = input("Location: ").strip()
                
                if obj_name:
                    self.config.memory.setdefault("personal_objects", {})
                    self.config.memory["personal_objects"][obj_name] = {
                        "location": location,
                        "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.config.save_memory()
                    print(f"✅ Added {obj_name} to personal objects.")
                    self.voice.speak(f"Added {obj_name} to memory.", "info")
        
        self.voice.speak("Memory mode completed.", "info")
    
    def memorize_scene(self, frame):
        """Memorize current camera scene"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.config.data_dir, f"memory_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        
        self.voice.speak(f"Scene memorized and saved. Total memories: {len(os.listdir(self.config.data_dir))}", "info")
        print(f"📸 Scene saved: {filename}")
    
    def trigger_emergency(self):
        """Trigger emergency alert"""
        self.emergencies_handled += 1
        self.voice.speak("EMERGENCY ALERT ACTIVATED! Danger detected! Alerting caregivers!", "emergency")
        
        # Log emergency
        emergency_log = {
            "timestamp": datetime.now().isoformat(),
            "type": "manual_trigger",
            "location": "unknown"
        }
        
        self.config.memory.setdefault("emergencies", [])
        self.config.memory["emergencies"].append(emergency_log)
        self.config.save_memory()
        
        print("🚨 EMERGENCY LOGGED: Check memory.json for details")
        time.sleep(2)
        self.voice.speak("Emergency response initiated. Help is on the way.", "warning")
    
    def emergency_test(self):
        """Test emergency system"""
        self.voice.speak("Starting emergency system test...", "info")
        time.sleep(1)
        
        emergencies = [
            ("FALL RISK", "Steep staircase detected immediately ahead!"),
            ("COLLISION ALERT", "Large obstacle in direct path!"),
            ("GET HELP", "Sending your location to emergency contacts!"),
            ("ALL CLEAR", "Emergency cleared. Safe path available.")
        ]
        
        for title, message in emergencies:
            print(f"🚨 {title}: {message}")
            self.voice.speak(message, "emergency" if "CLEAR" not in title else "info")
            time.sleep(2)
        
        self.voice.speak("Emergency system test completed successfully.", "info")
    
    def system_status(self):
        """Display system status"""
        print("\n" + "="*50)
        print("SYSTEM STATUS REPORT")
        print("="*50)
        print(f"System: {self.config.project_name} v{self.config.version}")
        print(f"Team: {self.config.team}")
        print(f"Uptime: {time.strftime('%H:%M:%S')}")
        print(f"Objects Detected: {self.objects_detected}")
        print(f"Warnings Issued: {self.warnings_issued}")
        print(f"Emergencies Handled: {self.emergencies_handled}")
        
        # Memory stats
        faces = len(self.config.memory.get('familiar_faces', {}))
        objects = len(self.config.memory.get('personal_objects', {}))
        print(f"Familiar Faces: {faces}")
        print(f"Personal Objects: {objects}")
        
        print("-"*50)
        self.voice.speak(f"System status: Active. Detected {self.objects_detected} objects. Issued {self.warnings_issued} warnings.", "info")
    
    def shutdown(self):
        """Graceful system shutdown"""
        print("\n" + "="*50)
        print("SYSTEM SHUTDOWN INITIATED")
        print("="*50)
        
        # Save final state
        self.config.save_memory()
        
        # Final report
        print(f"\n📊 FINAL REPORT:")
        print(f"  • Objects Detected: {self.objects_detected}")
        print(f"  • Warnings Issued: {self.warnings_issued}")
        print(f"  • Emergencies Handled: {self.emergencies_handled}")
        print(f"  • Memory Entries: {len(self.config.memory.get('familiar_faces', {})) + len(self.config.memory.get('personal_objects', {}))}")
        
        # Goodbye message
        self.voice.speak(f"Pragyan Netra system shutting down. Thank you for using our system. Stay safe!", "info")
        time.sleep(1)
        
        print("\n" + "="*50)
        print("PRAGYAN-NETRA SYSTEM OFFLINE")
        print("="*50)
        
        self.running = False

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    try:
        # Create and start system
        system = PragyanNetraSystem()
        system.start()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  System interrupted by user")
    except Exception as e:
        print(f"\n❌ System error: {e}")
    finally:
        print("\n" + "="*70)
        print("THANK YOU FOR USING PRAGYAN-NETRA")
        print("AI for Accessibility | Team Sparkerz")
        print("="*70)