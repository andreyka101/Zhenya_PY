inp = input("--")

match(inp):
    case("q"):
        print("I am (q)")
        num = 1
    case("w"):
        print("I am (w)")
        num = 2
    case("e"):
        print("I am (e)")
        num = 3
    case("r"):
        print("I am (r)")
        num = 4
    case("t"):
        print("I am (t)")
        num = 5
    case("y"):
        print("I am (y)")
        num = 6
    case _:
        print("I am not")
        num = 0
        
print(num)