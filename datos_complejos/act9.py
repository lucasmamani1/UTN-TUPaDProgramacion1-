agenda = {
    ("lunes, 10:00"): "Reunion",
    ("martes, 15:00"): "Cursar",
    ("miercoles, 19:00"): "Futbol",
    ("viernes, 18:00"): "Merienda" 
}

consultar_agenda = input("Ingresar dia del cual desea saber si tiene algun evento pendiente: ")

if consultar_agenda == 'lunes':
    print (agenda['lunes, 10:00'])
elif consultar_agenda == 'martes':
    print(agenda['martes, 15:00'])       
elif consultar_agenda == 'miercoles':
    print(agenda['miercoles, 19:00'])
elif consultar_agenda == 'viernes':
    print(agenda[("viernes, 18:00")])
else:
    print("En el dia ingresado no tiene ningun evento pendiente")

