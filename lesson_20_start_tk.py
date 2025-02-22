from tkinter import *


window = Tk()
window.title("lesson 20 start")
window.geometry("700x500")
window.config(bg="#C445FF")



lab_text_1 = Label(text="hello world" , bg="#75FF9A", fg="#FF7530" , font=["Segoe UI Black" , 15])
lab_text_1.place(x= 300 , y=200 , height=80 , width=200)



def fun_b_1():
    print("ok")

    lab_text_1.config(text="text")
    # lab_text_1.configure(text="text")

    button_1.place(y=30)

button_1 = Button(text="but 1" , command=fun_b_1)
button_1.place(x= 300 , y=300)
# button_1.pack()



# lab_text_2 = Label(text="yes" , bg="#343434", fg="#F8FF22" , font=["" , 15])
# lab_text_2.place(anchor="center" , relx=0.5, rely=0.5)



# lab_text_3 = Label(text="op" , bg="#C3C3C3", fg="#000000" , font=["" , 15])
# lab_text_3.place(anchor="center" , relx=0.5, rely=0.41)





window.mainloop()