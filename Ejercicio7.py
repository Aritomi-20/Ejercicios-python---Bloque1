minutos = int(input("Introduce los minutos totales:"))
horas = minutos // 60
minutos_sobrantes = minutos % 60
print (f"{minutos} minutos equivalen a {horas} horas y {minutos_sobrantes} minutos")