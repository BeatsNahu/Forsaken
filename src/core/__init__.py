"""Core package for Forsaken game.

This file makes `src/core` an explicit Python package so imports like
`from core.engine import Engine` work reliably when running from the
project root or other working directories.
"""

__all__ = ["engine", "scene", "scene_manager"]
