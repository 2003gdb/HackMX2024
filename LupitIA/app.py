from flask import Flask, jsonify, request, render_template
from audio_recorder import recorder

from catalogo import Catalogo, ListaTemp
from ventaButton import VentaButton
from compraButton import CompraButton
from chatbot import InventoryAssistant

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/record', methods=['POST'])
def seVendio():
    filename = recorder.record_audio()  # Graba el audio y guarda el archivo
    text = recorder.recognize_audio()  # Realiza el reconocimiento de voz

    assistant = InventoryAssistant()
    entradaUsuario = text
    producto, cantidad = assistant.parse_instruction(entradaUsuario)
    
    ventabutton.seVendio(producto, int(cantidad), catalogo, lista_temp)
    return jsonify({"filename": filename, "text": text})  # Devuelve el texto reconocido

@app.route('/hacer-inventario/<int:indice>', methods=['POST'])
def hacer_inventario(indice):
    print(indice)
    for i in lista_temp.productos:
        print(i.nombre)
    print(lista_temp.largo())

    while indice < lista_temp.largo():
        producto = lista_temp.productos[indice]  # Acceso a lista_temp.productos
        
        # Simulación de grabación y procesamiento
        print(f"Grabando {producto.nombre}...")  # Para monitoreo en el backend
        filename = recorder.record_audio()
        text = recorder.recognize_audio()
        
        assistant = InventoryAssistant()
        cantidad = assistant.parse_instruction2(text)

        # Actualizar el inventario del producto
        if cantidad is not None and isinstance(cantidad, int) and cantidad >= 0:
            producto.cantidadInventario = cantidad
            print(f"Inventario actualizado para {producto.nombre}: {producto.cantidadInventario}")
        else:
            print(f"Valor inválido de cantidad para {producto.nombre}. Cantidad recibida: {cantidad}")

        # Respuesta para el frontend
        indice += 1
        if indice == lista_temp.largo():
            print("mismo largo")
            return jsonify({"fin": "Inventario actualizado completamente."})
        
        return jsonify({"grabando": f"Grabando {producto.nombre}", "nombre": producto.nombre, "cantidad": cantidad})
        
@app.route('/mostrar_inventario_a_comprar', methods=['GET'])
def mostrar_inventario_a_comprar():
    compraButton.mostrarAComprar(catalogo)
    productos_a_comprar = []
    for p in catalogo.productos:
        producto = {"nombre": p.nombre, "cantidad_a_comprar": p.cantComprar}
        productos_a_comprar.append(producto)
    
    return jsonify(productos_a_comprar)

# Ruta para mostrar el catálogo
@app.route('/mostrar_catalogo', methods=['GET'])
def mostrar_catalogo():
    productos = []
    for p in catalogo.productos:
        producto = {"nombre": p.nombre, "cantidad": p.cantidadInventario}
        productos.append(producto)
        print(p.nombre, p.cantidadInventario)

    return jsonify(productos)

@app.route('/obtener-producto/<int:indice>', methods=['GET'])
def obtener_producto(indice):
    if lista_temp.largo() == 0:
        return jsonify({"fin": "No hay productos para procesar, la lista ya está vacía."})
    elif indice < lista_temp.largo():
        producto = lista_temp.productos[indice]
        return jsonify({"nombre": producto.nombre})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

if __name__ == '__main__':
    catalogo = Catalogo()
    lista_temp = ListaTemp()
    
    ventabutton = VentaButton()
    compraButton = CompraButton()

    # Iniciamos la aplicación Flask
    app.run(debug=True, port=5001)

