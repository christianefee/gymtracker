import numpy as np

class AnalizadorProgreso: 
    def __init__(self, sesiones: list) -> None:
        self.sesiones: list = sesiones
    
    def obtener_pesos_ejercicio(self, nombre_ejercicio: str) -> list:
        pesos = []
        for sesion in self.sesiones:
            for ejercicio in sesion["ejercicios"]:
                if ejercicio("nombre") == nombre_ejercicio:
                    pesos.append(ejercicio["peso"])
        return pesos
        pass

    def detectar_estancamiento(self, nombre_ejercicio: str) -> str:
        pesos: list = self.obtener_pesos_ejercicio(nombre_ejercicio)
        if len(pesos) < 3:
            return "No hay suficientes sesiones para analizar este ejercicio."
        ultimos_pesos: list = pesos[-3]
        diferencia: float = float(np.max(ultimos_pesos) - np.min(ultimos_pesos))
        if diferencia == 0:
            return f"Estancamiento detectado en {nombre_ejercicio}. Llevas 3 sesiones sin subir el peso"
        else:
            return f"Sigues progresando en {nombre_ejercicio}. Ultimo peso registrado: {pesos[-1]} kg."
        