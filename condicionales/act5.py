contrasenia_valida = str(input("Ingrese su contraseña: "))

len(contrasenia_valida)

if (len(contrasenia_valida)) >= 8 and (len(contrasenia_valida)) <= 14:
    print("Su contraseña es valida.")
else: 
    print("Su contraseña no es valida.")