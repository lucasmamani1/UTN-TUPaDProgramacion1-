

nombre = input("Ingrese su nombre: ")

c = nombre

mayus = int(input("Ingrese como quiere que se lea su nombre: 1) Mayuscula. 2)Minuscula. 3)Primer letra mayuscula."))

if mayus == 1 :
    c.upper()
    nombre_mayus = c.upper()
    print (f"Tu nombre es: ",nombre_mayus)
elif mayus == 2:
     c.lower()
     nombre_minus = c.lower()
     print(f"Tu nombre es: ", nombre_minus)
else: 
   c.title()
   nombre_title = c.title()
   print(f"Tu nombre es: ",nombre_title)