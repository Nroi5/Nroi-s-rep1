# class A:
#     def _init_(self, q, w, e, r):
#         self.q=q
#         self.q=w
#         self.q=e
#         self.q=r
#     def one(self):
#         print('class A one')


#     def two(self):
#         print('class A one')




# class B(A):
#     def __init__(self):
#         super().__init__(self, q, w, e, r)
#     def two(self):
#         super().two()
#         A.two(self)
#         print('new method')
    
#     def three(self):
#         print('class B three')



# a=A()
# a.one()
# a.two()

# b=B()
# b.one()
# b.two()
# b.three()






from random import randint

class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health, crit, miss ):
        self.model = model
        self.armor = armor
        self.damage = randint(min_damage, max_damage)
        self.health = health
        self.crit = crit
        self.miss = miss


    def info(self):
        print(f"{self.model} имеет лобовую броню {self.armor}мм при {self.health}ед. здоровья и урон в {self.damage} единиц")

    def shot(self,enemy):
        if randint(1,101) <= self.miss:
            print(f"\n{self.model}:")
            print(f"Командир, мы промахнулись ... ")
            return #выход из функции
        
        if randint(1,101) <= self.crit:
            mul_damage = 1.5
            enemy.health -= (self.damage * mul_damage - self.damage * mul_damage * enemy.armor // 100) 
            print(f"\n{self.model}:")
            print("КРИТ УРОН")
            print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
        else:
            enemy.health -= (self.damage  - self.damage  * enemy.armor // 100) 
            print(f"\n{self.model}:")
            print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")

tank1 = Tank("T-34", armor = 25, min_damage= 50,max_damage= 85, health = 1050, crit = 15, miss = 40)
tank2 = Tank("panzerkampwagen", 30, 35, 55, 1450, 15, 40)

tank1.info()
tank2.info()

while True:
    if tank1.health <= 0 and tank2.health <= 0:
        print("Ничья")
        break #выход из цикла
    elif tank1.health <= 0:
        print("выиграл " , tank2.model)
        break
    elif tank2.health <= 0:
        print("выиграл " , tank1.model)
        break

    tank1.shot( enemy = tank2 )
    tank2.shot( enemy = tank1 )




























