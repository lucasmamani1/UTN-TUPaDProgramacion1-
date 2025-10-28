with open("productos.txt", "r") as productos:
    lineas = productos.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")     
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
        
