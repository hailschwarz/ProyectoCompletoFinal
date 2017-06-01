from tkinter import *

def Player1():
    """
    Esta funcion da el nombre del jugador
    """
    print(player1.get())
    return(player1.get())


    
window = Tk()
player1 = StringVar()
player2 = StringVar()
window.title("Road fighter")
window.geometry("700x700")
imagen = PhotoImage(file="hehexd.png")
bakcground = Label(window,image=imagen).place(x=0,y=0)
WhiteBox = Entry(window,textvariable=player1,font=("Arial",14)).place(x=230,y=410)
WhiteBox1 = Entry(window,textvariable=player2,font=("Arial",14)).place(x=230,y=570)
Player1name = Label(window,text="Player1 name:",font=("Arial",14)).place(x=0,y=0)
Etiqueta = Label(window,textvariable=player1,font=("Arial",14)).place(x=125,y=0)
Player1name = Label(window,text="Player2 name:",font=("Arial",14)).place(x=400,y=0)
Etiqueta = Label(window,textvariable=player2,font=("Arial",14)).place(x=525,y=0)

window.mainloop()


