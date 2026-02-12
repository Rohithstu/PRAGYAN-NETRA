"""
Test Vision Module
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import cv2
import numpy as np

def test_obstacle_detection():
    """Test basic obstacle detection"""
    print("🧪 Testing Obstacle Detection...")
    
    try:
        from vision.obstacle_detection import ObstacleDetector
        
        # Create test detector
        detector = ObstacleDetector()
        
        # Create test image
        test_img = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.rectangle(test_img, (100, 100), (200, 200), (255, 255, 255), -1)
        
        # Test detection
        detections = detector.detect(test_img)
        
        print(f"  ✅ Detections returned: {type(detections)}")
        print(f"  ✅ Number of detections: {len(detections)}")
        
        # Test drawing
        result = detector.draw_detections(test_img.copy(), detections)
        print(f"  ✅ Drawing function works: {result.shape}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def test_stair_detection():
    """Test stair detection"""
    print("🧪 Testing Stair Detection...")
    
    try:
        from vision.stair_detection import StairDetector
        
        detector = StairDetector()
        
        # Create test image with horizontal lines (simulating stairs)
        test_img = np.zeros((480, 640, 3), dtype=np.uint8)
        for i in range(5):
            y = 200 + i * 30
            cv2.line(test_img, (100, y), (500, y), (255, 255, 255), 3)
        
        result = detector.detect_stairs(test_img)
        
        print(f"  ✅ Result type: {type(result)}")
        print(f"  ✅ Keys: {list(result.keys())}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def test_surface_analysis():
    """Test surface analysis"""
    print("🧪 Testing Surface Analysis...")
    
    try:
        from vision.surface_analysis import SurfaceAnalyzer
        
        analyzer = SurfaceAnalyzer()
        
        # Create test image
        test_img = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        
        result = analyzer.analyze_surface(test_img)
        
        print(f"  ✅ Result type: {type(result)}")
        print(f"  ✅ Contains 'surface_type': {'surface_type' in result}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("VISION MODULE TESTS")
    print("=" * 60)
    
    results = []
    
    results.append(("Obstacle Detection", test_obstacle_detection()))
    results.append(("Stair Detection", test_stair_detection()))
    results.append(("Surface Analysis", test_surface_analysis()))
    
    print("\n" + "=" * 60)
    print("TEST RESULTS:")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if success:
            passed += 1
    
    print(f"\n📊 Total: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All vision tests passed successfully!")
    else:
        print("⚠️ Some tests failed. Check errors above.")