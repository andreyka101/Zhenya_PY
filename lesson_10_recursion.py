
# def fun_2(x):
#     x+=1
#     print("fun_2 =" , x)
#     return x 


# def fun_1(num):
#     num+=1
#     print("fun_1 =" , num)
#     return fun_2(5) 
# print(fun_1(3))




# def fun_2(x):
#     x+=1
#     print("fun_2 =" , x)
#     return x 


# def fun_1(num):
#     num+=1
#     print("fun_1 =" , num)
#     return fun_2(num) 
# print(fun_1(3))




# num_1 = 10
# def fun_3():
#     global num_1
#     num_1 -= 1
#     print(num_1)
#     if(num_1 == 0):
#         return "end"
#     else:
#         return fun_3()

# print(fun_3())





# def fun_3(num):
#     print(num)
#     if(num == 0):
#         return "end"
#     else:
#         return fun_3(num - 1)

# print(fun_3(5))





# def fun_3(num , save = 0):
#     print("num =" , num , " save =" , save)
#     if(num == 0):
#         return save
#     return fun_3(num - 1 , save + num)
# print(fun_3(5))





# def fun_3(arr_loc:list , index = 0 , save = 0):
#     print("index =" , index , "arr_loc =" , arr_loc , " save =" , save)
#     if(len(arr_loc) == index):
#         return save
#     # save += arr_loc[index]
#     # return fun_3(arr_loc , index + 1 , save)

#     return fun_3(arr_loc , index + 1 , save + arr_loc[index])

# arr = [1,2,3,4,5,6,7]
# print(fun_3(arr))





def fun_3(arr_loc:list , index = 0 , arr_save = []):
    print("index =" , index , "arr_loc =" , arr_loc , " save =" , arr_save)
    if(len(arr_loc) == index):
        return arr_save
    
    # arr_save.append(arr_loc[index] + 1)

    if(arr_loc[index] % 2 == 0):
        arr_save.append(arr_loc[index])
    else:
        arr_save.append("ok")


    return fun_3(arr_loc , index + 1 , arr_save)




arr = [1,2,3,4,5,6,7]
print(fun_3(arr))







