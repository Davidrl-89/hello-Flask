from flask import render_template

from . import app
from .models import ListaMovimientos


@app.route('/')
def home():
    """
    Nuestra lista de movimientos guardados
    """
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/nuevo')
def nuevo():
    return "Creacion de movimiento"


@app.route('/modificar')
def actualizar():
    return "Actualizar movimiento"


@app.route('/borrar')
def borrar():
    return "Borrar movimiento"
