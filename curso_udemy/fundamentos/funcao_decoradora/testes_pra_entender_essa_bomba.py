# def validarArgumento(condicao):
#     def decorador(func):
#         def aninhada(*args, **kwargs):
#             if condicao(*args, **kwargs):
#                 return func(*args, **kwargs)
#             else:
#                 raise ValueError("Valor inválido.")
#         return aninhada
#     return decorador

# @validarArgumento(lambda x: x > 0)
# def calcularCubo(x):
#     return x**3
            
# cubo = calcularCubo(2)
# print(cubo)


# def validarArgumento(condicao):
#     def decorador(func):
#         def aninhada(*args,**kwargs):
#             if condicao(*args, **kwargs):
#                 return func(*args,**kwargs)
#             else:
#                 raise NameError("Nome inválido.")
#         return aninhada
#     return decorador

# @validarArgumento(lambda  x: x == 'natanbraslavsky')
# def printarNome(x):
#     return x

# nome = input("Digite o nome: ")
# validar = printarNome(nome)
# print(validar)
from time import time, sleep

def tempoExecucao(funcao):
    def aninhada(*args, **kwargs):
        inicio_tempo = time()
        resultado = funcao(*args,**kwargs)
        fim_tempo = time()
        tempo_final = fim_tempo - inicio_tempo
        print(f'O tempo de execução foi de {round(tempo_final,6)} segundos.')
        return resultado
    return aninhada

@tempoExecucao
def exemplo():
    sleep(1)

exemplo()
