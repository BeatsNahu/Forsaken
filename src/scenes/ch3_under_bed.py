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
                {"type": "give_item", "item": "Lata_alubias"},
                
                {
                    "type": "show_item_overlay",
                    "item_name": "Lata de Alubias",
                    "item_image": "assets/items/Lata_alubias.png"
                }
            ],
            "target": "scenes.ch4_frog",
        },
        {
            "text": "No",
            "target": "scenes.ch4_frog",
        }
    ]
}