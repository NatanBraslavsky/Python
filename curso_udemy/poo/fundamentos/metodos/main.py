class Carro:
    def __init__(self, nome ='Sei lá'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro(nome='celta')
celta.acelerar()
