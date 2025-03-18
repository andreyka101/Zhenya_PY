
arr = [1, 2, 3.1, 1, 4, 5, 1 , 8]


# arr.append(x) - Добавляет элемент x в конец списка
arr.append("text")
arr.append("text")
arr.append("text")
arr.append("text")
arr.append("text")
arr.append("text")
arr.append("text")
print(arr)

# добавляем список в список
# arr.append([99,98,97])
# print(arr)



# arr.extend(x) - Расширяет список arr, добавляя в конец все элементы списка x
# arr.extend([99,98,97])
# print(arr)



# arr.index(x, i) - Возвращает положение первого элемента со значением x поиск начинается с индекса i (можно не писать)
# print(arr.index(3.1))
# print(arr.index(1 , 2))



# arr.count(x) - Возвращает количество элементов со значением x
# print(arr.count(1))



# arr.insert(i, x) - Вставляет на i индекс элемент x
# arr.insert(3, 999)
# print(arr)



# arr.remove(x) - Удаляет первый элемент в списке, имеющий значение x
# arr.remove(3.1)
# arr.remove(1)
# arr.remove(1)
# print(arr)



# arr.pop(i) - 	Удаляет элемент по индексу i и возвращает его. Если индекс не указан, удаляется последний элемент
# arr.pop(3)
# print(arr.pop(2))
# print(arr.pop())
# print(arr.pop(-2))
# print(arr)



# arr.reverse() - Разворачивает список
# print(arr)
# arr.reverse()
# print(arr)



# arr.sort() - Сортирует список
# print(arr)
# arr.sort()
# print(arr)



# arr.clear() - Очищает список
# arr.clear()
# тоже очищает список
# arr = []
# print(arr)



# arr.copy() - Поверхностная копия списка

# пример без копии
# arr_2 = arr
# print("arr =" , arr)
# print("arr_2 =" , arr_2)
# arr.clear()
# print("arr =" , arr)
# print("arr_2 =" , arr_2)


# пример с копией
# arr_copy = arr.copy()
# print("arr =" , arr)
# print("arr_copy =" , arr_copy)
# arr.clear()
# print("arr =" , arr)
# print("arr_copy =" , arr_copy)






