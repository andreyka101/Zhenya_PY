# file = open("file_1.txt")
# print(file)




# режимы открытия:
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись




# file = open("file_1.txt" , "r")
# print(file.read())



# file_2 = open("file_1.txt" , "w")
# file_2.write("ygdgwywygd")
# file_2.close()



# file_3 = open("file_1.txt" , "r")
# print(file_3.read())



# file_4 = open("file_1.txt" , "a")
# file_4.write("12345")
# file_4.close()



# file_5 = open("lesson_11_match.py" , "r" , encoding="UTF-8")
# print(file_5)
# print(file_5.read())



# file_6 = open("pack_file/file_2.txt" , "r")
# print(file_6.read())



# file_7 = open("../del_file_global.txt" , "r")
# print(file_7.read())



# file_8 = open("../../фаилы/del_s.txt" , "r")
# print(file_8.read())



# file_9 = open("C:\main_brain\programsPython\del_file_global.txt" , "r")
# print(file_9.read())




# with open("file_1.txt" , "w") as file:
#     print(file)
#     file.write("ygdgwywygd")

# file_r = open("file_1.txt" , "r")
# print(file_r.read())




# print("12345\n    67890")
file_10 = open("file_1.txt" , "r")
# print(file_10.read())
# print(file_10.readlines())
print(file_10.read().split("\n"))


s= "qwww-55t5t-4444"
print(s.split("-"))



