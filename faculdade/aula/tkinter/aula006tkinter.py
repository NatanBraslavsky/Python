from tkinter import *

i = Tk()
i.title('Primeira Janela')
# i.geometry('600x300')
# i.resizable(False, False)
# i.state('zoomed')
# i.state('iconic')
# i.maxsize(900,500)
# i.minsize(300,150)
# i['bg'] = '#909090'

# try:
#     i.wm_iconbitmap('digital.ico')
# except:
#     pass

# btn = Button(i, text='Inserir', bg='red', font='Verdana 12')
# btn.pack()

# # Entry() cria uma caixa de entrada de dados
# e = Entry(i)
# e.pack()

# # Função do botão para mudar o texto do label
# def botao_clicado():
#     label.config(text='Oi, você clicou no botão!')

# # Botão para clicar e executar a função
# btn1 = Button(i,
#               text='Clique aqui',
#               font='Arial 10 italic',
#               fg='white',
#               bg='black',
#               relief='raised',
#               bd=5, 
#               padx=20,
#               pady=20,
#               activebackground='#45A049',
#               activeforeground='yellow',
#               command=botao_clicado
#               )
# btn1.pack(pady=20)

# # Label para exibir a mensagem
# label = Label(i, bg="#CECECE", fg='white')
# label.pack()

# Sistema grid
# x1 = Label(i, text='Teste1', bg='#CECECE')
# x2 = Label(i, text='Teste2', bg='#CECECE')
# x3 = Label(i, text='Teste3', bg='#CECECE')

# # Using grid layout for these labels
# x1.grid(row=0, column=0, padx=10, pady=10)
# x2.grid(row=0, column=1, padx=10, pady=10)
# x3.grid(row=0, column=2, padx=10, pady=10)


#-----------------------
# label_nome = Label(i,text='Nome:', font='Arial, 10')
# label_nome.grid(row=0, column=0, padx=10, pady=10)
# entry_nome = Entry(i)
# entry_nome.grid(row=0,column=1,padx=10,pady=10) 

# label_idade = Label(i,text='Idade:', font='Arial, 10')
# label_idade.grid(row=1, column=0, padx=10, pady=10)
# entry_idade = Entry(i)
# entry_idade.grid(row=1,column=1,padx=10,pady=10) 

# def informacoes():
#     nome = entry_nome.get()
#     idade = entry_idade.get()
#     r_Label.config(text = f'Nome: {nome}\nIdade: {idade}')

# btn2 = Button(i,text='Cadastrar', command=informacoes)
# btn2.grid(row=2,column=0,columnspan=2,padx=20)
# r_Label = Label(i, bg='#CECECE')
# r_Label.grid(row = 3, column = 0, columnspan = 2, pady=20)


#--------------------


def mostrar_selecionados():
    selecionados = []
    if futebol_var.get():
        selecionados.append('Futebol')
    if volei_var.get():
        selecionados.append('Vôlei')
    if basquete_var.get():
        selecionados.append('Basquete')
    
    r_label.config(text='Esporte(s) selecionado(s): ' + '☻ '.join(selecionados))


futebol_var = IntVar()
volei_var = IntVar()
basquete_var = IntVar()


a1 = Checkbutton(i, text='Futebol', variable=futebol_var)
a2 = Checkbutton(i, text='Vôlei', variable=volei_var)
a3 = Checkbutton(i, text='Basquete', variable=basquete_var)


a1.grid(row=0, column=0, padx=10, pady=10)
a2.grid(row=1, column=0, padx=10, pady=10)
a3.grid(row=2, column=0, padx=10, pady=10)


r_label = Label(i, text="Esporte(s) selecionado(s):", font=("Arial", 12))
r_label.grid(row=4, column=0, padx=10, pady=20)


btn2 = Button(i, text='Cadastrar', command=mostrar_selecionados)
btn2.grid(row=3, column=0, padx=10, pady=10)


i.mainloop()
