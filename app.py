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

#фукнция для получения курса
def getCourse(id):
    return xml.find("Valute",{"ID":id}).Value.text 

# print(getCourse("R01235"))

img = PhotoImage(file = "logo.png")#записал картинку
logo = Label(root, image = img)#создал надпись с картинкой
logo.place(x = 0, y = 0)# разместил

# lab = Label(root, text = "Курс валют", fg = "black", font = "Arial 22")
# lab.place(y=25, x=150)

# date_lab=Label(root, text=f"Курс на {today.replace('/','.')}", font = "Arial 18")
# date_lab.place(x=90, y=150)

# usd=Label(root, text="Доллар " +getCourse("R01235").replace(',','.'), font = "Arial 16")
# usd.place(x=90, y=190)

# eur=Label(root, text="Евро " +getCourse("R01239").replace(',','.'), font = "Arial 16")
# eur.place(x=90, y=230)

# ent=Entry(root, width=20)
# ent.pack()

# root.mainloop()





a=[i for i in range(0, 250) if (i % 30 == 0 or i % 31 == 0) and i!=0]
print(a)




