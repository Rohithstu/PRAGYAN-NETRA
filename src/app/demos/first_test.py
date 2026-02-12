# ============================================================================
# PRAGYAN-NETRA - FIRST TEST
# Team Sparkerz: Subhiksha, Jenisha, Kaviyasri, Sumithra
# ============================================================================

print("╔═══════════════════════════════════════════════════════╗")
print("║          PRAGYAN-NETRA - AI Vision System            ║")
print("║         For Visually Impaired Assistance             ║")
print("╚═══════════════════════════════════════════════════════╝")
print()
print("📋 Checking system requirements...")

# Test 1: Check Python
import sys
print(f"✅ Python version: {sys.version[:7]}")

# Test 2: Check OpenCV
try:
    import cv2
    print(f"✅ OpenCV installed: {cv2.__version__}")
except:
    print("❌ OpenCV not installed. Run: pip install opencv-python")

# Test 3: Check NumPy
try:
    import numpy as np
    print(f"✅ NumPy installed: {np.__version__}")
except:
    print("❌ NumPy not installed. Run: pip install numpy")

# Test 4: Create a simple test image
print("\n🎨 Creating test image...")
img = np.zeros((300, 500, 3), dtype=np.uint8)  # Black image

# Add PRAGYAN-NETRA logo
cv2.putText(img, "PRAGYAN", (50, 100), 
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
cv2.putText(img, "NETRA", (180, 150), 
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)
cv2.putText(img, "Team Sparkerz", (100, 220), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# Draw some obstacles (simulation)
cv2.rectangle(img, (350, 50), (450, 150), (255, 0, 0), -1)  # Blue box
cv2.circle(img, (100, 250), 30, (0, 0, 255), -1)  # Red circle

# Save the image
cv2.imwrite("pragyan_welcome.jpg", img)
print("📸 Image saved: pragyan_welcome.jpg")

print("\n" + "="*50)
print("✅ ALL TESTS PASSED!")
print("="*50)
print("\n🎯 Next: Run obstacle detection demo")
print("   Command: python demo_obstacle.py")