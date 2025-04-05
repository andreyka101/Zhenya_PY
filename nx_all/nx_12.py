
from tkinter import *

window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#000000")

canV = Canvas(height=500, width=600, bg="#ffffff")
canV.place(x=0, y=0)


a = 0
style1 = "pieslice"
radius = 100


def fun_1(val):
    global a, style1
    a = int(val)
    canV.delete("arc")
    if a == 360:
        style1 = "chord"
        canV.create_arc(100, 100, 300, 300, start=1, extent=a - 1,fill="#4DE487", width=4, outline="#D5EA87", style=style1, tags="arc")
    else:
        style1 = "pieslice"
        canV.create_arc(100, 100, 300, 300, start=1, extent=a,fill="#4DE487", width=4, outline="#D5EA87", style=style1, tags="arc")
    

def fun_2(val):
    global radius
    radius = int(val)
    canV.delete("arc") 

    canV.create_arc(100, 100, radius, radius, start=1, extent=a, 
                    fill="#4DE487", width=4, outline="#D5EA87", style=style1, tags="arc")
    



scale_1 = Scale(orient=HORIZONTAL, command=fun_1, from_=1, to=360, length=300)
scale_1.place(x=30, y=10)

scale_2 = Scale(orient=HORIZONTAL, command=fun_2, from_=100, to=400, length=300)
scale_2.place(x=30, y=60)




canV.create_arc(100, 100, 300, 300, start=1, extent=a,fill="#4DE487", width=0, outline="#D5EA87", style=style1, tags="arc")




window.mainloop()