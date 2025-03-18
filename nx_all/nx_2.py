def fun(num, num_1 , answer = 1):
    print(num, num_1 , answer)
    if num_1 == 0:
        return answer 
    elif num_1 > 0:
        return fun(num * num, num_1 - 1 , answer * num)
    # else:
    #     return answer 


num = int(input("==>"))
num_1 = int(input("==>"))
print(fun(num, num_1))