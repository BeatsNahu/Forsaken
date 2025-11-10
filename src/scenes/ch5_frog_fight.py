SCENE = {
  "start_battle": {
    "battle_id": "btl_01_frog",  	# id único
    "background": "assets.backgrounds.Jail.png",
    "enemies": [
  	  {"id":"frog","type":"frog"},
    ],
    "rules": {                      	# reglas del encuentro (gran ayuda para data-driven)
  	  "win_condition": "all_enemies_dead",
  	  "lose_condition": "party_dead",
    },
    "pre_battle_dialogue": [        	# si hay diálogo previo, opcional
  	  {"speaker":"Narrator","text":"La rana se enfada y te ataca."}
    ],
    "rewards": {                    	# aplicarse al ganar
  	  "add_fragments": ["frag_B"]
    },
    "on_victory_target": "scrips.ch4_mcwin",
    "on_defeat_target": "scrips.ch4_crias",
  }
}