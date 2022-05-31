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

from datetime import *
from tkinter import *
from tkinter.ttk import Notebook, Frame, Combobox, Radiobutton
import urllib.request
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates


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

def kurs(country,date):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if child.nodeName == country:
                countryy = child.childNodes[0].nodeValue
            if child.nodeName == "Value":
                value = child.childNodes[0].nodeValue
                break
        return value

def graf():
    periodd = ch_period.get()
    country = country_3.get()
    if per.get()==1:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master = grafic)
        raz = timedelta(days = 1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd=re.split(' - ',periodd)
        temp1 = datetime.strptime(periodd[1],"%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0],"%d/%m/%Y")
        while(temp1!=temp2+raz):
            k = kurs(country,temp1)
            k = k.replace(',','.')
            k = float(k)
            x.append(datetime.strftime(temp1, "%d%m"))
            y1 = round(k)
            y.append(y1)
            temp1+=raz
        fig.clear()
        matplotlib.pyplot.plot(x,y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row = 5,column = 5)
    if per.get() == 2:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=grafic)
        raz = timedelta(days=1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd = re.split(' - ', periodd)
        temp1 = datetime.strptime(periodd[1], "%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0], "%d/%m/%Y")
        while (temp1 != temp2 + raz):
            k = kurs(country, temp1)
            k = k.replace(',', '.')
            k = float(k)
            x.append(datetime.strftime(temp1, "%d.%m"))
            y1 = round(k)
            y.append(y1)
            temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)
    if per.get() == 3:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=grafic)
        raz = timedelta(days=6.5)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd = re.split(' - ', periodd)
        temp1 = datetime.strptime(periodd[1], "%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0], "%d/%m/%Y")
        while (temp1 < temp2):
            k = kurs(country, temp1)
            if k!=None:
                k = k.replace(',', '.')
                k = float(k)
                x.append(datetime.strftime(temp1, "%d.%m"))
                y1 = round(k)
                y.append(y1)
                temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)
    if per.get() == 4:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(12, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=grafic)
        raz = timedelta(weeks=4.4)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd = re.split(' - ', periodd)
        temp1 = datetime.strptime(periodd[1], "%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0], "%d/%m/%Y")
        while (temp1 < temp2 + raz):
            k = kurs(country, temp1)
            k = k.replace(',', '.')
            k = float(k)
            x.append(datetime.strftime(temp1, "%B.%Y"))
            y1 = round(k)
            y.append(y1)
            temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)



def period():
    if per.get()==1:
        periodscheck=[]
        now = date.today()
        temp = now
        delta = timedelta(weeks = 1)
        for i in range(4):
            string = ''
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string+=datetime.strftime(temp,"%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck
    if per.get()==2:
        periodscheck = []
        now = date.today()
        temp = now
        delta = timedelta(weeks = 4.4)
        for i in range(4):
            string = ''
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck
    if per.get()==3:
        periodscheck = []
        now = date.today()
        temp = now
        for i in range(4):
            ost = int(datetime.strftime(temp, "%m")) % 3
            delta = timedelta(weeks=ost * 4.4)
            string = ''
            temp = temp - delta
            string = temp.strftime("%d/%m/%Y") + ' - '
            delta = timedelta(weeks=13.2)
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck
    if per.get()==4:
        periodscheck = []
        now = date.today()
        temp = now
        delta = timedelta(weeks = 52)
        for i in range(4):
            string = ''
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck








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
per = IntVar()
periodscheck=[]
period1 = Radiobutton(grafic, text = 'Неделя', value = 1,variable= per,command=period)
period1.grid(row = 1, column = 1)
period2 = Radiobutton(grafic, text = 'Месяц', value = 2,variable= per, command=period)
period2.grid(row = 2, column = 1)
period3 = Radiobutton(grafic, text = 'Квартал', value = 3,variable= per,command=period)
period3.grid(row = 3, column = 1, pady = 10)
period4 = Radiobutton(grafic, text = 'Год', value = 4,variable= per, command=period)
period4.grid(row = 4, column = 1)
ch_period = Combobox(grafic)
ch_period.grid(row=1, column=2, padx=10, pady=10, ipadx=25,)
draw = Button(grafic, text = "Нарисовать график!",command = graf)
draw.grid(row = 4, column = 0, padx = 10, pady = 10, ipadx = 15)



tab_control.pack(expand=True, fill=BOTH, side="top")
window.mainloop()