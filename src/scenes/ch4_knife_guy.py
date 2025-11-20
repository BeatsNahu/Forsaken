SCENE = {
    "id": "ch4_knife_guy",
    "title": "Capitulo 2: un sonido sangriento",
    "background": "assets/backgrounds/rat_scenery.png", 
    "music": "assets/audio/music/soundtrack.ogg",
    "sfx_on_enter": "assets/audio/sfx/metallic_sound.ogg",
    "lines": [
        {"speaker": "Narrador", "text": "Después de una batalla agotadora,"},
        {"speaker": "Narrador", "text": "logras vencer a la rata gigante,"},
        {"speaker": "Narrador", "text": "pero no tienes tiempo para descansar..."},
        {"speaker": "Narrador", "text": "porque un sonido metálico resuena en la distancia."},
        {"speaker": "Narrador", "text": "Parece que tu batalla atrajo a otra criatura..."},
        {"speaker": "Narrador", "text": "Algo peligroso se acerca..."}
    ],
    "choices": [
        {
            "text": "Enfrentar lo que venga.",
            "target": "scenes.ch5_dark_door",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Decides quedarte para enfrentar aquello que se acerca,"},
                {"speaker": "Narrador", "text": "pero no estabas listo para lo que verías..."},
                {"speaker": "Narrador", "text": "La puerta frente a ti se abre lentamente..."}
            ]
        },
        {
        "text": "Salir corriendo.",
        "target": "scenes.ch5_torture",
        }
    ]
}