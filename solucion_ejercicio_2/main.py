import json, os
from pathlib import Path

class StockInvalidoError(Exception):
    """Excepción personalizada para indicar que el stock ingresado es inválido."""


class DispositivoEcológico:
    nombre : str
    __stock : int

    def __init__(self, nombre: str, stock: int):
        self.nombre = nombre
        self.stock = stock

    @property
    def stock(self): return self.__stock

    @stock.setter
    def stock(self, valor):
        try:
            self.__stock = int(valor)
            if int(valor) < 0:
                raise StockInvalidoError("El valor asignado a stock no debe ser negativo")
        except ValueError:
            raise StockInvalidoError("El valor asignado a stick debe ser numérico")
        except TypeError:
                    raise StockInvalidoError("El valor asignado a stock no debe ser nulo")

    def ficha_tecnica(self, imprimir: bool = False)-> str:
        ficha = f"nombre: {self.nombre} | stock: {self.stock}"

        if imprimir: print(ficha)
        return ficha

    def to_dict(self)-> dict:
        return {
            "nombre": self.nombre,
            "stock": self.stock
        }

class PanelSolar(DispositivoEcológico):
    modelo : str
    potencia : float

    def __init__(self, nombre: str, stock: int, modelo: str, potencia: float):
        super().__init__(nombre, stock)
        self.modelo = modelo
        self.potencia = potencia


    def ficha_tecnica(self, imprimir = False):
        ficha = super().ficha_tecnica()
        ficha += f" | modelo: {self.modelo} | potencia: {self.potencia}"

        if imprimir: print(ficha)
        return ficha

    def to_dict(self):
        dict = super().to_dict()
        dict["modelo"] = self.modelo
        dict["potencia"] = self.potencia

        return dict

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos: list[DispositivoEcológico | PanelSolar], ruta_archivo: str)-> bool:

        Path(ruta_archivo).mkdir(exist_ok=True)

        with open (ruta_archivo + "/catalogo_ecotech.json", "w") as archivo:
            lista_dispositivos_serializados = []
            for elemento in lista_dispositivos:
                lista_dispositivos_serializados.append(elemento.to_dict())
            json.dump(lista_dispositivos_serializados, archivo, indent= 4)

equipo_1 = DispositivoEcológico("preuba", 10)
equipo_2 = DispositivoEcológico("manolo", 5)

dispositivo_1 = PanelSolar("test_dispositivo_1", equipo_1.stock, "henrique", 110)
dispositivo_2 = PanelSolar("test_dispositivo_2", equipo_1.stock, "martin", 120)
dispositivo_3 = PanelSolar("test_dispositivo_3", equipo_1.stock, "carlo", 220)

print(equipo_1.to_dict())
print(dispositivo_2.to_dict())

lista_dispositivos =  [
    equipo_1,
    equipo_2,
    dispositivo_1,
    dispositivo_2,
    dispositivo_3
]

GestorInventario.guardar_catalogo_json(lista_dispositivos, "pruebas")