from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#C445FF")


t_x = 10
t_y = 100





def fun(event):

    text_l.config(text=event.widget)

window.bind("<Motion>" , fun)



def fun_click(event):

    # text_l.config(text=event.widget)
    element = event.widget
    # element.config(bg="#565656")

    # print(type(element))
    if(str(element) ==".!label" or str(element) ==".!label2" or str(element) ==".!label3" or str(element) ==".!label4"):
        element.config(bg="#E3B3FF")


window.bind("<Button-1>" , fun_click)



lab_1 = Label(bg="#FF7474")
lab_1.place(x=0 , y=0 , width=300 , height=250)
lab_2 = Label(bg="#FDFF74")
lab_2.place(x=300 , y=0 , width=300 , height=250)
lab_3 = Label(bg="#99FF74")
lab_3.place(x=0 , y=250 , width=300 , height=250)
lab_4 = Label(bg="#74FFF6")
lab_4.place(x=300 , y=250 , width=300 , height=250)





text_l = Label(text="" , font=("" , 14))
text_l.place(x=10 , y=100 , height=50)


window.mainloop()