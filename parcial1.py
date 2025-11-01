
menu_biblioteca = ["1- Ingresar titulo",
                 "2- Ingresar ejemplares",
                 "3- Ver catalogo",
                 "4- Consultar disponibilidad",
                 "5- Ver ejemplares agotados",
                 "6- Agregar titulo",
                 "7- Actualizar ejemplares(prestamo/devolucion)",
                 "8- Salir"]

titulos = []
ejemplares = []

while True:
    for opcion in menu_biblioteca:
        print(opcion)
    seleccion =(input("Elija una opcion: "))

    match seleccion:
        #ingresar titulo
        case "1": 
            titulo = input("Ingresar titulo: ")
            while titulo in titulos or titulo == "":
                print("Este titulo ya existe o no es valido, ingrese otro")
                titulo = input("Ingrese un titulo nuevamente: ")
            else:
                print(f"Titulo ingresado con exito")  
                titulos.append(titulo)
                pos = titulos.index(titulo)
                ejemplares.insert(pos, 0)
                print(f"{titulos}")  
        #ingresar ejemplares
        case "2":
            if not titulos:
                print("No hay ningun titulo, primero debe añadir uno.")
                continue
        #Los for utilizados son para recorrer nuestra lista de titulos
            for i, titulo in enumerate(titulos):
                 print(f"{i+1}-{titulo}")    
        #Los inputs se pasan de str a int ya que si usamos un int-input
        #se nos podría llegar a romper el codigo, esto lo hace mas seguro
            pos_str = input("Ingrese a que titulo desea agregar ejemplares: ")    
            while not pos_str.isdigit() or int(pos_str) - 1 < 0 or int(pos_str) - 1 >= len(titulos):
                 print("Error, ingrese una opcion valida")
                 pos_str = input("Ingrese a que titulo desea agregar ejemplares: ")
                 
            pos = int(pos_str)-1
                    
            cant_str = input("Ingrese la cantidad de ejemplares que desea agregar: ")
            while not cant_str.isdigit():
                  print("Error debe ingregar un numero.")
                  cant_str = input("Ingrese la cantidad de ejemplares que desea agregar: ")
            cant = int(cant_str)
            ejemplares[pos]+= cant
            print(f"Stock actualizado -> {titulos[pos]} : {ejemplares[pos]}")
        #ver catalogo
        case "3":
                if not titulos:
                    print("Actualmente no tiene titulos en el catalogo")
                else:
                    print("El catalogo es el siguiente: ")
                    for i, titulo in enumerate(titulos):
                     print(f"{i+1}-{titulo}")
        #consulta disponibilidad
        case "4":
                if not titulos:
                    print("Actualmente no tiene titulos en el catalogo, ingrese uno desde el menu.")
                    continue
                    
                for i, titulo in enumerate(titulos):
                        print(f"{i+1}-{titulo}")
                        
                pos_str = input("Ingrese el numero del título que desea consultar: ")
                
                while not pos_str.isdigit() or int(pos_str) - 1 < 0 or int(pos_str) - 1 >= len(titulos):
                  print("Error, ingrese un numero que aparezca en la lista ")
                  pos_str = input("Ingrese el numero del título que desea consultar: ")

                pos = int(pos_str) - 1
                print(f"El titulo '{titulos[pos]}' cuenta con {ejemplares[pos]} ejemplares")
                continue
        #ver ejemplares agotados
        case "5":    
                if not titulos:
                    print("No hay ningun titulo, primero debe añadir uno.")
                    continue   
                agotados = False
                for i, cant in enumerate(ejemplares):
                        if cant == 0:
                           agotados = True
                           print (f"{titulos[i]} -> AGOTADO")
                if not agotados:
                        print("Por el momento hay stock en todos los titulos.")
                                           
        #agregar titulo
        case "6":
                titulo_agregado = input("Ingrese el titulo a agregar: ")
                while titulo_agregado in titulos:
                        titulo_agregado= input("El titulo que ingreso ya existe, ingrese un nuevo titulo: ")
                else:
                        titulos.append(titulo_agregado)
                        print(f"El titulo {titulo_agregado} fue añadido con exito")
                        cant_str = input("Ingrese la cantidad de ejemplares que desea agregar: ")
                        while not cant_str.isdigit():
                                print("Error, debe ingresar un numero.")
                                cant_str = input("Ingrese nuevamente la cantidad de ejemplares: ")
                        cant = int(cant_str)
                        ejemplares.append(cant)
                        print(f"Usted ingreso {cant} ejemplares para el titulo {titulo_agregado}.")
        #actualizar ejemplares
        case "7":
                if not titulos:
                    print("Actualmente no tiene titulos en el catalogo")
                    continue
                for i, titulo in enumerate(titulos):
                    print(f"{i+1}-{titulo}")
                pos_str = input("Ingrese el numero del titulo: ")
                while not pos_str.isdigit() or int(pos_str) - 1 < 0 or int(pos_str) - 1 >= len(titulos):
                  print("Error, ingrese un numero que aparezca en la lista ")
                  pos_str = input("Ingrese nuevamente el numero del titulo: ")
                pos = int(pos_str)-1
                tramite_str = input("Seleccione una opcion:\n1- Prestamo\n2- Devolucion\n")
                if tramite_str == '1':
                        if ejemplares[pos] > 0:
                               ejemplares[pos]-=1
                               print(f"Prestamo realizado, quedan {ejemplares[pos]} ejemplares del titulo {titulos[pos]}")
                        else:
                                print("No quedan ejemplares disponibles para realizar el prestamo.")
                if tramite_str == '2':
                        ejemplares[pos]+=1
                        print(f"Devolucion exitosa, stock actual de {titulos[pos]}: {ejemplares[pos]}")      
        #salir
        case "8":
                print("Cerrando el programa, hasta luego.")
                break 
        #opcioninvalida   
        case _ :
                print("Error, ingrese una opcion que sea valida(1-8)")

