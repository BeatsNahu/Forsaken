SCENE = {
    "id": "ch3_bed",
    "title": "Capitulo 2: Croar de la Victoria",
    "background": "assets/backgrounds/frog_scenery1.png", 
    "music": "assets/audio/music/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrador", "text": "La celda XXX rapidamente te llama la atención,"},
        {"speaker": "Narrador", "text": "a diferencia de tu solitaria celda,"},
        {"speaker": "Narrador", "text": "esta tiene una cama y una mascota de compañia."},
        {"speaker": "Narrador", "text": "Algo debajo de la cama te llama la atención."},
        {"speaker": "Narrador", "text": "Quieres ver debajo de ella?"}
    ],
    
    "choices": [
        {
            "text": "Sí",
            "target": "scenes.ch3_under_bed",
        },
        {
            "text": "No",
            "target": "scenes.ch4_frog",
        }
    ]
}