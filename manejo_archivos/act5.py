buscar_producto = input("Ingrese el producto que esta buscando: ")
with open("productos.txt", "r") as productos:
    lineas = productos.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")     
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        if buscar_producto.lower() in partes[0].lower():
            print("Estos son los datos del producto que usted busca: ")
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
            break
    else:
        print("El producto que busca no se encuentra en nuestra lista de productos.")
            