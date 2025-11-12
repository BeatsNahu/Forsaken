SCENE = {
    "id": "ch3_under_bed",
    "background": "assets/backgrounds/bed_scenery.png", 
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrador", "text": "Rápidamente te acercas a la cama para ver debajo de ella,"},
        {"speaker": "Narrador", "text": "está tan oscuro que no puedes ver bien lo que hay."},
        {"speaker": "Narrador", "text": "Quieres meter la mano?"},
    ],
    "choices": [
        {
            "text": "Sí",
            "effects": [
                {"type": "give_item", "id": "Tenedor"},
                {"type": "add_fragment", "id": "frag_A"}
            ],
            "target": "scenes.ch4_frog",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Sin perder el tiempo, metes la mano debajo de la cama."},
                {"speaker": "Narrador", "text": "Mueves la mano entre el polvo y la suciedad..."},
                {"speaker": "Narrador", "text": "y consigues un tenedor oxidado!!"},
            ]
        },
        {
            "text": "No",
            "target": "scenes.ch4_frog",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Decides no arriesgarte a meter la mano en la oscuridad,"},
                {"speaker": "Narrador", "text": "y continúas explorando la habitación."},
            ]
        }
    ]
}