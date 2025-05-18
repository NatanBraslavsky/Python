from tkinter import *
'''
r = Tk()
r.geometry('500x500')
r.title('Aula 10')

x = Menu(r)

arquivo_menu = Menu(x,tearoff=False)
arquivo_menu.add_command(label='Novo')
arquivo_menu.add_command(label='Salvar')
arquivo_menu.add_command(label='Salvar como')
arquivo_menu.add_command(label='Imprimir')
arquivo_menu.add_command(label='Sair')
x.add_cascade(label='Arquivo',menu=arquivo_menu)
r.config(menu=x)

editar_menu = Menu(x,tearoff=0)
editar_menu.add_command(label='Copiar')
editar_menu.add_command(label='Colar')
editar_menu.add_command(label='Voltar')
editar_menu.add_command(label='Sair')
x.add_cascade(label='Editar',menu=editar_menu)
r.config(menu=x)'''

#exemplo para abrir uma nova janela através do botão - toplevel(raiz)
r = Tk()
r.geometry('500x500')
r.title('Janela Principal')
'''
def abrir_arquivo():
    nova_janela = Toplevel(r)
    nova_janela.geometry('500x500')
    nova_janela.title('Janela Secundária')
    l = Label(nova_janela, text='Está é uma nova janela!')
    l.pack()
    
btn = Button(r,text='Abrir Nova Janela',command=abrir_arquivo).pack()

#exemplo para abrir janela sem ação do usuario (má prática) --------------

nova_janela = Toplevel(r)
nova_janela.geometry('500x500')
nova_janela.title('Janela Secundária')
l = Label(nova_janela, text='Está é uma nova janela!')
l.pack()

#exemplo para abrir nova janela através do menu ------------------------------

menu_bar = Menu(r)
r.config(menu=menu_bar)

def abrir_arquivo():
    nova_janela = Toplevel(r)
    nova_janela.geometry('500x500')
    nova_janela.title('Janela Secundária')
    l = Label(nova_janela, text='Está é uma nova janela!')
    l.pack()

novo_menu = Menu(r,tearoff=0)
novo_menu.add_command(label='Abrir Nova Janela',command=abrir_arquivo)
menu_bar.add_cascade(label='Arquivo',menu=novo_menu)

#exemplo para abrir nova janela no objeto radiobutton ----------------------

f = Frame(r)
f.pack()

s = IntVar()

def abrir_arquivo():
    nova_janela = Toplevel(r)
    nova_janela.geometry('500x500')
    nova_janela.title('Janela Secundária')
    l = Label(nova_janela, text='Está é uma nova janela!')
    l.pack()

r1 = Radiobutton(f, text='Abrir Nova Janela',variable=s,value=1,command=abrir_arquivo).pack()
r2 = Radiobutton(f, text='Abrir Arquivo',variable=s,value=2).pack()
r3 = Radiobutton(f, text='Fechar Arquivo',variable=s,value=3).pack()'''

#exemplo de site ---------------------------------------------------------

div_cabecalho = Frame(r,bg='gray', width=800, height=50)
div_cabecalho.pack()

div_conteudo = Frame(r,bg='lightgray', width=800, height=600)
div_conteudo.pack()

div_rodape = Frame(r,bg='gray', width=800, height=50)
div_rodape.pack()








r.mainloop()