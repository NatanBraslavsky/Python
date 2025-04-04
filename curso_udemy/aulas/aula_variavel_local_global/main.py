def concatenar(string_inicial):
    valorFinal = string_inicial
    def interna(valor_a_concatenar):
        nonlocal valorFinal
        valorFinal+=valor_a_concatenar
        return valorFinal
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))

