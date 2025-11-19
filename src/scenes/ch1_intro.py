SCENE = {
    "id": "ch1_intro",
    "title": "Capitulo 1: Los dos caminos",
    "background": "assets/backgrounds/jail_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "Abres los ojos y te encuentras en un lugar que no reconoces;"},
        {"speaker": "Narrador", "text": "tratas de recordar cómo o cuándo llegaste aquí,"},
        {"speaker": "Narrador", "text": "pero cuanto más lo intentas,"},
        {"speaker": "Narrador", "text": "te vas dando cuenta de que no eres capaz de recordar nada,"},
        {"speaker": "Narrador", "text": "ni siquiera tu propio nombre."},
        {"speaker": "Narrador", "text": "La situación te hace sentir un escalofrío."}
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scenes.ch2_jails",
            "sfx": "assets/audio/sfx/swap_option.ogg",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "A pesar de tu confusión, decides acercarte a la puerta,"},
                {"speaker": "Narrador", "text": "pero como no ves nada interesante a tu alrededor,"},
                {"speaker": "Narrador", "text": "caminas directamente hacia el pasillo frente a ti."}
            ]
        }
    ]
}