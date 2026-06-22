class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        for p in self.productos:
            print(p)

    def mostrar_clientes(self):
        for c in self.clientes:
            print(c)