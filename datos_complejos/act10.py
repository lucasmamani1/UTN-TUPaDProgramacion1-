original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

invertido = {}

for p, provincia in original.items():
    invertido[provincia] = p
    
print(invertido)