SCENE = {
    "id": "pst_decadencia",
    "background": "assets/backgrounds/periodico.png",
    "music": "assets/audio/music/soundtrack.ogg", 
    "volume": 0.1,
    "sfx_on_enter": None, 
    "lines": [
        {"speaker": "Narrador", "text": "Finalment tot va acabar amb una gran polèmica:"},
        {"speaker": "Narrador", "text": "'El Dr. J.Harrison sembla estar directament relacionat"},
        {"speaker": "Narrador", "text": "amb la desaparició de diverses persones.'"},
        {"speaker": "Narrador", "text": "La notícia va omplir tots els noticiaris i la gent volia respostes,"},
        {"speaker": "Narrador", "text": " però quan van anar a buscar-li"},
        {"speaker": "Narrador", "text": "ell havia desaparegut dins del seu laboratori."},
        {"speaker": "Narrador", "text": "Clarament, la policia no es va quedar sense fer res"},
        {"speaker": "Narrador", "text": "i van anar darrere ell."},
        {"speaker": "Narrador", "text": "Però l'únic equip que va entrar al seu laboratori,"},
        {"speaker": "Narrador", "text": "mai va sortir."},
        {"speaker": "Narrador", "text": "Fins avui dia ningú sap on és el Dr. J.Harrison"},
        {"speaker": "Narrador", "text": "i ningú va tornar a parlar d'aquest incident,"},
        {"speaker": "Narrador", "text": "com si mai hagués existit..."},
    ],
    "choices": [
        {
            "text": "-->",
            "target": "scenes.pst_20",
            "sfx": "assets/audio/sfx/swap_option.ogg",
        }
    ]
}