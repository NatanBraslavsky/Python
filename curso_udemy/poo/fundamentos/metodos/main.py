class Carro:
    def __init__(self, nome ='Sei lá'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
# fusca.acelerar()

celta = Carro(nome='celta')
# celta.acelerar()

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('leão')
# print(leao.comendo('maçã'))

class Camera():
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando')
            return
        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome}NÃO está filmando')
            return
        
        print(f'Parando de filmar...')
        self.filmando=False

    def fotografar(self):
        if self.filmando:
            print(f'Não pode fotografar enquanto está filmando')
            return
        print(f'{self.nome} está fotografando')
        

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()
c1.fotografar()


# print(c1.filmando)
# print(c2.filmando)