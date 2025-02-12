opcion = int(input("Ingrese el año de nacimiento: "))

if opcion >= 1920 and opcion <= 1940:
    print("👋 Generacion silenciosa")
  
elif opcion >= 1941 and opcion <= 1964:
    print("👋 Baby Bommer")

elif opcion >= 1965 and opcion <= 1979:
    print("👋 Generacion X")

elif opcion >= 1980 and opcion <= 2000:
    print("👋 Generacion Y")

elif opcion >= 2001 and opcion <= 2010:
    print("👋 Generacion Y")

else:
    print("🚨 Año inválida. Inténtalo de nuevo.")