# import requests
# from bs4 import BeautifulSoup
# import openpyxl
# page = requests.get("https://www.mirea.ru/schedule/")
# soup = BeautifulSoup(page.text, "html.parser")
# result = soup.find("div", {"class":"rasspisanie"}).\
#  find(string = "Институт информационных технологий").\
#  find_parent("div").\
#  find_parent("div").\
#  findAll()  # получить ссылки
#

# f = open("file.xlsx", "wb") # открываем файл для записи, в режиме wb
# resp = requests.get("https://webservices.mirea.ru/upload/iblock/53c/2y9d6nveeqiwqazn8pr4zruasdic2x0d/ИИТ_3 курс_21-22_весна_очка.xlsx")
# f.write(resp.content)
# book = openpyxl.load_workbook("file") # открытие файла
# sheet = book.active # активный лист
# num_cols = sheet.max_column # количество столбцов
def wind_des(speed):
    speed=int(speed)
    if (speed>0 and speed<0.2):
        return 'Штиль'
    elif (speed>0,3 and speed<1.5):
        return 'Тихий'
    elif (speed>1.6 and speed<3.3):
        return 'Лёгкий'
    elif (speed>3.4 and speed<5.4):
        return "Слабый"
    elif (speed>5.5 and speed<7.9):
        return "Умеренный"
    elif (speed>8.0 and speed<10.7):
        return "Свежий"
    elif (speed>10.8 and speed<13.8):
        return "Сильный"
    elif (speed>13.9 and speed<17.1):
        return "Крепкий"
    elif (speed>17.2 and speed<20.7):
        return "Очень крепкий"
    elif (speed>20.8 and speed<24.4):
        return "Шторм"
    elif (speed>24.5 and speed<28.4):
        return "Сильный шторм"
    elif (speed>28.5 and speed<32.6):
        return "Жестокий шторм"
    else:
        return "Ураган :)"
def wind_dir(grad):
    grad = int(grad)
    if ((grad)>=90 and grad <180):
        return "Восток"
    elif ((grad)>=180 and grad <270):
        return "ЮГ"
    elif ((grad)>=270 and grad <348,75):
        return "Запад"
    else:
        return "Север"
import requests
from re import *
s_city = "Moscow,RU"
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/weather",
#                        params={'q': 'Moscow,RU', 'units': 'metric', 'lang': 'ru', 'APPID':'cabb0d1a47e3748838dbe5345d78caa9'})
#     # res = requests.get('http://api.openweathermap.org/data/2.5/find?q=Moscow,RU&type=like&APPID=cabb0d1a47e3748838dbe5345d78caa9')
#     data = res.json()
#     print(data)
#     print("Описание погоды:", data['weather'][0]['description'])
#     print("Температура:", data['main']['temp'],"C")
#     print("Минимальная температура:", data['main']['temp_min'],"C")
#     print("Максимальная температура:", data['main']['temp_max'],"C")
#     print("Давление: ", data['main']['pressure'])
#     print("Влажность: ", data['main']['humidity'])
#     print("Ветер: ",wind_des(data['wind']['speed']))
#     print("Направление ветра: ", wind_dir(data['wind']['deg']))
# except Exception as e:
#     print("Exception (weather):", e)
#     pass
"""try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': 524901, 'units': 'metric', 'lang': 'ru', 'APPID': 'cabb0d1a47e3748838dbe5345d78caa9'})
    data = res.json()
    for i in data['list']:
        if (search(r'\d[8621]{1}:',i['dt_txt'])):
            print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
except Exception as e:
    print("Exception (forecast):", e)
    pass"""