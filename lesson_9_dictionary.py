
# создание словаря
# obj = {
#     '233':5,
#     2:27,
#     'qwer':"text",
# }

# получаем словарь
# print(obj)

# получаем значение по ключу
# print(obj['233'])
# print(obj[2])



# словарь это список
# arr_obj = {
#     0:"q",
#     1:"w",
#     2:"e",
#     3:"r",
# }

# print(arr_obj)
# print(arr_obj[0])




# перезапись значения по ключу
# print(obj['233'])
# obj['233'] = 8
# print(obj['233'])




# создаём ключ значение
# print(obj)
# obj['super'] = "gg"
# print(obj)
# print(obj['super'])




# methods



# метод get возвращает значение ключа, но если его нет возвращает None
# print(obj)
# print(obj.get('233'))
# print(obj.get('111'))
# print(obj)

# здесь будет ошибка
# print(obj['111'])




# метод setdefault(key, val) - возвращает значение key, но если его нет создает key со значением val или None
# print(obj)
# print(obj.setdefault('233'))
# print(obj.setdefault('111' , 0))
# print(obj)




# метод keys возвращает список ключей
# arr_keys = obj.keys()
# print(arr_keys)
# print(type(arr_keys))

# для дальнейшей работы нужно использовать функцию list
# arr_keys = list(arr_keys)
# print(arr_keys[0])




# метод values возвращает список значений
# arr_values = obj.values()
# print(arr_values)
# print(type(arr_values))




# метод update(dist) - обновляет словарь obj, добавляя пары словаря dist
# print(obj)
# obj.update({
#     1:"q",
#     18:666,
# })
# print(obj)




# метод pop удаляет по ключу и возвращает значение
# print(obj)
# print(obj.pop("233"))
# print(obj)




# метод popitem удаляет по ключу и возвращает её
# print(obj)
# print(obj.popitem())
# print(obj)




# очищает словарь
# obj.clear()



# возвращает копию словаря
# obj.copy()
# obj_2 = obj




# создаёт разные ключи с одним значением 
# obj = obj.fromkeys(["qw","xny" , 60] , 2)
# print(obj)




# for перебирает все ключи словаря
# for i in obj:
#     print(i , " = " , obj[i])




# метод items позволяет for перебирать ключ и значение словаря
# for key , val in obj.items():
#     print(key , " = " , val)





# способ использования словаря:

# пример с if
# inp = input("-- ")
# if(inp == "q"):
#     num = 1 
# elif(inp == "w"):
#     num = 2 
# elif(inp == "e"):
#     num = 3 
# elif(inp == "r"):
#     num = 4 
# elif(inp == "t"):
#     num = 5 
# elif(inp == "y"):
#     num = 6
# print(num) 



# тоже самое ,но словарь
# inp = input("-- ")
# obj_if = {
#     "q":1,
#     "w":2,
#     "e":3,
#     "r":4,
#     "t":5,
#     "y":6,
# }
# num = obj_if[inp]
# print(num) 




# работа с функцией
# def fun_1():
#     print("i fun_1:")
#     return 45

# def fun_2():
#     print("i fun_2:")
#     return [1,2,3]
# obj_if = {
#     "q":fun_1,
#     "w":fun_2,
# }
# print(fun_1)
# print(fun_1())

# print(obj_if["q"])
# print(obj_if["q"]())








# дз
# лёгкая сложность задание 1
# создайте два словаря объедените их и выведите в консоль


# средняя сложность задание 2
# Создайте словарь, в котором ключами будут числа от 1 до 10, 
# а значениями эти же числа, возведенные в куб


# средняя сложность задание 3
# Создайте словарь из строки 'hello python' следующим образом: 
# в качестве ключей возьмите символ строки, 
# а значениями пусть будет индекс символа


# сложная сложность задание 4
# Даны два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.


