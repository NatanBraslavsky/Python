from tkinter import *


#!ex01
i = Tk()
i.title('Primeira Janela')

label_num1 = Label(i,text='Num1:', font='Arial, 10')
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = Entry(i)
entry_num1.grid(row=0,column=1,padx=10,pady=10) 

label_num2 = Label(i,text='Num2:', font='Arial, 10')
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = Entry(i)
entry_num2.grid(row=1,column=1,padx=10,pady=10) 

def somar():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    r_Label.config(text = f'Soma entre{num1} e {num2} = {num1+num2}')

btn2 = Button(i,text='Somar', command=somar)
btn2.grid(row=2,column=0,columnspan=2,padx=20)
r_Label = Label(i, bg='#CECECE')
r_Label.grid(row = 3, column = 0, columnspan = 2, pady=20)

i.mainloop()