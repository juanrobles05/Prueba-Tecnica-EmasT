from productoFisico import ProductoFisico
from productoDigital import ProductoDigital

productos = []

def agregar_producto(producto):
    productos.append(producto)

def obtener_productos():
    return productos

if __name__ == "__main__":

    producto1 = ProductoFisico("Camiseta", "Camiseta de algodón", 20.0, "Fisico", 100)
    producto2 = ProductoDigital("Ebook", "Libro digital en PDF", 10.0, "Digital", 0)

    agregar_producto(producto1)
    agregar_producto(producto2)

    for producto in obtener_productos():
        print(f"Nombre: {producto.obtenerNombre()}, Precio: {producto.obtenerPrecio()}, Tipo: {producto.obtenerTipo()}, Cantidad: {producto.obtenerCantidad()}")