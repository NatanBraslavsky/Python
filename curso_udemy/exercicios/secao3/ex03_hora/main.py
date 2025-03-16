hora = int(input("Que horas são?"))
if 0 <= hora <= 11:
    print("Bom dia.")
elif 12 <= hora <= 17:
    print("Boa tarde.")
elif 18<= hora <= 23:
    print("Boa noite.")
else:
    print("Não é um horario.")