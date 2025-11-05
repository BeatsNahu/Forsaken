SCENE = {
    "id": "ch3_cama",
    "background": "assets/backgrounds/Bed.png", 
    "music": "assets/Sounds/soundtrack.ogg", 
    "sfx_on_enter": None,
    "lines": [
        {"speaker": "Narrator", "text": "¿Revisas debajo de la cama?."},
    ],
    "choises": [
        {
            "text": "Sí",
            "effects": [
                {"type": "give_item", "id": "Tenedor"},
                {"type": "add_fragment", "id": "frag_A"}
            ],
            "target": "scripts.ch4_rana",
        },
        {
            "text": "No",
            "target": "scripts.ch4_rana",
        }
    ]
}