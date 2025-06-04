class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Natan', 'Braslavsky')
# p1.nome = 'Natan'
# p1.sobrenome = 'Braslavsky'

p2 = Pessoa('Joana', 'Barros')
# p2.nome = 'Joana'
# p2.sobrenome = 'Barros'

print(p1)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)