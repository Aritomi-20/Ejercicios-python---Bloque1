numero = int (input ("Introduce el numero factorial: "))

factorial=1

for i in range(1, numero+1):
    factorial=factorial*i

print(f"El factorial de {numero}! su resultado es {factorial}")
