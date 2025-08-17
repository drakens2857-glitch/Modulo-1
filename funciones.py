def saludar(nombre):
    """Función tradicional"""
    return f"Hola {nombre}"

doblar = lambda x: x * 2  # Función lambda

print(saludar("Negro"))
print("El doble de 5 es:", doblar(5))
