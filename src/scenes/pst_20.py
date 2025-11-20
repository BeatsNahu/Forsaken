SCENE = {
    "id": "ch1_intro",
    "background": "assets/backgrounds/20¿_.png",
    "music": "assets/audio/music/presentation.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "Abres los ojos y te encuentras en un lugar que no reconoces,"},
        {"speaker": "Narrador", "text": "tratas de recordar como o cuando llegaste aqui,"},
        {"speaker": "Narrador", "text": "pero cuanto mas lo intentas,"},
        {"speaker": "Narrador", "text": "te vas dando cuenta de que no eres capaz de recordar nada,"},
        {"speaker": "Narrador", "text": "nisiquiera tu propio nombre."},
        {"speaker": "Narrador", "text": "La situación te hace sentir un escalofrio."}
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scenes.ch1_intro",
            "sfx": "assets/audio/sfx/swap_option.ogg",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "A pesar de tu confusión, decides acercarte a la puerta,"},
                {"speaker": "Narrador", "text": "pero como no ves nada interesante a tu alrededor,"},
                {"speaker": "Narrador", "text": "caminas directamente hacia el pasillo frente a ti."}
            ]
        }
    ]
}