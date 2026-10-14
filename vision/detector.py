# dev/creator: sahil

from numpy import ndarray


class Detector:
    """Detector for crowd analysis - uses heuristic or synthetic modes only"""

    def __init__(self) -> None:
        self.mode = "heuristic"  # Always use heuristic for real footage

    @staticmethod
    def synthetic_boxes_from_points(people, box_size: int = 18) -> list:
        """Generate synthetic detection boxes from simulation points"""
        detections = []
        for p in people:
            x, y = p["x"], p["y"]
            half = box_size / 2
            conf = 0.72 + 0.25 * ((p["id"] % 7) / 7.0)
            detections.append({
                "box": (x - half, y - half, x + half, y + half),
                "conf": round(min(conf, 0.98), 2),
                "cx": x,
                "cy": y,
                "track_id": p["id"],
            })
        return detections
