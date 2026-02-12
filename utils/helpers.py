"""
PRAGYAN-NETRA - Utility Functions
Common helper functions used across modules
"""

import json
import os
import cv2
import numpy as np
from datetime import datetime

def load_config(config_path="config/settings.py"):
    """Load configuration from file"""
    config = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            exec(f.read(), {}, config)
    return config

def save_image(image, folder, name_prefix="img"):
    """Save image with timestamp"""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name_prefix}_{timestamp}.jpg"
    filepath = os.path.join(folder, filename)
    cv2.imwrite(filepath, image)
    return filepath

def calculate_distance(bbox, image_shape):
    """Estimate distance based on bounding box size"""
    x1, y1, x2, y2 = bbox
    box_area = (x2 - x1) * (y2 - y1)
    image_area = image_shape[0] * image_shape[1]
    ratio = box_area / image_area
    
    if ratio > 0.3:
        return "VERY_CLOSE", ratio
    elif ratio > 0.15:
        return "CLOSE", ratio
    elif ratio > 0.05:
        return "MODERATE", ratio
    else:
        return "FAR", ratio

def create_log_entry(event_type, details):
    """Create a log entry"""
    return {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "details": details
    }

def display_status(image, text, position=(10, 30), color=(0, 255, 0)):
    """Display status text on image"""
    cv2.putText(image, text, position, 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    return image