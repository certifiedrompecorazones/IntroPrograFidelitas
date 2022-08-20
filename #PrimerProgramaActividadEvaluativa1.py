#PrimerProgramaActividadEvaluativa1
#Este programa va a leer el peso de un fardo en kilos y lo va a convertir a libras. Finalmente va a presentar el dato en kilos y libras.

#VAR
from time import sleep

print ("Hola este es un programa el cual convierte el peso de un fardo en kilos a libras")
sleep(3)
fardo = float(input("Por favor ingrese el peso del vardo en kilos: "))

#EXE

libras = fardo * 2.2

print ("Peso ingresado en kilos:",fardo)
print ("Peso convertido a libras:",format(libras, '.4f'))