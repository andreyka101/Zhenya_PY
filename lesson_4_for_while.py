# операторы присваивания 
# num_x = 100
# num_x -= 3
# num_x += 3
# num_x /= 3
# num_x //= 3
# num_x %= 3
# num_x *= 3
# num_x **= 3




# цикл while работает когда значение True
# print("start")
# while(True):
#     print("ok")
# print("end")




# если значение False то цикл while не запустится
# print("start")
# while(False):
#     print("ok")
# print("end")




# все логические операторы if работают c while
# num = 0
# while(num <20):
#     print("ok" , num)
#     num += 1
# print("end" , num)




# num_2 = input("ввод/++")
# while(num_2 != "exit" and num_2 != "1"):
#     print(num_2 , "(no exit)")
#     num_2 = input("ввод/++")

# print("😎")





# цикл for работает какое то количество раз
# for i in range(10):
#     print(i)



# функция range даёт for диапазон чисел по которым for должен проходить
# print(range(20))



# num_2 = 20
# если range задать начало и конец то он не будет доходить до конца
# по этому пишем +1
# for index in range(2 , num_2+1):
#     print(index)

# print("end for index =" , index)



# памятка range
# range(x, y, z)
# x - start
# y - stop
# z - step



# for i in range(0 , 20 , 3):
#     print(i)




# шаг может быть отрицательным
# for i in range(50 , 20-1 , -3):
#     print(i)




# функция len возвращает длину строки
# print(len("qwerty"))
# num_str = "12345fefefef"
# print(len(num_str))




# через for можем получить каждый символ отдельно и его индекс
# num_str_2 = "qweryuo[';lkjhgdsdf]"
# for i in range(len(num_str_2)):
#     print(i)
#     print(num_str_2[i])
#     print("------")




# for проходится по всей строки и сразу получаем её символ
# for sym in num_str_2:
#     print(sym)





# цикл в цикле - двух мерный цикл
# for x in range(10):
#     print("x =" , x)
#     for y in range(10):
#         print(y)
#     print("-------end y")




# f строка
# print(str(4) + "=r")
# print(f"4{False}54545{4}=r")



# таблица
# for x in range(10):
#     answer = ""
#     for y in range(10):
#         answer += f"{x}{y}  "
#     print(answer)








# дз

# Задание 1. Напишите программу, в которой в  цикле пользователь вводит два числа, а программа выводит их сумму.
# Цикл работает пока пользователь не введет "Y" или "y".

# Задание 2. Написать программу-конвертер валют.
# Реализовать общение с пользователем через меню.
# Программа работает пока пользователь не введет "Y" или "y".

# Задание 3. Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Программа должна задавать от 3х вопросов.

# Задание 4. Вывести на экран ромб из звездочек.

# Задание 5. Вывести на экран икс из звездочек.
