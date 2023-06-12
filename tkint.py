from tkinter import *
window=Tk()
window.title('Вопросы')
window.geometry('700x500')

facts=[
    { 'text' : 'abeme?', 'right' : 1 },
    { 'text' : 'bbeme?', 'right' : 0 },
    { 'text' : 'obeme?', 'right' : 1 },
    { 'text' : 'cbeme?', 'right' : 0 }
]
point=0
ind=0

def check():
    global point, ind
    answer=var.get()
    if answer==facts[ind]['right']:
        point+=1
    
    if ind < len(facts)-1:
        ind+=1
        fact['text'] = facts[ind]['text']
    else:
        point_label=Label(text='Вы набрали: ' + str(point), font=('Arial', 18), bg='blue2', fg='red')
        point_label.place(x=200, y=300)




but=Button(text='Ответить', font=('Arial', 15), bg='blue2', fg='red', command=check)
but.place(x=10, y=160)

fact=Message(text=facts[ind]['text'], font=('Arial', 11), bg='SeaGreen1', fg='dark violet', width=100)
fact.place(x=10, y=75)
fact.configure(justify=CENTER)

Label_title=Label(text = 'Тестирование по Марвел', font=('Arial', 24), bg='grey', fg='red')
Label_title.place(x=0, y=0, width=700, height=50)

var=IntVar()
true=Radiobutton(text='Правда', variable=var, value=1)
true.place(x= 10, y= 100)

false=Radiobutton(text='Ложь', variable=var, value=0)
false.place(x= 10, y= 120)



window.mainloop()





















