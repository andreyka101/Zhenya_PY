from tkinter import *
from tkinter import ttk



window = Tk()
window.title("lesson 21")
# меняем ширину высоту и координаты окна
window.geometry("700x500")
window.config(bg="#C445FF")



lab_text_1 = Label(text="hello world" , bg="#75FF9A", fg="#FF7530" , font=["Segoe UI Black" , 15])
lab_text_1.place(x= 300 , y=200 , height=80 , width=200)




def fun_1():
    lab_text_1.config(text=num_check.get())

    if(num_check.get()):
        lab_text_1.config(bg="#FFFFFF", fg="#004C61")
    else:
        lab_text_1.config(bg="#FF0808", fg="#92FFE7")

# num_check = BooleanVar()
num_check = IntVar()
check_1 = Checkbutton(text="but check" , variable=num_check , command=fun_1)
check_1.place(x=10 , y=10)




ttk.Style().configure("My.TCheckbutton", foreground="#004D40",  background="#B2DFDB")
check_2 = ttk.Checkbutton(text="check 2" , variable=num_check , style="My.TCheckbutton")
check_2.place(x=10 , y=50)






window.mainloop()