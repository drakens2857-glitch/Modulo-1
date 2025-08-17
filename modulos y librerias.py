# mi_modulo.py
def saludar(nombre):
    return f"Hola {nombre}, desde mi módulo."

# usar_modulo.py
import math
import mi_modulo

print("Raíz cuadrada de 25:", math.sqrt(25))
print(mi_modulo.saludar("Nicolas"))

