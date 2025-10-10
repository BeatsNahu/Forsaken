import sys, os
from pathlib import Path
print("PWD:", os.getcwd())
print("sys.path[0]:", sys.path[0])
print("sys.path (head):", sys.path[:3])
print("Archivo main.py en:", Path(__file__).resolve())
