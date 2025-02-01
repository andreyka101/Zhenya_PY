class Animals():
    """fywfdywyfdfyw wdigwduggd"""
    num_x = 3
    def __init__(self , name_loc):
        self.name = name_loc
        print("hi" , self.name)
        print(self.num_x)

    def run(self):
        """this run"""
        print("run run run")
        self.num_x += 20


# num = 9
# '''122232fff'''


# print(num)


# ani = Animals("pip")

# ani.run()




class Cats(Animals):
    def __init__(self, name_cat):
        print("---ok---")

        super().__init__(name_cat)

        print("---end ok---")
    

    def run(self,step):
        print(step)
        super().run()
    

# red_cat = Cats("redCat")
# print(red_cat.num_x)
# red_cat.run(75757)
# print(red_cat.num_x)








class Dogs():
    def __init__(self , name_loc):
        print("i dog")
        self.name = name_loc
    def fun(self):
        print("hello fun")
        print("name dog =" , self.name)
    




class All_animals():
    def __init__(self , name):
        self.dogs = Dogs(name)
        self.cats = Cats(name)
    

dog_1 = All_animals("werty")
dog_1.dogs.fun()
print(dog_1.cats.num_x)
print(dog_1.dogs)

