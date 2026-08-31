from producto import producto

class ProductoFisico(producto):
    def __init__(self, nombre, descripcion, precio, tipo, cantidad):
        super().__init__(nombre, descripcion, precio, tipo, cantidad)
        self.tipo = "Fisico"