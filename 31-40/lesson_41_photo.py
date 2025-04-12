# pip install pillow


from tkinter import *
from PIL import Image , ImageTk
 
root = Tk()
root.geometry("600x500")
 
image = Image.open("photo_n1.png")
photo = ImageTk.PhotoImage(image)
label_photo = Label(image=photo)
label_photo.place(x=10 , y=10)

root.mainloop()


