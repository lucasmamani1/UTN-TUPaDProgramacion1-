agregar = input("Desea agregar algun producto?\n-Agregar\n-Salir\n")
while True:
    if agregar == 'agregar':
        print("Ingrese los datos del producto: ")
        nombre = input("Ingresa el nombre: ")
        precio = input("Ingresa el precio: ")
        cantidad = input("Ingresa la cantidad: ")
        archivo_productos = open("productos.txt", "a")
        archivo_productos.write(f"{nombre},{precio},{cantidad}\n")
        archivo_productos.close()
        print("El producto ingresado fue cargado con exito.")
        with open("productos.txt", "r") as productos:
             lineas = productos.readlines()
             for linea in lineas:
                    partes = linea.strip().split(",")     
                    nombre = partes[0]
                    precio = partes[1]
                    cantidad = partes[2]
                    print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
        break
    elif agregar == 'salir':
        print("Cerrando programa")
        break
    else:
        print("Elija una de las opciones mencionadas por favor\n")
        break