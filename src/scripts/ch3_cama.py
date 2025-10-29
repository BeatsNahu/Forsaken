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