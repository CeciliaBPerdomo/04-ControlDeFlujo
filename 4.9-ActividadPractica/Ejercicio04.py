# Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
cantidad = int(input("¿Cuántos números deseas ingresar? "))
if cantidad <= 0:
    print("Debes ingresar un número mayor que 0.")

else:
    suma = 0
    for i in range(cantidad):
        while True:
            num = int(input(f"Ingrese el número {i + 1}: "))
            break
        suma += num
    media = suma / cantidad
    print(f"La media aritmética de los números ingresados es: {media:.2f}")