CENE = {
    "id": "example_dialogue",
    "title": "Capítulo de Ejemplo",
    "background": "assets/backgrounds/jail_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.1,
    
    # --- Animaciones al entrar ---
    "animations_on_enter": [
        {
            "id": "hero_portrait",
            "image": "assets/characters/player_sprite.png", # (Asumiendo que tienes un sprite)
            "persist": True,             # Se queda en pantalla
            "duration": 0.7,
            "start_pos": [-400, 500],    # Slide-in desde la izquierda
            "end_pos": [300, 500],
            "start_scale": 1.0,
            "end_scale": 1.0
        }
    ],
    
    "lines": [
        {"speaker": "Narrador", "text": "Este es un ejemplo de escena de diálogo."},
        {"speaker": "Héroe", "text": "Puedo usar 'animations_on_enter' para aparecer."},
        {"speaker": "Narrador", "text": "Y ahora, una elección importante."}
    ],
    "choices": [
        {
            "text": "Elegir el camino 1",
            "target": "scenes.ch2_jails",
            "sfx": "assets/audio/sfx/option_selected.ogg",
            # --- Efectos al elegir ---
            "effects": [
                {"type": "notify", "text": "Has elegido el CAMINO 1", "duration": 4},
                {"type": "give_item", "item": "llave_simple"}
            ],
            # --- Diálogo después de elegir ---
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "El camino 1 se cierra detrás de ti..."}
            ]
        },
        {
            "text": "Elegir el camino 2",
            "target": "scenes.ch3_rat_fight",
            "sfx": "assets/audio/sfx/option_selected.ogg",
            "effects": [
                {"type": "notify", "text": "Has elegido el CAMINO 2", "duration": 4}
            ]
            # (Sin post_choice_lines, carga la escena 'target' al instante)
        }
    ]
}