from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("900x500")
window.config(bg="#C445FF")


t_x = 10
t_y = 100
text_l = Label(text="" , font=("" , 14))
text_l.place(x=100 , y=100 , height=50)


obj_button={}



def fun(event):
    print("ok")
    element = event.widget
    text_l.config(text=element["text"])

    if(element["text"] == "b1"):
        window.config(bg="#000000")
    if(element["text"] == "b2"):
        window.config(bg="#3D174F")
    if(element["text"] == "b3"):
        window.config(bg="#592172")
    if(element["text"] == "b4"):
        window.config(bg="#702A91")
    if(element["text"] == "b5"):
        window.config(bg="#8C34B5")
    if(element["text"] == "b6"):
        window.config(bg="#9735C4")
    if(element["text"] == "b7"):
        window.config(bg="#C445FF")




for i in range(7):
    obj_button[i] = Button(text=f"b{i}")
    obj_button[i].place(x=20 , y=30*i)
    obj_button[i].bind("<Button-1>",fun)







window.mainloop()