from tkinter import *
from tkinter import ttk


window = Tk()
window.title("game")
window.geometry("700x500")
window.config(bg="#0b138c")



lab_text_1 = Label(text="1) сколько будет 2+2?" , bg="#0b138c", fg="#ffffff" , font=["Arial Black" , 15])
lab_text_1.place(x= 230 , y=190)



def fun_1():
    print(value_radio.get())
    if(value_radio.get() == "b01"):

        lab_text_1.config(text="2) сколько лет 10 летнему мальчику?")
        check_1.config(command= fun_2)
        check_2.config(command= fun_2)
        check_3.config(command= fun_2)
        check_4.config(command= fun_2)
        check_1.config(text= "9")
        check_2.config(text= "10")
        check_3.config(text= "8")
        check_4.config(text= "7")
    elif(value_radio.get() == "b02"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)
    elif(value_radio.get() == "b03"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)
    elif(value_radio.get() == "b04"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)



def fun_2():
    print(value_radio.get())
    if(value_radio.get() == "b02"):
        lab_text_1.config(text="3) почему?")
        check_1.config(command= fun_3)
        check_2.config(command= fun_3)
        check_3.config(command= fun_3)
        check_4.config(command= fun_3)
        check_1.config(text= "1")
        check_2.config(text= "да")
        check_3.config(text= "нет")
        check_4.config(text= "потому что")
    elif(value_radio.get() == "b01"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)
    elif(value_radio.get() == "b03"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)
    elif(value_radio.get() == "b04"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)    


def fun_3():
    print(value_radio.get())
    if(value_radio.get() == "b04"):
        lab_text_1.config(text="4) да?")
        check_1.config(command= fun_4)
        check_2.config(command= fun_4)
        check_3.config(command= fun_4)
        check_4.config(command= fun_4)
        check_1.config(text= "2")
        check_2.config(text= "да(нет)")
        check_3.config(text= "да")
        check_4.config(text= "нет")
    elif(value_radio.get() == "b01"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)
    elif(value_radio.get() == "b03"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)
    elif(value_radio.get() == "b02"):
        lab_text_1.config(text="ответ неверный")
        check_1.config(value=None)
        check_2.config(value=None)
        check_3.config(value=None)
        check_4.config(value=None)  



def fun_4():
    print(value_radio.get())
    if(value_radio.get() == "b03"):
        lab_text_1.config(text="krassava")
    else:
        lab_text_1.config(text="loh")

    





value_radio = StringVar()


check_1 = ttk.Radiobutton(text="4(да)" , variable=value_radio , value="b01" , command= fun_1)
check_1.place(x=10 , y=10)

check_2 = ttk.Radiobutton(text="4(нет)" , variable=value_radio , value="b02" , command= fun_1)
check_2.place(x=10 , y=50)

check_3 = ttk.Radiobutton(text="да(нет)" , variable=value_radio , value="b03" , command= fun_1)
check_3.place(x=10 , y=90)

check_4 = ttk.Radiobutton(text="нет(да)" , variable=value_radio , value="b04" , command= fun_1)
check_4.place(x=10 , y=130)

window.mainloop()
