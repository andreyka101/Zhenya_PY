

class Dogs():
    # область self:
    num_x = 3
    # init - вызывается при создании класса
    # self - это хранилище переменных и методов
    def __init__(self , name_loc):
        # print("hi")

        # локальная переменной
        # num_loc = 8
        # print("num_loc =" , num_loc)

        # print("self.num_x =" , self.num_x)
        self.num_x = 100
        # print("self.num_x =" , self.num_x)
        
        # создание переменной
        self.str_text = "wdvdvvdg"
        # использование переменной
        # print("self.str_text =" , self.str_text)

        # print(name_loc)
        self.name = name_loc

        # если написать впереди (__) тогда переменная станет приватной
        self.__priv_num = 1
        self.__priv_num +=10

    # создание метода
    def fun(self):
        print("hello fun")
        print("name dog =" , self.name)
        self.run()

    # метод изменяет переменную
    def run(self):
        print("run run run")
        print("self.__priv_num =" , self.__priv_num)
        self.__p_fun()
        self.num_x += 20

    # рекурсия
    def fun_recursion(self , num):
        print(num)
        if(num == 0):
            return "end"
        else:
            return self.fun_recursion(num - 1)

    # метод возвращает приватную переменная
    def get_priv_num(self):
        return self.__priv_num

    # если написать впереди (__) метод станет приватный
    def __p_fun(self):
        print("hello i private")
    
    # del - вызывается при удалении объекта
    # def __del__(self):
    #     print("i delete")
        
    

        

# создание объекта (вызов класса)
dog_1 = Dogs("fidy")
# print(dog_1)
# print(type(dog_1))


# два разных объекта
# dog_2 = Dogs("gosha")



# получаем переменную класса (объекта):
# у каждого объекта свои переменные
# print("dog_1.num_x =" , dog_1.num_x)
# dog_1.num_x = 888
# print("dog_1.num_x =" ,dog_1.num_x)
# print("dog_2.num_x =" ,dog_2.num_x)
# print("Dogs().num_x =" ,Dogs("sharik").num_x)



# получаем имя собаки
# print(dog_1.name)



# вызываем метод
# dog_1.fun()
# метод = функция
# print(type(dog_1.fun))



# метод меняет переменную num_x
# print(dog_1.num_x)
# dog_1.run()
# dog_1.run()
# dog_1.run()
# dog_1.run()
# dog_1.run()
# print(dog_1.num_x)



# метод вызывает другой метод run
# print(dog_1.num_x)
# dog_1.fun()
# print(dog_1.num_x)



# рекурсия
# dog_1.fun_recursion(9)



# приватная переменная
# print(dog_1.__priv_num)
# dog_1.__priv_num = 7
# print(dog_1.__priv_num)
# dog_1.run()


# получаем приватную переменную
# print(dog_1.get_priv_num())



# приватный метод
# dog_1.run()
# dog_1.__p_fun()



# удалении объекта
del dog_1






# дз

# номер 1
# создайте класс с тремя переменными 
# у класса есть метод который возвращает все переменные в списке

# номер 2
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# номер 3
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)


