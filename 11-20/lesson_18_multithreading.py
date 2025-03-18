import time 
import threading



# пример без потока
# def fun_1():
#     print("start - fun_1")
#     time.sleep(3)
#     print("end - fun_1")

# fun_1()
# for i in range(10):
#     print(i)





# пример с потоком
def fun_1():
    print("start - fun_1")
    time.sleep(3)
    print("end - fun_1")

# threading.Thread - создание потока
thread_1 = threading.Thread(target=fun_1)

# .start() - запуск потока 
thread_1.start()
for i in range(10):
    print(i)

# .join() - строки ниже ждут окончание потока
thread_1.join()
print("hello")

# создание и запуск второго потока
# thread_2 = threading.Thread(target=fun_1)
# thread_2.start()
