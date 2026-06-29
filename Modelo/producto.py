class Producto:
    def __init__(self,
                 nombre:str,
                 descripcion:str,
                 cantidad: int,
                 precio:float,
                 disponible: bool
     ):
        # identificadores descriptivos para almacesar
        # la información de cada producto

        self.nombre = nombre
        self.descripcion = descripcion

        # tipo de datos numéricos
        self.cantidad = cantidad
        self.precio = precio

        #tipo de dato lógico

        self.disponible = disponible

    def mostrar_informacion(self)-> str:

        #Retornar una cadena de texto con la
        #información principal del producto

        return (
            f"Producto: {self.nombre}|"
            f"Descripcion:{self.descripcion}|"
            f"Cantidad: {self.cantidad}"
        )
    def __str__(self)-> str:

        # Representación en texto del objeto Producto

        return (
            f"{self.nombre}| "
            f"{self.descripcion}|"
            f"${self.precio}"
        )
