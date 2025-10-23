SCENE = {
    "id": "ch3_cama",
<<<<<<< HEAD
    "background": "assets/backgrounds/Bed.png",
    "music": "assets/Sounds/soundtrack.ogg", 
=======
    "title": "Chapter 0: The Beginning",
    "background": "assets.backgrounds.Jail.png",
>>>>>>> f65941e (refactor: remove unused chapter scripts to streamline the project)
    "lines": [
        {"speaker": "Narrator", "text": "¿Revisas debajo de la cama?."},
    ],
    "choises": [
        {
            "text": "Sí",
<<<<<<< HEAD
<<<<<<< HEAD
            "effects": [
                {"type": "give_item", "id": "Tenedor"},
                {"type": "add_fragment", "id": "frag_A"}
            ],
=======
            "give_item": "tenedor",
>>>>>>> f65941e (refactor: remove unused chapter scripts to streamline the project)
=======
            "give_item": "tenedor",                 #hay que canviarlo
>>>>>>> abdd92e (feat: implement battle scene structure and enhance enemy interactions)
            "target": "scripts.ch4_rana",
        },
        {
            "text": "No",
            "target": "scripts.ch4_rana",
        }
    ]
}