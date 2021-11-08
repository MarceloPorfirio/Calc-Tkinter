from tkinter import *

root = Tk()
root.title('Calculadora Simples')

e = Entry (root, width=42,borderwidth= 5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20)

def button_click(number):
    ##e.delete(0,END) 
    atual = e.get()
    e.delete(0,END) 
    e.insert(0, str(atual) + str(number))

## criar a function para limpar(deletar)

def button_clear():
    e.delete(0,END)  

##função de soma do botão
def button_add():
    primeiro_numero = e.get() 
    global f_num   
    global math 
    math = "adiçao" 
    f_num = int(primeiro_numero) 
    e.delete(0,END) 

##botão subtrarir
def button_sub():
    primeiro_numero = e.get()
    global f_num
    global math
    math = "subtraçao"
    f_num = int(primeiro_numero)
    e.delete(0,END)
    

##botão multi
def button_mult():
    primeiro_numero = e.get()
    global f_num
    global math
    math = "multiplicaçao"
    f_num = int(primeiro_numero)
    e.delete(0,END)

##botão div
def button_div():
    primeiro_numero = e.get()
    global f_num
    global math
    math = "divisao"
    f_num = int(primeiro_numero)
    e.delete(0,END)

##função do resultado do botão
def button_equal(): 
    segundo_numero = e.get() 
    e.delete(0, END) 
   
    if math == 'adiçao':
        e.insert(0,f_num + int(segundo_numero))
    
    if math == 'subtraçao':
        e.insert(0,f_num - int(segundo_numero))

    if math == 'multiplicaçao':
        e.insert(0,f_num * int(segundo_numero))

    if math == 'divisao':
        e.insert(0,f_num / int(segundo_numero))


#Definir os botoes
#Primeira linha            
button_1 = Button(root, text='1',pady=20 , padx=40, command=lambda: button_click(1))
button_2 = Button(root, text='2',pady=20 , padx=40, command=lambda: button_click(2))
button_3 = Button(root, text='3',pady=20 , padx=40, command=lambda: button_click(3))
##Segunda linha
button_4 = Button(root, text='4',pady=20 , padx=40, command=lambda: button_click(4))
button_5 = Button(root, text='5',pady=20 , padx=40, command=lambda: button_click(5))
button_6 = Button(root, text='6',pady=20 , padx=40, command=lambda: button_click(6))
#Terceira linha
button_7 = Button(root, text='7',pady=20 , padx=40, command=lambda: button_click(7))
button_8 = Button(root, text='8',pady=20 , padx=40, command=lambda: button_click(8))
button_9 = Button(root, text='9',pady=20 , padx=40, command=lambda: button_click(9))
#quarta linha
button_0 = Button(root, text='0',pady=20 , padx=40, command=lambda: button_click(0))
button_limpar = Button(root, text='Limpar',pady=20 , padx=71.3, command= button_clear)
#quinta linha
button_soma = Button(root, text='+',pady=20 , padx=39, command= button_add)
button_menos = Button(root, text='-',pady=20 , padx=39, command= button_sub)
button_multi = Button(root, text='x',pady=20 , padx=39, command= button_mult)
button_divis = Button(root, text='/',pady=20 , padx=39, command= button_div)
button_igual = Button(root, text='=',pady=20 , padx=86, command= button_equal)


##Colocar os botões na tela e em que coluna e linha que pertencem
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)

button_0.grid(row=6, column=0)
button_soma.grid(row=6, column=1)
button_menos.grid(row=6,column=2)

button_limpar.grid(row=7, column=1,columnspan=2)
button_multi.grid(row=7,column=0)
button_divis.grid(row=8,column=0)
button_igual.grid(row=8, column=1,columnspan=2)



root.mainloop()
