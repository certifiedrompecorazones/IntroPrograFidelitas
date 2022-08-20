#Ejercicio2Examen
paciente_1 = 0
paciente_2 = 0
paciente_3 = 0
paciente_4 = 0 
cedula = 1
while cedula != 0:
    cedula = int(input("Ingrese su cedula:"))
    if cedula == 0:
        print ("Total de pacientes tipo 1",paciente_1)
        print ("Total de pacientes tipo 2",paciente_2)
        print ("Total de pacientes tipo 3",paciente_3)
        print ("Total de pacientes tipo 4",paciente_4)
        break 
    edad = int(input("Ingrese su edad:"))
    tipo_enf = int(input("Ingrese el tipo de enfermedad:"))
    if tipo_enf == 1:
        paciente_1 = paciente_1 + 1
        print ("GRIPE, Enviar a reposo por 3 dias")
    elif tipo_enf ==2:
        paciente_2 = paciente_2 + 1
        print ("APENDICITIS Enviar a cirugía")
    elif tipo_enf == 3:
        paciente_3 = paciente_3 + 1
        print ("DENGUE Envía a reposo por 5 días")
    else:
        paciente_4 = paciente_4 + 1
        print ("ENVIAR A ANALISIS")
