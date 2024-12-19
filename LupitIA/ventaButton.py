from catalogo import Catalogo, Producto, ListaTemp

class VentaButton:
    
    #Mejorar con thefuzz
    def existe(self, detectaNombreProducto: str, catalogo: Catalogo) -> bool:
        for producto in catalogo.productos:
            if producto.nombre == detectaNombreProducto:
                return True
        return False

    def seVendio(self, detectaNombreProducto: str, detectaCantProducto: int, catalogo: Catalogo, lista_temp: ListaTemp):
        if self.existe(detectaNombreProducto, catalogo):
            # Actualizar `ventaSemanal` si el producto ya está en el catálogo
            producto_existente = catalogo.buscar_producto_por_nombre(detectaNombreProducto)
            producto_existente.ventaSemanal += detectaCantProducto
            producto_existente.cantidadInventario -= detectaCantProducto
            print(f"Producto '{detectaNombreProducto}' ya existe. Cantidad vendida actualizada a: {producto_existente.ventaSemanal}")
            return

        # Crear un nuevo producto y agregarlo al catálogo
        nuevo_producto = Producto(
            nombre=detectaNombreProducto,
            promedioVentasSemanales=0, 
            ventaSemanal=detectaCantProducto,
            cantidadInventario=0,
            cantComprar=0
        )

        nuevo_producto.ventaSemanal += detectaCantProducto
        catalogo.agregar_producto(nuevo_producto)
        print(f"Producto '{nuevo_producto.nombre}' agregado al catálogo.")
        self.insertarListaTemp(nuevo_producto, lista_temp)

    def insertarListaTemp(self, producto: Producto, lista_temp: ListaTemp):
        # Checar si el producto ya está en lista_temp
        for item in lista_temp.productos:
            if item.nombre == producto.nombre:
                print(f"El producto '{producto.nombre}' ya está en la lista temporal.")
                return
        # Agregar el producto si no está en lista_temp
        lista_temp.agregar_producto(producto)
        print(f"Producto '{producto.nombre}' agregado a la lista temporal.")


