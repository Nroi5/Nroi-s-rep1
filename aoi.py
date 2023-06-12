# import requests
# import lxml
# from bs4 import BeautifulSoup
# from datetime import datetime



# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
#                 # today=datetime.today()

#                 # today=today.strftime('%d/%m/%Y')




# def getCounter(id):
#     return xml.find("Valute", {'ID':id}).Value.text


# print(getCounter('R01035'), 'Фунтов стерлингов Соединенного королевства стоит 1 рубль', today )

# def parse(df, mf, yf, dl, ml, yl):
#     for y in range(yf, yl+1):
#         for m in range(mf, 13):
#             for d in range(df, 31):
#                 m1=m
#                 d1=d
#                 if m < 10:
#                     m1=f"0{m}"
#                 if d < 10:
#                     d1=f"0{d}"
#                 today=f"{d1}/{m1}/{y}"

#                 payload= {"date_req":today}

#                 r= requests.get(url, params=payload)

#                 xml=BeautifulSoup(r.content, "xml")
                
#                 return 


import requests#pip install requests
from bs4 import BeautifulSoup#pip install bs4
import lxml #pip install lxml
from datetime import datetime



url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()

today = today.strftime('%d/%m/%Y')

payload = {"date_req":today}

#params - параметр который подставляет данные в ссылку
r = requests.get(url, params = payload )

xml = BeautifulSoup(r.content, "xml")

def getCounter(id):
    return xml.find("Valute", {'ID':id}).Value.text


print(getCounter("R01215") ,'crone')
print(getCounter("R01235") , 'usd')
print(getCounter("R01239") ,'euro')




