# dev/creator: sahil
"""
vision — computer vision pipeline for aerial crowd analytics.

Modules
-------
detector          : YOLO-based person detector with synthetic fallback
tracker           : centroid-based multi-object tracker with trail history
pipeline          : unified frame-analysis entry point (real / heuristic / synthetic)
crowd_analytics   : ROI filtering, density scoring, speed & flow metrics, hotspot detection
heatmap           : density map builder and OpenCV heatmap overlay
heuristic_detector: content-aware crowd-point estimator (no model required)
video_processor   : frame drawing utilities — canvas, boxes, heatmap overlay, HUD, glow markers
"""

from vision.detector import Detector
from vision.tracker import CentroidTracker
from vision.pipeline import analyze_frame
from vision.crowd_analytics import (
    filter_in_roi,
    compute_density,
    average_speed,
    flow_direction,
    high_density_cells,
)
from vision.heatmap import build_density_map, overlay_heatmap
from vision.heuristic_detector import estimate_crowd_points
from vision.video_processor import (
    make_blank_aerial_canvas,
    draw_detections,
    apply_heatmap_overlay,
    draw_glow_markers,
    draw_hud,
    composite_bird_eye_inset,
)

__all__ = [
    "Detector",
    "CentroidTracker",
    "analyze_frame",
    "filter_in_roi",
    "compute_density",
    "average_speed",
    "flow_direction",
    "high_density_cells",
    "build_density_map",
    "overlay_heatmap",
    "estimate_crowd_points",
    "make_blank_aerial_canvas",
    "draw_detections",
    "apply_heatmap_overlay",
    "draw_glow_markers",
    "draw_hud",
    "composite_bird_eye_inset",
]
