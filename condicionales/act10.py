

hemisferio = input("Ingrese en que hemisferio se encuentra N/S:")
mes = int(input("Ingrese el mes en el que se encuentra: "))
dia = int(input("Ingrese el dia: "))

match hemisferio:
    case "N": 
     if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        print ("Invierno")
     elif (mes == 3 and dia <= 21) or (mes <= 6 and dia <= 20):
        print("Primavera")
     elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Verano")
     elif (mes >= 9 and dia >= 21) or (mes <= 12 and dia <= 20): 
        print("Otoño")
    case "S":
        if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
            print ("Verano")
        elif (mes == 3 and dia <= 21) or (mes <= 6 and dia <= 20):
            print("Otoño")
        elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20):
            print("Invierno")
        elif (mes >= 9 and dia >= 21) or (mes <= 12 and dia <= 20): 
            print("Primavera")
        
        
    
