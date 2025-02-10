import json



# json.dumps - переводит в json строку
# arr = [1,2,3,4,5,]
# print(arr[0])
# str_arr_j = json.dumps(arr)
# print(str_arr_j[0])
# print(type(str_arr_j))



# перезапись файла json
# file = open("j_file_1.json" , "w")
# file.write(str_arr_j)
# file.read()
# file.close()



# json.load - переводит открытый файл в list или dict
# file = open("j_file_1.json" , "r")
# arr_2 = json.loads(file.read())
# print(arr_2)
# print(type(arr_2))



# json.load - записывает list или dict в открытый файл
s = "key"
obj = {
    "yfwfd":266,
    s:"value",
    3:"qq",
}
# print(obj["key"])
file_3 = open("j_file_1.json" , "w")
json.dump(obj , file_3)



# json.load - переводит данные открытого файла в list или dict
file_3 = open("j_file_1.json" , "r")
arr_3 = json.load(file_3)
print(arr_3)
print(type(arr_3))




