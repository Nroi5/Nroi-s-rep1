# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __add__(self, other):
#         if isinstance(other,int):
#             return self.price + other
#         elif isinstance (other, Item):
#             return self.price + other.price
        
#     def __radd__(self, other):
#         if isinstance(other,int):
#             return self.price + other
    # def __sub__(self,other):
        #  if isinstance(other,int):
        #      return self.price - other
        #  elif isinstance (other, Item):
        #      return self.price - other.price



# item_1 = Item("Хлеб", 2)
# item_2 = Item("Бочка", 1)

# total_price=item_1 + item_2
# total_price2=3 + item_1
# total_price4=item_1 + item_1 + item_2
# # print(total_price)
# # print(total_price2)
# print(total_price4)


# # x="10"
# # if isinstance(x,int):
# #     print("Это число")
# # elif isinstance (x,str):
# #     print("Строка")

#################################алхимия#############################################



from tkinter import *
from random import randint
window = Tk()
window.geometry("600x800")

# subsample метод для уменьшения картинки в х колво раз
# zoom метод для увеличения картинки в х колво раз


class Fire:
    image = PhotoImage(file=r"alch/fire.png").subsample(4,4)
    
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

class Water:
    image = PhotoImage(file=r"alch/water.png").subsample(4,4)

class Wind:
    image = PhotoImage(file=r"alch/wind.png").subsample(4,4)

class Earth:
    image = PhotoImage(file=r"alch/ground.png").subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

class Clay:
    image = PhotoImage(file=r"alch/pottery.png").subsample(4,4)


elements= [Fire(), Water(), Wind(), Earth()]

canvas=Canvas(window, width = 600, height=800)
canvas.pack()

for elem in elements:
    canvas.create_image(randint(50,550), randint(50,550), image = elem.image)



# когда мы создаем картинку на холсте ей присваивается номер начиная с 1
def move(event):
    # print(event)
    # event.x, event.y - координаты мышки 
    # find_overlapping() - метод который возвращает id картинок в заданном прямоугольнике
    image_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)#кортеж 
    # image_id - кортеж 
    print(image_id)
    if len(image_id) == 2:
        element_1 = elements[ image_id[0]  - 1 ] 
        element_2 = elements[ image_id[1]  - 1 ] 

        new_element = element_1 + element_2
        #что появляется новый элемент и его не в списке
        if new_element and new_element not in elements:
            canvas.create_image(event.x, event.y, image = new_element.image)
            elements.append(new_element)

    #coords - двигаю картинку по ее id в направлении мышки
    canvas.coords(image_id, event.x, event.y)

window.bind("<B1-Motion>", move)
window.mainloop()

