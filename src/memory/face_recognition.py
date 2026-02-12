"""
PRAGYAN-NETRA - Face Recognition Module
Cognitive memory for familiar faces
"""

import os
import json
import cv2
import numpy as np

class FaceMemory:
    def __init__(self, data_dir='../../data'):
        self.data_dir = data_dir
        self.faces_dir = os.path.join(data_dir, 'faces')
        self.memory_file = os.path.join(data_dir, 'face_memory.json')
        
        os.makedirs(self.faces_dir, exist_ok=True)
        self.load_memory()
    
    def load_memory(self):
        """Load face memory from file"""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.memory = json.load(f)
        else:
            self.memory = {"known_faces": {}}
    
    def save_memory(self):
        """Save face memory to file"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def add_face(self, name, image=None, features=None):
        """Add a new face to memory"""
        face_id = len(self.memory['known_faces']) + 1
        
        self.memory['known_faces'][name] = {
            'id': face_id,
            'added': '2026-02-08',  # In real app, use datetime
            'samples': 1
        }
        
        # Save face image if provided
        if image is not None:
            face_path = os.path.join(self.faces_dir, f"{name}_{face_id}.jpg")
            cv2.imwrite(face_path, image)
        
        self.save_memory()
        return face_id
    
    def recognize_face(self, image):
        """Simulate face recognition"""
        # In real implementation, use FaceNet/MobileNet
        # For simulation, return a random known face
        import random
        
        if self.memory['known_faces']:
            names = list(self.memory['known_faces'].keys())
            return random.choice(names), 0.75
        else:
            return "UNKNOWN", 0.0
    
    def get_all_faces(self):
        """Get all known faces"""
        return self.memory['known_faces']