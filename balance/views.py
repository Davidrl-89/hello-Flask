from balance import app

@app.route('/')
def home():
    return "Pagina de inicio "

@app.route('/nuevo')
def nuevo():
    return "Creacion de movimiento"


@app.route('/modificar')
def actualizar():
    return "Actualizar movimiento"


@app.route('/borrar')
def borrar():
    return "Borrar movimiento"
