SCENE = {
    "id": "ch5_frog_fight",
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
        # Define the enemy frog
        {
            "id": "frog", 
            "type": "frog", 
            "hp": 60, 
            "max_hp": 60,
            "sprite": "assets/characters/combat_frog1.png", # Sprite path
            "pos": [150, 100], # Position on screen
            "hp_bar_sprite": "assets/ui/battle/hp_frog.png", 
            "hp_bar_pos": [0, 20],
            "sprite_scale_factor": 5.0, # <--- ¡NUEVO! (Multiplica el tamaño por 6)
            "hp_bar_scale_factor": 5.0, 

            "skills": [
                {"type": "ATTACK", "dmg_min": 1, "dmg_max": 3, "text": "Bite",
                 "sfx": "assets/audio/sfx/frog.ogg",
                 "vfx": "assets/vfx/bite_effect.png",
                 "vfx": "assets/characters/combat_frog2.png",
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
        {"speaker":"Narrator","text":"¡Una rana gigante aparece!"}
    ],
    "post_battle_dialogue": [
        {"speaker":"Narrator","text":"¡Has derrotado a la rana, felicidades!"}
    ],
    "rewards_on_victory": {
        "effects": [
            {"type": "give_item", "item": "lengua_rana"},   #falta que se pueda poner en un inventario para poder usarlo
        ]
    },
      # --- NEXT SCENES ---
    "on_victory_target": "scenes.ch6_long_hallway_frog",
    "on_defeat_target": "scenes.ch6_frog_lose"
}