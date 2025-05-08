from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
# window.resizable(False , True)
# window.resizable(False , False)

# window.maxsize(800,750)
# window.minsize(400,300)


photo = PhotoImage(file = "EhXxRUcU4AAFE5R.png")
window.iconphoto(False, photo)


window.config(bg="#C445FF")


canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)



# задаём тег фигуре
canV.create_rectangle(50 , 100 ,300,200 , fill="#0E4F68" , tags="i_rect")
# задаём два тега фигуре
canV.create_oval(10 , 400 ,100,500 , fill="#FFF678" , tags="i_rect ovalX")



# сохраняем id фигуры в переменную
# num_rect = canV.create_rectangle(50 , 100 ,300,200 , fill="#0E4F68")




def fun(e):
    # coords - меняем координаты по id или тегу
    # itemconfig - меняем другие переменные по id или тегу



    # меняем фигуру по тегу 
    canV.coords("i_rect" , 200 , 100 ,500,300)
    canV.itemconfig("i_rect" , width=5 , fill="#FF3333")

    canV.itemconfig("ovalX" , width=5 , fill="#8204FF")



    # меняем фигуру по id
    # canV.coords(num_rect , 200 , 100 ,500,300)
    # canV.itemconfig(num_rect , width=5 , fill="#FF3333")



window.bind("<KeyPress>" , fun)


window.mainloop()