# Datos iniciales 
edad = 15
antiguedad = 10
ingreso = 1500

if edad >= 18:
    if antiguedad >= 3:
        if ingreso > 2500:
            print("Credito aprobado")
        else:
            print("Credito no aprobado, el ingreso tiene que ser mayor a u$s2500")  
    elif antiguedad < 3: 
        if ingreso > 4000:
            print("Credito aprobado")
        else:
            print("Credito no aprobado, el ingreso tiene que ser mayor a u$s4000")
    else:
        print("Credito no aprobado")
else:
    print("Credito no aprobado, tiene que ser mayor de edad")