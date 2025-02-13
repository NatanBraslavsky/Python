#comentário de 1 linha
'''comentário de multiplas linhas'''

print('Boa noite!Sejam Bem Vindos!')

#Tipos de dados inteiro, float,string, booleano -------------------------------

nome = 'Thereza'
idade = 22
altura = 1.63
aprovado = True

print(nome,idade,altura,aprovado )
#print(nome + idade + altura + aprovado )

print( 5 + 5)
print( 5,5)
#print('5' + 5)
print( '5' + '5')
#print( "Olá!" + 5)
print( "Olá!" , 5)

print('O nome do aluno(a) é', nome)

a = 1
b = 2
c = 3.76654434

print('O valor de a = ',a,'\nO valor de b = ',b,'\nO valor de c = ',c)
print('O valor de c = ',round(c,2))

# exemplo de print com .format()

print('O valor de a = {}'.format(a))
print('O valor de a = {}, b = {} , c={:.2f}'.format(a,b,c))

#exemplo de f de string - f

print(f'O valor de a = {a}, o valor de  b = {b}, o valor de c = {c:.2f}')

#outra maneira de declarar variavel -----------------------------------

x,y,z = 1,2,3

print(f'x={x}, y={y}, z={z}')
print(f'A soma dos valores = {x + y + z}')