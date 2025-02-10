# Escribe un programa que lea un número impar por teclado. 
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

while True:
    opcion = int(input("Ingresa un número impar (o 0 para salir): "))

    if opcion == 0:
        print("👋 Saliendo del programa...")
        break
    
    if opcion % 2 == 0:
        print("🚨 Ese número es par. Intenta de nuevo.")
    else:
        print("✅ ¡Bien! Ingresaste un número impar.")