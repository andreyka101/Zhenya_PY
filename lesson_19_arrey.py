from array import array


arr = array("b" , [100,2, 30,3 , 6])
# arr = array("h" , [200,2,3])
# arr = array("f" , [1.3 , 45.7 , 3.9])
# print(arr)
# print(arr[0])

# print(1.3 + 0.1)



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



# print(arr.typecode)



# print(arr.itemsize)



# print(arr.buffer_info())



# print(arr)
# arr.byteswap() 
# print(arr)



# print(arr.tobytes())



# arr_2 = array("h")
# print(arr_2)
# # arr_2.frombytes(b"d\x00\x02\x03")
# arr_2.frombytes(bytes("d\x00\x02\x03" , encoding="UTF-8"))
# print(arr_2)



# with open("file_arr.txt" , "bw") as file:
#     arr.tofile(file)



# with open("file_arr.txt" , "br") as file:
#     arr_3 = array("h")
#     arr_3.fromfile(file , 2)
# print(arr_3)



# arr.fromlist([12 ,2,3])
# arr.extend([12 ,2,3])
# print(arr)



# print(type(arr))
# print(arr.tolist())
# print(type(arr.tolist()))






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


