def info_personal():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad : "))
    residencia = input("Ingrese su residencia: ")
    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
info_personal()