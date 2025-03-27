import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]#consigo acessar elemento por estar na memória, porem ocupa mt espaço
generator = (n for n in range(1000000))#nao consigo acessar elemento, ocupa pouco espaço

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


# for n in generator:
#     print(n)