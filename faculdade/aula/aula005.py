#Função  - def nome():
'''
def linha():
    print('-'* 50)

linha()
#---------------------------------------------------
def mostrar_nome(nome):
    print(f'Boa noite!{nome}')

nome = input('Digite o seu nome')
mostrar_nome(nome)
linha()

#-------------------------------------------------
def mostrar_nome(nome):
    print(f'Nome: {nome}')

quant_nome = int(input('Quantas pessoas deseja cadastrar? '))
for i in range(quant_nome):
    nome = input(f'Digite o seu nome {i + 1}: ')
    mostrar_nome(nome)

#---------------------------------------------------------

def soma(a,b):
    s = a + b
    print(f' A soma de {a} + {b} = {s}')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
soma(a,b)

#--------------------------------------------------------
def sub(a,b):
    return a - b

print(f'A subtração de {a} - {b} = {sub(a,b)}')

#-----------------------------------------------------------
def imc(peso,altura):
    return (peso/altura ** 2)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

print(f'O imc da pessoa: {imc(peso,altura):.2f}')

#-----------------------------------------------------------------
def soma_e_media(valor1,valor2):
    soma = valor1 + valor2
    media = (valor1 + valor2)/2
    return soma,media

valor1 = int(input('Digite o valor1 : '))
valor2= int(input('Digite o valor2 : '))

print(soma_e_media(valor1,valor2))

#-----------------------------------------------------------
def mult(valor1,valor2):return valor1 * valor2
print(f'A multiplicação de {valor1} * {valor2} = {mult(valor1,valor2)}')

#Função *args(passa quantos parametros forem necessários)------------------------------------

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

valores = input('Digite os numeros separados por virgula: ').split(',')
valores_int = ([int(valor) for valor in valores])

resultado = soma(*valores_int)
print(f'A soma dos valores: {resultado}')
print('A soma dos valores: ',resultado)

print(f'A soma dos valores: {soma(*valores_int)}')

#---------------------------------------------------------------
def maior(*args):
    print(args)
    print(type(args))

    for num in args:
        if num > 30:
            print(num)

#---------------------------------------------------

r = {'max':10, 'meio':5,'min':0}
def funcao(*args):
    for chave in args:
        print(chave)
funcao(*r)

maior(10,20,30,40,50,60)

# **kwargs() - empacotados dicionário -------------------------------

def exemplo(**kwargs):
    print(kwargs)

exemplo(a=1,b=2,c=3)

#----------------------------------------------------------------
def pessoa(nome,idade,cidade):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Cidade: {cidade}')

info_pessoa = {'nome':'Thereza','idade':30,'cidade':'Niteroi'}

pessoa(**info_pessoa)'''

#Exceção - https://docs.python.org/3/library/exceptions.html
'''
try:
    operação
except:
    erro
else:
    certo
finally:
    certo/errado

#--------------------------------------------------------------
try:
    num = int(input('Digite um numero: '))
    print(num)
except:
    print('Digite um numero válido')

#------------------------------------------------'''
try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    r = a/b
except:
    print('Tivemos um problema no sistema :(')
else:
    print(f'A divisão de {a} / {b} = {r}')