SCENE = {
  "start_battle": {
    "battle_id": "btl_01_bandits",  	# id único
    "background": "assets.backgrounds.Jail.png",
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
    "on_victory_target": "scrips.ch4_pivecuchillo",
    "on_defeat_target": "scrips.ch4_ratatecome",
    "post_battle_dialogue": [        	# si hay diálogo previo, opcional
  	  {"speaker":"Narrator","text":"Después de tu pelea, te acercas a la pila de latas y encuentras comida."},
  	  {"speaker":"Narrator","text":"La vida aumenta +x."}
    ]
  }
}