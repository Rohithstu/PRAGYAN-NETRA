# ============================================================
# PROJECT: PRAGYAN-NETRA OS (V4)
# TEAM: LOGIC LIONS
# LEAD: ROHITH REDDY
# MEMBERS: YASHWANTH, KARTHIKEYA, VENU
# ============================================================

import cv2
import threading
import numpy as np
import pyttsx3
import winsound
import time
import json
import queue
import pyaudio
import os
import face_recognition
from vosk import Model, KaldiRecognizer
from ultralytics import YOLO

class PragyanNetraOS:
    def __init__(self, vosk_path, face_db_path):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print("            PRAGYAN-NETRA - LOGIC LIONS EDITION")
        print(f"    Lead: Rohith Reddy | Yashwanth | Karthikeya | Venu")
        print("=" * 70)
        print("SYSTEM: INITIALIZING V4 CORE ENGINES...")
        
        # 1. Vision & Voice Engines
        try:
            self.yolo = YOLO("yolov10n.pt")
            print("✅ Vision: YOLOv10 Loaded")
        except:
            print("⚠️ Vision: YOLO model not found, running in lite mode")

        self.engine = pyttsx3.init()
        self.speech_queue = queue.Queue()
        
        # 2. Vosk Voice Command Setup
        try:
            self.model = Model(vosk_path)
            self.rec = KaldiRecognizer(self.model, 16000)
            print("✅ Voice: Vosk Offline Model Loaded")
        except:
            print("❌ Voice: Vosk path error. Check your VOSK_DIR")

        self.wake_word = "netra"

        # 3. Social Memory (Team & Friends)
        self.face_db_path = face_db_path
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_social_memory()
        
        # 4. State Management
        self.active_listening = False
        self.running = True
        self.last_wall_beep = 0
        self.last_face_time = {}

    def load_social_memory(self):
        """Loads faces from the data/faces directory"""
        if not os.path.exists(self.face_db_path): 
            os.makedirs(self.face_db_path)
        
        for f in os.listdir(self.face_db_path):
            if f.endswith((".jpg", ".png")):
                img = face_recognition.load_image_file(os.path.join(self.face_db_path, f))
                img = np.array(img, dtype='uint8')
                enc = face_recognition.face_encodings(img)
                if enc:
                    self.known_face_encodings.append(enc[0])
                    self.known_face_names.append(os.path.splitext(f)[0])
        print(f"🧠 MEMORY: {len(self.known_face_names)} identities loaded into Social Memory.")

    def wall_hazard_check(self, frame):
        """Logic Lions Edge-Density Wall Detection"""
        h, w = frame.shape[:2]
        roi = frame[int(h*0.7):h, int(w*0.3):int(w*0.7)]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        
        if np.sum(edges > 0) > 3500: # Threshold for a flat barrier
            if time.time() - self.last_wall_beep > 1.5:
                winsound.Beep(600, 250) # Warning tone
                self.last_wall_beep = time.time()

    def voice_listener(self):
        """Thread to handle 'Netra' wake word"""
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()

        print("🎤 SYSTEM ACTIVE: Say 'Netra' to interact...")
        while self.running:
            data = stream.read(4000, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data):
                res = json.loads(self.rec.Result())['text']
                
                if self.wake_word in res:
                    winsound.Beep(1000, 100) # Logic Lions Success Chirp
                    self.speech_queue.put(f"Yes Rohith, Logic Lions system is ready.")
                    self.active_listening = True
                
                if "status" in res:
                    self.speech_queue.put("All systems nominal. Vision and hazard detection active.")

    def speaker_worker(self):
        """Thread to handle audio feedback without blocking vision"""
        while self.running:
            if not self.speech_queue.empty():
                text = self.speech_queue.get()
                self.engine.say(text)
                self.engine.runAndWait()

    def run(self):
        # Start background threads
        threading.Thread(target=self.voice_listener, daemon=True).start()
        threading.Thread(target=self.speaker_worker, daemon=True).start()

        cap = cv2.VideoCapture(0)
        
        # Start-up greeting
        self.speech_queue.put("Welcome back Rohith Reddy. Pragyan Netra is online.")

        while self.running:
            ret, frame = cap.read()
            if not ret: break
            
            # 1. Structural Hazard Detection
            self.wall_hazard_check(frame)

            # 2. Social Memory & Recognition
            rgb_frame = frame[:, :, ::-1]
            face_locs = face_recognition.face_locations(rgb_frame)
            face_encs = face_recognition.face_encodings(rgb_frame, face_locs)

            for (t, r, b, l), enc in zip(face_locs, face_encs):
                matches = face_recognition.compare_faces(self.known_face_encodings, enc)
                name = self.known_face_names[matches.index(True)] if True in matches else "Unknown Person"
                
                # Logic Lions Distance Estimation
                dist_factor = r - l
                steps = round(450 / (dist_factor + 1)) 
                
                if name not in self.last_face_time or time.time() - self.last_face_time[name] > 12:
                    self.speech_queue.put(f"{name} identified, {steps} steps away.")
                    self.last_face_time[name] = time.time()

                # Visual UI
                cv2.rectangle(frame, (l, t), (r, b), (255, 0, 0), 2)
                cv2.putText(frame, f"{name} ({steps} steps)", (l, t-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            cv2.imshow("PRAGYAN-NETRA V4: LOGIC LIONS EDITION", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                self.speech_queue.put("System shutting down. Goodbye Rohith.")
                time.sleep(2)
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # SET YOUR DIRECTORIES HERE
    VOSK_DIR = r"C:\Users\Admin\PRAGYAN-NETRA\src\app\vosk-model"
    FACE_DIR = r"C:\Users\Admin\PRAGYAN-NETRA\data\faces"
    
    netra = PragyanNetraOS(VOSK_DIR, FACE_DIR)
    netra.run()
