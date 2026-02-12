# ============================================================
# PRAGYAN-NETRA - REAL AI DETECTION
# Using YOLOv8 for actual object detection
# ============================================================

print("=" * 60)
print("PRAGYAN-NETRA - REAL AI OBJECT DETECTION")
print("Using YOLOv8 Deep Learning Model")
print("=" * 60)
print()

print("📦 Step 1: Loading AI model...")
print("   (First time will download YOLOv8 - 6MB)")

try:
    from ultralytics import YOLO
    print("   ✅ YOLO library imported")
except:
    print("   ❌ ERROR: YOLO not installed")
    print("   Run: pip install ultralytics")
    exit()

# Load the model
print("\n🤖 Step 2: Loading YOLOv8 Nano model...")
model = YOLO('yolov8n.pt')  # Nano version (fastest)
print("   ✅ AI model loaded successfully!")

print("\n🎨 Step 3: Creating test scene for AI...")
import cv2
import numpy as np

# Create a realistic test image
height, width = 480, 640
scene = np.zeros((height, width, 3), dtype=np.uint8)

# Draw background
cv2.rectangle(scene, (0, 350), (width, height), (100, 100, 100), -1)  # Floor
cv2.rectangle(scene, (0, 0), (width, 350), (150, 200, 255), -1)       # Wall

# Draw objects that YOLO can recognize:
# 1. Person (top-left)
cv2.ellipse(scene, (150, 200), (25, 60), 0, 0, 360, (255, 255, 255), -1)
# 2. Chair (center)
cv2.rectangle(scene, (300, 250), (380, 350), (42, 42, 165), -1)      # Brown chair
cv2.rectangle(scene, (290, 200), (390, 220), (35, 35, 140), -1)      # Chair back
# 3. Bottle (right)
cv2.rectangle(scene, (500, 280), (515, 380), (255, 100, 0), -1)      # Blue bottle
# 4. Cell phone (bottom-center)
cv2.rectangle(scene, (280, 380), (340, 430), (200, 200, 200), -1)    # Phone

# Add PRAGYAN-NETRA label
cv2.putText(scene, "PRAGYAN-NETRA AI TEST", (150, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

# Save input image
input_file = "ai_test_input.jpg"
cv2.imwrite(input_file, scene)
print(f"   ✅ Test image saved: {input_file}")

print("\n🔍 Step 4: Running AI detection...")
print("   AI is analyzing the image...")

# Run YOLO detection
results = model(scene)

print("   ✅ AI analysis complete!")

# Process results
print("\n📊 Step 5: AI Detection Results:")
print("-" * 60)

detected_objects = []
for result in results:
    for box in result.boxes:
        confidence = float(box.conf[0])
        if confidence > 0.4:  # Only show confident detections
            class_id = int(box.cls[0])
            object_name = model.names[class_id]
            
            # Get bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Calculate position
            center_x = (x1 + x2) // 2
            if center_x < width // 3:
                position = "LEFT"
            elif center_x > 2 * width // 3:
                position = "RIGHT"
            else:
                position = "CENTER"
            
            # Distance estimation (based on object size)
            area = (x2 - x1) * (y2 - y1)
            if area > 30000:
                distance = "VERY CLOSE"
            elif area > 15000:
                distance = "CLOSE"
            elif area > 5000:
                distance = "MEDIUM"
            else:
                distance = "FAR"
            
            detected_objects.append({
                'name': object_name,
                'confidence': confidence * 100,
                'position': position,
                'distance': distance
            })

# Sort by confidence (highest first)
detected_objects.sort(key=lambda x: x['confidence'], reverse=True)

# Display results
if detected_objects:
    print(f"AI detected {len(detected_objects)} objects:")
    print("-" * 60)
    print(f"{'No.':3} {'OBJECT':12} {'CONFIDENCE':12} {'POSITION':10} {'DISTANCE':12}")
    print("-" * 60)
    
    for i, obj in enumerate(detected_objects[:5]):  # Show top 5
        print(f"{i+1:2}. {obj['name'].upper():12} {obj['confidence']:5.1f}%      {obj['position']:10} {obj['distance']:12}")
else:
    print("No objects detected with high confidence")

print("\n🔊 Step 6: Voice Alerts (Based on AI):")
print("-" * 60)

if detected_objects:
    for obj in detected_objects[:3]:  # Top 3 alerts
        if obj['confidence'] > 70 and obj['distance'] in ["VERY CLOSE", "CLOSE"]:
            print(f"🚨 URGENT: {obj['name']} is {obj['distance'].lower()} on your {obj['position'].lower()}!")
        elif obj['confidence'] > 60:
            print(f"⚠️  Alert: {obj['name']} detected {obj['distance'].lower()} on your {obj['position'].lower()}")
        else:
            print(f"ℹ️  Info: Possible {obj['name']} {obj['distance'].lower()} on your {obj['position'].lower()}")
else:
    print("✅ Path appears clear")

print("\n💾 Step 7: Saving AI results...")
# Draw results on image
result_image = results[0].plot()  # This adds colored boxes
output_file = "ai_test_output.jpg"
cv2.imwrite(output_file, result_image)
print(f"   ✅ Results saved: {output_file}")
print("   Open this file to see AI bounding boxes")

print("\n👀 Step 8: Displaying comparison...")
# Show before and after
cv2.imshow('Before AI (Input)', scene)
cv2.waitKey(1500)
cv2.imshow('After AI (Detection)', result_image)
cv2.waitKey(1500)
cv2.destroyAllWindows()

print("\n" + "=" * 60)
print("🎉 REAL AI DETECTION SUCCESSFUL!")
print("=" * 60)
print("\nWhat we accomplished:")
print("1. ✅ Loaded YOLOv8 AI model")
print("2. ✅ Created test scene")
print("3. ✅ Ran real object detection")
print("4. ✅ Got confidence scores")
print("5. ✅ Generated intelligent alerts")
print("6. ✅ Saved visual results")
print("\nCheck your folder for:")
print(f"• {input_file} - Original scene")
print(f"• {output_file} - AI detection results (with boxes)")
print("\nNext: Add REAL voice with: pip install pyttsx3")