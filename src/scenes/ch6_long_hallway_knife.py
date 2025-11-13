SCENE = {
    "id": "ch6_long_stairs",
    "background": "assets/backgrounds/hall_scenery.png",
    "music": "assets/audio/music/soundtrack.ogg",
    "lines": [
        {"speaker": "Narrator", "text": "Contra todo pronóstico logras derrotar al señor cuchillos."},
        {"speaker": "Narrator", "text": "La emoción de esa victoria completamente inesperada"},
        {"speaker": "Narrator", "text": "te da una renovada confianza que te ayuda a continuar con tu viaje"},
        {"speaker": "Narrator", "text": "y a adentrarte en un largo pasillo que parece no tener fin."},
    ],
    "choices": [
        {
            "text": "Continuar caminando.",
            "target": "scenes.ch7_continue_knife_guy",
            "post_choice_lines": [
                {"speaker": "Narrator", "text": "Sientes una extraña presión en el pecho mientras avanzas,"},
                {"speaker": "Narrator", "text": "como si el aire se hubiera vuelto más denso y pesado,"},
                {"speaker": "Narrator", "text": "una fuerte corriente de aire frío recorre el pasillo..."}
            ]
        }
    ]
}