class tienda:
    def __init__(self, producto, precio, fecha_v):
        self.producto = producto
        self.precio = precio
        self.fecha_v = fecha_v

    # Método para mostrar la información del auto
    def mostrar_info(self):
        print(f"producto: {self.producto}")
        print(f"precio: {self.precio}")
        print(f"fecha_v: {self.fecha_v}")

    # Método para arrancar el auto
    def disponible(self):
        print(f"El producto es {self.producto} y tiene un costo de {self.precio} y vence el {self.fecha_v} y esta disponible.")

    # Método para detener el auto
    def no_disponible(self):
        print(f"El producto es {self.producto} y tiene un costo de {self.precio} y vence el {self.fecha_v} no esta disponible.")

# Crear objetos de la clase Auto
producto1 = tienda("Leche", "7", "06/12/2025")
producto2 = tienda("yougurt", "5", "06/12/2024")

# Usar los métodos de los objetos
producto1.mostrar_info()
producto1.disponible()

print()  # Separador entre autos

producto2.mostrar_info()
producto2.no_disponible()