notas = []
soma = 0
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}:"))
    notas.append(nota)
    soma += notas[i]
media = soma /3
print(media)

