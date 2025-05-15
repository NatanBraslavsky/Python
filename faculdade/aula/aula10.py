from pydoc import text
from tkinter import *

tk = Tk()
tk.geometry('500x500')
tk.title('Aula 10')

# men = Menu(tk)

# arquivo_menu = Menu(tk)
# arquivo_menu.add_command(label='Novo')
# arquivo_menu.add_command(label='Salvar')
# arquivo_menu.add_command(label='Salvar como')
# arquivo_menu.add_command(label='Imprimir')
# arquivo_menu.add_command(label='Sair')
# men.add_cascade(label='Arquivo', menu=arquivo_menu)
# tk.config(menu=men)

# editar_menu = Menu(men, tearoff=0)
# editar_menu.add_command(label='Copiar')
# editar_menu.add_command(label='Colar')
# editar_menu.add_command(label='Voltar')
# editar_menu.add_command(label='Sair')
# men.add_cascade(label='Editar',menu=editar_menu)
# tk.config(menu=men)

# def abrir_arquivo():
#     nova_janela=Toplevel(tk)
#     nova_janela.geometry('500x500')
#     nova_janela.title('Janela Secundária')
#     l = Label(nova_janela, text='Esta é uma nova janela')
#     l.pack()
# btn = Button(tk, text='Abrir Nova Janela', command=abrir_arquivo).pack()

#ma pratica caralhoooooooooooooooooooooooo
# nova_janela = Toplevel(tk)
# nova_janela.geometry('500x500')
# nova_janela.title('Janela Secundaria')
# lab = Label(nova_janela, text='Esta é uma nova janela!')
# lab.pack()


# menu_bar = Menu(tk)
# tk.config(menu=menu_bar)
# def abrir_arquivo():
#     nova_janela = Toplevel(tk)
#     nova_janela.geometry('500x500')
#     nova_janela.title('Janela Secundária')
#     lab = Label(nova_janela, text='Esta é uma nova janela')
#     lab.pack()

# novo_menu = Menu(tk, tearoff=0)
# novo_menu.add_command(label='Abrir Nova Janela', command=abrir_arquivo)
# menu_bar.add_cascade(label='Arquivo', menu=novo_menu)



# f = Frame(tk)
# f.pack()

# s = IntVar()

# def abrir_arquivo():
#     nova_janela = Toplevel(tk)
#     nova_janela.geometry('500x500')
#     nova_janela.title('Janela Secundária')
#     lab = Label(nova_janela, text='Esta é uma nova janela.')
#     lab.pack()

# r1 = Radiobutton(f, text='Abrir Nova Janela', variable=s,value=1, command=abrir_arquivo).pack()
# r2 = Radiobutton(f, text='Abrir Arquivo', variable=s,value=2).pack()
# r2 = Radiobutton(f, text='Fechar Arquivo', variable=s,value=3).pack()

div_cabecalho = Frame(tk, bg='gray', width=800, height=50)
div_cabecalho.pack()
div_conteudo = Frame(tk, bg='lightgray', width=800, height=600)
div_conteudo.pack()
div_footer = Frame(tk, bg='gray', width=800, height=50)
div_footer.pack()


tk.mainloop()