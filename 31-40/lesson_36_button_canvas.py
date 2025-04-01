from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#C445FF")



canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)




def fun_1():
    canV.config(bg="#5FFFCC")

def fun_2():
    button_arr[1]["background"]= "#8222FF"




# список кнопок
button_arr = [
    {
        "x":50,
        "y":50,
        "width":160 + 50,
        "height":100 + 50,
        "background": "#FFED22",
        "active": False,
        "text":"hello\n world",
        "command": fun_1,
    },
    {
        "x":250,
        "y":300,
        "width":250 + 250,
        "height":150 + 300,
        "background": "#22E9FF",
        "active": False,
        "text":"hrrgrigrjig\neofeofekfok\niejiefj",
        "command": fun_2,
    },
]


# рендерим кнопки и текст в них
for element in button_arr:
    canV.create_rectangle(element["x"] , element["y"] , element["width"] , element["height"] , fill=element["background"] , width=0)
    canV.create_text((element["width"] + element["x"])/2, (element["height"] + element["y"])/2, text=element["text"] , justify="center" , font="s 14")






def fun_motion(event):
    window.title(f"{event.x} / {event.y}")

    for element in button_arr:
        if(event.x >= element["x"] and event.x <= element["width"] and event.y >= element["y"] and event.y <= element["height"] and not element["active"]):
            canV.create_rectangle(element["x"] , element["y"] , element["width"] , element["height"] , fill="#4D4D4D" , width=0)
            canV.create_text((element["width"] + element["x"])/2, (element["height"] + element["y"])/2, text=element["text"] , justify="center" , font="s 14" , fill="#fff")
        elif(not element["active"]):
            canV.create_rectangle(element["x"] , element["y"] , element["width"] , element["height"] , fill=element["background"] , width=0)
            canV.create_text((element["width"] + element["x"])/2, (element["height"] + element["y"])/2, text=element["text"] , justify="center" , font="s 14")
canV.bind("<Motion>" , fun_motion)




def fun_click(event):
    window.title(f"{event.x} / {event.y}")

    for element in button_arr:
        if(event.x >= element["x"] and event.x <= element["width"] and event.y >= element["y"] and event.y <= element["height"]):
            canV.create_rectangle(element["x"] , element["y"] , element["width"] , element["height"] , fill="#DA0000" , width=0)
            canV.create_text((element["width"] + element["x"])/2, (element["height"] + element["y"])/2, text=element["text"] , justify="center" , font="s 14")
            element["active"] = True
            element["command"]()
        else: 
            element["active"] = False
            canV.create_rectangle(element["x"] , element["y"] , element["width"] , element["height"] , fill=element["background"] , width=0)
            canV.create_text((element["width"] + element["x"])/2, (element["height"] + element["y"])/2, text=element["text"] , justify="center" , font="s 14")
canV.bind("<Button-1>" , fun_click)







window.mainloop()