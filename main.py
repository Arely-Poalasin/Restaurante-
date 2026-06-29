# Importación de clases desde otro módulo
from Modelo.producto import Producto
from Modelo.cliente import Cliente
from Servicios.restaurante import Restaurante

def main():
    # creación de objeto Producto

    producto_1= Producto(
        "Maito de tilapia",
        "Plato típico del Oriente",
        10,
        6.50,
        True
    )
    producto_2 = Producto(
        "Guayusa",
        "Bebida tradicional",
        15,
        1.25,
        True
    )



    # creación de objeto cliente
    cliente_1 = Cliente(
        "Arely Poalasin",
        "poalasin@gmail.com",
        18,
        True
    )
    
    cliente_2 = Cliente(
        "Juan Pascual",
        "juan07@gmail.com",
        20,
        True
    )


    # creación de un objeto Restaurante

    restaurante = Restaurante(
        "Sabor Amazonico"
    )


    #Registro de objetos en las listas
    restaurante.agregar_producto(producto_1)
    restaurante.agregar_producto(producto_2)

    restaurante.agregar.cliente(cliente_1)
    restaurante.agregar.cliente(cliente_2)

    # Visualizacion de la información
    # almacenada en las listas

    print("=== PRODUCTOS REGISTRADOS===")
    restaurante.mostrar_productos()

    print("\n=== CLIENTES REGISTRADOS===")
    restaurante.mostrar_clientes()

    #punto de incio del programa

    if __name__ == "__main__":
        main()
