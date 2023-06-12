def operation():
    a=int(input('Введите первое значение '))
    b=int(input('Введите второе значение '))
    operator=input('Выберите действие: (+ - * /) ')
    c=0
    file = open("file.txt", "w+", encoding="UTF-8")
    if operator =='+':
        c=a+b
        file.write(str(c))
    elif operator =='-':
        c=a-b
        file.write(str(c))
    elif operator =='*':
        c=a*b
        file.write(str(c))
    elif operator =='/':
        c=a/b
        file.write(str(c))
    else:
        print('Неправильно введено действие')
    
    file.close()

i = 1

while i <= 10:
    print(i)
    i += 1
else:
    print('Цикл окончен, i =', i)