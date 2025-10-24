# scrips/template_scene.py
# Plantilla de SCENE para escenas data-driven.
# Copia y modifica para cada capítulo. Comentarios explicativos en cada campo.

SCENE = {
	# ---------- IDENTIFICACIÓN Y METADATOS ----------
	"id": "chapter_01_intro",     	# (str) Identificador único de la escena (OBLIGATORIO)
	"title": "Introducción",     	# (str) Título legible (opcional, útil para herramientas/edición)
	"description": "Escena introductoria donde el jugador recibe la primera pista.",
	"tags": ["intro", "tutorial"],   # (list[str]) etiquetas libre para buscar/filtrar escenas
	"authors": ["Autor1", "Autor2"], # (list[str]) opcional, útil para colaboración
	"version": "1.0",            	# (str) versión de la escena

	# ---------- ASSETS Y PRESENTACIÓN ----------
	"background": "backgrounds/village_day.png",  # (str) ruta relativa dentro de assets/
	"background_transition": {                	# (obj) transición al cargar bg (opcional)
    	"type": "fade", "duration": 0.5       	# type: "fade"|"slide"|"none"
	},
	"music": {                                	# (obj) música de fondo (opcional)
    	"file": "music/intro_theme.ogg",
    	"loop": True,
    	"volume": 0.7
	},
	"sfx_on_enter": ["sfx/bell.ogg"],        	# (list[str]) reproducir al entrar

	# ---------- PERSONAJES / RETRATOS / POSICIÓN ----------
	# Lista de retratos a mostrar en la escena (pre-carga/capas)
	"portraits": [
    	# Un retrato puede tener múltiples poses/expresiones
    	{
        	"character_id": "old_man",      	# (str) id del personaje
        	"poses": {                      	# poses -> archivos relativos
            	"neutral": "portraits/old_neutral.png",
            	"happy":   "portraits/old_happy.png",
            	"angry":   "portraits/old_angry.png"
        	},
        	# parámetros de posicionamiento por defecto (proporcional a la pantalla)
        	"default_side": "left",         	# "left" | "right" | "center"
        	"scale": 1.0,
        	"z_index": 20                   	# orden de dibujado
    	}
	],

	# ---------- CONTENIDO: LÍNEAS Y DIÁLOGO ----------
	# Lista de líneas que se mostrarán secuencialmente.
	# Cada línea puede tener tags que controlen speed/type/sfx/etc.
	"lines": [
    	{
        	"speaker": "Narrador",         	# (str) nombre para mostrar en UI
        	"text": "Llegas al pueblo, y un anciano te saluda con respeto.",
        	"portrait": None,              	# (None o dict) cambiar retrato: {"character_id":"old_man","pose":"neutral"}
        	"voice": None,                 	# (str) ruta a voz/clip opcional
        	"tags": {                      	# (obj) metadatos para UI (opcional)
            	"speed": 45,               	# (int) chars por segundo para máquina de escribir
            	"wait_after": 0.5,         	# (float) segundos de espera automático tras la línea
            	"shake": False
        	},
        	"effects_on_display": [        	# (list[effect]) aplicados al mostrar la línea (opcional)
            	# e.g. {"type":"play_sfx","file":"sfx/footstep.ogg"}
        	]
    	},
    	# ... más líneas ...
	],

	# ---------- ELECCIONES (CHOICES) ----------
	# Aparecen cuando se acaban las líneas o cuando la línea contiene un tag que lo solicita.
	"choices": [
    	{
        	"id": "choice_help_old",       	# (str) id opcional de la elección
        	"text": "Sí, te ayudo, ¿qué necesitas?",  # (str) texto mostrado en la UI
        	"target": "scrips.chapter1_help",  # (str|null) módulo/escena a cargar (si null -> no cambia)
        	"effects": [                   	# (list[effect]) efectos aplicados al elegir
            	{"type": "give_item", "item": "map_fragment_1"},
            	{"type": "add_code_fragment", "fragment_id": "frag_A"}
        	],
        	"conditions": [                	# (list[condition]) condiciones para mostrar/activar
            	# e.g. {"type":"var_equals","name":"met_priest","value":True}
        	],
        	"ui": {                        	# (obj) sugerencias de UI (opcional)
            	"disabled_text": "Necesitas la llave",
            	"style": "default"
        	}
    	},
    	{
        	"text": "No, tengo prisa",
        	"target": "scrips.chapter1_leave",
        	"effects": [
            	{"type": "set_var", "name": "helped_old_man", "value": False}
        	]
    	}
	],

	# ---------- EFECTOS GLOBALES (APLICADOS AL ENTRAR/SALIR/AL FINAL) ----------
	"on_enter": [   # efectos que se ejecutan al cargar la escena
    	# {"type":"play_music","file":"music/theme.ogg"},
	],
	"on_exit": [	# efectos que se ejecutan al abandonar la escena
    	# {"type":"stop_music"}
	],
	"effects": [   # efectos aplicados al terminar la escena (si procede)
    	# {"type":"add_code_fragment","fragment_id":"frag_A"}
	],

	# ---------- LÓGICA/CONDICIONES AVANZADAS ----------
	# Reglas para activar o mostrar elementos
	"variables": {                       	# (obj) valores iniciales locales (opcional)
    	# "helped_old_man": False
	},

	# ---------- DATOS ADICIONALES / VISUALS / TRANSICIONES ----------
	"ui": {
    	"dialog_box": "ui/dialog_box_large.png",
    	"font": { "file": "fonts/OpenSans-Regular.ttf", "size": 28, "color": [255,255,255] }
	},
	"timing": {                          	# (obj) sugerencias de tiempo global para la escena
    	"default_text_speed": 45,        	# chars por segundo
    	"auto_advance": False
	},

	# ---------- METADATOS PARA HERRAMIENTAS/TESTS ----------
	"test": {
    	"expected_fragments_on_exit": ["frag_A"],   # (list) para pruebas automáticas
	}
}

# -----------------------------------------------------------------------
# NOTAS / DOCUMENTACIÓN Rápida para quien edite la escena:
#
# - Campos OBLIGATORIOS mínimos para una escena "simple" (texto + choices):
# 	id, lines (lista con al menos 1 elemento)
#   Recomendados: title, background, choices (si hay branching)
#
# - ESTRUCTURA de una línea en 'lines':
# 	{"speaker":str, "text":str, "portrait": None or {"character_id":"x","pose":"y"}, "tags": {...}}
#
# - FORMATO de un effect (ejemplos comunes):
# 	{"type":"give_item", "item":"item_id"}
# 	{"type":"set_var", "name":"var_name", "value": True}
# 	{"type":"add_code_fragment", "fragment_id":"frag_X"}
# 	{"type":"start_battle", "battle_module":"src.scenes.battle_easy"}
# 	{"type":"goto", "target":"scrips.endings.good_end"}
# 	{"type":"play_sfx", "file":"sfx/notify.ogg"}
#
# - FORMATO de una condición (ejemplos):
# 	{"type":"var_equals", "name":"helped_old_man", "value":True}
# 	{"type":"has_item", "item":"old_sword"}
#
# - Qué quitar para escenas muy simples:
# 	elimina 'portraits', 'music', 'on_enter', 'ui' y deja solo id, background (opcional),
# 	lines y choices. Mantén effects solo si la escena da items/fragmentos.
#
# - Seguridad: estos archivos son DATA. Evitar poner código ejecutable (funciones) dentro.
#   Cualquier lógica compleja (IA, peleas) debe implementarse en src/scenes/ como clases.
#
# -----------------------------------------------------------------------

# ----------------- Validación simple (puede ejecutarla tu compañero) -----------------
# Esta función es un validador muy básico que comprueba la presencia y tipos de campos.