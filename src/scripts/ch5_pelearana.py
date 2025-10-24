SCENE = {
    "id": "ch0_intro",
    "title": "Chapter 0: The Beginning",
    "background": "assets.backgrounds.Jail.png",
    "lines": [
        {"speaker": "Narrator", "text": "La rana se enfada y te ataca."},
    ],
    "choises": [
        {
            "text": "ganar",
            "target": "scripts.ch0_option1",
        },
        {
        "text": "perder",
        "target": "scripts.ch0_option2",
        }
    ]
}
SCENE = {
  "start_battle": {
    "battle_id": "btl_01_bandits",  	# id único
    "background": "assets.backgrounds.Jail.png",
    "player": {                     	# parámetros opcionales de apoyo
  	  "party": ["hero","companion"],
  	  "initial_hp": null          	# null = usar stats actuales del engine
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
    "on_victory_target": "scripts.ch6_mcwin",
    "on_defeat_target": "scripts.ch6_crias"
  }
}