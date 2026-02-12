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
        print("SYSTEM: INITIALIZING PRAGYAN-NETRA V4")
        
        # 1. Vision & Voice Engines
        self.yolo = YOLO("yolov10n.pt")
        self.engine = pyttsx3.init()
        self.speech_queue = queue.Queue()
        
        # 2. Vosk Setup
        self.model = Model(vosk_path)
        self.rec = KaldiRecognizer(self.model, 16000)
        self.wake_word = "netra"

        # 3. Social Memory
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
        if not os.path.exists(self.face_db_path): os.makedirs(self.face_db_path)
        for f in os.listdir(self.face_db_path):
            if f.endswith((".jpg", ".png")):
                img = face_recognition.load_image_file(os.path.join(self.face_db_path, f))
                # FORCE 8-bit conversion for NumPy 2 compatibility
                img = np.array(img, dtype='uint8')
                enc = face_recognition.face_encodings(img)
                if enc:
                    self.known_face_encodings.append(enc[0])
                    self.known_face_names.append(os.path.splitext(f)[0])
        print(f"MEMORY: {len(self.known_face_names)} identities loaded.")

    def wall_hazard_check(self, frame):
        """Detects walls by looking for high vertical edge density at floor level."""
        h, w = frame.shape[:2]
        roi = frame[int(h*0.7):h, int(w*0.3):int(w*0.7)]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        
        # Lowered threshold to 3000 for better sensitivity
        if np.sum(edges > 0) > 3000: 
            if time.time() - self.last_wall_beep > 1.2:
                winsound.Beep(500, 200) # Warning beep
                self.last_wall_beep = time.time()

    def voice_thread(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()

        print("🎤 Netra is listening... Say 'Netra'")
        while self.running:
            data = stream.read(4000, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data):
                res = json.loads(self.rec.Result())['text']
                print(f"Heard: {res}") # Debug line
                
                if self.wake_word in res:
                    winsound.Beep(1000, 100) # Feedback chirp
                    self.speech_queue.put("Yes, I am here.")
                    self.active_listening = True
                
                if self.active_listening and "stop" in res:
                    self.active_listening = False

    def speaker_worker(self):
        while self.running:
            if not self.speech_queue.empty():
                text = self.speech_queue.get()
                self.engine.say(text)
                self.engine.runAndWait()

    def run(self):
        threading.Thread(target=self.voice_thread, daemon=True).start()
        threading.Thread(target=self.speaker_worker, daemon=True).start()

        cap = cv2.VideoCapture(0)
        while self.running:
            ret, frame = cap.read()
            if not ret: break
            
            self.wall_hazard_check(frame)

            # Face & Distance Logic
            rgb_frame = frame[:, :, ::-1]
            face_locs = face_recognition.face_locations(rgb_frame)
            face_encs = face_recognition.face_encodings(rgb_frame, face_locs)

            for (t, r, b, l), enc in zip(face_locs, face_encs):
                matches = face_recognition.compare_faces(self.known_face_encodings, enc)
                name = self.known_face_names[matches.index(True)] if True in matches else "Unknown"
                
                # Distance Estimation (approx steps)
                steps = round(400 / (r - l + 1)) 
                
                if name not in self.last_face_time or time.time() - self.last_face_time[name] > 10:
                    self.speech_queue.put(f"{name} spotted, {steps} steps away.")
                    self.last_face_time[name] = time.time()

                cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)

            cv2.imshow("Netra OS V4", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    VOSK_DIR = r"C:\Users\Admin\PRAGYAN-NETRA\src\app\vosk-model"
    FACE_DIR = r"C:\Users\Admin\PRAGYAN-NETRA\data\faces"
    netra = PragyanNetraOS(VOSK_DIR, FACE_DIR)
    netra.run()