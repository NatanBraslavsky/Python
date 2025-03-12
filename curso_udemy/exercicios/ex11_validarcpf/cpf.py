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
vetor_multiplicacao_novedigitos = []
soma_vetor_multiplicado = 0
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
            break
        else:
            print("CPF inválido.")
    except:
        print("ERRO.")
soma_vetor_multiplicado *= 10
soma_vetor_multiplicado %= 11
primeiro_digito = 0 if soma_vetor_multiplicado >= 10 else soma_vetor_multiplicado
print(f"Primeiro dígito = {primeiro_digito}")
if primeiro_digito == int(cpf_array[9]):
    print("CPF Válido.")
else:
    print("CPF Não existe.")


