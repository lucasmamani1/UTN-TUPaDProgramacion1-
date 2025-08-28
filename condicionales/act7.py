vocales = "aeiouAEIOU"

frase_palabra = input("Ingrese una palabra: ")

if frase_palabra and frase_palabra[-1] in vocales:
    print(frase_palabra,"!")
else:
    print("",frase_palabra)
