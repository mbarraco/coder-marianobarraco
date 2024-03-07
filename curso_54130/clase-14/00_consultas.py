# Consulta de Matías Gonzalez
# Podemos ver lo del ejercicio del banco?
# La parte de consultar cuenta?

from b_banco import Banco
from a_entidades import Empresa, Persona


mi_banco = Banco("Matías Bank")
persona_1 = Persona("rogelia", 999, 34, "rogelia@gmail.com")
persona_2 = Persona("edgar", 777, 79, "edgar@gmail.com")
empresa_1 = Empresa("Nerv", 3434, "ikari@nerv.com")

print("todas las cuentas -> ", mi_banco.mostrar_todas_las_cuentas())

mi_banco.crear_cuenta(persona_1)
print("todas las cuentas -> ", mi_banco.mostrar_todas_las_cuentas())

mi_banco.crear_cuenta(persona_2)

print("todas las cuentas -> ", mi_banco.mostrar_todas_las_cuentas())

mi_banco.crear_cuenta(empresa_1)

print("todas las cuentas -> ", mi_banco.mostrar_todas_las_cuentas())


print("Cuenta de Rogelia -> ",  mi_banco.consultar_cuenta(persona_1))
mi_banco.depositar_en_cuenta(persona_1, 100)
print("Cuenta de Rogelia -> ",  mi_banco.consultar_cuenta(persona_1))
mi_banco.depositar_en_cuenta(persona_1, 94)
mi_banco.depositar_en_cuenta(persona_1, -70)
mi_banco.depositar_en_cuenta(persona_2, 1000)
mi_banco.depositar_en_cuenta(persona_2, -700)
print("Cuenta de Rogelia -> ",  mi_banco.consultar_cuenta(persona_1))
print("Cuenta de Edgar -> ",  mi_banco.consultar_cuenta(persona_2))


"""
pero persona_1 no se considera de tipo de dato persona?
o como hereda de cliente también se lo identifica asi
"""




"""
Thomas Mastrogiacomo to Everyone (7 Mar 2024, 19:12)
un nombre del cliente

Pablo Cala to Everyone (7 Mar 2024, 19:12)
una persona o una empresa

Valentino Zaninetti to Everyone (7 Mar 2024, 19:12)
un cliente

Esteban Gomez to Everyone (7 Mar 2024, 19:12)
Ahi no entiendo esa linea en la que sale cliente.identificador
"""