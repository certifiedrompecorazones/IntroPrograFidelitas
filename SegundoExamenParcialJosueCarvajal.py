#PrimerProblemaExamen

V1 = []
V2 = []
V3 = []
x = 0

def llenar_vectores():
    def ordenar_vectores():
        V1.append(valor_V1)
        V3.append(valor_V1)
        V2.append(valor_V2)
        V3.append(valor_V2)
    for x in range(5):
        valor_V1 = int(input("Ingrese un numero para el vector 1:"))
        valor_V2 = int(input("Ingrese un numero para el vector 2:"))
        ordenar_vectores()

llenar_vectores()
print(V1)
print(V3)
print(V2)



#SegundoProblemaExamen

matriz = []
vector = []
for i in range(0,5):
    matriz.append([])
    for j in range(0,5):
        valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
        vector.append(valor)
print()



print("Matriz")
print()

for fila in matriz:
    print("[", end = " ")
    for elemento in fila:
        print(elemento, end = " ")
    print("]")
print

print()
print("Vector")
print()
print(vector)