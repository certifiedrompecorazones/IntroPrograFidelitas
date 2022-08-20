#PrimerProgramaActividadEvaluativa2

total_kg = 0
total_lb = 0

for i in range (5):
    fardo = float(input("Por favor ingrese el peso del vardo en kilos: "))
    libras = fardo * 2.2
    print ("Peso ingresado en kilos:",fardo)
    print ("Peso convertido a libras:",format(libras, '.4f'))
    total_kg = total_kg + fardo
    print ("El total de kilos es de:",total_kg)
    total_lb = total_lb + libras
    print ("El total de libras es de:",total_lb)
    
promedio_kg = total_kg / 5
promedio_lb = total_lb / 5

print ("El promedio de kilos es de:",promedio_kg)
print ("El promedio de libras es de:",promedio_lb)

#AUTHOR:N0T-F0UND-404 https://github.com/N0T-F0UND-404