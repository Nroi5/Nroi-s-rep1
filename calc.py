a=0
b=0
c=0
print("Добро пожаловать в калькулятор.")
operator=input('Выберите действие: (+ - * / D) ')
def numbers():
    global a, b
    a=int(input('Введите первое целое число '))
    b=int(input('Введите второе целое число '))
def sum():
    numbers()
    print('Ответ= ', sum(int(a,b)))
  

def min():
    numbers()
    print('Ответ= ', min(int(a,b)))


def mult():
    numbers()
    print('Ответ= ', mult(int(a,b)))


def div():
    numbers()
    print('Ответ= ', div(int(a,b)))

def D():
    global c
    numbers()
    c=int(input('Введите третье целое число '))
    d=(b**2)-(4*a*c)
    print(f"Дискриминант по заданым числам равен: {d}.")
    if d < 0:
        print('Дискриминант отрицательный - корней нет')
    else:
        print(f"Корень из этого числа: {d ** 0.5}")

if operator=='+':
    sum()

elif operator=='-':
    min()

elif operator=='*':
    mult()

elif operator=='/':
    div(a,b)

elif operator == 'D':
    D()

else:
    print('Неправильно введено действие')