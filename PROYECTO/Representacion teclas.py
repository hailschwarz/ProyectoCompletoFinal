from tkinter import *




def keypress(event):
    if (event.keysym == 'Escape'):
            mainRoot.destroy()
            
    keyPressed=event.char
    print("You pressed" + keyPressed)

mainRoot = Tk()
print("Press a key")
mainRoot.bind_all('<Key>',keypress)
mainRoot.withdraw()
mainRoot.mainloop()
