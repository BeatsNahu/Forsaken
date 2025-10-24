SCENE = {
    "id": "ch0_intro",
    "title": "Chapter 0: The Beginning",
    "background": "assets.backgrounds.Jail.png",
    "lines": [
        {"speaker": "Narrator", "text": "Te acercas y ves en la esquina varias latas de comida,"},
        {"speaker": "Narrator", "text": "pero al acercarte aparece una rata mutante..."},
    ],
    "choises": [
        {
            "text": "ganar",
            Después de tu pelea, te acercas a la pila de latas y encuentras comida.La vida aumenta +x     #muestra por pantalla
            "target": "scripts.ch0_option1",
        },
        {
        "text": "perder",
        "target": "scripts.ch4_ratatecome",
        }
    ]
}