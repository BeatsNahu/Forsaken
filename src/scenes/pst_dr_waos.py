SCENE = {
    "id": "pst_dr_yelling",
    "background": "assets/backgrounds/doctor_waos.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "La situación te hace sentir un escalofrio."}
    ],
    "choices": [
        {
            "text": "Acércate a la puerta",
            "target": "scenes.pst_periodico",
            "sfx": "assets/audio/sfx/swap_option.ogg",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "caminas directamente hacia el pasillo frente a ti."}
            ]
        }
    ]
}