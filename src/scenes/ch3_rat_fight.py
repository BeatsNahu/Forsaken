SCENE = {
    "id": "ch3_rat_fight",
    "class": "BattleManager",  # Tell the engine to use BattleManager for this scene
    "music": "assets/audio/music/battle_theme.ogg", "volume": 0.5,
    # --- SCENARY SETUP ---
    "static_layers": [
        {"image": "assets/ui/battle/base.png", "pos": [0, 0], "scale_to_screen": True},
        {"image": "assets/ui/battle/light.png", "pos": [0, 0], "scale_to_screen": True},
        {"image": "assets/ui/battle/enemy_floor.png", "pos": [0, 0], "scale_to_screen": True}
    ],

    # --- BATTLE SETUP ---
    "player": {
        # Define the player's skills for this battle
        "skills": [
            {"id": "punch", "text": "Puño", "type": "ATTACK", "dmg": 10, "cost": 2, "cost_type": "HP",
             "sfx": "assets/audio/sfx/punch_hit.ogg", 
             "vfx": "assets/vfx/punch_effect.png",
             "start_pos": [960, 540],
             "end_pos": [960, 540]
            },
            {"id": "kick", "text": "Patada", "type": "ATTACK", "dmg": 1, "cost": 0,
             "sfx": "assets/audio/sfx/kick_hit.ogg",
             "vfx": "assets/vfx/kick_effect.png",
             "start_pos": [960, 540],
             "end_pos": [960, 540]
            },
            {"id": "defend", "text": "Defensa", "type": "DEFEND"},
            {"id": "item", "text": "Item", "type": "ITEM_MENU"}
        ]
    },
    "enemies": [
        # Define the enemy rat
        {
            "id": "rat", 
            "type": "rat", 
            "hp": 10, 
            "max_hp": 10,
            "sprite": "assets/characters/rat_mutant.png", # Sprite path
            "pos": [600, 160], # Position on screen
            "sprite_scale_factor": 10.0,
            "hp_bar_sprite": "assets/ui/battle/hp_rat.png", 
            "hp_bar_pos": [0, 20],
            "hp_bar_scale_factor": 5.0, 

            "skills": [
                {"type": "ATTACK", "dmg_min": 1, "dmg_max": 3, "text": "Bite",
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
        {"speaker":"Narrator","text":"¡Una rata mutante aparece!"}
    ],
    "post_battle_dialogue": [
        {"speaker":"Narrator","text":"La rata cae. Encuentras comida."}
    ],

    "rewards_on_victory": {
        "effects": [
            # 1. El efecto LÓGICO (añade al inventario)
            {"type": "give_item", "item": "Lata_alubias"},
            
            # 2. El efecto de curación
            {"type": "set_var", "name": "player_hp", "value": "+10"},
            
            # --- ¡NUEVO EFECTO VISUAL! ---
            {
                "type": "show_item_overlay",
                "item_name": "Lata de Alubias",
                "item_image": "assets/items/bean_can.png"
            }
        ]
    },
    
    "on_victory_target": "scenes.ch4_knife_guy",
    "on_defeat_target": "scenes.ch4_rat_lose"
}