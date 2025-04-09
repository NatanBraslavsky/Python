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


def mostrarInfo():
    lista = num_entry.get().split(',')
    nums = [int(n) for n in lista]
    

tk.mainloop()