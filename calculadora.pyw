from tkinter import *
from tkinter.font import BOLD 

root = Tk()
frame = Frame(root) 

operacion = ""
resultado = 0


root.geometry("300x400")
root.resizable(0,0)
root.title("Calculadora")
frame.config(height=300)
frame.pack(fill="x", side=BOTTOM)

contenedor = Frame(frame)
contenedor.config(relief="sunken")
contenedor.pack(fill="y")


# ---------------------Pantalla ------------------------------
numeroPantalla = StringVar()

pantalla = Entry(root, textvariable= numeroPantalla)
pantalla.config(bg="black", fg="Green", font=("arial", 20, BOLD), justify="right")
pantalla.place(width=290, height=100, x=5, y=25)

#---------------- pulsaciones de teclado----------------------
def numeroPulsado(num):
    global operacion

    if operacion != "": 
        numeroPantalla.set(num)
        operacion =""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


#<<<<<<<<<<<<< ----------borrar ------------------->>>>>>>>>>>>>>>>>>>>>

def borrado ():
    global resultado
    resultado =0
    numeroPantalla.set(" ")



#-------------------------------------------------------------Funcion Eval >>>>>>>>>>>>>>>>>>
def paraigual(): 
    global resultado
    final = eval((numeroPantalla.get()))

    numeroPantalla.set(final)
    resultado = 0

#----------------------------------------------------

num1 = Button(contenedor , text="1", width=8, height=3, command=lambda:numeroPulsado("1"))
num1.grid(row=0, column=1, pady=4, padx=3)

num2 = Button(contenedor , text="2",  width=8, height=3, command=lambda:numeroPulsado("2"))
num2.grid(row=0, column=2, pady=4, padx=3)

num3 = Button(contenedor , text="3",  width=8, height=3, command=lambda:numeroPulsado("3"))
num3.grid(row=0, column=3, pady=4, padx=3)

num4 = Button(contenedor , text="4",  width=8, height=3, command=lambda:numeroPulsado("4"))
num4.grid(row=1, column=1, pady=4, padx=3)

num5 = Button(contenedor , text="5",  width=8, height=3, command=lambda:numeroPulsado("5"))
num5.grid(row=1, column=2, pady=4, padx=3)

num6 = Button(contenedor , text="6",  width=8, height=3, command=lambda:numeroPulsado("6"))
num6.grid(row=1, column=3, pady=4, padx=3)

num7 = Button(contenedor , text="7",  width=8, height=3, command=lambda:numeroPulsado("7"))
num7.grid(row=2, column=1, pady=4, padx=3)

num8 = Button(contenedor , text="8",  width=8, height=3, command=lambda:numeroPulsado("8"))
num8.grid(row=2, column=2, pady=4, padx=3)

num9 = Button(contenedor , text="9",  width=8, height=3, command=lambda:numeroPulsado("9"))
num9.grid(row=2, column=3, pady=4, padx=3)

num0 = Button(contenedor , text="0",  width=8, height=3, command=lambda:numeroPulsado("0"))
num0.grid(row=3, column=2, pady=4, padx=3)

#-------------------Aca comienzan las letras y simbolos, no los numeros--------------

mas = Button(contenedor , text="+",  width=8, height=3, command=lambda:numeroPulsado("+"))
mas.grid(row=3, column=1, pady=4, padx=3)

menos = Button(contenedor , text="-",  width=8, height=3, command=lambda:numeroPulsado("-"))
menos.grid(row=3, column=3, pady=4, padx=3)

igual = Button(contenedor, text="=", width=8, height=3, command=lambda:paraigual())
igual.grid(row=0, column=4, pady=4, padx=3)

multiplica = Button(contenedor, text="X", width=8, height=3, command=lambda:numeroPulsado("*"))
multiplica.grid(row=1, column=4, pady=4, padx=3)

dividir = Button(contenedor, text="/", width=8, height=3, command=lambda:numeroPulsado("/"))
dividir.grid(row=2, column=4, pady=4, padx=3)

borrar = Button(contenedor, text="Ce", width=8, height=3, command=lambda:borrado())
borrar.grid(row=3, column=4, pady=4, padx=3)





root.mainloop()
