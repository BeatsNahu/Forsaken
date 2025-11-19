SCENE = {
    "id": "ch1_intro",
    "title": "el inicio de todo",
    "background": "assets/backgrounds/2077.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "En el año 2077 comenzó todo,"},
        {"speaker": "Narrador", "text": "fue cuando comenzó el verdadero canvió."}
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scenes.pst_dr_prof",
            "sfx": "assets/audio/sfx/swap_option.ogg",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "A pesar de tu confusión, decides acercarte a la puerta,"}
            ]
        }
    ]
}