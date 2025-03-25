from tkinter import *
import random


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#C445FF")


canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)



robot_obj={
    "x1":0,
    "y1":0,
    "x2":50,
    "y2":50,
}


# монетка появляется рандомно
rand_x = random.randint(0,11)
rand_y = random.randint(1, 9)
coin_obj={
    "x1":50 * rand_x,
    "y1":50 * rand_y,
    "x2":(50 * rand_x) + 50,
    "y2":(50 * rand_y) + 50,
}


canV.create_rectangle(list(robot_obj.values()) , width=0 , fill="#3B7893")
canV.create_oval(list(coin_obj.values()) , width=0 , fill="#FFEA2E")



def fun(event):
    print(event.keycode)
    # меняем координаты робота
    if((event.keycode == 65 or event.keycode == 37) and robot_obj["x1"] >0):
        robot_obj["x1"]-=50
        robot_obj["x2"]-=50
    elif((event.keycode == 68 or event.keycode == 39) and robot_obj["x2"] < 600):
        robot_obj["x1"]+=50
        robot_obj["x2"]+=50
    elif((event.keycode == 87 or event.keycode == 38) and robot_obj["y1"] >0):
        robot_obj["y1"]-=50
        robot_obj["y2"]-=50
    elif((event.keycode == 83 or event.keycode == 40) and robot_obj["y2"] < 500):
        robot_obj["y1"]+=50
        robot_obj["y2"]+=50

    
    # отрисовка робота
    canV.create_rectangle(0,0 ,600,500, width=0 , fill="#FFFFFF")
    canV.create_rectangle(list(robot_obj.values()) , width=0 , fill="#3B7893")
window.bind("<KeyPress>",fun)

window.mainloop()