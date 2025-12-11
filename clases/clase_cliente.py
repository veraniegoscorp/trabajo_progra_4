from .clase_persona import persona
class cliente(persona):
    def __init__(self, nombre, email, rut, id_cliente, nivel): # type: ignore
        super().__init__(nombre, email, rut) # type: ignore
        self.id_cliente = id_cliente
        if nivel not in ("General", "estudiante"):
            nivel = "General"
        self.nivel = nivel

    def AplicarDescuento(self):
        return 0.90 if self.nivel == "estudiante" else 0.0
#aqui se representa en el diagrama el extend como la relacion padre-hijo con persona