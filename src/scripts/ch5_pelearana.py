SCENE = {
    "id": "btl_01_frog",
    "class": "BattleManager",
    "music": "assets/sounds/battle_theme.ogg",

    # --- ESCENARIO ---
    "static_layers": [
        {"image": "assets/layers_battle/base.png", "pos": [0, 0], "scale_to_screen": True}
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
            "id": "frog",
            "type": "frog",
            "hp": 11,
            "max_hp": 11,
            "sprite": "assets/characters/frog.png",
            "pos": [700, 400],
            "hp_bar_sprite": "assets/layers_battle/hp_frog.png",
            "hp_bar_pos": [700, 200],
            "sprite_scale_factor": 1.0,
            "hp_bar_scale_factor": 1.0,
            "skills": [
                {"type": "ATTACK", "dmg_min": 1, "dmg_max": 3, "text": "Salto"}
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
        {"speaker": "Narrator", "text": "La rana se enfada y te ataca."}
    ],

    # --- REWARDS ---
    "rewards_on_victory": {
        "effects": [
            {"type": "give_item", "item": "frag_B"}
        ]
    },

    "on_victory_target": "scripts.ch6_mcwin",
    "on_defeat_target": "scripts.ch6_crias"
}
