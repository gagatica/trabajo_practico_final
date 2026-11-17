import pandas

#Punto A
#ejemplo de entrada: {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
def limpiar_registro_sensor(registro_raw):
    datos_df = pandas.DataFrame(registro_raw)

    datos_df["sensor_id"] = datos_df["sensor_id"].str.strip()
    datos_df["temperatura"] = datos_df["temperatura"].str.lower()
    datos_df["temperatura"] = datos_df["temperatura"].str.replace("c", "")
    datos_df["temperatura"] = datos_df["temperatura"].str.replace(",", ".")
    datos_df["temperatura"] = datos_df["temperatura"].str.strip()
    datos_df["temperatura"] = pandas.to_numeric(datos_df["temperatura"])
    datos_df["ubicacion"] = datos_df["ubicacion"].str.strip()
    datos_df["ubicacion"] = datos_df["ubicacion"].replace("", pandas.NA).fillna("Planta Central")

    return datos_df.to_dict(orient="records")[0]

#Punto B
def generar_resumen_sensores(lista_sensores_limpios: list[dict], umbral_temperatura: float) -> tuple:
    temperaturas_acumuladas = 0
    ids_a_devolver = []
    
    for lectura in lista_sensores_limpios:
        temperaturas_acumuladas += lectura.get("temperatura")
        if umbral_temperatura < lectura.get("temperatura"):
            ids_a_devolver.append(lectura.get("sensor_id"))
            
    promedio_temperatura = temperaturas_acumuladas / len(lista_sensores_limpios)
    return (ids_a_devolver, promedio_temperatura)


lista_registros = [
    {
        "sensor_id": [" SENSOR-001 "], 
        "temperatura": ["24.5C"],
        "ubicacion": ["Planta Norte"]
    },
    {
        "sensor_id": [" SENSOR-002 "], 
        "temperatura": ["30.2C"],
        "ubicacion": ["Planta Norte"]
    },
    {
        "sensor_id": [" SENSOR-003 "], 
        "temperatura": ["11.0C"],
        "ubicacion": ["Planta Norte"]
    }
]

lista_sensores_limpios = []
for registro in lista_registros:
    lista_sensores_limpios.append(limpiar_registro_sensor(registro))

print (lista_sensores_limpios)
print (generar_resumen_sensores(lista_sensores_limpios, 20))