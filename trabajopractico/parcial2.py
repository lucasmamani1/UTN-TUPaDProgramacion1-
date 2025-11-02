import time
import csv 

ARCHIVO_LIBRO = "libros.csv"
libros= [] #diccionario
nombres_libros = [] #verificar nombres para no duplicar
#############FUNCIONES DENTRO DEL MENU#################
#FUNCION PARA GUARDAR DATOS
def guardar_csv():
    with open(ARCHIVO_LIBRO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["libro", "stock"])
        for libro in libros:
            escritor.writerow([libro["libro"], libro["stock"]])


#CARGAR DATOS DEL CSV PARA TODAS LAS FUNCIONES
def cargar_datos():
    libros.clear()
    nombres_libros.clear()
    
    archivo = open(ARCHIVO_LIBRO, "a+", encoding="utf-8")
    archivo.seek(0) 
    contenido = archivo.read()
    if contenido.strip() == "": 
        archivo.write("libro,stock\n")
    archivo.close()

    archivo = open(ARCHIVO_LIBRO, "r", encoding="utf-8")
    lector = csv.DictReader(archivo)
    for fila in lector:
        if fila["libro"] != "" and fila["stock"].isdigit():
            libros.append({"libro": fila["libro"], "stock": int(fila["stock"])})
            nombres_libros.append(fila["libro"].lower())
    archivo.close()

    
#3
def mostrar_catalogo():
    if not libros:
        print("No hay libros cargados todavia.")
        return
    
    print("#### CATALOGO ####")
    for libro in libros:
        print(f"Libro: {libro['libro']} | Stock: {libro['stock']}")


#1
def ingresar_titulo():
    #cantidad de libros a ingresar
    cantidad_libros = input("Ingrese la cantidad de libros que desea ingresar: ")
    while not cantidad_libros.isdigit() or int(cantidad_libros) <= 0:
        print("Error, ingrese un numero mayor que 0.")
        cantidad_libros = input("Ingrese la cantidad de libros que desea ingresar: ").strip()
        
    cantidad_libros = int(cantidad_libros)
        #titulos añadidos
    for _ in range(cantidad_libros):
        titulo_libro = input("Ingrese el nombre del libro que desea agregar: ").lower().strip()
        if titulo_libro == "":
            print("No puede ingresar un titulo vacio.")
        elif titulo_libro in nombres_libros: 
            print("El titulo que ingreso ya existe en nuestra base de datos.")
        else: 
            nombres_libros.append(titulo_libro)
            libros.append({"libro": titulo_libro, "stock": 0})
            guardar_csv()
            print("Titulo agregado con exito.")
            
    
#2    
def ingresar_ejemplar():
    for i, libro in enumerate(libros):
        print(f"{i+1}- {libro['libro']} | Stock: {libro['stock']}")
    
    opcion = input("Elija el numero del libro al cual desea agregar ejemplares: ")    
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(libros):
        print("Numero invalido, elija una opcion del listado.")
        opcion = input("Ingrese nuevamente: ")
    opcion = int(opcion)
    opcion_seleccionada = libros[opcion -1]
    cantidad = input(f"Ingrese cuantos ejemplares desea agregarle al titulo '{opcion_seleccionada['libro']}': ")
    while not cantidad.isdigit() or int(cantidad) <= 0:
        print("Ingrese un numero valido mayor que 0.")
        cantidad = input("Cantidad: ")

    cantidad = int(cantidad)
    opcion_seleccionada['stock'] = int(opcion_seleccionada['stock']) + cantidad
    guardar_csv()

    print(f"Se agregaron {cantidad} ejemplares al titulo '{opcion_seleccionada['libro']}")

#4 
def consultar_disponibilidad():
    if not libros:
        print("No hay libros cargados.")
        return
    consulta = input("Ingrese el titulo del deseo que quiere consultar: ").lower().strip()
    if consulta == "":
        print("No se admiten espacios vacios")
        return
    encontrado = False
    for libro in libros:
        if consulta.lower() == libro['libro'].lower():
            encontrado = True
            if libro["stock"] > 0:
                print(f"El libro {libro['libro']} esta disponible, y cuenta con {libro['stock']} unidades.")
            else:
                print ("El libro no se encuentra disponible.")
                break
        
    if not encontrado:
            print("El libro que menciona no se encuentra en nuestro catalogo")
          
#5
def titulos_agotados():
    if not libros:
        print("No hay libros cargados.")
        return
    encontrado = False
    for libro in libros:
        if libro['stock'] == 0:
            print(f"El libro {libro['libro']} esta agotado.")
            encontrado = True
    if not encontrado:
        print("No hay libros agotados en el catalogo.")
    
            
#6
def agregar_titulo():
    titulo_nuevo = input("Ingresar el titulo que desea agregar: ").lower().strip()

    if titulo_nuevo == "":
        print("No se admiten espacios vacios, ingrese un titulo por favor.")
        return
    for libro in libros:
        if titulo_nuevo == libro['libro'].lower():
            print("Este libro ya se encuentra en el catalogo, por favor ingrese otro.")
            return
    print("El titulo que desea agregar, fue cargado exitosamente")
        
    numero_ejemplares = (input("Ingrese cuantos ejemplares desea agregar:")).strip()
    while not numero_ejemplares.isdigit() or int(numero_ejemplares) <= 0:
        print("Error, debe ingresar un numero mayor que 0.")
        numero_ejemplares = input("Vuelva a ingresar el numero de ejemplares, esta vez correctamente: ")
        
    numero_ejemplares = int(numero_ejemplares)
    
    libros.append({"libro": titulo_nuevo, "stock": numero_ejemplares})
    nombres_libros.append(titulo_nuevo)
    
    guardar_csv()

    print(f"El título '{titulo_nuevo}' fue cargado exitosamente con {numero_ejemplares} ejemplares.")
        
#7
def prestamos_devoluciones():
    if not libros:
        print("No hay libros cargados.")
        return
    accion = input("Ingrese una opcion: \n1- Prestamo.\n2- Devolucion.\n").lower().strip()
    if accion == "1" or accion == "prestamo":
        titulo_prestamo = input("Ingrese el titulo del cual desea solicitar prestamo: ")
        encontrado = False
        for libro in libros:
            if titulo_prestamo.lower() == libro['libro'].lower():
               encontrado = True
               cantidad = input(f"Ingrese cuantos ejemplares de '{libro['libro']}' desea obtener a prestamo: ").strip()
               while not cantidad.isdigit() or int(cantidad) <= 0:
                   cantidad = input("Error, ingrese un numero mayor que 0: ").strip()
               cantidad = int(cantidad)
               if cantidad > libro['stock']:
                    print(f"No hay suficiente stock. Solo hay {libro['stock']} unidades disponibles.")
               else:
                    libro['stock'] -= cantidad
                    print(f"Prestamo registrado. Se prestaron {cantidad} unidades de '{libro['libro']}'")
                    guardar_csv()
                    break
        if not encontrado:
            print("El libro que desea pedir prestado no se encuentra en nuestro catalogo.")
    elif accion == "2" or accion == "devolucion":
        encontrado = False
        titulo_devolucion = input("Ingrese el titulo del libro que desea devolver: ").lower().strip()
        for libro in libros:
            if titulo_devolucion.lower() == libro['libro'].lower():
                encontrado = True
                print("El titulo que desea devolver se encuentra en nuestro catalogo.")    
                num_devolucion = input("Ingrese la cantidad de ejemplares que desea devolver:").strip()
                while not num_devolucion.isdigit() or int(num_devolucion) <= 0:
                    num_devolucion = input("Error, ingrese un número mayor que 0: ").strip()
                num_devolucion = int(num_devolucion)
                libro['stock'] += num_devolucion
                print("La devolucion ha sido registrada con exito.")
        if not encontrado:  
            num_devolucion = input("El libro no estaba en el catalogo. Ingrese la cantidad de ejemplares a agregar: ").strip()
            while not num_devolucion.isdigit() or int(num_devolucion) <= 0:
                num_devolucion = input("Error, ingrese un número mayor que 0: ").strip()
            num_devolucion = int(num_devolucion)
            libros.append({"libro": titulo_devolucion, "stock": num_devolucion})
            nombres_libros.append(titulo_devolucion)
            print(f"El libro '{titulo_devolucion}' fue agregado con {num_devolucion} unidades.")
            guardar_csv()
    else:
        print("La opcion que eligio no esta permitida.")
        

def mostrar_menu():
    while True: 
        print("1) Ingresar titulos")
        print("2) Ingresar ejemplares")
        print("3) Mostrar catalogo")
        print("4) Consultar disponibilidad")
        print("5) Titulos agotados")
        print("6) Agregar titulo")
        print("7) Actualizar ejemplares(prestamo/devolucion)")
        print("8) Salir")
        opcion = input("Ingrese una opcion: ").strip()
        
        match opcion: 
            case "1":
                ingresar_titulo()
                
            case "2":
                ingresar_ejemplar()
                
            case "3":
                mostrar_catalogo()
                
            case "4":
                consultar_disponibilidad()
            case "5":
                titulos_agotados()
                
            case "6": 
                agregar_titulo()
                
            case "7":
                prestamos_devoluciones()
            case "8":
                print("Gracias por visitar nuestra aplicacion")
                break
            case _:
                print("Opcion incorrecta, seleccione otra(1-8)")
                time.sleep(2)
                
###########################################################################################################
  
cargar_datos()       
mostrar_menu()