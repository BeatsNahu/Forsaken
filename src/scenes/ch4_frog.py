SCENE = {
    "id": "ch4_rana",
    "background": "assets/backgrounds/frog_scenery2.png",
    "music": "assets/audio/music/soundtrack.ogg",
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrador", "text": "Cuando tratas de continuar con tu camino te das cuenta de que"},
        {"speaker": "Narrador", "text": "el pequeño compañero ha decidido cortarte el paso."},
        {"speaker": "Narrador", "text": "Qué harás?"}
    ],
    "choices": [
        {
            "text": "Acariciarle.",
            "target": "scenes.ch5_mutated",
        },
        {
        "text": "Darle una buena patada.",
        "target": "scenes.ch5_frog_fight",
        }
    ]
}