from Modelo.producto import Producto
from Modelo.cliente import Cliente
from Servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Sazón Amazonico")

# Crear productos
p1 = Producto("Maito de tilapia", 5.50, "Plato")
p2 = Producto("Guayusa", 1.25, "Bebida")

restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)

# Crear cliente
c1 = Cliente("Arely Poalasin", "1550246738")
c1.agregar_producto(p1)

restaurante.registrar_cliente(c1)

# Mostrar información
print("=== PRODUCTOS ===")
restaurante.mostrar_productos()

print("\n=== CLIENTES ===")
restaurante.mostrar_clientes()