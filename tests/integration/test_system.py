"""
Integration Test - Full System
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

def test_system_integration():
    """Test that all modules work together"""
    print("🧪 Testing System Integration...")
    
    modules_loaded = []
    
    try:
        from app.main import PragyanNetra
        modules_loaded.append("Main Application")
        print("  ✅ Main application imports successfully")
    except Exception as e:
        print(f"  ❌ Main app import failed: {e}")
    
    try:
        from vision.obstacle_detection import ObstacleDetector
        modules_loaded.append("Vision Module")
        print("  ✅ Vision module imports successfully")
    except Exception as e:
        print(f"  ❌ Vision import failed: {e}")
    
    try:
        from memory.face_recognition import FaceMemory
        modules_loaded.append("Memory Module")
        print("  ✅ Memory module imports successfully")
    except Exception as e:
        print(f"  ❌ Memory import failed: {e}")
    
    try:
        from voice.tts import VoiceAssistant
        modules_loaded.append("Voice Module")
        print("  ✅ Voice module imports successfully")
    except Exception as e:
        print(f"  ❌ Voice import failed: {e}")
    
    try:
        from navigation.path_guidance import PathGuide
        modules_loaded.append("Navigation Module")
        print("  ✅ Navigation module imports successfully")
    except Exception as e:
        print(f"  ❌ Navigation import failed: {e}")
    
    print(f"\n📦 Modules loaded: {len(modules_loaded)}/5")
    
    if len(modules_loaded) == 5:
        print("🎉 All modules integrate successfully!")
        return True
    else:
        print("⚠️ Some modules failed to load")
        return False

def test_data_flow():
    """Test data flow between modules"""
    print("\n🧪 Testing Data Flow...")
    
    try:
        # Simulate data flow
        import numpy as np
        
        # Create mock data
        mock_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        mock_detections = [
            {"type": "chair", "position": "LEFT", "confidence": 0.8},
            {"type": "table", "position": "CENTER", "confidence": 0.7}
        ]
        
        print("  ✅ Mock data created")
        
        # Test voice integration
        from voice.tts import VoiceAssistant
        voice = VoiceAssistant()
        voice.speak("Data flow test", "info")
        print("  ✅ Voice system responds")
        
        # Test navigation integration
        from navigation.path_guidance import PathGuide
        guide = PathGuide()
        path = guide.plan_path("START", "END", mock_detections)
        print(f"  ✅ Navigation path planned: {len(path)} steps")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Data flow error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("SYSTEM INTEGRATION TESTS")
    print("=" * 60)
    
    integration_ok = test_system_integration()
    data_flow_ok = test_data_flow()
    
    print("\n" + "=" * 60)
    print("FINAL RESULTS:")
    print("=" * 60)
    
    if integration_ok and data_flow_ok:
        print("🎉 SYSTEM INTEGRATION SUCCESSFUL!")
        print("All modules work together correctly.")
    else:
        print("⚠️ Integration issues detected.")
        print("Check module imports and dependencies.")
    
    print("\nNext: Run the system with 'python run.py'")