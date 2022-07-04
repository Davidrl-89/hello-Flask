from flask import Flask 

app = Flask(__name__)

"""
para ejecutar la app de Flask necesitamos un servidor web.
Flask nos proporciona una para desarrollo pero necesitamos un par
de variables

- Mac
    export  FLASK_APP=hello
    export  FLASK_ENV=development

"""


@app.route('/')
def hola():
    return "hola, soy Flask , y tu ¿como te llamas? "

@app.route('/adios')
def otra():
    return "Hasta luego"
