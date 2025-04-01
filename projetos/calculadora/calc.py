from tkinter import*

tk = Tk()
tk.resizable(0,0)
tk.title('Calculadora')
tk.geometry('300x450')
tk['bg'] = '#3D3D3D'

frame_resposta = Frame(tk,width=300,height=100, background='#3D3D3D')
frame_resposta.grid(row=0,column=0, columnspan=4)

label_resposta = Label(frame_resposta, text='', font='Arial 20', bg='#3D3D3D', fg='white')
label_resposta.pack(pady=30)

acumuladorTexto = ''

def atualizar_display():
    label_resposta.config(text=acumuladorTexto)

def botaosete():
    global acumuladorTexto
    acumuladorTexto+='7'
    atualizar_display()

def botaooito():
    global acumuladorTexto
    acumuladorTexto+='8'
    atualizar_display()

def botaonove():
    global acumuladorTexto
    acumuladorTexto+='9'
    atualizar_display()

def botaoquatro():
    global acumuladorTexto
    acumuladorTexto+='4'
    atualizar_display()

def botaocinco():
    global acumuladorTexto
    acumuladorTexto+='5'
    atualizar_display()

def botaoseis():
    global acumuladorTexto
    acumuladorTexto+='6'
    atualizar_display()

def botaoum():
    global acumuladorTexto
    acumuladorTexto+='1'
    atualizar_display()

def botaodois():
    global acumuladorTexto
    acumuladorTexto+='2'
    atualizar_display()

def botaotres():
    global acumuladorTexto
    acumuladorTexto+='3'
    atualizar_display()

def botaosoma():
    global acumuladorTexto
    acumuladorTexto+='+'
    atualizar_display()

def botaosubtracao():
    global acumuladorTexto
    acumuladorTexto+='-'
    atualizar_display()

def botaomultiplicacao():
    global acumuladorTexto
    acumuladorTexto+='*'
    atualizar_display()

def botaodivisao():
    global acumuladorTexto
    acumuladorTexto+='/'
    atualizar_display()

def botaozero():
    global acumuladorTexto
    acumuladorTexto+='0'
    atualizar_display()

def botaovirgula():
    global acumuladorTexto
    acumuladorTexto+=','
    atualizar_display()

def botaolimpar():
    global acumuladorTexto
    acumuladorTexto =''
    atualizar_display()

def botaoresultado():
    global acumuladorTexto
    try:
        resultado = eval(acumuladorTexto.replace(',', '.'))
        acumuladorTexto = str(resultado)
    except Exception:
        acumuladorTexto = "Erro"
    atualizar_display()





btn_sete = Button(tk,text=7, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaosete)
btn_sete.grid(row=1,column=0,padx=3,pady=3)

btn_oito = Button(tk,text=8, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaooito)
btn_oito.grid(row=1,column=1,padx=3,pady=3)

btn_nove = Button(tk,text=9, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaonove)
btn_nove.grid(row=1,column=2,padx=3,pady=3)

btn_quatro = Button(tk,text=4, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaoquatro)
btn_quatro.grid(row=2,column=0,padx=3,pady=3)

btn_cinco = Button(tk,text=5, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaocinco)
btn_cinco.grid(row=2,column=1,padx=3,pady=3)

btn_seis = Button(tk,text=6, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaoseis)
btn_seis.grid(row=2,column=2,padx=3,pady=3)

btn_um = Button(tk,text=1, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaoum)
btn_um.grid(row=3,column=0,padx=3,pady=3)

btn_dois = Button(tk,text=2, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaodois)
btn_dois.grid(row=3,column=1,padx=3,pady=3)

btn_tres = Button(tk,text=3, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaotres)
btn_tres.grid(row=3,column=2,padx=3,pady=3)

btn_zero = Button(tk,text=0, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaozero)
btn_zero.grid(row=4,column=1,padx=3,pady=3)

btn_virgula = Button(tk,text=',', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0, command=botaovirgula)
btn_virgula.grid(row=4,column=2,padx=3,pady=3)

btn_divisao = Button(tk,text='/', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0, command=botaodivisao)
btn_divisao.grid(row=1,column=3,padx=3,pady=3)

btn_multiplicacao = Button(tk,text='*', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0, command=botaomultiplicacao)
btn_multiplicacao.grid(row=2,column=3,padx=3,pady=3)

btn_subtracao = Button(tk,text='-', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0, command=botaosubtracao)
btn_subtracao.grid(row=3,column=3,padx=3,pady=3)

btn_soma = Button(tk,text='+', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0, command=botaosoma)
btn_soma.grid(row=4,column=3,padx=3,pady=3)

btn_resultado = Button(tk,text='=', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0, command=botaoresultado)
btn_resultado.grid(row=5,column=3,padx=3,pady=3)

btn_limpar = Button(tk,text='C', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0, command=botaolimpar)
btn_limpar.grid(row=5,column=2,padx=3,pady=3)

btn_vazio1 = Button(tk,text='', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0)
btn_vazio1.grid(row=5,column=1,padx=3,pady=3)

btn_vazio2 = Button(tk,text='', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#2F71C2', border=0)
btn_vazio2.grid(row=5,column=0,padx=3,pady=3)

btn_vazio3 = Button(tk,text='', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_vazio3.grid(row=4,column=0,padx=3,pady=3)







tk.mainloop()
