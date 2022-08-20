#SegundoProgramaActividadEvaluativa1
#Este programa va a solicitar al usuario 2 numeros los cuales seran almacenados en variables. Luego, esos numeros seran sumados y el resultado sera mostrado.
#Ademas de esto, se le volvera a preguntar al usuario por un tercer numero y sera multiplicado por el resultado de la suma de los dos numeros anteriores.

#VAR

print ("Hola, este es un programa el cual va a sumar 2 numeros y te va a dar el resultado de la suma")
print ("Ademas, te voy a pedir un tercer numero y lo voy a multiplicar por el resultado de la suma anterior y te voy a dar el resulado de la multiplicacion")

num_1 = float(input("Ingrese el primer numero a sumar: "))
num_2 = float(input("Ingrese el segundo numero a sumar: "))
suma = num_1 + num_2

#EXE

print ("El resultado de la suma es:",format(suma, '.4f'))

num_3 = float(input("Ahora ingresa un tercer numero para multiplicarlo por el resultado de la suma:"))

multi = suma * num_3

print ("El resultado de la multiplicacion es:",format(multi, '.4f'))

#AUTHOR:N0T-F0UND-404 https://github.com/N0T-F0UND-404