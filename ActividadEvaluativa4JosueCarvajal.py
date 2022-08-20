#Primer Ejercicio
#Primer Matriz

matriz = []
for i in range(0,3):
    matriz.append([])
    for j in range(0,3):
        valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
print()

print("Primera matriz")
print()

for fila in matriz:
    print("[", end = " ")
    for elemento in fila:
        print(elemento, end = " ")
    print("]")
print

#Segunda Matriz

print()

print("Segunda matriz")
print()

print("[",matriz[0][0], matriz[1][0], matriz[2][0],"]")
print("[",matriz[0][1], matriz[1][1], matriz[2][1],"]")
print("[",matriz[0][2], matriz[1][2], matriz[2][2],"]")
print()

#Segundo Ejercicio
#Primer Matriz

matriz = []
matriz2 = []
suma = 0
for i in range(0,3):
    matriz.append([])
    matriz2.append([])
    for j in range(0,3):
        valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        suma = suma + valor
        matriz[i].append(valor)
        matriz2[i].append(suma)
print()

print("Primera matriz")
print()

for fila in matriz:
    print("[", end = " ")
    for elemento in fila:
        print(elemento, end = " ")
    print("]")
print

#Segunda Matriz

print()

print("Segunda matriz")
print()

for fila2 in matriz2:
    print("[", end = " ")
    for elemento2 in fila2:
        print(elemento2, end = " ")
    print("]")
print()