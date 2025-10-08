def calcular_area_circulo(radio):
    area = 3.1416 * (radio*radio)
    return area
    
def calcular_perimetro_circulo(radio):
    
    perimetro = 2 * 3.1416 * radio
    return perimetro

    
radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es {area:.2f}, y su perimetro es {perimetro:.2f}")
