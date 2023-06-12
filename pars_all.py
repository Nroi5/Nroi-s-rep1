from tkinter import *
import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4
import lxml # pip install lxml
from datetime import datetime


root = Tk()

root.title("parse")
root.geometry("500x500+500+0")


#создаю ссылку на текущую дату
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()#получаю дату
today = today.strftime("%d/%m/%Y")#указываю дату в определенном формате

#делаю запрос
payload = {"date_req":today}#доп параметры

r = requests.get(url,params = payload )

xml = BeautifulSoup(r.content,"xml")#pip install lxml

def get_all():
    return xml.find_all("Valute")# Получаю все кусочки

#фукнция для получения курса
def getCourse(id):
    return xml.find("Valute",{"ID":id}).Value.text 

# print(getCourse("R01235"))

img = PhotoImage(file = "logo.png")#записал картинку
logo = Label(root, image = img)#создал надпись с картинкой
logo.place(x = 0, y = 0)# разместил

lab = Label(root, text = "Курс валют", fg = "black", font = "Arial 22")
lab.place(y=25, x=150)

date_lab=Label(root, text=f"Курс на {today.replace('/','.')}", font = "Arial 18")
date_lab.place(x=90, y=150)


all_course= get_all()
list_lable=[] #список надписей
for i in range(len(all_course)):
    curse=all_course[i].Name.text + ' '+ all_course[i].Value.text
    list_lable.append(
        Label(root, text = curse, font = "Arial 10")
    )
    list_lable[i].pack()




root.mainloop()