from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Перекрестье")
window.geometry("700x500")
window.config(bg="#b3b8ff")

lab_hor = Label(window, bg="white")
lab_hor.place(x=200, y=250, width=100, height=1)

lab_ver = Label(window, bg="white")
lab_ver.place(x=350, y=150, width=1, height=100)

def fun_1(v):
    lab_hor.place(x=scale_hor.get(), y=250)
    lab_ver.place(x=350, y=scale_ver.get())

scale_hor = Scale(window, from_=100, to=600, orient=HORIZONTAL, label="Горизонтальная", bg="#0b138c", fg="white", command=fun_1)
scale_hor.place(x=200, y=400)

scale_ver = Scale(window, from_=50, to=400, orient=VERTICAL, label="Вертикальная", bg="#0b138c", fg="white", command=fun_1)
scale_ver.place(x=50, y=100)


def fun_2():
    acc_x = 100 - abs(scale_hor.get() - 350) / 3.5
    acc_y = 100 - abs(scale_ver.get() - 250) / 2.5
    accuracy = (acc_x + acc_y) / 2
    lab_result.config(text=f"Точность: {accuracy:.2f}%")

but_update = Button(window, text="Обновить", command=fun_1, bg="#ffffff")
but_update.place(x=300, y=450)

but_check = Button(window, text="Зафиксировать", command=fun_2, bg="#ffffff")
but_check.place(x=400, y=450)

lab_result = Label(window, text="Точность: 100%", bg="#0b138c", fg="white", font=["Arial Black", 15])
lab_result.place(x=280, y=50)

window.mainloop()