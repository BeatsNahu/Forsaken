SCENE = {
    "id": "ch5_knife_fight",
    "class": "BattleManager",  # Tell the engine to use BattleManager for this scene
    "music": "assets/audio/music/battle_theme.ogg",

    # --- SCENARY SETUP ---
    "static_layers": [
        {"image": "assets/ui/battle/base.png", "pos": [0, 0], "scale_to_screen": True},
        {"image": "assets/ui/battle/light.png", "pos": [0, 0], "scale_to_screen": True},
        {"image": "assets/ui/battle/enemy_floor.png", "pos": [0, 0], "scale_to_screen": True},
    ],

    # --- BATTLE SETUP ---
    "player": {
        # Define the player's skills for this battle
        "skills": [
            {"id": "punch", "text": "Puño", "type": "ATTACK", "dmg": 5, "cost": 1, "cost_type": "HP"},
            {"id": "kick", "text": "Patada", "type": "ATTACK", "dmg": 2, "cost": 0},
            {"id": "defend", "text": "Defensa", "type": "DEFEND"},
            {"id": "item", "text": "Item", "type": "ITEM_MENU"}
        ]
    },
    "enemies": [
        # Define the enemy knife guy
        {
            "id": "knife_guy", 
            "type": "knife_guy", 
            "hp": 73, 
            "max_hp": 73,
            "sprite": "assets/characters/knife_guy.png", # Sprite path
            "pos": [640, 100], # Position on screen
            "hp_bar_sprite": "assets/layers_battle/hp_frog.png", 
            "hp_bar_pos": [360, 100],
            "sprite_scale_factor": 7.0, # <--- ¡NUEVO! (Multiplica el tamaño por 6)
            "hp_bar_scale_factor": 5.0, 

            "skills": [
                {"type": "ATTACK", "dmg_min": 2, "dmg_max": 4, "text": "Bite",
                 "sfx": "assets/audio/sfx/rat.ogg",
                 "vfx": "assets/vfx/bite_effect.png",
                 }
            ]
        }
    ],

    # --- RULES ---
    "rules": {
        "turn_order": "player_first", # "player_first", "enemy_first", "speed"
        "win_condition": "all_enemies_dead",
        "lose_condition": "player_dead"
    },
    
    # --- DIALOGUE ---
    "pre_battle_dialogue": [
        {"speaker":"Narrator","text":"¡Acaba de aparecer el Sr. Cuchillos!"}
    ],
    "post_battle_dialogue": [
        {"speaker":"Narrator","text":"Has perdi... HAS GANADO?!"},
        {"speaker":"Narrator","text":"Felicidades!!!"},

    ],

      # --- NEXT SCENES ---
    "on_victory_target": "scenes.ch6_long_hallway_knife",
    "on_defeat_target": "scenes.ch6_knife_lose"
}