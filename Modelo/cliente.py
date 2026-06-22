class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.pedido = []

    def agregar_producto(self, producto):
        self.pedido.append(producto)

    def __str__(self):
        return f"Cliente: {self.nombre} | ID: {self.identificacion}"