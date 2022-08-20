import os
from ast import Or
from ctypes.wintypes import PINT
from time import sleep
from turtle import clear

def menu():
    clear
    print("  __  ___  _______   _________  ___________  ___   ___    _______________   ____    _  ___  __")
    print(" / / / / |/ /  _/ | / / __/ _ \/ __/  _/ _ \/ _ | / _ \  / __/  _/ ___/ /  / __ \  | |/_/ |/_/")
    print("/ /_/ /    // / | |/ / _// , _/\ \_/ // // / __ |/ // / _\ \_/ // (_ / /__/ /_/ / _>  <_>  <  ")
    print("\____/_/|_/___/ |___/___/_/|_/___/___/____/_/ |_/____/ /___/___/\___/____/\____/ /_/|_/_/|_|  ")
    sleep(1 )
    print ("Bienvenido al sistema de matricula de la Universidad Siglo XX, donde el futuro es hoy")
    sleep(1)
    print ("1. Matricula de estudiante")
    print ("2. Congelamiento")
    print ("3. Salir")
    opcion = str(input("Por favor selecciona una opcion:"))
    if opcion == "1": 
        clear
        matricula()
    elif opcion == "2":
        clear
        congelamiento()
    elif opcion == "3":
        exit
    else:
        print ("Opcion invalida")
        sleep(1)
        menu()
        
def materias():
    i = 0
    num_mat=int(input("A continuación, por favor ingrese la cantidad de materias que desea matricular el estudiante: "))
    C1P = 0
    C2P = 0
    C3P = 0
    C4P = 0
    C5P = 0
    C6P = 0
    C7P = 0
    C8P = 0
    C9P = 0
    C10P = 0
    C11P = 0
    C12P = 0
    C13P = 0
    C14P = 0
    C15P = 0
    C16P = 0
    C17P = 0
    C18P = 0
    C19P = 0
    C20P = 0
    C1V = 0
    C2V = 0
    C3V = 0
    C4V = 0
    C5V = 0
    C6V = 0
    C7V = 0
    C8V = 0
    C9V = 0
    C10V = 0
    C11V = 0
    C12V = 0
    C13V = 0
    C14V = 0
    C15V = 0
    C16V = 0
    C17V = 0
    C18V = 0
    C19V = 0
    C20V = 0
    for i in range (num_mat):
        curso = str(input("Ingrese el ID del curso (C1-C20) y al final agregue P para presencial o V para virtual, por ejemplo C1P: "))
        file= open("FileTest.txt", "a")
        file.write("\n")
        file.write(curso)
        file.close()
        if curso == "C1P":
            if C1P <=25:
                C1P = C1P + 1
            else:
                print("Curso lleno")
        elif curso == "C2P":
            if C2P <=25:
                C2P = C2P + 1
            else:
                print("Curso lleno")
        elif curso == "C3P":
            if C3P <=25:
                C3P = C3P + 1
            else:
                print("Curso lleno")
        elif curso == "C4P":
            if C4P <=25:
                C4P = C4P + 1
            else:
                print("Curso lleno")
        elif curso == "C5P":
            if C5P <=25:
                C5P = C5P + 1
            else:
                print("Curso lleno")
        elif curso == "C6P":
            if C6P <=25:
                C6P = C6P + 1
            else:
                print("Curso lleno")
        elif curso == "C7P":
            if C7P <=25:
                C7P = C7P + 1
            else:
                print("Curso lleno")
        elif curso == "C8P":
            if C8P <=25:
                C8P = C8P + 1
            else:
                print("Curso lleno")
        elif curso == "C9P":
            if C9P <=25:
                C9P = C9P + 1
            else:
                print("Curso lleno")
        elif curso == "C10P":
            if C10P <=25:
                C10P = C10P + 1
            else:
                print("Curso lleno")
        elif curso == "C11P":
            if C11P <=25:
                C11P = C11P + 1
            else:
                print("Curso lleno")
        elif curso == "C12P":
            if C12P <=25:
                C12P = C12P + 1
            else:
                print("Curso lleno")
        elif curso == "C13P":
            if C13P <=25:
                C13P = C13P + 1
            else:
                print("Curso lleno")
        elif curso == "C14P":
            if C14P <=25:
                C14P = C14P + 1
            else:
                print("Curso lleno")
        elif curso == "C15P":
            if C15P <=25:
                C15P = C15P + 1
            else:
                print("Curso lleno")
        elif curso == "C16P":
            if C16P <=25:
                C16P = C16P + 1
            else:
                print("Curso lleno")
        elif curso == "C17P":
            if C17P <=25:
                C17P = C17P + 1
            else:
                print("Curso lleno")
        elif curso == "C18P":
            if C18P <=25:
                C18P = C18P + 1
            else:
                print("Curso lleno")
        elif curso == "C19P":
            if C19P <=25:
                C19P = C19P + 1
            else:
                print("Curso lleno")
        elif curso == "C20P":
            if C20P <=25:
                C20P = C20P + 1
            else:
                print("Curso lleno")
        elif curso == "C1V":
            if C1V <=10:
                C1V = C1V + 1
            else:
                print("Curso lleno")
        elif curso == "C2V":
            if C2V <=10:
                C2V = C2V + 1
            else:
                print("Curso lleno")
        elif curso == "C3V":
            if C3V <=10:
                C3V = C3V + 1
            else:
                print("Curso lleno")
        elif curso == "C4V":
            if C4V <=10:
                C4V = C4V + 1
            else:
                print("Curso lleno")
        elif curso == "C5V":
            if C5V <=10:
                C5V = C5V + 1
            else:
                print("Curso lleno")
        elif curso == "C6V":
            if C6V <=10:
                C6V = C6V + 1
            else:
                print("Curso lleno")
        elif curso == "C7V":
            if C7V <=10:
                C7V = C7V + 1
            else:
                print("Curso lleno")
        elif curso == "C8V":
            if C8V <=10:
                C8V = C8V + 1
            else:
                print("Curso lleno")
        elif curso == "C9V":
            if C9V <=10:
                C9V = C9V + 1
            else:
                print("Curso lleno")
        elif curso == "C10V":
            if C10V <=10:
                C10V = C10V + 1
            else:
                print("Curso lleno")
        elif curso == "C11V":
            if C11V <=10:
                C11V = C11V + 1
            else:
                print("Curso lleno")
        elif curso == "C12P":
            if C12V <=10:
                C12V = C12V + 1
            else:
                print("Curso lleno")
        elif curso == "C13V":
            if C13V <=10:
                C13V = C13V + 1
            else:
                print("Curso lleno")
        elif curso == "C14V":
            if C14V <=10:
                C14V = C14V + 1
            else:
                print("Curso lleno")
        elif curso == "C15V":
            if C15V <=10:
                C15V = C15V + 1
            else:
                print("Curso lleno")
        elif curso == "C16V":
            if C16V <=10:
                C16V = C16V + 1
            else:
                print("Curso lleno")
        elif curso == "C17V":
            if C17V <=10:
                C17V = C17V + 1
            else:
                print("Curso lleno")
        elif curso == "C18V":
            if C18V <=10:
                C18V = C18V + 1
            else:
                print("Curso lleno")
        elif curso == "C19V":
            if C19V <=10:
                C19V = C19V + 1
            else:
                print("Curso lleno")
        elif curso == "C20V":
            if C20V <=10:
                C20V = C20V + 1
            else:
                print("Curso lleno")
        else:
            print("Opcion invalida")
    cost_mate=num_mat*120000 #precio materias sumadas
    pre_matr=70000 #precio matricula
    #desglose de resultados en base al dato ingresado
    if num_mat<2:
        print("El numero de materias ingresado no puede ser menor de 2.")
        materias()
    if num_mat>6:
        print("El numero de materias ingresado no puede ser mayor a 6.")
        materias()
    if num_mat<=3:
        print("El estudiante no aplica para un descuento.")
    if num_mat == 4:
        print("El estudiante recibira un descuento por materia de 10%, lo cual no incluye la matricula")
        des_diez=cost_mate*0.1 #descuento de 10%
        cost_mate=cost_mate-des_diez #cambio en el precio
    if num_mat == 5:
        print("El estudiante recibira un descuento por materia de 10%, lo cual no incluye la matricula")
        des_diez=cost_mate*0.1 #descuento de 10%
        cost_mate=cost_mate-des_diez #cambio en el precio
    if num_mat==6:
        print("El estudiante recibira un descuento por materia de 15% y por matrícula del 5%.")
        des_quin=cost_mate*0.15 #descuento de 10%
        cost_mate=cost_mate-des_quin #cambio en el precio
        des_cin=pre_matr*0.05 #descuento de 5%
        pre_matr=pre_matr-des_cin #cambio en el precio
    precio_finalm=str(cost_mate+pre_matr) #sumando materias con matricula
    file= open("FileTest.txt", "a")
    file.write("\n")
    file.write("Costo: ")
    file.write(precio_finalm)
    file.write("\n")
    file.write("-----------FIN-----------")
    file.close()
    print("El costo total de la matricula es de:",precio_finalm)
    
def matricula():
    clear
    nombre_estudiante = str(input("Por favor ingrese el nombre del estudiante a matricular: "))
    correo_estudiante = str(input("Por favor ingrese el correo del estudiante: "))
    num_estudiante = str(input("Por favor ingrese el numero telefonico del estudiante: "))
    opcion = str(input("Es correcta la informacion?(Si/No): "))
    if opcion == "Si":
            print ("Datos ingresados con exito")
            print ("Nombre:", nombre_estudiante)
            print ("Correo electronico:",correo_estudiante)
            print ("Numero telefonico:", num_estudiante)
            #SE GUARDA LA INFORMACION DEL ESTUDIANTE EN UN ARCHIVO QUE SE GENERA EN LA RUTA EN LA QUE SE EJECTUA EL PROGRAMA Y CON EL NOMBRE DEL ESTUDIANTE
            import os
            file= open("FileTest.txt", "a")
            file.write("\n")
            file.write("-----------INICIO-----------")
            file.write("\n")
            file.write("Nombre del Estudiante: ")
            file.write(nombre_estudiante)
            file.write("\n")
            file.write("Correo del Estudiante: ")
            file.write(correo_estudiante)
            file.write("\n")
            file.write("Numero del Estudiante: ")
            file.write(num_estudiante)
            file.write("\n")
            file.write("ID de cursos matriculados: ")
            file.close()
            materias()
            input("Presione Enter para continuar...")
            menu()
    elif opcion == "si":
            print ("Datos ingresados con exito")
            print ("Nombre:", nombre_estudiante)
            print ("Correo electronico:",correo_estudiante)
            print ("Numero telefonico:", num_estudiante)
            #SE GUARDA LA INFORMACION DEL ESTUDIANTE EN UN ARCHIVO QUE SE GENERA EN LA RUTA EN LA QUE SE EJECTUA EL PROGRAMA Y CON EL NOMBRE DEL ESTUDIANTE
            import os
            file= open("FileTest.txt", "a")
            file.write("\n")
            file.write("-----------INICIO-----------")
            file.write("\n")
            file.write("Nombre del Estudiante: ")
            file.write(nombre_estudiante)
            file.write("\n")
            file.write("Correo del Estudiante: ")
            file.write(correo_estudiante)
            file.write("\n")
            file.write("Numero del Estudiante: ")
            file.write(num_estudiante)
            file.write("\n")
            file.write("ID de cursos matriculados: ")
            file.close()
            materias()
            input("Presione Enter para continuar...")
            menu()
    elif opcion == "no":
            clear
            matricula() 
    elif opcion == "No":
            clear
            matricula()
    else:
            print ("Opcion invalida")
            sleep(3)
            matricula()
            
def congelamiento():
    matricula()
    file= open("FileTest.txt", "a")
    file.write("\n")
    file.write("^^^^^^^^^ESTE ESTUDIANTE SE ENCUENTRA CONGELADO^^^^^^^^^")
    file.close()

menu()