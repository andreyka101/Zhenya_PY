from tkinter import *


window = Tk()
window.title("lesson 21")
# меняем ширину высоту и координаты окна
window.geometry("700x500")
window.config(bg="#C445FF")


arr = [60 ,  "qwert" , "ipot" , "while" , "26226"]


# Listbox - Отображение списка в интерфейсе 
list_box = Listbox(listvariable= Variable(value=arr) ,font=("" , 12))
list_box.place(x=20 , y=20)



lab_text = Label(font=("" , 14))
lab_text.place(x=250 , y=30)


entry_1 = Entry(bg="#101C57", fg="#82DCFF" , font=["Segoe UI Black" , 15])
entry_1.place(x= 250 , y=70 , width=180)





def fun_get_index():
    # list_box.curselection() - возвращает выбранный индекс 
    print(list_box.curselection()[0] + 100)
    lab_text.config(text=f"index {list_box.curselection()[0]}")
get_index_but = Button(text="get index" , command=fun_get_index)
get_index_but.place(x=40 , y=250)



def fun_get():
    # list_box.get(i) - возвращает элемент индекса i
    print(list_box.get(0))
    lab_text.config(text = list_box.get(list_box.curselection()[0]))
get_value_but = Button(text="get value" , command=fun_get)
get_value_but.place(x=40 , y=300)



def fun_create():
    # list_box.insert(x , element) - вставляет новый элемент на x индекс
    # list_box.insert(0 , "none")
    list_box.insert(0 , entry_1.get())

create_but = Button(text="create" , command=fun_create)
create_but.place(x=40 , y=350)



def fun_delete():
    # list_box.delete(i) - удаляет элемент по индексу i
    # list_box.delete(0)
    # list_box.delete(0 , 2)
    list_box.delete(list_box.curselection()[0])

delete_but = Button(text="delete" , command=fun_delete)
delete_but.place(x=40 , y=400)



def fun_rename():
    list_box.insert(list_box.curselection()[0] , entry_1.get())
    list_box.delete(list_box.curselection()[0])

rename_but = Button(text="rename" , command=fun_rename)
rename_but.place(x=40 , y=450)



window.mainloop()