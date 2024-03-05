from a_entidades import Persona, Empresa


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}

    def __str__(self):
        return f"Banco {self.nombre}"

    def crear_cuenta(self, cliente):
        self.cuentas[cliente.identificador] = 0

    def mostrar_todas_las_cuentas(self):
        return self.cuentas

    def transformar_cuentas_en_texto(self):
        texto = ""
        for identificador, saldo in self.cuentas.items():
            detalle = f"La cuenta {identificador} tiene saldo: {saldo}"
            texto = texto + detalle + "<br>"

        return texto

    def consultar_cuenta(self, cliente):
        pass

    def depositar_en_cuenta(self, cliente, monto):
        pass

    def consultar_saldo_en_cuenta(self, cliente):
        pass



# 1 - Crear un objeto "Banco"
mi_banco = Banco("Golden Brothers")
print(mi_banco)
print()

# 2 - Crear clientes
persona_1 = Persona("alberto", 22123233, 89, "al@berto.com")
empresa_1 = Empresa("Compumundo hipermegared", "20-1312312-12","compumundo@mundo.com")
print(persona_1)
print(empresa_1)
print()

# 3 - Crear cuentas

mi_banco.crear_cuenta(persona_1)
mi_banco.crear_cuenta(empresa_1)

print(mi_banco.mostrar_todas_las_cuentas())


