# Estruturas condicionais if/else/elif ------------------------
'''
a = int(input('O valor de a: '))
b = int(input('O valor de b: '))

if a > b:
    print(f' O valor {a} é maior')
else:
    print(f'O numero {a} é menor')
print('Fim')

#----------------------------------------------------------------
nome = input('Digite seu nome: ')
if nome == 'Isabel':
    print('Esse nome é bonito')
print('Boa noite!')

#------------------------------------------------------------------
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print(f'A idade da pessoa {idade} anos já pode votar')
else:
    print(f'A idade da pessoa {idade} anos não pode votar')
#-------------------------------------------------------------------
if idade >= 0 and idade < 3:
    print('Bebê')
elif idade >= 3 and idade < 10:
    print('Criança')
elif idade >= 10 and idade < 15:
    print('Adolescente')
elif idade >= 15 and idade < 60:
    print('Adulto')
else:
    print('Melhor idade')

#------------------------------------------------------------------------
c = int(input('O valor de c: '))
d = int(input('O valor de d: '))

res = 0
op = input('Digite a operação: +,-,*,/')
if op == '+':
    res = c + d
    print(f'A soma {c} + {d} = {res}')
elif op == '-':
    res = c - d
    print(f'A subtração {c} - {d} = {res}')
elif op == '*':
    res = c * d
    print(f'A multiplicação {c} * {d} = {res}')
elif op == '/':
    print(f'A soma {c} * {d} = {c / d}')
print('Término do programa')

#condicional ternária ----------------------------------------------------

nota = float(input('Digite sua nota: '))
print('Aprovado' if nota >= 6 else 'Reprovado')

idade = int(input('Digite sua idade: '))
print('Maior de idade' if idade >= 18 else 'Menor de idade')

# ----------------------------------------------------------------------------
f = float(input('Digite um numero: '))
if f <=10 and f %2 == 0:
    print(f'O valor {f} é menor igual e é par')
else:
    print('Não atende a condição')

#For -------------------------------------------------------------------------
g = 0
h = 10
for i in range(h):
    print('Olá!')

#----------------------------------------------------------------------------
for x in range(10):
    print(x)

#----------------------------------------------------------------------------
for numero in range(1,8):
    print(f'Numero: {numero}')

#----------------------------------------------------------------------------
for num in range (1,10):
    if num % 2 == 0:
        print(f'O numero {num} é par')
    else:
        print(f'O numero {num} é impar')

# start,stop,step -------------------------------------------------------------

for num1 in range(1,20,2):
    print(num1)

#--------------------------------------------------------------------------
for num2 in range(10):
    if num2 > 6:
        break
    print(f'Numero: {num2}')
print('Fim')

#continue -------------------------------------------------------------

for num3 in range(20,30):
    if num3 == 22:
        continue
    print(f'Numero: {num3}')

#tabuada --------------------------------------------------------------

t = int(input('Digite um numero para calcular a tabuada'))
for t1 in range(0,11):
    print(f'{t} * {t1} = {t * t1}')

#enumerate--------------------------------------------------------------
nome = input('Digite o seu nome ')
for p,v in enumerate(nome):
    print(f'Posição: {p} Letra: {v}')

#while ------------------------------------------------------------------
n = 1
while n != 0:
    n = int(input('Digite um valor '))
print('Acabou!')

#---------------------------------------------------------------------------
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor '))
    if n != 0:
        if n % 2== 0 :
            par += 1
        else:
            impar +=1
print(f'Você digitou {par} numeros pares {impar} numeros impares')

#----------------------------------------------------------------------------
sexo = input('Informe o seu sexo: [F/M/O] ').strip().upper()[0]
while sexo not in 'FMO':
    sexo = input('Informe o sexo: [F/M/O] ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')

# --------------------------------------------------------------------------
#import random

from random import randint

c = randint(0,10)
print('Tente adivinhar...')
acerto = False

while not acerto:
    j = int(input('Qual o seu palpite? '))
    if j == c:
        acerto = True
        print('Acertou!😊')
    else:
        print('Errou!✖️')'''

#----------------------------------------------------------------------------
n1 = int(input('O valor de n1: '))
n2 = int(input('O valor de n2: '))
op = 0
while op != 5:
    print('''
    [1]Soma
    [2]Subtração
    [3]Multiplicação
    [4]Divisão
    [5]Sair''')
    op = int(input('Escolha a opção'))
    if op == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'A subtração de {n1} - {n2} = {n1 - n2}')
    elif op == 3:
        print(f'A multiplicação de {n1} * {n2} = {n1 * n2}')
    elif op == 4:
        print(f'A divisão de {n1} / {n2} = {n1 / n2}')
    elif op == 5:
        print('Sair do programa')
    else:
        print('Opção inválida!')