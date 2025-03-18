def calc():
    x1= int(input("==>"))
    x2= int(input("==>"))
    d= input("введи действие")
    if (d== "+"):
        answer= x1 + x2
        print(answer)
    elif (d== "-"):
        answer= x1 - x2
        print(answer)
    elif (d== "/"):
        answer= x1 / x2
        print(answer)
    elif (d== "*"):
        answer= x1 * x2
        print(answer)
    else:
        print("error")

    with open("his.txt", "a", encoding="utf-8") as history:
        history.write(str(answer))

print(calc())


with open("his.txt", "r", encoding="utf-8") as history:
    print("История вычислений:")
    print(history.read())