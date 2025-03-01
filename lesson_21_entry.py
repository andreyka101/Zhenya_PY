from tkinter import *


window = Tk()
window.title("lesson 21")
# меняем ширину высоту и координаты окна
window.geometry("700x500+0+0")
window.config(bg="#C445FF")



lab_text_1 = Label(text="hello world" , bg="#75FF9A", fg="#FF7530" , font=["Segoe UI Black" , 15])
lab_text_1.place(x= 300 , y=200 , height=80 , width=200)



# ввод данных
entry_1 = Entry(bg="#101C57", fg="#82DCFF" , font=["Segoe UI Black" , 15])
entry_1.place(x= 300 , y=100 , width=180)



def fun_b_get():
    # entry_1.get() - возвращает текст Entry
    print(entry_1.get())
    lab_text_1.config(text=entry_1.get())
button_get = Button(text="get" , command=fun_b_get )
button_get.place(x= 300 , y=300)



def fun_b_insert():
    # entry_1.get() - возвращает текст Entry
    entry_1.insert(3 , "xxx")
button_insert = Button(text="insert" , command=fun_b_insert )
button_insert.place(x= 300 , y=350)



def fun_b_delete():
    # entry_1.get() - возвращает текст Entry
    # entry_1.delete(2 , 5)
    entry_1.delete(0 , len(entry_1.get()))
button_delete = Button(text="delete" , command=fun_b_delete )
button_delete.place(x= 300 , y=400)








# def fun_b_1():
#     # entry_1.get() - возвращает текст Entry
#     print(entry_1.get())
#     lab_text_1.config(text=entry_1.get())

#     # меняем ширину высоту и координаты окна через Entry
#     window.geometry(entry_1.get())

# button_1 = Button(text="set geo" , command=fun_b_1 )
# button_1.place(x= 300 , y=300)



# def fun_b_2():
#     # получаем ширину высоту и координаты окна
#     lab_text_1.config(text=window.geometry())
# button_2 = Button(text="get geo" , command=fun_b_2 )
# button_2.place(x= 100 , y=300)






window.mainloop()