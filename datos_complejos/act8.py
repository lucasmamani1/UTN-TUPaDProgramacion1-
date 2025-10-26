productos = {'Leche': 7, 'Azucar': 6, 'Sal' : 8, 'Cafe': 4}

#consultar el stock de un producto ingresado
stock = input("Ingrese el producto del cual desea saber el stock : ")
if stock in productos:
    print(f"El producto que usted selecciono cuenta con el siguiente stock: {productos[stock]} unidades")
else: 
    print ("El producto que sugirio no existe.")

agregar_stock = input("Elija el producto al cual desea añadir unidades: ")

if agregar_stock in productos:
    print(f"Cuenta con {productos[agregar_stock]}")
    cuanto_stock = int(input("Ponga la cantidad que desea añadir: "))
    productos[agregar_stock] += cuanto_stock
    print(f"El producto que eligio ahora cuenta con el siguiente stock: {productos[agregar_stock]}")
else:
    print("El producto que usted ingreso no se encuentra en nuestra base de datos.")
    nombre = (input("Ingrese el nombre: "))
    stock1 = int(input("Ingrese el stock: "))
    productos[nombre] = stock1
print(productos)
    
    
    
    


