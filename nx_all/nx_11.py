from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#000000")



canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)





canV.create_line(0,300 , 300, 300, fill="#000000" , width=5)

mainloop()