#Test

#MENU PRINCIPAL

from ast import Or
from ctypes.wintypes import PINT
from time import sleep
from turtle import clear

def matricula():
    clear
    nombre_estudiante = str(input("Por favor ingrese el nombre del estudiante a matricular: "))
    correo_estudiante = str(input("Por favor ingrese el correo del estudiante: "))
    num_estudiante = str(input("Por favor ingrese el numero telefonico del estudiante: "))
    opcion = str(input("Es correcta la informacion?(Si/No):"))
    if opcion == "Si":
            print ("Datos ingresados con exito")
            print ("Nombre:", nombre_estudiante)
            print ("Correo electronico:",correo_estudiante)
            print ("Numero telefonico:", num_estudiante)
            input("Presione Enter para continuar...")
            menu() #Por alguna razon python no esta llamando esta funcion, la cual no tira al menu principa.
    elif opcion == "si":
            print ("Datos ingresados con exito")
            print ("Nombre:", nombre_estudiante)
            print ("Correo electronico:",correo_estudiante)
            print ("Numero telefonico:", num_estudiante)
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
    menu()
    
#B.CANTIDAD DE MATERIAS
def materias():
    print(" ")
    num_mat=int(input("A continuación, por favor ingrese la cantidad de materias que desea matricular el estudiante: "))
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
    precio_finalm=cost_mate+pre_matr #sumando materias con matricula
    print("El costo total de la matricula es de:",precio_finalm)

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
opcion = str(input("Por favor selecciona una opcion:"))
if opcion == "1": 
    clear
    matricula()
else:
    print ("Opcion invalida")
    sleep(1)
    menu()