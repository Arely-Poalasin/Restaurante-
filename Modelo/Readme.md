# Sistema de Gestión de Restaurante
Nombre: Arely Betzabe Poalasin Shiguango
Carrera: Tecnologías de la información
Asignatura: Programación Orientada a Objetos
Paralelo:"c"
## Descripción

Este proyecto consiste en una aplicación básica desarrollada en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes dentro de un restaurante, almacenando la información mediante objetos y organizando el código en diferentes módulos para facilitar su comprensión y mantenimiento.

## Estructura del Proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## Funcionalidades

* Crear objetos de tipo Producto.
* Crear objetos de tipo Cliente.
* Registrar productos en el restaurante.
* Registrar clientes en el restaurante.
* Mostrar la información almacenada.
* Organizar el programa mediante módulos y clases.

## Conceptos Aplicados

### Identificadores Descriptivos

Se utilizan nombres claros y significativos para clases, métodos, atributos y variables, facilitando la lectura y comprensión del código.

**Ejemplos:**

* `Producto`
* `Cliente`
* `Restaurante`
* `nombre`
* `descripcion`
* `agregar_producto()`
* `mostrar_informacion()`

### Tipos de Datos

Durante el desarrollo del programa se utilizan diferentes tipos de datos:

| Tipo    | Ejemplo                       |
| ------- | ----------------------------- |
| `str`   | nombre, categoria, correo     |
| `int`   | cantidad, edad                |
| `float` | precio                        |
| `bool`  | disponible, cliente_frecuente |

### Anotaciones de Tipos

Se emplean anotaciones de tipos para indicar el tipo de dato esperado en parámetros y valores de retorno.

```python
nombre: str
edad: int
precio: float
```

```python
def mostrar_informacion(self) -> str:
```

### Estructuras de Datos Compuestas

La clase `Restaurante` utiliza listas para almacenar múltiples objetos.

```python
self.productos = []
self.clientes = []
```

Estas estructuras permiten registrar varios productos y clientes dentro del sistema.

### Programación Orientada a Objetos

El proyecto aplica conceptos fundamentales de POO:

* Clases
* Objetos
* Atributos
* Métodos
* Modularidad

## Buenas Prácticas Aplicadas

* Uso de identificadores descriptivos.
* Organización del código en módulos.
* Separación de responsabilidades mediante clases.
* Uso de anotaciones de tipos.
* Comentarios claros para facilitar el aprendizaje.
* Función principal `main()` como punto de entrada del programa.

## Reflexión

El uso de Programación Orientada a Objetos permite desarrollar sistemas más organizados, reutilizables y fáciles de mantener. Además, utilizar identificadores descriptivos y tipos de datos adecuados facilita la comprensión del código y mejora la calidad del desarrollo del software.
