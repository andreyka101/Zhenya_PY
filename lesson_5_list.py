
# создание списка
arr = [1, 2, 3.1, 4, 5]
# получаем весь список
print(arr)
# print(type(arr))
# получаем элемент списика по индексу
# print(arr[2])
# print(type(arr[2]))



# создание пустого списка
# arr_x = []
# print(arr_x)



# print(arr)
# меняем элемент списка
# arr[0] = 9
# print(arr)
# перезапись списка
# arr = [0,"yefegf" ,True , None]
# print(arr)



# возвращает длину списка
# print(len(arr))



# перебор списка по индексу
# for i in range(len(arr)):
    # print(arr[i])
    # arr[i] = "hello"
    # arr[i] = arr[i] + 20
# print(arr)



# перебор списка с помощью цикла for
# for el in arr:
#     print(el)



# список в списке
arr_2 = [
        [1,2,3],
        [4,5,6 ,999], 
        [7,8,9]
        ]
# print(arr_2)
# print(arr_2[1])
# print(type(arr_2[1]))
# print(arr_2[1][0])



# получаем элемент списика
# print([5,8,0][1])



# перебор двух мерного списка по индексу
# for x in range(len(arr_2)):
#     for y in range(len(arr_2[x])):
#         print(arr_2[x][y])



# перебор двух мерного списка
# for el_arr in arr_2:
#     for el in el_arr:
#         print(el)





# дз
# Задание 1. Напишите программу, которая с помощью цикла создает список чисел от 1 до 10, а также списки их квадратов и кубов.
# В конце списки выводятся на консоль.

# Задание 2. Написать, программу, которая вычисляет прибыль фирмы за 6 месяцев. Пользователь вводит прибыль 
# фирмы за каждый месяц.

# # 2
pr=[]
for i in range(6):
    pr.append(int(input("==>")))
print(pr)
sum_x = 0
for i in range(6):
    sum_x+=pr[i]
print(sum_x)

# Задание 3. Написать программу, которая выводит список в обратном порядке (можно использовать только метод len()).

# Задание 4. Пользователь вводит длину сторон пятиугольника, каждая сторона заноситься в список, необходимо 
# вычислить периметр пятиугольника (периметр — сумма всех сторон).

# Задание 5. Пользователь вводит прибыль фирмы за год 
# (12 месяцев). Необходимо определить месяц, в котором 
# прибыль была максимальна и месяц, в котором прибыль 
# была минимальна

# Задание 6. Дана температура воздуха за каждый день января. 
# Определить:
# а) среднюю температуру за месяц;
# б) сколько раз температура воздуха опускалась нижеуказанной метки.

# Задание 7. Напишите программу, которая удаляет дубликаты из списка.
