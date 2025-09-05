contador = 0
num = 0

while contador < 100:
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        print("Ingreso un numero par.")
    elif num % 2 == 1:
        print("Usted ingreso un numero impar.")
    
    if num > 0:
        print("El numero es positivo.")
    else:
        print("El numero es negativo.")
    contador += 1


    