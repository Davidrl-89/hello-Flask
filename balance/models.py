import csv
from datetime import date, datetime
from . import FICHERO


class Movimiento:
    def __init__(self, dic_datos):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(dic_datos["fecha"])
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es valido")

        self.concepto = dic_datos["concepto"]
        self.tipo = dic_datos["tipo"]
        self.cantidad = dic_datos["cantidad"]
    
    def __str__(self):
        return "fecha: {} concepto: {} tipo: {} cantidad: {} ".format(
            self.fecha,
            self.concepto,
            self.tipo,
            self.cantidad
        )


   


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                #self.movimientos.append(linea)
                mov = Movimiento(linea)
                self.movimientos.append(mov)
