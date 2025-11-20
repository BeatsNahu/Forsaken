SCENE = {
    "id": "ch3_rat_food",
    "background": "assets/backgrounds/zoom_bags.png", 
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrador", "text": "Aunque te desagrada la idea, no recuerdas la última  vez que comiste..."},
        {"speaker": "Narrador", "text": "y cuanto más lo piensas, más hambre sientes..."},
        {"speaker": "Narrador", "text": "¿Quieres rebuscar en las bolsas?"},
    ],

    "choices": [
        {
            "text": "DEFINITIVAMENTE SÍ.",
            "target": "scenes.ch3_rat_fight",
            "post_choice_lines": [
                {"speaker": "Narrador", "text": "Notas un movimiento extraño así que"},
                {"speaker": "Narrador", "text": "coges el primer objeto que ves para defenderte."},
            ],
            "effects": [
                {"type": "give_item", "item": "Metal_bar"},
                
                {
                    "type": "show_item_overlay",
                    "item_name": "Barra de metal",
                    "item_image": "assets/items/tubooxidado.png"
                }
            ]
        },
    ]
}       


