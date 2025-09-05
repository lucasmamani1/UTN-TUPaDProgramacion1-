import random
num = 1
intentos = 0 
rand= random.randint(0, 9) 
acierto = False

while num != rand: 
  rand= random.randint(0, 9) 
  num = int(input("Ingrese un numero: "))
  print(num,"")
  print(rand,"")
  intentos += 1
  if num == rand:
   print("Usted adivino en ",intentos,"intentos.")
    







    