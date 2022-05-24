"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Student. Новые поля: класс, дневник
    (словарь словарей вида предмет: {дата : отметка}). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления отметки в дневник, получения всех отметок по предмету,
    форматированной печати всего дневника. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, класс).
Создать производный от Person класс Teacher. Новые поля: номер кабинета, преподаваемые
    предметы (словарь вида класс: список предметов). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения кабинета, добавления и удаления предмета. Переопределить метод преобразования
    в строку для печати основной информации (ФИ, возраст, номер кабинета, предметы).
Создать класс Class. Поля: номер rкласса, список класса (список экземпляров класса Student), классный руководитель
    (экземпляр класса Teacher). Определить конструктор. Переопределить метод преобразования в строку для печати
    всей информации о классе (с использованием переопределения в классах Teacher и Student). Переопределить
    методы получения количества учеников функцией len, получения ученика/учителя по индексу, изменения
    по индексу, удаления по индексу (0 индекс - учитель, начиная с 1 - ученики). Переопределить
    операции + и - для добавления или удаления ученика из группы. Добавить функцию создания txt-файла и записи
    всей информации в него (в том числе дневников учеников).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""
students = []
teachers = []
classes = []

def info():
    print("Введите имя: ")
    name = input()
    print("Введите фамилию: ")
    surname = input()
    print("Введите возраст: ")
    age = int(input())
    print("Введите класс: ")
    clas = int(input())
    return name, surname, age, clas

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, name, surname, age, clas):
        Person.__init__(self, name, surname, age)
        self.clas = clas
        self.journal = {}

    def __str__(self):
        s = "Clas: {} \n{} {}, age: {}".format(self.clas, self.surname, self.name, self.age)
        return s

    def addmark(self,subject, date, mark):
        if subject in self.journal.keys():
            self.journal[subject].append({date:mark})
        else:
            self.journal[subject] = []
            self.journal[subject].append({date: mark})
        print("Вы успешно добавили запись в дневник! ")

    def getmarks(self, subject):
        for x in self.journal:
            if x == subject:
                print(x, ":", self.journal[x])

    def get_journal(self):
        print("Журнал ученика: ", self.surname, self.name)
        for x in self.journal.keys():
            s = f"{x}: {self.journal[x]}\n"
            s = str(s)
            s = s.replace('{','Дата: ')
            s = s.replace('}','')
            s = s.replace('[','')
            s = s.replace(']','')
            s = s.replace("':", ' / Отметка:')
            s = s.replace("'",'')
            print(s)


def Teacher(Person):
    def __init__(self, name, surname, age, clas, subjects):
        Person.__init__(self, name, surname, age)
        self.clas = clas
        self.subjects = {}

    def addsub(self):
        print("Список номер класса: ")
        num = int(input())
        for x in self.subjects:
                print(x, ":", self.subjects[x])
        print("Введите название предмета, который хотите добавить:")
        new_sub = input()
        if num in self.subjects.keys():
            self.subjects[num].append({num:new_sub})
        else:
            self.journal[num] = []
            self.journal[num].append({num: new_sub})

    def change_clas(self):
        print("Классы:")
        for x in self.subjects:
            print(x, ":", self.subjects[x])
        print("Введите номер кабинета, который хотите поменять: ")
        old_clas=int(input())
        print("Введите новый номер кабинета: ")
        new_clas = int(input())
        for x in self.subjects:
            if x==old_clas:
                self.subjects=new_clas
        print("Вы изменили номер кабинета!")
        for x in self.subjects:
            print(x)

    def del_sub(self):
        print("Предметы, преподаваемые в классе:")
        for x in self.subjects.keys():
            s = f"{x}: {self.subjects[x]}\n"
            s = str(s)
            s = s.replace('{', '')
            s = s.replace('}', '')
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace("'", '')
            print(s)
        print("Введите название предмета, который хотите удалить:")
        sub = input()
        for x in self.subjects:
            if x == sub:
                print(x, ":", self.journal[x])

def student():
    inf = info()
    stdnt = Student(inf[0], inf[1], inf[2], inf[3])
    students.append(stdnt.__str__())
    while True:
        print("Функции, доступные Вам для работе с учеником:",
              "1 - Добавить отметку",
              "2 - Вывести все отметки по определенному предмету",
              "3 - Форматированная печать всего дневника",
              "Введите ноль, чтобы закончить работу программы. ", sep="\n")
        menu1 = int(input())
        if menu1 == 1:
            print("Введите название предмета: ")
            subject = input()
            print("Введите дату получения отметки: ")
            date = input()
            print("Введите отметку: ")
            mark = int(input())
            stdnt.addmark(subject, date, mark)
            students[len(students)-1] = stdnt.__str__()
        elif menu1 == 2:
            print("Введите название предмета: ")
            subj = input()
            stdnt.getmarks(subj)
        elif menu1 == 3:
            stdnt.get_journal()
        elif menu1 == 0:
           break

def teacher():
    inf = info()
    teachere = Teacher(inf[0], inf[1], inf[2], inf[3])
    teachers.append(teachere.__str__())

    
def main():
    students_counter = len(students)
    while True:
        print("Функции, доступные Вам:",
              "1 - Добавить ученика",
              "2 - Добавить учителя",
              "3 - Добавить класс",
              "Введите ноль, чтобы закончить работу программы. ", sep="\n")
        menu = int(input())
        if menu == 1:
            student()

        elif menu == 2:
            teacher()

        #elif menu == 3:

        elif menu == 0:
            break

if __name__=="__main__":
    main()