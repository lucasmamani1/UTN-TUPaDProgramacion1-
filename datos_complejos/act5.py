frase = input("Escriba una frase: ")
frase_separada = frase.split()
setear_frase = set(frase_separada)
print(setear_frase)

contador_palabras = {}
for p in frase_separada:
    if p in contador_palabras:
        contador_palabras[p] += 1
    else:
        contador_palabras[p] = 1

print("\nCantidad de veces que aparece cada palabra:")
print(contador_palabras)