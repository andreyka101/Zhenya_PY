from tkinter import *


window = Tk()
window.title("lesson 21")
window.geometry("700x500+0+0")
window.config(bg="#C445FF")



lab_text_1 = Label(text="hello world" , bg="#75FF9A", fg="#FF7530" , font=["Segoe UI Black" , 15])
lab_text_1.place(x= 300 , y=200 , height=80 , width=200)



entry_1 = Entry(bg="#101C57", fg="#82DCFF" , font=["Segoe UI Black" , 15])
entry_1.place(x= 300 , y=100 , width=180)



def fun_b_1():
    print(entry_1.get())
    lab_text_1.config(text=entry_1.get())

    window.geometry(entry_1.get())

button_1 = Button(text="but 1" , command=fun_b_1 )
button_1.place(x= 300 , y=300)



def fun_b_2():
    lab_text_1.config(text=window.geometry())
button_2 = Button(text="get geo" , command=fun_b_2 )
button_2.place(x= 100 , y=300)






window.mainloop()