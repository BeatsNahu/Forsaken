SCENE = {
    "id": "ch4_pivecuchillo",
    "title": "Chapter 2: un sonido sangriento",
    "background": "assets/backgrounds/Jail.png", 
    "music": "assets/audio/music/soundtrack.ogg",
    "sfx_on_enter": "assets/Sounds/metalicosonido.ogg",
    "lines": [
        {"speaker": "Narrator", "text": "Escuchas un sonido metálico y de que alguien se acerca.."},
    ],
    "choises": [
        {
            "text": "Pelear.",
            "target": "scripts.ch5_peleapivecuchillo",
        },
        {
        "text": "Huir.",
        "target": "scripts.ch5_finaltortura",
        }
    ]
}