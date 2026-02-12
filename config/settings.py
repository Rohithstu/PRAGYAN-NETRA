# PRAGYAN-NETRA Configuration

# System Settings
PROJECT_NAME = "PRAGYAN-NETRA"
VERSION = "1.0.0"
TEAM = "Sparkerz"

# Paths
DATA_DIR = "data"
MODELS_DIR = "models"
LOGS_DIR = "logs"

# AI Model Paths
YOLO_MODEL = "models/yolo/yolov8n.pt"
FACENET_MODEL = "models/facenet/facenet_keras.h5"  # For future

# Voice Settings
VOICE_RATE = 160  # Speech speed
VOICE_VOLUME = 1.0  # 0.0 to 1.0
VOICE_GENDER = "female"  # Preferred voice gender

# Detection Settings
CONFIDENCE_THRESHOLD = 0.5
OBSTACLE_CLASSES = [
    'person', 'bicycle', 'car', 'motorcycle',
    'bus', 'truck', 'chair', 'table',
    'bottle', 'cell phone'
]

# Emergency Settings
EMERGENCY_CONTACTS = []  # Add phone numbers/emails
EMERGENCY_MESSAGE = "Emergency! User needs assistance!"

# Navigation Settings
SAFETY_THRESHOLD = 60  # Minimum safety score (0-100)
UPDATE_INTERVAL = 1.0  # Seconds between updates