minimas = [16, 20, 22, 15, 17, 21, 18]
maximas = [28, 27, 25, 29, 30, 32, 26]
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
vueltas_min = 0
vueltas_max = 0
temp_min = 0
temp_max = 0
while vueltas_min < 7:
    for temp in minimas:
        temp_min+=temp
        
        
        vueltas_min+=1
print(f"La temperatura minima promedio fue: {int(temp_min/7)}")

while vueltas_max < 7:
    for temp in maximas:
        temp_max+=temp
        vueltas_max+=1
print(f"La temperatura maxima promedio fue: {int(temp_max/7)}")

mayor_amplitud = 0
dia_amplitud = ""

for i in range(len(dias)):
    amplitud = maximas[i] - minimas[i]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = dias[i]

print(f"El día que más amplitud hubo fue {dia_amplitud} con {mayor_amplitud}° de amplitud.")










    
          

