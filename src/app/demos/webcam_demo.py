# ================================================
# PRAGYAN-NETRA - WEBCAM + AI + VOICE DEMO
# Real-time detection with voice alerts
# ================================================

print("=" * 60)
print("PRAGYAN-NETRA - REAL-TIME DETECTION")
print("Webcam + AI + Voice Integration")
print("=" * 60)

import cv2
import time
import pyttsx3

print("\n📦 Loading modules...")

# Initialize voice
engine = pyttsx3.init()
engine.setProperty('rate', 160)
print("✅ Voice engine ready")

# Initialize webcam
print("\n📷 Initializing webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ ERROR: Cannot open webcam")
    print("1. Check if webcam is connected")
    print("2. Close other apps using camera")
    exit()

print("✅ Webcam ready")

print("\n" + "=" * 60)
print("INSTRUCTIONS:")
print("1. Show objects to the camera")
print("2. System will detect and announce")
print("3. Press 'q' to quit")
print("4. Press 'v' to test voice")
print("=" * 60)

# Voice welcome
engine.say("Pragyan Netra real time detection activated")
engine.say("Show objects to the camera")
engine.runAndWait()

last_alert_time = 0
alert_cooldown = 3  # seconds

while True:
    # Capture frame
    ret, frame = cap.read()
    if not ret:
        print("❌ Cannot read from webcam")
        break
    
    # Display frame
    cv2.putText(frame, "PRAGYAN-NETRA - Real Time", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Press 'q' to quit | 'v' for voice test", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    
    # Show instructions on screen
    cv2.putText(frame, "Show: Person, Chair, Bottle, Phone", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    # Display the frame
    cv2.imshow('PRAGYAN-NETRA - Real Time Detection', frame)
    
    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        print("\n🛑 Stopping detection...")
        break
        
    elif key == ord('v'):
        print("\n🔊 Testing voice...")
        engine.say("Voice test. System is working")
        engine.runAndWait()
        
    elif key == ord('s'):
        # Take screenshot
        filename = f"screenshot_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Screenshot saved: {filename}")
        engine.say("Screenshot captured")
        engine.runAndWait()
    
    # Simulate detection every 5 seconds (for demo)
    current_time = time.time()
    if current_time - last_alert_time > alert_cooldown:
        # In real version, we would run YOLO here
        # For demo, we'll simulate based on what might be shown
        
        # Get some image properties for simulation
        height, width = frame.shape[:2]
        center_x = width // 2
        
        # Simple simulation based on brightness in different areas
        left_region = frame[height//2:, :width//3]
        center_region = frame[height//2:, width//3:2*width//3]
        right_region = frame[height//2:, 2*width//3:]
        
        left_brightness = left_region.mean()
        center_brightness = center_region.mean()
        right_brightness = right_region.mean()
        
        # Determine which side has most "obstacle" (dark area)
        if left_brightness < 100:
            alert = "Object detected on left side"
            print(f"⚠️  {alert}")
            engine.say(alert)
            engine.runAndWait()
            last_alert_time = current_time
        elif center_brightness < 100:
            alert = "Object detected ahead"
            print(f"⚠️  {alert}")
            engine.say(alert)
            engine.runAndWait()
            last_alert_time = current_time
        elif right_brightness < 100:
            alert = "Object detected on right side"
            print(f"⚠️  {alert}")
            engine.say(alert)
            engine.runAndWait()
            last_alert_time = current_time

# Cleanup
print("\n🔄 Releasing resources...")
cap.release()
cv2.destroyAllWindows()

# Goodbye message
engine.say("Pragyan Netra system shutting down")
engine.runAndWait()

print("\n" + "=" * 60)
print("DEMO COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("\nYou experienced:")
print("✅ Real-time webcam feed")
print("✅ Voice alerts and instructions")
print("✅ Object detection simulation")
print("✅ Interactive controls")
print("\nNext: Add real YOLO detection to this!")