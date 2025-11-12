SCENE = {
    "id": "ch4_frog",
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
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Te acercas amablemente mientras extiendes la mano hacia ella,"},
                {"speaker": "Narrador", "text": "la rana no parece molestarse por tu presencia y se deja acariciar..."}
            ]
        },
        {
            "text": "Darle una buena patada.",
            "target": "scenes.ch5_frog_fight",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Decides recurrir a la violencia para obligar a la rana a apartarse,"},
                {"speaker": "Narrador", "text": "te acercas rapidamente y lanzas una patada que falla..."}
            ]
        }
    ]
}