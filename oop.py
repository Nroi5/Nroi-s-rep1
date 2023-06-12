# from tkinter import *
# window=Tk()
# window.geometry("800x600")
# canvas=Canvas(window, width=800, height=600)
# canvas.pack() #расположение на весь экран  

# class House:
#     def __init__(self, color1, color2):
#         self.color_triangle=color1
#         self.color_sqare=color2
#         self.first_height=170
#         self.first_weight=130

        
#     def build_house(self, x, y):
#         h = self.first_height
#         w = self.first_weight



# house1=House()
# house1.build_house(389, 400)




# window.mainloop()







# # canvas.create_rectangle(10 , 10, 110, 110, fill='green', outline='red', width=10)

# canvas.create_polygon(10 , 180, 110, 190, 10, 10, fill='green', outline='red', width=10)


# canvas.create_rectangle(30 , 30, , 110, fill='green', outline='red', width=10)




# 

# атрибуты - существительные: цвет дома материал стен размеры дома

#Класс - пользовательский тип данных в котором описываются атрибуты, свойства и методы
# class Car:

#     #конструктор (инициализатор) вызывается сам при создании экземпляра-класса для иницилизации атрибутов
#     #
#     #
#     #
#     #
#     def __init__(self, name, speed) -> None:
#         self.name=name
#         pass
#     def drive(self):
#         print('Поехала')

# # экземпляр класса (объект)
# bmw=Car()
# bmw.drive() #вызов метота экземпляра класса

# audi=Car()
# audi.drive()


class Employee():
    def __init__(self, name,salary, on_vacation):
        self.name=name
        self.salary=salary
        self.on_vacation=on_vacation
        
    def get_info(self):
        print(f"{self.name} имеет зарплату {self.salary} тыс. рублей в месяц. Статус нахождения в отпуске: {self.on_vacation}.")


employee_list=[
    Employee('Max', 100, True),
    Employee('Oleg', 100, False),
    Employee('Artem', 100, True),
    Employee('Vitali', 100, False)
]

for employee in employee_list:
    employee.get_info()
    print("-" * 40)



