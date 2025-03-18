#tupla - é um conjunto de dados, é imutável, é representada pelo ()
'''
a = (1,2,3,4.5,'Marcelo',True)
print(a)
print(a[4])
print(a[-3])
print(a[1:5])
print(a[3:])
print(a[:4])

#concatenar tuplas - + --------------------------------------------

b = (1,2,3,4)
c = (5,6,7)
d = b + c
print(d)
print(f'A nova tupla : {b+c}')

#len() - mostra a quantidade de elementos ---------------------------------

aluno = ('Paulo','Julia','Isabel','Marcelo')
tam = len(aluno)
print(f'A quantidade de elementos na tupla : {tam}')

print(f'A quantidade de elementos na tupla : {len(aluno)}')

#--------------------------------------------------------------------------
for i in range(0,len(aluno)):
    print(f'Oi!{aluno[i]}')
print('Boa noite!')

#del()- deletar a tupla ---------------------------------------------------

del(aluno)
print(aluno)

#count() - mostra a quantidade de elementos repetidos ----------------------

f = (1,2,3,1,4,5,1)
g = (1,4,5)
h = f + g
print(f'O numero 1 repete {h.count(1)} vezes')

#index() - mostra a primeira posição da repetição do elemento-------------

print(f'O indice da primeira repetição é : {h.index(1)}')

#Lista() - a lista é mutavel, representada [] -----------------------------

a = [1,2,3,4.5,'Marcelo',True]
print(a)
print(a[4])
print(a[-3])
print(a[1:5])
print(a[3:])
print(a[:4])

a[4] = 'Thereza' #alteração do valor da lista
print(a)

b = [1,[True,'Thereza',0],5,8,9,[0,1,2]]
print(b)
print(b[5][1])
print(b[1][0])

#concatenação de lista + --------------------------------------------------

x= [1,2,3]
y = [10,20,30]

w = y + x
print(w)

#append() - adiciona novos elementos no final da lista -------------

x.append('Web 3')
print(x)

#recebendo valores externos ---------------------------------------------

pessoa = []     #ou list()

nome1 = input('Insira o seu nome ')
nome2 = input('Insira o seu nome ')
nome3 = input('Insira o seu nome ')

pessoa.append(nome1)
pessoa.append(nome2)
pessoa.append(nome3)
print(pessoa)

#---------------------------------------------------------------------------

num = list()
for i in range(3,15,2):
    num.append(i)
    print(i)

#insert() - adiciona novos elementos na posição desejada -------------------
num1 = [1,2,3]
num1.insert(1,'Thereza')
print(num1)

#remove() - remover elementos -------------------------------------------

num1.remove(2)
print(num1)

#min() - busca o menor valor da lista ----------------------------------

l = [10,20,50,40,80,0]
print(f'O menor valor da lista é : {min(l)}')

#max() - maior valor da lista ---------------------------------------------

print(f'O maior valor da lista é : {max(l)}')

# -------------------------------------------------------------------------

lista = [0] * 3
for a in range(0,len(lista)):
    lista[a] = float(input('Digite a nota1, nota2 e nota 3 '))
media = ((lista[0] + lista[1] + lista[2]) /3)
print(f'A media do aluno é : {media:.1f}')

#reverse() - inverter a lista -----------------------------------------------

r = [10,20,30,40,50]
r.reverse()
print(r)

#sum() - soma todos os elementos da lista ------------------------------------

print(f'A soma dos elementos é : {sum(r)}')

#pop() - apaga o ultimo elemento da lista -------------------------------------

r1 = [10,20,30,40,50]
r1.pop()
print(f'O ultimo elemento a ser apagado {r1}')

r1.pop(2)
print(f'O ultimo elemento a ser apagado {r1}')

#del() ---------------------------------------------------------------

del(r1[1:3])
print(r1)

#sort() - ordena os elementos em ordem crescente ---------------------

z = [100,2,78,0,15,98]
z.sort()
print(z)

#ordenar de forma decrescente ----------------------------------------

z.sort(reverse=True)
print(z)

#enumerate() ----------------------------------------------------------

lista = [10,20,30,40]
for i,v in enumerate(lista):
    print(f'Indice {i} Valor = {v}')

#dicionário - nome_dic = {'chave':'valor'} ---------------------------

d = {}    #ou #dict()
print(d)
print(type(d))

l = []
print(type(l))

t = ()
print(type(t))

#--------------------------------------------------------------------

if not d:
    print('O dicionário está vazio')
else:
    print('O dicionário não está vazio')

#-------------------------------------------------------------------

aluno = {
        'nome':'Thereza',
        'idade': 25,
        'sexo' : 'F'
}

print('Nome: ', aluno['nome'])
print('Idade: ', aluno['idade'])
print('Sexo: ', aluno['sexo'])

aluno['idade'] = 54
print(aluno)

aluno['email'] = 'teste@gmail.com'
print(aluno)

del aluno['sexo']
print(aluno)

#keys() - mostra somente a chave
#values() - mostra somente os valores
#items() - mostra a chave e o valor

filme = {'titulo':'Moana','ano':2016,'autor':'John Musker'}

print(filme.keys())
print(filme.values())
print(filme.items())

#-----------------------------------------------------------------------

disc = {'web1':10,'web2':8.0,'web3':10}
for c in disc.keys():
    print(f'Chave {c}')

for c in disc.values():
    print(f'Valor {c}')

for chave,valor in disc.items():
    print(f'Chave {chave} Valor {valor}')

#---------------------------------------------------------------------

notas = {}    #ou dict()

notas = {
        'G1':float(input('Digite a nota 1: ')),
        'G2':float(input('Digite a nota 2: ')),
        'G3':float(input('Digite a nota 3: ')),
}

for valor in notas.values():
    print(valor)

#update() - atualizar o dicionário ------------------------------------------

d2 = {'nome':'Thereza'}
d2.update({'nome':'Thereza Gondim'}) #atualizar o nome
print(d2)

d2.update({'idade':12}) #atualizar inserindo nova chave e valor
print(d2)

#------------------------------------------------------------------

a ={'a':1,'b':2,'c':3}
b = {'d':4}

b.update(a) #concatenar o dicionário
print(b)

#copy() - ------------------------------------------------------------

original = {'a':1,'b':2,'c':3}
copia = original.copy()
print(original)
print(copia)

copia['e'] = 8
print(copia)

#----------------------------------------------------------------------------

lista_pessoas = []

q = int(input('Quantas pessoas deseja cadastrar? '))
for i in range(q):
    pessoa = {
        'nome' : str(input('Digite o seu nome ')),
        'idade': str(input('Digite a sua idade ')),
        'email': str(input('Digite o seu email ')),
    }
    lista_pessoas.append(pessoa.copy())
print(lista_pessoas)

# --------------------------------------------------------------------------

estado = {}
lista = []

for i in range(0,3):
    estado['uf'] = input('Digite o seu estado ')
    estado['sigla'] = input('Digite a sigla ')
    lista.append(estado.copy())
print(lista)'''