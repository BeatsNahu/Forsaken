# =============================================================================
# --- GLOBAL GAME CONFIGURATION ---
# =============================================================================
# This file centralizes all the "magic" constants (fixed values)
# so your engine is easier to maintain and 100% data-driven.

# --- 1. General Game Configuration ---
GAME_TITLE = "Forsaken"
GAME_ICON_PATH = "assets/ui/logo.png"

# --- 2. Screen and Display ---
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

# --- 3. Font Paths and Sizes (Defaults) ---
FONT_PATH_DEFAULT = "assets/fonts/press-start.k.ttf"

# Sizes
FONT_SIZE_REGULAR = 20    # Normal dialog text
FONT_SIZE_SPEAKER = 24    # Speaker/name labels
FONT_SIZE_HUD = 28        # Battle ability text
FONT_SIZE_HUD_HP = 20     # Player HP in battle HUD
FONT_SIZE_LOG = 24        # Battle log text
FONT_SIZE_TITLE = 50      # Chapter titles
FONT_SIZE_MENU = 50       # Main menu options
FONT_SIZE_LOG = 24        # Battle log text

# --- 4. UI Timings and Speeds ---
TEXT_SPEED_DEFAULT = 30   # Characters/sec for typing effect
FADE_SPEED_DEFAULT = 400.0  # Fade-in/out speed for UI
TRANSITION_SPEED = 500    # Fade-to-black speed between scenes

# --- 5. UI Sound Paths (Defaults) ---
SFX_UI_SWAP = "assets/audio/sfx/swap_option.ogg"
SFX_UI_CONFIRM = "assets/audio/sfx/option_selected.ogg"
SFX_UI_TYPING = "assets/audio/sfx/type_writing1.ogg"
DEFAULT_MUSIC_VOLUME = 0.8
DEFAULT_SFX_VOLUME = 0.8

# --- 6. Colors ---
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_RED = (255, 0, 0)

# --- 7. Notification ---
NOTIFICATION_PADDING_Y = 10

# --- 8. Battle HUD Layout ---
# Relative positions within the battle HUD panel
BATTLE_HUD_PADDING_X = 500
BATTLE_HUD_HP_POS_Y = 500
BATTLE_HUD_SKILL_START_Y = 500
BATTLE_HUD_LINE_SPACING = 40

# Enemy HP bar within enemy panel
ENEMY_HP_BAR_OFFSET_X = 32  
ENEMY_HP_BAR_OFFSET_Y = 14  
ENEMY_HP_BAR_WIDTH = 102    
ENEMY_HP_BAR_HEIGHT = 4

# --- 9. Battle HUD Fallback Positions (if no panel image is loaded) ---
BATTLE_HUD_FALLBACK_BASE_X = 50
BATTLE_HUD_FALLBACK_BASE_Y = 880
BATTLE_HUD_FALLBACK_HP_POS_X = 50
BATTLE_HUD_FALLBACK_HP_POS_Y = 50
BATTLE_HUD_FALLBACK_SPACING = 40

