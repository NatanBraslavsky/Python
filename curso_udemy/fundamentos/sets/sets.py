
#?Lógica para tirar elementos duplicados
# array = [1,2,3,3,3,3,2,2,2]
# unico = []

# for elemento in array:
#     existe = False
#     for un in unico:
#         if un == elemento:
#             existe = True
#             break
#     if not existe:
#         unico.append(elemento)

# print(unico)

#?Sets fazem isso em poucas linhas!
# lista = [1,2,2,2,3,3,3]
# print(set(lista))

#?posso converter depois para lista de novo
# lista = [1,2,2,2,3,3,3]   
# s1 = set(lista)
# s2 = list(s1)
# print(s2)

#?add | update | discard
# s1 = set()
# s1.add("Natan")
# s1.add(2)
# s1.update(('davi', 1,2,3,4))
# s1.discard('davi')
# print(s1)

#?união '|'  interseção '&'  diferença '-'  diferença simétrica '^'(itens que não estão em ambos)
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s1 ^ s2

print(f"S1 = {s1}\n")
print(f"S2 = {s2}\n")

print(f"Uniao {s3}")
print(f"Interseção {s4}")
print(f"Diferença A-B {s5}")
print(f"Diferença B-A {s6}")
print(f"Diferença simétrica {s7}")




