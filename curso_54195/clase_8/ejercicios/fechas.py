from datetime import datetime


# Calcular edad

def calcular_edad(nacimiento):
    ahora_mismo = datetime.now()
    edad = ahora_mismo - nacimiento
    print(edad)


nacimiento = datetime(year=1990, month=2, day=25, hour=7, minute=35, second=30)

calcular_edad(nacimiento)