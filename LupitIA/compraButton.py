from catalogo import Catalogo, Producto, ListaTemp

class CompraButton:
    def calcularAComprar(self, producto: Producto):
        producto.cantComprar = producto.cantidadInventario - producto.promedioVentasSemanales
    
    def calcularVentasSemanales(self, producto: Producto):
        sumatoria = 0
        for ventaSemanal in producto.ventasSemanales:
            sumatoria += ventaSemanal
        producto.promedioVentasSemanales = sumatoria/len(producto.ventasSemanales)

    def calculosVariables(self, producto: Producto):
        producto.ventasSemanales.append(producto.ventaSemanal)
        self.calcularVentasSemanales(producto)
        self.calcularAComprar(producto)
        producto.ventaSemanal = 0

    def mostrarCatalogo(self, catalogo: Catalogo):
        for producto in catalogo.productos:
            self.calculosVariables(producto)
            producto.cantidadInventario += int(input())
    
    def mostrarAComprar(self, catalogo: Catalogo):
        for producto in catalogo.productos:
            self.calcularAComprar(producto)




