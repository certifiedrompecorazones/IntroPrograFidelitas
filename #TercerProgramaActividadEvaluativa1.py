#TercerProgramaActividadEvaluativa1
#En este programa ingresaremos el nombre de un alumno, notas de 4 quizes, 4 tareas, primer y segundo parcial. Luego se va a promediar las notas para obtener la nota final.
#Luego se va a presentar el nombre del alumno con el promedio correspondiente

#VAR

from time import sleep
print ("""
Se estara usando la siguiente rubrica:
Quizes 10%
Tareas 10%
Primer examen 40%
Segundo examen 40%
""")
print ()
print ("Por motivos de diseno, los valores admitidos para los quizes y tareas es de 0-5. Para los examenes, utilizar un rango de 0-100")

sleep(5)

estudiante = input("Ingrese el nombre del estudiante:")
quiz1 = int(input("Ingrese el puntuaje del primer quiz:"))
quiz2 = int(input("Ingrese el puntuaje del segundo quiz:"))
quiz3 = int(input("Ingrese el puntuaje del tercer quiz:"))
quiz4 = int(input("Ingrese el puntuaje del cuarto quiz:"))
tarea1 = int(input("Ingrese el puntuaje de la primera tarea:"))
tarea2 = int(input("Ingrese el puntuaje de la segunda tarea:"))
tarea3 = int(input("Ingrese el puntuaje de la tercera tarea:"))
tarea4 = int(input("Ingrese el puntuaje de la cuarta tarea:"))
primerexam = float(input("Ingrese el puntuaje del primer examen: "))
segundoexam = float(input("Ingrese el puntuaje del segundo examen: "))

#EXE

porcentajequiz1 = quiz1 * 5 / 10
porcetajequiz2 = quiz2 * 5 / 10
porcetajequiz3 = quiz3 * 5 / 10
porcetajequiz4 = quiz4 * 5 / 10
porcentajetarea1 = tarea1 * 5 / 10 
porcentajetarea2 = tarea2 * 5 / 10 
porcentajetarea3 = tarea3 * 5 / 10 
porcentajetarea4 = tarea4 * 5 / 10 
porcentajeexamen1 = primerexam * 40 / 100
porcentajeexamen2 = segundoexam * 40 / 100
promedio = porcentajequiz1 + porcetajequiz2 + porcetajequiz3 + porcetajequiz4 + porcentajetarea1 + porcentajetarea2 + porcentajetarea3 + porcentajetarea4 + porcentajeexamen1 + porcentajeexamen2

print("El estudiante",estudiante,"ha obtenido un promedio de:",promedio)

#AUTHOR:N0T-F0UND-404 https://github.com/N0T-F0UND-404