## Actividad 1

### Guardar información del usuario

```python
def guardar_informacion(base_de_datos):
    usuario = input("Ingresar usuario: ")
    password = input("Ingresar password: ")
    base_de_datos[usuario] = password


base_de_datos = dict()
guardar_informacion(base_de_datos)
```

### Leer información del usuario

Dos ejemplos:

#### Versión 1

```python
def leer_informacion(base_de_datos):
    usuario = input("Ingresar usuario: ")
    password = base_de_datos[usuario]
    return password

password = leer_informacion(base_de_datos)
print(f"La contraseña es: {password}")
```

#### Versión 2

```python
def leer_informacion(base_de_datos):
    usuario = input("Ingresar usuario: ")
    password = base_de_datos.get(usuario, "No encontrada")
    return password

password = leer_informacion(base_de_datos)
print(f"La contraseña es: {password}")
```


### Login

```python

def login(base_de_datos):

    login_incompleto = True

    while login_incompleto:
        usuario = input("Ingresar usuario: ")
        password = input("Ingresar password: ")
        if base_de_datos.get(usuario) == password:
            login_incompleto = False

login(base_de_datos)

```

### Guardar a un archivo

```python
import json

def guardar_base_de_datos(base_de_datos, nombre_de_archivo):

    mi_archivo = open(nombre_de_archivo, "w")
    json.dump(base_de_datos, mi_archivo)
    mi_archivo.close()

guardar_base_de_datos(base_de_datos, "base_de_datos.json")
```

## Extra 1: login más inteligente

```python

def login(base_de_datos):

    intentos_restantes = 3
    login_incompleto = True

    while login_incompleto:
        if intentos_restantes == 0:
            print("No tiene más intentos")
            break
        usuario = input("Ingresar usuario: ")
        password = input("Ingresar password: ")
        if base_de_datos.get(usuario) == password:
            login_incompleto = False
        intentos_restantes = intentos_restantes - 1
    else:
        print("Login exitoso!")


login(base_de_datos)

```