# =============================================================================
# --- MASTER ITEM DATABASE ---
# =============================================================================
# This is where we "hardcode" the definitions of all items
# in the game. The inventory will use this as a reference.
# =============================================================================

ITEM_DB = {
    
    "Lata_alubias": {
        "name": "Lata de Alubias",
        "image": "assets/items/Lata_alubias.png",
        "description": "Recupera 10 HP. Sabe a óxido y esperanza.",
        "on_use_effects": [
            {"type": "set_var", "name": "player_hp", "value": "+4"},
            {"type": "notify", "text": "Recuperaste 4 HP"}
            # Sound: {"sfx": "assets/audio/sfx/aa" }
        ]
    },

    "Medkit": {
        "name": "Botiquín Básico",
        "image": "assets/items/medkit.png",
        "description": "Recupera 50 HP. Huele a hospital.",
        "on_use_effects": [
            {"type": "set_var", "name": "player_hp", "value": "+50"},
            {"type": "notify", "text": "Recuperaste 50 HP"}
        ]
    }
}