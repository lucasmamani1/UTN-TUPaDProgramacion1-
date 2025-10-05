import random
vueltas = 0
nums = []

while vueltas < 15:
    num = random.randint(1,100)
    nums.append(num)
    vueltas+= 1
print(nums)

pares = []
impares = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)   
print(f"Los numeros pares son: {pares}")
print(f"Los numeros impares son: {impares}")
    