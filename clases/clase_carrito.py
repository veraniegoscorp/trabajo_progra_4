from .clase_itemcarrito import item_carrito

# module-level counter for carrito IDs
_carrito_counter = 1


class carrito:
    def __init__(self, cliente) -> None:  # type: ignore
        global _carrito_counter
        self.id_carrito = _carrito_counter
        _carrito_counter += 1
        self.cliente = cliente
        self.items: list[item_carrito] = []
        self.subtotal: float = 0.0
        self.descuento_aplicado: float = 0.0
        self.total: float = 0.0

    def agregar_items(self, producto, cantidad) -> None:  # type: ignore
        item = item_carrito(producto, cantidad)  # type: ignore
        self.items.append(item)
        self.calcular_subtotales()

    def calcular_subtotales(self):
        self.subtotal = sum(item.subtotal for item in self.items)
    
    def calcularTotal(self):
        descuento = self.cliente.AplicarDescuento() # type: ignore
        self.descuento_aplicado = round(self.subtotal * descuento,2) # type: ignore
        self.total = round(self.subtotal - self.descuento_aplicado, 2) # type: ignore

    def ticket(self):
        self.calcular_subtotales()
        self.calcularTotal()

        print("=== TICKET DE COMPRA ===")
        print(self.cliente.get_resume()) # type: ignore
        print("------------------------")
        for item in self.items:
            print(f"{item.producto.nombre} x{item.cantidad} "
                  f"= ${item.subtotal}")
        print("------------------------")
        print(f"Subtotal: ${self.subtotal}")
        print(f"Descuento aplicado: ${self.descuento_aplicado}") # type: ignore
        print(f"TOTAL A PAGAR: ${self.total}") # type: ignore
        print("========================")
#composicion porque carrito no puede existir sin items carrito
#ademas de que los items carrito son parte permanente de carrito no pueden existir por si solos
#item = item_carrito(producto,cantidad)

#la asociacion es porque carrito y cliente son clases independientes que se relacionan entre si
#carrito tiene un atributo cliente que hace referencia a un objeto de la clase cliente
#pero ninguno depende del otro para existir
#self.cliente = cliente


