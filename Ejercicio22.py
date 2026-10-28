import random

numero_secreto = random.randint (1,100)
intentos = 10
intentos_usados = 0

while intentos > 0:
    intento = int(input("Introduce el número: "))
    intentos_usados += 1
    intentos -= 1
    
    if intento == numero_secreto:
        print(f"El numero es correcto numero de intentos usados {intentos_usados} intentos")
        break
    elif intento < numero_secreto:
        print(f"El numero secreto es mayor. Te quedan {intentos} intentos.")
    else:
        print(f"El numero secreto es menor. Te quedan {intentos} intentos.")
if intentos==0 and intento != numero_secreto:
    print(f"Se acabaron los intentos. El número secreto era {numero_secreto}")
