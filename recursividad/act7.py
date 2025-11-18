def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_base = int(input("Ingrese el numero de bloques en el nivel base: "))
        
if nivel_base < 1:
    print("Error: El numero debe ser mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"Para una piramide con {nivel_base} bloques en la base:")
    print(f"Total de bloques necesarios: {total}")
    secuencia = ""
    for i in range(nivel_base, 0, -1):
        secuencia += str(i)
        if i != 1:
            secuencia += " + "
    print(f"Secuencia: {secuencia} = {total}")
