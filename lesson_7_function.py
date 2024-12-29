
# создание функции 
# def fun_1():
#     print("hello")
#     print("123")

# вызов функции
# print('start')
# fun_1()
# fun_1()
# print('end')




# функции везде
# print(min(2,3))
# print(max(2,3))
# print(sum([2,3]))




# return - возврат значения или переменной
# def fun_2() -> list:
#     print("123")
#     return 2

# print(fun_2())




#! (забыл рассказать) return закрывает функцию
# def fun_3():
#     print("hello")
#     return 0
#     print("world")

# print(fun_3())




# функция это переменная
# def fun_4():
#     print("225")
#     return [1,2,4,6]

# переменная num_f ссылается на функцию fun_4
# num_f = fun_4
# print(num_f())

# мы запускаем функцию с помощью круглых скобок
# print(fun_4())
# если скобоки не писать то получаем ячейку памяти
# print(fun_4)

# типы
# print(type(fun_4()))
# print(type(fun_4))




# функция читает локальную переменную этого файла
# def fun_5():
#     print("num =" , num_1)
#     return num_1 + 2

# num_1 = 3
# fun_5()
# print(fun_5())




# функция не может изменить локальную переменную этого файла
# def fun_6():
#     num_2 = 7
#     print("num_2 =" , num_2)

# num_2 = 4
# fun_6()
# print(num_2)




# когда мы создаём или меняем переменную в функции,
# она становится локальной для этой функции
# def fun_7():
#     num_3 = 7
#     print("num_3 =" , num_3)

# fun_7()
# этой переменной нет
# print(num_3)




# функция может менять только свои локальный переменные
# def fun_8():
#     num_4 = 7
#     print("num_4 =" , num_4)

# num_4 = 1
# fun_8()
# переменная не поменялась
# print(num_4)




# создание глобальной переменной в функции
# теперь переменная доступна везде
# def fun_9():
#     global num_5
#     print("num_4 =" , num_5)
#     num_5 = 7
#     print("num_4 =" , num_5)

# num_5 = 1
# fun_9()
# print(num_5)




# функция принимает значение
# def fun_7(x):
#     print(x)
#     return x * 2
# print(fun_7(5))




# функция принимает несколько значений
# def fun_7(z , x , r):
#     return x + z + r
# print(fun_7(5 , 8, 4))




# тип значения
# def fun_8(z:str):
#     return z 
# print(fun_8(5))




# значение по умолчанию
# def fun_9(z = 7):
#     return z 
# print(fun_9())
# print(fun_9(20))




# функция принимает несколько значений с значениями по умолчанию
# def fun_10(x, z = 5, r = 0):
#     return x , z , r
# print(fun_10(10 , 30))




# способ вставки значений
# def fun_11(x, z = 5, r = 0):
#     return x , z , r
# print(fun_11(r = 9 , x=50))




# функция в функции
# def fun_12():
#     def fun_x():
#         print("juj")
#     print("890")
#     fun_x()
# fun_12()




# у каждой функции своя локальная переменная
# def fun_9():
    
#     def fun_x():
#         num_6 = 3
#         print("fun_x =" , num_6)

#     fun_x()

#     num_6 = 2
#     print("fun_9 =" , num_6)

# num_6 = 1
# fun_9()
# print(num_6)




# пример работы глобальной переменной
# def fun_9():
#     def fun_x():
#         num_6 = 3
#         print("fun_x =" , num_6)

#     fun_x()
#     global num_6

#     num_6 = 2
#     print("fun_9 =" , num_6)

# num_6 = 1
# fun_9()
# print(num_6)




# пример создания функции
# эта функция возвращает длину 
# def super_len(arr_loc: list):
#     num = 0
#     for i in arr_loc:
#         num+=1
#     return num

# arr = [1,2,3,4,5]
# print(super_len(arr))







# dz 
# задание 1
# Написать функцию, выводящую на экран 
# прямоугольник с высотой Y и шириной X


# задание 2
# написать функцию которая принимает два числа и проверяет , если числа ровны вернёт True , если нет вернёт False


# задание 3
# написать функцию которая создаёт список случайных чисел , 
# функция принимает данные: длина списка , min , max


# задание 4
# Написать функцию дискриминант, которая принимает три числа