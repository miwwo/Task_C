"""Создать производный от Person класс Teacher. Новые поля: номер кабинета, преподаваемые
    предметы (словарь вида класс: список предметов). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения кабинета, добавления и удаления предмета. Переопределить метод преобразования
    в строку для печати основной информации (ФИ, возраст, номер кабинета, предметы)."""

from Person import Person
from log import log

class Teacher(Person):
    def __init__(self, name, surname, age, clas, x):
        Person.__init__(self, name, surname, age)
        self.clas = clas
        self.x = x
        self.subjects = {self.clas: self.x}
        log("CRE",'',"объект класса Teacher", "__init_")


    def ch_clas(self, new_cl):
        print("Старый номер кабинета:", self.clas)
        self.clas = new_cl
        self.subjects = {self.clas: self.x}
        print('Новый номер кабинета:', self.clas)
        log("INF", "change", "номер классс", "ch_clas")

    def add_subj(self, subj):
        self.x.append(subj)
        self.subjects = {self.clas: self.x}
        log("INF", "add", "предмет", "add_subject")

    def del_subj(self, subj):
        self.x.remove(subj)
        self.subjects = {self.clas: self.x}
        log("INF", "delete", "предмет", "del_subject")

    def __str__(self):
        s = "{} {}, age: {}, clas: {}, subjects: {} ".format(self.surname, self.name, self.age, self.clas, self.subjects[self.clas])
        log("INF", "print", "учитель", "__str__")
        return s


"""def main():
    teacher1 = Teacher('Людмила', 'Трысечкина', 45, '216', ['ИЗО'])
    teacher1.ch_clas('305')
    teacher1.add_subj('Матеша')
    teacher1.add_subj('Информатика')
    teacher1.add_subj('Физика')
    teacher1.del_subj('Матеша')
    print(teacher1)



if __name__=="__main__":
    main()"""