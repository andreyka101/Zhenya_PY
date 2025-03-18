
# импортируем библиотеку tkinter
from tkinter import *



# создаём окно 
window = Tk()
# меняем название окна
window.title("lesson 20 start")
# меняем ширину и высоту окна 
window.geometry("700x500")
# цвет окна
window.config(bg="#C445FF")



# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
# font = шрифт и размер текста 
lab_text_1 = Label(text="hello world" , bg="#75FF9A", fg="#FF7530" , font=["Segoe UI Black" , 15])
# placе - координаты и размер элемента
lab_text_1.place(x= 300 , y=200 , height=80 , width=200)



def fun_b_1():
    print("ok")
    # с помощью метода configure или config можно изменить параметры объекта 
    lab_text_1.config(text="text")
    # lab_text_1.configure(text="text")
    # изменяем координаты button_1
    button_1.place(y=30)

# создаём кнопку command вызывает функцию
button_1 = Button(text="but 1" , command=fun_b_1)
button_1.place(x= 300 , y=300)
# не требует координат
# button_1.pack()



# anchor позиционирует относительно окна
# lab_text_2 = Label(text="yes" , bg="#343434", fg="#F8FF22" , font=["" , 15])
# lab_text_2.place(anchor="center" , relx=0.5, rely=0.5)



# для удобного размещения anchor можно менять relx и rely
# lab_text_3 = Label(text="op" , bg="#C3C3C3", fg="#000000" , font=["" , 15])
# lab_text_3.place(anchor="center" , relx=0.5, rely=0.41)





# mainloop() - создаёт бесконечный цикл для отрисовки интерфейса
window.mainloop()





# start
# задача 1
# Создайте игру clicker, при нажатии на кнопку должно число увеличиваться на один

# задача 2
# Сделать игру найди кнопку, при нажатии на кнопку она перемещается в случайное место по координатам ,но не выходит за границы окна




# entry
# Задание 1.
# сделать калькулятор
# проще сделать через два entry для первого и второго числа

# Задание 2.
# сделать страницу регистрации и входа пользователя 
# зарегистрировано может быть много пользователей
