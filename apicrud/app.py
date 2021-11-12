from flask import Flask, url_for, redirect, request, jsonify
from models import *
import controller
import json
from serialisers import *


@app.route("/apicrud/<tipo>", methods=['GET'])
def get_method(tipo):
    if tipo == 'productos':
        data = controller.get_all(Producto)
        datos = jsonify([
                ProductoSerialiser.serialise(dato)
                for dato in data])
    if tipo == 'clientes':
        data = controller.get_all(Cliente)
        datos = jsonify([
                ClienteSerialiser.serialise(dato)
                for dato in data])
    ## REPLICAR PARA ORDENES
    return datos, 200

@app.route("/apicrud/<tipo>", methods=['POST'])
def post_method(tipo):
    datos = json.loads(request.data) 
    if (tipo == 'productos'):
        tipoModel = Producto
    if (tipo == 'clientes'):
        tipoModel = Cliente
    ## REPLICAR PARA CLIENTES, ORDENES
    controller.add_instance(tipoModel, datos)
    return json.dumps("Elemento Agregado "+str(datos)), 200

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0', debug=True)