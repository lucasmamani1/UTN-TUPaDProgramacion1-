num1 = int(input("Ingrese el primer numero: "))
print(num1)

num2 = int(input("Ingrese el segundo numero: "))
print(num2)

    
suma = 0

for sumados in range(num1+1, num2):
    suma += sumados

print("La suma total entre los numeros ingresados sin incluir los mismos es: ", suma)
