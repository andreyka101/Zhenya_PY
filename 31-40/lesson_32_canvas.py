from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#C445FF")


# создание элемента Canvas
canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)
# рисуем в Canvas с помощью методов



# create_line - создать линию
# fill = цвет
# width = толщина линии
# smooth = закругление углов

# задаём координаты точек 
# canV.create_line(0,0 , 100,300 , 500,200 , 400,400 , fill="#DF0000" , width=10 , smooth=True , stipple="gray25")

# задаём координаты точек через список
arr = [0,0 , 100,300 , 500,200 , 400,400]
canV.create_line(arr , fill="#DF0000" , width=10 , smooth=True , stipple="gray25")



# create_rectangle - создать квадрат
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
canV.create_rectangle(50 , 100 ,300,200 , fill="#0E4F68" , width= 0 , outline="#BA0C0C")



# create_polygon - создать многоугольник
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
canV.create_polygon(0,0 , 100,300 , 500,200 ,400,400 , fill="#FCFF40" , width= 5 , outline="#BA690C")



# очистка Canvas
canV.create_rectangle(0 , 0 ,600,500 , fill="#FFFFFF" , width= 0 )


# create_oval - создать овал или круг
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_oval(100 , 100 ,300,300 , fill="#0E4F68" , width= 5 , outline="#BA690C")




canV.create_text(400 , 400 , text="rfgtrfuwdw iejf\nefe[fe;[eoko]]\npefleflp\neefef" , fill="#FF8921" , font="Impact 14" , justify="center")




# canV.create_arc(100 , 100 ,300,300 , start=50 , extent=240, fill="#4DE487" , width= 0 , outline="#D5EA87")




# canV.create_arc(100 , 100 ,300,300 , start=50 , extent=60, fill="#4DE487" , width= 0 , outline="#D5EA87", style="pieslice")



# canV.create_arc(100 , 100 ,300,300 , start=50 , extent=260, fill="#4DE487" , width= 10 , outline="#D5EA87", style="arc")



canV.create_arc(100 , 100 ,300,300 , start=50 , extent=80, fill="#4DE487" , width= 0 , outline="#D5EA87", style="chord")




# arc, chord, or pieslice













window.mainloop()