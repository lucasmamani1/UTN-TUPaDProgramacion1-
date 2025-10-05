notas = [
    [7, 8, 9],
    [6, 9, 7],
    [5, 10, 7],
    [10, 9, 9],
    [5, 9, 6]
]

for i in range(5):
    sumaprom = 0
    for j in range(3):
        sumaprom += notas[i][j]
    promedio = sumaprom/3
    print (f"El promedio del estudiante {i + 1} es: {int(promedio)}")
    
for m in range(3):
    sumaprom = 0
    for i in range(5):
        sumaprom += notas[i][m]
    promedio = sumaprom/5
    print (f"El promedio de nota por materia es: Materia {m + 1}) {int(promedio)}")
        