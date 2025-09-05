num = int(input("Ingrese un numero: "))
sumanum = 0

for num in range (0,num):
    sumanum= sum(range(num+1))
    
print("Los numeros sumados dieron como resultado: ",sumanum)