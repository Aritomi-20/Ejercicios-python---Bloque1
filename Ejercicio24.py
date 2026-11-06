suma = 0
cantidad = 0

while True:
    numero = int(input("Número: "))

    if numero == 0:
        break

    suma += numero
    cantidad += 1

if cantidad > 0:
    media = suma / cantidad
    print(f"Suma total {suma}")
    print(f"Media: {media}")
else:
    print ("No se introdujo ningún numero.")
