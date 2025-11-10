SCENE = {
    "id": "btl_01_knifeguy",
    "class": "BattleManager",
    "music": "assets/sounds/battle_theme.ogg",

    # --- ESCENARIO ---
    "static_layers": [
        {"image": "assets/layers_battle/base.png", "pos": [0, 0], "scale_to_screen": True},
        {"image": "assets/layers_battle/light.png", "pos": [600, 50]},
        {"image": "assets/layers_battle/enemy_floor.png", "pos": [1350, 600]}
    ],

    # --- BATTLE SETUP ---
    "player": {
        "skills": [
            {"id": "punch", "text": "Puño", "type": "ATTACK", "dmg": 5, "cost": 1, "sfx": "assets/sounds/punch_hit.ogg"},
            {"id": "kick", "text": "Patada", "type": "ATTACK", "dmg": 2, "cost": 0},
            {"id": "defend", "text": "Defensa", "type": "DEFEND"},
            {"id": "item", "text": "Item", "type": "ITEM_MENU"}
        ]
    },

    "enemies": [
        {
            "id": "pivecuchillo",
            "type": "knifeguy",
            "hp": 12,
            "max_hp": 12,
            "sprite": "assets/characters/knife_guy.png",        # ruta del sprite
            "pos": [700, 400],                                 # posición en pantalla
            "hp_bar_sprite": "assets/layers_battle/hp_knifeguy.png",
            "hp_bar_pos": [700, 200],
            "sprite_scale_factor": 1.0,
            "hp_bar_scale_factor": 1.0,
            "skills": [
                {"type": "ATTACK", "dmg_min": 2, "dmg_max": 5, "text": "Knife Slash"}
            ]
        }
    ],

    # --- RULES ---
    "rules": {
        "turn_order": "player_first",
        "win_condition": "all_enemies_dead",
        "lose_condition": "player_dead"
    },

    # --- DIALOGUE ---
    "pre_battle_dialogue": [
        {"speaker": "Narrator", "text": "Te enfrentas al temido Knife Guy."}
    ],

    # --- REWARDS ---
    "rewards_on_victory": {
        "effects": [
            {"type": "give_item", "item": "frag_B"}
        ]
    },

    "on_victory_target": "scripts.ch7_salir",
    "on_defeat_target": "scripts.ch5_finaltortura"
}