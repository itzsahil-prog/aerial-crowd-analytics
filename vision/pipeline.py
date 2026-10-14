# dev/creator: sahil

from vision.heuristic_detector import estimate_crowd_points


def analyze_frame(frame_bgr, detector, tracker, simulator, conf_threshold,
                  use_real_detection, advance_simulation=True, roi=None,
                  target_count=None):

    # ── heuristic (content-aware) detection on real footage ──────────────────
    if use_real_detection and frame_bgr is not None:
        count = target_count or max(20, len(simulator.people))
        points = estimate_crowd_points(frame_bgr, target_count=count, roi=roi)

        if advance_simulation:
            tracked = tracker.update(points) if points else tracker.update([])
        else:
            tracked = dict(tracker.objects)

        obj_ids = list(tracked.keys())
        obj_pts = [tracked[i] for i in obj_ids]

        detections = []
        for (x, y) in points:
            half = 9
            matched_id = None
            for idx, pt in enumerate(obj_pts):
                if abs(pt[0] - x) < 1.0 and abs(pt[1] - y) < 1.0:
                    matched_id = obj_ids[idx]
                    break
            detections.append({
                "box": (x - half, y - half, x + half, y + half),
                "conf": 0.55, "cx": x, "cy": y,
                "track_id": matched_id,
            })

        detections = [d for d in detections if d["conf"] >= conf_threshold]
        return {"points": points, "detections": detections, "mode": "heuristic"}

    # ── synthetic simulation ─────────────────────────────────────────────────
    people = simulator.step() if advance_simulation else simulator.get_people()
    points = [(p["x"], p["y"]) for p in people]

    if advance_simulation:
        tracker.update(points)
    else:
        tracker.update([])

    detections = detector.synthetic_boxes_from_points(people)
    detections = [d for d in detections if d["conf"] >= conf_threshold]
    return {"points": points, "detections": detections, "mode": "synthetic"}
