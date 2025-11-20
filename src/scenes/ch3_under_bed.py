SCENE = {
    "id": "ch3_under_bed",
    "background": "assets/backgrounds/bed_scenery.png", 
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrador", "text": "Rápidamente te acercas a la cama para ver debajo de ella;"},
        {"speaker": "Narrador", "text": "está tan oscuro que no puedes ver bien lo que hay."},
        {"speaker": "Narrador", "text": "¿Quieres meter la mano?"},
    ],
    "choices": [
        {
            "text": "Sí",
            "effects": [
                {"type": "give_item", "item": "Metal_bar"},
                
                {
                    "type": "show_item_overlay",
                    "item_name": "Barra de metal",
                    "item_image": "assets/items/tubooxidado.png"
                }
            ],
            "target": "scenes.ch4_frog",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Notas un movimiento extraño así que"},
                {"speaker": "Narrador", "text": "coges el primer objeto que ves para defenderte."}
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