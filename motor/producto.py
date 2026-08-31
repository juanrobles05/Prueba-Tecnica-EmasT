class producto:

    def __init__(self, nombre, descripcion, precio, tipo, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        self.cantidad = cantidad

    def obtenerNombre(self):
        return self.nombre

    def obtenerPrecio(self):
        return self.precio

    def obtenerDescripcion(self):
        return self.descripcion

    def obtenerTipo(self):
        return self.tipo

    def obtenerCantidad(self):
        return self.cantidad

    def actualizarCantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizarPrecio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizarDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def calcularPrecioFinal(self):
        if self.tipo == "Digital":
            return self.precio * 0.15
        if self.cantidad > 50:
            return self.precio * 0.05