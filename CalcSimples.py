from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('200x400')
def somar():
    if (str(num1_entry.get()).isnumeric() and str(num2_entry.get()).isnumeric()): #verificando se é numero
        num1 = int(num1_entry.get()) ## temos q converter para inteiro
        num2 = int(num2_entry.get())
        labelRes ["text"] = num1 + num2
    else:
        labelRes["text"] = 'Valores Inválidos'

def diminuir():
    if (str(num3_entry.get()).isnumeric() and str(num4_entry.get()).isnumeric()):
        num3 = int(num3_entry.get()) 
        num4 = int(num4_entry.get())
        labelResSub ["text"] = num3 - num4
    else:
        labelResSub["text"] = 'Valores Inválidos'

def limpar():
    num1_entry.delete(0,END)
    num2_entry.delete(0,END)
    num3_entry.delete(0,END)
    num4_entry.delete(0,END)

num1 = Label(root,text='1º Número')
num1.pack()
num1_entry = Entry(root)
num1_entry.pack()

num2 = Label(root,text='2º Número')
num2.pack()
num2_entry = Entry(root)
num2_entry.pack()

botao = Button(root,text='Somar',command=somar)
botao.pack()

labelSoma = Label(root,text='Resultado')
labelSoma.pack()

labelRes = Label(root,text='')
labelRes.pack()

num3 = Label(root,text='1º Número')
num3.pack()
num3_entry = Entry(root)
num3_entry.pack()

num4 = Label(root,text='2º Número')
num4.pack()
num4_entry = Entry(root)
num4_entry.pack()

botao = Button(root,text='Subtrair',command=diminuir)
botao.pack()

labelSub = Label(root,text='Resultado')
labelSub.pack()

labelResSub = Label(root,text='')
labelResSub.pack()

botaoLimpar = Button(root,text='Limpar',command=limpar)
botaoLimpar.pack(anchor=E)

root.mainloop()
