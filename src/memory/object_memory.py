"""
PRAGYAN-NETRA - Object Memory Module
Remember personal objects and locations
"""

import os
import json
from datetime import datetime

class ObjectMemory:
    def __init__(self, data_dir='../../data'):
        self.data_dir = data_dir
        self.memory_file = os.path.join(data_dir, 'object_memory.json')
        
        os.makedirs(os.path.join(data_dir, 'objects'), exist_ok=True)
        self.load_memory()
    
    def load_memory(self):
        """Load object memory"""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.memory = json.load(f)
        else:
            self.memory = {"personal_objects": {}}
    
    def save_memory(self):
        """Save object memory"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def add_object(self, obj_name, location, description=""):
        """Add a personal object to memory"""
        self.memory['personal_objects'][obj_name] = {
            'location': location,
            'description': description,
            'added': datetime.now().isoformat(),
            'last_seen': datetime.now().isoformat()
        }
        self.save_memory()
    
    def find_object(self, obj_name):
        """Find a remembered object"""
        return self.memory['personal_objects'].get(obj_name)
    
    def get_all_objects(self):
        """Get all remembered objects"""
        return self.memory['personal_objects']
    
    def update_location(self, obj_name, new_location):
        """Update object location"""
        if obj_name in self.memory['personal_objects']:
            self.memory['personal_objects'][obj_name]['location'] = new_location
            self.memory['personal_objects'][obj_name]['last_seen'] = datetime.now().isoformat()
            self.save_memory()
            return True
        return False