sueldo_base = int(input("Ingresar el sueldo base del vendedor: "))
venta1 = int(input("Monto de la primera venta: "))
venta2 = int (input("Monto de la segunda venta: "))
venta3 = int (input ("Monto de la tercera venta: "))

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.10
total_recibir = sueldo_base + comision

print (f"Total de ventas {total_ventas}")
print (f"Total de comision {comision}")
print (f"Total a recibir en el mes: {total_recibir}")
