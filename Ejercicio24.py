cantidad = int(input("¿Cuántos números vas a introducir?"))

mayores = 0
menores = 0 
iguales = 0

for i in range(1, cantidad + 1):
    numero = int (input(f"Introduce el número {i}:"))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
print(f"Números mayores que 0: {mayores}")
print(f"Números menores que 0: {menores}")
print(f"Números iguales que 0: {iguales}")