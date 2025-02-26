class tienda:
    def __init__(self, producto, precio, fecha_v):
        self.producto = producto
        self.precio = precio
        self.fecha_v = fecha_v

    def mostrar_info(self):
        print(f"producto: {self.producto}")
        print(f"precio: {self.precio}")
        print(f"fecha_v: {self.fecha_v}")

    def disponible(self):
        print(f"El producto es {self.producto} y tiene un costo de {self.precio} y vence el {self.fecha_v} y esta disponible.")

    def no_disponible(self):
        print(f"El producto es {self.producto} y tiene un costo de {self.precio} y vence el {self.fecha_v} no esta disponible.")

producto1 = tienda("Leche", "7", "06/12/2025")
producto2 = tienda("yougurt", "5", "06/12/2024")
producto3 = tienda("Pollo", "12", "07/10/2021")
