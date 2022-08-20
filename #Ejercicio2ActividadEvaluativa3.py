#Ejercicio2ActividadEvaluativa3
suma = 0 
test={}
for x in range (0,10):
    valor = int(input("Digite algun numero:"))
    test[x] = valor
    suma = suma + valor
for x in range (10):
    print (test[x],end=" ")

print ("El total de la suma es de:",suma)