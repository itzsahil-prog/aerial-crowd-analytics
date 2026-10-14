#!/usr/bin/env python3
"""
Comprehensive feature test for AerialSense
Tests all modules, imports, and key functions
"""

import sys
import traceback
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def test_imports():
    """Test all module imports"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Module Imports{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    modules = [
        'config',
        'simulation.crowd_simulator',
        'vision.detector',
        'vision.tracker',
        'vision.pipeline',
        'vision.crowd_analytics',
        'vision.heatmap',
        'vision.video_processor',
        'visualization.bird_eye_view',
        'visualization.crowd_3d',
        'export.video_generator',
    ]
    
    passed = 0
    failed = 0
    
    for module in modules:
        try:
            __import__(module)
            print(f"{GREEN}✓{RESET} {module}")
            passed += 1
        except Exception as e:
            print(f"{RED}✗{RESET} {module}: {e}")
            failed += 1
    
    print(f"\n{YELLOW}Import Results: {passed} passed, {failed} failed{RESET}\n")
    return failed == 0


def test_config():
    """Test configuration"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Configuration{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    import config
    
    required_attrs = [
        'DEFAULT_FRAME_WIDTH', 'DEFAULT_FRAME_HEIGHT', 'THEME',
        'SIM_DEFAULTS', 'DENSITY_THRESHOLDS'
    ]
    
    passed = 0
    failed = 0
    
    for attr in required_attrs:
        if hasattr(config, attr):
            value = getattr(config, attr)
            print(f"{GREEN}✓{RESET} {attr} = {value if not isinstance(value, dict) else '{...}'}")
            passed += 1
        else:
            print(f"{RED}✗{RESET} Missing: {attr}")
            failed += 1
    
    print(f"\n{YELLOW}Config Results: {passed} passed, {failed} failed{RESET}\n")
    return failed == 0


def test_simulation():
    """Test crowd simulation"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Crowd Simulation{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    from simulation.crowd_simulator import CrowdSimulator
    
    try:
        sim = CrowdSimulator(width=1280, height=720, num_people=50)
        print(f"{GREEN}✓{RESET} CrowdSimulator initialized")
        
        people = sim.step()
        print(f"{GREEN}✓{RESET} Simulation step executed")
        
        positions = sim.get_people()
        print(f"{GREEN}✓{RESET} Got {len(positions)} positions")
        
        sim.set_population(100)
        print(f"{GREEN}✓{RESET} Population updated to 100")
        
        sim.reset()
        print(f"{GREEN}✓{RESET} Simulation reset")
        
        print(f"\n{YELLOW}Simulation: All tests passed{RESET}\n")
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Simulation failed: {e}")
        traceback.print_exc()
        return False


def test_detection():
    """Test detection and tracking"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Detection & Tracking{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    import numpy as np
    from vision.detector import Detector
    from vision.tracker import CentroidTracker
    
    try:
        detector = Detector()
        print(f"{GREEN}✓{RESET} Detector initialized (mode: {detector.mode})")
        
        tracker = CentroidTracker(max_disappeared=10, max_distance=50)
        print(f"{GREEN}✓{RESET} CentroidTracker initialized")
        
        # Test synthetic detection
        if detector.mode == "heuristic":
            print(f"{GREEN}✓{RESET} Detector ready (heuristic mode)")
        else:
            print(f"{GREEN}✓{RESET} Detector in synthetic mode")
        
        objects = tracker.update([])
        print(f"{GREEN}✓{RESET} Tracker updated: {len(objects)} tracked")
        
        print(f"\n{YELLOW}Detection & Tracking: All tests passed{RESET}\n")
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Detection/Tracking failed: {e}")
        traceback.print_exc()
        return False


def test_analytics():
    """Test crowd analytics functions"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Crowd Analytics{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    from vision.crowd_analytics import (
        filter_in_roi, compute_density, average_speed,
        flow_direction, high_density_cells
    )
    from vision.tracker import CentroidTracker
    
    try:
        # Test ROI filtering
        points = [(100, 100), (200, 200), (1000, 600)]
        roi = (50, 50, 500, 500)
        filtered = filter_in_roi(points, roi)
        print(f"{GREEN}✓{RESET} filter_in_roi: {len(filtered)} in ROI")
        
        # Test density computation
        density, label, color = compute_density(len(filtered), roi, 1280, 720)
        print(f"{GREEN}✓{RESET} compute_density: {density:.2f} ({label})")
        
        # Test tracker-based metrics
        tracker = CentroidTracker()
        speed = average_speed(tracker, [])
        print(f"{GREEN}✓{RESET} average_speed: {speed:.2f}")
        
        angle, mag = flow_direction(tracker, [])
        print(f"{GREEN}✓{RESET} flow_direction: {angle:.1f}° mag={mag:.2f}")
        
        # Test hotspot detection
        cells = high_density_cells(points, 1280, 720)
        print(f"{GREEN}✓{RESET} high_density_cells: {len(cells)} hotspots")
        
        print(f"\n{YELLOW}Analytics: All tests passed{RESET}\n")
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Analytics failed: {e}")
        traceback.print_exc()
        return False


def test_visualizations():
    """Test visualization functions"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Visualizations{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    from visualization.bird_eye_view import build_bird_eye_figure
    from visualization.crowd_3d import build_3d_density_figure
    
    try:
        points = [(100, 100), (200, 200), (300, 300)]
        w, h = 1280, 720
        
        # Test bird's eye view
        bev_fig = build_bird_eye_figure(points, w, h)
        print(f"{GREEN}✓{RESET} Bird's-eye view figure created")
        
        # Test 3D surface mode
        fig3d_surface = build_3d_density_figure(points, w, h, mode="surface")
        print(f"{GREEN}✓{RESET} 3D density (surface mode) created")
        
        # Test 3D points mode
        fig3d_points = build_3d_density_figure(points, w, h, mode="points")
        print(f"{GREEN}✓{RESET} 3D density (points mode) created")
        
        # Test empty data handling
        fig3d_empty_surface = build_3d_density_figure([], w, h, mode="surface")
        print(f"{GREEN}✓{RESET} 3D density (empty, surface) handled correctly")
        
        fig3d_empty_points = build_3d_density_figure([], w, h, mode="points")
        print(f"{GREEN}✓{RESET} 3D density (empty, points) handled correctly")
        
        print(f"\n{YELLOW}Visualizations: All tests passed{RESET}\n")
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Visualizations failed: {e}")
        traceback.print_exc()
        return False


def test_pipeline():
    """Test complete pipeline"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing Complete Pipeline{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    import numpy as np
    from vision.pipeline import analyze_frame
    from vision.detector import Detector
    from vision.tracker import CentroidTracker
    from simulation.crowd_simulator import CrowdSimulator
    
    try:
        detector = Detector()
        tracker = CentroidTracker()
        simulator = CrowdSimulator(width=1280, height=720, num_people=50)
        
        dummy_frame = np.zeros((720, 1280, 3), dtype=np.uint8)
        roi = (100, 100, 1000, 600)
        
        # Test with simulation
        result = analyze_frame(
            frame_bgr=dummy_frame,
            detector=detector,
            tracker=tracker,
            simulator=simulator,
            conf_threshold=0.5,
            use_real_detection=False,
            advance_simulation=True,
            roi=roi,
            target_count=50
        )
        
        print(f"{GREEN}✓{RESET} Pipeline executed successfully")
        print(f"  - Mode: {result['mode']}")
        print(f"  - Points: {len(result['points'])}")
        print(f"  - Detections: {len(result['detections'])}")
        
        print(f"\n{YELLOW}Pipeline: All tests passed{RESET}\n")
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Pipeline failed: {e}")
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all tests"""
    print(f"\n{BLUE}{'#'*60}{RESET}")
    print(f"{BLUE}# AerialSense — Comprehensive Feature Test{RESET}")
    print(f"{BLUE}{'#'*60}{RESET}")
    
    results = {
        'Imports': test_imports(),
        'Configuration': test_config(),
        'Simulation': test_simulation(),
        'Detection & Tracking': test_detection(),
        'Analytics': test_analytics(),
        'Visualizations': test_visualizations(),
        'Pipeline': test_pipeline(),
    }
    
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Final Results{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = f"{GREEN}✓ PASSED{RESET}" if result else f"{RED}✗ FAILED{RESET}"
        print(f"{test_name:.<40} {status}")
    
    print(f"\n{YELLOW}{'='*60}{RESET}")
    if passed == total:
        print(f"{GREEN}All {total} test suites passed! ✓{RESET}")
        print(f"{YELLOW}{'='*60}{RESET}\n")
        return 0
    else:
        print(f"{RED}{passed}/{total} test suites passed{RESET}")
        print(f"{YELLOW}{'='*60}{RESET}\n")
        return 1


if __name__ == '__main__':
    sys.exit(run_all_tests())
