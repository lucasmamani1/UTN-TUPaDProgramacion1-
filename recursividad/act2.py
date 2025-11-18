def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

n = int(input("Ingrese la posicion hasta la que se desee mostrar la serie de Fibonacci: "))
    
if n < 0:
    print("Por favor, ingrese un numero positivo.")
else:
    print(f"\nSerie de Fibonacci hasta la posicion {n}:")
    print("-" * 40)
    
    # Mostrar la serie completa
    for i in range(n + 1):
        valor = fibonacci(i)
        print(f"Posicion {i}: {valor}")
