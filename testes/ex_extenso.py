algarismos = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dez_cima = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove',]
vinte_cima = ['vinte', 'trinta', 'quarente', 'cinquente', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seicentos', 'setecentos', 'oitocentos', 'novecentos']
milhar = ['mil']

num = int(input("Número até 1999: "))
tamanho = len(str(num))
x = str(num)[tamanho-1]
print(algarismos[int(x)-1])