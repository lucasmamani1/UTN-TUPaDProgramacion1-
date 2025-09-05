from statistics import mode, median, mean
contador = 0
num = 0
sumanum = 0
media1= 0

while contador < 100:
    num = int(input("Ingrese un numero: "))
    sumanum += num
    
    contador +=1
print("La suma de los numeros es: ",sumanum)
media1 = sumanum/100
print("La media de los numeros sumados es: ",media1)
