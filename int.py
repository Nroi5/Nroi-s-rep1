# class A:
#     def voice(self):
#         print()
# #полиморфный класс
# class B(A):
#     def voice(self):
#         print("b")

# class C(A):
#     def voice(self):
#         print("c")


# b = B()
# c = C()

# b.voice()
# c.voice()


# x = "hello " + "world"

# y = 1 + 2 +3

# print(x)
# print(y)

# str
# int



#все состоит из обьект

# print(id(1), type(1))
# print(id(id), type(id))
# print(id(type), type(type))




# class A:
#     #реализация класса
#     def public(self):
#         print("public")

#     def _private(self):
#         print("_private")
# #не хотим использовать этот метод в реализации экземпляра класса
# #название для экз класса представляется в виде a._A__protect()
#     def __protect(self):  
#         print("__protect")

#     def all_methods(self):
#         self.public()
#         self._private()
#         self.__protect()

# #реализация экземпляра класса
# a = A()
# # a.public()          # могу использовать в классе и экземпляре
# # a._private()        # могу использовать в классе и экземпляре , но в экземепляре не стоит 
# # a.__protect() #получу ошибку
# # a._A__protect() # не получу ошибку

# a.all_methods()






# class People:
#     def __init__(self) -> None:
#         self.x = 1
#         self._y = 2
#         self.__z = 3
#     def eat(self):
#         self._eat1()
#         self._eat2()
#         self._eat3()
#         self._eat4()

#         print("человек покушал")

#     def _eat1(self):
#         print("человек взял еду")

#     def _eat2(self):
#         print("человек положил в рот еду")

#     def _eat3(self):
#         print("человек жует еду")

#     def _eat4(self):
#         print("человек проглотил еду")

# people1 = People()
# people1.eat()

# print(people1.x,people1._y, people1._People__z)




#для использования только одного экземпляра класса
# class Singleton(object):
    #создает обьект
    #cls - класс
#     def __new__(cls) :
#         # print(cls)
#         # print(super().__new__(cls))


#         #если у класса нету атрибута instance
#         if not hasattr(cls,"instance"):
#         #хранится ссылка на новый обьект
#             cls.instance =  super().__new__(cls)
#         return cls.instance
    
#     #потом вызывыается инициализатор
#     def __init__(self) -> None:
#         self.x = 1 # a.x = 3
#         print("выполнился инициализатор")


# #при создании обьекта "a"  создаю в классе атрибут instance
# #при создании последующих обьектов смотрю, что у класса Singleton есть уже атрибут instance
# #поэтому возвращаю не новый обьект, а именно первый (тоесть ссылка на "a")
# a = Singleton()
# b = Singleton()


# print(id(a))
# print(id(b))


# print(a)

# print(a.instance )


# print(a.d)
# print(a.y)

# a.z = 3
# print(a.z)








#15:45 - 15:55






# def decorator(func):
#     def wrapper():
#         print("start func")
#         func()
#         print("end func")
#     return wrapper


# @decorator
# def main():
#     print("func main >>>")

# main= decorator(func=main)
# main()

import time


def time_at(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("время выполнения", end - start)
    return wrapper


@time_at
def main(val):
    return [x for x in range(val) if x%2 ==0]

main(999_999)


















