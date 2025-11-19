SCENE = {
    "id": "pst_2077",
    "title": "L'inici de tot",
    "background": "assets/backgrounds/2077.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "En una era nova, on la tecnologia ha avançat molt,"},
        {"speaker": "Narrador", "text": "apareix gent amb mentalitats una mica extremistes."},
        {"speaker": "Narrador", "text": "A principis de l'any 2077 va sortir un investigador autònom,"},
        {"speaker": "Narrador", "text": "era el Dr. J.Harrison, un home amb una visió innovadora..."},
        {"speaker": "Narrador", "text": "o al menys això deia ell."},
    ],
    "choices": [
        {
            "text": "-->",
            "target": "scenes.pst_dr_prof",
            "sfx": "assets/audio/sfx/swap_option.ogg",
        }
    ]
}