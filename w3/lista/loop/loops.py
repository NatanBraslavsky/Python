#loop lista
lista = ["banana", "maça", "pera", "uva"]
contador = 0
for x in lista:
    print(x)

#cria nova lista
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#define um tamanho do loop
for x in range(10):
   print(x)