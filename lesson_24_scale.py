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
    lab_text_1.config(text=scale_1.get() , bg="#FFE875")
but_1 = ttk.Button(text="get val" , command=fun_1)
but_1.place(x=10 , y=60)





def fun_2(value):
    lab_text_1.config(text=value , bg="#75FF9A")
    but_1.place(y= int(value) + 60)


# scale_1 = Scale()
# scale_1 = Scale(orient=VERTICAL)
scale_1 = Scale(orient=HORIZONTAL , command=fun_2 , from_= 0 , to=15 , length=300)
scale_1.place(x=10 , y=10)
# scale_1.place(x=10 , y=10 , width=300)



def fun_3(value):
    lab_text_1.config(text=value , bg="#8E0C0C")
    lab_text_1.place(x= int(float(value)))



scale_2 = ttk.Scale(orient=HORIZONTAL , command=fun_3 , from_= 0 , to=700)
scale_2.place(x=200 , y=100)





window.mainloop()