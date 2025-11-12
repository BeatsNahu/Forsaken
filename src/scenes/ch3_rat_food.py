SCENE = {
    "id": "ch3_rat_food",
    "background": "assets/backgrounds/rat_scenery.png", 
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrador", "text": "Al entrar en la celda xxx un olor desconocido te invade,"},
        {"speaker": "Narrador", "text": "te das cuenta de que en la pared hay varias bolsas apiladas,"},
        {"speaker": "Narrador", "text": "con algo que parece... ligeramente comestible."}
    ],
    
    "choices": [
        {
            "text": "Acercarse a las bolsas.",
            "target": "scenes.ch3_food_bags",
        },
    ]
}