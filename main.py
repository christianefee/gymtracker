import json
from modelos.usuario import Usuario
from modelos.ejercicio import Ejercicio
from modelos.sesion import Sesion
from modelos.ejercicios import EJERCICIOS
from logica.analizador import AnalizadorProgreso
from logica.recomendador import Recomendador
from logica.equilibrio import AnalizadorEquilibrio

ARCHIVO_USUARIOS: str = "datos/usuarios.json"
ARCHIVO_SESIONES: str = "datos/sesiones.json"

def cargar_usuarios() -> dict:
    with open(ARCHIVO_USUARIOS, "r") as archivo:
        return json.load(archivo)

def guardar_usuarios(usuarios: dict) -> None:
    with open(ARCHIVO_USUARIOS, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def cargar_sesiones() -> list:
    with open(ARCHIVO_SESIONES, "r") as archivo:
        return json.load(archivo)

def guardar_sesiones(sesiones: list) -> None:
    with open(ARCHIVO_SESIONES, "w") as archivo:
        json.dump(sesiones, archivo, indent=4)

