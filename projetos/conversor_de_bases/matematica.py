def binarioDecimal(bin):
    #bin[i]  2*i
    j = len(bin) - 1
    calc = 0
    for i in bin:
        calc += int(i) * 2 ** j
        j-=1
    return calc

while True:
    binario = input("Digite em binário: ")
    isBinario = False
    for i in binario:
        if i != '1' and i != '0':
            print("Digite em binário!!")
            isBinario = False
        else:
            isBinario = True

    if isBinario:
        print(binarioDecimal(binario))
        break

