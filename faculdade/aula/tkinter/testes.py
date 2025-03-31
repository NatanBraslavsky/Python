from tkinter import*

tk = Tk() # criar uma instância da janela
tk.title('Primeira Janela') #inserir titulo na janela
tk.geometry('600x300')

def botao_clicado():
    label.config(text='Oi,você clicou no botão!')

btn1 = Button(tk,
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

label = Label(tk,
              bg = "#CECECE",
              fg = 'white')
label.pack()

tk.mainloop()
