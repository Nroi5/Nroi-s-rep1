# Hastebin
# # # def func(a, b):
# # #     return a ** b


# # # x = func(10,3)
# # # print(x)

# # # # LAMBDA - анонимная однострочная функция
# # # func_2 = lambda a, b : a ** b

# # # x = func_2(10) 
# # # print(x)


# # # while
# # x = [1,2,3,4,5,6,7,8,9]
# # # функция для фильтра, если она возвращает True то мы записываем этот обьеки
# # def filt_1(item):
# #     if item < 5:
# #         return True
    
# #     #   return item < 5



# # new_x_3 = []
# # #3
# # for i in x:
# #     if i < 5:
# #         new_x_3.append(i)



# # #filter - класс для фильтрации итерируемой коллекции
# # #1
# # new_x = filter(filt_1, x)

# # #2
# # new_x_2 = filter(lambda item : item < 5 , x)

# # print(new_x)


# # for i in new_x:
# #     print(i)

# # new_x = list(new_x) # filter object -> list
# # print(new_x)


# ########### map - класс который вызывает функцию и передает туда элемент последовательности
# str_list = ['1','2','3','4','5']

# new_str_list_2 = []

# for i in str_list:
#     new_str_list_2.append(int(i))


# new_str_list_1 = list(
#                         map(int, str_list)
#                     )

# print(new_str_list_1)




# y = [1,2,3,4,5]

# def u(item_list):
#     new_list = []
#     for i in item_list:
#         new_list.append(i ** i)
#     return new_list


# new_y = list(map( lambda item : item ** item, y))
# print(new_y)
from pprint import pprint # функция для красивого вывода п
# goods = [ 
#     {
#         'name': 'Iphone 14'
#         'brand': 'Apple',
#         'price': 1200,
#     },
#     {
#         'name': 'REALME C25s',
#         'brand': 'REALME',
#         'price': 400,
#     },
#     {
#         'name': 'Samsung Galaxy A53',
#         'brand': 'Samsung',
#         'price': 500
#     }
# ]
# # sorted - сортирует коллекцию по ключу
# pprint(goods)
# print("-" * 40)
# pprint(
#     sorted(goods, key = lambda item : item['price'])
# )



# name = ['павел', 'olga', 'max']

# for ind, value in enumerate(name):
#     print(ind, value)

#zip- класс для объединения объектов нескольких последовательностей в кортежи'
a=[1,2,3]
b=['A','B','C']
a_b = list(zip(a,b))
pprint(a_b)




