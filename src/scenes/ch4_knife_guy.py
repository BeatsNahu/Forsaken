SCENE = {
    "id": "ch4_knife_guy",
    "title": "Capitulo 2: un sonido sangriento",
    "background": "assets/backgrounds/jail_scenery.png", 
    "music": "assets/audio/music/soundtrack.ogg",
    "sfx_on_enter": "assets/audio/sfx/metallic_sound.ogg",
    "lines": [
        {"speaker": "Narrador", "text": "Consigues derrotar a la rata mutante y continúas caminando"},
        {"speaker": "Narrador", "text": "hasta que el sonido de algo metálico siendo arrastrado"},
        {"speaker": "Narrador", "text": "por una pared, llama tu atención."},
        {"speaker": "Narrador", "text": "Sientes que algo peligroso se acerca..."}
    ],
    "choices": [
        {
            "text": "Enfrentar lo que venga.",
            "target": "scenes.ch5_knife_fight",
        },
        {
        "text": "Salir corriendo.",
        "target": "scenes.ch5_torture",
        }
    ]
}