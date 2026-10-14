# dev/creator: sahil
"""
simulation — synthetic aerial crowd simulation engine.

Modules
-------
crowd_simulator : physics-based agent simulator with cluster attraction,
                  velocity clamping, and boundary reflection.
                  Supports dynamic population resizing and deterministic
                  seeding for reproducible runs.
"""

from simulation.crowd_simulator import CrowdSimulator

__all__ = [
    "CrowdSimulator",
]
