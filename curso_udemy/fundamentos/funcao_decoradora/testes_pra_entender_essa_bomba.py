def validarArgumento(condicao):
    def decorador(func):
        def aninhada(*args, **kwargs):
            if condicao(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Valor inválido.")
        return aninhada
    return decorador

@validarArgumento(lambda x: x > 0)
def calcularCubo(x):
    return x**3
            
cubo = calcularCubo(2)
print(cubo)
