from tkinter import *


window = Tk()
window.title("lesson 28")
window.geometry("600x500")
window.config(bg="#C445FF")


canV = Canvas(height=500 , width=600 , bg="#ffffff")
canV.place(x=0 , y=0)


# старые координаты мыши
coords_obj ={
    "x":None,
    "y":None,
}



#NOTE - paint карандаш v1
# def funB1(event):
#     #LINK - создаём круг при движении мыши
#     canV.create_oval( event.x-5 , event.y-5 ,event.x + 5 , event.y + 5 , fill="black")
# canV.bind("<B1-Motion>" , funB1)




#NOTE - paint карандаш v2
# def funB1(event):
#     global coords_obj
#     if(event.state == 264):
#         if(coords_obj["x"] == None):
#             coords_obj["x"] = event.x
#             coords_obj["y"] = event.y
#         #LINK - создаем линию между старыми и новыми координатами мыши
#         canV.create_line( coords_obj["x"] , coords_obj["y"] ,event.x , event.y , fill="black" , width=10 , smooth=True)
#         #LINK - новые координаты становятся старыми
#         coords_obj["x"] = event.x
#         coords_obj["y"] = event.y
#     if(event.state == 8):
#         coords_obj["x"] = None
#         coords_obj["y"] = None
# canV.bind("<Motion>" , funB1)




#NOTE - paint карандаш v3
def funB1(event):
    global coords_obj
    if(event.state == 264):
        if(coords_obj["x"] == None):
            coords_obj["x"] = event.x
            coords_obj["y"] = event.y
        

        #TODO - вар. 1: 
        #LINK - если старыми и новыми координатами мыши находятся на большом расстоянии рисуем линию
        # ,если на маленьком рисуем круг
        # length_coords_X = coords_obj["x"] - event.x
        # length_coords_Y = coords_obj["y"] - event.y
        # if(length_coords_X < 0):
        #     length_coords_X = length_coords_X * -1
        # if(length_coords_Y < 0):
        #     length_coords_Y = length_coords_Y * -1
        # print(length_coords_X)
        # if(length_coords_X > 4 or length_coords_Y > 4):
        #     canV.create_line( coords_obj["x"] , coords_obj["y"] ,event.x , event.y , fill="black" , width=10 , smooth=True)
        # else:
        #     canV.create_oval( event.x-5 , event.y-5 ,event.x + 5 , event.y + 5 , fill="black")
        

        #TODO - вар. 2: 
        #LINK - более простой способ рисуем линию и круг одновременно
        canV.create_line( coords_obj["x"] , coords_obj["y"] ,event.x , event.y , fill="black" , width=10 , smooth=True)
        canV.create_oval( event.x-5 , event.y-5 ,event.x + 5 , event.y + 5 , fill="black")



        coords_obj["x"] = event.x
        coords_obj["y"] = event.y
    if(event.state == 8):
        coords_obj["x"] = None
        coords_obj["y"] = None
canV.bind("<Motion>" , funB1)








#NOTE - paint ластик
def funB3(event):
    canV.create_oval( event.x-20 , event.y-20 ,event.x + 20 , event.y + 20 , fill="white" ,width=0)
canV.bind("<B3-Motion>" , funB3)

window.mainloop()