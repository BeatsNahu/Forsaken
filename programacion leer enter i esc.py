import sys
import tty
import termios

def leer_una_tecla():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        tecla = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return tecla
while True:
    tecla = leer_una_tecla()
    print(f"Presionaste: {repr(tecla)}")  # repr para mostrar caracteres invisibles
    if tecla == '\x1b':  # Detectar esc
        print("Saliendo...")
        break
    elif tecla == '\r':  # Detectar enter
        print("wenas             a")

