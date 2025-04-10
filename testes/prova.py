from tkinter import *

tk = Tk()
tk.geometry('300x300')
tk.title('prova')

def calcFahr():
    try:
        tempCel = float(temp_entry.get())
        calc = (tempCel * 9 / 5) + 32
        resp_label.config(text=round(calc))
    except:
        resp_label.config(text='erro.')
    
def calcKelv():
    try:
        tempCel = float(temp_entry.get())
        calc = tempCel + 273.15
        resp_label.config(text=round(calc))
    except:
        resp_label.config(text='erro.')

temp_entry = Entry(tk)
temp_entry.pack()

btnfah = Button(tk,text='verificar', command=calcFahr)
btnfah.pack()

btnkel = Button(tk,text='verificar', command=calcKelv)
btnkel.pack()

resp_label = Label(tk)
resp_label.pack()

tk.mainloop()