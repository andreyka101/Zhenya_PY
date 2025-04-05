from tkinter import *

# 1

window = Tk()
window.geometry("600x500")
window.config(bg="#000000")


canV = Canvas(window, width=600, height=500, bg="#ffffff")
canV.place(x=0, y=0)


entry = Entry(window, font=("Arial", 16), bg="#d0d0d0", fg="#000000", justify="center")
entry.place(x=150, y=30, width=300, height=30)


def update_text(event):
    text = entry.get()
    canV.delete("text_frame")  
    x, y = 300, 250 


    canV.create_text(x + 2, y + 2, text=text, font=("Arial", 30, "bold"), fill="#777777", tags="text_frame")


    canV.create_text(x, y, text=text, font=("Arial", 30, "bold"), fill="#000000", tags="text_frame")


    bbox = canV.bbox("text_frame")
    if bbox:
        canV.create_rectangle(bbox[0]-10, bbox[1]-10, bbox[2]+10, bbox[3]+10,
                              outline="#444444", width=4, tags="text_frame")


entry.bind("<KeyRelease>", update_text)


window.mainloop()