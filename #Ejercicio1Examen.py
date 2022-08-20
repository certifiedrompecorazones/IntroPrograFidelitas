#Ejercicio1Examen

i = 0
total_colones = 0
total_dolar = 0
total_euro = 0
total_yen = 0

for i in range (5):
    colones = float(input("Ingrese la cantidada de colones:"))
    total_colones = total_colones + colones
    print("1.Dolar")
    print ("2.Euro")
    print ("3.Yen")
    tipo_mond = int(input("Seleccione la moneda a la cual desearia convertir:"))
    if tipo_mond == 1:
        tipo_camb = float(input("Ingrese el tipo de cambio de hoy:"))
        conv_dolar = colones/tipo_camb
        total_dolar = total_dolar + conv_dolar
        print ("El monto ingresado en colones es:",colones)
        print ("La moneda que escogio fue el Dolar")
        print ("El tipo de cambio que ingreso fue:",tipo_camb)
        print ("El monto a entregar es de:$",format(conv_dolar, '.2f'))
    elif tipo_mond == 2:
        tipo_camb = float(input("Ingrese el tipo de cambio de hoy:"))
        conv_euro = colones/tipo_camb
        total_euro = total_euro + conv_euro
        print ("El monto ingresado en colones es:",colones)
        print ("La moneda que escogio fue el Euro")
        print ("El tipo de cambio que ingreso fue:",tipo_camb)
        print ("El monto a entregar es de:€",format(conv_euro, '.2f'))
    elif tipo_mond == 3:
        tipo_camb = float(input("Ingrese el tipo de cambio de hoy:"))
        conv_yen = colones/tipo_camb
        total_yen = total_yen + conv_yen
        print ("El monto ingresado en colones es:",colones)
        print ("La moneda que escogio fue el Yen")
        print ("El tipo de cambio que ingreso fue:",tipo_camb)
        print ("El monto a entregar es de:¥",format(conv_yen, '.2f'))

    else:
        print ("Opcion invalida, vuelva a intentar")

print ("El total de colones recibidos fueron:₡",total_colones)
print ("El total de dolares entregados fueron:$",total_dolar)
print ("El total de euros entregados fueron:€",total_euro)
print ("El total de yenes entregados fueron:¥",total_yen)