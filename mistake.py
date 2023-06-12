import time 

# # f = open("test.txt",'w')
# # f.write("hello")
# # f.close()

# # with open("test.txt",'w') as f:
# #     f.write("hello")
# # #закрытие идет автоматически



# class Timer:

#     def __enter__(self):
#         self.start = time.time()
#         return self.start

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         end = time.time()
#         print("Время выполнения: ", end - self.start)
#         #если exc_type не равна None - значит там исключение
#         if exc_type is not None:
#             #если ошибок нет то параметры равны None
#             print("-" * 40)
#             print("exc_type : ", exc_type)
#             print("-" * 40)   
#             print("exc_value : ", exc_value)
#             print("-" * 40)
#             print("exc_tb : ", exc_tb)
#             print("-" * 40)
#         #если метод exit возвращает true - то пропускаем исключения (try except)
#             return True
# #когда может использоваться:
# # connect и disconnect с чем-нибудь(база данных, сервером)

# with Timer() as t : #__enter__     в t записываю то что отдал в return
#     for i in range(10):
#         print(i) 
#     print(t)
#         # 1/0

# print("Код после исключения")
# #__exit__


# # итерируемый обьект
# my_list = [1,2,3,4,5]

# #итер - обьект для итераций
# my_iter = iter(my_list) #__iter__ получаю итер
# print(my_iter)

# print(next(my_iter))# __next__ - двигает итер
# print(next(my_iter))# __next__ - двигает итер
# print(next(my_iter))# __next__ - двигает итер
# print(next(my_iter))# __next__ - двигает итер
# print(next(my_iter))# __next__ - двигает итер

# print(next(my_iter))# __next__ - двигает итер



# for i in my_list: # i = iter(my_list)
#     print(i)      # next(i)


#сделать класс как range только чтобы он выводил
#рандомные числа
# from random import randint

# class MyIter:
#     def __init__(self, limit) -> None:
#         self.limit = limit
#         self.__reload = limit
#     #вернуть ссылку на обьект (дополнитьна какая-нибудь логика, 
#     # например обновление лимита)
#     def __iter__(self):
#         self.limit = self.__reload #обновляю лимит
#         return self #вернуть ссылку на обьект

#     def __next__(self):#двигаем итер и даем ему значние
#         if self.limit == 0:
#             #raise - вызов исключения
#             raise StopIteration #выходим из for (break) 
        
#         self.limit -= 1
#         return randint(1,101)
    
# test = MyIter(10)
# #limit = 10
# for i in test: #ждет StopIteration и выполнчет break
#     print(i)

# print("-" * 50)
# #limit = 0
# # через iter обновляю limit опять до 10
# for i in test: #ждет StopIteration и выполнчет break
#     print(i)


# for i in range(10):
#     print(i)



# age = 13
# if age < 18:
    # raise IndentationError #сами вызываем исключение
    # raise Exception("Вам нельзя на фильм ужасов")

#2 дз

# from random import randint

# class MyIter:
#     def __init__(self, limit) -> None:
#         self.limit = limit
#         self.__reload = limit
#     #вернуть ссылку на обьект (дополнитьна какая-нибудь логика, 
#     # например обновление лимита)
#     def __iter__(self):
#         self.limit = self.__reload #обновляю лимит
#         return self #вернуть ссылку на обьект

#     def __next__(self):#двигаем итер и даем ему значние
#         # if self.limit == 0:
#         #     #raise - вызов исключения
#         #     raise StopIteration #выходим из for (break) 
        
#         self.limit -= 1
#         return randint(1,101)
    
# test = MyIter(10)
# #limit = 10
# for i in test: #ждет StopIteration и выполнячет break
#     print(i)

# print("-" * 50)
# #limit = 0
# # через iter обновляю limit опять до 10
# for i in test: #ждет StopIteration и выполнчет break
#     print(i)



#1 дз
class MyFile:
    def __init__(self, path, mode, encoding = "UTF-8"):
        self.path = path
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.path,self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
#когда может использоваться:
# connect и disconnect с чем-нибудь(база данных, сервером)

with MyFile("test.py","w") as f : #__enter__     в t записываю то что отдал в return