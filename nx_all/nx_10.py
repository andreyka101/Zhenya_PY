from tkinter import *
from tkinter import ttk



window = Tk()
window.title("clicker")
window.geometry("700x500")
window.config(bg="#f4ffad")

value_radio = StringVar()

h=30
w=80
f=15


def fun_1():
    print(value_radio.get())
    if(value_radio.get() == "b01"):
        window.config(bg="#005d9b")
        lab_text_1.config(bg="#005d9b")
        lab_text_1.config(fg="#f4ffad")
        entry_1.config(bg="#f4ffad",fg="#000000")
        entry_2.config(bg="#f4ffad",fg="#000000")
    elif(value_radio.get() == "b02"):
        window.config(bg="#ff0000")
        lab_text_1.config(bg="#ff0000")
        lab_text_1.config(fg="#ffffff")
        entry_1.config(bg="#6a0000",fg="#ffffff")
        entry_2.config(bg="#6a0000",fg="#ffffff")

    elif(value_radio.get() == "b03"):
        window.config(bg="#000000")
        lab_text_1.config(bg="#000000")
        lab_text_1.config(fg="#26ff00")
        entry_1.config(bg="#000000",fg="#26ff00")
        entry_2.config(bg="#000000",fg="#26ff00")

    elif(value_radio.get() == "b04"):
        window.config(bg="#f4ffad")
        lab_text_1.config(bg="#f4ffad")
        lab_text_1.config(fg="#005d9b")
        entry_1.config(bg="#005d9b",fg="#ffffff")
        entry_2.config(bg="#005d9b",fg="#ffffff")




def fun_b_2():
    global h
    global w
    global f
    h += 10  
    button_1.place(height=h)
    w += 10  
    button_1.place(width=w)
    f += 1  
    button_1.config(font=["Yu Gothic UI Light" , f])

def fun_b_3():
    global h
    global w
    global f
    h -= 10  
    button_1.place(height=h)
    w -= 10  
    button_1.place(width=w)
    f -= 1  
    button_1.config(font=["Yu Gothic UI Light" , f])

def fun_4_b(event):
    if(event.keycode == 13):
        wi = int(entry_1.get())
        he = int(entry_2.get())
        window.geometry(f"{wi}x{he}")


button_2 = Button(text="bigger" , command=fun_b_2)
button_3 = Button(text="smaller" , command=fun_b_3)
entry_1 = Entry(bg="#005d9b", fg="#ffffff" , font=["Yu Gothic UI Light" , 15])
entry_2 = Entry(bg="#005d9b", fg="#ffffff" , font=["Yu Gothic UI Light" , 15])
check_1 = ttk.Radiobutton(text="синий" , variable=value_radio , value="b01" , command= fun_1)
check_2 = ttk.Radiobutton(text="красный" , variable=value_radio , value="b02" , command= fun_1)
check_3 = ttk.Radiobutton(text="черный" , variable=value_radio , value="b03" , command= fun_1)
check_4 = ttk.Radiobutton(text="классический" , variable=value_radio , value="b04" , command= fun_1)




def funPress(event):
    if(event.keycode == 17):
        button_2.place(x= 30 , y=300)
        button_3.place(x= 30 , y=350)
        entry_1.place(x= 30 , y=200 , width=180)
        entry_2.place(x= 30 , y=250 , width=180)
        check_1.place(x=30 , y=10)
        check_2.place(x=30 , y=50)
        check_3.place(x=30 , y=90)
        check_4.place(x=30 , y=130)

        
        


window.bind("<Return>" , fun_4_b)
window.bind("<KeyPress>" , funPress)

def funRelease(event):
    if(event.keycode == 17):
        button_2.place(x= -30 , y=-300)
        button_3.place(x= -30 , y=-350)
        entry_1.place(x= -30 , y=-200 , width=180)
        entry_2.place(x= -30 , y=-250 , width=180)
        check_1.place(x=-30 , y=-10)
        check_2.place(x=-30 , y=-50)
        check_3.place(x=-30 , y=-90)
        check_4.place(x=-30 , y=-130)



window.bind("<KeyRelease>" , funRelease)







c= 0
lab_text_1 = Label(text=c , bg="#f4ffad", fg="#005d9b" , font=["Yu Gothic UI Light" , 15])
lab_text_1.place(anchor="center" , relx=0.5, rely=0.4 , height=80 , width=200)


def fun_b_1():
    global c
    c += 1  
    lab_text_1.config(text=c)






button_1 = Button(text="click" , font=["Yu Gothic UI Light" , f], command=fun_b_1)
button_1.place(anchor="center" , relx=0.5, rely=0.6, height=h , width=w)




window.mainloop()








# width = int(window_width_entry.get())
#         height = int(window_height_entry.get())
#         window.geometry(f"{width}x{height}")





