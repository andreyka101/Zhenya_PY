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
    # считываем переменную
    print(value_radio.get())

    if(value_radio.get() == "b1"):
        window.config(bg="#FF4545")
    elif(value_radio.get() == "b2"):
        window.config(bg="#FFFC45")
    elif(value_radio.get() == "b3"):
        window.config(bg="#45FF8F")
    elif(value_radio.get() == "b4"):
        window.config(bg="#4570FF")





# value_radio общая переменная для связи четырех Radiobutton
# value_radio = IntVar()
value_radio = StringVar()



# variable - привязка Radiobutton к переменной
check_1 = ttk.Radiobutton(text="but 1" , variable=value_radio , value="b1" , command= fun_1)
check_1.place(x=10 , y=10)

check_2 = ttk.Radiobutton(text="but 2" , variable=value_radio , value="b2" , command= fun_1)
check_2.place(x=10 , y=50)

check_3 = ttk.Radiobutton(text="but 3" , variable=value_radio , value="b3" , command= fun_1)
check_3.place(x=10 , y=90)

check_4 = ttk.Radiobutton(text="but 4" , variable=value_radio , value="b4" , command= fun_1)
check_4.place(x=10 , y=130)





# три других Radiobutton они не связаны с четырьмя выше
num_radio_2 = StringVar()


check_5 = ttk.Radiobutton(text="but 5" , variable=num_radio_2 , value="b1" , command= fun_1)
check_5.place(x=110 , y=10)

check_6 = ttk.Radiobutton(text="but 6" , variable=num_radio_2 , value="b2" , command= fun_1)
check_6.place(x=110 , y=50)

check_7 = ttk.Radiobutton(text="but 6" , variable=num_radio_2 , value="b3" , command= fun_1)
check_7.place(x=110 , y=90)







window.mainloop()