from tkinter import *
import time
import random

    
ventana = Tk()
def instrucciones():
    """
    Abre las instrucciones de como jugar el juego
    """
    global img, jugar
    fondo.place_forget()
    boton2.place_forget()
    boton3.place_forget()
    botonsalir.place_forget()
    ventana.geometry("700x700")
    img = PhotoImage(file="instrucciones.png")
    i = Label(ventana,image=img).place(x=0,y=0)
    jugar = Button(ventana,text="Jugar",font=("Arial",14),command=VersusMode)
    jugar.place(x=0,y=600)
    
    
              
#VersusMode menu
ventana.geometry("700x700")
ventana.resizable(width=False,height=False)
ventana.title("NekoPara speed")
def VersusMode():
    global background,WhiteBox,WhiteBox1,Player1name,Etiqueta,Player2name,Etiqueta2,jugarboton,jugarboton2,jugarboton3,jugarboton4,jugarboton5,player1,player2
    ventana.geometry("700x700")
    """
    Esta funcion hace aparecer el menu del versus mode
    """
    fondo.place_forget()
    boton2.place_forget()
    boton3.place_forget()
    botonsalir.place_forget()
    #Botonos e imagenes del versus mode
    ventana.resizable(width=False,height=False)
    player1 = StringVar()
    player2 = StringVar()
    ventana.title("NekoPara speed")
    ventana.geometry("700x700")
    botonjugar = PhotoImage(file="jugarbutton.png")
    fonde = PhotoImage(file="hehexd.png")
    background = Label(ventana,image=fonde)
    WhiteBox = Entry(ventana,textvariable=player1,font=("Arial",14))
    WhiteBox1 = Entry(ventana,textvariable=player2,font=("Arial",14))
    Player1name = Label(ventana,text="Player1 name:",font=("Arial",14))
    Etiqueta = Label(ventana,textvariable=player1,font=("Arial",14))
    Player2name = Label(ventana,text="Player2 name:",font=("Arial",14))
    Etiqueta2 = Label(ventana,textvariable=player2,font=("Arial",14))
    background.place(x=0,y=0)
    WhiteBox.place(x=230,y=410)
    WhiteBox1.place(x=230,y=570)
    Player1name.place(x=0,y=0)
    Etiqueta.place(x=125,y=0)
    Player2name.place(x=400,y=0)
    Etiqueta2.place(x=525,y=0)
    jugarbotonc = Button(ventana,text="Cargar",command=cargar)
    jugarbotonc.place(x=600,y=640)
    jugarboton = Button(ventana,text="NIVEL 1",command=nivel1)
    jugarboton.place(x=0,y=640)
    jugarboton2 = Button(ventana,text="NIVEL 2",command=nivel2)
    jugarboton2.place(x=120,y=640)
    jugarboton3 = Button(ventana,text="NIVEL 3",command=nivel3)
    jugarboton3.place(x=240,y=640)
    jugarboton4 = Button(ventana,text="NIVEL 4",command=nivel4)
    jugarboton4.place(x=360,y=640)
    jugarboton5 = Button(ventana,text="NIVEL 5",command=nivel5)
    jugarboton5.place(x=480,y=640)
    
    ventana.mainloop()

#niveles
def nivel1():
    """
    Abre el nivel 1 con una velocidad de 10
    """
    global vel
    vel=10
    Pista()
def nivel2():
    """
    Abre el nivel 2 con una velocidad de 12
    """
    global vel
    vel=12
    Pista()
def nivel3():
    """
    Abre el nivel 3 con una velocidad de 15
    """
    global vel
    vel=15
    Pista()
def nivel4():
    """
    Abre el nivel 4 con una velocidad de 18
    """
    global vel
    vel=18
    Pista()
def nivel5():
    """
    Abre el nivel 5 con una velocidad de 20
    """
    global vel
    vel=20
    Pista()


#Funcion que abre la pista
def Pista():
    """
    Pista principal
    """
    ventana.geometry("1300x700")
    ventana.title("NekoPara speed")
    
    global i,aa,bb,m1,m2,vivo,j,carrito1,vel,h,fonde,pista,k,carro,carro1,conter5,carrito,carroTonto,carroMove,carroSeg,carrito2,carrito3,carrito4,bidon,carrito22,carrito33,carrito44,tiempo1,tiempo2,Ltiempo1,Ltiempo2
    global background,WhiteBox,WhiteBox1,Player1name,conter3,conter4,Etiqueta,Player2name,Etiqueta2,jugarboton,q,w,player1,player2,r,t,conter2,fuel,fuel1,bidon,gasolinaplayer1,gasolinaplayer2,n1,n2
    
    background.place_forget()
    WhiteBox.place_forget()
    WhiteBox1.place_forget()
    Etiqueta.place_forget()
    Player2name.place_forget()
    jugarboton.place_forget()
    jugarboton2.place_forget()
    jugarboton3.place_forget()
    jugarboton4.place_forget()
    jugarboton5.place_forget()
    i = 280
    j = 650
    q = 884
    w = 650
    r = 650
    t = -90
    aa = 280
    bb = -100
    m1=1
    m2=1
    vivo=True
    n1=player1.get()
    n2=player2.get()

    h = Canvas(ventana,width=1300,height=700)
    
    pista = PhotoImage(file="Pista1.png")

    carro = PhotoImage(file="carrito1.png")
    carro1 = PhotoImage(file="carrito2.png")
    carroTonto = PhotoImage(file="carroTonto.png")
    carroMove = PhotoImage(file="carroMove.png")
    carroSeg = PhotoImage(file="carroSeg.png")
    bidon = PhotoImage(file="bidon.png")
    fonde = h.create_image(r,t,image=pista)
    carrito = h.create_image(i,j,image=carro)
    carrito1 = h.create_image(q,w,image=carro1)
    carrito2 = h.create_image(aa,bb,image=carroTonto)
    carrito22 = h.create_image(900,bb,image=carroTonto)
    carrito3 = h.create_image(350,-350,image=carroMove)
    carrito33 = h.create_image(900,-350,image=carroMove)
    carrito4 = h.create_image(300,-1800,image=carroSeg)
    carrito44 = h.create_image(900,-1800,image=carroSeg)
    fuel = h.create_image(290,-800,image=bidon)
    fuel1 = h.create_image(q,-800,image=bidon)
    conter2 = 1
    conter3 =100
    conter4 =100
    conter5 = 1

    tiempo1=0
    tiempo2=0
    Ltiempo1 = Label(h,text="puntos:\n"+str(tiempo1),font=("Arial",14))
    Ltiempo2 = Label(h,text="puntos:\n"+str(tiempo2),font=("Arial",14))
   
    Etiqueta = Label(h,text=n1,font=("Arial",14)).place(x=0,y=0)
    Etiqueta2 = Label(h,text=n2,font=("Arial",14)).place(x=1210,y=0)
    Etiquita4 = Label(h,text="Gasolina",font=("Arial",14)).place(x=0,y=200)
    Etiquita6 = Label(h,text="Gasolina",font=("Arial",14)).place(x=1210,y=200)


    
    ventana.bind('<Left>',izquierda1)
    ventana.bind('<Right>',derecha1)
    ventana.bind('<a>',izquierda)
    ventana.bind('<d>',derecha)
    ventana.bind('<A>',izquierda)
    ventana.bind('<D>',derecha)
    ventana.bind('<g>',guardar)
    ventana.bind('<G>',guardar)
    h.place(x=0,y=0)
    gasolinaplayer1 = Label(h,text=str(conter3),font=("Arial",14))
    gasolinaplayer1.place(x=0,y=250)
    gasolinaplayer2 = Label(h,text=str(conter4),font=("Arial",14))
    gasolinaplayer2.place(x=1210,y=250)
    gasolina()
    a=random.randint(288,386)
    carrito2 = h.create_image(a,-100,image=carroTonto)
    Enemigos()
    movimientoPista()
    #carritoTonto()
    h.pack()

def Enemigos():
    """
    funcion donde aparecen los enemigos, las colisiones, y las acciones
    que conlleva
    """
    global h,carro,carro1,carroTonto,carroMove,carroSeg,carrito,carrito1,carrito2,carrito3,carrito4,a,b,carrito22,fuel,fuel1,bidon,carrito33,carrito44,conter3,conter4,vivo,m1,m2
    if(vivo):
        a=random.randint(288,386)
        b=random.randint(870,1000)
        h.move(carrito2,0,vel)
        h.move(carrito22,0,vel)
        h.move(fuel,0,vel)
        h.move(fuel1,0,vel)
        h.move(carrito3,m1*2,vel)
        h.move(carrito33,m2*2,vel)
        if(h.coords(carrito3)[0]<248 or h.coords(carrito3)[0] >396):
            m1*=-1
        if(h.coords(carrito33)[0]<860 or h.coords(carrito33)[0]>1008):
            m2*=-1
        if(h.coords(carrito4)[0]>h.coords(carrito)[0] and conter3>0):
            h.move(carrito4,-2,vel)
        elif(h.coords(carrito4)[1]<h.coords(carrito)[0] and conter3>0):
            h.move(carrito4,2,vel)
        else:
            h.move(carrito4,0,vel)
            
        if(h.coords(carrito44)[0]>h.coords(carrito1)[0] and conter4>0):
            h.move(carrito44,-2,vel)
        elif(h.coords(carrito44)[0]<h.coords(carrito1)[0] and conter4>0):
            h.move(carrito44,2,vel)
        else:
            h.move(carrito44,0,vel)
            
        if(h.coords(carrito2)[1]<-100):
            h.delete(carrito2)
            carrito2 = h.create_image(a,-100,image=carroTonto)
        if(h.coords(carrito2)[1]>1000):
            h.delete(carrito2)
            carrito2 = h.create_image(a,-100,image=carroTonto)
        if(h.coords(carrito22)[1]<-100):
            h.delete(carrito22)
            carrito22 = h.create_image(b,-100,image=carroTonto)
        if(h.coords(carrito22)[1]>1000):
            h.delete(carrito22)
            carrito22 = h.create_image(b,-100,image=carroTonto)
        if(h.coords(fuel)[1]<-1000):
            h.delete(fuel)
            fuel = h.create_image(a,-500,image=bidon)
        if(h.coords(fuel)[1]>1400):
            h.delete(fuel)
            fuel = h.create_image(a,-500,image=bidon)
        if(h.coords(fuel1)[1]<-1000):
            h.delete(fuel1)
            fuel1 = h.create_image(b,-500,image=bidon)
        if(h.coords(fuel1)[1]>1400):
            h.delete(fuel1)
            fuel1 = h.create_image(b,-500,image=bidon)
        if(h.coords(carrito3)[1]<-400):
            h.delete(carrito3)
            carrito3 = h.create_image(a,-300,image=carroMove)
        if(h.coords(carrito3)[1]>1400):
            h.delete(carrito3)
            carrito3 = h.create_image(a,-300,image=carroMove)
        if(h.coords(carrito33)[1]<-400):
            h.delete(carrito33)
            carrito33 = h.create_image(b,-300,image=carroMove)
        if(h.coords(carrito33)[1]>1400):
            h.delete(carrito33)
            carrito33 = h.create_image(b,-300,image=carroMove)
        if(h.coords(carrito4)[1]<-1700):
            h.delete(carrito4)
            carrito4 = h.create_image(a,-700,image=carroSeg)
        if(h.coords(carrito4)[1]>1400):
            h.delete(carrito4)
            carrito4 = h.create_image(a,-700,image=carroSeg)
        if(h.coords(carrito44)[1]<-1700):
            h.delete(carrito44)
            carrito44 = h.create_image(b,-700,image=carroSeg)
        if(h.coords(carrito44)[1]>1400):
            h.delete(carrito44)
            carrito44 = h.create_image(b,-700,image=carroSeg)

        ##colision

        o1=h.coords(carrito2)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3-=10
            h.delete(carrito2)
            carrito2 = h.create_image(a,-100,image=carroTonto)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4-=10
            h.delete(carrito2)
            carrito2 = h.create_image(a,-100,image=carroTonto)

        o1=h.coords(carrito22)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3-=10
            h.delete(carrito22)
            carrito22 = h.create_image(b,-100,image=carroTonto)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4-=10
            h.delete(carrito22)
            carrito22 = h.create_image(b,-100,image=carroTonto)

        o1=h.coords(fuel)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3+=30
            h.delete(fuel)
            fuel = h.create_image(a,-100,image=bidon)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4+=30
            h.delete(fuel)
            fuel = h.create_image(a,-100,image=bidon)

        o1=h.coords(fuel1)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3+=30
            h.delete(fuel1)
            fuel1 = h.create_image(b,-100,image=bidon)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4+=30
            h.delete(fuel1)
            fuel1 = h.create_image(b,-100,image=bidon)

        o1=h.coords(carrito3)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3-=10
            h.delete(carrito3)
            carrito3 = h.create_image(a,-100,image=carroMove)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4-=10
            h.delete(carrito3)
            carrito3 = h.create_image(a,-100,image=carroMove)

        o1=h.coords(carrito33)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3-=10
            h.delete(carrito33)
            carrito33 = h.create_image(b,-100,image=carroMove)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4-=10
            h.delete(carrito33)
            carrito33 = h.create_image(b,-100,image=carroMove)

        o1=h.coords(carrito4)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3-=10
            h.delete(carrito4)
            carrito4 = h.create_image(a,-100,image=carroSeg)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4-=10
            h.delete(carrito4)
            carrito4 = h.create_image(a,-100,image=carroSeg)

        o1=h.coords(carrito44)
        o2=h.coords(carrito)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter3-=10
            h.delete(carrito44)
            carrito44 = h.create_image(b,-100,image=carroSeg)
        o2=h.coords(carrito1)
        if(max(o1[0],o2[0])-min(o1[0],o2[0])<=30 and max(o1[1],o2[1])-min(o1[1],o2[1])<=60):
            conter4-=10
            h.delete(carrito44)
            carrito44 = h.create_image(b,-100,image=carroSeg)
        ventana.after(60,Enemigos)
    
        
    
def gasolina():
    """
    Funcion donde la gasolina disminuye segun se avanza, y rellena la gasolina
    al reoger un bidon
    """
    global conter2,conter3,conter4,conter5,carrito1,carrito,carrito2,carrito3,carrito4,carro,carro1,carroTonto,carroMove,Ltiempo1,Ltiempo2,carroSeg,a,fuel1,fuel,vivo,bidon,gasolinaplayer1,gasolinaplayer2,tiempo1,tiempo2
    if(vivo):
        Ltiempo1.destroy()
        Ltiempo1 = Label(h,text="puntos:\n"+str(tiempo1),font=("Arial",14))
        Ltiempo1.place(x=0,y=350)
        Ltiempo2.destroy()
        Ltiempo2 = Label(h,text="puntos:\n"+str(tiempo2),font=("Arial",14))
        Ltiempo2.place(x=1210,y=350)
        posx = h.coords(carrito)[0]
        posy = h.coords(carrito)[1]
        posx1 = h.coords(carrito1)[0]
        posy1 = h.coords(carrito1)[1]
        fuelx = h.coords(fuel)[0]
        fuely = h.coords(fuel)[1]
        fuelx1 = h.coords(fuel1)[0]
        fuely1 = h.coords(fuel1)[1]
        if(conter3>0):
            tiempo1+=1
            conter3 -= 1
            gasolinaplayer1.destroy()
            gasolinaplayer1 = Label(h,text=str(conter3),font=("Arial",14))
            gasolinaplayer1.place(x=0,y=250)
        else:
            if(conter3 > -10000):
                gasolinaplayer1.destroy()
                gasolinaplayer1 = Label(h,text="MUERTO",font=("Arial",14))
                gasolinaplayer1.place(x=0,y=250)
                h.delete(carrito)
                carrito = h.create_image(-1000,-1000)
                conter3=-11000
        if(conter4>0):
            conter4 -= 1
            tiempo2+=1
            gasolinaplayer2.destroy()
            gasolinaplayer2 = Label(h,text=str(conter4),font=("Arial",14))
            gasolinaplayer2.place(x=1210,y=250)
        else:
            if(conter4 > -10000):
                gasolinaplayer2.destroy()
                gasolinaplayer2 = Label(h,text="MUERTO",font=("Arial",14))
                gasolinaplayer2.place(x=1210,y=250)
                h.delete(carrito1)
                carrito1 = h.create_image(-1000,-1000)
                conter4=-11000
        
        if(conter4 <= -10000 and conter3 <= -10000):
            #vivo=False
            perder()
                                                                                                      
        h.after(1000,gasolina)
        
def movimientoPista():
    """
    Mueve la psita y la actualiza
    """
    global h,ventana,fonde,conter2,conter3,conter4,conter5,a
    if(vivo):
        conter = 0
        conter1 = 0

        if(conter<8):
            h.move(fonde,0,2)
            conter = conter+1
            conter1 = conter1+1
            ventana.after(1,movimientoPista)
            
        if(h.coords(fonde)[1]>1000):
            h.move(fonde,0,-h.coords(fonde)[1])
        
    
def derecha(event):
    """
    Mueve el carro del jugador 1 hacia la derecha
    """
    global i,j,carrito1,carrito,h,carro,q,w
    if(i<396 and conter3>0):
        
        h.delete(carrito)
        i = i + 8
        carrito = h.create_image(i,j,image=carro)
        
def izquierda(event):
    """
    Mueve el carro del jugador 1 hacia la izuquierda
    """
    global i,j,carrito1,carrito,h,carro
    if(i>248 and conter3>0):
        h.delete(carrito)
        i = i - 8
        carrito = h.create_image(i,j,image=carro)


def derecha1(event):
    """
    Mueve el carro del jugador 2 hacia la derecha
    """
    global carrito1,h,carro1,q,w
    if(q<1008 and conter4>0):
        h.delete(carrito1)
        q = q + 8
        carrito1 = h.create_image(q,w,image=carro1)

        
def izquierda1(event):
    """
    Mueve el carro del jugador 2 hacia la izquierda
    """
    global carrito1,h,carro1,q,w
    if(q>860 and conter4>0):
        h.delete(carrito1)
        q = q - 8
        carrito1 = h.create_image(q,w,image=carro1)

def perder():
    """
    funcion para finalizar el juego, donde senala quien ha sido el ganador
    """ 
    global h
    go=Label(h,image=gameover).place(x=450,y=200)
    ganador1=Label(h,text="EL GANADOR ES:").place(x=570,y=450)
    if(tiempo1>tiempo2):
        ganador=Label(h,text=n1+" CON "+str(tiempo1)+" PUNTOS").place(x=570,y=490)
    else:
        ganador1=Label(h,text=n2+" CON "+str(tiempo2)+" PUNTOS").place(x=570,y=490)
def guardar(event):
    """
    Funcion para guardar la partida
    """
    a=open("save.txt","w")
    a.write(n1+"\n")
    a.write(n2+"\n")
    a.write(str(tiempo1)+"\n")
    a.write(str(tiempo2)+"\n")
    a.write(str(conter3)+"\n")
    a.write(str(conter4)+"\n")
    a.write(str(vel)+"\n")
    a.close()

def cargar():
    """
    Funcion para cargar el juego en el momento que se guarda
    """
    global n1,n2,tiempo1,tiempo2,conter3,conter4,vel
    a=open("save.txt","r")
    n1=a.readline()
    n2=a.readline()
    tiempo1=int(a.readline())
    tiempo2=int(a.readline())
    conter3=int(a.readline())
    conter4=int(a.readline())
    vel=int(a.readline())
    a.close()
    PistaC()

def PistaC():
    """
    Abre el guardado
    """
    ventana.geometry("1300x700")
    global i,aa,bb,vivo,j,m1,m2,carrito1,vel,h,fonde,pista,k,carro,carro1,conter5,carrito,carroTonto,carroMove,carroSeg,carrito2,carrito3,carrito4,bidon,carrito22,carrito33,carrito44,tiempo1,tiempo2,Ltiempo1,Ltiempo2
    global background,WhiteBox,WhiteBox1,Player1name,conter3,conter4,Etiqueta,Player2name,Etiqueta2,jugarboton,q,w,player1,player2,r,t,conter2,fuel,fuel1,bidon,gasolinaplayer1,gasolinaplayer2,n1,n2
    background.place_forget()
    WhiteBox.place_forget()
    WhiteBox1.place_forget()
    Etiqueta.place_forget()
    Player2name.place_forget()
    jugarboton.place_forget()
    jugarboton2.place_forget()
    jugarboton3.place_forget()
    jugarboton4.place_forget()
    jugarboton5.place_forget()
    m1=1
    m2=1
    i = 280
    j = 650
    q = 884
    w = 650
    r = 650
    t = -90
    aa = 280
    bb = -100
    vivo=True
    h = Canvas(ventana,width=1300,height=700)
    pista = PhotoImage(file="Pista1.png")
    carro = PhotoImage(file="carrito1.png")
    carro1 = PhotoImage(file="carrito2.png")
    carroTonto = PhotoImage(file="carroTonto.png")
    carroMove = PhotoImage(file="carroMove.png")
    carroSeg = PhotoImage(file="carroSeg.png")
    bidon = PhotoImage(file="bidon.png")
    fonde = h.create_image(r,t,image=pista)
    carrito = h.create_image(i,j,image=carro)
    carrito1 = h.create_image(q,w,image=carro1)
    carrito2 = h.create_image(aa,bb,image=carroTonto)
    carrito22 = h.create_image(900,bb,image=carroTonto)
    carrito3 = h.create_image(350,-350,image=carroMove)
    carrito33 = h.create_image(900,-350,image=carroMove)
    carrito4 = h.create_image(300,-1800,image=carroSeg)
    carrito44 = h.create_image(900,-1800,image=carroSeg)
    fuel = h.create_image(290,-800,image=bidon)
    fuel1 = h.create_image(q,-800,image=bidon)
    conter2 = 1
    conter5 = 1
    Ltiempo1 = Label(h,text="puntos:\n"+str(tiempo1),font=("Arial",14))
    Ltiempo2 = Label(h,text="puntos:\n"+str(tiempo2),font=("Arial",14))
    Etiqueta = Label(h,text=n1,font=("Arial",14)).place(x=0,y=0)
    Etiqueta2 = Label(h,text=n2,font=("Arial",14)).place(x=1210,y=0)
    Etiquita4 = Label(h,text="Gasolina",font=("Arial",14)).place(x=0,y=200)
    Etiquita6 = Label(h,text="Gasolina",font=("Arial",14)).place(x=1210,y=200)
    ventana.bind('<Left>',izquierda1)
    ventana.bind('<Right>',derecha1)
    ventana.bind('<a>',izquierda)
    ventana.bind('<d>',derecha)
    ventana.bind('<A>',izquierda)
    ventana.bind('<D>',derecha)
    ventana.bind('<g>',guardar)
    ventana.bind('<G>',guardar)
    h.place(x=0,y=0)
    gasolinaplayer1 = Label(h,text=str(conter3),font=("Arial",14))
    gasolinaplayer1.place(x=0,y=250)
    gasolinaplayer2 = Label(h,text=str(conter4),font=("Arial",14))
    gasolinaplayer2.place(x=1210,y=250)
    gasolina()
    a=random.randint(288,386)
    carrito2 = h.create_image(a,-100,image=carroTonto)
    Enemigos()
    movimientoPista()
    h.pack()

gameover = PhotoImage(file="GO.png")
imagen = PhotoImage(file="Menuu.png")
imgbnt = PhotoImage(file="button2.png")
imgbnt2 = PhotoImage(file="button.png")
imgbnt3 = PhotoImage(file="button3.png")
imgbnt4 = PhotoImage(file="Salirbutton.png")
botonjugar = PhotoImage(file="jugarbutton.png")
fondo = Label(ventana,image=imagen)
fondo.place(x=0,y=0)
boton2 = Button(ventana,image=imgbnt2,command=VersusMode)
boton2.place(x=200,y=430)
boton3  = Button(ventana,image=imgbnt3,command=instrucciones)
boton3.place(x=200,y=550)
botonsalir = Button(ventana,image=imgbnt4,command=ventana.destroy)
botonsalir.place(x=0,y=650)

ventana.mainloop()

