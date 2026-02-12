"""
PRAGYAN-NETRA - Gemini AI Integration
Advanced AI responses using Google Gemini
"""

import json

class GeminiIntegration:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.enabled = api_key is not None
        
        # Pre-defined responses for offline use
        self.responses = {
            "greeting": [
                "Hello! I'm your Pragyan Netra assistant.",
                "Welcome to Pragyan Netra AI vision system.",
                "Hello there! Ready to assist you."
            ],
            "obstacle": {
                "chair": "A chair is blocking your path. Consider moving around it.",
                "table": "There's a table ahead. You might want to change direction.",
                "person": "A person is nearby. They might be moving, so proceed cautiously.",
                "stairs": "Stairs detected. Please be very careful and use handrail if available.",
                "door": "A door is ahead. Check if it's open before proceeding."
            },
            "navigation": {
                "left": "Turn left to avoid the obstacle.",
                "right": "Turn right for a clearer path.",
                "straight": "The path ahead looks clear. Continue straight.",
                "stop": "Please stop. There's an obstacle very close."
            },
            "emergency": [
                "Emergency detected! Help is on the way.",
                "Danger! Please move to a safe location immediately.",
                "Emergency alert activated. Stay calm, assistance is coming."
            ]
        }
    
    def get_response(self, query_type, details=None):
        """Get AI response for given query"""
        if not self.enabled:
            return self._get_offline_response(query_type, details)
        
        # In real implementation, call Gemini API
        # For now, use offline responses
        return self._get_offline_response(query_type, details)
    
    def _get_offline_response(self, query_type, details):
        """Get pre-defined offline response"""
        import random
        
        if query_type == "greeting":
            return random.choice(self.responses["greeting"])
        
        elif query_type == "obstacle" and details:
            obj_type = details.get('type', '').lower()
            if obj_type in self.responses["obstacle"]:
                return self.responses["obstacle"][obj_type]
            else:
                return f"A {obj_type} is detected. Please proceed with caution."
        
        elif query_type == "navigation" and details:
            direction = details.get('direction', '').lower()
            if direction in self.responses["navigation"]:
                return self.responses["navigation"][direction]
            else:
                return "Please adjust your path based on the obstacle locations."
        
        elif query_type == "emergency":
            return random.choice(self.responses["emergency"])
        
        else:
            return "I'm here to help. Please describe what you need."
    
    def analyze_scene(self, scene_description):
        """Analyze scene description (simulated)"""
        # In real implementation, send to Gemini for analysis
        analysis = {
            "summary": "Based on the scene, there are multiple obstacles.",
            "primary_hazard": "Chair on the left side",
            "recommended_action": "Move slightly to the right",
            "confidence": 0.85
        }
        
        return analysis
    
    def generate_detailed_guidance(self, obstacles, context):
        """Generate detailed guidance based on obstacles and context"""
        guidance = {
            "immediate_action": "Continue with caution",
            "long_term_advice": "",
            "warnings": [],
            "suggestions": []
        }
        
        close_obstacles = [o for o in obstacles if o.get('distance') in ['CLOSE', 'VERY_CLOSE']]
        
        if close_obstacles:
            guidance["immediate_action"] = "Slow down and assess the path"
            for obs in close_obstacles[:2]:  # Top 2 closest
                guidance["warnings"].append(
                    f"{obs.get('type', 'Object')} is very close on your {obs.get('position', 'side')}"
                )
        
        if len(obstacles) > 3:
            guidance["suggestions"].append("Consider taking an alternative route")
        
        if context and context.get('current_location') == 'STAIRS':
            guidance["long_term_advice"] = "Always use handrails on stairs"
        
        return guidance