import json



# file_3 = open("w.json" , "r")
# file_3.close()

def load():
    users = open("w.json", "r")
    arr_2 = json.loads(users.read())

    if (w== "new"):
        print(arr_2)
        arr_2[input("name ==>")] = input("password ==>")
        with open("w.json", "w") as file:
            json.dump(arr_2 , file)



    # elif (w== "del"):



w= input("==>")
while(w != "ex" or w != "exit"):
    load()
    w= input("==>")