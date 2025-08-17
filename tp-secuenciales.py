1.
print("Hola mundo")


2.

nombre = (input("Ingrese su nombre: "))
print ("Hola", nombre,"!")

3.

nombre = (input("Ingrese su nombre: "))  
apellido = (input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
residencia = (input("Ingrese su lugar de residencia: "))

print("Soy", nombre, apellido," de", edad," años y vivo en ", residencia)

4.

radio = int(input("Ingrese el radio de un circulo: "))
area = 3.1416 * (radio*radio)
perimetro = 2 * 3.1416 * radio

print ("El area del circulo segun su radio es: ", area)
print ("El perimetro del circulo segun su radio es: ", perimetro)

5.

seg = int(input("Ingrese la cantidad de segundos que desea pasar a hora: "))

hora = 3600

horaseg = seg / hora

print ("Los segundos indicados equivalen a ",horaseg, "hs")

6.

num= int(input("Ingrese un numero a multiplicar: "))
multiplicar = +1

for i in range (1,11):
    print(f"{num}*{i} = {num*i}")


7.

num1= int(input("Ingrese el primer numero(Los numeros ingresados deben ser distintos de 0):"))
num2= int(input("Ingrese el segundo numero: "))

print("Los numeros sumados son : ",(num1+num2))
print("Los numeros restados son : ",(num1-num2))
print("Los numeros multiplicados son : ",(num1*num2))
print("Los numeros dividos son : ",(num1/num2))

8.

peso= float(input("Ingrese su peso: "))
altura= float(input("Ingrese su altura: "))

print("Su IMC es: ",peso/(altura*altura))

9.

celsius = float(input("Ingrese los grados que desea pasar a fahrenheit: "))

fahrenheit = (celsius*9/5)+32

print("Los grados indicados en fahrenheit serían: ",fahrenheit)

10.

num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))

promedio = (num1+num2+num3)/3

print("El promedio de estos numeros es: ", promedio)



