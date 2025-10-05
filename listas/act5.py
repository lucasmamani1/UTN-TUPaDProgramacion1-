estudiantes = ["Lucas", "Nair", "Mai", "Sofia", "Jorge", "Tomi", "Roman", "Severino"]

estudiante = ""

accion = input("Selecciona una opcion:\n1-Eliminar estudiante\n2-Agregar estudiante\n")

if accion == "1":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    estudiantes.remove(eliminar)
elif accion == "2":
    agregar = input("Ingrese el nombre del estudiante que desea agregar: ")
    estudiantes.append(agregar)
print(estudiantes)
    

