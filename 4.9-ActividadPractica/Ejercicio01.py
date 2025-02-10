#¡Instrucciones e iteración!
# Realiza los ejercicios 1, 2, 3, 4, 5 y 6.
# Formato: Puedes completar estas consignas en un Google Docs o un link a tu Colabs.

# Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.
def suma():
    opcion3 = int(input('Ingresa un numero: '))
    opcion4 = int(input('Ingresa otro numero: '))

    total = opcion3 + opcion4
    print(f'La suma de {opcion3} y {opcion4} es igual a {total}.')

def resta():
    opcion5 = int(input('Ingresa un numero: '))
    opcion6 = int(input('Ingresa otro numero: '))

    total = opcion5 - opcion6

    print(f'La resta de {opcion5} y {opcion6} es igual a {total}.')

def multiplicacion():
    
    opcion5 = int(input('Ingresa un numero: '))
    opcion6 = int(input('Ingresa otro numero: '))

    total = opcion5 * opcion6

    print(f'La multiplicacion de {opcion5} y {opcion6} es igual a {total}.')

while True:
    print("\n📌 MENÚ DE OPERACIONES")
    print("1️⃣ Suma")
    print("2️⃣ Resta")
    print("3️⃣ Multiplicación")
    print("4️⃣ Finalizar")

    opcion = int(input("Selecciona una opción del menú: "))

    if opcion == 4:
        print("👋 Saliendo del programa...")
        break

    elif opcion == 1:
        suma()

    elif opcion == 2:
        resta()

    elif opcion == 3:
        multiplicacion()

    else:
        print("🚨 Opción inválida. Inténtalo de nuevo.")