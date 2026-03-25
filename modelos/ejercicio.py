class Ejercicio:
    def __init__(self, nombre: str, musculo: str, peso: str, series: str, repeticiones: str):
        self.nombre: str = nombre 
        self.musculo: str = musculo
        self.peso: str = peso
        self.series: str = series
        self.repeticiones: str = repeticiones
        pass

    def calcular_volumen(self) -> float:
        return self.peso * self.series * self.repeticiones
    