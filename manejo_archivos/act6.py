productos = []

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre = partes[0]
            precio = partes[1]
            cantidad = partes[2]
            productos.append({
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            })
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

modificar = input("¿Desea modificar algún producto?\n1- Si\n2- No\n")

while modificar.lower() == "si":
    nombre_modificar = input("Ingrese el nombre del producto que desea modificar: ")

    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_modificar.lower():
            print(f"Se encontro el producto buscado: {producto}")
            producto["precio"] = input("Actualice el precio: ")
            producto["cantidad"] = input("Actualice la cantidad: ")
            encontrado = True
            break

    if not encontrado:
        print("El producto que ingreso no se encuentra")

    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)

    modificar = input("¿Desea modificar otro producto?\n1- Si\n2- No\n")

print("Cerrando programa")