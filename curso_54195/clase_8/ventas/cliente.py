from datetime import datetime


class Cliente():

    def __init__(self, email):
        self.compras = []
        self.email = email # esto es un atributo de instancia
        self.id = datetime.now().timestamp()

    def registrar_compra(self, producto, valor):
        self.compras.append(
            {"producto": producto, "valor": valor}
        )

    def imprimir_compras(self):
        if self.compras == []:
            print("No hay compras registradas")
        else:
            for compra in self.compras:
                print(compra)

    def __str__(self):
        return f"{self.email} ({self.id})"


