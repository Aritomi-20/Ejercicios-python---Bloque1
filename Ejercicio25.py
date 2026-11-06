while True:
    caracter = input("Introdice un caracter: ")
    
    if caracter == " ":
        print("Programa terminado.")
        break

    if caracter.lower() in "aeiou":
        print("VOCAL")

    else:
        print("NO VOCAL")
