def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un numero entero positivo: "))
    
if numero < 1:
    print("Ingrese un numero positivo.")
else:
    print(f"\nFactoriales de los numeros del 1 al {numero}:")
    
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")