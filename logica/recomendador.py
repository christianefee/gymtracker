from modelos.ejercicios import EJERCICIOS

class Recomendador:
    def __init__(self, sesiones: list, peso_usuario: float, nivel: str) -> None:
        self.sesiones: list = sesiones
        self.peso_ususario: float = peso_usuario
        self.nivel: str = nivel
        pass

    def obtener_pesos_ejercicio(self, nombre_ejercicio: str) -> list:
        pesos: list = []
        for sesion in self.sesiones:
            for ejercicio in sesion["ejercicios"]:
                if ejercicio["nombre"] == nombre_ejercicio:
                    pesos.append(ejercicio["peso"])
        return pesos
    
    def calcular_peso_objetivo(self, nombre_ejercicio: str) -> float:
        if nombre_ejercicio not in EJERCICIOS:
            return 0.0
        
        multiplicadores: tuple = EJERCICIOS[nombre_ejercicio]
        if self.nivel == "principiante":
            return self.peso_ususario * multiplicadores[1]
        elif self.nivel == "promedio":
            return self.peso_ususario * multiplicadores[2]
        else:
            return self.peso_ususario * multiplicadores[3]

    def generar_recomendacion(self, nombre_ejercicio: str) -> str:
        pesos: list = self.obtener_pesos_ejercicio(nombre_ejercicio)

        if len(pesos) < 3:
            return f"No hay suficientes sesiones para generar una recomendacion."
        
        peso_actual: float = pesos[-1]
        peso_objetivo: float = self.calcular_peso_objetivo(nombre_ejercicio)
        ultimos_pesos: list = pesos[-3:]

        todos_iguales: bool = len(set(ultimos_pesos)) == 1

        if peso_actual >= peso_objetivo:
            return f"Excelente nivel en {nombre_ejercicio}. Estas en tu peso objetivo o por encima ({peso_actual})"
        elif todos_iguales == True:
            nuevo_peso: float = peso_actual + 2.5
            return f"Llevas 3 sesiones con el mismo peso en {nombre_ejercicio}, intenta subir a {nuevo_peso} kg"
        else:
            diferencia: float = round(peso_objetivo - peso_actual, 1)
            return f"Vas muy bien en {nombre_ejercicio} campeon. Te faltan {diferencia} kg para alcanzar tu peso objetovo {peso_objetivo}."
        
