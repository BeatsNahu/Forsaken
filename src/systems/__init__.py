"""Systems package for Forsaken game.

Makes `src/systems` an explicit package so imports like
`from systems.ui_manager import DialogueBox` work reliably.
"""

__all__ = ["animation_manager", "battle_manager", "transition_manager", "ui_manager"]
