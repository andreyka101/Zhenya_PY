
# функция это переменная
# def fun(x):
#     return x*2
# print(fun(4))
# print(fun)
# fun_num = fun
# print(fun_num(7))



# создание лямбды
# лямбда всегда возвращает значение
# num = 3
# lam = lambda: num * 2
# print(lam)
# print(lam())



# передача лямбде значения
# lam_2 = lambda x: x * 3
# print(lam_2(4))
# print(lam_2(2))



# передача лямбде несколько значений
# lam_3 = lambda x , y , z: x+y+z
# print(lam_3(1,2,3))



# значение по умолчанию в лямбде
# lam_3 = lambda x = 9: x + 100
# print(lam_3(1))
# print(lam_3())



# значение по умолчанию в лямбде
# lam_3 = lambda y, x = 9: x + y
# print(lam_3(1))
# print(lam_3(2,3))



# лямбду можно не сохранять
# print(lambda x = 1: x + 100)
# print((lambda x = 1: x + 100)())
# print((lambda x = 1: x + 100)(23))



# обычное условие
# num_x1 = 7
# if(num_x1 > 5):
#     answer_1 = "yes"
# else:
#     answer_1 = "not"
# print(answer_1)



# условие в одну строку
# num_x2 = 2
# answer_2 = "yes" if(num_x2 > 5) else "not"
# print(answer_2)
# print("yes" if(num_x2 > 5) else "not")



# условие в лямбде
# lam_3 = lambda x , y: x if(x > y) else x*y
# print(lam_3(3,5))
# print(lam_3(5,3))



# лямбда в условие
# num = 5
# lam_if_1 = (lambda x: x*2) if(num > 4) else (lambda z: z**5)
# print(lam_if_1(3))



# лямбда возвращает лямбду
# lam_3 = lambda: (lambda z=1: z**5)
# print(lam_3()(5))



# лямбда возвращает условие которое возвращает лямбду 🙂
# lam_3 = lambda w: (lambda x: x*2) if(w > 4) else (lambda z: z**5)
# print(lam_3(5)(2))





# map(fun, arr) - использует функцию fun к каждому элементу arr
# def fun_1(x):
#     return x + 1
# arr = [1,2,3,4,5]
# чтобы map корректно работала её нужно вызывать в функции list
# arr_2 = list(map(fun_1 , arr))
# print(arr)
# print(arr_2)



# использование лямбды в функции map
# arr_3 = [1,2,3,4,5]
# arr_3 = list(map(lambda x: x*2 , arr_3))
# print(arr_3)



# map - принимает до шесть списков
# lambda x, y - x элемент первого списка , y элемент второго списка
# arr_4 = [1,2,3,4,5]
# arr_5 = [6,7,8,9,0]
# arr_6 = list(map(lambda x, y: x+y , arr_4 , arr_5))
# print(arr_6)



# filter - он фильтрует
# arr_7 = [1,2,3,4,5,6]
# arr_7 = list(filter(lambda x: x <= 3 , arr_7))
# print(arr_7)



# умножаю каждый элемент списка который находится в списке
# arr_8 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# def fun_2(element_arr):
#     print(element_arr)
#     return list(map(lambda x: x * 2 , element_arr))
# arr_8 = list(map(fun_2 , arr_8))
# print(arr_8)



# тоже самое , но здесь лямбда в лямбде
# arr_9 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# arr_9 = list(map(lambda e_arr: list(map(lambda x: x+100 , e_arr)) , arr_9))
# print(arr_9)






# дз
# задачи на лямбду (lambda):
# номер 1
# дан список чисел все числа которые равны 1, 2, 3 должны стать числом 0 

# номер 2
# дан список чисел и строк убрать все строки из списка

# номер 3
# даны два списка чисел которые имеют одинаковый размер 
# написать программу которая сравнивает элемент каждого списков и сохраняет самый большой
# пример: 
#     даны списки
#         ar1 = [1,3,6]
#         ar2 = [3,9,2]
#         ответ : [3,9,6]

# номер 4
# дан список в котором списки с числами ,каждое число списка умножить на num
# переменная num прибавляется на 1 с каждым новым списком (num изначально равен 2)


