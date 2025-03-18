from tkinter import *


window = Tk()
window.title("lesson 21")
# меняем ширину высоту и координаты окна
window.geometry("700x500")
window.config(bg="#C445FF")

def fun_1():
    window.config(bg="#FF8C45")

def fun_2():
    print(num_check.get())
    if(num_check.get()):
        window.geometry("400x300")
    else:
        window.geometry("700x500")

def fun_3():
    if(num_radio.get() == 1):
        window.config(bg="#D6D6D6")
    elif(num_radio.get() == 2):
        window.config(bg="#717171")
    elif(num_radio.get() == 3):
        window.config(bg="#3D3C3C")




# file_menu = Menu(all_menu , tearoff=0)
file_menu = Menu(tearoff=0)
file_menu.add_command(label="fs1")
file_menu.add_command(label="fs2")
file_menu.add_command(label="fs3")
file_menu.add_command(label="fs4")




# создание меню
all_menu = Menu(tearoff=0)

# кнопка для меню
all_menu.add_command(label="but")

# разделение
all_menu.add_separator()

# checkbox
num_check = BooleanVar()
all_menu.add_checkbutton(label="check", variable=num_check , command=fun_2)

# radiobutton
num_radio = IntVar()
all_menu.add_radiobutton(label="b1", variable=num_radio ,value=1, command=fun_3)
all_menu.add_radiobutton(label="b2", variable=num_radio ,value=2 , command=fun_3)
all_menu.add_radiobutton(label="b3", variable=num_radio ,value=3 , command=fun_3)

# создание под меню
all_menu.add_cascade(label="f menu" , menu=file_menu)


# создание главного меню
main_menu = Menu()
main_menu.add_command(label="color" , command=fun_1)
main_menu.add_cascade(label="all_menu" , menu=all_menu)



# подключение главного меню
window.config(menu=main_menu)
window.mainloop()





# дз

# Задание 1. Написать имитацию кассового аппарата для магазина.
# Кассир должен выбрать товар и ввести его количество, 
# затем выбрать следующий товар. По завершению ввода 
# вывести на экран всю сумму покупки.
# В списке товаров должно быть не меньше
# 4-х товаров, должна отображаться их цена. Предусмотреть 
# неправильно вводимые данные.
# доп:
# . Хранение общей выручки магазина;
# . Ограничить количество товара в магазине



