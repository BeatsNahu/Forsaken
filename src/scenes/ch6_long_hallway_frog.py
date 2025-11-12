SCENE = {
    "id": "ch6_long_hallway",
    "background": "assets/backgrounds/hall_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg",
    "lines": [
        {"speaker": "Narrador", "text": "Tras una intensa batalla,"},
        {"speaker": "Narrador", "text": "logras vencer a la rana mutante y te adentras por el pasillo."},
        {"speaker": "Narrador", "text": "Caminas con cuidado por el oscuro y largo corredor,"},
        {"speaker": "Narrador", "text": "el pasillo se alarga y te adentras aún más en la oscuridad..."},
    ],
    "choices": [
        {
            "text": "Continuar caminando.",
            "target": "scenes.ch7_continue_frog",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Sin dudarlo, decides continuar avanzando por el pasillo."}
            ]
        }
    ]
}