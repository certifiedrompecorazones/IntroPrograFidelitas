#TercerProgramaActividadEvaluativa2

i = 0
A = 0
B = 0
C = 0
D = 0
E = 0

for i in range (10):
    numero = int(input("Ingrese un digito:"))
    if numero < 0:
        A = A + 1
    elif numero >= 0 and numero < 50:
        B = B + 1
    elif numero >= 50 and numero <=100:
        C = C + 1
    elif numero >100 and numero <=150:
        D = D + 1
    elif numero >150:
        E = E + 1
total_numeros = A + B + C + D + E
print("La sumatoria de cada uno de los grupos es de:",total_numeros)
print("Para la categoria A, hubo:",A)
print("Para la categoria B, hubo:",B)
print("Para la categoria C, hubo:",C)
print("Para la categoria D, hubo:",D)
print("Para la categoria E, hubo:",E)

#AUTHOR:N0T-F0UND-404 https://github.com/N0T-F0UND-404