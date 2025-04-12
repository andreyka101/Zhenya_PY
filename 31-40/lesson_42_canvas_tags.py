from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#C445FF")


canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)




canV.create_oval(10 , 400 ,100,500 , fill="#FFF678" , tags="i_rect ovalX")

canV.create_rectangle(50 , 100 ,300,200 , fill="#0E4F68" , tags="i_rect")
# num_rect = canV.create_rectangle(50 , 100 ,300,200 , fill="#0E4F68")



def fun(e):
    canV.coords("i_rect" , 200 , 100 ,500,300)
    canV.itemconfig("i_rect" , width=5 , fill="#FF3333")

    canV.itemconfig("ovalX" , width=5 , fill="#8204FF")


    # canV.coords(num_rect , 200 , 100 ,500,300)
    # canV.itemconfig(num_rect , width=5 , fill="#FF3333")



window.bind("<KeyPress>" , fun)


window.mainloop()