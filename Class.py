"""Создать класс Class. Поля: номер rкласса, список класса (список экземпляров класса Student), классный руководитель
    (экземпляр класса Teacher). Определить конструктор. Переопределить метод преобразования в строку для печати
    всей информации о классе (с использованием переопределения в классах Teacher и Student). Переопределить
    методы получения количества учеников функцией len, получения ученика/учителя по индексу, изменения
    по индексу, удаления по индексу (0 индекс - учитель, начиная с 1 - ученики). Переопределить
    операции + и - для добавления или удаления ученика из группы. Добавить функцию создания txt-файла и записи
    всей информации в него (в том числе дневников учеников)."""

from Student import Student
from Teacher import Teacher

class Class(Student, Teacher):
    def __init__(self, n_clas, list_students, clas_teacher):
        self.n_clas = n_clas
        self.list_students = list_students
        self.clas_teacher = clas_teacher
        self.main_clas = []
        self.main_clas.append(self.clas_teacher)
        self.main_clas += self.list_students

    def __len__(self):
        print("Количество студентов:", len(self.list_students))

    def __getitem__(self, index):
        print("Человек по индексу[", index, "]:", self.main_clas[index])

    def __delitem__(self, index):
        self.list_students.pop(index)
        return self.list_students

    def __setitem__(self, index, person):
        self.main_clas[index] = person


    def __sub__(self, student):
        self.list_students.remove(student)
        return self.list_students

    def __add__(self, student):
        self.list_students.append(student)
        return self.list_students

    def __str__(self):
        s = "Class №{}\nClass teacher:{}\nStudents:\n".format(self.n_clas, self.clas_teacher)
        for j in range(1, len(self.main_clas)):
            s = s + str(j) + ' - ' + str(self.main_clas[j]) + '\n'
        return s


    def file(self, address):
        f = open(address, "w")
        f.writelines(f"Class №{self.n_clas}\nClass teacher:{self.clas_teacher}\n\nStudents:\n")
        for j in range(1, len(self.main_clas)):
            x = self.main_clas[j]
            s = str(j) + ' - ' + str(x) + '\n'
            f.writelines(s)
            f.write("Journal:\n")
            if not x.journal:
                f.writelines('Журнал оценок пуст! :С')
            else:
                for i in x.journal:
                    h = x.prr(i, x.journal)
                    f.writelines(h)
            f.writelines("\n\n")
        f.close

student1 = Student('Михаил', "Стручкин", 13, 9)
student1.add_mark('ОБЖ', 5, '12/01')
student2 = Student('Елизавета', "Пупкина", 14, 9)
student2.add_mark('ОБЖ', 3, '12/01')
student3 = Student('Иван', "Иванов", 13, 9)
student4 = Student('Кристина', "Мисина", 14, 9)
student4.add_mark('Матеша', 5, '1/1')
clas_teacher = Teacher('Людмила', 'Трысечкина', 45, '216', ['ИЗО'])
clas_teacher.add_subj('Информатика')
list_students = []
list_students += student1, student2, student3, student4
main_class = Class(7, list_students, clas_teacher)
#main_class.__getitem__(2)
student5 = Student('Мария', "Кирова", 15, 9)
#main_class - student1
#main_class + student5
#main_class.__setitem__(2, student5)
#main_class.__len__()
main_class.file('fifile.txt')
"""try:
    print("Введите индекс ученика, которого хотите удалить:")
    index = int(input())
    x = main_class.amount_of_student()
    if index < 1:
        raise ValueError("Индексы учеников идет от единицы!")
    if index > x:
        raise IndexError(f"Вы ввели индекс, который больше количества учеников, а именно больше: {x}\n")
    main_class.delete_student(index-1)
    print("Ученик по индексу[", index, "] удален!")
    print(main_class)
except ValueError as err:
    print(err, "\nПопробуйте еще раз!")
    index = int(input())
    main_class.delete_student(index-1)
    print("Ученик по индексу[", index, "] удален!")
    print(main_class)
except IndexError as err:
    print(err, "\nПопробуйте еще раз!")
    index = int(input())
    main_class.delete_student(index-1)
    print("Ученик по индексу[", index, "] удален!")
    print(main_class)"""
"""try:
 student6 = Student('Николай', 'Андреев',-5, 9)
 if student6.age<=0:
     raise ValueError("Возраст не может быть отрицательный или быть равен нулю! Попробуйте снова!\n")
 main_class+student6
 print("Ученик был добавлен!")
except ValueError as err:
    print(err,"Введите возраст ученика заново:")
    new_age = int(input())
    student6.age = new_age
    main_class+student6
    print("Ученик был добавлен!")"""
"""try:
    student6 = Student(213153, 'Андреев', 15, 9)
    if not str(student6.name).isalpha():
        raise ValueError('Имя не может состоять не из букв!Попробуйте еще раз!')
    main_class + student6
    print("Ученик был добавлен!")
except ValueError as err:
    print(err, "\nВведите имя ученика заново:")
    new_name = input()
    student6.name = new_name
    main_class + student6
    print("Ученик был добавлен!")
finally:
    print("The End.")
"""