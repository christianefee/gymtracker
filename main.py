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

# Cambio
