from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("900x500")
window.config(bg="#C445FF")


text_l = Label(text="" , font=("" , 14))
text_l.place(x=10 , y=100)



def funPress(event):
    text_l.config(text=event)

    
    # text_l.config(text=event.keysym)
    # if(event.keysym == "r"):
    #     window.config(bg="#FF4545")


    if(event.keycode == 82):
        window.config(bg="#FF4545")


    # text_l.config(text=event.state)
    if(event.keycode == 82 and event.state == 12):
        window.config(bg="#7FFF3A")

window.bind("<KeyPress>" , funPress)




def funRelease(event):
    text_l.config(text=event)
    if(event.keycode == 82):
        window.config(bg="#4589FF")
window.bind("<KeyRelease>" , funRelease)



window.mainloop()