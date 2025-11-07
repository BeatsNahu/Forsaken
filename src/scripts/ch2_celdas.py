
SCENE = {
    "id": "ch2_celdas",
    "background": "assets/backgrounds/Doors_scenary.png", 
    "music": "assets/Sounds/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrator", "text": "Al acercarte, miras alrededor y no ves nada destacable."},
        {"speaker": "Narrator", "text": "Sales de tu celda y vas a otra."},
    ],
    "choises": [
        {
            "text": "Revisar la celda Nª 002.",
            "target": "scripts.ch3_pelearata",
        },
        {
            "text": "Revisar la celda Nª XXX.",
            "target": "scripts.ch3_cama",
        }
    ]
}