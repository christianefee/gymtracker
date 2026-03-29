from modelos.ejercicio import Ejercicio

class Sesion:
    def __init__(self, nombre: str, fecha: str):
        self.nombre: str = nombre
        self.fecha: str = fecha
        self.ejercicios: list = []

    def agregar_ejercicio(self, ejercicio: Ejercicio):
        self.ejercicios.append(ejercicio)

    def calcular_volumen_total(self) -> float:
        total: float = 0
        for ejercicio in self.ejercicios:
            total += ejercicio.calcular_volumen()
        return total
