from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(4)]

media1= mean(numeros_aleatorios)
mediana1= median(numeros_aleatorios)    
moda= mode(numeros_aleatorios)

if media1 > mediana1 and mediana1 > moda :
    print(numeros_aleatorios, "Sesgo positivo")

elif media1 < mediana1 and mediana1 < moda : 
    print (numeros_aleatorios, "Sesgo negativo")

else:
       print(numeros_aleatorios, "Sin sesgo")
