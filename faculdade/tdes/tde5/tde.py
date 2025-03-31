from tkinter import *

tk = Tk()

tk.geometry('700x400')
tk.resizable(0,0)

#?ex 01
# label_numero = Label(tk,text='Digite um número: ', font='Arial 14')
# label_numero.grid(row=0,column=0,pady=10,padx=10)
# entry_numero = Entry(tk)
# entry_numero.grid(row=1,column=0,padx=10,pady=10)

# def receberDados():
#     try:
#         numero = float(entry_numero.get())
#         if numero > 0:
#             resp_label.config(text='Seu número é positivo.')
#         elif numero < 0:
#             resp_label.config(text='Seu número é negativo.')
#         else:
#             resp_label.config(text='Seu número é neutro')
#     except:
#         resp_label.config(text='Digite algo válido')

# btn = Button(tk,text='Clique', command=receberDados)
# btn.grid(row=1,column=1,padx=10,pady=10)
# resp_label = Label(tk, font='Arial 14')
# resp_label.grid(row=2,column=0,padx=10,pady=10)


#?ex02
# label_num = Label(tk,text='Insira um número')
# label_num.grid(row=0,column=0,padx=10,pady=10)
# entry_num = Entry(tk)
# entry_num.grid(row=0,column=1,padx=10,pady=10)

# label_limite = Label(tk,text='Insira o limite')
# label_limite.grid(row=1,column=0,padx=10,pady=10)
# entry_limite = Entry(tk)
# entry_limite.grid(row=1,column=1,padx=10,pady=10)

# numeros = []
# def informacoes():
#     try:
#         num = int(entry_num.get())
#         limite = int(entry_limite.get())
#         numeros.append(num)
#         lista_label.config(text=f'{numeros}')
#         if num > limite:
#             resp_label.config(text=f'{numeros.index(num)}')
#     except:
#         resp_label.config(text='Erro.')

    

# btn = Button(tk, text='Adicionar',command=informacoes)
# btn.grid(row=2,column=0,padx=10,pady=10)

# resp_label = Label(tk)
# resp_label.grid(row=3,column=0,padx=10,pady=10)
# lista_label = Label(tk)
# lista_label.grid(row=3,column=1,padx=10,pady=10)


#?ex03
# label_ano = Label(tk, text='Digite um ano: ')
# label_ano.grid(row=0, column=0, padx=10, pady=10)
# entry_ano = Entry(tk)
# entry_ano.grid(row=0,column=1,padx=10, pady=10)

# def bissexto():
#     try:
#         ano = int(entry_ano.get())
#         isBissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
#         if isBissexto:
#             resp_label.config(text='É bissexto.')
#         else:
#             resp_label.config(text='Não é bissexto.')
#     except:
#         resp_label.config(text='Digite um valor valido.')


# btn = Button(tk,text='Clique', command=bissexto)
# btn.grid(row=1,column=0,padx=10, pady=10)


# resp_label = Label(tk)
# resp_label.grid()



#?ex04
# entryNumUm = Entry(tk)
# entryNumUm.grid(row=0, column=0, padx=10,pady=10)

# entryNumDois = Entry(tk)
# entryNumDois.grid(row=0,column=1,padx=10,pady=10)

# def operacao():
#     try:
#         num1 = float(entryNumUm.get())
#         num2 = float(entryNumDois.get())
#         label_resposta.config(text=f'{num1:.0f} + {num2:.0f} = {num1+num2:.0f}\n{num1:.0f} - {num2:.0f} = {num1-num2:.0f}\n{num1:.0f} * {num2:.0f} = {num1*num2:.0f}\n{num1:.0f} / {num2:.0f} = {num1/num2:.0f}')
#     except: 
#         label_resposta.config(text='Dígito inválido.')


# btnOperacao = Button(tk, text='Resultado', command=operacao)
# btnOperacao.grid(row=1,column=0, padx=10, pady=10)

# label_resposta = Label(tk)
# label_resposta.grid(row=1,column=1,padx=10,pady=10)


#?ex05
entryNumUm = Entry(tk)
entryNumUm.grid(row=0,column=0,padx=10,pady=10)

entryNumDois = Entry(tk)
entryNumDois.grid(row=0,column=1,padx=10,pady=10)

entryNumTres = Entry(tk)
entryNumTres.grid(row=0,column=2,padx=10,pady=10)

entryNumQuatro = Entry(tk)
entryNumQuatro.grid(row=0,column=3,padx=10,pady=10)

def verificar():
    numeros = []
    qtdNove = 0
    qtdTres = 0
    mensagem = ''
    try:
        numeros.append(int(entryNumUm.get()))
        numeros.append(int(entryNumDois.get()))
        numeros.append(int(entryNumTres.get()))
        numeros.append(int(entryNumQuatro.get()))

        for i in numeros:
            if i == 9:
                qtdNove +=1
            if i % 2 == 0:
                mensagem += f'{i}\n'

            
        mensagem+= f'Quantidade de nove: {qtdNove}\n'
        mensagem+= f'3 no indice: {numeros.index(3)}\n'
        
    except:
        labelResposta.config(text=f'Erro.')

    labelResposta.config(text=mensagem)
   
    

btn = Button(tk, text='Enviar.', command=verificar)
btn.grid(row=1,column=0,padx=10,pady=10)

labelResposta = Label(tk)
labelResposta.grid(row=1,column=1,padx=10,pady=10)


tk.mainloop()