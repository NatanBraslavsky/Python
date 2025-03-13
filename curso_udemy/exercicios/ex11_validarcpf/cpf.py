"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
10  9  8  7  6  5  4  3  2
7   4  6  8  2  4  8  9  0
70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

vetor_multiplicacao_novedigitos = []
soma_vetor_multiplicado = 0
vetor_mult_segundo_digito = []
soma_vetor_segundo_digito = 0
while True:
    input_cpf = input("Digite o cpf: ").replace(".", "").replace("-", "")
    tamanho_cpf = len(input_cpf)
    try:
        if tamanho_cpf == 11:
            cpf_array = str(input_cpf)
            for i in range(tamanho_cpf - 2):
                multiplicacao = int(cpf_array[i]) * (10 - i)
                vetor_multiplicacao_novedigitos.append(multiplicacao)
            for i in range(len(vetor_multiplicacao_novedigitos)):
                soma_vetor_multiplicado += vetor_multiplicacao_novedigitos[i]
            for i in range(10):
                multiplicacao_segundo_digito = int(cpf_array[i]) * (11 - i)
                vetor_mult_segundo_digito.append(multiplicacao_segundo_digito)
            for i in range(len(vetor_mult_segundo_digito)):
                soma_vetor_segundo_digito += vetor_mult_segundo_digito[i]
            break
        else:
            print("CPF inválido.")
    except:
        print("ERRO.")
soma_vetor_multiplicado *= 10
soma_vetor_multiplicado %= 11
primeiro_digito = 0 if soma_vetor_multiplicado >= 10 else soma_vetor_multiplicado
soma_vetor_segundo_digito *= 10
soma_vetor_segundo_digito %= 11
segundo_digito = 0 if soma_vetor_segundo_digito > 9 else soma_vetor_segundo_digito
print(f"Primeiro dígito = {primeiro_digito}")
if primeiro_digito == int(cpf_array[9]):
    print("CPF Válido.")
else:
    print("CPF Não existe.")

print(vetor_mult_segundo_digito)
