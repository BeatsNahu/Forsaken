SCENE = {
    "id": "ch4_rana",
    "title": "Chapter 2: Croar de la Victoria",
    "background": "assets/backgrounds/Frog_scenary.png",
    "music": "assets/Sounds/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrator", "text": "En una esquina ves una rana."},
    ],
    "choises": [
        {
            "text": "Acariciar.",
            "target": "scripts.ch5_envenenado",
        },
        {
        "text": "Darle un patada.",
        "target": "scripts.ch5_pelearana",
        }
    ]
}