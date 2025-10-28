with open("productos.txt", "w") as productos:
    productos.write("manzana,250,30\n")
    productos.write("pan,500,20\n")
    productos.write("leche,950,15\n")
    
with open("productos.txt", "r") as productos:
    contenido = productos.read()
print(contenido)