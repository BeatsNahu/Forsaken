SCENE = {
    "id": "example_battle",
    "class": "BattleManager",
    "music": "assets/audio/music/battle_theme.ogg",

    "static_layers": [
        {"image": "assets/layers_battle/base.png", "pos": [0, 0], "scale_to_screen": True}
    ],

    "player": {
        "skills": [
            # --- Ataque con VFX y SFX ---
            {"id": "punch", "text": "Puño", "type": "ATTACK", "dmg": 5, "cost": 1, "cost_type": "HP",
             "sfx": "assets/audio/sfx/punch_hit.ogg",
             "vfx": "assets/effects/punch_effect.png" #
            },
            # --- Ataque con DIFERENTES VFX y SFX ---
            {"id": "claws", "text": "Garras", "type": "ATTACK", "dmg": 3, "cost": 0,
             "sfx": "assets/audio/sfx/claws_hit.ogg", # (Necesitarías este audio)
             "vfx": "assets/effects/claws_effect.png" #
            }
        ]
    },
    "enemies": [
        {
            "id": "knife_guy", 
            "type": "knife_wielder", 
            "hp": 20, 
            "max_hp": 20,
            "sprite": "assets/characters/knife_guy.png", # (Asumiendo que tienes este sprite)
            "pos": [1400, 300],
            "hp_bar_sprite": "assets/layers_battle/hp_rat.png", # (Reutilizando la barra de la rata)
            "hp_bar_pos": [1400, 250],
            "sprite_scale_factor": 5.0,
            "hp_bar_scale_factor": 5.0, 
            "skills": [
                 # --- Ataque enemigo con sus propios VFX y SFX ---
                {"type": "ATTACK", "dmg_min": 2, "dmg_max": 4, "text": "Cuchillada",
                 "sfx": "assets/audio/sfx/knife_swing.ogg", # (Necesitarías este audio)
                 "vfx": "assets/effects/knife_effect.png" #
                }
            ]
        }
    ],
    "rules": {                      	# reglas del encuentro (gran ayuda para data-driven)
  	        "turn_order": "speed",      	# "speed", "player_first", "round_robin"
  	        "win_condition": "all_enemies_dead",
  	        "lose_condition": "party_dead"
    },
    "pre_battle_dialogue": [        	# si hay diálogo previo, opcional
  	        {"speaker":"Leader","text":"¡No pasaréis!"},
  	        {"speaker":"Hero","text":"No tenemos tiempo para esto..."}
    ],
    "rewards": {                    	# aplicarse al ganar
  	        "xp": 150,
  	        "items": ["gold_pouch","bandit_mask_fragment"],
  	        "add_fragments": ["frag_B"]
    },
    "on_victory_target": "scrips.after_battle_scene",
    "on_defeat_target": "scrips.game_over",
    "on_escape_target": "scrips.escaped_scene"
}



