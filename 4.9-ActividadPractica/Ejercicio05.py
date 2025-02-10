# Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo: 
# 🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

numeros = [1, 3, 5, 7]
while True:
    num = int(input("Ingresa un número entero del 0 al 9: "))
    if 0 <= num >= 9:
        break  
    else:
        print("El número debe estar entre 0 y 9.")

    if num in numeros:
        print(f"✅ El número {num} está en la lista.")
    else:
        print(f"❌ El número {num} no está en la lista.")