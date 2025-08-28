edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario < 12 :
    print("Niño/a.")
elif edad_usuario >= 12 and edad_usuario < 18: 
    print ("Adolescente.")
elif edad_usuario >= 18 and edad_usuario < 30:
    print ("Adulto joven.")
else:
    print ("Adulto.")