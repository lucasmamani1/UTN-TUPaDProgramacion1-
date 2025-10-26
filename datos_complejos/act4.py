usuario = {}

for i in range(5):
    nombre = input("Ingrese su nombre: ")
    numero = int(input("Ingrese su numero: "))
    i+=1
    usuario[nombre] = numero
    


print (usuario)

nombre_agenda = input ("Ingrese el nombre del cual desea buscar el numero: ")

if nombre_agenda in usuario: 
    print(f"El numero de {nombre_agenda} es: {usuario[nombre_agenda]}")
else: 
    print("El dato que acaba de ingresar no se encuentra entre los usuarios registrados.")