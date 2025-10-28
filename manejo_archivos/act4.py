productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip() 
        partes = linea.split(",")
    
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1].strip()),
            "cantidad": int(partes[2].strip())
        }
        
        productos.append(producto)
for p in productos:
    print(p)
