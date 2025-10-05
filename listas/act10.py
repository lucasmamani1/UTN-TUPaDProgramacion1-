ventas = [
    [5, 4, 7, 8, 9, 4, 10],  # Pan
    [12, 15, 8, 10, 11, 12, 9],  # Leche
    [6, 8, 9, 10, 7, 8, 9],  # Queso
    [14, 12, 10, 12, 10, 9, 13]   # Huevos
]

total_productos = []

for i in range(4):
    producto_total = 0
    for j in range(7):
        producto_total += ventas[i][j]
    total_productos.append(producto_total)
    print(f"Producto {i + 1} : {producto_total}")
 
#dia con mas ventas  
mayores_ventas = 0 
dia = 0
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    total_productos.append(producto_total)
    print(f"Total del dia {j + 1} : {total_dia}")
if total_dia > mayores_ventas:
    mayores_ventas = total_dia
    dia = j
print(f"El dia con mayor ventas fue el dia {j + 1}, con {mayores_ventas} ventas")

mayor_producto = 0
indice_prod = 0

for i in range(4):
    if total_productos[i] > mayor_producto:
        mayor_producto = total_productos[i]
        indice_prod = i
print(f"El producto que mas se vendio fue el producto {indice_prod + 1}, con {mayor_producto} ventas")
    
