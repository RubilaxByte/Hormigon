from flask import Flask, render_template, request, redirect
from cliente_hormigon import ClienteHormigon

app = Flask(__name__)

@app.route('/')
def index():
    clientes = ClienteHormigon.obtener_clientes()
    return render_template('index.html', clientes=clientes)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    localidad = request.form['localidad']
    km_planta = request.form['km_planta']
    
    # Crear un nuevo objeto ClienteHormigon
    nuevo_cliente = ClienteHormigon(nombre, apellido, telefono, direccion, localidad, km_planta)
    
    # Guardar el cliente en la base de datos
    nuevo_cliente.guardar_en_bd()
    
    # Redirigir a la página principal
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)