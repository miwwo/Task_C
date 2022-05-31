"""Создать производный от Person класс Student. Новые поля: класс, дневник
    (словарь словарей вида предмет: {дата : отметка}). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления отметки в дневник, получения всех отметок по предмету,
    форматированной печати всего дневника. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, класс)."""

from Person import Person
from log import log
from pprint import pprint
class Student(Person):
    def __init__(self, name, surname, age, clas):
        Person.__init__(self, name, surname, age)
        self.clas = clas
        self.journal = {}
        log("CRE",'',"объект класса Student","__init__")
    def __str__(self):
        s = "{} {}, clas: {}, age: {}".format(self.surname, self.name, self.clas, self.age)
        log("INF", "print", "студент", "__str__")
        return s
    def pr(self, x, journal):
        s = f"{self.journal[x]}\n"
        s = str(s)
        s = s.replace(' {','Дата: ')
        s = s.replace('{', 'Дата: ')
        s = s.replace('}','')
        s = s.replace('[','')
        s = s.replace(']','')
        s = s.replace("':", ' - Отметка:')
        s = s.replace("'",'')
        s = s.replace(',', '\n')
        print(s)

    def prr(self, x, journal):
        s = f" {x}:\n{self.journal[x]}"
        s = str(s)
        s = s.replace(' {','Дата: ')
        s = s.replace('{', 'Дата: ')
        s = s.replace('}','')
        s = s.replace('[','')
        s = s.replace(']','')
        s = s.replace("':", ' - Отметка:')
        s = s.replace("'",'')
        s = s.replace(',', '\n')
        return s

    def add_mark(self, subject, mark, date):
        if subject in self.journal.keys():
            self.journal[subject].append({date: mark})
        else:
            self.journal[subject] = []
            self.journal[subject].append({date: mark})
        log("INF", "add", "отметка в журнал студента", "add_mark")

    def get_marks(self,subject):
        if subject in self.journal:
            print("Оценки по предмету:", subject)
            self.pr(subject, self.journal)
            log("INF", "print", "оценки по предмету", "get_marks")

    def get_journal(self):
        if not self.journal:
            print('None')
        else:
            print("Журнал:\n")
            for x in self.journal:
                i = self.prr(x, self.journal)
                print(i)
            print('\n')
            log("INF", "print", "журнал", "get_journal")

"""def main():
    student1 = Student('Иван', "Иванов", 14, 9)
    print(student1)
    student1.add_mark('ОБЖ', 5, '12/01')
    student1.add_mark('ОБЖ', 3, '28/5')
    student1.add_mark('Матеша', 2, '1/1')
    student1.get_marks('Матеша')
    print(student1)
    student1.get_journal()

if __name__=="__main__":
    main()"""