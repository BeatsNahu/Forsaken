SCENE = {
    "id": "ch0_intro",
    "title": "Chapter 0: The Beginning",
    "background": "assets.backgrounds.Jail.png",
    "lines": [
        {"speaker": "Narrator", "text": "Vas en la dirección en la que venía el monstruo y a lo lejos"},
        {"speaker": "Narrator", "text": "encuentras una salida al río."},
    ],
    "choises": [
        {
            "text": "Sigues el camino del río.",
            "target": "scripts.ch8_finalbosque",
        },
        {
        "text": "Das media vuelta y vuelves adentro.",
        "target": "scripts.ch8_venganza",
        }
    ]
}