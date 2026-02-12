"""
PRAGYAN-NETRA - Obstacle Detection Module
Uses YOLOv8 for real-time object detection
"""

import cv2
import numpy as np
from ultralytics import YOLO

class ObstacleDetector:
    def __init__(self, model_path='../models/yolo/yolov8n.pt'):
        """Initialize YOLOv8 detector"""
        self.model = YOLO(model_path)
        self.obstacle_classes = ['person', 'chair', 'table', 'bottle', 
                                'cell phone', 'stairs', 'door']
        
    def detect(self, image):
        """Detect obstacles in image"""
        results = self.model(image)
        detections = []
        
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                confidence = float(box.conf[0])
                bbox = box.xyxy[0].tolist()
                label = self.model.names[cls_id]
                
                if label in self.obstacle_classes and confidence > 0.5:
                    detections.append({
                        'type': label,
                        'confidence': confidence,
                        'bbox': bbox,
                        'position': self._get_position(bbox, image.shape)
                    })
        
        return detections
    
    def _get_position(self, bbox, image_shape):
        """Determine if object is left, center, or right"""
        x_center = (bbox[0] + bbox[2]) / 2
        width = image_shape[1]
        
        if x_center < width / 3:
            return "LEFT"
        elif x_center > 2 * width / 3:
            return "RIGHT"
        else:
            return "CENTER"
    
    def draw_detections(self, image, detections):
        """Draw bounding boxes on image"""
        for det in detections:
            x1, y1, x2, y2 = map(int, det['bbox'])
            label = f"{det['type']}: {det['confidence']:.2f}"
            
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return image