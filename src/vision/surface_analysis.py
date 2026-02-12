"""
PRAGYAN-NETRA - Surface Analysis Module
Detects surface changes, slopes, uneven terrain
"""

import cv2
import numpy as np

class SurfaceAnalyzer:
    def __init__(self):
        self.prev_frame = None
        
    def analyze_surface(self, frame):
        """Analyze surface for changes and hazards"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Edge detection for surface patterns
        edges = cv2.Canny(gray, 50, 150)
        
        # Detect lines (potential surface patterns)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, 
                               minLineLength=50, maxLineGap=10)
        
        analysis = {
            'surface_type': self._classify_surface(edges),
            'hazards': self._detect_hazards(edges),
            'slope': self._estimate_slope(lines) if lines is not None else 0,
            'confidence': 0.7
        }
        
        self.prev_frame = gray
        return analysis
    
    def _classify_surface(self, edges):
        """Classify surface type based on edge patterns"""
        edge_density = np.sum(edges > 0) / edges.size
        
        if edge_density > 0.3:
            return "ROUGH"
        elif edge_density > 0.1:
            return "TEXTURED"
        else:
            return "SMOOTH"
    
    def _detect_hazards(self, edges):
        """Detect potential surface hazards"""
        hazards = []
        
        # Look for abrupt changes (potholes, cracks)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, 
                                      cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Significant area
                hazards.append({
                    'type': 'SURFACE_DISCONTINUITY',
                    'area': area,
                    'severity': 'HIGH' if area > 1000 else 'MEDIUM'
                })
        
        return hazards
    
    def _estimate_slope(self, lines):
        """Estimate surface slope from lines"""
        if lines is None or len(lines) == 0:
            return 0
        
        angles = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            angles.append(angle)
        
        avg_angle = np.mean(angles)
        return abs(avg_angle)  # Absolute slope value