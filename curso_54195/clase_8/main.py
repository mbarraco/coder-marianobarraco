from ventas.cliente import Cliente
from ventas.base_de_datos import BaseDeDatos

cliente_1 = Cliente("mariano@coder.com")
cliente_2 = Cliente("nico@coder.com")
cliente_3 = Cliente("susana@coder.com")

cliente_1.registrar_compra("termo", 100)
cliente_1.registrar_compra("mate", 80)
cliente_1.registrar_compra("bombilla", 30)
cliente_1.registrar_compra("yerba", 5)
cliente_2.registrar_compra("termo", 100)
cliente_2.registrar_compra("mate", 80)
cliente_3.registrar_compra("bombilla", 30)
cliente_3.registrar_compra("yerba", 5)

bd = BaseDeDatos()
bd.guardar_compras_de_cliente(cliente_1)
bd.guardar_compras_de_cliente(cliente_2)
bd.guardar_compras_de_cliente(cliente_3)


cliente_messi = Cliente("lionel_messi@coder.com")

cliente_messi.imprimir_compras()

compras_de_messi = bd.cargar_compras_de_cliente(cliente_messi)
cliente_messi.compras = compras_de_messi
cliente_messi.imprimir_compras()
