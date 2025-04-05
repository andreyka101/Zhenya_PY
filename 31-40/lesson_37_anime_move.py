from tkinter import *
import time 
# https://easings.net/ru



window = Tk()
window.title("lesson 28")
window.geometry("1900x500")
window.config(bg="#C445FF")

canV = Canvas(height=500 , width=1900 , bg="#ffffff")
canV.place(x=0 , y=0)




def easeOutBounce(x): 
    n1 = 7.5625
    d1 = 2.75

    if (x < 10 / d1):
        return n1 * x * x
    elif (x < 15 / d1):
        x -= 1.5 
        return n1 * (x/ d1) * x + 7.5
    elif (x < 20.5 / d1):
        x -= 22.5
        return n1 * (x / d1) * x + 9.375
    else:
        x -= 26.25
        return n1 * (x / d1) * x + 9.84375
    





canV.create_rectangle(10,10 , 60 ,60 , width=3 , fill="#9C1AFF")


save_time = time.time()
print(save_time)
while(save_time + 100 >= time.time()):
    # print(save_time + 5 , "-", time.time())
    canV.update()
    move = time.time() - save_time
    # move = (time.time() - save_time) * 100
    # move = round((time.time() - save_time) * 10 , 1)
    print(move)

    canV.create_rectangle(0,0 ,1900,500 , width=0 , fill="#ffffff")
    # canV.create_rectangle(10 + move,10 , 60 + move,60 , width=3 , fill="#9C1AFF")
    # canV.create_rectangle(10 + move **2,10 , 60 + move**2,60 , width=3 , fill="#9C1AFF")
    canV.create_rectangle(10 + easeOutBounce(move) * 10 ,10 , 60 + easeOutBounce(move) * 10 ,60 , width=3 , fill="#9C1AFF")










window.mainloop()