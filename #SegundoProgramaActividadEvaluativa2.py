#SegundoProgramaActividadEvaluativa2

precio_unitario = 0
iva = 0
cantidad = 0
impuesto = 0
preciofinal = 0
total = 0

while True:
    precio_unitario = float(input("Ingrese el precio unitario del producto:"))
    cantidad = int(input("Ingrese la cantidad de productos a comprar:"))
    impuesto = float(input("Digite 1 para IVA Tipo 1 - 2% de recargo, 2 para IVA de tipo 2 - 7% de recargo, 3 para IVA tipo 3 - 14% de recargo:"))
    if impuesto == 1:
        iva = precio_unitario * 0.02
        preciofinal = iva + precio_unitario
        break
    elif impuesto == 2:
        iva = precio_unitario * 0.07
        preciofinal = iva + precio_unitario
        break
    elif impuesto == 3:
        iva = precio_unitario * 0.14
        preciofinal = iva + precio_unitario
        break
total = preciofinal * cantidad
print("El total de la compra es:₡",total)

#AUTHOR:N0T-F0UND-404 https://github.com/N0T-F0UND-404