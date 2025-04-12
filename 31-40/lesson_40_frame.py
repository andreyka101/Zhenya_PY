from tkinter import *
 
root = Tk()
root.title("METANIT.COM")
root.geometry("600x500")
 
frame = Frame(bg="#000")
name_label = Label(frame, text="Введите имя")
name_label.place(x=10 , y=10)
 
frame.place(x=200 , y=0 , width=100 , height=80)

root.mainloop()