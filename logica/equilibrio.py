class AnalizadorEquilibrio:
    def __init__(self, sesiones: list) -> None:
        self.sesiones: list = sesiones

    def calcular_volumen_por_musculo(self) -> dict:
        volumen_por_musculo = {}
        for sesion in self.sesiones:
            for ejercicio in sesion["ejercicios"]:
                musculo = ejercicio["musculo"]
                volumen = ejercicio["peso"] * ejercicio["serie"] * ejercicio["repeticiones"]
                if musculo not in volumen_por_musculo:
                    volumen_por_musculo[musculo] = 0.0
                volumen_por_musculo[musculo] += volumen
        return volumen_por_musculo

    def calcular_distribucion(self) -> dict:
        volumen_por_musculo = self.calcular_volumen_por_musculo()
        total = sum(volumen_por_musculo.values())
        
        distribucion = {}
        for musculo, volumen in volumen_por_musculo():
            distribucion[musculo] = round((volumen / total) * 100, 1)
        return distribucion

    def detectar_desbalance(self) -> str:
        distribucion = self.calcular_distribucion()
        musculos_bajos = []
        for musculo, porcentaje in distribucion.items():
            if porcentaje < 10.0:
                musculos_bajos.append(musculo)
        if len(musculos_bajos) == 0:
            return f"No se detectaron desbalances musculares"
        else:
            return f"Grupos musculares descuidados: {musculos_bajos}. Se recomienda trabajarlos mas."
        
