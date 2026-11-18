def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float =0.4)-> float:
    if consumo_kwh < 0:
        raise ValueError("El nivel de consumo en Kw no puede encontrarse por debajo de 0")
    return consumo_kwh * factor_emision

