from tkinter import *
from tkinter import filedialog
import re

# root = Tk()
#
#
# def Hello(event):
#     print( "Yet another hello world")
#
#
# btn = Button(root,                  #родительское окно
#              text="Click me",       #надпись на кнопке
#              width=30,height=5,     #ширина и высота
#              bg="white",fg="black") #цвет фона и надписи
# btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
# btn.pack()                          #расположить кнопку на главном окне
# root.mainloop()




"""def Quit(ev):
    global root
    root.destroy()


def LoadFile(ev):
    fn = filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def SaveFile(ev):
    fn = filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))


root = Tk()

panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Load')
saveBtn = Button(panelFrame, text='Save')
quitBtn = Button(panelFrame, text='Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x=10, y=10, width=40, height=40)
saveBtn.place(x=60, y=10, width=40, height=40)
quitBtn.place(x=110, y=10, width=40, height=40)

root.mainloop()"""

from datetime import datetime, timedelta, date
from tkinter import *
from tkinter.ttk import Notebook, Frame, Combobox, Radiobutton
import urllib.request
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates


# 4 - Valute, 3 - country, 2 - Nominal
def parsing(date):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if child.nodeName == "Name":
                countries.append(child.childNodes[0].nodeValue)
            if child.nodeName == "Value":
                valutues.append(child.childNodes[0].nodeValue)
    return countries,valutues
def kurs(country):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if child.nodeName == country:
                countries.append(child.childNodes[0].nodeValue)
            if child.nodeName == "Value":
                valutues.append(child.childNodes[0].nodeValue)

def convert():
    x = country_1.get()
    y = country_2.get()
    z = money.get()
    x_index = countries.index(x)
    x1 = valutues[x_index]
    y_index = countries.index(y)
    y1 = valutues[y_index]
    x1 = x1.replace(',','.')
    y1 = y1.replace(',', '.')
    x = float(x1)
    y = float(y1)
    z = float(z)
    res = str(float((x*z)/y))
    result.configure(text = res)



window = Tk()
window.title("Конвертер валют")
window.minsize(width=500, height=200)
window.maxsize(width=1600, height=1000)
tab_control = Notebook(window)
calc = Frame(tab_control)
tab_control.add(calc, text="Калькулятор валют")

countries = []
valutues = []
countries = parsing(datetime.today())[0]
country_1 = Combobox(calc)
country_1.grid(row=0, column=0, padx=10, pady=10, ipadx=25)
country_1['values'] = countries
country_2 = Combobox(calc)
country_2.grid(row=1, column=0, padx=10, pady=10, ipadx=25)
country_2['values'] = countries
money = Entry(calc)
money.grid(row=0, column=1, pady=10, padx=10)
result = Label(calc, text="")
result.grid(row=1, column=1, pady=10, padx=10)
convert = Button(calc, text = "Конвертировать",command = convert)
convert.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 15)

grafic = Frame(tab_control)
tab_control.add(grafic, text = "Динамика курса")
set1 = Label(grafic, text = "Валюта")
set1.grid(row = 0, column = 0, ipadx = 25)
set2 = Label(grafic, text = "Период")
set2.grid(row = 0, column = 1, ipadx = 25)
set3 = Label(grafic, text = "Выбор периода")
set3.grid(row = 0, column = 2, ipadx = 25)
country_3 = Combobox(grafic)
country_3.grid(row=1, column=0, padx=10, pady=10, ipadx=25)
country_3['values'] = countries
period1 = Radiobutton(grafic, text = 'Неделя', value = 1)
period1.grid(row = 1, column = 1)
period2 = Radiobutton(grafic, text = 'Месяц', value = 2)
period2.grid(row = 2, column = 1)
period3 = Radiobutton(grafic, text = 'Квартал', value = 3)
period3.grid(row = 3, column = 1, pady = 10)
period4 = Radiobutton(grafic, text = 'Год', value = 4)
period4.grid(row = 4, column = 1)
ch_period = Combobox(grafic)
ch_period.grid(row=1, column=2, padx=10, pady=10, ipadx=25)



tab_control.pack(expand=True, fill=BOTH, side="top")
window.mainloop()