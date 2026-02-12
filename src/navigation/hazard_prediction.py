"""
PRAGYAN-NETRA - Hazard Prediction Module
Predicts potential hazards based on context
"""

import numpy as np
from datetime import datetime

class HazardPredictor:
    def __init__(self):
        self.hazard_history = []
        
    def predict_hazards(self, current_obstacles, context=None):
        """Predict potential hazards"""
        hazards = []
        
        # Immediate hazards from current obstacles
        for obs in current_obstacles:
            if obs.get('distance') in ['VERY_CLOSE', 'CLOSE']:
                hazards.append({
                    'type': 'IMMEDIATE_COLLISION',
                    'object': obs.get('type', 'UNKNOWN'),
                    'position': obs.get('position', 'UNKNOWN'),
                    'severity': 'HIGH',
                    'time_to_impact': 'IMMEDIATE'
                })
        
        # Context-based predictions
        if context and 'predictions' in context:
            for pred in context['predictions']:
                if pred['confidence'] > 0.7:
                    hazards.append({
                        'type': 'PREDICTED_OBSTACLE',
                        'object': pred['type'],
                        'position': pred['position'],
                        'severity': 'MEDIUM',
                        'time_to_impact': 'SOON',
                        'confidence': pred['confidence']
                    })
        
        # Environmental hazards (simulated)
        current_hour = datetime.now().hour
        if 18 <= current_hour <= 6:  # Evening/Night
            hazards.append({
                'type': 'LOW_LIGHT',
                'severity': 'MEDIUM',
                'recommendation': 'USE_ASSISTIVE_LIGHT'
            })
        
        # Remove duplicates
        unique_hazards = []
        seen = set()
        for hazard in hazards:
            key = (hazard['type'], hazard.get('object', ''), hazard.get('position', ''))
            if key not in seen:
                seen.add(key)
                unique_hazards.append(hazard)
        
        return unique_hazards
    
    def calculate_risk_score(self, hazards):
        """Calculate overall risk score (0-100)"""
        if not hazards:
            return 0
        
        severity_weights = {
            'HIGH': 10,
            'MEDIUM': 5,
            'LOW': 2
        }
        
        total_score = 0
        for hazard in hazards:
            severity = hazard.get('severity', 'LOW')
            total_score += severity_weights.get(severity, 1)
        
        # Normalize to 0-100 scale
        risk_score = min(100, total_score * 5)
        return risk_score
    
    def get_safety_recommendations(self, hazards, risk_score):
        """Get safety recommendations based on hazards"""
        recommendations = []
        
        if risk_score > 70:
            recommendations.append("🚨 EMERGENCY: Stop immediately and seek assistance")
        
        for hazard in hazards:
            if hazard['type'] == 'IMMEDIATE_COLLISION':
                recommendations.append(f"⚠️ Avoid {hazard.get('object')} on your {hazard.get('position')}")
            elif hazard['type'] == 'LOW_LIGHT':
                recommendations.append("💡 Low light conditions detected. Proceed with caution.")
            elif hazard['type'] == 'PREDICTED_OBSTACLE':
                recommendations.append(f"🔮 Watch for {hazard.get('object')} on your {hazard.get('position')}")
        
        if not recommendations and risk_score < 30:
            recommendations.append("✅ Path appears safe. Continue with normal pace.")
        
        return recommendations