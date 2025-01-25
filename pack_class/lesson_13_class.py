

class Dogs():
    num_x = 3
    def __init__(self , name_loc):
        # print("hi")
        # num_loc = 8
        # print("num_loc =" , num_loc)

        # print("self.num_x =" , self.num_x)
        self.num_x = 100
        # print("self.num_x =" , self.num_x)
        
        self.str_text = "wdvdvvdg"
        # print("self.str_text =" , self.str_text)

        # print(name_loc)
        self.name = name_loc

        self.__priv_num = 1
        self.__priv_num +=10

    
    def fun(self):
        print("hello fun")
        print("name dog =" , self.name)
        self.run()


    def run(self):
        print("run run run")
        print("self.__priv_num =" , self.__priv_num)
        self.__p_fun()
        self.num_x += 20


    def fun_recursion(self , num):
        print(num)
        if(num == 0):
            return "end"
        else:
            return self.fun_recursion(num - 1)


    # def get_priv_num(self):
    #     return self.__priv_num


    def __p_fun(self):
        print("hello i private")
    

    # def __del__(self):
    #     print("i delete")
        
    

        



dog_1 = Dogs("fidy")
# print(dog_1)
# print(type(dog_1))


# dog_2 = Dogs("gosha")



# print("dog_1.num_x =" , dog_1.num_x)
# dog_1.num_x = 888
# print("dog_1.num_x =" ,dog_1.num_x)
# print("dog_2.num_x =" ,dog_2.num_x)
# print("Dogs().num_x =" ,Dogs("sharik").num_x)



# print(dog_1.name)



# print(type(dog_1.fun))
# dog_1.fun()



# print(dog_1.num_x)
# dog_1.run()
# dog_1.run()
# dog_1.run()
# dog_1.run()
# dog_1.run()
# print(dog_1.num_x)



# print(dog_1.num_x)
# dog_1.fun()
# print(dog_1.num_x)



# dog_1.fun_recursion(9)



# dog_1.run()

# print(dog_1.__priv_num)
# dog_1.__priv_num = 7
# print(dog_1.__priv_num)
# dog_1.run()


# print(dog_1.get_priv_num())



# dog_1.run()
# dog_1.__p_fun()



del dog_1

