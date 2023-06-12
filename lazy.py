# #Строгие вычесления - те которые происходят непосредственно в момент инициализации объекста или вызова функции/метода 
# # происходят только непосредственно в тот момент когда они нам понадобились
# #yield почти то же самое как retutn но после этого мы можем продолжать ее

# # my_list2 = (x for x in range(1,100))
# # print(my_list2)

# # print(next(my_list2))
# # print(my_list2)
# # print(next(my_list2))
# # print(my_list2)
# # print(next(my_list2))
# # print(my_list2)
# # print(next(my_list2))
# # print(my_list2)
# # print(next(my_list2))
# # print(my_list2)
# # print(next(my_list2))
# # print(my_list2)

# def lazy_func():
#     for i in range(1,11):
#         print("Перед yield i = ",i)
#         yield i
#         print("После yield i = ",i) 



# for item in lazy_func():
#     print(item)

# f = open("text.txt", "w", encoding="UTF=8")
# f.write("hello world")
# f.close

# with open("text.txt", "w", encoding="UTF=8") as f:# автоматом закрывает файл
#     f.write("Hello worldo")
# import contextlib

# @contextlib.contextmanager
# def
my_list2 = (x **2 for x in range(1,1000001))
print(my_list2)

def gen_mill():
    for i in range(1,1000000):
        yield i**2
