# lista = [1,2,3,4,5,6]

# lista_par = [x for x in lista if x % 2 == 0]

# print(lista_par)



# numero = [1,2,3,4,5]
# lista = [x**2 for x in numero if x % 2 == 0]

# print(numero, lista, sep='\n')


x = 1
y = 1
while x < 100:
    x,y = y, y+x
    if x % 3 == 0:
        print(x)