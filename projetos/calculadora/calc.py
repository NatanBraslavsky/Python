from tkinter import*

tk = Tk()
tk.resizable(0,0)
tk.title('Calculadora')
tk.geometry('320x550')
tk['bg'] = '#3D3D3D'

frame_resposta = Frame(tk,width=320,height=100, background='#3D3D3D')
frame_resposta.grid(row=0,column=0, columnspan=4)

btn_sete = Button(tk,text=7, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_sete.grid(row=1,column=0,padx=3,pady=3)

btn_oito = Button(tk,text=8, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_oito.grid(row=1,column=1,padx=3,pady=3)

btn_nove = Button(tk,text=9, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_nove.grid(row=1,column=2,padx=3,pady=3)

btn_quatro = Button(tk,text=4, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_quatro.grid(row=2,column=0,padx=3,pady=3)

btn_cinco = Button(tk,text=5, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_cinco.grid(row=2,column=1,padx=3,pady=3)

btn_seis = Button(tk,text=6, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_seis.grid(row=2,column=2,padx=3,pady=3)

btn_um = Button(tk,text=1, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_um.grid(row=3,column=0,padx=3,pady=3)

btn_dois = Button(tk,text=2, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_dois.grid(row=3,column=1,padx=3,pady=3)

btn_tres = Button(tk,text=3, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_tres.grid(row=3,column=2,padx=3,pady=3)

btn_zero = Button(tk,text=0, width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_zero.grid(row=4,column=1,padx=3,pady=3)

btn_virgula = Button(tk,text=',', width=7,height=2,font='Arial 13', fg='#f1f1f1', background='#5A98BF', border=0)
btn_virgula.grid(row=4,column=2,padx=3,pady=3)




tk.mainloop()
