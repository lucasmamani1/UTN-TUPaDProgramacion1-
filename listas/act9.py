tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)


for fila in tablero:
    for celda in fila:
        print(celda, end = " ")
    print()
    
jugador = "X"
jugadas = 0

while jugadas < 9:
    print(f"Turno del jugador {jugador}")
        
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Movimiento no valido, intente de nuevo")
        print("Recuerde que solo son validos los movimientos 0-1-2")
        continue
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas+=1
    else:
        print("Casilla ocupada, intente de nuevo.")
        continue
    
    for fila in tablero:
        for celda in fila:
            print(celda, end = " ")
        print()
    
    if jugador == "X":
        jugador = "O"
    else: 
        jugador = "X"