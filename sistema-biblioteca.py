import time
import csv
import os 
print(os.listdir())

ARCHIVO_LIBRO = "libros.csv"

#############FUNCIONES DENTRO DEL MENU#################
#3
def mostrar_catalogo():
    libros= []
    with open(ARCHIVO_LIBRO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            libros.append({"libro": fila["libro"], "stock": fila["stock"]})
    return  



#1
def ingresar_titulo():
    cantidad_libro = int(input("Ingresar la cantidad de titulos que desea ingresar: "))
    while cantidad_libro == 0:
        print("Opcion no valida, por favor ingrese un numero mayor que 0")
        return

#2    
def ingresar_ejemplar():
    pass

def mostrar_menu():
    while True: 
        print("1) Ingresar titulos")
        print("2) Ingresar ejemplares")
        print("3) Mostrar catalogo")
        print("4) Consultar disponibilidad")
        print("5) Titulos agotados")
        print("6) Agregar titulo")
        print("7) Actualizar ejemplares(prestamo/devolucion)")
        print("8) Salir")
        opcion = input("Ingrese una opcion: ").strip()
        
        match opcion: 
            case "1":
                ingresar_titulo()
                #Ingreso de titulos 
                pass
            case "2":
                ingresar_ejemplar()
                pass
            case "3":
                mostrar_catalogo()
                pass
            case "4":
                #Disponibles
                pass
            case "5":
                #Agotados
                pass
            case "6": 
                #Titulos nuevos
                pass
            case "7":
                #Actualizacion de ejemplares
                pass
            case "8":
                print("Gracias por visitar nuestra aplicacion")
                break
            case _:
                print("Opcion incorrecta, seleccione otra(1-8)")
                time.sleep(2)
                
                
                
mostrar_menu()