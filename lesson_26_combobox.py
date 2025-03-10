from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 21")
# меняем ширину высоту и координаты окна
window.geometry("700x500")
window.config(bg="#C445FF")


arr = [60 ,  "qwert" , "ipot" , "while" , "26226"]

# Combobox - это совмищение Listbox и Entry
combox = ttk.Combobox(values=arr)
combox.place(x=20 , y=20)



lab_text = Label(font=("" , 14))
lab_text.place(x=250 , y=30)



def fun_get():
    # combox.get() - получаем значение 
    lab_text.config(text=combox.get())
get_but = Button(text="get index" , command=fun_get)
get_but.place(x=40 , y=250)




def fun_rename():
    # combox.insert(i, x) - Вставляет на i индекс строку x
    combox.insert(3 , "XZX")
rename_but = Button(text="rename" , command=fun_rename)
rename_but.place(x=40 , y=300)




def fun_delete():
    # combox.delete(i, x) - удаляет строку начиная с индекса i и длиной x
    combox.delete(0 , END)

delete_but = Button(text="delete" , command=fun_delete)
delete_but.place(x=40 , y=350)



window.mainloop()