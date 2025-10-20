SCENE = {
    "id": "ch3_cama",
    "title": "Chapter 0: The Beginning",
    "background": "assets.backgrounds.Jail.png",
    "lines": [
        {"speaker": "Narrator", "text": "¿Revisas debajo de la cama?."},
    ],
    "choises": [
        {
            "text": "Sí",
            "give_item": "tenedor",
            "target": "scripts.ch4",
        },
        {
            "text": "No",
            "target": "scripts.ch4",
        }
    ]
}