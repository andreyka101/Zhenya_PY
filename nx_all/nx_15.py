import time
from tkinter import *

window = Tk()
window.title("Анимация для даунов")
window.geometry("600x500")
window.config(bg="#C445FF")

canV = Canvas(height=500, width=600, bg="#ffffff")
canV.place(x=0, y=0)

x = 0

def fun():
    global x
    while True:
        x = (x + 1) % 360
        canV.delete("arcc")
        canV.create_arc(200, 200, 300, 300, start=x, extent=260, fill="#000000", width=10, outline="#000000", style="arc", tags="arcc")
        window.update()
        time.sleep(0.02)

fun()
window.mainloop()
