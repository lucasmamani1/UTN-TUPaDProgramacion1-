vueltas = 0
productos = []

while vueltas < 5:
    producto = input("Cargue un producto: ")
    print (producto)
    vueltas +=1
    productos.append(producto)
    
productos_ordenados = sorted(productos)
print (productos_ordenados)

prod_eliminado = input("Ingrese cual de estos productos desea eliminar: ")
if prod_eliminado in productos: 
    productos.remove(prod_eliminado)
    print(f"El producto seleccionado: {prod_eliminado} fue eliminado con exito.")
    print(productos)

    



    
