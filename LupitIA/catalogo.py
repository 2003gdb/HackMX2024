class Producto:
    def __init__(self, nombre: str, promedioVentasSemanales: int, ventaSemanal: int, cantidadInventario: int, cantComprar: int):
        self.nombre = nombre
        self.promedioVentasSemanales = promedioVentasSemanales
        self.ventaSemanal = ventaSemanal
        self.cantidadInventario = cantidadInventario
        self.cantComprar = cantComprar
        self.ventasSemanales = []

class ListaTemp:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)
    
    def vaciar(self):
        self.productos = []
        print(len(self.productos))

    def largo(self):
        if len(self.productos)== 0:
            return -1
        else:
            return len(self.productos)

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.cantidadInventario)
    
    def buscar_producto_por_nombre(self, nombre: str):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None
