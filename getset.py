class People:
    def __init__(self, name, year):
        self.__name = name #public
        self.__year = year #private (можем использовать и в классе и в объекте,
        #но подразумеваем что только в классе)

        #@property - getter
    @property
    def name(self):
        return self.__name
    
    @property
    def year(self):
        return f"{self.__year} года рождения"
    
    @name.setter
    def name(self, name):
        self.__name = name

    @year.setter
    def year(self, year):
        if year <= 1940 or year >= 2024:
            raise Exception("одна ошибка и ты ошибся")
        self.__year = year

    @name.deleter
    def name(self):
        # self.__name = None
        del self.__name


    @year.deleter
    def year(self):
        # self.__year = None
        del self.__year
# реализация объекта
people1=People("Максим", 2005, )

# people1.name=None
# people1.year=None
print(people1.name)
print(people1.year)

del people1.name
del people1.year
print(people1.name)
print(people1.year)





# class Человек:
#     def кушать(self):
#         self.жевать()
#         self.проглотить()
#         print("я покушал")
    
#     def жевать(self):
#         print("я жую")

#     def _проглотить(self):
#         print("я проглотил")

# чел = Человек()
# чел._проглотить()

class Not_list(list):
    def delete_last_el():
        # self.pop()
        del self[-1]

