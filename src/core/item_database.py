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
            {"type": "set_var", "name": "player_hp", "value": "+10"},
            {"type": "notify", "text": "Recuperaste 10 HP"}
            # Sound: {"sfx": "assets/audio/sfx/aa" }
        ]
    },

    "Medkit": {
        "name": "Pastillas Basicas",
        "image": "assets/items/pastillas.png",
        "description": "Recupera 50 HP. Huele a hospital.",
        "on_use_effects": [
            {"type": "set_var", "name": "player_hp", "value": "+50"},
            {"type": "notify", "text": "Recuperaste 50 HP"}
        ]
    },

    "Metal_bar": {
        "name": "Barra de Metal",
        "image": "assets/items/tubooxidado.png",
        "description": "Daño permanente +5. Es un poco tosco de usar",
        "on_use_effects": [
            {"type": "set_var", "name": "player_base_damage", "value": "+5"},
            {"type": "notify", "text": "daño +5"}
        ]
    },
    "fork": {
        "name": "Tenedor Oxidado",
        "image": "assets/items/fork.png",
        "description": "Daño permanente +4. Es un poco pintiagudo",
        "on_use_effects": [
            {"type": "set_var", "name": "player_base_damage", "value": "+4"},
            {"type": "notify", "text": "daño +4"}
        ]
    },
}