SCENE = {
    "id": "ch2_jails",
    "background": "assets/backgrounds/doors_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "effects_on_enter": [
        {"type": "notify", "text": "Tu destino empieza a tomar forma.", "duration": 4}
    ],
    "lines": [
        {"speaker": "Narrator", "text": "Al acercarte, miras alrededor y no ves nada destacable."},
        {"speaker": "Narrator", "text": "Sales de tu celda y vas a otra."},
    ],
    "choices": [
        {
            "text": "Revisar la celda Nª 002.",
            "target": "scenes.ch3_rat_fight",
        },
        {
            "text": "Revisar la celda Nª XXX.",
            "target": "scenes.ch3_bed",
        }
    ]
}