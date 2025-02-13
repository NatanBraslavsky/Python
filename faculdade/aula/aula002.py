#Operadores aritméticos +, - ,*, /, % ,**, // -----------------------
'''
a,b,c,d = 2,4,6,8

s = a + b + c + d
sub = b - c
m = a * b
div = a / b
p = a ** b  # potencia
i = b // a  #inteiro da divisão

print('A soma de {} + {} + {} + {} = {} '.format(a,b,c,d,s))
print(f'A soma de {a} + {b} + {c} + {d} = {s}')

print(f'A multiplicação de {c} * {a} = {c * a}')

print(f'O inteiro da divisão = {i}')

# operação combinada---------------------------------------

r = (5 + 3) * 2 ** 3 / 4
print(f'O resultado = {r}')

# recebendo valores externos -----------------------------

x = int(input('Digite o valor de x '))
y = int(input('Digite o valor de y '))

print(f'A divisão de {x} / {y} = {x/y}')

#outra maneira de converter o input ------------------------------------------

x1 = input('Digite o valor de x1 ')
y1 = input('Digite o valor de y1 ')

x1 = int(x1)
y1 = int(y1)

print(f'A subtração de {x} - {y} = {x - y}')

#incremento e decremento não existe no python. podemos usar o += ou -=

contador = 0
contador += 1
print(contador)

contador -= 2
print(contador)

#Operadores relacionais >,<,>=,<=,==,!= -----------------------------------------

c = 10
d = '10'
print(c == d)

print(c != d)
print(c > d)

#comparação encadeada ------------------------------------------------------

nota = 8
print(7 <= nota <= 10)

#Operadores lógicos - and , or , not ---------------------------------------

idade  = int(input('Digite sua idade: '))
possui_cnh = True

print(idade >= 18 and possui_cnh)

print( not possui_cnh)

a,b = 3,7
print(a > 5 or b > 5)
print(a > 5 or b > 5)

#Operador in e not in -----------------------------------------------------

f = [1,2,3,4,5]
print(4 in f)
print(4 not in f)
print(50 not in f)

#math ------------------------------------------------------------

import math

#pow() - potencia -----------------------------------------------

b = float(input('Digite o valor da base '))
p = int(input('Digite o valor da potência '))

print(f'O numero {b} elevado {p} = {math.pow(b,p)}')

m = math.pow(b,p)
print(f'O numero {b} elevado {p} = {m}')

#sqrt() - raiz quadrada ------------------------------------

print(f'A raiz quadrada {b} = {math.sqrt(b)}')

#arredondamenbto : round ,ceil , floor ------------------------
d = math.sqrt(b)
print(f'A raiz quadrada {b} = {round(d,2)}')

print(f'A raiz quadrada {b} = {round(math.sqrt(b),1)}')

print(f'A raiz quadrada {b} = {math.ceil(math.sqrt(b))}')
print(f'A raiz quadrada {b} = {math.ceil(d)}')

print(f'A raiz quadrada {b} = {math.floor(math.sqrt(b))}')
print(f'A raiz quadrada {b} = {math.floor(d)}')

#trunc() - parte inteira do valor -----------------------------------

print(f'A parte inteira de {b} = {math.trunc(b)}')

# outra maneira de importar o modulo --------------------------------

from math import pow

b = float(input('Digite o valor da base '))
p = int(input('Digite o valor da potência '))

print(f'A potencia de {b}^{p} = {pow(b,p)}')

import random

#numeros aleatorios entre 0 e 1

r = random.random()
print(r)

#numeros inteiro definindo o intervalo

r1 = random.randint(1,10)
print(r1)

print(random.random() * 10)

from random import randint,randrange,uniform,choice,shuffle

print(randint(1,10))

#inteiro com intervalo -------------------------------------------

print(randrange(1,10,2))

#numeros flutuantes com intervalo --------------------------------

print(f'{uniform(10,100):.2f}')

i = float(input('Digite o valor inicial '))
f = float(input('Digite o valor final '))

print(f'O valor aleatorio é {uniform(i,f):.1f}')

#choice() - escolhe um valor aleatoriamente dentro de uma lista -----------

t = [10,20,30,40,50,60,70,80,90]
print(choice(t))

#shuffle() - embaralha os elementos da lista ----------------------------------

shuffle(t)
print(t)

#Desafio:Você quer simular a opção de jogar uma
# moeda e resultar em cara ou coroa.

#Analisar string ----------------------------------------------------------

#len() - quantidade de caracteres ---------------------------------------

nome = str(input('Qual o seu nome ? '))
print(f'O nome da pessoa é {nome} ele tem {len(nome)} letras.')

tam = len(nome)
print(f'O nome da pessoa é {nome} ele tem {tam} letras.')

#upper() - maiusculo -------------------------------------------

print(f'O nome da pessoa é {nome.upper()}')

#lower() - minusculo ------------------------------------------

print(f'O nome da pessoa é {nome.lower()}')

#swapcase() - inverte a string de maiusculo para minusculo e vice versa --

g = 'Desenvolvimento Web III'
print(f'A string invertida é {g.swapcase()}')

#replace() - altera o valor da string ---------------------------------------

print(f'O novo valor é {g.replace('Web','Prog')}')

#count() - quantidade de vezes que o elemento repete ----------------

print(f'A letra e repete {g.count('e')}')

#split() - dividir a string ----------------------------------------'''

l = 'Boa noite!'

print(l.split())

#join() - concatena e altera o separador -------------------------------

print('-'.join(l))
print(' '.join(l))
print(' '.join(l).split())

#strip() - remove o espaço inicial e final ----------------------------

l1 = '       Boa noite!      '
print(l1)
print(l1.strip())

#lstrip() - remove o espaço da esquerda ----------------------------------

print(l1.lstrip())

#rstrip() --------------------------------------------------------------

print(l1.rstrip())