from tkinter import *

tk = Tk()
tk.geometry('500x500')
tk.resizable(0,0)
tk.title('Rev 1')

#?1
# def verificar_numero():
#     num = int(num_entry.get())
#     if num == 0:
#         resposta = '0'
#     else: 
#         resposta = 'positivo' if num > 0 else 'negativo'
#         resp_label.config(text=resposta)

# num_entry = Entry(tk)
# num_entry.pack()

# btn = Button(tk, text='verificar', command=verificar_numero)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()




#?2
# def verificar():
#     lista = num_entry.get().split(',')
#     limite = int(limite_entry.get())
#     numeros = [int(num) for num in lista]
#     for i in numeros:
#         if i > limite:
#             resp_label.config(text = numeros.index(i))
#             break
#         else:
#             resp_label.config(text= '-1')

# num_entry = Entry(tk)
# num_entry.pack()

# limite_entry = Entry(tk)
# limite_entry.pack()

# btn = Button(tk, text='clique', command=verificar)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()


#?3
# def isbissexto():
#     ano = int(ano_entry.get())
#     textoBissexto = 'É bissexto' if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)) else 'Não é bissexto'
#     resp_label.config(text=textoBissexto)

# ano_entry = Entry(tk)
# ano_entry.pack()

# btn = Button(tk, text='verificar', command=isbissexto)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()


#?4
# def calculadora():
#     num1 = int(num1_entry.get())
#     num2 = int(num2_entry.get())
#     calculo = f'{num1} + {num2} = {num1+num2}\n' +f'{num1} - {num2} = {num1 - num2}\n' +f'{num1} * {num2} = {num1 * num2}\n'+(f'{num1} / {num2} = {num1 / num2}' if num2 > 0 else 'Não é possivel dividir por 0 ou menor.')
#     resp_label.config(text=calculo)

# num1_entry = Entry(tk)
# num1_entry.pack()

# num2_entry = Entry(tk)
# num2_entry.pack()

# btn = Button(tk,text='clique', command= calculadora)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()

#?5
# def mostrarInfo():
#     lista = num_entry.get().split(',')
#     nums = [int(n) for n in lista]
#     qtdNove = nums.count(9)
#     try:
#         pos = nums.index(3)
#     except:
#         pos = -1
#     pares = [x for x in nums if x % 2 == 0]
#     resp_label.config(text=
#                       f'Qtd nove: {qtdNove}\n'+
#                       f'Index primeiro tres: {pos}\n'+
#                       f'pares: {pares}'
#                       )

# num_entry = Entry(tk)
# num_entry.pack()

# btn = Button(tk, text='clique', command=mostrarInfo)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()



#? prova. questao gorjeta

# def desconto():
#     try:
#         valor = float(valor_entry.get())
#         intvar = intvarValores.get()
#         if intvar == 10:
#             valorTotal = valor * 1.10
#         elif intvar == 15:
#             valorTotal = valor * 1.15
#         elif intvar == 20:
#             valorTotal = valor * 1.2
#         else:
#             valorTotal = valor
#         resp_label.config(text=f'Valor total: R${round(valorTotal,2)}')
#     except:
#         resp_label.config(text='Erro')
    

# valor_entry = Entry(tk)
# valor_entry.place(x=1,y=1)

# intvarValores = IntVar()

# btnDez = Radiobutton(tk, text='10%', variable=intvarValores, value=10)
# btnDez.pack()

# btnQuin = Radiobutton(tk, text='15%', variable=intvarValores, value=15)
# btnQuin.pack()

# btnVin = Radiobutton(tk, text='20%',variable=intvarValores, value=20)
# btnVin.pack()

# btn = Button(tk, text='Verificar', command=desconto)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()


#?mesma questao 2 tentativa pra treino

# def valorTotal():
#     try:
#         valor = float(valor_entry.get())
#         desc = desconto.get()
#         if desc == 10:
#             valorTot = valor * 1.1
#         elif desc == 15:
#             valorTot = valor * 1.15
#         elif desc == 20:
#             valorTot = valor * 1.2
#         else:
#             valorTot = valor
#         resp_label.config(text=f'Valor Total a pagar R${round(valorTot,2)}')
#     except:
#         resp_label.config(text='Erro.')

# valor_entry = Entry(tk)
# valor_entry.place(x=10,y=10)

# desconto = IntVar()

# desc10 = Radiobutton(tk, text='10%', variable=desconto, value=10)
# desc10.place(x=100,y=10)

# desc15 = Radiobutton(tk, text='15%', variable=desconto,value=15)
# desc15.place(x=200,y=10)

# desc20 = Radiobutton(tk,text='20%',variable=desconto,value=20)
# desc20.place(x=300,y=10)

# btn = Button(tk,text='Verificar', command=valorTotal)
# btn.place(x=400,y=10)

# resp_label = Label(tk)
# resp_label.place(x=10,y=100)





tk.mainloop()