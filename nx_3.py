arr_4 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
num = 1
def fun(x):
    global num
    num += 1
    return x * num
lam_4= list(map(lambda arr_x: list(map(fun, arr_x)) , arr_4))
print(lam_4)