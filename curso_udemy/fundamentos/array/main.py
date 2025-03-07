lista = [10, 20, 30, 40]

lista.insert(0, 5)#adiciona no indece 0, o número 5

del lista[-1]#deletei o ultimo item da lista

lista.append(10)#adicionei no final

lista.pop()#deletei o final

print(lista)


##testes
a = 0.1
b = 0.7
c = round(a + b, 1)
print(c)

frase = 'olha so, que coisa interessante'
arrayFrase = frase.split(",")
for i in range(len(arrayFrase)):
    print(f"{arrayFrase[i].strip()}")


##testes
lista = ['mamao', 'banana', 'pera']
f1, f2, *_ = lista #'*' é o resto da lista 
print(f1,f2, _)

p, *_, u = lista
print(p, u)

if lista == 'mamao':
    print(lista)
else:
    print(lista) 
