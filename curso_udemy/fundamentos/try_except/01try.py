digito = input("Digite um número: ")
try:
    digitoFloat = float(digito)#daria erro se eu tentasse converter uma string para um float, por isso o try
    print("Numero: ", digitoFloat)
except:
    print("Isso não é um número.")
