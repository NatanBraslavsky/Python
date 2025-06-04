class Carro:
    def __init__(self, nome ='Sei lá'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro(nome='celta')
celta.acelerar()

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('leão')
print(leao.comendo('maçã'))