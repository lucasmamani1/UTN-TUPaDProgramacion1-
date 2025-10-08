def seg_a_horas():
    hora = 3600
    seg = int(input("Ingrese los segundos que desea pasar a horas: "))
    hora = seg / hora
    return hora

segundos = seg_a_horas()
print(f"Los segundos que ingreso equivalen a {segundos}")

    