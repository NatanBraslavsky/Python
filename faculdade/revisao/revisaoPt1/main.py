from tkinter import *

tk = Tk()
tk.geometry('300x300')


#? 01

# def verificar_numero(num):
#     n = int(num.get())
#     resposta = ''
#     if n > 0:
#         resposta = 'Positivo'
#     elif n < 0:
#         resposta = 'Negativo'
#     else:
#         resposta = 'Nulo.'
#     resp_label.config(text=resposta)
    

# num_entry = Entry(tk, width=30)
# num_entry.pack()

# btn = Button(tk,text='verificar', command=lambda:verificar_numero(num_entry))
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()


#? 02
 
# nums_entry = Entry(tk)
# nums_entry.pack()

# limite_entry = Entry(tk)
# limite_entry.pack()

# resp_label = Label(tk)
# resp_label.pack()

# lista = []
# def maiorLimite():
#     num = int(nums_entry.get())
#     lista.append(num)
#     limite = int(limite_entry.get())
#     for i in lista:
#         if i > limite:
#             resp_label.config(text = lista.index(i))
#         else:
#             resp_label.config(text = -1)
    

# btn = Button(tk, text='Clique', command=maiorLimite)
# btn.pack()


#? 03

# def bissexto():
#     ano = int(ano_entry.get())
#     isBissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
#     bi = ''
#     if isBissexto:
#         bi = 'Bissexto'
#     else:
#         bi = 'Não é bissexto'
#     resp_label.config(text = bi)
    
# ano_entry = Entry(tk)
# ano_entry.pack()

# btn = Button(tk,text='clique', command=bissexto)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()


#? 04

# def mostrarOperacao():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     resp_label.config(text = f'{num1} + {num2} = {num1 + num2}\n{num1} - {num2} = {num1 - num2}\n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {num1/num2}')

# num1_entry = Entry(tk)
# num1_entry.pack()

# num2_entry = Entry(tk)
# num2_entry.pack()

# btn = Button(tk,text='Clique', command=mostrarOperacao)
# btn.pack()

# resp_label = Label(tk)
# resp_label.pack()
    

#? 05

def infoLista():
    numeros = nums_entry.get().split(",")
    numeros = [int(num) for num in numeros]
    qtdNove = numeros.count(9)
    valorTres = numeros.index(3)
    pares = [i for i in numeros if i % 2 == 0]
    resp_label.config(text = f'Quantidade nove: {qtdNove}\nPrimeiro valor 3 no index: {valorTres}\nPares: {pares}')
    
nums_entry = Entry(tk)
nums_entry.pack()

btn = Button(tk, text='Clique', command=infoLista)
btn.pack()

resp_label = Label(tk)
resp_label.pack()

tk.mainloop()
