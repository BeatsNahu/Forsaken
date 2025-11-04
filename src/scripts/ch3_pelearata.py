SCENE = {
    "id": "ch3_pelearata",
    "class": "BattleManager",  # Tell the engine to use BattleManager for this scene
    
    # --- ASSETS ---
    "background": "assets/backgrounds/Battle_scenary.png",
    "music": "assets/Sounds/battle_theme.ogg",

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
        # Define the enemy rat
        {
            "id": "rat", 
            "type": "rat", 
            "hp": 10, 
            "max_hp": 10,
            "sprite": "sprites/rat_mutant.png", # Sprite path
            "pos": [1400, 300],
            "skills": [
                {"type": "ATTACK", "dmg_min": 1, "dmg_max": 3, "text": "Bite"}
            ]
        }
        # Podrías añadir otra rata aquí
        # { "id": "rata_2", "type": "rat", "hp": 8, ... }
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

    # --- REWARDS AND NEXT SCENES ---
    "rewards_on_victory": {
        "effects": [
            {"type": "give_item", "item": "Lata_alubias"},
            {"type": "set_var", "name": "player_hp", "value": "+10"} # IDEAL: Heal player by 10 HP
        ]
    },
    
    "on_victory_target": "scripts.ch4_pivecuchillo",
    "on_defeat_target": "scripts.ch4_ratatecome"
}