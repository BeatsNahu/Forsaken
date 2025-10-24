SCENE = {
    "id": "ch3_cama",
    "title": "Chapter 0: The ------",
    "background": "assets.backgrounds.Bed.png",
    "lines": [
        {"speaker": "Narrator", "text": "¿Revisas debajo de la cama?."},
    ],
    "choises": [
        {
            "text": "Sí",
            "give_item": "tenedor",                 #hay que canviarlo
            "target": "scripts.ch4_rana",
        },
        {
            "text": "No",
            "target": "scripts.ch4_rana",
        }
    ]
}