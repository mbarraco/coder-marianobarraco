class Cliente:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


    def __str__(self):
        return f"Cliente: {self.email}"