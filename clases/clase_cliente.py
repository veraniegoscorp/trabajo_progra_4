# Clase cliente
from .clase_persona import persona

# module-level counter to generate simple numeric IDs in-memory
_cliente_counter = 1


class cliente(persona):
    def __init__(self, nombre: str, email: str, rut: str, nivel: str, password: str) -> None:  # type: ignore
        global _cliente_counter
        super().__init__(nombre, email, rut)  # type: ignore
        self.id_cliente: int = _cliente_counter
        _cliente_counter += 1
        self.nivel = nivel
        if nivel not in ("General", "estudiante"):
            self.nivel = "General"
        self.password = password

    def AplicarDescuento(self) -> float:
        return 0.90 if self.nivel == "estudiante" else 0.0
#aqui se representa en el diagrama el extend como la relacion padre-hijo con persona
