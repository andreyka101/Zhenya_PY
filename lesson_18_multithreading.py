import time 
import threading



# def fun_1():
#     print("start - fun_1")
#     time.sleep(3)
#     print("end - fun_1")


# fun_1()
# for i in range(10):
#     print(i)





def fun_1():
    print("start - fun_1")
    time.sleep(3)
    print("end - fun_1")


thread_1 = threading.Thread(target=fun_1)
thread_1.start()


for i in range(10):
    print(i)


thread_1.join()
print("hello")


# thread_2 = threading.Thread(target=fun_1)
# thread_2.start()
