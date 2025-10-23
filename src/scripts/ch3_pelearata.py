<<<<<<< HEAD
SCENE = {
    "id": "ch3_pelearata",
<<<<<<< HEAD
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
=======
    "title": "Chapter 0: The Beginning",
    "background": "assets.backgrounds.Jail.png",
    "lines": [
        {"speaker": "Narrator", "text": "Te acercas y ves en la esquina varias latas de comida, pero al acercarte aparece una rata mutante."},
    ]
    "start_battle": {
        "background": "assets.backgrounds.Jail.png",
        "player":{
            "initiaol_hp": null
        },
        "enemies": {
            
        }
    }
>>>>>>> f65941e (refactor: remove unused chapter scripts to streamline the project)
}
=======
"start_battle": {
  "battle_id": "btl_01_rat",  	# id único
  "background": "assets.backgrounds.Jail.png",
  "arena": {
  	"width_ratio": 0.9,         	# parámetros visuales si quieres
  	"height_ratio": 0.5
  },
  "player": {                     	# parámetros opcionales de apoyo
  	"party": ["hero","companion"],
  	"initial_hp": null          	# null = usar stats actuales del engine
  },
  "enemies": [
  	{"id":"bandit_1","type":"rat","level":3,"hp":120,"pose":"idle"}
  ],
  "rules": {                      	# reglas del encuentro (gran ayuda para data-driven)
  	"turn_order": "speed",      	# "speed", "player_first", "round_robin"
  	"win_condition": "all_enemies_dead",
  	"lose_condition": "party_dead"
  },
  "pre_battle_dialogue": [        	# si hay diálogo previo, opcional
  	{"speaker":"Hero","text":"Te acercas y ves en la esquina varias latas de comida, pero al acercarte aparece una rata mutante."}
  ],
  "rewards": {                    	# aplicarse al ganar
  	"add_fragments": ["frag_B"]
  },
  "on_victory_target": "scrips.after_battle_scene",
  "on_defeat_target": "scrips.game_over",
}



>>>>>>> abdd92e (feat: implement battle scene structure and enhance enemy interactions)
