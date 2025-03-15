from tkinter import *
from tkinter import ttk



window = Tk()
window.title("lesson 21")
window.geometry("700x500")
window.config(bg="#f4ffad")

arr = ["хлеб - 30 руб" , "вода - 10 руб" , "шокодлад - 70 руб" , "молоко - 20 руб"]
list_box = Listbox(listvariable= Variable(value=arr) ,font=("Yu Gothic UI Light" , 12))
list_box.place(x=450 , y=70)




col= 10





obj = {}

entry_1 = None
entry_2 = None




def fun_b_1():
    col-1
    if col > 1:
        global entry_1, entry_2
        text = entry_1.get()
        if (text == "молоко"):
            obj[20] = text
            print(obj)
        elif(text == "хлеб"): 
            obj[30] = text
            print(obj)
        elif(text == "шоколад"): 
            obj[70] = text
            print(obj)
        elif(text == "вода"): 
            obj[10] = text
            print(obj)
        else: 
            print("error")
            lab_text_3 = Label(text="!Ошибка!" , bg="#ffa7a7", fg="#ff0000" , font=["Arial Black" , 20])
            lab_text_3.place(x= 30 , y=300)
        entry_1 = Entry(bg="#005d9b", fg="#ffffff" , font=["Yu Gothic UI Light" , 15])
        entry_1.place(x= 180 , y=75 , width=180)
        entry_2 = Entry(bg="#005d9b", fg="#ffffff" , font=["Yu Gothic UI Light" , 15])
        entry_2.place(x= 180 , y=145 , width=180)
    else: 
        lab_text_3 = Label(text="!Ошибка!" , bg="#ffd476", fg="#ff9d00" , font=["Arial Black" , 20])
        lab_text_3.place(x= 30 , y=350)


def fun_b_2():
    arr_values = obj.values()
    # print("arr_values =", arr_values)
    # arr_keys = obj.keys()
    # print("arr_keys =", arr_keys)
    # w= arr_values, sum(arr_keys)
    w = ""
    for key,val in obj.items():
        w += f"{val}: {key}\n"

    lab_text_4 = Label(text=w , bg="#ffffff", fg="#000000" , font=["Arial Black" , 20])
    lab_text_4.place(x= 30 , y=300)

# ["wee 20","wee 220","wee 2"]

def fun_1():
        global entry_1, entry_2
        entry_1 = Entry(bg="#005d9b", fg="#ffffff" , font=["Yu Gothic UI Light" , 15])
        entry_1.place(x= 180 , y=75 , width=180)
        entry_2 = Entry(bg="#005d9b", fg="#ffffff" , font=["Yu Gothic UI Light" , 15])
        entry_2.place(x= 180 , y=145 , width=180)
        lab_text_1 = Label(text="Введите товар" , bg="#f4ffad", fg="#005d9b" , font=["Yu Gothic UI Light" , 15])
        lab_text_1.place(x= 10 , y=70)
        lab_text_2 = Label(text="Введите кол-во" , bg="#f4ffad", fg="#005d9b" , font=["Yu Gothic UI Light" , 15])
        lab_text_2.place(x= 10 , y=140)
        button_1 = Button(text="следующий товар" , command=fun_b_1)
        button_1.place(x=30 , y=200)
        button_2 = Button(text="завершить ввод" , command=fun_b_2)
        button_2.place(x=130 , y=200)




all_menu = Menu(tearoff=0)


num_radio = IntVar()
all_menu.add_radiobutton(label="Новый покупатель", variable=num_radio ,value=1, command=fun_1)
all_menu.add_separator()
all_menu.add_radiobutton(label="b2", variable=num_radio ,value=2)
all_menu.add_separator()
all_menu.add_radiobutton(label="b3", variable=num_radio ,value=3)



main_menu = Menu()
main_menu.add_cascade(label="all_menu" , menu=all_menu)





window.config(menu=main_menu)
window.mainloop()