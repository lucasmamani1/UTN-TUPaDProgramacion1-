aprobados_parcial1= {'Sofia', 'Nair', 'Mailen', 'Lucas', 'Jorge'}
aprobados_parcial2= {'Nair', 'Mailen', 'Lucas'}

aprobaron_ambos = aprobados_parcial1 & aprobados_parcial2
print(f"Aprobaron ambos parciales {aprobaron_ambos}")

aprobaron_uno = aprobados_parcial1 ^ aprobados_parcial2
print (f"Aprobaron solo un parcial: {aprobaron_uno}")

almenos_uno = aprobados_parcial1|aprobados_parcial2
print(f"Aprobaron almenos un parcial: {almenos_uno}")