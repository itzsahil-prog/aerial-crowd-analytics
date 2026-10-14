# dev/creator: sahil
"""
export — video rendering and export utilities.

Modules
-------
video_generator : renders annotated demo MP4 clips from simulation or uploaded
                  footage; writes to outputs/ with automatic fallback to the
                  system temp directory on read-only filesystems (e.g. Streamlit Cloud).
"""

from export.video_generator import generate_demo_video

__all__ = [
    "generate_demo_video",
]
