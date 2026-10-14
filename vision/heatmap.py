# dev/creator: sahil

import cv2
import numpy as np
from numpy import ndarray

from config import HEATMAP_ALPHA


def build_density_map(
    points_xy, frame_w: int, frame_h: int,
    downscale: int = 3, sigma: float = 16, point_boost: float = 3.0,
) -> ndarray:
    small_w = max(1, frame_w // downscale)
    small_h = max(1, frame_h // downscale)
    accum = np.zeros((small_h, small_w), dtype=np.float32)

    for x, y in points_xy:
        sx = int(np.clip(x / downscale, 0, small_w - 1))
        sy = int(np.clip(y / downscale, 0, small_h - 1))
        accum[sy, sx] += point_boost

    k = max(3, int(round(sigma / downscale * 3)) | 1)
    blurred: ndarray = cv2.GaussianBlur(accum, (k, k), sigmaX=sigma / downscale)

    if blurred.max() > 0:
        blurred = np.sqrt(blurred / blurred.max())

    full: ndarray = cv2.resize(blurred, (frame_w, frame_h), interpolation=cv2.INTER_LINEAR)
    return full


def overlay_heatmap(frame_bgr: ndarray, density_map: ndarray, alpha: float = 0.7) -> ndarray:
    heat_u8: ndarray = np.clip(density_map, 0, 1).astype(np.float32)
    heat_u8 = (heat_u8 * 255).astype(np.uint8)
    colormap = getattr(cv2, "COLORMAP_TURBO", cv2.COLORMAP_JET)
    heat_color: ndarray = cv2.applyColorMap(heat_u8, colormap)  # type: ignore[arg-type]

    mask = np.clip(density_map * 1.6, 0, 1).astype(np.float32)[..., None]
    blended = (
        frame_bgr.astype(np.float32) * (1 - alpha * mask)
        + heat_color.astype(np.float32) * (alpha * mask)
    )
    return np.clip(blended, 0, 255).astype(np.uint8)
