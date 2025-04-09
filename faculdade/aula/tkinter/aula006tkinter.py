from tkinter import*

tk = Tk() # criar uma instância da janela
tk.title('Primeira Janela') #inserir titulo na janela
tk.geometry('600x300') #definir o tamanho da janela
#i.resizable(0,1) #restringir o redimensionamento da janela
#i.state('zoomed') #para a janela abrir em tela cheia
#i.state('iconic') # para abrir a janela minimizada, na barra de tarefas
tk.maxsize(900,500) #definir o maior tamanho da janela
tk.minsize(300,150) #definir o menor tamanho da janela
tk['bg'] = '#CECECE' #definir a cor de fundo da janela que pode ser escrito ou em hexadecimal
# tk.wm_iconbitmap('digital.ico') #inserir o icone na janela
'''
#Entry() - cria uma caixa de entrada de dados ----------------------------

e = Entry(i)
e.pack()

#Button() inserir um botão na janela --------------------------------------

btn = Button(i,text='Inserir',font='Verdana 12 bold').pack()

#Label() - rotulo  -------------------------------------------------------------

def botao_clicado():
    label.config(text='Oi,você clicou no botão!')

btn1 = Button(i,
        text = 'Clique aqui',
        font = 'Arial 10 italic',
        fg = 'white', #cor da fonte
        bg = '#4CAF50',#cor de fundo
        relief = 'raised', #para inserir borda
        bd = 5, #tamanho da borda
        padx= 20,#espaço entre o conteudo e a bora na horizontal
        pady= 10,#espaço entre o conteudo e a bora na vertical
        activebackground='#45A049',#alterar a cor de fundo ao clicar no botão
        activeforeground='yellow',#alterar a cor da fonte ao clicar no botão
        command=botao_clicado #ação a ser exercida pelo botão
        )
btn1.pack(pady=20)

label = Label(i,
              bg = "#CECECE",
              fg = 'white')
label.pack()

#Sistema grid(linha e coluna) -----------------------------------------------

x1 = Label(i,text='Teste1',bg='red')
x2 = Label(i,text='Teste2',bg='yellow')
x3 = Label(i,text='Teste3',bg='orange')

x1.grid(row=0,column=0,padx=10)
x2.grid(row=1,column=1,padx=10)
x3.grid(row=2,column=2,padx=10)

#-----------------------------------------------------------------------
label_nome = Label(i,text='Nome:',font='Arial 10',bg='#CECECE')
label_nome.grid(row=0, column=0,padx=10,pady=10)

entry_nome = Entry(i)
entry_nome.grid(row=0,column=1,padx=10,pady=10)

label_idade = Label(i,text='Idade:',font='Arial 10',bg='#CECECE')
label_idade.grid(row=1, column=0,padx=10,pady=10)

entry_idade = Entry(i)
entry_idade.grid(row=1,column=1,padx=10,pady=10)

def informacoes():
    nome = entry_nome.get()
    idade = entry_idade.get()
    r_Label.config(text=f'Nome: {nome}\nIdade: {idade}')

btn2 = Button(i,text='Cadastrar',command=informacoes)
btn2.grid(row=2,column=0,columnspan=2,pady=20)

r_Label = Label(i,bg='#CECECE')
r_Label.grid(row=3,column=0,columnspan=2)

#Checkbutton() - seleção multipla -------------------------------------------
'''
# def mostrar_selecionados():
#     selecionados = []
#     if futebol_var.get():
#         selecionados.append('Futebol')
#     if volei_var.get():
#         selecionados.append('Volei')
#     if natacao_var.get():
#         selecionados.append('Natação')
#     if tenis_var.get():
#         selecionados.append('Tênis')
#     if basquete_var.get():
#         selecionados.append('Basquete')
#     if surf_var.get():
#         selecionados.append('Surf')

#     r_label.config(text='Esporte(s) selecionado(s): '+' ☻ '.join(selecionados))

# futebol_var = IntVar()
# volei_var = IntVar()
# natacao_var = IntVar()
# tenis_var = IntVar()
# basquete_var = IntVar()
# surf_var = IntVar()

# t = Label(tk,text='Qual o seu esporte favorito',bg='#CECECE')
# a1 = Checkbutton(tk,text='Futebol',bg='#CECECE',variable=futebol_var)
# a2 = Checkbutton(tk,text='Volei',bg='#CECECE',variable=volei_var)
# a3 = Checkbutton(tk,text='Natação',bg='#CECECE',variable=natacao_var)
# a4 = Checkbutton(tk,text='Tenis',bg='#CECECE',variable=tenis_var)
# a5 = Checkbutton(tk,text='Basquete',bg='#CECECE',variable=basquete_var)
# a6 = Checkbutton(tk,text='Surf',bg='#CECECE',variable=surf_var)

# t.place(x=10,y=10)
# a1.place(x=10,y=40)
# a2.place(x=90,y=40)
# a3.place(x=160,y=40)
# a4.place(x=250,y=40)
# a5.place(x=320,y=40)
# a6.place(x=400,y=40)

# btn = Button(tk,text='Clique aqui',command=mostrar_selecionados)
# btn.place(x=10,y=70)

# r_label = Label(tk,text='Esportes selecionados: Nenhum',bg='#CECECE')
# r_label.place(x=10,y=100)

#Radiobutton() - seleção simples ----------------------------------------

def verificar():
    resp_label.config(text=valor.get())

valor = IntVar()

r1 = Radiobutton(tk,text='Opção 1',variable=valor,value=1,bg='#CECECE')
r2 = Radiobutton(tk,text='Opção 2',variable=valor,value=2,bg='#CECECE')
r3 = Radiobutton(tk,text='Opção 3',variable=valor,value=3,bg='#CECECE')
btn = Button(tk,text='verificar', command=verificar)
btn.place(x=300,y=10)
resp_label = Label(tk)
resp_label.place(x = 400, y = 10)

r1.place(x=10,y=10)
r2.place(x=100,y=10)
r3.place(x=200,y=10)

#Listbox() - cria uma lista --------------------------------------------

# # lista=Listbox(tk,selectmode=MULTIPLE)
# # lista.insert(0,'AC')
# # lista.insert(1,'AM')
# # lista.insert(2,'AL')
# # lista.insert(3,'MG')
# # lista.insert(4,'RJ')
# # lista.insert(5,'SP')
# # lista.insert(END,'TO')
# # lista.pack()

# # estado = ['a','b','c']
# # for e in estado:
# #     lista.insert(END,e)


tk.mainloop()