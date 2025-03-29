from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x600")
window.config(bg="#000000")



canV = Canvas(height=600 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)

# canV.create_oval(-1,-1 , 1,1)
# canV.create_oval(-2+300,-2+300 , 2+300,2+300 , fill="#000")


canV.create_oval(-3+300,-3+300 , 3+300,3+300 , fill="#000")


for i in range(-200 , 200 , 1):
    # canV.create_oval(i+300, 20+300 , i+300, 20+300 , fill="#000")


    # canV.create_oval(i +299, i **2 +299 , i +301, i**2 +301 , fill="#000")

    
    canV.create_oval((i *10) +299, (i**2)*-1 +299 , (i *10) +301, (i**2)*-1 +301 , fill="#000")



mainloop()