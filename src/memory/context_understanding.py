"""
PRAGYAN-NETRA - Context Understanding Module
Understands scenes and maintains context
"""

import json
import os
from datetime import datetime

class ContextManager:
    def __init__(self, data_dir="../../data"):
        self.data_dir = data_dir
        self.context_file = os.path.join(data_dir, "context_memory.json")
        self.load_context()
        
    def load_context(self):
        """Load context memory"""
        if os.path.exists(self.context_file):
            with open(self.context_file, 'r') as f:
                self.context = json.load(f)
        else:
            self.context = {
                "current_location": "UNKNOWN",
                "last_obstacles": [],
                "frequent_paths": {},
                "time_patterns": {}
            }
    
    def save_context(self):
        """Save context memory"""
        with open(self.context_file, 'w') as f:
            json.dump(self.context, f, indent=2)
    
    def update_location(self, location, confidence=0.8):
        """Update current location context"""
        self.context['current_location'] = location
        self.context['location_confidence'] = confidence
        self.context['last_updated'] = datetime.now().isoformat()
        self.save_context()
    
    def add_obstacle_context(self, obstacle_type, position, time_of_day=None):
        """Add obstacle to context memory"""
        if time_of_day is None:
            time_of_day = datetime.now().strftime("%H:%M")
        
        obstacle_entry = {
            "type": obstacle_type,
            "position": position,
            "time": time_of_day,
            "timestamp": datetime.now().isoformat()
        }
        
        self.context['last_obstacles'].append(obstacle_entry)
        
        # Keep only last 50 obstacles
        if len(self.context['last_obstacles']) > 50:
            self.context['last_obstacles'] = self.context['last_obstacles'][-50:]
        
        # Update frequency
        key = f"{obstacle_type}_{position}"
        self.context['frequent_paths'][key] = \
            self.context['frequent_paths'].get(key, 0) + 1
        
        self.save_context()
    
    def predict_obstacles(self, current_time=None):
        """Predict likely obstacles based on history"""
        if current_time is None:
            current_time = datetime.now().strftime("%H:%M")
        
        predictions = []
        
        # Analyze patterns
        for obstacle in self.context['last_obstacles'][-20:]:  # Last 20
            if obstacle['time'][:2] == current_time[:2]:  # Same hour
                predictions.append({
                    "type": obstacle['type'],
                    "position": obstacle['position'],
                    "confidence": 0.6,
                    "based_on": "TIME_PATTERN"
                })
        
        # Check frequent paths
        for key, count in self.context['frequent_paths'].items():
            if count > 3:  # Appeared at least 3 times
                obs_type, position = key.split('_', 1)
                predictions.append({
                    "type": obs_type,
                    "position": position,
                    "confidence": min(0.9, count / 10),
                    "based_on": "FREQUENCY"
                })
        
        return predictions
    
    def get_context_summary(self):
        """Get current context summary"""
        return {
            "location": self.context['current_location'],
            "recent_obstacles": len(self.context['last_obstacles']),
            "known_patterns": len(self.context['frequent_paths']),
            "time_patterns": len(self.context['time_patterns'])
        }