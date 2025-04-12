from tkinter import *

window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#000000")


canV = Canvas(window, width=600, height=500, bg="#ffffff")
canV.place(x=0, y=0)

counter = 0
dragging = False
offset_x = 0
offset_y = 0


def fun_click():
    global counter
    counter += 1
    button_click.config(text=f"clicks: {counter}")


def start_drag(event):
    global dragging, offset_x, offset_y
    dragging = True

    offset_x = event.x
    offset_y = event.y


def do_drag(event):
    if dragging:
        canV.coords(window_id, event.x - offset_x, event.y - offset_y)


def stop_drag(event):
    global dragging
    dragging = False


frame = Frame(canV, bg="#dddddd", bd=3, relief=RIDGE)

button_click = Button(frame, text="clicks: 0", font=("Arial", 12), command=fun_click)
button_click.pack(padx=10, pady=10)


window_id = canV.create_window(200, 200, window=frame, anchor="nw")

frame.bind("<Button-1>", start_drag)
frame.bind("<B1-Motion>", do_drag)
frame.bind("<ButtonRelease-1>", stop_drag)

window.mainloop()