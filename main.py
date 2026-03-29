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

def ver_historial() -> None:
    sesiones: list = cargar_sesiones()
    nombre_usuario: str = input("\nNombre de usuario: ")

    sesiones_usuario: list = []
    for sesion in sesiones:
        if sesion["usuario"] == nombre_usuario:
            sesiones_usuario.append(sesion)

    print(f"\n--- HISTORIAL DE {nombre_usuario.upper()} ---")

    for sesion in sesiones_usuario:
        print(f"\nSesion: {sesion['nombre']} | Fecha: {sesion['fecha']}")
        print("Ejercicios:")
        for ejercicio in sesion["ejercicios"]:
            print(f"  - {ejercicio['nombre']} | Musculo: {ejercicio['musculo']} | Peso: {ejercicio['peso']} kg | Series: {ejercicio['series']} | Reps: {ejercicio['repeticiones']}")

def analizar_progreso() -> None:
    sesiones: list = cargar_sesiones()
    nombre_usuario: str = input("\nNombre de usuario: ")

    sesiones_usuario: list = []
    for sesion in sesiones:
        if sesion["usuario"] == nombre_usuario:
            sesiones_usuario.append(sesion)

    if len(sesiones_usuario) == 0:
        print("No hay sesiones registradas para este usuario.")
        return

    nombre_ejercicio: str = input("Nombre del ejercicio a analizar: ")

    analizador: AnalizadorProgreso = AnalizadorProgreso(sesiones_usuario)
    resultado: str = analizador.detectar_estancamiento(nombre_ejercicio)
    print(f"\n{resultado}")

def generar_recomendacion() -> None:
    sesiones: list = cargar_sesiones()
    usuarios: dict = cargar_usuarios()
    nombre_usuario: str = input("\nNombre de usuario: ")

    if nombre_usuario not in usuarios:
        print("Usuario no encontrado.")
        return

    sesiones_usuario: list = []
    for sesion in sesiones:
        if sesion["usuario"] == nombre_usuario:
            sesiones_usuario.append(sesion)

    if len(sesiones_usuario) == 0:
        print("No hay sesiones registradas para este usuario.")
        return

    nombre_ejercicio: str = input("Nombre del ejercicio: ")
    peso_usuario: float = usuarios[nombre_usuario]["peso"]
    nivel: str = usuarios[nombre_usuario]["nivel"]

    recomendador: Recomendador = Recomendador(sesiones_usuario, peso_usuario, nivel)
    resultado: str = recomendador.generar_recomendacion(nombre_ejercicio)
    print(f"\n{resultado}")



    
## Estos def son para cargar y guardar en los JSON
