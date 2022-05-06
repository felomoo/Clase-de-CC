import random
placa = ""
for c in range(0,3):
    placaN1 = 0
    placaN1 = random.randint(0,9)
    placaN1str = str(placaN1)
    placa +=placaN1str
for c in range(0,3):
    placaL1 = ""
    placaL1 = chr(random.randint(ord("A"), ord("Z")))
    placaL1str = str(placaL1)
    placa+=placaL1str
print(placa)