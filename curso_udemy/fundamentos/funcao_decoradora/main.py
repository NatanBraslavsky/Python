
# def criarFuncao(func):
#     def interna(*args, **kwargs):
#         for arg in args:
#             is_string(arg)
#         resultado = func(*args, **kwargs)
#         return resultado
#     return interna

# def inverterString(string):
#     return string[::-1]

# def is_string(param):
#     if not isinstance(param, str):
#         raise TypeError('Parametro deve ser uma string.')
    
# inverte_string_checando_parametro = criarFuncao(inverterString)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)





def criarFuncao(func):
    def interna(*args, **kwargs):
        for arg in args:
            isInt(arg)
        resultado = func(*args,**kwargs)
        return resultado
    return interna

@criarFuncao
def quadrado(x):
    return x**2

def isInt(parametro):
    if not isinstance(parametro, int):
        raise TypeError('O parametro deve ser inteiro.')


quad = quadrado('a')
print(quad)


