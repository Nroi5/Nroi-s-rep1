from tkinter import *
import random


window = Tk()

W = 600
H = 600

window.geometry(f"{W}x{H}")

canvas = Canvas(window, width = W, height = H)
# canvas.pack()
#альтернативный способ
canvas.place(in_ = window,x = 0, y = 0)

bg_img = PhotoImage(file = "bg_2.png" )

class Knight:
    def __init__(self) :
        self.x = 70
        self.y = H//2
        #speed
        self.v = 0

        self.photo = PhotoImage(file ="knight.png")
    

    def up(self,event):
        self.v = -3

    def down(self,event):
        self.v = 3

    def stop(self,event):
        self.v = 0


class Dragon:
    def __init__(self) :
        self.x = 750
        self.y = random.randint(100,500)
        self.v = random.randint(1,3)
        self.photo = PhotoImage(file = "dragon.png")


#создал обьект рыцаря
black_knight = Knight()

#создал обьект дракошек
many_dragon = []
for i in range(3):
    #добаляю дракошку в список
    many_dragon.append(Dragon())






def game():
    canvas.delete("all")
    #задний фон
    canvas.create_image(W//2 , H // 2, image = bg_img)
    #рыцарь
    canvas.create_image(black_knight.x , black_knight.y , image = black_knight.photo)
    #логика движения
    black_knight.y += black_knight.v
    #дракон на данный момент
    cur_dragon = 0
    #индекс дракона которого нужно убрать
    dragon_to_kill = -1

    #прорисовываю дракошек
    for drgn in many_dragon:
        drgn.x -= drgn.v
        canvas.create_image(drgn.x , drgn.y , image = drgn.photo)

        if ((drgn.x - black_knight.x)**2) + ((drgn.y - black_knight.y)**2) <= (96)**2:
            dragon_to_kill = cur_dragon
        #меняю индекс для след дракошки
        cur_dragon += 1


        #если дракон дошел до замка
        if drgn.x <= 0 :
            canvas.delete("all")
            canvas.create_text(W//2, H//2, text = "вы проиграли", font = "Vernada 42", fill = "purple")
            break
    
    #если индекс >= 0 то консулся дракошки
    if dragon_to_kill >= 0:
        del many_dragon[dragon_to_kill]

    #если убили всех дракошек
    if len(many_dragon) == 0:
        canvas.delete("all")
        canvas.create_text(W//2, H//2, text = "вы выиграли", font = "Vernada 42", fill = "purple")
    else:
        #опять вызываю функцию 
        window.after(5,game)

game()
###################################15:45 - 15:55
#привязал кнопки к методам
window.bind("<Key-Up>",black_knight.up)
window.bind("<Key-Down>",black_knight.down)
#когжа не нажимаю
window.bind("<KeyRelease>", black_knight.stop)


window.mainloop()



# class War:
#     def __init__(self) -> None:
#         self.hp  = 100
    

#     def attack(self, enemy):
#         enemy.hp -= 20

# war1 = War()
# war2 = War()

# while True:
#     war1.attack(war2)
#     war2.attack(war1)
#     print(war1.hp ,war2.hp )
