import csv
from datetime import date
from . import FICHERO

CLAVES_IGNORADAS = ["errores"]

class Movimiento:
    def __init__(self, dic_datos):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(dic_datos["fecha"])
            hoy = date.today()
            if self.fecha > hoy:
                self.errores.append("La fecha no puede ser futura")
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

    def agregar(self, movimiento):
        self.movimientos.append(movimiento)
        self.guardar_archivo()

    def guardar_archivo(self):
        nombres = list(self.movimientos[0].__dict__.keys())
        for nombre in nombres:
            if nombre == CLAVES_IGNORADAS:
                nombres.remove(nombre)

        with open(FICHERO, "w") as fichero:
            writer = csv.DictWriter(fichero, nombres)
            writer.writeheader()
            for mov in self.movimientos:
                dic_mov = mov.__dict__
                for nombre in CLAVES_IGNORADAS:
                    dic_mov.pop(nombre)
                writer.writerow(dic_mov)

    def __str__(self):
        return f"Lista de {len(self.movimientos)} movimientos"

    def __repr__(self) -> str:
        return self.__str__()
