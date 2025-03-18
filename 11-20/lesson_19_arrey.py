

# нужная ссылка
# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html

from array import array


# создаём массив
# array(r , s)
# r - режим массива (размер каждой ячейки в массиве , таблица в ссылке)
# s - список (можно не писать)

# варианты массивов:
arr = array("b" , [100,2, 30,3 , 6]) # int
# arr = array("h" , [200,2,3]) # int
# arr = array("f" , [1.3 , 45.7 , 3.9]) # float


# работаем с массивом как со списком
# print(arr)
# print(arr[0])

# print(1.3 + 0.1)



# у массива есть методы списков:
# array.append(х)
# array.count(х)
# array.index(х) 
# array.insert(n, х)
# array.pop(i)
# array.remove(х)
# array.reverse()
# array.extend(iter) 

# arr.append(50)
# print(arr)



# возвращает режим массива (символ при создании массива)
# print(arr.typecode)



# размер в байтах каждого элемента в массиве
# print(arr.itemsize)



# кортеж (ячейка памяти, длина масива). Полезно для низкоуровневых операций.
# print(arr.buffer_info())



# .byteswap() - преобразовывает байты
# print(arr)
# arr.byteswap() 
# print(arr)



# .tobytes() - преобразовывает к байтам
# print(arr.tobytes())



# frombytes(x) - делает массив из байт
# arr_2 = array("h")
# print(arr_2)
# b"" - строка байт
# # arr_2.frombytes(b"d\x00\x02\x03") # вар 1
# bytes(b, r) - превращает строку (b) в байты для работы нужно указать кодировку (r)
# arr_2.frombytes(bytes("d\x00\x02\x03" , encoding="UTF-8")) # вар 2
# print(arr_2)



# .tofile(f) - сохраняет массив в открытый файл (f) , файл сохраняется в байтах
# with open("file_arr.txt" , "bw") as file:
#     arr.tofile(file)



# .fromfile(f , n) - записывает (n) чисел из (f) файла в массив , числа в файле должны быть в байтах
# with open("file_arr.txt" , "br") as file:
#     arr_3 = array("h")
#     arr_3.fromfile(file , 2)
# print(arr_3)



# .fromlist() - добавление элементов из списка
# arr.fromlist([12 ,2,3])
# тоже самое что extend()
# arr.extend([12 ,2,3])
# print(arr)



# .tolist() - преобразование массива в список
# print(type(arr))
# print(arr.tolist())
# print(type(arr.tolist()))





# сортировка пузырьком
def sort_arr(arr_loc):
    for r in arr_loc:
        for i in range(len(arr_loc) - 1):
            if(arr_loc[i] > arr_loc[i+1]):
                print(arr_loc[i] , arr_loc[i+1])
                el = arr_loc[i]
                arr_loc[i] = arr_loc[i + 1]
                arr_loc[i + 1] = el
                print(arr_loc)
    
    return arr_loc

print(arr)
print(sort_arr(arr))






# дз
# номер 1
# создайте много поточную сортировку пузырьком