from tkinter import *

window = Tk()

i = 0
j = 0
presionar = False
x = None


window.geometry("700x700")
pista = PhotoImage(file="Pista1.png")
carrito1 = PhotoImage(file="carrito1.png")
carrito2 = PhotoImage(file="carrito2.png")
fonde = Label(window,image=pista).place(x=0,y=0)
carrito = Label(window,image=carrito1).place(x=130,y=640)
carrito2 = Label(window,image=carrito2).place(x=500,y=640)


def derecha():
    """
    """
    global presiono,x,i,j
    d.delete(x)
    i = i + 10
    #x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
    x = d.create_image(100+i,100+j,image=carrito)

def izquierda():
    """
    """
    global presiono,x,i,j
    d.delete(x)
    i = i - 10
    #x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
    x = d.create_image(100+i,100+j,image=carrito)

def key(event):
    """
    """
    global i,j,presionar,x
    tecla = repr(event.char)
    print(tecla)
    if(tecla == "'d'"):
        if(1 < 500):
            d.delete(x)
            i += 10
            x = d.move_image(100+i,100+j,image="carrito1.png")
    if(tecla == "'a'"):
        if(i > -50):
            d.delete(x)
            i = i - 10
            x = d.move_image(100+i,100+j,image="carrito1.png")
    


    carrito.bind("<key>",key)    

    
window.mainloop()


