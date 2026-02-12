# PRAGYAN-NETRA OBSTACLE DETECTION DEMO
# SIMPLE VERSION - NO ERRORS

print("=" * 60)
print("PRAGYAN-NETRA - OBSTACLE DETECTION")
print("Team Sparkerz")
print("=" * 60)
print()

print("1. Loading libraries...")
import cv2
import numpy as np

print("2. Creating test scene...")
# Create image
img = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw obstacles
cv2.rectangle(img, (100, 150), (200, 250), (0, 0, 255), -1)  # Red obstacle
cv2.rectangle(img, (300, 200), (400, 300), (0, 255, 0), -1)   # Green obstacle
cv2.circle(img, (500, 200), 60, (255, 0, 0), -1)              # Blue obstacle

# Add labels
cv2.putText(img, "CHAIR", (120, 140), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
cv2.putText(img, "TABLE", (320, 190), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
cv2.putText(img, "PERSON", (470, 140), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Add title
cv2.putText(img, "PRAGYAN-NETRA Demo", (150, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

# Save image
cv2.imwrite("demo_scene.jpg", img)
print("3. Image saved: demo_scene.jpg")

# Show results
print("\n4. Detection Results:")
print("-" * 40)
print("1. CHAIR   - LEFT   - CLOSE   - DANGER: HIGH")
print("2. TABLE   - CENTER - MEDIUM  - DANGER: MEDIUM")
print("3. PERSON  - RIGHT  - FAR     - DANGER: LOW")

print("\n5. Voice Alerts:")
print("-" * 40)
print("WARNING: Chair close on left!")
print("Caution: Table ahead in center")
print("Info: Person far on right")

print("\n6. Navigation Advice:")
print("-" * 40)
print("Move diagonally right to avoid obstacles")

print("\n" + "=" * 60)
print("NEXT STEP:")
print("Install YOLO for real AI detection:")
print("Command: pip install ultralytics")
print("=" * 60)

# Show image
cv2.imshow('PRAGYAN-NETRA Demo', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()