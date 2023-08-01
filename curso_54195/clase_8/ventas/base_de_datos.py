import json


class BaseDeDatos:

    def guardar_compras_de_cliente(self, cliente):
        # TAREA: no guardar el @coder.com (el dominio del mail) como nombre de archivo
        nombre_de_archivo = f"{cliente.email}.json"
        with open(nombre_de_archivo, "w") as outfile:
            compras_en_formato_texto = json.dumps(cliente.compras)
            outfile.write(compras_en_formato_texto)


    def cargar_compras_de_cliente(self, cliente):
        nombre_de_archivo = f"{cliente.email}.json"
        with open(nombre_de_archivo, "r") as infile:
            compras_en_formato_texto = infile.read()
            compras = json.loads(compras_en_formato_texto)

        return compras