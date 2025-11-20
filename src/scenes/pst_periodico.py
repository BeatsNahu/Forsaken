SCENE = {
    "id": "ch1_intro",
    "background": "assets/backgrounds/periodico.png",
    "music": "assets/audio/music/presentation.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "Despues de la falta de avances del doctor Waos,"},
        {"speaker": "Narrador", "text": "diversas personas critican si de verdad estaba"},
        {"speaker": "Narrador", "text": "hablando en serio sobre la evolucion de la humanidad."},
        {"speaker": "Narrador", "text": "Devido a las recientes desapariciones se cree que"},
        {"speaker": "Narrador", "text": "el doctor Waos secuestró a varias personas para"},
        {"speaker": "Narrador", "text": "dibersos experimentos."},
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scenes.pst_20",
            "sfx": "assets/audio/sfx/swap_option.ogg",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "A pesar de tu confusión, decides acercarte a la puerta,"},
                {"speaker": "Narrador", "text": "pero como no ves nada interesante a tu alrededor,"},
                {"speaker": "Narrador", "text": "caminas directamente hacia el pasillo frente a ti."}
            ]
        }
    ]
}