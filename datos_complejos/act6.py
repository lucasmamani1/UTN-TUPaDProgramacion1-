alumnos = {}

for i in range(3):
    alumno = input("Ingrese su nombre: ")
    print(f"Ingresá las 3 notas de {alumno}:")
    nota1 = float(input(f"Primer nota: "))
    nota2 = float(input(f"Segunda nota: "))
    nota3 = float(input(f"Tercer nota: "))
    alumnos[alumno] = (nota1, nota2, nota3)
print(alumnos)

alumno_promedio = input("Ingrese el nombre del alumno del cual le interese saber el promedio: ")
if alumno_promedio in alumnos:
    notas = alumnos[alumno]
    promedio = sum(notas) / len(notas)    
    print (f"El promedio del alumno es: {promedio}")
else: 
    print("El alumno que busca no se encuentra en esta clase.")