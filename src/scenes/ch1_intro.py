SCENE = {
    "id": "ch1_intro",
    "title": "Chapter 1: Los dos caminos",
    "background": "assets/backgrounds/jail_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.5,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrator", "text": "Estás en una especie de celda,"},
        {"speaker": "Narrator", "text": "pero no recuerdas cómo llegaste allí."},
        {"speaker": "Narrator", "text": "Ves la puerta de tu celda abierta, ¿qué haces?."}
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scenes.ch2_jails",
            "sfx": "assets/audio/sfx/swap_option.ogg"
        }
    ]
}