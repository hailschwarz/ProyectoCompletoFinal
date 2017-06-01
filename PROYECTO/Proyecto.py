
from tkinter import *


ventana = Tk()
ventana.resizable(width=False,height=False)


#Versus mode menu
def VentanaQuit():
    """
    Funcion para abrir menu del versus mode
    """
    ventana.destroy()
    window = Tk()
    window.resizable(width=False,height=False)
    player1 = StringVar()
    player2 = StringVar()
    window.title("Road fighter")
    window.geometry("700x700")
    botonjugar = PhotoImage(file="jugarbutton.png")
    fonde = PhotoImage(file="hehexd.png")
    bakcground = Label(window,image=fonde).place(x=0,y=0)
    WhiteBox = Entry(window,textvariable=player1,font=("Arial",14)).place(x=230,y=410)
    WhiteBox1 = Entry(window,textvariable=player2,font=("Arial",14)).place(x=230,y=570)
    Player1name = Label(window,text="Player1 name:",font=("Arial",14)).place(x=0,y=0)
    Etiqueta = Label(window,textvariable=player1,font=("Arial",14)).place(x=125,y=0)
    Player1name = Label(window,text="Player2 name:",font=("Arial",14)).place(x=400,y=0)
    Etiqueta = Label(window,textvariable=player2,font=("Arial",14)).place(x=525,y=0)

#Pista versus mode
    def VersusQuit():
        window.destroy()
        ventane = Tk()
        ventane.resizable(width=False,height=False)
        i = 0
        j = 0
        presionar = False
        x = None
        d = Canvas(ventane, width=30, height=60).place(x=185,y=650)
        d.bind("<Key>", key)


        ventane.geometry("700x700")
        pista = PhotoImage(file="Pista.png")
        carrito1 = PhotoImage(file="carrito1.png")
        carrito2 = PhotoImage(file="carrito2.png")
        fonde = Label(ventane,image=pista).place(x=0,y=-2100)
        


        def derecha():
            """
            """
            global presiono,x,i,j,carrito1
            d.delete(x)
            i = i + 10
            #x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
            x = d.create_image(100+i,100+j,image=carrito1)

        def izquierda():
            """
            """
            global presiono,x,i,j,carrito1
            d.delete(x)
            i = i - 10
            #x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
            x = d.create_image(100+i,100+j,image=carrito1)

        def key(event):
            """
            """
            global x,i,j,carrito1
            tecla = repr(event.char)
            print(tecla)
            if(tecla == "'d'"):
                if(i < 500):
                    d.delete(x)
                    i = i + 10
                    x = d.create_image(100+i,100+j,image=carrito1)
                else:
                    d.delete(x)
                    i = -100
                    x = d.create_image(100+i,100+j,image=carrito1)            
            if(tecla == "'a'"):
                if(i > -50):
                    d.delete(x)
                    i = i - 10
                    x = d.create_image(100+i,100+j,image=carrito1)
                else:
                    d.delete(x)
                    x = d.create_image(100+i,100+j,image=carrito1)


    

        
        ventane.mainloop()




    boton = Button(window,image=botonjugar,command=VersusQuit).place(x=0,y=600)



    window.mainloop()

#Menu principal

ventana.geometry("700x700")
ventana.title("Road fighter")
#Imaganes
imagen = PhotoImage(file="Menu.png")
imgbnt = PhotoImage(file="button2.png")
imgbnt2 = PhotoImage(file="button.png")
imgbnt3 = PhotoImage(file="button3.png")
imgbnt4 = PhotoImage(file="Salirbutton.png")
fondo = Label(ventana,image=imagen).place(x=0,y=0)
boton = Button(ventana,image=imgbnt).place(x=200,y=320)
boton2 = Button(ventana,image=imgbnt2,command=VentanaQuit).place(x=200,y=430)
boton3  = Button(ventana,image=imgbnt3).place(x=200,y=550)
botonsalir = Button(ventana,image=imgbnt4,command=ventana.destroy).place(x=0,y=650)



    



ventana.mainloop()




