"start_battle": {
  "battle_id": "btl_01_bandits",  	# id único
  "background": "backgrounds/forest_clear.png",
  "music": "music/battle_theme.ogg",
  "arena": {
  	"width_ratio": 0.9,         	# parámetros visuales si quieres
  	"height_ratio": 0.5
  },
  "player": {                     	# parámetros opcionales de apoyo
  	"party": ["hero","companion"],
  	"initial_hp": null          	# null = usar stats actuales del engine
  },
  "enemies": [
  	{"id":"bandit_1","type":"bandit","level":3,"hp":120,"pose":"idle"},
  	{"id":"bandit_2","type":"bandit","level":2,"hp":90,"pose":"idle"},
  	{"id":"bandit_leader","type":"bandit_leader","level":5,"hp":300,"pose":"angry"}
  ],
  "rules": {                      	# reglas del encuentro (gran ayuda para data-driven)
  	"turn_order": "speed",      	# "speed", "player_first", "round_robin"
  	"win_condition": "all_enemies_dead",
  	"lose_condition": "party_dead",
  	"escape_allowed": True
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



