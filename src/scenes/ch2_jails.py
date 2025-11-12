SCENE = {
    "id": "ch2_jails",
    "background": "assets/backgrounds/doors_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "effects_on_enter": [
        {"type": "notify", "text": "Tu destino empieza a tomar forma.", "duration": 4}
    ],
    "lines": [
        {"speaker": "Narrador", "text": "Sales de lo que parecia ser una celda"},
        {"speaker": "Narrador", "text": "y te encuentras con una habitación que se divide en dos pasillos,"},
        {"speaker": "Narrador", "text": "ambos nombrados como 002 y XXX."},
        {"speaker": "Narrador", "text": "Teniendo en cuenta el lugar en el que despertaste,"},
        {"speaker": "Narrador", "text": "supones que ambos pasillos llevan a más celdas."}
    ],
    "choices": [
        {
            "text": "Revisar la celda Nª 002.",
            "target": "scenes.ch3_bed",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "El otro pasillo no te llama demasiado la atención,"},
                {"speaker": "Narrador", "text": "asi que decides continuar hacia la celda 002."},
            ]
        },
        {
            "text": "Revisar la celda Nª XXX.",
            "target": "scenes.ch3_rat_food",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Sientes una extraña curiosidad por el pasillo XXX,"},
                {"speaker": "Narrador", "text": "asi que decides caminar hacia esa dirección."},
            ]
        }
    ]
}