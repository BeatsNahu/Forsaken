SCENE = {
  "start_battle": {
    "battle_id": "btl_01_bandits",  	# id único
    "background": "assets.backgrounds.Jail.png",
    },
    "enemies": [
  	  {"id":"pivecuchillo","type":"pivecuchillo"},
    ],
    "rules": {                      	# reglas del encuentro (gran ayuda para data-driven)
  	  "win_condition": "all_enemies_dead",
  	  "lose_condition": "party_dead",
    },
    "pre_battle_dialogue": [        	# si hay diálogo previo, opcional
  	  {"speaker":"Narrator","text":"Te acercas y ves en la esquina varias latas de comida,"},
  	  {"speaker":"Narrator","text":"pero al acercarte aparece una rata mutante..."}
    ],
    "rewards": {                    	# aplicarse al ganar
  	  "add_fragments": ["frag_B"]
    },
    "on_victory_target": "scripts.ch7_salir",
    "on_defeat_target": "scripts.ch6_finaltortura"
    }