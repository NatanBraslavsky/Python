'''class Aluno:
    def __init__(self,nome, idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f'Olá!Boa noite!Meu nome é {self.nome},tenho {self.idade} anos e estudo  {self.curso}')

    def maioridade(self):
        if self.idade >= 18:
            print(f'{self.nome} é maior de idade!')
        else:
            print(f'{self.nome} é menor de idade!')


aluno1 = Aluno('Thereza', 15,'Python')
aluno1.apresentar()

aluno2 = Aluno('Gustavo', 21,'Java')
aluno2.apresentar()
aluno1.maioridade()
aluno2.maioridade()

#-------------------------------------------------------------------

class Aluno:
    def __init__(self,nome, idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def apresentar(self):
        print(f'Olá!Boa noite!Meu nome é {self.nome},tenho {self.idade} anos e estudo  {self.curso}')

    def adiconar_notas(self,nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print('Nota inválida.Insira uma nota entre 0 e 10.')

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        print(f'A media do aluno(a) {self.nome}: {media:.2f}')
        if media >= 7:
            print(f'{self.nome} foi aprovado!')
        else:
            print(f'{self.nome} foi reprovado!')

aluno1 = Aluno('Thereza', 15,'Python')
aluno1.apresentar()
aluno1.adiconar_notas(5.9)
aluno1.adiconar_notas(4.5)
aluno1.adiconar_notas(2.0)
aluno1.verificar_aprovacao()'''

#-----------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self,nome, idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def apresentar(self):
        print(f'Olá!Boa noite!Meu nome é {self.nome},tenho {self.idade} anos e estudo  {self.curso}')

    def adiconar_notas(self,nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f'Nota {nota} adicionada com sucesso!')
        else:
            print('Nota inválida.Insira uma nota entre 0 e 10.')

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        print(f'A media do aluno(a) {self.nome}: {media:.2f}')
        if media >= 7:
            print(f'{self.nome} foi aprovado!')
        else:
            print(f'{self.nome} foi reprovado!')
'''
def menu():
    aluno = None

    while True:
        print('\n=========Menu===========')
        print('1 - Cadastrar Aluno')
        print('2 - Adicionar nota do aluno')
        print('3 - Media/Aprovação')
        print('4 - Mostrar dados do aluno')
        print('5 - Sair')

        opcao = input('Escolha a opção desejada(1-5)').strip()

        if not opcao:
            print('Entrada vazia.Digite uma opção')
            continue

        if opcao == '1':
            nome = input('Digite o nome do aluno: ')
            idade = int(input('Digite a idade do aluno: '))
            curso = input('Digite o curso do aluno: ')
            aluno = Aluno(nome, idade, curso)
            print('Aluno cadastrado com sucesso!')

        elif opcao == '2':
            if aluno:
                try:
                    nota = float(input('Digite a nota do aluno: '))
                    aluno.adiconar_notas(nota)
                except ValueError:
                    print('Nota inválida.Insira uma nota entre 0 e 10.')
            else:
                print('Cadastre um aluno primeiro (opção 1).')

        elif opcao == '3':
            if aluno:
                aluno.verificar_aprovacao()
            else:
                print('Nenhum aluno cadastrado')

        elif opcao == '4':
            if aluno:
                aluno.apresentar()
                print('Notas:',aluno.notas)
                print(f'Média atual: {aluno.calcular_media():.2f}')
            else:
                print('Nenhum aluno cadastrado')

        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')
menu()'''

import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        return media >= 7, media

class App:
    def __init__(self,root):
        self.root = root
        self.root.title('Aluno')
        self.aluno = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='Nome: ').grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self.root, text='Idade: ').grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.root)
        self.idade_entry.grid(row=1, column=1)

        tk.Label(self.root, text='Curso: ').grid(row=2, column=0)
        self.curso_entry = tk.Entry(self.root)
        self.curso_entry.grid(row=2, column=1)

        tk.Button(self.root,text='Cadastrar Aluno',command=self.cadastrar_aluno).grid(row=3,columnspan=2,pady=10)

        tk.Label(self.root,text='Nota: ').grid(row=4, column=0)
        self.nota_entry = tk.Entry(self.root)
        self.nota_entry.grid(row=4, column=1)

        tk.Button(self.root,text='Adicionar nota: ',command=self.adicionar_nota).grid(row=5,columnspan=2,pady=10)

        tk.Button(self.root,text='Media/Situação',command=self.mostrar_media).grid(row=6,columnspan=2,pady=5)
        tk.Button(self.root,text='Mostrar dados',command=self.mostrar_dados).grid(row=7,columnspan=2,pady=5)

    def cadastrar_aluno(self):
        nome = self.nome_entry.get().strip()
        idade = self.idade_entry.get().strip()
        curso = self.curso_entry.get().strip()

        if nome and idade.isdigit() and curso:
            self.aluno = Aluno(nome, int(idade), curso)
            messagebox.showinfo('Cadastro!', f'Aluno {nome} cadastrado com sucesso!')
        else:
            messagebox.showwarning('Erro!Preencha todos os campos!')

    def adicionar_nota(self):
        if not self.aluno:
            messagebox.showwarning('Erro!Cadastre um aluno primeiro')
            return
        nota = self.nota_entry.get()
        try:
            nota = float(nota)
            if self.aluno.adicionar_nota(nota):
                messagebox.showinfo('Nota: ',f'Nota {nota} adicionada com sucesso!')
                self.nota_entry.delete(0, tk.END)
            else:
                messagebox.showerror('Erro!Nota deve estar entre 0 e 10!')
        except ValueError:
            messagebox.showwarning('Digite um numero válido!')

    def mostrar_media(self):
        if not self.aluno:
            messagebox.showwarning('erro!Cadastre um aluno primeiro')
            return
        aprovado,media = self.aluno.verificar_aprovacao()
        status = 'aprovado' if aprovado else 'reprovado'
        messagebox.showinfo('Resultado',f'Media : {media:.2f}\n Situação: {status}')

    def mostrar_dados(self):
        if not self.aluno:
            messagebox.showwarning('erro!Cadastre um aluno primeiro')
            return
        dados = (
            f'Nome: {self.aluno.nome}\n'
            f'Idade: {self.aluno.idade}\n'
            f'Curso: {self.aluno.curso}\n'
            f'Nota: {self.aluno.notas}\n'
            f'Media: {self.aluno.calcular_media()}\n'
        )
        messagebox.showinfo('dados Aluno', dados)
root = tk.Tk()
app = App(root)
root.mainloop()