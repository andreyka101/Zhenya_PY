from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("900x500")
window.config(bg="#C445FF")


t_x = 10
t_y = 100
text_l = Label(text="" , font=("" , 14))
text_l.place(x=10 , y=100 , height=50)



def funMotion(event):
    # text_l.config(text=event)
    window.title(f"{event.x}/{event.y}")

    # text_l.config(text=event.state)
# window.bind("<Motion>" , funMotion)

text_l.bind("<Motion>" , funMotion)




def funB1(event):
    text_l.config(text=event)

    # text_l.config(text=event.num)

#     text_l.config(text=event.state)
window.bind("<Button-1>" , funB1)




def funB2(event):
    text_l.config(text=event)

    # text_l.config(text=event.num)

    # text_l.config(text=event.state)
window.bind("<Button-2>" , funB2)




def funB3(event):
    text_l.config(text=event)

    # text_l.config(text=event.num)

    # text_l.config(text=event.state)
window.bind("<Button-3>" , funB3)




def funMouseWheel(event):
    global t_y , t_x
    text_l.config(text=event)

    # text_l.config(text=event.state)

    # if(event.delta == - 120):
    #     t_y += 20
    # if(event.delta == 120):
    #     t_y -= 20
    # text_l.place(y=t_y)


    # t_y += (event.delta/10)*2
    # text_l.place(y=t_y)

window.bind("<MouseWheel>" , funMouseWheel)




def funBMotion(event):
    text_l.config(text=event)

    # text_l.config(text=event.num)

    # text_l.config(text=event.state)
window.bind("<B1-Motion>" , funBMotion)







window.mainloop()