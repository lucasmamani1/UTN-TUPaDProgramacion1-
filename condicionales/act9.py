magnitud = int(input("Ingrese la magnitud del terremoto en una escala del 1 al 10: "))

if magnitud < 3 :
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4 :
    print ("Leve")
elif magnitud >= 4 and magnitud < 5 :
    print("Moderado")
elif magnitud >= 5 and magnitud < 6 :
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7 : 
    print("Muy fuerte")
else: 
    print("Extremo")