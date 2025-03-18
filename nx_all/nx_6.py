import random
from tkinter import *

window = Tk()
window.title("calculator")
window.geometry("900x700")
window.config(bg="#9fdaff")

answer= 0

lab_text_1 = Label(text=answer , bg="#dbff93", fg="#000000" , font=["Yu Gothic UI Light" , 15])
lab_text_1.place(x= 500 , y=250 , height=80 , width=200)



entry_1 = Entry(bg="#dbff93", fg="#000000" , font=["Yu Gothic UI Light" , 15])
entry_1.place(x= 200 , y=250 , width=50)

entry_2 = Entry(bg="#dbff93", fg="#000000" , font=["Yu Gothic UI Light" , 15])
entry_2.place(x= 300 , y=250 , width=50)

entry_3 = Entry(bg="#dbff93", fg="#000000" , font=["Yu Gothic UI Light" , 15])
entry_3.place(x= 400 , y=250 , width=50)


def fun_b_1():
    print(entry_1.get())
    print(entry_2.get())
    print(entry_3.get())
    if entry_2.get() == "+":
        answer = int(entry_1.get()) + int(entry_3.get())
    elif entry_2.get() == "-":
        answer = int(entry_1.get()) - int(entry_3.get())
    elif entry_2.get() == "*":
        answer = int(entry_1.get()) * int(entry_3.get())
    elif entry_2.get() == "/":
        answer = int(entry_1.get()) / int(entry_3.get())
    lab_text_1.config(text=answer)






button_3 = Button(text="but 1" , command=fun_b_1 )
button_3.place(x= 300 , y=300)

window.mainloop()