
# класс родитель
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



# наследуем класс Animals
# в наследуемом классе можно создавать свои переменные и методы
class Cats(Animals):
    def __init__(self, name_cat):
        print("---ok---")

        # вызываем метод Animals
        super().__init__(name_cat)

        print("---end ok---")
    

    def run(self,step):
        print(step)
        
        # вызываем метод Animals
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
    




# класс хранит в себе несколько классов
class All_animals():
    def __init__(self , name):
        self.dogs = Dogs(name)
        self.cats = Cats(name)
    

dog_1 = All_animals("werty")
dog_1.dogs.fun()
print(dog_1.cats.num_x)
print(dog_1.dogs)







# дз

# номер 1
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления дополнителиного числа (3, 4, 5 и тд) (его можно вызвать много раз и подучить много чисел)



# задание 2
# создайте родительский класс , описывающий транспорт
# (модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации о транспорте.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# наследуйте класс автомобили в котором есть ещё одна переменная количество мест

# наследуйте класс вертолеты с дополнительным методом взлет 
