SCENE = {
    "id": "ch1_intro",
    "title": "Chapter 1: Los dos caminos",
    "background": "assets/backgrounds/Jail_scenary.png",
    "music": "assets/Sounds/soundtrack.ogg", 
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrator", "text": "Estás en una especie de celda,"},
        {"speaker": "Narrator", "text": "pero no recuerdas cómo llegaste allí."},
        {"speaker": "Narrator", "text": "Ves la puerta de tu celda abierta, ¿qué haces?."},
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scripts.ch2_celdas",
            "sfx": None
        }
    ]
}