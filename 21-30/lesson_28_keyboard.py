from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("900x500")
window.config(bg="#C445FF")


text_l = Label(text="" , font=("" , 14))
text_l.place(x=10 , y=100)



def funPress(event):
    # event - получаем информацию о обработчике (клавиша)
    text_l.config(text=event)

    # event.keysym - название клавиши
    # text_l.config(text=event.keysym)
    # if(event.keysym == "r"):
    #     window.config(bg="#FF4545")

    # event.keycode - номер клавиши
    if(event.keycode == 82):
        window.config(bg="#FF4545")

    # event.state - информация о дополнительно зажатых клавиш
    # text_l.config(text=event.state)
    if(event.keycode == 82 and event.state == 12):
        window.config(bg="#7FFF3A")

# обработчик нажатия клавиши клавиатуры 
window.bind("<KeyPress>" , funPress)




def funRelease(event):
    # event - получаем информацию о обработчике (клавиша)
    text_l.config(text=event)

    # event.keycode - номер клавиши
    if(event.keycode == 82):
        window.config(bg="#4589FF")

# обработчик отжатие клавиши клавиатуры
window.bind("<KeyRelease>" , funRelease)



window.mainloop()