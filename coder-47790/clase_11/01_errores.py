def mi_func():
    raise Exception("este es mi mensaje!")


# intenta ejecutar lo siguiente: mi_func(). Si hay alguna excepcion
# avisale al programador por consola: "hubo un error en mi_func" y
# continua con la ejecucion del programa
try:
    mi_func()
except Exception:
    print("hubo un error en mi_func")

print("programa ejecutado exitosamente!")
