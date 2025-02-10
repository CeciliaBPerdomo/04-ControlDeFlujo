# Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100: 
# 🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. 
# El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

total = 0

for i in range(1, 100, 2):
    total = total + i

print(f'La suma de los numeros impares es {total}.')