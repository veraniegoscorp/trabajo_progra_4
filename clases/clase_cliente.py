from .clase_persona import persona
class cliente(persona):
    def __init__(self, nombre, email, rut, nivel,password): # type: ignore
        super().__init__(nombre, email, rut) # type: ignore
        contador_id_cliente = 1
        self.id_cliente = contador_id_cliente
        contador_id_cliente += 1
        self.nivel = nivel
        if nivel not in ("General", "estudiante"):
            nivel = "General"
        self.password = password


    def AplicarDescuento(self):
        return 0.90 if self.nivel == "estudiante" else 0.0
#aqui se representa en el diagrama el extend como la relacion padre-hijo con persona
