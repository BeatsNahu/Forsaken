SCENE = {
    "id": "pst_periodico",
    "background": "assets/backgrounds/doctor_decadencia.png",
    "music": "assets/audio/music/presentation.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "Però la gent volia miracles,"},
        {"speaker": "Narrador", "text": "ell no podia complir amb les seves expectatives"},
        {"speaker": "Narrador", "text": "i els experiments van començar a no donar els resultats esperats,"},
        {"speaker": "Narrador", "text": "així que ell va començar a prendre mesures desesperades."},
        {"speaker": "Narrador", "text": "Faria el que sigui necessari per a avançar amb els seus experiments"},
        {"speaker": "Narrador", "text": " i demostrar-li al món que el no és un mentider..."},
    ],
    "choices": [
        {
            "text": "-->",
            "target": "scenes.pst_decadencia",
            "sfx": "assets/audio/sfx/swap_option.ogg",
        }
    ]
}