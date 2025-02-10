# Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# 🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

# Todos los números del 0 al 10
lista1 = list(range(0, 11))
print("0 al 10:", lista1)

# Todos los números del -10 al 0
lista2 = list(range(-10, 1))
print("-10 al 0:", lista2)

# Todos los números pares del 0 al 20
lista3 = list(range(0, 21, 2))
print("Pares 0 al 20:", lista3)

# Todos los números impares entre -20 y 0
lista4 = list(range(-19, 0, 2))
print("Impares -20 a 0:", lista4)

# Todos los números múltiplos de 5 del 0 al 50
lista5 = list(range(0, 51, 5))
print("Múltiplos de 5 del 0 al 50:", lista5)
